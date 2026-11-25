"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-momentum.

2160x3840; frame set to 4.5 x 8 (1 unit = 480 px). The valley is turned so its long axis runs
vertically; panels are stacked, not cropped. Numbers recomputed from the same recurrence as
../experiment.py. Type floor 48. Safe area +-1.95 x +-3.4.
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
_FALLBACK = {"B02": 14.29, "B03": 13.44, "B04": 10.62, "B05": 13.18, "B06": 13.97, "B07": 12.97}
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


def top2(a, b, ca=DIM, cb=INK):
    return VGroup(T(a, 48, ca).move_to([0, 3.0, 0]), T(b, 48, cb).move_to([0, 2.4, 0]))


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


def P(p):   # valley turned: long axis (x) vertical
    return np.array([1.3 * p[1], 0.38 * p[0] - 0.55, 0.0])


def contours():
    g = VGroup()
    for c in (20.5, 10.0, 4.0, 1.0, 0.25):
        a = np.sqrt(2 * c); b = np.sqrt(2 * c / 25)
        e = Ellipse(width=2 * b * 1.3, height=2 * a * 0.38, color=DIM, stroke_width=3)
        e.move_to([0, -0.55, 0])
        g.add(e)
    return g


def pts_and_lines(pth, color, n):
    ds = VGroup(*[Dot(P(p), radius=0.08, color=color) for p in pth[:n + 1]])
    ls = VGroup(*[Line(P(pth[i]), P(pth[i + 1]), color=color, stroke_width=4) for i in range(n)])
    return ds, ls


