"""vertical/scenes.py — NATIVE 9:16 Manim scenes B02–B07 for claude-liam-embeddings.

2160x3840; frame set to 4.5 x 8 (1 unit = 480 px). Re-composed for a tall frame (uniform scale
so angles stay true; readouts stacked). Numbers recomputed from the same vectors as
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
_FALLBACK = {"B02": 12.01, "B03": 15.02, "B04": 12.91, "B05": 14.0, "B06": 11.07, "B07": 12.54}
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


CAT, DOG, CAR = np.array([4.0, 1.0]), np.array([3.0, 2.0]), np.array([1.0, 4.0])


def arrow(O, v, u, color=INK, w=6):
    end = [O[0] + u * v[0], O[1] + u * v[1], 0]
    return Arrow([O[0], O[1], 0], end, buff=0, color=color, stroke_width=w, max_tip_length_to_length_ratio=0.15)


class B02_Plane(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        O = (-1.8, -2.4); u = 0.8
        xax = Arrow([O[0], O[1], 0], [O[0] + 3.6, O[1], 0], buff=0, color=DIM, stroke_width=4, max_tip_length_to_length_ratio=0.06)
        yax = Arrow([O[0], O[1], 0], [O[0], O[1] + 5.0, 0], buff=0, color=DIM, stroke_width=4, max_tip_length_to_length_ratio=0.06)
        fl = T("furry", 48, DIM).move_to([O[0] + 1.8, O[1] - 0.65, 0])
        vl = T("vehicle", 48, DIM).move_to([O[0] + 0.95, 3.05, 0])
        self.play(Create(xax), Create(yax), FadeIn(fl), FadeIn(vl), run_time=1.2)
        items = [("cat", CAT, 0.30, 2.4), ("dog", DOG, 0.46, 1.7), ("car", CAR, 0.62, 1.0)]
        for name, v, frac, y in items:
            until(self, D, frac)
            a = arrow(O, v, u)
            tip = (O[0] + u * v[0], O[1] + u * v[1])
            lab = T(name, 48).move_to([tip[0] + 0.1, tip[1] + 0.6, 0])
            rd = T(f"{name} {int(v[0])}, {int(v[1])}", 48).move_to([0.8, y, 0])
            self.play(Create(a), FadeIn(lab), FadeIn(rd), run_time=0.9)
        finish(self, D)


class B03_Distance(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        O = (-1.8, -0.5); u = 0.3
        tip = lambda v: np.array([O[0] + u * v[0], O[1] + u * v[1], 0])
        a_cat = arrow(O, CAT, u)
        a_car = arrow(O, CAR, u)
        l_cat = T("cat", 48).move_to([tip(CAT)[0] + 0.1, tip(CAT)[1] - 0.6, 0])
        l_car = T("car", 48).move_to([tip(CAR)[0], tip(CAR)[1] + 0.65, 0])
        hd = VGroup(T("distance says", 48, DIM).move_to([0, 3.0, 0]), T("car is closer", 48, DIM).move_to([0, 2.4, 0]))
        self.play(Create(a_cat), Create(a_car), FadeIn(l_cat), FadeIn(l_car), run_time=1.2)
        until(self, D, 0.20)
        d1 = DashedLine(tip(CAT), tip(CAR), color=ACC, stroke_width=5)
        r1 = T("to car: 4.2", 48).move_to([0, -2.0, 0])
        self.play(Create(d1), FadeIn(r1), run_time=0.9)
        until(self, D, 0.34)
        c3 = tip(3 * CAT)
        a3 = arrow(O, 3 * CAT, u, DIM, 4)
        l3 = T("3 cats", 48, DIM).move_to([c3[0] - 0.8, c3[1] + 0.65, 0])
        self.play(Create(a3), FadeIn(l3), run_time=1.0)
        until(self, D, 0.44)
        off = np.array([0.0, -0.3, 0])
        d2 = DashedLine(tip(CAT) + off, c3 + off, color=ACC, stroke_width=5)
        r2 = T("to 3 cats: 8.2", 48).move_to([0, -2.8, 0])
        self.play(Create(d2), FadeIn(r2), run_time=0.9)
        until(self, D, 0.74)
        self.play(FadeIn(hd), run_time=0.6)
        finish(self, D)


class B04_Angle(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        O = (-1.8, -2.4); u = 0.8
        arrows = [("cat", CAT), ("dog", DOG), ("car", CAR)]
        grp = VGroup(*[arrow(O, v, u) for _, v in arrows])
        labs = VGroup(*[T(n, 48).move_to([O[0] + u * v[0] + 0.1, O[1] + u * v[1] + 0.6, 0]) for n, v in arrows])
        hd = T("angle from cat", 48, DIM).move_to([0, 3.05, 0])
        self.play(*[Create(a) for a in grp], FadeIn(labs), FadeIn(hd), run_time=1.3)
        th = lambda v: float(np.degrees(np.arctan2(v[1], v[0])))
        center = [O[0], O[1], 0]
        until(self, D, 0.34)
        arc1 = Arc(radius=1.3, start_angle=np.radians(th(CAT)), angle=np.radians(th(DOG) - th(CAT)), arc_center=center, color=INK, stroke_width=5)
        r1 = T("dog: 20°", 48).move_to([0.8, 2.2, 0])
        self.play(Create(arc1), FadeIn(r1), run_time=0.9)
        until(self, D, 0.54)
        arc2 = Arc(radius=1.9, start_angle=np.radians(th(CAT)), angle=np.radians(th(CAR) - th(CAT)), arc_center=center, color=ACC, stroke_width=5)
        r2 = T("car: 62°", 48).move_to([0.8, 1.5, 0])
        self.play(Create(arc2), FadeIn(r2), run_time=0.9)
        until(self, D, 0.78)
        ang = np.radians(th(CAT))
        ray = DashedLine(center, [O[0] + 3.7 * np.cos(ang), O[1] + 3.7 * np.sin(ang), 0], color=DIM, stroke_width=4)
        r3 = T("3 cats: 0°", 48).move_to([0.65, 0.8, 0])
        self.play(Create(ray), FadeIn(r3), run_time=0.9)
        finish(self, D)


class B05_Cosine(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        panel = RoundedRectangle(width=3.95, height=6.4, corner_radius=0.2, stroke_color=INK, stroke_width=3,
                                 fill_color=CARD, fill_opacity=1).move_to([0, 0, 0])
        e0 = _eq("eq0", 3.3).move_to([0, 2.1, 0])
        self.play(FadeIn(panel), FadeIn(e0), run_time=1.2)
        until(self, D, 0.40)
        e1 = _eq("eq1", 3.4).move_to([0, 0.8, 0])
        self.play(FadeIn(e1), run_time=1.0)
        until(self, D, 0.62)
        c1 = T("cat · dog = 14", 48, DIM).move_to([0, -0.5, 0])
        self.play(FadeIn(c1), run_time=0.6)
        until(self, D, 0.76)
        c2 = VGroup(T("same direction", 48, DIM), T("scores 1", 48, DIM)).arrange(DOWN, buff=0.1).move_to([0, -1.9, 0])
        box = SurroundingRectangle(e1, color=ACC, buff=0.15, stroke_width=4)
        self.play(FadeIn(c2), Create(box), run_time=0.7)
        finish(self, D)


def rows_portrait(scene, D, names, vals, y0, head, hi_idx, hi_frac):
    hd = T(head, 48, DIM).move_to([0, 3.0, 0])
    txt = VGroup(*[T(f"{n} {v:.2f}").move_to([0, y, 0]).align_to([L, 0, 0], LEFT) for n, v, y in zip(names, vals, y0)])
    ys = [y - 0.5 for y in y0]
    pre = VGroup(*[Rectangle(width=0.3, height=0.4).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.15, y, 0]) for y in ys])
    fin = VGroup(*[Rectangle(width=max(v * 3.8, 0.05), height=0.4).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + max(v * 3.8, 0.05) / 2, y, 0])
                   for v, y in zip(vals, ys)])
    scene.play(FadeIn(hd), FadeIn(txt), run_time=0.8)
    until(scene, D, 0.14)
    scene.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.6)
    scene.play(Transform(pre, fin), run_time=1.8)
    until(scene, D, hi_frac)
    hi = Rectangle(width=fin[hi_idx].width, height=0.55).set_fill(ACC, 1).set_stroke(DIM, 3).move_to(fin[hi_idx].get_center())
    scene.play(Transform(pre[hi_idx], hi), run_time=0.6)


class B06_Pairs(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        rows_portrait(self, D, ["cat, dog", "dog, car", "cat, car", "cat, 3x"], [0.9417, 0.7399, 0.4706, 1.0],
                      [2.0, 0.6, -0.8, -2.2], "cosine", 3, 0.84)
        finish(self, D)


class B07_Bites(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        y0 = [2.1, 0.2, -1.7]
        hd = T("cosine", 48, DIM).move_to([0, 3.0, 0])
        t1 = T("cat, dog 0.94").move_to([0, y0[0], 0]).align_to([L, 0, 0], LEFT)
        t2 = T("cat, 3x 1.00").move_to([0, y0[1], 0]).align_to([L, 0, 0], LEFT)
        t3 = T("cat, zeros").move_to([0, y0[2], 0]).align_to([L, 0, 0], LEFT)
        ys = [y - 0.6 for y in y0]
        pre = VGroup(*[Rectangle(width=0.3, height=0.6).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + 0.15, y, 0]) for y in ys[:2]])
        fin = VGroup(*[Rectangle(width=v * 3.8, height=0.6).set_fill(BAR, 1).set_stroke(DIM, 3).move_to([L + v * 3.8 / 2, y, 0])
                       for v, y in zip((0.9417, 1.0), ys[:2])])
        self.play(FadeIn(hd), FadeIn(t1), FadeIn(t2), run_time=0.8)
        until(self, D, 0.15)
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.6)
        self.play(Transform(pre, fin), run_time=1.6)
        until(self, D, 0.45)
        empty = Rectangle(width=3.8, height=0.6, color=DIM, stroke_width=3).move_to([L + 1.9, ys[2], 0])
        und = T("undefined", 48, ACC).move_to([0, -2.9, 0])
        self.play(FadeIn(t3), Create(empty), FadeIn(und), run_time=1.0)
        finish(self, D)
