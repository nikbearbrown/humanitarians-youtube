# SHOTLIST — Same App, New Look

Seven beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Six are registered Remotion compositions; one (B01) is an image plate built by
`make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | BEFORE AND AFTER | app screenshots | `make_plates.py` · pair | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | CONTRAST IS ARITHMETIC | remotion | `TypesetMath` (3 rows) | illustrate | yes → `TypesetMath916` |
| B03 | WHAT THE CHECKER SAW | remotion | `ExecutedData` (table, 4 rows) | illustrate | yes → `ExecutedData916` |
| B04 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B05 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B06 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Screenshots: `images/src/app_before.png`, `app_after.png` (2x captures from
`evidence/recapture.mjs`, cropped to the top 1640 px; sidecars say how).

**Timing note:** TypesetMath/ExecutedData are 15 s comps and these beats are
11–12 s, so `remotion_scenes.py` retimes them ~1.3×; `build_beats.py` authors
reveal times in comp time (`COMP_S / clock`).

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
