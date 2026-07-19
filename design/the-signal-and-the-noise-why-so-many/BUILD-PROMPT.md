# BUILD PROMPT — the-signal-and-the-noise-why-so-many

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-signal-and-the-noise-why-so-many --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-signal-and-the-noise-why-so-many
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-signal-and-the-noise-why-so-many --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-signal-and-the-noise-why-so-many
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-signal-and-the-noise-why-so-many/the-signal-and-the-noise-why-so-many-slate.mp4`
