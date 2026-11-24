"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-cross-entropy.

Rendered at 2160x3840. Manim keeps the frame height at 8 units, so the portrait frame is set to
4.5 x 8 (1 unit = 480 px). These are not crops of the landscape scenes: each beat is re-composed
as a column (rows of horizontal bars, stacked readouts) with the same story, numbers and timing.
Numbers come from ../experiment_output.txt. Equations: MathText SVGs (no dvisvgm for MathTex).
Type floor: font_size >= 48 (x-height >= 72 px at 3840 tall). Portrait safe area: +-1.95 x +-3.4.
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
_FALLBACK = {"B02": 14.21, "B03": 12.57, "B04": 12.61, "B05": 16.96, "B06": 18.73, "B07": 14.23}
L = -1.9   # left margin of the column


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


def TL(s, y, size=48, color=INK):
    t = T(s, size, color)
    t.move_to([0, y, 0]).align_to([L, 0, 0], LEFT)
    return t


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


def softmax(z):
    e = np.exp(np.array(z) - max(z)); return e / e.sum()


def hbars(vals, ys, scale, h=0.5, fill=BAR):
    g = VGroup()
    for v, y in zip(vals, ys):
        w = max(float(v) * scale, 0.05)
        r = Rectangle(width=w, height=h)
        r.set_fill(fill, 1).set_stroke(DIM, 3)
        r.move_to([L + w / 2, y, 0])
        g.add(r)
    return g


def vbars(vals, cx, base, H, bw=0.6, gap=0.55, fill=BAR):
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


SCORES = [2.0, 1.0, 0.1]
P = softmax(SCORES)
P2 = softmax([2.341, 0.758, 0.001])
NAMES = ["cat", "dog", "fox"]


# ═════════════════════════════════════════════════════════════════════════════
class B02_Shares(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        y0 = [2.0, 0.2, -1.6]
        txt = VGroup(*[TL(f"{n}  {s:.1f}", y + 0.4) for n, s, y in zip(NAMES, SCORES, y0)])
        by = [y - 0.3 for y in y0]
        E = np.exp(SCORES)
        pre = hbars(E / E.max(), by, 3.0)
        fin = hbars(P, by, 3.0)
        pct = VGroup(*[T(f"{round(float(p) * 100)}%", 48).next_to(r, RIGHT, buff=0.15) for r, p in zip(fin, P)])
        sm = T("softmax", 48, DIM).move_to([0, 3.15, 0])
        self.play(FadeIn(txt), FadeIn(sm), run_time=1.2)
        until(self, D, 0.28)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=1.0)
        self.play(Transform(pre, fin), run_time=1.2)
        self.play(FadeIn(pct), run_time=0.6)
        until(self, D, 0.78)
        hi = Rectangle(width=float(P[0]) * 3.0, height=0.7).set_fill(ACC, 1).set_stroke(DIM, 3)
        hi.move_to([L + float(P[0]) * 3.0 / 2, by[0], 0])
        tag = T("right answer", 48).move_to([0, -3.0, 0])
        self.play(Transform(pre[0], hi), FadeIn(tag), run_time=0.6)
        finish(self, D)


