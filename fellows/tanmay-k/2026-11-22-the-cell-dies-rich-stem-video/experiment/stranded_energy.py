"""How much of a coin cell is left when a device browns out?
Our own simulation of a CR2032-class cell (illustrative model, not a bench measurement).

Cell model: open-circuit voltage Voc(q) and internal resistance R(q), both functions of charge used q (mAh).
A device asks for a burst of I mA; the terminal voltage during the burst is Voc(q) - I*R(q). The first burst
whose terminal voltage is under the reset line is a brownout. We report how much of the cell is unspent then.

Inputs (all "about", read from the manufacturers' published graphs; see FACTCHECK.md rows 1-9):
  Duracell CR2032 225 mAh datasheet: open-circuit 3.0 V.
  Energizer coin handbook p4, 2032 under a 75 ohm pulse (about 30 mA, 0.1 s on / 4.9 s off): resistance and
  open-circuit curves read from the plot; the plotted run ends at about 208 mAh (our reference capacity Q_REF).
Everything below the inputs is our code. Seed 32 is used only for the unit-spread band.
Run: /opt/homebrew/bin/python3.12 stranded_energy.py
"""
import json, numpy as np

Q_REF = 208.0                                   # mAh, end of the Energizer plotted run (about)
V_RESET = 2.0                                   # V, our chosen illustrative reset line
ON_S, PERIOD_S, SLEEP_MA = 0.1, 5.0, 0.005      # burst length, burst period, sleep draw (illustrative)

# graph-read points (q mAh, value), about
R_PTS = [(0, 10), (25, 13), (100, 14), (125, 15.5), (150, 19), (185, 28), (200, 45), (208, 65)]
V_PTS = [(0, 3.00), (25, 2.90), (100, 2.88), (150, 2.82), (185, 2.72), (200, 2.62), (208, 2.55)]

def curve(pts):
    xs, ys = zip(*pts)
    return lambda q: np.interp(q, xs, ys)

R_OF_Q, VOC_OF_Q = curve(R_PTS), curve(V_PTS)

def first_brownout_grid(i_ma, vreset=V_RESET, r_scale=1.0, voc=None, step=0.01):
    voc = voc or VOC_OF_Q
    """Smallest q on a fine grid where Voc - I*R < reset; None if never before Q_REF."""
    q = np.arange(0.0, Q_REF + step, step)
    v = voc(q) - (i_ma / 1000.0) * r_scale * R_OF_Q(q)
    bad = np.nonzero(v < vreset)[0]
    return float(q[bad[0]]) if bad.size else None

def first_brownout_cycles(i_ma, vreset=V_RESET, r_scale=1.0, voc=None):
    voc = voc or VOC_OF_Q
    """Same question answered the long way: step the device burst by burst, spending charge each cycle."""
    q = 0.0
    dq = (i_ma * ON_S + SLEEP_MA * (PERIOD_S - ON_S)) / 3600.0      # mAh used per cycle
    while q <= Q_REF:
        if voc(q) - (i_ma / 1000.0) * r_scale * R_OF_Q(q) < vreset:
            return q
        q += dq
    return None

def energy_share_left(q_fail, voc=None):
    voc = voc or VOC_OF_Q
    """Energy still in the cell at q_fail as a share of the energy of the whole run (integral of Voc dq)."""
    q = np.linspace(0, Q_REF, 20001); e = np.cumsum(voc(q)) * (q[1] - q[0])
    ef = float(np.interp(q_fail, q, e)) if q_fail is not None else e[-1]
    return 1.0 - ef / e[-1]

def row(i_ma, **kw):
    q = first_brownout_grid(i_ma, **kw)
    left_q = 0.0 if q is None else 1 - q / Q_REF       # no brownout before the plotted end: nothing stranded
    return {"burst_mA": i_ma, "q_fail_mAh": q,
            "charge_left_pct": round(100 * left_q, 1),
            "energy_left_pct": round(100 * (energy_share_left(q, kw.get("voc")) if q is not None else 0.0), 1)}

