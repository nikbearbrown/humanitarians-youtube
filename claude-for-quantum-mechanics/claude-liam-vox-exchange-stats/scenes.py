import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------------------
# B01 — Title card (CARD beat)
# ---------------------------------------------------------------------------
class B01_Title(Scene):
    def construct(self):
        duration = DUR.get("B01", 6.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 1.9)
        rule1 = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.1)
        mid_box = Rectangle(width=13.5, height=1.1).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        mid_box.move_to(UP * 0.2)
        rule2 = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 0.5)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.0)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        teal_accent = Line(LEFT * 1.5, RIGHT * 1.5, color=TEAL, stroke_width=1.2).move_to(DOWN * 2.5)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline = Text("Why Two Electrons Avoid Each Other With No Force", font=DISPLAY, font_size=26,
                        color=INK).move_to(UP * 0.2)
        sub = Text("Exchange statistics — antisymmetry", font=SERIF, font_size=24,
                   color=TEAL).move_to(DOWN * 1.0)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(mid_box), run_time=0.4)
        self.play(Write(headline), run_time=0.4)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(accent_dot1), FadeIn(accent_dot2), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.play(Write(sub), run_time=0.4)
        self.play(Create(teal_accent), run_time=0.3)
        self.wait(max(0.1, duration - 3.3))


