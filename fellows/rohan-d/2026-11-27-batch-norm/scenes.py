"""scenes.py — Manim body beats B02–B07 for claude-liam-batch-norm.

Batches A = [2,4,6,8], B = [200,400,600,800]. Every number comes from experiment_output.txt.
Equations: MathText SVGs. Each scene stretches to its beat's measured audio and holds across the
45-55% midpoint.
"""
from manim import *
import numpy as np
import json
import os

BG = ManimColor("#F2F0E9"); INK = ManimColor("#3D3929"); ACC = ManimColor("#D97757")
DIM = ManimColor("#8B8F96"); GHOST = ManimColor("#D9D4C7"); CARD = ManimColor("#FAF9F5")
BAR = ManimColor("#A8A491")
FONT = "EB Garamond"
_HERE = os.path.dirname(os.path.abspath(__file__))
_FALLBACK = {"B02": 12.57, "B03": 14.64, "B04": 9.92, "B05": 18.99, "B06": 18.24, "B07": 13.29}


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
    m = SVGMobject(os.path.join(_HERE, "assets", name + ".svg"))
    m.set_color(INK)
    m.set(width=width)
    return m


XS = [-3.6, -1.2, 1.2, 3.6]


def num_row(vals, y, color=INK, fmt="{}"):
    return VGroup(*[T(fmt.format(v), 52, color).move_to([x, y, 0]) for v, x in zip(vals, XS)])


def card_row(y):
    return RoundedRectangle(width=12.2, height=2.2, corner_radius=0.2, stroke_color=DIM, stroke_width=3,
                            fill_color=CARD, fill_opacity=1).move_to([0, y, 0])


def dot_row(y, color=INK):
    return VGroup(*[Dot([x, y, 0], radius=0.17, color=color) for x in XS])


NORM = [-1.34, -0.45, 0.45, 1.34]


