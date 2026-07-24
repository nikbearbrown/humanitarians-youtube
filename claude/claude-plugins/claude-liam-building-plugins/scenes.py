"""
scenes.py — doodle scenes for claude-liam-building-plugins
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


class B03Doodle(Scene):
    """Reveal doodle — You are the business (9.11s)"""
    def construct(self):
        headline = 'You are the business'
        body     = 'This matters most when you are the business. The solo operator wears e'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('You are the business', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.6)


class B04Doodle(Scene):
    """Reveal doodle — Lift it out (8.81s)"""
    def construct(self):
        headline = 'Lift it out'
        body     = 'The expertise lives in one head. A custom plugin draws it out and make'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Lift it out', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.3)


class B08Doodle(Scene):
    """Reveal doodle — Expertise, written down (12.27s)"""
    def construct(self):
        headline = 'Expertise, written down'
        body     = 'Skills are the expertise itself — your proposal structure, your pricin'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Expertise, written down', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.8)


class B13Doodle(Scene):
    """Reveal doodle — Describe it aloud (12.39s)"""
    def construct(self):
        headline = 'Describe it aloud'
        body     = 'You describe the workflow in plain language. When I sign a new client,'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Describe it aloud', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.9)


class B18Doodle(Scene):
    """Reveal doodle — Hand this off (11.03s)"""
    def construct(self):
        headline = 'Hand this off'
        body     = 'That last phrase — I just wish I could hand this off — is usually a pl'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Hand this off', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.5)


class B23Doodle(Scene):
    """Reveal doodle — Expertise, shared (10.86s)"""
    def construct(self):
        headline = 'Expertise, shared'
        body     = "That's the quiet upside of a file-based tool. The way you've refined a"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Expertise, shared', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.4)

