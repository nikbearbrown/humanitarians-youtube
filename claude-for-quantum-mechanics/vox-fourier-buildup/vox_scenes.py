"""vox_scenes.py — Build any shape out of pure waves
(vox-fourier-buildup, slate cut, 16:9).
Color law: TEAL=eigenstate/mode/amplitude; CRIMSON=partial sum/probability; GOLD=target fill; SLATE=axes.
Exclusions: no complex Fourier transform; no continuum limit; keep in particle-in-a-box frame.
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


def _axes(x_range=(-0.1, 1.1), y_range=(-1.3, 1.3), x_len=5.5, y_len=2.4, color=SLATE):
    ax = Axes(
        x_range=x_range, y_range=y_range,
        x_length=x_len, y_length=y_len,
        axis_config={"color": color, "stroke_width": 1.2, "include_tip": False,
                     "include_ticks": False},
    )
    return ax


def _sine_mode(ax, n, amplitude=0.9, color=TEAL, stroke_width=2.2, n_pts=200):
    """Plot sin(n*pi*x) on [0,1] with given amplitude."""
    x_vals = np.linspace(0, 1, n_pts)
    y_vals = amplitude * np.sin(n * np.pi * x_vals)
    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _partial_sum(ax, n_max, target_func, n_pts=200, color=CRIMSON, stroke_width=2.5):
    """Plot partial Fourier sum up to mode n_max for target_func on [0,1]."""
    x_vals = np.linspace(0, 1, n_pts)
    # Compute Fourier coefficients for target
    c = {}
    dx = 1.0 / n_pts
    for n in range(1, n_max + 1):
        mode_vals = np.sin(n * np.pi * x_vals)
        c[n] = 2.0 * np.sum(target_func(x_vals) * mode_vals) * dx

    y_sum = np.zeros(n_pts)
    for n in range(1, n_max + 1):
        y_sum += c[n] * np.sin(n * np.pi * x_vals)

    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_sum)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _target_curve(ax, func, n_pts=200, color=GOLD, stroke_width=1.5, fill=True):
    """Plot target function on [0,1]."""
    x_vals = np.linspace(0, 1, n_pts)
    y_vals = func(x_vals)
    pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_vals)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_as_corners(pts)
    return curve


def _triangular(x):
    """Triangular spike: normalized to peak ~0.9."""
    y = np.where(x < 0.5, 2 * x, 2 * (1 - x))
    return 0.9 * y


def _square_wave(x, amplitude=0.9):
    """Square wave: +amplitude for x<0.5, -amplitude for x>0.5."""
    return np.where(x < 0.5, amplitude, -amplitude)


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Give me enough sine waves\nand I'll draw you anything —\neven a square corner.",
                        font=SERIF, color=INK, font_size=30, line_spacing=1.2)
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
        headline = Text("Why do Fourier coefficients\nlook like Born-rule\nprobability amplitudes?",
                        font=SERIF, color=INK, font_size=32, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — energy modes in a box ───────────────────────────────────
class B03_EnergyModes(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Energy eigenstates: sine modes in a box",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        y_offsets = [1.6, 0.0, -1.6]
        n_labels = ["n = 1,  E₁", "n = 2,  E₂ = 4E₁", "n = 3,  E₃ = 9E₁"]
        colors = [TEAL, TEAL, TEAL]

        # State 2: n=1 mode
        ax1 = _axes(y_range=(-1.1, 1.1), x_len=5.0, y_len=1.2)
        ax1.move_to(LEFT * 1.5 + UP * y_offsets[0])
        mode1 = _sine_mode(ax1, n=1, amplitude=0.8, color=colors[0])
        lbl1 = Text(n_labels[0], font=DISPLAY, color=TEAL, font_size=18)
        lbl1.move_to(RIGHT * 4.2 + UP * y_offsets[0])
        self.play(Create(ax1), Create(mode1), FadeIn(lbl1), run_time=0.6)

        # State 3: n=2 mode
        ax2 = _axes(y_range=(-1.1, 1.1), x_len=5.0, y_len=1.2)
        ax2.move_to(LEFT * 1.5 + UP * y_offsets[1])
        mode2 = _sine_mode(ax2, n=2, amplitude=0.8, color=colors[1])
        lbl2 = Text(n_labels[1], font=DISPLAY, color=TEAL, font_size=18)
        lbl2.move_to(RIGHT * 4.2 + UP * y_offsets[1])
        self.play(Create(ax2), Create(mode2), FadeIn(lbl2), run_time=0.5)

        # State 4: n=3 mode
        ax3 = _axes(y_range=(-1.1, 1.1), x_len=5.0, y_len=1.2)
        ax3.move_to(LEFT * 1.5 + UP * y_offsets[2])
        mode3 = _sine_mode(ax3, n=3, amplitude=0.8, color=colors[2])
        lbl3 = Text(n_labels[2], font=DISPLAY, color=TEAL, font_size=18)
        lbl3.move_to(RIGHT * 4.2 + UP * y_offsets[2])
        self.play(Create(ax3), Create(mode3), FadeIn(lbl3), run_time=0.5)

        # State 5: summary separator line
        sep = Line(LEFT * 6.5 + DOWN * 2.8, RIGHT * 6.5 + DOWN * 2.8,
                   color=SLATE, stroke_width=0.8)
        key_lbl = Text("Each mode: definite energy, fixed wavelength",
                       font=DISPLAY, color=SLATE, font_size=18)
        key_lbl.move_to(DOWN * 3.2)
        self.play(Create(sep), FadeIn(key_lbl), run_time=0.5)

        self.wait(_dur("B03") - 2.6)


# ── B04 THE PROBLEM — target shape and coefficients ─────────────────────────
class B04_TargetAndCoefficients(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Arbitrary shape = sum of modes",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Target triangular spike
        ax_target = _axes(y_range=(-0.1, 1.1), x_len=4.5, y_len=2.2)
        ax_target.move_to(LEFT * 3.5 + UP * 0.9)
        tgt = _target_curve(ax_target, _triangular, color=GOLD, stroke_width=2.2)
        tgt_lbl = Text("target ψ(x)", font=DISPLAY, color=SLATE, font_size=18)
        tgt_lbl.move_to(LEFT * 3.5 + UP * 2.4)
        self.play(Create(ax_target), Create(tgt), FadeIn(tgt_lbl), run_time=0.6)

        # State 3: Coefficient bars
        bar_x_center = RIGHT * 2.5
        bar_title = Text("Coefficients  cₙ", font=DISPLAY, color=TEAL, font_size=19, weight=BOLD)
        bar_title.move_to(bar_x_center + UP * 2.4)
        self.play(FadeIn(bar_title), run_time=0.4)

        c_vals = [0.9, 0.0, 0.1, 0.0, 0.04]  # approximate for triangular (odd only)
        bar_y_base = 0.8
        bars = VGroup()
        bar_lbls = VGroup()
        for i, (c, n) in enumerate(zip(c_vals, [1, 2, 3, 4, 5])):
            bar_h = c * 1.6
            bar = Rectangle(width=0.5, height=bar_h + 0.001,
                            color=TEAL if c > 0.05 else SLATE,
                            fill_opacity=0.5 if c > 0.05 else 0.2)
            bar.set_stroke(TEAL if c > 0.05 else SLATE, width=1.2)
            bar.move_to(bar_x_center + RIGHT * (i * 0.75 - 1.5) + UP * (bar_y_base - 0.9 + bar_h / 2))
            lbl = Text(f"n={n}", font=DISPLAY, color=INK, font_size=14)
            lbl.move_to(bar_x_center + RIGHT * (i * 0.75 - 1.5) + UP * (bar_y_base - 0.9 - 0.4))
            bars.add(bar)
            bar_lbls.add(lbl)
        self.play(Create(bars), FadeIn(bar_lbls), run_time=0.6)

        # State 4: Arrow from target to bars
        arr = Arrow(LEFT * 1.2 + UP * 0.8, RIGHT * 0.8 + UP * 0.8,
                    buff=0, color=SLATE, stroke_width=2.0,
                    max_tip_length_to_length_ratio=0.15)
        self.play(Create(arr), run_time=0.4)

        # State 5: Key note at bottom
        note_bar = Rectangle(width=9.0, height=0.6, color=SLATE, fill_opacity=0.06)
        note_bar.set_stroke(SLATE, width=1.0)
        note_bar.move_to(DOWN * 2.8)
        note_lbl = Text("Even modes (n=2,4,...) contribute zero for symmetric triangular spike",
                        font=DISPLAY, color=SLATE, font_size=17)
        note_lbl.move_to(DOWN * 2.8)
        self.play(FadeIn(note_bar), FadeIn(note_lbl), run_time=0.5)

        self.wait(_dur("B04") - 3.0)


# ── B05 THE MECHANISM — projection = Born-rule amplitude ─────────────────────
class B05_BornRuleProjection(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Fourier coefficient = quantum inner product",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Projection formula
        proj_box = Rectangle(width=8.0, height=0.85, color=TEAL, fill_opacity=0.07)
        proj_box.set_stroke(TEAL, width=1.8)
        proj_box.move_to(UP * 2.1)
        proj_lbl = Text("cₙ = ⟨φₙ | ψ⟩ = ∫ φₙ*(x) ψ(x) dx",
                        font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        proj_lbl.move_to(UP * 2.1)
        self.play(Create(proj_box), FadeIn(proj_lbl), run_time=0.6)

        # State 3: Probability formula
        prob_box = Rectangle(width=5.5, height=0.75, color=CRIMSON, fill_opacity=0.07)
        prob_box.set_stroke(CRIMSON, width=1.8)
        prob_box.move_to(UP * 0.8)
        prob_lbl = Text("P(Eₙ) = |cₙ|²",
                        font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        prob_lbl.move_to(UP * 0.8)
        self.play(Create(prob_box), FadeIn(prob_lbl), run_time=0.6)

        # State 4: Explanatory note
        note1_box = Rectangle(width=9.5, height=0.65, color=INK, fill_opacity=0.05)
        note1_box.set_stroke(INK, width=1.0)
        note1_box.move_to(UP * -0.6)
        note1_lbl = Text("Fourier decomposition IS the energy measurement in QM",
                         font=DISPLAY, color=INK, font_size=21, weight=BOLD)
        note1_lbl.move_to(UP * -0.6)
        self.play(Create(note1_box), FadeIn(note1_lbl), run_time=0.5)

        # State 5: The projection picture (geometric intuition bar)
        geom_bar = Rectangle(width=9.5, height=0.6, color=SLATE, fill_opacity=0.06)
        geom_bar.set_stroke(SLATE, width=1.0)
        geom_bar.move_to(UP * -2.0)
        geom_lbl = Text("Project ψ onto φₙ: measure the overlap — that IS the Born rule",
                        font=DISPLAY, color=SLATE, font_size=18)
        geom_lbl.move_to(UP * -2.0)
        # Add a small arrow showing projection
        proj_arr = Line(UP * -1.2 + LEFT * 2.0, UP * -1.5 + LEFT * 0.5,
                        color=TEAL, stroke_width=2.0)
        self.play(Create(geom_bar), FadeIn(geom_lbl), Create(proj_arr), run_time=0.5)

        self.wait(_dur("B05") - 2.7)


# ── B06 THE MECHANISM — accumulating partial sums ───────────────────────────
class B06_PartialSumBuildup(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Modes accumulate toward the target",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        ax = _axes(y_range=(-1.1, 1.1), x_len=10.0, y_len=4.5)
        ax.move_to(UP * 0.2)
        self.play(Create(ax), run_time=0.4)

        # Target (GOLD faint, shown first)
        tgt = _target_curve(ax, _triangular, color=GOLD, stroke_width=1.5)
        tgt_lbl = Text("target", font=DISPLAY, color=SLATE, font_size=16)
        tgt_lbl.move_to(ax.c2p(0.55, 1.05))
        self.play(Create(tgt), FadeIn(tgt_lbl), run_time=0.4)

        # State 2: n=1 partial sum
        sum1 = _partial_sum(ax, 1, _triangular, color=CRIMSON, stroke_width=2.5)
        n1_lbl = Text("n=1", font=DISPLAY, color=CRIMSON, font_size=16)
        n1_lbl.move_to(ax.c2p(0.2, -0.9))
        self.play(Create(sum1), FadeIn(n1_lbl), run_time=0.5)

        # State 3: n=1+3 partial sum
        sum3 = _partial_sum(ax, 3, _triangular, color=CRIMSON, stroke_width=2.5)
        n3_lbl = Text("n=1+3", font=DISPLAY, color=CRIMSON, font_size=16)
        n3_lbl.move_to(ax.c2p(0.82, -0.9))
        self.play(Transform(sum1, sum3), FadeOut(n1_lbl), FadeIn(n3_lbl), run_time=0.7)

        # State 4: n=1+3+5 partial sum
        sum5 = _partial_sum(ax, 5, _triangular, color=TEAL, stroke_width=2.5)
        n5_lbl = Text("n≤5", font=DISPLAY, color=TEAL, font_size=16)
        n5_lbl.move_to(ax.c2p(0.15, -1.0))
        self.play(Transform(sum1, sum5), FadeOut(n3_lbl), FadeIn(n5_lbl), run_time=0.7)

        # State 5: convergence label
        conv_box = Rectangle(width=5.0, height=0.55, color=TEAL, fill_opacity=0.12)
        conv_box.set_stroke(TEAL, width=1.5)
        conv_box.move_to(DOWN * 3.0)
        conv_lbl = Text("Partial sum → target as more modes added",
                        font=DISPLAY, color=TEAL, font_size=17, weight=BOLD)
        conv_lbl.move_to(DOWN * 3.0)
        self.play(FadeIn(conv_box), FadeIn(conv_lbl), run_time=0.4)

        self.wait(_dur("B06") - 3.2)


# ── B07 THE IMPLICATION — square wave / Gibbs phenomenon ────────────────────
class B07_SquareWaveGibbs(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Square wave: Gibbs ringing at discontinuities",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        ax = _axes(y_range=(-1.2, 1.2), x_len=10.0, y_len=4.0)
        ax.move_to(UP * 0.3)
        self.play(Create(ax), run_time=0.4)

        # State 2: Target square wave
        sq_tgt = _target_curve(ax, _square_wave, color=GOLD, stroke_width=1.5)
        sq_lbl = Text("square wave", font=DISPLAY, color=SLATE, font_size=16)
        sq_lbl.move_to(ax.c2p(0.25, 1.05))
        self.play(Create(sq_tgt), FadeIn(sq_lbl), run_time=0.4)

        # State 3: n=1 (odd modes only)
        sum1 = _partial_sum(ax, 1, _square_wave, color=CRIMSON, stroke_width=2.5)
        n1_lbl2 = Text("n=1", font=DISPLAY, color=CRIMSON, font_size=16)
        n1_lbl2.move_to(ax.c2p(0.75, -1.05))
        self.play(Create(sum1), FadeIn(n1_lbl2), run_time=0.5)

        # State 4: n=1,3,5 (odd modes)
        sum5 = _partial_sum(ax, 5, _square_wave, color=CRIMSON, stroke_width=2.5)
        n5_lbl2 = Text("n≤5 (odd)", font=DISPLAY, color=CRIMSON, font_size=16)
        n5_lbl2.move_to(ax.c2p(0.15, -1.05))
        self.play(Transform(sum1, sum5), FadeOut(n1_lbl2), FadeIn(n5_lbl2), run_time=0.7)

        # State 5: Gibbs bracket annotation
        gibbs_box = Rectangle(width=1.2, height=0.5, color=SLATE, fill_opacity=0.06)
        gibbs_box.set_stroke(SLATE, width=1.2)
        gibbs_box.move_to(ax.c2p(0.5, 1.0))
        gibbs_lbl = Text("Gibbs\novershoot", font=DISPLAY, color=SLATE, font_size=14)
        gibbs_lbl.move_to(DOWN * 3.1 + LEFT * 3.0)
        self.play(Create(gibbs_box), FadeIn(gibbs_lbl), run_time=0.5)

        self.wait(_dur("B07") - 3.0)


# ── B08 THE IMPLICATION — completeness and normalization ─────────────────────
class B08_Completeness(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Completeness: any wavefunction decomposes into eigenstates",
                     font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Completeness equation
        comp_box = Rectangle(width=8.5, height=0.85, color=TEAL, fill_opacity=0.07)
        comp_box.set_stroke(TEAL, width=1.8)
        comp_box.move_to(UP * 2.1)
        comp_lbl = Text("ψ(x) = Σₙ cₙ φₙ(x)   (energy eigenbasis)",
                        font=SERIF, color=TEAL, font_size=26, slant=ITALIC)
        comp_lbl.move_to(UP * 2.1)
        self.play(Create(comp_box), FadeIn(comp_lbl), run_time=0.6)

        # State 3: Normalization constraint
        norm_box = Rectangle(width=6.0, height=0.75, color=CRIMSON, fill_opacity=0.07)
        norm_box.set_stroke(CRIMSON, width=1.8)
        norm_box.move_to(UP * 0.8)
        norm_lbl = Text("Σₙ |cₙ|² = 1   (probabilities sum to 1)",
                        font=SERIF, color=CRIMSON, font_size=26, slant=ITALIC)
        norm_lbl.move_to(UP * 0.8)
        self.play(Create(norm_box), FadeIn(norm_lbl), run_time=0.6)

        # State 4: QM content note
        qm_box = Rectangle(width=9.5, height=0.65, color=INK, fill_opacity=0.05)
        qm_box.set_stroke(INK, width=1.0)
        qm_box.move_to(UP * -0.6)
        qm_lbl = Text("Fourier series is QM in a box — not just an analogy",
                      font=DISPLAY, color=INK, font_size=21, weight=BOLD)
        qm_lbl.move_to(UP * -0.6)
        self.play(Create(qm_box), FadeIn(qm_lbl), run_time=0.5)

        # State 5: Parseval line
        parseval_bar = Rectangle(width=9.5, height=0.6, color=SLATE, fill_opacity=0.06)
        parseval_bar.set_stroke(SLATE, width=1.0)
        parseval_bar.move_to(UP * -2.1)
        parseval_lbl = Text("Parseval's theorem = quantum normalization condition",
                            font=DISPLAY, color=SLATE, font_size=18)
        parseval_lbl.move_to(UP * -2.1)
        self.play(Create(parseval_bar), FadeIn(parseval_lbl), run_time=0.5)

        self.wait(_dur("B08") - 2.7)


# ── B09 THE EXAMPLE — triangular spike probabilities ─────────────────────────
class B09_TriangularSpike(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Triangular spike: 99% in the ground state",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 2: Formula for coefficients
        coeff_box = Rectangle(width=8.0, height=0.75, color=TEAL, fill_opacity=0.07)
        coeff_box.set_stroke(TEAL, width=1.5)
        coeff_box.move_to(UP * 2.1)
        coeff_lbl = Text("cₙ ∝ (8/n²π²) sin(nπ/2)   →   zero for all even n",
                         font=DISPLAY, color=TEAL, font_size=20)
        coeff_lbl.move_to(UP * 2.1)
        self.play(Create(coeff_box), FadeIn(coeff_lbl), run_time=0.6)

        # State 3: Table header + n=1 row
        hdr_box = Rectangle(width=6.0, height=0.55, color=SLATE, fill_opacity=0.12)
        hdr_box.set_stroke(SLATE, width=1.2)
        hdr_box.move_to(UP * 0.9)
        hdr_lbl = Text("mode n      |cₙ|²      P(Eₙ)", font=DISPLAY, color=SLATE, font_size=19)
        hdr_lbl.move_to(UP * 0.9)
        self.play(Create(hdr_box), FadeIn(hdr_lbl), run_time=0.4)

        row1_box = Rectangle(width=6.0, height=0.55, color=TEAL, fill_opacity=0.12)
        row1_box.set_stroke(TEAL, width=1.5)
        row1_box.move_to(UP * 0.1)
        row1_lbl = Text("  n = 1          0.987      99%", font=DISPLAY, color=TEAL, font_size=19, weight=BOLD)
        row1_lbl.move_to(UP * 0.1)
        self.play(Create(row1_box), FadeIn(row1_lbl), run_time=0.5)

        # State 4: n=3, n=5 rows
        row3_box = Rectangle(width=6.0, height=0.55, color=CRIMSON, fill_opacity=0.07)
        row3_box.set_stroke(CRIMSON, width=1.2)
        row3_box.move_to(UP * -0.7)
        row3_lbl = Text("  n = 3          0.012       1%", font=DISPLAY, color=CRIMSON, font_size=19)
        row3_lbl.move_to(UP * -0.7)
        row5_box = Rectangle(width=6.0, height=0.55, color=CRIMSON, fill_opacity=0.07)
        row5_box.set_stroke(CRIMSON, width=1.2)
        row5_box.move_to(UP * -1.4)
        row5_lbl = Text("  n = 5          0.001      <1%", font=DISPLAY, color=CRIMSON, font_size=19)
        row5_lbl.move_to(UP * -1.4)
        self.play(Create(row3_box), FadeIn(row3_lbl), Create(row5_box), FadeIn(row5_lbl), run_time=0.5)

        # State 5: conclusion bar
        concl_bar = Rectangle(width=8.0, height=0.55, color=GOLD, fill_opacity=0.28)
        concl_bar.set_stroke(GOLD, width=0)
        concl_bar.move_to(DOWN * 2.6)
        concl_lbl = Text("A triangular spike is almost entirely the ground state",
                         font=DISPLAY, color=INK, font_size=19, weight=BOLD)
        concl_lbl.move_to(DOWN * 2.6)
        self.play(FadeIn(concl_bar), FadeIn(concl_lbl), run_time=0.5)

        self.wait(_dur("B09") - 3.0)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Fourier modes = eigenstates.\nCoefficients = amplitudes.\nBuilding shapes = superposition.",
                        font=SERIF, color=INK, font_size=26, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
