# BUILD-LOG — Claude, Dispatched.

## Decisions

- **Topic → 4 acts:** core architecture (protocol/payload/origin), the
  gateway/BFF pattern (the actual answer to "why two API services" — not
  duplication, division of labor), use cases including IoT/streaming, and
  the honest tradeoffs (browser/gRPC-Web gap, debuggability vs.
  performance). Structured to directly answer every point the human asked
  for, plus additional depth volunteered per their explicit invitation to
  add more and go research-centric.
- **No single source document** — content is general, stable,
  publicly-documented software-architecture knowledge, deliberately kept
  free of version numbers, benchmark percentages, and named third-party
  product claims. See `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-3, A2-5, A4-3, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-10-04-fastapi-vs-grpc/`
  — matching the established dated-fellow-report convention (no explicit
  location given this time, per standing precedent).
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session (no explicit spec restated this time either).
- **File-integrity note, carried forward**: this `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on two of the last three builds
  (`chapter-5`, `gcp-cicd-deployment`) — both recovered by consolidating
  into the complete copy. Renders will be spot-checked with `ffprobe`
  immediately after each compile, and the directory listing checked for a
  stray duplicate (`<name>1` or `<name>_1`) before considering a build
  finished.
