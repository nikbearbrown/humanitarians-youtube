"""scenes.py — Manim body beats B02–B07 for claude-liam-convolution.

6x6 image with rows [0,0,0,9,9,9], 3x3 kernel with rows [-1,0,1]. Every number comes from
experiment_output.txt (recomputed here). Each scene stretches to its beat's measured audio and
holds across the 45-55% midpoint.
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
_FALLBACK = {"B02": 11.12, "B03": 12.42, "B04": 13.76, "B05": 9.79, "B06": 16.38, "B07": 10.56}


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


IMG = np.array([[0, 0, 0, 9, 9, 9]] * 6)
KER = np.array([[-1, 0, 1]] * 3)
CELL = 0.8
IMG_C = (-3.6, 0.3)


def grid(vals, cx, cy, cell, fill_fn, texts=True):
    n, m = vals.shape
    rects, txt = VGroup(), VGroup()
    for i in range(n):
        for j in range(m):
            x = cx + (j - (m - 1) / 2) * cell
            y = cy - (i - (n - 1) / 2) * cell
            r = Rectangle(width=cell, height=cell).set_fill(fill_fn(vals[i, j]), 1).set_stroke(DIM, 2)
            r.move_to([x, y, 0])
            rects.add(r)
            if texts:
                t = Text(("−" if vals[i, j] < 0 else "") + str(abs(int(vals[i, j]))), font=FONT, font_size=48, color=INK)
                t.move_to([x, y, 0])
                txt.add(t)
    return rects, txt


img_fill = lambda v: BAR if v == 0 else CARD
ker_fill = lambda v: CARD
KER_C = (3.0, 1.2)
OUT_Y = -2.0


def window(col, row=0, cx=IMG_C[0], cy=IMG_C[1], cell=CELL):
    x = cx + (col - 2.5 + 1.0) * cell
    y = cy - (row - 2.5 + 1.0) * cell
    return Rectangle(width=3 * cell, height=3 * cell, color=ACC, stroke_width=7).move_to([x, y, 0])


def conv_val(col, row=0):
    return int(np.sum(IMG[row:row + 3, col:col + 3] * KER))


# ═════════════════════════════════════════════════════════════════════════════
class B02_Image(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B02")
        ir, it = grid(IMG, IMG_C[0], IMG_C[1], CELL, img_fill)
        self.play(FadeIn(ir), FadeIn(it), run_time=1.4)
        until(self, D, 0.18)
        kr, kt = grid(KER, KER_C[0], KER_C[1], 0.9, ker_fill)
        lab = T("kernel", 48, DIM).move_to([5.3, KER_C[1], 0])
        self.play(FadeIn(kr), FadeIn(kt), FadeIn(lab), run_time=0.8)
        until(self, D, 0.45)
        ex = IMG_C[0] - 3 * CELL + 3 * CELL
        edge = DashedLine([ex, IMG_C[1] + 2.4, 0], [ex, IMG_C[1] - 2.4, 0], color=ACC, stroke_width=6)
        self.play(Create(edge), run_time=0.8)
        until(self, D, 0.72)
        cap = T("edge", 48, ACC).move_to([-3.6, 3.0, 0])
        self.play(FadeIn(cap), run_time=0.6)
        finish(self, D)


class B03_Window(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B03")
        ir, it = grid(IMG, IMG_C[0], IMG_C[1], CELL, img_fill)
        kr, kt = grid(KER, KER_C[0], KER_C[1], 0.9, ker_fill)
        lab = T("kernel", 48, DIM).move_to([5.3, KER_C[1], 0])
        self.add(ir, it, kr, kt, lab)
        self.wait(0.3)
        colbox = Rectangle(width=0.9, height=2.7, color=INK, stroke_width=6).move_to([KER_C[0] - 0.9, KER_C[1], 0])
        until(self, D, 0.12)
        self.play(Create(colbox), run_time=0.5)
        self.play(Transform(colbox, Rectangle(width=0.9, height=2.7, color=INK, stroke_width=6).move_to([KER_C[0], KER_C[1], 0])), run_time=0.6)
        self.play(Transform(colbox, Rectangle(width=0.9, height=2.7, color=INK, stroke_width=6).move_to([KER_C[0] + 0.9, KER_C[1], 0])), run_time=0.6)
        until(self, D, 0.46)
        w = window(0)
        self.play(Create(w), run_time=0.8)
        until(self, D, 0.78)
        ro = T("sum = 0", 52).move_to([KER_C[0], -0.7, 0])
        self.play(FadeIn(ro), run_time=0.6)
        finish(self, D)


class B04_Slide(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B04")
        ir, it = grid(IMG, IMG_C[0], IMG_C[1], CELL, img_fill)
        kr, kt = grid(KER, KER_C[0], KER_C[1], 0.9, ker_fill)
        lab = T("kernel", 48, DIM).move_to([5.3, KER_C[1], 0])
        w = window(0)
        ro = T("sum = 0", 52).move_to([KER_C[0], -0.7, 0])
        self.add(ir, it, kr, kt, lab, w, ro)
        out_cells = []
        for k in range(4):
            r = Rectangle(width=1.0, height=0.8).set_fill(CARD, 1).set_stroke(DIM, 2).move_to([1.5 + k, OUT_Y, 0])
            t = T(str(conv_val(k)), 48).move_to([1.5 + k, OUT_Y, 0])
            out_cells.append((r, t))
        olab = T("output", 48, DIM).move_to([3.0, -3.0, 0])
        self.play(FadeIn(out_cells[0][0]), FadeIn(out_cells[0][1]), FadeIn(olab), run_time=0.6)
        times = [0.18, 0.40, 0.62]
        for k in (1, 2, 3):
            until(self, D, times[k - 1])
            ro2 = T(f"sum = {conv_val(k)}", 52).move_to([KER_C[0], -0.7, 0])
            self.play(Transform(w, window(k)), FadeTransform(ro, ro2), run_time=0.9)
            ro = ro2
            self.play(FadeIn(out_cells[k][0]), FadeIn(out_cells[k][1]), run_time=0.4)
        until(self, D, 0.86)
        out_cells[1][0].set_fill(ACC, 1)
        out_cells[2][0].set_fill(ACC, 1)
        finish(self, D)


class B05_Map(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B05")
        ir, it = grid(IMG, IMG_C[0], IMG_C[1], CELL, img_fill)
        out = np.array([[0, 27, 27, 0]] * 4)
        orr, ot = grid(out, 3.4, 0.3, 0.9, lambda v: CARD)
        olab = T("output", 48, DIM).move_to([3.4, -2.3, 0])
        self.add(ir, it)
        self.wait(0.4)
        until(self, D, 0.15)
        self.play(FadeIn(orr), FadeIn(ot), FadeIn(olab), run_time=1.2)
        until(self, D, 0.66)
        hi = VGroup(*[Rectangle(width=0.9, height=0.9).set_fill(ACC, 1).set_stroke(DIM, 2).move_to(orr[i * 4 + j].get_center())
                      for i in range(4) for j in (1, 2)])
        self.play(Transform(VGroup(*[orr[i * 4 + j] for i in range(4) for j in (1, 2)]), hi), run_time=0.8)
        finish(self, D)


class B06_Share(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B06")
        S = 7.5 / 576.0
        rows = [("connect all", 576, 1.3), ("one kernel", 9, -0.4)]
        labs = VGroup(*[T(n).move_to([0, y, 0]).align_to([-6.2, 0, 0], LEFT) for n, _, y in rows])
        bars = VGroup()
        for _, n, y in rows:
            w = max(n * S, 0.05)
            r = Rectangle(width=w, height=1.1).set_fill(BAR, 1).set_stroke(DIM, 3)
            r.move_to([-2.8 + w / 2, y, 0])
            bars.add(r)
        vals = VGroup(*[T(str(n)).next_to(r, RIGHT, buff=0.25) for (_, n, _), r in zip(rows, bars)])
        head = T("weights", 48, DIM).move_to([0, 3.0, 0])
        self.play(FadeIn(head), FadeIn(labs), run_time=0.8)
        until(self, D, 0.14)
        pre = VGroup(*[Rectangle(width=0.2, height=1.1).set_fill(BAR, 1).set_stroke(DIM, 2).move_to([-2.7, y, 0]) for _, _, y in rows])
        self.play(*[GrowFromEdge(r, LEFT) for r in pre], run_time=0.6)
        self.play(Transform(pre, bars), FadeIn(vals), run_time=1.8)
        until(self, D, 0.50)
        r = T("edge moved left → 27, 0, 0, 0", 48).move_to([0, -2.3, 0])
        self.play(FadeIn(r), pre[1].animate.set_fill(ACC, 1), run_time=0.8)
        finish(self, D)


class B07_Shrink(Scene):
    def construct(self):
        self.camera.background_color = BG
        D = _D("B07")
        def g(n):
            rr, _ = grid(np.zeros((n, n), dtype=int), -3.4, 0.0, 0.9, lambda v: BAR, texts=False)
            return rr
        g6, g4, g2 = g(6), g(4), g(2)
        frame = Rectangle(width=5.4, height=5.4, color=DIM, stroke_width=3).move_to([-3.4, 0.0, 0])
        r1 = T("6 by 6", 56).move_to([3.5, 1.4, 0])
        self.play(FadeIn(g6), FadeIn(r1), Create(frame), run_time=1.0)
        until(self, D, 0.28)
        r2 = T("4 by 4", 56).move_to([3.5, 1.4, 0])
        self.play(Transform(g6, g4), FadeTransform(r1, r2), run_time=1.2)
        until(self, D, 0.50)
        r3 = T("2 by 2", 56).move_to([3.5, 1.4, 0])
        self.play(Transform(g6, g2), FadeTransform(r2, r3), run_time=1.2)
        until(self, D, 0.72)
        n1 = T("next kernel: no room", 48).move_to([3.3, 0.0, 0])
        self.play(FadeIn(n1), run_time=0.6)
        until(self, D, 0.88)
        n2 = T("padding keeps 6", 48, DIM).move_to([3.3, -1.0, 0])
        self.play(FadeIn(n2), run_time=0.6)
        finish(self, D)
