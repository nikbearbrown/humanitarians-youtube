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


class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Why Uncertainty Isn't About\nBumping the Particle",
                     font=DISPLAY, color=INK, font_size=34, line_spacing=1.3).move_to([0, 0.5, 0])
        sub = Text("the Kennard inequality",
                   font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([0, -0.8, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_TwoHistograms(Scene):
    """Two histograms: position (TEAL) and momentum (CRIMSON)."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: position histogram (TEAL)
        left_title = SerifLabel("position measurements", accent=TEAL, size=18).move_to([-3.5, 3.2, 0])
        x_axis_l = Arrow([-5.8, -2.5, 0], [-0.2, -2.5, 0], color=INK, stroke_width=1.5, buff=0)
        x_lbl_l = SerifLabel("x", accent=INK, size=18).move_to([-0.0, -3.0, 0])
        sigma_x = 0.6
        bar_xs = np.linspace(-3.5, -0.5, 8)
        bars_l = VGroup(*[
            Rectangle(width=0.32, height=2.8 * np.exp(-(bx + 2.0)**2 / (2 * sigma_x**2)),
                      fill_color=TEAL, fill_opacity=0.6, stroke_color=TEAL, stroke_width=1.0
                      ).move_to([bx, -2.5 + 1.4 * np.exp(-(bx + 2.0)**2 / (2 * sigma_x**2)), 0])
            for bx in bar_xs
        ])
        sx_lbl = SerifLabel("sigma_x", accent=TEAL, size=18).move_to([-2.0, -1.5, 0])

        # Right: momentum histogram (CRIMSON) — wider
        right_title = SerifLabel("momentum measurements", accent=CRIMSON, size=18).move_to([3.5, 3.2, 0])
        x_axis_r = Arrow([0.2, -2.5, 0], [5.8, -2.5, 0], color=INK, stroke_width=1.5, buff=0)
        p_lbl_r = SerifLabel("p", accent=INK, size=18).move_to([6.0, -3.0, 0])
        sigma_p = 1.5
        bar_ps = np.linspace(0.5, 5.5, 8)
        bars_r = VGroup(*[
            Rectangle(width=0.32, height=1.0 * np.exp(-(bp - 3.0)**2 / (2 * sigma_p**2)),
                      fill_color=CRIMSON, fill_opacity=0.6, stroke_color=CRIMSON, stroke_width=1.0
                      ).move_to([bp, -2.5 + 0.5 * np.exp(-(bp - 3.0)**2 / (2 * sigma_p**2)), 0])
            for bp in bar_ps
        ])
        sp_lbl = SerifLabel("sigma_p", accent=CRIMSON, size=18).move_to([3.0, -1.5, 0])

        prod_lbl = SerifLabel("sigma_x * sigma_p >= hbar/2", accent=INK, size=20).move_to([0, -3.5, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowArrow(x_axis_l), run_time=0.3)
        self.play(Create(bars_l), FadeIn(sx_lbl), run_time=0.5)
        self.play(FadeIn(right_title), GrowArrow(x_axis_r), run_time=0.3)
        self.play(Create(bars_r), FadeIn(sp_lbl), run_time=0.5)
        self.play(FadeIn(prod_lbl, shift=UP * 0.2), run_time=0.4)
        self.wait(dur - 2.4)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("No particle is measured twice. No bump happens.\nYet sigma_x times sigma_p >= hbar/2 always.\nWhere does the limit come from?",
                     font=DISPLAY, color=INK, font_size=16, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_CommutatorCard(Scene):
    """[x̂, p̂] = iℏ — the canonical commutation relation."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        formula = Text("[x, p] = i*hbar",
                       font=MONO, color=TEAL, font_size=36).move_to([0, 1.5, 0])
        box = SurroundingRectangle(formula, color=TEAL, buff=0.25, stroke_width=2.0)

        lbl1 = SerifLabel("xp means: first multiply by x, then differentiate", accent=INK, size=18).move_to([0, 0.0, 0])
        lbl2 = SerifLabel("px means: first differentiate, then multiply by x", accent=INK, size=18).move_to([0, -0.6, 0])
        lbl3 = SerifLabel("the product rule creates the extra i*hbar", accent=TEAL, size=18).move_to([0, -1.4, 0])
        lbl4 = SerifLabel("this non-commutativity is the root cause", accent=TEAL, size=20).move_to([0, -2.3, 0])

        # Order-of-operations diagram: two arrows showing xp vs px
        xp_arrow = Arrow(start=[-3.5, 2.8, 0], end=[-0.5, 2.8, 0],
                         color=TEAL, stroke_width=2.0, buff=0.05)
        px_arrow = Arrow(start=[0.5, 2.8, 0], end=[3.5, 2.8, 0],
                         color=CRIMSON, stroke_width=2.0, buff=0.05)
        xp_lbl = SerifLabel("x then p", accent=TEAL, size=16).move_to([-2.0, 3.2, 0])
        px_lbl = SerifLabel("p then x", accent=CRIMSON, size=16).move_to([2.0, 3.2, 0])

        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.4)
        self.play(Create(box), run_time=0.3)
        self.play(GrowArrow(xp_arrow), FadeIn(xp_lbl), run_time=0.3)
        self.play(GrowArrow(px_arrow), FadeIn(px_lbl), run_time=0.3)
        self.play(FadeIn(lbl1), run_time=0.3)
        self.play(FadeIn(lbl2), run_time=0.3)
        self.play(FadeIn(lbl3), run_time=0.3)
        self.play(FadeIn(lbl4), run_time=0.3)
        self.wait(dur - 2.7)


class B05_SpikeVsWave(Scene):
    """Definite position = spike; Fourier transform = flat plane wave."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: delta spike in x
        left_title = SerifLabel("definite position", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        x_base_l = Arrow([-5.8, -2.0, 0], [-0.2, -2.0, 0], color=INK, stroke_width=1.5, buff=0)
        spike = Line([-3.0, -2.0, 0], [-3.0, 2.5, 0], color=TEAL, stroke_width=3.5)
        x_lbl_l = SerifLabel("x", accent=INK, size=18).move_to([-0.2, -2.6, 0])
        delta_lbl = SerifLabel("sigma_x -> 0", accent=TEAL, size=18).move_to([-3.0, -2.8, 0])

        # Fourier arrow
        f_arrow = Arrow(start=[-0.2, 0, 0], end=[0.2, 0, 0], color=INK, stroke_width=2, buff=0)
        f_lbl = SerifLabel("Fourier", accent=INK, size=14).move_to([0, 0.4, 0])

        # Right: flat plane wave in p
        right_title = SerifLabel("momentum: completely unknown", accent=CRIMSON, size=18).move_to([3.5, 3.2, 0])
        x_base_r = Arrow([0.2, -2.0, 0], [5.8, -2.0, 0], color=INK, stroke_width=1.5, buff=0)
        flat_line = Line([0.4, 0.0, 0], [5.6, 0.0, 0], color=CRIMSON, stroke_width=3.0)
        p_lbl_r = SerifLabel("p", accent=INK, size=18).move_to([5.8, -2.6, 0])
        flat_lbl = SerifLabel("sigma_p -> inf", accent=CRIMSON, size=18).move_to([3.0, -2.8, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowArrow(x_base_l), run_time=0.3)
        self.play(Create(spike), FadeIn(delta_lbl), FadeIn(x_lbl_l), run_time=0.4)
        self.play(GrowArrow(f_arrow), FadeIn(f_lbl), run_time=0.3)
        self.play(FadeIn(right_title), GrowArrow(x_base_r), run_time=0.3)
        self.play(Create(flat_line), FadeIn(flat_lbl), FadeIn(p_lbl_r), run_time=0.4)
        self.wait(dur - 2.2)


class B06_GaussianMinimum(Scene):
    """Gaussian in x and p; Robertson hyperbola with dot at the Gaussian."""
    def construct(self):
        dur = DUR.get("B06", 10.0)
        # Two Gaussian curves side by side
        x_vals = np.linspace(-2.5, 2.5, 200)

        left_curve_pts = [np.array([x - 3.5, 2.5 * np.exp(-x**2 / 0.5), 0]) for x in x_vals]
        left_curve = VMobject(color=TEAL, stroke_width=3.0)
        left_curve.set_points_smoothly(left_curve_pts)
        left_base = Line([-6.0, -0.5, 0], [-1.0, -0.5, 0], color=INK, stroke_width=1.5)
        left_lbl = SerifLabel("psi(x): Gaussian", accent=TEAL, size=18).move_to([-3.5, -1.2, 0])

        right_curve_pts = [np.array([x + 3.5, 2.5 * np.exp(-x**2 / 0.5), 0]) for x in x_vals]
        right_curve = VMobject(color=TEAL, stroke_width=3.0)
        right_curve.set_points_smoothly(right_curve_pts)
        right_base = Line([1.0, -0.5, 0], [6.0, -0.5, 0], color=INK, stroke_width=1.5)
        right_lbl = SerifLabel("phi(p): also Gaussian", accent=TEAL, size=18).move_to([3.5, -1.2, 0])

        formula = Text("sigma_x * sigma_p = hbar/2  (minimum)",
                       font=MONO, color=TEAL, font_size=22).move_to([0, -2.5, 0])
        min_chip = LabelChip("tightest possible compromise", accent=TEAL, size=18).move_to([0, -3.5, 0])

        divider = Line([0, -1.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        self.play(Create(divider), run_time=0.2)
        self.play(Create(left_base), run_time=0.2)
        self.play(Create(left_curve), run_time=0.4)
        self.play(FadeIn(left_lbl), run_time=0.2)
        self.play(Create(right_base), run_time=0.2)
        self.play(Create(right_curve), run_time=0.4)
        self.play(FadeIn(right_lbl), run_time=0.2)
        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.4)
        self.play(GrowFromCenter(min_chip), run_time=0.4)
        self.wait(dur - 2.8)


class B07_RobertsonFormula(Scene):
    """Robertson inequality formula."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        formula = Text("sigma_A * sigma_B >= (1/2) * |<[A,B]>|",
                       font=MONO, color=TEAL, font_size=24).move_to([0, 2.0, 0])
        box = SurroundingRectangle(formula, color=TEAL, buff=0.25, stroke_width=2.0)

        lbl1 = SerifLabel("A, B = any two observables", accent=INK, size=20).move_to([0, 0.6, 0])
        lbl2 = SerifLabel("[A, B] = AB - BA (commutator)", accent=INK, size=20).move_to([0, -0.1, 0])
        lbl3 = SerifLabel("proof: Cauchy-Schwarz, no measurement", accent=TEAL, size=20).move_to([0, -1.0, 0])
        lbl4 = SerifLabel("for x and p: gives sigma_x*sigma_p >= hbar/2", accent=TEAL, size=20).move_to([0, -1.8, 0])

        # CS bound visualized as a right-angle at the origin
        ax_a = Arrow(start=[-5.5, -3.0, 0], end=[5.5, -3.0, 0], color=INK, stroke_width=1.5, buff=0)
        ax_b = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 3.0, 0], color=INK, stroke_width=1.5, buff=0)
        sigma_a_lbl = SerifLabel("sigma_A", accent=INK, size=16).move_to([5.5, -3.4, 0])
        sigma_b_lbl = SerifLabel("sigma_B", accent=INK, size=16).move_to([-5.0, 3.2, 0])
        hyperbola_pts = [np.array([-4.5 + i * 0.18, -3.0 + 1.5 / (-4.5 + i * 0.18 + 4.8), 0])
                         for i in range(50) if abs(-4.5 + i * 0.18 + 4.8) > 0.15]
        # Simple hyperbola-like curve: sigma_A * sigma_B = const
        k_vals = np.linspace(0.3, 4.5, 100)
        hyp_pts = [np.array([-5.0 + k * 2.3, -3.0 + 1.2 / k, 0])
                   for k in k_vals if -3.0 + 1.2 / k < 3.0]
        hyp_curve = VMobject(color=TEAL, stroke_width=2.5)
        hyp_curve.set_points_smoothly(hyp_pts)
        hyp_lbl = SerifLabel("sigma_A*sigma_B = bound", accent=TEAL, size=16).move_to([3.5, -1.5, 0])

        self.play(GrowArrow(ax_a), GrowArrow(ax_b), run_time=0.3)
        self.play(FadeIn(sigma_a_lbl), FadeIn(sigma_b_lbl), run_time=0.2)
        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.4)
        self.play(Create(box), run_time=0.3)
        self.play(FadeIn(lbl1), run_time=0.3)
        self.play(FadeIn(lbl2), run_time=0.3)
        self.play(Create(hyp_curve), FadeIn(hyp_lbl), run_time=0.4)
        self.play(FadeIn(lbl3), run_time=0.3)
        self.play(FadeIn(lbl4), run_time=0.3)
        self.wait(dur - 2.8)


