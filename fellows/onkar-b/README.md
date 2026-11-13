# Onkar Bhujbal — Humanitarians AI Fellow

- **Role:** AI Software Engineer
- **Project:** Mycroft — Provenance Gatekeeper
- **Repository:** (https://github.com/nikbearbrown/mycroft/tree/main/provenance-gatekeeper)
- **Group / supervisor:** Mycroft / Shradha Katte
- **Agreement period:** 01 Sep 2026 — 30 Sep 2026

## Research question

Can an automated system successfully intercept and mathematically grade AI hallucinations against a persistent ledger of ground truth before humans ever see the output?

Large language models confidently generate false numeric data. This project builds the "Provenance Gatekeeper"—a strict verification pipeline utilizing FastAPI, ChromaDB, and SQLite—to ensure every AI claim is cross-referenced, categorized by magnitude/directional error, permanently logged, and routed to human operators via webhook if a failure is detected.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| [01–07 Sep](./2026-09-07-work-infrastructure-cicd/) | Infrastructure & CI/CD | Scaffolded a Dockerized FastAPI backend to ensure execution isolation and integrated GitHub Actions to enforce strict deployment governance. | [drive](https://drive.google.com/drive/folders/1WVcJvvy4fNrPXxgYmsOFLT2A5cCjKg-c) | [log](./2026-09-07-work-infrastructure-cicd/FRICTIONAL.md) |
| [08–14 Sep](./2026-09-14-work-data-ingestion/) | Data Ingestion & Orchestration | Engineered the retrieval pipeline by loading financial ground-truth data via n8n into a local ChromaDB vector database. | [drive](https://drive.google.com/drive/folders/1_wYTFuAuS0MCtqxwmmeCd0e_2IEOw-Yd) | [log](./2026-09-14-work-data-ingestion/FRICTIONAL.md) |
| [15–21 Sep](./2026-09-21-work-evaluation-layer/) | Evaluation Layer Engineering | Built deterministic grading logic to evaluate claims against the retrieved ledger, categorizing failures into strict magnitude and directional errors. | [drive](https://drive.google.com/drive/folders/1ca944LZn-m0oxm6S7Iq7rM5UrwprYLAK) | [log](./2026-09-21-work-evaluation-layer/FRICTIONAL.md) |
| [21–28 Sep](./2026-09-28-work-tracking-alerting/) | Tracking & Alerting System | Implemented a persistent SQLite database to permanently log all evaluated AI claims and integrated an automated outbound webhook system. | [drive](https://drive.google.com/drive/folders/1v0LFVRNdma-HeUjIoWLViYzKnBw5ecIq) | [log](./2026-09-28-work-tracking-alerting/FRICTIONAL.md) |

## STEM Topics

Research, scripts, and logic mine; formatting and layout validation QC via Claude.

| Week | Topic | Evidence | Log |
|---|---|---|---|
| [01–07 Sep](./2026-09-07-stem-vector-embeddings/) | Vector Embeddings | [drive](https://drive.google.com/drive/folders/1n8JjUTFApVEmNuDq416108mWD_j6mkn3) | [log](./2026-09-07-stem-vector-embeddings/FRICTIONAL.md) |
| [08–14 Sep](./2026-09-14-stem-reversal-curse/) | The Reversal Curse | [drive](https://drive.google.com/drive/folders/1R9HBJLmG9eLfsHnnvfllq9S4OmcPE6I2) | [log](./2026-09-14-stem-reversal-curse/FRICTIONAL.md) |
| [15–21 Sep](./2026-09-21-stem-rag-architecture/) | RAG Architecture | [drive](https://drive.google.com/drive/folders/1oKfHZTythPKP0Ixc74HHd8syWrhaXeGq) | [log](./2026-09-21-stem-rag-architecture/FRICTIONAL.md) |
| [21–28 Sep](./2026-09-28-stem-ai-guardrails/) | AI Guardrails | [drive](https://drive.google.com/drive/folders/1P9ePipZ7jwVtWySA69wZ3eFxB_nD15I9) | [log](./2026-09-28-stem-ai-guardrails/FRICTIONAL.md) |

## Next steps

- **Week 5 (29 Sep – 05 Oct):** Build a UI dashboard to visualize the AI failure matrix directly from the SQLite database.
- **Week 6 (06–12 Oct):** Stress test the full evaluation pipeline with adversarial inputs to map the false positive limits of the deterministic grader.
- **Week 7 (13–19 Oct):** Cloud deployment of the entire Provenance Gatekeeper architecture for live 24/7 testing.
- **Week 8 (20–26 Oct):** Final system audit and comprehensive documentation handoff for future fellows.

## Hours and renewal

- [Weekly hours](HOURS.md)
- [Renewal request](RENEWAL.md)
