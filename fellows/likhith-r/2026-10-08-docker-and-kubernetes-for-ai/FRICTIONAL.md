# Frictional Log — Docker and Kubernetes for AI

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-08 — Build a 60-second explainer on Docker and Kubernetes for AI workloads, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected containers to make a model run identically everywhere, and Kubernetes to simply run Docker at scale. I also wanted this video to land at exactly 60 seconds.

- **Where it resisted, and what I did next:**
  The docs corrected both of my assumptions: containers share the host kernel and GPU containers need the host's driver, and Kubernetes doesn't need the Docker Engine. Hitting exactly 60 seconds took me several rounds of trimming and timing. The type-lock check also flagged outlined pills and nested boxes, which I had redesigned.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, checked the claims against the Docker, NVIDIA and Kubernetes docs, and fixed what the checks found. I asked for "AI" instead of "A I" after hearing how the voice said it, and accepted adding the "often overkill" limit.

- **What I understand now, and what I still do not:**
  I understand Docker solves portability and Kubernetes solves running many copies reliably. I haven't deployed a real model to a cluster yet.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md)
