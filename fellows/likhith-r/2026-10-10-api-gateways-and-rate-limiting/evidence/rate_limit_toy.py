"""Toy rate limiters behind the on-screen outcomes in B05-B08 (claude-hai-api-gateways).

Mirrors the inputs hard-wired as defaults in runtime/remotion/src/ApiGateway.tsx so the
numbers the scenes compute can be checked independently. Pure Python, deterministic.
"""

def fixed_cap(n_requests, limit):
    """B05: n requests inside one 1-second window against a per-second cap."""
    return sum(1 for i in range(n_requests) if i < limit)

def token_bucket(cap, refill_every, burst, flood, horizon=100):
    """B06: refills land before a request at the same instant (same rule as the scene)."""
    ev = [(u, 0, None) for u in range(refill_every, horizon + 1, refill_every)]
    ev += [(u, 1, "burst") for u in burst] + [(u, 1, "flood") for u in flood]
    ev.sort()
    tokens, out = cap, []
    for u, kind, group in ev:
        if kind == 0:
            tokens = min(cap, tokens + 1)
        elif tokens >= 1:
            tokens -= 1; out.append((u, group, True))
        else:
            out.append((u, group, False))
    return out

def fixed_window(hits, limit, window):
    ok = []
    for i, s in enumerate(hits):
        same = [p for p in hits[:i] if p // window == s // window]
        ok.append(len(same) < limit)
    return ok

def sliding_window(hits, limit, window):
    ok = []
    for i, s in enumerate(hits):
        inside = [p for j, p in enumerate(hits[:i]) if ok[j] and p > s - window]
        ok.append(len(inside) < limit)
    return ok

if __name__ == "__main__":
    print("B05 fixed cap: 10 requests, limit 5/s ->", fixed_cap(10, 5), "passed,", 10 - fixed_cap(10, 5), "rejected (429)")
    tb = token_bucket(5, 10, [14, 16, 18, 20], [46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76])
    b = [o for _, g, o in tb if g == "burst"]; f = [o for _, g, o in tb if g == "flood"]
    print("B06 token bucket (cap 5, +1 per tick): burst", "".join("✓" if o else "✕" for o in b),
          "| flood", "".join("✓" if o else "✕" for o in f),
          f"| passed {sum(b) + sum(f)}, rejected {len(b) + len(f) - sum(b) - sum(f)}")
    hits = list(range(55, 65))
    fw, sw = fixed_window(hits, 5, 60), sliding_window(hits, 5, 60)
    print("B07 hits at 0:55-1:04, limit 5/min: fixed passes", sum(fw), "| sliding passes", sum(sw),
          "| sliding rejects", [f"{h // 60}:{h % 60:02d}" for h, o in zip(hits, sw) if not o])
    greedy = ["A", "A", "B", "A", "C"] + ["A"] * 19
    fair = [["A", "B", "C"][i % 3] for i in range(24)]
    cnt = lambda seq: {u: seq.count(u) for u in "ABC"}
    print("B08 24 shared slots: no limits", cnt(greedy), "| per-user", cnt(fair))
