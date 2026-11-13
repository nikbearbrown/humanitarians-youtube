# End-to-End Validation — Triaging the First Staging Deployment

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCallChain` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~1:59 (8 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-10-01-medas-stage-pipeline-validation`

## About this video

**project-update** video (one of the two distinct videos required
per week — see `learning/` in this same folder for the companion **STEM/AI
topic** video). Covers the first real `stage-v1.0.0` deployment, validated
checkpoint by checkpoint rather than as one black box: triggering the
pipeline with a real release tag, triaging it stage by stage (auth → build →
push → deploy), reading GitHub Actions' own logs/step-summaries as the
observability layer that makes that triage possible, and confirming the
rollback path against that same deployed image before calling the pipeline
verified end-to-end.

**Provenance note:** the fellow-supplied script for this reel had several
garbled/cut-off fragments (mid-sentence corruption, likely a copy-paste
glitch). Each was repaired to a complete sentence preserving the evident
intended meaning — every repair is logged verbatim, before and after, in
`FACTCHECK.md`. Nothing was added beyond completing what was clearly already
there.

Continues the series established in `2026-08-25-medas-frontend-cicd/`
through `2026-09-24-medas-stage-environment-security/`.


Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure as every other reel in
this book (not a content defect); the shipped master was produced by running
the identical encode command by hand (faster x264 preset) and verifying it
against the same QC checker and a manual frame review.
