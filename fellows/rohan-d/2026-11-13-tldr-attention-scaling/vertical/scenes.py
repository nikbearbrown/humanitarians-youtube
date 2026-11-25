"""vertical/scenes.py — NATIVE 9:16 Manim LEARN scenes for tldr-attention-scaling (B10–B18).

Rendered at 2160x3840 (run.sh passes -r 2160,3840 for a 9:16 sheet). Manim keeps the frame
height at 8 units, so the portrait frame is 4.5 x 8 units and 1 unit = 480 px. These are not
crops of the landscape scenes: each beat is re-composed as a column (stacked panels, two-line
readouts, bars stacked top/bottom) with the same story, data and timing.

Same data as the landscape scenes (seeded run beside this file: experiment_output.txt).
Type floor: font_size >= 30 (x-height of a lowercase-only word >= 41 px at 3840 px tall).
Equations: MathText SVGs in ../assets (Manim MathTex unavailable: no dvisvgm).
"""
from manim import *
import numpy as np
import json
import os

# Portrait frame: Manim keeps 14.22 x 8 even at -r 2160,3840 (it would squash the picture), so set 4.5 x 8.
try:
    config.frame_height = 8.0
    config.frame_width = 4.5
except Exception:
    pass

BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
DIM = ManimColor("#8B8F96")
CARD = ManimColor("#FAF9F5")
BAR = ManimColor("#A8A491")
FONT = "EB Garamond"

_HERE = os.path.dirname(os.path.abspath(__file__))
_ASSETS = [os.path.join(_HERE, "assets"), os.path.join(_HERE, "..", "assets")]
_FALLBACK = {"B10": 14.68, "B11": 14.06, "B12": 12.86, "B13": 12.82, "B14": 13.06,
             "B15": 6.14, "B16": 13.18, "B17": 15.87, "B18": 12.03}


