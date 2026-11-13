# FEEDBACK — "How AI Music Generators Turn Text Into Audio"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04, B06) and
`sync_cues.py`, writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `TokSampleCount` |
| B02 | MECHANISM | `TokCodebook` |
| B03 | MATH | `TokResidual` |
| B04 | MEASURED | `TokCodecQuality` |
| B05 | PREDICT | `TokNextGuess` |
| B06 | THE TEXT | `TokTextSteer` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is
two commands: `python codec.py` then `python export_tok_data.py` (about two and a half minutes).
