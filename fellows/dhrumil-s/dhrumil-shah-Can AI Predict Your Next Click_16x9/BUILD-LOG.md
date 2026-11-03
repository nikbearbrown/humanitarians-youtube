# BUILD-LOG — Can AI Predict Your Next Click (16:9 presenter-intro edition)

| Item | Value |
|---|---|
| Build date | 2026-09-15 (16:9 edition) · 9:16 intro edition 2026-09-14 · source film 2026-09-12 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Script version | v3 — unchanged from the 9:16 intro edition (B00 presenter intro + 16-beat film) |
| Beat sheet | `beat_sheet.json` — 17 beats (B00–B16); metadata updated for 16:9 |
| Derived from | `youtube/mycroft-thesisguard-brief/Can AI Predict Your Next Click` (9:16) |
| Reference format | `youtube/mycroft-thesisguard-brief/Can-AI-discover-new-quantum-materials-16x9` (landscape editorial style, header + scene counter, persistent SOURCE tags, 3840×2160 Remotion master) |

## What was reused unchanged

| Item | Source |
|---|---|
| Data, features, models, evaluation, scored customers | `data/`, `models/`, `evaluation/` — seed 20260912 |
| `video_data.json` (every on-screen number) | `scenes/remotion/data/` |
| Narration (17 Kokoro `af_kore` beats, 376 words, 153.46 s) | `audio/` |
| Captions (98 sentence cues → 83 captions) | `captions/` |
| Music bed, SFX, final mix (−14.1 LUFS, −1.5 dBTP) | `assets/`, `audio/final_mix.wav` |
| Manim reliability diagram | `scenes/renders/B12_calibration.mp4` |

Because the audio did not change, the timeline is identical: 155.96 s (2:36) including the
2.5 s end-card hold. Beat durations (s): B00 10.96 · B01 10.89 · B02 4.10 · B03 8.07 · B04 8.71 ·
B05 11.01 · B06 8.55 · B07 5.99 · B08 9.06 · B09 5.92 · B10 7.52 · B11 9.29 · B12 8.21 · B13 7.82 ·
B14 15.60 · B15 8.76 · B16 12.99

## What was built new

| Item | Value |
|---|---|
| Composition | `CanAIPredictYourNextClick16x9` — `scenes/remotion/CanAIPredictYourNextClick16x9.tsx` |
| Cover | `CPNCCover16x9` — `scenes/remotion/CPNCCover16x9.tsx` |
| Registry | `runtime/remotion/src/Root.tsx`, folder `Can-AI-Predict-Your-Next-Click-16x9` |
| Remotion namespaces | `src/can-ai-predict-next-click-16x9/`, `public-can-ai-predict-next-click-16x9/` (9:16 cuts untouched) |
| Design canvas | 1920 × 1080, native 16:9 (no 9:16 source, no crop) |
| Master method | `--scale=2` → 3840 × 2160, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled from it |
| FPS | 30 |
| Scripts | `scripts/sync_to_remotion.py`, `scripts/render_masters.py` rewritten for 16:9 names, sizes, QC sheet |

## Dataset and model summary (unchanged)

5,000 synthetic customers · 1,217,852 events · 14 model features · logistic regression selected for
click / purchase / churn · test ROC-AUC 0.881 / 0.889 / 0.882 · purchase ECE 0.010 · label-shuffle
ROC-AUC 0.525 ± 0.126 over 20 runs · no PII, no protected attributes.

