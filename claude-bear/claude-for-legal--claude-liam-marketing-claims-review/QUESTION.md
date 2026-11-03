# QUESTION.md

**Question:** Claude picked up a skill called marketing-claims-review — does
that mean Claude will just tell me whether my ad is legal?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-marketing-claims-review`, a Teardown
skill-explainer under `anthropics/claude-for-legal/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>` is
still present in three places (B00, B03, BHTF), the same unfilled-`>` bug
already documented on the `claude-for-legal--claude-liam-hiring-review`,
`-case-brief`, and `-build-guide` sibling redos. Unlike those siblings,
though, the actual `marketing-claims-review/SKILL.md` IS reachable on this
machine — not at the path the source's `source_skill` metadata names
(`/Users/bear/.../product-legal/skills/marketing-claims-review/SKILL.md`,
which does not exist here), but at
`/Users/nik/Documents/Cowork/anthropics/claude-for-legal/product-legal/skills/marketing-claims-review/SKILL.md`,
a mirrored copy. This redo reads that file directly and fills the `>` gaps
with the skill's real, verifiable content (claim taxonomy, the
substantiation check, the claim-by-claim call format, the "ready to ship"
attorney gate) rather than staying generic. See BUILD-LOG.md.
