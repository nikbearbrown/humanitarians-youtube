# How a Computer Turns Text into a Voice — Tanishaa

## This week's contribution
- **Question:** how does a computer turn written text into a spoken voice, and where does it go wrong?
- **Prediction:** the engine would read "I read it yesterday" in the past tense from context.
- **What I built:** a 2½-minute explainer narrated by Bella, the AI voice the video explains. The worked example (`demo/tts_demo.py`) runs the same Kokoro engine on four tricky sentences in two voices and records the phonemes, waveforms, sample rate and style numbers.
- **Observed result:** the prediction was wrong. Kokoro (kokoro-onnx 0.6.1, espeak-ng phonemes) said "reed" in both tenses, read "Oak Dr." as "Oak Doctor", and turned "$5" into "dollar five". Bella and Michael (am_michael) made identical mistakes, because a voice is a 256-number style that changes how sounds are made, not which sounds are chosen.
- **Next experiment:** add a text-normalization step before the phonemizer (spell out money, expand "Dr." by position) and re-run the demo to see which mistakes it fixes.

## Human and AI work
- **My decisions, implementation and verification:** topic choice (from four options), script approval. _[Tanishaa: add what you reviewed or changed.]_
- **AI tools/voices used and what they generated:** Claude (Claude Code) drafted the script, wrote the demo, the beat sheet and the TtvScenes Remotion scenes, and ran the build. Kokoro `af_bella` (a local AI voice) speaks all narration, which is disclosed in the opening.
- **What I rejected or corrected:** _[Tanishaa: add anything you changed.]_ The script's B05 originally claimed the engine picked the right tense; the real demo showed it didn't, so B05 shows the mistakes instead.
- **What remains unverified or failed:** step 3's timing bars (B03) are schematic. The ONNX model returns audio only, not per-sound durations. Kokoro also plans timing inside one network, so the four steps describe text-to-speech in general rather than Kokoro's exact architecture.

## Reproduce
- Brutalist commit `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-08.
- Steps: `python demo/tts_demo.py` → `python3 build_sheet.py` → `generate_audio_kokoro.py` → `python word_times.py` → `python3 build_sheet.py` → `remotion_scenes.py` → `python add_bug.py B00 B07 B08` → `./art final`.
- Media (MP4/MP3/WAV) goes to Drive, not GitHub.

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape | _[Tanishaa: add Drive week folder link]_ (`landscape/`) | 3840×2160 | 2:31.0 | `7a4cc57e7bc5fbbb67932c6d04da73d70e0b5cbe6d785118514d03b9efd6fb7e` |
| Vertical | _[Tanishaa: add Drive week folder link]_ (`vertical/`) | 2160×3840 | 2:31.0 | `1f69140f003f1b9d6bd909f4b013f0696aa9f03dbcb6bfac0ef8d130b8a0cf37` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending
