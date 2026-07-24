"""
scenes.py — doodle scenes for claude-liam-sales
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
    """Reveal doodle — At the table (8.83s)"""
    def construct(self):
        headline = 'At the table'
        body     = "Picture the freelancer at the kitchen table with a lead they don't kno"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('At the table', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.3)


class B12Doodle(Scene):
    """Reveal doodle — In the room (8.41s)"""
    def construct(self):
        headline = 'In the room'
        body     = "Now you're in the room. Present, not scrambling — because the research"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('In the room', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(4.9)


class B13Doodle(Scene):
    """List doodle — Capture it fresh (10.13s)"""
    def construct(self):
        items = ["The call ends. while it's fresh,", 'Their timeline, their real conce']
        group = VGroup()
        for i, it in enumerate(items):
            dot = Dot(radius=0.1, color=SPARK).shift(LEFT*3.5 + DOWN*(i*0.85 - (len(items)-1)*0.425))
            txt = ink_text(it, 30).next_to(dot, RIGHT, buff=0.3).align_to(dot, UP).shift(DOWN*0.04)
            group.add(dot, txt)
        spark = ink_text('Capture it fresh', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for i in range(0, len(group), 2):
            self.play(FadeIn(group[i]), Write(group[i+1]), run_time=0.55)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(6.6)


class B18Doodle(Scene):
    """Reveal doodle — Honest, no manager (7.57s)"""
    def construct(self):
        headline = 'Honest, no manager'
        body     = "It's like having a sales manager who keeps you honest about follow-thr"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Honest, no manager', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(4.1)


class B22Doodle(Scene):
    """Reveal doodle — Be present (9.71s)"""
    def construct(self):
        headline = 'Be present'
        body     = "But don't let it automate the relationship. It's excellent at preparat"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Be present', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.2)


class B24Doodle(Scene):
    """List doodle — Keep it current (9.92s)"""
    def construct(self):
        items = ['And keep your notes current. it ', 'Sparse notes make sparse briefin']
        group = VGroup()
        for i, it in enumerate(items):
            dot = Dot(radius=0.1, color=SPARK).shift(LEFT*3.5 + DOWN*(i*0.85 - (len(items)-1)*0.425))
            txt = ink_text(it, 30).next_to(dot, RIGHT, buff=0.3).align_to(dot, UP).shift(DOWN*0.04)
            group.add(dot, txt)
        spark = ink_text('Keep it current', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for i in range(0, len(group), 2):
            self.play(FadeIn(group[i]), Write(group[i+1]), run_time=0.55)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(6.4)

