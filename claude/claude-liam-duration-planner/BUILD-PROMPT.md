# BUILD-PROMPT — claude-liam-duration-planner
# "Claude, Timed." | duration-planner skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 171.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-duration-planner
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-duration-planner
python3 runtime/scripts/compile.py youtube/claude-liam-duration-planner --height 1080
open youtube/claude-liam-duration-planner/claude-liam-duration-planner.mp4
```

## Key decisions
- **Self-demo**: Real pace-check of two beats from claude-liam-sim-scout (video 12, this batch).
  B03=6.04s above floor, B04=20.12s at-ceiling for mechanism (genuinely single idea, no split).
- **Greeting**: Vanakkam (Tamil) — unique in this batch run.
- **Title**: "Claude, Timed." — the hold recommendations and total runtime are the artifact.
