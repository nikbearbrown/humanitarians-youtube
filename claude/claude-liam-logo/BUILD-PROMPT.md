# BUILD-PROMPT — claude-liam-logo
# "Claude, Stung." | logo skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 254.0s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-logo
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-logo
python3 runtime/scripts/compile.py youtube/claude-liam-logo --height 1080
open youtube/claude-liam-logo/claude-liam-logo.mp4
```

## Key decisions
- **Self-demo**: LogoOutro beat JSON — showing the full beat entry the logo script appends to beat_sheet.json. Free, no jingle required.
- **Greeting**: Kia ora (Māori) — unique in this batch run.
- **Title**: "Claude, Stung." — the LogoOutro brand sting is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.9× slow-mo (10s Remotion clip stretched to 38.89s narration) — known, non-blocking.
