#!/usr/bin/env python3
"""One small image per well-known public repo where the user recently had a pull request merged, one per
Packing Center page that credits the user, plus the README lines that show and link them. Uses the workflow's token, which can only see public data.
Usage: cards.py out_dir README.md"""
import base64, datetime as dt, html, json, os, re, sys, textwrap, urllib.request

USER = os.environ['USERNAME']
TOKEN = os.environ['GITHUB_TOKEN']
REPO = os.environ['GITHUB_REPOSITORY']
OUT, README = sys.argv[1:3]
MIN_STARS = 50
MAX_CARDS = 4
WINDOW_DAYS = 365
OWN_ORGS = {USER, 'TrustGen', 'BakeLab', 'MINE-Lab-ND', 'mit-calc', 'kdd26-relscifm', 'OpenRSI-Foundation', 'Levain-Arena', 'Enterprise-Agent'}
# Records credited by name on a page of Erich's Packing Center (no pull request behind them).
PACKING_CENTER = 'https://erich-friedman.github.io/packing/'
PACKING_PAGES = ['penintri']
CREDIT_NAME = 'Yue Huang'
START, END = '<!-- recent-contributions:start -->', '<!-- recent-contributions:end -->'
FONT = '-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif'


def graphql(query, **variables):
    req = urllib.request.Request('https://api.github.com/graphql',
                                 json.dumps({'query': query, 'variables': variables}).encode(),
                                 {'Authorization': f'bearer {TOKEN}', 'Content-Type': 'application/json'})
    answer = json.load(urllib.request.urlopen(req))
    if answer.get('errors'):
        sys.exit(json.dumps(answer['errors']))
    return answer['data']


def merged_prs():
    since = (dt.date.today() - dt.timedelta(days=WINDOW_DAYS)).isoformat()
    q = f'author:{USER} is:pr is:merged is:public -user:{USER} merged:>={since} sort:created-desc'
    data = graphql('''query($q:String!){search(query:$q,type:ISSUE,first:100){nodes{... on PullRequest{
        title url mergedAt repository{nameWithOwner url stargazerCount isPrivate owner{login avatarUrl(size:112)}}}}}}''', q=q)
    return data['search']['nodes']


def short(n):
    return f'{n / 1000:.1f}k' if n >= 1000 else str(n)


def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.headers.get_content_type(), r.read()


def draw(title, lines, foot, kind, image, label):
    y = 44
    body = ''
    for line in lines:
        body += f'<text class="p" x="68" y="{y}">{html.escape(line)}</text>'
        y += 19
    height = 98  # the same for every card, so a row of them lines up
    picture = base64.b64encode(image).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 410 {height}" width="410" height="{height}" role="img" aria-label="{html.escape(label, quote=True)}">
