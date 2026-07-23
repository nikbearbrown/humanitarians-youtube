# BUILD PROMPT — the-paper-trail-in-the-studio

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-paper-trail-in-the-studio --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-paper-trail-in-the-studio
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-paper-trail-in-the-studio --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-paper-trail-in-the-studio
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-paper-trail-in-the-studio/the-paper-trail-in-the-studio-slate.mp4`
