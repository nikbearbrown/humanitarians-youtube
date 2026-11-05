# SOURCES.md — a-comma-changed-the-answer

Retrieved 2026-10-30.

**A.** Singh, A. K. & Strouse, D. J. (2024). *Tokenization counts: the impact of
tokenization on arithmetic in frontier LLMs.* arXiv:2402.14903 (v1, 22 Feb 2024).
https://arxiv.org/abs/2402.14903 · https://arxiv.org/html/2402.14903v1

**B.** Physics engine repo, commit `2dc4aa4`:
https://github.com/jashshah127/humanitariansai/tree/2dc4aa408e02a78fd595e35cee8012017a9972e6/physics-engine

| Beat | Claim | Source |
|---|---|---|
| B00, B03 | GPT-3.5 addition accuracy 75.6% (default) → 97.8% (comma-separated), 8-shot | A §3.1: "from 68.5% 1-shot to 75.6% 8-shot" (L2R); "from 95.6% 1-shot to 97.8% 8-shot" (R2L) |
| B03 | 7–9 digit addends; model gpt-3.5-turbo-0301 (Figure 1: "March 2023 models") | A §2.1, §3.1, Fig. 1 caption |
| B03 | authors at UCL (Gatsby Unit) and Google DeepMind | A, author affiliations |
| B02 | tokenizer has a token for every 1-, 2-, 3-digit string; chunks long numbers into 3 digits, left to right | A abstract; intro; Fig. 3 caption ("chunks of 3 digits, left-to-right") |
| B02 | 8302080 → 830 · 208 · 0 | Derived from the left-to-right 3-digit rule in A; A itself uses 8302080 as its separator example (§3.2) |
| B04 | randomness off: greedy decoding, temperature 0 | A §2.1: "We use greedy decoding (temperature=0) in all experiments." |
| B04 | the gap shrinks with model scale | A abstract |
| B05 | the LLM never does arithmetic; SymPy solves | B `docs/Physics_Engine_Brief_v2.md` |
| B05 | SymPy has no randomness; one problem ×10, identical output | B `engine/README.md` V2 section; `EVALUATION.md` claim 2 |
| B05 | example knowns m₁=4 kg, m₂=6 kg → a = 1.96 m/s² | B `golden_set/golden_set_16.csv`, MECH-003. Hand check: (6−4)/10 × 9.8 = 1.96 ✓ |
| B06 | grading fairness: same problem, same reference | B `EVALUATION.md` claim 2 |
| B06 | hint before `T − 39.2 = 4a`, after `T − g·m₁ = a·m₁` | B `MEASUREMENT.md` "Tutor hints got materially better" |

## Checked and NOT used

GPT-4 figures (84.4% → 98.9%) appeared in a search summary but could not be found
in the paper's text; 98.9% in the paper is a formatting-adherence figure, not
accuracy. Dropped.

## Expiring figures

The 75.6/97.8 figures describe a March 2023 model. They are props on B03 with the
model date on screen; B07 says the percentages change and the rule doesn't.
