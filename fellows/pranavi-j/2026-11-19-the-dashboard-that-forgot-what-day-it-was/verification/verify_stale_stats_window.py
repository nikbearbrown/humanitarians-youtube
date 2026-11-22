#!/usr/bin/env python3
"""
Live verification harness for the F1 fix (FeedCRUD.get_stats(), Project 29
regulatory intelligence dashboard backend, mycroft repo).

Unlike this fellow's D1 report (which had no working DATABASE_URL and fell
back to a synthetic reconstruction -- see
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/verification/
verify_dashboard_stats.py's own docstring), this session DOES have a
reachable live Postgres instance (`PGPASSWORD=postgres psql -h localhost
-p 5431 -U postgres -d mycroft_intelligence`), confirmed working before
this script was written (see FRICTIONAL.md). So this harness runs the real
query text directly against the real, live `mycroft_intelligence` DB via
psycopg2 -- not a synthetic/sqlite reconstruction.

Does NOT modify anything in /Users/pranavijs/mycroft or the live DB --
every query here is a read-only SELECT. Confirmed via
`git -C /Users/pranavijs/mycroft status --short` before and after this
session (clean both times; the F1 fix was already committed before this
video build started) -- see FRICTIONAL.md.

What this script does:
  1. Extracts the REAL, current (already-fixed) severity-count SQL block
     from crud.py on disk and confirms it appears verbatim (exactly once) --
     refuses to proceed on a mismatch, same discipline as the D1 harness.
  2. Reconstructs the PRE-FIX SQL by re-adding exactly the one clause
     F1-VERIFICATION.md's diff removed (`WHERE created_at >= NOW() -
     INTERVAL '7 days'`) -- the inverse of the real fix, not an
     independently-imagined "old" query.
  3. Runs both queries, unmodified, directly against the live DB.
  4. Separately replicates list_feeds()'s actual default ordering/limit
     (`ORDER BY created_at DESC, urgency_score DESC`, the frontend's real
     `limit: 100` from App.jsx's `feedsAPI.listFeeds({ limit: 100 })`, no
     date filter) to show the top-100 slice the frontend actually renders
     contains real Critical/High rows -- the concrete panel-vs-panel
     disagreement, not just query-text inspection.
  5. Prints a before/after table and checks it against F1-VERIFICATION.md's
     own reported numbers (0/0/0/0 -> 33/98/280/0; 24 Critical / 8 High in
     the top-100 slice).
"""
import re
import sys

import psycopg2
import psycopg2.extras

CRUD_PATH = (
    "/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/"
    "Regulatory_QA/backend/app/crud.py"
)

DB_CONFIG = dict(
    host="localhost",
    port=5431,
    user="postgres",
    password="postgres",
    dbname="mycroft_intelligence",
)

with open(CRUD_PATH, "r", encoding="utf-8") as f:
    crud_src = f.read()

# --- Extract the real, current (post-fix) severity SQL block --------------
POST_FIX_SQL = """
                SELECT
                    COUNT(*) FILTER (WHERE impact_level = 'Critical') as critical,
                    COUNT(*) FILTER (WHERE impact_level = 'High') as high,
                    COUNT(*) FILTER (WHERE impact_level = 'Medium') as medium,
                    COUNT(*) FILTER (WHERE impact_level = 'Low') as low
                FROM regulatory_feeds
            """.strip()

occurrences = crud_src.count(POST_FIX_SQL)
if occurrences != 1:
    raise SystemExit(
        f"Expected the real post-fix severity SQL block to appear exactly "
        f"once in {CRUD_PATH}, found {occurrences}. Refusing to trust this "
        f"harness's assumptions -- the F1 fix may have been reverted, "
        f"reformatted, or renamed since this script was written."
    )
print("[ok] real post-fix severity SQL block confirmed verbatim in crud.py (1 match)")

