"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-overfitting.

Rendered at 2160x3840; frame set to 4.5 x 8 (1 unit = 480 px). Re-composed as columns, not
cropped from landscape. Numbers from ../experiment_output.txt. Type floor 48. Safe: +-1.95 x +-3.4.
"""
from manim import *
import numpy as np
import json
import os

try:
    config.frame_height = 8.0
    config.frame_width = 4.5
except Exception:
    pass

BG = ManimColor("#F2F0E9"); INK = ManimColor("#3D3929"); ACC = ManimColor("#D97757")
DIM = ManimColor("#8B8F96"); BAR = ManimColor("#A8A491")
FONT = "EB Garamond"
_HERE = os.path.dirname(os.path.abspath(__file__))
_FALLBACK = {"B02": 14.61, "B03": 7.72, "B04": 10.9, "B05": 15.55, "B06": 13.29, "B07": 14.46}


def _D(bid):
    try:
        for b in json.load(open(os.path.join(_HERE, "beat_sheet.json")))["beats"]:
            if b["beat_id"] == bid and b.get("actual_duration_s"):
                return float(b["actual_duration_s"])
    except Exception:
        pass
    return _FALLBACK[bid]


def T(s, size=48, color=INK):
    return Text(s, font=FONT, font_size=max(size, 48), color=color)


def until(scene, D, frac):
    t = frac * D - scene.renderer.time
    if t > 0.02:
        scene.wait(t)


def finish(scene, D):
    scene.wait(max(D - 0.06 - scene.renderer.time, 0.05))


N = 8
X = np.linspace(0, 1, N)
Y = 2 * X + np.random.default_rng(3).normal(0, 0.25, N)
XT = np.linspace(0, 1, 200)
YT = 2 * XT + np.random.default_rng(99).normal(0, 0.25, 200)
TRAIN = [0.0987, 0.0913, 0.0851, 0.0358, 0.0308, 0.0012, 0.0000]
TEST = [0.0737, 0.0834, 0.0831, 0.1390, 0.1390, 0.2109, 0.2211]
FRESH_IDX = list(range(6, 200, 12))


def coef(d):
    return np.polyfit(X, Y, d)


def make_axes():
    return Axes(x_range=[0, 1, 0.5], y_range=[-1.1, 2.4, 1], x_length=3.2, y_length=4.6,
                axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.0, -0.7, 0])


def curve(ax, d):
    c = coef(d)
    return ax.plot(lambda t: float(np.clip(np.polyval(c, t), -1.05, 2.35)), x_range=[0, 1, 0.005],
                   color=INK, stroke_width=5)


def train_dots(ax):
    return VGroup(*[Dot(ax.c2p(float(x), float(y)), radius=0.1, color=INK) for x, y in zip(X, Y)])


def fresh_dots(ax):
    return VGroup(*[Dot(ax.c2p(float(XT[i]), float(YT[i])), radius=0.08, color=DIM, fill_opacity=0.0).set_stroke(DIM, 3)
                    for i in FRESH_IDX])


def misses(ax, d):
    c = coef(d)
    g = VGroup()
    for i in FRESH_IDX:
        yp = float(np.clip(np.polyval(c, XT[i]), -1.05, 2.35))
        g.add(Line(ax.c2p(float(XT[i]), float(YT[i])), ax.c2p(float(XT[i]), yp), color=DIM, stroke_width=3))
    return g


def top2(a, b, ca=DIM):
    return VGroup(T(a, 48, ca).move_to([0, 3.0, 0]), T(b, 48).move_to([0, 2.4, 0]))


class B02_Line(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        ax = make_axes()
        dots = train_dots(ax)
        line = curve(ax, 1)
        self.play(Create(ax), FadeIn(dots), run_time=1.2)
        self.play(Create(line), run_time=1.0)
        r1 = top2("degree 1", "train 0.099")
        until(self, D, 0.34)
        self.play(FadeIn(r1), run_time=0.6)
        until(self, D, 0.55)
        fd = fresh_dots(ax)
        self.play(FadeIn(fd), run_time=0.9)
        r2 = top2("degree 1", "test 0.074")
        self.play(FadeTransform(r1, r2), run_time=0.8)
        finish(self, D)


class B03_Memorize(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        ax = make_axes()
        dots = train_dots(ax)
        line = curve(ax, 1)
        r1 = top2("degree 1", "train 0.099")
        self.add(ax, dots, line, r1)
        self.wait(0.3)
        until(self, D, 0.18)
        self.play(Transform(line, curve(ax, 7)), run_time=2.2)
        r2 = top2("degree 7", "train 0.000")
        until(self, D, 0.62)
        rings = VGroup(*[Circle(radius=0.2, color=ACC, stroke_width=5).move_to(ax.c2p(float(x), float(y))) for x, y in zip(X, Y)])
        self.play(FadeTransform(r1, r2), Create(rings), run_time=0.9)
        finish(self, D)


class B04_Fresh(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ax = make_axes()
        dots = train_dots(ax)
        cv = curve(ax, 7)
        fd = fresh_dots(ax)
        ms = misses(ax, 7)
        r1 = top2("degree 7", "test 0.221")
        self.add(ax, dots, cv)
        self.play(FadeIn(fd), run_time=0.9)
        until(self, D, 0.28)
        self.play(Create(ms), run_time=1.2)
        self.play(FadeIn(r1), run_time=0.6)
        until(self, D, 0.74)
        r2 = top2("degree 1", "test 0.074")
        self.play(Transform(cv, curve(ax, 1)), Transform(ms, misses(ax, 1)), FadeTransform(r1, r2), run_time=1.6)
        finish(self, D)


class B05_Sweep(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        ax = Axes(x_range=[0.5, 7.5, 1], y_range=[0, 0.25, 0.05], x_length=3.6, y_length=3.4,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.05, -0.2, 0])
        cap = VGroup(T("error by", 48).move_to([0, 3.0, 0]), T("degree", 48).move_to([0, 2.4, 0]))
        px = lambda d: 0.05 - 1.8 + (d - 0.5) * (3.6 / 7.0)
        py = lambda v: -1.9 + v / 0.25 * 3.4
        ticks = VGroup(*[T(str(d)).move_to([px(d), -2.35, 0]) for d in range(1, 8)])
        self.play(Create(ax), FadeIn(ticks), FadeIn(cap), run_time=1.1)
        tr = [np.array([px(d + 1), py(TRAIN[d]), 0.0]) for d in range(7)]
        te = [np.array([px(d + 1), py(TEST[d]), 0.0]) for d in range(7)]
        tr_line = VGroup(*[Line(tr[i], tr[i + 1], color=DIM, stroke_width=6) for i in range(6)])
        te_line = VGroup(*[Line(te[i], te[i + 1], color=INK, stroke_width=6) for i in range(6)])
        tr_dots = VGroup(*[Dot(p, radius=0.1, color=DIM) for p in tr])
        te_dots = VGroup(*[Dot(p, radius=0.1, color=INK) for p in te])
        until(self, D, 0.26)
        self.play(Create(tr_line), FadeIn(tr_dots), run_time=2.0)
        until(self, D, 0.52)
        self.play(Create(te_line), FadeIn(te_dots), run_time=2.0)
        lt = T("train", 48, DIM).move_to([-0.9, -3.0, 0])
        le = T("test", 48).move_to([0.9, -3.0, 0])
        self.play(FadeIn(lt), FadeIn(le), run_time=0.5)
        until(self, D, 0.84)
        gap = Line(tr[-1], te[-1], color=ACC, stroke_width=8)
        self.play(Create(gap), run_time=0.6)
        finish(self, D)


class B06_MoreData(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        S = 3.6 / 0.25
        base = -2.0
        def mk(tr, te):
            g = VGroup()
            for cx, v in ((-0.95, tr), (0.95, te)):
                h = max(v * S, 0.05)
                r = Rectangle(width=1.5, height=h).set_fill(BAR, 1).set_stroke(DIM, 3)
                r.move_to([cx, base + h / 2, 0])
                g.add(r)
            return g
        b8 = mk(0.0, 0.2211)
        b40 = mk(0.0353, 0.0655)
        names = VGroup(T("train").move_to([-0.95, base - 0.5, 0]), T("test").move_to([0.95, base - 0.5, 0]))
        head1 = top2("degree 7", "8 points", INK)
        v1 = VGroup(T("0.000").move_to([-0.95, base + 0.45, 0]), T("0.221").move_to([0.95, base + 0.2211 * S + 0.4, 0]))
        self.play(FadeIn(head1), FadeIn(names), *[GrowFromEdge(r, DOWN) for r in b8], run_time=1.2)
        self.play(FadeIn(v1), run_time=0.5)
        until(self, D, 0.52)
        head2 = top2("degree 7", "40 points", INK)
        v2 = VGroup(T("0.035").move_to([-0.95, base + 0.0353 * S + 0.4, 0]), T("0.066").move_to([0.95, base + 0.0655 * S + 0.4, 0]))
        self.play(Transform(b8, b40), FadeTransform(head1, head2), FadeTransform(v1, v2), run_time=2.0)
        b8[1].set_fill(ACC, 1)
        finish(self, D)


class B07_Floor(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        S = 3.0 / 0.25
        L = -1.9
        vals = [0.0737, 0.0831, 0.2211]
        ys = [1.6, 0.2, -1.2]
        labs = VGroup(*[T(f"{n}  {v:.3f}").move_to([0, y + 0.7, 0]).align_to([L, 0, 0], LEFT)
                        for n, v, y in zip(("degree 1", "degree 3", "degree 7"), vals, ys)])
        bs = VGroup(*[Rectangle(width=v * S, height=0.5).set_fill(BAR, 1).set_stroke(DIM, 3) for v in vals])
        for r, v, y in zip(bs, vals, ys):
            r.move_to([L + v * S / 2, y, 0])
        head = T("test error").move_to([0, 3.05, 0])
        self.play(FadeIn(head), FadeIn(labs), *[GrowFromEdge(r, LEFT) for r in bs], run_time=1.6)
        until(self, D, 0.52)
        fx = L + 0.0625 * S
        floor = VGroup(*[DashedLine([fx, y + 0.3, 0], [fx, y - 0.3, 0], color=INK, stroke_width=5) for y in ys])
        ft = VGroup(T("dashed line:", 48, DIM).move_to([0, -2.4, 0]), T("noise floor", 48, DIM).move_to([0, -3.0, 0]))
        self.play(Create(floor), FadeIn(ft), run_time=1.0)
        until(self, D, 0.82)
        self.play(bs[2].animate.set_fill(ACC, 1), run_time=0.6)
        finish(self, D)
