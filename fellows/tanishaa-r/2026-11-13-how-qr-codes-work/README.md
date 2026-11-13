# How a QR Code Works — Tanishaa

## This week's contribution
- **Question:** how can a QR code still scan when part of it is covered?
- **Prediction:** the highest error-correction level ("30%") should survive having about 30% of the code covered.
- **What I built:** a 2½-minute explainer. The worked example (`demo/qr_demo.py`) encodes our channel link at every level, covers a growing square in the middle, and tries to read it back with a real QR reader (OpenCV).
- **Observed result:** the lowest level (L) failed once a 7 × 7 patch was covered. The highest (H) still read with 17 × 17 covered, about 21% of the code's area, not 30%. The 30% counts codewords, and a solid patch cuts across more codewords than its area suggests.
- **Next experiment:** scatter the damage (smudges, a scratch line) instead of one block, and see whether the readable share gets closer to 30%.

## Human and AI work
- **My decisions, implementation and verification:** topic choice (QR codes, from four options), script approval (v2, after the fact-check). _[Tanishaa: add what you reviewed or changed.]_
- **AI tools/voices used and what they generated:** Claude (Claude Code) drafted the script, wrote the demo, the fact-check, the beat sheets and QrScenes.tsx, and ran the build. Kokoro `af_bella` (a local AI voice) speaks all narration, which is disclosed in the opening.
- **What I rejected or corrected:** _[Tanishaa: add anything you changed.]_ The fact-check caught one wrong line in v1 ("most of a QR code isn't your message", false at the lowest level), reworded in v2.
- **What remains unverified or failed:** the damage test uses one reader (OpenCV); phone camera apps may do a little better or worse. The history (1994, Denso Wave, car parts) is from Wikipedia, because Denso Wave's own sites would not load.

## Reproduce
- Brutalist commit `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-13.
- Steps: `python demo/qr_demo.py` → `python3 build_sheet.py` → `generate_audio_kokoro.py . --speed 0.95` → `python word_times.py` → `python3 build_sheet.py` → `remotion_scenes.py` → `python add_bug.py B00 B10` → `./art final`; vertical: `./art vertical`, edit B09/B10, render, `add_bug.py --dir vertical B00 B10`, `./art final vertical --height 3840`.
- Media (MP4/MP3) is on Drive, not GitHub: [week folder 13-11-2026](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of).

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape `HowQrCodesWork_TanishaaR.mp4` | [Drive week folder](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of) (`landscape/`) | 3840×2160 | 2:38.0 | `217ac6f1f4efadc18b9cb869ac4d1d6f933b81716ec63a8e562e143a9b8f3e38` |
| Vertical `HowQrCodesWork_TanishaaR.mp4` | [Drive week folder](https://drive.google.com/drive/folders/1U8_ewZfbnmSDZF3BNg6Z896sAiY9p8Of) (`vertical/`) | 2160×3840 | 2:38.0 | `0942a2bd5bc3c4714ddaf257c3386d063a4f2b64f3aa5b0d2883679826ee2842` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending
