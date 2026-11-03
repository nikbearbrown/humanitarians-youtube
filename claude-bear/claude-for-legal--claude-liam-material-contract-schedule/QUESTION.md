# QUESTION.md

**Question:** Claude picked up a skill called material-contract-schedule —
did it actually learn how to judge which contracts matter in a deal, or is
that not what's going on?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-material-contract-schedule`, a Teardown
skill-explainer under `anthropics/claude-for-legal/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>` is
still present in four places (B00, B03, BVDT, BHTF), and the SKILL.md it was
meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/material-contract-schedule/SKILL.md`)
does not exist on this machine (confirmed: only `youtube/` exists locally
under `anthropics/claude-for-legal/`; no `corporate-legal/` directory).
This is the identical unfilled-`>` gap already documented on the
`claude-for-legal--claude-liam-case-brief` and `...-build-guide` sibling
redos. See BUILD-LOG.md for how this redo handled it: the source's true,
generic argument (what a skill is, how it executes, why it's a
specification with a limit) is preserved and expanded to meet hai-simple's
six-move spine. The one piece of real, non-invented domain knowledge used
as the anchor's flavor is the well-known generic shape of a material
contracts disclosure schedule itself (a document, produced during M&A
diligence, listing contracts material to a deal) — not anything about how
this particular unread SKILL.md implements it. A related research note in
this book's own `youtube/video-ideas.md` (Candidate 11, sourced from
`corporate-legal/README.md`) explicitly EXCLUDES "the disclosure schedule
build" from its own scope — i.e. it documents a sibling skill's mechanism,
not this one's — so that material is not borrowed here either.
