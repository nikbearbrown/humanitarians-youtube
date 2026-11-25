"""scenes.py — Manim LEARN scenes for tldr-attention-scaling (section 1: B10–B18).

Palette: cream #F2F0E9, ink #3D3929, ONE terracotta #D97757 moment per beat, dim grey for foils.
Every number on screen comes from the seeded runs beside this file (experiment_output.txt,
naive_output.txt). Instances are regenerated here with the same recipe (seed 7, q then K).
Equations are MathText SVGs (assets/eq1.svg, eq2.svg): Manim MathTex is blocked (no dvisvgm).
Each scene stretches to its beat's measured audio and holds still across 45–55% of the beat
(GATE T / Gate V sample the midpoint).
"""
from manim import *
import numpy as np
import json
import os

# ── palette ──────────────────────────────────────────────────────────────────
BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
DIM = ManimColor("#8B8F96")
GHOST = ManimColor("#D9D4C7")
CARD = ManimColor("#FAF9F5")
BAR = ManimColor("#A8A491")
FONT = "EB Garamond"

_HERE = os.path.dirname(os.path.abspath(__file__))
_FALLBACK = {"B10": 14.68, "B11": 14.06, "B12": 12.86, "B13": 12.82, "B14": 13.06,
             "B15": 6.14, "B16": 13.18, "B17": 15.87, "B18": 12.03}


