# BUILD-LOG — Monte Carlo Schedule Risk

Reel: `monte-carlo-schedule-risk` · channel @HumanitariansAI · narrator Sanjana Rao
Skill: cli-explainer (Claude skin) · voice af_bella (Bella) · built 2026-09-02.

## Decisions
- Topic chosen by the creator: **Monte Carlo schedule risk** (AI + project management).
- Framing: first-person as Sanjana, cold open "Hi, I'm Sanjana … this video is about …".
- Two deliverables: 16:9 4K (3840×2160) long + 9:16 Short.
- Output kept local under "Humanitarians AI Brutalist files" — NOT pushed to GitHub (per request).

## Pipeline (Windows — bash wrappers bypassed; scripts called directly)
1. `generate_audio_kokoro.py` → 12 mp3s, af_bella, total ≈ 4:52. Durations = master clock.
2. `remotion_scenes.py` → 7 Claude beats (B00,B03,B04,B06,B07,B10,B11) at 4K, extended to audio length.
3. `manim -qk -r 3840,2160` → 5 output scenes (B01,B02,B05,B08,B09) → manim/<BID>.mp4.
4. `compile.py --height 2160` → review + final 16:9 master.
5. Visual QC + PROOF self-review → fixes → recompile.
6. 9:16 Short authored + compiled at 2160×3840.

## Toolkit change (Windows compat)
- `runtime/scripts/remotion_scenes.py`: `npx` resolved via `shutil.which("npx")` so
  subprocess (no shell) finds `npx.cmd` on Windows. Necessary for any render.

## Honesty / DOUBLE-CHECK
- All on-screen numbers come from the reel's own seed-locked simulator (scenes.py).
- Plan (sum of most-likely, v1 chain) = 19 days. v1 P80 ≈ 29.3; v2 (parallel merge)
  P80 ≈ 29.8 — v2 legitimately later + wider (merge bias), verified numerically.
- No model version numbers or drifting counts on screen (won't date the video).

## GATE N (Professor Bear's notes)
- N/A for this reel — it is a self-authored cli-explainer, not a fellow-report wrap,
  so there is no Bear-notes beat to sign.
