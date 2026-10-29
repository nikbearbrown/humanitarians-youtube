# Rishabh M. — Humanitarians AI Fellow

- **Role:** Technical Lead
- **Supervisor:** Nik Bear Brown
- **Agreement period:** 1 Aug — 31 Oct
- **GitHub:** [@RishabhHM](https://github.com/RishabhHM)
- **Drive (all weeks):** https://drive.google.com/drive/folders/1T7BaNfXxid7w38P0RiMq-5RKPZWBqHSo

## Weekly work

Drive folders are named by the Friday of each reporting week.

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| [3–7 Aug](./2026-07-29-fellows-portal-refactor/) | Fellows Portal refactor | One shared admin password replaced by three roles (fellow, admin, super-admin), without a roles table | [drive](https://drive.google.com/drive/folders/1nCRcJBro2DOLOOiIDad9eehPNXtCSQsp) | - |
| [10–14 Aug](./2026-08-14-dead-links-live-redirects/) | Site link and route cleanup | Dead links, duplicated tool files and an unreachable route fixed | [drive](https://drive.google.com/drive/folders/1ZpGBUbUjC_IPkM-zQ-sbvsQYPRLAgZKO) | - |
| [24–28 Aug](./2026-08-28-agentic-design-patterns-part-1/) | Agentic Design Patterns · Part 1 | *The Prompt Is Not The System* | [drive](https://drive.google.com/drive/folders/13w6xlluEtCFhMQGBpVoiqvvPo4Qyo1gM) | - |
| [31 Aug – 4 Sep](./2026-09-04-agentic-design-patterns-part-2/) | Agentic Design Patterns · Part 2 | *State Is The Hard Part* | [drive](https://drive.google.com/drive/folders/1Qn7Qh_WEXj12mIUq6F8RUpesRn-fAZAu) | - |
| [7–11 Sep](./2026-09-11-agentic-design-patterns-part-3/) | Agentic Design Patterns · Part 3 | *The Constraints Are The Design* | [drive](https://drive.google.com/drive/folders/1-T8VfuV9PZTEEDlliOZzI6VuOj_VoZHO) | - |
| [14–18 Sep](./2026-09-18-research-assistant-part-1/) | Research Assistant · Stage 1 infrastructure | Five services wired and health-checked before any AI — *Infrastructure First, AI Second* | [drive](https://drive.google.com/drive/folders/1j0UDC0IdGHN4p1YBhjwIisUKjXqrA3-K) · [repo](https://github.com/RishabhHM/AI-Research-Assistant) | - |
| [21–25 Sep](./2026-09-25-research-assistant-part-2/) | Research Assistant · Stage 1 design | Six design questions applied to every Stage 1 decision — *Six Questions Instead Of Sixty Patterns* | [drive](https://drive.google.com/drive/folders/16plFmboLsS9cXeln9Xs9OEbUUr9O7hN1) · [repo](https://github.com/RishabhHM/AI-Research-Assistant) | - |
| [28 Sep – 2 Oct](./2026-10-02-research-assistant-part-3/) | Research Assistant · Stage 1 bugs | Seven bugs, each read as symptom → cause → rule — *Let The Bugs Teach You* | [drive](https://drive.google.com/drive/folders/1QOtmHi60Fr26abq6rK3c_mb0sWLQoWW7) · commit [`9849fdf`](https://github.com/RishabhHM/AI-Research-Assistant/commit/9849fdfc17981b74dbb8042edbbe6413bd191b33) | - |
| [5–9 Oct](./2026-10-09-research-assistant-part-4/) | Research Assistant · Stage 2A metadata ingestion | Real arXiv metadata in Postgres: rate-limited client, parser designed from real responses, one idempotent upsert per day, first DAG — 527 papers. *Design From Real Data* | [drive](https://drive.google.com/drive/folders/1TcLfQncfg-LSAnTao7RW7xvedUpr2oOB) · commit [`22f9c6b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/22f9c6b39ff163efd52be7e7d4a6892f5bb2aefc) | [log](./2026-10-09-research-assistant-part-4/FRICTIONAL.md) |
| [12–16 Oct](./2026-10-16-research-assistant-part-5/) | Research Assistant · Stage 2B PDF processing | PDFs downloaded through the rate limiter, cached atomically by version, parsed by Docling in Airflow only, saved as sections; per-paper status makes the queue a query. *The Queue Is A Query* | [drive](https://drive.google.com/drive/folders/1rca04Q1xJCdidYSC3QelYdoodXrX9G1H) · commit [`10d074b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/10d074b4324e2b00eb8546eefcb25f3d12509873) | [log](./2026-10-16-research-assistant-part-5/FRICTIONAL.md) |
| [19–23 Oct](./2026-10-23-research-assistant-part-6/) | Research Assistant · Stage 2C orchestration | A daily DAG with an overlapping five-day window, retries and timeouts, cleanup that runs after failures, a report that keeps failed runs red, and a papers API that shows the pipeline. *Keep Failures Red* | [drive](https://drive.google.com/drive/folders/1L6V_ArnaUhA5H21NCZkvHcUROG6IgxBY) · commit [`cc5cdd3`](https://github.com/RishabhHM/AI-Research-Assistant/commit/cc5cdd3ac3470e7f8467be413099bec5e627f340) | [log](./2026-10-23-research-assistant-part-6/FRICTIONAL.md) |

Each commit link is the last commit of that reporting week in [AI-Research-Assistant](https://github.com/RishabhHM/AI-Research-Assistant).

## Hours and renewal

- [Weekly hours](HOURS.md)
- [Renewal request](RENEWAL.md)

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
