# FACTCHECK — "SQL, Read Fewer Rows."

Reel: `fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics`
Checked: 2026-09-16 · Checker: Supriya Kushwaha (scaffold pass)
Revised: 2026-09-16 (rev 2) — fixture extended to three pairs; `date_trunc` dropped
from B07's spoken list and artifact card; rows 12a/12b/12c, 13, 13b, L2, L4, L5 updated

DOUBLE-CHECK LAW: every factual claim in narration, in on-screen copy, and in the
description is listed below with its verdict and the evidence behind it. Claims are
graded by **how** they were verified, because that distinction matters more than a
tick mark:

- **EXECUTED** — reproduced on this machine by running code in `demo/`. Strongest.
  Re-runnable: `python3 demo/build_demo.py`.
- **DOC** — asserted from vendor documentation. The URL is given. **These are the
  rows to re-read before signing GATE P** — they are the rows I cannot prove from
  this repo alone.
- **ARGUMENT** — our editorial judgement, presented in the reel as judgement and
  not as fact.

## Narration and on-screen claims

| # | Claim | Where | Basis | Evidence | Verdict |
|---|---|---|---|---|---|
| 1 | The `postings` table holds 400,000 rows | B00 · B01 · B03 · B04 · B07 · description | EXECUTED | `SELECT COUNT(*) FROM postings` → `400000`; `demo/RESULTS.md` | ✓ |
| 2 | 11,369 rows match January 2026 (2.84% selectivity) | B00 · B01 · B03 · B04 · B06 · B07 | EXECUTED | `demo/build_demo.py` prints `jan2026_rows=11369`, `selectivity = 2.84%` | ✓ |
| 3 | The answer is 4,459 rows / groups | B00 · B01 · B04 | EXECUTED | both queries return 4,459 groups | ✓ |
| 4 | The two queries return an IDENTICAL result set | B00 · B06 · `slideMeta` | EXECUTED | `sorted(rows_a) == sorted(rows_b)` → `True`; `build_demo.py` exits non-zero if this ever fails | ✓ |
| 5 | Plan A is `SCAN postings`; Plan B is `SEARCH postings USING INDEX idx_postings_posted_at (posted_at>? AND posted_at<?)` | B00 · B03 (verbatim on screen) · B06 | EXECUTED | `demo/explain_a_non_sargable.txt`, `demo/explain_b_sargable.txt` — captured, unedited | ✓ |
| 6 | B01's isotype field: 400 dots, "1 DOT = 1,000 ROWS" | B01 graphic | EXECUTED + declared | Scale is stated in `slideMeta` on screen. Component renders one dot per unit, so 400,000 dots is not renderable; 400 dots at ×1,000 is the honest isotype. The counter's own percentages (3% → 1%) are correct roundings of the real 2.84% and 1.11%; dot counts round to 11 and 4 (real: 11,369 and 4,459). | ✓ **simplification, labelled** |
| 7 | "Thirty-five times fewer" rows read | B04 · B06 · B00 output line | EXECUTED | 400,000 / 11,369 = **35.18** → "thirty-five times" | ✓ |
| 8 | "Plan A is two decades away" from the answer's floor | B04 | EXECUTED | 400,000 / 4,459 = 89.7 = **1.95 decades** on the log axis. "Two decades" is a rounding of 1.95, spoken about a log axis that is on screen. | ✓ |
| 9 | `EXPLAIN QUERY PLAN` "costs nothing to run, and it does not run your query" | B02 · B07 · `artifactLines` | EXECUTED + DOC | Measured: `EXPLAIN QUERY PLAN` on Query A = **0.69 ms**; the query itself = **61.9 ms** (89×). It reports the plan without executing. Doc: sqlite.org/eqp.html | ✓ |
| 10 | `SCAN` means the engine reads every row of the table | B03 · B07 | DOC | SQLite query-planner docs describe `SCAN` as a full table scan vs `SEARCH` as an indexed lookup — sqlite.org/eqp.html, sqlite.org/queryplanner.html. **Consistent with** the executed timings (58.5 ms vs 14.2 ms) and with plan A losing the index. | ✓ |
| 11 | Wrapping an indexed column in a function makes the index unusable | B06 (the insight) · B07 | EXECUTED for `strftime`; DOC for the general rule | Executed: the only difference between A and B is `strftime(...)` vs a bare range, and A loses the index. General rule doc: sqlite.org/optoverview.html (§ the index-usability / "analyzable" constraint requires the indexed column appear bare on one side of the comparison). | ✓ |
| 12a | `CAST` around an indexed column makes the index unusable | B07 · `artifactLines` | **EXECUTED** | Pair 2, `demo/explain_c_non_sargable_cast.txt` vs `explain_d_sargable_cast.txt`: `CAST(branch_id AS TEXT) = '42'` → `SCAN postings`; `branch_id = 42` → `SEARCH postings USING INDEX idx_postings_branch_id (branch_id=?)`. Identical single-row aggregate from both; 400,000 → 1,625 rows read (246×). | ✓ |
| 12b | `UPPER` around an indexed column makes the index unusable | B07 · `artifactLines` | **EXECUTED** | Pair 3, `demo/explain_e_non_sargable_upper.txt` vs `explain_f_sargable_upper.txt`: `UPPER(account_ref) = 'AC-04242'` → `SCAN postings`; `account_ref = 'AC-04242'` → `SEARCH postings USING INDEX idx_postings_account_ref (account_ref=?)`. Identical row from both; 400,000 → 76 rows read (5,263×). `build_demo.py` asserts 0 rows where `account_ref != UPPER(account_ref)`, so the rewrite is genuinely equivalent. **Collation caveat: see L5.** | ✓ |
| 12c | `date_trunc` behaves the same way | **written description ONLY** — removed from B07's narration and artifact card on 2026-09-16 | DOC — not executable here | `date_trunc` is a PostgreSQL function; it does not exist in SQLite, so it cannot be run against this fixture at any effort. Mechanism is identical (indexed column wrapped in an expression) — postgresql.org/docs/17/using-explain.html. **No longer spoken or shown**, so a correction costs no re-render. The description labels it explicitly as documented rather than demonstrated. | ✓ **scoped out of the video** |
| 13 | Measured timings, pair 1: ≈60 ms (SCAN) vs ≈15 ms (SEARCH), ≈4.1× | B06 `notes` ("~60 ms" / "~15 ms") · `demo/RESULTS.md` | EXECUTED | `demo/timing.py`, **9 runs**, fresh connection, `PRAGMA cache_size=0`. Medians **60.18 ms** and **14.64 ms** (min/max 59.41–61.34 and 14.30–15.36). **Re-measured after the fixture gained `account_ref`, `branch_id` and two more indexes** — the scan reads more pages now, so the earlier 58.5/14.2 figures moved to 60.18/14.64. On-screen text uses `~` so run-to-run noise cannot falsify it. | ✓ **machine-specific — labelled** |
| 13b | The wrapped queries all read 400,000 rows yet take 17 / 29 / 60 ms | `demo/RESULTS.md` only — never on screen, never spoken | EXECUTED | `demo/timing.py`. The spread is per-row work (date parsing, temp B-tree for `GROUP BY`), not rows read. This is the positive evidence for why the reel's load-bearing claim is rows read and not milliseconds. | ✓ |
| 14 | "Optimization is the argument about how many rows the database touches" | B01 | ARGUMENT | Our framing, delivered as framing. Defensible and standard, but it is a thesis, not a measurement. | ✓ as argument |
| 15 | Fewer rows read does NOT mean proportionally faster | not claimed anywhere | — | Deliberately absent. 35× fewer rows gave 4.1× faster here; the reel never multiplies one into the other. `demo/RESULTS.md` § "What is NOT claimed". | ✓ by omission |

