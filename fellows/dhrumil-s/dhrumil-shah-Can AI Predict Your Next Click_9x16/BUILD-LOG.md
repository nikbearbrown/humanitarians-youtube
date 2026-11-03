# BUILD-LOG — Can AI Predict Your Next Click (presenter-intro edition)

| Item | Value |
|---|---|
| Build date | 2026-09-14 (intro edition) · source film built 2026-09-12 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Script version | v3 — v2 film + B00 presenter intro ("Hi, I am Dhrumil Shah, and this video is about…") |
| Beat sheet | `beat_sheet.json` — 17 beats (B00–B16) |
| Reference format | `youtube/mycroft-thesisguard-brief/Can-AI-discover-new-quantum-materials-9x16` (cream/ink/terracotta editorial style, header + scene counter, persistent SOURCE tags, vertical stacks, Remotion master) |

## Dataset

| Item | Value |
|---|---|
| Brand | BrewBox — fictional online coffee shop |
| Seed | 20260912 |
| Customers | 5,000 |
| Simulated days | 240 (2026-01-05 → 2026-08-31) |
| Event rows | 1,217,852 |
| Features per model | 14 (+1 excluded diagnostic: `email_opens_30d`) |
| Prediction dates | 2026-03-21, 04-05, 04-20 (train) · 05-20 (validate) · 07-04 (test) |
| Feature rows | 25,000 (15,000 train · 5,000 validate · 5,000 test) |
| PII | none — synthetic IDs only |

## Models

| Target | Algorithms evaluated | Validation log loss (LR / HGB) | Selected | Test ROC-AUC | Test PR-AUC (base) | Brier | ECE |
|---|---|---|---|---:|---:|---:|---:|
| click_next_7d | Logistic regression, HistGradientBoosting | 0.3924 / 0.3970 | Logistic regression | 0.881 | 0.760 (0.292) | 0.125 | 0.020 |
| convert_next_7d | same | 0.2348 / 0.2428 | Logistic regression | 0.889 | 0.576 (0.116) | 0.070 | 0.010 |
| churn_next_30d | same | 0.3707 / 0.3739 | Logistic regression | 0.882 | 0.674 (0.244) | 0.116 | 0.019 |

Selection rule: lowest validation log loss; logistic baseline kept if within 1%.

**Leakage checks** (`evaluation/leakage_checks.json`): label windows close before later
prediction dates ✅ · targets/IDs/opens excluded ✅ · feature code sees history slice only ✅ ·
label-shuffle ROC-AUC 0.525 ± 0.126 over 20 runs (real 0.889) ✅.

**Fairness / subgroup QC:** no demographic or protected attributes exist. Audit by the only
subgroup available (simulated pre-fetch mail client): click-model ROC-AUC 0.885 vs 0.877;
mean predicted vs observed within 1 pp in both groups. Opens differ 8.4 vs 3.4 while clicks are
1.9 vs 1.8 — the reason opens are excluded. Segment actions are tests with consent and human
review; no pricing differentiation.

## Narration and audio

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M (kokoro-onnx 0.6.1) · `af_kore` · speed 1.0 · 24 kHz |
| Words | 376 (348 source + 28 intro) |
| Narration duration | 153.46 s (measured) |
| End-card hold | 2.50 s |
| Video duration | 155.96 s (2:36) — target 2:20–2:50 ✅ · hard max 2:59 ✅ |
| Speech stretching | none (v1 draft at 476 words was rewritten, not sped up) |
| Music / SFX | code-synthesised; 42 SFX cues; music side-chain ducked under narration |
| Final mix | −14.1 LUFS integrated · −1.5 dBTP · LRA 2.8 LU · 48 kHz stereo |

Measured beat durations (s): B00 10.96 · B01 10.89 · B02 4.10 · B03 8.07 · B04 8.71 · B05 11.01 · B06 8.55 · B07 5.99 · B08 9.06 · B09 5.92 · B10 7.52 · B11 9.29 · B12 8.21 · B13 7.82 · B14 15.60 · B15 8.76 · B16 12.99

## Captions

`captions/VALIDATION.md`: 98 measured sentence cues → 83 captions · 0 overlaps ·
shortest 0.92 s · longest wrapped line 25 characters · 0 single-word captions ·
burned in at y 1372–1540 (design px), above the platform UI band.

## Video