## QC issues found and fixed (16:9 edition)

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Folder | "Can AI Predict Your Next Click_16x9?" is illegal on Windows (`?`) | Folder named without the "?"; on-screen title keeps it |
| 2 | Layout B00 | Greeting wrapped to three lines ("Dhrumil / Shah.") in the 760 px column | 800 px column, 104 px type — two lines |
| 3 | Layout B07 | "Customer A" broke with a lone "A" on line two | 112 px, `nowrap` |
| 4 | Layout B09 | "Customer B" and "74 days silent" both wrapped | 84 px / 44 px, `nowrap` |
| 5 | Layout B11 | Headline ran to three lines | 700 px column, 58 px type — two lines |
| 6 | Layout B13 | "Campaign caused conversion" and the lift formula wrapped | 52 px equation (`nowrap`), 32 px lift line |
| 7 | Layout B14 | "Einstein Engagement Scoring predicts:" wrapped | 38 px — one line |
| 8 | Cover | "predict you?" wrapped so "you?" sat alone on line three | 136 px, 980 px column, `nowrap` — two lines |
| 9 | Layout B14 | After fix 7, "predicts:" still dropped to a second line | 34 px, `nowrap` |
| 10 | Render | Review cut failed at frame 3023 (0.7 s into B12): compositor "No frame found at position 21000". The clip was byte-identical to the one that rendered the 9:16 masters. First hypothesis — B-frames — was tested with an all-intra re-encode and **did not fix it** (next failure: position 27999) | Hypothesis rejected; see fix 11 |
| 11 | Render | Real cause: Remotion's compositor looks embedded-video frames up by exact timestamp. Frame 28 was requested as 27999 against a stored pts of 28000 (1/30000 timescale), so the lookup missed. The 9:16 render only passed because its requested times happened to align | B12 now shows the Manim diagram as a 1408×1408 PNG sequence selected per frame (`Img`, no decoder, no seek). `scripts/stage_manim_clip.py` writes `scenes/renders/B12_frames/` + `B12_frames.json`; `scripts/sync_to_remotion.py` copies them. The chart pixels are unchanged |
| 12 | Layout B12 | Late-reveal check: CALIBRATION value "55% → 56%" wrapped to two lines | 44 px, `nowrap` |
| 13 | Sync / render | First master attempt: `shutil.rmtree` on the Remotion copy of `B12_frames/` hit `PermissionError` (Windows/OneDrive lock), leaving 36 of 276 frames. A pipe to `tail` hid the failed exit code, so the master started anyway and cancelled after 331 s on 404s for `f_0001.png…` | `sync_to_remotion.py` overwrites in place (`dirs_exist_ok`), deletes only stale frames, and exits if the frame count is short; render chain now runs with `pipefail` and checks for 276 public frames before rendering |

Review cut (960×540) after fix 11: rendered cleanly, 156.01 s, 30 fps. Late-reveal contact sheet
(`_qc/late_sheet.png`, 96% of B00, B01, B05, B06, B07, B08, B11, B12, B14, B15; B16 at 55%; end card):
every late element lands inside its column, captions stay in the bottom band, source tags stay clear.
The only issue found was fix 12.

First 16:9 storyboard pass (all 17 beats at 70% of each beat): every scene compiled and rendered;
captions stayed in the bottom band and the source tag stayed clear in every frame. Fixes 2–7 came
from that pass.

Earlier fixes inherited from the 9:16 builds (label-shuffle repeat, caption balancing, B14 Apple wording,
Manim label and constant-fps staging, NaN export guard) are documented in the 9:16 folder's BUILD-LOG.

## Final render and output probe

4K render time: 678 s (Remotion, `--scale=2`, concurrency 8), followed by Lanczos downscales.
Decode = full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| `output/Can-AI-Predict-Your-Next-Click-4k(16x9)_Dhrumil_Shah.mp4` | 39.4 MB | 3840 × 2160 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-1920x1080(16x9)_Dhrumil_Shah.mp4` | 14.7 MB | 1920 × 1080 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-1280x720(16x9)_Dhrumil_Shah.mp4` | 9.1 MB | 1280 × 720 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-proxy-960x540(16x9)_Dhrumil_Shah.mp4` | 5.4 MB | 960 × 540 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |

The 0.05 s beyond 155.96 s is AAC priming/padding. Runtime and audio match the 9:16 intro cut exactly.

**Visual QC:** `_qc/qc-sheet.png` — 17 stills from the 1920×1080 master at 70% of each beat. All
layout fixes 2–9 and 12 are present in the master; no clipping, collisions, or captions over content.
Native-pixel 4K crop of B12's metric column (`_qc/4k_native_crop_B12.png`) confirms crisp 4K text
and that the calibration row ("55% → 56%") sits on one line. The PNG-sequence reliability diagram is
checked in the QC sheet and review cut; its source frames are 1408 px for a 704 px (×2) display.

**Storyboards:** `storyboard/beat_00.png` … `beat_16.png` (960×540).
**Thumbnails:** `thumbnails/cover_1920x1080.png`, `thumbnails/cover_3840x2160.png`.

## QC summary

| Check | Result |
|---|---|
| Scientific / data / model / probability QC | ✅ unchanged from the 9:16 cut — every on-screen number from `video_data.json` |
| Privacy / fairness QC | ✅ synthetic data only; no protected attributes |
| Visual QC | ✅ after fixes 2–9, 12 |
| Landscape QC — native 16:9, no crop or letterbox | ✅ |
| Audio QC | ✅ identical mix: −14.1 LUFS, −1.5 dBTP (human listening pass still recommended) |
| Caption QC | ✅ bottom band, clear of the player progress bar |
| Render robustness | ✅ after fixes 11 and 13 |
| Fact-check QC | ⏳ FACTCHECK S01 human confirmation; G05 wording decision |
| Pedagogy QC | ⏳ Gate P human sign-off |
| Presenter voice | ⏳ intro says "I am Dhrumil Shah" in `af_kore` (female voice) — presenter decision |

**Publishing: not authorised.**
