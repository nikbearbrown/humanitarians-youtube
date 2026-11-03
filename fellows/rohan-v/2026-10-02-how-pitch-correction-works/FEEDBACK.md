# FEEDBACK — "How Pitch Correction Works"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes
narration forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04,
B05) and `sync_cues.py`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `PitchCycles` |
| B02 | MECHANISM | `PitchFindPeriod` |
| B03 | MATH | `PitchSnapCents` |
| B04 | MEASURED | `PitchMelodyFix` |
| B05 | RETUNE SPEED | `PitchRetuneSpeed` |
| B06 | THE CATCH | `PitchWrongNote` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the
evidence is two commands: `python pitch_demo.py` then `python export_pitch_data.py` (about ten
seconds on a laptop).
