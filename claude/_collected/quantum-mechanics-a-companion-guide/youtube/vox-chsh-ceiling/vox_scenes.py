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
        duration = DUR.get("B01", 8.0)
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
        headline = Text("Why 2 Becomes 2√2 — How Bell Beat Einstein", font=DISPLAY, font_size=26,
                        color=INK).move_to(UP * 0.2)
        sub = Text("CHSH inequality — quantum entanglement", font=SERIF, font_size=24,
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
# B02 — CHSH setup: Alice, Bob, four correlations, classical bound (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_CHSHSetup(Scene):
    def construct(self):
        duration = DUR.get("B02", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Alice box
        alice_box = Rectangle(width=3.5, height=2.0).set_fill(SLATE, 0.1).set_stroke(INK, 1.5)
        alice_box.move_to(LEFT * 4.0 + UP * 1.2)
        alice_lbl = Text("Alice", font=DISPLAY, font_size=24, color=INK).move_to(LEFT * 4.0 + UP * 1.7)
        a1_lbl = Text("a₁ or a₂", font=MONO, font_size=18, color=TEAL).move_to(LEFT * 4.0 + UP * 0.9)

        # Bob box
        bob_box = Rectangle(width=3.5, height=2.0).set_fill(SLATE, 0.1).set_stroke(INK, 1.5)
        bob_box.move_to(RIGHT * 4.0 + UP * 1.2)
        bob_lbl = Text("Bob", font=DISPLAY, font_size=24, color=INK).move_to(RIGHT * 4.0 + UP * 1.7)
        b1_lbl = Text("b₁ or b₂", font=MONO, font_size=18, color=TEAL).move_to(RIGHT * 4.0 + UP * 0.9)

        # Connector line
        conn_line = DashedLine(LEFT * 2.2 + UP * 1.2, RIGHT * 2.2 + UP * 1.2,
                               color=INK, stroke_width=1.5, dash_length=0.25)

        # CHSH bound equation
        eq_box = Rectangle(width=12, height=0.9).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2)
        eq_box.move_to(DOWN * 1.5)
        eq = Text("|E(a₁,b₁)+E(a₁,b₂)+E(a₂,b₁)−E(a₂,b₂)| ≤ 2",
                  font=MONO, font_size=20, color=CRIMSON).move_to(DOWN * 1.5)
        classical_lbl = Text("Classical ceiling — any pre-set answer theory",
                             font=SERIF, font_size=20, color=CRIMSON).move_to(DOWN * 2.6)

        # Top rule
        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.5)

        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=CRIMSON, stroke_width=1.0).move_to(DOWN * 3.5)
        mid_dot = Dot(radius=0.12, color=INK).move_to(ORIGIN + UP * 1.2)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(alice_box), run_time=0.4)
        self.play(Write(alice_lbl), run_time=0.3)
        self.play(Write(a1_lbl), run_time=0.3)
        self.play(Create(conn_line), run_time=0.4)
        self.play(FadeIn(mid_dot), run_time=0.3)
        self.play(FadeIn(bob_box), run_time=0.4)
        self.play(Write(bob_lbl), run_time=0.3)
        self.play(Write(b1_lbl), run_time=0.3)
        self.play(FadeIn(eq_box), run_time=0.3)
        self.play(Write(eq), run_time=0.5)
        self.play(Write(classical_lbl), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.8))


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
        q_box = Rectangle(width=9, height=1.4).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        accent_dot = Dot(radius=0.08, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
        question = Text("Can experiment push the score above 2?",
                        font=DISPLAY, font_size=36, color=INK).move_to(UP * 0.2)
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
# B04 — Optimal angles + quantum correlation formula (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_OptimalAngles(Scene):
    def construct(self):
        duration = DUR.get("B04", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title rule
        top_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.5)

        # Correlation formula
        formula_box = Rectangle(width=9, height=0.9).set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        formula_box.move_to(UP * 2.7)
        formula = Text("E_QM = −cos θ  (singlet)", font=MONO, font_size=26, color=TEAL).move_to(UP * 2.7)

        # Four angle labels in a 2×2 grid
        # a₁=0°, b₁=45°, a₂=90°, b₂=135°
        angle_box = Rectangle(width=10, height=2.5).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        angle_box.move_to(UP * 0.5)
        a1_txt = Text("a₁ = 0°", font=MONO, font_size=22, color=TEAL).move_to(LEFT * 3.5 + UP * 1.2)
        b1_txt = Text("b₁ = 45°", font=MONO, font_size=22, color=TEAL).move_to(RIGHT * 0.5 + UP * 1.2)
        a2_txt = Text("a₂ = 90°", font=MONO, font_size=22, color=TEAL).move_to(LEFT * 3.5 + DOWN * 0.1)
        b2_txt = Text("b₂ = 135°", font=MONO, font_size=22, color=TEAL).move_to(RIGHT * 0.5 + DOWN * 0.1)

        # Pairwise angle differences
        diff_box = Rectangle(width=10, height=0.8).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        diff_box.move_to(DOWN * 2.0)
        diff_lbl = Text("All pairwise angles: 45° (except a₂,b₂ = 135° → 45° reflected)",
                        font=SERIF, font_size=18, color=INK).move_to(DOWN * 2.0)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.0).move_to(DOWN * 3.5)

        mid_accent = Dot(radius=0.12, color=TEAL).move_to(LEFT * 0.5 + UP * 0.5)
        corner_dot = Dot(radius=0.1, color=INK).move_to(RIGHT * 6.5 + UP * 3.5)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(corner_dot), run_time=0.3)
        self.play(FadeIn(formula_box), run_time=0.4)
        self.play(Write(formula), run_time=0.4)
        self.play(FadeIn(angle_box), run_time=0.3)
        self.play(FadeIn(mid_accent), run_time=0.3)
        self.play(Write(a1_txt), run_time=0.3)
        self.play(Write(b1_txt), run_time=0.3)
        self.play(Write(a2_txt), run_time=0.3)
        self.play(Write(b2_txt), run_time=0.3)
        self.play(FadeIn(diff_box), run_time=0.3)
        self.play(Write(diff_lbl), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.8))


