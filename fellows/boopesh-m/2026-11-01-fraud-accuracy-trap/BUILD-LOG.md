# BUILD-LOG — The 99.9% Accuracy Trap

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-01/02 in a Linux cloud container (Python 3.13 venv,
Manim 0.20.1, Remotion 4.0.535, Kokoro `am_onyx`, scikit-learn 1.9.1 installed from PyPI for the experiment).

## Commands
```bash
cd code && python3 fraud_trap.py > run.log && python3 typeset.py ../assets ../short/assets && cd ..
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>         # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00    # B10 (--force after a prop fix), B80; short: B00
<brutalist>/art run <reel>                # Manim 4K + gates A/W/B, review cut
python3 <brutalist>/runtime/scripts/type_check.py <reel>                    # GATE T: PASS
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical
```
Experiment reproducibility: a second run of `fraud_trap.py` in a scratch folder gave an identical `results.json`
(apart from runtime).

## Gates and fixes (in order)
- Length: first narration measured 160 s (at the 2:40 limit) → trimmed B20/B30/B50/B60 to 142 s.
- B10 hesitant writer: first render never corrected (trigger `"means it works."` with the period never matches a
  token core) → trigger `means it works`, re-rendered with `--force`; corrected line lands at ≈6 s of a 7.5 s beat.
- GATE A (static): the dot grid was built with explicit coordinates down to y = −4.3 before re-centering →
  built with `arrange_in_grid`.
- GATE B (layout, strict): "1 fraud" label touching the red ring (label-on-curve) → label removed, caption under the
  grid says "1 fraud (red)"; three safe-area warnings (B20 caption, B40 rotated row labels, B60 x-axis title) → moved.
- GATE T (type): B40 rotated row labels read as 35 px runs (< 41 px) → removed (the four boxes are self-labelled);
  recall/precision formulas re-typeset with `\dfrac` at full size. Short B20 card titles 56 px x-height (< 72 px) → 30 pt.
- Gate V on the review cuts: only `edge-bleed` BLOCKERs from the burned-in review labels (false positives per the
  brief); the clean finals passed (`art final` exit 0; short `_qc/REPORT.md`: 0 BLOCKER / 0 MAJOR).
- Skin lint (warning only, same as the reference reels): B90 outro is a Manim scene, not `ClaudeTitleOutro`.

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/fraud-accuracy-trap-master.mp4` (verified receipt `fraud-accuracy-trap-master.verified.json`) | 3840×2160 | 142.6 s | −24.7 LUFS | f3e7e5642ed8ac1f9b5ef4152e91911db75a4d685098cc57d75387e5b51e3ebe |
| **delivered** `landscape/FraudAccuracyTrap_BoopeshM.mp4` | 3840×2160 | 142.7 s | −14.1 LUFS, −0.8 dBTP | 4a34fe75a30bcb1cf43f1100d97bcebcd89bb92f5aff2602eda9c58b84b8a278 |
| toolkit master `vertical/fraud-accuracy-trap-short-master.mp4` (verified receipt) | 2160×3840 | 52.7 s | −24.4 LUFS | 6e3e4134f21cd3411df5550fa76f1224a3bb2770d3396000f2f4ad0c7cca012a |
| **delivered** `vertical/FraudAccuracyTrap_BoopeshM.mp4` | 2160×3840 | 52.8 s | −14.2 LUFS, −0.9 dBTP | 56893c18832918756b6f22cab189adbf7a8d4bfe1d3638a8422195226391beb2 |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC 320k, `+faststart`) to YouTube's
reference level. The master was renamed `<slug>-master.mp4` after verification (the receipt's `output` field still
names the original path). Eight frames of each delivery file were looked at.
