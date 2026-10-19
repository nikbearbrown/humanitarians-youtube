#!/usr/bin/env python3
"""Compute every plate for Ep. 13 — *The Signal We Imagined.*

NOTHING HERE IS A DRAWING OF A RESULT. Each plate runs the real search:
dynamic spectra with terrestrial interference, a narrowband signal injected
under one of three hypotheses, and the actual de-Doppler statistic a radio
technosignature pipeline computes. The central claim is ASSERTED and the
script writes nothing if it fails.

  waterfall.png   what the data is: interference standing vertical at zero
                  drift, one injected signal leaning across it.

  three.png       the same field under three hypotheses about what a
                  transmitter does. All three are things a transmitter can
                  do; only the first is what searches assume.

  recall.png      recall for each hypothesis under a search that excludes
                  zero drift and one that includes it.
                  ASSERTS claim 1 — the drift-corrected signal is found
                  NEVER by the first search and ALWAYS by the second.

  edge.png        the control: recall of the drift-corrected signal against
                  the search's lower drift limit.
                  ASSERTS claim 2 — the blind spot is caused by that one
                  number, and appears exactly where it crosses zero.

  compare.png     the payoff: morphology recall against cadence recall,
                  for each hypothesis.
                  ASSERTS claim 3 — the cadence test recovers the signal
                  that the morphology search scores ZERO on, because it
                  tests where a signal comes from rather than what it looks
                  like.

  A FOURTH PLATE WAS CUT. An earlier version measured how many other things
  in the field share the candidate's drift rate, to argue that zero drift is
  too crowded to search. The measurement does not support it: the median is
  6 look-alikes for a drifting candidate and 5 for a stationary one -- no
  difference. The real flood of zero-drift interference is a property of
  actual spectrum occupancy, which four simulated lines do not reproduce,
  and raising the line count until the claim came true would be tuning the
  experiment to the conclusion. `seti.lookalikes` is still there and still
  runs; it is simply not claimed. BLC1's look-alike argument stays in the
  reel as a PUBLISHED result (Sheikh et al. 2021), not a measured one.

  cadence.png     the other test: three ON scans and three OFF scans. A
                  source on the sky appears only in the ONs.

Deterministic: one seed, 1313, logged in SOURCES.md.

Run:  python assets/gen_seti.py           (numpy + Pillow)
      python assets/gen_seti.py --force   (ignore the cache and recompute)
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
import seti as S

HERE = Path(__file__).resolve().parent
OUT = HERE / "plots"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = HERE / ".cache_seti.npz"

SEED = 1313
N = 80
SNR = 1.6

CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)
ACCT = (164, 74, 50)
WHITE = (255, 255, 255)

HYP = {
    "assumed": dict(dr=(0.60, 2.00), duty=None),
    "corrected": dict(dr=(0.0, 0.0), duty=None),
    "pulsed": dict(dr=(0.60, 2.00), duty=0.45),
}
SEARCH = {"excl": (0.30, 2.40), "incl": (0.0, 2.40)}


def draw(rng, hyp):
    """Drift is drawn POSITIVE by convention; real searches cover both signs
    and the symmetry buys nothing here except unreadable plates."""
    lo, hi = hyp["dr"]
    return (float(rng.uniform(lo, hi)) if hi > 0 else 0.0,
            float(rng.uniform(80, S.NF - 80)))


def field(rng, hyp=None, d=None, f0=None, signal=True, rfi=True):
    wf = S.blank(rng)
    if rfi:
        S.add_rfi(wf, rng)
    if signal:
        S.add_track(wf, f0, d, SNR, duty=hyp["duty"], rng=rng)
    return wf


def run():
    if CACHE.exists() and "--force" not in sys.argv:
        print("[gen_seti] using cache (pass --force to recompute)")
        return np.load(CACHE, allow_pickle=True)["payload"].item()

    # The threshold is set by the NOISE. Calibrating it on fields that
    # contain interference makes it track the brightest interference line,
    # and then nothing can exceed it -- the interference is not meant to be
    # under the threshold, it is meant to be the pile of hits a human sifts.
    rng = np.random.default_rng(SEED + 7)
    peaks = [S.dedoppler_map(field(rng, signal=False, rfi=False),
                             *SEARCH["incl"])[1].max() for _ in range(40)]
    th = float(np.percentile(peaks, 95))
    print("[gen_seti] threshold %.2f  (noise-only map max, 95th pct)" % th)

    recall, looks = {}, {}
    for hname, hyp in HYP.items():
        for sname, (lo, hi) in SEARCH.items():
            r = np.random.default_rng(SEED + 99)
            hits = 0
            for _ in range(N):
                d, f0 = draw(r, hyp)
                hits += S.detected(field(r, hyp, d, f0), f0, d, lo, hi, th)
            recall[(hname, sname)] = hits / N
    # look-alikes
    for hname, hyp in HYP.items():
        r = np.random.default_rng(SEED + 555)
        c = []
        for _ in range(40):
            d, f0 = draw(r, hyp)
            c.append(S.lookalikes(field(r, hyp, d, f0), d,
                                  *SEARCH["incl"], th))
        looks[hname] = c
        print("  look-alikes %-10s median %4.1f" % (hname, np.median(c)))

    # the control: where does the blind spot begin?
    edges = np.linspace(0.0, 0.48, 9)
    edge = []
    for e in edges:
        r = np.random.default_rng(SEED + 99)
        hits = 0
        for _ in range(40):
            d, f0 = draw(r, HYP["corrected"])
            hits += S.detected(field(r, HYP["corrected"], d, f0), f0, d,
                               e, 0.70, th)
        edge.append(hits / 40)
    print("  edge sweep:", " ".join("%.2f" % v for v in edge))

    # the cadence test
    lo, hi = SEARCH["incl"]

    def peak(w, d, f0):
        drifts, m = S.dedoppler_map(w, lo, hi)
        near = np.abs(drifts - d) <= 0.06
        if not near.any():
            return -np.inf
        a, b = int(f0 - 3), int(f0 + 4)
        return float(m[near, max(a, 0):min(b, S.NF)].max())

    r = np.random.default_rng(SEED + 31)
    null = []
    for _ in range(40):
        d, f0 = draw(r, HYP["corrected"])
        ons = [field(r, HYP["corrected"], d, f0) for _ in range(3)]
        offs = [field(r, HYP["corrected"], d, f0) for _ in range(3)]
        null.append(min(peak(w, d, f0) for w in ons)
                    - max(peak(w, d, f0) for w in offs))
    margin = float(np.percentile(null, 95))
    cad = {}
    for hname, hyp in HYP.items():
        r = np.random.default_rng(SEED + 77)
        hits = 0
        for _ in range(50):
            d, f0 = draw(r, hyp)
            ons = [field(r, hyp, d, f0) for _ in range(3)]
            offs = [field(r, hyp, d, f0, signal=False) for _ in range(3)]
            hits += (min(peak(w, d, f0) for w in ons)
                     - max(peak(w, d, f0) for w in offs)) > margin
        cad[hname] = hits / 50
        print("  cadence %-10s recall %.2f" % (hname, cad[hname]))

    # one sample field per hypothesis, for the pictures
    samples = {}
    for hname, hyp in HYP.items():
        r = np.random.default_rng(SEED + 4)
        d, f0 = draw(r, hyp)
        if hname == "corrected":
            f0 = 300.0
        if hname in ("assumed", "pulsed"):
            f0 = 170.0
        samples[hname] = (field(r, hyp, d, f0), d, f0)
    r = np.random.default_rng(SEED + 12)
    d, f0 = draw(r, HYP["assumed"])
    cad_scans = ([field(r, HYP["assumed"], d, f0) for _ in range(3)],
                 [field(r, HYP["assumed"], d, f0, signal=False)
                  for _ in range(3)])

    payload = dict(th=th, recall=recall, looks=looks, edges=edges,
                   edge=edge, cad=cad, margin=margin, samples=samples,
                   cad_scans=cad_scans)
    np.savez_compressed(CACHE, payload=np.array(payload, dtype=object))
    return payload


# ═════════════════════════════════════════════════════════════════════════════
#  drawing — plates carry IMAGERY ONLY; every label lives in scenes.py
# ═════════════════════════════════════════════════════════════════════════════
def spectro(wf, w=520, h=360, vmax=None):
    """A dynamic spectrum: time down, frequency across, ink on cream."""
    v = np.clip(wf, 0, None)
    v = v / (vmax or np.percentile(v, 99.0) or 1.0)
    # Gamma 2.80, not 0.75. At 0.75 the mid-grey noise was LIFTED toward
    # ink, the frame became a uniform texture, and GATE V measured an
    # ink/background luminance separation of 0.22-0.25 against a 0.30 floor
    # -- correctly: the structure that matters was no more contrasty than
    # the noise around it. Pushing the mids back toward cream leaves the
    # interference lines and the injected track dark and everything else
    # pale, which is both legible and what the beat is about.
    v = np.clip(v, 0, 1) ** 2.80
    bg, fg = np.array(CREAM, float), np.array(INK, float)
    rgb = bg[None, None, :] + (fg - bg)[None, None, :] * v[:, :, None]
    img = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
    img = img.resize((w, h), Image.LANCZOS)
    ImageDraw.Draw(img).rectangle([0, 0, w - 1, h - 1], outline=GHOST, width=2)
    return img


def mark_track(img, f0, drift, colour=ACC, w=520, h=360, pad=7):
    """Ring the injected signal where it actually is."""
    d = ImageDraw.Draw(img)
    sx, sy = w / float(S.NF), h / float(S.NT)
    pts = [((f0 + drift * t) * sx, (t + 0.5) * sy) for t in range(S.NT)]
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        d.line([x0 - pad, y0, x1 - pad, y1], fill=colour, width=2)
        d.line([x0 + pad, y0, x1 + pad, y1], fill=colour, width=2)
    return img


def row(panels, gap=26, bg=CREAM):
    hh = max(p.height for p in panels)
    ww = sum(p.width for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (ww, hh), bg)
    x = 0
    for p in panels:
        sheet.paste(p, (x, (hh - p.height) // 2))
        x += p.width + gap
    return sheet


def col(panels, gap=22, bg=CREAM):
    ww = max(p.width for p in panels)
    hh = sum(p.height for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (ww, hh), bg)
    y = 0
    for p in panels:
        sheet.paste(p, ((ww - p.width) // 2, y))
        y += p.height + gap
    return sheet


class Axes:
    def __init__(self, w, h, xlim, ylim, m=(18, 18, 18, 18)):
        self.img = Image.new("RGB", (w, h), CREAM)
        self.d = ImageDraw.Draw(self.img)
        self.xlim, self.ylim = xlim, ylim
        l, r, t, b = m
        self.bx = (l, t, w - r, h - b)
        self.d.rectangle(self.bx, outline=GHOST, width=2)

    def X(self, x):
        l, _, r, _ = self.bx
        a, b = self.xlim
        return l + (r - l) * (x - a) / float(b - a)

    def Y(self, y):
        _, t, _, b = self.bx
        a, c = self.ylim
        return b - (b - t) * (y - a) / float(c - a)

    def grid(self, ys):
        l, _, r, _ = self.bx
        for y in ys:
            yy = self.Y(y)
            self.d.line([l + 2, yy, r - 2, yy], fill=(214, 210, 196), width=1)

    def bar(self, x, y, w, colour, y0=0.0):
        """A zero-height bar still has to be visible AS a zero, or the beat
        reads as a missing bar rather than a measured nothing."""
        top, base = self.Y(y), self.Y(y0)
        if abs(top - base) < 5:
            self.d.rectangle([self.X(x - w), base - 5, self.X(x + w), base],
                             fill=colour)
        else:
            self.d.rectangle([self.X(x - w), top, self.X(x + w), base],
                             fill=colour)

    def poly(self, xs, ys, colour, width=7, rr=9):
        pts = [(self.X(a), self.Y(b)) for a, b in zip(xs, ys)]
        self.d.line(pts, fill=colour, width=width, joint="curve")
        for px, py in pts:
            self.d.ellipse([px - rr, py - rr, px + rr, py + rr], fill=colour)


def waterfall_plate(p):
    wf, d, f0 = p["samples"]["assumed"]
    img = spectro(wf, 1500, 700)
    return mark_track(img, f0, d, w=1500, h=700, pad=16)


def three_plate(p):
    panels = []
    for k in ("assumed", "corrected", "pulsed"):
        wf, d, f0 = p["samples"][k]
        img = spectro(wf, 500, 420)
        panels.append(mark_track(img, f0, d, w=500, h=420, pad=9))
    return row(panels, gap=26)


def three_v_plate(p):
    """Stacked, for portrait: side by side at 3.44 units each panel is 1.1
    units across and the drift of the marked track stops being readable."""
    panels = []
    for k in ("assumed", "corrected", "pulsed"):
        wf, d, f0 = p["samples"][k]
        img = spectro(wf, 760, 300)
        panels.append(mark_track(img, f0, d, w=760, h=300, pad=11))
    return col(panels, gap=20)


def recall_plate(p):
    ax = Axes(1560, 780, (0.0, 3.2), (0.0, 1.08))
    ax.grid([0.25, 0.5, 0.75, 1.0])
    for i, k in enumerate(("assumed", "corrected", "pulsed")):
        ax.bar(0.62 + i * 1.0 - 0.17, p["recall"][(k, "excl")], 0.15, INK)
        ax.bar(0.62 + i * 1.0 + 0.17, p["recall"][(k, "incl")], 0.15, ACC)
    return ax.img


def edge_plate(p):
    ax = Axes(1560, 780, (-0.035, 0.515), (-0.06, 1.08))
    ax.grid([0.5, 1.0])
    ax.poly(p["edges"], p["edge"], ACCT)
    return ax.img


def compare_plate(p):
    """Ink = the morphology search (excluding zero drift).
    Terracotta = the cadence test. Same signals, same fields."""
    ax = Axes(1560, 780, (0.0, 3.2), (0.0, 1.08))
    ax.grid([0.25, 0.5, 0.75, 1.0])
    for i, k in enumerate(("assumed", "corrected", "pulsed")):
        ax.bar(0.62 + i * 1.0 - 0.17, p["recall"][(k, "excl")], 0.15, INK)
        ax.bar(0.62 + i * 1.0 + 0.17, p["cad"][k], 0.15, ACC)
    return ax.img


def _trace(wf, d, f0, w=560, h=150, span=60):
    """One de-Doppler trace at the candidate's drift rate.

    The raw waterfall cannot show this: a signal at the detection limit is
    invisible per pixel, which is the whole reason a search integrates. So
    the cadence plate shows what the TEST actually compares -- the
    integrated spectrum at the candidate's own drift rate -- where a real
    signal is a peak and its absence is flat.
    """
    drifts, m = S.dedoppler_map(wf, 0.0, 2.40)
    near = np.abs(drifts - d) <= 0.06
    prof = m[near].max(axis=0) if near.any() else m.max(axis=0)
    a, b = int(f0 - span), int(f0 + span)
    seg = prof[max(a, 0):min(b, S.NF)]
    img = Image.new("RGB", (w, h), CREAM)
    dr = ImageDraw.Draw(img)
    lo, hi = -1.0, 8.0
    base = h - 10
    dr.line([6, base, w - 6, base], fill=GHOST, width=2)
    pts = []
    for i, v in enumerate(seg):
        x = 6 + (w - 12) * i / max(len(seg) - 1, 1)
        y = base - (base - 12) * (v - lo) / (hi - lo)
        pts.append((x, max(min(y, base), 6)))
    dr.line(pts, fill=INK, width=3, joint="curve")
    dr.rectangle([0, 0, w - 1, h - 1], outline=GHOST, width=2)
    return img


def cadence_plate(p):
    ons, offs = p["cad_scans"]
    r = np.random.default_rng(SEED + 12)
    d, f0 = draw(r, HYP["assumed"])
    left = col([_trace(w, d, f0) for w in ons], gap=14)
    right = col([_trace(w, d, f0) for w in offs], gap=14)
    return row([left, right], gap=30)


def selfcheck(p):
    r = p["recall"]
    print("\n[gen_seti] === the three claims ===")
    print("  %-12s %14s %14s" % ("hypothesis", "excludes zero", "includes zero"))
    for k in ("assumed", "corrected", "pulsed"):
        print("  %-12s %14.2f %14.2f" % (k, r[(k, "excl")], r[(k, "incl")]))
    print("  1. the drift-corrected signal: %.2f  ->  %.2f"
          % (r[("corrected", "excl")], r[("corrected", "incl")]))
    print("  2. the blind spot appears at the search edge: %s"
          % " ".join("%.2f" % v for v in p["edge"]))
    print("  3. cadence recall: " + "  ".join(
        "%s %.2f" % (k, p["cad"][k]) for k in HYP))
    print("     (look-alikes measured and NOT claimed: " + "  ".join(
        "%s %.0f" % (k, np.median(p["looks"][k])) for k in HYP) + ")")

    fails = []
    if not (r[("corrected", "excl")] <= 0.02 and r[("corrected", "incl")] >= 0.95):
        fails.append("claim 1: the drift-corrected signal is not a clean "
                     "blind spot (%.2f -> %.2f)"
                     % (r[("corrected", "excl")], r[("corrected", "incl")]))
    if not (r[("assumed", "excl")] >= 0.90):
        fails.append("claim 1: the ASSUMED signal is not reliably found "
                     "(%.2f) -- the comparison means nothing if the search "
                     "does not work on its own hypothesis"
                     % r[("assumed", "excl")])
    if not (p["edge"][0] >= 0.95 and p["edge"][-1] <= 0.05):
        fails.append("claim 2: recall does not fall across the swept edge "
                     "(%.2f -> %.2f)" % (p["edge"][0], p["edge"][-1]))
    if not (p["cad"]["corrected"] >= 0.60
            and r[("corrected", "excl")] <= 0.02):
        fails.append("claim 3: the cadence test does not recover the signal "
                     "the morphology search misses (cadence %.2f against "
                     "morphology %.2f)"
                     % (p["cad"]["corrected"], r[("corrected", "excl")]))
    if not (abs(p["cad"]["assumed"] - p["cad"]["corrected"]) < 0.30):
        fails.append("claim 3: the cadence test is not insensitive to the "
                     "drift hypothesis (%.2f vs %.2f)"
                     % (p["cad"]["assumed"], p["cad"]["corrected"]))
    if fails:
        for m in fails:
            print("  FAIL " + m)
        raise SystemExit("[gen_seti] a central claim does not hold — fix the "
                         "CLAIM, not the tolerance. Nothing written.")
    print("  -> all hold. writing plates.\n")


def main():
    p = run()
    selfcheck(p)
    for name, fn in (("waterfall", waterfall_plate),
                     ("three", three_plate),
                     ("three_v", three_v_plate),
                     ("recall", recall_plate),
                     ("edge", edge_plate),
                     ("compare", compare_plate),
                     ("cadence", cadence_plate)):
        img = fn(p)
        img.save(OUT / ("%s.png" % name))
        print("[gen_seti] %-10s %dx%d  ratio %.3f"
              % (name, img.width, img.height, img.height / img.width))


if __name__ == "__main__":
    main()
