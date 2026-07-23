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
        duration = DUR.get("B01", 7.0)
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
        headline = Text("Why Uncertainty Isn't About Bumping the Particle", font=DISPLAY, font_size=26,
                        color=INK).move_to(UP * 0.2)
        sub = Text("Preparation uncertainty — Robertson 1929", font=SERIF, font_size=24,
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
# B02 — Balloon analogy: wrong picture (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_BalloonAnalogy(Scene):
    def construct(self):
        duration = DUR.get("B02", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Balloon circle
        balloon = Circle(radius=1.4, color=CRIMSON, stroke_width=3).set_fill(CRIMSON, 0.2)
        balloon.move_to(LEFT * 2.0 + UP * 0.5)

        # Photon arrow pointing at balloon
        photon_arr = Arrow(RIGHT * 3.5 + UP * 0.5, RIGHT * 0.5 + UP * 0.5,
                           color=CRIMSON, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        photon_lbl = Text("photon", font=MONO, font_size=20, color=CRIMSON).move_to(RIGHT * 4.2 + UP * 0.5)

        # Red X
        x_bar1 = Line(LEFT * 5.0 + UP * 2.5, RIGHT * 1.0 + DOWN * 2.5,
                      color=CRIMSON, stroke_width=5)
        x_bar2 = Line(LEFT * 5.0 + DOWN * 2.5, RIGHT * 1.0 + UP * 2.5,
                      color=CRIMSON, stroke_width=5)

        # Label
        wrong_label = Text("'Bump it to find it' — wrong picture", font=SERIF, font_size=22,
                           color=CRIMSON).move_to(DOWN * 3.2)

        # Top rule
        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.2)

        # Corner dot
        corner_dot = Dot(radius=0.1, color=CRIMSON).move_to(LEFT * 6.5 + UP * 3.2)

        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=CRIMSON, stroke_width=1.0).move_to(DOWN * 3.8)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(corner_dot), run_time=0.3)
        self.play(FadeIn(balloon), run_time=0.5)
        self.play(GrowArrow(photon_arr), run_time=0.4)
        self.play(Write(photon_lbl), run_time=0.3)
        self.play(Create(x_bar1), run_time=0.3)
        self.play(Create(x_bar2), run_time=0.3)
        self.play(Write(wrong_label), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B03 — The Question card (CARD beat)
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 8.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        accent_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        accent_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=2.5).move_to(UP * 1.4)
        q_box = Rectangle(width=11, height=1.4).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        accent_dot = Dot(radius=0.08, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
        question = Text("What is the uncertainty principle\nactually about?",
                        font=DISPLAY, font_size=36, color=INK,
                        line_spacing=1.2).move_to(UP * 0.2)
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
# B04 — Robertson bound: coupled width-gauges (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_CoupledWidths(Scene):
    def construct(self):
        duration = DUR.get("B04", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Before label
        before_lbl = Text("Before any measurement", font=SERIF, font_size=22, color=TEAL).move_to(UP * 3.3)
        before_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.5).move_to(UP * 2.8)

        # Left: σ_x gauge (narrow)
        sx_bg = Rectangle(width=3.0, height=4.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        sx_bg.move_to(LEFT * 3.5 + DOWN * 0.3)
        sx_title = Text("σ_x", font=MONO, font_size=28, color=TEAL).move_to(LEFT * 3.5 + UP * 1.8)
        sx_bar = Rectangle(width=0.6, height=2.5).set_fill(TEAL, 0.6).set_stroke(TEAL, 2)
        sx_bar.move_to(LEFT * 3.5 + DOWN * 0.5)
        sx_lbl = Text("narrow", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.5 + DOWN * 2.1)

        # Right: σ_p gauge (wide)
        sp_bg = Rectangle(width=3.0, height=4.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        sp_bg.move_to(RIGHT * 3.5 + DOWN * 0.3)
        sp_title = Text("σ_p", font=MONO, font_size=28, color=TEAL).move_to(RIGHT * 3.5 + UP * 1.8)
        sp_bar = Rectangle(width=0.6, height=3.8).set_fill(TEAL, 0.6).set_stroke(TEAL, 2)
        sp_bar.move_to(RIGHT * 3.5 + DOWN * 0.1)
        sp_lbl = Text("wide", font=MONO, font_size=18, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 2.1)

        # Coupling arrow
        link_arr = Arrow(LEFT * 0.8 + DOWN * 0.3, RIGHT * 0.8 + DOWN * 0.3,
                         color=INK, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        link_lbl = Text("×", font=MONO, font_size=24, color=INK).move_to(DOWN * 0.3)

        # Separator
        sep = Line(UP * 2.8, DOWN * 2.8, color=SLATE, stroke_width=1).move_to(ORIGIN)

        self.play(Create(before_rule), run_time=0.3)
        self.play(Write(before_lbl), run_time=0.4)
        self.play(FadeIn(sx_bg), run_time=0.4)
        self.play(Write(sx_title), run_time=0.3)
        self.play(FadeIn(sx_bar), run_time=0.3)
        self.play(Write(sx_lbl), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(sp_bg), run_time=0.4)
        self.play(Write(sp_title), run_time=0.3)
        self.play(FadeIn(sp_bar), run_time=0.3)
        self.play(Write(sp_lbl), run_time=0.3)
        self.play(GrowArrow(link_arr), run_time=0.3)
        self.play(Write(link_lbl), run_time=0.3)
        self.wait(max(0.1, duration - 4.9))


# ---------------------------------------------------------------------------
# B05 — Robertson inequality + Gaussian curves (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_RobertsonBound(Scene):
    def construct(self):
        duration = DUR.get("B05", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Equation
        eq_box = Rectangle(width=9, height=0.95).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        eq_box.move_to(UP * 3.2)
        eq = Text("σ_x · σ_p ≥ ℏ/2", font=MONO, font_size=30, color=TEAL).move_to(UP * 3.2)

        # Top rule for equation
        eq_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.5).move_to(UP * 2.5)

        # Left panel: narrow σ_x (tall Gaussian)
        h_axis_l = Line(LEFT * 0.05, RIGHT * 3.0, color=INK, stroke_width=2).move_to(LEFT * 3.7 + DOWN * 1.8)
        # Gaussian curve: tall/narrow
        narrow_pts = []
        for i in range(41):
            t = -2.0 + i * 0.1
            x = -3.7 + t * 1.0
            y = -1.8 + 2.5 * np.exp(-t**2 * 4)
            narrow_pts.append([x, y, 0])
        narrow_curve = VMobject(color=TEAL, stroke_width=3)
        narrow_curve.set_points_smoothly(narrow_pts)
        narrow_lbl = Text("σ_x small", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.7 + DOWN * 2.5)

        # Right panel: wide σ_p (broad Gaussian)
        h_axis_r = Line(LEFT * 0.05, RIGHT * 3.0, color=INK, stroke_width=2).move_to(RIGHT * 2.7 + DOWN * 1.8)
        wide_pts = []
        for i in range(41):
            t = -2.0 + i * 0.1
            x = 2.7 + t * 1.2
            y = -1.8 + 0.9 * np.exp(-t**2 * 0.8)
            wide_pts.append([x, y, 0])
        wide_curve = VMobject(color=TEAL, stroke_width=3)
        wide_curve.set_points_smoothly(wide_pts)
        wide_lbl = Text("σ_p large", font=MONO, font_size=18, color=TEAL).move_to(RIGHT * 2.7 + DOWN * 2.5)

        # Panel labels
        lbl_x = Text("position x", font=SERIF, font_size=20, color=INK).move_to(LEFT * 3.7 + DOWN * 3.1)
        lbl_p = Text("momentum p", font=SERIF, font_size=20, color=INK).move_to(RIGHT * 2.7 + DOWN * 3.1)

        # Dividing rule
        mid_rule = Line(UP * 2.4, DOWN * 3.5, color=SLATE, stroke_width=1).move_to(ORIGIN)

        self.play(FadeIn(eq_box), run_time=0.3)
        self.play(Write(eq), run_time=0.4)
        self.play(Create(eq_rule), run_time=0.3)
        self.play(Create(h_axis_l), run_time=0.3)
        self.play(Create(narrow_curve), run_time=0.5)
        self.play(Write(narrow_lbl), run_time=0.3)
        self.play(Create(mid_rule), run_time=0.3)
        self.play(Create(h_axis_r), run_time=0.3)
        self.play(Create(wide_curve), run_time=0.5)
        self.play(Write(wide_lbl), run_time=0.3)
        self.play(Write(lbl_x), Write(lbl_p), run_time=0.3)
        self.wait(max(0.1, duration - 4.8))


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
        headline = Text("Non-commuting operators bound the state itself.",
                        font=DISPLAY, font_size=30, color=INK).move_to(UP * 0.2)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_accent), run_time=0.3)
        self.play(Write(headline), run_time=0.4)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(FadeIn(bottom_dot1), FadeIn(bottom_dot2), run_time=0.3)
        self.play(Create(accent_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.2))


# ---------------------------------------------------------------------------
# B07 — Commutator [x̂, p̂] = iℏ forces joint floor (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_Commutator(Scene):
    def construct(self):
        duration = DUR.get("B07", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Commutator equation
        top_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.5)
        comm_box = Rectangle(width=9, height=1.0).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        comm_box.move_to(UP * 2.5)
        comm = Text("[x̂, p̂] = iℏ", font=MONO, font_size=32, color=TEAL).move_to(UP * 2.5)

        # Arrow down
        arr = Arrow(UP * 1.8, UP * 1.0, color=TEAL, buff=0, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.2)

        # Consequence box
        consq_box = Rectangle(width=12, height=0.9).set_fill(SLATE, 0.1).set_stroke(TEAL, 1.5)
        consq_box.move_to(UP * 0.5)
        consq = Text("Commutator ≠ 0  →  joint floor on σ_x · σ_p", font=MONO, font_size=22,
                     color=INK).move_to(UP * 0.5)

        # Two operator boxes (don't line up when swapped)
        xp_box = Rectangle(width=2.5, height=1.0).set_fill(TEAL, 0.2).set_stroke(TEAL, 2)
        xp_box.move_to(LEFT * 2.0 + DOWN * 1.8)
        xp_lbl = Text("x̂ p̂", font=MONO, font_size=24, color=TEAL).move_to(LEFT * 2.0 + DOWN * 1.8)

        neq_sym = Text("≠", font=MONO, font_size=28, color=INK).move_to(DOWN * 1.8)

        px_box = Rectangle(width=2.5, height=1.0).set_fill(CRIMSON, 0.2).set_stroke(CRIMSON, 2)
        px_box.move_to(RIGHT * 2.0 + DOWN * 1.8)
        px_lbl = Text("p̂ x̂", font=MONO, font_size=24, color=CRIMSON).move_to(RIGHT * 2.0 + DOWN * 1.8)

        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1).move_to(DOWN * 3.5)

        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(comm_box), run_time=0.4)
        self.play(Write(comm), run_time=0.4)
        self.play(GrowArrow(arr), run_time=0.3)
        self.play(FadeIn(consq_box), run_time=0.3)
        self.play(Write(consq), run_time=0.4)
        self.play(FadeIn(xp_box), run_time=0.3)
        self.play(Write(xp_lbl), run_time=0.3)
        self.play(Write(neq_sym), run_time=0.3)
        self.play(FadeIn(px_box), run_time=0.3)
        self.play(Write(px_lbl), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.8))


