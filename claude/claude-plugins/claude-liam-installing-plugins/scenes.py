"""
scenes.py — doodle scenes for claude-liam-installing-plugins
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


class B04Doodle(Scene):
    """Reveal doodle — Shared plugins upload too (10.97s)"""
    def construct(self):
        headline = 'Shared plugins upload too'
        body     = "Someone shares a plugin — a colleague's workflow, a community creation"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Shared plugins upload too', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.5)


class B08Doodle(Scene):
    """Reveal doodle — Your call, your depth (11.75s)"""
    def construct(self):
        headline = 'Your call, your depth'
        body     = 'How far you take it is your call. Install and run the defaults — fine,'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Your call, your depth', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.2)


class B10Doodle(Scene):
    """Reveal doodle — This is the studio (10.6s)"""
    def construct(self):
        headline = 'This is the studio'
        body     = 'This is the studio — one person, a few screens, real clients waiting o'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('This is the studio', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.1)


class B11Doodle(Scene):
    """Reveal doodle — And these are the clients (10.41s)"""
    def construct(self):
        headline = 'And these are the clients'
        body     = 'And these are the clients it now understands — accountants, lawyers, f'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('And these are the clients', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.9)


class B17Doodle(Scene):
    """Reveal doodle — Authorize, then reach (10.56s)"""
    def construct(self):
        headline = 'Authorize, then reach'
        body     = 'Connecting is the standard login flow — authorize access the same way '
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Authorize, then reach', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.1)


class B21Doodle(Scene):
    """Reveal doodle — Local to your machine (11.16s)"""
    def construct(self):
        headline = 'Local to your machine'
        body     = 'One catch worth knowing: your plugins and everything you taught them l'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Local to your machine', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.7)