def _D(bid):
    try:
        for b in json.load(open(os.path.join(_HERE, "beat_sheet.json")))["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return _FALLBACK[bid]


def T(s, size=36, color=INK):
    return Text(s, font=FONT, font_size=max(size, 30), color=color)


def until(scene, D, frac):
    t = frac * D - scene.renderer.time
    if t > 0.02:
        scene.wait(t)


def finish(scene, D):
    scene.wait(max(D - 0.06 - scene.renderer.time, 0.05))


def instance(d):
    rng = np.random.default_rng(7)
    q = rng.standard_normal(d)
    K = rng.standard_normal((6, d))
    return K @ q


def softmax(x):
    e = np.exp(x - np.max(x))
    return e / e.sum()


AVG_MAX = {4: 0.574, 16: 0.778, 64: 0.890, 512: 0.961}
FIXED10 = {4: 0.209, 64: 0.368, 2048: 0.809}
SLOPE = {4: 0.203, 512: 0.028}
STD = [(4, 2.0), (16, 4.0), (64, 8.0), (256, 16.0), (512, 22.64), (2048, 45.31)]


def bars(w, cx=0.0, base=-2.3, H=4.8, bw=0.45, gap=0.22, fill=BAR):
    g = VGroup()
    n = len(w)
    total = n * bw + (n - 1) * gap
    for i, x in enumerate(w):
        h = max(float(x) * H, 0.03)
        r = Rectangle(width=bw, height=h)
        r.set_fill(fill, 1).set_stroke(DIM, 3)
        r.move_to([cx - total / 2 + bw / 2 + i * (bw + gap), base + h / 2, 0])
        g.add(r)
    return g


def bar_labels(g, size=30):
    out = VGroup()
    for i, r in enumerate(g):
        out.add(T(str(i + 1), size).move_to([r.get_center()[0], g[0].get_bottom()[1] - 0.3, 0]))
    return out


def readout(d, y=3.1):
    return T(f"length {d}", 36).move_to([0, y, 0])


HALF = 1.85   # number line half-width (score span 50)
LY = 1.55     # number line y


def numberline(y=LY, half=HALF, span=50):
    line = Line([-half, y, 0], [half, y, 0], color=INK, stroke_width=3)
    ticks = VGroup(*[Line([v / span * half, y - 0.1, 0], [v / span * half, y + 0.1, 0], color=INK, stroke_width=3)
                     for v in (-40, -20, 0, 20, 40)])
    labels = VGroup(*[T(str(v), 30).move_to([v / span * half, y - 0.4, 0]) for v in (-40, 0, 40)])
    return VGroup(line, ticks, labels)


def dots(scores, y=LY, half=HALF, span=50, scale=1.0):
    return VGroup(*[Dot([float(s) * scale / span * half, y, 0], radius=0.11, color=INK) for s in scores])


SBARS = dict(cx=0, base=-0.95, H=2.2, bw=0.4, gap=0.2)


class B10_SixBars(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B10")
        BIG = dict(base=-2.0, H=4.6)
        b = bars(softmax(instance(4)), **BIG)
        labs = bar_labels(b)
        cap = T("six keys, one query", 34, DIM).move_to([0, -3.05, 0])
        ro = readout(4)
        self.play(FadeIn(ro), LaggedStart(*[GrowFromEdge(r, DOWN) for r in b], lag_ratio=0.1),
                  FadeIn(labs), FadeIn(cap), run_time=1.6)
        until(self, D, 0.60)
        nb = bars(softmax(instance(512)), **BIG)
        self.play(FadeTransform(ro, readout(512)), Transform(b, nb), run_time=2.0)
        pct = T("99.6%", 44).next_to(b[1], RIGHT, buff=0.25).align_to(b[1], UP)
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
        bb = bars(softmax(s512), **SBARS)
        cap = T("scores", 32, DIM).move_to([-1.45, LY + 0.65, 0])
        lab = T("average largest weight", 32).move_to([0, -2.3, 0])
        st = {"ro": readout(512), "val": T(f"{AVG_MAX[512]:.3f}", 44).move_to([0, -2.9, 0])}
        self.play(FadeIn(nl), FadeIn(st["ro"]), FadeIn(cap), FadeIn(ds), FadeIn(bb), FadeIn(lab),
                  FadeIn(st["val"]), run_time=0.8)

        def step(d, run=1.1):
            s_ = instance(d)
            ro_n = readout(d)
            val_n = T(f"{AVG_MAX[d]:.3f}", 44).move_to([0, -2.9, 0])
            anims = [Transform(ds, dots(s_)), Transform(bb, bars(softmax(s_), **SBARS)),
                     FadeTransform(st["ro"], ro_n), FadeTransform(st["val"], val_n)]
            st["ro"], st["val"] = ro_n, val_n
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
        ax = Axes(x_range=[-8, 8, 4], y_range=[0, 1, 1], x_length=3.9, y_length=3.8,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0, 0.0, 0])
        curve = ax.plot(lambda x: sig(x), x_range=[-8, 8], color=INK, stroke_width=5)
        cap = T("two-way softmax sketch", 30, DIM).move_to([0, 2.4, 0])
        ro = readout(4)
        sl = T(f"slope  {SLOPE[4]:.3f}", 40).move_to([0, -2.65, 0])
        tag = T("our measure", 32, DIM).move_to([0, -3.2, 0])
        self.play(Create(ax), FadeIn(ro), FadeIn(cap), run_time=0.7)
        self.play(Create(curve), run_time=1.2)
        d4 = VGroup(*[Dot(ax.c2p(float(x), sig(float(x))), radius=0.12, color=INK) for x in instance(4)])
        self.play(FadeIn(d4), FadeIn(sl), FadeIn(tag), run_time=0.8)
        until(self, D, 0.62)
        s5 = np.clip(instance(512), -7.5, 7.5)
        d5 = VGroup(*[Dot(ax.c2p(float(x), sig(float(x))), radius=0.12, color=INK) for x in s5])
        self.play(Transform(d4, d5), FadeTransform(ro, readout(512)),
                  FadeTransform(sl, T(f"slope  {SLOPE[512]:.3f}", 40).move_to([0, -2.65, 0])), run_time=1.5)
        finish(self, D)


class B13_FixedTen(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B13")
        head = T("divide every score by 10", 30).move_to([0, 3.05, 0])
        self.play(FadeIn(head), run_time=0.5)
        rows = []
        for d, y in ((4, 1.8), (64, -0.1), (2048, -2.0)):
            w = softmax(instance(d) / 10.0)
            b = bars(w, cx=1.0, base=y - 0.65, H=1.4, bw=0.24, gap=0.07)
            lab = T(f"length {d}", 30).move_to([-1.9, y + 0.35, 0]).align_to([-1.9, 0, 0], LEFT)
            val = T(f"{FIXED10[d]:.3f}", 40).move_to([-1.9, y - 0.3, 0]).align_to([-1.9, 0, 0], LEFT)
            rows.append((b, lab, val))
        cap = T("average largest weight", 32, DIM).move_to([0, -3.05, 0])
        until(self, D, 0.10)
        self.play(FadeIn(rows[0][1]), FadeIn(rows[0][0]), FadeIn(rows[0][2]), FadeIn(cap), run_time=0.9)
        until(self, D, 0.28)
        self.play(FadeIn(rows[1][1]), FadeIn(rows[1][0]), FadeIn(rows[1][2]), run_time=0.9)
        until(self, D, 0.62)
        self.play(FadeIn(rows[2][1]), FadeIn(rows[2][0]), FadeIn(rows[2][2]), run_time=0.9)
        rows[2][0][int(np.argmax(softmax(instance(2048) / 10.0)))].set_fill(ACC, 1)
        finish(self, D)


class B14_WidthVsLength(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B14")
        ox, oy = -1.8, -2.6

        def P(d, s):
            return np.array([ox + (np.log2(d) - 2) * 0.36, oy + s * 0.105, 0])

        xaxis = Line([ox - 0.15, oy, 0], [ox + 3.45, oy, 0], color=INK, stroke_width=3)
        yaxis = Line([ox - 0.15, oy, 0], [ox - 0.15, oy + 4.9, 0], color=INK, stroke_width=3)
        xl = VGroup(*[T(str(d), 30).move_to([P(d, 0)[0], oy - 0.38, 0]) for d in (4, 16, 64, 256, 2048)])
        cap_x = T("length", 32, DIM).move_to([ox + 2.7, oy + 0.5, 0])
        cap_y = T("width of the scores", 34, DIM).move_to([0, 3.05, 0])
        self.play(Create(xaxis), Create(yaxis), FadeIn(xl), FadeIn(cap_x), FadeIn(cap_y), run_time=1.0)
        pts = {d: Dot(P(d, s), radius=0.11, color=INK) for d, s in STD}
        labs = {d: T(f"{s:g}", 30).next_to(pts[d], UP if d <= 64 else (LEFT if d == 2048 else DR), buff=0.1 if d <= 64 else 0.06) for d, s in STD}
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
        ring = Circle(radius=0.24, color=ACC, stroke_width=4).move_to(pts[2048])
        self.play(Create(ring), run_time=0.5)
        finish(self, D)   # HOLD on "commit"


class B15_Fold(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B15")
        nl = numberline()
        s = instance(512)
        ds = dots(s)
        bb = bars(softmax(s), **SBARS)
        ro = readout(512)
        cap = T("scores", 32, DIM).move_to([-1.45, LY + 0.45, 0])
        self.add(nl, ds, bb, ro, cap)
        self.wait(0.15)
        ns = s / np.sqrt(512)
        self.play(Transform(ds, dots(ns)), Transform(bb, bars(softmax(ns), **SBARS)), run_time=2.3)
        note = T("÷ √512  → width 1", 36).move_to([0, 2.65, 0])
        band = Rectangle(width=2 * 1.0 / 50 * HALF * 2, height=0.4, stroke_color=DIM, stroke_width=3).move_to([0, LY, 0])
        self.play(FadeIn(note), Create(band), run_time=0.6)
        finish(self, D)


def _eq(name, width):
    # Gate A runs this file in a scratch folder against a stub Manim, so do not fail on a
    # missing file here; the real render (reel folder) resolves it and Manim errors if absent.
    path = next((os.path.join(a, name + ".svg") for a in _ASSETS if os.path.exists(os.path.join(a, name + ".svg"))),
                os.path.join(_ASSETS[0], name + ".svg"))
    m = SVGMobject(path)
    m.set_color(INK)
    m.set(width=width)
    return m


class B16_NameIt(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B16")
        l1 = T("score =", 38).move_to([0, 3.1, 0])
        l2 = T("a sum of d products", 38).move_to([0, 2.55, 0])
        panel = RoundedRectangle(width=3.8, height=4.9, corner_radius=0.18, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, -0.85, 0])
        e0 = _eq("eq0", 3.5).move_to([0, 1.2, 0])
        self.play(Write(l1), Write(l2), FadeIn(panel), FadeIn(e0), run_time=1.4)
        until(self, D, 0.30)
        e1 = _eq("eq1", 3.1).move_to([0, -0.2, 0])
        self.play(FadeIn(e1), run_time=0.9)
        until(self, D, 0.62)
        e2 = _eq("eq2", 2.5).move_to([0, -2.0, 0])
        self.play(FadeIn(e2), run_time=0.9)
        finish(self, D)


class B17_ReadIt(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B17")
        panel = RoundedRectangle(width=3.8, height=1.6, corner_radius=0.15, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 2.4, 0])
        e1 = _eq("eq1", 3.3).move_to(panel)
        self.add(panel, e1)
        rows = [("left: spread squared", 0.10, 1.0), ("= means exactly d", 0.22, 0.35), ("if independent", 0.22, -0.25),
                ("q, k: random", 0.36, -1.1), ("d: a plain count", 0.36, -1.65),
                ("check at 512", 0.74, -2.5), ("512.65 → 1.00", 0.78, -3.05)]
        mark = Dot(radius=0.1, color=ACC)
        until(self, D, 0.08)
        for i, (txt, frac, y) in enumerate(rows):
            t = T(txt, 30).move_to([0, y, 0]).align_to([-1.6, 0, 0], LEFT)
            until(self, D, frac)
            mark.move_to(t.get_left() + LEFT * 0.2)
            if i == 0:
                self.play(FadeIn(t), FadeIn(mark), run_time=0.6)
            else:
                self.play(FadeIn(t), mark.animate.move_to(t.get_left() + LEFT * 0.2), run_time=0.6)
        finish(self, D)


class B18_SixBarsBack(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B18")
        s = instance(512)
        raw = bars(softmax(s), base=-2.0, H=4.6)
        raw[1].set_fill(ACC, 1)
        labs = bar_labels(raw)
        self.add(raw, labs)
        self.wait(0.3)
        raw_t = bars(softmax(s), base=0.7, H=1.9)
        raw_t[1].set_fill(ACC, 1)
        rl = T("raw", 40).move_to([0, 3.1, 0])
        self.play(Transform(raw, raw_t), Transform(labs, bar_labels(raw_t)), FadeIn(rl), run_time=1.0)
        sc = bars(softmax(s / np.sqrt(512)), base=-2.8, H=1.8)
        sc_labs = bar_labels(sc)
        sl = T("scaled", 40).move_to([0, -0.4, 0])
        until(self, D, 0.22)
        self.play(FadeIn(sl), FadeIn(sc_labs), LaggedStart(*[GrowFromEdge(r, DOWN) for r in sc], lag_ratio=0.1),
                  run_time=1.4)
        until(self, D, 0.66)
        wa = T("a weighted average", 36).move_to([0, -1.15, 0])
        self.play(FadeIn(wa), run_time=0.6)
        finish(self, D)
