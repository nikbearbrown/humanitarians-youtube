# BUILD-LOG — Claude, Converted.

## Decisions

- **Topic → 4 acts:** the four conversion maps + the FTC legal edge
  (stated once), directing (not delegating) two conversions, the real
  three-way worked example + GATE 3, and the chapter's own failure table
  + bridge to Chapter 10 — structured to track the source chapter's own
  Overview → Exercise → Worked Example → What Can Go Wrong → Bridge
  shape.
- **Source:** `ai1-cli/chapters/09-convert-what-survives.md`, read in
  full; cross-checked against the matching research doc. See
  `FACTCHECK.md`.
- **Honesty constraint carried through**: the chapter's worked example
  is real (a live agent conversion) but deliberately omits a fabricated
  human rewrite. This build's narration (A3-2, A3-3) preserves that
  honesty rather than inventing one.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-4, A3-4, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-10-13-chapter9/`
  — no explicit folder name given this time, so today's date was used
  per standing precedent.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **Image sourcing was unusually difficult this build**: a "stencil"
  metaphor candidate turned out to be vulgar graffiti on review and was
  rejected; a ship's wheel candidate turned out to be a decorative
  chandelier, not a usable helm photo; a conductor photo was rejected
  for depicting an identifiable named individual (consistent with this
  session's standing rule against decorative use of named real people);
  and the Wikimedia Commons API itself rate-limited mid-session,
  requiring a short wait before retrying. Settled on 4 VOX images
  (14.3%) rather than force a weak fifth image to hit the usual
  15–30% quota.
- **File-integrity note, carried forward**: the `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session. Renders
  will be spot-checked with `ffprobe` immediately after each compile,
  cross-checked against the beat sheet's own summed duration, and the
  directory listing checked for a stray duplicate before considering a
  build finished.
