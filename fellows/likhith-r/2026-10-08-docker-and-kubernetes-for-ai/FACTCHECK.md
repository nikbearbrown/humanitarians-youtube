# FACTCHECK — Docker and Kubernetes for AI

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | A model can work on a laptop and crash in production | PASS | Classic environment-mismatch failure | Output labelled illustrative |
| 2 | B03 | Library versions, OS and GPU drivers differ between machines; one mismatch can break it | PASS | Docker "what is a container" rationale | Versions labelled illustrative |
| 3 | B04 | Docker packs model, code and dependencies into one image that runs the same anywhere | CORRECTED | Docker image docs; NVIDIA Container Toolkit (host driver) | On-screen note: GPU hosts still need their own driver; verdict says "compatible host" |
| 4 | B05 | One container can't absorb spikes, recover from crashes or spread load | PASS | A single process has no replicas, restart policy across hosts, or balancer | Traffic labelled illustrative |
| 5 | B06 | Kubernetes orchestrates many containers across many machines | PASS | Kubernetes overview | — |
| 6 | B07 | It adds copies with demand, replaces failed ones, spreads traffic | PASS | K8s overview (self-healing, load balancing); HPA docs (autoscaling, when configured) | Replica counts labelled illustrative |
| 7 | B08 | Docker → portable; Kubernetes → scalable and resilient | PASS | Follows from 3 and 6 | — |
| 8 | B09 | Serves many users without hand-managing servers; often overkill for one small model | PASS | Capability, not a measured figure; operational-overhead caveat | — |
