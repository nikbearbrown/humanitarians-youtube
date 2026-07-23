"""vox_scenes.py — A packet spreads because its fast parts run ahead
(vox-packet-spread, slate cut, 16:9).
Color law: TEAL=low-momentum (slow) components; CRIMSON=high-momentum (fast) components;
           GOLD=packet envelope highlight; SLATE=axes/structure.
Exclusions: no Schrodinger time evolution derivation; no relativistic case.
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


def _gaussian(x, center=0.0, sigma=1.0, amplitude=1.0):
    return amplitude * np.exp(-((x - center) ** 2) / (2 * sigma ** 2))


def _gaussian_packet(ax, center=0.0, sigma=1.0, amplitude=0.9, k0=3.0,
                     color=TEAL, stroke_width=2.2, n_pts=300):
    """Plot a Gaussian wave packet: envelope * cos(k0*x)."""
    x_vals = np.linspace(-7, 7, n_pts)
    envelope = _gaussian(x_vals, center, sigma, amplitude)
    y_vals = envelope * np.cos(k0 * (x_vals - center))
    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _gaussian_envelope(ax, center=0.0, sigma=1.0, amplitude=0.9,
                        color=GOLD, stroke_width=1.5, n_pts=200):
    """Plot just the Gaussian envelope (no oscillation)."""
    x_vals = np.linspace(-7, 7, n_pts)
    y_vals = _gaussian(x_vals, center, sigma, amplitude)
    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _momentum_gaussian(ax, p0=0.0, sigma_p=0.5, amplitude=0.9,
                        color=CRIMSON, stroke_width=2.2, n_pts=200):
    """Plot Gaussian in momentum space."""
    p_vals = np.linspace(-3, 3, n_pts)
    y_vals = _gaussian(p_vals, p0, sigma_p, amplitude)
    pts = [ax.c2p(p, y) for p, y in zip(p_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _axes_simple(x_range=(-6.5, 6.5), y_range=(-1.1, 1.1), x_len=6.0, y_len=2.4, color=SLATE):
    ax = Axes(
        x_range=x_range, y_range=y_range,
        x_length=x_len, y_length=y_len,
        axis_config={"color": color, "stroke_width": 1.2, "include_tip": False,
                     "include_ticks": False},
    )
    return ax


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("A quantum particle can't hold its shape.\nThe narrower you make it,\nthe faster it smears.",
                        font=SERIF, color=INK, font_size=24, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B01") - 1.3)


# ── B02 CARD ──────────────────────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Narrow packet = wide momentum range\n= faster spreading. Why?",
                        font=SERIF, color=INK, font_size=32, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — Gaussian packet and its Fourier pair ───────────────────
class B03_GaussianPair(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Position Gaussian ↔ Momentum Gaussian",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Position-space Gaussian
        ax_x = _axes_simple(x_range=(-3.5, 3.5), y_range=(-0.1, 1.1), x_len=5.5, y_len=2.2)
        ax_x.move_to(LEFT * 3.2 + UP * 0.8)
        psi_curve = _gaussian_envelope(ax_x, center=0.0, sigma=0.8, color=TEAL)
        x_lbl = Text("ψ(x, 0)", font=DISPLAY, color=TEAL, font_size=19, slant=ITALIC)
        x_lbl.move_to(LEFT * 3.2 + UP * 2.3)
        dx_line = Line(ax_x.c2p(-0.8, 0.6), ax_x.c2p(0.8, 0.6), color=TEAL, stroke_width=2.0)
        dx_lbl = Text("Δx", font=DISPLAY, color=TEAL, font_size=17, slant=ITALIC)
        dx_lbl.move_to(ax_x.c2p(0.0, 0.7))
        self.play(Create(ax_x), Create(psi_curve), FadeIn(x_lbl), run_time=0.6)
        self.play(Create(dx_line), FadeIn(dx_lbl), run_time=0.4)

        # State 3: Momentum-space Gaussian
        ax_p = _axes_simple(x_range=(-3.5, 3.5), y_range=(-0.1, 1.1), x_len=5.5, y_len=2.2)
        ax_p.move_to(RIGHT * 3.2 + UP * 0.8)
        phi_curve = _momentum_gaussian(ax_p, p0=0.0, sigma_p=1.5, color=CRIMSON)
        p_lbl = Text("φ(p)", font=DISPLAY, color=CRIMSON, font_size=19, slant=ITALIC)
        p_lbl.move_to(RIGHT * 3.2 + UP * 2.3)
        dp_line = Line(ax_p.c2p(-1.5, 0.6), ax_p.c2p(1.5, 0.6), color=CRIMSON, stroke_width=2.0)
        dp_lbl = Text("Δp", font=DISPLAY, color=CRIMSON, font_size=17, slant=ITALIC)
        dp_lbl.move_to(ax_p.c2p(0.0, 0.7))
        self.play(Create(ax_p), Create(phi_curve), FadeIn(p_lbl), run_time=0.5)
        self.play(Create(dp_line), FadeIn(dp_lbl), run_time=0.4)

        # State 4: Fourier pair relationship
        rel_box = Rectangle(width=5.0, height=0.65, color=SLATE, fill_opacity=0.08)
        rel_box.set_stroke(SLATE, width=1.2)
        rel_box.move_to(UP * -1.5)
        rel_lbl = Text("Δx · Δp = ℏ/2   (minimum uncertainty)",
                       font=DISPLAY, color=SLATE, font_size=19)
        rel_lbl.move_to(UP * -1.5)
        self.play(Create(rel_box), FadeIn(rel_lbl), run_time=0.5)

        # State 5: Narrow position = wide momentum annotation
        note_bar = Rectangle(width=9.5, height=0.6, color=INK, fill_opacity=0.05)
        note_bar.set_stroke(INK, width=1.0)
        note_bar.move_to(UP * -2.6)
        note_lbl = Text("Narrow position → wide momentum range",
                        font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        note_lbl.move_to(UP * -2.6)
        self.play(Create(note_bar), FadeIn(note_lbl), run_time=0.5)

        self.wait(_dur("B03") - 2.9)


# ── B04 THE PROBLEM — components move at different speeds ─────────────────────
class B04_ComponentSpeeds(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Each momentum component: its own speed",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Horizontal axis with components
        ax = _axes_simple(x_range=(-6.5, 6.5), y_range=(-1.1, 1.1), x_len=11.0, y_len=1.5)
        ax.move_to(UP * 1.0)
        self.play(Create(ax), run_time=0.4)

        # Low-k (slow) component
        x_vals = np.linspace(-6.5, 6.5, 400)
        y_slow = 0.6 * np.cos(1.5 * x_vals) * _gaussian(x_vals, -2.0, 1.5, 1.0)
        pts_slow = [ax.c2p(x, y) for x, y in zip(x_vals, y_slow)]
        slow_curve = VMobject(color=TEAL, stroke_width=2.0)
        slow_curve.set_points_as_corners(pts_slow)
        slow_lbl = Text("low p (slow)", font=DISPLAY, color=TEAL, font_size=17)
        slow_lbl.move_to(LEFT * 3.5 + UP * 2.4)
        self.play(Create(slow_curve), FadeIn(slow_lbl), run_time=0.5)

        # High-k (fast) component
        y_fast = 0.6 * np.cos(4.0 * x_vals) * _gaussian(x_vals, 1.5, 1.2, 1.0)
        pts_fast = [ax.c2p(x, y) for x, y in zip(x_vals, y_fast)]
        fast_curve = VMobject(color=CRIMSON, stroke_width=2.0)
        fast_curve.set_points_as_corners(pts_fast)
        fast_lbl = Text("high p (fast)", font=DISPLAY, color=CRIMSON, font_size=17)
        fast_lbl.move_to(RIGHT * 2.5 + UP * 2.4)
        self.play(Create(fast_curve), FadeIn(fast_lbl), run_time=0.5)

        # State 4: Velocity arrows
        slow_arr = Arrow(LEFT * 3.5 + UP * -0.6, LEFT * 1.5 + UP * -0.6,
                         buff=0, color=TEAL, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.18)
        slow_v_lbl = Text("v = p_low/m", font=DISPLAY, color=TEAL, font_size=16)
        slow_v_lbl.move_to(LEFT * 2.5 + UP * -1.0)
        fast_arr = Arrow(RIGHT * 1.0 + UP * -0.6, RIGHT * 4.5 + UP * -0.6,
                         buff=0, color=CRIMSON, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.18)
        fast_v_lbl = Text("v = p_high/m (faster!)", font=DISPLAY, color=CRIMSON, font_size=16)
        fast_v_lbl.move_to(RIGHT * 2.8 + UP * -1.0)
        self.play(Create(slow_arr), FadeIn(slow_v_lbl), Create(fast_arr), FadeIn(fast_v_lbl), run_time=0.5)

        # State 5: Key separation note
        sep_bar = Rectangle(width=9.0, height=0.6, color=GOLD, fill_opacity=0.2)
        sep_bar.set_stroke(GOLD, width=0)
        sep_bar.move_to(DOWN * 2.4)
        sep_lbl = Text("Different speeds → components separate → packet broadens",
                       font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        sep_lbl.move_to(DOWN * 2.4)
        self.play(FadeIn(sep_bar), FadeIn(sep_lbl), run_time=0.5)

        self.wait(_dur("B04") - 2.9)


# ── B05 THE MECHANISM — spreading animation ──────────────────────────────────
class B05_SpreadingAnimation(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Fast components run ahead; slow ones lag behind",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: t=0 packet (tight)
        ax = _axes_simple(x_range=(-6.5, 6.5), y_range=(-1.1, 1.1), x_len=11.0, y_len=3.5)
        ax.move_to(UP * 0.3)
        self.play(Create(ax), run_time=0.4)

        pkt0 = _gaussian_packet(ax, center=0.0, sigma=0.8, amplitude=0.9, k0=3.5, color=TEAL)
        env0 = _gaussian_envelope(ax, center=0.0, sigma=0.8, amplitude=0.9, color=GOLD)
        t0_lbl = Text("t = 0", font=DISPLAY, color=TEAL, font_size=18)
        t0_lbl.move_to(ax.c2p(0.0, 1.05))
        self.play(Create(pkt0), Create(env0), FadeIn(t0_lbl), run_time=0.5)

        # State 3: t=1 packet (spreading)
        pkt1 = _gaussian_packet(ax, center=1.5, sigma=2.0, amplitude=0.4, k0=3.5, color=CRIMSON)
        env1 = _gaussian_envelope(ax, center=1.5, sigma=2.0, amplitude=0.4, color=GOLD)
        t1_lbl = Text("t = T", font=DISPLAY, color=CRIMSON, font_size=18)
        t1_lbl.move_to(ax.c2p(1.5, 0.55))
        self.play(
            Transform(pkt0, pkt1), Transform(env0, env1),
            FadeOut(t0_lbl), FadeIn(t1_lbl),
            run_time=0.9,
        )

        # State 4: Fast/slow component annotations
        fast_box = Rectangle(width=2.2, height=0.5, color=CRIMSON, fill_opacity=0.08)
        fast_box.set_stroke(CRIMSON, width=1.2)
        fast_box.move_to(ax.c2p(3.5, -0.85))
        fast_note = Text("fast (CRIMSON)\nrun ahead", font=DISPLAY, color=CRIMSON, font_size=14)
        fast_note.move_to(ax.c2p(3.5, -0.75))
        slow_box = Rectangle(width=2.2, height=0.5, color=TEAL, fill_opacity=0.08)
        slow_box.set_stroke(TEAL, width=1.2)
        slow_box.move_to(ax.c2p(-2.0, -0.85))
        slow_note = Text("slow (TEAL)\nlag behind", font=DISPLAY, color=TEAL, font_size=14)
        slow_note.move_to(ax.c2p(-2.0, -0.75))
        self.play(FadeIn(fast_box), FadeIn(fast_note), FadeIn(slow_box), FadeIn(slow_note), run_time=0.5)

        # State 5: Width annotation
        width_line = Line(ax.c2p(-1.5, 0.22), ax.c2p(4.5, 0.22), color=SLATE, stroke_width=1.5)
        width_lbl = Text("Δx(T) > Δx(0)", font=DISPLAY, color=SLATE, font_size=18)
        width_lbl.move_to(DOWN * 2.8)
        self.play(Create(width_line), FadeIn(width_lbl), run_time=0.4)

        self.wait(_dur("B05") - 3.2)


# ── B06 THE MECHANISM — spreading formula ────────────────────────────────────
class B06_SpreadingFormula(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Exact spreading formula",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Formula
        form_box = Rectangle(width=9.5, height=0.85, color=TEAL, fill_opacity=0.07)
        form_box.set_stroke(TEAL, width=1.8)
        form_box.move_to(UP * 2.1)
        form_lbl = Text("Δx(t) = Δx(0) · √[1 + (tℏ / m·Δx(0)²)²]",
                        font=SERIF, color=TEAL, font_size=25, slant=ITALIC)
        form_lbl.move_to(UP * 2.1)
        self.play(Create(form_box), FadeIn(form_lbl), run_time=0.6)

        # State 3: Plot the spreading curve
        ax = Axes(
            x_range=(0, 4, 1), y_range=(0, 3.5, 1),
            x_length=7.0, y_length=2.8,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "include_ticks": True},
        )
        ax.move_to(UP * -0.8)
        t_lbl = Text("t (in units of t₀)", font=DISPLAY, color=SLATE, font_size=14)
        t_lbl.move_to(ax.c2p(4.0, -0.5))
        dx_ax_lbl = Text("Δx(t) / Δx(0)", font=DISPLAY, color=SLATE, font_size=14)
        dx_ax_lbl.move_to(ax.c2p(-0.8, 3.0))

        t_vals = np.linspace(0, 4, 200)
        y_vals = np.sqrt(1 + t_vals ** 2)
        pts = [ax.c2p(t, y) for t, y in zip(t_vals, y_vals)]
        spread_curve = VMobject(color=TEAL, stroke_width=2.5)
        spread_curve.set_points_as_corners(pts)
        self.play(Create(ax), FadeIn(t_lbl), FadeIn(dx_ax_lbl), Create(spread_curve), run_time=0.6)

        # State 4: t0 marker
        t0_dot = Dot(ax.c2p(1, np.sqrt(2)), color=GOLD, radius=0.12)
        t0_note = Text("t = t₀: Δx = √2·Δx(0)", font=DISPLAY, color=SLATE, font_size=15)
        t0_note.move_to(ax.c2p(2.5, 1.6))
        self.play(FadeIn(t0_dot), FadeIn(t0_note), run_time=0.4)

        # State 5: Large-t asymptote
        asym_box = Rectangle(width=6.0, height=0.55, color=CRIMSON, fill_opacity=0.07)
        asym_box.set_stroke(CRIMSON, width=1.2)
        asym_box.move_to(DOWN * 3.0)
        asym_lbl = Text("Large t: Δx(t) → tℏ / (m·Δx(0))  — linear growth",
                        font=DISPLAY, color=CRIMSON, font_size=17)
        asym_lbl.move_to(DOWN * 3.0)
        self.play(FadeIn(asym_box), FadeIn(asym_lbl), run_time=0.5)

        self.wait(_dur("B06") - 3.1)


# ── B07 THE IMPLICATION — narrower spreads faster ────────────────────────────
class B07_NarrowerFaster(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Narrower initial packet spreads faster",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Two spreading curves
        ax = Axes(
            x_range=(0, 4, 1), y_range=(0, 5.5, 1),
            x_length=8.0, y_length=3.5,
            axis_config={"color": SLATE, "stroke_width": 1.2, "include_tip": False,
                         "include_ticks": True},
        )
        ax.move_to(UP * 0.0)
        t_lbl = Text("time", font=DISPLAY, color=SLATE, font_size=14)
        t_lbl.move_to(ax.c2p(4.2, -0.4))

        t_vals = np.linspace(0, 4, 200)
        # Narrow: t0=1 => scales as sqrt(1+t^2)
        y_narrow = np.sqrt(1 + t_vals ** 2)
        # Wide: t0=3 => much slower growth (Δx0 larger, so t0 larger, grows slower)
        y_wide = np.sqrt(1 + (t_vals / 3) ** 2)

        pts_narrow = [ax.c2p(t, y) for t, y in zip(t_vals, y_narrow)]
        pts_wide = [ax.c2p(t, y) for t, y in zip(t_vals, y_wide)]

        curve_narrow = VMobject(color=CRIMSON, stroke_width=2.5)
        curve_narrow.set_points_as_corners(pts_narrow)
        curve_wide = VMobject(color=TEAL, stroke_width=2.5)
        curve_wide.set_points_as_corners(pts_wide)

        n_lbl = Text("narrow Δx₀", font=DISPLAY, color=CRIMSON, font_size=16)
        n_lbl.move_to(ax.c2p(3.0, 5.0))
        w_lbl = Text("wide Δx₀", font=DISPLAY, color=TEAL, font_size=16)
        w_lbl.move_to(ax.c2p(3.5, 1.7))

        self.play(Create(ax), FadeIn(t_lbl), run_time=0.4)
        self.play(Create(curve_narrow), FadeIn(n_lbl), run_time=0.5)
        self.play(Create(curve_wide), FadeIn(w_lbl), run_time=0.5)

        # State 4: Explanation box
        expl_box = Rectangle(width=9.5, height=0.65, color=INK, fill_opacity=0.05)
        expl_box.set_stroke(INK, width=1.0)
        expl_box.move_to(DOWN * 2.5)
        expl_lbl = Text("Narrow Δx₀ → large Δp → large spread of speeds → fast spreading",
                        font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        expl_lbl.move_to(DOWN * 2.5)
        self.play(Create(expl_box), FadeIn(expl_lbl), run_time=0.5)

        # State 5: Key constraint
        key_bar = Rectangle(width=8.5, height=0.55, color=SLATE, fill_opacity=0.07)
        key_bar.set_stroke(SLATE, width=1.0)
        key_bar.move_to(DOWN * 3.3)
        key_lbl = Text("Squeezing a particle in space = forcing it to run away faster",
                       font=DISPLAY, color=SLATE, font_size=17)
        key_lbl.move_to(DOWN * 3.3)
        self.play(FadeIn(key_bar), FadeIn(key_lbl), run_time=0.4)

        self.wait(_dur("B07") - 2.8)


# ── B08 THE IMPLICATION — classical analogy ───────────────────────────────────
class B08_ClassicalAnalogy(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Same physics: any dispersive wave spreads",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: QM panel
        qm_box = Rectangle(width=4.5, height=2.8, color=TEAL, fill_opacity=0.06)
        qm_box.set_stroke(TEAL, width=1.5)
        qm_box.move_to(LEFT * 3.0 + UP * 0.7)
        qm_title = Text("QUANTUM", font=DISPLAY, color=TEAL, font_size=18, weight=BOLD)
        qm_title.move_to(LEFT * 3.0 + UP * 2.0)
        qm_e1 = Text("Electron wave packet", font=DISPLAY, color=TEAL, font_size=16)
        qm_e1.move_to(LEFT * 3.0 + UP * 1.2)
        qm_e2 = Text("v = p/m (each component)", font=DISPLAY, color=TEAL, font_size=15)
        qm_e2.move_to(LEFT * 3.0 + UP * 0.5)
        qm_e3 = Text("Δp = ℏ/Δx forces spreading", font=DISPLAY, color=TEAL, font_size=15)
        qm_e3.move_to(LEFT * 3.0 + DOWN * 0.2)
        self.play(Create(qm_box), FadeIn(qm_title), FadeIn(qm_e1), FadeIn(qm_e2), FadeIn(qm_e3), run_time=0.6)

        # State 3: Classical panel
        cl_box = Rectangle(width=4.5, height=2.8, color=SLATE, fill_opacity=0.06)
        cl_box.set_stroke(SLATE, width=1.5)
        cl_box.move_to(RIGHT * 3.0 + UP * 0.7)
        cl_title = Text("CLASSICAL", font=DISPLAY, color=SLATE, font_size=18, weight=BOLD)
        cl_title.move_to(RIGHT * 3.0 + UP * 2.0)
        cl_e1 = Text("Water wave pulse", font=DISPLAY, color=SLATE, font_size=16)
        cl_e1.move_to(RIGHT * 3.0 + UP * 1.2)
        cl_e2 = Text("v = ω/k (each frequency)", font=DISPLAY, color=SLATE, font_size=15)
        cl_e2.move_to(RIGHT * 3.0 + UP * 0.5)
        cl_e3 = Text("Different speeds → spreading", font=DISPLAY, color=SLATE, font_size=15)
        cl_e3.move_to(RIGHT * 3.0 + DOWN * 0.2)
        self.play(Create(cl_box), FadeIn(cl_title), FadeIn(cl_e1), FadeIn(cl_e2), FadeIn(cl_e3), run_time=0.5)

        # State 4: Common label
        common_arr = Line(LEFT * 0.8 + UP * 0.7, RIGHT * 0.8 + UP * 0.7,
                          color=INK, stroke_width=1.5)
        common_lbl = Text("kinematics +\nFourier", font=DISPLAY, color=INK, font_size=17, weight=BOLD)
        common_lbl.move_to(UP * 0.7)
        self.play(Create(common_arr), FadeIn(common_lbl), run_time=0.5)

        # State 5: Bottom conclusion
        concl_bar = Rectangle(width=8.5, height=0.55, color=GOLD, fill_opacity=0.28)
        concl_bar.set_stroke(GOLD, width=0)
        concl_bar.move_to(DOWN * 2.5)
        concl_lbl = Text("Not a quantum mystery — a wave fact",
                         font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        concl_lbl.move_to(DOWN * 2.5)
        self.play(FadeIn(concl_bar), FadeIn(concl_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.7)


# ── B09 THE EXAMPLE — numerical estimates ─────────────────────────────────────
class B09_NumericalExample(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("1 nm electron: spreading in femtoseconds",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Given
        hdr_box = Rectangle(width=7.5, height=0.6, color=SLATE, fill_opacity=0.12)
        hdr_box.set_stroke(SLATE, width=1.2)
        hdr_box.move_to(UP * 2.1)
        hdr_lbl = Text("Given: electron localized to Δx₀ = 1 nm",
                       font=DISPLAY, color=SLATE, font_size=20)
        hdr_lbl.move_to(UP * 2.1)
        self.play(Create(hdr_box), FadeIn(hdr_lbl), run_time=0.5)

        # State 3: Momentum spread
        dp_box = Rectangle(width=7.5, height=0.6, color=TEAL, fill_opacity=0.07)
        dp_box.set_stroke(TEAL, width=1.5)
        dp_box.move_to(UP * 1.1)
        dp_lbl = Text("Δp = ℏ/Δx₀  ~  0.1 eV/c",
                      font=DISPLAY, color=TEAL, font_size=20)
        dp_lbl.move_to(UP * 1.1)
        self.play(Create(dp_box), FadeIn(dp_lbl), run_time=0.5)

        # State 4: Timescale
        ts_box = Rectangle(width=7.5, height=0.6, color=CRIMSON, fill_opacity=0.07)
        ts_box.set_stroke(CRIMSON, width=1.5)
        ts_box.move_to(UP * 0.1)
        ts_lbl = Text("t_spread = m·Δx₀² / ℏ  ~  8.6 femtoseconds",
                      font=DISPLAY, color=CRIMSON, font_size=20)
        ts_lbl.move_to(UP * 0.1)
        self.play(Create(ts_box), FadeIn(ts_lbl), run_time=0.5)

        # State 5: Interpretation
        int_bar = Rectangle(width=8.5, height=0.55, color=GOLD, fill_opacity=0.28)
        int_bar.set_stroke(GOLD, width=0)
        int_bar.move_to(DOWN * 1.2)
        int_lbl = Text("Within ~10 fs, packet has doubled in width",
                       font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        int_lbl.move_to(DOWN * 1.2)
        self.play(FadeIn(int_bar), FadeIn(int_lbl), run_time=0.5)

        # Scale note
        scale_lbl = Text("1 nm = width of ~3 atoms. Spreading = ultra-fast quantum kinematics.",
                         font=DISPLAY, color=SLATE, font_size=16)
        scale_lbl.move_to(DOWN * 2.5)
        self.play(FadeIn(scale_lbl), run_time=0.4)

        self.wait(_dur("B09") - 2.9)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Narrow in x = wide in p.\nWide in p = components separate.\nComponents separate = spreading.",
                        font=SERIF, color=INK, font_size=25, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
