# BUILD PROMPT — the-song-that-lied-to-you

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-song-that-lied-to-you --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-song-that-lied-to-you
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-song-that-lied-to-you --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-song-that-lied-to-you
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-song-that-lied-to-you/the-song-that-lied-to-you-slate.mp4`
