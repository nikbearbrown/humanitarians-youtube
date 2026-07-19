# BUILD PROMPT — review-standard-deviations

Paste this into Claude Code (from `books/`) to build the final cut:

```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
    brutalist-art/youtube/hai-fellows/review-standard-deviations --no-gate
python3 brutalist-art/runtime/scripts/remotion_scenes.py \
    brutalist-art/youtube/hai-fellows/review-standard-deviations
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-standard-deviations --review
python3 brutalist-art/runtime/scripts/compile.py \
    brutalist-art/youtube/hai-fellows/review-standard-deviations
```

Free pipeline only. Do not publish.
Review cut: `brutalist-art/youtube/hai-fellows/review-standard-deviations/review-standard-deviations-slate.mp4`
