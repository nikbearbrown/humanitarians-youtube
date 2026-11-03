# State Is The Hard Part

- **Status:** draft
- **YouTube:** —
- **Playlist:** Agentic Design Patterns · Part 2 of 3
- **Channel:** @HumanitariansAI · **Voice:** Kokoro `af_sarah`
- **Long:** 3840×2160 · 4:37 — `agentic-design-patterns-part-2.mp4`
- **Short:** 2160×3840 · 1:55 — `short/agentic-design-patterns-part-2-short.mp4`
- **Last updated:** 2026-09-04

## Subject

Patterns 7–13 — multi-agent collaboration, memory, learning, goal monitoring,
exception handling, human-in-the-loop, RAG. Grouped as the source groups them:
orchestration, memory, fail-safes.

The reel argues that all seven are one problem wearing different clothes. State
conflicts, context bloat, poisoned feedback, drift, recovery, suspension, index
drift — every pattern's primary bottleneck is a question about state: who holds
it, how it decays, who may write to it, what happens when it breaks. B11 argues
the case against: one task, one user, one session means skip all seven.

## Change notes

- 2026-09-04 — built and QC'd. Gate V clean (0/0, 30 frames long · 20 short).
  No new components needed — `AgenticPatternDiagram` from Part 1 carried all
  seven topologies on props alone.

## Notes

- **The thesis is ours, not the source's.** "State is the hard part" is a
  synthesis of seven separately-named bottlenecks, not a sentence in Gulli's
  book. Flagged as interpretation in `FACTCHECK.md`; the reel argues it rather
  than asserting it, and a viewer can reject the thesis and still have learned
  all seven patterns. Worth knowing before it ships under your name.
- **Credit:** *Agentic Design Patterns: A Hands-On Guide to Building Intelligent
  Systems* by Antonio Gulli — identical wording to Part 1, by design. On the
  outro card and in `description.txt`.
- **Cut from the source, deliberately:** both formulas (the composite retrieval
  score and the σ drift threshold) and all named vendor technologies (MCP,
  Redis, RabbitMQ, Jira). Reasoning in `PEDAGOGY.md` — at ~20s a beat a formula
  consumes the beat and teaches less than the sentence, and vendor names date a
  video faster than anything else.
- **The Short is purpose-authored, not a `shorts.py` derivative cut** — same
  rationale as Part 1. All seven in brief, funnelling to the long.
- **Short QC needs a workaround.** Gate V's burn-in exclusion is 16:9-only and
  reports false `edge-bleed` BLOCKERs on portrait review cuts. QC the clean cut:
  `final_frame_check.py <dir> --mp4 <clean>.mp4`.

## Prerequisite

Assumes but does not require Part 1 ("The Prompt Is Not The System"). B00
restates the premise in one line for a cold viewer.
