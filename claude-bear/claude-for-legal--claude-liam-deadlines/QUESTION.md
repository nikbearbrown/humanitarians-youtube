# QUESTION.md

**Question:** Can Claude track my legal deadlines for me and tell me when things are due?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's `deadlines`
skill for legal work).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be: `"The skill is deadlines. >."`, `"Claude's job: >."`,
`SkillTeardownMechanism.body` left as `">"`, `ClaudeVerdictArtifact.artifactLines`
includes a bare `">"`, `"I want to >."`. Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/deadlines/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor a
`legal-clinic` folder exists anywhere. Same defect class as the `clearance` /
`ai-inventory` / `ai-tool-handoff` / `aia-generation` / `amendment-history` siblings
already delivered in this family.

**The call:** reconstructed a generic, defensible account of what a legal-deadlines
skill does — take a triggering date and a stated rule (a filing deadline, a response
window, a statute-of-limitations period), compute the resulting date(s), and return a
calendar of what's due and when — described generically per the fresh-script Phase 1
rule ("when in doubt, describe behavior generically") rather than inventing specific
jurisdiction rules, court-rule citations, or claims about which deadlines apply to a
real matter. No fact in the resulting script is Claude-specific, jurisdiction-specific,
or a legal-outcome claim; the central fact (the skill computes from the rule you give it
— it does not know the controlling rule for you) holds regardless of the exact source
text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-deadlines/beat_sheet.json` (7-beat
Teardown skill-teardown, register "Teardown"). Shape and beat count are locked from that
source; this build re-registers the narration to Plain, replaces the cold open with
BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