def _D(bid):
    """Measured narration length of a beat (the clock). Falls back to the audio run."""
    try:
        for b in json.load(open(os.path.join(_HERE, "beat_sheet.json")))["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return _FALLBACK[bid]


def T(s, size=36, color=INK):
    # GATE T floor: smallest text run must clear 41 px at 4K -> font_size >= 48 (x-height of lowercase-only words)
    return Text(s, font=FONT, font_size=max(size, 48), color=color)


def until(scene, D, frac):
    t = frac * D - scene.renderer.time
    if t > 0.02:
        scene.wait(t)


def finish(scene, D):
    t = D - 0.06 - scene.renderer.time
    scene.wait(max(t, 0.05))


# ── seeded data (same recipe as experiment.py) ───────────────────────────────
def instance(d):
    rng = np.random.default_rng(7)
    q = rng.standard_normal(d)
    K = rng.standard_normal((6, d))
    return K @ q


def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()


AVG_MAX = {4: 0.574, 16: 0.778, 64: 0.890, 512: 0.961}   # experiment_output.txt (20 000 trials)
FIXED10 = {4: 0.209, 64: 0.368, 2048: 0.809}             # naive_output.txt
SLOPE = {4: 0.203, 512: 0.028}                            # our measure, experiment_output.txt
STD = [(4, 2.0), (16, 4.0), (64, 8.0), (256, 16.0), (512, 22.64), (2048, 45.31)]


# ── shared builders (the state factory) ──────────────────────────────────────
def bars(w, cx=0.0, base=-2.2, H=4.0, bw=0.7, gap=0.35, fill=BAR):
    g = VGroup()
    n = len(w)
    total = n * bw + (n - 1) * gap
    for i, x in enumerate(w):
        h = max(float(x) * H, 0.04)
        r = Rectangle(width=bw, height=h)
        r.set_fill(fill, 1).set_stroke(DIM, 3)   # grey outline: short bars must not read as sub-floor text blobs (GATE T)
        r.move_to([cx - total / 2 + bw / 2 + i * (bw + gap), base + h / 2, 0])
        g.add(r)
    return g


def bar_labels(g, size=32):
    out = VGroup()
    for i, r in enumerate(g):
        out.add(T(str(i + 1), size).move_to([r.get_center()[0], g[0].get_bottom()[1] - 0.35, 0]))
    return out


def readout(d, pos=UP * 3.0 + LEFT * 3.6):
    return T(f"length {d}", 40).move_to(pos)


def numberline(y=0.7, half=5.5, span=50):
    line = Line([-half, y, 0], [half, y, 0], color=INK, stroke_width=3)
    ticks = VGroup()
    labels = VGroup()
    for v in (-40, -20, 0, 20, 40):
        x = v / span * half
        ticks.add(Line([x, y - 0.12, 0], [x, y + 0.12, 0], color=INK, stroke_width=3))
    for v in (-40, 0, 40):
        labels.add(T(str(v), 32).move_to([v / span * half, y - 0.45, 0]))
    return VGroup(line, ticks, labels)


def dots(scores, y=0.7, half=5.5, span=50, scale=1.0):
    g = VGroup()
    for s in scores:
        g.add(Dot([float(s) * scale / span * half, y, 0], radius=0.14, color=INK))
    return g


# ═════════════════════════════════════════════════════════════════════════════
class B10_SixBars(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B10")
        w4 = softmax(instance(4))
        w512 = softmax(instance(512))
        BIG = dict(bw=0.8, gap=0.38, H=4.3, base=-1.85)
        b = bars(w4, **BIG)
        labs = bar_labels(b)
        cap = T("six keys, one query", 36, DIM).move_to([0, -3.0, 0])
        ro = readout(4)
        self.play(FadeIn(ro), LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.1),
                  FadeIn(labs), FadeIn(cap), run_time=1.6)
        until(self, D, 0.60)
        ro2 = readout(512)
        nb = bars(w512, **BIG)
        self.play(FadeTransform(ro, ro2), Transform(b, nb), run_time=2.0)
        pct = T("99.6%", 48).next_to(b[1], RIGHT, buff=0.3).align_to(b[1], UP)
        b[1].set_fill(ACC, 1)
        self.play(FadeIn(pct), run_time=0.5)
        finish(self, D)


class B11_ScoresSpread(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B11")
        nl = numberline()
        s512 = instance(512)
        ds = dots(s512)
        bb = bars(softmax(s512), cx=0, base=-2.3, H=1.3, bw=0.5, gap=0.25)
        cap = T("scores", 36, DIM).move_to([-5.0, 1.55, 0])
        ro = readout(512)
        cnt = T("average largest weight  0.961", 36).move_to([0, -3.0, 0])
        self.play(FadeIn(nl), FadeIn(ro), FadeIn(cap), FadeIn(ds), FadeIn(bb), FadeIn(cnt), run_time=0.8)

        st = {"ro": ro, "cnt": cnt}

        def step(d, run=1.1):
            s_ = instance(d)
            ro_n = readout(d)
            cnt_n = T(f"average largest weight  {AVG_MAX[d]:.3f}", 36).move_to([0, -3.0, 0])
            anims = [Transform(ds, dots(s_)),
                     Transform(bb, bars(softmax(s_), cx=0, base=-2.3, H=1.3, bw=0.5, gap=0.25)),
                     FadeTransform(st["ro"], ro_n), FadeTransform(st["cnt"], cnt_n)]
            st["ro"], st["cnt"] = ro_n, cnt_n
            return anims, run

        until(self, D, 0.08)
        a, r = step(4); self.play(*a, run_time=r)
        until(self, D, 0.22)
        a, r = step(16); self.play(*a, run_time=r)
        until(self, D, 0.34)
        a, r = step(64); self.play(*a, run_time=r)
        until(self, D, 0.60)
        a, r = step(512, 1.4); self.play(*a, run_time=r)
        finish(self, D)


def sig(x):
    return 1 / (1 + np.exp(-x))


class B12_FlatEnds(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B12")
        ax = Axes(x_range=[-8, 8, 4], y_range=[0, 1, 1], x_length=10.5, y_length=4.0,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False},
                  ).move_to([0, -0.3, 0])
        curve = ax.plot(lambda x: sig(x), x_range=[-8, 8], color=INK, stroke_width=5)
        cap = T("two-way softmax sketch", 32, DIM).move_to([0, -3.0, 0])
        ro = readout(4)
        sl = T(f"slope  {SLOPE[4]:.3f}", 40).move_to([3.7, 3.0, 0])
        tag = T("our measure", 32, DIM).next_to(sl, DOWN, buff=0.28)
        self.play(Create(ax), FadeIn(ro), FadeIn(cap), run_time=0.7)
        self.play(Create(curve), run_time=1.2)
        s4 = instance(4)
        d4 = VGroup(*[Dot(ax.c2p(float(x), sig(float(x))), radius=0.16, color=INK) for x in s4])
        self.play(FadeIn(d4), FadeIn(sl), FadeIn(tag), run_time=0.8)
        until(self, D, 0.62)
        s5 = np.clip(instance(512), -7.5, 7.5)
        d5 = VGroup(*[Dot(ax.c2p(float(x), sig(float(x))), radius=0.16, color=INK) for x in s5])
        self.play(Transform(d4, d5), FadeTransform(ro, readout(512)),
                  FadeTransform(sl, T(f"slope  {SLOPE[512]:.3f}", 40).move_to([3.7, 3.0, 0])), run_time=1.5)
        finish(self, D)


class B13_FixedTen(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B13")
        head = T("divide every score by 10", 40).move_to([0, 3.0, 0])
        self.play(FadeIn(head), run_time=0.5)
        panels = []
        for d, cx in ((4, -4.4), (64, 0.0), (2048, 4.4)):
            w = softmax(instance(d) / 10.0)
            b = bars(w, cx=cx, base=-1.5, H=3.2, bw=0.42, gap=0.2)
            lab = T(f"length {d}", 36).move_to([cx, 2.0, 0])
            val = T(f"{FIXED10[d]:.3f}", 40).move_to([cx, -2.05, 0])
            panels.append((b, lab, val))
        cap = T("average largest weight", 32, DIM).move_to([0, -2.95, 0])
        until(self, D, 0.10)
        self.play(FadeIn(panels[0][1]), FadeIn(panels[0][0]), FadeIn(panels[0][2]), FadeIn(cap), run_time=0.9)
        until(self, D, 0.28)
        self.play(FadeIn(panels[1][1]), FadeIn(panels[1][0]), FadeIn(panels[1][2]), run_time=0.9)
        until(self, D, 0.62)
        self.play(FadeIn(panels[2][1]), FadeIn(panels[2][0]), FadeIn(panels[2][2]), run_time=0.9)
        panels[2][0][int(np.argmax(softmax(instance(2048) / 10.0)))].set_fill(ACC, 1)
        finish(self, D)


class B14_WidthVsLength(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B14")
        ox, oy = -5.0, -2.3

        def P(d, s):
            return np.array([ox + (np.log2(d) - 2) * 1.0, oy + s * 0.095, 0])

        xaxis = Line([ox - 0.2, oy, 0], [ox + 10.2, oy, 0], color=INK, stroke_width=3)
        yaxis = Line([ox - 0.2, oy, 0], [ox - 0.2, oy + 4.6, 0], color=INK, stroke_width=3)
        xl = VGroup(*[T(str(d), 32).move_to([P(d, 0)[0], oy - 0.4, 0]) for d in (4, 16, 64, 256, 2048)])
        cap_x = T("length", 36, DIM).move_to([ox + 10.0, oy + 0.55, 0])
        cap_y = T("width of the scores", 36, DIM).move_to([ox + 3.6, oy + 4.55, 0])
        self.play(Create(xaxis), Create(yaxis), FadeIn(xl), FadeIn(cap_x), FadeIn(cap_y), run_time=1.0)
        pts = {d: Dot(P(d, s), radius=0.15, color=INK) for d, s in STD}
        labs = {d: T(f"{s:g}", 32).next_to(pts[d], UP if d <= 64 else DR, buff=0.12 if d <= 64 else 0.08) for d, s in STD}
        until(self, D, 0.10)
        for d in (4, 16, 64):
            self.play(FadeIn(pts[d]), FadeIn(labs[d]), run_time=0.5)
            self.wait(0.35)
        until(self, D, 0.32)
        curve = ParametricFunction(lambda t: P(2 ** t, np.sqrt(2 ** t)), t_range=[2, 11], color=INK, stroke_width=4)
        self.play(Create(curve), run_time=1.2)
        until(self, D, 0.60)
        for d in (256, 512, 2048):
            self.play(FadeIn(pts[d]), FadeIn(labs[d]), run_time=0.5)
            self.wait(0.25)
        ring = Circle(radius=0.3, color=ACC, stroke_width=4).move_to(pts[2048])
        self.play(Create(ring), run_time=0.5)
        finish(self, D)   # HOLD: nothing moves on "commit"


class B15_Fold(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B15")
        nl = numberline()
        s = instance(512)
        ds = dots(s)
        bb = bars(softmax(s), cx=0, base=-2.3, H=1.3, bw=0.5, gap=0.25)
        ro = readout(512)
        cap = T("scores", 36, DIM).move_to([-5.0, 1.55, 0])
        self.add(nl, ds, bb, ro, cap)
        self.wait(0.15)
        ns = s / np.sqrt(512)
        self.play(Transform(ds, dots(ns)),
                  Transform(bb, bars(softmax(ns), cx=0, base=-2.3, H=1.3, bw=0.5, gap=0.25)),
                  run_time=2.3)
        note = T("÷ √512  → width 1", 40).move_to([0, 2.3, 0])
        band = Rectangle(width=2 * 1.0 / 50 * 5.5 * 2, height=0.5, stroke_color=DIM, stroke_width=3).move_to([0, 0.7, 0])
        self.play(FadeIn(note), Create(band), run_time=0.6)
        finish(self, D)


def _eq(name, width):
    m = SVGMobject(os.path.join(_HERE, "assets", name + ".svg"))
    m.set_color(INK)
    m.set(width=width)
    return m


class B16_NameIt(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B16")
        line = T("score = a sum of d products", 44).move_to([0, 2.7, 0])
        panel = RoundedRectangle(width=11.4, height=5.0, corner_radius=0.2, stroke_color=INK,
                                 stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([0, -0.35, 0])
        e0 = _eq("eq0", 8.6).move_to([0, 1.2, 0])
        self.play(Write(line), FadeIn(panel), FadeIn(e0), run_time=1.4)
        until(self, D, 0.30)
        e1 = _eq("eq1", 7.0).move_to([0, -0.15, 0])
        self.play(FadeIn(e1), run_time=0.9)
        until(self, D, 0.62)
        e2 = _eq("eq2", 5.6).move_to([0, -1.85, 0])
        self.play(FadeIn(e2), run_time=0.9)
        finish(self, D)


class B17_ReadIt(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B17")
        panel = RoundedRectangle(width=6.0, height=5.4, corner_radius=0.15, stroke_color=INK,
                                 stroke_width=3, fill_color=CARD, fill_opacity=1).move_to([-3.2, 0.0, 0])
        e1 = _eq("eq1", 5.2).move_to(panel)
        self.add(panel, e1)
        rows = [("left: spread squared", 0.10),
                ("= means exactly d", 0.22),
                ("if independent", 0.22),
                ("q, k: random", 0.36),
                ("d: a plain count", 0.36),
                ("512 → 512.65 → 1.00", 0.78)]
        ys = [2.6, 1.6, 0.9, -0.1, -0.8, -2.2]
        mark = Dot(radius=0.12, color=ACC)
        items = []
        for (txt, frac), y in zip(rows, ys):
            t = T(txt, 48).move_to([2.3, y, 0]).align_to([0.1, 0, 0], LEFT)
            items.append((t, frac))
        until(self, D, 0.08)
        for i, (t, frac) in enumerate(items):
            until(self, D, frac)
            mark.move_to(t.get_left() + LEFT * 0.3)
            if i == 0:
                self.play(FadeIn(t), FadeIn(mark), run_time=0.6)
            else:
                self.play(FadeIn(t), mark.animate.move_to(t.get_left() + LEFT * 0.3), run_time=0.6)
        finish(self, D)


class B18_SixBarsBack(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B18")
        s = instance(512)
        raw = bars(softmax(s), cx=0, bw=0.8, gap=0.38, H=4.3, base=-1.85)
        raw[1].set_fill(ACC, 1)
        labs = bar_labels(raw)
        self.add(raw, labs)
        self.wait(0.3)
        rl = T("raw", 48).move_to([-3.0, 1.95, 0])
        raw_t = bars(softmax(s), cx=-3.0, H=3.6)
        raw_t[1].set_fill(ACC, 1)
        self.play(Transform(raw, raw_t), Transform(labs, bar_labels(raw_t)), FadeIn(rl), run_time=1.0)
        sc = bars(softmax(s / np.sqrt(512)), cx=3.5, bw=0.6, gap=0.25, H=3.6)
        sc_labs = bar_labels(sc)
        sl = T("scaled", 48).move_to([3.5, 1.95, 0])
        until(self, D, 0.22)
        self.play(FadeIn(sl), FadeIn(sc_labs), LaggedStart(*[GrowFromEdge(r, DOWN) for r in sc], lag_ratio=0.1),
                  run_time=1.4)
        until(self, D, 0.66)
        wa = T("a weighted average", 48).move_to([0, 2.95, 0])
        self.play(FadeIn(wa), run_time=0.6)
        finish(self, D)