# --- Reconstruct the PRE-FIX SQL by re-adding exactly the removed clause --
# (F1-VERIFICATION.md, "The fix" diff -- the inverse of the one-line removal.)
PRE_FIX_SQL = """
                SELECT
                    COUNT(*) FILTER (WHERE impact_level = 'Critical') as critical,
                    COUNT(*) FILTER (WHERE impact_level = 'High') as high,
                    COUNT(*) FILTER (WHERE impact_level = 'Medium') as medium,
                    COUNT(*) FILTER (WHERE impact_level = 'Low') as low
                FROM regulatory_feeds
                WHERE created_at >= NOW() - INTERVAL '7 days'
            """.strip()

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def run_query(sql, label):
    cur.execute(sql)
    row = dict(cur.fetchone())
    print(f"{label}: {row}")
    return row


print()
print("=== fixture data range (real, live DB) ===")
cur.execute("SELECT MIN(created_at) AS min_created, MAX(created_at) AS max_created FROM regulatory_feeds")
fixture_range = dict(cur.fetchone())
print(fixture_range)

cur.execute("SELECT COUNT(*) AS total_feeds FROM regulatory_feeds")
total_feeds = dict(cur.fetchone())["total_feeds"]
print(f"total_feeds (unwindowed COUNT(*), same as get_stats()'s total_feeds field): {total_feeds}")

print()
print("=== PRE-FIX (reconstructed: real 7-day WHERE clause re-added) ===")
pre = run_query(PRE_FIX_SQL, "pre-fix (7-day window)")

print()
print("=== POST-FIX (real, current SQL from crud.py on disk) ===")
post = run_query(POST_FIX_SQL, "post-fix (unwindowed)")

print()
print("=== list_feeds()'s actual default ordering/limit, no date filter ===")
print("(ORDER BY created_at DESC, urgency_score DESC -- crud.py; LIMIT 100 -- App.jsx's feedsAPI.listFeeds({ limit: 100 }))")
cur.execute(
    """
    SELECT impact_level, COUNT(*) AS n FROM (
        SELECT impact_level FROM regulatory_feeds
        ORDER BY created_at DESC, urgency_score DESC
        LIMIT 100
    ) sub GROUP BY impact_level ORDER BY impact_level
    """
)
top100 = {row["impact_level"]: row["n"] for row in cur.fetchall()}
print(top100)

conn.close()

print()
print("=== ASSERTIONS ===")
assertions = [
    ("fixture min_created == 2026-07-14 (date part)", str(fixture_range["min_created"])[:10] == "2026-07-14"),
    ("fixture max_created == 2026-07-24 (date part)", str(fixture_range["max_created"])[:10] == "2026-07-24"),
    ("total_feeds == 411", total_feeds == 411),
    ("pre.critical == 0", pre["critical"] == 0),
    ("pre.high == 0", pre["high"] == 0),
    ("pre.medium == 0", pre["medium"] == 0),
    ("pre.low == 0", pre["low"] == 0),
    ("post.critical == 33", post["critical"] == 33),
    ("post.high == 98", post["high"] == 98),
    ("post.medium == 280", post["medium"] == 280),
    ("post.low == 0", post["low"] == 0),
    ("top-100 slice Critical == 24", top100.get("Critical") == 24),
    ("top-100 slice High == 8", top100.get("High") == 8),
]
failed = False
for label, ok in assertions:
    print(f"{'PASS' if ok else 'FAIL'} -- {label}")
    if not ok:
        failed = True

if failed:
    print("\nONE OR MORE ASSERTIONS FAILED.")
    sys.exit(1)

print(
    "\nALL ASSERTIONS PASSED: against the real, live mycroft_intelligence DB "
    "(411 rows, created_at 2026-07-14 to 2026-07-24), the pre-fix 7-day-"
    "windowed severity query returns 0/0/0/0 unconditionally, and the real, "
    "current post-fix unwindowed query returns Critical 33 / High 98 / "
    "Medium 280 / Low 0 -- exactly matching F1-VERIFICATION.md's reported "
    "numbers and D1-VERIFICATION.md's own independently-verified unwindowed "
    "impact_level counts. The same live DB's actual list_feeds()-equivalent "
    "top-100 slice (the one FeedList.jsx renders, no date filter) contains "
    "24 real Critical- and 8 real High-tagged rows -- the concrete, "
    "zero-click contradiction between the two panels on the same page."
)
