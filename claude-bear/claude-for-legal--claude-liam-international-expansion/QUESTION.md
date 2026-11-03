# QUESTION — claude-for-legal--claude-liam-international-expansion

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-international-expansion/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-08-03), but its narration text carries **literal, never-filled
template placeholders** (`>`) at every point where the actual skill-specific
fact should be — `"The skill is international-expansion. >."`, `"Claude's
job: >."`, `"The SKILL.md is the spec — >."`, `"I want to >."` The
`source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/international-expansion/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `international-expansion` SKILL.md, no `employment-legal` folder under
`claude-for-legal`). So there are no real facts to carry over: the source is
a teardown-format shell whose skill-specific content was never actually
authored. (Same defect class already found and logged in this family's
`claude-liam-ai-inventory` redo — see that reel's QUESTION.md/BUILD-LOG.md.)

**What the source DOES give us:** the metadata's one substantive line —
`"Reference: implementation-planning framework for international hiring."`
— plus the topic label `INTERNATIONAL-EXPANSION · ANTHROPIC SKILL`. That's
enough to identify the domain unambiguously: a legal/HR team's first hire in
a country they haven't operated in before, and the planning work that has to
happen before an offer goes out.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject into a generic,
defensible account of what actually has to be decided before a first
international hire — worker classification and choice of legal employer —
described generically per the fresh-script Phase 1 rule ("when in doubt,
describe behavior generically") rather than inventing a specific product's
screens, checklist fields, or output format. No fact here is Claude-specific
or unverifiable; it is the general shape of an international-hiring
implementation plan (classify the role, decide who the legal employer is,
attach the country's mandatory terms) as used in employment-law practice
broadly.

**Question this reel actually answers:** A team is about to hire its first
person in a country it has never operated in. The instinct is to draft an
employment contract like always. What actually has to be decided first?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
