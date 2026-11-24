# BUILD-LOG — How an AI Sells a Big Order (2026-11-22 week, built 2026-11-23)

Toolkit: /home/user/nikbearbrown/brutalist.art @ a99b5323 (not modified, not updated).
Env: /opt/brut/bin (Python 3.13.18, numpy 2.5.5, Manim 0.20.1). The CPUs were shared with another builder.

## Done
1. **Sources.** Almgren & Chriss author PDF (Dec 2000) fetched from a GitHub mirror and read
   (§1.1–2.3). Nevmyvaka, Feng & Kearns (ICML 2006) not reachable, so it is cited only (⚠️ FACTCHECK).
2. **Evidence.** `code/execution_rl.py` (numpy only, seed-locked) writes `code/results.json`
   and `code/run.log`. It was run twice and both outputs were byte-identical:
   results.json sha256 `adcb0c64a75b4be203906d5f6367dbad76f9d12b0f0c3321ab00b291031ac9b6`,
   run.log sha256 `8dd1fdcdf53287489d0aa622f5b0c146151e0d96d09353827e6c67c6029f01c6` (`code/determinism.txt`).
   Headline: dump 100 bps · TWAP 9.89 (std 33.7, p95 65.4) · agent 13.31 (std 24.5, p95 53.6) ·
   AC 13.19 (std 24.1, p95 52.7). Objective (cost + λ·var): agent 22.424 vs AC 22.053 (+1.68%).
   Iterations before this (all logged in FACTCHECK "Honest notes"):
   - v1 plain Q-learning: agent held 3,250 shares to the last step (+47%).
   - v2 vectorized, exploring starts: +94%. Bug found: the last-step value was read from untrained actions.
   - v3 bug fixed: +21%.
   - v4 double Q-learning: +7.7%.
   - Parameter/length scan, then final at 40M runs: +1.7%.
3. **Beat sheets** from `make_sheet.py`. Every spoken number is asserted against results.json.
   Approvals and audio measurements are preserved on re-run. 16:9: 10 beats (B00 … B90), 423 words.
   Short: 6 beats, 135 words.
