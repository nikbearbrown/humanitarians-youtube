# SHOTLIST — *What We Chased Before.*

Ep. 10 · 14 beats · every slot filled by the pipeline; no pantry, no slates.

**LAYOUT BAND PLAN** — every Manim beat obeys it, in both aspects. The vertical
bands are identical in 16:9 and 9:16 because Manim keeps `frame_height = 8.0`
either way; only the horizontal extent changes (x ±6.15 landscape, x ±1.80
portrait).

| y | what sits there |
|---|---|
| +3.02 | title (chrome) |
| +2.66 | hairline (chrome) |
| +2.40 … −1.90 | the figure |
| −2.50 | the closing line, terracotta rule at −2.78 |
| −3.20 | citation, left-anchored (chrome) |
| −3.12 | `@HumanitariansAI` wordmark bug, right-anchored (chrome, LOGO LAW) |

**PLATE GEOMETRY.** `ph = pw × (ih/iw)`, and the landscape figure band is only
4.30 units. Seven of this reel's ten GATE B failures came from sizing a plate
by eye and leaving nothing underneath it.

| plate | pixels | ih/iw | used at pw | ph |
|---|---|---|---|---|
| `selection` | 1500×760 | 0.507 | 6.40 | 3.24 |
| `deadline` | 1560×780 | 0.500 | 6.40 | 3.20 |
| `loop` | 1720×740 | 0.430 | 7.00 | 3.01 |
| `composition` | 1720×620 | 0.360 | 8.60 | 3.10 |
| `boundary` | 1720×700 | 0.407 | 7.60 | 3.09 |
| `budget` | 1560×780 | 0.500 | 4.90 | 2.45 |

**COLOUR CONTRACT.** Terracotta marks **what doubt finds**: the rare class in
every plot, the uncertainty-sampling picks, the exploration quota, the one
recall curve that moves. Ink marks **the confident majority**: the well-sampled
classes, the accuracy number that rises while nothing improves, the count of
confirmed Ia that exploration costs. The mapping never flips.

The load-bearing consequence is **B06**, where the ink curves lie flat on the
axis at zero for twelve seasons while the accuracy panel beside them climbs.

| Beat | Lane | Scene / pattern | The picture | Motion |
|---|---|---|---|---|
| B00 | Remotion | `ClaudeComposerAsk` | Cold open. The ask types itself; three result lines land it ANSWERED. | type-on |
| B01 | Manim | `B01_Presenter` | Name card. Two rows — "nine episodes / AI looks at the sky", **struck**, then "this one / AI chooses what we look at" in the accent. | kinetic |
| B02 | Manim | `B02_OneBreath` | **The BLUF, not an exhibit.** Three sets of kinetic type: IT FADES IN DAYS → THERE ARE TOO MANY → IT LEARNED FROM OUR LAST CHOICE, the last underlined in the accent. | kinetic |
| B03 | Manim | `B03_TheDeadline` | Three computed Bazin light curves with the useful window shaded and a terracotta rule at its edge. Counters: **10,000,000** changes a night · **1 in 10** ever gets a spectrum, underlined. | drawon |
| B04 | Manim | `B04_WhichOnes` | Four published confirmation-fraction bars by peak magnitude; the two faint bands ring terracotta around what was never confirmed. A quiet tag: *published, not measured here*. | isotype |
| B05 | Manim | `B05_TheLoop` | **The mechanism.** Four chained boxes — WE CHOOSE → IT GETS A LABEL → THE MODEL LEARNS → IT RECOMMENDS — with a terracotta return leg routed clear of every label, back into the first box. | drawon |
| B06 | Manim | `B06_TwelveSeasons` | **The experiment.** Two panels: accuracy rising for all three strategies, and rare-class recall where only the terracotta curve moves. Counter: **48 of 60** runs never recognise it once. | annotate |
| B07 | Manim | `B07_WhatGotLabelled` | The labelled set's composition season by season, greedy against doubt. Two figures: **0.19%** and **16.8%**. | stagger |
| B08 | Manim | `B08_SpendItOnDoubt` | The feature space at season 1 and season 8: ink for what is labelled, terracotta rings for where the next spectra go. Chips: **3.6×** the base rate, then **8.4×**. | annotate |
| B09 | Manim | `B09_TheReceipt` | A card: **92 spectra, not 127**, for the same performance, with a **25% fewer** chip. Beside it: microlensing events · flaring stars, over a **struck** line — never in anyone's training set. | stagger |
| B10 | Manim | `B10_TheTell` | A card: "it is getting better" **struck**; "it is getting narrower" boxed in terracotta. Beside it the trade-off curve, and **35% → 92%**. | stagger |
| B11 | Remotion | `ClaudeVerdictArtifact` | Four recap lines, one per spoken clause. | stagger |
| B12 | Remotion | `ClaudeComposerAsk` | The handoff prompt, typed while read aloud; three grading criteria. | type-on |
| B13 | Remotion | `ClaudeTitleOutro` | Title restate, handle, series subline. | fade |

## Motion lanes

stagger ×4 · type-on ×2 · kinetic ×2 · drawon ×2 · annotate ×2 · isotype ×1 ·
fade ×1. No lane exceeds the histogram warning threshold; GATE L passes clean.

## Where portrait carries less

**The rule: anything the narration SPEAKS stays on screen; the on-screen-only
extras are what portrait loses.**

| Beat | Dropped in 9:16 | Why that one |
|---|---|---|
| B03 | the "window where a spectrum still says something" caption | never spoken — the narration says "a spectrum is only useful early" — and portrait cannot fit plate + two captions + two counters with sublines + a closer |
| B10 | the budget plate's axis label | it brushed the counter beneath it, and the closing line already names the axis |

B05 does not drop an element but **re-routes**: the four boxes stack vertically
and the return leg runs down the right-hand side instead of underneath.

## Pacing

`scenes.py` paces each scene to its measured narration via `Paced`, and
`hold_to_beat` subtracts `TAIL_TRIM` so every scene lands *under* its beat — a
short clip is padded with a held frame, a long one is centre-cut and would lose
its closing line.

## 9:16

`short/` carries the same 14 beats at 2160×3840 — no beats cut. Remotion beats
re-render against the `…916` compositions; Manim beats re-render from the same
`scenes.py`.
