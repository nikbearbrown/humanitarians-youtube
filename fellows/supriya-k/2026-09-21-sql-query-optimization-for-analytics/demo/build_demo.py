#!/usr/bin/env python3
"""build_demo.py — EXECUTABLE EVIDENCE for the reel
"SQL Query Optimization for Analytics" (fellows/supriya-k, 2026-09-16).

Builds a local, free, deterministic SQLite analytics table and captures the
REAL `EXPLAIN QUERY PLAN` output for THREE pairs of logically identical queries.
Each pair differs by exactly one thing: whether the indexed column appears BARE
in the predicate, or wrapped in a function.

  pair 1  strftime  posted_at    strftime('%Y-%m', posted_at) = '2026-01'
                                 vs  posted_at >= '2026-01-01' AND < '2026-02-01'
  pair 2  CAST      branch_id    CAST(branch_id AS TEXT) = '42'
                                 vs  branch_id = 42
  pair 3  UPPER     account_ref  UPPER(account_ref) = 'AC-04242'
                                 vs  account_ref = 'AC-04242'

In every pair both queries return the SAME rows. Only the bare-column version
can use the index. The plan is the evidence.

No network, no API keys, no paid service. Deterministic: seeded PRNG, so the row
counts and plans in demo/RESULTS.md reproduce byte-for-byte.

EXITS NON-ZERO if any pair's two queries stop returning identical result sets —
the evidence is self-checking, so a silent drift cannot reach the reel.

    python3 build_demo.py        # rebuilds postings.db + writes the capture files
"""
import random
import sqlite3
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DB = HERE / "postings.db"
SEED = 20260916
N_ROWS = 400_000
N_ACCOUNTS = 5_000
START = date(2024, 1, 1)
END = date(2026, 12, 31)

# The UPPER pair filters on account_ref; the CAST pair filters on branch_id.
#
# WHY NOT CAST(account_id AS TEXT)?  Because pair 1 GROUPs BY account_id. Putting
# an index on account_id lets the planner satisfy that GROUP BY by walking the
# index instead of building a temp B-tree, which rewrites pair 1's plan A from
#     |--SCAN postings              +  USE TEMP B-TREE FOR GROUP BY
# to
#     `--SCAN postings USING INDEX idx_postings_account_id
# Still a full scan of all 400,000 rows — but it prints the words "USING INDEX"
# on the SCAN side, which flatly contradicts the reel's narration and would make
# B03's on-screen evidence teach the opposite of the lesson. So the CAST probe
# uses branch_id, a dimension key pair 1 never touches. Same canonical mistake
# ("the key arrived as text from a CSV"), no collateral damage to pair 1.
PROBE_ACCOUNT = 4242
PROBE_REF = f"AC-{PROBE_ACCOUNT:05d}"          # 'AC-04242' — stored already uppercase
N_BRANCHES = 250
PROBE_BRANCH = 42                              # in range [1, 250]

AGG = "SELECT COUNT(*) AS n, SUM(amount_cents) AS total_cents\nFROM postings\n"

# --- pair 1 — strftime on an indexed DATE column -------------------------------
Q_NON_SARGABLE = """SELECT account_id, SUM(amount_cents) AS total_cents
FROM postings
WHERE strftime('%Y-%m', posted_at) = '2026-01'
GROUP BY account_id;"""

Q_SARGABLE = """SELECT account_id, SUM(amount_cents) AS total_cents
FROM postings
WHERE posted_at >= '2026-01-01' AND posted_at < '2026-02-01'
GROUP BY account_id;"""

# --- pair 2 — CAST on an indexed INTEGER column --------------------------------
# The classic analytics version of this bug: the id arrived as text from a CSV or
# an API, so the filter stringifies the column to compare it. Same rows, no index.
Q_CAST_NON_SARGABLE = AGG + f"WHERE CAST(branch_id AS TEXT) = '{PROBE_BRANCH}';"
Q_CAST_SARGABLE     = AGG + f"WHERE branch_id = {PROBE_BRANCH};"

# --- pair 3 — UPPER on an indexed TEXT column ----------------------------------
# account_ref is stored ALREADY uppercase, so the UPPER() is a defensive habit
# that buys nothing and costs the index. That is the point: the wrapper is pure
# cost here, not a bug in the logic. (See the collation caveat in RESULTS.md.)
Q_UPPER_NON_SARGABLE = AGG + f"WHERE UPPER(account_ref) = '{PROBE_REF}';"
Q_UPPER_SARGABLE     = AGG + f"WHERE account_ref = '{PROBE_REF}';"

# pair_id, human label, wrapped query + its capture file, bare query + its file
PAIRS = [
    ("strftime", "strftime() on an indexed DATE column",
     Q_NON_SARGABLE,       "explain_a_non_sargable.txt",
     Q_SARGABLE,           "explain_b_sargable.txt"),
    ("CAST", "CAST() on an indexed INTEGER column",
     Q_CAST_NON_SARGABLE,  "explain_c_non_sargable_cast.txt",
     Q_CAST_SARGABLE,      "explain_d_sargable_cast.txt"),
    ("UPPER", "UPPER() on an indexed TEXT column",
     Q_UPPER_NON_SARGABLE, "explain_e_non_sargable_upper.txt",
     Q_UPPER_SARGABLE,     "explain_f_sargable_upper.txt"),
]


