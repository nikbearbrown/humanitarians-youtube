# BUILD-PROMPT — claude-liam-hai
# "Claude, Pragmatic." | hai skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 240.0s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-hai
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-hai
python3 runtime/scripts/compile.py youtube/claude-liam-hai --height 1080
open youtube/claude-liam-hai/claude-liam-hai.mp4
```

## Key decisions
- **Self-demo**: Phase 2 (register rewrite) — canonical shot-planner beat + Pragmatist rewrite (method/when-to/when-NOT-to/where-it-fails). Free, no brand_variant.py needed.
- **Greeting**: Bonjour (French) — unique in this batch run.
- **Title**: "Claude, Pragmatic." — the Pragmatist register rewrite is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.8× slow-mo (10s Remotion clip stretched to 38.23s narration) — known, non-blocking.
