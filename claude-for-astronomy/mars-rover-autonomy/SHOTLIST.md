# SHOTLIST — *Nobody Is Coming to Approve It.*

Ep. 06 · 14 beats · every slot filled by the pipeline; no pantry, no slates.

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

| Beat | Lane | Scene / pattern | The picture | Motion |
|---|---|---|---|---|
| B00 | Remotion | `ClaudeComposerAsk` | Cold open. The ask types itself; three result lines land it ANSWERED. | type-on |
| B01 | Manim | `B01_Presenter` | Name card. `OM MALI` with a terracotta hairline; beside it two rows — "every episode so far: too much data", **struck**, then "this one: too much distance" in the accented token. | kinetic |
| B02 | Manim | `B02_OneBreath` | Kinetic type in three sets over a faint navcam plate: ONE PLAN A DAY → two decision chips → SCORED, NOT ASKED. | kinetic |
| B03 | Manim | `B03_LightTime` | Earth and Mars as two discs with a long channel between them. A terracotta pulse crosses; a bracket reads 3–22 MINUTES, ONE WAY; the return doubles it. A struck joystick chip. A sol bar: ONE COMMAND BLOCK. | annotate |
| B04 | Manim | `B04_WhatItSees` | The synthetic navcam plate, its stereo partner behind it, an arrow to the cost grid drawing on cell by cell; one cell ringed terracotta with STEP HEIGHT and SLOPE. | draw-on |
| B05 | Manim | `B05_TheFan` | The cost grid full width. The candidate fan draws on (~1,700 PATHS chip, 6 m bracket); rejected arcs stay grey, survivors darken under a CLEARANCE CHECK chip, one arc turns terracotta with a ring on its waypoint. | draw-on |
| B06 | Manim | `B06_Aegis` | The rockfield plate → the contour version (six closed outlines draw on) → three measurement chips (SIZE, BRIGHTNESS, RANGE) → a SCENE PROFILE card → the ranked plate with one terracotta contour. | draw-on |
| B07 | Manim | `B07_Snowdrift` | The top-down route map. Grey straight line labelled 520 m; terracotta driven route labelled 759 m; counters for 6 SOLS and ~12 SOLS SAVED. | annotate |
| B08 | Manim | `B08_TheProfile` | A document card: SCENE PROFILE, four rule lines typing in (prefer LARGE / BRIGHT / NEAR / THIS OUTLINE), then a signature line WRITTEN ON EARTH, BEFORE LAUNCH. An arrow carries it across the gap to the rover mark. | stagger |
| B09 | Manim | `B09_Result` | Two autonomy bars (CURIOSITY 6.2%, PERSEVERANCE ~90%), a distance rule at 699.9 m, and two AEGIS bars (>93% vs ~20%), each with its condition. | isotype |
| B10 | Manim | `B10_TwoLimits` | Left: the route map reduced, a terracotta bracket over the 239 m of detour, CAUTION PAID IN METRES. Right: a sol axis with SOL 442 and SOL 697, the span filled terracotta reading 255 SOLS. | annotate |
| B11 | Remotion | `ClaudeVerdictArtifact` | Four recap lines, one per spoken clause. | stagger |
| B12 | Remotion | `ClaudeComposerAsk` | The handoff prompt, typed while read verbatim; three grading criteria as output lines. | type-on |
| B13 | Remotion | `ClaudeTitleOutro` | Title restate, handle, series subline. | fade |

## Motion lanes

draw-on ×3 · annotate ×3 · kinetic ×2 · type-on ×2 · stagger ×2 · isotype ×1 · fade ×1.
No lane exceeds the histogram warning threshold.

## Colour discipline

Terracotta `#D97757` appears as a **mark** and marks exactly one committed
decision per beat: the chosen path (B05), the chosen rock (B06), the driven
route (B07), the signature on the profile (B08), the detour and the sol span
(B10). Accented *text* uses `#A44A32`. `#B9B4A0` is strokes and fills only.

## 9:16

`short/` carries the same 14 beats at 2160×3840 — no beats cut. Remotion beats
re-render against the `…916` compositions; Manim beats re-render from the same
`scenes.py`, which branches on the frame aspect. See `BUILD-LOG.md` § "The 9:16
cut".
