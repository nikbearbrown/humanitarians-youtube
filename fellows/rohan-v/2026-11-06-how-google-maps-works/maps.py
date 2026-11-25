"""EXECUTABLE EVIDENCE for "How Google Maps Works."

A simulated city and a simulated sky, built to show each job a maps app does, with every number measured.
Nothing here is Google's code or Google's data: the methods are the textbook ones Google's own posts describe
in general terms (satellite ranging, shortest paths, speeds from phones, history plus live data, aggregated
visits, rider reports).

  1. WHERE AM I   GPS: ranges from simulated satellites, solved for position AND the phone's clock error;
                  open sky vs a street between tall buildings; why 3 satellites are not enough.
  2. THE ROUTE    a 30 x 30 grid city with local streets, avenues and a highway; Dijkstra vs A* on travel
                  time (nodes explored, same answer).
  3. TRAFFIC      rush hour with a jam and a crash; phones report their speed on each road; estimated speeds
                  vs the truth as the number of phones grows.
  4. ARRIVAL TIME 300 trips; predicted from speed limits, from history, from live phones, and history + live.
  5. HOW BUSY     a cafe's week of visits; only opted-in phones are counted, with privacy noise added; the
                  popular-times bars vs the real crowd; a quiet shop with too little data.
  6. HOW CROWDED  a bus route; a few riders answer "how crowded?"; predicted crowding per trip vs the truth.

    python maps.py        # writes evidence/run.log, results.json, scene.json
"""
import heapq
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
LOG = []
SCENE = {}


def P(s=""):
    print(s)
    LOG.append(s)


rng = np.random.default_rng(1106)
C = 299_792_458.0

# =============================================================== 1. WHERE AM I
R_E, R_S = 6_371_000.0, 26_560_000.0          # Earth radius; GPS orbit radius (about 20,200 km up)


def sky(n, min_el, r):
    """n satellites above min_el degrees elevation, as (az, el) and ECEF positions, for a receiver at (R_E,0,0)."""
    out = []
    while len(out) < n:
        az, el = r.uniform(0, 2 * np.pi), np.arcsin(r.uniform(np.sin(np.radians(min_el)), 1))
        # direction in local east-north-up, then the satellite along that ray at orbit radius
        d = np.array([np.sin(el), np.cos(el) * np.sin(az), np.cos(el) * np.cos(az)])   # (up=x, east=y, north=z)
        rcv = np.array([R_E, 0, 0])
        b = rcv @ d
        t = -b + np.sqrt(b * b - (R_E ** 2 - R_S ** 2))
        out.append((az, el, rcv + t * d))
    return out


def solve(sats, rho, iters=12):
    """Least squares for receiver x, y, z and clock bias (in metres) from pseudoranges."""
    x = np.array([R_E, 0, 0, 0.0]) + np.array([5000, 5000, 5000, 0])
    S = np.array([s[2] for s in sats])
    for _ in range(iters):
        d = np.linalg.norm(S - x[:3], axis=1)
        H = np.hstack([-(S - x[:3]) / d[:, None], np.ones((len(S), 1))])
        dx, *_ = np.linalg.lstsq(H, rho - (d + x[3]), rcond=None)
        x += dx
    return x


def gps_trial(n, min_el, sigma, r, bias_m=0.0, clock_s=1e-3):
    sats = sky(n, min_el, r)
    rcv = np.array([R_E, 0, 0])
    true = np.array([np.linalg.norm(s[2] - rcv) for s in sats])
    rho = true + C * clock_s + r.normal(0, sigma, n) + bias_m * r.random(n)   # bias: reflections in a street canyon
    x = solve(sats, rho)
    return float(np.linalg.norm(x[:3] - rcv)), sats, float(x[3] / C)


