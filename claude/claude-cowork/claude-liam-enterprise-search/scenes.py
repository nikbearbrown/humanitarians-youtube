"""
scenes.py — doodle scenes for claude-liam-enterprise-search
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
    """List doodle — The company knows (10.86s)"""
    def construct(self):
        items = ["In a bigger org it's worse", "The doc you need isn't even your"]
        group = VGroup()
        for i, it in enumerate(items):
            dot = Dot(radius=0.1, color=SPARK).shift(LEFT*3.5 + DOWN*(i*0.85 - (len(items)-1)*0.425))
            txt = ink_text(it, 30).next_to(dot, RIGHT, buff=0.3).align_to(dot, UP).shift(DOWN*0.04)
            group.add(dot, txt)
        spark = ink_text('The company knows', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for i in range(0, len(group), 2):
            self.play(FadeIn(group[i]), Write(group[i+1]), run_time=0.55)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(7.4)


class B13Doodle(Scene):
    """Reveal doodle — Where did we stand? (9.75s)"""
    def construct(self):
        headline = 'Where did we stand?'
        body     = "Client context. A client you haven't heard from in six months emails t"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Where did we stand?', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.2)


class B14Doodle(Scene):
    """List doodle — A briefing, assembled (10.11s)"""
    def construct(self):
        items = ['The plugin assembles the briefin', 'The original proposal, your proj']
        group = VGroup()
        for i, it in enumerate(items):
            dot = Dot(radius=0.1, color=SPARK).shift(LEFT*3.5 + DOWN*(i*0.85 - (len(items)-1)*0.425))
            txt = ink_text(it, 30).next_to(dot, RIGHT, buff=0.3).align_to(dot, UP).shift(DOWN*0.04)
            group.add(dot, txt)
        spark = ink_text('A briefing, assembled', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        for i in range(0, len(group), 2):
            self.play(FadeIn(group[i]), Write(group[i+1]), run_time=0.55)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(6.6)


class B17Doodle(Scene):
    """Contrast doodle — Said it before? (12.65s)"""
    def construct(self):
        left_lbl, right_lbl = 'And Avoiding Contradic', 'Before You Quote A Pri'
        l_box = ink_rect(3.6, 2.4, fill=CREAM).move_to(LEFT*3.2)
        l_txt = ink_text(left_lbl, 28, color=INK_DIM).move_to(LEFT*3.2).scale(0.95)
        r_box = ink_rect(3.6, 2.4, color=SPARK, fill="#FFF8F5").move_to(RIGHT*3.2)
        r_txt = ink_text(right_lbl, 28, BOLD, INK).move_to(RIGHT*3.2).scale(0.95)
        vs = ink_text("→", 52, BOLD, SPARK).move_to(ORIGIN)
        spark = ink_text('Said it before?', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Create(l_box), Write(l_txt), run_time=0.8)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(r_box), Write(r_txt), run_time=0.8)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(9.2)


class B20Doodle(Scene):
    """Reveal doodle — Your reach, faster (9.98s)"""
    def construct(self):
        headline = 'Your reach, faster'
        body     = "You can feel the boundary. You only ever see what you're already clear"
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Your reach, faster', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(6.5)


class B23Doodle(Scene):
    """Reveal doodle — Document as you go (14.04s)"""
    def construct(self):
        headline = 'Document as you go'
        body     = 'And the last habit compounds. Every time you note why you chose someth'
        line = Line(LEFT*3.5, RIGHT*3.5, color=SPARK, stroke_width=4).shift(UP*0.15)
        h = ink_text(headline, 46, BOLD).move_to(UP*1.1)
        b = ink_text(body, 28, color=INK_DIM).move_to(DOWN*0.65)
        spark = ink_text('Document as you go', 26, color=INK_DIM).to_edge(DOWN, buff=0.6)
        self.play(Write(h), run_time=1.0)
        self.play(Create(line), run_time=0.5)
        self.play(Write(b), run_time=0.9)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(10.5)

