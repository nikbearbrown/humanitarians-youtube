# BUILD-LOG — Claude, Compared.

## Decisions

- **Topic → 4 acts:** cost (official per-token pricing across all four
  providers), context window (the convergence near 1M tokens, and what
  still varies), use case (each company's real specialization, framed
  as a deliberate bet rather than a ranking), and open vs. proprietary
  (the clean split that used to exist, vs. the messier 2026 reality of
  Meta running both a closed and an open model at once).
- **No book source this time** — a general, research-centric comparison
  per the human's explicit request, with two comparison axes added
  beyond the four requested (deployment model, and the 2026 open/closed
  licensing shift), per their invitation to add more.
- **Research method**: loaded the `claude-api` skill first (its trigger
  condition — the prompt names Anthropic — fired explicitly) for
  Anthropic's own cached pricing table. For OpenAI, Google, and Meta, an
  initial WebSearch pass surfaced only third-party aggregator sites with
  conflicting numbers for the same models; every number actually used in
  this build was instead verified directly via WebFetch against each
  vendor's own official pricing/docs page. See `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-4, A3-5, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-10-13-llm-apis-compared/`
  — no explicit folder name given, so today's date + a descriptive slug
  was used per standing precedent.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **Image sourcing hit the Commons rate limit again mid-session** —
  handled the same way as the Chapter 9 build: a short wait, then
  resumed. Two candidate images were rejected after visual review (an
  unrecognizable corroded archaeological fragment meant to represent a
  "padlock," and a container-port landscape shot too distant to read as
  a capacity metaphor) and replaced with stronger fits.
- **File-integrity note, carried forward**: the `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session. Renders
  will be spot-checked with `ffprobe` immediately after each compile,
  cross-checked against the beat sheet's own summed duration, and the
  directory listing checked for a stray duplicate before considering a
  build finished.
