# Renewal request — Onkar Bhujbal

- **Current agreement:** 01 Sep 2026 — 30 Sep 2026
- **Requested period:** 01 Oct 2026 — 30 Nov 2026

- **Project:** Mycroft — Provenance Gatekeeper
- **Repository:** https://github.com/nikbearbrown/mycroft/tree/main/provenance-gatekeeper

## What the current period produced

Four weeks of building a deterministic AI validation pipeline from the ground up. All evidence is stored across GitHub and Google Drive. 

- Designed a containerized, CI/CD-governed backend using FastAPI and Docker to enforce strict execution isolation.
- Built a secure data ingestion and retrieval layer utilizing n8n webhooks and a local ChromaDB instance to lock in financial ground truth.
- Engineered a programmatic evaluation layer capable of intercepting LLM responses and mathematically grading their accuracy, automatically categorizing failures into strict magnitude and directional errors.
- Secured long-term model accountability by routing all grading verdicts into an immutable SQLite ledger and establishing a webhook alarm system for immediate human operator notification.
- Authored and rendered 8 Brutalist explainer videos in true 4K (16:9 and 9:16) covering the core project infrastructure and four critical STEM architecture topics (Vector Embeddings, The Reversal Curse, RAG, and AI Guardrails).

### Evidence

| Week | Work Update | Drive | Log |
|---|---|---|---|
| 1 — Infrastructure & CI/CD | [folder](./2026-09-07-work-infrastructure-cicd/) | [drive](https://drive.google.com/drive/folders/1WVcJvvy4fNrPXxgYmsOFLT2A5cCjKg-c) | [log](./2026-09-07-work-infrastructure-cicd-week-1/FRICTIONAL.md) |
| 2 — Data Ingestion | [folder](./2026-09-14-work-data-ingestion/) | [drive](https://drive.google.com/drive/folders/1_wYTFuAuS0MCtqxwmmeCd0e_2IEOw-Yd) | [log](./2026-09-14-work-data-ingestion-week-2/FRICTIONAL.md) |
| 3 — Evaluation Layer | [folder](./2026-09-21-work-evaluation-layer/) | [drive](https://drive.google.com/drive/folders/1ca944LZn-m0oxm6S7Iq7rM5UrwprYLAK) | [log](./2026-09-21-work-evaluation-layer-week-3/FRICTIONAL.md) |
| 4 — Tracking & Alerting | [folder](./2026-09-28-work-tracking-alerting/) | [drive](https://drive.google.com/drive/folders/1v0LFVRNdma-HeUjIoWLViYzKnBw5ecIq) | [log](./2026-09-28-work-tracking-alerting-week-4/FRICTIONAL.md) |

## STEM Topics

| Week | Topic | Drive | Log |
|---|---|---|---|
| 01–07 Sep | Vector Embeddings | [drive](https://drive.google.com/drive/folders/1n8JjUTFApVEmNuDq416108mWD_j6mkn3) | [log](./2026-09-07-stem-vector-embeddings/FRICTIONAL.md) |
| 08–14 Sep | The Reversal Curse | [drive](https://drive.google.com/drive/folders/1R9HBJLmG9eLfsHnnvfllq9S4OmcPE6I2) | [log](./2026-09-14-stem-reversal-curse/FRICTIONAL.md) |
| 15–21 Sep | RAG Architecture | [drive](https://drive.google.com/drive/folders/1oKfHZTythPKP0Ixc74HHd8syWrhaXeGq) | [log](./2026-09-21-stem-rag-architecture/FRICTIONAL.md) |
| 21–28 Sep | AI Guardrails | [drive](https://drive.google.com/drive/folders/1P9ePipZ7jwVtWySA69wZ3eFxB_nD15I9) | [log](./2026-09-28-stem-ai-guardrails/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md). Weekly Frictional logs: one per folder, listed in [README.md](README.md).

## Plan for the requested period (October - November)

Weeks 5–12, continuing the build and transitioning to production scaling:

1. **Dashboard Visualization** (October). Build a user interface allowing human operators to actively query the SQLite error ledger and view historical accuracy metrics without requiring command-line access.
2. **Adversarial Stress Testing** (October). Flood the evaluation layer with edge-case syntax, obfuscated numeric formats, and prompt injections to identify the false-positive limitations of the numeric normalizer. 
3. **Cloud Deployment & Latency Optimization** (Early November). Transition the entire Dockerized stack from local execution to a live, persistent cloud environment. Benchmark the latency added by the Guardrail layer and optimize the API to reduce the execution tax.
4. **Semantic Gatekeeping Expansion** (November). Expand the evaluation layer beyond strict numeric limits to catch logic-based and semantic hallucinations against the ChromaDB ledger.
5. **Handoff & Audit** (Late November). Finalize system documentation, clean up architecture diagrams, and prepare the project repository for the next fellow to expand upon.

Reporting continues as it has: a dated Frictional log per work folder, weekly hours, and structured Brutalist video updates.

## Open items I am carrying

- Migration of the final 4K MP4 renders from the Google Drive holding area into the official `brutalist.yt` YouTube publishing pipeline.