class B08_CommutingPair(Scene):
    """Commuting operators share eigenbasis — can both be definite."""
    def construct(self):
        dur = DUR.get("B08", 11.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: non-commuting (x and p)
        left_title = SerifLabel("x and p: do NOT commute", accent=CRIMSON, size=18).move_to([-3.5, 3.2, 0])
        comm1 = Text("[x, p] = i*hbar  ≠ 0",
                     font=MONO, color=CRIMSON, font_size=20).move_to([-3.5, 1.5, 0])
        result1 = SerifLabel("no shared eigenbasis", accent=CRIMSON, size=18).move_to([-3.5, 0.5, 0])
        result2 = SerifLabel("cannot both be sharp", accent=CRIMSON, size=18).move_to([-3.5, -0.2, 0])

        # Right: commuting (E and p for free particle)
        right_title = SerifLabel("E and p: DO commute", accent=TEAL, size=18).move_to([3.5, 3.2, 0])
        comm2 = Text("[E, p] = 0",
                     font=MONO, color=TEAL, font_size=20).move_to([3.5, 1.5, 0])
        result3 = SerifLabel("shared eigenbasis exists", accent=TEAL, size=18).move_to([3.5, 0.5, 0])
        result4 = SerifLabel("both can be sharp at once", accent=TEAL, size=18).move_to([3.5, -0.2, 0])

        key = SerifLabel("uncertainty is about commutators, not clumsy tools", accent=INK, size=18).move_to([0, -2.5, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), run_time=0.3)
        self.play(FadeIn(comm1), run_time=0.3)
        self.play(FadeIn(result1), FadeIn(result2), run_time=0.3)
        self.play(FadeIn(right_title), run_time=0.3)
        self.play(FadeIn(comm2), run_time=0.3)
        self.play(FadeIn(result3), FadeIn(result4), run_time=0.3)
        self.play(FadeIn(key), run_time=0.4)
        self.wait(dur - 2.7)


class B09_AtomConfinement(Scene):
    """Atom in a box: confinement implies minimum kinetic energy."""
    def construct(self):
        dur = DUR.get("B09", 10.0)
        # Box (atom)
        box = Rectangle(width=2.5, height=2.5, color=INK, stroke_width=2.5).move_to([0, 0.5, 0])
        atom = Circle(radius=0.3, color=TEAL, fill_color=TEAL, fill_opacity=0.5,
                      stroke_width=2.0).move_to([0, 0.5, 0])
        delta_lbl = SerifLabel("Delta_x ~ 1 Angstrom", accent=INK, size=18).move_to([0, -0.7, 0])
        brace = DoubleArrow(start=[-1.25, -1.3, 0], end=[1.25, -1.3, 0],
                            color=INK, stroke_width=1.8, buff=0)

        sigma_p = SerifLabel("=> sigma_p >= hbar / (2 * Delta_x)", accent=TEAL, size=18).move_to([0, -1.8, 0])
        ke_lbl = SerifLabel("=> minimum kinetic energy = zero-point energy", accent=TEAL, size=18).move_to([0, -2.5, 0])
        conclusion = SerifLabel("confinement = energy floor", accent=TEAL, size=20).move_to([0, -3.3, 0])

        self.play(Create(box), run_time=0.4)
        self.play(FadeIn(atom), run_time=0.3)
        self.play(GrowFromCenter(brace), FadeIn(delta_lbl), run_time=0.4)
        self.play(FadeIn(sigma_p), run_time=0.3)
        self.play(FadeIn(ke_lbl), run_time=0.3)
        self.play(FadeIn(conclusion), run_time=0.3)
        self.wait(dur - 2.2)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Uncertainty is not clumsiness.\nThe limit lives in the state.\nNon-commuting: no shared eigenbasis.\nGaussian: tightest compromise.",
                      font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
