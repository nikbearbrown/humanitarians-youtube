# -*- coding: utf-8 -*-
"""Portrait (9:16) Manim scenes for the "The Risk Register" SHORT.
Render at -r 2160,3840. Frame pinned 9x16; content inside x[-4.1,4.1] y[-7.6,7.6].
"""
from manim import *

config.frame_width = 9.0
config.frame_height = 16.0
PALETTE = {"bg": "#FAF9F5", "ink": "#3D3929", "accent": "#D97757", "muted": "#B7AE9E",
           "good": "#4A7C59", "red": "#A44A32", "panel": "#EFEBE1"}
SERIF, SANS = "DejaVu Serif", "DejaVu Sans"


def check_mark(color=PALETTE["good"], scale=1.0):
    v = VMobject(stroke_color=color, stroke_width=9)
    v.set_points_as_corners([[-0.2, 0.02, 0], [-0.04, -0.18, 0], [0.26, 0.24, 0]])
    return v.scale(scale)


class S01_ScoreOwnWatch(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        eyebrow = Text("THE RISK REGISTER", font=SANS, color=PALETTE["muted"],
                       font_size=32, weight=BOLD).move_to([0, 7.0, 0])
        title = Text("Score. Own.\nWatch.", font=SERIF, color=PALETTE["ink"],
                     font_size=60, weight=BOLD, line_spacing=0.9).move_to([0, 5.3, 0])
        self.play(FadeIn(eyebrow), Write(title), run_time=1.3)
        self.wait(0.3)

        rows = [("SCORE", "AI rates the known risks", PALETTE["good"]),
                ("OWN", "you add the risk AI can't see", PALETTE["accent"]),
                ("WATCH", "each risk: a trigger + an owner", PALETTE["ink"])]
        ys = [3.0, 1.5, 0.0]
        for (word, desc, col), y in zip(rows, ys):
            w = Text(word, font=SANS, color=col, font_size=46, weight=BOLD).move_to([0, y + 0.45, 0])
            d = Text(desc, font=SANS, color=PALETTE["ink"], font_size=28).move_to([0, y - 0.32, 0])
            self.play(FadeIn(w, shift=UP * 0.1), run_time=0.35)
            self.play(FadeIn(d), run_time=0.35)
            self.wait(0.5)

        rule = Text("a register nobody watches\nis just a list", font=SANS,
                    color=PALETTE["accent"], font_size=35, weight=BOLD,
                    line_spacing=0.9).move_to([0, -2.3, 0])
        punch = Text("the AI fills the grid.\nyou find what's off it.", font=SERIF,
                     color=PALETTE["ink"], font_size=44, weight=BOLD,
                     line_spacing=0.9).move_to([0, -4.6, 0])
        last = Text("score the known -\nown the specific", font=SANS, color=PALETTE["muted"],
                    font_size=27, line_spacing=0.9).move_to([0, -6.4, 0])
        self.play(FadeIn(rule, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(punch, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(last), run_time=0.6)
        self.wait(3.2)
        self.play(Indicate(punch, color=PALETTE["accent"], scale_factor=1.05), run_time=0.6)
        self.wait(6.4)


class S03_Outro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        eyebrow = Text("HUMANITARIANS AI  FELLOWS", font=SANS, color=PALETTE["muted"],
                       font_size=30, weight=BOLD).move_to([0, 4.6, 0])
        title = VGroup(
            Text("The Risk", font=SERIF, color=PALETTE["ink"], font_size=80, weight=BOLD),
            VGroup(
                Text("Register", font=SERIF, color=PALETTE["ink"], font_size=80, weight=BOLD),
                Text(".", font=SERIF, color=PALETTE["accent"], font_size=80, weight=BOLD),
            ).arrange(RIGHT, buff=0.03),
        ).arrange(DOWN, buff=0.25).move_to([0, 2.3, 0])
        rule = Line([-3.6, 0, 0], [3.6, 0, 0], color=PALETTE["accent"],
                    stroke_width=4).move_to([0, 0.1, 0])
        handle = Text("@HumanitariansAI", font=SANS, color=PALETTE["accent"],
                      font_size=50, weight=BOLD).move_to([0, -1.2, 0])
        sub = Text("with Sanjana Rao", font=SANS, color=PALETTE["ink"],
                   font_size=38, weight=BOLD).move_to([0, -2.5, 0])
        tag = Text("Score. Own. Watch.", font=SERIF, color=PALETTE["muted"],
                   font_size=40).move_to([0, -4.4, 0])
        self.play(FadeIn(eyebrow, shift=DOWN * 0.12), FadeIn(title, shift=UP * 0.1), run_time=1.0)
        self.play(Create(rule), FadeIn(handle, shift=UP * 0.12), FadeIn(sub),
                  FadeIn(tag, shift=UP * 0.1), run_time=0.8)
        self.wait(3.7)
