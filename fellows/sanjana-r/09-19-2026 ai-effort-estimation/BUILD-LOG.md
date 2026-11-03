# BUILD-LOG — AI Effort Estimation

Reel: `ai-effort-estimation` · channel @HumanitariansAI · narrator Sanjana Rao
Skill: cli-explainer (Claude skin) · voice af_bella (Bella, female) · built 2026-09-19.

## Decisions
- Topic (fellow's choice): **AI effort estimation** via reference-class forecasting
  + velocity calibration (AI + project management). Raw AI/gut guess → honest range.
- Framing: first-person as Sanjana, cold open "Hi, I'm Sanjana … this video is about …".
- Two deliverables: 16:9 4K (3840×2160) long + 9:16 Short (`ai-effort-estimation-short`).
- Output kept local under "Humanitarians AI Brutalist files" — NOT pushed to GitHub (per request).
- Precedent matched: `monte-carlo-schedule-risk` (brand claude-hai, af_bella, @HumanitariansAI,
  first-person greeting "Hi, Sanjana", ClaudeTitleOutro with @HumanitariansAI). That film
  scored 12/12 PASS; its one noted weakness (a numerically subtle effect) is addressed here
  with a large, explicitly-numbered effect (gut 10 → honest P80 ~19).

## Pipeline (Windows — bash wrappers bypassed; scripts called directly)
1. `generate_audio_kokoro.py` → 12 mp3s, af_bella. Durations = master clock.
2. `remotion_scenes.py --now <iso>` → Claude beats (B00,B03,B04,B06,B07,B10,B11) at 4K (--scale=2).
3. `manim -qk -r 3840,2160` → 5 output scenes (B01,B02,B05,B08,B09) → manim/<BID>.mp4.
4. `compile.py --height 2160` → final 16:9 master (skip --review on Windows: drawtext font-path bug).
5. `add_transitions.py` → cross-dissolve-through-cream at every beat boundary → *-fx.mp4.
6. Visual QC (frame sampling) + PROOF self-review → fixes → recompile.
7. 9:16 Short authored + compiled at 2160×3840.

## Honesty / DOUBLE-CHECK
- All on-screen numbers come from the reel's own seed-locked estimator (scenes.py),
  identical to the HISTORY/VELOCITY shown in estimate.py v2 (B07). See SOURCES.md.
- Gut sprint total 10 days; calibrated P80 total ~19 days; per-task 8.0-11.5 / 2.3-2.8 / 3.4-5.1.
- Falsifiability shown on screen (B08): a task with no reference class is flagged to spike,
  not estimated — the method's honest boundary.
- No model version numbers or drifting counts on screen (won't date the video).

## GATE N (Professor Bear's notes)
- N/A — self-authored cli-explainer, not a fellow-report wrap; no Bear-notes beat to sign.
