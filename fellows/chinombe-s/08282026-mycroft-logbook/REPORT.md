# Sprint 1 — Request logbook

- **Week:** 24–28 Aug 2026 · merged 2026-09-02 as commit `b46d48e`
- **Project:** Mycroft — Adaptive Model Routing & Inference Gateway
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/b46d48e

- **Video:** [Why We Built the Mycroft Log Book Before the AI Router](https://www.youtube.com/watch?v=nC1xKKoPuUE)
- **Drive:** https://drive.google.com/drive/folders/1H2fjjURBSxWyUZ5dBAkl9Ced5ANGVGSJ
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [MCP](../08282026-whatismcp/)

## What this sprint was for

The project's claim is that Mycroft can route each request to the cheapest model
that still answers correctly, and save money doing it. That claim is only worth
making if the saving can be **measured**, so the first sprint built the
measurement layer  before any routing logic, any model connection, or any live
call.

Nothing in this sprint touches the network. No API keys, no providers, no
fixtures.

## What was built

| File | What it does |
|---|---|
| `scripts/gateway/schema.py` | The record contract. Defines one `Attempt`  a single physical call  and rejects any record that would corrupt later measurement. |
| `scripts/gateway/logbook.py` | Append-only writer. Validates a record before touching the file, and holds both a process-local lock and an OS file lock while writing. |
| `scripts/gateway/prices.py` + `prices.json` | Versioned price table. Cost is computed and frozen at log time, with the table's version stored on the row. |
| `scripts/gateway/report.py` | Reads the log back: cost per request, per attempt, percentiles, provenance. |
| 4 test files | 24 tests passing at merge. |

## Results

**A retried request no longer looks cheaper than it is.** The central design
decision is that one *logical request* can contain several *physical attempts*,
sharing one `request_id`. A retry does not get a fresh id. On a two-attempt
escalation, averaging per attempt reports **$4.65** where the request actually
cost **$9.30** — exactly half, and in the flattering direction. The incorrect
average is deliberately kept in `report.py`, labelled incorrect, and pinned by a
test so it cannot quietly become the number someone reports.

**A model with no published price cannot be called.** An unpriced model used to
cost $0.00 on the row. It now raises `UnknownModelPrice` *before* the provider is
contacted: a request that cannot be accounted for is not made.

**Rows cannot be written without being recorded.** Validation runs before the
file is opened, and there is no code path that returns a response without a row.

**A data-loss bug was found and fixed.** The first writer used `O_APPEND` with
one `os.write` per row  atomic on POSIX, not on Windows through separate
handles. The concurrency test wrote **153 of 200 rows and raised no error**.
Fixed with a `threading.Lock` plus an OS file lock on a sidecar `.lock` file; the
test now writes all 200.

## What this sprint does *not* do

- No routing. Which model serves a request is still decided by the caller.
- No live calls, so no evidence yet about what models actually cost in practice.
- The price table at this point holds configured rates, not observed ones.

## Evidence

- Commit `b46d48e` — https://github.com/nikbearbrown/mycroft/commit/b46d48e
- `logs/RUN_LOG.md`, entry dated 2026-09-02 (backfilled 2026-09-10, labelled as
  backfilled)
- `scripts/gateway/FINDINGS.md`  why model choice needed one door at all: it is
  currently hardcoded four incompatible ways across the repository
- Tests: `python -m pytest scripts/gateway/tests -q`

## Limits and open items

- The work merged without a RUN_LOG entry, which the repository's own logging
  rule requires. Backfilled eight days later and labelled as not
  contemporaneous.
- 101 scripts under `scripts/tools|gigo|ingest/` cannot be imported at all
  (hyphenated filenames, underscore imports, no `__init__.py`). Not fixed 
  `scripts/gateway/` sits outside that tree deliberately. Recorded in FINDINGS.
- Cost figures in this sprint are arithmetic on a configured price table. The
  first observed costs arrive in Sprint 2.

## Next

