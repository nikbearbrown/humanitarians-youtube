# BUILD PROMPT — what-you-cant-see-is-killing-you

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/what-you-cant-see-is-killing-you --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/what-you-cant-see-is-killing-you
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/what-you-cant-see-is-killing-you --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/what-you-cant-see-is-killing-you
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/what-you-cant-see-is-killing-you/what-you-cant-see-is-killing-you-slate.mp4`
