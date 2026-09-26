# FEEDBACK — "How AI Image Generators Turn Noise Into a Picture"

Reviewer notes. Empty until someone reviews it.

## How to leave feedback

Point at a beat by its ID. Narration durations are the master clock, so a note that changes narration forces regenerating that beat's audio, re-running `align.py` and `sync_cues.py` (the word clock moves with the words), re-rendering the scene to its new duration, and recompiling both cuts.

| Beat | Act | Component |
|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` |
| B01 | BACKGROUND | `DiffuseSeedStatic` |
| B02 | ANALOGY | `DiffuseRainForward` |
| B03 | MECHANISM | `DiffuseMixEquation` |
| B04 | MEASURED | `DiffuseReverseRun` |
| B05 | SEED AND PROMPT | `DiffuseSeedPrompt` |
| B06 | WHAT TO DO | `HaiApplyCard` |
| B07 | OUTRO | `HaiTitleOutro` |

If a **number** is disputed, check [MEASUREMENTS.txt](./MEASUREMENTS.txt) — every figure on screen has a line in it. Re-running the evidence is three commands: `python train_toy_diffusion.py`, `python scan_seeds.py`, `python export_toy_data.py` (about 45 minutes on a laptop CPU). If a **claim about Midjourney** is disputed, [FACTCHECK.md](./FACTCHECK.md) quotes the documentation line it rests on.

## Review status

- PM review: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Notes

_(none yet)_
