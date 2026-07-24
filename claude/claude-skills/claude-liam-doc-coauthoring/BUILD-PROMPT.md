# BUILD-PROMPT — claude-liam-doc-coauthoring

Standalone rebuild instructions for this reel.

## Identity
- Slug: `claude-liam-doc-coauthoring`
- Skill: `claude-explainer` + `skill-teardown` modifier
- Source skill: `anthropics/skills/skills/doc-coauthoring/SKILL.md`
- Channel: claude-liam (Kokoro am_onyx, free pipeline)
- Format: 16:9, 1280×720 output

## Reel folder
`anthropics/skills/youtube/claude-liam-doc-coauthoring/`

## Remotion components (in `brutalist-art/runtime/remotion/src/scenes/`)
- `DocCoauthoringAnatomy.tsx` — B01: TRIGGER + 3 stage cards + doc types
- `DocCoauthoringStage1.tsx` — B02: Stage 1 info dump + 5 meta questions + exit condition
- `DocCoauthoringStage2.tsx` — B03: Stage 2 6-step per-section loop (SELF-DEMO)
- `DocCoauthoringStage3.tsx` — B04: Stage 3 reader testing — auto vs manual + exit condition
- `DocCoauthoringTell.tsx` — B05: Teardown — context bleed insight + what it gets right/bites

## Rebuild commands (run from `brutalist-art/`)
```bash
python3 runtime/scripts/generate_audio_kokoro.py ../anthropics/skills/youtube/claude-liam-doc-coauthoring/
python3 runtime/scripts/remotion_scenes.py ../anthropics/skills/youtube/claude-liam-doc-coauthoring/
python3 runtime/scripts/compile.py ../anthropics/skills/youtube/claude-liam-doc-coauthoring/
ffmpeg -i ../anthropics/skills/youtube/claude-liam-doc-coauthoring/claude-liam-doc-coauthoring.mp4 \
  -vf fps=2 ../anthropics/skills/youtube/claude-liam-doc-coauthoring/_qc/frames/frame_%04d.png
```

## World-language greeting
B00: "Guten Tag" (German) — Liam cold open, in for Bear

## Notes
- Three-stage workflow: Context Gathering → Refinement → Reader Testing
- Key insight: Reader Testing uses fresh Claude with no context bleed
- Quality gate: 3 consecutive iterations with no change → ask about cuts
- Best for: docs reviewed at scale (PRD, RFC, decision doc)
