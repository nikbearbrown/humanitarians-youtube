# BUILD-LOG — The Backtest Mirage

Brutalist toolkit `a99b5323` (main, not upgraded), built 2026-11-08 in a Linux cloud container (Python 3.13 venv,
numpy 2.5.4, Manim 0.20.1, Remotion 4.0.535, Kokoro `am_onyx`). Another builder shared the 4 CPUs.

## Commands
```bash
cd code && python3 backtest_mirage.py > run.log && python3 typeset.py ../assets && cd ..   # 54 s
python3 make_sheet.py && (cd short && python3 make_sheet.py)
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <reel>         # and <reel>/short
python3 <brutalist>/runtime/scripts/remotion_scenes.py <reel> --only B00    # B10 (--force after a prop fix), B80; short: B00
<brutalist>/art run <reel>                # Manim 4K + gates A/W/B, review cut
python3 <brutalist>/runtime/scripts/type_check.py <reel>                    # GATE T: PASS
<brutalist>/art final <reel> --height 2160 --out weekly-submission/landscape
<brutalist>/art final <reel>/short --height 3840 --out weekly-submission/vertical
```
Experiment reproducibility: a second run of `backtest_mirage.py` in a scratch folder gave an identical
`results.json` (apart from `runtime_s`), an identical `run.log` and identical arrays in `curves.npz`.

## Gates and fixes (in order)
- Length: narration measured 144.0 s landscape / 45.2 s Short (inside 2:00–2:40 and 0:40–0:60); the Short's B30
  got one extra sentence so it would not sit at the 40 s floor.
- B10 hesitant writer: first correction "is the luckiest of 10,000 tries" stopped at "10." (the comma in "10,000"
  ended the replacement) → "is just the luckiest try", re-rendered with `--force`; corrected line lands at ≈4.5 s of
  a 7.5 s beat.
- Preview frames: small text lost its spaces ("randomnoise") → text built 3× larger and scaled down; B40 y-axis title
  collided with tick labels; B50 value labels crossed ghost outlines; B60 paper card touched the title; B70 winner
  label ran into a bar; Short B10 "1 = good" label sat on a ghost frame → all moved.
- Narration: B40 "turns down" → "stalls, then slips" (the winner's out-of-sample line first rises, then falls).
- GATE A (static): `slant=ITALIC` constant unknown to the checker stub → `slant="ITALIC"`.
- GATE B (layout, strict): B30 "…on pure noise" below the safe area → moved up; B40 "2 years · locked" wider than
  its panel (label on a curve) → "locked", and "+100%" left of the safe area → chart shifted right.
- GATE T (type): PASS on both reels first time.
- Gate V on the review cuts: only `edge-bleed` BLOCKERs from the burned-in review labels (false positives per the
  brief); the clean finals passed (`art final` exit 0; `_qc/REPORT.md` 0 BLOCKER / 0 MAJOR for both).
- Skin lint (warning only, same as the reference reels): B90 outro is a Manim scene, not `ClaudeTitleOutro`; Short
  B00 uses `ClaudeComposerAsk916` (the portrait composer).

## Exports
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| toolkit master `landscape/backtest-mirage-master.mp4` (verified receipt `backtest-mirage-master.verified.json`) | 3840×2160 | 144.25 s | −24.7 LUFS | 2463630b5562a284ead4f742de354047a666c5911bb4c3c58ccc5e81eb97f0f0 |
| **delivered** `landscape/BacktestMirage_BoopeshM.mp4` | 3840×2160 | 144.3 s | −14.2 LUFS, −0.95 dBTP | 3ae8c51555e605794f6851226d0dd205f8a4352b2c67bb1ef19eee6ef55661fa |
| toolkit master `vertical/backtest-mirage-short-master.mp4` (verified receipt) | 2160×3840 | 45.29 s | −24.3 LUFS | f3c8f2717d7a140756fc53fdcadcb25c9cb62220608581c905f138561be47667 |
| **delivered** `vertical/BacktestMirage_BoopeshM.mp4` | 2160×3840 | 45.4 s | −14.3 LUFS, −0.99 dBTP | 97134de6416ca71e1d42ab92e5ea6a94f6c845117034c433087efbb0d221980b |

Delivered files = verified masters with the video stream copied bit-for-bit and only the audio
loudness-normalised (two-pass ffmpeg `loudnorm`, I=−14, TP=−1, LRA=11, linear; AAC 320k, `+faststart`) to YouTube's
reference level. The master was renamed `<slug>-master.mp4` after verification (the receipt's `output` field still
names the original path). Eight frames of each delivery file were looked at.