<defs><clipPath id="c"><rect x="0" y="6" width="54" height="54" rx="11"/></clipPath></defs>
<style>
  text{{font-family:{FONT}}}
  .o{{font-size:15px;fill:#57606A}}.r{{font-size:15px;font-weight:600;fill:#1F3A7A}}.s{{font-size:13px;fill:#57606A}}
  .p{{font-size:13.5px;fill:#24292F}}.d{{font-size:12px;fill:#6E7781}}
  .all{{animation:up .7s ease-out both}}
  @keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
  @media (prefers-color-scheme:dark){{.o,.s{{fill:#8B949E}}.r{{fill:#A9BCF0}}.p{{fill:#E6EDF3}}.d{{fill:#7D8590}}}}
  @media (prefers-reduced-motion:reduce){{.all{{animation:none}}}}
</style>
<g class="all">
<rect x="0" y="6" width="54" height="54" rx="11" fill="#FFFFFF"/>
<image x="0" y="6" width="54" height="54" clip-path="url(#c)" href="data:{kind};base64,{picture}"/>
<text x="68" y="20">{title}</text>
{body}<text class="d" x="68" y="{y}">{html.escape(foot)}</text>
</g>
</svg>
'''


def repo_card(pr):
    repo = pr['repository']
    owner, name = repo['nameWithOwner'].split('/')
    kind, avatar = fetch(repo['owner']['avatarUrl'])
    merged = dt.datetime.fromisoformat(pr['mergedAt'].replace('Z', '+00:00')).strftime('%b %Y')
    title = (f'<tspan class="o">{html.escape(owner)}/</tspan><tspan class="r">{html.escape(name)}</tspan>'
             f'<tspan class="s" dx="8">★ {short(repo["stargazerCount"])}</tspan>')
    return draw(title, textwrap.wrap(pr['title'], 54)[:2], f'Merged {merged}', kind, avatar,
                f'{repo["nameWithOwner"]}: {pr["title"]}')


def packing_credits(text):
    """The numbers credited to the user on one page, and the latest month named.
    A table row holds the images N.png; the next row holds one value cell per image, in the same order."""
    numbers, months = [], []
    rows = re.split(r'(?i)<tr\b[^>]*>', text)
    for row, values in zip(rows, rows[1:]):
        images = re.findall(r'(?i)src="?(\d+)\.png', row)
        cells = re.split(r'(?i)<td align=center>', values)[1:]
        for n, cell in zip(images, cells):
            cell = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', cell))
            if CREDIT_NAME in cell:
                numbers.append(int(n))
                month = re.search(rf'{CREDIT_NAME} in ([A-Z][a-z]+ \d{{4}})', cell)
                if month:
                    months.append(dt.datetime.strptime(month.group(1), '%B %Y'))
    return numbers, max(months) if months else None


def packing_cards():
    """(slug, url, label, svg) for each page where the user is still credited."""
    cards = []
    for page in PACKING_PAGES:
        url = f'{PACKING_CENTER}{page}/'
        text = fetch(url)[1].decode('latin-1')
        numbers, month = packing_credits(text)
        if not numbers:
            continue
        name = re.search(r'(?is)<title>(.*?)</title>', text).group(1).strip()
        kind, figure = fetch(f'{url}{numbers[-1]}.png')
        line = f'{name}: n = {", ".join(map(str, numbers))}'
        title = f'<tspan class="r">Erich&#x27;s Packing Center</tspan>'
        foot = f'Found {month.strftime("%b %Y")}' if month else ''
        cards.append((f'packing-{page}', url, f"Erich's Packing Center: {line}",
                      draw(title, [line], foot, kind, figure, f"Erich's Packing Center. {line}")))
    return cards


def main():
    seen, chosen = set(), []
    for pr in merged_prs():
        repo = pr['repository']
        if repo['isPrivate'] or repo['owner']['login'] in OWN_ORGS or repo['stargazerCount'] < MIN_STARS:
            continue
        if repo['nameWithOwner'] not in seen:
            seen.add(repo['nameWithOwner'])
            chosen.append(pr)
    chosen.sort(key=lambda p: -p['repository']['stargazerCount'])
    chosen = chosen[:MAX_CARDS]
    os.makedirs(f'{OUT}/cards', exist_ok=True)
    rows = []

    def add(slug, url, label, svg):
        open(f'{OUT}/cards/{slug}.svg', 'w', encoding='utf-8').write(svg)
        rows.append(f'<a href="{url}"><img alt="{html.escape(label, quote=True)}" '
                    f'src="https://raw.githubusercontent.com/{REPO}/output/cards/{slug}.svg" width="385"></a>')
        print(slug, label)

    for pr in chosen:
        name = pr['repository']['nameWithOwner']
        add(name.replace('/', '__'), pr['url'], name, repo_card(pr))
    for card in packing_cards():
        add(*card)
    text = open(README, encoding='utf-8').read()
    block = START + '\n' + '\n'.join(rows) + '\n' + END
    new = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: block, text, flags=re.S)
    assert START in text
    open(README, 'w', encoding='utf-8').write(new)


if __name__ == '__main__':
    main()
