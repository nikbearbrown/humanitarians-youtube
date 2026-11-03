# FEEDBACK — "How Noise-Cancelling Headphones Work"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04) and `sync_cues.py`,
writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `AncWaves` |
| B02 | MECHANISM | `AncSystem` |
| B03 | MATH | `AncPhase` |
| B04 | MEASURED | `AncTypes` |
| B05 | THE CURVE | `AncCurve` |
| B06 | WHAT TO DO | `HaiApplyCard` |
| B07 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is two
commands: `python anc.py` then `python export_anc_data.py` (about thirty seconds).
