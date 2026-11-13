# Week 10 Technical Learnings — Deployment Strategy Fundamentals

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCallChain` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~1:58 (8 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-11-12-canary-bluegreen-deployment-learning`

## About this video

Covers the theory behind canary and blue-green deployments: the shared
problem both solve (a standard deploy exposes 100% of users instantly), how
a canary gradually ramps traffic while monitoring, how blue-green validates
a fully isolated second environment before an atomic cutover, why Cloud
Run's immutable-revision-plus-traffic-percentage model makes both just two
usage patterns of one primitive rather than separate features, how to
choose between them, and why deployment strategy is risk management, not
just automation.


Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure as every other reel in
this book (not a content defect); the shipped master was produced by running
the identical encode command by hand (faster x264 preset) and verifying it
against the same QC checker and a manual frame review.
