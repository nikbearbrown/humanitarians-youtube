# QUESTION.md

**Question:** Can Claude approve my leave request, or just check it?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's
`leave-tracker` skill for employment-legal / HR work).

**Name usable:** N/A.

**Source-gap finding (logged, not asked):** the source sheet is fully "built" (7 beats,
all marked VIDEO/filled, dated 2026-07-25) but its narration text carries literal,
never-filled template placeholders (`>`) at every point where the actual skill-specific
fact should be:

- B00: `"The skill is leave-tracker. >. A SKILL.md tells Claude exactly how."`
- B03: `"Claude's job: >. What it gets right: repeatable results. What it bites:
  anything outside the spec."` (`SkillTeardownMechanism.body` is the literal string `">"`)
- BVDT: `"The SKILL.md is the spec — >. Same input, same output, every run."`
  (`ClaudeVerdictArtifact.artifactLines` includes a bare `">"`)
- BHTF: `"Paste this into Claude: 'I want to >. Read the leave-tracker skill...'"`

Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/leave-tracker/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an
`employment-legal` folder exists anywhere. So there were no real facts to carry over
beyond the topic (LEAVE-TRACKER, an Anthropic skill for employment-legal/HR work — file
size 1k per the source's own `SkillTeardownAnatomy` props, which was already filled, not
a placeholder) and the shape (Teardown skill-teardown format, 7 beats: cold open,
anatomy, pipeline, design tell, verdict, handoff, outro) — same defect class as the
`clearance`/`ai-inventory`/`ai-tool-handoff`/`aia-generation`/`amendment-history`
siblings already delivered in this family.

**The call:** reconstructed a generic, defensible account of what a leave-tracker skill
does — checking a requested or logged absence against the leave policy a SKILL.md
specifies (accrual, eligibility windows, blackout dates) and returning a structured
report that flags anything outside the policy — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing a specific jurisdiction's leave law, a specific HRIS integration, or an
approval outcome. No fact in the resulting script is Claude-specific or unverifiable;
the central fact (a policy check is not an approval decision) is true of any such skill
regardless of its exact source text.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/claude-for-legal/youtube/claude-liam-leave-tracker/beat_sheet.json` (7-beat
Teardown skill-teardown, register "Teardown"). Shape and beat count are locked from that
source; this build re-registers the narration to Plain, replaces the cold open with
BrutalistHesitantWriter, and reskins the close to Humanitarians AI.
