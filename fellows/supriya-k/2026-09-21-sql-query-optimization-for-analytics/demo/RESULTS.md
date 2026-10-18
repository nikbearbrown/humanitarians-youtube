# demo/ — EXECUTABLE EVIDENCE for "SQL, Read Fewer Rows."

Every number spoken or shown in this reel comes from this folder. Nothing here
is a mock, a screenshot request, or pseudocode: `build_demo.py` builds a real
local SQLite database and captures real `EXPLAIN QUERY PLAN` output.

**Free tier, no keys, no network.** SQLite ships with macOS (`/usr/bin/sqlite3`).

## Reproduce

```bash
cd demo
python3 build_demo.py     # rebuilds postings.db, rewrites all six explain_*.txt
python3 timing.py         # measured wall-clock, all three pairs (supporting only)
```

Deterministic: `SEED = 20260916`, so row counts and plans reproduce exactly.
`postings.db` is gitignored (18 MB, regenerable); the captures are tracked.

**The evidence is self-checking.** For each pair, `build_demo.py` runs both
queries and compares their full result sets. If any rewrite ever stops being
equivalent, the script prints `EVIDENCE FAILURE` and **exits non-zero** — a
silent drift cannot reach the reel. (Verified by deliberately breaking one
rewrite: exit code 1.)

## The fixture

| Fact | Value |
|---|---|
| Engine | SQLite `3.45.3` (Python `sqlite3` module); CLI captures via `/usr/bin/sqlite3` 3.51.0 |
| Table | `postings(posting_id, account_id, account_ref, branch_id, posted_at, amount_cents)` |
| Rows | **400,000** |
| Accounts | 5,000 · Branches | 250 |
| Date span | 2024-01-01 → 2026-12-31 |
| Indexes | `idx_postings_posted_at`, `idx_postings_account_ref`, `idx_postings_branch_id`, then `ANALYZE` |

`account_ref` (`'AC-04242'`, always uppercase) and `branch_id` (1–250) are both
**derived** from `account_id` and consume no random numbers, so the PRNG stream —
and therefore every `posted_at` value, and therefore the 11,369-row January
figure the reel quotes — is bit-identical to the original single-index fixture.

### Why there is no index on `account_id`

Deliberate, and worth knowing before anyone "fixes" it. Pair 1 does
`GROUP BY account_id`. Add an index on `account_id` and the planner satisfies that
grouping by walking the index instead of building a temp B-tree, which rewrites
pair 1's wrapped plan from

```
|--SCAN postings
`--USE TEMP B-TREE FOR GROUP BY
```

to

```
`--SCAN postings USING INDEX idx_postings_account_id
```

It is still a full scan of all 400,000 rows — but it prints the words
**USING INDEX on the SCAN side**, which contradicts the reel's narration and would
make B03's on-screen evidence teach the opposite of the lesson. So the `CAST`
probe uses `branch_id`, a dimension key pair 1 never touches: same canonical
mistake ("the key arrived as text from a CSV"), no collateral damage to pair 1.

## The three pairs (demo/queries.sql)

Each pair is two logically identical queries. Only one thing differs: whether the
indexed column appears **bare** in the predicate, or **wrapped in a function**.

| Pair | Column | Wrapped (non-sargable) | Bare (sargable) | Rows matched |
|---|---|---|---|---|
| 1 `strftime` | `posted_at` (DATE) | `strftime('%Y-%m', posted_at) = '2026-01'` | `posted_at >= '2026-01-01' AND posted_at < '2026-02-01'` | 11,369 (2.84%) |
| 2 `CAST` | `branch_id` (INTEGER) | `CAST(branch_id AS TEXT) = '42'` | `branch_id = 42` | 1,625 (0.406%) |
| 3 `UPPER` | `account_ref` (TEXT) | `UPPER(account_ref) = 'AC-04242'` | `account_ref = 'AC-04242'` | 76 (0.019%) |

Pair 1 aggregates `GROUP BY account_id`; pairs 2 and 3 are single-row aggregates.

## Captured plans — the load-bearing evidence

All six captures are unedited. **Every wrapped query reads all 400,000 rows.
Every bare query seeks.**

### Pair 1 — `strftime` on an indexed DATE column

`explain_a_non_sargable.txt` — shown verbatim in B03 (left card):

