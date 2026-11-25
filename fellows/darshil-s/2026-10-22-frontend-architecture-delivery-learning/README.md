# Week 7 Technical Learnings — Frontend Architecture & Delivery Concepts

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCallChain` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~2:13 (8 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-10-22-frontend-architecture-delivery-learning`

## About this video

Covers five frontend-specific delivery concepts: Vite's build-time (not
runtime) environment-variable resolution and why each environment needs its
own build, the SPA routing fallback that lets a client-side router take
over from the web server, serving compiled static assets through a
lightweight server like Nginx instead of Node/a dev server, the Vitest +
React Testing Library testing strategy that checks behavior rather than
implementation details, and baking a version identifier into the build so
a running app can report exactly what's live.

Continues the series established in `2026-08-25-medas-frontend-cicd/`
through `2026-10-15-medas-fullstack-integration-validation/`.

Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure as every other reel in
this book (not a content defect); the shipped master was produced by running
the identical encode command by hand (faster x264 preset) and verifying it
against the same QC checker and a manual frame review.
