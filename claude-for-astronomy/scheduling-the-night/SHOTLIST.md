# SHOTLIST — Ep. 17, *scheduling-the-night*

*Finish What You Start.* · claude-hai · Pragmatist · Kokoro `af_bella`
**14 beats · 430 words · 2:40 predicted · ships 16:9 (3840×2160) AND 9:16 (2160×3840)**

---

## Lanes

| lane | beats | engine |
|---|---|---|
| ask (Remotion) | B00, B11, B12, B13 | `ClaudeComposerAsk` ×2, `ClaudeVerdictArtifact`, `ClaudeTitleOutro` |
| manim | B01–B10 | `scenes.py`, aspect-aware, one class per beat |

## The colour contract

**Terracotta `#D97757` is THE PLANNER** — the thing being examined.
**Ink `#3D3929` is GREEDY** — the fixed reference it is measured against.

B06 teaches it once, with both dials side by side and labelled *outside* the
plate. It never flips in B08 or B10.

Two local exceptions, each taught inside its own beat because they cannot be
read off the contract:

- **B03** — terracotta marks three *highlighted fields*. No scheduler exists
  yet; the beat is the board before anyone has moved.
- **B09** — the terracotta *curve* is greedy-under-payment, and marker **fill**
  is the price: filled = exposure rate held, hollow = rate given up.

## Beats

| # | act | lane | graphic | plate | the shot |
|---|---|---|---|---|---|
| B00 | COLD OPEN | ask | `ClaudeComposerAsk` | — | types the ask; three result lines land |
| B01 | FRAME | manim | `B01_Presenter` | — | OM MALI; struck row, then a boxed one; Ep. 17 |
| B02 | FRAME | manim | `B02_OneBreath` | — | three card rows; the third underlined in accent |
| B03 | THE BOARD | manim | `B03_TheBoard` | `window.png` | 34 altitude tracks, 3 hot, the 20° floor shaded |
| B04 | THE NUMBER | manim | `B04_TheNumber` | — | 10²⁵⁶⁷ against 10⁸⁰ atoms |
| B05 | RUBIN'S MOVE | manim | `B05_RubinsMove` | — | three basis maps → weighted sum → one ring |
| B06 | ZTF'S MOVE | manim | `B06_ZtfsMove` | `tour.png` | 16-block strip, one lit; two alt-az dials |
| B07 | THE EQUALS SIGN | manim | `B07_TheEqualsSign` | — | both / neither allowed, one STRUCK; the constraint |
| B08 | WHAT IT BOUGHT | manim | `B08_WhatItBought` | `completion.png` | one square per started field; 78 holes vs none |
| B09 | PAY IT TO CARE | manim | `B09_PayItToCare` | `bonus.png` | completion climbs; markers go hollow before the line |
| B10 | THE TELL | manim | `B10_TheTell` | `airmass.png` | two level rate chips; depth gap; the counterweight |
| B11 | VERDICT | ask | `ClaudeVerdictArtifact` | — | "WHEN NOT TO LEARN IT", five rows |
| B12 | HANDOFF | ask | `ClaudeComposerAsk` | — | the viewer's own schedule |
| B13 | OUTRO | ask | `ClaudeTitleOutro` | — | title card |

## Aspect discipline

Portrait is **not a crop**. The vertical band plan is identical (Manim keeps
`frame_height = 8.0` in both); only the horizontal extent changes — x ±6.15
landscape, x ±1.80 portrait. The rule for what goes: **anything the narration
speaks stays**; on-screen-only extras are what portrait loses.

What portrait does differently, per beat:

- **B01** — name/role stack *above* the card instead of beside it.
- **B03 / B09 / B10** — the right-hand legend column becomes a stack beneath
  the plate.
- **B05** — "COVERAGE OWED" shortens to "COVERAGE" so all three cell labels
  render at one size (a label `_fit()` has to scale reads as a mistake beside
  unscaled siblings).
- **B06 / B08** — plate narrows; dial and grid labels move to the per-aspect
  literals `DIAL_X`, `COMP_L_X`, `COMP_R_X`.
- **B07** — the pair chips stack vertically rather than sitting side by side.

## Plate rule

Plates carry **imagery only** — no text, ticks or legend. Every label is
placed by `scenes.py` *outside* the plate, because a plate is an
`ImageMobject` and GATE B is nearly blind to its interior. Two defects in this
episode were found only by reading frames, both invisible to every gate:

1. **B06 landscape** — the plate was drawn *over* the "16 BLOCKS, one filter
   each" sub-label and hid it completely.
2. **B08** — the "401 STARTED" row landed within 0.01 units of the plate's top
   frame and read as contact.

## Numbers on screen

All are named constants at the top of `scenes.py` and all are printed and
**asserted** by `assets/gen_sched.py`, so a changed experiment cannot silently
disagree with a label.

`10^2567` · `10^80` · `EVERY 30 SECONDS` · `16 BLOCKS` · `401 STARTED` ·
`78 STRANDED` · `360 STARTED` · `0 STRANDED` · `90.5 /h` · `90.0 /h` ·
median airmass `1.7` / `1.3` (one decimal — the ILP stops on wall clock, so
the second decimal moves between runs) · `0.975` · ZTF filter changes
`3.6` vs `2.0`.
