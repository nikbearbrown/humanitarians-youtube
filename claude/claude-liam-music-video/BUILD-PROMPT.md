# BUILD-PROMPT — claude-liam-music-video
# "Claude, Synced." | music-video skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 219.2s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-music-video
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-music-video
python3 runtime/scripts/compile.py youtube/claude-liam-music-video --height 1080
open youtube/claude-liam-music-video/claude-liam-music-video.mp4
```

## Key decisions
- **Self-demo**: Phase 4 plan for a 128 BPM, C-major, bright, high-DR dance track. Phase 1 (librosa analyze) requires a real WAV file — not available in the free pipeline demo. The plan output (section map + visualizer choices + sparing 2-beat media ask) is the genuine demonstrable deliverable.
- **Greeting**: Kumusta (Filipino) — unique in this batch run.
- **Title**: "Claude, Synced." — the librosa-first approach and code-generated visuals are the artifact.
- **Mechanism 2**: "design from song" quote is a paraphrase of the full sentence; verbatim match confirmed in SKILL.md design seam section.
