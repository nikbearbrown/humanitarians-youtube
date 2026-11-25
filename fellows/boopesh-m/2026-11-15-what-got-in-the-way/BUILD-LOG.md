# BUILD-LOG — What Got in the Way

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-15 in a Linux cloud container (Python 3.13
venv, Manim 0.20.1, Remotion, Kokoro `am_onyx`), sharing 4 CPUs with another build. Data: `humanitarians-youtube`
`215e6a5f..dc2963ec` (this week, 32 frictional logs) and `bc722c05..215e6a5f` (last week, recounted; published
numbers re-checked on `a953b021`).

## Commands
```bash
python3 code/week_stats.py > code/run.log      # -> code/results.json (both weeks + theme sort)
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>          # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00     # B10, B80; short: B00
<brutalist>/art run <reel>                    # Manim 4K + gates L/A/W/B, review cut
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape        # runs GATE T: PASS
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical   # runs GATE T: PASS
```

## Gates and fixes (in order)
- Voice gate: approval recorded from Boopesh's 2026-10-24 words ("I approve am_onyx as my narrator voice."),
  subject fingerprint `9fbee75c…c85e` (same as his earlier reels), both sheets.
- Data: last week's "still reproduces" assert failed (27/75/19/95 today vs 26/74/18/95 published) because PR #375
  merged late on Sat Nov 7 after last week's fetch. The script now asserts the published numbers on `a953b021` and
  uses today's recount, shown on screen (B50).
- Pre-checks (fillcheck at 1920×1080 / 1080×1920): landscape B20 strip caption over the right title-safe edge,
  B60 duration lines over the left edge while `Indicate` scaled them, B40 at 54% fill → fixed; then Clean. Short
  Clean first time (after moving B10's card below its header). Small bold text collapsed word spaces → all
  landscape text now set 4× and scaled down.
- B10 hesitant writer: corrected line "The hardest part was checking the result." is on screen by 4.5 s of 7.9 s.
- GATE A: `B20_Themes` raised a TypeError in the static stub (`get_y() - 0.6`) → replaced with `next_to`.
- GATE B (strict): landscape B20 footnote 0.02 below the safe area → rows moved up; 0 errors / 0 warnings.
- GATE T: landscape B40 failed bbox-overlap (the outlined "watch / view / re-read" boxes read as text runs around
  their own words) → boxes are now filled panels; PASS. Short B30 failed min-size (64 px < 72 px: x-height-only
  word runs in the 25 pt card titles) → titles 30 pt (fitted), chip labels 27 pt, "MY OBSTACLE: ACCESS" in caps;
  stale clips deleted so `art run` re-rendered them → PASS.
- Review-cut Gate V: only `edge-bleed` hits on every frame (burned-in review timestamps); the clean finals report
  0 BLOCKER / 0 MAJOR (landscape 18 frames, Short 10 frames).
- Lint notes: "OUTRO LAW wants ClaudeTitleOutro" (both) and "COLD OPEN LAW wants ClaudeComposerAsk" (Short uses the
  916 variant) — kept, as required by the fellow brief.

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/what-got-in-the-way-master.mp4` (verified receipt `…-master.verified.json`) | 3840×2160 | 140.75 s | −24.5 LUFS | 4b3e4d69e9f15268c18986b588d6190984b03d0a5b105ad74987b5ae3312bc4d |
| **delivered** `landscape/WhatGotInTheWay_BoopeshM.mp4` | 3840×2160 | 140.8 s (2:21) | −14.2 LUFS, −0.8 dBTP | 371372ccbf4740c0319acbbb6923aeb8cd3e072fd40752273b98f69082bb2e7e |
| toolkit master `vertical/what-got-in-the-way-short-master.mp4` (verified receipt) | 2160×3840 | 49.25 s | −24.2 LUFS | d0c0db111bdd0b4e61bc7f74505a4bd9e044cef704dad9d4f5c01f14be23f45c |
| **delivered** `vertical/WhatGotInTheWay_BoopeshM.mp4` | 2160×3840 | 49.3 s (0:49) | −14.1 LUFS, −1.0 dBTP | 43c25a19cd76ed650d07d6c94ad94591b876b8f893fa46c3b1fc99ed5511f035 |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC `-b:a 320k`, `+faststart`).
The masters were renamed `<slug>-master.mp4` after verification (the receipts' `output` field still names
the original path; their `sha256` matches the renamed file). Eight frames of each delivery were looked at
(plus end-of-beat frames): no footer text, every beat completes before its cut.
