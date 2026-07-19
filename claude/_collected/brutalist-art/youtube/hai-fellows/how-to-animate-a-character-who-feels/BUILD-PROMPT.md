# BUILD PROMPT — how-to-animate-a-character-who-feels

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/how-to-animate-a-character-who-feels --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/how-to-animate-a-character-who-feels
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/how-to-animate-a-character-who-feels --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/how-to-animate-a-character-who-feels
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/how-to-animate-a-character-who-feels/how-to-animate-a-character-who-feels-slate.mp4`
