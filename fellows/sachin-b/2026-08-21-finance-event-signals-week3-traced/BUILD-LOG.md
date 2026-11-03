# BUILD-LOG — "Claude, Traced." (Week 3)

Session date: 2026-08-31 · Toolkit: `brutalist.art` (cli-explainer skill) ·
Cost: $0.00 · Register: Teardown, claude-liam channel.

## What was built

12-beat `cli-explainer` reel over the real Week 3 build of
`finance-event-signals`. Same Claude-skin/GitHub-skin split and shared
toolkit fixes as Weeks 1-2 (see Week 1's BUILD-LOG.md for the `npx` PATH
shim, QC burn-in mask, and em-dash audio-encoding bug — all fixed once,
applied to this reel too).

## Content-specific note

Like Week 2's LangGraph bug, the `topic-init` readiness-probe fix landed in
the same commit as the original k8s manifest — B06 shows the real current
fix (an `until rpk topic list …` wait loop) rather than a fabricated
"before" YAML.

## The strongest disclosed limit in the whole series

B08 is not manufactured tension — it's the project's own recorded finding
that the HPA never demonstrated a scale-out event, with the reason
(workload too short for the metrics evaluation window) stated plainly.

## Known gaps in this submission

- **9:16 cut not built.**
- **PROOF-REVIEW: pending.**
