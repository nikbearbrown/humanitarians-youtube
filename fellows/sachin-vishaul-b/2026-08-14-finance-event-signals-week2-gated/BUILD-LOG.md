# BUILD-LOG — "Claude, Gated." (Week 2)

Session date: 2026-08-31 · Toolkit: `brutalist.art` (cli-explainer skill) ·
Cost: $0.00 · Register: Teardown, claude-liam channel.

## What was built

12-beat `cli-explainer` reel over the real Week 2 build of
`finance-event-signals`. Same Claude-skin/GitHub-skin split as Week 1 (see
that folder's BUILD-LOG.md for the shared toolkit fixes — the `npx` PATH
shim, the QC burn-in exclusion fix, and the em-dash encoding bug that made
Kokoro spell out "circumflex euros" — all found and fixed once and applied
to every reel in this batch, this one included).

## Content-specific note

The LangGraph `{}`-return bug (B05/B06) and its fix landed in the *same*
commit in the source repo — unlike Week 1's two-commit diff, there was no
"before" version to show as a real diff. Resolved by showing the real
current fixed line (which carries its own inline comment naming the bug)
rather than inventing a fabricated buggy snippet.

## Known gaps in this submission

- **9:16 cut not built.**
- **PROOF-REVIEW: pending.**