# ═════════════════════════════════════════════════════════════════════════════
class B02_Scales(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        ca, cb = card_row(1.3), card_row(-1.7)
        la = T("A", 56).move_to([-5.7, 1.3, 0]); lb = T("B", 56).move_to([-5.7, -1.7, 0])
        da, db = dot_row(0.75), dot_row(-2.25)
        until(self, D, 0.08)
        self.play(FadeIn(ca), FadeIn(la), FadeIn(da), run_time=0.8)
        na = num_row([2, 4, 6, 8], 1.7)
        self.play(FadeIn(na), run_time=0.8)
        until(self, D, 0.42)
        self.play(FadeIn(cb), FadeIn(lb), FadeIn(db), run_time=0.8)
        nb = num_row([200, 400, 600, 800], -1.3)
        self.play(FadeIn(nb), run_time=0.8)
        until(self, D, 0.80)
        mk = T("100 times", 52, ACC).move_to([0, -0.2, 0])
        self.play(FadeIn(mk), run_time=0.6)
        finish(self, D)


class B03_Normalize(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=12.4, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = _eq("eq0", 3.6).move_to([0, 2.15, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.0)
        until(self, D, 0.26)
        r1 = num_row([2, 4, 6, 8], 1.1)
        t1 = T("x", 48, DIM).move_to([-5.35, 1.1, 0])
        self.play(FadeIn(r1), FadeIn(t1), Create(Line([-4.6, 0.45, 0], [4.6, 0.45, 0], color=GHOST, stroke_width=3)), run_time=0.8)
        until(self, D, 0.48)
        r2 = num_row(["−3", "−1", "1", "3"], -0.2)
        t2 = T("x − 5", 48, DIM).move_to([-5.35, -0.2, 0])
        self.play(FadeIn(r2), FadeIn(t2), Create(Line([-4.6, -0.85, 0], [4.6, -0.85, 0], color=GHOST, stroke_width=3)), run_time=0.8)
        until(self, D, 0.74)
        r3 = num_row(["−1.34", "−0.45", "0.45", "1.34"], -1.5)
        t3 = T("÷ 2.24", 48, DIM).move_to([-5.35, -1.5, 0])
        self.play(FadeIn(r3), FadeIn(t3), run_time=0.8)
        box = Rectangle(width=9.0, height=1.0, color=ACC, stroke_width=4).move_to([0.0, -1.5, 0])
        self.play(Create(box), run_time=0.5)
        finish(self, D)


class B04_Same(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ca, cb = card_row(1.3), card_row(-1.7)
        la = T("A", 56).move_to([-5.7, 1.3, 0]); lb = T("B", 56).move_to([-5.7, -1.7, 0])
        da, db = dot_row(0.75), dot_row(-2.25)
        na = num_row([2, 4, 6, 8], 1.7)
        nb = num_row([200, 400, 600, 800], -1.3)
        self.add(ca, cb, la, lb, da, db, na)
        self.wait(0.4)
        until(self, D, 0.10)
        self.play(FadeIn(nb), run_time=0.7)
        until(self, D, 0.42)
        na2 = num_row(NORM, 1.7)
        nb2 = num_row(NORM, -1.3)
        self.play(FadeTransform(na, na2), FadeTransform(nb, nb2), run_time=1.4)
        until(self, D, 0.78)
        box = Rectangle(width=12.5, height=5.6, color=ACC, stroke_width=5).move_to([0, -0.2, 0])
        self.play(Create(box), run_time=0.7)
        finish(self, D)


class B05_Valley(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        head = T("condition number", 48, DIM).move_to([0, 3.0, 0])
        l1 = T("raw").move_to([0, 1.9, 0]).align_to([-6.2, 0, 0], LEFT)
        l2 = T("normalized").move_to([0, 0.8, 0]).align_to([-6.2, 0, 0], LEFT)
        pre = VGroup(*[Rectangle(width=0.2, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.9, y, 0]) for y in (1.9, 0.8)])
        fin = VGroup(Rectangle(width=5.0, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-3.0 + 2.5, 1.9, 0]),
                     Rectangle(width=0.06, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-3.0 + 0.03, 0.8, 0]))
        v1 = T("3,182,113").next_to(fin[0], RIGHT, buff=0.25)
        v2 = T("1.4").next_to(fin[1], RIGHT, buff=0.25)
        self.play(FadeIn(head), FadeIn(l1), FadeIn(l2), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), FadeIn(v1), FadeIn(v2), run_time=1.6)
        until(self, D, 0.40)
        h2 = T("steps to near-best loss", 48, DIM).move_to([0, -0.5, 0])
        s1 = T("raw").move_to([0, -1.6, 0]).align_to([-6.2, 0, 0], LEFT)
        s2 = T("normalized").move_to([0, -2.6, 0]).align_to([-6.2, 0, 0], LEFT)
        w1 = T("not in 100,000").move_to([0, -1.6, 0]).align_to([-2.9, 0, 0], LEFT)
        w2 = T("4", 56, ACC).move_to([0, -2.6, 0]).align_to([-2.9, 0, 0], LEFT)
        self.play(FadeIn(h2), FadeIn(s1), FadeIn(s2), run_time=0.7)
        until(self, D, 0.54)
        self.play(FadeIn(w1), FadeIn(w2), run_time=0.7)
        finish(self, D)


class B06_GammaBeta(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        panel = RoundedRectangle(width=12.4, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e1 = _eq("eq1", 4.4).move_to([0, 2.1, 0])
        self.play(FadeIn(panel), FadeIn(e1), run_time=1.0)
        until(self, D, 0.34)
        r1 = num_row(NORM, 0.7)
        t1 = T("in", 48, DIM).move_to([-5.5, 0.7, 0])
        self.play(FadeIn(r1), FadeIn(t1), run_time=0.8)
        until(self, D, 0.62)
        r2 = num_row(["−1.68", "0.11", "1.89", "3.68"], -0.8)
        t2 = T("out", 48, DIM).move_to([-5.4, -0.8, 0])
        self.play(FadeIn(r2), FadeIn(t2), run_time=0.8)
        until(self, D, 0.80)
        cap = T("gamma 2, beta 1", 48, DIM).move_to([0, -2.2, 0])
        box = Rectangle(width=9.0, height=1.0, color=ACC, stroke_width=4).move_to([0.0, -0.8, 0])
        self.play(FadeIn(cap), Create(box), run_time=0.7)
        finish(self, D)


class B07_SmallBatch(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        sizes = ["batch 1", "batch 2", "batch 8", "batch 32"]
        vals = [0.999, 0.707, 0.351, 0.176]
        ys = [1.8, 0.7, -0.4, -1.5]
        head = T("wobble of the batch mean", 48, DIM).move_to([0, 3.0, 0])
        labs = VGroup(*[T(n).move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for n, y in zip(sizes, ys)])
        pre = VGroup(*[Rectangle(width=0.2, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-3.0, y, 0]) for y in ys])
        fin = VGroup(*[Rectangle(width=v * 6.0, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-3.1 + v * 3.0, y, 0])
                       for v, y in zip(vals, ys)])
        txt = VGroup(*[T(f"{v:.2f}").next_to(r, RIGHT, buff=0.25) for v, r in zip(vals, fin)])
        self.play(FadeIn(head), FadeIn(labs), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), FadeIn(txt), run_time=1.6)
        until(self, D, 0.70)
        z = T("batch of one: every output is 0", 52, ACC).move_to([0, -2.7, 0])
        self.play(FadeIn(z), run_time=0.8)
        finish(self, D)
