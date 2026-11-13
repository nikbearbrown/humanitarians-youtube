# FEEDBACK — "How Shazam Finds a Song"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04) and
`sync_cues.py`, writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `ShazamPeaks` |
| B02 | MECHANISM | `ShazamHashPairs` |
| B03 | MATH | `ShazamOffsetVote` |
| B04 | MEASURED | `ShazamMatch` |
| B05 | NOISE | `ShazamNoiseSweep` |
| B06 | THE CATCH | `ShazamVersions` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is
two commands: `python fingerprint.py` then `python export_shazam_data.py` (about twenty seconds on a
laptop).
