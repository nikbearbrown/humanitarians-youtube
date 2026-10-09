#!/usr/bin/env python3
"""osworld_check.py — best single small model on the OSWorld-Verified leaderboard.

Downloads the leaderboard's own results file (the page renders it client-side) and lists
the top entry and the best single models of <= 9B parameters — excluding entries that pair
a small model with a larger planner ("w/ gpt-4o"), combine models ("+"), or are MoE models
with more total weights ("A3B"). Needs openpyxl (Anaconda python3 has it).

Run:  python3 osworld_check.py > osworld_check.out
"""
import datetime
import io
import re
import urllib.request

import openpyxl

URL = "http://osworld-v1.xlang.ai/static/data/osworld_verified_results.xlsx"
print("OSWorld-Verified results file:", URL, "fetched", datetime.date.today())
wb = openpyxl.load_workbook(io.BytesIO(urllib.request.urlopen(URL, timeout=60).read()),
                            read_only=True, data_only=True)
rows = list(wb.worksheets[0].iter_rows(values_only=True))
I = {k: i for i, k in enumerate(rows[0]) if k}


def day(v):
    if isinstance(v, (int, float)):
        return (datetime.date(1899, 12, 30) + datetime.timedelta(days=int(v))).isoformat()
    return str(v)[:10]


out = []
for r in rows[1:]:
    try:
        sr = float(r[I["Success rate"]])
    except (TypeError, ValueError):
        continue
    if r[I["Model"]]:
        out.append((sr, r[I["Model"]], r[I["Approach type"]], day(r[I["Date"]]), r[I["Success/Total"]]))
out.sort(reverse=True)
print("scored rows", len(out), "| top:", out[0])
small = [o for o in out if re.search(r"(?<![\d.])([1-9](\.\d)?)B\b", o[1])
         and "w/" not in o[1] and "A3B" not in o[1] and "+" not in o[1]]
print("single model <=9B (no larger planner, no MoE), top 8:")
for o in small[:8]:
    print(" ", o)
print("latest entry date:", max(o[3] for o in out))