def build() -> None:
    """Build the fixture.

    IMPORTANT — do not add an rng call to the row loop. `account_ref` and
    `branch_id` are both DERIVED from `account_id` on purpose: they consume no
    random numbers, so the PRNG stream (and therefore every posted_at value, and
    therefore the 11,369-row January figure quoted throughout the reel) is
    bit-identical to the original single-index fixture.
    """
    DB.unlink(missing_ok=True)
    rng = random.Random(SEED)
    span = (END - START).days
    con = sqlite3.connect(DB)
    con.executescript(
        """
        CREATE TABLE postings (
            posting_id   INTEGER PRIMARY KEY,
            account_id   INTEGER NOT NULL,
            account_ref  TEXT    NOT NULL,   -- 'AC-04242', always uppercase
            branch_id    INTEGER NOT NULL,   -- derived dimension key, 1..250
            posted_at    TEXT    NOT NULL,   -- ISO date, 'YYYY-MM-DD'
            amount_cents INTEGER NOT NULL
        );
        """
    )
    rows = []
    for i in range(N_ROWS):
        account_id = rng.randrange(1, N_ACCOUNTS + 1)
        posted_at = (START + timedelta(days=rng.randrange(span + 1))).isoformat()
        amount_cents = rng.randrange(-500_000, 500_000)
        rows.append((i + 1, account_id, f"AC-{account_id:05d}",
                     (account_id % N_BRANCHES) + 1, posted_at, amount_cents))
    con.executemany("INSERT INTO postings VALUES (?,?,?,?,?,?)", rows)
    con.executescript(
        """
        CREATE INDEX idx_postings_posted_at   ON postings(posted_at);
        CREATE INDEX idx_postings_account_ref ON postings(account_ref);
        CREATE INDEX idx_postings_branch_id   ON postings(branch_id);
        -- Deliberately NO index on account_id — see the PROBE_ACCOUNT comment.
        ANALYZE;
        """
    )
    con.commit()
    con.close()


def sh(sql: str) -> str:
    """Run SQL through the sqlite3 CLI so the captured text is what a human sees."""
    out = subprocess.run(
        ["sqlite3", str(DB)],
        input=sql,
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.rstrip("\n")


def capture(query: str, filename: str) -> str:
    """Write the unedited EXPLAIN QUERY PLAN capture and return the plan text."""
    plan = sh("EXPLAIN QUERY PLAN " + query)
    (HERE / filename).write_text(
        "$ sqlite3 postings.db\nsqlite> EXPLAIN QUERY PLAN\n"
        + query
        + "\n\n"
        + plan
        + "\n"
    )
    return plan


def main() -> None:
    build()
    con = sqlite3.connect(DB)

    total = con.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    jan = con.execute(
        "SELECT COUNT(*) FROM postings "
        "WHERE posted_at >= '2026-01-01' AND posted_at < '2026-02-01'"
    ).fetchone()[0]
    probe_ref_rows = con.execute(
        "SELECT COUNT(*) FROM postings WHERE account_ref = ?", (PROBE_REF,)
    ).fetchone()[0]
    probe_branch_rows = con.execute(
        "SELECT COUNT(*) FROM postings WHERE branch_id = ?", (PROBE_BRANCH,)
    ).fetchone()[0]
    # Sanity: account_ref must be a pure function of account_id, and uppercase.
    mismatched = con.execute(
        "SELECT COUNT(*) FROM postings WHERE account_ref != UPPER(account_ref)"
    ).fetchone()[0]

    print(f"sqlite {sqlite3.sqlite_version}  rows={total}  jan2026_rows={jan}")
    print(f"selectivity (January 2026) = {jan}/{total} = {100*jan/total:.2f}%")
    print(f"probe account_ref {PROBE_REF} rows = {probe_ref_rows}"
          f"  ({100*probe_ref_rows/total:.3f}%)")
    print(f"probe branch_id {PROBE_BRANCH} rows = {probe_branch_rows}"
          f"  ({100*probe_branch_rows/total:.3f}%)")
    print(f"rows where account_ref != UPPER(account_ref) = {mismatched}  (must be 0)")

    failures = []
    if mismatched:
        failures.append(
            f"account_ref is not uniformly uppercase ({mismatched} rows) — the UPPER() "
            "pair is only equivalent because storage is already normalised"
        )

    queries_doc = []
    for pid, label, q_wrapped, f_wrapped, q_bare, f_bare in PAIRS:
        rows_wrapped = con.execute(q_wrapped).fetchall()
        rows_bare = con.execute(q_bare).fetchall()
        identical = sorted(rows_wrapped) == sorted(rows_bare)

        plan_wrapped = capture(q_wrapped, f_wrapped)
        plan_bare = capture(q_bare, f_bare)

        print(f"\n=== pair {pid} — {label} ===")
        print(f"same result set: {identical}"
              f"  (rows returned: wrapped={len(rows_wrapped)} bare={len(rows_bare)})")
        print(f"--- wrapped ({f_wrapped}) ---\n{plan_wrapped}")
        print(f"--- bare    ({f_bare}) ---\n{plan_bare}")

        if not identical:
            failures.append(
                f"pair {pid}: the two queries do NOT return the same rows — "
                f"the rewrite is not equivalent, so it is not evidence"
            )

        queries_doc.append(
            f"-- pair {pid} — {label}\n"
            f"-- wrapped (non-sargable) -> {f_wrapped}\n{q_wrapped}\n\n"
            f"-- bare (sargable) -> {f_bare}\n{q_bare}\n"
        )

    con.close()
    (HERE / "queries.sql").write_text("\n".join(queries_doc))

    if failures:
        print("\nEVIDENCE FAILURE:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("\nall pairs verified: every rewrite returns an identical result set")


if __name__ == "__main__":
    main()
