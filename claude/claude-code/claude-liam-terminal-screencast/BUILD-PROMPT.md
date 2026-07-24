# BUILD-PROMPT — claude-liam-terminal-screencast
# "Claude, Typed." | terminal-screencast skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 191.2s

## Standalone rebuild instructions

To rebuild this video from scratch:

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art

# 1. Regenerate audio (Kokoro, no ElevenLabs)
python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/claude-liam-terminal-screencast/beat_sheet.json \
  --no-gate

# 2. Render Remotion scenes (foreground, concurrency=1)
python3 runtime/scripts/remotion_scenes.py \
  youtube/claude-liam-terminal-screencast

# 3. Compile review cut
./art run youtube/claude-liam-terminal-screencast

# 4. Open and review
open youtube/claude-liam-terminal-screencast/claude-liam-terminal-screencast.mp4
```

## Key decisions

- **Self-demo**: UV catastrophe beat spine plan — shows the free authoring step
  (beat_plan.py output) rather than a full render. The plan itself is the artifact.
- **Three laws teardown**: spine law (problem before prompts), revision law
  (check-and-change is structural), actual-code law (receipt must be real).
- **Greeting**: Merhaba (Turkish) — unique in this batch run.
- **Title**: "Claude, Typed." — the terminal session is the artifact.

## Skill source

`skills/make/terminal-screencast/SKILL.md` (~7 KB)

All three verbatim quotes verified against SKILL.md on 2026-07-18.
See SOURCES.md for line references.
