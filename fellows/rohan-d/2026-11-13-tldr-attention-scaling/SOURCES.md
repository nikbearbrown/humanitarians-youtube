# SOURCES — tldr-attention-scaling

- Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin. "Attention Is All You Need." arXiv:1706.03762v7 (2 Aug 2023); NeurIPS 2017. https://arxiv.org/abs/1706.03762 · local `../sources/attention-is-all-you-need.pdf` (text in `../sources/attention.txt`). Read 2026-11-23: §1–6, Tables 1–4, footnote 4. Section used: §3.2.1 and footnote 4.
  - The paper permits reproduction of tables and figures for scholarly and journalistic works with attribution. This film rebuilds, not copies, any figure.
- Computation: `experiment.py`, `naive_fixed_divisor.py`, `bhtf_check.py`, run with numpy under conda env `brutalist` (Python 3.12). Seeds: all 7 (`numpy.random.default_rng(7)`). Outputs: `experiment_output.txt`, `naive_output.txt`, `bhtf_output.txt`.
- Reuse of the toolkit's own scenes: ClaudeTldrWhat, ClaudeTldrWhy, BrutalistHesitantWriter, ClaudeDefinitions, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro (`brutalist.art/`).
- Corrections to the source's framing: none needed; scope narrowed to the paper's own stated assumption (see FACTCHECK #9, #17).
- Credit line for the verdict page: "Idea from Vaswani et al., 2017."
