# Design From Real Data

- **Status:** built — awaiting Rishabh's review
- **Series:** Building a Research Assistant · Part 4 (Stage 2A)
- **Channel:** @HumanitariansAI · **Voice:** Kokoro `af_sarah` · **Greeting:** Greetings (slug pick)
- **Long:** 3840×2160 · 5:37 · 18 beats — `research-assistant-part-4.mp4`
- **Short:** 2160×3840 · 1:23 · 9 beats — `short/research-assistant-part-4-short.mp4`
- **Last updated:** 2026-10-09

## Subject
Stage 2A, Oct 5–8: real arXiv metadata into Postgres. Two carry-over bugs, four rules
(respect the service, real data first, isolate failures, safe to repeat), and the code each
rule became: a config floor on the rate limit, a parser shaped by three real responses, one
rate limiter, a retry policy, Alembic in a one-off container, one upsert per day, the first DAG.

## Notes
- First person, build-log framing. No course/reference mentioned; no credit line.
- Omitted for length: the pre-commit vs `make lint` mismatch (Step 3a), sync-vs-async decision.
- LOGO LAW: arXiv, Postgres, Airflow, FastAPI marks on diagram nodes (new `logo` node prop).
- B10 shows the real verify snippet; its results are the numbers recorded in the Stage 2 log,
  labelled as recorded, not a screen capture.
