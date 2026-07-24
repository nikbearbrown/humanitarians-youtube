# BUILD-PROMPT — claude-liam-audience-preset
# "Claude, Branded." | audience-preset skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 211.5s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-audience-preset
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-audience-preset
python3 runtime/scripts/compile.py youtube/claude-liam-audience-preset --height 1080
open youtube/claude-liam-audience-preset/claude-liam-audience-preset.mp4
```

## Key decisions
- **Self-demo**: Phase 2 (register rewrite) — canonical mechanism beat + HAI Pragmatist rewrite + Medhavy Wonder rewrite. All three shown in B04 ClaudeCodeBeat. Free, no brand_variant.py needed.
- **Greeting**: Hei (Norwegian) — unique in this batch run.
- **Title**: "Claude, Branded." — the non-destructive brand fork is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.6× slow-mo (10s Remotion clip stretched to 36.39s narration) — known, non-blocking.