class B02_Valley(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        cs = contours()
        head = top2("a narrow", "valley")
        self.play(FadeIn(cs), FadeIn(head), run_time=1.2)
        gd = path(0.0, 8)
        start = Dot(P(START), radius=0.12, color=INK)
        lab = Circle(radius=0.22, color=ACC, stroke_width=5).move_to(P(START))
        until(self, D, 0.22)
        self.play(FadeIn(start), FadeIn(lab), run_time=0.6)
        ds, ls = pts_and_lines(gd, INK, 8)
        until(self, D, 0.36)
        for i in range(8):
            self.play(Create(ls[i]), FadeIn(ds[i + 1]), run_time=0.45)
        until(self, D, 0.82)
        r = top2("plain descent", "47 steps", DIM, INK)
        self.play(FadeTransform(head, r), run_time=0.8)
        finish(self, D)


class B03_Rule(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=3.95, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = _eq("eq0", 3.5).move_to([0, 2.1, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        until(self, D, 0.40)
        e1 = _eq("eq1", 3.0).move_to([0, 1.0, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.62)
        c1 = VGroup(T("v = memory of", 48, DIM), T("past slopes", 48, DIM)).arrange(DOWN, buff=0.1).move_to([0, -0.5, 0])
        self.play(FadeIn(c1), run_time=0.6)
        until(self, D, 0.78)
        c2 = VGroup(T("beta 0 =", 48, DIM), T("plain descent", 48, DIM)).arrange(DOWN, buff=0.1).move_to([0, -2.1, 0])
        box = SurroundingRectangle(e0, color=ACC, buff=0.15, stroke_width=4)
        self.play(FadeIn(c2), Create(box), run_time=0.7)
        finish(self, D)


class B04_Faster(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        cs = contours()
        gd = path(0.0, 8)
        gds, gls = pts_and_lines(gd, DIM, 8)
        r1 = top2("plain", "47 steps", DIM, INK)
        self.add(cs, gds, gls, r1)
        self.wait(0.4)
        mo = path(0.5, 12)
        ds, ls = pts_and_lines(mo, INK, 12)
        until(self, D, 0.22)
        for i in range(12):
            self.play(Create(ls[i]), FadeIn(ds[i + 1]), run_time=0.4)
        until(self, D, 0.80)
        r2 = top2("plain 47", "momentum 20", DIM, INK)
        self.play(FadeTransform(r1, r2), ds[12].animate.set_color(ACC), run_time=0.8)
        finish(self, D)


class B05_Cancel(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        gy = [25.0, -18.75, -7.81, 11.33, 1.07]; vy = [25.0, -6.25, -10.94, 5.86, 4.0]
        gx = [4.0, 3.72, 3.32, 2.89, 2.47]; vx = [4.0, 5.72, 6.18, 5.98, 5.46]
        def panel(g, v, scale, base, head_y, title):
            head = T(title, 48).move_to([0, head_y, 0])
            gb, vb = VGroup(), VGroup()
            for i in range(5):
                x0 = -1.6 + i * 0.8
                for (grp, val, dx, col) in ((gb, g[i], -0.14, BAR), (vb, v[i], 0.14, INK)):
                    h = max(abs(val) * scale, 0.05)
                    r = Rectangle(width=0.24, height=h).set_fill(col, 1).set_stroke(DIM, 2)
                    r.move_to([x0 + dx, base + (h / 2 if val >= 0 else -h / 2), 0])
                    grp.add(r)
            bl = Line([-1.9, base, 0], [1.9, base, 0], color=INK, stroke_width=3)
            return head, gb, vb, bl
        a = panel(gy, vy, 0.036, 1.7, 3.0, "across valley")
        b = panel(gx, vx, 0.15, -1.1, 0.3, "along valley")
        steps = VGroup(*[T(str(i + 1), 48, DIM).move_to([-1.6 + i * 0.8, -1.7, 0]) for i in range(5)])
        leg1 = T("slope", 48, DIM).move_to([-0.8, -2.7, 0])
        leg2 = T("velocity", 48).move_to([0.9, -2.7, 0])
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
        y0 = [2.1, 1.15, 0.2, -0.75, -1.7, -2.65]
        head = T("beta · steps", 48, DIM).move_to([0, 3.0, 0])
        txt = VGroup(*[T(f"{b}   {'200+' if n == 200 else n}").move_to([0, y, 0]).align_to([L, 0, 0], LEFT)
                       for b, n, y in zip(betas, steps, y0)])
        bars = VGroup()
        for n, y in zip(steps, y0):
            w = n * 3.8 / 200.0
            r = Rectangle(width=w, height=0.22).set_fill(BAR, 1).set_stroke(DIM, 2)
            r.move_to([L + w / 2, y - 0.45, 0])
            bars.add(r)
        self.play(FadeIn(head), FadeIn(txt), run_time=0.9)
        until(self, D, 0.28)
        pre = VGroup(*[Rectangle(width=0.3, height=0.22).set_fill(BAR, 1).set_stroke(DIM, 2).move_to([L + 0.15, y - 0.45, 0])
                       for y in y0])
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.8)
        self.play(Transform(pre, bars), run_time=1.8)
        until(self, D, 0.86)
        hi = Rectangle(width=20 * 3.8 / 200.0, height=0.3).set_fill(ACC, 1).set_stroke(DIM, 2).move_to(bars[1].get_center())
        self.play(Transform(pre[1], hi), run_time=0.6)
        finish(self, D)


class B07_Overshoot(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        n = 40
        ax = Axes(x_range=[0, n, 10], y_range=[-3, 4.5, 1], x_length=3.5, y_length=4.0,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.1, -0.3, 0])
        def px(t): return 0.1 - 1.75 + t * 3.5 / n
        def py(x): return -0.3 - 2.0 + (x + 3.0) * 4.0 / 7.5
        def poly(beta, color):
            pth = path(beta, n)
            return VGroup(*[Line([px(i), py(pth[i][0]), 0], [px(i + 1), py(pth[i + 1][0]), 0], color=color, stroke_width=5)
                            for i in range(n)])
        head = top2("x against", "step")
        l5, l9 = poly(0.5, DIM), poly(0.9, INK)
        zero = DashedLine([-1.65, py(0.0), 0], [1.85, py(0.0), 0], color=DIM, stroke_width=3)
        leg5 = T("0.5", 48, DIM).move_to([-0.8, -2.95, 0])
        leg9 = T("0.9", 48).move_to([0.9, -2.95, 0])
        self.play(Create(ax), FadeIn(head), Create(zero), run_time=1.0)
        until(self, D, 0.20)
        self.play(Create(l5), FadeIn(leg5), run_time=1.6)
        until(self, D, 0.42)
        self.play(Create(l9), FadeIn(leg9), run_time=1.8)
        until(self, D, 0.62)
        pth = path(0.9, n)
        dot = Dot([px(11), py(float(pth[11][0])), 0], radius=0.12, color=ACC)
        tag = VGroup(T("-2.17", 48), T("at step 11", 48)).arrange(DOWN, buff=0.05).move_to([0.6, 0.4, 0])
        self.play(FadeIn(dot), FadeIn(tag), run_time=0.6)
        until(self, D, 0.84)
        r = top2("beta 0.99", "loss 1.1 at 200", DIM, INK)
        self.play(FadeTransform(head, r), run_time=0.8)
        finish(self, D)
