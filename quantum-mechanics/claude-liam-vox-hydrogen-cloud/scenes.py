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
        headline = Text("Why the Electron Has No Orbit, Only a Cloud", font=DISPLAY, font_size=28,
                        color=INK).move_to(UP * 0.2)
        sub = Text("Hydrogen 1s — peak vs mean", font=SERIF, font_size=24,
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
# B02 — Bohr model: electron on a circle at a₀ (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B02_BohrCircle(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Proton at center
        proton = Dot(radius=0.3, color=CRIMSON).move_to(ORIGIN)
        proton_label = Text("+", font=DISPLAY, font_size=28, color=INK).move_to(ORIGIN)

        # Bohr circle
        bohr_circle = Circle(radius=2.5, color=CRIMSON, stroke_width=2.5)

        # Electron on the circle
        electron = Dot(radius=0.22, color=CRIMSON).move_to(RIGHT * 2.5)
        electron_label = Text("e⁻", font=DISPLAY, font_size=20, color=INK).move_to(RIGHT * 2.5)

        # a₀ radius arrow
        radius_arrow = Arrow(ORIGIN, RIGHT * 2.5, color=CRIMSON, buff=0.3,
                             stroke_width=2, max_tip_length_to_length_ratio=0.15)
        radius_label = Text("a₀ = 0.053 nm", font=MONO, font_size=24,
                            color=CRIMSON).move_to(UP * 0.5 + RIGHT * 1.2)

        # "One radius" box
        one_box = Rectangle(width=5.5, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        one_box.move_to(DOWN * 2.5)
        one_label = Text("One radius: peak = mean = orbit radius", font=SERIF, font_size=22,
                         color=CRIMSON).move_to(DOWN * 2.5)

        # Ground line
        ground_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1).move_to(DOWN * 3.2)

        # Tick at a₀ on the circle
        a0_tick = Line(RIGHT * 2.3, RIGHT * 2.7, color=CRIMSON, stroke_width=2.5)

        self.play(GrowFromCenter(proton), run_time=0.4)
        self.play(Create(bohr_circle), run_time=0.5)
        self.play(GrowFromCenter(electron), run_time=0.3)
        self.play(Write(proton_label), Write(electron_label), run_time=0.3)
        self.play(GrowArrow(radius_arrow), run_time=0.4)
        self.play(Create(a0_tick), run_time=0.3)
        self.play(Write(radius_label), run_time=0.3)
        self.play(Create(ground_rule), run_time=0.3)
        self.play(FadeIn(one_box), run_time=0.3)
        self.play(Write(one_label), run_time=0.4)
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
        q_box = Rectangle(width=10, height=1.6).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 1.0)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        accent_dot = Dot(radius=0.08, color=TEAL).move_to(ORIGIN + DOWN * 2.8)
        question = Text("What if most probable ≠ average?",
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
# B04 — P(r) curve builds up (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_PrCurve(Scene):
    def construct(self):
        duration = DUR.get("B04", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Axes
        h_axis = Line(LEFT * 0.5, RIGHT * 6.0, color=INK, stroke_width=2).move_to(DOWN * 2.8)
        v_axis = Line(DOWN * 3.0, UP * 2.8, color=INK, stroke_width=2).move_to(LEFT * 6.0)
        x_label = Text("r / a₀", font=MONO, font_size=22, color=INK).move_to(RIGHT * 5.5 + DOWN * 3.2)
        p_label = Text("P(r)", font=MONO, font_size=22, color=INK).move_to(LEFT * 5.5 + UP * 3.0)

        # r axis ticks: 1a₀, 2a₀, 3a₀, 4a₀, 5a₀
        ticks = []
        tick_labels = []
        a0_px = 1.5  # pixels per a₀
        for i in range(1, 6):
            x_pos = LEFT * 6.0 + RIGHT * (i * a0_px) + DOWN * 2.8
            t = Line(x_pos + DOWN * 0.12, x_pos + UP * 0.12, color=INK, stroke_width=1.5)
            tl = Text(f"{i}a₀", font=MONO, font_size=18, color=INK).move_to(x_pos + DOWN * 0.45)
            ticks.append(t)
            tick_labels.append(tl)
        tick_vgroup = VGroup(*ticks)
        ticklbl_vgroup = VGroup(*tick_labels)

        # P(r) = (4/a0^3) r^2 exp(-2r/a0) — plot as TEAL curve
        curve_pts = []
        for i in np.linspace(0.001, 5.5, 200):
            y_val = 4.0 * (i**2) * np.exp(-2.0 * i)  # dimensionless a₀ units
            x_screen = -6.0 + i * a0_px
            y_screen = -2.8 + y_val * 5.0  # scale
            if y_screen < 2.8:
                curve_pts.append([x_screen, y_screen, 0])
        pr_curve = VMobject(color=TEAL, stroke_width=3.5)
        pr_curve.set_points_smoothly(curve_pts)

        # Shaded area under curve (lighter teal fill)
        shade_pts = [[curve_pts[0][0], -2.8, 0]] + curve_pts + [[curve_pts[-1][0], -2.8, 0]]
        shade = VMobject(color=TEAL, fill_opacity=0.15, stroke_width=0)
        shade.set_points_smoothly(shade_pts)

        # Origin dot
        origin_dot = Dot(radius=0.1, color=INK).move_to(LEFT * 6.0 + DOWN * 2.8)
        # Top border line
        top_border = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.0).move_to(UP * 3.3)

        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(GrowFromCenter(origin_dot), run_time=0.3)
        self.play(Create(tick_vgroup), run_time=0.3)
        self.play(Write(ticklbl_vgroup), Write(x_label), Write(p_label), run_time=0.4)
        self.play(FadeIn(shade), run_time=0.4)
        self.play(Create(pr_curve), run_time=0.8)
        self.play(Create(top_border), run_time=0.3)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B05 — Peak marker at a₀ (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_PeakMarker(Scene):
    def construct(self):
        duration = DUR.get("B05", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        a0_px = 1.5
        # Axes
        h_axis = Line(LEFT * 0.5, RIGHT * 6.0, color=INK, stroke_width=2).move_to(DOWN * 2.8)
        v_axis = Line(DOWN * 3.0, UP * 2.8, color=INK, stroke_width=2).move_to(LEFT * 6.0)
        x_label = Text("r / a₀", font=MONO, font_size=22, color=INK).move_to(RIGHT * 5.5 + DOWN * 3.2)

        # P(r) curve (same as B04)
        curve_pts = []
        for i in np.linspace(0.001, 5.5, 200):
            y_val = 4.0 * (i**2) * np.exp(-2.0 * i)
            x_screen = -6.0 + i * a0_px
            y_screen = -2.8 + y_val * 5.0
            if y_screen < 2.8:
                curve_pts.append([x_screen, y_screen, 0])
        pr_curve = VMobject(color=TEAL, stroke_width=3.5)
        pr_curve.set_points_smoothly(curve_pts)

        # Peak position: r = 1a₀ → x = -6.0 + 1.5 = -4.5
        peak_x = -6.0 + a0_px
        peak_y_val = 4.0 * 1.0 * np.exp(-2.0)
        peak_y = -2.8 + peak_y_val * 5.0

        # Vertical dashed line at r = a₀
        peak_line = DashedLine([peak_x, -2.8, 0], [peak_x, peak_y, 0],
                               color=CRIMSON, stroke_width=2.5, dash_length=0.2)

        # Peak dot
        peak_dot = Dot(radius=0.2, color=CRIMSON).move_to([peak_x, peak_y, 0])

        # Peak label
        peak_label = Text("r_peak = a₀", font=MONO, font_size=24, color=CRIMSON)
        peak_label.move_to([peak_x + 1.5, peak_y + 0.5, 0])

        # Arrow pointing to peak
        peak_arrow = Arrow([peak_x + 1.2, peak_y + 0.3, 0], [peak_x + 0.3, peak_y + 0.1, 0],
                           color=CRIMSON, buff=0, stroke_width=2,
                           max_tip_length_to_length_ratio=0.2)

        # Bohr's result banner
        bohr_box = Rectangle(width=6, height=0.7).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 1)
        bohr_box.move_to(UP * 2.0 + RIGHT * 1.5)
        bohr_text = Text("Bohr's orbit lands here — peak only", font=SERIF, font_size=20,
                         color=CRIMSON).move_to(UP * 2.0 + RIGHT * 1.5)

        origin_dot = Dot(radius=0.1, color=INK).move_to(LEFT * 6.0 + DOWN * 2.8)
        self.add(bg)
        self.play(Create(h_axis), run_time=0.4)
        self.play(Create(v_axis), run_time=0.3)
        self.play(GrowFromCenter(origin_dot), run_time=0.3)
        self.play(Create(pr_curve), run_time=0.6)
        self.play(Create(peak_line), run_time=0.4)
        self.play(GrowFromCenter(peak_dot), run_time=0.3)
        self.play(GrowArrow(peak_arrow), run_time=0.3)
        self.play(Write(peak_label), Write(x_label), run_time=0.4)
        self.play(FadeIn(bohr_box), run_time=0.3)
        self.play(Write(bohr_text), run_time=0.4)
        self.wait(max(0.1, duration - 4.5))


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
        content_box = Rectangle(width=13, height=1.6).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.2)
        teal_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.2)
        bottom_dot1 = Dot(radius=0.1, color=TEAL).move_to(LEFT * 6.0 + DOWN * 0.7)
        bottom_dot2 = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 6.0 + DOWN * 0.7)
        accent_rule = Line(LEFT * 3, RIGHT * 3, color=INK, stroke_width=0.8).move_to(DOWN * 2.0)
        left_accent = Rectangle(width=0.18, height=1.6).set_fill(TEAL, 0.4).set_stroke(width=0)
        left_accent.move_to(LEFT * 6.6 + UP * 0.2)
        section_label = Text("THE MECHANISM", font=DISPLAY, font_size=22,
                              color=TEAL).move_to(UP * 2.5)
        headline = Text("The tail pulls the average past the peak.",
                        font=DISPLAY, font_size=32, color=INK).move_to(UP * 0.2)
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
# B07 — Mean marker at 3a₀/2 with tail highlight (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_MeanMarker(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        a0_px = 1.5
        # Axes
        h_axis = Line(LEFT * 0.5, RIGHT * 6.0, color=INK, stroke_width=2).move_to(DOWN * 2.8)
        v_axis = Line(DOWN * 3.0, UP * 2.8, color=INK, stroke_width=2).move_to(LEFT * 6.0)

        # P(r) curve
        curve_pts = []
        for i in np.linspace(0.001, 5.5, 200):
            y_val = 4.0 * (i**2) * np.exp(-2.0 * i)
            x_screen = -6.0 + i * a0_px
            y_screen = -2.8 + y_val * 5.0
            if y_screen < 2.8:
                curve_pts.append([x_screen, y_screen, 0])
        pr_curve = VMobject(color=TEAL, stroke_width=3.5)
        pr_curve.set_points_smoothly(curve_pts)

        # Peak line (crimson)
        peak_x = -6.0 + a0_px
        peak_y_val = 4.0 * np.exp(-2.0)
        peak_y = -2.8 + peak_y_val * 5.0
        peak_line = DashedLine([peak_x, -2.8, 0], [peak_x, peak_y + 0.2, 0],
                               color=CRIMSON, stroke_width=2.5, dash_length=0.2)
        peak_dot = Dot(radius=0.18, color=CRIMSON).move_to([peak_x, peak_y, 0])
        peak_lbl = Text("a₀", font=MONO, font_size=20, color=CRIMSON).move_to([peak_x, -3.2, 0])

        # Mean line (teal, at 1.5 a₀)
        mean_x = -6.0 + 1.5 * a0_px
        mean_y_val = 4.0 * (1.5**2) * np.exp(-3.0)
        mean_y = -2.8 + mean_y_val * 5.0
        mean_line = DashedLine([mean_x, -2.8, 0], [mean_x, mean_y + 0.2, 0],
                               color=TEAL, stroke_width=2.5, dash_length=0.2)
        mean_dot = Dot(radius=0.18, color=TEAL).move_to([mean_x, mean_y, 0])
        mean_lbl = Text("3a₀/2", font=MONO, font_size=20, color=TEAL).move_to([mean_x, -3.2, 0])

        # Arrow showing the gap
        gap_arrow = Arrow([peak_x + 0.15, -2.0, 0], [mean_x - 0.15, -2.0, 0],
                          color=INK, buff=0, stroke_width=2,
                          max_tip_length_to_length_ratio=0.15)
        gap_label = Text("gap", font=MONO, font_size=20, color=INK).move_to(
            [(peak_x + mean_x)/2, -1.7, 0])

        # Tail label
        tail_lbl = Text("tail", font=SERIF, font_size=20, color=TEAL).move_to(RIGHT * 2.5 + UP * 0.3)

        self.play(Create(h_axis), Create(v_axis), run_time=0.4)
        self.play(Create(pr_curve), run_time=0.6)
        self.play(Create(peak_line), run_time=0.4)
        self.play(GrowFromCenter(peak_dot), run_time=0.3)
        self.play(Write(peak_lbl), run_time=0.3)
        self.play(Create(mean_line), run_time=0.4)
        self.play(GrowFromCenter(mean_dot), run_time=0.3)
        self.play(Write(mean_lbl), run_time=0.3)
        self.play(GrowArrow(gap_arrow), run_time=0.4)
        self.play(Write(gap_label), Write(tail_lbl), run_time=0.3)
        self.wait(max(0.1, duration - 4.7))


