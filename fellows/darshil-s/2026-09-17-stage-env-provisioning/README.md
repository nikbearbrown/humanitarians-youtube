# Stage Environment: Provisioning GCP and GitHub

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCodeViewer` / `GitHubCallChain` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~2:50 (10 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-09-17-medas-stage-environment-provisioning`

## About this video

Week 2's **project-update** video (one of the two distinct videos required
per week — see `learning/` in this same folder for the companion **STEM/AI
topic** video). Implementation only, by design: this reel assumes the
underlying concepts (what WIF/IAM/CI-CD/Cloud Run are) are already covered by
last week's and this week's learning videos, and shows only what was actually
done to provision a stage environment that mirrors dev:

1. A dedicated `medas-frontend-stage` Artifact Registry repo.
2. Widening the existing WIF provider's trust condition (no new pool) to
   also accept stage-environment runs.
3. An IAM binding scoped to the stage GitHub Environment's principal set
   specifically — not the whole repository — keeping dev and stage
   cryptographically separated on one shared service account.
4. A new GitHub `stage` Environment: the same two secrets as dev, and six
   variables, three of which actually differ (`REPOSITORY`, `SERVICE`,
   `API_URL`).
5. Two validation runs: a real `stage-v0.1.0` tag deploy, then a rollback
   run against that same tag with `environment: stage`.

Narration is authored from the fellow-supplied Week 2 scope (provided
2026-09-17) — see `FACTCHECK.md` for the honest self-reported/derived split.
Continues the series established in `2026-08-25-medas-frontend-cicd/`,
`2026-08-31-medas-ci-rollback/`, `2026-08-31-medas-trust-chain/` and
`2026-10-09-meddas-dev-pipeline-gcp-deployment/`.



## Rebuilding this video

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
python3 runtime/scripts/generate_audio_kokoro.py ../BrutalistVideo/darshil-s/2026-09-17-medas-stage-environment-provisioning
python3 runtime/scripts/remotion_scenes.py       ../BrutalistVideo/darshil-s/2026-09-17-medas-stage-environment-provisioning
./art final ../BrutalistVideo/darshil-s/2026-09-17-medas-stage-environment-provisioning
```

Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure seen on the two prior
reels (not a content defect); the shipped master was produced by running the
identical encode command by hand and verifying it against the same QC
checker and a manual frame review.
