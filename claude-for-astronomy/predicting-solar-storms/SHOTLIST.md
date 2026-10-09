# SHOTLIST — *The Same Sunspot, Twice.*

Ep. 12 · `predicting-solar-storms` · 14 beats · 400 words
Channel `claude-hai`, Pragmatist register, Kokoro `af_bella`, $0.00.

**ILLUSTRATE LAW.** The Claude UI appears at **B00, B11, B12, B13 only**.
All ten inner beats illustrate their own concept as reel-local Manim
(`scenes.py`). No composer wallpaper.

**Aspect.** One `scenes.py` lays out both cuts. `frame_height = 8.0` either
way, so the vertical band plan is identical and only the horizontal extent
changes — x ±6.15 landscape, ±1.80 portrait. Portrait is **not a crop**: it
carries fewer elements, larger. The rule — *anything the narration speaks
stays on screen; the on-screen-only extras are what portrait loses.*

---

## Plates

All seven come from `assets/gen_solar.py`. Plates carry **imagery only** —
every label, counter and citation is vector type in `scenes.py`.

| Plate | px | ratio | What it is |
|---|---|---|---|
| `regions.png` | 1560×740 | 0.474 | Ten regions as tracks of hourly dots; flare rows in terracotta |
| `split.png` | 1550×700 | 0.452 | The same tracks under a random row split ‖ a by-region split |
| `split_v.png` | 760×830 | 1.092 | The same pair, stacked, for portrait |
| `nearest.png` | 1560×700 | 0.449 | Distance to the nearest training row, both splits overlaid |
| `scores.png` | 1560×780 | 0.500 | Four bars: two models × two splits |
| `spread.png` | 1560×780 | 0.500 | The same four, twelve runs each, medians and ranges |
| `control.png` | 1560×780 | 0.500 | Inflation against region-fingerprint strength |

**Plate geometry.** `ph = pw × (ih/iw)`. The landscape figure band is 4.30
units. The 0.50-ratio plates run at pw 6.6 (→ 3.30 tall). `regions` runs at
7.00 and `split` at 7.40 — **both were caught too tall on the first pass**,
`split` at 4.79 units with a label landing at y 3.54, above the title.
`split_v` is 1.09, so in portrait at pw 3.10 it is 3.39 tall and needs most
of the figure band.

---

## Beats

| # | Act | Lane | Scene | The shot |
|---|---|---|---|---|
| B00 | COLD OPEN | ask | `ClaudeComposerAsk` | Composer types the ask; `splitting 20,228 rows from 350 regions…`; three result lines — every region in both sets / the flexible model "wins" / it drops 75% |
| B01 | FRAME | manim | `B01_Presenter` | OM MALI writes in; row one STRUCK (eleven episodes / does the AI work?), row two boxed (this one / how we checked); series line |
| B02 | FRAME | manim | `B02_OneBreath` | Three kinetic lines: ONE REGION, MEASURED FOR DAYS → SHUFFLE, THEN SPLIT → **YOU TESTED ITS MEMORY**, the third accented and underlined |
| B03 | THE STAKES | manim | `B03_Stakes` | 49 ink squares draw as an isotype count; date card 3 Feb 2022; **38 turn terracotta and fall away**; counter 38 of 49 |
| B04 | THE MECHANISM | manim | `B04_TheData` | `regions.png`; the top track ringed and named; chips — 58 rows, 1 flare row in 58 |
| B05 | THE MECHANISM | manim | `B05_TheSplit` | `split.png` / `split_v.png`; terracotta test rows scatter through every track, then whole tracks go terracotta; counters **100%** and **0%** |
| B06 | THE MECHANISM | manim | `B06_TheLeak` | `nearest.png`; the two piles named; 0.13 against 0.38 |
| B07 | THE RESULT | manim | `B07_TheHeadline` | Bars drawn **natively**, growing on the spoken figure: ink to 0.36, terracotta past it to 0.48, bracket +0.13, chip "rows shuffled" |
| B08 | THE RESULT | manim | `B08_TheReversal` | `scores.png`, all four bars; the by-region pair ringed; **−75%** counter; the plain model's 0.36 → 0.37 noted |
| B09 | THE RESULT | manim | `B09_NotOneRun` | `spread.png`; twelve points per column; the two terracotta columns far apart, no overlap |
| B10 | THE TELL | manim | `B10_TheTell` | `control.png`; the curve followed to zero; a card types **split by region, not by row** |
| B11 | VERDICT | ask | `ClaudeVerdictArtifact` | Five artefact lines, the fifth accented. Five, not four — a four-line card sits on GATE V's bbox-fill floor (Ep. 10) |
| B12 | HANDOFF | ask | `ClaudeComposerAsk` | `Your turn.`; the prompt types itself; three grading lines |
| B13 | OUTRO | ask | `ClaudeTitleOutro` | Title restate, terracotta period, rule, handle, subline |

**B07 is drawn natively rather than from `scores.png`** so the two bars grow
*on* the spoken figures, and so B08 can then show the same bars in context
with the second pair collapsing. Two consecutive plate beats of the same
chart would have been a slideshow; this is an escalation.

---

## Colour contract

Terracotta `#D97757` is the ONE accent and marks **the leak and what it
buys** — the test rows scattered through every region, the pile of near-zero
neighbour distances, the flexible model's inflated bar and its collapse, the
inflation curve. Ink marks **what survives an honest test** — the plain
model, which does not move between splits.

The load-bearing moment is B08: the ink bar lands at the height it had
before and the terracotta one falls by three quarters. The accent that has
meant "the flexible model's advantage" for three beats is the thing that
evaporates.

Accented text is `#A44A32` (4.7:1 on cream). `#B9B4A0` is strokes and fills
only — never text.

---

## Band plan (both aspects)

| | landscape | portrait |
|---|---|---|
| title | +3.02 | +3.14 |
| hairline | +2.66 | +2.84 |
| figure | +2.40 … −1.90 | +2.62 … −2.02 |
| closing line | −2.50 | −2.42 |
| citation | −3.20 | −2.95 |
| wordmark bug | −3.12 | −3.28 (right-anchored, LOGO LAW) |

---

## Portrait reductions

Dropped at 9:16, all on-screen-only, none of it spoken:

- **B03** — the "published ledger" chip. It sat under the date card and its
  stroke read as a curve beneath the type; the citation line names the
  sources anyway.
- **B06** — the 0.13 / 0.38 side column. The two piles stay named, and the
  voice carries the comparison.
- **B08** — the "the plain model does not move: 0.36 → 0.37" line.
- **B09** — the two-row side column.
- **B10** — the fix card's frame and its "the fix, in one line" header; the
  two accented lines themselves stay, because the voice reads them.

Nothing the narration speaks is dropped in either aspect.

---

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01); a card typing itself line by line (B02); an isotype count
where 38 of 49 marks change colour and fall (B03); a ring travelling to one
track while a counter runs its rows (B04); the same tracks re-coloured two
different ways (B05); bars growing to value on the spoken figure (B07); a bar
that collapses while a counter runs backwards (B08); twelve points landing
per column (B09); a curve followed to zero and a fix typing itself (B10).
**No two consecutive beats share a visual scheme.**