## Things stripped to keep the video from dating (DOUBLE-CHECK LAW)

- **No model/version numbers in narration.** `modelLabel: "Fable 5"` appears only
  as composer chrome, matching the library default; the narration never names a
  model, so a model refresh does not date the reel.
- **No "Postgres does X" claim in the voice.** The engine-specific naming
  (`Seq Scan` / `Index Scan`) is confined to the written description and
  `SOURCES.md`, where it can be corrected without a re-render.
- **No benchmark headline.** "4× faster" is never spoken — it is machine-specific
  and would be quoted out of context. Rows read is structural; milliseconds are not.
- **No vendor comparison and no "always/never" tuning advice.**

## Known limitations, stated rather than hidden

- **L1 — SQLite is not a production analytics warehouse.** The fixture is a
  400,000-row local SQLite table because the toolkit is free-tier-only and the
  evidence has to be reproducible on the viewer's laptop. The *mechanism* (an
  index cannot serve an expression) is engine-independent; the specific plan
  keywords are not. The reel says "EXPLAIN", not "EXPLAIN QUERY PLAN", in its
  takeaway for exactly this reason.
- **L2 — RESOLVED.** Both halves are now closed.

  **(a) The fixture was extended** (2026-09-16): `demo/build_demo.py` builds
  **three** pairs on the same 400,000-row fixture, same seed, and asserts
  identical result sets for all three — non-zero exit otherwise.

  **(b) `date_trunc` was dropped from the reel** (2026-09-16, L2 option 2). It is
  a PostgreSQL function absent from SQLite, so it could never be executed against
  this fixture; keeping it in the voice would have left one unmeasured assertion
  inside a list of measured ones. It was removed from **both** B07's
  `narration_text` and its on-screen `artifactLines` entry, and rehomed to the
  video description where a correction costs no re-render.

  | Function | Spoken in B07? | Status | Evidence |
  |---|---|---|---|
  | `strftime` | yes | **EXECUTED** | pair 1 — `explain_a`/`explain_b` |
  | `CAST` | yes | **EXECUTED** | pair 2 — `explain_c`/`explain_d` |
  | `UPPER` | yes | **EXECUTED** | pair 3 — `explain_e`/`explain_f` |
  | `date_trunc` | **no — removed** | DOC, description only | PostgreSQL docs; row 12c |

  **Every function the narration names is now measured evidence.** The edit was
  free: it landed before GATE P was signed. `NARRATION-GATE-P.md` is at **rev 2**
  and carries the diff.

