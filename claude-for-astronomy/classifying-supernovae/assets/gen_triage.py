#!/usr/bin/env python3
"""Compute every plate for Ep. 10 — *What We Chased Before.*

NOTHING HERE IS A DRAWING OF A RESULT. The centrepiece is a real closed-loop
experiment, run many times and averaged, and its central claim is ASSERTED. If
the assertion fails the script writes nothing.

  selection.png    the PUBLISHED selection function: what fraction of
                   transients get a spectrum, by brightness. A ledger, not a
                   computation, and labelled as such on screen.

  deadline.png     computed Bazin light curves for three transient types, with
                   the window in which a spectrum is still informative marked.
                   This is why the decision cannot wait.

  loop.png         THE CENTREPIECE. Twelve seasons of a closed loop: train on
                   what has been labelled, spend a fixed spectroscopic budget,
                   add those labels, retrain. Three strategies. Two panels:
                   overall accuracy, and recall on the rare class.
                   ASSERTS: under the greedy strategy overall accuracy RISES
                   while rare-class recall STAYS NEAR ZERO, and uncertainty
                   sampling ends with at least three times that recall and at
                   least 0.40 in absolute terms.

                   Note the direction of the finding. Rare-class recall does
                   not collapse -- it begins at zero, because a brightness-
                   biased seed set contains no rare objects, and it never
                   leaves. The loop does not create the blind spot; it
                   inherits it and then preserves it.

  composition.png  what the labelled set is made of, season by season, under
                   each strategy. The loop is visible directly.

  boundary.png     the feature space: the population, the labelled seed, and
                   where each strategy spends its next twenty spectra.

  budget.png       the honest trade-off: exploration fraction against rare-class
                   recall AND against confirmed-Ia count. Exploration is not
                   free, and the plate says so.

Run:  python assets/gen_triage.py    (numpy + Pillow only; no network, no keys)

Deterministic: one seed, 1017, logged in SOURCES.md.
"""
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

SEED = 1017
OUT = Path(__file__).resolve().parent / "plots"
OUT.mkdir(parents=True, exist_ok=True)

# ── the Claude fidelity palette ──────────────────────────────────────────────
CREAM = (242, 240, 233)
INK = (61, 57, 41)
SOFT = (110, 106, 87)
GHOST = (185, 180, 160)
ACC = (217, 119, 87)          # terracotta — marks THE LOOP / what the choice costs
ACCT = (164, 74, 50)
WHITE = (255, 255, 255)

# ── the simulated population ────────────────────────────────────────────────
# Three classes with deliberately overlapping features. The rare class sits in
# the overlap between the two common ones, which is what makes it both
# scientifically interesting and invisible to a confidence-greedy strategy.
CLASSES = ("Ia", "II", "rare")
FRAC = (0.65, 0.30, 0.05)
MU = np.array([[0.00, 0.00], [2.20, 0.60], [1.10, 1.60]])
SD = np.array([[0.62, 0.55], [0.85, 0.70], [0.55, 0.48]])
MAG_MU = np.array([18.5, 19.0, 19.8])     # the rare class is fainter on average
MAG_SD = np.array([1.00, 1.00, 0.90])

N_POP = 6000
N_TEST = 4000
N_SEED = 30
N_SEASONS = 12
BUDGET = 20
N_REPEAT = 60          # the outcome is bimodal; 12 was not enough


def draw_population(n, rng):
    """Features, magnitudes and true labels for n transients."""
    y = rng.choice(len(CLASSES), size=n, p=FRAC)
    x = MU[y] + rng.normal(0, 1, (n, 2)) * SD[y]
    mag = MAG_MU[y] + rng.normal(0, 1, n) * MAG_SD[y]
    return x, mag, y


