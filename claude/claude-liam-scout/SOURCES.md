# SOURCES — claude-liam-scout
# "Claude, Scouting." | 2026-07-18

## Primary source
- **Skill SKILL.md**: `brutalist-art/skills/make/scout/SKILL.md`
  - ~3 KB, covers: scouting protocol, selectivity principle, vox bar,
    candidate card format, output rules
  - All quotes verified against this file on 2026-07-18

## Verbatim quotes used (with line context)

### SELECTIVITY quote (B05 on-screen)
> "Your value is selectivity, not coverage: most chapter content is not a film."
- Source: `skills/make/scout/SKILL.md` — core principle (early in body)

### VOX BAR quote (B06 on-screen)
> "if you cannot write THE QUESTION as a gap formula and name a concrete KEY CASE, the concept is not a card yet."
- Source: `skills/make/scout/SKILL.md` — scout command step 3

### STOP-AT-CARD quote (B07 on-screen)
> "Never write narration, beats, or scenes here. Stop at the card."
- Source: `skills/make/scout/SKILL.md` — Output rules section

## Self-demo data
- Target book: `../organic-chemistry` (32 chapters)
- Command: `python3 skills/make/scout/scripts/scan_book.py ../organic-chemistry`
- Real output captured 2026-07-18: 32 chapters scanned, word counts written,
  manifest saved to `organic-chemistry/youtube/_chapters.json`

## Computed values
- Number of beats: 11 (B00–B07, BVDT, BHTF, BOUT)
- UI beats: 5 (B00, B03, BVDT, BHTF, BOUT) — per ILLUSTRATE LAW
- Illustration beats: 6 (B01, B02, B04, B05, B06, B07)
- Self-demo target: organic-chemistry scan (32 chapters, real manifest output)
- Total runtime: 111.7s

## Supporting references
- `skills/make/scout/reference/selection.md` — vox bar + score rubric
- `skills/make/scout/reference/candidate-format.md` — card schema
- `CLAUDE-BRAND.md` — palette law and channel table
- `runtime/remotion/src/tokens/claude.ts` — token source of truth