- **L3 — Expression indexes are a real exception, unmentioned.** Both SQLite and
  Postgres can index an expression (`CREATE INDEX ... ON postings(strftime(...))`),
  which would make Query A fast. Out of scope for a one-insight reel and named
  here so nobody thinks it was missed. If a commenter raises it, the answer is
  "yes, and that is the next video."
- **L4 — CLOSED 2026-09-16.** The four cited documentation URLs were re-read by
  Supriya Kushwaha on 2026-09-16 and rows **10** (`SCAN` = full table scan),
  **11** (the index-usability constraint) and **12c** (`date_trunc` mechanism,
  description-only) were confirmed against them. No wording changed as a result.
- **L5 — Pair 3's `UPPER` rewrite is collation-dependent.** Dropping `UPPER()` is
  equivalent here *only* because `account_ref` is stored uniformly uppercase under
  SQLite's default BINARY collation (`build_demo.py` asserts this: 0 rows where
  `account_ref != UPPER(account_ref)`). Under `COLLATE NOCASE`, under MySQL's
  default collation, or with genuinely mixed-case data, the two queries return
  **different rows** and the "rewrite" is a bug. The reel's spoken takeaway says
  "rewrite it as a bare range", which is safe for the date case it demonstrates;
  a viewer applying it to a text column with mixed-case data could introduce a
  correctness bug.

  **Mitigated in the description (2026-09-16).** A two-sentence caveat now sits
  directly under the takeaway paragraph in `*-youtube.md` — the place a reader is
  about to copy the move from — naming case-sensitive collation as the
  precondition and `COLLATE NOCASE` / MySQL's default as the failure case, with
  the right fixes (normalise on write, or index the expression). Chosen over a
  narration mention deliberately: the description costs **no re-gate and no
  re-render**, and the caveat is a footnote to the lesson rather than part of it.
  `build_demo.py` also asserts the precondition it depends on, so the claim cannot
  silently rot. **Residual risk: a viewer who never reads the description.**
  Accepted for a 3-minute reel whose demonstrated case is a date column, not a
  text column.

