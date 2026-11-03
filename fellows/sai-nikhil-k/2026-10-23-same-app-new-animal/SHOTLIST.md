# SHOTLIST — Same App, New Animal

Eleven beats, two deliverables (16:9 and the full-length 9:16), **no open
slots**. Seven are registered Remotion compositions; four (B01, B03, B05, B07)
are image plates built by `make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | GAVIA TODAY | app screenshots | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | THE LOON MODEL ON SEALS | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B03 | ASKED ABOUT OTHER ANIMALS | app screenshots | `make_plates.py` · pair | staged reveal + 2% push | yes → `pantry/B03-916.mp4` |
| B04 | WHY AERIAL ANIMALS VANISH | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B05 | ONE FRAME, TWO WAYS | NOAA survey frame | `make_plates.py` · frame+tile | staged reveal + 2% push | yes → `pantry/B05-916.mp4` |
| B06 | WHAT TO BUILD | remotion | `ClaudeScienceChipGrid` (6 chips, 3 cols) | illustrate | yes → `ClaudeScienceChipGrid916` |
| B07 | WHO'S NEXT | screenshot + photos | `make_plates.py` · band+3 | staged reveal + 2% push | yes → `pantry/B07-916.mp4` |
| B08 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B09 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B10 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Images, captions, credits and cue words are in `build_beats.py`; provenance per
file in `images/src/<slug>.json` and SOURCES.md. Every image is scaled whole and
outlined; nothing is generated.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
