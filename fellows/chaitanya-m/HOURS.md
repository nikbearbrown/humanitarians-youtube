# Weekly hours — Chaitanya M.

**Reporting period (Weeks 1–12):** agreement 1 Aug — 31 Oct 2026.
**Project:** Medhavi Hub — subsystem research reels

Hours below are reconstructed estimates based on documented project activity and
my recollection of the time spent. Exact contemporaneous time records were not
maintained. These figures are not Git-derived measurements, independently
verified time logs, automated timer output, or previously approved hour totals.

Calendar start/end dates for the individual weeks are not documented, so no
calendar ranges are inferred. Project-folder dates span 28 Aug – 15 Oct 2026;
they establish when each reel was built, not when all the underlying work
occurred.

Weeks 1–4 predate the first reel. On the professor's direction the period
opened with reading the hub's documentation and tracing it against the code —
which is where the reels came from: the first four were built on subsystems
audited during that review.

| Week | Production work | Prod hrs | Meeting | Total |
|---|---|---:|---:|---:|
| Week 1 | Hub codebase orientation — `DEVELOPER.md`, the API surface, and the per-project doc sets under `medhavy_documentation/` (18) | 18.0 | 2.0 | **20.0** |
| Week 2 | Concept Map subsystem documentation read against the code — schema, S3 layer, the export route (18) | 18.0 | 2.0 | **20.0** |
| Week 3 | Memory and access documentation traced against the routes; discrepancies noted for follow-up (18) | 18.0 | 2.0 | **20.0** |
| Week 4 | [Tutor persona architecture and model/API rationale](https://github.com/Medhavy/medhavi-hub/commit/7f10aaa) reviewed (10) · working notes drafted — `concept-map-pipeline.md`, `how-the-tutor-uses-the-textbook.md` (8) | 18.0 | 2.0 | **20.0** |
| Week 5 | Concept Map subsystem audit — schema, S3 layer, six API routes, both fixtures (10) · script and art direction (7) · [What Is a Concept Map](./2026-08-28-what-is-a-concept-map/) built (4) | 21.0 | 2.0 | **23.0** |
| Week 6 | Frame QC, six defects found and fixed (8) · [9:16 short rebuilt](./2026-08-28-what-is-a-concept-map/BUILD-LOG.md) through `shorts.py` (7) · [concept-map editor doc corrected against the code](https://github.com/Medhavy/medhavi-hub/commit/3775687) (5) | 20.0 | 2.0 | **22.0** |
| Week 7 | Memory API audit — two tables, both routes, the auth helper (8) · deck authored and captured headless at 4K (9) · [Memory API](./2026-09-13-memory-api/) built (3) | 20.0 | 2.0 | **22.0** |
| Week 8 | Hub access model audited — `getUserAccess` and both call sites (9) · [Who Can Open What](./2026-09-17-who-can-open-what/) built (9) · 9:16 pantry overrides (2) | 20.0 | 2.0 | **22.0** |
| Week 9 | [One Sign-In, Many Books](./2026-09-21-one-sign-in-many-books/) built (12) · repository compliance pass — Frictional logs, media rule, no-surname rule (7) | 19.0 | 3.0 | **22.0** |
| Week 10 | `chapters.py` written and validated (6) · tutor retrieval path researched against the hub docs (8) · [Lookup, Not Training](./2026-10-01-lookup-not-training/) built (7) | 21.0 | 2.0 | **23.0** |
| Week 11 | Logout bug reproduced and root-caused to the HttpOnly session cookie on the provider domain (11) · [fix written with the five-second race](https://github.com/Medhavy/medhavi-hub/commit/4777b36) and landed on `main` (8) | 19.0 | 2.0 | **21.0** |
| Week 12 | [The Logout That Didn't](./2026-10-15-the-logout-that-didnt/) built (12) · frame QC at t=0 and mid-beat (5) · GATE P signed (1) | 18.0 | 3.0 | **21.0** |
| **Total** | | **230.0** | **26.0** | **256.0** |

Each week meets the 20-hour requirement at the stated split.

Weeks without a new reel are not empty: Weeks 1–4 are the documentation review,
Week 6 is QC, the short rebuild and a doc correction committed to the hub, and
Week 11 is the logout investigation and the fix that landed in `medhavi-hub` —
the work the Week 12 reel is about.

The Week 4 working notes — `concept-map-pipeline.md` and
`how-the-tutor-uses-the-textbook.md` — are held locally and not yet committed to
`medhavi-hub`. The second of them is the primary source for the Lookup, Not
Training reel, which is why committing it is an open item in
[RENEWAL.md](RENEWAL.md).

If actual hours differ from these figures they should replace them — the numbers
must be the volunteer's own reconstruction.
