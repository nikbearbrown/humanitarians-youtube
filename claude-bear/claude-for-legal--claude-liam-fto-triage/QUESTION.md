# QUESTION.md

**Question:** Can Claude clear a new product of patent risk before we launch it?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's `fto-triage`
skill for IP-legal work — FTO = Freedom To Operate).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be: `"The skill is fto-triage. >."`, `"Claude's job: >."`, the
`SkillTeardownMechanism.body` prop left as `">"`, `ClaudeVerdictArtifact.artifactLines`
includes a bare `">"`, and the handoff command `"I want to >."`. Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/fto-triage/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an `ip-legal`
folder exists anywhere. So there were no real facts to carry over beyond the topic
(FTO-TRIAGE, an Anthropic skill for IP-legal work — file size 25k per the source's own
`SkillTeardownAnatomy` props) and the shape (Teardown skill-teardown format, 7 beats:
cold open, anatomy, pipeline, design tell, verdict, handoff, outro) — same defect class
as the `clearance` / `ai-inventory` / `ai-tool-handoff` / `aia-generation` /
`amendment-history` siblings in this family.

**The call:** reconstructed a generic, defensible account of what an FTO-triage skill
does — screening a described product or feature against a checklist of claim elements,
keywords, and jurisdictions a SKILL.md defines, then returning a structured triage
report that flags matters for a closer look — described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than inventing
specific patent databases, search tools, or legal-outcome claims. No fact in the
resulting script is Claude-specific or unverifiable; the central fact (a triage pass is
not a freedom-to-operate legal opinion) is true of any such skill regardless of its exact
source text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-fto-triage/beat_sheet.json` (7-beat
Teardown skill-teardown, register "Teardown"). Shape and beat count are locked from that
source; this build re-registers the narration to Plain, replaces the cold open with
BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
