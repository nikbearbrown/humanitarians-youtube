# BUILD-LOG — Claude, Signed.

## Decisions

- **Topic → 4 acts:** why a fact is a record not a recollection (Mata v.
  Avianca, the `verified` flag), the three constitutional rules (check
  before searching, unverified by default, append-only), the
  trace-add-sign-and-refuse exercise plus the real worked example, and
  the chapter's own failure table — structured to track the source
  chapter's own Overview → Exercise → Worked Example → What Can Go Wrong
  → Bridge shape, matching the Chapter 6 build's pattern.
- **Source:** `ai1-cli/chapters/07-facts-check-a-claim-record-it-sign-it.md`,
  read in full; cross-checked against the matching research doc and the
  live `ai1-cli/facts/facts.json` (confirmed the Rosser Reeves USP worked
  example is a real entry, not illustrative). See `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card.
- **Card-beat lesson applied from Chapter 6**: act cards given real
  spoken narration and the correct `{title, index}` prop shape from
  authoring time, not discovered as a bug after the fact.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-4, A3-3, A4-3.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-10-04-chapter7/`
  — folder name given explicitly by the human.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **End-card handle lesson applied from Chapter 6**: `shorts.py` bakes
  the Short's silent end-card handle into a PNG at generation time via a
  `--handle` flag (default `@nikbearbrown`), not read dynamically from
  the beat sheet at compile time — will pass `--handle @DivyankSingh`
  explicitly when deriving the Short this time, instead of discovering
  it in the qc-sheet afterward.
- **File-integrity note, carried forward**: the `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session. Renders
  will be spot-checked with `ffprobe` immediately after each compile,
  cross-checked against the beat sheet's own summed duration, and the
  directory listing checked for a stray duplicate before considering a
  build finished.
