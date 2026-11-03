# QUESTION — claude-for-legal--claude-liam-nda-review

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-nda-review/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-26), but its narration text carries **literal, never-filled template
placeholders** (`>`) at every point where the actual skill-specific fact
should be — `"The skill is nda-review. >."`, `"Claude's job: >. What it gets
right: repeatable results. What it bites: anything outside the spec."`,
`"nda-review makes Claude execute one task reliably. The SKILL.md is the
spec — >."`, `"I want to >. Read the nda-review skill and walk me through
what you will do before you do it."` The `source_skill` field it names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/nda-review/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `nda-review` SKILL.md, no `commercial-legal` or `bear-textbooks` folder).
So there are no real facts to carry over: the source is a teardown-format
shell that was never actually authored — the identical defect class already
logged for the `claude-for-legal--claude-liam-memo`, `-board-minutes`,
`-ai-tool-handoff`, `-ai-inventory`, and `-dsar-response` siblings in this
same batch.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("NDA REVIEW") into a generic, defensible account of what reviewing a
non-disclosure agreement actually involves and what a Claude-assisted
first pass can and can't finish by itself — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically")
rather than inventing a specific skill's steps, UI, or product claims. The
facts this reel leans on are ordinary contract-drafting convention, not a
Claude-specific or unverifiable claim: a confidentiality clause
conventionally carries carve-outs (information that's already public,
independently developed, already known, or required to be disclosed by
law); what counts as a reasonable duration or scope for those carve-outs
varies by jurisdiction and deal; and a document-level pass can compare
clauses against a standard baseline, but cannot itself render a legal
opinion on enforceability.

**Question this reel actually answers:** If Claude reviews an NDA and
nothing comes back flagged, does that mean the NDA is safe to sign?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
