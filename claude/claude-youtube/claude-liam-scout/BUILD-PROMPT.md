# BUILD-PROMPT — claude-liam-scout
# "Claude, Scouting." | scout skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 111.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art

# 1. Regenerate audio (Kokoro, no ElevenLabs)
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-scout

# 2. Render Remotion scenes (foreground, concurrency=1)
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-scout

# 3. Compile (bypass run.sh — all-REMOTION build)
python3 runtime/scripts/compile.py youtube/claude-liam-scout --height 1080

# 4. Open and review
open youtube/claude-liam-scout/claude-liam-scout.mp4
```

Note: use compile.py directly (not ./art run) — all-REMOTION builds have no
scenes.py. The run.sh guard requires scenes.py for non-vox-electoral-college
reels.

## Key decisions

- **Self-demo**: scan_book.py run on organic-chemistry (32 chapters). Real
  manifest output — not faked.
- **Three laws teardown**: selectivity (not coverage), vox bar (gap formula +
  key case), stop-at-card (never cross into builder territory).
- **Greeting**: Jambo (Swahili) — unique in this batch run.
- **Title**: "Claude, Scouting." — the candidate card is the artifact.

## Skill source

`skills/make/scout/SKILL.md` (~3 KB)
`skills/make/scout/scripts/scan_book.py` — chapter manifest generator

All three verbatim quotes verified against SKILL.md on 2026-07-18.
See SOURCES.md for line references and real self-demo output.
