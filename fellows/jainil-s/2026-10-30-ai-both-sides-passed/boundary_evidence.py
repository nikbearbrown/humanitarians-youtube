"""
Primary evidence for "Both Sides Passed".

A two-stage pipeline. The producer validates what it emits. The consumer
validates what it receives. Both sets of checks pass. The data is still wrong,
because nothing compares what the producer MEANT with what the consumer
EXPECTED -- and that comparison is the only place the mismatch exists.

Setup
-----
  5,000 payment events: event_id, ts_ms, amount, currency, status.
  Timestamps follow a realistic daily rhythm (quiet overnight, peak early
  afternoon) because that shape turns out to matter.

  Seven defects, each applied on its own to a known-good batch. All seven are
  ordinary integration failures, not exotic corruption.

Three levels of checking
------------------------
  in-stage   What each side can check about its own data in isolation:
             required fields present, types correct, timestamps positive.
             This is what most pipelines actually have.

  boundary   A contract between the two stages, profiled from a known-good
             run: agreed ranges for the medians, the allowed status values,
             uniqueness of the key, the rate of negative amounts.

  + shape    The boundary contract plus the DISTRIBUTION of events across the
             hour of day, compared by total variation distance.

Every figure spoken or shown in the video comes out of this file.
Run:  python boundary_evidence.py
"""
import numpy as np

RNG = np.random.default_rng(0)
N = 5000
DAY0 = 1_760_000_000_000          # a fixed midnight, in epoch milliseconds

# Hour-of-day weights: quiet overnight, peak early afternoon.
HOUR_W = np.array([.5, .3, .2, .2, .3, .6, 1.2, 2.2, 3.4, 4.3, 5.0, 5.4,
                   5.6, 5.9, 6.0, 5.7, 5.1, 4.4, 3.6, 2.9, 2.2, 1.6, 1.1, .7])
HOUR_W = HOUR_W / HOUR_W.sum()


def good_batch():
    hrs = RNG.choice(24, size=N, p=HOUR_W)
    ts = DAY0 + hrs * 3_600_000 + RNG.integers(0, 3_600_000, N)
    return [{"event_id": int(i),
             "ts_ms": int(ts[i]),
             "amount": round(float(RNG.gamma(2, 18)), 2),
             "currency": "USD",
             "status": str(RNG.choice(["ok", "failed", "refunded"], p=[.8, .15, .05]))}
            for i in range(N)]


DEFECTS = [
    ("timestamps in seconds, not ms", lambda rs: [{**r, "ts_ms": r["ts_ms"] // 1000} for r in rs]),
    ("amount in cents, not dollars",  lambda rs: [{**r, "amount": round(r["amount"] * 100, 2)} for r in rs]),
    ("a new status value appears",    lambda rs: [{**r, "status": "pending_review"} if i % 20 == 0 else r
                                                  for i, r in enumerate(rs)]),
    ("nulls encoded as -1",           lambda rs: [{**r, "amount": -1.0} if i % 25 == 0 else r
                                                  for i, r in enumerate(rs)]),
    ("timezone shift (+5:30)",        lambda rs: [{**r, "ts_ms": r["ts_ms"] + 19_800_000} for r in rs]),
    ("amount arrives as a string",    lambda rs: [{**r, "amount": str(r["amount"])} for r in rs]),
    ("late rows duplicate event_id",  lambda rs: rs + [dict(r) for r in rs[:250]]),
]

FIELDS = ("event_id", "ts_ms", "amount", "currency", "status")


def in_stage_checks(rows):
    """Presence, type and sign — what a stage can verify about itself alone."""
    for r in rows:
        for k in FIELDS:
            if k not in r or r[k] is None:
                return True
        if not isinstance(r["amount"], (float, int, np.floating)):
            return True
        if not isinstance(r["ts_ms"], (int, np.integer)) or r["ts_ms"] <= 0:
            return True
    return False


def hour_profile(ts):
    h = np.bincount((np.asarray(ts, dtype=np.int64) // 3_600_000) % 24, minlength=24)
    return h / h.sum()


def boundary_checks(rows, ref, use_shape):
    amounts = [r["amount"] for r in rows]
    if any(isinstance(a, str) for a in amounts):
        return True, "amount type changed between the stages"
    am = np.array(amounts, dtype=float)
    ts = np.array([r["ts_ms"] for r in rows], dtype=np.int64)

    if not (ref["ts_lo"] <= np.median(ts) <= ref["ts_hi"]):
        return True, "timestamp median outside the agreed range"
    if not (ref["am_lo"] <= np.median(am) <= ref["am_hi"]):
        return True, "amount median outside the agreed range"
    if {r["status"] for r in rows} - ref["domain"]:
        return True, "status outside the agreed domain"
    if (am < 0).mean() > 0.005:
        return True, "negative amounts above the agreed rate"
    if len({r["event_id"] for r in rows}) != len(rows):
        return True, "event_id is no longer unique"
    if use_shape:
        tvd = 0.5 * np.abs(hour_profile(ts) - ref["hours"]).sum()
        if tvd > 0.15:
            return True, f"hour-of-day shape moved (TVD {tvd:.2f})"
    return False, ""


def main():
    print(__doc__.split("Run:")[0].strip())
    base = good_batch()
    ts0 = np.array([r["ts_ms"] for r in base], dtype=np.int64)
    am0 = np.array([r["amount"] for r in base])
    ref = {"ts_lo": np.median(ts0) * 0.999, "ts_hi": np.median(ts0) * 1.001,
           "am_lo": np.median(am0) * 0.5,   "am_hi": np.median(am0) * 2.0,
           "domain": {"ok", "failed", "refunded"}, "hours": hour_profile(ts0)}

    print(f"\n{N} events, 7 defects, each applied on its own to a known-good batch\n")
    print(f"{'defect':<32}{'in-stage':<11}{'boundary':<11}{'+ shape':<9} what the boundary saw")
    a = b = c = 0
    for name, fn in DEFECTS:
        bad = fn([dict(r) for r in base])
        s = in_stage_checks(bad)
        v1, _ = boundary_checks(bad, ref, False)
        v2, why = boundary_checks(bad, ref, True)
        a, b, c = a + s, b + v1, c + v2
        print(f"{name:<32}{'CAUGHT' if s else 'passes':<11}"
              f"{'CAUGHT' if v1 else 'passes':<11}{'CAUGHT' if v2 else 'passes':<9} {why}")

    n = len(DEFECTS)
    print("\n--- the numbers the video uses ---")
    print(f"  caught by each stage checking its own data : {a}/{n}")
    print(f"  caught by a contract at the boundary       : {b}/{n}")
    print(f"  caught once the contract profiles SHAPE    : {c}/{n}")
    print("\n  The only defect in-stage checks catch is the one that changes a TYPE.")
    print("  Every other defect leaves the data individually valid on both sides.")
    print("  The one the plain boundary misses is the timezone shift: 5.5 hours is")
    print("  0.001% of an epoch-millisecond value, far inside any sane range check,")
    print("  but it moves the daily rhythm enough to see.")


if __name__ == "__main__":
    main()
