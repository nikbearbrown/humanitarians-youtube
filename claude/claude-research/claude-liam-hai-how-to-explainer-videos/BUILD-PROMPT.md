# BUILD-PROMPT.md — claude-liam-hai-how-to-explainer-videos

Paste-ready Claude Code prompt to build the final cut end to end.
Run from `books/` under `caffeinate claude --dangerously-skip-permissions`.

```
Build the claude-liam-hai-how-to-explainer-videos reel to final cut.

Reel folder: brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos/

Steps:
1. Generate Kokoro audio (free, no spend): 
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos --no-gate

2. Render all Remotion scenes:
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos

3. Compile at 1920x1080:
   python3 brutalist-art/runtime/scripts/compile.py \
     brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos --height 1080

4. Visual QC (MANDATORY — sample frames and audit 8-point rubric):
   mkdir -p brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos/_qc/frames
   ffmpeg -i brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos/claude-liam-hai-how-to-explainer-videos.mp4 \
     -vf fps=2 brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos/_qc/frames/%05d.png -y
   Read key frames (B00@5s, B01@mid, B02@mid, B03@mid, B04@mid, B05@mid, B06@mid, B07@mid, B08@mid, B09@mid).
   Audit: edge bleed, title-safe margins, overflow, collision, legibility, brand bug, aspect.
   Log defects in _qc/REPORT.md. Fix root causes, re-render, recompile until zero BLOCKER/MAJOR.

5. Probe final mp4:
   ffprobe -v quiet -show_streams -show_format \
     brutalist-art/youtube/claude-liam-hai-how-to-explainer-videos/claude-liam-hai-how-to-explainer-videos.mp4 \
     | grep -E "width|height|duration|nb_frames"
   Verify: 1920x1080, ~145s, all frames present.

6. Report the beat→timestamp table and confirm done.

Do NOT publish. Output stays in the reel folder for human review.
```

## Custom Remotion scenes (registered in runtime/remotion/src/Root.tsx)

| Scene ID | File | Beat |
|---|---|---|
| HaiExplainerFig1Pipeline | scenes/HaiExplainerFig1Pipeline.tsx | B01 |
| HaiExplainerFig2Folder | scenes/HaiExplainerFig2Folder.tsx | B02 |
| HaiExplainerFig3Command | scenes/HaiExplainerFig3Command.tsx | B03 |
| HaiExplainerFig4Prompt | scenes/HaiExplainerFig4Prompt.tsx | B04 |
| HaiExplainerFig5Revise | scenes/HaiExplainerFig5Revise.tsx | B05 |
| HaiExplainerFig6Publish | scenes/HaiExplainerFig6Publish.tsx | B06 |
