"""vox_scenes.py — Tunneling: one angstrom, one order of magnitude
(vox-tunneling-exponent, slate cut, 16:9)
Color law: TEAL=transmitted/surviving wavefunction; CRIMSON=barrier/forbidden region;
           GOLD=log-scale meter readout.
Exclusions: no WKB derivation; no Gamow factor; anchored to T=e^(-2kL) and STM.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Move an STM tip one\nangstrom closer.\nThe current jumps tenfold.",
                        font=SERIF, color=INK, font_size=30, line_spacing=1.2)
        headline.move_to(DOWN * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B01") - 1.3)


# ── B02 CARD ──────────────────────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 2.2)
        headline = Text("Classical current changes\nsmoothly. Tunneling current\ncollapses by powers of ten.\nWhy?",
                        font=SERIF, color=INK, font_size=28, line_spacing=1.2)
        headline.move_to(UP * 0.3)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — decaying exponential in barrier ────────────────────────
class B03_DecayingExponential(Scene):
    def construct(self):
        """Show decaying exponential wavefunction inside a barrier."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Inside the barrier: a real decaying exponential",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Axes region
        ax_left = -5.5
        ax_right = 5.5
        ax_y = -1.5
        # Barrier region: x from -1.0 to 1.5
        bar_left = -1.0
        bar_right = 1.5

        # Ground line
        gnd = Line(np.array([ax_left, ax_y, 0.0]),
                   np.array([ax_right, ax_y, 0.0]),
                   color=INK, stroke_width=1.0)
        gnd.set_stroke(color=INK, width=1.0, opacity=1)

        # Barrier rectangle
        bar_rect = Rectangle(
            width=bar_right - bar_left, height=2.5,
            color=CRIMSON, fill_opacity=0.13
        )
        bar_rect.set_stroke(CRIMSON, width=1.5)
        bar_rect.move_to(np.array([(bar_left + bar_right) / 2.0, ax_y + 1.25, 0.0]))

        self.play(Create(gnd), Create(bar_rect), run_time=0.6)

        # Label for barrier
        bar_label = Text("barrier (E < V)", font=DISPLAY, color=CRIMSON, font_size=18)
        bar_label.move_to(np.array([(bar_left + bar_right) / 2.0, ax_y + 3.0, 0.0]))
        self.play(FadeIn(bar_label), run_time=0.4)

        # Oscillating wave on left (allowed region)
        n_pts = 80
        x_left = np.linspace(ax_left, bar_left, n_pts)
        y_left = 0.55 * np.sin(2.5 * x_left + 2.0) + ax_y + 0.55
        pts_left = [np.array([x_left[i], y_left[i], 0.0]) for i in range(n_pts)]
        wave_left = VMobject(color=TEAL, stroke_width=2.8, fill_opacity=0)
        wave_left.set_stroke(color=TEAL, width=2.8, opacity=1)
        wave_left.set_points_smoothly(pts_left)
        self.play(Create(wave_left), run_time=0.6)

        # Decaying exponential inside barrier
        kappa = 2.8  # visual scale
        x_bar = np.linspace(bar_left, bar_right, 60)
        amplitude_at_entry = 0.55  # match wave amplitude at bar_left
        y_bar = amplitude_at_entry * np.exp(-kappa * (x_bar - bar_left)) + ax_y
        # Clamp to ax_y
        y_bar = np.maximum(y_bar, ax_y + 0.02)
        pts_bar = [np.array([x_bar[i], y_bar[i], 0.0]) for i in range(len(x_bar))]
        wave_bar = VMobject(color=TEAL, stroke_width=2.8, fill_opacity=0)
        wave_bar.set_stroke(color=TEAL, width=2.8, opacity=1)
        wave_bar.set_points_smoothly(pts_bar)
        self.play(Create(wave_bar), run_time=0.7)

        # Small transmitted wave on right
        amp_transmitted = amplitude_at_entry * np.exp(-kappa * (bar_right - bar_left))
        x_right = np.linspace(bar_right, ax_right, n_pts)
        y_right = amp_transmitted * 0.8 * np.sin(2.5 * x_right + 1.5) + ax_y + amp_transmitted * 0.8
        pts_right = [np.array([x_right[i], y_right[i], 0.0]) for i in range(n_pts)]
        wave_right = VMobject(color=TEAL, stroke_width=2.8, fill_opacity=0)
        wave_right.set_stroke(color=TEAL, width=2.8, opacity=1)
        wave_right.set_points_smoothly(pts_right)
        self.play(Create(wave_right), run_time=0.5)

        # Label: psi ~ e^(-kappa*x)
        decay_eq = Text("psi ~ e^(-kappa x)  inside barrier",
                        font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        decay_eq.move_to(UP * 1.6)
        self.play(FadeIn(decay_eq), run_time=0.5)

        self.wait(_dur("B03") - 3.8)


# ── B04 THE PROBLEM — kappa definition and scale ─────────────────────────────
class B04_KappaScale(Scene):
    def construct(self):
        """Show kappa definition and its numerical value for 1eV barrier."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Kappa: the spatial decay rate",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Show formula: kappa = sqrt(2m(V-E)) / hbar
        kappa_def = Text("kappa = sqrt(2m(V-E)) / hbar",
                         font=SERIF, color=INK, font_size=28, slant=ITALIC)
        kappa_def.move_to(UP * 2.0)
        kappa_box = Rectangle(width=6.5, height=0.75, color=SLATE, fill_opacity=0.07)
        kappa_box.set_stroke(SLATE, width=1.2)
        kappa_box.move_to(UP * 2.0)
        self.play(Create(kappa_box), FadeIn(kappa_def), run_time=0.6)

        # Numerical value
        num_lbl = Text("For electrons, V-E = 1 eV:", font=DISPLAY, color=INK, font_size=22)
        num_lbl.move_to(UP * 0.8)
        val_lbl = Text("kappa ~ 5.1 nm^(-1)", font=MONO, color=TEAL, font_size=30)
        val_lbl.move_to(UP * 0.0)
        val_box = Rectangle(width=4.5, height=0.8, color=TEAL, fill_opacity=0.07)
        val_box.set_stroke(TEAL, width=1.5)
        val_box.move_to(UP * 0.0)

        self.play(FadeIn(num_lbl), run_time=0.5)
        self.play(Create(val_box), FadeIn(val_lbl), run_time=0.5)

        # Interpretation: 1/e fold every 0.2 nm
        interp = Text("One e-fold of decay every 0.2 nm", font=DISPLAY, color=TEAL, font_size=22)
        interp.move_to(DOWN * 1.2)
        self.play(FadeIn(interp), run_time=0.5)

        # Scale bar showing 0.2 nm = 2 angstroms
        scale_line = Line(np.array([-1.2, -2.4, 0.0]),
                          np.array([1.2, -2.4, 0.0]),
                          color=INK, stroke_width=1.5)
        scale_line.set_stroke(color=INK, width=1.5, opacity=1)
        tick_l = Line(np.array([-1.2, -2.6, 0.0]),
                      np.array([-1.2, -2.2, 0.0]),
                      color=INK, stroke_width=1.5)
        tick_l.set_stroke(color=INK, width=1.5, opacity=1)
        tick_r = Line(np.array([1.2, -2.6, 0.0]),
                      np.array([1.2, -2.2, 0.0]),
                      color=INK, stroke_width=1.5)
        tick_r.set_stroke(color=INK, width=1.5, opacity=1)
        scale_lbl = Text("0.2 nm  =  2 angstroms", font=DISPLAY, color=INK, font_size=20)
        scale_lbl.move_to(DOWN * 3.0)

        self.play(Create(scale_line), Create(tick_l), Create(tick_r), run_time=0.4)
        self.play(FadeIn(scale_lbl), run_time=0.4)

        self.wait(_dur("B04") - 3.8)


# ── B05 THE MECHANISM — T = e^(-2kL) formula ─────────────────────────────────
class B05_TransmissionFormula(Scene):
    def construct(self):
        """Show T = e^(-2*kappa*L) and explain the factor of two."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Transmission probability through the barrier",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Main formula
        formula = Text("T  =  e^(-2 kappa L)", font=SERIF, color=TEAL, font_size=42,
                       slant=ITALIC)
        formula.move_to(UP * 1.5)
        f_box = Rectangle(width=6.0, height=1.1, color=TEAL, fill_opacity=0.09)
        f_box.set_stroke(TEAL, width=2.0)
        f_box.move_to(UP * 1.5)
        self.play(Create(f_box), FadeIn(formula), run_time=0.7)

        # Explain components
        k_lbl = Text("kappa = decay rate in barrier",
                     font=DISPLAY, color=INK, font_size=20)
        k_lbl.move_to(UP * 0.3)

        L_lbl = Text("L = barrier width", font=DISPLAY, color=INK, font_size=20)
        L_lbl.move_to(DOWN * 0.2)

        two_lbl = Text("factor of 2: amplitude squared gives probability",
                       font=DISPLAY, color=INK, font_size=20)
        two_lbl.move_to(DOWN * 0.8)

        self.play(FadeIn(k_lbl), run_time=0.4)
        self.play(FadeIn(L_lbl), run_time=0.4)
        self.play(FadeIn(two_lbl), run_time=0.4)

        # Animated: show L growing, T shrinking
        gold_bar = Rectangle(width=7.0, height=0.6, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0, opacity=0)
        gold_bar.move_to(DOWN * 2.2)
        result_lbl = Text("Wider barrier = exponentially smaller T",
                          font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        result_lbl.move_to(DOWN * 2.2)
        self.play(FadeIn(gold_bar), FadeIn(result_lbl), run_time=0.5)

        self.wait(_dur("B05") - 3.4)


# ── B06 THE MECHANISM — one decade per 2.3 units ─────────────────────────────
class B06_DecadeRule(Scene):
    def construct(self):
        """Scan: each 2.3 units of 2kL drops T by factor of 10."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Every 2.3 units of 2kL: one order of magnitude",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Table showing 2kL values and T
        rows = [
            ("0.5",  "~0.61",  "substantial"),
            ("2",    "~0.14",  "partial"),
            ("4.6",  "~0.01",  "1%"),
            ("10",   "~4.5e-5", "very small"),
            ("20",   "~2e-9",  "negligible"),
        ]
        header_2kL = Text("2kL", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        header_T = Text("T", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        header_q = Text("regime", font=DISPLAY, color=SLATE, font_size=20, weight=BOLD)
        header_2kL.move_to(LEFT * 3.5 + UP * 2.0)
        header_T.move_to(UP * 2.0)
        header_q.move_to(RIGHT * 3.0 + UP * 2.0)
        self.play(FadeIn(header_2kL), FadeIn(header_T), FadeIn(header_q), run_time=0.4)

        for i, (v2kL, vT, vQ) in enumerate(rows):
            y = 1.0 - i * 0.85
            t_color = TEAL if i < 2 else (CRIMSON if i >= 3 else INK)
            col1 = Text(v2kL, font=MONO, color=INK, font_size=20)
            col1.move_to(LEFT * 3.5 + UP * y)
            col2 = Text(vT, font=MONO, color=t_color, font_size=20)
            col2.move_to(UP * y)
            col3 = Text(vQ, font=DISPLAY, color=SLATE, font_size=18)
            col3.move_to(RIGHT * 3.0 + UP * y)
            self.play(FadeIn(col1), FadeIn(col2), FadeIn(col3), run_time=0.3)

        # Rule highlight
        rule_bar = Rectangle(width=7.0, height=0.6, color=GOLD, fill_opacity=0.28)
        rule_bar.set_stroke(GOLD, width=0, opacity=0)
        rule_bar.move_to(DOWN * 2.8)
        rule_lbl = Text("e^(-2.303) = 0.1  ->  each +2.3 units divides T by 10",
                        font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        rule_lbl.move_to(DOWN * 2.8)
        self.play(FadeIn(rule_bar), FadeIn(rule_lbl), run_time=0.5)

        self.wait(_dur("B06") - 3.8)


# ── B07 THE MECHANISM — semi-log plot is a straight line ─────────────────────
class B07_SemiLogLine(Scene):
    def construct(self):
        """Semi-log plot of T vs L: straight line shows exponential law."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("On a semi-log scale, T vs L is a straight line",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Coordinate system — manual (avoid Axes complexity)
        origin = np.array([-4.5, -2.5, 0.0])
        x_end = np.array([4.5, -2.5, 0.0])
        y_end = np.array([-4.5, 3.0, 0.0])

        x_ax = Line(origin, x_end, color=INK, stroke_width=1.5)
        x_ax.set_stroke(color=INK, width=1.5, opacity=1)
        y_ax = Line(origin, y_end, color=INK, stroke_width=1.5)
        y_ax.set_stroke(color=INK, width=1.5, opacity=1)

        x_lbl = Text("barrier width L", font=DISPLAY, color=INK, font_size=18)
        x_lbl.move_to(np.array([0.0, -3.2, 0.0]))
        y_lbl = Text("log(T)", font=DISPLAY, color=INK, font_size=18)
        y_lbl.move_to(np.array([-5.5, 0.3, 0.0]))

        self.play(Create(x_ax), Create(y_ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.6)

        # Plot the straight line: log(T) = -2*kappa*L
        # Map: L in [0, 4] on x, log10(T) in [0, -10] on y
        n_pts = 60
        kappa_vis = 1.2  # visual kappa (scaled to fill plot nicely)
        L_vals = np.linspace(0, 4.0, n_pts)
        log_T_vals = -2 * kappa_vis * L_vals  # log scale: goes from 0 to -9.6

        x_scale = 2.1  # pixels per unit L
        y_scale = 0.56  # pixels per unit log10T

        line_pts = [origin + RIGHT * L_vals[i] * x_scale + UP * log_T_vals[i] * y_scale
                    for i in range(n_pts)]
        decay_line = VMobject(color=TEAL, stroke_width=3.0, fill_opacity=0)
        decay_line.set_stroke(color=TEAL, width=3.0, opacity=1)
        decay_line.set_points_smoothly(line_pts)

        self.play(Create(decay_line), run_time=1.2)

        # Y-axis ticks and labels at log10 = 0, -2, -4, -6, -8
        for log_val in [0, -2, -4, -6, -8]:
            tick_y = origin[1] + log_val * y_scale
            if tick_y < -2.5 + 5.2 and tick_y > -2.5:  # within axis range
                tick = Line(np.array([origin[0] - 0.15, tick_y, 0.0]),
                            np.array([origin[0] + 0.15, tick_y, 0.0]),
                            color=INK, stroke_width=1.0)
                tick.set_stroke(color=INK, width=1.0, opacity=1)
                t_lbl = Text(f"10^{log_val}", font=MONO, color=INK, font_size=14)
                t_lbl.move_to(np.array([origin[0] - 1.1, tick_y, 0.0]))
                self.play(Create(tick), FadeIn(t_lbl), run_time=0.15)

        # Slope annotation
        slope_lbl = Text("slope = -2 kappa", font=DISPLAY, color=TEAL, font_size=20)
        slope_lbl.move_to(np.array([1.5, 0.8, 0.0]))
        slope_box = Rectangle(width=3.8, height=0.6, color=TEAL, fill_opacity=0.07)
        slope_box.set_stroke(TEAL, width=1.2)
        slope_box.move_to(np.array([1.5, 0.8, 0.0]))
        self.play(Create(slope_box), FadeIn(slope_lbl), run_time=0.5)

        self.wait(_dur("B07") - 4.0)


# ── B08 THE IMPLICATION — STM resolution from sensitivity ────────────────────
class B08_STMResolution(Scene):
    def construct(self):
        """Show STM tip scanning over atoms; current changes by factor e per angstrom."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("STM: one angstrom of height = factor-e current change",
                     font=SERIF, color=INK, font_size=25, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Surface with atomic bumps
        surface_y = -1.8
        surface = Line(np.array([-5.5, surface_y, 0.0]),
                       np.array([5.5, surface_y, 0.0]),
                       color=INK, stroke_width=1.5)
        surface.set_stroke(color=INK, width=1.5, opacity=1)

        # Three atomic bumps
        bump_centers = [-3.0, 0.0, 3.0]
        bump_heights = [0.4, 0.65, 0.35]
        bumps = VGroup()
        for cx, h in zip(bump_centers, bump_heights):
            bump = Ellipse(width=1.0, height=h, color=INK, fill_opacity=0.25)
            bump.set_stroke(INK, width=1.0)
            bump.move_to(np.array([cx, surface_y + h / 2.0, 0.0]))
            bumps.add(bump)

        self.play(Create(surface), run_time=0.4)
        self.play(Create(bumps), run_time=0.6)

        # STM tip — triangle
        tip_cx = -3.0
        tip_cy = surface_y + bump_heights[0] + 0.9  # above the first bump
        tip_tri = Polygon(
            np.array([tip_cx, tip_cy + 0.5, 0.0]),
            np.array([tip_cx - 0.4, tip_cy + 0.9, 0.0]),
            np.array([tip_cx + 0.4, tip_cy + 0.9, 0.0]),
            color=SLATE, fill_opacity=0.5
        )
        tip_tri.set_stroke(SLATE, width=1.2)
        self.play(Create(tip_tri), run_time=0.5)

        # Current value label
        I_lbl = Text("I (current)", font=DISPLAY, color=TEAL, font_size=20)
        I_lbl.move_to(RIGHT * 3.5 + UP * 1.5)

        # Show tip moving over the bump and current changing
        # Move tip from -3 to 0 (over the big bump)
        def get_tip_y(cx_val):
            # Surface height at this x
            h = 0.0
            for bcx, bh in zip(bump_centers, bump_heights):
                dist = abs(cx_val - bcx)
                if dist < 0.6:
                    h = max(h, bh * (1 - dist / 0.6))
            return surface_y + h + 0.9

        tracker = ValueTracker(-3.0)

        def update_tip(tri):
            cx_val = tracker.get_value()
            tip_cy_new = get_tip_y(cx_val)
            tip_pts = [
                np.array([cx_val, tip_cy_new + 0.5, 0.0]),
                np.array([cx_val - 0.4, tip_cy_new + 0.9, 0.0]),
                np.array([cx_val + 0.4, tip_cy_new + 0.9, 0.0]),
            ]
            tri.set_points_as_corners(tip_pts)

        tip_tri.add_updater(update_tip)
        self.add(I_lbl)
        self.play(tracker.animate.set_value(3.0), run_time=2.5)
        tip_tri.remove_updater(update_tip)

        # Factor-e annotation
        e_lbl = Text("~e per angstrom of height change", font=DISPLAY,
                     color=TEAL, font_size=20)
        e_lbl.move_to(UP * 0.2)
        e_box = Rectangle(width=5.5, height=0.6, color=TEAL, fill_opacity=0.07)
        e_box.set_stroke(TEAL, width=1.2)
        e_box.move_to(UP * 0.2)
        self.play(Create(e_box), FadeIn(e_lbl), run_time=0.5)

        # Result: atomic resolution
        res_lbl = Text("Enough contrast to resolve single atoms",
                       font=DISPLAY, color=INK, font_size=20)
        res_lbl.move_to(DOWN * 1.0)
        self.play(FadeIn(res_lbl), run_time=0.4)

        self.wait(_dur("B08") - 5.9)


# ── B09 STILL·ai — STM image ─────────────────────────────────────────────────
class B09_STMImage(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        slate_box = Rectangle(width=12.0, height=6.5, color=SLATE, fill_opacity=0.12)
        slate_box.set_stroke(SLATE, width=1.5)
        slate_box.move_to(UP * 0.2)
        slate_lbl = Text("SLATE · ai image", font=DISPLAY, color=SLATE,
                         font_size=26, weight=BOLD)
        slate_lbl.move_to(UP * 0.2)
        caption = Text("STM tip over atomic surface — tunneling current decays exponentially with gap",
                       font=SERIF, color=INK, font_size=18, slant=ITALIC)
        caption.move_to(DOWN * 2.8)
        self.add(bg, slate_box, slate_lbl, caption)
        self.wait(_dur("B09"))


# ── B10 THE EXAMPLE — illustrative STM numbers ───────────────────────────────
class B10_IllustrativeSTM(Scene):
    def construct(self):
        """Illustrative calculation: kappa=10.8/nm, gap changes, current jumps 10x."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Illustrative: STM tip over copper surface",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        note = Text("(illustrative values)", font=DISPLAY, color=SLATE, font_size=18)
        note.move_to(UP * 2.5)
        self.play(FadeIn(title), FadeIn(note), run_time=0.5)

        # Given parameters
        p1 = Text("Barrier above electron energy: 4.5 eV", font=DISPLAY, color=INK, font_size=20)
        p1.move_to(UP * 1.6)
        p2 = Text("kappa ~ 10.8 nm^(-1)", font=MONO, color=INK, font_size=22)
        p2.move_to(UP * 0.9)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.5)

        # Two gap values and their T
        # gap 1: L = 0.3 nm -> 2kL = 6.5
        col_l = -3.5
        col_r = 2.5

        gap1_box = Rectangle(width=4.5, height=2.2, color=CRIMSON, fill_opacity=0.06)
        gap1_box.set_stroke(CRIMSON, width=1.2)
        gap1_box.move_to(LEFT * 3.5 + UP * -0.5)
        gap1_hdr = Text("Gap = 0.3 nm", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        gap1_hdr.move_to(LEFT * 3.5 + UP * 0.4)
        gap1_2kL = Text("2kL = 6.5", font=MONO, color=INK, font_size=20)
        gap1_2kL.move_to(LEFT * 3.5 + UP * -0.3)
        gap1_T = Text("T ~ 0.0015", font=MONO, color=CRIMSON, font_size=20)
        gap1_T.move_to(LEFT * 3.5 + UP * -1.0)
        self.play(Create(gap1_box), FadeIn(gap1_hdr), run_time=0.4)
        self.play(FadeIn(gap1_2kL), FadeIn(gap1_T), run_time=0.4)

        # gap 2: L = 0.2 nm -> 2kL = 4.3
        gap2_box = Rectangle(width=4.5, height=2.2, color=TEAL, fill_opacity=0.06)
        gap2_box.set_stroke(TEAL, width=1.2)
        gap2_box.move_to(RIGHT * 2.5 + UP * -0.5)
        gap2_hdr = Text("Gap = 0.2 nm", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        gap2_hdr.move_to(RIGHT * 2.5 + UP * 0.4)
        gap2_2kL = Text("2kL = 4.3", font=MONO, color=INK, font_size=20)
        gap2_2kL.move_to(RIGHT * 2.5 + UP * -0.3)
        gap2_T = Text("T ~ 0.013", font=MONO, color=TEAL, font_size=20)
        gap2_T.move_to(RIGHT * 2.5 + UP * -1.0)
        self.play(Create(gap2_box), FadeIn(gap2_hdr), run_time=0.4)
        self.play(FadeIn(gap2_2kL), FadeIn(gap2_T), run_time=0.4)

        # Arrow between them
        arr = Arrow(np.array([-1.5, -0.5, 0.0]),
                    np.array([0.3, -0.5, 0.0]),
                    buff=0, stroke_width=2.5, color=INK,
                    max_tip_length_to_length_ratio=0.20)
        arr_lbl = Text("1 angstrom closer", font=DISPLAY, color=INK, font_size=18)
        arr_lbl.move_to(UP * -0.1)
        self.play(Create(arr), FadeIn(arr_lbl), run_time=0.4)

        # Result: ~9x jump
        result = Text("~9x current jump", font=DISPLAY, color=TEAL,
                      font_size=24, weight=BOLD)
        result.move_to(DOWN * 2.3)
        result_box = Rectangle(width=4.5, height=0.7, color=TEAL, fill_opacity=0.08)
        result_box.set_stroke(TEAL, width=1.5)
        result_box.move_to(DOWN * 2.3)
        self.play(Create(result_box), FadeIn(result), run_time=0.5)

        self.wait(_dur("B10") - 4.8)


# ── B11 RECAP ─────────────────────────────────────────────────────────────────
class B11_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("T = e^(-2kL).\nOne angstrom.\nOne order of magnitude.",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.25)
        headline.move_to(DOWN * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B11") - 1.3)
