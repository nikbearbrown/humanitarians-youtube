# BUILD-PROMPT — kavya-opentelemetry-ai-agents

Paste into Claude Code from the brutalist.art toolkit root to rebuild both finals end to end.
Free path only: Kokoro, Remotion and ffmpeg. No paid API calls. Never publish.

```
Rebuild youtube/kavya-opentelemetry-ai-agents to two clean 4K finals.

1. Read skills/make/ai-explainer/SKILL.md, docs/FELLOWS-SUBMISSION.md and
   docs/PIPELINE-SAFETY.md in full.
2. Re-run the evidence: python -I youtube/kavya-opentelemetry-ai-agents/demo/otel_demo.py and
   confirm it matches demo/otel_demo_output.txt and the out lines in B03/B04 exactly.
3. Audio first: python runtime/scripts/generate_audio_kokoro.py youtube/kavya-opentelemetry-ai-agents
4. Preview before every 4K render (remotion_scenes.py --stills, final_frame_check.py --frames-dir),
   and LOOK at the stills: the checker does not catch text clipped inside a terminal window.
5. Landscape: remotion_scenes.py <reel> --force, then ./art final <reel> --height 2160 --out <dir>
6. Portrait: ./art vertical <reel>, keep the portrait patch documented in BUILD-LOG.md, render
   vertical/ with --force, then ./art final <reel>/vertical --height 3840 --out <dir>
7. Look at frames from both finals. Record SHA-256, resolution and duration in README.md. Do not
   mark any human review as done.
```

On Windows, put `runtime/bin/ffmpeg-master-latest-win64-gpl/bin` on PATH and set `PYTHONUTF8=1` first.
