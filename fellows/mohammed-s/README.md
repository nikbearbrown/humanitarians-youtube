# Mohammed S.

**Role:** Data Engineer  
**Project:** Mycroft  
**GitHub:** [@mdhussainshariff](https://github.com/mdhussainshariff)

Renewal requests: [renewal-requests/](renewal-requests/README.md) · Weekly hours: [HOURS.md](HOURS.md)

## What's in this folder

11 work folders, one per report or video, each dated to the Monday of its reporting week:

- `2026-08-03-risk-management-explanation/` — AAA to D: Rating Mycroft's Risk Score
- `2026-08-10-bond-pricing/` — Bond Pricing and Duration: Price-Yield Curve with Claude
- `2026-08-17-ai-data-engineering-etl/` — ETL, Simplified
- `2026-08-24-ai-data-quality/` — The Rule, Not The Report.
- `2026-09-07-claude-hai-verification-log-demo/` — Build Maya's Three-Beat Verification Log with Claude Code
- `2026-09-14-data-contract-simulation/` — Prove The Number Changed.
- `2026-09-21-onprem-rag-bot/` — Chat With Your Own Data, Zero API Calls
- `2026-09-28-snowflake-cortex-triage/` — Cortex, In The Warehouse.
- `2026-10-05-hussain-snowshift-migration-overview/` — Compiling Is Not Migrating.
- `2026-10-19-jboss-migrator-overview/` — Prove Nothing Broke.
- `2026-10-19-muse/` — Muse, Doing The Errands.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.

**Read these notes with the tables:**

- **The logs were written later.** Every `FRICTIONAL.md` entry was written on 2026-10-28,
  reconstructed from the artifacts in each folder. None was written at the time.
- **Folder weeks are reporting weeks, not build dates.** Several folders carry dates inside
  their own artifacts that fall outside their assigned week; each log states the artifact dates.
- **Commits were batched.** Files were uploaded to this repository in batches (2026-09-22,
  2026-10-07, 2026-10-28), not committed as the work happened.

## Project evidence

Code work behind the videos. Links go to the specific pull request or commit.

| Work | Week | Code | Video | Log |
|---|---|---|---|---|
| Mycroft Risk Management Agent — credit rating in the report | 3–9 Aug | [PR #16](https://github.com/Humanitariansai/Mycroft/pull/16) | not recorded | [log](2026-08-03-risk-management-explanation/FRICTIONAL.md) |
| Mycroft data contract agent — metric-impact simulation | 14–20 Sep | [4469968](https://github.com/mdhussainshariff/Mycroft/commit/4469968) · [Data_Quality_Agent](https://github.com/Humanitariansai/Mycroft/tree/main/Data_Quality_Agent) | [drive](https://drive.google.com/file/d/1Ee-pSSfbInmZ8Ofzas5AtXBY9oSFSaSs/view) | [log](2026-09-14-data-contract-simulation/FRICTIONAL.md) |
| snowshift — SQL Server → Snowflake migration: restructure, lint, deploy, parity | 5–11 Oct | [eb342d4](https://github.com/mdhussainshariff/snowshift/commit/eb342d4) | [watch](https://youtu.be/KXX2EEeFhV8) | [log](2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| snowshift — duplicate-key fixes in import and journal procedures | 5–11 Oct | [7ba5900](https://github.com/mdhussainshariff/snowshift/commit/7ba5900) | [watch](https://youtu.be/KXX2EEeFhV8) | [log](2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| JBoss EAP 7 → 8 / Java 8 → 17 migrator — design, then config-driven upgrade orchestrator | 19–25 Oct | [55c4dcb](https://github.com/mdhussainshariff/mycroft-nikbearbrown/commit/55c4dcb) on branch `jboss-migrator` | [drive](https://drive.google.com/file/d/1x3qaq8DK7e7wsPWpLcXuouCnvzPYp0fU/view) | [log](2026-10-19-jboss-migrator-overview/FRICTIONAL.md) |

## STEM topics

One explainer per week. "Drive" is the 4K 16:9 master unless noted.

| Week | Topic | Video | Drive | Log |
|---|---|---|---|---|
| 3–9 Aug | Credit ratings from a risk score (AAA to D) | - | - | [log](2026-08-03-risk-management-explanation/FRICTIONAL.md) |
| 10–16 Aug | Bond pricing, duration and convexity | - | [drive](https://drive.google.com/file/d/16vbJhf1HLBpK7cDR3TL45pEE2BSSGrM-/view) · [review cut](https://drive.google.com/file/d/1UMdcjmJd738WMqJfX8urfOIkc8f-X1ct/view) | [log](2026-08-10-bond-pricing/FRICTIONAL.md) |
| 17–23 Aug | ETL with AI: the glue, not the judgment | - | [drive](https://drive.google.com/file/d/1R9FqiQcs3fIOewDfXi4Hhb7YNgE13jEb/view) · [9:16](https://drive.google.com/file/d/1sw9VyEg0JCoEfJUT21f4UH5Nl6Gg4LBt/view) | [log](2026-08-17-ai-data-engineering-etl/FRICTIONAL.md) |
| 24–30 Aug | Data standards and data quality with AI | - | [drive](https://drive.google.com/file/d/1PZRssDuDJz-h1B2NFuSxbq2c6GOdPFzH/view) · [9:16](https://drive.google.com/file/d/1ODE9fVMFCr1ob57svwo5HXMtJ5aJ3_Ce/view) | [log](2026-08-24-ai-data-quality/FRICTIONAL.md) |
| 7–13 Sep | Verification logs for model outputs | - | - | [log](2026-09-07-claude-hai-verification-log-demo/FRICTIONAL.md) |
| 14–20 Sep | Data contracts: schema changes that compile clean | - | [drive](https://drive.google.com/file/d/1Ee-pSSfbInmZ8Ofzas5AtXBY9oSFSaSs/view) · [9:16](https://drive.google.com/file/d/1wOflv1QptmWlAfL-nKszKDVTydqBs97p/view) | [log](2026-09-14-data-contract-simulation/FRICTIONAL.md) |
| 21–27 Sep | On-prem RAG with Open WebUI + Ollama | [first POC](https://www.youtube.com/watch?v=0aKoW-FIhew) | [drive](https://drive.google.com/file/d/1ij-jtcLdOkGDB3_DJqcodBghyEp9LqSs/view) · [review cut](https://drive.google.com/file/d/1qHCQTXqYmXnyXVXEbAfjMsnfc-Vsspji/view) | [log](2026-09-21-onprem-rag-bot/FRICTIONAL.md) |
| 28 Sep – 4 Oct | Snowflake Cortex: LLM functions inside the warehouse | - | [drive](https://drive.google.com/file/d/1jUjwteKmC5kMXrox271ABzHlgqxAxmmL/view) · [9:16](https://drive.google.com/file/d/1V7MkPccDITX5ocRm4hpqQ-RUVxkK_2Ra/view) | [log](2026-09-28-snowflake-cortex-triage/FRICTIONAL.md) |
| 5–11 Oct | Database migration: compiling is not migrating | [video](https://youtu.be/KXX2EEeFhV8) | [drive](https://drive.google.com/file/d/1ahafItD4roNI5A0nX4XRpwvl1RLJxWrL/view) · [9:16](https://drive.google.com/file/d/1vki1nCCm9olcM2DgZdSzhFB5hA5v_l_G/view) | [log](2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| 19–25 Oct | Application migration: JBoss EAP 7 → 8, Java 8 → 17 | - | [drive](https://drive.google.com/file/d/1x3qaq8DK7e7wsPWpLcXuouCnvzPYp0fU/view) · [9:16](https://drive.google.com/file/d/1Euh_WxXFnlUjKojfC_dcBpj-wUq53xZO/view) | [log](2026-10-19-jboss-migrator-overview/FRICTIONAL.md) |
| 19–25 Oct | Personal AI agents: Meta's Muse | - | [drive](https://drive.google.com/file/d/1vTD4MOc3M4aL8AkJuA_JLMgVMpR7xSlv/view) · [9:16](https://drive.google.com/file/d/1jYMG_iPMmDhtGzr2ukL1A8dmCgc-hf9O/view) | [log](2026-10-19-muse/FRICTIONAL.md) |
