# BUILD-PROMPT — claude-liam-lyric-resync
# "Claude, Recut." | lyric-resync skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 216.3s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-lyric-resync
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-lyric-resync
python3 runtime/scripts/compile.py youtube/claude-liam-lyric-resync --height 1080
open youtube/claude-liam-lyric-resync/claude-liam-lyric-resync.mp4
```

## Key decisions
- **Self-demo**: Phase 4 prompt writing for Scarborough Fair B03. Phases 1-3 (librosa, faster-whisper, extract_frames) require a WAV file and video. Phase 4 reasoning — look at still + lyric, write image_prompt + video_prompt — is the genuine free deliverable.
- **Greeting**: Selam (Tigrinya/Ethiopian) — unique in this batch run.
- **Title**: "Claude, Recut." — the vision step and single-unit regeneration are the artifact.
