"""scenes.py — Manim body beats B02–B07 for claude-liam-momentum.

Loss f(x,y) = 0.5(x^2 + 25 y^2), start (4,1), step 0.07, heavy-ball momentum. All numbers come
from experiment_output.txt (the same recurrence is recomputed here). Equations: MathText SVGs.
Each scene stretches to its beat's measured audio and holds across the 45-55% midpoint.
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
_FALLBACK = {"B02": 14.29, "B03": 13.44, "B04": 10.62, "B05": 13.18, "B06": 13.97, "B07": 12.97}


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


H = np.array([1.0, 25.0])
START = np.array([4.0, 1.0])
LR = 0.07


def path(beta, n):
    p = START.copy(); v = np.zeros(2); out = [p.copy()]
    for _ in range(n):
        v = beta * v + H * p
        p = p - LR * v
        out.append(p.copy())
    return out


# screen mapping for the valley
CX, CY = 0.0, -0.3
def P(p):
    return np.array([CX + 0.9 * p[0], CY + 1.6 * p[1], 0.0])


def contours():
    g = VGroup()
    for c in (20.5, 10.0, 4.0, 1.0, 0.25):
        a = np.sqrt(2 * c); b = np.sqrt(2 * c / 25)
        e = Ellipse(width=2 * a * 0.9, height=2 * b * 1.6, color=DIM, stroke_width=3)
        e.move_to([CX, CY, 0])
        g.add(e)
    return g


def pts_and_lines(pth, color, n):
    ds = VGroup(*[Dot(P(p), radius=0.1, color=color) for p in pth[:n + 1]])
    ls = VGroup(*[Line(P(pth[i]), P(pth[i + 1]), color=color, stroke_width=4) for i in range(n)])
    return ds, ls


def top(s, color=INK):
    return T(s, 52, color).move_to([0, 3.0, 0])


# ═════════════════════════════════════════════════════════════════════════════
class B02_Valley(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        cs = contours()
        head = top("a narrow valley", DIM)
        self.play(FadeIn(cs), FadeIn(head), run_time=1.2)
        gd = path(0.0, 8)
        start = Dot(P(START), radius=0.16, color=INK)
        lab = T("start (4, 1)", 48, DIM).next_to(start, UP, buff=0.35).shift(RIGHT * 0.2)
        until(self, D, 0.22)
        self.play(FadeIn(start), FadeIn(lab), run_time=0.6)
        ds, ls = pts_and_lines(gd, INK, 8)
        until(self, D, 0.36)
        for i in range(8):
            self.play(Create(ls[i]), FadeIn(ds[i + 1]), run_time=0.45)
        until(self, D, 0.82)
        r = top("plain descent: 47 steps")
        self.play(FadeTransform(head, r), run_time=0.8)
        finish(self, D)


class B03_Rule(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=11.6, height=5.6, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0.1, 0])
        e0 = _eq("eq0", 8.0).move_to([0, 1.5, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        until(self, D, 0.40)
        e1 = _eq("eq1", 6.4).move_to([0, 0.0, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.62)
        c1 = T("v = memory of past slopes", 48, DIM).move_to([0, -1.2, 0])
        self.play(FadeIn(c1), run_time=0.6)
        until(self, D, 0.78)
        c2 = T("beta 0 = plain descent", 48, DIM).move_to([0, -2.0, 0])
        box = SurroundingRectangle(e0, color=ACC, buff=0.2, stroke_width=4)
        self.play(FadeIn(c2), Create(box), run_time=0.7)
        finish(self, D)


class B04_Faster(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        cs = contours()
        gd = path(0.0, 8)
        gds, gls = pts_and_lines(gd, DIM, 8)
        for m in (*gds, *gls):
            m.set_opacity(0.8)
        r1 = top("plain: 47 steps", DIM)
        self.add(cs, gds, gls, r1)
        self.wait(0.4)
        mo = path(0.5, 12)
        ds, ls = pts_and_lines(mo, INK, 12)
        until(self, D, 0.22)
        for i in range(12):
            self.play(Create(ls[i]), FadeIn(ds[i + 1]), run_time=0.4)
        until(self, D, 0.80)
        r2 = top("plain: 47 · momentum: 20")
        self.play(FadeTransform(r1, r2), ds[12].animate.set_color(ACC), run_time=0.8)
        finish(self, D)


class B05_Cancel(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        gy = [25.0, -18.75, -7.81, 11.33, 1.07]; vy = [25.0, -6.25, -10.94, 5.86, 4.0]
        gx = [4.0, 3.72, 3.32, 2.89, 2.47]; vx = [4.0, 5.72, 6.18, 5.98, 5.46]
        def panel(cx, g, v, scale, base, title):
            head = T(title, 48).move_to([cx, 3.0, 0])
            gb, vb = VGroup(), VGroup()
            for i in range(5):
                x0 = cx - 2.0 + i * 1.0
                for (grp, val, dx, col) in ((gb, g[i], -0.2, BAR), (vb, v[i], 0.2, INK)):
                    h = max(abs(val) * scale, 0.05)
                    r = Rectangle(width=0.32, height=h).set_fill(col, 1).set_stroke(DIM, 2)
                    r.move_to([x0 + dx, base + (h / 2 if val >= 0 else -h / 2), 0])
                    grp.add(r)
            base_line = Line([cx - 2.5, base, 0], [cx + 2.5, base, 0], color=INK, stroke_width=3)
            return head, gb, vb, base_line
        a = panel(-3.4, gy, vy, 0.06, 0.9, "across the valley")
        b = panel(3.4, gx, vx, 0.24, -1.6, "along the valley")
        steps = VGroup(*[T(str(i + 1), 48, DIM).move_to([-5.4 + i * 1.0, -2.3, 0]) for i in range(5)],
                       *[T(str(i + 1), 48, DIM).move_to([1.4 + i * 1.0, -2.3, 0]) for i in range(5)])
        leg1 = T("slope", 48, DIM).move_to([-1.0, -3.05, 0])
        leg2 = T("velocity", 48).move_to([1.6, -3.05, 0])
        self.play(FadeIn(a[0]), FadeIn(b[0]), Create(a[3]), Create(b[3]), FadeIn(steps), run_time=1.0)
        until(self, D, 0.20)
        self.play(*[GrowFromEdge(r, DOWN) for r in a[1]], *[GrowFromEdge(r, DOWN) for r in b[1]], FadeIn(leg1), run_time=1.3)
        until(self, D, 0.46)
        self.play(*[GrowFromEdge(r, DOWN) for r in a[2]], *[GrowFromEdge(r, DOWN) for r in b[2]], FadeIn(leg2), run_time=1.3)
        until(self, D, 0.84)
        self.play(b[2][2].animate.set_fill(ACC, 1), run_time=0.6)
        finish(self, D)


class B06_Sweep(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        betas = ["0", "0.5", "0.8", "0.9", "0.95", "0.99"]
        steps = [47, 20, 29, 53, 99, 200]
        ys = [2.0, 1.1, 0.2, -0.7, -1.6, -2.5]
        S = 7.0 / 200.0
        head = top("steps to loss below 0.01", DIM)
        labs = VGroup(*[T(f"beta {b}").move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for b, y in zip(betas, ys)])
        bars = VGroup()
        for n, y in zip(steps, ys):
            w = n * S
            r = Rectangle(width=w, height=0.62).set_fill(BAR, 1).set_stroke(DIM, 3)
            r.move_to([-3.3 + w / 2, y, 0])
            bars.add(r)
        vals = VGroup(*[T(("200+" if n == 200 else str(n))).next_to(r, RIGHT, buff=0.2) for n, r in zip(steps, bars)])
        self.play(FadeIn(head), FadeIn(labs), run_time=0.9)
        until(self, D, 0.28)
        for r, v in zip(bars, vals):
            self.play(GrowFromEdge(r, LEFT), FadeIn(v), run_time=0.7)
        until(self, D, 0.86)
        self.play(bars[1].animate.set_fill(ACC, 1), run_time=0.6)
        finish(self, D)


class B07_Overshoot(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        n = 40
        ax = Axes(x_range=[0, n, 10], y_range=[-3, 4.5, 1], x_length=10.5, y_length=4.4,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.2, -0.4, 0])
        def px(t): return -5.05 + t * 10.5 / n
        def py(x): return -0.4 - 2.2 + (x + 3.0) * 4.4 / 7.5
        def poly(beta, color):
            pth = path(beta, n)
            return VGroup(*[Line([px(i), py(pth[i][0]), 0], [px(i + 1), py(pth[i + 1][0]), 0], color=color, stroke_width=5)
                            for i in range(n)])
        head = top("x against step", DIM)
        l5, l9 = poly(0.5, DIM), poly(0.9, INK)
        zero = DashedLine([-5.05, py(0.0), 0], [5.45, py(0.0), 0], color=GHOST, stroke_width=4)
        a5 = T("0.5", 48, DIM).move_to([-3.0, py(0.9) + 0.55, 0])
        a9 = T("0.9", 48).move_to([1.2, py(-1.6) - 0.0, 0])
        self.play(Create(ax), FadeIn(head), Create(zero), run_time=1.0)
        until(self, D, 0.20)
        self.play(Create(l5), FadeIn(a5), run_time=1.6)
        until(self, D, 0.42)
        self.play(Create(l9), FadeIn(a9), run_time=1.8)
        until(self, D, 0.62)
        pth = path(0.9, n)
        dot = Dot([px(11), py(float(pth[11][0])), 0], radius=0.17, color=ACC)
        tag = T("-2.17 at step 11", 48).next_to(dot, DOWN, buff=0.25).shift(RIGHT * 1.2)
        self.play(FadeIn(dot), FadeIn(tag), run_time=0.6)
        until(self, D, 0.84)
        r = top("beta 0.99: loss 1.1 at step 200")
        self.play(FadeTransform(head, r), run_time=0.8)
        finish(self, D)
