# QUESTION.md

**Question:** We're expanding into a new state (or country) — can Claude just rewrite our
employee handbook for it?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of an Anthropic skill,
`expansion-update`, filed under `employment-legal` in the `claude-for-legal` family).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be: `"The skill is expansion-update. >."`, `"Claude's job: >."`
(`SkillTeardownMechanism.body` left as `">"`), `ClaudeVerdictArtifact.artifactLines`
includes a bare `">"`, `"I want to >."` (BHTF's own handoff prompt). Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/expansion-update/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an
`employment-legal` folder exists anywhere. Same defect class as the `clearance` /
`ai-inventory` / `ai-tool-handoff` / `aia-generation` / `amendment-history` siblings
already delivered in this family.

**The call:** reconstructed a generic, defensible account of what an employment-law
"expansion update" skill does — compare an existing policy document (handbook, offer
letter template, notice) against the requirements of a new jurisdiction or expanded
scope, and flag the specific sections that need updating — described generically per
the fresh-script Phase 1 rule ("when in doubt, describe behavior generically") rather
than inventing a specific state's statute, a specific handbook clause, or a legal
outcome. No fact in the resulting script is Claude-specific, jurisdiction-specific, or a
legal-conclusion claim; the central fact (a flagged checklist is not a finished,
lawyer-approved handbook) holds regardless of the exact source text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-expansion-update/beat_sheet.json`
(7-beat Teardown skill-teardown, register "Teardown"). Shape and beat count are locked
from that source; this build re-registers the narration to Plain, replaces the cold
open with BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
