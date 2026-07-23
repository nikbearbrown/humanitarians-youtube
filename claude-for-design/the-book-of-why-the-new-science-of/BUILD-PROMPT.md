# BUILD PROMPT — the-book-of-why-the-new-science-of

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-book-of-why-the-new-science-of --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-book-of-why-the-new-science-of
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-book-of-why-the-new-science-of --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-book-of-why-the-new-science-of
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-book-of-why-the-new-science-of/the-book-of-why-the-new-science-of-slate.mp4`
