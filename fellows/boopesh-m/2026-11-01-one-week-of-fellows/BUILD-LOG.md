# BUILD-LOG — One Week of Fellows

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-01/02 in a Linux cloud container (Python 3.13
venv, Manim 0.20.1, Remotion 4.0.535, Kokoro `am_onyx`). Data: `humanitarians-youtube` `c9fca929..bc722c05`.

## Commands
```bash
python3 code/week_stats.py                    # -> code/results.json, run.log
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>          # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00     # B10, B80; short: B00
<brutalist>/art run <reel>                    # Manim 4K + gates L/A/W/B, review cut
python3 <brutalist>/runtime/scripts/type_check.py <reel>                     # GATE T: PASS (both)
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical
```

## Gates and fixes (in order)
- Voice gate: approval recorded from Boopesh's 2026-10-24 words ("I approve am_onyx as my narrator voice."),
  subject fingerprint `9fbee75c…c85e` (same as his earlier reels).
- B10 hesitant writer first rendered without its correction (trigger words ended in a period) → fixed; the
  Remotion stamp then restored the old props once, so the beat was re-rendered with a cleared stamp; last frame
  checked ("A week of work is a folder of small evidence.").
- Pre-checks (fillcheck at 1920×1080 / 1080×1920) → Clean after layout fixes (bars/day labels, label overflow,
  title cards); Short B30 contrast flag → dark mat, later replaced by plain cards.
- GATE T: landscape B50 (fit-scaled titles, 38 px < 41 px) → long titles wrap onto two lines; Short B30 (tiny text
  inside screenshots, then serif x-height 68 px < 72 px) → native cards with sans titles. Both PASS.
- GATE B layout audit: 0 errors, 0 warnings (both). GATE W: clean.
- Review-cut Gate V: only `edge-bleed` hits from the burned-in review labels; the clean finals report 0 BLOCKER / 0 MAJOR.
- Lint note: "OUTRO LAW wants ClaudeTitleOutro" — kept the Manim HAI outro required by the fellow brief.

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/one-week-of-fellows-master.mp4` (verified receipt) | 3840×2160 | 144.46 s | −24.7 LUFS | 77457fd99f695e73f99f64b57de7f7b76f16940545e9cac87d6d09cd1a9815c3 |
| **delivered** `landscape/OneWeekOfFellows_BoopeshM.mp4` | 3840×2160 | 144.5 s | −14.1 LUFS, −0.9 dBTP | 6d542b29610e6ecbc86219d0ffc35c8d5fe6bb9114a04dc76dde56914bcf243b |
| toolkit master `vertical/one-week-of-fellows-short-master.mp4` (verified receipt) | 2160×3840 | 47.46 s | −23.9 LUFS | 76bb6736f0eec260fc02a3e0094f2ddb103a9d757d7796627134a09545501a24 |
| **delivered** `vertical/OneWeekOfFellows_BoopeshM.mp4` | 2160×3840 | 47.5 s | −14.3 LUFS, −1.0 dBTP | 357bf5ed9dbd3ff86969d789c6536accb7a394c5edc1421582a7c6c511ab70d2 |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC 320k, `+faststart`).
Eight frames of each delivery were looked at (plus end-of-beat frames): no footer text, all beats complete.
