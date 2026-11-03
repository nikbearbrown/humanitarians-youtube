# Rollback Workflow

**Skill:** cli-explainer (`--tool github`) · **Voice:** am_onyx (Darshil)
**Destination:** `darshil-s/2026-09-03-medas-frontend-cicd-rollback-worflow`

## About this video

A companion to [`2026-08-25-medas-frontend-cicd`](../2026-08-25-medas-frontend-cicd/README.md), covering the Rollback workflow added to `medas-aggregation-frontend` (`.github/workflows/rollback.yaml`): how to switch a live environment back to a previously working version without rebuilding anything.

The video covers the workflow's manual `workflow_dispatch` trigger (environment + version, chosen deliberately by a person, never automatic), the two guards that run before anything touches a live service — input validation (the version tag must match the chosen environment) and an Artifact Registry image-exists check — and the final redeploy step, which repoints Cloud Run at an already-built image instead of compiling anything fresh.

Every command and step shown is drawn directly from `docs/rollback-workflow.md` — no placeholder-typo narrative, no screen recordings; every visual is a native Remotion reconstruction of the real material.

## Status

Beat sheet and render not yet in this folder.
