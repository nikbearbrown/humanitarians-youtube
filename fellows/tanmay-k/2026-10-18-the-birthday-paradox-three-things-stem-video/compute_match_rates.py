"""Birthday-paradox match rates: uniform model vs real US birth calendars.
Data: US federal births-by-day (NCHS 1994-2003, SSA 2000-2014), copies from
fivethirtyeight/data (CC BY 4.0). Seed fixed for reproducibility."""
import csv, json, math, random
from collections import defaultdict
SEED = 2701
FILES = {"NCHS 1994-2003": "data/US_births_1994-2003_CDC_NCHS.csv",
         "SSA 2000-2014": "data/US_births_2000-2014_SSA.csv"}

def p_match_uniform(n, d=365):
    q = 1.0
    for i in range(n): q *= (d - i) / d
    return 1 - q

def p_match_exact(n, p):
    """P(at least two share) for n people with day probabilities p (exact DP on elementary symmetric polys)."""
    e = [1.0] + [0.0] * n
    for x in p:
        for k in range(n, 0, -1): e[k] += e[k - 1] * x
    return 1 - math.factorial(n) * e[n]

def n_for(target, f):
    n = 1
    while f(n) < target: n += 1
    return n

def calendar(path, drop_feb29=False):
    t = defaultdict(int)
    for r in csv.DictReader(open(path)):
        m, d = int(r["month"]), int(r["date_of_month"])
        if drop_feb29 and (m, d) == (2, 29): continue
        t[(m, d)] += int(r["births"])
    tot = sum(t.values())
    return {k: v / tot for k, v in t.items()}

out = {"seed": SEED, "uniform": {}, "real": {}}
for n in (10, 23, 30, 40, 50, 57, 70):
    out["uniform"][n] = round(p_match_uniform(n), 4)
out["uniform"]["n_for_50pct"] = n_for(.5, p_match_uniform)
out["uniform"]["n_for_99pct"] = n_for(.99, p_match_uniform)
# "someone shares MY birthday" (a specific day): 1-(364/365)^n
out["uniform"]["n_match_me_50pct"] = math.ceil(math.log(.5) / math.log(364 / 365))
out["uniform"]["p_match_me_at_23"] = round(1 - (364 / 365) ** 22, 4)  # 22 others
rng = random.Random(SEED)
for name, path in FILES.items():
    for tag, drop in (("with Feb 29", False), ("365-day (no Feb 29)", True)):
        cal = calendar(path, drop)
        days = list(cal); w = [cal[d] for d in days]; p = [cal[d] for d in days]
        res = {"max_day_over_mean": round(max(w) * len(w), 3), "min_day_over_mean": round(min(w) * len(w), 3)}
        for n in (23, 30, 50):
            ex = p_match_exact(n, p)
            trials = 400_000
            hits = 0
            for _ in range(trials):
                s = rng.choices(range(len(days)), weights=w, k=n)
                hits += len(set(s)) < n
            res[n] = {"exact": round(ex, 4), "simulated": round(hits / trials, 4)}
        res["n_for_50pct"] = n_for(.5, lambda k: p_match_exact(k, p))
        out["real"][f"{name} | {tag}"] = res
json.dump(out, open("match-rates.json", "w"), indent=2)
print(json.dumps(out, indent=2))
