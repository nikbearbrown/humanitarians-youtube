"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-batch-norm.

2160x3840; frame set to 4.5 x 8 (1 unit = 480 px). Batches become stacked columns / tables so the
numbers fit a tall frame (not a crop of the landscape rows). Numbers from ../experiment.py.
Type floor 48. Safe area +-1.95 x +-3.4.
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
DIM = ManimColor("#8B8F96"); CARD = ManimColor("#FAF9F5"); BAR = ManimColor("#A8A491")
FONT = "EB Garamond"
_HERE = os.path.dirname(os.path.abspath(__file__))
_ASSETS = [os.path.join(_HERE, "assets"), os.path.join(_HERE, "..", "assets")]
_FALLBACK = {"B02": 12.57, "B03": 14.64, "B04": 9.92, "B05": 18.99, "B06": 18.24, "B07": 13.29}
L = -1.9


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


def _eq(name, width):
    path = next((os.path.join(a, name + ".svg") for a in _ASSETS if os.path.exists(os.path.join(a, name + ".svg"))),
                os.path.join(_ASSETS[0], name + ".svg"))
    m = SVGMobject(path)
    m.set_color(INK)
    m.set(width=width)
    return m


ROWS = [1.1, 0.3, -0.5, -1.3]
NORM = ["−1.34", "−0.45", "0.45", "1.34"]


def card(cx, w=1.9, h=4.6, cy=0.0):
    return RoundedRectangle(width=w, height=h, corner_radius=0.15, stroke_color=DIM, stroke_width=3,
                            fill_color=CARD, fill_opacity=1).move_to([cx, cy, 0])


def col(vals, cx, color=INK):
    return VGroup(*[T(str(v), 48, color).move_to([cx, y, 0]) for v, y in zip(vals, ROWS)])


def dots(cx):
    return VGroup(*[Dot([cx, y - 0.0, 0], radius=0.1, color=INK) for y in ROWS])


class B02_Scales(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        ca, cb = card(-1.0), card(1.0)
        ha, hb = T("A", 56).move_to([-1.0, 1.95, 0]), T("B", 56).move_to([1.0, 1.95, 0])
        da, db = dots(-1.6), dots(0.4)
        until(self, D, 0.08)
        self.play(FadeIn(ca), FadeIn(ha), FadeIn(da), run_time=0.8)
        na = col([2, 4, 6, 8], -0.8)
        self.play(FadeIn(na), run_time=0.8)
        until(self, D, 0.42)
        self.play(FadeIn(cb), FadeIn(hb), FadeIn(db), run_time=0.8)
        nb = col([200, 400, 600, 800], 1.2)
        self.play(FadeIn(nb), run_time=0.8)
        until(self, D, 0.80)
        mk = T("100 times", 52, ACC).move_to([0, -2.95, 0])
        self.play(FadeIn(mk), run_time=0.6)
        finish(self, D)


class B03_Normalize(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=3.95, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = VGroup(T("normalized =", 48).move_to([0, 2.95, 0]), T("(x − mean)", 48).move_to([0, 2.3, 0]), T("÷ spread", 48).move_to([0, 1.65, 0]))
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.0)
        xs = [-1.3, -0.05, 1.2]
        ys = [0.1, -0.7, -1.5, -2.3]
        until(self, D, 0.26)
        h1 = T("x", 48, DIM).move_to([xs[0], 0.95, 0])
        c1 = VGroup(*[T(str(v), 48).move_to([xs[0], y, 0]) for v, y in zip([2, 4, 6, 8], ys)])
        self.play(FadeIn(h1), FadeIn(c1), Create(Line([-1.8, 0.55, 0], [1.8, 0.55, 0], color=DIM, stroke_width=2)), run_time=0.8)
        until(self, D, 0.48)
        h2 = T("−5", 48, DIM).move_to([xs[1], 0.95, 0])
        c2 = VGroup(*[T(v, 48).move_to([xs[1], y, 0]) for v, y in zip(["−3", "−1", "1", "3"], ys)])
        self.play(FadeIn(h2), FadeIn(c2), run_time=0.8)
        until(self, D, 0.74)
        h3 = T("÷2.24", 48, DIM).move_to([xs[2], 0.95, 0])
        c3 = VGroup(*[T(v, 48).move_to([xs[2], y, 0]) for v, y in zip(NORM, ys)])
        self.play(FadeIn(h3), FadeIn(c3), run_time=0.8)
        box = Rectangle(width=1.5, height=3.1, color=ACC, stroke_width=4).move_to([xs[2], -1.1, 0])
        self.play(Create(box), run_time=0.5)
        finish(self, D)


class B04_Same(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ca, cb = card(-1.0), card(1.0)
        ha, hb = T("A", 56).move_to([-1.0, 1.95, 0]), T("B", 56).move_to([1.0, 1.95, 0])
        da, db = dots(-1.6), dots(0.4)
        na, nb = col([2, 4, 6, 8], -0.8), col([200, 400, 600, 800], 1.2)
        self.add(ca, cb, ha, hb, da, db, na)
        self.wait(0.4)
        until(self, D, 0.10)
        self.play(FadeIn(nb), run_time=0.7)
        until(self, D, 0.42)
        na2, nb2 = col(NORM, -0.8), col(NORM, 1.2)
        self.play(FadeTransform(na, na2), FadeTransform(nb, nb2), run_time=1.4)
        until(self, D, 0.78)
        box = Rectangle(width=3.95, height=4.9, color=ACC, stroke_width=5).move_to([0, 0, 0])
        self.play(Create(box), run_time=0.7)
        finish(self, D)


class B05_Valley(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        head = VGroup(T("condition", 48, DIM).move_to([0, 3.0, 0]), T("number", 48, DIM).move_to([0, 2.45, 0]))
        t1 = T("raw 3,182,113").move_to([0, 1.65, 0]).align_to([L, 0, 0], LEFT)
        t2 = T("normalized 1.4").move_to([0, 0.4, 0]).align_to([L, 0, 0], LEFT)
        pre = VGroup(*[Rectangle(width=0.2, height=0.3).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.1, y, 0]) for y in (1.1, -0.15)])
        fin = VGroup(Rectangle(width=3.8, height=0.3).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 1.9, 1.1, 0]),
                     Rectangle(width=0.06, height=0.3).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.03, -0.15, 0]))
        self.play(FadeIn(head), FadeIn(t1), FadeIn(t2), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), run_time=1.6)
        until(self, D, 0.40)
        h2 = VGroup(T("steps to", 48, DIM).move_to([0, -1.0, 0]), T("near-best loss", 48, DIM).move_to([0, -1.55, 0]))
        s1 = T("raw: 100,000+").move_to([0, -2.3, 0]).align_to([L, 0, 0], LEFT)
        s2 = T("normalized: 4", 48, ACC).move_to([0, -3.0, 0]).align_to([L, 0, 0], LEFT)
        self.play(FadeIn(h2), run_time=0.7)
        until(self, D, 0.54)
        self.play(FadeIn(s1), FadeIn(s2), run_time=0.7)
        finish(self, D)