4. **Assets.** `assets/hai-logo-1-ink.png` was rasterized from logos/humanitarians/humanitarians-logo-1.svg
   by `code/hai_logo_png.py` (pycairo, unchanged paths; ImageMagick's SVG delegate is broken here).
   `assets/ac-formula-ink.svg` comes from `code/make_formula.py` (toolkit typeset_math.py). Both are copied to short/assets/.
5. **Scenes.** `scenes.py` (7 Manim scenes) and `short/scenes.py` (5 portrait scenes) were pre-checked
   with the run.sh gates run standalone:
   - Gate A (static_scene_check): all clean.
   - Gate W (wcag_margin_check): all clean.
   - Gate B (manim_layout_audit --curve-strict, plus --portrait for the Short): all clean.
   - fillcheck.sh (final_frame_check at 50%/85%; 1920×1080 and 1080×1920 drafts): "Clean".
   - Preview stills inspected by eye.
   Fixes along the way: edge-bleed on B40, B50, B70 and B90; a header collision on B30/B60;
   label-on-line in B30; Short type too wide (Gate B errors on 5/5 scenes); Short B20 underfill
   (ghost outlines added).
6. **Paperwork.** FACTCHECK, SHOTLIST, PROMPTS (16:9 + short/), README, short/README, PROOF,
   FRICTIONAL, description.txt (chapters from render_duration_s), short/description.txt.
7. The row was appended to `fellows/boopesh-m/README.md`.

## Blocked, then resumed
At first, recording `metadata.approvals.voice` was refused by the session's permission check
(an agent writing a human sign-off). The build stopped before audio, as the brief asks.
Boopesh then approved am_onyx himself in chat on 2026-11-23 ("Yes, approve am_onyx"), and the
coordinator recorded it in both sheets (subject_sha256 9fbee75c…). `./art approvals` exited 0. The
approvals block was not edited by this builder; `make_sheet.py` preserves it.

## Render (2026-11-23, shared CPUs, load up to ~12)
1. **Audio** with `generate_audio_kokoro.py`: 16:9 is **132.71 s** of narration (2:12.7, inside 2:00–2:40, so no
   trim was needed); the Short is **46.12 s**. `make_sheet.py` was re-run so the Remotion props carry the measured durations.
2. **Remotion**, one beat per call: B00, B10 and B80 (16:9), and short B00 (ClaudeComposerAsk916).
   - The B10 last frame shows the corrected line fully landed: "Sell a big order in slices."
   - B10 was re-rendered once: a card detail wrapped with an orphan word, so it was shortened to "learns the size of each slice".
   - `remotion_scenes.py` also updates the git-ignored `runtime/remotion/_bench/consumers.json` in the toolkit.
     `git status` there stays clean.
3. **`./art run`** (16:9 and Short): Gates L, A, W and B passed on every scene. The review-cut Gate V
   BLOCKERs are all `edge-bleed` from the burned-in review labels, a known false positive.
4. **GATE T (`type_check.py`)**: the Short passed first time. The 16:9 failed twice on B40 (§8.1, a 40 px
   "text run"):
   - first the "→" glyph in "10 → 1", replaced with "10 down to 1";
   - then the rotated "shares left" axis label, whose sideways letters measured 40 px; it became a horizontal label.
   After that: PASS.
5. **4K text-wrap defect found by looking at frames.** The layout audit renders at 854 px and wrote *wrapped*
   SVGs into the reel's Manim text cache (`media/texts`). The 4K renders then reused them, so three long lines
   wrapped (B60 caption, B70 read-more line, B90 data line). The first 16:9 `art final` was stopped before
   encoding. Fixes: the three lines were shortened (they now fit at every resolution, checked), the text caches
   were cleared, and B60, B70 and B90 re-rendered. Short B20 had an overlap ("equal slices" over
   "price can drift"); it was re-laid out and re-rendered.
6. **`./art final`** for the 16:9, then for the Short, one after the other. Both exited 0 (GATE T, then
   final_frame_check). The masters were renamed to `<slug>-master.mp4` together with their `.verified.json`.
7. **Delivery**: video stream copied, two-pass loudnorm (I −14, TP −1, LRA 11, linear=true), AAC 320k, faststart.
   | | master in | delivery out |
   |---|---|---|
   | 16:9 | −24.70 LUFS, TP −3.80 | **−14.1 LUFS**, TP −1.0 (ebur128 check) |
   | Short | −23.89 LUFS, TP −5.76 | **−14.1 LUFS**, TP −1.0 (ebur128 check) |
   ffmpeg reported `normalization_type: dynamic` for both: linear gain of about +10 dB would have broken TP −1.
8. **Looked at** 8 evenly spaced frames and the last frame of every beat, in both delivery files. No clipping,
   overlap or wrap remained.
9. **Durations**: 16:9 master 132.92 s, delivery 133.00 s. Short master 46.25 s, delivery 46.30 s. All are under 180 s.

## Hashes
| File | SHA-256 |
|---|---|
| code/results.json | adcb0c64a75b4be203906d5f6367dbad76f9d12b0f0c3321ab00b291031ac9b6 |
| code/run.log | 8dd1fdcdf53287489d0aa622f5b0c146151e0d96d09353827e6c67c6029f01c6 |
| landscape/ai-sells-a-big-order-master.mp4 | ddd243f334269ecc87008d039debaa6cc26574a5a160cec77d8dc9fa3171ceac |
| landscape/AISellsABigOrder_BoopeshM.mp4 | 87a45baa0dd5633cbb7c88fd4e935e8acc668590e3af1f77553b5fdf7a3a2cec |
| vertical/ai-sells-a-big-order-short-master.mp4 | cf0282bb3456f946b6926a438aa30ad2bde6e28ff127a829f611fcae7af78652 |
| vertical/AISellsABigOrder_BoopeshM.mp4 | 78e15fd0e6cb7a4e24726fa66c13dbd60becb661322a027bc9d29e7c4e3e9a44 |

Skin-lint notes (informational, not gates): the Short's B00 uses ClaudeComposerAsk916, the portrait composer the
brief asks for. B90 is a Manim outro, not ClaudeTitleOutro, as the brief asks (that one hardcodes @NikBearBrown).
