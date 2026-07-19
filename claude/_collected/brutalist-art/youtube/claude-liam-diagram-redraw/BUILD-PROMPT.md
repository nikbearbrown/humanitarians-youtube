# BUILD-PROMPT — claude-liam-diagram-redraw
# "Claude, Redrawn." | diagram-redraw skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 195.5s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-diagram-redraw
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-diagram-redraw
python3 runtime/scripts/compile.py youtube/claude-liam-diagram-redraw --height 1080
open youtube/claude-liam-diagram-redraw/claude-liam-diagram-redraw.mp4
```

## Key decisions
- **Self-demo**: Stage 1 candidate plan for quantum_mechanics — free, deterministic (no AI). Shows classification split (19 doable / 8 logos / 20 photos) and top 5 ranked candidates.
- **Greeting**: Olá (Portuguese) — unique in this batch run for video 34.
- **Title**: "Claude, Redrawn." — the fresh house-style SVG is the artifact; the editorial signal is the method.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.44× slow-mo — known, non-blocking.
