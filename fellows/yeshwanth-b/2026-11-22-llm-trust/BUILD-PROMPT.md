# BUILD-PROMPT — claude-hai-llm-trust

Paste into Claude Code from the `brutalist.art` toolkit root. Free pipeline; no paid calls; never publishes.

```text
Build the reel at ~/Documents/AI_Content_submission/youtube/claude-hai-llm-trust end to end:
1. Requirements: runtime/remotion/src/scenes/TrustLLM.tsx is registered in Root.tsx (9 compositions × 16:9 and 9:16),
   and BackgroundAgents.tsx provides AgentChecklist, AgentFitSort and ChannelTitleOutro.
2. Evidence (local): cd evidence && python3 overlap.py > overlap.json && python3 embed.py > embed.json && python3 boiling.py > boiling.txt
3. python3 make_sheet.py author
4. python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed 0.95
5. python3 make_sheet.py finish && python3 make_docs.py
6. cp beat_sheet.json beat_sheet.pre-remotion.json; python3 runtime/scripts/remotion_scenes.py <reel>
7. ./art final <reel> --height 2160 --fps 30 --out <reel>/exports
8. ./art vertical <reel>; python3 make_vertical.py; python3 runtime/scripts/remotion_scenes.py <reel>/vertical
9. ./art final <reel>/vertical --height 3840 --fps 30 --out <reel>/exports/vertical
10. Visual QC: read frames of both masters (not just the mp4 probe); fix scene sources until zero BLOCKER/MAJOR.
Report; do not publish.
```
