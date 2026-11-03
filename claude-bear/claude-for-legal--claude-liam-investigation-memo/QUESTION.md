# QUESTION.md

**Question:** Claude picked up a skill called investigation-memo — does that
mean Claude itself now has judgment about what happened in the investigation?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-investigation-memo`, a Teardown
skill-explainer under `anthropics/claude-for-legal/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific fill. A literal `>` placeholder survives verbatim in two
places (B03's `body`, BHTF's `command`), and a second, related defect sits
in B00's `output` line and BVDT's `artifactLines`: the sentence "Draft or
update the privileged investigation memo from the." is truncated
mid-clause, never completed. This is the identical unfilled-source bug
already documented on the `claude-for-legal--claude-liam-hiring-review`,
`claude-for-legal--claude-liam-case-brief`, and `claude-for-legal--claude-
liam-build-guide` sibling redos. The SKILL.md investigation-memo was meant
to describe (`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/
claude-for-legal/employment-legal/skills/investigation-memo/SKILL.md`) does
not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`employment-legal/` directory).

This redo preserves every fact the source DOES establish (a skill is a
folder Claude reads before it acts; the whole routine lives in one file,
SKILL.md; Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers) and treats "investigation-memo" only as the named
example of a skill-shaped folder aimed at writing up an investigation in a
fixed structure. No specific claim about what investigation-memo's
particular employment-legal procedure or memo template actually contains is
asserted anywhere. See BUILD-LOG.md for the full account.
