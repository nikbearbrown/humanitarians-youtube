# QUESTION.md

**Question:** Can Claude decide which issues in a batch of deal documents actually
kill the deal?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's
`diligence-issue-extraction` skill for corporate-legal work).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be: `"The skill is diligence-issue-extraction. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."`. Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/diligence-issue-extraction/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor a
`corporate-legal` folder exists anywhere. So there were no real facts to carry over
beyond the topic (DILIGENCE-ISSUE-EXTRACTION, an Anthropic skill for corporate-legal
work) and the shape (Teardown skill-teardown format, 7 beats: cold open, anatomy,
pipeline, design tell, verdict, handoff, outro) — same defect class as the
`clearance`/`ai-inventory`/`ai-tool-handoff`/`aia-generation`/`amendment-history`
siblings in this family.

**The call:** reconstructed a generic, defensible account of what a diligence
issue-extraction skill does — reading a batch of deal documents against a checklist of
issue categories a SKILL.md defines (things like change-of-control clauses, missing
consents, expired licenses), and returning a structured issues report — described
generically per the fresh-script Phase 1 rule ("when in doubt, describe behavior
generically") rather than inventing specific document types, database names, or a
legal-outcome claim about any real deal. No fact in the resulting script is
Claude-specific or unverifiable; the central fact (a screening checklist is not a
judgment about what actually matters to the deal) is true of any such skill regardless
of its exact source text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-diligence-issue-extraction/beat_sheet.json`
(7-beat Teardown skill-teardown, register "Teardown"). Shape and beat count are locked
from that source; this build re-registers the narration to Plain, replaces the cold open
with BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
