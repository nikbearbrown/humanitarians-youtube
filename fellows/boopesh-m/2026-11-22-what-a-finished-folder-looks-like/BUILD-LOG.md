# BUILD-LOG — What a Finished Folder Looks Like (built 2026-11-23)

Toolkit: `brutalist.art` @ `a99b5323` (not pulled, not upgraded; Remotion 4.0.535 “BEHIND” notice
ignored as instructed). Manim 0.20.1, Kokoro (kokoro-onnx), Python venv `/opt/brut/bin`.
Data repo: `humanitarians-youtube` main @ `2a32d04e`. Reel: this folder; Short: `short/`.

## 1. Setup after the wipe
`./setup` → audio, captions, Manim, Remotion, slates/compile, fonts ready; Manim LaTeX equation
beats blocked (not used; no formulas in this film).

## 2. Data (executable evidence)
`python3 code/week_stats.py` run twice → identical `results.json`
(`526c49ecc0e03cbac04a242dffdacbdd4a2e73c7c9a66c2299e450772b7df291`) and `run.log`
(`00183c8077c9c4c20d60a522f4cdb031d16d20bcce9ee1f5326e530b7e4b55cf`). Key numbers: 18 merged PRs
(0 squash), 54 new dated work folders, 19 fellows; pieces beat sheet 51 · FRICTIONAL 45 · README 43 ·
FACTCHECK 39 · SHOTLIST 35 · PROMPTS 35 · code 35 · description 12 · PROOF 4; 0 folders with all
nine, 8 with eight (all missing only PROOF). Week before, recounted: 20 · 54 · 18 · 34 (published
19 · 53 · 17 · 32; snapshot before PR #402 reproduces the published numbers exactly).

## 3. Beat sheets and approvals
`make_sheet.py` writes both sheets from `results.json` and asserts the claims (IDs B00…B90 only).
Voice: Kokoro `am_onyx`, `voice_policy: persistent-fellow-selected`; fingerprint
`9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e`. The record first carried
Boopesh’s 2026-10-24 approval (“I approve am_onyx as my narrator voice.”); at 2026-11-23 19:23 UTC
the coordinator replaced it in both sheets with his re-approval for this week (“Yes, approve
am_onyx”), same fingerprint. `make_sheet.py` preserves an existing approvals block and never
rewrites it. `./art approvals … --fingerprints` and the runtime validation pass for both sheets.

## 4. Audio (the clock)
`generate_audio_kokoro.py`, speed 0.94. First pass at speed 1.0 gave 119.2 s (under the 2:00
floor); narration lengthened slightly and slowed to 0.94 → landscape 139.73 s of narration
(render 140.0 s), Short 45.34 s (render 45.46 s; first Short draft 39.8 s was under 0:40 and was extended).

## 5. Gates and what they caught (in order)
| Gate | Result | Fix |
|---|---|---|
| A static pre-flight | `NameError: np` (the checker’s stub manim exports no numpy) | explicit `import numpy as np` |
| fill pre-check 16:9 (fillcheck.sh, 1920×1080) | B60 underfill 52 % at 50 %; B70 edge-bleed right | right-column headings shown from the start; takeaway columns re-spaced, file names 27 pt |
| B layout audit (strict) | B90 text-on-text + safe-area warnings | root cause: `Text(color=…)` inflates bounding boxes and 4×-built long lines are silently wrapped by Pango; colour now set after construction, landscape text built at 2× |
| fill pre-check 9:16 | B20 edge-bleed left (PANEL card 0.08 u outside title-safe) | card moved inside |
| W WCAG / A static / B audit (both reels, all scenes) | clean | — |
| GATE V on review cuts | edge-bleed on every frame (burned-in timecode + beat labels) | expected review-cut false positive; label-free concat re-checked: 16:9 clean; Short B00 composer title overran the right edge → `segment` shortened to “A Finished Folder”, B00 re-rendered, clean |
| T type check | PASS both (16:9 smallest run 42 px vs 41 px floor in B60; Short ≥ 82 px vs 72 px) | — |
| final export (16:9, then Short, one after the other) | both `ready`; final frame check 20/20 and 10/10 frames clean | — |

## 6. Masters and deliveries
| File | Size | Duration | Loudness | SHA-256 |
|---|---|---|---|---|
| `landscape/finished-folder-master.mp4` (+ `.verified.json`) | 3840×2160, 24 fps | 140.000 s | −24.4 LUFS | `f0f52f802f5f197f21a6b89d27c8e864e0b0f0663049a36ad17d7e53ac6d572d` |
| `landscape/FinishedFolder_BoopeshM.mp4` | 3840×2160 | 140.10 s | −14.1 LUFS, TP −0.8 dBTP | `081fdea008a811975bbff48b4f8f283cae8ad69ac4ae4cac7a99d1eac8a44558` |
| `vertical/finished-folder-short-master.mp4` (+ `.verified.json`) | 2160×3840, 24 fps | 45.458 s | −23.7 LUFS | `8af9016b75631c3884107ef9cf71d1c655a11b559356ae5701d60353bcc48d52` |
| `vertical/FinishedFolder_BoopeshM.mp4` | 2160×3840 | 45.50 s | −14.1 LUFS, TP −0.9 dBTP | `b4e732dd0132475f9d369da34de38cfbf0af45d57209eef0f405de2cc6609f4c` |

Delivery copies: video stream copied (stream MD5 identical to the master), audio two-pass
`loudnorm=I=-14:TP=-1:LRA=11:linear=true` (16:9 measured I −24.42, TP −3.10, LRA 5.40, thresh −34.76,
offset 0.76; Short −23.83 / −3.54 / 5.80 / −34.26 / 0.92), AAC 320k, 48 kHz, `+faststart`. ffmpeg
reported `normalization_type: dynamic` for pass 2 (a +10 dB linear gain would exceed the −1 dBTP
ceiling), so the limiter engaged; measured result −14.14 / −14.17 LUFS. Duration +0.04–0.10 s
is AAC priming. Folders under `/home/user/weekly-submission/`; description copied to
`FinishedFolder-description.txt`.

## 7. Looked at
8 evenly spaced frames of each delivery file and the last frame of every beat (16:9: 10, Short: 5):
all text inside the safe area, no overlaps, accent only on the number that matters, one dark beat,
outro complete. Not done: no human listened to the narration in this build (no speech model on the
machine); pronunciation was checked with Kokoro’s phonemizer only.

## 8. Toolkit side effects
The toolkit's own scripts created gitignored files in the checkout (`runtime/remotion/_bench/consumers.json`,
`runtime/remotion/.latest-remotion`, `runtime/scripts/__pycache__/`). `runtime/remotion/package-lock.json`
showed as modified when this build started and shows clean at the end; it was not edited by hand
(most likely rewritten by the toolkit's own `npx` calls, not verified). `git status` of `brutalist.art`
is clean at `a99b5323`; nothing in it was edited.
