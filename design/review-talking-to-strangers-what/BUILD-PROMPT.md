# BUILD PROMPT — review-talking-to-strangers-what

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/review-talking-to-strangers-what --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/review-talking-to-strangers-what
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-talking-to-strangers-what --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-talking-to-strangers-what
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/review-talking-to-strangers-what/review-talking-to-strangers-what-slate.mp4`