# ---------------------------------------------------------------------------
# B02 — Distinguishable joint probability: no preferred diagonal (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_DistinguishableProb(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Axes
        h_axis = Line(LEFT * 0.3, RIGHT * 4.5, color=INK, stroke_width=2).move_to(DOWN * 3.2 + LEFT * 1.0)
        v_axis = Line(DOWN * 3.2, UP * 3.0, color=INK, stroke_width=2).move_to(LEFT * 5.5)
        x1_label = Text("x₁", font=MONO, font_size=22, color=INK).move_to(RIGHT * 3.2 + DOWN * 3.5)
        x2_label = Text("x₂", font=MONO, font_size=22, color=INK).move_to(LEFT * 5.5 + UP * 3.2)

        # 2D probability grid: 5×5 uniform dots (distinguishable — no structure)
        prob_dots = VGroup()
        for i in range(5):
            for j in range(5):
                x = -5.5 + 1.0 + i * 1.6
                y = -3.5 + j * 1.6
                intensity = 0.3 + 0.2 * np.sin(i) * np.cos(j)  # slight variation
                d = Dot(radius=0.25, color=CRIMSON, fill_opacity=intensity + 0.2)
                d.move_to([x, y, 0])
                prob_dots.add(d)

        # Label box
        label_box = Rectangle(width=7, height=0.7).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 1.5)
        label_box.move_to(RIGHT * 3.5 + UP * 2.0)
        label = Text("Distinguishable: no node, no ridge", font=SERIF, font_size=22,
                     color=CRIMSON).move_to(RIGHT * 3.5 + UP * 2.0)

        # Title rule
        title_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.2)

        origin_dot = Dot(radius=0.12, color=INK).move_to(LEFT * 5.5 + DOWN * 3.2)
        corner_bar = Rectangle(width=0.15, height=6.8).set_fill(CRIMSON, 0.18).set_stroke(width=0)
        corner_bar.move_to(RIGHT * 3.0 + DOWN * 0.0)
        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(FadeIn(origin_dot), run_time=0.3)
        self.play(Write(x1_label), Write(x2_label), run_time=0.3)
        self.play(FadeIn(prob_dots), run_time=0.6)
        self.play(Create(title_rule), run_time=0.3)
        self.play(FadeIn(corner_bar), run_time=0.3)
        self.play(FadeIn(label_box), run_time=0.3)
        self.play(Write(label), run_time=0.4)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B03 — The Question card (CARD beat)
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        accent_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        accent_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=2.5).move_to(UP * 1.4)
        q_box = Rectangle(width=9, height=1.4).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        accent_dot = Dot(radius=0.08, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
        question = Text("What forces the statistics?",
                        font=DISPLAY, font_size=40, color=INK).move_to(UP * 0.2)
        self.add(bg)
        self.play(FadeIn(accent_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(GrowFromCenter(q_box), run_time=0.4)
        self.play(Write(question), run_time=0.5)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(FadeIn(accent_dot), run_time=0.3)
        self.wait(max(0.1, duration - 3.0))


# ---------------------------------------------------------------------------
# B04 — Antisymmetry forces zero at diagonal (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_Antisymmetry(Scene):
    def construct(self):
        duration = DUR.get("B04", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Equation display
        eq_box = Rectangle(width=12, height=1.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        eq_box.move_to(UP * 3.2)
        eq = Text("ψ(x₁, x₂) = −ψ(x₂, x₁)", font=MONO, font_size=28, color=TEAL).move_to(UP * 3.2)

        # x₁ = x₂ substitution
        sub_box = Rectangle(width=12, height=0.9).set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        sub_box.move_to(UP * 1.8)
        sub = Text("At x₁ = x₂:  ψ(x, x) = −ψ(x, x)", font=MONO, font_size=26,
                   color=INK).move_to(UP * 1.8)

        # Arrow
        arr = Arrow(UP * 1.2, UP * 0.5, color=TEAL, buff=0, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.2)

        # Result
        result_box = Rectangle(width=8, height=0.9).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        result_box.move_to(UP * 0.0)
        result = Text("∴  ψ(x, x) = 0", font=MONO, font_size=28, color=TEAL).move_to(UP * 0.0)

        # Explanation
        expl_box = Rectangle(width=12, height=1.0).set_fill(SLATE, 0.08).set_stroke(SLATE, 1)
        expl_box.move_to(DOWN * 1.5)
        expl = Text("Zero means they cannot sit at the same point — no force, just algebra",
                    font=SERIF, font_size=22, color=INK).move_to(DOWN * 1.5)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.0)

        top_accent = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(UP * 3.8)
        self.play(Create(top_accent), run_time=0.3)
        self.play(FadeIn(eq_box), run_time=0.4)
        self.play(Write(eq), run_time=0.4)
        self.play(FadeIn(sub_box), run_time=0.3)
        self.play(Write(sub), run_time=0.4)
        self.play(GrowArrow(arr), run_time=0.3)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.4)
        self.play(FadeIn(expl_box), run_time=0.3)
        self.play(Write(expl), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B05 — Node along diagonal x₁ = x₂ (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_DiagonalNode(Scene):
    def construct(self):
        duration = DUR.get("B05", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # 2D probability surface: fermion (teal off-diagonal, zero on diagonal)
        # Axes
        h_axis = Line(LEFT * 0.3, RIGHT * 4.5, color=INK, stroke_width=2).move_to(DOWN * 3.2 + LEFT * 1.0)
        v_axis = Line(DOWN * 3.2, UP * 3.0, color=INK, stroke_width=2).move_to(LEFT * 5.5)
        x1_label = Text("x₁", font=MONO, font_size=22, color=INK).move_to(RIGHT * 3.2 + DOWN * 3.5)
        x2_label = Text("x₂", font=MONO, font_size=22, color=INK).move_to(LEFT * 5.5 + UP * 3.2)

        # Probability dots — zero on diagonal, positive off-diagonal
        prob_dots = VGroup()
        for i in range(5):
            for j in range(5):
                x = -5.5 + 1.0 + i * 1.6
                y = -3.5 + j * 1.6
                if i == j:
                    # On diagonal: zero (don't draw)
                    pass
                else:
                    # Off-diagonal: positive
                    intensity = abs(i - j) * 0.12 + 0.2
                    d = Dot(radius=0.25, color=TEAL, fill_opacity=min(intensity, 0.9))
                    d.move_to([x, y, 0])
                    prob_dots.add(d)

        # Diagonal node line
        diag_line = Line([-5.5 + 1.0, -3.5, 0], [-5.5 + 1.0 + 4 * 1.6, -3.5 + 4 * 1.6, 0],
                         color=CRIMSON, stroke_width=3.5)
        diag_label = Text("node: ψ = 0", font=MONO, font_size=22,
                          color=CRIMSON).move_to(RIGHT * 1.5 + DOWN * 0.5)

        # Title
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.2)
        title = Text("Fermion: zero on diagonal", font=DISPLAY, font_size=24,
                     color=TEAL).move_to(RIGHT * 3.0 + UP * 2.5)

        origin_dot = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.5 + DOWN * 3.2)
        corner_bar = Rectangle(width=0.15, height=6.8).set_fill(TEAL, 0.18).set_stroke(width=0)
        corner_bar.move_to(RIGHT * 3.0 + DOWN * 0.0)
        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(FadeIn(origin_dot), run_time=0.3)
        self.play(Write(x1_label), Write(x2_label), run_time=0.3)
        self.play(FadeIn(prob_dots), run_time=0.6)
        self.play(Create(diag_line), run_time=0.5)
        self.play(Write(diag_label), run_time=0.3)
        self.play(Create(title_rule), run_time=0.3)
        self.play(FadeIn(corner_bar), run_time=0.3)
        self.play(Write(title), run_time=0.4)
        self.wait(max(0.1, duration - 4.0))


# ---------------------------------------------------------------------------
# B06 — Mechanism card (CARD beat)
# ---------------------------------------------------------------------------
class B06_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B06", 4.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 2.5)
        rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.4)
        content_box = Rectangle(width=13, height=1.4).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.2)
        teal_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.0)
        bottom_dot1 = Dot(radius=0.1, color=TEAL).move_to(LEFT * 6.0 + DOWN * 0.6)
        bottom_dot2 = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 0.6)
        accent_rule = Line(LEFT * 3, RIGHT * 3, color=INK, stroke_width=0.8).move_to(DOWN * 1.8)
        left_accent = Rectangle(width=0.18, height=1.4).set_fill(TEAL, 0.4).set_stroke(width=0)
        left_accent.move_to(LEFT * 6.6 + UP * 0.2)
        section_label = Text("THE MECHANISM", font=DISPLAY, font_size=22,
                              color=TEAL).move_to(UP * 2.5)
        headline = Text("Antisymmetry carves a permanent node.",
                        font=DISPLAY, font_size=32, color=INK).move_to(UP * 0.2)
        self.add(bg, headline)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_accent), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(FadeIn(bottom_dot1), FadeIn(bottom_dot2), run_time=0.3)
        self.play(Create(accent_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.2))


