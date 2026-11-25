# SHOTLIST — Every Input, Not Just Some

Ten beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Eight are registered Remotion compositions; two (B02, B05) are image plates
built by `make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE PRICE OF A PROOF | remotion | `TypesetMath` (2 rows) | illustrate | yes → `TypesetMath916` |
| B02 | TESTS VERSUS A PROOF | post figure + photos | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B02-916.mp4` |
| B03 | THE RECIPE | remotion | `ClaudeScienceChipGrid` (6 chips, 3 cols) | illustrate | yes → `ClaudeScienceChipGrid916` |
| B04 | A MILLION TESTS, ONE PROOF | remotion | `ExecutedData` (table, 4 rows) | illustrate | yes → `ExecutedData916` |
| B05 | WHAT CAME OUT | post charts + repo screenshot | `make_plates.py` · 2x2 | staged reveal + 2% push | yes → `pantry/B05-916.mp4` |
| B06 | VERIFIED IS NOT BUG-FREE | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B07 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B08 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B09 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Images, captions, credits and cue words are in `build_beats.py`; provenance per
file in `images/src/<slug>.json` and SOURCES.md. Every image is scaled whole and
outlined; nothing is generated.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
