# SHOTLIST — state-space-models-and-mamba (9:16 SHORT)

## Total: 1:48 (107.63s) · 6 beats + silent endcard · 9:16 · Kokoro am_onyx (male)

A DERIVATIVE CUT of the 3:35 landscape reel, not a re-edit. Six beats were
dropped; the six that remain reuse the parent's measured audio unchanged. Only
the OUTRO narration was regenerated, per the Shorts Law.

Durations are the MEASURED Kokoro audio. Manim run-times were copied verbatim
from the landscape `scenes.py` — geometry changed, timing did not.

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | INTRO | bookend | REMOTION | ClaudeComposerAsk916 | 5.29s | Cold open; SPEAKS THE NAME — "I'm Uday Sonawane" |
| B01 | BLUF | manim | MANIM | `B01_CostCurves` | 17.69s | Quadratic vs linear. Portrait: curve labels move to a legend below the plot |
| B02 | FRAMEWORK | manim | MANIM | `B02_ThreeAxes` | 17.88s | **The framework graphic** — STATE / UPDATE / COST. Portrait: row of 3 becomes one column |
| B06 | MECHANISM | manim | MANIM | `B06_MambaSelection` | 22.10s | Per-token Δ B C; carries arXiv:2312.00752 on screen. Portrait: 5 tokens → 4 |
| B08 | FALSIFIABILITY | manim | MANIM | `B08_CopyingCeiling` | 27.11s | Fixed box vs growing store, both held; carries arXiv:2402.01032. Portrait: stacked |
| B11 | OUTRO | bookend | REMOTION | ClaudeTitleOutro916 | 13.06s | **Rewritten** funnel outro — names what was cut, points at the long |
| END | — | endcard | CARD | silent | 4.50s | Branded endcard, `next:` points at the full explainer |

## What was dropped, and why

| Beat | Act | Why it did not survive the cut |
|---|---|---|
| B03 | WORKED EXAMPLE | Scoring RNN and Transformer is a 3-column grid — the one layout portrait cannot hold at a legible size |
| B04 | MECHANISM | The SSM equations; the short states the fixed-state idea without the control-theory derivation |
| B05 | MECHANISM | S4's fixed matrices. B06 needs "they used to be fixed" as one narrated clause, not its own beat |
| B07 | EVIDENCE | The paper's four headline numbers. Cut with regret — but numbers without the surrounding argument are the thing PROOF warns against |
| B09 | VERDICT | The scorecard is a payoff for having watched all three mechanism beats |
| B10 | YOUR TURN | The scaffolded task needs the full rubric in view to be actionable |

Kept: the framework and the case that breaks it. That is the teaching spine.

## Lane histogram

```
MANIM     4 beats   84.78s  (78.8%)   BLUF / FRAMEWORK / MECHANISM / FALSIFIABILITY
REMOTION  2 beats   18.35s  (17.0%)   bookends only, both rewired to 916 compositions
CARD      1 beat     4.50s  ( 4.2%)   silent endcard
PANTRY    0 beats    0.00s  ( 0.0%)   no human-supplied media needed
```

## No source, no verdict

Two of the four body beats carry a visible arXiv citation at the moment of the
claim, unchanged from the parent: B06 (Gu & Dao 2023, arXiv:2312.00752) and B08
(Jelassi et al. 2024, arXiv:2402.01032). The citation strip is reserved by
`fit_src()` so the body never lands on it — GATE B reads that as
label-on-a-line, which is how the parent reel earned the same guard.

The 5× throughput claim is NOT in this cut: it lived in B07, which was dropped.
No number appears in the short that is not sourced on screen.

## Portrait notes (GATE B)

The 9:16 frame is 4.5 × 8 (x ±2.25, y ±4.0) — a third of the landscape width.
B06 drops its token run from five to four rather than scaling five 1.75-wide
parameter boxes below legibility; four still carries the claim (per-token
parameters, one propagated, one forgotten).

B08's side-by-side is preserved in substance: the fixed state box and the
growing store are on screen TOGETHER and held to the end of the beat, which is
what the PROOF production gate asks for. Only the axis changed.