class B03_Charge(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        panel = RoundedRectangle(width=3.95, height=6.0, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = _eq("eq0", 3.2).move_to([0, 1.9, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        cap = VGroup(T("p = the share", 48, DIM), T("given to the", 48, DIM), T("right answer", 48, DIM))
        cap.arrange(DOWN, buff=0.2).move_to([0, -1.6, 0])
        self.play(FadeIn(cap), run_time=0.6)
        until(self, D, 0.42)
        e1 = _eq("eq1", 3.6).move_to([0, 0.2, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.80)
        box = SurroundingRectangle(e1, color=ACC, buff=0.2, stroke_width=4)
        self.play(Create(box), run_time=0.6)
        finish(self, D)


class B04_Curve(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ax = Axes(x_range=[0, 1, 0.5], y_range=[0, 5, 1], x_length=3.4, y_length=3.0,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": False}).move_to([0.1, 1.2, 0])
        yl = T("loss", 48, DIM).move_to([-1.2, 3.05, 0])
        xl = T("share p", 48, DIM).move_to([0.1, -0.65, 0])
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=1.0)
        curve = ax.plot(lambda x: -np.log(x), x_range=[0.008, 1], color=INK, stroke_width=5)
        self.play(Create(curve), run_time=1.3)
        until(self, D, 0.34)
        ys = [-1.35, -1.9, -2.45, -3.0]
        rows = {}
        for (q, frac), y in zip(((0.9, 0.36), (0.5, 0.50), (0.1, 0.64), (0.01, 0.78)), ys):
            loss = -np.log(q)
            d = Dot(ax.c2p(q, loss), radius=0.12, color=INK)
            t = TL(f"{q:g} → {loss:.3f}", y)
            rows[q] = (d, t, frac)
        for q, (d, t, frac) in rows.items():
            until(self, D, frac)
            self.play(FadeIn(d), FadeIn(t), run_time=0.45)
        self.play(rows[0.01][0].animate.set_color(ACC).scale(1.6), run_time=0.5)
        finish(self, D)


class B05_TwoModels(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        acc = T("accuracy 67%", 48).move_to([0, 3.0, 0])
        blocks = []
        for name, vals, base, loss in (("A", [0.9, 0.9, 0.1], 0.7, 0.84), ("B", [0.6, 0.6, 0.4], -1.6, 0.65)):
            b0 = vbars([0.5, 0.5, 0.5], 0, base, 1.3)
            b = vbars(vals, 0, base, 1.3)
            vl = VGroup(*[T(f"{round(v * 100)}%", 48).next_to(r, UP, buff=0.1) for v, r in zip(vals, b)])
            ml = T(f"{name}: loss {loss:.2f}", 48).move_to([0, base - 0.5, 0])
            blocks.append((b0, b, vl, ml))
        self.play(FadeIn(acc), run_time=0.6)
        until(self, D, 0.08)
        self.play(*[GrowFromEdge(r, DOWN) for g in blocks for r in g[0]], run_time=1.0)
        self.play(*[Transform(g[0], g[1]) for g in blocks], run_time=1.2)
        self.play(*[FadeIn(g[2]) for g in blocks], run_time=0.6)
        until(self, D, 0.74)
        self.play(*[FadeIn(g[3]) for g in blocks], blocks[0][0][2].animate.set_fill(ACC, 1), run_time=0.7)
        finish(self, D)


class B06_Step(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        eq = _eq("eq2", 2.3).move_to([0, 2.45, 0])
        loss0 = T("loss 0.417", 48).move_to([0, 3.15, 0])
        y0 = [1.1, -0.5, -2.1]
        by = [y - 0.3 for y in y0]
        sl = ["−0.341", "+0.242", "+0.099"]
        txt = VGroup(*[TL(f"{n}  {s}", y + 0.4) for n, s, y in zip(NAMES, sl, y0)])
        b = hbars(P, by, 3.0)
        self.play(FadeIn(eq), FadeIn(loss0), run_time=1.0)
        self.play(*[GrowFromEdge(r, LEFT) for r in b], FadeIn(txt), run_time=1.4)
        until(self, D, 0.50)
        nb = hbars(P2, by, 3.0)
        loss1 = T("loss 0.264", 48).move_to([0, 3.15, 0])
        self.play(Transform(b, nb), FadeTransform(loss0, loss1), run_time=1.8)
        hi = Rectangle(width=float(P2[0]) * 3.0, height=0.7).set_fill(ACC, 1).set_stroke(DIM, 3)
        hi.move_to([L + float(P2[0]) * 3.0 / 2, by[0], 0])
        self.play(Transform(b[0], hi), run_time=0.4)
        until(self, D, 0.80)
        step = T("step size 1", 48, DIM).move_to([0, -3.0, 0])
        self.play(FadeIn(step), run_time=0.5)
        finish(self, D)


class B07_Bites(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        r1 = VGroup(T("share 0", 56), T("loss ∞", 56)).arrange(DOWN, buff=0.2).move_to([0, 2.1, 0])
        base = Line([-1.9, -1.7, 0], [1.9, -1.7, 0], color=INK, stroke_width=3)
        self.play(FadeIn(r1), Create(base), run_time=0.8)
        until(self, D, 0.38)
        r2 = VGroup(T("clip at one", 48), T("in a trillion", 48), T("→ 27.63", 56)).arrange(DOWN, buff=0.08).move_to([0, 2.1, 0])
        self.play(FadeTransform(r1, r2), run_time=0.9)
        H = 1.7 / 27.63
        big = Rectangle(width=1.3, height=27.63 * H).set_fill(BAR, 1).set_stroke(DIM, 3)
        big.move_to([-1.0, -1.7 + 27.63 * H / 2, 0])
        small = Rectangle(width=1.3, height=10.05 * H).set_fill(BAR, 1).set_stroke(DIM, 3)
        small.move_to([1.0, -1.7 + 10.05 * H / 2, 0])
        l1 = VGroup(T("one big", 48), T("mistake", 48)).arrange(DOWN, buff=0.05).move_to([-1.0, -2.5, 0])
        l2 = VGroup(T("1,000 at", 48), T("99%", 48)).arrange(DOWN, buff=0.05).move_to([1.0, -2.5, 0])
        v1 = T("27.6", 48).next_to(big, UP, buff=0.12)
        v2 = T("10.05", 48).next_to(small, UP, buff=0.12)
        until(self, D, 0.55)
        self.play(GrowFromEdge(big, DOWN), FadeIn(l1), run_time=1.0)
        self.play(FadeIn(v1), run_time=0.4)
        until(self, D, 0.78)
        self.play(GrowFromEdge(small, DOWN), FadeIn(l2), run_time=1.0)
        self.play(FadeIn(v2), run_time=0.4)
        big.set_fill(ACC, 1)
        finish(self, D)