P("1. WHERE AM I (simulated GPS: ranges to satellites; the phone's clock is 1 ms off)")
P(f"  a 1 ms clock error is {C * 1e-3 / 1000:,.0f} km of range error, so the phone solves for its clock as a 4th unknown")
open_err = [gps_trial(8, 10, 3.0, rng)[0] for _ in range(400)]
canyon_err = [gps_trial(5, 45, 3.0, rng, bias_m=25.0)[0] for _ in range(400)]
P(f"  open sky, 8 satellites, 3 m ranging noise: median error {np.median(open_err):.1f} m, 95% within {np.percentile(open_err, 95):.1f} m")
P(f"  street between tall buildings, 5 high satellites + reflections: median {np.median(canyon_err):.1f} m, 95% within {np.percentile(canyon_err, 95):.1f} m")
# 3 satellites: 4 unknowns cannot be solved; show it by the rank of the geometry
s3 = sky(3, 10, rng)
H3 = np.hstack([-(np.array([s[2] for s in s3]) - [R_E, 0, 0]) / R_S, np.ones((3, 1))])
P(f"  3 satellites: {np.linalg.matrix_rank(H3)} equations for 4 unknowns (x, y, z, clock): no unique answer")
e_ex, sats_ex, clk = gps_trial(8, 10, 3.0, np.random.default_rng(42))
P(f"  example fix: 8 satellites, error {e_ex:.1f} m, clock error recovered {clk * 1e3:.4f} ms (true 1.0000)")
SCENE["gps"] = dict(sats=[[round(float(np.degrees(a)), 1), round(float(np.degrees(e)), 1)] for a, e, _ in sats_ex],
                    open_med=round(float(np.median(open_err)), 1), open_95=round(float(np.percentile(open_err, 95)), 1),
                    canyon_med=round(float(np.median(canyon_err)), 1), canyon_95=round(float(np.percentile(canyon_err, 95)), 1),
                    example_err=round(e_ex, 1), clock_km=round(C * 1e-3 / 1000))

# =============================================================== 2. THE CITY AND THE ROUTE
N = 30
xs = np.arange(N) * 160.0
pos = {}
for i in range(N):
    for j in range(N):
        pos[(i, j)] = (xs[i] + rng.normal(0, 18), xs[j] + rng.normal(0, 18))
SPEED = {"local": 30, "avenue": 50, "highway": 90}       # km/h limits


def road_class(a, b):
    (i1, j1), (i2, j2) = a, b
    if i1 == i2 and i1 in (7, 22) or j1 == j2 and j1 == 15:
        return "highway" if (i1 == i2 and i1 == 22) or (j1 == j2 and j1 == 15) else "avenue"
    if (i1 == i2 and i1 % 5 == 0) or (j1 == j2 and j1 % 5 == 0):
        return "avenue"
    return "local"


edges = {}
for i in range(N):
    for j in range(N):
        for di, dj in ((1, 0), (0, 1)):
            a, b = (i, j), (i + di, j + dj)
            if b in pos and rng.random() > 0.04:       # a few missing blocks (parks, rivers)
                L = float(np.hypot(pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]))
                cls = road_class(a, b)
                edges[(a, b)] = edges[(b, a)] = dict(len=L, cls=cls, free=SPEED[cls])
adj = {}
for (a, b) in edges:
    adj.setdefault(a, []).append(b)


def travel_time(e, speed_kmh):
    return edges[e]["len"] / (speed_kmh / 3.6)


def shortest(src, dst, speed, astar=False):
    vmax = max(SPEED.values()) / 3.6
    h = (lambda n: np.hypot(pos[n][0] - pos[dst][0], pos[n][1] - pos[dst][1]) / vmax) if astar else (lambda n: 0.0)
    dist, prev, done, order = {src: 0.0}, {}, set(), []
    pq = [(h(src), src)]
    while pq:
        _, u = heapq.heappop(pq)
        if u in done:
            continue
        done.add(u)
        order.append(u)
        if u == dst:
            break
        for v in adj[u]:
            nd = dist[u] + travel_time((u, v), speed[(u, v)])
            if nd < dist.get(v, np.inf):
                dist[v], prev[v] = nd, u
                heapq.heappush(pq, (nd + h(v), v))
    path, n = [dst], dst
    while n != src:
        n = prev[n]
        path.append(n)
    return path[::-1], dist[dst], order


free_speed = {e: d["free"] for e, d in edges.items()}
SRC, DST = (3, 4), (26, 25)
path_d, t_d, order_d = shortest(SRC, DST, free_speed)
path_a, t_a, order_a = shortest(SRC, DST, free_speed, astar=True)
straight = np.hypot(pos[SRC][0] - pos[DST][0], pos[SRC][1] - pos[DST][1])
P("")
P(f"2. THE ROUTE (a {N} x {N} grid city: local streets 30 km/h, avenues 50, a highway 90; {len(edges) // 2} road segments)")
P(f"  from {SRC} to {DST}, {straight / 1000:.1f} km apart as the crow flies")
P(f"  Dijkstra: explored {len(order_d)} of {len(pos)} intersections; best route {t_d / 60:.1f} min, {len(path_d) - 1} segments")
P(f"  A*:       explored {len(order_a)} intersections (aims at the destination); same route: {path_a == path_d}, {t_a / 60:.1f} min")
used = [edges[(a, b)]["cls"] for a, b in zip(path_d, path_d[1:])]
P(f"  the fastest route uses highway on {used.count('highway')} segments, avenues on {used.count('avenue')}, local streets on {used.count('local')}")

