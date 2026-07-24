# BUILD-PROMPT — claude-liam-explainer-deepen
# "Claude, Deepened." | explainer-deepen skill teardown
# Built: 2026-07-18 | Kokoro af_kore

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art

# 1. Regenerate audio (Kokoro, no ElevenLabs)
python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/claude-liam-explainer-deepen/beat_sheet.json \
  --no-gate

# 2. Render Remotion scenes (foreground, concurrency=1)
python3 runtime/scripts/remotion_scenes.py \
  youtube/claude-liam-explainer-deepen

# 3. Compile review cut
./art run youtube/claude-liam-explainer-deepen

# 4. Open and review
open youtube/claude-liam-explainer-deepen/claude-liam-explainer-deepen.mp4
```

## Key decisions

- **Self-demo**: Real audit run on claude-liam-sketch-explainer (video 2 of
  this batch). Output is genuine — 2 critical failures, 5 warnings, real
  verdict NEEDS-BB-CONVERSION. Not faked.
- **Three laws teardown**: audit gate (bidirectional — never rewrite a passer),
  lift law (concept not script), depth law (instances + tangent earn runtime).
- **Greeting**: Yassou (Greek) — unique in this batch run.
- **Title**: "Claude, Deepened." — the conversion is the artifact.

## Skill source

`skills/make/explainer-deepen/SKILL.md` (~7 KB)
`skills/make/explainer-deepen/scripts/audit.py` — runnable 10-check scorecard

All three verbatim quotes verified against SKILL.md on 2026-07-18.
See SOURCES.md for line references and real self-demo output.
