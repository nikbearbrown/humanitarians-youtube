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
        duration = DUR.get("B01", 5.0)
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
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline = Text("Why a Particle Can Walk Through a Wall", font=DISPLAY, font_size=30,
                        color=INK).move_to(UP * 0.2)
        sub = Text("Quantum tunneling — the exponential", font=SERIF, font_size=24,
                   color=TEAL).move_to(DOWN * 1.0)
        teal_accent = Line(LEFT * 1.5, RIGHT * 1.5, color=TEAL, stroke_width=1.2).move_to(DOWN * 2.5)
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
# B02 — Classical reflection: ball bounces off wall (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_ClassicalReflection(Scene):
    def construct(self):
        duration = DUR.get("B02", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Ground line
        ground = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=2).move_to(DOWN * 3.0)

        # The wall (barrier)
        wall = Rectangle(width=1.2, height=4.5).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        wall.move_to(UP * 0.0)

        # Energy level label inside wall
        barrier_label = Text("V₀", font=DISPLAY, font_size=28, color=CRIMSON).move_to(UP * 2.2)

        # Energy level of ball (horizontal line, below barrier top)
        energy_line = DashedLine(LEFT * 5, RIGHT * 5, color=INK, stroke_width=2,
                                 dash_length=0.25).move_to(UP * 0.8)
        energy_label = Text("E < V₀", font=MONO, font_size=24, color=INK).move_to(LEFT * 5.5 + UP * 1.1)

        # Ball (CRIMSON dot)
        ball = Dot(radius=0.28, color=CRIMSON).move_to(LEFT * 5.0 + UP * 0.8)

        # Incoming arrow
        arrow_in = Arrow(LEFT * 5.5 + UP * 0.8, LEFT * 1.5 + UP * 0.8,
                         color=CRIMSON, buff=0, stroke_width=3,
                         max_tip_length_to_length_ratio=0.15)
        # Reflected arrow
        arrow_out = Arrow(LEFT * 1.5 + UP * 0.8, LEFT * 5.5 + UP * 0.8,
                          color=CRIMSON, buff=0, stroke_width=3,
                          max_tip_length_to_length_ratio=0.15)

        # "Always bounces" label
        bounce_label = Text("Always reflects — 100%", font=SERIF, font_size=24,
                            color=CRIMSON).move_to(DOWN * 2.2)

        # Classical label
        classical_tag = Rectangle(width=3.5, height=0.6).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 1.5)
        classical_tag.move_to(DOWN * 2.2)

        self.play(Create(ground), run_time=0.4)
        self.play(FadeIn(wall), run_time=0.4)
        self.play(Write(barrier_label), run_time=0.3)
        self.play(Create(energy_line), run_time=0.4)
        self.play(Write(energy_label), run_time=0.3)
        self.play(GrowFromCenter(ball), run_time=0.3)
        self.play(GrowArrow(arrow_in), run_time=0.5)
        self.play(GrowArrow(arrow_out), run_time=0.5)
        self.play(FadeIn(classical_tag), run_time=0.3)
        self.play(Write(bounce_label), run_time=0.3)
        self.wait(max(0.1, duration - 4.0))


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
        q_box = Rectangle(width=12, height=2.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 1.3)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        question = Text("How does it get through\na region it cannot enter?",
                        font=DISPLAY, font_size=34, color=INK,
                        line_spacing=1.2).move_to(UP * 0.2)
        accent_dot3 = Dot(radius=0.08, color=TEAL).move_to(ORIGIN + DOWN * 2.5)
        self.add(bg)
        self.play(FadeIn(accent_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(GrowFromCenter(q_box), run_time=0.4)
        self.play(Write(question), run_time=0.5)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.play(FadeIn(accent_dot3), run_time=0.3)
        self.wait(max(0.1, duration - 3.1))


# ---------------------------------------------------------------------------
# B04 — Classical forbidden region: KE goes negative (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalForbidden(Scene):
    def construct(self):
        duration = DUR.get("B04", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Three regions
        left_box = Rectangle(width=5.0, height=5.0).set_fill(GROUND, 0.0).set_stroke(INK, 1.5)
        left_box.move_to(LEFT * 5.5 + UP * 0.0)
        barrier_box = Rectangle(width=3.0, height=5.0).set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2)
        barrier_box.move_to(ORIGIN)
        right_box = Rectangle(width=5.0, height=5.0).set_fill(GROUND, 0.0).set_stroke(INK, 1.5)
        right_box.move_to(RIGHT * 5.5 + UP * 0.0)

        # Region labels
        left_label = Text("Allowed\nKE > 0", font=MONO, font_size=22, color=INK,
                          line_spacing=1.1).move_to(LEFT * 5.5 + UP * 1.8)
        barrier_label = Text("FORBIDDEN\nKE < 0", font=DISPLAY, font_size=22, color=CRIMSON,
                              line_spacing=1.1).move_to(ORIGIN + UP * 1.8)
        right_label = Text("Allowed\nKE > 0", font=MONO, font_size=22, color=INK,
                           line_spacing=1.1).move_to(RIGHT * 5.5 + UP * 1.8)

        # Classical verdict line
        verdict_box = Rectangle(width=8, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        verdict_box.move_to(DOWN * 2.4)
        verdict = Text("Classical: ψ must be zero inside — particle cannot exist here",
                       font=SERIF, font_size=22, color=CRIMSON).move_to(DOWN * 2.4)

        # Cross mark over barrier
        cross_h = Line(LEFT * 0.5 + DOWN * 0.3, RIGHT * 0.5 + DOWN * 0.3,
                       color=CRIMSON, stroke_width=4)
        cross_v = Line(DOWN * 0.8, UP * 0.2, color=CRIMSON, stroke_width=4)
        separator = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.0).move_to(DOWN * 1.7)

        self.play(FadeIn(left_box), run_time=0.4)
        self.play(FadeIn(barrier_box), run_time=0.4)
        self.play(FadeIn(right_box), run_time=0.4)
        self.play(Write(left_label), Write(right_label), run_time=0.4)
        self.play(Write(barrier_label), run_time=0.4)
        self.play(Create(cross_h), run_time=0.3)
        self.play(Create(cross_v), run_time=0.3)
        self.play(Create(separator), run_time=0.3)
        self.play(FadeIn(verdict_box), run_time=0.3)
        self.play(Write(verdict), run_time=0.4)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B05 — Inside barrier: ψ'' = κ²ψ gives exponential decay (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_ExponentialDecay(Scene):
    def construct(self):
        duration = DUR.get("B05", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Barrier shaded region
        barrier = Rectangle(width=3.5, height=6.0).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        barrier.move_to(RIGHT * 0.5)

        # Axes
        axes_line_h = Line(LEFT * 6.5, RIGHT * 6.5, color=INK, stroke_width=1.5).move_to(DOWN * 2.8)
        axes_line_v = Line(DOWN * 3.0, UP * 3.0, color=INK, stroke_width=1.5).move_to(LEFT * 6.0)
        x_label = Text("x", font=MONO, font_size=22, color=INK).move_to(RIGHT * 6.6 + DOWN * 2.8)
        psi_label = Text("ψ(x)", font=MONO, font_size=22, color=INK).move_to(LEFT * 6.0 + UP * 3.2)

        # Incoming oscillating wave (left region)
        wave_pts = []
        for i in np.linspace(-6.0, -1.75, 120):
            y = 0.9 * np.sin(2.5 * i) - 0.5
            wave_pts.append([i, y, 0])
        wave = VMobject(color=TEAL, stroke_width=3)
        wave.set_points_smoothly(wave_pts)

        # Exponential decay inside barrier
        decay_pts = []
        for i in np.linspace(-1.75, 2.25, 80):
            x_shifted = i + 1.75
            y = 0.9 * np.exp(-1.4 * x_shifted) - 0.5
            decay_pts.append([i, y, 0])
        decay_wave = VMobject(color=TEAL, stroke_width=3)
        decay_wave.set_points_smoothly(decay_pts)

        # Small surviving tail (right of barrier)
        tail_start_y = 0.9 * np.exp(-1.4 * 4.0) - 0.5
        tail_pts = []
        for i in np.linspace(2.25, 6.0, 80):
            amp = 0.9 * np.exp(-1.4 * 4.0)
            y = amp * np.sin(2.5 * i + 1.0) - 0.5
            tail_pts.append([i, y, 0])
        tail_wave = VMobject(color=TEAL, stroke_width=3)
        tail_wave.set_points_smoothly(tail_pts)

        # Formula
        eq_box = Rectangle(width=5.0, height=0.8).set_fill(SLATE, 0.1).set_stroke(SLATE, 1)
        eq_box.move_to(UP * 2.8)
        eq = Text("ψ'' = κ²ψ  →  e^{-κx}", font=MONO, font_size=26, color=TEAL).move_to(UP * 2.8)

        # Decay label
        decay_label = Text("decays — does not vanish", font=SERIF, font_size=22,
                           color=TEAL).move_to(UP * 1.8)

        # Amplitude annotation dot at start of decay
        decay_dot = Dot(radius=0.18, color=TEAL).move_to(LEFT * 1.75 + DOWN * 0.5)

        self.play(Create(axes_line_h), run_time=0.4)
        self.play(Create(axes_line_v), run_time=0.3)
        self.play(FadeIn(barrier), run_time=0.4)
        self.play(Create(wave), run_time=0.6)
        self.play(Create(decay_wave), run_time=0.5)
        self.play(GrowFromCenter(decay_dot), run_time=0.3)
        self.play(Create(tail_wave), run_time=0.5)
        self.play(FadeIn(eq_box), run_time=0.3)
        self.play(Write(eq), run_time=0.4)
        self.play(Write(psi_label), Write(x_label), run_time=0.3)
        self.play(Write(decay_label), run_time=0.4)
        self.wait(max(0.1, duration - 5.4))


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
        content_box = Rectangle(width=13, height=1.8).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.2)
        teal_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.2)
        bottom_dot1 = Dot(radius=0.1, color=TEAL).move_to(LEFT * 6.0 + DOWN * 0.7)
        bottom_dot2 = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 0.7)
        accent_rule = Line(LEFT * 3, RIGHT * 3, color=INK, stroke_width=0.8).move_to(DOWN * 2.0)
        section_label = Text("THE MECHANISM", font=DISPLAY, font_size=22,
                              color=TEAL).move_to(UP * 2.5)
        headline = Text("The amplitude passes through —\ndecaying exponentially.",
                        font=DISPLAY, font_size=30, color=INK,
                        line_spacing=1.2).move_to(UP * 0.2)
        left_accent = Rectangle(width=0.18, height=1.8).set_fill(TEAL, 0.4).set_stroke(width=0)
        left_accent.move_to(LEFT * 6.6 + UP * 0.2)
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
# B07 — Surviving tail launches transmitted wave (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_TransmittedWave(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Thick barrier
        barrier = Rectangle(width=2.5, height=6.5).set_fill(CRIMSON, 0.2).set_stroke(CRIMSON, 2.5)
        barrier.move_to(ORIGIN)
        barrier_label = Text("barrier", font=MONO, font_size=20, color=CRIMSON).move_to(UP * 3.0)

        # Axes
        h_axis = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 2.5)
        v_axis = Line(DOWN * 2.8, UP * 3.0, color=INK, stroke_width=1.5).move_to(LEFT * 6.0)
        psi_lbl = Text("ψ", font=MONO, font_size=22, color=INK).move_to(LEFT * 6.0 + UP * 3.2)
        x_lbl = Text("x", font=MONO, font_size=22, color=INK).move_to(RIGHT * 6.2 + DOWN * 2.5)

        # Incident wave (left)
        inc_pts = []
        for i in np.linspace(-6.8, -1.25, 120):
            y = 1.2 * np.sin(2.2 * i) - 0.5
            inc_pts.append([i, y, 0])
        inc_wave = VMobject(color=TEAL, stroke_width=3.5)
        inc_wave.set_points_smoothly(inc_pts)

        # Decay inside barrier
        dec_pts = []
        for i in np.linspace(-1.25, 1.25, 60):
            x_sh = i + 1.25
            y = 1.2 * np.exp(-1.6 * x_sh) - 0.5
            dec_pts.append([i, y, 0])
        dec_wave = VMobject(color=TEAL, stroke_width=3)
        dec_wave.set_points_smoothly(dec_pts)

        # Surviving tail at exit
        tail_amp = 1.2 * np.exp(-1.6 * 2.5)
        trans_pts = []
        for i in np.linspace(1.25, 6.8, 120):
            y = tail_amp * np.sin(2.2 * i + 0.5) - 0.5
            trans_pts.append([i, y, 0])
        trans_wave = VMobject(color=TEAL, stroke_width=3.5)
        trans_wave.set_points_smoothly(trans_pts)

        # Labels
        inc_label = Text("incident", font=MONO, font_size=20, color=TEAL).move_to(LEFT * 4.5 + UP * 1.5)
        trans_label = Text("transmitted", font=MONO, font_size=20, color=TEAL).move_to(RIGHT * 4.5 + UP * 1.5)
        survived_box = Rectangle(width=4.5, height=0.6).set_fill(TEAL, 0.1).set_stroke(TEAL, 1)
        survived_box.move_to(DOWN * 2.0)
        survived_text = Text("tail survives → transmitted particle", font=SERIF, font_size=20,
                             color=TEAL).move_to(DOWN * 2.0)

        # Dot marking surviving tail amplitude
        tail_dot = Dot(radius=0.18, color=TEAL).move_to(RIGHT * 1.25 + DOWN * 0.5)

        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(FadeIn(barrier), run_time=0.4)
        self.play(Write(barrier_label), run_time=0.3)
        self.play(Create(inc_wave), run_time=0.5)
        self.play(Create(dec_wave), run_time=0.4)
        self.play(GrowFromCenter(tail_dot), run_time=0.3)
        self.play(Create(trans_wave), run_time=0.5)
        self.play(Write(inc_label), run_time=0.3)
        self.play(Write(trans_label), run_time=0.3)
        self.play(FadeIn(survived_box), run_time=0.3)
        self.play(Write(survived_text), run_time=0.4)
        self.wait(max(0.1, duration - 5.4))


