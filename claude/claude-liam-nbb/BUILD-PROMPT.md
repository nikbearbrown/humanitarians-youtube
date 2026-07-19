# BUILD-PROMPT — claude-liam-nbb
# "Claude, Torn Down." | nbb skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 262.8s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-nbb
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-nbb
python3 runtime/scripts/compile.py youtube/claude-liam-nbb --height 1080
open youtube/claude-liam-nbb/claude-liam-nbb.mp4
```

## Key decisions
- **Self-demo**: Phase 2 (register rewrite) — canonical beat narration + Teardown rewrite shown side-by-side in B04. Free, no ElevenLabs needed for the demonstration.
- **Greeting**: Ciao (Italian) — unique in this batch run.
- **Title**: "Claude, Torn Down." — the Feynman × MKBHD register rewrite is the artifact.
- **NOTE**: The actual nbb skill uses ElevenLabs Bear clone voice (paid). This teardown video uses Kokoro am_onyx as it's a claude-liam channel explainer about the skill, not an nbb build.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 4.1× slow-mo (10s Remotion clip stretched to 40.55s narration) — known, non-blocking.
