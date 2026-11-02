# FEEDBACK — "How AI Voices Read a Script"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04, B05) and `sync_cues.py`,
writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts. Check any new proper noun
with the pronunciation step before voicing it (B05 is about exactly that).

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `VoicePipeline` |
| B02 | MECHANISM | `VoiceG2P` |
| B03 | MEASURED | `VoiceHeteronyms` |
| B04 | NUMBERS | `VoiceNumbers` |
| B05 | THE FIX | `VoiceRespell` |
| B06 | WHAT TO DO | `HaiApplyCard` |
| B07 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is two
commands: `python voice.py` then `python export_voice_data.py` (about a minute).
