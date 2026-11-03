# QUESTION — claude-for-legal--claude-liam-memo

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-memo/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-26), but its narration text carries **literal, never-filled template
placeholders** (`>`) at every point where the actual skill-specific fact
should be — `"The skill is memo. >."`, `"Claude's job: >."`, `"The SKILL.md
is the spec — >."`, `"I want to >. Read the memo skill and walk me through
what you will do before you do it."` The `source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/memo/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `memo` SKILL.md, no `legal-clinic` folder). So there are no real facts to
carry over: the source is a teardown-format shell that was never actually
authored — the identical defect class already logged for the
`claude-for-legal--claude-liam-board-minutes`, `-ai-tool-handoff`,
`-ai-inventory`, and `-dsar-response` siblings in this same batch.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("MEMO") into a generic, defensible account of what a legal memo actually
is and what a drafting handoff to Claude can and can't finish by itself —
described generically per the fresh-script Phase 1 rule ("when in doubt,
describe behavior generically") rather than inventing a specific skill's
steps, UI, or product claims. The one fact this reel leans on — that a
legal memo is a predictive, internal analysis of law applied to facts (an
issue-rule-application-conclusion draft), not a final verified opinion, and
that its citations are conventionally checked against current law before
anyone relies on it — is ordinary legal-practice convention, not a
Claude-specific or unverifiable claim.

**Question this reel actually answers:** If Claude drafts a legal memo that
reads confidently and cites real cases, is that memo ready to rely on, or
does something else still have to happen first?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
