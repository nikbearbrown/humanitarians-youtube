# SHOTLIST — weekly-fixtures-before-validators (9:16 SHORT)

## Total: 1:27 (87.33s) · 6 beats + silent endcard · 9:16 · Kokoro am_onyx (male)

A DERIVATIVE CUT of the 3:02 landscape reel, not a re-edit. Seven beats were
dropped; the six that remain reuse the parent's measured audio unchanged. Only
the OUTRO narration was regenerated, per the Shorts Law.

Durations are the MEASURED Kokoro audio. Manim run-times were copied verbatim
from the landscape `scenes.py` — geometry changed, timing did not.

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | INTRO | bookend | REMOTION | ClaudeComposerAsk916 | 7.98s | Cold open; SPEAKS THE NAME — "I'm Uday Sonawane" |
| B01 | PROBLEM | manim | MANIM | `B01_TodoSteps` | 11.07s | Six hollow status boxes; empty six-cell ledger. Portrait: TODO tag becomes a trailing column |
| B02 | FRAMEWORK | manim | MANIM | `B02_Method` | 18.15s | **The framework graphic** — 4 method cards. Portrait: 2×2 grid becomes one column |
| B05 | OUTPUT | manim | MANIM | `B05_DefectCatalogue` | 18.05s | 18 chips into 7 class rows. Portrait: class label sits ABOVE its chips |
| B09 | FALSIFIABILITY | manim | MANIM | `B09_WrongEntity` | 17.77s | Checks and verdict both on screen, held. Portrait: stacked, not side by side |
| B12 | OUTRO | bookend | REMOTION | ClaudeTitleOutro916 | 9.81s | **Rewritten** funnel outro — names what was cut, points at the long |
| END | — | endcard | CARD | silent | 4.50s | Branded endcard, `next:` points at the full report |

## What was dropped, and why

| Beat | Act | Why it did not survive the cut |
|---|---|---|
| B03, B06 | CLI | The ask beats are scaffolding around the cycles; without the cycles they carry nothing |
| B04, B07 | CODE | Verbatim source in monospace is unreadable at phone size. This is the honest reason — a center-cut or a shrink would have shipped text nobody can read |
| B08 | OUTPUT | Second output beat; B05 already proves the method produced something |
| B10 | SUMMARY | A week's ledger is a long-form payoff, not a Short's |
| B11 | NEXT STEPS | The scaffolded task needs the full method in view to be actionable |

Kept: the framework and the case that breaks it. That is the teaching spine.

## Lane histogram

```
MANIM     4 beats   65.04s  (74.5%)   PROBLEM / FRAMEWORK / OUTPUT / FALSIFIABILITY
REMOTION  2 beats   17.79s  (20.4%)   bookends only, both rewired to 916 compositions
CARD      1 beat     4.50s  ( 5.2%)   silent endcard
PANTRY    0 beats    0.00s  ( 0.0%)   no human-supplied media needed
```

## Portrait notes (GATE B)

The 9:16 frame is 4.5 × 8 (x ±2.25, y ±4.0) — a third of the landscape width.
Nothing that was a row survives as a row. Every body group is routed through
`fit()` into a declared BODY_TOP..BODY_BOTTOM band rather than trusting
hand-placed coordinates, same guard as the parent reel.

B09's side-by-side is preserved in substance: the four passing checks and the
failing verdict are on screen TOGETHER and held to the end of the beat, which
is what the PROOF production gate asks for. Only the axis changed.