# ---------------------------------------------------------------------------
# B08 — T ∝ e^{−2κL}: halving L multiplies T enormously (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_ExponentialSensitivity(Scene):
    def construct(self):
        duration = DUR.get("B08", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.2)

        # Formula box
        formula_box = Rectangle(width=7, height=0.9).set_fill(TEAL, 0.1).set_stroke(TEAL, 1.5)
        formula_box.move_to(UP * 2.3)
        formula = Text("T  ≈  e^{-2κL}", font=MONO, font_size=32, color=TEAL).move_to(UP * 2.3)

        # Thick barrier illustration
        thick_barrier = Rectangle(width=3.5, height=3.0).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.5)
        thick_barrier.move_to(LEFT * 3.5 + DOWN * 0.5)
        thick_label = Text("L", font=DISPLAY, font_size=26, color=CRIMSON).move_to(LEFT * 3.5 + UP * 1.4)
        thick_T = Text("T = T₀", font=MONO, font_size=24, color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 2.2)

        # Thin barrier illustration
        thin_barrier = Rectangle(width=1.75, height=3.0).set_fill(TEAL, 0.15).set_stroke(TEAL, 2.5)
        thin_barrier.move_to(RIGHT * 3.5 + DOWN * 0.5)
        thin_label = Text("L/2", font=DISPLAY, font_size=26, color=TEAL).move_to(RIGHT * 3.5 + UP * 1.4)
        thin_T = Text("T = T₀ × e^{κL}", font=MONO, font_size=24, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 2.2)

        # Arrow between them
        compare_arrow = Arrow(LEFT * 1.2 + DOWN * 0.5, RIGHT * 1.8 + DOWN * 0.5,
                              color=INK, buff=0, stroke_width=2.5,
                              max_tip_length_to_length_ratio=0.15)
        halve_label = Text("halve L", font=SERIF, font_size=20, color=INK).move_to(UP * 0.2)

        # Bracket showing width L
        thick_brace_top = Line(LEFT * 2.0 + UP * 1.6, LEFT * 5.0 + UP * 1.6,
                               color=CRIMSON, stroke_width=2)
        # Bracket showing width L/2
        thin_brace_top = Line(RIGHT * 2.5 + UP * 1.6, RIGHT * 4.5 + UP * 1.6,
                              color=TEAL, stroke_width=2)

        self.play(Create(title_rule), run_time=0.4)
        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula), run_time=0.4)
        self.play(FadeIn(thick_barrier), run_time=0.4)
        self.play(Create(thick_brace_top), run_time=0.3)
        self.play(Write(thick_label), Write(thick_T), run_time=0.4)
        self.play(GrowArrow(compare_arrow), run_time=0.4)
        self.play(Write(halve_label), run_time=0.3)
        self.play(FadeIn(thin_barrier), run_time=0.4)
        self.play(Create(thin_brace_top), run_time=0.3)
        self.play(Write(thin_label), Write(thin_T), run_time=0.4)
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
        q_box = Rectangle(width=11, height=1.4).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 1.0)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.5)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.5)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        text = Text("Exponential sensitivity — that is the point.",
                    font=DISPLAY, font_size=30, color=INK).move_to(UP * 0.2)
        corner_dot = Dot(radius=0.09, color=INK).move_to(ORIGIN + DOWN * 2.8)
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
# B11 — Alpha decay: He tunnels Coulomb barrier (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_AlphaDecay(Scene):
    def construct(self):
        duration = DUR.get("B11", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Nuclear well (left inner region)
        well = Rectangle(width=3.5, height=4.0).set_fill(SLATE, 0.2).set_stroke(INK, 2)
        well.move_to(LEFT * 1.5 + DOWN * 0.3)
        well_label = Text("nucleus", font=MONO, font_size=20, color=INK).move_to(LEFT * 1.5 + UP * 2.1)

        # Coulomb barrier (shaded)
        coulomb = Rectangle(width=2.5, height=4.0).set_fill(CRIMSON, 0.22).set_stroke(CRIMSON, 2.5)
        coulomb.move_to(RIGHT * 1.5 + DOWN * 0.3)
        coulomb_label = Text("Coulomb\nbarrier", font=MONO, font_size=18, color=CRIMSON,
                             line_spacing=1.1).move_to(RIGHT * 1.5 + UP * 2.0)

        # Outside (right)
        outside_line = Line(RIGHT * 2.75 + DOWN * 2.3, RIGHT * 7.0 + DOWN * 2.3,
                            color=INK, stroke_width=1.5)

        # Alpha particle (teal dot)
        alpha = Dot(radius=0.28, color=TEAL).move_to(LEFT * 2.5 + DOWN * 0.3)
        alpha_label = Text("α", font=DISPLAY, font_size=24, color=TEAL).move_to(LEFT * 2.5 + UP * 0.4)

        # Tunneling arrow
        tunnel_arrow = Arrow(LEFT * 0.5 + DOWN * 0.3, RIGHT * 4.5 + DOWN * 0.3,
                             color=TEAL, buff=0, stroke_width=3,
                             max_tip_length_to_length_ratio=0.12)

        # Numbers box
        nums_box = Rectangle(width=9, height=1.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1)
        nums_box.move_to(DOWN * 3.0)
        nums = Text("Po-212: 0.3 μs  |  Th-232: 1.4×10¹⁰ yr  →  10²⁴ range",
                    font=MONO, font_size=20, color=TEAL).move_to(DOWN * 3.0)

        # Dotted outer turning point line
        turning_pt = DashedLine(RIGHT * 2.75 + UP * 2.0, RIGHT * 2.75 + DOWN * 2.3,
                                color=TEAL, stroke_width=1.5, dash_length=0.2)

        self.play(FadeIn(well), run_time=0.4)
        self.play(Write(well_label), run_time=0.3)
        self.play(FadeIn(coulomb), run_time=0.4)
        self.play(Write(coulomb_label), run_time=0.3)
        self.play(GrowFromCenter(alpha), run_time=0.3)
        self.play(Write(alpha_label), run_time=0.3)
        self.play(GrowArrow(tunnel_arrow), run_time=0.5)
        self.play(Create(outside_line), run_time=0.3)
        self.play(Create(turning_pt), run_time=0.3)
        self.play(FadeIn(nums_box), run_time=0.3)
        self.play(Write(nums), run_time=0.4)
        self.wait(max(0.1, duration - 4.8))


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
        section_label = Text("WORKED EXAMPLE", font=DISPLAY, font_size=22,
                              color=TEAL).move_to(UP * 2.5)
        headline = Text("κ for a 1 eV barrier", font=DISPLAY, font_size=34,
                        color=INK).move_to(UP * 0.3)
        left_bar = Rectangle(width=0.15, height=1.2).set_fill(TEAL, 0.5).set_stroke(width=0)
        left_bar.move_to(LEFT * 6.6 + UP * 0.3)
        extra_dot = Dot(radius=0.09, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
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
# B13 — Worked example: κ = 5.1 nm⁻¹, e^{-10.2} ≈ 3.7×10⁻⁵ (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 22.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title banner
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("κ for a 1 eV barrier, L = 1 nm", font=DISPLAY, font_size=24,
                          color=INK).move_to(UP * 3.7)

        # Step 1 box
        step1_box = Rectangle(width=12, height=1.0).set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        step1_box.move_to(UP * 2.4)
        step1 = Text("Given: mₑ = 9.11×10⁻³¹ kg,  ΔV = 1 eV = 1.6×10⁻¹⁹ J",
                     font=MONO, font_size=22, color=INK).move_to(UP * 2.4)

        # Arrow 1
        arr1 = Arrow(UP * 1.8, UP * 1.3, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 2 box
        step2_box = Rectangle(width=12, height=1.0).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        step2_box.move_to(UP * 0.8)
        step2 = Text("κ = √(2mΔV) / ħ  ≈  5.1 nm⁻¹", font=MONO, font_size=26,
                     color=TEAL).move_to(UP * 0.8)

        # Arrow 2
        arr2 = Arrow(UP * 0.2, DOWN * 0.3, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 3 box
        step3_box = Rectangle(width=12, height=1.0).set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        step3_box.move_to(DOWN * 0.8)
        step3 = Text("At L = 1 nm:  e^{-2 × 5.1 × 1}  =  e^{-10.2}", font=MONO, font_size=24,
                     color=INK).move_to(DOWN * 0.8)

        # Result box
        result_box = Rectangle(width=8.5, height=1.0).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 2.2)
        result = Text("≈  3.7 × 10⁻⁵  (small, but not zero)", font=MONO, font_size=26,
                      color=TEAL).move_to(DOWN * 2.2)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.2)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Write(title_text), run_time=0.4)
        self.play(FadeIn(step1_box), run_time=0.3)
        self.play(Write(step1), run_time=0.4)
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(FadeIn(step2_box), run_time=0.3)
        self.play(Write(step2), run_time=0.4)
        self.play(GrowArrow(arr2), run_time=0.3)
        self.play(FadeIn(step3_box), run_time=0.3)
        self.play(Write(step3), run_time=0.4)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.0))


# ---------------------------------------------------------------------------
# B14 — Recap card (CARD beat)
# ---------------------------------------------------------------------------
class B14_Recap(Scene):
    def construct(self):
        duration = DUR.get("B14", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.18).set_stroke(width=0)
        top_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.8)
        answer_box = Rectangle(width=13, height=2.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        answer_box.move_to(UP * 0.4)
        rule_bot = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.3)
        kicker_box = Rectangle(width=6, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1)
        kicker_box.move_to(DOWN * 2.0)
        bottom_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.8)
        eyebrow = Text("THE ANSWER", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        answer = Text("Its amplitude decays through —\nif the wall is thin, enough survives.",
                      font=DISPLAY, font_size=28, color=INK,
                      line_spacing=1.25).move_to(UP * 0.4)
        kicker = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                      color=TEAL).move_to(DOWN * 2.0)
        left_accent = Dot(radius=0.12, color=TEAL).move_to(LEFT * 6.0 + UP * 2.8)
        right_accent = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 6.0 + UP * 2.8)
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
