# SHOTLIST — Ten Words Apart

Ten beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Seven are registered Remotion compositions; three (B01, B03, B05) are image
plates built by `make_plates.py` (word tiles from `make_tiles.py`).

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | HOW IT SCORES | word tiles (Commons photos) | `make_plates.py` · rows2 | staged reveal + 2% push | yes → `pantry/B01-916.mp4` (4+3 tile grids) |
| B02 | THE SCORE | remotion | `TypesetMath` (2 rows) | illustrate | yes → `TypesetMath916` |
| B03 | THE EXPERIMENT | model card + author figures | `make_plates.py` · hero+2 | staged reveal + 2% push | yes → `pantry/B03-916.mp4` |
| B04 | WE RE-SCORED IT | remotion | `ExecutedData` (table, 4 rows) | illustrate | yes → `ExecutedData916` |
| B05 | ASKED FOR ADJECTIVES | word tiles + author figure | `make_plates.py` · wide+side | staged reveal + 2% push | yes → `pantry/B05-916.mp4` |
| B06 | DID IT WRITE BETTER? | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B07 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B08 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B09 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Images, captions, credits and cue words are in `build_beats.py`; provenance per
file in `images/src/<slug>.json` and SOURCES.md. Tiles are the only crop
(centre squares, `make_tiles.py`); everything else is scaled whole. Nothing is
generated.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
