# BUILD PROMPT — subby-the-writing-tool-you-didnt

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/subby-the-writing-tool-you-didnt --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/subby-the-writing-tool-you-didnt
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/subby-the-writing-tool-you-didnt --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/subby-the-writing-tool-you-didnt
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/subby-the-writing-tool-you-didnt/subby-the-writing-tool-you-didnt-slate.mp4`
