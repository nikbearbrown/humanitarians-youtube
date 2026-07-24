# BUILD PROMPT — claude-liam-code-walkthrough
# "Claude, Building." | code-walkthrough skill teardown
# Paste into Claude Code (--dangerously-skip-permissions) from books/

## Standalone rebuild prompt

```
You are rebuilding a completed brutalist-art meta-series reel end-to-end.
Work from brutalist-art/youtube/claude-liam-code-walkthrough/.
Read the full beat_sheet.json before touching any file.

PIPELINE (in order):

1. GATE P — verify PEDAGOGY.md ends "VERDICT: PASS". If it doesn't, stop.

2. AUDIO — generate Kokoro audio for all beats with actual_duration_s == 0:
   cd books
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     brutalist-art/youtube/claude-liam-code-walkthrough --no-gate

3. REMOTION SCENES — render all beats with shot.remotion.pattern:
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     brutalist-art/youtube/claude-liam-code-walkthrough

4. COMPILE — assemble to mp4:
   python3 brutalist-art/runtime/scripts/compile.py \
     brutalist-art/youtube/claude-liam-code-walkthrough

5. VISUAL QC — sample frames at 2fps + each beat at ~15/50/85%:
   mkdir -p brutalist-art/youtube/claude-liam-code-walkthrough/_qc/frames
   ffmpeg -i brutalist-art/youtube/claude-liam-code-walkthrough/claude-liam-code-walkthrough.mp4 \
     -vf fps=2 brutalist-art/youtube/claude-liam-code-walkthrough/_qc/frames/%05d.png

6. PROBE + OPEN:
   ffprobe -v quiet -print_format json -show_streams \
     brutalist-art/youtube/claude-liam-code-walkthrough/claude-liam-code-walkthrough.mp4
   open brutalist-art/youtube/claude-liam-code-walkthrough/claude-liam-code-walkthrough.mp4
```
