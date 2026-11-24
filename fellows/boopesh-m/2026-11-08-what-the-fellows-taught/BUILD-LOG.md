# BUILD-LOG — What the Fellows Taught

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-08 in a Linux cloud container (Python 3.13
venv, Manim 0.20.1, Remotion, Kokoro `am_onyx`), sharing 4 CPUs with another build. Data: `humanitarians-youtube`
`bc722c05..a953b021` (this week) and `c9fca929..bc722c05` (last week, recomputed).

## Commands
```bash
python3 code/week_stats.py                    # -> code/results.json, run.log (both weeks)
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
- GATE F: first `art run` refused before FACTCHECK/SHOTLIST/PROMPTS existed → paperwork written first.
- Pre-checks (fillcheck at 1920×1080 / 1080×1920): B20 legend and B30 labels crossed the title-safe edge → moved;
  dated-strip labels overlapped → restacked. Then Clean.
- B10 hesitant writer: corrected line "This week's new folders were mostly lessons." is on screen by 6.0 s of 8.3 s.
- GATE B (strict): landscape B50 footnote 0.09 below the safe area; Short B10 labels 0.05 left of it → fixed,
  0 errors / 0 warnings.
- GATE T: landscape PASS first time. Short failed min-size on B20/B30/B40 (auto-shrunk card, small labels,
  x-height-only words) and one bbox overlap (dim copy under lit rows) → enlarged type, removed the dim text copy;
  stale filled clips deleted so `art run` re-rendered them → PASS.
- Review-cut Gate V: only `edge-bleed` hits from the burned-in review timestamps; the clean finals report
  0 BLOCKER / 0 MAJOR (landscape 20 frames, Short 12 frames).
- A standalone `type_check.py` run on the landscape was terminated (SIGTERM, empty log, likely CPU contention);
  `art final` ran GATE T itself (TYPECHECK.md: PASS).
- Lint notes: "OUTRO LAW wants ClaudeTitleOutro" (both) and "COLD OPEN LAW wants ClaudeComposerAsk" (Short uses the
  916 variant) — kept, as required by the fellow brief.

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/what-the-fellows-taught-master.mp4` (verified receipt `…-master.verified.json`) | 3840×2160 | 135.4 s | −24.6 LUFS | 2cfbd322b650d2a54279f001ae5c7ae2635253d8902be2f1c58d1c2852bd018c |
| **delivered** `landscape/WhatTheFellowsTaught_BoopeshM.mp4` | 3840×2160 | 135.5 s (2:15) | −14.1 LUFS, −0.9 dBTP | a4330f9c97a218b6b72f7ca860c694338cbf9fdce8fc478fb924884f2c7ded22 |
| toolkit master `vertical/what-the-fellows-taught-short-master.mp4` (verified receipt) | 2160×3840 | 49.8 s | −23.7 LUFS | 5a073933441a991c8b6c0a57d5ef23d8add42c6984ccbeb13e324c65e81a3565 |
| **delivered** `vertical/WhatTheFellowsTaught_BoopeshM.mp4` | 2160×3840 | 49.8 s (0:50) | −14.1 LUFS, −1.0 dBTP | 6690c00e32da881e5980da187fd3c7cfd7ac61bf53ec07f2cb42e157bc727b08 |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC 320k, `+faststart`).
The masters were renamed `<slug>-master.mp4` after verification (the receipts' `output` field still names
the original path; their `sha256` matches the renamed file). Eight frames of each delivery were looked at
(plus end-of-beat frames): no footer text, every beat completes before its cut.