# ── a transparent classifier ────────────────────────────────────────────────
class GaussianNB:
    """Gaussian naive Bayes, written out rather than imported.

    Chosen deliberately over an ensemble: a class with NO labelled examples
    simply cannot be predicted, so the feedback mechanism this episode is about
    is visible in the model rather than buried inside it.
    """

    def fit(self, x, y):
        self.classes = np.unique(y)
        self.mu = np.zeros((len(self.classes), x.shape[1]))
        self.var = np.zeros_like(self.mu)
        self.prior = np.zeros(len(self.classes))
        for i, c in enumerate(self.classes):
            xi = x[y == c]
            self.mu[i] = xi.mean(axis=0)
            # a floor on the variance: with two or three examples the empirical
            # variance can collapse to zero and the posterior becomes a delta
            self.var[i] = np.maximum(xi.var(axis=0), 0.04)
            self.prior[i] = len(xi) / len(x)
        return self

    def log_proba(self, x):
        lp = np.zeros((len(x), len(self.classes)))
        for i in range(len(self.classes)):
            d = x - self.mu[i]
            lp[:, i] = (np.log(self.prior[i])
                        - 0.5 * np.sum(np.log(2 * math.pi * self.var[i]))
                        - 0.5 * np.sum(d ** 2 / self.var[i], axis=1))
        return lp

    def proba(self, x):
        lp = self.log_proba(x)
        lp -= lp.max(axis=1, keepdims=True)
        p = np.exp(lp)
        return p / p.sum(axis=1, keepdims=True)

    def predict(self, x):
        return self.classes[np.argmax(self.log_proba(x), axis=1)]


# ── the three follow-up strategies ──────────────────────────────────────────
def pick_canonical(unlabelled, mag, proba, k, rng):
    """What the community actually did: observe the brightest things.

    Ishida+2019 names the consequence -- "the predomination of brighter
    objects" and "the predominance of SNe Ia over other SN types" -- and
    attributes it to "a follow-up strategy designed to maximize the number of
    spectroscopically confirmed SNe Ia".
    """
    return unlabelled[np.argsort(mag[unlabelled])[:k]]


def pick_greedy(unlabelled, mag, proba, k, rng):
    """Spend the budget where the classifier is most sure. Maximises the count
    of confirmed events, which is a perfectly reasonable thing to want."""
    conf = proba[unlabelled].max(axis=1)
    return unlabelled[np.argsort(-conf)[:k]]


def pick_uncertain(unlabelled, mag, proba, k, rng):
    """Spend it where the classifier is least sure -- the smallest margin
    between its top two classes. This is Fink's deployed rule, which takes
    "the closest 10 alerts to P_Ia = 0.5"."""
    p = np.sort(proba[unlabelled], axis=1)
    margin = p[:, -1] - p[:, -2]
    return unlabelled[np.argsort(margin)[:k]]


STRATEGIES = (("canonical", pick_canonical), ("greedy", pick_greedy),
              ("uncertainty", pick_uncertain))


def run_loop(strategy, rng):
    """One full survey: seed, then N_SEASONS of train -> spend -> relabel."""
    x, mag, y = draw_population(N_POP, rng)
    xt, _, yt = draw_population(N_TEST, rng)

    # The seed set is what history handed us: bright objects only.
    bright = np.argsort(mag)[:int(N_POP * 0.10)]
    seed = rng.choice(bright, size=N_SEED, replace=False)
    labelled = np.zeros(N_POP, bool)
    labelled[seed] = True

    def measure(clf):
        pred = clf.predict(xt)
        m = yt == 2
        return (float(np.mean(pred == yt)),
                float(np.mean(pred[m] == 2)) if m.any() else 0.0,
                [int(np.sum(y[labelled] == c)) for c in range(3)])

    # Season 0 is what history handed us, before a single new spectrum.
    a0, r0, c0 = measure(GaussianNB().fit(x[labelled], y[labelled]))
    acc, rare_recall, comp = [a0], [r0], [c0]

    for _ in range(N_SEASONS):
        clf = GaussianNB().fit(x[labelled], y[labelled])
        proba = np.zeros((N_POP, 3))
        pk = clf.proba(x)
        for i, c in enumerate(clf.classes):
            proba[:, c] = pk[:, i]
        unlab = np.flatnonzero(~labelled)
        if len(unlab) == 0:
            break
        pick = strategy(unlab, mag, proba, min(BUDGET, len(unlab)), rng)
        labelled[pick] = True
        # Evaluate AFTER spending, so season s reflects s rounds of spectra.
        a, r, c = measure(GaussianNB().fit(x[labelled], y[labelled]))
        acc.append(a); rare_recall.append(r); comp.append(c)

    return np.array(acc), np.array(rare_recall), np.array(comp)


def run_all():
    """Repeat, then take the MEDIAN.

    The rare-class outcome is bimodal: a greedy run either stumbles on a rare
    object early and learns the class, or never sees one at all. Averaging
    across that mixes two different stories into a number that describes
    neither -- a 12-repeat mean read 0.088 where the median is 0.000 and
    48 runs in 60 end with no recall whatsoever.
    """
    out = {}
    for name, fn in STRATEGIES:
        A, R, C = [], [], []
        for r in range(N_REPEAT):
            a, rr, c = run_loop(fn, np.random.default_rng(SEED + 100 * r))
            A.append(a); R.append(rr); C.append(c)
        A, R, C = np.array(A), np.array(R), np.array(C)
        out[name] = (np.median(A, axis=0), np.median(R, axis=0),
                     np.mean(C, axis=0), R[:, -1])
    return out


