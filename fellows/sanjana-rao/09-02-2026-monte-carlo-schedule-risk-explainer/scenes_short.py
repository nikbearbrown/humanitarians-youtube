# -*- coding: utf-8 -*-
"""Portrait (9:16) Manim scene for the Monte Carlo schedule-risk SHORT.
Render at -r 2160,3840. We PIN the coordinate frame to 9x16 so the layout
fills the tall canvas deterministically: x in [-4.5, 4.5], y in [-8, 8]."""
import numpy as np
from manim import *

config.frame_width = 9.0
config.frame_height = 16.0

PALETTE = {"bg": "#FAF9F5", "ink": "#3D3929", "accent": "#D97757",
           "muted": "#B7AE9E", "good": "#4A7C59", "panel": "#EFEBE1"}

np.random.seed(42)
_N = 60000
_d  = np.random.triangular(3, 5, 12, _N)
_be = np.random.triangular(5, 8, 20, _N)
_fe = np.random.triangular(4, 7, 16, _N)
_t  = np.random.triangular(2, 4, 10, _N)
_r  = np.random.triangular(1, 2,  5, _N)
V1 = _d + _be + _t + _r
PLAN = 19

DMIN, DMAX = 12, 40
XL, XW = -3.9, 7.8          # fill the width
BASE = -2.2
MAXH = 4.0                  # tall histogram, kept clear of the title

def x_of(day):
    return XL + (day - DMIN) / (DMAX - DMIN) * XW

def hist(data, color, opacity=0.85):
    counts, edges = np.histogram(data, bins=np.arange(DMIN, DMAX + 1, 1))
    m = counts.max()
    bw = (XW / (DMAX - DMIN)) * 0.9
    g = VGroup()
    for c, left in zip(counts, edges[:-1]):
        h = max((c / m) * MAXH, 0.001)
        b = Rectangle(width=bw, height=h, stroke_width=0,
                      fill_color=color, fill_opacity=opacity)
        b.move_to([x_of(left + 0.5), BASE + h / 2, 0])
        g.add(b)
    return g


class S01_ShortHist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        eyebrow = Text("MONTE CARLO SCHEDULE RISK", font="DejaVu Sans",
                       color=PALETTE["muted"], font_size=30, weight=BOLD).move_to([0, 7.0, 0])
        title = Text("Your deadline\nis a guess.", font="DejaVu Serif",
                     color=PALETTE["ink"], font_size=70, weight=BOLD,
                     line_spacing=0.9).move_to([0, 5.4, 0])
        self.play(FadeIn(eyebrow), Write(title), run_time=1.2)
        self.wait(0.8)

        ax = Line([XL - 0.2, BASE, 0], [XL + XW + 0.2, BASE, 0],
                  color=PALETTE["ink"], stroke_width=4)
        cap = Text("project finish (days)", font="DejaVu Sans", color=PALETTE["muted"],
                   font_size=30).next_to(ax, DOWN, buff=0.35)
        self.play(Create(ax), FadeIn(cap), run_time=0.7)

        bars = hist(V1, PALETTE["accent"], 0.85)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                              lag_ratio=0.02, run_time=4.2))
        self.wait(2.0)

        px = x_of(PLAN)
        pl = DashedLine([px, BASE, 0], [px, BASE + MAXH + 0.3, 0],
                        color=PALETTE["ink"], stroke_width=6)
        plt = Text("plan 19", font="DejaVu Sans", color=PALETTE["ink"],
                   font_size=34, weight=BOLD)
        plt.next_to([px, BASE + MAXH + 0.3, 0], UP, buff=0.12).shift(LEFT * 0.9)
        self.play(Create(pl), FadeIn(plt), run_time=0.7)
        self.wait(2.6)

        p80 = float(np.percentile(V1, 80))
        bx = x_of(p80)
        bl = Line([bx, BASE, 0], [bx, BASE + MAXH + 0.3, 0],
                  color=PALETTE["accent"], stroke_width=7)
        blt = Text(f"P80  {p80:.0f}", font="DejaVu Sans", color=PALETTE["accent"],
                   font_size=38, weight=BOLD)
        blt.next_to([bx, BASE + MAXH + 0.3, 0], UP, buff=0.12).shift(RIGHT * 0.9)
        self.play(Create(bl), FadeIn(blt), run_time=0.8)
        self.wait(3.0)

        punch = Text("simulate it 10,000x\nand commit to the P80",
                     font="DejaVu Sans", color=PALETTE["ink"], font_size=46,
                     weight=BOLD, line_spacing=0.95).move_to([0, -5.4, 0])
        self.play(FadeIn(punch, shift=UP * 0.25), run_time=0.9)
        self.wait(2.2)
