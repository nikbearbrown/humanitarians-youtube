# QUESTION.md

**Question:** Claude picked up a skill called investigation-summary — does it
write one summary of the investigation, or does something else happen?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-investigation-summary`, a Teardown
skill-explainer under `anthropics/claude-for-legal/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>` is
still present in four places (B00, B03, BVDT, BHTF), the identical unfilled-
`>` bug already documented on the `claude-for-legal--claude-liam-case-brief`
and `claude-for-legal--claude-liam-build-guide` sibling redos. The SKILL.md
investigation-summary was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/investigation-summary/SKILL.md`)
does not exist on this machine (confirmed: only `youtube/` exists locally
under `anthropics/claude-for-legal/`; no `employment-legal/` directory). One
real, filled fact DOES survive the source, unlike the fully-blank case-brief
gap: the skill's one-line job description, present verbatim in the source's
B00 output lines and metadata — "Draft an audience-specific summary from the
privileged investigation." This redo builds its whole argument from that one
sentence plus the generic, verifiable mechanics of any Claude skill (folder +
SKILL.md, read-then-execute, specification semantics) — never inventing a
specific procedural step from the unread SKILL.md. See BUILD-LOG.md.
