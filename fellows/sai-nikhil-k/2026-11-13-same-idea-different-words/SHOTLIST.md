# SHOTLIST — Same Idea, Different Words

Seven beats, two deliverables (16:9 and the full-length 9:16), **no open slots**.
Six are registered Remotion compositions; one (B01) is an image plate built by
`make_plates.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THREE CYCLONES | Portals renders | `make_plates.py` · three | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | HOW A CHECK SCORES SAMENESS | remotion | `TypesetMath` (2 rows) | illustrate | yes → `TypesetMath916` |
| B03 | WHAT THE WORDS MISS | remotion | `ExecutedData` (table, 3 rows) | illustrate | yes → `ExecutedData916` |
| B04 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B05 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B06 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

Stills: `images/src/portal_{reindeer,manta,stork}.png`, 1920×1080 canvas grabs
from `evidence/portal_shots.mjs` (CC BY-NC-SA 4.0, Ethan Mollick's Portals).

**Timing note:** TypesetMath/ExecutedData are 15 s comps on 10 s beats;
`build_beats.py` authors reveal times in comp time (`COMP_S / clock`).

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
