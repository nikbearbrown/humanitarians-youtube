# QUESTION

**Verbatim (SUBJECT.json):** "Claude, Data Visualization."

**Who asked / where:** Not a real pasted question — this is a redo-mode build
of a skill-teardown reel. `SUBJECT.json`'s `source_sheet` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-data-visualization/beat_sheet.json`,
a rendered Teardown-register `claude-liam` reel walking through the
`data-visualization` Anthropic skill (the `data` plugin's chart-design
tool). Per hai-simple's redo contract, the actually-askable question this
reel answers is: **when Claude "does data visualization," does that mean
picking a colorful palette, or something else first?**

**Name usable:** N/A — no named asker; redo of a batch-built reel.

## Source-material note

The source sheet's own body narration is generic scaffolding text with no
skill-specific content (B01: "SKILL.md is the instruction set. 1 file
total."; B02: a content-free 3-step "Read SKILL.md -> Execute -> Return
output" pipeline; B03: a truncated restatement of the skill's own
`description` field cut off mid-sentence — "Use when building ch[arts]").
Its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/data-visualization/SKILL.md`)
does not exist anywhere in this local tree (confirmed: `ls` fails). Per the
REDO LAW ("keep its question, its facts... the missing/truncated facts
could not simply be invented"), the real facts below are re-sourced from
the actual public file: `github.com/anthropics/knowledge-work-plugins`,
`data/skills/data-visualization/SKILL.md` (fetched via
`raw.githubusercontent.com`, read in full this invocation). This is the
same resolution the sibling reel
`knowledge-work-plugins--claude-liam-create-viz` used for the same defect
class in the same skill family, earlier the same day.

Real facts used: the chart-selection-by-relationship table (trend->line,
ranking->horizontal bar, composition-over-time->stacked area, many-variable
correlation->heatmap, geographic->choropleth), the explicit "when NOT to
use" list (pie charts, 3D charts, dual-axis charts), and the Design
Principles / Accessibility sections (color encodes meaning and one accent
carries the story; red/green-only fails ~8% of men; every chart must survive
without color via pattern/label/line-style).
