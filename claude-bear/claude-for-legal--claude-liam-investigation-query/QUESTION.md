# QUESTION.md

**Question:** Claude picked up a skill called investigation-query — does
that mean Claude itself can work out what actually happened, cross-
referencing witness accounts and judging who's telling the truth?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-investigation-query`, a Teardown
skill-teardown format under `anthropics/claude-for-legal/`). Not a live
viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in two beats (B03, BHTF), matching the identical
unfilled-`>` bug already documented on the `claude-for-legal--claude-liam-
case-brief`, `-hiring-review`, `-internal-investigation`, `-investigation-
add`, `-investigation-open`, and `-investigation-memo` sibling redos. The
SKILL.md investigation-query was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/investigation-query/SKILL.md`) does not exist
on this machine (confirmed: only `youtube/` exists locally under
`anthropics/claude-for-legal/`; no `employment-legal/` directory).

One genuine fact fragment survived the placeholder bug intact, repeated
verbatim in both B00's `output` prop and BVDT's `artifactLines`: **"Ask
questions against an open investigation log — what witnesses said,"** (the
sentence is itself cut off mid-thought in the source, but the surviving
clause is unambiguous and consistent across both beats). That single fact —
investigation-query searches/answers questions against an existing
investigation log, for example what a given witness said — is the only
investigation-query-specific claim this redo asserts. Everything else about
the actual employment-law query procedure inside the unread SKILL.md is left
unclaimed. See BUILD-LOG.md for how this redo handled the gap.
