"""Clustered groups: everyone born inside one W-day window of the calendar.
Real day weights (SSA 2000-2014, Feb 29 dropped, circular year). Exact DP, no sampling."""
import csv, json, math
from collections import defaultdict
import datetime as dt
t = defaultdict(int)
for r in csv.DictReader(open("data/US_births_2000-2014_SSA.csv")):
    m, d = int(r["month"]), int(r["date_of_month"])
    if (m, d) == (2, 29): continue
    t[(m, d)] += int(r["births"])
days = [(dt.date(2001, 1, 1) + dt.timedelta(i)) for i in range(365)]  # 2001 is non-leap
w = [t[(x.month, x.day)] for x in days]

def p_match(n, p):
    s = sum(p); p = [x / s for x in p]
    e = [1.0] + [0.0] * n
    for x in p:
        for k in range(n, 0, -1): e[k] += e[k - 1] * x
    return 1 - math.factorial(n) * e[n]

def n_for(target, p):
    n = 2
    while p_match(n, p) < target: n += 1
    return n

out = {}
for W in (365, 180, 90, 60, 30, 14, 7):
    vals23, n50 = [], []
    for s in range(365):
        p = [w[(s + i) % 365] for i in range(W)]
        vals23.append(p_match(23, p))
        if W <= 90 and s % 15 == 0: n50.append(n_for(.5, p))
    out[W] = {"mean": round(sum(vals23) / 365, 4), "min": round(min(vals23), 4), "max": round(max(vals23), 4),
              "uniform_same_W": round(p_match(23, [1] * W), 4),
              "people_for_50pct_range": [min(n50), max(n50)] if n50 else None}
# seasonal view: busiest vs quietest 30-day window
json.dump(out, open("cluster-rates.json", "w"), indent=2)
for W, v in out.items(): print(W, v)
