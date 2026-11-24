# BUILD-LOG — Brutalist, Shared

Brutalist toolkit `a99b5323` (main, 2026-10-23), built 2026-10-24 in a Linux cloud container (Python 3.13 venv, Manim 0.20.1, Remotion 4.0.535, Kokoro `am_onyx`).

## Commands
```bash
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>         # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00    # B10, B80; short: B00
<brutalist>/art run <reel>                # Manim 4K + gates A/W/B, review cut
python3 <brutalist>/runtime/scripts/type_check.py <reel>                    # GATE T: PASS
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical
```

## Gates and fixes (in order)
- GATE L kicker → `topic: "Irreducibly Human"`. Professor-notes gate tripped by beat IDs B05/B06 → renumbered B00…B90.
- GATE A (static) → string font weights, `scale_to_fit_*` instead of size setters.
- GATE B (layout, strict) → date label under a stem line; title/caption past safe area → moved.
- GATE T (type) → accent #C4623F was 3.86:1 on cream → #A64B2A (5.4:1); thumbnails cropped to title + command (the mascot's #D97757 body read as accent text).
- Final frame check → underfill on B50/B70/B90 and Short B10/B30/B40/B90 → structure shown dimmed from the start, layouts spread. Review-cut Gate V edge-bleed hits were the burned-in review timecode/labels (clean cut: 0 BLOCKER).
- Fellow checklist: footer text removed (no HAI bug, `channel_title: ""`, no typewriter brand label).

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `brutalist-shared.mp4` (verified receipt) | 3840×2160 | 133.46 s | −24.5 LUFS | 7a4a8562d4adc5bd25c764be6d5968ea8cb8e4b74f5312e702f0b4039bd9b531 |
| **delivered** `landscape/BrutalistShared_BoopeshM.mp4` | 3840×2160 | 133.5 s | −14.1 LUFS, −1.0 dBTP | 422523e93bcca5aa68c3568b62b7950c136cc23d59e3c671028bdc764a34b54c |
| toolkit master `brutalist-shared-short.mp4` (verified receipt) | 2160×3840 | 39.9 s | — | 9a5c2a588f93c3ae27233c6a0d8796577a1f9ea5504f5b94b4e45a625d3b6a8a |
| **delivered** `vertical/BrutalistShared_BoopeshM.mp4` | 2160×3840 | 39.9 s | −14.2 LUFS, −0.9 dBTP | 038e3a478d5522ef60112b530672d0c4fe226d63733704bec9c0e2f3150508b9 |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, linear) to YouTube's reference level.
