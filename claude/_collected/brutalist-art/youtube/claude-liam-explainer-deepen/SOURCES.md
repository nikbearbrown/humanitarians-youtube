# SOURCES — claude-liam-explainer-deepen
# "Claude, Deepened." | 2026-07-18

## Primary source
- **Skill SKILL.md**: `brutalist-art/skills/make/explainer-deepen/SKILL.md`
  - ~7 KB, covers: audit rubric (10 checks), conversion phases, lift law,
    depth law, silent mode contract, what NOT to do
  - All quotes verified against this file on 2026-07-18

## Verbatim quotes used (with line context)

### AUDIT GATE quote (B05 on-screen)
> "Never 'convert' a video that already passes the audit."
- Source: `skills/make/explainer-deepen/SKILL.md` — What NOT to do section

### LIFT LAW quote (B06 on-screen)
> "you keep what it teaches, not how it sketched it."
- Source: `skills/make/explainer-deepen/SKILL.md` — convert step 2
- Note: original has italics markers (*what it teaches*, *how it sketched it*)
  — displayed without markdown on screen

### DEPTH LAW quote (B07 on-screen)
> "depth comes from instances and the tangent, never from padding."
- Source: `skills/make/explainer-deepen/SKILL.md` — convert step 3

## Self-demo data
- Audit target: `youtube/claude-liam-sketch-explainer/beat_sheet.json`
- Command: `python3 skills/make/explainer-deepen/scripts/audit.py youtube/claude-liam-sketch-explainer`
- Real output captured 2026-07-18:
  - 2 critical failures: no INSTANCE beats before ABSTRACTION, equation without tangent
  - 5 warnings: series/font/style/accent/slug/roles/BOUNDARY
  - Verdict: NEEDS-BB-CONVERSION

## Computed values
- Number of beats: 11 (B00–B07, BVDT, BHTF, BOUT)
- UI beats: 5 (B00, B03, BVDT, BHTF, BOUT) — per ILLUSTRATE LAW
- Illustration beats: 6 (B01, B02, B04, B05, B06, B07)
- Self-demo target: claude-liam-sketch-explainer (real audit, real output)
- Skill SKILL.md size: approximately 7 KB

## Supporting references
- `skills/make/math-explainer/reference/pedagogy.md` — depth standard referenced by skill
- `CLAUDE-BRAND.md` — palette law and channel table
- `runtime/remotion/src/tokens/claude.ts` — token source of truth
