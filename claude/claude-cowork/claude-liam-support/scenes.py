"""
scenes.py — doodle scenes for claude-liam-support
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


class B01Doodle(Scene):
    """Reveal doodle — Customers mean support (11.24s)"""
    def construct(self):
        headline = 'Customers mean support'
        body     = 'One truth first: if you have customers, you have support. It arrives w'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Customers mean support', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.7)


class B08Doodle(Scene):
    """Reveal doodle — Experience, structured (12.39s)"""
    def construct(self):
        headline = 'Experience, structured'
        body     = "And fourth, it builds a knowledge base. Every question you've ever ans"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Experience, structured', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(8.9)


class B13Doodle(Scene):
    """List doodle — Three failed payments (10.41s)"""
    def construct(self):
        items = ["Now a hard one. a customer's pay", "They're angry. you ask for a rep", 'Offers a concrete fix.']
        group = VGroup()
        for i, it in enumerate(items):
            dot = Dot(radius=0.1, color=SPARK).shift(LEFT*3.5 + DOWN*(i*0.85 - (len(items)-1)*0.425))
            txt = ink_text(it, 30).next_to(dot, RIGHT, buff=0.3).align_to(dot, UP).shift(DOWN*0.04)
            group.add(dot, txt)
        spark = ink_text('Three failed payments', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for i in range(0, len(group), 2):
            self.play(FadeIn(group[i]), Write(group[i+1]), run_time=0.55)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(6.9)


class B14Doodle(Scene):
    """Reveal doodle — You add the human line (11.07s)"""
    def construct(self):
        headline = 'You add the human line'
        body     = 'Claude drafts in your tone — it acknowledges the frustration, explains'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('You add the human line', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.6)


class B18Doodle(Scene):
    """Contrast doodle — Read before you send (12.74s)"""
    def construct(self):
        left_lbl, right_lbl = "Draft, Don'T Autosend,", 'Claude Catches The Rig'
        l_box = ink_rect(3.6, 2.4, fill=CREAM).move_to(LEFT*3.2)
        l_txt = ink_text(left_lbl, 28, color=INK_DIM).move_to(LEFT*3.2).scale(0.95)
        r_box = ink_rect(3.6, 2.4, color=SPARK, fill="#FFF8F5").move_to(RIGHT*3.2)
        r_txt = ink_text(right_lbl, 28, BOLD, INK).move_to(RIGHT*3.2).scale(0.95)
        vs = ink_text("→", 52, BOLD, SPARK).move_to(ORIGIN)
        spark = ink_text('Read before you send', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Create(l_box), Write(l_txt), run_time=0.8)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(r_box), Write(r_txt), run_time=0.8)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(9.2)

