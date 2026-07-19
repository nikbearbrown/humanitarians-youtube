# BUILD PROMPT — the-voice-before-the-music-why-songs

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-voice-before-the-music-why-songs --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-voice-before-the-music-why-songs
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-voice-before-the-music-why-songs --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-voice-before-the-music-why-songs
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-voice-before-the-music-why-songs/the-voice-before-the-music-why-songs-slate.mp4`
