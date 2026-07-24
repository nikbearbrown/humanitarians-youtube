"""
scenes.py — doodle scenes for claude-liam-troubleshooting
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


class B05Doodle(Scene):
    """Reveal doodle — Credentials go stale (13.8s)"""
    def construct(self):
        headline = 'Credentials go stale'
        body     = "A service that won't authenticate almost always means stale credential"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Credentials go stale', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(10.3)


class B11Doodle(Scene):
    """Reveal doodle — Isolate by shrinking (9.3s)"""
    def construct(self):
        headline = 'Isolate by shrinking'
        body     = 'That third step carries more than its size. Shrink the request until i'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Isolate by shrinking', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.8)


class B12Doodle(Scene):
    """Reveal doodle — Nothing sits still (12.99s)"""
    def construct(self):
        headline = 'Nothing sits still'
        body     = "Plugins don't sit still. Anthropic improves the official ones; communi"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Nothing sits still', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(9.5)


class B15Doodle(Scene):
    """Reveal doodle — A monthly habit (10.99s)"""
    def construct(self):
        headline = 'A monthly habit'
        body     = 'Make it a habit. Set a monthly reminder to browse the directory and se'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('A monthly habit', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.5)


class B16Doodle(Scene):
    """Reveal doodle — The model persists (9.69s)"""
    def construct(self):
        headline = 'The model persists'
        body     = "Because that's the real skill here. Not memorizing today's menus — but"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('The model persists', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.2)

