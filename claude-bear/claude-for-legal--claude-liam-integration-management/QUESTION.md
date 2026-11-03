# QUESTION — claude-for-legal--claude-liam-integration-management

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-integration-management/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled), but
its narration text carries **literal, never-filled template placeholders**
(`>`) at every point where the actual skill-specific fact should be —
`"the skill is integration-management. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."` The `source_skill` field it
names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/integration-management/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `integration-management` SKILL.md, no `corporate-legal` folder) — the same
defect class already logged on the `ai-inventory`/`ai-tool-handoff`/
`aia-generation`/`fto-triage`/`gap-surfacer`/`handbook-updates` siblings in
this same factory.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from two facts the
source DID actually fill in (not placeholders): the B00 shot's `output`
array reads `"Post-closing M&A integration tracker — phased workplan,"`
and `BVDT`'s `artifactLines` repeats the identical phrase. Those two lines
are real, load-bearing facts, not template debris — they say plainly what
the skill tracks (a post-closing M&A integration) and how (a phased
workplan). Everything downstream in this script is built from that phrase,
described generically per the fresh-script Phase 1 rule ("when in doubt,
describe behavior generically") rather than inventing a specific tool's UI,
step names, or output format. No fact here is Claude-specific or
unverifiable — it is the general shape of a post-merger-integration
tracking practice (workstream, owner, phase, status) as used in
integration-management work broadly.

**Question this reel actually answers:** The deal just closed. The
instinct is to write an integration PLAN — one document, done once, laying
out what has to happen. What should the team actually build: a plan, or a
tracker?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
