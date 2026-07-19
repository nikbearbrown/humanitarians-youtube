# BUILD-PROMPT — claude-liam-dance-video
# "Claude, Dancing." | dance-video skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 190.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-dance-video
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-dance-video
python3 runtime/scripts/compile.py youtube/claude-liam-dance-video --height 1080
open youtube/claude-liam-dance-video/claude-liam-dance-video.mp4
```

## Key decisions
- **Self-demo**: Phase 2 dance segmentation — write 3 beats for a rubber-hose Calloway character (120 BPM swing) using the 4-part formula: CHARACTER + DANCE + CAMERA + BACKGROUND + STYLE. Phase 3+ requires Higgsfield (paid); Phase 2 is free.
- **Greeting**: Talofa (Samoan) — unique in this batch run.
- **Title**: "Claude, Dancing." — the beat-synced character reel is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3× slow-mo (10s Remotion clip stretched to match 30.4s narration) — known, non-blocking.
