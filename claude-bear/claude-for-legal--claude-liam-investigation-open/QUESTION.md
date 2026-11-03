# QUESTION.md

**Question:** Claude picked up a skill called investigation-open — does that
mean Claude itself decides when a workplace issue becomes a formal
investigation?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-investigation-open`, a Teardown
skill-teardown format under `anthropics/claude-for-legal/`). Not a live
viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in three beats (B00, B03, BVDT), matching the identical
unfilled-`>` bug already documented on the `claude-for-legal--claude-liam-
case-brief`, `-hiring-review`, `-internal-investigation`, and
`-investigation-add` sibling redos. The SKILL.md investigation-open was
meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-
legal/employment-legal/skills/investigation-open/SKILL.md`) does not exist
on this machine (confirmed: only `youtube/` exists locally under
`anthropics/claude-for-legal/`; no `employment-legal/` directory).

One genuine fact fragment survived the placeholder bug intact, repeated
verbatim in both B00's `output` prop and BVDT's `artifactLines`: **"Open a
new internal investigation matter — runs intake,"** (the sentence is itself
cut off mid-thought in the source, but the surviving clause is unambiguous
and consistent across both beats). That single fact — investigation-open
creates a new matter record and runs an intake step — is the only
investigation-open-specific claim this redo asserts. Everything else about
the actual employment-law intake procedure inside the unread SKILL.md is
left unclaimed. See BUILD-LOG.md for how this redo handled the gap.
