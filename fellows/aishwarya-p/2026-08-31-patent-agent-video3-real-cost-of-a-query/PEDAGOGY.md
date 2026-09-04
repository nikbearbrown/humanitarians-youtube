# PEDAGOGY — The Real Cost of a Query (hai cli-explainer, patent agent progress video 3)

A progress-recap video documenting a real BigQuery quota error, the honest investigation into its cause, the real cost math and billing decision, a genuine rejected alternative, and a second real cost center (the Anthropic API, including a real model refusal).

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real 403 error, verbatim ✓
- B01 — the real quota mechanics (1 TiB free, billed past that) ✓
- B02 — the real investigation: a wrong assumption (LIKE is expensive) corrected by real job-history evidence (exact match cost the same; caching is what's actually free) ✓
- B03 — the real math ($6.25/TiB → ~$0.71/lookup) and the real decision to add billing ✓
- B04 — a genuinely explored and genuinely rejected alternative (smaller table, wrong era of data) — presented honestly as a dead end, not glossed over ✓
- B05 — the second real cost center (Anthropic API), including the real refusal encountered and how it was handled ✓
- B06 — HANDOFF, a runnable prompt teaching the same real discipline (check job history / table structure before trusting a query's cost) ✓
- B07 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "116.58 gigabytes" scanned | Real BigQuery job history screenshot, this session | OK — exact figure from the real Query job details panel |
| "$6.25 per TiB" | Real web search, multiple corroborating 2026 sources | OK — verified rate, not assumed |
| "≈ $0.71 per lookup" | Real arithmetic: 116.58 GB ÷ 1024 × $6.25 | OK — shown as a derived calculation, not asserted as an official figure |
| "same query repeated: 0 B (cached)" | Real BigQuery job history screenshot, this session | OK — the second, cached run's actual bytes-processed figure |
| "last updated 2017" for the alternative table | Real BigQuery Details tab, this session | OK — table metadata directly observed |
| The real refusal (`stop_reason="refusal"`, category `"bio"`) | Real debug output from this session's actual API call | OK — the literal field values returned by the API |

## Friction protected

- Kept: B02 explicitly narrates the wrong assumption before the right one, rather than only presenting the correct answer — this is the same real investigative process that happened, not a cleaned-up version of it.
- Kept: B04 presents the alternative table exploration as a real dead end rather than omitting it — a viewer doing similar work will hit the same kind of "promising but wrong" table and benefits from seeing it checked and honestly rejected.

VERDICT: PASS
