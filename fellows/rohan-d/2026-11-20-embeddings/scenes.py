"""scenes.py — Manim body beats B02–B07 for claude-liam-embeddings.

Toy vectors cat (4,1), dog (3,2), car (1,4), cat x3 = (12,3). Every number comes from
experiment_output.txt (recomputed here). Equations: MathText SVGs. Each scene stretches to its
beat's measured audio and holds across the 45-55% midpoint.
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
_FALLBACK = {"B02": 12.01, "B03": 15.02, "B04": 12.91, "B05": 14.0, "B06": 11.07, "B07": 12.54}


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


CAT, DOG, CAR = np.array([4.0, 1.0]), np.array([3.0, 2.0]), np.array([1.0, 4.0])


def arrow(O, v, u, color=INK, w=6):
    end = [O[0] + u * v[0], O[1] + u * v[1], 0]
    return Arrow([O[0], O[1], 0], end, buff=0, color=color, stroke_width=w, max_tip_length_to_length_ratio=0.15)


# ═════════════════════════════════════════════════════════════════════════════
class B02_Plane(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        O = (-5.2, -2.3); u = 1.15
        xax = Arrow([O[0], O[1], 0], [O[0] + 6.0, O[1], 0], buff=0, color=DIM, stroke_width=4, max_tip_length_to_length_ratio=0.06)
        yax = Arrow([O[0], O[1], 0], [O[0], O[1] + 4.9, 0], buff=0, color=DIM, stroke_width=4, max_tip_length_to_length_ratio=0.06)
        fl = T("furry", 48, DIM).move_to([O[0] + 3.0, O[1] - 0.65, 0])
        vl = T("vehicle", 48, DIM).move_to([O[0] + 0.9, 3.05, 0])
        self.play(Create(xax), Create(yax), FadeIn(fl), FadeIn(vl), run_time=1.2)
        items = [("cat", CAT, 0.30, (0.2, 0.0), 1.4), ("dog", DOG, 0.46, (0.7, 0.0), 0.4), ("car", CAR, 0.62, (0.75, 0.0), -0.6)]
        for name, v, frac, off, y in items:
            until(self, D, frac)
            a = arrow(O, v, u)
            tip = (O[0] + u * v[0], O[1] + u * v[1])
            lab = T(name, 48).move_to([tip[0] + 0.75, tip[1] + 0.05, 0])
            rd = T(f"{name} ({int(v[0])}, {int(v[1])})", 48).move_to([3.4, y + 1.0, 0])
            self.play(Create(a), FadeIn(lab), FadeIn(rd), run_time=0.9)
        finish(self, D)


class B03_Distance(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        O = (-6.0, -2.0); u = 0.85
        a_cat = arrow(O, CAT, u)
        a_car = arrow(O, CAR, u)
        tip = lambda v: np.array([O[0] + u * v[0], O[1] + u * v[1], 0])
        l_cat = T("cat", 48).move_to([tip(CAT)[0] + 0.1, tip(CAT)[1] - 0.6, 0])
        l_car = T("car", 48).move_to([tip(CAR)[0], tip(CAR)[1] + 0.65, 0])
        self.play(Create(a_cat), Create(a_car), FadeIn(l_cat), FadeIn(l_car), run_time=1.2)
        until(self, D, 0.20)
        d1 = DashedLine(tip(CAT), tip(CAR), color=ACC, stroke_width=5)
        r1 = T("to car: 4.2", 48).move_to([2.6, 2.2, 0])
        self.play(Create(d1), FadeIn(r1), run_time=0.9)
        until(self, D, 0.34)
        c3 = tip(3 * CAT)
        a3 = arrow(O, 3 * CAT, u, DIM, 4)
        l3 = T("3 cats", 48, DIM).move_to([c3[0] + 1.0, c3[1] + 0.05, 0])
        self.play(Create(a3), FadeIn(l3), run_time=1.0)
        until(self, D, 0.44)
        off = np.array([0.0, -0.4, 0])
        d2 = DashedLine(tip(CAT) + off, c3 + off, color=ACC, stroke_width=5)
        r2 = T("to 3 cats: 8.2", 48).move_to([2.6, 1.4, 0])
        self.play(Create(d2), FadeIn(r2), run_time=0.9)
        until(self, D, 0.86)
        cap = T("distance says car is closer", 48).move_to([0, 3.0, 0])
        self.play(FadeIn(cap), run_time=0.6)
        finish(self, D)


class B04_Angle(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        O = (-5.2, -2.3); u = 1.25
        arrows = [("cat", CAT), ("dog", DOG), ("car", CAR)]
        grp = VGroup()
        for name, v in arrows:
            a = arrow(O, v, u)
            grp.add(a)
        labs = VGroup(*[T(name, 48).move_to([O[0] + u * v[0] + 0.75, O[1] + u * v[1] + 0.05, 0]) for name, v in arrows])
        self.play(*[Create(a) for a in grp], FadeIn(labs), run_time=1.3)
        th = lambda v: float(np.degrees(np.arctan2(v[1], v[0])))
        center = [O[0], O[1], 0]
        until(self, D, 0.34)
        arc1 = Arc(radius=2.0, start_angle=np.radians(th(CAT)), angle=np.radians(th(DOG) - th(CAT)), arc_center=center, color=INK, stroke_width=5)
        r1 = T("cat, dog: 20°", 48).move_to([3.3, 1.4, 0])
        self.play(Create(arc1), FadeIn(r1), run_time=0.9)
        until(self, D, 0.54)
        arc2 = Arc(radius=2.9, start_angle=np.radians(th(CAT)), angle=np.radians(th(CAR) - th(CAT)), arc_center=center, color=ACC, stroke_width=5)
        r2 = T("cat, car: 62°", 48).move_to([3.3, 0.4, 0])
        self.play(Create(arc2), FadeIn(r2), run_time=0.9)
        until(self, D, 0.78)
        ang = np.radians(th(CAT))
        ray = DashedLine(center, [O[0] + 8.2 * np.cos(ang), O[1] + 8.2 * np.sin(ang), 0], color=DIM, stroke_width=4)
        r3 = T("cat, 3 cats: 0°", 48).move_to([3.3, -0.6, 0])
        self.play(Create(ray), FadeIn(r3), run_time=0.9)
        finish(self, D)


class B05_Cosine(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        panel = RoundedRectangle(width=11.6, height=5.8, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = _eq("eq0", 4.6).move_to([0, 1.7, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        until(self, D, 0.40)
        e1 = _eq("eq1", 6.0).move_to([0, 0.1, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.62)
        c1 = T("cat · dog = 14", 48, DIM).move_to([0, -1.3, 0])
        self.play(FadeIn(c1), run_time=0.6)
        until(self, D, 0.76)
        c2 = T("same direction scores 1", 48, DIM).move_to([0, -2.2, 0])
        box = SurroundingRectangle(e1, color=ACC, buff=0.2, stroke_width=4)
        self.play(FadeIn(c2), Create(box), run_time=0.7)
        finish(self, D)


def rows_scene(scene, D, names, vals, ys, S, head, hi_idx, hi_frac, extra=None):
    labs = VGroup(*[T(n).move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for n, y in zip(names, ys)])
    hd = T(head, 48, DIM).move_to([0, 3.0, 0])
    pre = VGroup(*[Rectangle(width=0.3, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.45, y, 0]) for y in ys])
    fin = VGroup()
    for v, y in zip(vals, ys):
        w = max(v * S, 0.05)
        fin.add(Rectangle(width=w, height=0.7).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.6 + w / 2, y, 0]))
    txt = VGroup(*[T(f"{v:.2f}").next_to(r, RIGHT, buff=0.25) for v, r in zip(vals, fin)])
    scene.play(FadeIn(hd), FadeIn(labs), run_time=0.8)
    until(scene, D, 0.14)
    scene.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.6)
    scene.play(Transform(pre, fin), FadeIn(txt), run_time=1.8)
    until(scene, D, hi_frac)
    hi = Rectangle(width=max(vals[hi_idx] * S, 0.05), height=0.9).set_fill(ACC, 1).set_stroke(DIM, 3).move_to(fin[hi_idx].get_center())
    scene.play(Transform(pre[hi_idx], hi), run_time=0.6)
    return pre


class B06_Pairs(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        rows_scene(self, D, ["cat, dog", "dog, car", "cat, car", "cat, 3 cats"], [0.9417, 0.7399, 0.4706, 1.0],
                   [1.9, 0.7, -0.5, -1.7], 5.5, "cosine", 3, 0.84)
        finish(self, D)


class B07_Bites(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        ys = [1.8, 0.2, -1.4]
        names = ["cat, dog", "cat, 3 cats", "cat, zeros"]
        vals = [0.9417, 1.0]
        S = 6.2
        labs = VGroup(*[T(n).move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for n, y in zip(names, ys)])
        hd = T("cosine", 48, DIM).move_to([0, 3.0, 0])
        pre = VGroup(*[Rectangle(width=0.3, height=0.95).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.45, y, 0]) for y in ys[:2]])
        fin = VGroup(*[Rectangle(width=v * S, height=0.95).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([-2.6 + v * S / 2, y, 0])
                       for v, y in zip(vals, ys[:2])])
        txt = VGroup(*[T(f"{v:.2f}").next_to(r, RIGHT, buff=0.25) for v, r in zip(vals, fin)])
        self.play(FadeIn(hd), FadeIn(labs), run_time=0.8)
        until(self, D, 0.15)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.6)
        self.play(Transform(pre, fin), FadeIn(txt), run_time=1.6)
        until(self, D, 0.62)
        empty = Rectangle(width=6.2, height=0.95, color=DIM, stroke_width=3).move_to([-2.6 + 3.1, ys[2], 0])
        und = T("undefined", 48, ACC).move_to([0.5, ys[2], 0])
        self.play(Create(empty), FadeIn(und), run_time=1.0)
        finish(self, D)
