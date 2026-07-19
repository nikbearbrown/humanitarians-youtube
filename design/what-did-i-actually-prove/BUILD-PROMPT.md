# BUILD PROMPT — what-did-i-actually-prove

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/what-did-i-actually-prove --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/what-did-i-actually-prove
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/what-did-i-actually-prove --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/what-did-i-actually-prove
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/what-did-i-actually-prove/what-did-i-actually-prove-slate.mp4`
