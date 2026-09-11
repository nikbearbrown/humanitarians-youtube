# SHOTLIST — *The Number Went Up.*

Ep. 08 · 14 beats · every slot filled by the pipeline; no pantry, no slates.

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

**COLOUR CONTRACT.** Terracotta marks **what the machine decides**: the
detections the network calls real, the two real postage-stamp classes out of
eight, the fitted tracklet, the uncertainty cloud, the probability curve. Ink
marks **what the sky actually does**: the Earth, the capture disc, the
catalogued fraction. The mapping never flips, so B04 teaches it once and every
later plate reads for free. Accented *text* is `#A44A32`; `#B9B4A0` is strokes
and fills only.

The load-bearing consequence is **B06**, where the terracotta *stops at a
boundary*. The learned half of the pipeline ends there and the number that
frightens people comes out of the ink half. That is the episode.

| Beat | Lane | Scene / pattern | The picture | Motion |
|---|---|---|---|---|
| B00 | Remotion | `ClaudeComposerAsk` | Cold open. The ask types itself; three result lines land it ANSWERED. | type-on |
| B01 | Manim | `B01_Presenter` | Name card. `OM MALI` with a terracotta hairline; beside it two rows — "seven episodes / AI reads the sky", **struck**, then "this one / the reading ends, the arithmetic begins" in the accented token. | kinetic |
| B02 | Manim | `B02_OneBreath` | **The BLUF, and deliberately NOT an exhibit.** Kinetic type in three sets on a card: THE SKY IS SCANNED / every night → A NETWORK REMOVES / the junk → ARITHMETIC DECIDES / whether to worry, the last underlined in the accent. | kinetic |
| B03 | Manim | `B03_TheHaystack` | Two synthetic sky frames and their real difference, labelled last night / tonight / **the difference**, with a terracotta ring on the one real mover. A chip: ABOUT 100,000 ALERTS A NIGHT. | drawon |
| B04 | Manim | `B04_EightKinds` | The eight postage-stamp classes as a 4×2 grid, cosmic ray and dipole **ringed**. Beside it: ONE PIXEL / TWO LOBES, then a chip — ONLY TWO OF THE EIGHT ARE REAL. | isotype |
| B05 | Manim | `B05_Tracklet` | Four terracotta detections with a straight line fitted through them, four hollow artefacts that no line fits, and three counters: 99.6% / 0.4% / **90% less to screen**, underlined. | annotate |
| B06 | Manim | `B06_WhereLearningStops` | **The colour contract's hinge.** A terracotta-filled LEARNED box — "is this dot real?" — an arrow, and an ink-outlined COMPUTED box — "where does it go?". Label: the terracotta stops here. Beneath, one fitted ink track and a terracotta fan of every orbit the data still allows. | drawon |
| B07 | Manim | `B07_TheNumberWentUp` | The **published** Sentry record for 2024 YR4, rebuilt as a native plot: 0.6 → 1.8 → 1.1 → **3.1%** underlined in the accent → the ink collapse to below 0.1%. A chip: TORINO 3 — ONLY APOPHIS EVER MATCHED IT. | annotate |
| B08 | Manim | `B08_WhyItHadTo` | **Computed in this reel.** Three target-plane panels — a terracotta cloud shrinking against a fixed ink Earth, labelled in the core / on the tail / past the Earth — and beside them the computed probability curve with its peak marked. Chip: COMPUTED IN THIS REEL, NOT REDRAWN. | drawon |
| B09 | Manim | `B09_Again` | An ink Moon with the same terracotta cloud crossing it, the 4.3% lunar figure **struck through**, and: ruled out — 5 March 2026, from Webb. | annotate |
| B10 | Manim | `B10_TheTell` | A card headed WHAT IS ACTUALLY AUTOMATED: "is this dot real?" boxed in terracotta; "should you move?" **struck**. Beside it the completeness bars by size class against the 90% rule, and a counter: 11 caught before impact, ever. | stagger |
| B11 | Remotion | `ClaudeVerdictArtifact` | Four recap lines, one per spoken clause. | stagger |
| B12 | Remotion | `ClaudeComposerAsk` | The handoff prompt, typed while read aloud; three grading criteria as output lines. | type-on |
| B13 | Remotion | `ClaudeTitleOutro` | Title restate, handle, series subline. | fade |

## Motion lanes

drawon ×3 · annotate ×3 · kinetic ×2 · type-on ×2 · stagger ×2 · isotype ×1 ·
fade ×1. No lane exceeds the histogram warning threshold, and GATE L passes
clean.

## Where portrait carries less

9:16 is not a crop — with the same height and a third of the width it has
*less* usable area. Five scenes drop a secondary element by design. **The rule
used to choose what goes: anything the narration SPEAKS stays on screen; the
on-screen-only extras are what portrait loses.**

| Beat | Dropped in 9:16 | Why that one |
|---|---|---|
| B04 | the two explanatory sublines under ONE PIXEL / TWO LOBES | the two phrases themselves are spoken; the gloss is not |
| B05 | the 0.4% false-negative counter | 99.6% and 90% are spoken; 0.4% is not |
| B07 | the rotated "chance of impact" y-axis label | rotated it is 1.4 units tall and crosses the portrait safe edge — the identical defect Ep. 07's B07 hit |
| B08 | the "the peak" label | the curve carries its own ink peak marker |
| B09 | the "same object · same date · same shape of story" chip | the only element in the beat the narration never speaks |
| B10 | the completeness plate and its labels | on-screen-only evidence; dropping it keeps every spoken item visible |

## Pacing

`scenes.py` paces each scene to its measured narration via the `Paced` base
class (RT multiplier, per-reveal HOLD, and `hold_to_beat()` on the tail), so
`compile.py` never has to stretch a clip. Ep. 06 shipped a first cut with three
beats slowed 3.2–3.3× before this was added, and GATE V cannot see it.

## 9:16

`short/` carries the same 14 beats at 2160×3840 — no beats cut. Remotion beats
re-render against the `…916` compositions; Manim beats re-render from the same
`scenes.py`. See `BUILD-LOG.md` § "The 9:16 cut".
