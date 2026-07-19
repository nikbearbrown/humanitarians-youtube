# BUILD PROMPT — one-little-sun-how-we-built-an-ai

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/one-little-sun-how-we-built-an-ai --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/one-little-sun-how-we-built-an-ai
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/one-little-sun-how-we-built-an-ai --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/one-little-sun-how-we-built-an-ai
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/one-little-sun-how-we-built-an-ai/one-little-sun-how-we-built-an-ai-slate.mp4`
