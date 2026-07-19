# BUILD-PROMPT — claude-liam-sim-scout
# "Claude, Simulating." | sim-scout skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 149.3s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-sim-scout
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-sim-scout
python3 runtime/scripts/compile.py youtube/claude-liam-sim-scout --height 1080
open youtube/claude-liam-sim-scout/claude-liam-sim-scout.mp4
```

## Key decisions
- **Self-demo**: Real MANIM lane card from organic-chemistry Chapter 5 (Stereochemistry at Tetrahedral Centers).
  Lactic acid enantiomers non-superimposition — artifact as motion, two testable predictions stated.
- **Greeting**: Ahoj (Czech) — unique in this batch run.
- **Title**: "Claude, Simulating." — the simulation-ideas.md card is the artifact.
