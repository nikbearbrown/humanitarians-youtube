# FEEDBACK — "How Apps Find a Song's Key"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B02) and `sync_cues.py`,
writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `KeyNotes` |
| B02 | MECHANISM | `KeyChroma` |
| B03 | MATH | `KeyProfiles` |
| B04 | MEASURED | `KeyGrid` |
| B05 | THE CATCH | `KeyRelative` |
| B06 | KEY CHANGE | `KeyChange` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is two
commands: `python key.py` then `python export_key_data.py` (about twenty seconds).
