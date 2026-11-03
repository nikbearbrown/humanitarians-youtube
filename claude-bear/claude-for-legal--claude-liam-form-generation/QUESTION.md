# QUESTION.md

**Question:** Claude picked up a "skill" called form-generation — did it
learn to draft legal forms, or is that not what's going on?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-form-generation`, a Teardown
skill-explainer under `anthropics/claude-for-legal/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>` is
still present in four places (B00, B03, BVDT, BHTF), identical to the
already-documented gap on the `claude-for-legal--claude-liam-case-brief`
sibling redo. The SKILL.md form-generation was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/
claude-for-legal/legal-clinic/skills/form-generation/SKILL.md`) does not
exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about which fields form-generation's particular
legal-clinic procedure actually fills or how. This redo treats
"form-generation" literally and generically — the named example of a
skill-shaped folder, using only the well-known, generic shape of a
fillable legal form (a fixed set of fields — parties, dates, signatures —
filled from case facts) as anchor flavor — and never asserts an invented
procedure from the unread SKILL.md. Logged in SCRIPT.md and BUILD-LOG.md
as well.
