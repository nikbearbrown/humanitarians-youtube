"""
scenes.py — doodle scenes for claude-liam-productivity
Auto-generated VOX→MANIM doodles. All scenes: 1920x1080, 24fps, cream bg.
"""
from manim import *

CREAM   = "#F2F0E9"
INK     = "#3D3929"
SPARK   = "#D97757"
INK_DIM = "#8A8575"
SANS    = "SF Pro Display"

config.background_color = CREAM
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 24

def ink_text(s, size=36, weight=NORMAL, color=INK):
    return Text(s, font=SANS, font_size=size, weight=weight, color=color,
                disable_ligatures=True)

def ink_rect(w, h, color=INK, fill=CREAM, fill_opacity=1.0, stroke_width=3):
    return RoundedRectangle(corner_radius=0.15, width=w, height=h,
                            stroke_color=color, stroke_width=stroke_width,
                            fill_color=fill, fill_opacity=fill_opacity)


class B06Doodle(Scene):
    """Flow doodle — Scattered → summary (10.9s)"""
    def construct(self):
        steps = ['Scattered', 'summary']
        boxes, arrows = [], []
        start_x = -(len(steps)-1)*1.8
        for i, s in enumerate(steps):
            b = ink_rect(2.8, 0.85).move_to(RIGHT*(start_x + i*3.6))
            l = ink_text(s, 26).move_to(b)
            boxes.append(VGroup(b, l))
        for i in range(len(steps)-1):
            a = Arrow(RIGHT*(start_x+i*3.6+1.4), RIGHT*(start_x+(i+1)*3.6-1.4),
                      buff=0, color=SPARK, stroke_width=3, tip_length=0.2)
            arrows.append(a)
        spark = ink_text('Scattered → summary', 28, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for b in boxes:
            self.play(Create(b), run_time=0.6)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.4)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(7.4)


class B11Doodle(Scene):
    """Reveal doodle — First thing, ask (6.76s)"""
    def construct(self):
        headline = 'First thing, ask'
        body     = 'Picture the first move of the day. Before the tabs, before the noise —'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('First thing, ask', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(3.3)


class B14Doodle(Scene):
    """Contrast doodle — Prep before the room (9.3s)"""
    def construct(self):
        left_lbl, right_lbl = 'Second Workflow', 'Before A Meeting That '
        l_box = ink_rect(3.6, 2.4, fill=CREAM).move_to(LEFT*3.2)
        l_txt = ink_text(left_lbl, 28, color=INK_DIM).move_to(LEFT*3.2).scale(0.95)
        r_box = ink_rect(3.6, 2.4, color=SPARK, fill="#FFF8F5").move_to(RIGHT*3.2)
        r_txt = ink_text(right_lbl, 28, BOLD, INK).move_to(RIGHT*3.2).scale(0.95)
        vs = ink_text("→", 52, BOLD, SPARK).move_to(ORIGIN)
        spark = ink_text('Prep before the room', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Create(l_box), Write(l_txt), run_time=0.8)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(r_box), Write(r_txt), run_time=0.8)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(5.8)


class B15Doodle(Scene):
    """Reveal doodle — Walk in ready (9.28s)"""
    def construct(self):
        headline = 'Walk in ready'
        body     = 'You walk in already knowing who they are, what they want, and what to '
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Walk in ready', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.8)


class B17Doodle(Scene):
    """Reveal doodle — Capture, don't switch (10.82s)"""
    def construct(self):
        headline = "Capture, don't switch"
        body     = 'And the small one that saves you daily: capture without breaking flow.'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text("Capture, don't switch", 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.3)


class B23Doodle(Scene):
    """Reveal doodle — A tidy desk (8.04s)"""
    def construct(self):
        headline = 'A tidy desk'
        body     = "In practice it feels less like an app and more like a desk that's alre"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('A tidy desk', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(4.5)

