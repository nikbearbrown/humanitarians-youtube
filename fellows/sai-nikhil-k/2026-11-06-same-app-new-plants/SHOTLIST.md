# SHOTLIST — Same App, New Plants

Ten beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Seven are registered Remotion compositions; three (B01, B03, B05) are image
plates built by `make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE MODEL MENU | app screenshots | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | WHAT 0.72 MEANS | remotion | `TypesetMath` (3 rows) | illustrate | yes → `TypesetMath916` |
| B03 | FOUR INVADERS | iNaturalist photos | `make_plates.py` · four | staged reveal + 2% push | yes → `pantry/B03-916.mp4` |
| B04 | NATIVE LOOK-ALIKES | remotion | `ExecutedData` (probability, 4 rows) | illustrate | yes → `ExecutedData916` |
| B05 | CALLED INVASIVE | app screenshots | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B05-916.mp4` |
| B06 | STILL TO DO | remotion | `ClaudeScienceChipGrid` (6 chips, 3 cols) | illustrate | yes → `ClaudeScienceChipGrid916` |
| B07 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B08 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B09 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Images, captions, credits and cue words are in `build_beats.py`; provenance per
file in `images/src/<slug>.json` and SOURCES.md. Every image is scaled whole and
outlined; nothing is generated.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
