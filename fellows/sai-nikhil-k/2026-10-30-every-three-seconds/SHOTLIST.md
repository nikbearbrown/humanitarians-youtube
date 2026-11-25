# SHOTLIST — Every Three Seconds

Ten beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Eight are registered Remotion compositions; two (B01, B06) are image plates
built by `make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | CHECK AN AUDIO | app screenshots | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | HOW IT HEARS | remotion | `ClaudeScienceChipGrid` (6 chips, 3 cols) | illustrate | yes → `ClaudeScienceChipGrid916` |
| B03 | ONE WINDOW, ONE NUMBER | remotion | `TypesetMath` (3 rows) | illustrate | yes → `TypesetMath916` |
| B04 | A PERFECT SCORE | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B05 | UNDER THE DRONE | remotion | `ExecutedData` (probability, 4 rows) | illustrate | yes → `ExecutedData916` |
| B06 | ONE RECORDING, TWO WAYS | app screenshots | `make_plates.py` · pair | staged reveal + 2% push | yes → `pantry/B06-916.mp4` |
| B07 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B08 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B09 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Images, captions, credits and cue words are in `build_beats.py`; provenance per
file in `images/src/<slug>.json` and SOURCES.md. Every image is scaled whole and
outlined; nothing is generated.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
