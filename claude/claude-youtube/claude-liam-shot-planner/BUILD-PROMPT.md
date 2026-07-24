# BUILD-PROMPT — claude-liam-shot-planner
# "Claude, Routing." | shot-planner skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 172.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-shot-planner
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-shot-planner
python3 runtime/scripts/compile.py youtube/claude-liam-shot-planner --height 1080
open youtube/claude-liam-shot-planner/claude-liam-shot-planner.mp4
```

## Key decisions
- **Self-demo**: Real routing of two beats from the ai-1/ch07 script (built in video 13).
  HOOK=data→Remotion/high; INSTANCE=realworld→design override (text-is-mechanism) + red flag 2 blocked.
- **Greeting**: Salaam (Arabic) — unique in this batch run.
- **Title**: "Claude, Routing." — the routed beat_sheet.json fields are the artifact.
