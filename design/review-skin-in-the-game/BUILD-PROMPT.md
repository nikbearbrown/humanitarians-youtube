# BUILD PROMPT — review-skin-in-the-game

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/review-skin-in-the-game --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/review-skin-in-the-game
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-skin-in-the-game --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-skin-in-the-game
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/review-skin-in-the-game/review-skin-in-the-game-slate.mp4`
