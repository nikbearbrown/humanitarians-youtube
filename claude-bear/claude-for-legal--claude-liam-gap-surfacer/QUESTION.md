# QUESTION — claude-for-legal--claude-liam-gap-surfacer

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-gap-surfacer/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled,
dated 2026-07-25), but its narration text carries **literal, never-filled
template placeholders** (`>`) at every point where the actual skill-specific
fact should be — `"Claude's job: >."`, `"the SKILL.md is the spec — >."`,
`"I want to >."` The `source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/gap-surfacer/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `gap-surfacer` SKILL.md, no `regulatory-legal` folder). The book's own
audit files confirm this independently: `_audit/audit_results.csv` and
`_audit/REBUILD-WORKLIST.csv` both flag this exact sheet with
`no-FACTCHECK`. So there are no real facts to carry over: the source is a
teardown-format shell whose skill-specific content was never actually
authored — the same defect already found and logged in this factory for
the sibling `claude-liam-ai-inventory` redo.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the skill's name
— "gap-surfacer" — into a generic, defensible account of what that kind of
task pattern does: compare a checklist of things a document is supposed to
contain against the document itself, and report the items that have no
matching text — the gaps. Described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing this specific skill's exact steps, output format, or trigger
phrases. No fact here is Claude-specific or unverifiable; it is the general
shape of a checklist-vs-document gap check, illustrated with an ordinary
legal example (a contract missing a standard clause).

**Question this reel actually answers:** When a tool like this reviews a
contract against a checklist and reports nothing wrong with an item, what
does that silence actually mean — and what's the one thing people guess
wrong about what this kind of check is even looking for?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
