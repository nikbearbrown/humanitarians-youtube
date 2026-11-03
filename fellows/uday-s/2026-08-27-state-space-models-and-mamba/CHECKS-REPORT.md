# CHECKS-REPORT — state-space-models-and-mamba

Written before the first slate compiled, per the ai-explainer PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's question answered |
| B01 | BLUF | SHOW | quadratic vs linear cost curves (Manim) |
| B02 | FRAMEWORK | SHOW | three axis cards: STATE / UPDATE / COST (Manim) |
| B03 | WORKED EXAMPLE | SHOW | RNN + Transformer scoring grid (Manim) |
| B04 | MECHANISM | SHOW | SSM equations + fixed-state chain (Manim) |
| B05 | MECHANISM | SHOW | identical A B C per token + citation (Manim) |
| B06 | MECHANISM | SHOW | per-token Δ B C + citation (Manim) |
| B07 | EVIDENCE | SHOW | four sourced claim cards (Manim) |
| B08 | FALSIFIABILITY | SHOW | fixed box vs growing store, side by side (Manim) |
| B09 | VERDICT | SHOW | Mamba scored + use/be-careful (Manim) |
| B10 | YOUR TURN | SHOW | composer, scaffolded prompt + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — STATE / UPDATE / COST shown AS A STRUCTURE at 22.98s,
                   before any architecture is scored.
WORKED EXAMPLE ✓   B03 — the rubric applied live to RNN and Transformer, with
                   the reasoning ("it forgets nothing, and pays every token"),
                   not just the verdict.
FALSIFIABILITY ✓   B08 — and it is PREDICTED by axis 1 rather than bolted on:
                   fixed state ⇒ copying ceiling (Jelassi et al. 2024). The
                   framework earns its keep by forecasting the failure.
SCAFFOLDED TASK ✓  B10 — score an architecture I did not cover, then name a
                   task it should fail and the axis that predicts it. GOOD/BAD
                   answers stated.
BOOKENDS ✓         B00 cold open · B10 "Your turn." · B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Four beats carry visible arXiv citations (B05, B06,
                   B07, B08); every numeric claim sits under one.
```

## Legibility contract

- Every claim beat names its artifact in `shot.show` / `shot.visual_intent`.
- B03 and B08 are comparisons: both sides are on screen together and held for
  the remainder of the beat, never stated once and dropped.
- Un-highlighted elements sit at INK_SOFT (`#6B6559`) on cream — well above the
  ~40% opacity floor; nothing is faded out to make a highlight work.
- No LaTeX: `dvisvgm` is absent, so equations are plain Text/Pango.

## Notes

- **ILLUSTRATE LAW**: the Claude UI appears only in the three bookends.
- **REBUILD LAW**: no figure is lifted from any paper. The curves in B01 are a
  schematic of quadratic-vs-linear shape, carrying no axis numbers, precisely
  because no measured data backs them — shape only, which is what the law
  permits when exact data is not being reproduced.
- GATE L was run before authoring; no reusable component existed for axis
  scoring or state recurrence, so the nine beats are authored Manim, not slates.
