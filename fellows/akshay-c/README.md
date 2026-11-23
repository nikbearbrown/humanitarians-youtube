# Akshay C.

**Role:** Software Engineer  
**Project:** Humanitarians AI — YouTube Content & Automation  
**GitHub:** [@aks2161989](https://github.com/aks2161989)

Humanitarians AI fellow working on YouTube content, Brutalist technical explainers,
content review, and automation of the post-publication workflow.

## What's in this folder

Each Brutalist video has its own work folder containing the supporting project files,
including beat sheets, prompts, fact-checking notes, scene definitions, shot lists,
and portrait-specific configuration where applicable.

## Week of 2026-11-18

- Reviewed 10 videos from the Claude_bear folder and published them to the Humanitarians AI
- Created [How Database Sharding Scales Horizontal Storage](./2026-11-18_database_sharding_scales_horizontal_storage/)
- Humanitarians AI YoTube Publication Notification Pipeline: Live Integrations, Poller Automation & End-to-End Verification:
  - Live Cloud Google Sheet Synchronization:
    - Connected directly to live cloud Google Sheets for both fellow rosters and video tracker data.
    - Implemented automatic startup syncing and periodic synchronization of active/inactive fellow statuses and project
      assignments.
    - Added fallback mechanisms to local tracker files if the cloud sheet is empty or unreachable.
  - Autonomous Background Polling & Scheduling:
    - Implemented a background automated poller with configurable cron scheduling to periodically reconcile video publication
      states.
    - Added operational and browser-friendly endpoints (/api/pipeline/reconcile, /api/pipeline/poller/status,
      /api/pipeline/fellows) for real-time monitoring and manual triggers.
  - YouTube Privacy Detection & Public Status Verification:
    - Implemented live YouTube public oEmbed verification.
    - Added logic to distinguish between Unlisted and Public states, preventing premature publication notifications while
      videos are still in draft or review.
    - Added safeguards to protect existing PUBLISHED states from accidental rollback.
  - Live SMTP Dispatch:
    - Wired production-ready SMTP email dispatching while ensuring local development runs smoothly even when live mail credentials are not configured.
  - Simulation Runner & Verification:
    - Built an end-to-end simulation harness with flexible identifier routing and repeatable pipeline reset capabilities to test publication cycles end-to-end.

## Week of 2026-11-11

- Reviewed 9 videos from the Claude_bear folder and published them to the Humanitarians AI
  Extending Claude playlist.
- Created [How Consistent Hashing Scales Distributed Systems](./2026-11-11_consistent_hashing_scales_distributed_systems/)
  as a Brutalist technical explainer.
- Humanitarians AI YoTube Publication Notification Pipeline: Core Foundation & Idempotent Pipeline Architecture:
  - Relational Domain Modeling & Data Ingestion:
    - Designed the relational schema across projects, fellows, pms, videos, review_events, and notifications with foreign key relationships and database-level SQL check constraints.
    - Implemented canonical ingestion extractors to parse Google Drive URLs, isolate stable file IDs, and map YouTube video identifiers cleanly.
  - Notification Adapters & Preview System:
    - Built multi-sink notification handlers supporting DRY_RUN, REDIRECTED (test inbox with routing metadata), and live dispatch modes.
    - Created responsive HTML email templates with dynamic publication details and personalized video links.
  - Reconciliation Engine & Two-Phase State Machine:
    - Implemented the core reconciliation engine with concurrency execution locking to prevent overlapping runs.
    - Built the two-phase idempotent state machine (PENDING → pre-commit SENDING → SENT / FAILED) to guarantee zero duplicate emails even during network retries or process crashes.
  - Reliability & Stranded Record Recovery:
    - Implemented automated exponential backoff retries and a recovery worker for records stranded in in-flight states.
    - Documented system architecture, state transitions, and system design diagrams.

## Week of 2026-11-04

- Reviewed 14 videos from the Claude_bear folder and published them to the Humanitarians AI
  Extending Claude playlist.
- Created [How Circuit Breakers Prevent Cascading Failures](./2026-11-04_how_circuit_breakers_prevent_cascading_failures/)
  as a Brutalist technical explainer.

## Week of 2026-10-28

- Reviewed 14 videos from the Claude_bear folder and published them to the Humanitarians AI
  Extending Claude playlist.
- Created [How Database Indexing Makes Queries Fast](./2026-10-28_database_indexing_makes_queries_fast/)
  as a Brutalist technical explainer.

## Week of 2026-10-21

- Reviewed 14 videos from the Claude_bear folder and published them to the Humanitarians AI
  Extending Claude playlist.
- Created [How API gateways handle Millions of API requests](./2026-10-21_api_gateways_manage_millions_of_requests/)
  as a Brutalist technical explainer.

## Week of 2026-10-14

- Reviewed 14 videos from the Claude_bear folder and published them to the Humanitarians AI
  Extending Claude playlist.
- Created [How Message Queues Prevent Systems from Crashing](./2026-10-14_how_message_queues_prevent_systems-_from_crashing/)
  as a Brutalist technical explainer.

## Week of 2026-10-07

- Reviewed and uploaded 10 videos from the Claude_bear folder to the Humanitarians AI YouTube channel.
- Created [How Caching Makes Applications Faster](./2026-10-07_how_caching_makes_applications_faster/) as both a 4K landscape (3840×2160) and native 4K portrait (2160×3840) Brutalist explainer.
- Began development work on the automated YouTube publication notification pipeline with the team.
- Reviewed the existing publication workflow and requirements for automatically notifying fellows when their submitted videos are published on YouTube.
- Designed the initial phased approach for connecting video submission records, fellow information, YouTube publication status, and automated email notifications.
- Identified reliability requirements including deterministic video/fellow tracking, duplicate-notification prevention, delivery state tracking, retries, auditability, and safe staged rollout.
- Reviewed the proposed approach with the project manager and began Phase 1 implementation planning.

## Week of 2026-09-28

- Reviewed 14 videos from the Claude_bear folder and published them to the Humanitarians AI
  Claude Basics playlist.
- Created [How Load Balancers Handle Millions of Requests](./2026-09-30_how_load_balancers_handle_millions_of_requests/)
  as a Brutalist technical explainer.

## Week of 2026-09-21

- Reviewed and published 14 videos from the Claude_bear folder to the Humanitarians AI YouTube channel.
- Created [How CDNs Deliver Content So Fast](./2026-09-21_how_cdns_deliver_content_fast/)
  as a Brutalist technical explainer.
- Continued reviewing Humanitarians AI video content and supporting the YouTube content workflow.

## Week of 2026-09-14

- Reviewed and published 14 videos from the Claude_bear folder to the Humanitarians AI YouTube channel.
- Created [How Redis Handles Millions of Requests](./2026-09-18_redis_millions_of_requests/)
  as a Brutalist technical explainer.
- Continued studying and applying the Brutalist video-production workflow.

## Week of 2026-09-07

- Reviewed and published 14 videos from the Claude_bear folder to the Humanitarians AI YouTube channel.
- Created [How Kafka Handles Millions of Events](./2026-09-11-kafka-millions-of-events/)
  as a Brutalist technical explainer.
- Reviewed the Brutalist production workflow and began contributing to Humanitarians AI
  YouTube content activities.

## Frictional log

Every work subfolder carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open.

Append as you go; never rewrite an earlier entry. It is not graded and not a performance
review. See <https://www.humanitarians.ai/fellows> for what an entry contains.