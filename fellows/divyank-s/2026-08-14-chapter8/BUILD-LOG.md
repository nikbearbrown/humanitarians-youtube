# BUILD-LOG — Claude, Cut.

## Decisions

- **Topic → 4 acts:** the three-part method + the correctly-attributed
  "murder your darlings" maxim, cutting per the plan + the real
  disposition numbers, the exclusion log's four fields + the real
  demote-not-cut worked example + resolving disagreement explicitly, and
  the chapter's own failure table + bridge to Chapter 9.
- **Source:** `ai1-cli/chapters/08-cut-to-the-blueprint.md`, read in
  full; cross-checked against the matching research doc and — one level
  deeper than usual — the actual GATE 0 disposition table in
  `chapters/01-inventory-research-blueprint-signoff.md`, to confirm the
  "21/2/1/0" numbers and the school-apparatus global cut independently
  rather than trusting Chapter 8's own restatement of them. See
  `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card.
- **A1-1 image rejected and re-sourced mid-build**: the first pruning-
  shears candidate turned out to be a cluttered store-shelf display with
  visible price tags; swapped for a clean, in-use product photo.
- **A4-1 metaphor pivoted during sourcing**: planned as a frayed/broken
  rope, but reliable rope photos weren't findable; pivoted to an
  incomplete jigsaw puzzle with a visible gap — a stronger, cleaner fit
  for "something missing leaves a visible gap" anyway.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-4, A3-4, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-08-14-chapter8/`
  — folder name given explicitly by the human.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **A beat-sheet authoring bug caught before rendering**: beat A4-3 had
  copy-pasted Act III's label instead of Act IV's; caught and fixed
  during the SOURCES.md review pass, before any audio or render spend.
- **File-integrity note, carried forward**: the `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session. Renders
  will be spot-checked with `ffprobe` immediately after each compile,
  cross-checked against the beat sheet's own summed duration, and the
  directory listing checked for a stray duplicate before considering a
  build finished.
