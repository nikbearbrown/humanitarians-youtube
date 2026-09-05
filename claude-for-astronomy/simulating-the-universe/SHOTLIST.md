# SHOTLIST — *The Universe You Can Afford.*

Ep. 07 · 14 beats · every slot filled by the pipeline; no pantry, no slates.

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

**COLOUR CONTRACT.** Terracotta marks **the cheap answer**, every time: the
Zel'dovich curve, the Zel'dovich panel and its frame, the approximation's error,
the arrow that cannot leave the training box. Ink marks the expensive truth. The
mapping never flips, so the viewer learns it once at B05 and reads every later
plate for free. Accented *text* uses `#A44A32`; `#B9B4A0` is strokes and fills only.

| Beat | Lane | Scene / pattern | The picture | Motion |
|---|---|---|---|---|
| B00 | Remotion | `ClaudeComposerAsk` | Cold open. The ask types itself; three result lines land it ANSWERED. | type-on |
| B01 | Manim | `B01_Presenter` | Name card. `OM MALI` with a terracotta hairline; beside it two rows — "six episodes / AI looks at the data", **struck**, then "this one / AI replaces the physics" in the accented token. | kinetic |
| B02 | Manim | `B02_OneBreath` | A computed cosmic-web plate, captioned as a 2D toy. Kinetic type in three sets: NO EXPERIMENT IS POSSIBLE → SO YOU SIMULATE IT, THOUSANDS OF TIMES → NOBODY CAN AFFORD THAT. | kinetic |
| B03 | Manim | `B03_ParameterSpace` | A 2D slice of parameter space with 150 seeded sample dots, one per cosmology. Three counters: 44,100 SIMULATIONS, 7,000 COSMOLOGIES, 8.5 TRILLION PARTICLES, then a terracotta chip: BUILT AS TRAINING DATA. | isotype |
| B04 | Manim | `B04_NoShortcut` | The starting-field plate, then the loop every N-body code runs — DEPOSIT, SOLVE, KICK, DRIFT as four chips around a ring, a terracotta arc tracing progress, and a HUNDREDS OF STEPS chip. | draw-on |
| B05 | Manim | `B05_Zeldovich` | One particle, one arrow, one straight move: ONE MOVE, THEN STOP. Then the Zel'dovich plate arrives **framed in terracotta**, with two chips: RIGHT WHILE IT IS SMOOTH / WRONG ONCE IT COLLAPSES. | draw-on |
| B06 | Manim | `B06_TheCorrection` | The terracotta Zel'dovich plate **minus** the ink N-body plate, resolving into the measured residual. A network glyph takes the residual as its target: LEARN THIS. | draw-on |
| B07 | Manim | `B07_Result` | The measured power-spectrum plate; the scene draws the axis labels and names the two curves. Then WITHIN ~5% and A THOUSANDTH OF THE TIME. | annotate |
| B08 | Manim | `B08_DesignTell` | A card: WHAT THE MODEL LEARNED. Row one, **struck**: the law of gravity. Row two, boxed in terracotta: the map from start to finish — "…for the universes it was shown". Beside it, the training set as a plate. | stagger |
| B09 | Manim | `B09_WhereItBreaks` | The halo zoom pair — N-body in ink, Zel'dovich in terracotta — with a ring on the core the cheap guess fails to build, and the two measured figures: 4% on large scales, 58% on small ones. | annotate |
| B10 | Manim | `B10_TheBox` | A box labelled THE COSMOLOGIES IT WAS TRAINED ON, filled with N-body runs as dots, the emulator chip inside it, and an arrow out of the box **crossed out** in terracotta: a cosmology it never saw. | annotate |
| B11 | Remotion | `ClaudeVerdictArtifact` | Four recap lines, one per spoken clause. | stagger |
| B12 | Remotion | `ClaudeComposerAsk` | The handoff prompt, typed while read verbatim; three grading criteria as output lines. | type-on |
| B13 | Remotion | `ClaudeTitleOutro` | Title restate, handle, series subline. | fade |

## Motion lanes

draw-on ×3 · annotate ×3 · kinetic ×2 · type-on ×2 · stagger ×2 · isotype ×1 · fade ×1.
No lane exceeds the histogram warning threshold.

## Where portrait carries less

9:16 is not a crop — with the same height and a third of the width it has *less*
usable area. Six scenes drop a secondary element by design:

| Beat | Dropped in 9:16 |
|---|---|
| B03 | the two axis labels (the title already says what the box is) |
| B06 | the network glyph and its "learn this" label |
| B07 | the rotated `power` y-axis label, and the "on the statistics cosmologists actually use" note |
| B08 | the training-set plate on the right |
| B09 | the "measured in this reel's own run" tag |
| B10 | nothing dropped — the box and struck arrow simply stack |

## Pacing

`scenes.py` paces each scene to its measured narration via the `Paced` base
class (RT multiplier, per-reveal HOLD, and `hold_to_beat()` on the tail), so
`compile.py` never has to stretch a clip. Ep. 06 shipped a first cut with three
beats slowed 3.2–3.3× before this was added, and GATE V cannot see it.

## 9:16

`short/` carries the same 14 beats at 2160×3840 — no beats cut. Remotion beats
re-render against the `…916` compositions; Manim beats re-render from the same
`scenes.py`. See `BUILD-LOG.md` § "The 9:16 cut".
