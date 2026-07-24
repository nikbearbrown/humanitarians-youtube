"""
scenes.py — doodle scenes for claude-liam-what-plugins-are
Replaces VOX pantry slots: B05, B11, B12, B16.
All scenes: 1920×1080, 24 fps, cream #F2F0E9 background, ink #3D3929.
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


# ── Helpers ──────────────────────────────────────────────────────────────────

def ink_text(s, size=36, weight=NORMAL, color=INK):
    return Text(s, font=SANS, font_size=size, weight=weight, color=color)

def ink_rect(w, h, color=INK, fill=CREAM, fill_opacity=1.0, stroke_width=3):
    return RoundedRectangle(corner_radius=0.15, width=w, height=h,
                            stroke_color=color, stroke_width=stroke_width,
                            fill_color=fill, fill_opacity=fill_opacity)


# ── B05 — Reach into your tools (~10s) ───────────────────────────────────────

class B05Doodle(Scene):
    """
    Central hub 'Claude' with 4 connector arrows radiating out to labeled tool boxes.
    Narration: Connectors are the reach — sales plugin to CRM, data to spreadsheets, etc.
    """
    def construct(self):
        # Hub
        hub = ink_rect(2.4, 0.9).set_fill(SPARK, opacity=0.15).move_to(ORIGIN)
        hub_lbl = ink_text("Claude", 34, BOLD).move_to(hub)

        # Tools at cardinal + diagonal positions
        tools = [
            ("CRM",         UP * 2.4),
            ("Files",       RIGHT * 4.2),
            ("Search",      DOWN * 2.4),
            ("Spreadsheet", LEFT * 4.2),
        ]
        boxes, labels, arrows = [], [], []
        for name, pos in tools:
            b = ink_rect(2.0, 0.8).set_fill(CREAM, 1.0).move_to(pos)
            l = ink_text(name, 28).move_to(pos)
            # Arrow from hub edge toward box
            a = Arrow(ORIGIN, pos, buff=0.5, color=INK, stroke_width=3,
                      tip_length=0.22, max_tip_length_to_length_ratio=0.25)
            boxes.append(b); labels.append(l); arrows.append(a)

        spark = ink_text("Connectors are the reach.", 26, color=INK_DIM).to_edge(DOWN, buff=0.55)

        # Animate
        self.play(Create(hub), Write(hub_lbl), run_time=1.2)
        for b, l, a in zip(boxes, labels, arrows):
            self.play(GrowArrow(a), Create(b), Write(l), run_time=0.7)
        self.play(FadeIn(spark), run_time=0.6)
        self.wait(3.2)  # total ≈ 10s


# ── B11 — The well-read friend (~5.5s) ────────────────────────────────────────

class B11Doodle(Scene):
    """
    Two side-by-side figures: casual friend with books vs professional with clipboard.
    Narration: friend who reads a lot vs someone who reviews contracts professionally.
    """
    def construct(self):
        # Left figure — friend
        f_head = Circle(0.35, color=INK, stroke_width=3, fill_color=CREAM, fill_opacity=1)
        f_body = Line(DOWN * 0.35, DOWN * 1.5, color=INK, stroke_width=3)
        f_arms = Line(LEFT * 0.7 + DOWN * 0.8, RIGHT * 0.7 + DOWN * 0.8, color=INK, stroke_width=3)
        f_leg1 = Line(DOWN * 1.5, DOWN * 2.3 + LEFT * 0.35, color=INK, stroke_width=3)
        f_leg2 = Line(DOWN * 1.5, DOWN * 2.3 + RIGHT * 0.35, color=INK, stroke_width=3)
        friend = VGroup(f_head, f_body, f_arms, f_leg1, f_leg2).shift(LEFT * 3.8 + UP * 0.6)

        books = VGroup(*[
            ink_rect(1.0, 0.22, fill=SPARK, fill_opacity=0.3 + i * 0.15).shift(
                LEFT * 3.8 + DOWN * (0.9 + i * 0.26))
            for i in range(3)
        ])

        f_lbl = ink_text("friend who\nreads a lot", 22, color=INK_DIM).shift(LEFT * 3.8 + DOWN * 2.9)

        # Right figure — professional
        p_head = Circle(0.35, color=INK, stroke_width=3, fill_color=CREAM, fill_opacity=1)
        p_body = Line(DOWN * 0.35, DOWN * 1.5, color=INK, stroke_width=3)
        p_arms = Line(LEFT * 0.7 + DOWN * 0.8, RIGHT * 0.7 + DOWN * 0.8, color=INK, stroke_width=3)
        p_leg1 = Line(DOWN * 1.5, DOWN * 2.3 + LEFT * 0.35, color=INK, stroke_width=3)
        p_leg2 = Line(DOWN * 1.5, DOWN * 2.3 + RIGHT * 0.35, color=INK, stroke_width=3)
        pro = VGroup(p_head, p_body, p_arms, p_leg1, p_leg2).shift(RIGHT * 3.8 + UP * 0.6)

        clipboard = ink_rect(1.0, 1.4).shift(RIGHT * 4.7 + DOWN * 0.35)
        clip_lines = VGroup(*[
            Line(LEFT * 0.35, RIGHT * 0.35, color=INK_DIM, stroke_width=1.5).shift(
                RIGHT * 4.7 + DOWN * (0.1 + i * 0.3))
            for i in range(3)
        ])
        p_lbl = ink_text("professional\nreviewer", 22, color=INK_DIM).shift(RIGHT * 3.8 + DOWN * 2.9)

        vs = ink_text("vs", 42, BOLD, SPARK).move_to(ORIGIN + UP * 0.3)

        self.play(Create(friend), run_time=0.7)
        self.play(FadeIn(books, shift=UP * 0.1), Write(f_lbl), run_time=0.6)
        self.play(FadeIn(vs), run_time=0.4)
        self.play(Create(pro), run_time=0.7)
        self.play(Create(clipboard), Create(clip_lines), Write(p_lbl), run_time=0.6)
        self.wait(2.5)  # total ≈ 5.5s


# ── B12 — The professional (~6.5s) ────────────────────────────────────────────

class B12Doodle(Scene):
    """
    A contract document with annotation marks appearing clause by clause.
    Narration: asking someone who reviews contracts professionally — that's the whole reason.
    """
    def construct(self):
        doc = ink_rect(5.5, 6.2).move_to(UP * 0.2)
        header = ink_text("CONTRACT", 28, BOLD).move_to(UP * 2.9)
        lines = VGroup(*[
            Line(LEFT * 2.3, RIGHT * 2.3, color=INK_DIM, stroke_width=1.2).shift(
                UP * (2.0 - i * 0.5))
            for i in range(8)
        ])

        # Annotation marks that appear on specific clauses
        flag1 = ink_text("⚑", 30, color=SPARK).move_to(RIGHT * 2.8 + UP * 2.0)
        flag2 = ink_text("⚑", 30, color=SPARK).move_to(RIGHT * 2.8 + UP * 0.5)
        checkmark = ink_text("✓", 36, BOLD, "#5C9B6E").move_to(RIGHT * 2.8 + DOWN * 0.5)

        note = ink_text("reviewed professionally", 26, color=INK_DIM).to_edge(DOWN, buff=0.55)

        self.play(Create(doc), Write(header), run_time=0.9)
        self.play(Create(lines), run_time=0.7)
        self.play(FadeIn(flag1, scale=1.3), run_time=0.5)
        self.play(FadeIn(flag2, scale=1.3), run_time=0.5)
        self.play(FadeIn(checkmark, scale=1.3), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(2.9)  # total ≈ 6.5s


# ── B16 — You keep the judgment (~14s) ────────────────────────────────────────

class B16Doodle(Scene):
    """
    A balance scale — plugin output on the left, human hand on the right.
    Three phrases appear: 'Legal flags · Finance builds · You decide'.
    Narration: the plugin can't weigh the clause against the deal — you keep that call.
    """
    def construct(self):
        # Fulcrum
        fulcrum = Triangle(color=INK, fill_color=INK, fill_opacity=1).scale(0.3).move_to(DOWN * 1.6)
        post = Line(DOWN * 1.3, UP * 0.4, color=INK, stroke_width=4)
        beam = Line(LEFT * 3.2 + UP * 0.4, RIGHT * 3.2 + UP * 0.4, color=INK, stroke_width=4)

        # Left pan — doc/plugin output
        l_string = Line(LEFT * 3.2 + UP * 0.4, LEFT * 3.2 + DOWN * 0.5, color=INK_DIM, stroke_width=2)
        l_pan = ink_rect(2.0, 0.6, fill=CREAM, fill_opacity=1).move_to(LEFT * 3.2 + DOWN * 0.85)
        l_lbl = ink_text("plugin output", 22, color=INK_DIM).move_to(LEFT * 3.2 + DOWN * 0.85)

        # Right pan — human
        r_string = Line(RIGHT * 3.2 + UP * 0.4, RIGHT * 3.2 + DOWN * 0.5, color=INK_DIM, stroke_width=2)
        r_pan = ink_rect(2.0, 0.6, fill=CREAM, fill_opacity=1).move_to(RIGHT * 3.2 + DOWN * 0.85)
        r_lbl = ink_text("your call", 22, BOLD, SPARK).move_to(RIGHT * 3.2 + DOWN * 0.85)

        # Three phrases
        phrase1 = ink_text("Legal flags.", 30, color=INK_DIM).shift(UP * 2.7 + LEFT * 3.5)
        phrase2 = ink_text("Finance builds.", 30, color=INK_DIM).shift(UP * 2.7)
        phrase3 = ink_text("You decide.", 34, BOLD, INK).shift(UP * 2.7 + RIGHT * 3.5)

        self.play(Create(fulcrum), Create(post), run_time=0.8)
        self.play(Create(beam), run_time=0.5)
        self.play(Create(l_string), Create(l_pan), Write(l_lbl), run_time=0.8)
        self.play(Create(r_string), Create(r_pan), Write(r_lbl), run_time=0.8)
        self.play(Write(phrase1), run_time=0.7)
        self.play(Write(phrase2), run_time=0.7)
        self.play(Write(phrase3), run_time=0.8)
        # Human pan tips slightly down — you have the heavier call
        self.play(
            beam.animate.rotate(-0.12, about_point=beam.get_center()),
            run_time=1.2
        )
        self.wait(5.7)  # total ≈ 14s
