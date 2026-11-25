# FACTCHECK — meddas-dev-pipeline-gcp-deployment

Status: self-reported fellow project update. Every claim below is spoken
verbatim from the narration script Darshil supplied on 2026-10-09 describing
his own work on `medas-aggregation-frontend`. No independent audit of the
live GCP project, Artifact Registry, or GitHub Actions configuration was
performed for this reel — unlike `medas-frontend-cicd` and `medas-trust-chain`,
which were reconstructed directly from `DEPLOY.md` / `Dockerfile` /
`deploy-workflow.md`, this reel's source is the fellow's own account of the
system, taken at his word. Mechanism claims are also consistent with what
was independently verified in those two earlier reels (Workload Identity
Federation, Artifact Registry, Cloud Run, tag-triggered deploys).

| # | Beat | Claim (as spoken) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00 | The pipeline covers: containerized, deployed to GCP, secured, automated, rollback-capable | SELF-REPORTED | Fellow-supplied narration script, 2026-10-09 | — |
| 2 | B01 | Multi-stage Docker build: Node/Vite build stage → Nginx runtime stage; final image has no build tools or source, only compiled app + minimal web server; SPA routing configured | SELF-REPORTED, consistent with prior verified reel | Narration script; mechanism matches the Dockerfile shown in `medas-frontend-cicd` B10 (node:20-slim build stage → nginx:1.27-alpine runtime) | — |
| 3 | B02 | Images version-tagged and immutable in Artifact Registry; Cloud Run is fully managed, handles scaling/load balancing/HTTPS automatically | SELF-REPORTED, consistent with prior verified reel | Narration script; matches Artifact Registry + Cloud Run setup shown in `medas-frontend-cicd` B01/B12 | — |
| 4 | B03 | Workload Identity Federation replaces stored service-account keys; short-lived, auto-rotated credentials; IAM scoped to one repository | SELF-REPORTED, consistent with prior verified reel | Narration script; matches the WIF trust chain built and audited in `medas-trust-chain` B02–B05 | — |
| 5 | B04 | Every PR runs lint, automated test suite (Vitest + RTL), and a production build before merge; a tag triggers build→push→deploy with no manual steps | SELF-REPORTED | Narration script. Not independently re-verified against the live `.github/workflows` files for this reel; PR-gate existence is consistent with `medas-ci-rollback`'s stated CI workflow (lint/test/build on PR) per the darshil-s book README | Re-verify against the live workflow YAML before a FELLOWS-SUBMISSION publish if this claim is load-bearing |
| 6 | B05 | A dedicated rollback workflow redeploys any previously validated image without rebuilding; build and deploy are decoupled | SELF-REPORTED, consistent with prior reel | Narration script; matches the rollback workflow covered in `medas-ci-rollback` per the darshil-s book README | — |
| 7 | B06 | The same pipeline drives dev, staging, and production, differentiated only by tag + GitHub Environment config | SELF-REPORTED | Narration script. Dev-only tag/environment behavior was independently shown in `medas-frontend-cicd`/`medas-trust-chain` (tag prefix → env=dev); staging/production parity is the fellow's stated design intent, not independently observed in those two reels | — |
| 8 | B07 | Closing summary: containerized, secure, automated, resilient, scalable | SELF-REPORTED | Narration script — restates B01–B06 | — |

No fabricated incidents, timings, or GCP identifiers appear in this reel — only
the diagram labels needed to stage the narration, all drawn from the script
itself or from the already-verified prior reels in this series.
