# FEEDBACK — "How Google Maps Works"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py` and `sync_cues.py`, writing
`props.durationSeconds`, rebuilding and re-rendering the scene (`python build_hf.py B0x --render` for a
HyperFrames beat, which reads the new cues), and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | WHERE AM I | HyperFrames `gps` (`hyperframes/B01-l.html`, `B01-v.html`) |
| B02 | THE MAP | HyperFrames `build` |
| B03 | THE ROUTE | HyperFrames `route` |
| B04 | TRAFFIC | HyperFrames `traffic` |
| B05 | ARRIVAL TIME | HyperFrames `eta` |
| B06 | HOW BUSY | HyperFrames `busy` |
| B07 | HOW CROWDED | HyperFrames `bus` |
| B08 | WHAT TO DO | `HaiApplyCard` |
| B09 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is
`python maps.py` (seeded, so the numbers repeat), then `python build_hf.py` to rewrite the compositions.
Rendering writes its temporary frames to D:, never C:.
