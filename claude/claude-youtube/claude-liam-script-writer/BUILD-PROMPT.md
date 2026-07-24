# BUILD-PROMPT — claude-liam-script-writer
# "Claude, Scripted." | script-writer skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 161.1s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-script-writer
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-script-writer
python3 runtime/scripts/compile.py youtube/claude-liam-script-writer --height 1080
open youtube/claude-liam-script-writer/claude-liam-script-writer.mp4
```

## Key decisions
- **Self-demo**: Real script sketch from ai-1/chapters/07-chapter-writing.md.
  One insight (log.csv all-green ≠ good chapters), key case (fluency-trap phrase),
  mystery gap named, first two beats (HOOK + INSTANCE) with roles assigned.
- **Greeting**: Shalom (Hebrew) — unique in this batch run.
- **Title**: "Claude, Scripted." — the script.md + beat_sheet.json are the artifact.