# ═════════════════════════════════════════════════════════════════════════════
#  rendering helpers
# ═════════════════════════════════════════════════════════════════════════════
def _frame(img, colour=INK, width=3):
    ImageDraw.Draw(img).rectangle([0, 0, img.width - 1, img.height - 1],
                                  outline=colour, width=width)
    return img


def _axes(d, m, pw, ph, ygrid=(0.25, 0.5, 0.75, 1.0)):
    for f in ygrid:
        yy = m['t'] + ph - f * ph
        d.line([(m['l'], yy), (m['l'] + pw, yy)], fill=(226, 222, 210), width=1)
    d.line([(m['l'], m['t']), (m['l'], m['t'] + ph), (m['l'] + pw, m['t'] + ph)],
           fill=INK, width=3)


def _row(panels, gap=16, bg=CREAM):
    h = max(p.height for p in panels)
    w = sum(p.width for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (w, h), bg)
    x = 0
    for p in panels:
        sheet.paste(p, (x, (h - p.height) // 2))
        x += p.width + gap
    return sheet


# ═════════════════════════════════════════════════════════════════════════════
#  1. the published selection function
# ═════════════════════════════════════════════════════════════════════════════
def selection_plate(w=1500, h=760):
    """Published confirmation fractions by brightness. A LEDGER, not a
    computation -- the reel labels it as published on screen."""
    bars = [("< 17", 0.80), ("17–18.5", 0.95), ("18.5–20", 0.35), ("20–22", 0.15)]
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    m = {'l': 96, 'r': 56, 't': 52, 'b': 88}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    _axes(d, m, pw, ph)
    slot = pw / len(bars)
    bw = slot * 0.44
    for i, (_, frac) in enumerate(bars):
        x = m['l'] + slot * (i + 0.5)
        y0 = m['t'] + ph
        y1 = m['t'] + ph - frac * ph
        d.rectangle([x - bw / 2, m['t'], x + bw / 2, y0], outline=GHOST, width=3)
        d.rectangle([x - bw / 2, y1, x + bw / 2, y0], fill=INK)
        if frac < 0.5:
            d.rectangle([x - bw / 2, m['t'], x + bw / 2, y1], outline=ACC, width=5)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "selection.png")
    print("  selection.png   published confirmation fraction by peak magnitude: "
          + ", ".join(f"{a}->{b:.0%}" for a, b in bars))


# ═════════════════════════════════════════════════════════════════════════════
#  2. the deadline
# ═════════════════════════════════════════════════════════════════════════════
def bazin(t, a, t0, t_rise, t_fall):
    """The standard analytic transient light-curve shape (Bazin et al. 2009).
    Rises on t_rise, falls on t_fall; the peak is a real function of both."""
    return a * np.exp(-(t - t0) / t_fall) / (1.0 + np.exp(-(t - t0) / t_rise))


def deadline_plate(w=1560, h=780):
    t = np.linspace(-6, 60, 700)
    curves = [("Ia", 1.00, 0.0, 3.2, 22.0, ACC),
              ("II", 0.82, 4.0, 6.5, 40.0, INK),
              ("fast", 0.70, -1.0, 1.6, 6.5, SOFT)]
    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    m = {'l': 92, 'r': 52, 't': 50, 'b': 86}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']

    def X(v):
        return m['l'] + (v - t[0]) / (t[-1] - t[0]) * pw

    def Y(v):
        return m['t'] + ph - v * ph

    # the window in which a spectrum still says something: while it is bright
    d.rectangle([X(0), m['t'], X(12), m['t'] + ph], fill=(250, 238, 232))
    _axes(d, m, pw, ph)
    peaks = {}
    for name, a, t0, tr, tf, col in curves:
        f = bazin(t, a, t0, tr, tf)
        f = f / f.max() * a
        d.line([(X(tt), Y(vv)) for tt, vv in zip(t, f)], fill=col, width=6)
        peaks[name] = float(t[np.argmax(f)])
    d.line([(X(12), m['t']), (X(12), m['t'] + ph)], fill=ACCT, width=4)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "deadline.png")
    print("  deadline.png    Bazin peaks at t = "
          + ", ".join(f"{k} {v:+.1f}d" for k, v in peaks.items())
          + ";  decision window drawn 0–12 d")


