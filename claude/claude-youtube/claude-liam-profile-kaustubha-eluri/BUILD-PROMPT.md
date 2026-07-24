# BUILD-PROMPT.md — claude-liam-profile-kaustubha-eluri

Paste-ready Claude Code prompt to rebuild the final cut end to end.
Run from `books/` under `caffeinate claude --dangerously-skip-permissions`.

```
Build the claude-liam-profile-kaustubha-eluri reel to final cut.

Reel folder: humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/

Steps:
1. Generate Kokoro audio (free, no spend):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri --no-gate

2. Render all Remotion scenes:
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri

3. Compile at 1920x1080:
   python3 brutalist-art/runtime/scripts/compile.py \
     humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri --height 1080

4. Visual QC (MANDATORY — sample frames and audit 8-point rubric):
   mkdir -p humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/_qc/frames
   ffmpeg -i humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/claude-liam-profile-kaustubha-eluri.mp4 \
     -vf fps=2 humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/_qc/frames/%05d.png -y
   Read key frames. Audit: edge bleed, title-safe, overflow, collision, legibility, brand bug, aspect.
   Log defects in _qc/REPORT.md. Fix root causes, re-render, recompile until zero BLOCKER/MAJOR.

5. Probe final mp4:
   ffprobe -v quiet -show_streams -show_format \
     humanitarians_html/youtube/claude-liam-profile-kaustubha-eluri/claude-liam-profile-kaustubha-eluri.mp4 \
     | grep -E "width|height|duration|nb_frames"
   Verify: 1920x1080, ~202s, all frames present.

6. Report the beat→timestamp table and confirm done.

Do NOT publish. Output stays in the reel folder for human review.
```

## Custom Remotion scenes (registered in runtime/remotion/src/Root.tsx)

| Scene ID | File | Beat |
|---|---|---|
| ProfileKaustubhaFig1Gap | scenes/ProfileKaustubhaFig1Gap.tsx | B01 |
| ProfileKaustubhaFig2ModelSystem | scenes/ProfileKaustubhaFig2ModelSystem.tsx | B02 |
| ProfileKaustubhaFig3Projects | scenes/ProfileKaustubhaFig3Projects.tsx | B03 |
| ProfileKaustubhaFig4Resilience | scenes/ProfileKaustubhaFig4Resilience.tsx | B04 |
| ProfileKaustubhaFig5CitedUsed | scenes/ProfileKaustubhaFig5CitedUsed.tsx | B05 |
| ProfileKaustubhaCredit | scenes/ProfileKaustubhaCredit.tsx | B06 |