# ---------------------------------------------------------------------------
# B08 — Harmonic oscillator levels and saturation (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_HOLevels(Scene):
    def construct(self):
        duration = DUR.get("B08", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title rule
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.5)
        title = Text("Harmonic oscillator: product of widths", font=DISPLAY, font_size=24,
                     color=TEAL).move_to(UP * 3.0)

        # Energy levels n=0,1,2,3
        levels = []
        labels = []
        for n in range(4):
            y = -2.0 + n * 1.4
            lev = Line(LEFT * 2.5, RIGHT * 2.5, color=TEAL, stroke_width=2.5)
            lev.move_to(LEFT * 1.5 + UP * y)
            levels.append(lev)
            n_lbl = Text(f"n={n}", font=MONO, font_size=18, color=INK).move_to(LEFT * 4.5 + UP * y)
            labels.append(n_lbl)

        # σ_x·σ_p labels
        prod_labels = []
        values = ["ℏ/2  (floor!)", "(3/2)ℏ", "(5/2)ℏ", "(7/2)ℏ"]
        colors = [TEAL, INK, INK, INK]
        for n in range(4):
            y = -2.0 + n * 1.4
            pl = Text(f"σ_x·σ_p = {values[n]}", font=MONO, font_size=18, color=colors[n])
            pl.move_to(RIGHT * 3.5 + UP * y)
            prod_labels.append(pl)

        # Ground state highlight box
        gnd_box = Rectangle(width=8.5, height=0.55).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        gnd_box.move_to(RIGHT * 3.5 + DOWN * 2.0)

        # Bottom accent
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.5)

        self.play(Create(title_rule), run_time=0.3)
        self.play(Write(title), run_time=0.4)
        for i in range(4):
            self.play(Create(levels[i]), run_time=0.2)
        self.play(FadeIn(gnd_box), run_time=0.3)
        for i in range(4):
            self.play(Write(labels[i]), run_time=0.2)
        for i in range(4):
            self.play(Write(prod_labels[i]), run_time=0.2)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.0))


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
        q_box = Rectangle(width=10, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.5)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.5)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        corner_dot = Dot(radius=0.09, color=INK).move_to(ORIGIN + DOWN * 2.8)
        text = Text("Uncertainty is in the state.\nNo apparatus required.",
                    font=DISPLAY, font_size=34, color=INK,
                    line_spacing=1.2).move_to(UP * 0.2)
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
# B11 — Robertson vs Ozawa comparison table (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_RobertsonOzawa(Scene):
    def construct(self):
        duration = DUR.get("B11", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title
        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.5)

        # Left: Robertson
        r_box = Rectangle(width=7.0, height=6.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 2)
        r_box.move_to(LEFT * 3.7 + DOWN * 0.2)
        r_title = Text("Robertson 1929", font=DISPLAY, font_size=22, color=TEAL).move_to(LEFT * 3.7 + UP * 2.7)
        r_type = Text("Preparation uncertainty", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 3.7 + UP * 2.0)
        r_eq = Text("σ_x · σ_p ≥ ℏ/2", font=MONO, font_size=20, color=TEAL).move_to(LEFT * 3.7 + UP * 1.0)
        r_what = Text("The STATE itself", font=SERIF, font_size=18, color=INK).move_to(LEFT * 3.7 + UP * 0.2)
        r_note = Text("No apparatus needed", font=SERIF, font_size=18, color=INK).move_to(LEFT * 3.7 + DOWN * 0.5)

        # Separator
        sep = Line(UP * 3.5, DOWN * 3.5, color=INK, stroke_width=1.5).move_to(ORIGIN)

        # Right: Ozawa
        o_box = Rectangle(width=7.0, height=6.5).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 2)
        o_box.move_to(RIGHT * 3.7 + DOWN * 0.2)
        o_title = Text("Ozawa 2003", font=DISPLAY, font_size=22, color=CRIMSON).move_to(RIGHT * 3.7 + UP * 2.7)
        o_type = Text("Measurement-disturbance", font=MONO, font_size=18, color=CRIMSON).move_to(RIGHT * 3.7 + UP * 2.0)
        o_eq = Text("ε(x)η(p)+… ≥ ℏ/2", font=MONO, font_size=20, color=CRIMSON).move_to(RIGHT * 3.7 + UP * 1.0)
        o_what = Text("Apparatus noise + recoil", font=SERIF, font_size=18, color=INK).move_to(RIGHT * 3.7 + UP * 0.2)
        o_note = Text("Different inequality", font=SERIF, font_size=18, color=INK).move_to(RIGHT * 3.7 + DOWN * 0.5)

        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1).move_to(DOWN * 3.8)

        r_accent = Rectangle(width=0.15, height=6.5).set_fill(TEAL, 0.5).set_stroke(width=0)
        r_accent.move_to(LEFT * 7.1 + DOWN * 0.2)
        o_accent = Rectangle(width=0.15, height=6.5).set_fill(CRIMSON, 0.5).set_stroke(width=0)
        o_accent.move_to(RIGHT * 7.1 + DOWN * 0.2)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(r_box), run_time=0.4)
        self.play(FadeIn(r_accent), run_time=0.3)
        self.play(Write(r_title), run_time=0.3)
        self.play(Write(r_type), run_time=0.3)
        self.play(Write(r_eq), run_time=0.3)
        self.play(Write(r_what), run_time=0.3)
        self.play(Write(r_note), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(o_box), run_time=0.4)
        self.play(FadeIn(o_accent), run_time=0.3)
        self.play(Write(o_title), run_time=0.3)
        self.play(Write(o_type), run_time=0.3)
        self.play(Write(o_eq), run_time=0.3)
        self.play(Write(o_what), run_time=0.3)
        self.play(Write(o_note), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.7))


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
        headline = Text("Gaussian state in harmonic oscillator", font=DISPLAY, font_size=32,
                        color=INK).move_to(UP * 0.3)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_bar), run_time=0.3)
        self.play(Write(headline), run_time=0.4)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(Create(accent_rule), run_time=0.3)
        self.play(FadeIn(extra_dot), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B13 — Worked example: Gaussian σ_x · σ_p = ℏ/2 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 19.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title banner
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("Ground state ψ₀: Gaussian minimum-uncertainty state",
                          font=MONO, font_size=18, color=INK).move_to(UP * 3.7)

        # Step 1
        s1_box = Rectangle(width=13, height=0.75).set_fill(TEAL, 0.06).set_stroke(TEAL, 1)
        s1_box.move_to(UP * 2.8)
        s1 = Text("ψ₀ ∝ e^{-αx²/2}     α = mω/ℏ",
                  font=MONO, font_size=22, color=TEAL).move_to(UP * 2.8)

        # Step 2
        s2_box = Rectangle(width=13, height=0.75).set_fill(SLATE, 0.08).set_stroke(SLATE, 1)
        s2_box.move_to(UP * 1.8)
        s2 = Text("σ_x² = ℏ/(2mω)       σ_p² = ℏmω/2",
                  font=MONO, font_size=22, color=INK).move_to(UP * 1.8)

        # Arrow
        arr = Arrow(UP * 1.2, UP * 0.5, color=TEAL, buff=0, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.2)

        # Step 3
        s3_box = Rectangle(width=13, height=0.75).set_fill(TEAL, 0.08).set_stroke(TEAL, 1)
        s3_box.move_to(UP * 0.0)
        s3 = Text("σ_x · σ_p = √(ℏ/(2mω)) · √(ℏmω/2) = ℏ/2",
                  font=MONO, font_size=22, color=TEAL).move_to(UP * 0.0)

        # Result box
        result_box = Rectangle(width=10, height=0.9).set_fill(TEAL, 0.18).set_stroke(TEAL, 2.5)
        result_box.move_to(DOWN * 1.5)
        result = Text("= ℏ/2   Equality: minimum-uncertainty state",
                      font=MONO, font_size=24, color=TEAL).move_to(DOWN * 1.5)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Write(title_text), run_time=0.4)
        self.play(FadeIn(s1_box), run_time=0.3)
        self.play(Write(s1), run_time=0.4)
        self.play(FadeIn(s2_box), run_time=0.3)
        self.play(Write(s2), run_time=0.4)
        self.play(GrowArrow(arr), run_time=0.3)
        self.play(FadeIn(s3_box), run_time=0.3)
        self.play(Write(s3), run_time=0.5)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.2))


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
        answer = Text("The state itself is uncertain.\nNo kick required.",
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
