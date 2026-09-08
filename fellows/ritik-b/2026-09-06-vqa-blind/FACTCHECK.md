# FACTCHECK — "Visual Question Answering, Blind?"

Verified 2026-09-06. Every number that appears ON SCREEN is listed here with the
primary source it came from and the beat that shows it. Nothing in the reel is
asserted from memory, and every published figure is rendered in the same frame as
its citation (`VqaStage`'s `source` slot / `ClaudeVerdictArtifact.sourceNote`).

Two figures in the reel are **illustrative, not measured** — they show the shape of a
mechanism, not a result. Both are labelled as such on screen. They are listed at the
bottom so the distinction is auditable.

## Primary sources

| Key | Source |
|---|---|
| ANTOL | Antol, Agrawal, Lu, Mitchell, Batra, Zitnick, Parikh. "VQA: Visual Question Answering." ICCV 2015. arXiv:1505.00468 |
| GOYAL | Goyal, Khot, Summers-Stay, Batra, Parikh. "Making the V in VQA Matter: Elevating the Role of Image Understanding in Visual Question Answering." CVPR 2017. arXiv:1612.00837 |
| VIT | Dosovitskiy et al. "An Image is Worth 16x16 Words." ICLR 2021. arXiv:2010.11929 |
| VILT | Kim, Son, Kim. "ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision." ICML 2021. arXiv:2102.03334 |
| LXMERT | Tan & Bansal. "LXMERT: Learning Cross-Modality Encoder Representations from Transformers." EMNLP 2019. arXiv:1908.07490 |

## Claims shown on screen

| Beat | Claim as shown | Verdict | Source |
|---|---|---|---|
| B00, B06 | Question-only ("blind") model: **48.76** overall, open-ended, real images | VERIFIED | ANTOL, Table 2 ("LSTM Q") |
| B00, B06 | Question + image: **57.75** | VERIFIED | ANTOL, Table 2 ("deeper LSTM Q + norm I") |
| B06 | Prior "yes": **29.66** | VERIFIED | ANTOL, Table 2 |
| B06 | Human, question + image: **83.30** | VERIFIED | ANTOL (reported human accuracy, real images, Q+I) |
| B06 | Blind model on yes/no questions: **78.20** | VERIFIED | ANTOL, Table 2, yes/no column for LSTM Q |
| B06 | Bracket label **+8.99 points** | DERIVED | 57.75 − 48.76 = 8.99. Arithmetic on two verified figures, shown alongside both |
| B07 | Language-only baseline **48.21 → 43.01** (unbalanced v1 → balanced v2) | VERIFIED | GOYAL |
| B07 | MCB **60.36 → 54.22** | VERIFIED | GOYAL (best model tested; UU → UB) |
| B07 | HieCoAtt **57.09 → 50.31** | VERIFIED | GOYAL |
| B07 | Complementary images: workers shown **24 nearest neighbours**, pick one where the answer differs; **not possible for 22%** of questions | VERIFIED | GOYAL (collection procedure) |
| B03 | 224 × 224 px, 16 × 16 patches, 14 × 14 = **196 patch tokens** | DERIVED + VERIFIED | Patch-token construction from VIT; 224/16 = 14, 14² = 196 is arithmetic shown on screen |
| B04 | single-stream = concatenate then self-attend (**ViLT**) | VERIFIED | VILT |
| B04 | two-stream = two towers plus cross-attention (**LXMERT**) | VERIFIED | LXMERT |
| B05 | standard VQA is scored as classification over a fixed answer vocabulary | VERIFIED | ANTOL / GOYAL evaluation protocol — accuracy against a closed answer set, not free generation |

## De-sensitised / deliberately NOT claimed

- **No model-version or SOTA claim.** The reel never says "models today still do this."
  It says the ORIGINAL benchmark was broken and balancing was the fix, both of which are
  historical facts with papers attached. This is what keeps the video from dating.
- **No size for the answer vocabulary.** The widely-used 3,129-answer vocabulary comes
  from later work, not from ANTOL or GOYAL, so B05 says "the most frequent training
  answers" and shows no count.
- **"the best model of the day"** (B07 narration) is scoped to *tested in GOYAL*, which is
  what the on-screen row label says ("MCB — best model tested").
- **No claim that blind ≈ sighted on VQA v2.** The blind/sighted gap is quoted only for
  VQA v1, which is where those two figures come from.

## Illustrative, labelled on screen as such

| Beat | What is illustrative | On-screen label |
|---|---|---|
| B04 | The attention field over the 14 × 14 grid — a deterministic Gaussian around the umbrella, sharpened as the softmax step lands | "Illustrative attention field — the shape of the read, not measured weights." |
| B05 | The answer distribution (red 0.71, black 0.11, blue 0.07, yellow 0.06, white 0.05) | "Illustrative distribution — the mechanism, not a measured model output." |
| B03/B04/B07 | The street scene itself — drawn in SVG per REBUILD LAW, never a lifted photograph | B07: "Scenes redrawn (illustrative) — the procedure, not the paper's photographs." |
