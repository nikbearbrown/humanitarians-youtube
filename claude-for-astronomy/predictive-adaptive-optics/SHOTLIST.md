# SHOTLIST — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · 14 beats · 428 words

Lane key: **R** = Remotion (the Claude UI), **M** = reel-local Manim scene
(`scenes.py`), **P** = Manim scene carrying a plate from `assets/gen_ao.py`.

| # | Beat | Lane | What the viewer watches | Portrait drops |
|---|---|---|---|---|
| B00 | COLD OPEN | R | `ClaudeComposerAsk` — the ask types, send arms, three result lines land | — (916 composition) |
| B01 | FRAME | M | name writes in, struck row / boxed row, series line | the two-column split becomes a stack |
| B02 | FRAME (BLUF) | M | card draws, three lines type, the third is accented and underlined | nothing |
| B03 | THE DISTANCE | **P** `slide.png` | two wavefront cuts, offset; then r₀ and the 1.7 cm slide as rules | the `1 kHz · 1.7 ms` chip and its PUBLISHED note |
| B04 | THE LAW | **P** `lawlog.png` | the lag curve, the coherence-time crosshair, the 16% connector | the exponent chip and the 1 rad² note |
| B05 | THE FILTER | M | 24 ticks, a weight fan, an arrow jumping 2 ms into an empty slot | nothing |
| B06 | BACK OR ACROSS | **P** `decomp.png` | six bars in two groups; across / back / both named with values | two method notes |
| B07 | THE CEILING | **P** `noise.png` | two curves falling as the sensor gets noisier, dots on the realistic rule | the quiet-sensor chip |
| B08 | THE BUDGET | **P** `budget.png` | two stacked budgets; the terracotta slice collapses, the bar barely shortens | the PUBLISHED note |
| B09 | ON SKY | M | two dated cards fill, the shared fact lands below both | the shared-fact line keeps, nothing else to drop |
| B10 | THE TELL | M | the expectation is struck; two cards of paired counters | the pairs stack instead of sitting side by side |
| B11 | VERDICT | R | `ClaudeVerdictArtifact` — five lines reveal | — (916 composition) |
| B12 | HANDOFF | R | `ClaudeComposerAsk` — the suggested prompt types, three grading lines | — (916 composition) |
| B13 | OUTRO | R | `ClaudeTitleOutro` — title restate, handle, subline | — (916 composition) |

## Aspect discipline

The reel ships 16:9 (3840×2160) and 9:16 (2160×3840). **Portrait is not a
crop.** Manim keeps `frame_height = 8.0` in both, so the vertical band plan is
identical; only x changes (±6.15 → ±1.80).

**The reduction rule: anything the narration SPEAKS stays on screen.** What
portrait loses is on-screen-only extras — chips, provenance notes, secondary
method lines. Every number the voice says is present in both cuts.

Six scenes turn a landscape right-hand column into stacked rows in portrait
(B03, B04, B06, B07, B08, and B10's counter pairs). Those branches play fewer
reveals, which is what `RT_PORTRAIT` exists to absorb.

## The colour contract

Terracotta `#D97757` marks **the subject of each beat**; ink marks the
**fixed reference** it is measured against.

- B03 — the wavefront the mirror *holds* · against the one that is really there
- B04 — the *whole* lag error · against the part inside the correctable band
- B06 — prediction from the *past* · against spatial and combined
- B07 — *one* layer · against three
- B08 — the *servo-lag* slice · against everything untouchable

The mapping never flips, so B03 teaches it once.

## What is never shown

No image being repaired. `ideas.md`'s Notes fence Ep. 16 off from Ep. 09
(`denoising-deep-space`): this episode is about **real-time instrument
control**, and every correction in it happens before the photons reach the
detector. B02 says so in its closing line — *before the light is recorded*.
