# BUILD-LOG — Claude, Packaged.

## Decisions

- **Topic → 4 acts:** what a course package actually is (Common Cartridge,
  `.imscc` anatomy, 1EdTech rebrand, interoperability), the one build path
  (`build-canvas.sh` → `build-imscc-standard.py`), import and the
  silent-failure risk, and module order as pedagogy — structured to track
  the source chapter's own Overview → Exercise → Worked Example → What
  Can Go Wrong → Bridge shape.
- **Source:** `ai1-cli/chapters/06-export-to-canvas.md`, read in full;
  cross-checked against `ai1-cli/research/06-export-to-canvas.md` and the
  actual `build-canvas.sh` script in the repo. See `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card (now correctly renders
  the handle override added during the FastAPI vs gRPC build).
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-3, A3-3, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-09-20-chapter-6/`
  — folder name given explicitly by the human.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **File-integrity note, carried forward**: this `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session, most
  recently the FastAPI vs gRPC build (both the 16:9 master and the 9:16
  Short were affected). Renders will be spot-checked with `ffprobe`
  immediately after each compile, cross-checked against the beat sheet's
  own summed duration (not just internal consistency), and the directory
  listing checked for a stray duplicate (`<name>1` or `<name>_1`) before
  considering a build finished.
