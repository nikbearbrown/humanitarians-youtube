"""
scenes.py — doodle scenes for claude-liam-product
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


class B02Doodle(Scene):
    """Reveal doodle — Ten ideas, no team (11.84s)"""
    def construct(self):
        headline = 'Ten ideas, no team'
        body     = 'Picture the solo builder. Ten ideas on sticky notes, a few hours a wee'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Ten ideas, no team', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.3)


class B08Doodle(Scene):
    """Contrast doodle — Decide before you code (10.52s)"""
    def construct(self):
        left_lbl, right_lbl = 'That Spec Is The Thing', 'It Forces The Edge Cas'
        l_box = ink_rect(3.6, 2.4, fill=CREAM).move_to(LEFT*3.2)
        l_txt = ink_text(left_lbl, 28, color=INK_DIM).move_to(LEFT*3.2).scale(0.95)
        r_box = ink_rect(3.6, 2.4, color=SPARK, fill="#FFF8F5").move_to(RIGHT*3.2)
        r_txt = ink_text(right_lbl, 28, BOLD, INK).move_to(RIGHT*3.2).scale(0.95)
        vs = ink_text("→", 52, BOLD, SPARK).move_to(ORIGIN)
        spark = ink_text('Decide before you code', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Create(l_box), Write(l_txt), run_time=0.8)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(r_box), Write(r_txt), run_time=0.8)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(7.0)


class B14Doodle(Scene):
    """Reveal doodle — A wall of voices (8.87s)"""
    def construct(self):
        headline = 'A wall of voices'
        body     = 'Because the trap is loudness. A folder of feedback is a wall of voices'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('A wall of voices', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(5.4)


class B15Doodle(Scene):
    """Reveal doodle — Common beats loud (12.1s)"""
    def construct(self):
        headline = 'Common beats loud'
        body     = 'But the plugin counts instead of listening for volume. The loudest req'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Common beats loud', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.6)


class B18Doodle(Scene):
    """Reveal doodle — Give them a reason (11.5s)"""
    def construct(self):
        headline = 'Give them a reason'
        body     = "Because a release note isn't a changelog for you — it's a reason for t"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Give them a reason', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.0)


class B23Doodle(Scene):
    """Reveal doodle — You keep the call (10.24s)"""
    def construct(self):
        headline = 'You keep the call'
        body     = 'So it hands you a shortlist, not a verdict. The prioritization is a ju'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('You keep the call', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.7)

