# QUESTION — claude-for-legal--claude-liam-dsar-response

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-dsar-response/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-07-25), but its narration text carries **literal, never-filled
template placeholders** (`>`) at every point where the actual skill-specific
fact should be — `"The skill is dsar-response. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` The `source_skill` field
it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/privacy-legal/skills/dsar-response/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `dsar-response` SKILL.md, no `privacy-legal` folder). So there are no
real facts to carry over: the source is a Teardown-format shell that was
never actually authored — the same source-gap already logged for the
sibling `claude-for-legal--claude-liam-amendment-history` /
`-ai-inventory` / `-ai-tool-handoff` / `-aia-generation` / `-board-minutes`
redos in this same family.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("DSAR RESPONSE") and the family (`claude-for-legal`, a privacy-legal skill
set) into a generic, defensible account of what responding to a Data
Subject Access Request actually requires — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically")
rather than inventing a specific tool's UI, output format, or undocumented
behavior. No fact here is Claude-specific or unverifiable; it is the
ordinary shape of a DSAR response: a person asks an organization what
personal data it holds on them, the organization must search every system
that could hold a record under every identifier the person has used, and
must send back only that person's data — not anyone else's mixed into the
same record.

**Question this reel actually answers:** A person asks a company what
personal data it holds on them. Where does the company need to look, and
what has to happen before the answer goes back to them?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
