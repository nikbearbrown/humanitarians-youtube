"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-kmeans.

2160x3840; frame set to 4.5 x 8 (1 unit = 480 px). Scatter on top, readouts stacked beneath (not a
crop of the landscape layout). Numbers from ../experiment.py. Type floor 48. Safe +-1.95 x +-3.4.
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
DIM = ManimColor("#8B8F96"); GHOST = ManimColor("#D9D4C7"); BAR = ManimColor("#A8A491")
FONT = "EB Garamond"
_HERE = os.path.dirname(os.path.abspath(__file__))
_FALLBACK = {"B02": 9.41, "B03": 11.14, "B04": 13.16, "B05": 6.74, "B06": 13.25, "B07": 17.05}
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


PTS = np.array([[1, 1], [1.5, 2], [3, 4], [5, 7], [3.5, 5], [4.5, 5], [3.5, 4.5]], dtype=float)
C0 = np.array([[1, 1], [5, 6]], dtype=float)
C1 = np.array([[1.25, 1.5], [3.9, 5.1]], dtype=float)
LAB = [0, 0, 1, 1, 1, 1, 1]
OX, OY, S = -1.5, -0.45, 0.5


def P(p):
    return np.array([OX + S * p[0], OY + S * p[1], 0.0])


FRAME = Rectangle(width=6.0 * S, height=7.3 * S, color=GHOST, stroke_width=4).move_to([OX + 3.0 * S, OY + 3.65 * S, 0])


def dots(group_fill=True):
    g = VGroup()
    for p, l in zip(PTS, LAB):
        d = Dot(P(p), radius=0.1, color=INK)
        if group_fill and l == 1:
            d.set_fill(BAR, 1).set_stroke(INK, 3)
        g.add(d)
    return g


def center(c):
    return Square(side_length=0.28, color=INK, stroke_width=3).set_fill(ACC, 1).move_to(P(c))


def lines_to(C, labs):
    return VGroup(*[Line(P(p), P(C[l]), color=DIM, stroke_width=3) for p, l in zip(PTS, labs)])


def rd(s, y, color=INK, size=48):
    return T(s, size, color).move_to([0, y, 0])


class B02_Start(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        pts = VGroup(*[Dot(P(p), radius=0.1, color=INK) for p in PTS])
        self.play(FadeIn(FRAME), FadeIn(pts), FadeIn(rd("7 points", -1.0)), run_time=1.2)
        until(self, D, 0.28)
        cs = VGroup(center(C0[0]), center(C0[1]))
        self.play(FadeIn(cs), FadeIn(rd("2 centers", -1.65)), run_time=0.8)
        until(self, D, 0.42)
        self.play(FadeIn(rd("start (1, 1)", -2.35)), FadeIn(rd("start (5, 6)", -3.0)), run_time=0.8)
        finish(self, D)


class B03_Assign(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        pts = VGroup(*[Dot(P(p), radius=0.1, color=INK) for p in PTS])
        cs = VGroup(center(C0[0]), center(C0[1]))
        self.add(FRAME, pts, cs)
        self.wait(0.3)
        until(self, D, 0.10)
        ring = Circle(radius=0.22, color=INK, stroke_width=5).move_to(P(PTS[2]))
        l1 = Line(P(PTS[2]), P(C0[0]), color=DIM, stroke_width=4)
        l2 = Line(P(PTS[2]), P(C0[1]), color=DIM, stroke_width=4)
        self.play(Create(ring), Create(l1), Create(l2), run_time=0.9)
        until(self, D, 0.38)
        self.play(FadeIn(rd("to 1st: 3.6", -1.2)), FadeIn(rd("to 2nd: 2.8", -1.9)), run_time=0.8)
        until(self, D, 0.62)
        self.play(Transform(VGroup(l1, l2), lines_to(C0, [0, 0, 1, 1, 1, 1, 1])), run_time=1.2)
        until(self, D, 0.84)
        self.play(FadeIn(rd("2 and 5 points", -2.8)), run_time=0.7)
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
        until(self, D, 0.08)
        self.play(Transform(cs[0], center(C1[0])), Transform(ls, lines_to(np.array([C1[0], C0[1]]), LAB)), run_time=1.4)
        self.play(FadeIn(rd("1: (1.25, 1.5)", -1.5)), run_time=0.6)
        until(self, D, 0.36)
        self.play(Transform(cs[1], center(C1[1])), Transform(ls, lines_to(C1, LAB)), run_time=1.4)
        self.play(FadeIn(rd("2: (3.9, 5.1)", -2.3)), run_time=0.6)
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
        rings = VGroup(*[Circle(radius=0.26, color=INK, stroke_width=4).move_to(P(c)) for c in C1])
        self.play(FadeIn(rings), FadeIn(rd("no change", -1.5, INK, 60)), FadeIn(rd("2 rounds", -2.4, INK, 60)), run_time=0.9)
        finish(self, D)


class B06_Inertia(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        head = T("inertia", 48, DIM).move_to([0, 3.0, 0])
        t1 = T("start 19.25").move_to([0, 2.0, 0]).align_to([L, 0, 0], LEFT)
        t2 = T("1 move 8.53").move_to([0, 0.4, 0]).align_to([L, 0, 0], LEFT)
        pre = VGroup(*[Rectangle(width=0.2, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.1, y, 0]) for y in (1.3, -0.3)])
        fin = VGroup(Rectangle(width=3.8, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 1.9, 1.3, 0]),
                     Rectangle(width=1.68, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.84, -0.3, 0]))
        self.play(FadeIn(head), FadeIn(t1), FadeIn(t2), run_time=0.8)
        until(self, D, 0.14)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.5)
        self.play(Transform(pre, fin), run_time=1.8)
        until(self, D, 0.42)
        cap = T("never goes up", 52, ACC).move_to([0, -1.6, 0])
        self.play(FadeIn(cap), run_time=0.7)
        finish(self, D)


class B07_BadStart(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        def panel(cy, centers, line_pts, label, col):
            corner = [(0, 0), (0, 2), (4, 0), (4, 2)]
            pp = lambda x, y: np.array([-1.6 + 0.8 * x, cy - 0.8 + 0.8 * y, 0.0])
            ds = VGroup(*[Dot(pp(*c), radius=0.12, color=INK) for c in corner])
            cs = VGroup(*[Square(side_length=0.3, color=INK, stroke_width=3).set_fill(ACC, 1).move_to(pp(*c)) for c in centers])
            dl = DashedLine(pp(*line_pts[0]), pp(*line_pts[1]), color=DIM, stroke_width=4)
            fr = Rectangle(width=3.6, height=2.0, color=GHOST, stroke_width=4).move_to([0, cy, 0])
            r = T(label, 52, col).move_to([0, cy - 1.55, 0])
            return fr, ds, cs, dl, r
        A = panel(1.8, [(0, 1), (4, 1)], [(2, -0.3), (2, 2.3)], "1: inertia 4", INK)
        B = panel(-1.45, [(2, 0), (2, 2)], [(-0.3, 1), (4.3, 1)], "2: inertia 16", ACC)
        self.play(FadeIn(A[0]), FadeIn(A[1]), FadeIn(B[0]), FadeIn(B[1]), run_time=0.8)
        until(self, D, 0.20)
        self.play(FadeIn(A[2]), Create(A[3]), FadeIn(A[4]), run_time=1.0)
        until(self, D, 0.52)
        self.play(FadeIn(B[2]), Create(B[3]), FadeIn(B[4]), run_time=1.0)
        finish(self, D)