# ---------------------------------------------------------------------------
# B08 — Two different numbers proof (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_TwoNumbers(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title rule
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.0)

        # Orbit case
        orbit_box = Rectangle(width=6, height=3.5).set_fill(CRIMSON, 0.1).set_stroke(CRIMSON, 2)
        orbit_box.move_to(LEFT * 3.5 + UP * 0.5)
        orbit_title = Text("Orbit", font=DISPLAY, font_size=26, color=CRIMSON).move_to(LEFT * 3.5 + UP * 2.0)
        orbit_circle = Circle(radius=0.8, color=CRIMSON, stroke_width=2.5).move_to(LEFT * 3.5 + UP * 0.5)
        orbit_dot = Dot(radius=0.15, color=CRIMSON).move_to(LEFT * 3.5 + RIGHT * 0.8 + UP * 0.5)
        orbit_eq = Text("peak = mean = a₀", font=MONO, font_size=20, color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 1.2)

        # Cloud case
        cloud_box = Rectangle(width=6, height=3.5).set_fill(TEAL, 0.08).set_stroke(TEAL, 2)
        cloud_box.move_to(RIGHT * 3.5 + UP * 0.5)
        cloud_title = Text("Cloud", font=DISPLAY, font_size=26, color=TEAL).move_to(RIGHT * 3.5 + UP * 2.0)
        cloud_circle = Circle(radius=1.1, color=TEAL, stroke_width=1, fill_opacity=0.15)
        cloud_circle.set_fill(TEAL, 0.15)
        cloud_circle.move_to(RIGHT * 3.5 + UP * 0.5)
        cloud_inner = Circle(radius=0.5, color=TEAL, stroke_width=1, fill_opacity=0.3)
        cloud_inner.move_to(RIGHT * 3.5 + UP * 0.5)
        cloud_eq = Text("peak ≠ mean", font=MONO, font_size=20, color=TEAL).move_to(RIGHT * 3.5 + DOWN * 1.2)

        # X mark on orbit
        x_line1 = Line(LEFT * 4.8 + DOWN * 0.3, LEFT * 2.2 + DOWN * 1.8,
                       color=CRIMSON, stroke_width=3)
        x_line2 = Line(LEFT * 2.2 + DOWN * 0.3, LEFT * 4.8 + DOWN * 1.8,
                       color=CRIMSON, stroke_width=3)

        self.play(Create(title_rule), run_time=0.4)
        self.play(FadeIn(orbit_box), run_time=0.4)
        self.play(Write(orbit_title), run_time=0.3)
        self.play(Create(orbit_circle), run_time=0.4)
        self.play(GrowFromCenter(orbit_dot), run_time=0.3)
        self.play(Write(orbit_eq), run_time=0.3)
        self.play(FadeIn(cloud_box), run_time=0.4)
        self.play(Write(cloud_title), run_time=0.3)
        self.play(FadeIn(cloud_circle), FadeIn(cloud_inner), run_time=0.4)
        self.play(Write(cloud_eq), run_time=0.3)
        self.play(Create(x_line1), run_time=0.3)
        self.play(Create(x_line2), run_time=0.3)
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
        q_box = Rectangle(width=10, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.5)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.5)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        corner_dot = Dot(radius=0.09, color=INK).move_to(ORIGIN + DOWN * 2.8)
        text = Text("Orbit → one number.  Cloud → two.",
                    font=DISPLAY, font_size=32, color=INK).move_to(UP * 0.2)
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
# B10 — Spherical probability cloud, with no preferred trajectory
# ---------------------------------------------------------------------------
class B10_SphericalCloud(Scene):
    def construct(self):
        duration = DUR.get("B10", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("A CLOUD HAS NO PREFERRED DIRECTION", font=DISPLAY,
                     font_size=28, color=INK).to_edge(UP, buff=0.55)
        nucleus = Dot(radius=0.16, color=CRIMSON)
        rings = VGroup(*[
            Circle(radius=r, color=TEAL, stroke_width=1.5,
                   stroke_opacity=max(0.12, 0.52 - r * 0.08))
            for r in (0.75, 1.35, 2.0, 2.65)
        ])

        rng = np.random.default_rng(17)
        cloud = VGroup()
        for _ in range(180):
            angle = rng.uniform(0, 2 * np.pi)
            radius = min(2.75, rng.gamma(2.2, 0.58))
            point = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            opacity = max(0.10, 0.65 * (1 - radius / 3.1))
            cloud.add(Dot(point=point, radius=0.025, color=TEAL,
                          fill_opacity=opacity, stroke_opacity=0))

        label90 = Text("90% probability region", font=MONO, font_size=22,
                       color=TEAL).move_to(RIGHT * 4.8 + UP * 1.25)
        arrow90 = Arrow(RIGHT * 4.0 + UP * 1.05, RIGHT * 2.4 + UP * 0.75,
                        color=TEAL, stroke_width=2.5, buff=0.08)
        no_path = Text("no orbit • no path between measurements", font=SERIF,
                       font_size=28, color=INK).move_to(DOWN * 3.25)
        axes = VGroup(
            Line(LEFT * 3.1, RIGHT * 3.1, color=INK, stroke_opacity=0.25),
            Line(DOWN * 3.1, UP * 3.1, color=INK, stroke_opacity=0.25),
        )

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(axes), GrowFromCenter(nucleus), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(d) for d in cloud], lag_ratio=0.004), run_time=2.4)
        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.15), run_time=1.2)
        self.play(GrowArrow(arrow90), FadeIn(label90), run_time=0.8)
        self.play(FadeIn(no_path), run_time=0.6)
        self.play(Rotate(cloud, angle=PI / 3), Rotate(rings, angle=PI / 3), run_time=2.0)
        self.wait(max(0.1, duration - 8.2))


