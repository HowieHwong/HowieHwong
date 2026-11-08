<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.png">
  <img alt="Yue Huang 黄跃 — building human-centered, self-evolving AI systems" src="assets/header-light.png" width="100%">
</picture>

[Website](https://howiehwong.github.io/) &nbsp;·&nbsp; [Scholar](https://scholar.google.com/citations?user=HvzvvqQAAAAJ) &nbsp;·&nbsp; [X](https://x.com/HowieH36226) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/yue-huang-696816265/) &nbsp;·&nbsp; [Email](mailto:yhuang37@nd.edu) &nbsp;·&nbsp; [CV](https://howiehwong.github.io/cv.html)

Hi there 👋

I am a third-year PhD student at the [University of Notre Dame](https://www.nd.edu/), advised by Prof. [Xiangliang Zhang](https://scholar.google.com/citations?user=BhRJe4wAAAAJ&hl=en) in the [MINE Lab](https://mine-lab-nd.github.io/).

Previously at [Microsoft Research](https://www.microsoft.com/en-us/research/), [MIT-IBM Watson AI Lab](https://mitibmwatsonailab.mit.edu/), [IBM Research](https://research.ibm.com/), and [Tsinghua KEG](https://keg.cs.tsinghua.edu.cn/).

## Research

<strong>I build self-improvement <em>humane</em> and <em>humanized</em> intelligence</strong>: foundation models and agentic systems <em>aligned with human values</em>, informed by human <em>cognition</em>, and supported by reliable <em>infrastructure</em>.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lane-alignment-dark.png">
  <img alt="Alignment" src="assets/lane-alignment-light.png" height="38">
</picture>

I study how to align foundation models and agentic systems with human values, from individual behavior to collective dynamics. My work uncovers emergent social intelligence risks that agent-level safeguards alone cannot prevent ([Emergent Social Intelligence Risks](https://arxiv.org/abs/2603.27771) <sup>Nature Machine Intelligence</sup>). I also benchmark trustworthiness ([TrustLLM](https://proceedings.mlr.press/v235/huang24x.html) <sup>ICML'24</sup>, [TrustGen](https://openreview.net/forum?id=Fcf5fLmaeG) <sup>ICLR'26</sup>), train honest and helpful models ([HonestLLM](https://arxiv.org/abs/2406.00380) <sup>NeurIPS'24</sup>), examine biases in LLM-as-a-judge ([Justice or Prejudice?](https://openreview.net/forum?id=3GTtZFiajM) <sup>ICLR'25</sup>), and prioritize safety in alignment ([SPA](https://arxiv.org/abs/2511.06222) <sup>AAAI'26 Oral</sup>, [Capability-Oriented Risk](https://arxiv.org/abs/2602.12124) <sup>ICML'26</sup>).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lane-cognition-dark.png">
  <img alt="Cognition" src="assets/lane-cognition-light.png" height="38">
</picture>

I probe how models reason and perceive, deciding when to use tools ([MetaTool](https://arxiv.org/abs/2310.03128) <sup>ICLR'24</sup>), adapting reasoning style to the task ([AdaReasoner](https://mine-lab-nd.github.io/project/adareasoner.html) <sup>NeurIPS'25 Spotlight</sup>), exposing flaws in social character simulation ([TrustSim](https://openreview.net/forum?id=B5E3ijlLML) <sup>COLM'25</sup>), diagnosing failure modes at scale ([ProbeLLM](https://arxiv.org/abs/2602.12966) <sup>ICML'26</sup>), ranking models by question difficulty ([RankLLM](https://arxiv.org/abs/2602.12424) <sup>ICLR'26</sup>), and probing visual aesthetic judgment ([VAB](https://vab.bakelab.ai/) <sup>COLM'26</sup>). I also explore emotionally-adaptive generative AI ([EmoNest](https://openreview.net/forum?id=cyGU1R569i) <sup>NeurIPS'25 Creative</sup>, [NARRA-Gym](https://arxiv.org/abs/2605.08503) <sup>NeurIPS'26</sup>, [Omelune](https://howiehwong.github.io/omelune/) <sup>Mac app</sup>).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lane-infrastructure-dark.png">
  <img alt="Infrastructure" src="assets/lane-infrastructure-light.png" height="38">
</picture>

I build the toolchain that makes the above possible: frameworks for unified synthetic data ([DataGen](https://openreview.net/forum?id=F5R0lG74Tu) <sup>ICLR'25</sup>, [ChemOrch](https://github.com/HowieHwong/ChemOrch) <sup>NeurIPS'25</sup>), synthetic interaction data for scalable personalization ([PersonaGym](https://arxiv.org/abs/2602.12394) <sup>KDD'26</sup>), foundational guardrails for safer agentic systems ([Safiron](https://openreview.net/forum?id=M47SWYubR5) <sup>ICLR'26</sup>), a new guardian model paradigm ([Guardian-as-an-Advisor](https://arxiv.org/abs/2604.07655) <sup>ACL'26 Findings</sup>), agent infrastructure that turns compute into verifiable improvement and has broken 120 world records in mathematics ([Épi](https://bakeai.inc/research/articles/epi/) <sup>Bake AI</sup>), and infrastructure for recursive self-improvement ([RSI Arena](https://rsiarena.org/) <sup>Live at COLM'26</sup>).

## Blog

- [**RSI Arena: Towards Recursive Self-Improvement with Human Feedback**](https://bakeai.inc/research/blogs/rsi-arena/) · Bake AI
- [**Reward Hacking Challenges Oversight of Autonomous Research Agents**](https://bakeai.inc/research/blogs/reward-hacking/) · Bake AI

## Research Artifacts

Open-source toolkits, benchmarks, and datasets from our work on trustworthy and aligned foundation models.

- [**RiskLab**](https://github.com/HowieHwong/RiskLab) · Toolkit · ACL 2026 Demo: A controlled multi-agent framework for probing emergent social risks in LLM agent collectives, specified as topology–environment–protocol–agent–task quintuples.
- [**ProbeLLM**](https://github.com/HowieHwong/ProbeLLM) · Toolkit · ICML 2026: An automated probing framework that discovers structured LLM failure modes via hierarchical Monte Carlo Tree Search, tool-augmented test generation, and failure-aware clustering.
- [**ValueLence**](https://github.com/HowieHwong/ValueLence) · Dashboard: The first unified platform for dynamic, fine-grained value probing of LLMs — value curation, probe generation, response collection, and multi-dimensional evaluation.
- [**SDE-Harness**](https://github.com/HowieHwong/sde-harness) · Toolkit: Scientific Discovery Evaluation — an extensible framework designed to accelerate AI-powered scientific discovery.
- [**ChemOrch**](https://github.com/HowieHwong/ChemOrch) · Toolkit · NeurIPS 2025: Intelligent task orchestration for chemical research — turns a chemical task into high-quality instruction–response pairs.
- [**TrustEval**](https://github.com/TrustGen/TrustEval-toolkit) · Toolkit · NAACL 2025 Demo: A modular, extensible toolkit for trust evaluation of generative foundation models across safety, fairness, robustness, privacy, and more.
- [**DataGen**](https://github.com/HowieHwong/UniGen) · Toolkit · ICLR 2025: An LLM-powered framework for generating diverse, accurate, and highly controllable text datasets.
- [**TrustLLM**](https://github.com/HowieHwong/TrustLLM) · Toolkit · ICML 2024: A Python package that helps you assess the trustworthiness of your LLM more quickly.
- [**MetaTool**](https://github.com/HowieHwong/MetaTool) · Dataset · ICLR 2024: A benchmark for evaluating whether LLMs have tool-usage awareness and can correctly choose the right tool.