| Item | Value |
|---|---|
| Renderer | Remotion 4.0.486 (bundled Chrome Headless Shell), composition `CanAIPredictYourNextClick9x16` (registered in `runtime/remotion/src/Root.tsx`, folder Can-AI-Predict-Your-Next-Click) |
| Design canvas | 1080 × 1920, native 9:16 (no 16:9 source, no crop) |
| FPS | 30 |
| Master method | `--scale=2` → 2160 × 3840, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled from it |
| Manim | `B12_calibration` 1728 × 1728, re-encoded to constant 30 fps |
| Beats / scenes | 17 |

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Evaluation | Single label-shuffle test gave AUC 0.55 (random coefficients can align with real signal) | Repeat 20× and report mean ± sd |
| 2 | Captions | Sentence split left a dangling "customers." merged into the next sentence | Rebuild sentences, balanced re-split; 0 single-word captions |
| 3 | Fact-check | "Apple Mail can load emails automatically" overstated Apple's documentation | Rewritten to "download email images in the background"; audio, captions, music, mix regenerated |
| 4 | Manim | "perfect calibration" label overlapped the model line | Moved below the diagonal |
| 5 | Render | `video_data.json` contained `NaN` (unsubscribed customers have no click score) → bundle failed | Plot only customers with both scores; `allow_nan=False` guard |
| 6 | Layout B01 | Third hook card collided with SOURCE tag and caption | 12-row grid, compact cards; invalid highlight index corrected |
| 7 | Layout B10 | Headline wrapped into the scatter plot | 48 px single-line headline; plot moved down |
| 8 | Layout B12 | Metric chips overlapped the Manim card and SOURCE tag | Clip 760 px; chips repositioned |
| 9 | Layout B13 | Lift line wrapped, crowding SOURCE tag | 34 px |
| 10 | Animation B09 | Churn ring filled too slowly for a 5.9 s beat | 12-frame ramp |
| 11 | Cover | Silhouette read as a floating head over a dome | Proportions tightened |
| 12 | Render | Compositor "No frame found" at 6.37 s in the Manim clip (irregular timestamps) | `scripts/stage_manim_clip.py` constant-fps re-encode with 1 s tail |

Review cut (540×960) rendered cleanly after fix 12: 145.05 s, 30 fps. Late-reveal contact sheet
(`_qc/late_sheet.png`) checked at 96% of each late-reveal beat and on the end card: no clipping,
overlaps, or safe-area violations.

| 13 | Intro edition | Folder name "Can AI Predict Your Next Click?" is illegal on Windows (`?`) | Folder named without the "?"; title keeps it |
| 14 | Intro edition | Kokoro pronunciation of "Dhrumil" | Phonemised as /dɹˈuːmɪl/ (DROO-mil) — correct, no respelling needed |
| 15 | Intro edition | Intro frames at 2.0 s, 8.3 s, 10.3 s | Greeting, summary card, chips, pipeline preview all clear of caption band ✅ |

## Final render and output probe

4K render time: 691 s (Remotion, concurrency 8), followed by Lanczos downscales.
Decode = full `ffmpeg -f null` pass with no errors. Source: `_qc/OUTPUT-PROBE.md`.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| `output/Can-AI-Predict-Your-Next-Click-4k(9x16)_Dhrumil_Shah.mp4` | 38.6 MB | 2160 × 3840 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-1080x1920(9x16)_Dhrumil_Shah.mp4` | 14.3 MB | 1080 × 1920 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-720x1280(9x16)_Dhrumil_Shah.mp4` | 9.2 MB | 720 × 1280 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |
| `output/Can-AI-Predict-Your-Next-Click-proxy-540x960(9x16)_Dhrumil_Shah.mp4` | 5.3 MB | 540 × 960 | 30 | 156.01 s | H.264 | AAC 48 kHz | PASS |

The 0.05 s beyond 155.96 s is AAC priming/padding.

**Visual QC:** `_qc/qc-sheet.png` (17 stills from the 1080×1920 master at 70% of each beat) —
B00 intro renders as approved; B01–B16 match the source film with counters now reading "/ 17";
no clipping, collisions, or captions in the platform UI band.

**Storyboards:** `storyboard/beat_00.png` … `beat_16.png`. **Thumbnails:** `thumbnails/cover_1080x1920.png`, `cover_2160x3840.png`.

## QC summary

| Check | Result |
|---|---|
| Scientific QC — no unsupported ML claims | ✅ see FACTCHECK (G05 wording flagged for reviewer) |
| Data QC — no leakage, no PII, no future info in features | ✅ |
| Model QC — held-out later-date evaluation, meaningful metrics | ✅ |
| Probability QC — no fabricated probabilities | ✅ every on-screen number from `video_data.json` |
| Privacy QC — synthetic data only | ✅ |
| Fairness QC — subgroup audit, no protected attributes | ✅ (limited: simulation-only subgroup) |
| Visual QC | ✅ after fixes 6–11 |
| Vertical QC — native 9:16 | ✅ |
| Audio QC — clear narration, music subordinate | ✅ −14.1 LUFS, side-chain ducking (human listening pass still recommended) |
| Caption QC | ✅ |
| Safe-area QC | ✅ |
| Fact-check QC — current product claims | ⏳ S01 human confirmation |
| Pedagogy QC | ⏳ Gate P human sign-off |
| Originality QC | ✅ new topic, data, scenes; shares only the house visual language with the reference |

**Publishing: not authorised.** Open items: FACTCHECK S01, G05; PEDAGOGY Gate P (including intro-length retention check).