# ---------------------------------------------------------------------------
# B07 — Boson vs fermion comparison (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_BosonFermion(Scene):
    def construct(self):
        duration = DUR.get("B07", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Left: Fermion
        fermion_box = Rectangle(width=7, height=7.0).set_fill(TEAL, 0.05).set_stroke(TEAL, 2)
        fermion_box.move_to(LEFT * 3.7 + UP * 0.0)
        fermion_title = Text("Fermion (−)", font=DISPLAY, font_size=24, color=TEAL).move_to(LEFT * 3.7 + UP * 3.2)

        # Fermion dots — off-diagonal
        fermion_dots = VGroup()
        for i in range(4):
            for j in range(4):
                x = -7.0 + 1.1 + i * 1.5
                y = -2.8 + j * 1.5
                if i != j:
                    d = Dot(radius=0.28, color=TEAL, fill_opacity=0.5 + abs(i-j)*0.08)
                    d.move_to([x, y, 0])
                    fermion_dots.add(d)
        # Fermion diagonal line (node)
        fermion_diag = Line([-7.0 + 1.1, -2.8, 0], [-7.0 + 1.1 + 3*1.5, -2.8 + 3*1.5, 0],
                            color=CRIMSON, stroke_width=3)
        fermion_lbl = Text("node", font=MONO, font_size=18, color=CRIMSON).move_to(LEFT * 1.8 + DOWN * 0.3)

        # Right: Boson
        boson_box = Rectangle(width=7, height=7.0).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 2)
        boson_box.move_to(RIGHT * 3.7 + UP * 0.0)
        boson_title = Text("Boson (+)", font=DISPLAY, font_size=24, color=CRIMSON).move_to(RIGHT * 3.7 + UP * 3.2)

        # Boson dots — enhanced on diagonal
        boson_dots = VGroup()
        for i in range(4):
            for j in range(4):
                x = 0.5 + i * 1.5
                y = -2.8 + j * 1.5
                if i == j:
                    d = Dot(radius=0.38, color=CRIMSON, fill_opacity=0.9)
                else:
                    d = Dot(radius=0.20, color=CRIMSON, fill_opacity=0.3)
                d.move_to([x, y, 0])
                boson_dots.add(d)
        boson_lbl = Text("ridge", font=MONO, font_size=18, color=CRIMSON).move_to(RIGHT * 5.2 + DOWN * 0.3)

        # Separator
        sep = Line(UP * 3.8, DOWN * 3.8, color=INK, stroke_width=1.5).move_to(ORIGIN)

        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.8)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(fermion_box), run_time=0.4)
        self.play(Write(fermion_title), run_time=0.3)
        self.play(FadeIn(fermion_dots), run_time=0.5)
        self.play(Create(fermion_diag), run_time=0.4)
        self.play(Write(fermion_lbl), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(boson_box), run_time=0.4)
        self.play(Write(boson_title), run_time=0.3)
        self.play(FadeIn(boson_dots), run_time=0.5)
        self.play(Write(boson_lbl), run_time=0.3)
        self.wait(max(0.1, duration - 4.7))