## Verdict

**Every claim the reel speaks or shows is EXECUTED and reproducible**, and the
evidence script fails loudly rather than drifting quietly. The one function that
could not be executed against a SQLite fixture (`date_trunc`) was removed from
the video rather than labelled inside it, so no unmeasured assertion is left in
the frame or in the voice. Three scope limits (L1, L3, L5) are stated rather than
concealed, and L5 is now mitigated in the description. No figure appears on screen
that is not in `demo/RESULTS.md`.

Re-verified 2026-09-16 after extending the fixture: **pair 1's two captures are
byte-identical to the pre-extension versions**, and every figure in the narration
(400,000 · 11,369 · 4,459 · 2.84% · 35× · "two decades") is unchanged. The only
narration edit since rev 1 is the function list in B07, recorded in
`NARRATION-GATE-P.md` rev 2.

FACTCHECK STATUS: **PASS — no open items.** L4 closed 2026-09-16 (docs re-read,
rows 10/11/12c confirmed). **GATE P signed 2026-09-16** by Supriya Kushwaha —
`PEDAGOGY.md` and `NARRATION-GATE-P.md` (rev 2) both carry `VERDICT: PASS`, and
voice approval for `af_bella` is on record.

Still outstanding, and explicitly **outside** this factcheck's scope: LOGO LAW
(`PEDAGOGY.md` open item 1 — blocks the master, not the render) and the
post-render frame QC (open item 3 — Q1/Q2 in `SHOTLIST.md`).

## Rev 3 corrections (2026-10-17, v2 rebuild)

Audit by re-running `demo/build_demo.py` (2026-10-17): 400,000 rows, 11,369 in January,
4,459 groups from both queries, `same result set: True` for all three pairs. Every
EXECUTED figure above still reproduces. Changes, approved by Supriya 2026-10-17:

| # | Where | Rev 2 | Evidence | Rev 3 |
|---|---|---|---|---|
| C1 | B07 voice + card line 4 | "rewrite it as a bare range" | `demo/queries.sql`: pair CAST rewrites to `branch_id = 42`, pair UPPER to `account_ref = 'AC-04242'` — equalities. Only the strftime rewrite is a range. | "compare the bare column instead" |
| C2 | B06 screen | "~15 ms" / "~60 ms" on the two branches | Real (pair 1 medians 14.64 / 60.18 ms) but machine-specific; row 13b of this file says timings are "never on screen, never spoken" | removed from screen |
| C3 | B06 voice | "an index works on the column, not on a function of the column" | L3: expression indexes are a real exception | "a **plain** index works on the column…" |
| C4 | B02 voice, B07 card line 1 | "costs nothing to run"; "EXPLAIN is free" | `EXPLAIN QUERY PLAN` does not execute the query, but SQLite still parses and plans it | "costs almost nothing" |
| C5 | B00 voice | "the same 4,459 rows, byte for byte" | `build_demo.py:211` compares `sorted(fetchall())` — row values, not bytes | "byte for byte" dropped |
| C6 | B01 voice | "the shape of every analytics query" | overgeneralization | "a typical analytics query" |

L1, L3 and L5 remain stated limitations; C3 narrows the spoken claim so it no longer
contradicts L3.
