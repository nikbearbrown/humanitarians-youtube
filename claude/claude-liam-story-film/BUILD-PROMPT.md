# BUILD-PROMPT — claude-liam-story-film
# "Claude, Narrating." | story-film skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 165.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-story-film
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-story-film
python3 runtime/scripts/compile.py youtube/claude-liam-story-film --height 1080
open youtube/claude-liam-story-film/claude-liam-story-film.mp4
```

## Key decisions
- **Self-demo**: Phase 2 beat segmentation of Poe's "The Raven" (1845, public domain). Phase 1 (ElevenLabs) and Phase 3+ (Higgsfield/Hailuo) are paid — only Phase 2 is in scope for the free pipeline demo. Three beats from the opening stanza with scene descriptions, camera moves, and style preset filled.
- **Greeting**: Sawadee (Thai) — unique in this batch run.
- **Title**: "Claude, Narrating." — the narration clock and phase-gate honesty are the artifact.
- **Mechanism 3**: story-film documents its own incomplete build state (3 of 5 phases not yet built). Treated as an integrity mechanism, not a caveat — a skill that claims to be complete when it isn't produces silent failures at the expensive phase.
