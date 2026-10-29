# BUILD-PROMPT — kavya-data-agents-harness

Paste into Claude Code from the brutalist.art toolkit root to rebuild both finals end to end.
Free path only: Kokoro, Remotion, ffmpeg. No paid API calls. Never publish.

```
Rebuild youtube/kavya-data-agents-harness to two clean 4K finals.

1. Read skills/make/ai-explainer/SKILL.md, docs/FELLOWS-SUBMISSION.md and
   docs/PIPELINE-SAFETY.md in full.
2. Re-run the evidence: python -I youtube/kavya-data-agents-harness/demo/harness_demo.py and
   confirm it matches demo/harness_demo_output.txt and the out lines in B03/B04 exactly.
3. Audio first: python runtime/scripts/generate_audio_kokoro.py youtube/kavya-data-agents-harness
4. Landscape: python runtime/scripts/remotion_scenes.py youtube/kavya-data-agents-harness --force
   then ./art run youtube/kavya-data-agents-harness (review), then
   ./art final youtube/kavya-data-agents-harness --height 2160 --out <landscape dir>
5. Portrait: ./art vertical youtube/kavya-data-agents-harness, then render vertical/ with
   remotion_scenes.py --force and ./art final youtube/kavya-data-agents-harness/vertical
   --height 3840 --out <vertical dir>
6. Visual QC: sample frames from both finals (>=2 fps plus 15/50/85% of each beat), READ the PNGs,
   log defects in _qc/REPORT.md, fix root causes and re-render until no BLOCKER or MAJOR remains.
7. Record SHA-256, resolution and duration of both finals in README.md. Do not mark any human review as done.
```

On Windows, put `runtime/bin/ffmpeg-master-latest-win64-gpl/bin` on PATH and set `PYTHONIOENCODING=utf-8` first.
