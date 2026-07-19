# BUILD PROMPT — why-your-character-doesnt-fall-through

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/why-your-character-doesnt-fall-through --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/why-your-character-doesnt-fall-through
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/why-your-character-doesnt-fall-through --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/why-your-character-doesnt-fall-through
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/why-your-character-doesnt-fall-through/why-your-character-doesnt-fall-through-slate.mp4`
