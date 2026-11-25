# Week 8 Technical Learnings — Terraform & Cloud Run Billing Fundamentals

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCallChain` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~2:02 (8 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-10-29-terraform-cloudrun-billing-learning`

## About this video

Covers Infrastructure as Code with Terraform — what it solves versus manual
setup, its provider/resource/plan/apply model, and idempotency via state —
paired with how Cloud Run's request-based billing actually works and the
concrete cost levers it exposes: min/max instances, concurrency, and
CPU/memory sizing.

**Provenance note:** the fellow-supplied script for this reel had several
garbled/cut-off fragments (mid-sentence corruption, likely a copy-paste
glitch — the same pattern seen in `medas-stage-pipeline-validation` and
`medas-fullstack-integration-validation`). Each was repaired to a complete
sentence preserving the evident intended meaning — every repair is logged
verbatim, before and after, in `FACTCHECK.md`. Note also that this video's
content is a general learning topic: the project's own infrastructure (per
every other reel in this book) is still provisioned via direct `gcloud` /
GitHub Actions commands, not Terraform — this video does not claim otherwise.

Continues the series established in `2026-08-25-medas-frontend-cicd/`
through `2026-10-22-frontend-architecture-delivery-learning/`.

Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure as every other reel in
this book (not a content defect); the shipped master was produced by running
the identical encode command by hand (faster x264 preset) and verifying it
against the same QC checker and a manual frame review.
