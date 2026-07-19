# BUILD-PROMPT — claude-liam-lyric-overlay
# "Claude, Overlaid." | lyric-overlay skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 213.4s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-lyric-overlay
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-lyric-overlay
python3 runtime/scripts/compile.py youtube/claude-liam-lyric-overlay --height 1080
open youtube/claude-liam-lyric-overlay/claude-liam-lyric-overlay.mp4
```

## Key decisions
- **Self-demo**: theme.ts configuration for bright travel footage. No WAV file needed — theming is purely configuration. Values derived from documented knobs: waveformMid=0.78, scrimOpacity=0.55, lyricStyle='outline'.
- **Greeting**: Habari (Swahili) — unique in this batch run.
- **Title**: "Claude, Overlaid." — the extraction guarantee and two-pass lyric strategy are the artifact.
