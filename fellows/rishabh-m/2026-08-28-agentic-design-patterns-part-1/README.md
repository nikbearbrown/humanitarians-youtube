# The Prompt Is Not The System

- **Status:** draft
- **YouTube:** —
- **Playlist:** Agentic Design Patterns · Part 1 of 3
- **Channel:** @HumanitariansAI · **Voice:** Kokoro `af_sarah`
- **Long:** 3840×2160 · 4:30 — `agentic-design-patterns-part-1.mp4`
- **Short:** 2160×3840 · 1:39 — `short/agentic-design-patterns-part-1-short.mp4`
- **Last updated:** 2026-08-28

## Subject

The first six agentic design patterns — prompt chaining, routing,
parallelization, reflection, tool use, planning. The through-line is that a
prompt failing in production is an architecture problem, not a prompting one,
and that every pattern buys reliability by charging you in latency or tokens.

Body beats each carry the pattern's honest cost: the 3–5 step ceiling, the
router as a single point of failure, the rate limiter, the uncapped critic loop,
the tool-use security surface, the undebuggable dependency graph. B10 argues the
case *against* the whole set — one step, deterministic output, or a waiting user
means a single call is better engineering.

## Change notes

- 2026-08-28 — built and QC'd. Gate V clean (0 BLOCKER / 0 MAJOR, 28 frames).
  Short authored, not derived — see Notes.

## Notes

- **Credit is required on publication.** Concepts come from *Agentic Design
  Patterns: A Hands-On Guide to Building Intelligent Systems* by Antonio Gulli.
  Carried on the outro card and in `description.txt`. **Use the identical
  wording on Parts 2 and 3** — retrofitting a changed credit across three
  published reels is the avoidable mistake.
- **Assorted YouTube explainers informed the notes but are deliberately not
  cited** — not individually identifiable, and no claim traces to any one of
  them. Reasoning recorded in `SOURCES.md`.
- **The Short is purpose-authored, not a `shorts.py` derivative cut.** The
  toolkit's Shorts law says drop beats, never re-author. But dropping beats from
  a six-pattern argument leaves an arbitrary subset and a broken premise, so the
  Short covers all six in brief and funnels to the long. Deliberate deviation.
- **Two components were built for this reel** and now live in the shared
  toolkit: `AgenticPatternDiagram` (parameterized flow diagram, all six
  topologies) and `HaiTitleOutro`. The latter exists because `ClaudeTitleOutro`
  hardcodes `@NikBearBrown` with no override — there was no compliant outro for
  this channel.
- **Short QC needs a workaround.** Gate V's burn-in exclusion is 16:9-only, so
  it reports false `edge-bleed` BLOCKERs on every portrait review cut. QC the
  clean cut instead: `final_frame_check.py <dir> --mp4 <clean>.mp4`.
