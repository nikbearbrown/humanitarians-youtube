# BUILD PROMPT — games-design-and-play

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/games-design-and-play --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/games-design-and-play
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/games-design-and-play --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/games-design-and-play
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/games-design-and-play/games-design-and-play-slate.mp4`
