"""gps_demo.py — the real calculation behind "How GPS Knows Where You Are".

Places a receiver on Boston Common and four satellites at GPS orbital radius
(26,560 km from Earth's centre, i.e. ~20,200 km up), each above the horizon.
Computes the signal travel times, then gives the receiver a clock that is off
by 1 microsecond (a cheap phone clock). Solves for position two ways:
  A) ignoring the clock error (position only, least squares on 4 ranges)
  B) solving for the clock error as a 4th unknown (what real GPS does)
and reports how far each answer lands from the truth. Writes demo/gps_output.json.

The satellite geometry is illustrative (chosen positions, not a live almanac);
the physics and the solver are real.   Run:  python demo/gps_demo.py
"""
import json
from pathlib import Path

import numpy as np

C = 299_792_458.0                      # speed of light, m/s
RE = 6_371_000.0                       # mean Earth radius, m
R_ORBIT = 26_560_000.0                 # GPS orbital radius, m
HERE = Path(__file__).resolve().parent


def ecef(lat, lon, r):
    la, lo = np.radians(lat), np.radians(lon)
    return r * np.array([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)])


truth = ecef(42.355, -71.066, RE)     # Boston Common (spherical Earth)
sats = np.array([ecef(70, -60, R_ORBIT), ecef(25, -40, R_ORBIT), ecef(30, -105, R_ORBIT), ecef(5, -75, R_ORBIT)])
up = truth / np.linalg.norm(truth)
elev = [float(np.degrees(np.arcsin(np.dot((s - truth) / np.linalg.norm(s - truth), up)))) for s in sats]
assert all(e > 10 for e in elev), elev

ranges = np.linalg.norm(sats - truth, axis=1)
travel = ranges / C
BIAS = 1e-6                            # receiver clock off by one microsecond
pseudo = ranges + C * BIAS             # what the phone "measures"


def solve(n_unknowns):
    x = np.zeros(4)                    # start at Earth's centre, clock 0
    for _ in range(20):
        d = np.linalg.norm(sats - x[:3], axis=1)
        model = d + (x[3] if n_unknowns == 4 else 0)
        J = np.hstack([(x[:3] - sats) / d[:, None], np.ones((4, 1))])[:, :n_unknowns]
        dx, *_ = np.linalg.lstsq(J, pseudo - model, rcond=None)
        x[:n_unknowns] += dx
    return x


a, b = solve(3), solve(4)
out = {
    "receiver": "Boston Common, 42.355 N 71.066 W (spherical Earth)",
    "orbit_altitude_km": round((R_ORBIT - RE) / 1000),
    "satellite_elevation_deg": [round(e, 1) for e in elev],
    "range_km": [round(r / 1000) for r in ranges],
    "travel_ms": [round(t * 1000, 2) for t in travel],
    "clock_error_us": BIAS * 1e6,
    "clock_error_m": round(C * BIAS, 1),
    "ignore_clock_error_m": round(float(np.linalg.norm(a[:3] - truth)), 1),
    "solve_clock_error_m": float(f"{np.linalg.norm(b[:3] - truth):.2e}"),
    "solved_clock_us": round(b[3] / C * 1e6, 6),
    "relativity_us_per_day": 38, "relativity_drift_km_per_day": round(38e-6 * C / 1000, 1),
}
(HERE / "gps_output.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
