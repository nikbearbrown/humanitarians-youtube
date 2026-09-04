# QUESTION

**The question:** "Claude, Cowork Plugin Customizer." — when Claude runs a
Skill named `cowork-plugin-customizer`, is that a plugin Claude has
installed, the way an app installs a feature — or something else?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-cowork-plugin-customizer/beat_sheet.json`
(a Teardown-register batch build, brand `claude-liam`, `@NikBearBrown`,
`source_skill` pointing at a path on Bear's separate machine —
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md`
— not present in this workspace). 7 beats: B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro.

**Source defect found and handled:** the source's B00, B03, BVDT, and BHTF
narration all contain a literal unfilled `>` placeholder where a
skill-specific detail (Claude's exact customization job, the "gets right /
bites" specifics, the handoff task) was meant to be substituted by the batch
builder and never was — confirmed against
`BUILD-SKILL-EXPLAINERS-LOG.md`/`SKILL-EXPLAINERS-BATCH-LOG.md`, which show
this reel as a 2026-07-25 batch build with no local copy of the real
`SKILL.md` ever fetched. The one substantive fact the source DOES carry
(present in B00's `output` array and BVDT's artifact lines, not behind a
placeholder): *"Customize a Claude Code plugin for a specific organization's
tools."* Per NO-INVENTED-FACTS (hai-simple SKILL.md PHASE 1: "no invented
UI... when in doubt, describe behavior generically"), this redo does not
guess what the `>` placeholders were meant to say. It keeps every fact the
source actually states, states the mechanism generically and accurately
where the source is silent, and replaces the source's private, unrunnable
Your-Turn task (which asked the viewer to invoke a skill only Bear's
machine has) with a generalized, actually-runnable version of the same
pedagogical move: read a Skill's file before running it.

**Body facts carried from source (unchanged, not invented):**
- a Claude Skill is a folder, not installed software; it contains a
  `SKILL.md` — plain-language instructions
- `cowork-plugin-customizer`'s stated job: customize a Claude Code plugin
  for a specific organization's tools
- Claude reads the file, then works through its Steps section in order
- same input produces the same steps every run (repeatable)
- the limit is scope: only what the file specifies

**Naive framing (B00, corrected on screen):** "Is cowork-plugin-customizer a
plugin that Claude installs?" → corrects "installs" to "reads" (the name
itself — "plugin" — invites the newcomer's default read that this is
installed software; it's a folder Claude reads before acting).

**Your Turn (generalized from the source's unrunnable version):** the
source's task named `cowork-plugin-customizer` by name, a skill that exists
only in Bear's private book and that no viewer can run. This redo keeps the
teaching point — reading the file predicts the run — but points it at any
Skill the viewer actually has.
