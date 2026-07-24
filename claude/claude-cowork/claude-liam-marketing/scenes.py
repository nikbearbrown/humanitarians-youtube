"""
scenes.py — doodle scenes for claude-liam-marketing
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
    """Reveal doodle — The scrawled brief (9.77s)"""
    def construct(self):
        headline = 'The scrawled brief'
        body     = 'The alternative is the brief you scrawl between meetings — half a thou'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('The scrawled brief', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.3)


class B07Doodle(Scene):
    """Reveal doodle — Find the gap (10.97s)"""
    def construct(self):
        headline = 'Find the gap'
        body     = 'It also watches the competition — how rivals position themselves, who '
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Find the gap', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.5)


class B15Doodle(Scene):
    """Flow doodle — The launch sequence (7.89s)"""
    def construct(self):
        steps = ['The launch sequenc', 'outcome']
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
        spark = ink_text('The launch sequence', 28, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for b in boxes:
            self.play(Create(b), run_time=0.6)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.4)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(4.4)


class B16Doodle(Scene):
    """Flow doodle — Each on the last (10.97s)"""
    def construct(self):
        steps = ['Each on the last', 'outcome']
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
        spark = ink_text('Each on the last', 28, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for b in boxes:
            self.play(Create(b), run_time=0.6)
        for a in arrows:
            self.play(GrowArrow(a), run_time=0.4)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(7.5)


class B21Doodle(Scene):
    """Reveal doodle — Delegate the dread (9.81s)"""
    def construct(self):
        headline = 'Delegate the dread'
        body     = 'Everyone has formats they dread — captions, subject lines, meta descri'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Delegate the dread', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.3)


class B23Doodle(Scene):
    """Reveal doodle — You keep the judgment (12.63s)"""
    def construct(self):
        headline = 'You keep the judgment'
        body     = 'But review everything that goes public. It drafts well; your touch is '
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('You keep the judgment', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(9.1)

