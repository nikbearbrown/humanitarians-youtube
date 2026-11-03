#!/usr/bin/env python3
"""timing.py — measured wall-clock for all three plan pairs.

SUPPORTING EVIDENCE ONLY. The reel's load-bearing claim is ROWS READ, which is a
structural property of the plan. Milliseconds belong to the hardware: they are
machine-specific and noisy run to run, so this script reports a spread (min /
median / max over N runs) rather than a single number pretending to be exact.

    python3 timing.py [N]        # N runs per query, default 9
"""
import sqlite3
import statistics
import sys
import time

from build_demo import (
    DB, PAIRS,
    Q_NON_SARGABLE, Q_SARGABLE,
    Q_CAST_NON_SARGABLE, Q_CAST_SARGABLE,
    Q_UPPER_NON_SARGABLE, Q_UPPER_SARGABLE,
)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 9


def bench(q, n=N):
    """Fresh connection + cache_size=0 per run, so we are not timing the cache."""
    ts = []
    for _ in range(n):
        con = sqlite3.connect(DB)
        con.execute("PRAGMA cache_size=0")
        t = time.perf_counter()
        con.execute(q).fetchall()
        ts.append((time.perf_counter() - t) * 1000)
        con.close()
    return min(ts), statistics.median(ts), max(ts)


print(f"{N} runs per query · fresh connection · PRAGMA cache_size=0\n")
print(f"{'pair / plan':<44} {'min':>9} {'median':>9} {'max':>9}")
print("-" * 74)

for pid, label, q_wrapped, _fw, q_bare, _fb in PAIRS:
    qs = {
        "strftime": (Q_NON_SARGABLE, Q_SARGABLE),
        "CAST": (Q_CAST_NON_SARGABLE, Q_CAST_SARGABLE),
        "UPPER": (Q_UPPER_NON_SARGABLE, Q_UPPER_SARGABLE),
    }[pid]
    lo_w, md_w, hi_w = bench(qs[0])
    lo_b, md_b, hi_b = bench(qs[1])
    print(f"{pid + '  wrapped -> SCAN':<44} {lo_w:8.2f}  {md_w:8.2f}  {hi_w:8.2f}")
    print(f"{pid + '  bare    -> SEARCH':<44} {lo_b:8.2f}  {md_b:8.2f}  {hi_b:8.2f}")
    print(f"{'':<44} {'speedup (median): ' + format(md_w / md_b, '.1f') + '×':>29}")
    print()

print("All figures in milliseconds. Machine-specific — see FACTCHECK.md row 13.")