# ═════════════════════════════════════════════════════════════════════════════
#  3. the loop                                   (THE SELF-CHECK)
# ═════════════════════════════════════════════════════════════════════════════
def loop_plate(res, w=1720, h=740):
    seasons = np.arange(0, N_SEASONS + 1)
    panels = []
    # Accuracy lives in a narrow band (0.86-0.93). On a 0-1 axis all three
    # strategies collapse onto one flat line and the panel says nothing -- yet
    # the point IS that accuracy rises while the panel beside it stays at zero.
    RANGES = {0: (0.84, 0.94), 1: (0.0, 1.0)}
    for which, ylab in ((0, "overall accuracy"), (1, "rare-class recall")):
        lo, hi = RANGES[which]
        pim = Image.new("RGB", ((w - 16) // 2, h), WHITE)
        d = ImageDraw.Draw(pim)
        m = {'l': 88, 'r': 44, 't': 46, 'b': 80}
        pw, ph = pim.width - m['l'] - m['r'], h - m['t'] - m['b']
        _axes(d, m, pw, ph)

        def X(s):
            return m['l'] + s / N_SEASONS * pw

        def Y(v, lo=lo, hi=hi):
            return m['t'] + ph - float(np.clip((v - lo) / (hi - lo), 0, 1)) * ph

        for name, col, wid in (("canonical", GHOST, 5),
                               ("greedy", INK, 6),
                               ("uncertainty", ACC, 7)):
            series = res[name][which]
            d.line([(X(s), Y(v)) for s, v in zip(seasons, series)],
                   fill=col, width=wid)
        d.rectangle([0, 0, pim.width - 1, h - 1], outline=INK, width=3)
        panels.append(pim)
    _row(panels).save(OUT / "loop.png")

    g_acc, g_rare = res["greedy"][0], res["greedy"][1]
    u_rare = res["uncertainty"][1]
    zero = {k: float(np.mean(res[k][3] < 0.02)) for k in
            ("canonical", "greedy", "uncertainty")}

    rises = g_acc[-1] > g_acc[0]
    # NOT "collapses", and not merely "low". The MEDIAN greedy run ends with
    # the rare class never recognised once: a brightness-biased seed set
    # contains no rare objects, so the classifier cannot predict the class at
    # all, so a confidence-greedy budget never queries one.
    stuck = g_rare[-1] < 0.02 and zero["greedy"] >= 0.50
    beaten = u_rare[-1] >= 0.40 and zero["uncertainty"] <= 0.05

    print(f"  loop.png        greedy:      accuracy {g_acc[0]:.3f} -> "
          f"{g_acc[-1]:.3f}   rare recall (median) {g_rare[0]:.3f} -> "
          f"{g_rare[-1]:.3f}")
    print(f"                  uncertainty: accuracy "
          f"{res['uncertainty'][0][-1]:.3f}   rare recall (median) "
          f"{res['uncertainty'][1][0]:.3f} -> {u_rare[-1]:.3f}")
    print(f"                  canonical:   accuracy "
          f"{res['canonical'][0][-1]:.3f}   rare recall (median) "
          f"{res['canonical'][1][-1]:.3f}")
    print(f"                  runs ending with NO rare-class recall, of "
          f"{N_REPEAT}: canonical {zero['canonical']*N_REPEAT:.0f}, greedy "
          f"{zero['greedy']*N_REPEAT:.0f}, uncertainty "
          f"{zero['uncertainty']*N_REPEAT:.0f}")
    ok = rises and stuck and beaten
    print(f"                  SELF-CHECK  accuracy rises: {rises} | greedy "
          f"median ~0 and >=50% of runs at zero: {stuck} | uncertainty "
          f">=0.40 and <=5% at zero: {beaten}  -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit(
            "[gen_triage] SELF-CHECK FAILED — the closed loop did not behave as "
            "the episode claims. Do not narrate a result the simulation does "
            "not produce; fix the experiment or drop the claim.")
    return g_acc, g_rare, u_rare


# ═════════════════════════════════════════════════════════════════════════════
#  4. what the labelled set is made of
# ═════════════════════════════════════════════════════════════════════════════
def composition_plate(res, w=1720, h=620):
    panels = []
    for name in ("greedy", "uncertainty"):
        comp = res[name][2]
        pim = Image.new("RGB", ((w - 16) // 2, h), WHITE)
        d = ImageDraw.Draw(pim)
        m = {'l': 80, 'r': 40, 't': 44, 'b': 76}
        pw, ph = pim.width - m['l'] - m['r'], h - m['t'] - m['b']
        slot = pw / (N_SEASONS + 1)
        bw = slot * 0.66
        for s in range(N_SEASONS + 1):
            tot = max(comp[s].sum(), 1e-9)
            x = m['l'] + slot * (s + 0.5)
            y = m['t'] + ph
            for c, col in ((0, GHOST), (1, SOFT), (2, ACC)):
                hgt = comp[s][c] / tot * ph
                d.rectangle([x - bw / 2, y - hgt, x + bw / 2, y], fill=col)
                y -= hgt
        d.line([(m['l'], m['t']), (m['l'], m['t'] + ph),
                (m['l'] + pw, m['t'] + ph)], fill=INK, width=3)
        d.rectangle([0, 0, pim.width - 1, h - 1], outline=INK, width=3)
        panels.append(pim)
    _row(panels).save(OUT / "composition.png")
    g, u = res["greedy"][2], res["uncertainty"][2]
    print(f"  composition.png rare fraction of the labelled set at season {N_SEASONS}: "
          f"greedy {g[-1][2]/g[-1].sum():.3%}  ·  uncertainty "
          f"{u[-1][2]/u[-1].sum():.2%}")


# ═════════════════════════════════════════════════════════════════════════════
#  5. where each strategy spends the budget
# ═════════════════════════════════════════════════════════════════════════════
def boundary_plate(w=1720, h=700):
    """Where doubt lives, in season 1 and again in season 8.

    A season-1 classifier has never seen a rare object, so its uncertainty is
    just the boundary between the two classes it DOES know, and the picks are
    barely enriched. Once a handful of rare objects carry labels, doubt moves
    to where they are. The migration is the mechanism, and showing only the
    first panel would misrepresent the strategy as ineffective.
    """
    rng = np.random.default_rng(SEED + 7)
    x, mag, y = draw_population(2400, rng)
    bright = np.argsort(mag)[:240]
    lab = np.zeros(len(x), bool)
    lab[rng.choice(bright, size=N_SEED, replace=False)] = True
    base = float(np.mean(y == 2))

    x0, x1 = x[:, 0].min() - 0.3, x[:, 0].max() + 0.3
    y0, y1 = x[:, 1].min() - 0.3, x[:, 1].max() + 0.3
    snaps, stats = {}, {}

    for season in range(1, 9):
        clf = GaussianNB().fit(x[lab], y[lab])
        proba = np.zeros((len(x), 3))
        pk = clf.proba(x)
        for i, c in enumerate(clf.classes):
            proba[:, c] = pk[:, i]
        unlab = np.flatnonzero(~lab)
        picks = pick_uncertain(unlab, mag, proba, 18, rng)
        if season in (1, 8):
            snaps[season] = (lab.copy(), picks.copy())
            stats[season] = float(np.mean(y[picks] == 2))
        lab[picks] = True

    panels = []
    for season in (1, 8):
        known, picks = snaps[season]
        pim = Image.new("RGB", ((w - 16) // 2, h), WHITE)
        d = ImageDraw.Draw(pim)
        m = {'l': 62, 'r': 40, 't': 42, 'b': 66}
        pw, ph = pim.width - m['l'] - m['r'], h - m['t'] - m['b']

        def X(v):
            return m['l'] + (v - x0) / (x1 - x0) * pw

        def Y(v):
            return m['t'] + ph - (v - y0) / (y1 - y0) * ph

        _axes(d, m, pw, ph, ygrid=(0.25, 0.5, 0.75))
        for i in range(len(x)):
            col = GHOST if y[i] != 2 else (206, 176, 160)
            d.ellipse([X(x[i, 0]) - 3, Y(x[i, 1]) - 3,
                       X(x[i, 0]) + 3, Y(x[i, 1]) + 3], fill=col)
        for i in np.flatnonzero(known):
            d.ellipse([X(x[i, 0]) - 5, Y(x[i, 1]) - 5,
                       X(x[i, 0]) + 5, Y(x[i, 1]) + 5], fill=INK)
        for i in picks:
            d.ellipse([X(x[i, 0]) - 9, Y(x[i, 1]) - 9,
                       X(x[i, 0]) + 9, Y(x[i, 1]) + 9], outline=ACC, width=4)
        d.rectangle([0, 0, pim.width - 1, h - 1], outline=INK, width=3)
        panels.append(pim)
    _row(panels).save(OUT / "boundary.png")
    print(f"  boundary.png    rare fraction of the picks: season 1 "
          f"{stats[1]:.0%} ({stats[1]/max(base,1e-9):.1f}x the {base:.0%} base "
          f"rate)  ->  season 8 {stats[8]:.0%} "
          f"({stats[8]/max(base,1e-9):.1f}x)")


# ═════════════════════════════════════════════════════════════════════════════
#  6. the honest trade-off
# ═════════════════════════════════════════════════════════════════════════════
def budget_plate(w=1560, h=780):
    """Exploration is not free. Mixing a fraction e of uncertainty picks into a
    greedy budget buys rare-class recall and costs confirmed-Ia count."""
    fracs = np.linspace(0.0, 1.0, 11)
    recall, ia_count = [], []
    for e in fracs:
        rr, nia = [], []
        for r in range(40):
            rng = np.random.default_rng(SEED + 31 * r + int(e * 100))
            x, mag, y = draw_population(N_POP, rng)
            xt, _, yt = draw_population(N_TEST, rng)
            bright = np.argsort(mag)[:int(N_POP * 0.10)]
            lab = np.zeros(N_POP, bool)
            lab[rng.choice(bright, size=N_SEED, replace=False)] = True
            for _ in range(N_SEASONS):
                clf = GaussianNB().fit(x[lab], y[lab])
                proba = np.zeros((N_POP, 3))
                pk = clf.proba(x)
                for i, c in enumerate(clf.classes):
                    proba[:, c] = pk[:, i]
                unlab = np.flatnonzero(~lab)
                k_e = int(round(BUDGET * e))
                pick = list(pick_uncertain(unlab, mag, proba, k_e, rng)) if k_e else []
                rest = np.setdiff1d(unlab, np.array(pick, int))
                pick += list(pick_greedy(rest, mag, proba, BUDGET - k_e, rng))
                lab[np.array(pick, int)] = True
            clf = GaussianNB().fit(x[lab], y[lab])
            pred = clf.predict(xt)
            mrare = yt == 2
            rr.append(float(np.mean(pred[mrare] == 2)))
            nia.append(int(np.sum(y[lab] == 0)))
        # The FRACTION OF SURVEYS that end up recognising the rare class at
        # all. The median of a bimodal outcome jumps between 0 and ~0.6 as the
        # mix crosses a threshold and draws as a jagged step; this is smooth,
        # bounded, and is the question a time-allocation committee asks.
        recall.append(float(np.mean(np.array(rr) > 0.02)))
        ia_count.append(np.mean(nia))
    recall = np.array(recall)
    ia = np.array(ia_count) / max(np.max(ia_count), 1e-9)

    img = Image.new("RGB", (w, h), WHITE)
    d = ImageDraw.Draw(img)
    m = {'l': 92, 'r': 52, 't': 50, 'b': 86}
    pw, ph = w - m['l'] - m['r'], h - m['t'] - m['b']
    _axes(d, m, pw, ph)

    def X(v):
        return m['l'] + v * pw

    def Y(v):
        return m['t'] + ph - float(np.clip(v, 0, 1)) * ph

    d.line([(X(f), Y(v)) for f, v in zip(fracs, recall)], fill=ACC, width=7)
    d.line([(X(f), Y(v)) for f, v in zip(fracs, ia)], fill=INK, width=6)
    d.rectangle([0, 0, w - 1, h - 1], outline=INK, width=3)
    img.save(OUT / "budget.png")
    print(f"  budget.png      surveys that recognise the rare class AT ALL: "
          f"{recall[0]:.0%} at 0% exploration -> {recall[-1]:.0%} at 100%;  "
          f"confirmed-Ia count falls to {ia[-1]:.0%} of its peak")
    return fracs, recall, ia


# ═════════════════════════════════════════════════════════════════════════════
def main():
    print(f"[gen_triage] seed {SEED}; {N_REPEAT} repeats x {N_SEASONS} seasons "
          f"x {BUDGET} spectra -> {OUT}")
    selection_plate()
    deadline_plate()
    res = run_all()
    loop_plate(res)
    composition_plate(res)
    boundary_plate()
    budget_plate()
    print("[gen_triage] done — six plates, one hard self-check passed.")


if __name__ == "__main__":
    main()
