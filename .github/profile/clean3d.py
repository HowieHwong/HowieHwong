#!/usr/bin/env python3
"""Keep only the 3D calendar from github-profile-3d-contrib's image: drop the radar, the pie
and the star/fork counts, crop to the calendar, and write the yearly total in the empty corner.
Usage: clean3d.py in.svg out.svg"""
import re, sys
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
root = ET.parse(sys.argv[1]).getroot()
kids = list(root)
assert [k.tag.split('}')[1] for k in kids] == ['style', 'rect', 'g', 'g', 'g', 'g'], 'layout changed'
total = next(t.text for t in kids[5].iter(f'{{{NS}}}text') if re.fullmatch(r'[\d,]+', t.text or ''))
total = int(total.replace(',', ''))
for k in kids[3:]:
    root.remove(k)
x, y, w, h = 10, 120, 1216, 716
root.set('viewBox', f'{x} {y} {w} {h}')
root.set('width', str(w))
root.set('height', str(h))
root.remove(kids[1])
label = ET.SubElement(root, f'{{{NS}}}g')
big = ET.SubElement(label, f'{{{NS}}}text', {'x': '40', 'y': '752', 'class': 'fill-strong', 'style': 'font-size:44px;font-weight:600'})
big.text = f'{total:,}'
small = ET.SubElement(label, f'{{{NS}}}text', {'x': '40', 'y': '786', 'class': 'fill-weak', 'style': 'font-size:24px'})
small.text = 'contributions in the last year'
open(sys.argv[2], 'w', encoding='utf-8').write(ET.tostring(root, encoding='unicode'))
