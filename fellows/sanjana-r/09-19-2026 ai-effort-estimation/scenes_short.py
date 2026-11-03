# -*- coding: utf-8 -*-
"""Portrait (9:16) Manim scene for the AI Effort Estimation SHORT.
Render at -r 2160,3840. We PIN the coordinate frame to 9x16 so the layout
fills the tall canvas deterministically: x in [-4.5, 4.5], y in [-8, 8].
Numbers match estimate.py / scenes.py in the 16:9 long."""
import numpy as np
from manim import *

config.frame_width = 9.0
config.frame_height = 16.0

PALETTE = {"bg": "#FAF9F5", "ink": "#3D3929", "accent": "#D97757",
           "muted": "#B7AE9E", "good": "#4A7C59", "panel": "#EFEBE1"}

CLASSES = {
    "integration": [4, 6, 7, 9, 14],
    "ui_form":     [1, 2, 2, 3],
    "crud":        [2, 3, 3, 4, 6],
}
VELOCITY = 1.15
TASKS = [
    ("OAuth login",     "integration", 5),
    ("Settings page",   "ui_form",     2),
    ("Export endpoint", "crud",        3),
]
def rng_of(cls):
    a = np.array(CLASSES[cls], float)
    p50, p80 = np.percentile(a, [50, 80]) * VELOCITY
    return round(float(p50), 1), round(float(p80), 1)
GUT_TOTAL = sum(g for _, _, g in TASKS)
P80_TOTAL = sum(rng_of(c)[1] for _, c, _ in TASKS)

# per-row track spanning days 0..16 across the portrait width
XL, XW, DAY_MAX = -3.7, 7.4, 16.0
def x_of(day):
    return XL + (day / DAY_MAX) * XW


class S01_ShortRanges(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        eyebrow = Text("AI EFFORT ESTIMATION", font="DejaVu Sans",
                       color=PALETTE["muted"], font_size=30, weight=BOLD).move_to([0, 7.0, 0])
        title = Text("Your estimate\nis too optimistic.", font="DejaVu Serif",
                     color=PALETTE["ink"], font_size=62, weight=BOLD,
                     line_spacing=0.9).move_to([0, 5.3, 0])
        self.play(FadeIn(eyebrow), Write(title), run_time=1.2)
        self.wait(0.8)

        # gridlines for reference
        grid = VGroup()
        for d in (5, 10, 15):
            grid.add(DashedLine([x_of(d), 3.0, 0], [x_of(d), -3.4, 0],
                                color=PALETTE["muted"], stroke_width=1.4,
                                dash_length=0.08).set_opacity(0.5))
            grid.add(Text(str(d), font="DejaVu Sans", color=PALETTE["muted"],
                          font_size=26).move_to([x_of(d), -3.9, 0]))
        grid.add(Text("days", font="DejaVu Sans", color=PALETTE["muted"],
                      font_size=26).move_to([x_of(16) + 0.3, -3.9, 0]))
        self.play(FadeIn(grid), run_time=0.6)

        ys = [2.2, 0.4, -1.4]
        for (name, cls, gut), y in zip(TASKS, ys):
            p50, p80 = rng_of(cls)
            nm = Text(name, font="DejaVu Sans", color=PALETTE["ink"],
                      font_size=34, weight=BOLD).move_to([0, y + 0.95, 0])
            band = Rectangle(width=x_of(p80) - x_of(p50), height=0.5,
                             stroke_width=0, fill_color=PALETTE["accent"],
                             fill_opacity=0.78)
            band.move_to([(x_of(p50) + x_of(p80)) / 2, y, 0])
            rlbl = Text(f"{p50:.1f}-{p80:.1f}", font="DejaVu Sans",
                        color=PALETTE["accent"], font_size=30,
                        weight=BOLD).next_to(band, RIGHT, buff=0.2)
            gdot = Dot([x_of(gut), y, 0], radius=0.16, color=PALETTE["ink"])
            gtxt = Text(f"gut {gut}", font="DejaVu Sans", color=PALETTE["ink"],
                        font_size=26).next_to(gdot, DOWN, buff=0.12)
            self.play(FadeIn(nm), run_time=0.3)
            self.play(GrowFromEdge(band, LEFT), FadeIn(rlbl),
                      GrowFromCenter(gdot), FadeIn(gtxt), run_time=0.7)
            self.wait(1.2)

        punch = VGroup(
            Text(f"gut {GUT_TOTAL}", font="DejaVu Serif", color=PALETTE["muted"],
                 font_size=52, weight=BOLD),
            Text("->", font="DejaVu Sans", color=PALETTE["ink"],
                 font_size=52, weight=BOLD),
            Text(f"honest ~{P80_TOTAL:.0f}", font="DejaVu Serif", color=PALETTE["accent"],
                 font_size=52, weight=BOLD),
        ).arrange(RIGHT, buff=0.35).move_to([0, -5.6, 0])
        sub = Text("estimate from history, report a range", font="DejaVu Sans",
                   color=PALETTE["ink"], font_size=32, weight=BOLD).move_to([0, -6.5, 0])
        self.play(FadeIn(punch, shift=UP * 0.25), run_time=0.9)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(2.2)
