"""Check the rule  n ~ round_half_up(1.2*sqrt(d) + 0.5)  against the exact smallest n with P(match) >= 50%,
for d equally likely slots. Also exact values used in B16/B17 and day-weight spread for B09."""
import math, csv, json
from collections import defaultdict
def pm(n, d):
    if n > d: return 1.0
    q = 1.0
    for i in range(n): q *= (d - i) / d
    return 1 - q
def n50(d):
    n = 2
    while pm(n, d) < .5: n += 1
    return n
def rule(d): return math.floor(1.2 * math.sqrt(d) + 0.5 + 0.5)  # round half up
out = {"rule_vs_exact": {}, "cases": {}, "spread": {}}
bad = []
for d in range(2, 2001):
    e, r = n50(d), rule(d)
    if e != r: bad.append((d, e, r))
out["rule_vs_exact"] = {"range": [2, 2000], "mismatches": len(bad), "max_abs_miss": max([abs(e - r) for _, e, r in bad] or [0]),
                        "first_mismatches": bad[:10]}
for d in (365, 180, 90, 60, 30, 14, 7, 12, 50, 100, 25):
    out["cases"][d] = {"exact_n": n50(d), "rule_n": rule(d), "raw": round(1.2 * math.sqrt(d) + .5, 2)}
out["cases"]["month_4_5"] = [round(pm(4, 12), 4), round(pm(5, 12), 4)]
out["cases"]["pick1to50_8_9"] = [round(pm(8, 50), 4), round(pm(9, 50), 4)]
# day-weight spread (SSA 2000-2014, Feb 29 dropped)
t = defaultdict(int)
for r in csv.DictReader(open("data/US_births_2000-2014_SSA.csv")):
    m, d = int(r["month"]), int(r["date_of_month"])
    if (m, d) != (2, 29): t[(m, d)] += int(r["births"])
mean = sum(t.values()) / 365
ratios = sorted(v / mean for v in t.values())
for lo, hi in ((0.9, 1.1), (0.85, 1.15), (0.8, 1.2)):
    out["spread"][f"{lo}-{hi}"] = round(sum(lo <= x <= hi for x in ratios) / 365, 3)
out["spread"]["min_max"] = [round(ratios[0], 3), round(ratios[-1], 3)]
out["spread"]["lowest5"] = [round(x, 3) for x in ratios[:5]]
json.dump(out, open("sqrt-rule.json", "w"), indent=2, default=str)
print(json.dumps(out, indent=1, default=str))
