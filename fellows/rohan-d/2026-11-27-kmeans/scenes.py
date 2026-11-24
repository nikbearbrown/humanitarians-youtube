"""scenes.py — Manim body beats B02–B07 for claude-liam-kmeans.

Seven toy points, k = 2, centers start at (1,1) and (5,6). Every number comes from
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
_FALLBACK = {"B02": 9.41, "B03": 11.14, "B04": 13.16, "B05": 6.74, "B06": 13.25, "B07": 17.05}


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


PTS = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]], dtype=float)
C0 = np.array([[1, 1], [5, 6]], dtype=float)
C1 = np.array([[1.25, 1.5], [3.9, 5.1]], dtype=float)
LAB = [0, 0, 1, 1, 1, 1, 1]
OX, OY, S = -5.8, -3.1, 0.8


def P(p):
    return np.array([OX + S * p[0], OY + S * p[1], 0.0])


def dots(group_fill=True):
    g = VGroup()
    for p, l in zip(PTS, LAB):
        d = Dot(P(p), radius=0.14, color=INK)
        if group_fill and l == 1:
            d.set_fill(BAR, 1).set_stroke(INK, 3)
        g.add(d)
    return g


def center(c):
    return Square(side_length=0.34, color=INK, stroke_width=3).set_fill(ACC, 1).move_to(P(c))


def lines_to(C, labs):
    return VGroup(*[Line(P(p), P(C[l]), color=DIM, stroke_width=3) for p, l in zip(PTS, labs)])


RX = 2.6
FRAME = Rectangle(width=6.0 * S, height=7.3 * S, color=GHOST, stroke_width=4).move_to([OX + 3.0 * S, OY + 3.65 * S, 0])


def rd(s, y, color=INK):
    return T(s, 52, color).move_to([RX, y, 0])


# ═════════════════════════════════════════════════════════════════════════════
class B02_Start(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        pts = VGroup(*[Dot(P(p), radius=0.14, color=INK) for p in PTS])
        self.play(FadeIn(FRAME), FadeIn(pts), FadeIn(rd("7 points", 1.8)), run_time=1.2)
        until(self, D, 0.45)
        cs = VGroup(center(C0[0]), center(C0[1]))
        self.play(FadeIn(cs), FadeIn(rd("2 centers", 0.9)), run_time=0.8)
        until(self, D, 0.70)
        self.play(FadeIn(rd("start (1, 1)", 0.0)), FadeIn(rd("start (5, 6)", -0.9)), run_time=0.8)
        finish(self, D)


class B03_Assign(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        pts = VGroup(*[Dot(P(p), radius=0.14, color=INK) for p in PTS])
        cs = VGroup(center(C0[0]), center(C0[1]))
        self.add(FRAME, pts, cs)
        self.wait(0.3)
        until(self, D, 0.10)
        ring = Circle(radius=0.3, color=INK, stroke_width=5).move_to(P(PTS[2]))
        l1 = Line(P(PTS[2]), P(C0[0]), color=DIM, stroke_width=4)
        l2 = Line(P(PTS[2]), P(C0[1]), color=DIM, stroke_width=4)
        self.play(Create(ring), Create(l1), Create(l2), run_time=0.9)
        until(self, D, 0.38)
        self.play(FadeIn(rd("to 1st: 3.6", 1.8)), FadeIn(rd("to 2nd: 2.8", 0.9)), run_time=0.8)
        until(self, D, 0.62)
        allines = lines_to(C0, [0, 0, 1, 1, 1, 1, 1])
        self.play(Transform(VGroup(l1, l2), allines), run_time=1.2)
        until(self, D, 0.84)
        self.play(FadeIn(rd("2 points | 5 points", 0.0)), run_time=0.7)
        finish(self, D)


class B04_Update(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        pts = dots()
        cs = VGroup(center(C0[0]), center(C0[1]))
        ls = lines_to(C0, LAB)
        self.add(FRAME, pts, ls, cs)
        self.wait(0.3)
        until(self, D, 0.14)
        self.play(Transform(cs[0], center(C1[0])), Transform(ls, lines_to(np.array([C1[0], C0[1]]), LAB)), run_time=1.4)
        self.play(FadeIn(rd("group 1: (1.25, 1.5)", 1.4)), run_time=0.6)
        until(self, D, 0.52)
        self.play(Transform(cs[1], center(C1[1])), Transform(ls, lines_to(C1, LAB)), run_time=1.4)
        self.play(FadeIn(rd("group 2: (3.9, 5.1)", 0.4)), run_time=0.6)
        finish(self, D)


class B05_Repeat(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        pts = dots()
        cs = VGroup(center(C1[0]), center(C1[1]))
        ls = lines_to(C1, LAB)
        self.add(FRAME, pts, ls, cs)
        self.wait(0.6)
        until(self, D, 0.20)
        rings = VGroup(*[Circle(radius=0.34, color=INK, stroke_width=4).move_to(P(c)) for c in C1])
        self.play(FadeIn(rings), FadeIn(T("no point changed", 60).move_to([RX, 1.2, 0])), FadeIn(T("done in 2 rounds", 60).move_to([RX, 0.1, 0])), run_time=0.9)
        finish(self, D)


class B06_Inertia(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        head = T("inertia", 48, DIM).move_to([0, 3.0, 0])
        l1 = T("start").move_to([0, 1.5, 0]).align_to([-6.2, 0, 0], LEFT)
        l2 = T("after one move").move_to([0, -0.2, 0]).align_to([-6.2, 0, 0], LEFT)
        pre = VGroup(*[Rectangle(width=0.2, height=1.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.1, y, 0]) for y in (1.5, -0.2)])
        fin = VGroup(Rectangle(width=6.0, height=1.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.2 + 3.0, 1.5, 0]),
                     Rectangle(width=2.66, height=1.1).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.2 + 1.33, -0.2, 0]))
        v1 = T("19.25").next_to(fin[0], RIGHT, buff=0.25)
        v2 = T("8.53").next_to(fin[1], RIGHT, buff=0.25)
        self.play(FadeIn(head), FadeIn(l1), FadeIn(l2), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), FadeIn(v1), FadeIn(v2), run_time=1.8)
        until(self, D, 0.42)
        cap = T("never goes up", 52, ACC).move_to([0, -2.0, 0])
        self.play(FadeIn(cap), run_time=0.7)
        finish(self, D)


class B07_BadStart(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        def panel(cx, centers, line_pts, title, ytxt, txt, col):
            corner = [(0, 0), (0, 2), (4, 0), (4, 2)]
            pp = lambda x, y: np.array([cx - 2.4 + 1.2 * x, 0.3 - 1.2 + 1.2 * y, 0.0])
            ds = VGroup(*[Dot(pp(*c), radius=0.15, color=INK) for c in corner])
            cs = VGroup(*[Square(side_length=0.34, color=INK, stroke_width=3).set_fill(ACC, 1).move_to(pp(*c)) for c in centers])
            dl = DashedLine(pp(*line_pts[0]), pp(*line_pts[1]), color=DIM, stroke_width=4)
            t = T(title, 48, DIM).move_to([cx, 2.55, 0])
            r = T(txt, 52, col).move_to([cx, -1.95, 0])
            return ds, cs, dl, t, r
        A = panel(-3.2, [(0, 1), (4, 1)], [(2, -0.3), (2, 2.3)], "start 1", 0, "inertia 4", INK)
        B = panel(3.2, [(2, 0), (2, 2)], [(-0.3, 1), (4.3, 1)], "start 2", 0, "inertia 16", ACC)
        frames = VGroup(*[Rectangle(width=5.6, height=3.5, color=GHOST, stroke_width=4).move_to([cx, 0.3, 0]) for cx in (-3.2, 3.2)])
        self.play(FadeIn(frames), FadeIn(A[0]), FadeIn(A[3]), FadeIn(B[0]), FadeIn(B[3]), run_time=0.8)
        until(self, D, 0.20)
        self.play(FadeIn(A[1]), Create(A[2]), FadeIn(A[4]), run_time=1.0)
        until(self, D, 0.52)
        self.play(FadeIn(B[1]), Create(B[2]), FadeIn(B[4]), run_time=1.0)
        finish(self, D)
