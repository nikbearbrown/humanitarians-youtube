# FEEDBACK — "How Apps Find a Song's Tempo"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration
forces regenerating that beat's audio, re-running `align.py`, `mix_listen.py` (B01) and
`sync_cues.py`, writing `props.durationSeconds`, re-rendering the scene, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `TempoBeats` |
| B02 | MECHANISM | `TempoOnsets` |
| B03 | MATH | `TempoAutocorr` |
| B04 | MEASURED | `TempoPrior` |
| B05 | THE CATCH | `TempoGrid` |
| B06 | DRIFT | `TempoDrift` |
| B07 | WHAT TO DO | `HaiApplyCard` |
| B08 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt). Re-running the evidence is
two commands: `python tempo.py` then `python export_tempo_data.py` (about twenty seconds on a laptop;
add librosa to `PYTHONPATH` for the cross-check column).
