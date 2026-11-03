# The Constraints Are The Design

- **Status:** draft
- **YouTube:** —
- **Playlist:** Agentic Design Patterns · Part 3 of 3 (finale)
- **Channel:** @HumanitariansAI · **Voice:** Kokoro `af_sarah`
- **Long:** 3840×2160 · 5:00 — `agentic-design-patterns-part-3.mp4`
- **Short:** 2160×3840 — `short/agentic-design-patterns-part-3-short.mp4`
- **Last updated:** 2026-09-11

## Subject

Patterns 14–20 — inter-agent communication, resource-aware optimization, tree of
thoughts, evaluation and monitoring, guardrails, prioritization, exploration —
closing with the source's five-step interview blueprint.

The reel inverts the series. Parts 1 and 2 taught patterns that *add*
capability; these seven take it away on purpose, and that subtraction is what
turns a demo into production. B10 is the payoff beat the other two parts do not
have: the only beat in three videos that says what to *do* rather than what
something *is*.

## Change notes

- 2026-09-11 — built and QC'd. Gate V clean (0/0, 30 frames). No new components
  — third reel carried by `AgenticPatternDiagram` on props alone, including
  B10's blueprint chain.

## Notes

- **The thesis is ours, not the source's.** "These seven subtract capability on
  purpose" is a synthesis. Closer to the source than Part 2's was — its own
  opening names "production constraints, safety guardrails, cost-resource
  trade-offs" as the expert/intermediate divide — but the framing is ours.
  Flagged in `FACTCHECK.md`.
- **Credit:** *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
  Systems* by Antonio Gulli — identical wording to Parts 1 and 2, as planned
  from the start of the series.
- **Cut deliberately:** the priority-score formula (consistent with Part 2's
  formula cuts), BFS/DFS search algorithms, and named model families ("o1/o3-class"
  → "Reasoning · expensive"). Reasoning in `PEDAGOGY.md`.
- **One source error not propagated:** §P16 writes "BFS (Breaded-First Search)"
  for Breadth-First Search. Search algorithms were cut as extraneous, so it never
  reached the screen. Worth correcting in the notes if you expand that section.
- **"Over 50% cost reduction" softened** to "can halve the bill" — the source
  asserts it with no checkable citation.
- **The Short is purpose-authored**, not a `shorts.py` derivative cut — same
  rationale as Parts 1 and 2. It keeps the blueprint beat.
- **Short QC needs a workaround.** Gate V's burn-in exclusion is 16:9-only and
  false-flags portrait review cuts. QC the clean cut:
  `final_frame_check.py <dir> --mp4 <clean>.mp4`.

## Series

Closes the three-part arc: architecture (Part 1) → state (Part 2) → constraints
(Part 3). Watchable cold — B00 restates the arc in two lines — but B12 and B14
close all twenty patterns, so it lands hardest last.
