# BUILD PROMPT — claude-liam-math-explainer
# "Claude, Derived." | math-explainer skill teardown
# Paste into Claude Code (--dangerously-skip-permissions) from books/

## Standalone rebuild prompt

```
You are rebuilding a completed brutalist-art meta-series reel end-to-end.
Work from brutalist-art/youtube/claude-liam-math-explainer/.
Read the full beat_sheet.json before touching any file.

PIPELINE (in order):

1. GATE P — verify PEDAGOGY.md ends "VERDICT: PASS". If it doesn't, stop.

2. AUDIO — generate Kokoro audio for all beats with actual_duration_s == 0:
   cd books
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     brutalist-art/youtube/claude-liam-math-explainer --no-gate

3. REMOTION SCENES — render all beats with shot.remotion.pattern:
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     brutalist-art/youtube/claude-liam-math-explainer

4. COMPILE — assemble to mp4:
   python3 brutalist-art/runtime/scripts/compile.py \
     brutalist-art/youtube/claude-liam-math-explainer

5. VISUAL QC — sample frames at 2fps + each beat at ~15/50/85%:
   mkdir -p brutalist-art/youtube/claude-liam-math-explainer/_qc/frames
   ffmpeg -i brutalist-art/youtube/claude-liam-math-explainer/claude-liam-math-explainer.mp4 \
     -vf fps=2 brutalist-art/youtube/claude-liam-math-explainer/_qc/frames/%05d.png
   Read each PNG. Audit 9-point rubric. Log defects in _qc/REPORT.md.
   Fix root causes in scene source and re-render until zero BLOCKER/MAJOR.

6. PROBE — verify audio present and duration sane:
   ffprobe -v quiet -print_format json -show_streams \
     brutalist-art/youtube/claude-liam-math-explainer/claude-liam-math-explainer.mp4

7. OPEN — auto-open the final mp4:
   open brutalist-art/youtube/claude-liam-math-explainer/claude-liam-math-explainer.mp4

Report: final duration, beat count, any QC defects fixed.
Never publish — output stays in the reel folder for human review.
```
