# BUILD-PROMPT — claude-hai-rag-pipelines

Paste into Claude Code from the toolkit root:

> In this folder, rebuild youtube/brutalist/claude-hai-rag-pipelines as review cuts only (never publish).
> 1. Gate check: FACTCHECK.md, SHOTLIST.md, PROMPTS.md present; `./art scenes --check RagRetrieve` and `RagRetrieve916` RENDERABLE.
> 2. Audio: `.venv/bin/python runtime/scripts/generate_audio_kokoro.py youtube/brutalist/claude-hai-rag-pipelines --speed 1.1`, then set every beat's props.durationSeconds = actual_duration_s (both sheets).
> 3. 16:9: `./art run youtube/brutalist/claude-hai-rag-pipelines` (renders Remotion, compiles at 3840×2160, GATE V).
> 4. 9:16: `./art vertical youtube/brutalist/claude-hai-rag-pipelines`, re-apply the portrait B01/B11 props from BUILD-LOG.md, `runtime/scripts/remotion_scenes.py <reel>/vertical --force`, `runtime/scripts/compile.py <reel>/vertical --review --height 3840`.
> 5. Visual QC: sample each beat at 15/50/85%, Read the PNGs, fix scene source in runtime/remotion/src/RagPipeline.tsx until 0 BLOCKER / 0 MAJOR; log in _qc/REPORT.md and BUILD-LOG.md. Report durations and gate results.
