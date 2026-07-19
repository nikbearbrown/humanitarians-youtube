# BUILD PROMPT — five-senses-one-song

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/five-senses-one-song --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/five-senses-one-song
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/five-senses-one-song --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/five-senses-one-song
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/five-senses-one-song/five-senses-one-song-slate.mp4`
