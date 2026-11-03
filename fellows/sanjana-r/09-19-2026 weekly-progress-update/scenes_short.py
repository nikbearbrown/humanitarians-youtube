# -*- coding: utf-8 -*-
"""Portrait (9:16) dashboard scene for the Two-Week Progress Review SHORT.
Render at -r 2160,3840. Frame pinned to 9x16: x in [-4.5,4.5], y in [-8,8].
Numbers match scenes.py / the tracker (Sep 6-19)."""
import numpy as np
from manim import *

config.frame_width = 9.0
config.frame_height = 16.0

PAL = {"bg": "#FAF9F5", "ink": "#3D3929", "accent": "#D97757",
       "muted": "#B7AE9E", "good": "#4A7C59", "panel": "#EFEBE1", "line": "#8A8172"}

REVIEWED, UPLOADED, CHANGES, FELLOWS = 172, 119, 50, 38
WK1, WK2 = 87, 85


class S01_ShortDash(Scene):
    def construct(self):
        self.camera.background_color = PAL["bg"]

        eyebrow = Text("TWO-WEEK PROGRESS", font="DejaVu Sans", color=PAL["muted"],
                       font_size=30, weight=BOLD).move_to([0, 7.1, 0])
        big = Text("172", font="DejaVu Serif", color=PAL["accent"], weight=BOLD,
                   font_size=120).move_to([0, 5.4, 0])
        sub = Text("videos reviewed", font="DejaVu Sans", color=PAL["ink"],
                   font_size=40, weight=BOLD).move_to([0, 4.1, 0])
        self.play(FadeIn(eyebrow), FadeIn(big, scale=0.8), FadeIn(sub), run_time=1.1)
        self.wait(1.4)

        # KPI mini-cards
        cards = [("119", "uploaded", PAL["good"], -2.75),
                 ("50", "changes", PAL["accent"], 0.0),
                 ("38", "fellows", PAL["ink"], 2.75)]
        grp = VGroup()
        for val, lab, col, x in cards:
            box = RoundedRectangle(corner_radius=0.14, width=2.5, height=1.7,
                                   stroke_color=PAL["muted"], stroke_width=2,
                                   fill_color=PAL["panel"], fill_opacity=1.0).move_to([x, 2.3, 0])
            v = Text(val, font="DejaVu Serif", color=col, weight=BOLD,
                     font_size=52).move_to([x, 2.55, 0])
            l = Text(lab, font="DejaVu Sans", color=PAL["muted"],
                     font_size=24).move_to([x, 1.65, 0])
            grp.add(box, v, l)
        self.play(FadeIn(grp, shift=UP * 0.15), run_time=0.8)
        self.wait(1.8)

        # week bars
        base_y, maxh, m = -3.4, 3.0, max(WK1, WK2)
        def bar(x, val, col, top, subl):
            h = maxh * val / m
            r = Rectangle(width=1.9, height=h, stroke_width=0, fill_color=col,
                          fill_opacity=0.9).move_to([x, base_y + h / 2, 0])
            v = Text(str(val), font="DejaVu Serif", color=col, weight=BOLD,
                     font_size=50).next_to(r, UP, buff=0.15)
            t = Text(top, font="DejaVu Sans", color=PAL["ink"], font_size=30,
                     weight=BOLD).move_to([x, base_y - 0.45, 0])
            s = Text(subl, font="DejaVu Sans", color=PAL["muted"],
                     font_size=23).move_to([x, base_y - 1.0, 0])
            return VGroup(r, v, t, s)
        base = Line([-3.4, base_y, 0], [3.4, base_y, 0], color=PAL["ink"], stroke_width=3)
        w1 = bar(-1.7, WK1, PAL["line"], "Week 1", "other projects")
        w2 = bar(1.7, WK2, PAL["accent"], "Week 2", "Mycroft")
        self.play(Create(base), run_time=0.3)
        self.play(GrowFromEdge(w1[0], DOWN), FadeIn(w1[1:]),
                  GrowFromEdge(w2[0], DOWN), FadeIn(w2[1:]), run_time=1.0)
        self.wait(1.6)

        foot = Text("one week Mycroft, the next other projects", font="DejaVu Sans",
                    color=PAL["ink"], font_size=30, weight=BOLD).move_to([0, -6.7, 0])
        self.play(FadeIn(foot), run_time=0.6)
        self.wait(2.0)
