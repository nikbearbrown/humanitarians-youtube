# SOURCES: Attention, One Head at a Time

## The source this film is cut from
- **`SOURCE.md`** (this folder) is our own written explainer of scaled dot-product attention, written 2026-11-22 because `tldr` expects written source material. Every claim in it was checked against the paper below. It is cut into one learning section in `tldr-sections-attention.md` (GATE S, pending). Per the BOOKLOOP law, the film does not name it on screen or in narration.

## References
- A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, I. Polosukhin. "Attention Is All You Need." *Advances in Neural Information Processing Systems 30* (NIPS 2017), Long Beach. arXiv:1706.03762.
  - §3.1: d_model = 512.
  - §3.2.1: Eq. (1), the √d_k rationale and its variance footnote, and dot-product vs additive attention.
  - §3.2.2: multi-head attention, h = 8, d_k = d_v = 64, W^O.
  - §3.5: sinusoidal positional encodings added to the input embeddings.
  - Read 2026-11-22 via the arXiv abstract page and the ar5iv HTML rendering. Every item above was confirmed TRUE.
- Pedagogy: `skills/make/tldr/reference/pedagogy.md` (3Blue1Brown template, as gates).

## Executable evidence
- `demo/attention_demo.py` (pure numpy, seed 290537) writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
  - Environment: Python 3.12.13, numpy 2.5.5, Windows 11.
  - Hashes: script `7f79b621…`, evidence `b48f90c9…` (full hashes in RUN-LOG.txt).
- `make_sheet.py` reads every on-screen number from `evidence.json`. It asserts every spoken number against the same file.
- **Seed choice.** 290537 came from a scratch search over default_rng seeds 0–299,999 for legibility. The criteria are listed in the demo's docstring and re-asserted when it runs: small integer Q/K/V, a non-trivial heat map, value points in convex position, and no near-ties.
- **The "kids" embedding** [1 1 1 0] was hand-picked from {−1, 0, 1}⁴ so that its value point is distinct from the other four. It is documented in the demo.

## Corrections applied (DOUBLE-CHECK law)
Details are in FACTCHECK #2, #3, #5, #10 and #31.
- **B00:** "weighted average of all the words" became "of what all the words carry". The average is over values.
- **B00 and B02:** "never picks" became "blends rather than picks" / "doesn't pick". Weights can approach one-hot.
- **B01:** "in every layer" became "layer after layer". Hybrid architectures exist.
- **B10:** "Nothing from outside the sentence went in" became "The head only sees these four words". The learned weights come from outside the sentence.
- **B19:** "Transformers fix this by adding a position signal" became "The original transformer fixes this…". Later models often use rotary or relative schemes.

## Seeds
- Embeddings and toy projections: numpy `default_rng(290537)`.
- Variance check: `default_rng(0)`, 100,000 pairs at d = 64.
- Hesitant writer: `seed: "tldr-attention"`.
- Outro mascot and polarity: seeded by slug `tldr-attention`.
