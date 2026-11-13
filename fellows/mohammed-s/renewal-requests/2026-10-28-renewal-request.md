# Renewal request — Mohammed Hussain Shariff

**Current agreement:** 1 Aug 2026 — 31 Oct 2026

**Requested period:** 1 Nov 2026 — 25 Nov 2026

**Project:** Mycroft

**Current Project:** Legacy Application Migration Using AI 

**Repository:** <https://github.com/mdhussainshariff/snowshift> (database migration, current period) · <https://github.com/mdhussainshariff/jboss-migrator> (JBoss migrator; also [PR #75](https://github.com/nikbearbrown/mycroft/pull/75) into `nikbearbrown/mycroft`)

**Request date:** 2026-10-29

## What the current period produced

Data-engineering and migration work on Mycroft and on my own migration project, each with a
STEM explainer. The evidence is linked below and in the [README](../README.md); every
figure here traces to a commit, a test or a QC record in those folders, not to an estimate.

- **Mycroft Risk Management Agent — credit rating** ([PR #16](https://github.com/Humanitariansai/Mycroft/pull/16)).
  Maps the risk score to nine bond-style tiers (AAA to D). The rating was added as a nested,
  additive block so the 14 original report keys — which a downstream Google Sheet maps by
  name — never change. A test locks both key lists (14 original, 15 camelCase).
- **Mycroft data contract agent — metric-impact simulation** ([4469968](https://github.com/mdhussainshariff/Mycroft/commit/4469968)).
  Rebuilds the marts to measure what a schema change does to the numbers. The test case is a
  change that compiles, runs and passes every test while leaving `fct_mrr` 100× low; the
  simulation reports it, and the test suite asserts the ratio.
- **snowshift — SQL Server → Snowflake migration** ([eb342d4](https://github.com/mdhussainshariff/snowshift/commit/eb342d4), [7ba5900](https://github.com/mdhussainshariff/snowshift/commit/7ba5900)).
  A 1,244-line `Main.sql` split into 29 files across 8 ordered stages; a 27-rule linter that
  found a real `SELECT TOP 10` that would have failed on Snowflake; an ordered deploy with
  dry-run that stops at the first failure; and aggregate parity checks on declared columns.
  Found and fixed one migration gap: Snowflake declares but does not enforce `UNIQUE`, so a
  repeated import would have doubled the budget. 103 tests pass. **Not yet run against a live
  Snowflake account.**
- **JBoss EAP 7 → 8 / Java 8 → 17 migrator — design and first code.** A six-stage pipeline built
  from existing tools (Red Hat MTA, OpenRewrite, Eclipse Transformer, JBoss CLI / WildFly Server
  Migration Tool), an LLM step that may only propose fixes, and characterization tests plus a
  diff guard as the proof. It is now working code in a public repository
  ([jboss-migrator](https://github.com/mdhussainshariff/jboss-migrator)): six stage modules, five of them unit-tested, and batch mode for
  migrating a portfolio of apps from one file with each failure isolated ([41d62af](https://github.com/mdhussainshariff/jboss-migrator/commit/41d62aff2c06b62e384a2aacea969d15d3487bdd)).
  23 of 23 unit tests pass. **Not yet run end to end on a real JBoss application.**
- **Thirteen STEM explainers** on finance, data engineering, data quality, RAG, AI agents,
  AI developer tools and migration. Eleven have rendered 4K masters on Drive; one is published on
  YouTube. Each has a fact-check and a visual QC record.

## Evidence

| Work | Code | Drive | Video | Log |
|---|---|---|---|---|
| Risk rating in the Mycroft report | [PR #16](https://github.com/Humanitariansai/Mycroft/pull/16) | - | - | [log](../2026-08-03-risk-management-explanation/FRICTIONAL.md) |
| Data contract metric-impact simulation | [4469968](https://github.com/mdhussainshariff/Mycroft/commit/4469968) | [drive](https://drive.google.com/file/d/1Ee-pSSfbInmZ8Ofzas5AtXBY9oSFSaSs/view) | - | [log](../2026-09-14-data-contract-simulation/FRICTIONAL.md) |
| snowshift — restructure, lint, deploy, parity | [eb342d4](https://github.com/mdhussainshariff/snowshift/commit/eb342d4) | [drive](https://drive.google.com/file/d/1ahafItD4roNI5A0nX4XRpwvl1RLJxWrL/view) | [watch](https://youtu.be/KXX2EEeFhV8) | [log](../2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| snowshift — duplicate-key fix | [7ba5900](https://github.com/mdhussainshariff/snowshift/commit/7ba5900) | [drive](https://drive.google.com/file/d/1ahafItD4roNI5A0nX4XRpwvl1RLJxWrL/view) | [watch](https://youtu.be/KXX2EEeFhV8) | [log](../2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| JBoss migrator — design and orchestrator | [55c4dcb](https://github.com/mdhussainshariff/mycroft-nikbearbrown/commit/55c4dcb) | [drive](https://drive.google.com/file/d/1x3qaq8DK7e7wsPWpLcXuouCnvzPYp0fU/view) | - | [log](../2026-10-19-jboss-migrator-overview/FRICTIONAL.md) |
| jboss-migrator — public repository and batch mode | [41d62af](https://github.com/mdhussainshariff/jboss-migrator/commit/41d62aff2c06b62e384a2aacea969d15d3487bdd) | [drive](https://drive.google.com/file/d/1i0hmrU8h4Kf1W9MCT9Yj-9YoiupJpfFO/view) | - | [log](../2026-10-26-jboss-migrator-update/FRICTIONAL.md) |

## Stem Topics

| Week | Topic | Video | Drive | Log |
|---|---|---|---|---|
| 3–9 Aug | Credit ratings from a risk score | - | - | [log](../2026-08-03-risk-management-explanation/FRICTIONAL.md) |
| 10–16 Aug | Bond pricing, duration and convexity | - | [drive](https://drive.google.com/file/d/16vbJhf1HLBpK7cDR3TL45pEE2BSSGrM-/view) | [log](../2026-08-10-bond-pricing/FRICTIONAL.md) |
| 17–23 Aug | ETL with AI | - | [drive](https://drive.google.com/file/d/1R9FqiQcs3fIOewDfXi4Hhb7YNgE13jEb/view) | [log](../2026-08-17-ai-data-engineering-etl/FRICTIONAL.md) |
| 24–30 Aug | Data standards and data quality | - | [drive](https://drive.google.com/file/d/1PZRssDuDJz-h1B2NFuSxbq2c6GOdPFzH/view) | [log](../2026-08-24-ai-data-quality/FRICTIONAL.md) |
| 7–13 Sep | Verification logs for model outputs | - | - | [log](../2026-09-07-claude-hai-verification-log-demo/FRICTIONAL.md) |
| 14–20 Sep | Data contracts and schema change | - | [drive](https://drive.google.com/file/d/1Ee-pSSfbInmZ8Ofzas5AtXBY9oSFSaSs/view) | [log](../2026-09-14-data-contract-simulation/FRICTIONAL.md) |
| 21–27 Sep | On-prem RAG | [first POC](https://www.youtube.com/watch?v=0aKoW-FIhew) | [drive](https://drive.google.com/file/d/1ij-jtcLdOkGDB3_DJqcodBghyEp9LqSs/view) | [log](../2026-09-21-onprem-rag-bot/FRICTIONAL.md) |
| 28 Sep – 4 Oct | Snowflake Cortex | - | [drive](https://drive.google.com/file/d/1jUjwteKmC5kMXrox271ABzHlgqxAxmmL/view) | [log](../2026-09-28-snowflake-cortex-triage/FRICTIONAL.md) |
| 5–11 Oct | Database migration | [video](https://youtu.be/KXX2EEeFhV8) | [drive](https://drive.google.com/file/d/1ahafItD4roNI5A0nX4XRpwvl1RLJxWrL/view) | [log](../2026-10-05-hussain-snowshift-migration-overview/FRICTIONAL.md) |
| 19–25 Oct | Application migration: JBoss and Java | - | [drive](https://drive.google.com/file/d/1x3qaq8DK7e7wsPWpLcXuouCnvzPYp0fU/view) | [log](../2026-10-19-jboss-migrator-overview/FRICTIONAL.md) |
| 19–25 Oct | Personal AI agents: Meta's Muse | - | [drive](https://drive.google.com/file/d/1vTD4MOc3M4aL8AkJuA_JLMgVMpR7xSlv/view) | [log](../2026-10-19-muse/FRICTIONAL.md) |
| 26 Oct – 1 Nov | JBoss migrator update: batch mode | - | [drive](https://drive.google.com/file/d/1i0hmrU8h4Kf1W9MCT9Yj-9YoiupJpfFO/view) | [log](../2026-10-26-jboss-migrator-update/FRICTIONAL.md) |
| 26 Oct – 1 Nov | Spec-driven AI IDEs: Amazon's Kiro | - | [drive](https://drive.google.com/file/d/1XBUPVLg_xhwwyR3bB8Ao_JWWsx9BxZBB/view) | [log](../2026-10-26-kiro-spec-ide/FRICTIONAL.md) |

Weekly hours: [HOURS.md](../HOURS.md). Weekly Frictional logs: one per work folder, listed in [README.md](../README.md).

**Coverage.** Weekly records run from 3 Aug to 1 Nov.

## Why migration

Moving internal applications off legacy platforms is everyday work for a developer in a
bank: Java EE apps on old application servers, Java 8 runtimes past support, Struts and
early Spring front ends, and stored-procedure-heavy databases. The tools that move the code
exist. The hard part — and the part this project is about — is **proving the migration
changed nothing it should not have**, especially the differences that raise no error. The
snowshift work showed one (an unenforced `UNIQUE` constraint); the plan below applies the
same discipline to application code.

All work uses public sample applications and synthetic data. No bank source code, data or
configuration is used.

## Plan for the requested period

Sprints 1–5 build the Java migrator; each one gates the next. Starting point:
[jboss-migrator at 41d62af](https://github.com/mdhussainshariff/jboss-migrator/commit/41d62aff2c06b62e384a2aacea969d15d3487bdd) — six stages, batch mode, 23 unit tests, never yet run on a real app.

1. **Baseline before touching anything (2–6 Nov).** Pick a public JBoss EAP 7 / Java 8 sample
   application with real persistence and security, and get it building and deploying. Write
   characterization tests and a diff guard over the business-logic and UI packages. If a green
   baseline cannot be reached, report that; it is the precondition for every later claim.
2. **Inventory (9–13 Nov).** Run the MTA CLI and record every mandatory / optional / potential
   issue. Confirm the exact OpenRewrite recipe packages (an open item from the design). Classify
   each issue in advance as recipe-safe or needs-a-human, and freeze that list before any recipe runs.
3. **Mechanical migration (16–20 Nov).** Apply the OpenRewrite recipes and Eclipse Transformer.
   Report how many mandatory issues the tools close, against the frozen list. The diff guard
   must show zero changes to protected code, and the characterization tests must still pass.
4. **What needs a human (23–25 Nov).** Handle the remaining issues: an LLM step proposes fixes,
   and a human reviews every one. Regenerate the server config with JBoss CLI or the WildFly
   Server Migration Tool, and deploy on EAP 8 / Java 17. Publish what needed a human, with
   time spent — including "could not migrate" if that is the result.


The next stack is chosen by which one the Java work makes most reusable; the choice is
proposed in writing before it starts.

Reporting continues: a dated Frictional log per work folder written during the week rather
than afterwards, weekly hours in `HOURS.md`, commits as the work happens, and one STEM
explainer plus one progress video per week.

## Open items I am carrying

- snowshift: first live deploy against a Snowflake account, then re-record B09 of its video.
- Snowflake Cortex reel: re-check its four documented claims against `docs.snowflake.com` before publishing.
- JBoss migrator: confirm the OpenRewrite recipe package paths.
- Videos not yet linked: risk-rating (3–9 Aug) and verification-log demo (7–13 Sep); progress videos for most weeks.
- GATE P sign-offs for the risk-rating, on-prem RAG and snowshift reels were given but never written back into their `PEDAGOGY.md` files.
