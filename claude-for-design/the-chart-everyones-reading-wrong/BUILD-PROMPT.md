# BUILD PROMPT — the-chart-everyones-reading-wrong

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/the-chart-everyones-reading-wrong --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/the-chart-everyones-reading-wrong
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-chart-everyones-reading-wrong --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/the-chart-everyones-reading-wrong
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/the-chart-everyones-reading-wrong/the-chart-everyones-reading-wrong-slate.mp4`
