# BUILD-LOG — Claude, Shipped.

## Decisions

- **Topic → 4 acts:** GitHub Actions + Pull Requests (the merge gate),
  Environments (the promotion path), Docker + Kubernetes (package +
  orchestrate, including a concrete GKE setup path), Deployment strategies
  (Rolling/Blue-Green/Canary — how you actually expose new code to
  traffic). Chosen to mirror the natural order code actually travels:
  written → gated → promoted → packaged/orchestrated → rolled out.
- **No single source document** — content is general, stable,
  publicly-documented DevOps/cloud-engineering mechanism across GitHub
  Actions, Docker, Kubernetes/GKE, and deployment-strategy theory,
  deliberately kept free of version numbers, pricing, or copy-pasteable
  command syntax to avoid dating the video or making unverifiable claims.
  See `FACTCHECK.md`.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, matching the convention established on the
  `vector-databases` and `chapter-5` builds.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-4, A2-3, A2-5, A4-3, A4-4 (one per act,
  two in Acts II and IV).
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-09-27-gcp-cicd-deployment/`
  — matching the established dated-fellow-report convention.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840).
- **Pre-existing file-integrity note carried forward from the last two
  builds**: this `humanitarians-youtube` folder lives under `Documents`,
  which appears to be cloud-synced (a real iCloud sync-conflict split the
  entire `chapter-5` folder into two directories mid-build in the prior
  session — recovered by consolidating into the complete copy before this
  build started). Renders will be spot-checked with `ffprobe` immediately
  after each compile rather than assumed correct.
