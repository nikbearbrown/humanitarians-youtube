# BUILD-PROMPT — claude-liam-claude-api

Standalone rebuild instructions for this reel.

## Identity
- Slug: `claude-liam-claude-api`
- Skill: `claude-explainer` + `skill-teardown` modifier
- Source skill: `anthropics/skills/skills/claude-api/SKILL.md`
- Channel: claude-liam (Kokoro am_onyx, free pipeline)
- Format: 16:9, 1280×720 output

## Reel folder
`anthropics/skills/youtube/claude-liam-claude-api/`

## Remotion components (in `brutalist-art/runtime/remotion/src/scenes/`)
- `ClaudeApiAnatomy.tsx` — B01: TRIGGER callout + language chips + task reference
- `ClaudeApiSurfaces.tsx` — B02: Three API surfaces + 4 agent criteria
- `ClaudeApiDrift.tsx` — B03: API drift table (SELF-DEMO, verbatim SKILL.md)
- `ClaudeApiModels.tsx` — B04: Model table (SELF-DEMO, verbatim SKILL.md)
- `ClaudeApiTell.tsx` — B05: Teardown moment — TRIGGER architecture + 44 pitfalls

Standard bookend scenes (already registered):
- `ClaudeComposerAsk` — B00 (cold open) and BHTF (handoff)
- `ClaudeVerdictArtifact` — BVDT (verdict)
- `ClaudeTitleOutro` — BOUT (outro)

## Rebuild commands (run from `brutalist-art/`)
```bash
# 1. Generate audio
python3 runtime/scripts/generate_audio_kokoro.py ../anthropics/skills/youtube/claude-liam-claude-api/

# 2. Render Remotion scenes
python3 runtime/scripts/remotion_scenes.py ../anthropics/skills/youtube/claude-liam-claude-api/

# 3. Compile
python3 runtime/scripts/compile.py ../anthropics/skills/youtube/claude-liam-claude-api/

# 4. QC
ffmpeg -i ../anthropics/skills/youtube/claude-liam-claude-api/mp4/claude-liam-claude-api.mp4 \
  -vf fps=2 ../anthropics/skills/youtube/claude-liam-claude-api/_qc/frames/frame_%04d.png
```

## World-language greeting
B00: "Bonjour" (French) — Liam cold open, in for Bear

## Notes
- TRIGGER fires BEFORE the target file opens — pre-scan gate, not post-request lookup
- DEFAULT model: claude-opus-4-8 (non-negotiable unless user names another)
- API drift: budget_tokens → adaptive (returns 400 on current models)
- 44 pitfalls documented in SKILL.md; none enforced at call time