def safe_burst_mA(q, vreset=V_RESET):
    """Largest burst the cell can still pass when q mAh are used: (Voc - reset) / R."""
    return 1000.0 * (VOC_OF_Q(q) - vreset) / R_OF_Q(q)

if __name__ == "__main__":
    rng = np.random.default_rng(32)
    out = {"inputs": {"Q_REF_mAh": Q_REF, "V_RESET": V_RESET, "R_PTS": R_PTS, "V_PTS": V_PTS,
                      "pulse": [ON_S, PERIOD_S, SLEEP_MA]}}
    bursts = [2, 5, 8, 10, 15, 20, 25, 30, 35, 40, 50, 60, 75, 100, 120]
    out["sweep"] = [row(i) for i in bursts]

    # cross-check: the cycle-by-cycle answer against the grid answer (equal work, different method)
    chk = []
    for i in (10, 20, 30, 50, 75):
        a, b = first_brownout_grid(i), first_brownout_cycles(i)
        chk.append({"burst_mA": i, "grid": a, "cycles": b, "diff_mAh": None if a is None or b is None else round(abs(a - b), 3)})
    out["crosscheck"] = chk

    out["safe_burst_vs_used"] = [{"used_mAh": q, "safe_burst_mA": round(float(safe_burst_mA(q)), 1)}
                                 for q in (0, 25, 100, 150, 185, 200, 208)]

    # sensitivity: reset line, flat open-circuit voltage, resistance scale
    sens = {}
    for vr in (1.8, 2.0, 2.2, 2.4):
        sens[f"reset_{vr}"] = [row(i, vreset=vr) for i in (8, 30, 100)]
    flat = curve([(0, 2.87), (150, 2.87), (208, 2.55)])
    sens["voc_flat_2.87"] = [row(i, voc=flat) for i in (8, 30, 100)]
    for s in (0.8, 1.2):
        sens[f"R_x{s}"] = [row(i, r_scale=s) for i in (8, 30, 100)]
    # drain-dependent resistance: Energizer's 3 uA run (inset, p4) rises much earlier and ends near 90 mAh (about)
    keep = (R_OF_Q, VOC_OF_Q, Q_REF)
    R_OF_Q, VOC_OF_Q, Q_REF = curve([(0, 9), (25, 13), (50, 25), (75, 55), (90, 100)]), curve([(0, 3.00), (90, 2.85)]), 90.0
    sens["R_3uA_curve_Qref90"] = [row(i) for i in (8, 30, 60)]
    R_OF_Q, VOC_OF_Q, Q_REF = keep
    out["sensitivity"] = sens

    # unit-to-unit spread (assumption: lognormal sigma 0.15 on the whole resistance curve)
    band = {}
    scales = np.exp(rng.normal(0, 0.15, 400))
    for i in (8, 30, 60):
        left = [100 * (1 - q / Q_REF) if q is not None else 0.0
                for q in (first_brownout_grid(i, r_scale=float(s)) for s in scales)]
        band[str(i)] = {"p10": round(float(np.percentile(left, 10)), 1), "median": round(float(np.median(left)), 1),
                        "p90": round(float(np.percentile(left, 90)), 1)}
    out["unit_spread_left_pct"] = band
    json.dump(out, open("stranded_energy.json", "w"), indent=1)

    print("burst mA | brownout at mAh | charge left % | energy left %")
    for r in out["sweep"]:
        print(f"{r['burst_mA']:>8} | {str(r['q_fail_mAh']):>15} | {r['charge_left_pct']:>13} | {r['energy_left_pct']:>12}")
    print("sensitivity:",json.dumps(sens)[:2000])
    print("cross-check:", chk)
    print("safe burst vs used:", out["safe_burst_vs_used"])
    print("unit spread:", band)
