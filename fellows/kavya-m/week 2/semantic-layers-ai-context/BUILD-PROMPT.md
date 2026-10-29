# BUILD-PROMPT — kavya-semantic-layers-ai-context

Paste into Claude Code from the brutalist.art toolkit root to rebuild both finals end to end.
Free path only: Kokoro, Remotion and ffmpeg. No paid API calls. Never publish.

```
Rebuild youtube/kavya-semantic-layers-ai-context to two clean 4K finals.

1. Read skills/make/ai-explainer/SKILL.md, docs/FELLOWS-SUBMISSION.md and
   docs/PIPELINE-SAFETY.md in full.
2. Re-run the evidence: python -I youtube/kavya-semantic-layers-ai-context/demo/semantic_demo.py and
   confirm it matches demo/semantic_demo_output.txt and the out lines in B03/B04 exactly.
3. Audio first: python runtime/scripts/generate_audio_kokoro.py youtube/kavya-semantic-layers-ai-context
4. Preview before every 4K render: remotion_scenes.py <reel> --stills, then
   runtime/qc/final_frame_check.py --frames-dir on the 50/95% stills.
5. Landscape: remotion_scenes.py <reel> --force, then
   ./art final <reel> --height 2160 --out <landscape dir>
6. Portrait: ./art vertical <reel>, keep the portrait patch documented in BUILD-LOG.md (B01 short lines,
   B02 labels only, B03/B04 short path, no blank lines), render vertical/ with --force, then
   ./art final <reel>/vertical --height 3840 --out <vertical dir>
7. Look at frames from both finals. Record SHA-256, resolution and duration in README.md. Do not
   mark any human review as done.
```

On Windows, put `runtime/bin/ffmpeg-master-latest-win64-gpl/bin` on PATH and set `PYTHONUTF8=1` first.