# ---------------------------------------------------------------------------
# B08 — Exchange correlation: separation statistics (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_Separation(Scene):
    def construct(self):
        duration = DUR.get("B08", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Three horizontal bars showing average separation
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.0)

        # Fermion bar (largest)
        f_bar = Rectangle(width=8.0, height=0.9).set_fill(TEAL, 0.25).set_stroke(TEAL, 2)
        f_bar.move_to(LEFT * 0.0 + UP * 1.5)
        f_label = Text("Fermions:  ⟨(x₁−x₂)²⟩  LARGEST", font=MONO, font_size=22,
                       color=TEAL).move_to(UP * 1.5)

        # Distinguishable bar (middle)
        d_bar = Rectangle(width=6.0, height=0.9).set_fill(INK, 0.12).set_stroke(INK, 2)
        d_bar.move_to(LEFT * 1.0 + UP * 0.0)
        d_label = Text("Distinguishable:  baseline", font=MONO, font_size=22,
                       color=INK).move_to(LEFT * 1.0 + UP * 0.0)

        # Boson bar (smallest)
        b_bar = Rectangle(width=4.5, height=0.9).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        b_bar.move_to(LEFT * 1.75 + DOWN * 1.5)
        b_label = Text("Bosons:  SMALLEST", font=MONO, font_size=22,
                       color=CRIMSON).move_to(LEFT * 1.75 + DOWN * 1.5)

        # Bottom note
        note_box = Rectangle(width=10, height=0.8).set_fill(SLATE, 0.1).set_stroke(SLATE, 1)
        note_box.move_to(DOWN * 3.0)
        note = Text("No interaction — only symmetry postulate", font=SERIF, font_size=20,
                    color=INK).move_to(DOWN * 3.0)

        # Top rule for context
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.0).move_to(DOWN * 3.8)

        sep_rule = Line(LEFT * 7, RIGHT * 7, color=SLATE, stroke_width=1.0).move_to(UP * 3.5)
        self.play(Create(sep_rule), run_time=0.3)
        self.play(Create(title_rule), run_time=0.4)
        self.play(FadeIn(f_bar), run_time=0.4)
        self.play(Write(f_label), run_time=0.4)
        self.play(FadeIn(d_bar), run_time=0.4)
        self.play(Write(d_label), run_time=0.3)
        self.play(FadeIn(b_bar), run_time=0.4)
        self.play(Write(b_label), run_time=0.3)
        self.play(FadeIn(note_box), run_time=0.3)
        self.play(Write(note), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.7))


