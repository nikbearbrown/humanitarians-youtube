# BUILD-PROMPT — claude-liam-kids-video
# "Claude, Cubs." | kids-video skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 223.2s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-kids-video
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-kids-video
python3 runtime/scripts/compile.py youtube/claude-liam-kids-video --height 1080
open youtube/claude-liam-kids-video/claude-liam-kids-video.mp4
```

## Key decisions
- **Self-demo**: Phase 1 Gate K-valid beat sheet for "circle" episode (ages 1-3) — 13 beats demonstrating the contingency triad, exemplar variability, contrast case, and co-view close. Gate K checks all pass in the plan. Purely free; Gate K requires the kids_gate.py script (no spend), and audio/visual phases require the host mascot and Manim (not needed for Phase 1).
- **Greeting**: Konnichiwa (Japanese) — unique in this batch run.
- **Title**: "Claude, Cubs." — the Gate K-valid beat plan is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 4.8× slow-mo (10s Remotion clip stretched to match 48.5s narration) — known, non-blocking.
