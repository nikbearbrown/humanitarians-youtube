# QUESTION.md

**Question (as a viewer would ask it):** "If Claude already looked at this
screenshot once, doesn't sending it again cost nothing?"

**Who asked:** nobody specific — this is a redo-mode reel. `SUBJECT.json`
points at an existing Teardown-register scaffold,
`anthropics/claude-quickstarts/youtube/screenshot-prompt-caching/beat_sheet.json`,
itself built from `computer-use-best-practices/README.md` (Claude Quickstarts,
Anthropic) plus a worked example seed (50-turn task, 5 unique desktop states).
The underlying question is the one a developer hits the first time they watch
a computer-use agent's token bill: repeated screenshots look free because
nothing in the image changed, but the API doesn't know that until told.

**Name usable:** N/A — no individual asker; source is a public quickstart.

**Note on duplication:** the identical underlying facts (same source
directory's numbers: 50 turns, 35 identical repeats, ~2,000 tokens/screenshot,
`cache_control: {"type":"ephemeral"}`, 5 states A–E, 100,000 vs 10,000 tokens,
90% saved) were already built and delivered once before as
`hai-simple/claude-basics--screenshot-prompt-caching` (2026-08-28), from a
*different* source-sheet path
(`anthropics/youtube/claude-basics/screenshot-prompt-caching/`). This is a
second, independently-queued redo target from a different source path, per
the same non-dedup convention documented in
`claude-quickstarts--browser-coordinate-scaling/BUILD-LOG.md`. To avoid a
byte-identical duplicate, this build uses fresh narration, a different
wrong-guess framing (question form, not statement form), and pulls in the
"dialog still open / progress bar still moving" imagery from the original
Teardown source's B01 that the `claude-basics` sibling did not use — while
keeping every number exactly as sourced (they are measured facts, not
illustrative choices, so they are not varied for variety's sake).