# ---------------------------------------------------------------------------
# B09 — Implication card (CARD beat)
# ---------------------------------------------------------------------------
class B09_ImplicationCard(Scene):
    def construct(self):
        duration = DUR.get("B09", 3.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        accent_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        accent_bar.move_to(UP * 2.5)
        rule_top = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.4)
        q_box = Rectangle(width=8, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.5)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.5)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        corner_dot = Dot(radius=0.09, color=INK).move_to(ORIGIN + DOWN * 2.8)
        text = Text("No force. Just a sign.",
                    font=DISPLAY, font_size=38, color=INK).move_to(UP * 0.2)
        self.add(bg)
        self.play(FadeIn(accent_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(GrowFromCenter(q_box), run_time=0.4)
        self.play(Write(text), run_time=0.4)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(FadeIn(corner_dot), run_time=0.3)
        self.wait(max(0.1, duration - 2.9))


# ---------------------------------------------------------------------------
# B10 — Antisymmetry creates shell structure instead of a 1s pile-up
# ---------------------------------------------------------------------------
class B10_ShellStructure(Scene):
    def construct(self):
        duration = DUR.get("B10", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("ANTISYMMETRY BUILDS THE PERIODIC TABLE", font=DISPLAY,
                     font_size=28, color=INK).to_edge(UP, buff=0.5)
        divider = Line(UP * 3.1, DOWN * 3.1, color=INK, stroke_opacity=0.3)
        left_head = Text("Without exclusion", font=DISPLAY, font_size=25,
                         color=CRIMSON).move_to(LEFT * 3.9 + UP * 2.65)
        right_head = Text("Fermions", font=DISPLAY, font_size=25,
                          color=TEAL).move_to(RIGHT * 3.9 + UP * 2.65)

        left_nucleus = Dot(LEFT * 3.9, radius=0.16, color=INK)
        left_orbit = Circle(radius=1.15, color=CRIMSON, stroke_width=2).move_to(LEFT * 3.9)
        piled = VGroup(*[
            Dot(LEFT * 3.9 + np.array([0.42 * np.cos(a), 0.42 * np.sin(a), 0]),
                radius=0.11, color=CRIMSON)
            for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)
        ])
        pile_label = Text("everyone piles into 1s", font=MONO, font_size=20,
                          color=CRIMSON).move_to(LEFT * 3.9 + DOWN * 2.05)

        right_center = RIGHT * 3.9
        right_nucleus = Dot(right_center, radius=0.16, color=INK)
        shells = VGroup(*[
            Circle(radius=r, color=TEAL, stroke_width=1.6,
                   stroke_opacity=0.75 - i * 0.12).move_to(right_center)
            for i, r in enumerate((0.75, 1.35, 2.0))
        ])
        shell_dots = VGroup()
        for r, count in ((0.75, 2), (1.35, 4), (2.0, 6)):
            for a in np.linspace(0, 2 * np.pi, count, endpoint=False):
                shell_dots.add(Dot(right_center + np.array([r*np.cos(a), r*np.sin(a), 0]),
                                   radius=0.095, color=TEAL))
        shell_label = Text("states fill shell by shell", font=MONO, font_size=20,
                           color=TEAL).move_to(RIGHT * 3.9 + DOWN * 2.55)
        verdict = Text("atoms gain size • matter gains structure", font=SERIF,
                       font_size=27, color=INK).move_to(DOWN * 3.35)

        self.play(FadeIn(title), Create(divider), run_time=0.6)
        self.play(FadeIn(left_head), FadeIn(right_head), run_time=0.5)
        self.play(GrowFromCenter(left_nucleus), Create(left_orbit), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in piled], lag_ratio=0.08), run_time=1.2)
        self.play(FadeIn(pile_label), run_time=0.4)
        self.play(GrowFromCenter(right_nucleus), LaggedStart(*[Create(s) for s in shells], lag_ratio=0.18), run_time=1.2)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in shell_dots], lag_ratio=0.07), run_time=1.7)
        self.play(FadeIn(shell_label), FadeIn(verdict), run_time=0.6)
        self.play(Indicate(shells, color=TEAL), run_time=1.0)
        self.wait(max(0.1, duration - 7.8))