# =============================================================== 3. TRAFFIC
centre = np.array([xs[N // 2], xs[N // 2]])


def congestion(day_rng, incident=True):
    """True rush-hour speed factor per segment (1 = free flow): downtown slows, the highway jams, one crash."""
    f = {}
    for (a, b), d in edges.items():
        if (b, a) in f:
            f[(a, b)] = f[(b, a)]
            continue
        m = (np.array(pos[a]) + np.array(pos[b])) / 2
        downtown = np.exp(-np.sum((m - centre) ** 2) / (2 * 1100 ** 2))
        base = 1 - 0.55 * downtown
        if d["cls"] == "highway":
            base *= 0.55 if m[0] < xs[18] else 0.95          # the inbound highway jams
        base *= day_rng.lognormal(0, 0.12)
        f[(a, b)] = float(np.clip(base, 0.08, 1.0))
    if incident:                                             # a crash on the avenue at column 10
        for (a, b) in edges:
            if a[1] == b[1] == 10 and 12 <= a[0] <= 16 and 12 <= b[0] <= 16:
                f[(a, b)] = 0.12
    return f


today = congestion(np.random.default_rng(99))
true_speed = {e: edges[e]["free"] * today[e] for e in edges}


def probe(n_phones, r):
    """n phones drive random trips; each segment driven gives a measured speed (driver-to-driver spread 15%)."""
    samples = {}
    nodes = list(pos)
    for _ in range(n_phones):
        a, b = nodes[r.integers(len(nodes))], nodes[r.integers(len(nodes))]
        if a == b:
            continue
        p, _, _ = shortest(a, b, hist_speed, astar=True)     # drivers plan by usual traffic; they don't know about the crash
        for e in zip(p, p[1:]):
            samples.setdefault(e, []).append(true_speed[e] * r.lognormal(0, 0.15))
    return samples


def estimate(samples, fallback, min_n=3):
    est, used_live = {}, 0
    for e in edges:
        s = samples.get(e, [])
        if len(s) >= min_n:
            est[e] = float(np.median(s))
            used_live += 1
        else:
            est[e] = fallback[e]
    return est, used_live / len(edges)


def level(f):
    return 2 if f < 0.4 else 1 if f < 0.75 else 0          # 0 green, 1 orange, 2 red


history_days = [congestion(np.random.default_rng(1000 + d), incident=False) for d in range(20)]
hist_speed = {e: edges[e]["free"] * float(np.mean([h[e] for h in history_days])) for e in edges}
P("")
P("3. LIVE TRAFFIC (rush hour: downtown slow, inbound highway jammed, a crash on one avenue)")
traffic_rows = []
for n in (0, 100, 500, 2000, 8000):
    est, cov = estimate(probe(n, np.random.default_rng(n)) if n else {}, hist_speed)
    err = np.median([abs(est[e] - true_speed[e]) / true_speed[e] for e in edges])
    acc = np.mean([level(est[e] / edges[e]["free"]) == level(today[e]) for e in edges])
    crash = [e for e in edges if today[e] == 0.12]
    crash_seen = np.mean([level(est[e] / edges[e]["free"]) == 2 for e in crash])
    traffic_rows.append(dict(phones=n, live_cover=round(cov, 3), med_err=round(float(err), 3), colour_right=round(float(acc), 3),
                             crash_red=round(float(crash_seen), 3)))
    P(f"  {n:5d} phones: {cov * 100:4.1f}% of roads have live data; speed error median {err * 100:4.1f}%; "
      f"colour right on {acc * 100:4.1f}% of roads; crash shown red on {crash_seen * 100:3.0f}% of its segments")
est_live, _ = estimate(probe(2000, np.random.default_rng(2000)), hist_speed)
est_500, _ = estimate(probe(500, np.random.default_rng(500)), hist_speed)
crash_edges = [f"{a[0]},{a[1]}|{b[0]},{b[1]}" for (a, b) in edges if a < b and today[(a, b)] == 0.12]

# =============================================================== 4. ARRIVAL TIME
def route_time(p, speed):
    return sum(travel_time(e, speed[e]) for e in zip(p, p[1:]))


trip_r = np.random.default_rng(5)
nodes = list(pos)
blend = {e: 0.7 * est_live[e] + 0.3 * hist_speed[e] for e in edges}
errs = {k: [] for k in ("limits", "history", "live", "both")}
eta_example = None
for _ in range(300):
    a, b = nodes[trip_r.integers(len(nodes))], nodes[trip_r.integers(len(nodes))]
    if np.hypot(pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]) < 1500:
        continue
    p, _, _ = shortest(a, b, blend, astar=True)              # the route the app would pick
    truth = route_time(p, true_speed) * trip_r.lognormal(0, 0.05)   # plus lights and luck
    for k, sp in (("limits", free_speed), ("history", hist_speed), ("live", est_live), ("both", blend)):
        errs[k].append(abs(route_time(p, sp) - truth) / truth)
    if eta_example is None and len(p) > 30 and route_time(p, free_speed) < 0.8 * truth:
        eta_example = dict(path=[f"{i},{j}" for i, j in p], actual=round(truth / 60, 2),
                           limits=round(route_time(p, free_speed) / 60, 2), both=round(route_time(p, blend) / 60, 2),
                           history=round(route_time(p, hist_speed) / 60, 2))
P("")
P(f"4. ARRIVAL TIME ({len(errs['both'])} rush-hour trips over 1.5 km; error = |predicted - actual| / actual)")
eta_rows = {}
P(f"  example trip ({len(eta_example['path']) - 1} segments): actual {eta_example['actual']} min; speed limits said "
  f"{eta_example['limits']}, history {eta_example['history']}, history + live {eta_example['both']}")
for k, lab in (("limits", "speed limits only"), ("history", "history (20 past days)"), ("live", "live phones (2,000)"), ("both", "history + live")):
    e = np.array(errs[k])
    eta_rows[k] = dict(median=round(float(np.median(e)), 4), within10=round(float(np.mean(e < 0.10)), 4))
    P(f"  {lab:24s}: median error {np.median(e) * 100:5.1f}%, within 10% on {np.mean(e < 0.10) * 100:5.1f}% of trips")

# =============================================================== 5. HOW BUSY
HOURS = np.arange(6, 23)
cafe_rate = 6 + 38 * np.exp(-((HOURS - 12.5) ** 2) / 2.2) + 26 * np.exp(-((HOURS - 18.5) ** 2) / 3.0)   # visitors per hour
OPT_IN, WEEKS, EPS = 0.25, 8, 1.0
br = np.random.default_rng(7)
true_week = np.array([br.poisson(cafe_rate) for _ in range(WEEKS)])            # every visitor, 8 Fridays
counted = br.binomial(true_week, OPT_IN)                                         # only opted-in phones
noisy = counted.sum(0) + br.laplace(0, 1 / EPS, len(HOURS))                     # privacy noise on the totals
bars_true = true_week.mean(0) / true_week.mean(0).max()
bars_est = np.clip(noisy, 0, None) / np.clip(noisy, 0, None).max()
corr = float(np.corrcoef(bars_true, bars_est)[0, 1])
peak_true, peak_est = int(HOURS[np.argmax(bars_true)]), int(HOURS[np.argmax(bars_est)])
shop_rate = 0.6 + 0.8 * np.exp(-((HOURS - 15) ** 2) / 6)
shop_counted = br.binomial(np.array([br.poisson(shop_rate) for _ in range(WEEKS)]), OPT_IN).sum()
P("")
P(f"5. HOW BUSY (a cafe, {WEEKS} Fridays; {OPT_IN * 100:.0f}% of visitors' phones counted; Laplace noise, epsilon {EPS})")
P(f"  real visitors {int(true_week.sum()):,}; counted {int(counted.sum()):,}")
P(f"  popular-times bars vs the real crowd: correlation {corr:.3f}; busiest hour {peak_est}:00 (real {peak_true}:00)")
P(f"  a quiet shop: {int(shop_counted)} counted visits in {WEEKS} weeks; with a 100-visit minimum it shows no chart")
SCENE["busy"] = dict(hours=HOURS.tolist(), true=[round(float(v), 3) for v in bars_true], est=[round(float(v), 3) for v in bars_est],
                     corr=round(corr, 3), peak_true=peak_true, peak_est=peak_est, opt_in=OPT_IN, weeks=WEEKS,
                     visitors=int(true_week.sum()), counted=int(counted.sum()), shop_counted=int(shop_counted))

# =============================================================== 6. HOW CROWDED
TRIPS = np.arange(6.0, 22.0, 0.5)
SEATS, CAP = 40, 70
load_mean = 12 + 52 * np.exp(-((TRIPS - 8.25) ** 2) / 0.9) + 46 * np.exp(-((TRIPS - 17.75) ** 2) / 1.3)


def crowd(load):
    return 0 if load < 0.6 * SEATS else 1 if load <= SEATS else 2     # many seats / few seats / standing


tr = np.random.default_rng(8)
days = 30
REPORT_P = 0.03
reports = []
for d in range(days):
    loads = np.clip(tr.normal(load_mean, 0.12 * load_mean + 3), 0, CAP)
    for k, L in enumerate(loads):
        for _ in range(tr.binomial(int(L), REPORT_P)):
            reports.append((k, crowd(L)))
pred = []
for k in range(len(TRIPS)):
    r_k = [c for kk, c in reports if kk == k]
    pred.append(int(np.bincount(r_k, minlength=3).argmax()) if len(r_k) >= 3 else -1)
test_loads = np.clip(tr.normal(load_mean, 0.12 * load_mean + 3), 0, CAP)
truth_lv = [crowd(L) for L in test_loads]
have = [k for k in range(len(TRIPS)) if pred[k] >= 0]
acc_c = float(np.mean([pred[k] == truth_lv[k] for k in have]))
P("")
P(f"6. HOW CROWDED (one bus route, {len(TRIPS)} trips a day, {SEATS} seats; {REPORT_P * 100:.0f}% of riders answer; {days} days of answers)")
P(f"  {len(reports):,} answers; a prediction for {len(have)} of {len(TRIPS)} trips (3+ answers needed)")
P(f"  predicted level matches the next day's real crowding on {acc_c * 100:.1f}% of trips")
miss = [(float(TRIPS[k]), pred[k], truth_lv[k]) for k in have if pred[k] != truth_lv[k]]
P(f"  misses: " + ", ".join(f"{int(t)}:{int(round((t % 1) * 60)):02d} said {['seats', 'few seats', 'standing'][p]}, was {['seats', 'few seats', 'standing'][q]}" for t, p, q in miss[:4]))
SCENE["bus"] = dict(trips=TRIPS.tolist(), pred=pred, truth=truth_lv, load=[round(float(v), 1) for v in test_loads],
                    seats=SEATS, cap=CAP, acc=round(acc_c, 3), reports=len(reports), report_p=REPORT_P)

# =============================================================== write
SCENE["city"] = dict(n=N, nodes={f"{i},{j}": [round(pos[(i, j)][0]), round(pos[(i, j)][1])] for (i, j) in pos},
                     # per segment: from, to, class, true level, history-only level, 500-phone level, 2000-phone level
                     edges=[[f"{a[0]},{a[1]}", f"{b[0]},{b[1]}", edges[(a, b)]["cls"], level(today[(a, b)]),
                             level(hist_speed[(a, b)] / edges[(a, b)]["free"]), level(est_500[(a, b)] / edges[(a, b)]["free"]),
                             level(est_live[(a, b)] / edges[(a, b)]["free"])] for (a, b) in edges if a < b],
                     crash=crash_edges, eta_example=eta_example,
                     src=f"{SRC[0]},{SRC[1]}", dst=f"{DST[0]},{DST[1]}",
                     route=[f"{i},{j}" for i, j in path_d], dijkstra=[f"{i},{j}" for i, j in order_d],
                     astar=[f"{i},{j}" for i, j in order_a], route_min=round(t_d / 60, 1))
res = dict(gps={k: v for k, v in SCENE["gps"].items() if k != "sats"},
           route=dict(dijkstra=len(order_d), astar=len(order_a), nodes=len(pos), same=path_a == path_d, minutes=round(t_d / 60, 2),
                      km=round(straight / 1000, 2)),
           traffic=traffic_rows, eta=eta_rows,
           busy={k: v for k, v in SCENE["busy"].items() if k not in ("hours", "true", "est")},
           bus={k: v for k, v in SCENE["bus"].items() if k not in ("trips", "pred", "truth", "load")})
(EV / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
(EV / "scene.json").write_text(json.dumps(SCENE), encoding="utf-8")
(EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
P("")
P("wrote evidence/run.log, results.json, scene.json")
