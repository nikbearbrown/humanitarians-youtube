# BUILD PROMPT — how-light-works-and-why-it-controls

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/how-light-works-and-why-it-controls --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/how-light-works-and-why-it-controls
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/how-light-works-and-why-it-controls --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/how-light-works-and-why-it-controls
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/how-light-works-and-why-it-controls/how-light-works-and-why-it-controls-slate.mp4`