# ---------------------------------------------------------------------------
# B11 — Helium singlet-triplet splitting (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_HeliumSplitting(Scene):
    def construct(self):
        duration = DUR.get("B11", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Two energy level diagrams side by side
        top_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.2)

        # Left: Parahelium (singlet, spatial symmetric, higher energy)
        para_box = Rectangle(width=6.5, height=6.5).set_fill(SLATE, 0.05).set_stroke(INK, 1.5)
        para_box.move_to(LEFT * 3.5 + DOWN * 0.2)
        para_title = Text("Parahelium (singlet)", font=DISPLAY, font_size=22,
                          color=INK).move_to(LEFT * 3.5 + UP * 2.7)
        para_spin = Text("spatial: symmetric", font=MONO, font_size=18,
                         color=CRIMSON).move_to(LEFT * 3.5 + UP * 2.0)
        para_level = Line(LEFT * 5.8, LEFT * 1.2, color=INK, stroke_width=2.5).move_to(LEFT * 3.5 + UP * 0.8)
        para_E = Text("E₀ + J + K", font=MONO, font_size=20, color=INK).move_to(LEFT * 3.5 + UP * 1.3)

        # Right: Orthohelium (triplet, spatial antisymmetric, lower energy)
        ortho_box = Rectangle(width=6.5, height=6.5).set_fill(SLATE, 0.05).set_stroke(TEAL, 1.5)
        ortho_box.move_to(RIGHT * 3.5 + DOWN * 0.2)
        ortho_title = Text("Orthohelium (triplet)", font=DISPLAY, font_size=22,
                           color=TEAL).move_to(RIGHT * 3.5 + UP * 2.7)
        ortho_spin = Text("spatial: antisymmetric", font=MONO, font_size=18,
                          color=TEAL).move_to(RIGHT * 3.5 + UP * 2.0)
        ortho_level = Line(RIGHT * 1.2, RIGHT * 5.8, color=TEAL, stroke_width=2.5).move_to(RIGHT * 3.5 + DOWN * 0.3)
        ortho_E = Text("E₀ + J − K  (lower)", font=MONO, font_size=20,
                       color=TEAL).move_to(RIGHT * 3.5 + UP * 0.2)

        # Arrow showing energy difference
        diff_arrow = Arrow(np.array([0.0, 0.8, 0.0]), np.array([0.0, -0.3, 0.0]),
                           color=INK, buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        diff_label = Text("2K", font=MONO, font_size=24, color=INK).move_to(RIGHT * 0.6 + UP * 0.2)

        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(DOWN * 3.8)
        self.play(Create(top_rule), run_time=0.4)
        self.play(FadeIn(para_box), run_time=0.4)
        self.play(Write(para_title), run_time=0.3)
        self.play(Write(para_spin), run_time=0.3)
        self.play(Create(para_level), run_time=0.3)
        self.play(Write(para_E), run_time=0.3)
        self.play(FadeIn(ortho_box), run_time=0.4)
        self.play(Write(ortho_title), run_time=0.3)
        self.play(Write(ortho_spin), run_time=0.3)
        self.play(Create(ortho_level), run_time=0.3)
        self.play(Write(ortho_E), run_time=0.3)
        self.play(GrowArrow(diff_arrow), run_time=0.3)
        self.play(Write(diff_label), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.2))