# ---------------------------------------------------------------------------
# B11 — Bohr's luck: length scale real, orbit not (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B11_BohrLuck(Scene):
    def construct(self):
        duration = DUR.get("B11", 12.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Two columns
        left_rule = Line(UP * 3.5, DOWN * 3.5, color=INK, stroke_width=1).move_to(ORIGIN)

        # Left: Bohr's result
        left_box = Rectangle(width=7.5, height=5.0).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.5)
        left_box.move_to(LEFT * 3.8 + UP * 0.2)
        left_title = Text("Bohr 1913", font=DISPLAY, font_size=24, color=CRIMSON).move_to(LEFT * 3.8 + UP * 2.3)
        bohr_eq1 = Text("E_n = −13.6 eV / n²", font=MONO, font_size=22, color=CRIMSON).move_to(LEFT * 3.8 + UP * 1.2)
        bohr_eq2 = Text("a₀ = 0.053 nm", font=MONO, font_size=22, color=CRIMSON).move_to(LEFT * 3.8 + UP * 0.3)
        bohr_wrong = Text("orbit: WRONG", font=MONO, font_size=20, color=CRIMSON).move_to(LEFT * 3.8 + DOWN * 0.8)

        # Cross over orbit label
        cross = Line(LEFT * 5.5 + DOWN * 0.8, LEFT * 2.0 + DOWN * 0.8,
                     color=CRIMSON, stroke_width=3)

        # Right: QM result
        right_box = Rectangle(width=7.5, height=5.0).set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        right_box.move_to(RIGHT * 3.8 + UP * 0.2)
        right_title = Text("QM exact", font=DISPLAY, font_size=24, color=TEAL).move_to(RIGHT * 3.8 + UP * 2.3)
        qm_eq1 = Text("same energies ✓", font=MONO, font_size=22, color=TEAL).move_to(RIGHT * 3.8 + UP * 1.2)
        qm_eq2 = Text("same a₀ ✓", font=MONO, font_size=22, color=TEAL).move_to(RIGHT * 3.8 + UP * 0.3)
        qm_right = Text("cloud: CORRECT", font=MONO, font_size=20, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.8)

        # Top rule and bottom accent dots
        top_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1.5).move_to(UP * 3.2)
        bottom_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=1.0).move_to(DOWN * 3.2)
        check_dot = Dot(radius=0.2, color=TEAL).move_to(RIGHT * 3.8 + DOWN * 0.8)

        self.play(Create(top_rule), run_time=0.4)
        self.play(FadeIn(left_box), run_time=0.4)
        self.play(Write(left_title), run_time=0.3)
        self.play(Write(bohr_eq1), Write(bohr_eq2), run_time=0.4)
        self.play(Write(bohr_wrong), run_time=0.3)
        self.play(Create(cross), run_time=0.3)
        self.play(Create(left_rule), run_time=0.3)
        self.play(FadeIn(right_box), run_time=0.4)
        self.play(Write(right_title), run_time=0.3)
        self.play(Write(qm_eq1), Write(qm_eq2), run_time=0.4)
        self.play(Write(qm_right), run_time=0.3)
        self.play(GrowFromCenter(check_dot), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.4))


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
        headline = Text("a₀ and 3a₀/2", font=DISPLAY, font_size=36,
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
# B13 — Worked example: a₀ = 0.053 nm, 3a₀/2 = 0.079 nm (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B13_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B13", 20.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title banner
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("P(r) = (4/a₀³)r²e^{−2r/a₀}",
                          font=MONO, font_size=24, color=INK).move_to(UP * 3.7)

        # Step 1 box
        step1_box = Rectangle(width=12, height=0.9).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        step1_box.move_to(UP * 2.5)
        step1 = Text("Peak:  dP/dr = 0  →  r_peak = a₀ = 0.053 nm",
                     font=MONO, font_size=22, color=CRIMSON).move_to(UP * 2.5)

        # Arrow 1
        arr1 = Arrow(UP * 1.9, UP * 1.4, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 2 box
        step2_box = Rectangle(width=12, height=0.9).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        step2_box.move_to(UP * 0.9)
        step2 = Text("Mean:  ⟨r⟩ = ∫r·P(r)dr  =  3a₀/2  =  0.079 nm",
                     font=MONO, font_size=22, color=TEAL).move_to(UP * 0.9)

        # Arrow 2
        arr2 = Arrow(UP * 0.3, DOWN * 0.2, color=TEAL, buff=0, stroke_width=2,
                     max_tip_length_to_length_ratio=0.2)

        # Step 3: gap
        step3_box = Rectangle(width=12, height=0.9).set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        step3_box.move_to(DOWN * 0.7)
        step3 = Text("Gap = 0.079 − 0.053  =  0.026 nm",
                     font=MONO, font_size=22, color=INK).move_to(DOWN * 0.7)

        # Result box
        result_box = Rectangle(width=10, height=0.9).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 2.0)
        result = Text("Two numbers → no orbit → there is a cloud",
                      font=MONO, font_size=24, color=TEAL).move_to(DOWN * 2.0)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.0)

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
        answer = Text("The gap between peak and mean\nis the cloud. There is no orbit.",
                      font=DISPLAY, font_size=28, color=INK,
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