class B06_GammaBeta(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        panel = RoundedRectangle(width=3.95, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e1 = VGroup(T("out =", 48).move_to([0, 2.95, 0]), T("gamma × in", 48).move_to([0, 2.3, 0]), T("+ beta", 48).move_to([0, 1.65, 0]))
        self.play(FadeIn(panel), FadeIn(e1), run_time=1.0)
        ys = [0.1, -0.7, -1.5, -2.3]
        until(self, D, 0.34)
        hin = T("in", 48, DIM).move_to([-0.9, 0.9, 0])
        cin = VGroup(*[T(v, 48).move_to([-0.9, y, 0]) for v, y in zip(NORM, ys)])
        self.play(FadeIn(hin), FadeIn(cin), run_time=0.8)
        until(self, D, 0.62)
        hout = T("out", 48, DIM).move_to([0.9, 0.9, 0])
        cout = VGroup(*[T(v, 48).move_to([0.9, y, 0]) for v, y in zip(["−1.68", "0.11", "1.89", "3.68"], ys)])
        self.play(FadeIn(hout), FadeIn(cout), run_time=0.8)
        until(self, D, 0.80)
        box = Rectangle(width=1.7, height=3.3, color=ACC, stroke_width=4).move_to([0.9, -1.1, 0])
        self.play(Create(box), run_time=0.7)
        finish(self, D)


class B07_SmallBatch(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        sizes = [("batch 1", 0.999), ("batch 2", 0.707), ("batch 8", 0.351), ("batch 32", 0.176)]
        y0 = [1.9, 0.8, -0.3, -1.4]
        head = T("mean wobble", 48, DIM).move_to([0, 3.05, 0])
        txt = VGroup(*[T(f"{n} {v:.2f}").move_to([0, y, 0]).align_to([L, 0, 0], LEFT) for (n, v), y in zip(sizes, y0)])
        ys = [y - 0.5 for y in y0]
        pre = VGroup(*[Rectangle(width=0.2, height=0.3).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.1, y, 0]) for y in ys])
        fin = VGroup(*[Rectangle(width=v * 3.8, height=0.3).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + v * 1.9, y, 0])
                       for (_, v), y in zip(sizes, ys)])
        self.play(FadeIn(head), FadeIn(txt), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), run_time=1.6)
        until(self, D, 0.70)
        z = VGroup(T("batch of one:", 48, ACC).move_to([0, -2.55, 0]), T("output is 0", 48, ACC).move_to([0, -3.05, 0]))
        self.play(FadeIn(z), run_time=0.8)
        finish(self, D)