# ---------------------------------------------------------------------------
# B05 — CHSH sum = 2√2, 41% above classical (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_CHSHSum(Scene):
    def construct(self):
        duration = DUR.get("B05", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Steps
        top_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.5).move_to(UP * 3.5)

        s1_box = Rectangle(width=11, height=0.8).set_fill(TEAL, 0.06).set_stroke(TEAL, 1)
        s1_box.move_to(UP * 2.5)
        s1 = Text("Each E = −cos 45° = −1/√2 ≈ −0.707", font=MONO, font_size=22, color=TEAL).move_to(UP * 2.5)

        s2_box = Rectangle(width=11, height=0.8).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        s2_box.move_to(UP * 1.3)
        s2 = Text("|S| = |−4/√2| = 2√2 ≈ 2.828", font=MONO, font_size=24, color=TEAL).move_to(UP * 1.3)

        # Classical vs quantum comparison
        classical_bar = Rectangle(width=5.5, height=0.75).set_fill(CRIMSON, 0.2).set_stroke(CRIMSON, 2)
        classical_bar.move_to(LEFT * 1.25 + DOWN * 0.3)
        classical_lbl = Text("Classical max: 2", font=MONO, font_size=20, color=CRIMSON).move_to(LEFT * 1.25 + DOWN * 0.3)

        quantum_bar = Rectangle(width=7.8, height=0.75).set_fill(TEAL, 0.2).set_stroke(TEAL, 2)
        quantum_bar.move_to(LEFT * 0.1 + DOWN * 1.5)
        quantum_lbl = Text("Quantum:  2√2 ≈ 2.828", font=MONO, font_size=20, color=TEAL).move_to(LEFT * 0.1 + DOWN * 1.5)

        gap_lbl = Text("Gap: 41% above classical ceiling", font=SERIF, font_size=22, color=INK).move_to(DOWN * 2.8)

        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.5)

        corner_dot = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 6.5 + UP * 3.5)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(corner_dot), run_time=0.3)
        self.play(FadeIn(s1_box), run_time=0.3)
        self.play(Write(s1), run_time=0.4)
        self.play(FadeIn(s2_box), run_time=0.3)
        self.play(Write(s2), run_time=0.4)
        self.play(FadeIn(classical_bar), run_time=0.3)
        self.play(Write(classical_lbl), run_time=0.3)
        self.play(FadeIn(quantum_bar), run_time=0.3)
        self.play(Write(quantum_lbl), run_time=0.3)
        self.play(Write(gap_lbl), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.0))


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
        headline = Text("Entanglement bends the correlation curve.",
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
# B07 — −cosθ curve vs classical linear (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_CorrelationCurve(Scene):
    def construct(self):
        duration = DUR.get("B07", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Axes
        h_axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2).move_to(DOWN * 3.0)
        v_axis = Line(DOWN * 3.5, UP * 3.0, color=INK, stroke_width=2).move_to(LEFT * 5.5)

        # Axis labels
        x_lbl = Text("θ (degrees)", font=SERIF, font_size=18, color=INK).move_to(RIGHT * 4.5 + DOWN * 3.5)
        y_lbl = Text("E", font=MONO, font_size=18, color=INK).move_to(LEFT * 5.5 + UP * 3.2)

        # Tick marks: 0°, 45°, 90°, 135°, 180°
        tick_xs = [-5.5 + 5.5 * d / 180 * 2 for d in [0, 45, 90, 135, 180]]
        tick_labels_deg = ["0°", "45°", "90°", "135°", "180°"]
        ticks = VGroup()
        for tx, tlbl in zip(tick_xs, tick_labels_deg):
            tick = Line([tx, -3.1, 0], [tx, -2.9, 0], color=INK, stroke_width=1.5)
            ticks.add(tick)

        # Classical dashed line (linear from E=−1 at 0° to E=+1 at 180°)
        classical_pts = [[-5.5 + 5.5 * d / 180 * 2, -3.0 + 3.0 * d / 180 * 2, 0] for d in range(0, 181, 5)]
        # Actually classical for singlet at same axis: perfect anticorrelation at 0, 0 at 90, +1 at 180
        # But classical correlation for LHV at angle θ: linear from −1 to +1 → E_classical = θ/90 − 1 mapped
        classical_curve = VMobject(color=CRIMSON, stroke_width=2.5, stroke_opacity=0.7)
        classical_pts_arr = []
        for d in range(0, 181, 4):
            t = d / 180.0
            x = -5.5 + 5.5 * 2 * t
            y = -3.0 + (2 * t) * 3.0  # linear
            classical_pts_arr.append([x, y, 0])
        classical_curve.set_points_smoothly(classical_pts_arr)

        # Quantum −cosθ curve
        quantum_pts = []
        for d in range(0, 181, 3):
            t = d * np.pi / 180
            x = -5.5 + (d / 180) * 11.0
            y = -3.0 + (-np.cos(t) + 1) * 3.0  # scale to [-3, 0] → [0, 3]
            # Actually y coordinate: E = −cosθ, range from −1 to +1
            # Map E to y: y = E * 1.5 (scale factor)
            y = (-np.cos(t)) * 1.8
            quantum_pts.append([x, y, 0])
        quantum_curve = VMobject(color=TEAL, stroke_width=3)
        quantum_curve.set_points_smoothly(quantum_pts)

        # Probe dots at 45° intervals
        probe_dots = VGroup()
        for d in [45, 90, 135]:
            t = d * np.pi / 180
            x = -5.5 + (d / 180) * 11.0
            y = -np.cos(t) * 1.8
            probe_dots.add(Dot(radius=0.18, color=TEAL).move_to([x, y, 0]))

        # Legend
        legend_classical = Line(LEFT * 7 + DOWN * 3.5, LEFT * 5.5 + DOWN * 3.5,
                                color=CRIMSON, stroke_width=2.5)
        leg_c_lbl = Text("Classical", font=SERIF, font_size=16, color=CRIMSON).move_to(LEFT * 4.5 + DOWN * 3.5)
        legend_quantum = Line(LEFT * 3 + DOWN * 3.5, LEFT * 1.5 + DOWN * 3.5,
                              color=TEAL, stroke_width=3)
        leg_q_lbl = Text("Quantum −cosθ", font=SERIF, font_size=16, color=TEAL).move_to(RIGHT * 0.2 + DOWN * 3.5)

        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(FadeIn(ticks), run_time=0.3)
        self.play(Write(x_lbl), run_time=0.3)
        self.play(Create(classical_curve), run_time=0.6)
        self.play(Create(quantum_curve), run_time=0.7)
        self.play(FadeIn(probe_dots), run_time=0.4)
        self.play(FadeIn(legend_classical), run_time=0.3)
        self.play(Write(leg_c_lbl), run_time=0.3)
        self.play(FadeIn(legend_quantum), run_time=0.3)
        self.play(Write(leg_q_lbl), run_time=0.3)
        self.wait(max(0.1, duration - 5.0))


# ---------------------------------------------------------------------------
# B08 — Experimental scores: Aspect 1982, loophole-free 2015 (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_ExperimentalScores(Scene):
    def construct(self):
        duration = DUR.get("B08", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Number line from 0 to 3
        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.5)
        nline = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=2).move_to(UP * 0.5)

        # Classical ceiling at x=2 → map [0,3] to [-6, 6] → 2 = x_coord=2/3*12-6=2
        # Map: value v → x = (v / 3.0) * 12.0 - 6.0
        def v2x(v): return (v / 3.0) * 12.0 - 6.0

        classical_mark = Line([v2x(2), -0.1, 0], [v2x(2), 1.1, 0], color=CRIMSON, stroke_width=3)
        classical_lbl = Text("2\nClassical max", font=MONO, font_size=18, color=CRIMSON).move_to([v2x(2), 1.8, 0])

        tsirelson_mark = Line([v2x(2 * np.sqrt(2)), -0.1, 0], [v2x(2 * np.sqrt(2)), 1.1, 0],
                              color=TEAL, stroke_width=3)
        tsirelson_lbl = Text("2√2\nTsirelson", font=MONO, font_size=18, color=TEAL).move_to([v2x(2 * np.sqrt(2)), 1.8, 0])

        # Aspect 1982 arrow
        aspect_dot = Dot(radius=0.15, color=CRIMSON).move_to([v2x(2.697), 0.5, 0])
        aspect_lbl = Text("2.697\nAspect 1982", font=MONO, font_size=16, color=CRIMSON).move_to([v2x(2.697), -0.8, 0])

        # 2015 arrow
        lf_dot = Dot(radius=0.18, color=TEAL).move_to([v2x(2.828), 0.5, 0])
        lf_lbl = Text("2.828\n2015 loophole-free", font=MONO, font_size=16, color=TEAL).move_to([v2x(2.828), -0.8, 0])

        # Bottom summary
        summary_box = Rectangle(width=12, height=0.75).set_fill(SLATE, 0.08).set_stroke(TEAL, 1)
        summary_box.move_to(DOWN * 2.8)
        summary = Text("LHV ruled out at >10 standard deviations", font=SERIF, font_size=20,
                       color=INK).move_to(DOWN * 2.8)

        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.0).move_to(DOWN * 3.5)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(nline), run_time=0.3)
        self.play(Create(classical_mark), run_time=0.3)
        self.play(Write(classical_lbl), run_time=0.3)
        self.play(Create(tsirelson_mark), run_time=0.3)
        self.play(Write(tsirelson_lbl), run_time=0.3)
        self.play(FadeIn(aspect_dot), run_time=0.3)
        self.play(Write(aspect_lbl), run_time=0.3)
        self.play(FadeIn(lf_dot), run_time=0.3)
        self.play(Write(lf_lbl), run_time=0.3)
        self.play(FadeIn(summary_box), run_time=0.3)
        self.play(Write(summary), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.3))


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
        text = Text("Pre-set answers are ruled out.",
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
# B11 — No FTL signaling: marginal is random (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_NoFTL(Scene):
    def construct(self):
        duration = DUR.get("B11", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.5)

        # Alice
        alice_box = Rectangle(width=4, height=2.5).set_fill(SLATE, 0.08).set_stroke(INK, 1.5)
        alice_box.move_to(LEFT * 4.5 + UP * 1.0)
        alice_lbl = Text("Alice", font=DISPLAY, font_size=22, color=INK).move_to(LEFT * 4.5 + UP * 1.9)
        alice_axis = Text("Chooses axis", font=MONO, font_size=16, color=INK).move_to(LEFT * 4.5 + UP * 1.2)
        alice_out = Text("+1 or −1", font=MONO, font_size=16, color=TEAL).move_to(LEFT * 4.5 + UP * 0.5)

        # Bob
        bob_box = Rectangle(width=4, height=2.5).set_fill(SLATE, 0.08).set_stroke(INK, 1.5)
        bob_box.move_to(RIGHT * 4.5 + UP * 1.0)
        bob_lbl = Text("Bob", font=DISPLAY, font_size=22, color=INK).move_to(RIGHT * 4.5 + UP * 1.9)
        bob_random = Text("50/50 random", font=MONO, font_size=16, color=INK).move_to(RIGHT * 4.5 + UP * 1.2)
        bob_note = Text("(regardless of Alice)", font=SERIF, font_size=14, color=INK).move_to(RIGHT * 4.5 + UP * 0.5)

        # Connection
        sep = DashedLine(LEFT * 2.0 + UP * 1.0, RIGHT * 2.0 + UP * 1.0,
                         color=INK, stroke_width=1.5, dash_length=0.3)
        no_ftl = Text("No FTL signal", font=MONO, font_size=18, color=CRIMSON).move_to(UP * 0.1)

        # Classical comparison line
        compare_box = Rectangle(width=12, height=0.75).set_fill(SLATE, 0.06).set_stroke(SLATE, 1)
        compare_box.move_to(DOWN * 2.2)
        compare = Text("Correlation only visible after comparing data — at light speed",
                       font=SERIF, font_size=18, color=INK).move_to(DOWN * 2.2)

        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.0).move_to(DOWN * 3.5)

        top_accent = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.0).move_to(UP * 3.8)
        self.play(Create(top_accent), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(alice_box), run_time=0.4)
        self.play(Write(alice_lbl), run_time=0.3)
        self.play(Write(alice_axis), run_time=0.3)
        self.play(Write(alice_out), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(bob_box), run_time=0.4)
        self.play(Write(bob_lbl), run_time=0.3)
        self.play(Write(bob_random), run_time=0.3)
        self.play(Write(bob_note), run_time=0.3)
        self.play(Write(no_ftl), run_time=0.3)
        self.play(FadeIn(compare_box), run_time=0.3)
        self.play(Write(compare), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.5))


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
        headline = Text("Optimal CHSH angles: 0°, 45°, 90°, 135°", font=DISPLAY, font_size=28,
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
# B13 — Worked example: four-term CHSH calculation (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 20.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("Singlet: E = −cosθ   angles: a₁=0°, b₁=45°, a₂=90°, b₂=135°",
                          font=MONO, font_size=18, color=INK).move_to(UP * 3.7)

        # Four rows
        rows = [
            ("(a₁,b₁): θ=45°  →  E = −cos45° = −1/√2", TEAL),
            ("(a₁,b₂): θ=45°  →  E = −cos45° = −1/√2", TEAL),
            ("(a₂,b₁): θ=45°  →  E = −cos45° = −1/√2", TEAL),
            ("(a₂,b₂): θ=135° →  E = −cos135° = +1/√2", CRIMSON),
        ]
        row_boxes = []
        row_texts = []
        for k, (txt, col) in enumerate(rows):
            y = 2.4 - k * 1.0
            rb = Rectangle(width=13, height=0.75).set_fill(SLATE, 0.06).set_stroke(col, 1)
            rb.move_to(UP * y)
            rt = Text(txt, font=MONO, font_size=19, color=col).move_to(UP * y)
            row_boxes.append(rb)
            row_texts.append(rt)

        # Arrow
        arr = Arrow(UP * 0.0, DOWN * 0.7, color=TEAL, buff=0, stroke_width=2,
                    max_tip_length_to_length_ratio=0.2)

        # Result
        result_box = Rectangle(width=13, height=0.85).set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        result_box.move_to(DOWN * 1.4)
        result = Text("|S| = |−1/√2 −1/√2 −1/√2 −(+1/√2)| = 4/√2 = 2√2",
                      font=MONO, font_size=20, color=TEAL).move_to(DOWN * 1.4)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.0)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Write(title_text), run_time=0.4)
        for rb, rt in zip(row_boxes, row_texts):
            self.play(FadeIn(rb), run_time=0.2)
            self.play(Write(rt), run_time=0.3)
        self.play(GrowArrow(arr), run_time=0.3)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.5)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.5))


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
        answer = Text("Entanglement scores 2√2.\nPre-set answers are dead.",
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