# ---------------------------------------------------------------------------
# B12 — Example card (CARD beat)
# ---------------------------------------------------------------------------
class B12_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B12", 3.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 2.5)
        rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.5)
        content_box = Rectangle(width=11, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.3)
        rule2 = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.7)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.2)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.2)
        accent_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        left_bar = Rectangle(width=0.15, height=1.2).set_fill(TEAL, 0.5).set_stroke(width=0)
        left_bar.move_to(LEFT * 6.6 + UP * 0.3)
        extra_dot = Dot(radius=0.09, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
        section_label = Text("WORKED EXAMPLE", font=DISPLAY, font_size=22,
                              color=TEAL).move_to(UP * 2.5)
        headline = Text("Separation statistics", font=DISPLAY, font_size=36,
                        color=INK).move_to(UP * 0.3)
        self.add(bg, headline)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_bar), run_time=0.3)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(Create(accent_rule), run_time=0.3)
        self.play(FadeIn(extra_dot), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B13 — Worked example: 1D box, fermion > dist > boson (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 21.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title banner
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("Two non-interacting particles in 1D box, orbitals ψ₁, ψ₂",
                          font=MONO, font_size=20, color=INK).move_to(UP * 3.7)

        # Step 1: Distinguishable
        s1_box = Rectangle(width=12, height=0.85).set_fill(INK, 0.06).set_stroke(INK, 1.5)
        s1_box.move_to(UP * 2.6)
        s1 = Text("Distinguishable:  ⟨(x₁−x₂)²⟩ = baseline  D",
                  font=MONO, font_size=22, color=INK).move_to(UP * 2.6)

        # Arrow 1
        arr1 = Arrow(UP * 2.0, UP * 1.5, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 2: Fermion
        s2_box = Rectangle(width=12, height=0.85).set_fill(TEAL, 0.1).set_stroke(TEAL, 1.5)
        s2_box.move_to(UP * 1.0)
        s2 = Text("Fermion (−):  ⟨(x₁−x₂)²⟩ = D + exchange > D",
                  font=MONO, font_size=22, color=TEAL).move_to(UP * 1.0)

        # Arrow 2
        arr2 = Arrow(UP * 0.4, DOWN * 0.1, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 3: Boson
        s3_box = Rectangle(width=12, height=0.85).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        s3_box.move_to(DOWN * 0.6)
        s3 = Text("Boson (+):  ⟨(x₁−x₂)²⟩ = D − exchange < D",
                  font=MONO, font_size=22, color=CRIMSON).move_to(DOWN * 0.6)

        # Result
        result_box = Rectangle(width=10, height=0.85).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 2.0)
        result = Text("fermion > dist > boson — no H change",
                      font=MONO, font_size=24, color=TEAL).move_to(DOWN * 2.0)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.2)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Write(title_text), run_time=0.4)
        self.play(FadeIn(s1_box), run_time=0.3)
        self.play(Write(s1), run_time=0.4)
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(FadeIn(s2_box), run_time=0.3)
        self.play(Write(s2), run_time=0.4)
        self.play(GrowArrow(arr2), run_time=0.3)
        self.play(FadeIn(s3_box), run_time=0.3)
        self.play(Write(s3), run_time=0.4)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.4))


# ---------------------------------------------------------------------------
# B14 — Recap card (CARD beat)
# ---------------------------------------------------------------------------
class B14_Recap(Scene):
    def construct(self):
        duration = DUR.get("B14", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.18).set_stroke(width=0)
        top_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.8)
        answer_box = Rectangle(width=13, height=2.0).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        answer_box.move_to(UP * 0.5)
        rule_bot = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.2)
        kicker_box = Rectangle(width=6, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1)
        kicker_box.move_to(DOWN * 2.0)
        bottom_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.8)
        left_accent = Dot(radius=0.12, color=TEAL).move_to(LEFT * 6.0 + UP * 2.8)
        right_accent = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 6.0 + UP * 2.8)
        eyebrow = Text("THE ANSWER", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        answer = Text("Antisymmetry writes the node.\nNo force needed.",
                      font=DISPLAY, font_size=30, color=INK,
                      line_spacing=1.25).move_to(UP * 0.5)
        kicker = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                      color=TEAL).move_to(DOWN * 2.0)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(answer_box), run_time=0.4)
        self.play(Write(answer), run_time=0.5)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(FadeIn(kicker_box), run_time=0.3)
        self.play(Write(kicker), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.play(FadeIn(left_accent), FadeIn(right_accent), run_time=0.3)
        self.wait(max(0.1, duration - 3.7))