```
QUERY PLAN
|--SCAN postings
`--USE TEMP B-TREE FOR GROUP BY
```

`explain_b_sargable.txt` — shown verbatim in B03 (right card):

```
QUERY PLAN
|--SEARCH postings USING INDEX idx_postings_posted_at (posted_at>? AND posted_at<?)
`--USE TEMP B-TREE FOR GROUP BY
```

Same result set: **True** — 4,459 groups from both. **35× fewer rows read**
(400,000 / 11,369 = 35.2).

### Pair 2 — `CAST` on an indexed INTEGER column

`explain_c_non_sargable_cast.txt`:

```
QUERY PLAN
`--SCAN postings
```

`explain_d_sargable_cast.txt`:

```
QUERY PLAN
`--SEARCH postings USING INDEX idx_postings_branch_id (branch_id=?)
```

Same result set: **True** — one identical aggregate row from both.
**246× fewer rows read** (400,000 / 1,625).

### Pair 3 — `UPPER` on an indexed TEXT column

`explain_e_non_sargable_upper.txt`:

```
QUERY PLAN
`--SCAN postings
```

`explain_f_sargable_upper.txt`:

```
QUERY PLAN
`--SEARCH postings USING INDEX idx_postings_account_ref (account_ref=?)
```

Same result set: **True** — one identical aggregate row from both.
**5,263× fewer rows read** (400,000 / 76).

**The `UPPER()` here is not even fixing anything.** `account_ref` is stored
already uppercase, so the wrapper is a defensive habit that changes no rows and
costs the entire index. That is the sharpest version of the lesson in the folder.

## Supporting evidence — measured wall-clock (`timing.py`)

9 runs per query, fresh connection each run, `PRAGMA cache_size=0`, milliseconds:

| Pair | Plan | min | median | max | Speedup (median) |
|---|---|---|---|---|---|
| 1 `strftime` | wrapped → SCAN | 59.41 | **60.18** | 61.34 | — |
| 1 `strftime` | bare → SEARCH | 14.30 | **14.64** | 15.36 | **4.1×** |
| 2 `CAST` | wrapped → SCAN | 17.24 | **17.43** | 17.66 | — |
| 2 `CAST` | bare → SEARCH | 1.61 | **1.62** | 1.75 | **10.8×** |
| 3 `UPPER` | wrapped → SCAN | 28.74 | **28.86** | 29.20 | — |
| 3 `UPPER` | bare → SEARCH | 0.09 | **0.09** | 0.11 | **333×** |

Machine-specific (Darwin 25.5.0, this laptop) and labelled as such in
`FACTCHECK.md` row 13.

### Read this table the right way — it makes the reel's point twice

All three wrapped queries read **the same 400,000 rows**, yet they take 17 ms,
29 ms and 60 ms. The difference is per-row work, not rows read: `strftime` has to
parse a date string 400,000 times *and* the query builds a temp B-tree for the
`GROUP BY`; `CAST` on an integer is cheap by comparison.

That is exactly why **rows read is the reel's load-bearing claim and milliseconds
are not.** Rows read is a structural property of the plan and reproduces on any
machine. Milliseconds depend on the function, the aggregate, the page cache and
the hardware — which is why no timing figure is ever spoken in the narration.

## What is NOT claimed here

- Not that N× fewer rows means N× faster. Pair 1 read 35× fewer rows and ran
  ~4× faster. The reel never multiplies one into the other.
- Not that this generalises to every engine verbatim. PostgreSQL reports
  `Seq Scan` / `Index Scan` rather than `SCAN` / `SEARCH`; the mechanism is the
  same and the reel's takeaway says "run EXPLAIN", not "run EXPLAIN QUERY PLAN".
- **Not that `date_trunc` was tested here.** It is a PostgreSQL function and does
  not exist in SQLite, so it cannot be executed against this fixture at all. It
  remains the one documentation-only item — see `FACTCHECK.md` L2.
- **Not that `UPPER()` is always removable.** Pair 3's rewrite is equivalent only
  because `account_ref` is stored uniformly uppercase under SQLite's default
  BINARY collation (`build_demo.py` asserts 0 rows where
  `account_ref != UPPER(account_ref)`). Under a case-insensitive collation
  (`COLLATE NOCASE`, or MySQL's default) or with genuinely mixed-case data, the
  two queries are **not** equivalent and the rewrite would be a bug. The fix
  there is to normalise on write, or index the expression — not to drop the
  `UPPER()`.
