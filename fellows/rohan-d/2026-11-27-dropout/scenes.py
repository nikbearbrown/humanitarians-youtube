"""scenes.py — Manim body beats B02–B07 for claude-liam-dropout.

Eight activations 1..8 (sum 36), p = 0.5, inverted dropout. Every number comes from
experiment_output.txt. Each scene stretches to its beat's measured audio and holds across the
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
_FALLBACK = {"B02": 12.1, "B03": 10.43, "B04": 12.61, "B05": 10.86, "B06": 16.28, "B07": 15.13}


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


A = np.arange(1, 9, dtype=float)
MASK = np.array([1, 0, 0, 0, 1, 1, 1, 0])
XS = [(i - 3.5) * 1.25 for i in range(8)]


def bar(i, h, base, hollow=False):
    r = Rectangle(width=0.9, height=max(h, 0.05))
    if hollow:
        r.set_fill(CARD, 1).set_stroke(DIM, 3)
    else:
        r.set_fill(BAR, 1).set_stroke(DIM, 3)
    r.move_to([XS[i], base + max(h, 0.05) / 2, 0])
    return r


def bars(scale, base, mask=None, mult=None):
    g = VGroup()
    for i in range(8):
        keep = True if mask is None else bool(mask[i])
        m = 1.0 if (mult is None or not keep) else mult
        g.add(bar(i, A[i] * scale * m, base, hollow=not keep))
    return g


def top(s, color=INK, size=52):
    return T(s, size, color).move_to([0, 3.0, 0])


# ═════════════════════════════════════════════════════════════════════════════
class B02_Mask(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        base, sc = -2.5, 0.45
        labs = VGroup(*[T(str(i + 1), 48).move_to([XS[i], base - 0.5, 0]) for i in range(8)])
        full = bars(sc, base)
        pre = VGroup(*[Rectangle(width=0.9, height=0.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([XS[i], base + 0.05, 0]) for i in range(8)])
        head = top("activations sum to 36")
        self.play(FadeIn(labs), FadeIn(head), run_time=0.8)
        self.play(*[GrowFromEdge(r, DOWN) for r in pre], run_time=0.6)
        self.play(Transform(pre, full), run_time=1.2)
        until(self, D, 0.50)
        self.play(Transform(pre, bars(sc, base, MASK)), run_time=1.2)
        until(self, D, 0.78)
        r = top("kept: 1 + 5 + 6 + 7 = 19")
        self.play(FadeTransform(head, r), run_time=0.7)
        finish(self, D)


class B03_Scale(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        base, sc = -2.5, 0.3
        labs = VGroup(*[T(str(i + 1), 48, DIM).move_to([XS[i], base - 0.5, 0]) for i in range(8)])
        cur = bars(sc, base, MASK)
        h1 = top("kept: 19")
        self.add(labs, cur, h1)
        self.wait(0.4)
        until(self, D, 0.15)
        self.play(Transform(cur, bars(sc, base, MASK, mult=2.0)), run_time=1.6)
        until(self, D, 0.62)
        h2 = top("19 × 2 = 38", ACC)
        self.play(FadeTransform(h1, h2), run_time=0.8)
        finish(self, D)


class B04_Average(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        base, sc = -2.4, 0.07
        outs = [18, 40, 44, 22, 28]
        xs = [-4.4 + i * 2.0 for i in range(5)]
        pre = VGroup(*[Rectangle(width=1.1, height=0.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([x, base + 0.05, 0]) for x in xs])
        fin = VGroup(*[Rectangle(width=1.1, height=v * sc).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([x, base + v * sc / 2, 0]) for x, v in zip(xs, outs)])
        vals = VGroup(*[T(str(v), 48).move_to([x, base + v * sc + 0.4, 0]) for x, v in zip(xs, outs)])
        head = top("five more masks", DIM)
        self.play(*[GrowFromEdge(r, DOWN) for r in pre], FadeIn(head), run_time=0.7)
        self.play(Transform(pre, fin), FadeIn(vals), run_time=1.6)
        until(self, D, 0.42)
        ly = base + 36 * sc
        ln = DashedLine([-5.6, ly, 0], [5.6, ly, 0], color=INK, stroke_width=4)
        lt = T("36", 48, DIM).move_to([5.9, ly, 0])
        self.play(Create(ln), FadeIn(lt), run_time=0.8)
        until(self, D, 0.78)
        r = top("10,000 masks: 35.98", ACC)
        self.play(FadeTransform(head, r), run_time=0.7)
        finish(self, D)


class B05_WhyScale(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        base, sc = -2.3, 0.1
        xs, vs = [-3.1, 3.1], [18.0, 36.0]
        names = ["no scaling", "scaled"]
        labs = VGroup(*[T(n).move_to([x, base - 0.5, 0]) for n, x in zip(names, xs)])
        pre = VGroup(*[Rectangle(width=3.8, height=0.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([x, base + 0.05, 0]) for x in xs])
        fin = VGroup(*[Rectangle(width=3.8, height=v * sc).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([x, base + v * sc / 2, 0]) for x, v in zip(xs, vs)])
        vals = VGroup(*[T(f"{v:.1f}", 56).move_to([x, base + v * sc + 0.45, 0]) for x, v in zip(xs, vs)])
        self.play(FadeIn(labs), *[GrowFromEdge(r, DOWN) for r in pre], run_time=0.8)
        self.play(Transform(pre, fin), FadeIn(vals), run_time=1.6)
        until(self, D, 0.52)
        ly = base + 36 * sc
        ln = DashedLine([-5.6, ly, 0], [5.6, ly, 0], color=INK, stroke_width=4)
        self.play(Create(ln), run_time=0.8)
        until(self, D, 0.80)
        self.play(pre[1].animate.set_fill(ACC, 1), run_time=0.6)
        finish(self, D)


class B06_Crowd(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        cell = 0.3
        rects = VGroup()
        for i in range(16):
            for j in range(16):
                r = Rectangle(width=cell, height=cell).set_fill(BAR, 1).set_stroke(GHOST, 2)
                r.move_to([-3.5 + (j - 7.5) * cell, 0.2 - (i - 7.5) * cell, 0])
                rects.add(r)
        self.play(FadeIn(rects), run_time=1.4)
        until(self, D, 0.40)
        self.play(FadeIn(T("256 masks", 56).move_to([2.9, 1.5, 0])), run_time=0.7)
        self.play(FadeIn(T("one set of weights", 48).move_to([2.9, 0.5, 0])), run_time=0.7)
        until(self, D, 0.78)
        hi = rects[0].copy().set_fill(ACC, 1)
        self.play(Transform(rects[0], hi), FadeIn(T("average 36.0", 56, ACC).move_to([2.9, -0.8, 0])), run_time=0.8)
        finish(self, D)


class B07_Noise(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        rows = [("p = 0.1", 4.76, 1.9), ("p = 0.5", 14.28, 0.4), ("p = 0.9", 42.85, -1.1)]
        S = 7.0 / 43.0
        head = top("wobble of the output", DIM)
        labs = VGroup(*[T(n).move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for n, _, y in rows])
        pre = VGroup(*[Rectangle(width=0.2, height=1.0).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.9, y, 0]) for _, _, y in rows])
        fin = VGroup(*[Rectangle(width=v * S, height=1.0).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-3.0 + v * S / 2, y, 0]) for _, v, y in rows])
        txt = VGroup(*[T(f"{v:.1f}").next_to(r, RIGHT, buff=0.25) for (_, v, _), r in zip(rows, fin)])
        self.play(FadeIn(head), FadeIn(labs), run_time=0.8)
        until(self, D, 0.12)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), FadeIn(txt), run_time=1.6)
        until(self, D, 0.72)
        z = T("switch dropout off at test time", 52, ACC).move_to([0, -2.3, 0])
        self.play(FadeIn(z), run_time=0.8)
        finish(self, D)
