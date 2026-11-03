# FEEDBACK — "How Auto-Captions Find Each Word"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B04) and `sync_cues.py`,
writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `CapSpectro` |
| B02 | MECHANISM | `CapTiming` |
| B03 | MEASURED | `CapAccuracy` |
| B04 | NOISE | `CapNoise` |
| B05 | THE CATCH | `CapCatch` |
| B06 | WHAT TO DO | `HaiApplyCard` |
| B07 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is two
commands: `python captions.py` then `python export_cap_data.py` (several minutes on the CPU). Expect the 0 dB and
−5 dB results to move a little between runs (FACTCHECK, "The noisy runs differ"); the clean to +5 dB results were
identical across two runs.
