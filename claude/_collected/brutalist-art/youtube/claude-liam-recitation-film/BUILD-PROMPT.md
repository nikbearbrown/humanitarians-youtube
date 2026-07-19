# BUILD-PROMPT — claude-liam-recitation-film
# "Claude, Reciting." | recitation-film skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 207.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-recitation-film
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-recitation-film
python3 runtime/scripts/compile.py youtube/claude-liam-recitation-film --height 1080
open youtube/claude-liam-recitation-film/claude-liam-recitation-film.mp4
```

## Key decisions
- **Self-demo**: Phase 1 beat plan for Keats "Bright Star" (1819), lines 1–4 — peak line declared, roles assigned (breathe/illustrate/teach), one teach chip with OED citation. Purely free; Phase 3 (align) needs a real performance audio file.
- **Greeting**: Aloha (Hawaiian) — unique in this batch run.
- **Title**: "Claude, Reciting." — the margin-law-governed plan is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.5× slow-mo (10s Remotion clip stretched to 35.6s narration) — known, non-blocking.
