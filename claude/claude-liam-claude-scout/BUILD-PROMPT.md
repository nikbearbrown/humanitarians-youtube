# BUILD-PROMPT — claude-liam-claude-scout
# "Claude, Finding." | claude-scout skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 120.1s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art

python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-claude-scout
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-claude-scout
python3 runtime/scripts/compile.py youtube/claude-liam-claude-scout --height 1080
open youtube/claude-liam-claude-scout/claude-liam-claude-scout.mp4
```

## Key decisions

- **Self-demo**: Real candidate card for claude-code-for-students Ch.1
  ("The Homework/Quiz Gap"). Chapter was read live; card premises traced to
  source. Not faked.
- **Three mechanisms**: brand-fit test (UI must be set), honest-cap (source
  pointer required, no vibes), cards-only boundary (human gate is real).
- **Greeting**: Sawubona (Zulu) — unique in this batch run.
- **Title**: "Claude, Finding." — the candidate card is the artifact.
