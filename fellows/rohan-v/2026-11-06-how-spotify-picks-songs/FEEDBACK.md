# FEEDBACK — "How Spotify Picks Songs"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py` and `sync_cues.py`, writing
`props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | SIGNALS | `RecsSignals` |
| B02 | THE GRID | `RecsGrid` |
| B03 | WHAT IT LEARNED | `RecsNeighbours` |
| B04 | THE TEST | `RecsAccuracy` |
| B05 | THE CATCH | `RecsPopularity` |
| B06 | EXPLORE | `RecsExplore` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [evidence/run.log](./evidence/run.log). Re-running the evidence is two
commands: `python recs.py` then `python export_recs_data.py` (on the CPU; the feedback loop retrains the model 18
times and takes longest). Every step is seeded, and a partial re-run on 2026-11-09 reproduced the accuracy
results exactly.
