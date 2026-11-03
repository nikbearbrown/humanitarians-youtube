# Frictional log — Adaptive Model Routing Gateway, Sprint 1

## 2026-09-02 — the request logbook

- **Video (progress):** https://www.youtube.com/watch?v=nC1xKKoPuUE
- **Drive:** https://drive.google.com/drive/folders/1H2fjjURBSxWyUZ5dBAkl9Ced5ANGVGSJ?usp=drive_link
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/b46d48e


**What I was working on.** The measurement layer under the routing gateway 
a logbook that records, for every model request, which model answered, why it
was chosen, what it cost and how long it took. No routing logic, no live calls,
no API keys. Sprint board week 24–28 Aug; merged 2026-09-02.

**What I tried, and what I expected.**
- I expected this to be the easy sprint. Appending a line of JSON to a file per
  request is not a hard problem, and I thought the sprint's content was mostly
  deciding which fields to record.
- I expected "cost" to be one number per request. My first sketch had one row
  per request with a cost column.

**Where it resisted, and what I did next.**
- The one-row-per-request model was wrong, and it was wrong in the direction
  that flatters you. When a request fails on a cheap model and is retried on a
  strong one, that is one logical request and two physical calls. If each call
  gets its own row and you average the rows, an escalated request looks
  *cheaper* than it is. The pinned example in the tests: the same two attempts
  report $4.65 as a per-attempt mean and $9.30 as the real per-request cost.
  Restructured to `request_id` plus `attempt_no`, where a retry keeps the
  request id rather than starting a fresh one. The incorrect average is still
  in `report.py`, labelled incorrect and pinned by a test, so nobody
  reintroduces it by accident.
- The writer lost data on Windows and did not say so. It used `O_APPEND` with
  one `os.write` per row, which is atomic on POSIX. On Windows, concurrent
  appends through separate handles are not: the concurrency test wrote **153 of
  200 rows and raised no error**. That is the worst failure mode I have hit on
  this project  not a crash, just a quieter month. Fixed with a process-local
  `threading.Lock` plus an OS file lock on a sidecar `.lock` file.
- A model with no entry in the price table used to cost $0.00. Changed to raise
  `UnknownModelPrice` before the provider is called, so an unpriceable request
  is refused rather than silently logged as free.
- Self-inflicted, and worth recording: I once pasted the test file's contents
  into `logbook.py` and got a circular import I did not understand for a while.
  Another time I added a test file without the `conftest.py` fixtures it
  depended on and spent a while on `fixture 'prices_v1' not found`. Both were
  paste discipline, not logic  and both are the kind of thing that stops being
  a mystery once you read the traceback from the bottom up.
- Also this sprint: 101 scripts under `scripts/tools|gigo|ingest/` cannot be
  imported at all (hyphenated filenames, underscore imports, no `__init__.py`).
  I did not fix them  out of scope  but `scripts/gateway/` is deliberately
  outside that tree so the new code is importable. Recorded in FINDINGS rather
  than quietly worked around.
- Process friction: the work merged as `b46d48e` with **no RUN_LOG entry**,
  which the repository's own logging rule requires. Backfilled on 2026-09-10
  and labelled as backfilled. This has since happened twice more, which tells
  me it is a habit problem and not an oversight.

**What Claude contributed, and what I did with it.**
- Claude helped me with the architecture a folder structures and i wrote all the 
  scripts
- Accepted: the request/attempt split, and keeping the wrong average in the
  code labelled as wrong. I would not have thought to keep a known-bad number
  on purpose, and it is the thing most likely to stop this bug returning.
- Accepted: raising on an unpriced model instead of defaulting to zero.
- Evidence: commit `b46d48e`; `logs/RUN_LOG.md` entry dated 2026-09-02;
  `scripts/gateway/`  `schema.py`, `prices.py`, `logbook.py`, `report.py`.

**What I understand now, and what I still do not.**
- Understood: a measurement bug is more dangerous than a crash. Both the
  per-attempt average and the Windows append loss produced *plausible* output
  and no error. Everything downstream every cost comparison in Sprints 4
  through 8 rests on this layer being right, so it is worth the pedantry.
- Understood: "atomic append" is a promise the operating system makes, not the
  language. I had assumed file appends were simply safe.
- Not understood at the time: why cost had to be frozen at log time with the
  price table's version attached. It made sense later, when a model was retired
  and its prices changed old rows still trace to the table that priced them.
- Still open from this sprint: the 101 unimportable scripts.