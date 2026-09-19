# SHOTLIST — *The Sharpest Guess.*

Ep. 09 · 14 beats · every slot filled by the pipeline; no pantry, no slates.

**LAYOUT BAND PLAN** — every Manim beat obeys it, in both aspects. The vertical
bands are identical in 16:9 and 9:16 because Manim keeps `frame_height = 8.0`
either way; only the horizontal extent changes (x ±6.15 landscape, x ±1.80
portrait). `scenes.py` reads the frame and lays out accordingly.

| y | what sits there |
|---|---|
| +3.02 | title (chrome) |
| +2.66 | hairline (chrome) |
| +2.40 … −1.90 | the figure |
| −2.50 | the closing line, terracotta rule at −2.78 |
| −3.20 | citation, left-anchored (chrome) |
| −3.12 | `@HumanitariansAI` wordmark bug, right-anchored (chrome, LOGO LAW) |

**PLATE GEOMETRY.** Every plate is a row of square panels, so
`ph = pw × (ih/iw)`. The figure band is 4.30 units tall in landscape, so this
arithmetic has to be done, not assumed — Ep. 08's B04 plate was 4.19 units tall
and covered the title, and this reel's B09 first draft put a 3.60-unit plate at
y = 0.92, pushing its top to +2.72 and its axis label into the title.

| plate | pixels | ih/iw | ph at pw = 10.6 |
|---|---|---|---|
| `twokinds` · `forward` · `nullspace` | 1888×460 | 0.2436 | 2.58 |
| `threeanswers` | 1412×460 | 0.3258 | 3.45 |
| `posterior` | 2364×460 | 0.1946 | 2.06 |
| `varratio` | 1640×820 | **0.5000** | **5.30** — the tall one; sized to 5.80 wide |

**COLOUR CONTRACT.** Terracotta marks **what the prior supplied**: the
difference between two skies the telescope cannot distinguish, the disagreement
between posterior samples, the variance-ratio curve, the invented half of a
reconstruction. Ink marks **what the photons measured**: the observation, the
data-consistent part, the agreed core. The mapping never flips, so B05 teaches
it once and every later plate reads for free. Accented *text* is `#A44A32`;
`#B9B4A0` is strokes and fills only.

The load-bearing consequence is **B08**, where the disagreement map is the only
terracotta object on screen and is also the only honest output.

| Beat | Lane | Scene / pattern | The picture | Motion |
|---|---|---|---|---|
| B00 | Remotion | `ClaudeComposerAsk` | Cold open. The ask types itself; three result lines land it ANSWERED. | type-on |
| B01 | Manim | `B01_Presenter` | Name card. `OM MALI` with a terracotta hairline; beside it two rows — "eight episodes / AI reads the sky", **struck**, then "this one / AI draws it" in the accented token. | kinetic |
| B02 | Manim | `B02_OneBreath` | **The BLUF, and deliberately NOT an exhibit.** Three sets of kinetic type on a card: BLURRED AND NOISY → SOME OF IT IS ARITHMETIC → THE REST IS AN ASSUMPTION, the last underlined in the accent. | kinetic |
| B03 | Manim | `B03_TwoKinds` | Four computed panels: striped · cleaned · blurred · the truth. A quiet chip under the first pair (a pattern: measured, subtracted, 3.6% left) and a terracotta chip under the second (a loss: nothing subtracts this). | drawon |
| B04 | Manim | `B04_TheChain` | The forward model as four panels — the real sky, blurred, photons, plus read noise — with a LOSSY chip under the second and a counter: **98%** of the grid's frequencies carry nothing. | drawon |
| B05 | Manim | `B05_SameData` | **The centrepiece, and a proof.** Two skies, the terracotta map of how they differ, and the single observation they share. Counters: **52%** apart as skies · **0.0000** noise σ between their images, underlined. | annotate |
| B06 | Manim | `B06_ThreeAnswers` | Three posterior samples under three different priors, with **χ²/N = 1.008 · 1.007 · 1.008** typed beneath, "all three match the data equally well", and a terracotta chip: they differ from each other by 36%. | stagger |
| B07 | Manim | `B07_WhereItComesFrom` | An ink card of training tiles → an arrow → a terracotta box: THE PRIOR / what a galaxy looks like. Counter: **17,852** simulated galaxies, and the cost pair (landscape only). | isotype |
| B08 | Manim | `B08_ManyAnswers` | Five panels — three samples, their mean, and the terracotta disagreement map — with two lines: *where they agree, the photons decided* / *where they disagree, the prior did*, and a chip: above the cutoff the spread IS the prior — 1.0000. | annotate |
| B09 | Manim | `B09_WhenItInvents` | The computed variance-ratio curve with a terracotta ring on its weak-data end, and beside it the two **published** figures — 0.0114 at SNR 699, 0.0685 at SNR 7 — under a tag reading *published, not measured here*. | annotate |
| B10 | Manim | `B10_TheTell` | A card headed WHAT A DENOISER ACTUALLY DOES: "removes the noise" **struck**; "adds an assumption" boxed in terracotta. Beside it two schematic panels, a drawn tick, and **QUALITATIVELY** in ink. | stagger |
| B11 | Remotion | `ClaudeVerdictArtifact` | Four recap lines, one per spoken clause. | stagger |
| B12 | Remotion | `ClaudeComposerAsk` | The handoff prompt, typed while read aloud; three grading criteria as output lines. | type-on |
| B13 | Remotion | `ClaudeTitleOutro` | Title restate, handle, series subline. | fade |

## Motion lanes

drawon ×2 · annotate ×3 · kinetic ×2 · type-on ×2 · stagger ×3 · isotype ×1 ·
fade ×1. No lane exceeds the histogram warning threshold, and GATE L passes
clean.

## Where portrait carries less

9:16 is not a crop — with the same height and a third of the width it has
*less* usable area. Five scenes drop a secondary element by design. **The rule
for choosing what goes: anything the narration SPEAKS stays on screen; the
on-screen-only extras are what portrait loses.**

| Beat | Dropped in 9:16 | Why that one |
|---|---|---|
| B05 | long panel labels, shortened to "sky one / sky two / differ / observed" | four labels across 3.44 units cannot carry full phrases |
| B07 | the cost pair (133 hours on 32 GPUs · 100 seconds) | never spoken; the 17,852 counter is the figure that matters |
| B08 | all five panel labels | 0.69 units each is unreadable, and the two sentence rows below name what the panels are |
| B09 | nothing dropped — the curve and the published pair simply stack | both are load-bearing for the published/computed distinction |
| B10 | the two comparison cards and the drawn tick | their labels collided with QUALITATIVELY, which is the part the narration actually speaks |

## Pacing

`scenes.py` paces each scene to its measured narration via the `Paced` base
class (RT multiplier, per-reveal HOLD, and `hold_to_beat()` on the tail), so
`compile.py` never has to stretch a clip. Ep. 06 shipped a first cut with three
beats slowed 3.2–3.3× before this was added, and GATE V cannot see it.

A residual undershoot of ~0.1 s on some beats is frame quantisation inside
Manim's `play()` and is left alone deliberately: a short clip is padded with a
held frame (invisible), while a long one is centre-cut and would clip the
closing line off both ends.

## 9:16

`short/` carries the same 14 beats at 2160×3840 — no beats cut. Remotion beats
re-render against the `…916` compositions; Manim beats re-render from the same
`scenes.py`. See `BUILD-LOG.md` § "The 9:16 cut".
