"""scenes.py — Manim body beats B02–B07 for claude-liam-cross-entropy.

Palette: cream #F2F0E9, ink #3D3929, ONE terracotta #D97757 moment per beat, dim grey for foils.
Every number on screen comes from experiment_output.txt. Equations are MathText SVGs
(assets/eq*.svg): Manim MathTex is blocked (no dvisvgm). Each scene stretches to its beat's
measured audio and holds still across 45–55% of the beat (GATE T / Gate V sample the midpoint).
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
_FALLBACK = {"B02": 14.21, "B03": 12.57, "B04": 12.61, "B05": 16.96, "B06": 18.73, "B07": 14.23}


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


def bars(vals, cx=0.0, base=-1.8, H=4.0, bw=0.9, gap=0.9, fill=BAR):
    g = VGroup()
    n = len(vals)
    total = n * bw + (n - 1) * gap
    for i, v in enumerate(vals):
        h = max(float(v) * H, 0.05)
        r = Rectangle(width=bw, height=h)
        r.set_fill(fill, 1).set_stroke(DIM, 3)
        r.move_to([cx - total / 2 + bw / 2 + i * (bw + gap), base + h / 2, 0])
        g.add(r)
    return g


def softmax(z):
    e = np.exp(np.array(z) - max(z)); return e / e.sum()


SCORES = [2.0, 1.0, 0.1]
P = softmax(SCORES)                       # 0.659 0.2424 0.0986
P2 = softmax([2.341, 0.758, 0.001])       # after one step
NAMES = ["cat", "dog", "fox"]


# ═════════════════════════════════════════════════════════════════════════════
class B02_Shares(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        xs = [-4.0, 0.0, 4.0]
        names = [T(n).move_to([x, -2.45, 0]) for n, x in zip(NAMES, xs)]
        scores = [T(f"{s:.1f}", 56).move_to([x, 3.0, 0]) for s, x in zip(SCORES, xs)]
        lab = T("scores", 48, DIM).move_to([-6.0 + 0.9, 3.0, 0]).shift(LEFT * 0.0)
        self.play(FadeIn(VGroup(*names)), LaggedStart(*[FadeIn(s) for s in scores], lag_ratio=0.25), run_time=1.4)
        until(self, D, 0.30)
        sm = T("softmax", 48, DIM).move_to([0, 1.85, 0])
        E = np.exp(SCORES)
        bs = bars(E / E.max(), cx=0, base=-1.9, H=4.2, bw=1.5, gap=2.5)
        bs_final = bars(P, cx=0, base=-1.9, H=4.2, bw=1.5, gap=2.5)
        pct = VGroup(*[T(f"{round(float(p) * 100)}%", 56).next_to(r, UP, buff=0.2) for r, p in zip(bs_final, P)])
        self.play(FadeIn(sm), *[GrowFromEdge(r, DOWN) for r in bs], run_time=1.2)
        self.play(Transform(bs, bs_final), run_time=1.2)
        self.play(FadeIn(pct), run_time=0.6)
        until(self, D, 0.78)
        tag = T("right answer", 48).move_to([-4.0, -3.05, 0])
        self.play(FadeIn(tag), bs[0].animate.set_fill(ACC, 1).stretch_to_fit_width(1.8), run_time=0.6)
        finish(self, D)


class B03_Charge(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=11.6, height=5.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0.1, 0])
        e0 = _eq("eq0", 5.2).move_to([0, 1.35, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        cap = T("p = the share given to the right answer", 48, DIM).move_to([0, -1.95, 0])
        self.play(FadeIn(cap), run_time=0.6)
        until(self, D, 0.42)
        e1 = _eq("eq1", 6.8).move_to([0, -0.35, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.80)
        box = SurroundingRectangle(e1, color=ACC, buff=0.25, stroke_width=4)
        self.play(Create(box), run_time=0.6)
        finish(self, D)


class B04_Curve(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ax = Axes(x_range=[0, 1, 0.5], y_range=[0, 5, 1], x_length=9.5, y_length=4.6,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.4, -0.1, 0])
        yl = T("loss", 48, DIM).move_to([-4.35, 2.75, 0])
        xl = T("share given to the right answer", 48, DIM).move_to([0.4, -3.0, 0])
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=1.0)
        curve = ax.plot(lambda x: -np.log(x), x_range=[0.008, 1], color=INK, stroke_width=5)
        self.play(Create(curve), run_time=1.3)
        until(self, D, 0.34)
        pts = {}
        for q, direction in ((0.9, UP), (0.5, UR), (0.1, UR), (0.01, RIGHT)):
            loss = -np.log(q)
            d = Dot(ax.c2p(q, loss), radius=0.14, color=INK)
            txt = T(f"{q:g} → {loss:.3f}", 48).next_to(d, direction, buff=0.3 if direction is not UR else 0.2)
            if q == 0.5:
                txt.shift(UP * 0.8)
            pts[q] = (d, txt)
        for q, frac in ((0.9, 0.36), (0.5, 0.50), (0.1, 0.64), (0.01, 0.78)):
            until(self, D, frac)
            self.play(FadeIn(pts[q][0]), FadeIn(pts[q][1]), run_time=0.45)
        self.play(pts[0.01][0].animate.set_color(ACC).scale(1.6), run_time=0.5)
        finish(self, D)


class B05_TwoModels(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        A, Bv = [0.9, 0.9, 0.1], [0.6, 0.6, 0.4]
        LA, LB = 0.84, 0.65
        groups = []
        for name, vals, cx, loss in (("Model A", A, -3.8, LA), ("Model B", Bv, 3.8, LB)):
            head = T(name).move_to([cx, 3.15, 0])
            b0 = bars([0.5, 0.5, 0.5], cx=cx, base=-1.0, H=3.2, bw=0.8, gap=0.75)
            b = bars(vals, cx=cx, base=-1.0, H=3.2, bw=0.8, gap=0.75)
            vl = VGroup(*[T(f"{round(v * 100)}%", 48).next_to(r, UP, buff=0.15) for v, r in zip(vals, b)])
            ql = VGroup(*[T(f"Q{i + 1}", 48, DIM).move_to([r.get_center()[0], -1.5, 0]) for i, r in enumerate(b)])
            acc = T("accuracy 67%", 48).move_to([cx, -2.35, 0])
            ml = T(f"mean loss {loss:.2f}", 48).move_to([cx, -3.05, 0])
            groups.append((head, b, vl, ql, acc, ml, b0))
        until(self, D, 0.06)
        self.play(*[FadeIn(g[0]) for g in groups], run_time=0.5)
        self.play(*[GrowFromEdge(r, DOWN) for g in groups for r in g[6]],
                  *[FadeIn(g[3]) for g in groups], run_time=1.0)
        self.play(*[Transform(g[6], g[1]) for g in groups], run_time=1.2)
        self.play(*[FadeIn(g[2]) for g in groups], run_time=0.6)
        until(self, D, 0.46)
        self.play(*[FadeIn(g[4]) for g in groups], run_time=0.6)
        until(self, D, 0.74)
        self.play(*[FadeIn(g[5]) for g in groups], groups[0][6][2].animate.set_fill(ACC, 1), run_time=0.7)
        finish(self, D)


class B06_Step(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        xs = [-2.9, 0.0, 2.9]
        eq = _eq("eq2", 3.6).move_to([-4.0, 3.05, 0])
        loss0 = T("loss 0.417", 56).move_to([3.7, 3.05, 0])
        b = bars(P, cx=0, base=-1.55, H=3.7, bw=1.3, gap=1.6)
        names = [T(n).move_to([x, -2.05, 0]) for n, x in zip(NAMES, xs)]
        sl = ["−0.341", "+0.242", "+0.099"]
        slopes = VGroup(*[T(s, 56).move_to([x, -2.85, 0]) for s, x in zip(sl, xs)])
        self.play(FadeIn(eq), FadeIn(loss0), *[GrowFromEdge(r, DOWN) for r in b],
                  FadeIn(VGroup(*names)), run_time=1.5)
        until(self, D, 0.22)
        self.play(FadeIn(slopes), run_time=0.8)
        until(self, D, 0.50)
        nb = bars(P2, cx=0, base=-1.55, H=3.7, bw=1.3, gap=1.6)
        loss1 = T("loss 0.264", 56).move_to([3.7, 3.05, 0])
        self.play(Transform(b, nb), FadeTransform(loss0, loss1), run_time=1.8)
        b[0].set_fill(ACC, 1)
        until(self, D, 0.80)
        step = T("step size 1", 48, DIM).move_to([-0.3, 2.0, 0])
        self.play(FadeIn(step), run_time=0.5)
        finish(self, D)


class B07_Bites(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        r1 = T("share 0  →  loss ∞", 56).move_to([0, 3.0, 0])
        base = Line([-6.0, -2.2, 0], [6.0, -2.2, 0], color=INK, stroke_width=3)
        self.play(FadeIn(r1), Create(base), run_time=0.8)
        until(self, D, 0.38)
        r2 = T("clip at one in a trillion  →  27.63", 56).move_to([0, 3.0, 0])
        self.play(FadeTransform(r1, r2), run_time=0.9)
        H = 3.5 / 27.63
        big = Rectangle(width=1.8, height=27.63 * H).set_fill(BAR, 1).set_stroke(DIM, 3)
        big.move_to([-2.8, -2.2 + 27.63 * H / 2, 0])
        small = Rectangle(width=1.8, height=10.05 * H).set_fill(BAR, 1).set_stroke(DIM, 3)
        small.move_to([2.8, -2.2 + 10.05 * H / 2, 0])
        l1 = T("one confident mistake", 48).move_to([-2.8, -2.8, 0])
        l2 = T("1,000 answers at 99%", 48).move_to([2.8, -2.8, 0])
        v1 = T("27.6", 56).next_to(big, UP, buff=0.15)
        v2 = T("10.05", 56).next_to(small, UP, buff=0.15)
        until(self, D, 0.55)
        self.play(GrowFromEdge(big, DOWN), FadeIn(l1), run_time=1.0)
        self.play(FadeIn(v1), run_time=0.4)
        until(self, D, 0.78)
        self.play(GrowFromEdge(small, DOWN), FadeIn(l2), run_time=1.0)
        self.play(FadeIn(v2), run_time=0.4)
        big.set_fill(ACC, 1)
        finish(self, D)
