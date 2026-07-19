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
        title = Text("Why a Quantum Particle\nSpreads Out on Its Own",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        sub = Text("dispersion and the spreading packet", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_MomentaBundle(Scene):
    """Narrow packet in x + wide spread in k-space."""
    def construct(self):
        dur = DUR.get("B02", 9.0)
        x_vals = np.linspace(-5.5, 5.5, 200)
        sigma = 0.6

        # Spatial packet (left)
        pts_x = [np.array([x - 2.5, 2.5 * np.exp(-x**2 / (2 * sigma**2)), 0]) for x in np.linspace(-3, 3, 200)]
        packet = VMobject(color=TEAL, stroke_width=3)
        packet.set_points_smoothly(pts_x)
        x_base = Line([-5.5, 0, 0], [0, 0, 0], color=INK, stroke_width=1.5)
        x_lbl = SerifLabel("narrow in x", accent=TEAL, size=20).move_to([-2.5, -1.2, 0])

        # k-space spread (right)
        k_vals = np.linspace(-2.5, 2.5, 200)
        sigma_k = 1.5  # wide because sigma_x is narrow
        pts_k = [np.array([k + 3.5, 2.0 * np.exp(-k**2 / (2 * sigma_k**2)), 0]) for k in k_vals]
        k_curve = VMobject(color=CRIMSON, stroke_width=3)
        k_curve.set_points_smoothly(pts_k)
        k_base = Line([0.5, 0, 0], [6.5, 0, 0], color=INK, stroke_width=1.5)
        k_lbl = SerifLabel("wide in k (momenta)", accent=CRIMSON, size=20).move_to([3.5, -1.2, 0])

        divider = Line([0, -2.0, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        self.play(Create(x_base), Create(k_base), Create(divider), run_time=0.3)
        self.play(Create(packet), FadeIn(x_lbl), run_time=0.5)
        self.play(Create(k_curve), FadeIn(k_lbl), run_time=0.5)
        self.wait(dur - 1.5)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("A tidy quantum packet. No forces.\nNo collisions. Spreads wider with time.\nHow does a particle blur on its own?",
                     font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_FastSlow(Scene):
    """Fast components outrun slow: the packet fans out."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Three arrows diverging
        origin = [-5.0, 0, 0]
        slow_end = [1.0, -1.5, 0]
        med_end = [3.0, 0, 0]
        fast_end = [5.5, 1.5, 0]

        slow = Arrow(start=origin, end=slow_end, color=CRIMSON, stroke_width=2.5, buff=0)
        med = Arrow(start=origin, end=med_end, color=INK, stroke_width=2.5, buff=0)
        fast = Arrow(start=origin, end=fast_end, color=TEAL, stroke_width=2.5, buff=0)

        slow_lbl = SerifLabel("slow (low k)", accent=CRIMSON, size=20).move_to([1.5, -2.5, 0])
        med_lbl = SerifLabel("medium k", accent=INK, size=20).move_to([3.0, -0.7, 0])
        fast_lbl = SerifLabel("fast (high k)", accent=TEAL, size=20).move_to([5.0, 2.5, 0])

        start_lbl = LabelChip("all start here", accent=INK, size=18).move_to([-5.0, 1.0, 0])

        self.play(GrowFromCenter(start_lbl), run_time=0.3)
        self.play(GrowArrow(slow), GrowArrow(med), GrowArrow(fast), run_time=0.6)
        self.play(FadeIn(slow_lbl), FadeIn(med_lbl), FadeIn(fast_lbl), run_time=0.5)
        self.wait(dur - 1.6)


class B05_PacketStretches(Scene):
    """Side-by-side: tight packet at t=0, wide packet at t=later."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: t=0, tight
        left_title = SerifLabel("t = 0", accent=TEAL, size=22).move_to([-3.5, 3.2, 0])
        sigma0 = 0.5
        pts_l = [np.array([x - 3.0, 2.5 * np.exp(-x**2 / (2 * sigma0**2)), 0]) for x in np.linspace(-3, 3, 200)]
        curve_l = VMobject(color=TEAL, stroke_width=3)
        curve_l.set_points_smoothly(pts_l)
        base_l = Line([-6.0, 0, 0], [-0.2, 0, 0], color=INK, stroke_width=1.5)

        # Right: t=later, wide
        right_title = SerifLabel("t = later", accent=CRIMSON, size=22).move_to([3.5, 3.2, 0])
        sigma1 = 1.8
        pts_r = [np.array([x + 3.0, 0.7 * np.exp(-x**2 / (2 * sigma1**2)), 0]) for x in np.linspace(-4, 4, 200)]
        curve_r = VMobject(color=CRIMSON, stroke_width=3)
        curve_r.set_points_smoothly(pts_r)
        base_r = Line([0.2, 0, 0], [6.0, 0, 0], color=INK, stroke_width=1.5)

        self.play(Create(divider), run_time=0.2)
        self.play(Create(base_l), Create(curve_l), FadeIn(left_title), run_time=0.5)
        self.play(Create(base_r), Create(curve_r), FadeIn(right_title), run_time=0.5)
        self.wait(dur - 1.4)


class B06_TightFastSpread(Scene):
    """Tight vs wide initial packet: narrower spreads faster."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        # Two packetss at t=0
        narrow_lbl = LabelChip("narrow start", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        narrow_pts = [np.array([x - 3.5, 2.0 * np.exp(-x**2 / 0.2), 0]) for x in np.linspace(-2, 2, 200)]
        narrow = VMobject(color=TEAL, stroke_width=3)
        narrow.set_points_smoothly(narrow_pts)

        wide_lbl = LabelChip("wide start", accent=CRIMSON, size=20).move_to([3.5, 3.2, 0])
        wide_pts = [np.array([x + 3.5, 2.0 * np.exp(-x**2 / 2.0), 0]) for x in np.linspace(-4, 4, 200)]
        wide_start = VMobject(color=CRIMSON, stroke_width=3)
        wide_start.set_points_smoothly(wide_pts)

        base_l = Line([-6.0, 0, 0], [-0.2, 0, 0], color=INK, stroke_width=1.5)
        base_r = Line([0.2, 0, 0], [6.0, 0, 0], color=INK, stroke_width=1.5)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # After-spreading labels
        fast_rate = LabelChip("spreads fast", accent=TEAL, size=18).move_to([-3.5, -2.5, 0])
        slow_rate = LabelChip("spreads slowly", accent=CRIMSON, size=18).move_to([3.5, -2.5, 0])

        self.play(Create(divider), Create(base_l), Create(base_r), run_time=0.3)
        self.play(Create(narrow), FadeIn(narrow_lbl), run_time=0.5)
        self.play(Create(wide_start), FadeIn(wide_lbl), run_time=0.5)
        self.play(
            narrow.animate.stretch_to_fit_width(4.5),
            run_time=dur * 0.35
        )
        self.play(GrowFromCenter(fast_rate), GrowFromCenter(slow_rate), run_time=0.4)
        self.wait(dur * 0.1)


class B07_DoublingTime(Scene):
    """Doubling time formula."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        formula = Text("t_double ~ m * sigma_0^2 / hbar",
                       font=MONO, color=TEAL, font_size=30).move_to([0, 2.0, 0])
        m_lbl = SerifLabel("m = mass", accent=INK, size=20).move_to([-3.0, 0.5, 0])
        s_lbl = SerifLabel("sigma_0 = initial width", accent=TEAL, size=20).move_to([3.0, 0.5, 0])

        key1 = SerifLabel("tighter sigma_0 → shorter doubling time", accent=TEAL, size=20).move_to([0, -0.8, 0])
        key2 = SerifLabel("heavier particle → spreads more slowly", accent=INK, size=20).move_to([0, -1.6, 0])

        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(m_lbl), FadeIn(s_lbl), run_time=0.5)
        self.play(FadeIn(key1), FadeIn(key2), run_time=0.5)
        self.wait(dur - 1.9)


class B08_DispersionComparison(Scene):
    """E vs k: linear (photon) vs quadratic (electron)."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        ax_x = Arrow(start=[-5.5, -3.0, 0], end=[5.5, -3.0, 0], color=INK, stroke_width=2, buff=0)
        ax_y = Arrow(start=[-5.5, -3.0, 0], end=[-5.5, 3.0, 0], color=INK, stroke_width=2, buff=0)
        k_lbl = SerifLabel("k", accent=INK, size=20).move_to([5.5, -3.4, 0])
        e_lbl = SerifLabel("E", accent=INK, size=20).move_to([-5.5, 3.4, 0])

        k_vals = np.linspace(0.1, 4.5, 100)

        # Photon: E = hbar*c*k (linear)
        lin_pts = [np.array([-5.0 + k * 2.3, -3.0 + k * 1.3, 0]) for k in k_vals]
        lin_curve = VMobject(color=TEAL, stroke_width=3)
        lin_curve.set_points_smoothly(lin_pts)
        lin_lbl = SerifLabel("photon: linear\nno spreading", accent=TEAL, size=18).move_to([3.0, 1.0, 0])

        # Electron: E = hbar^2*k^2/2m (quadratic)
        quad_pts = [np.array([-5.0 + k * 2.3, -3.0 + k**2 * 0.28, 0]) for k in k_vals if -3.0 + k**2 * 0.28 < 3.0]
        quad_curve = VMobject(color=CRIMSON, stroke_width=3)
        quad_curve.set_points_smoothly(quad_pts)
        quad_lbl = SerifLabel("electron: quadratic\nspreads", accent=CRIMSON, size=18).move_to([-0.5, 2.5, 0])

        self.play(GrowArrow(ax_x), GrowArrow(ax_y), FadeIn(k_lbl), FadeIn(e_lbl), run_time=0.4)
        self.play(Create(lin_curve), FadeIn(lin_lbl), run_time=0.5)
        self.play(Create(quad_curve), FadeIn(quad_lbl), run_time=0.5)
        self.wait(dur - 1.6)


class B09_Example(Scene):
    """Illustrative: 1 nm electron, doubling time calculation."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        params = Text("sigma_0 = 1 nm, electron",
                      font=MONO, color=TEAL, font_size=26).move_to([0, 2.5, 0])
        arrow = Arrow(start=[0, 2.0, 0], end=[0, 1.0, 0], color=INK, stroke_width=2.5, buff=0.1)
        result = Text("t_double ~ 8.7 fs", font=MONO, color=TEAL, font_size=30).move_to([0, 0.4, 0])
        tight = Text("sigma_0 = 0.1 nm:", font=MONO, color=CRIMSON, font_size=24).move_to([-1.0, -0.8, 0])
        tight_result = Text("t_double ~ 87 as", font=MONO, color=CRIMSON, font_size=24).move_to([2.5, -0.8, 0])
        note = SerifLabel("sigma_0 shrinks x10 → time shrinks x100", accent=INK, size=20).move_to([0, -2.0, 0])

        self.play(FadeIn(ill_lbl), FadeIn(params), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(FadeIn(result), run_time=0.4)
        self.play(FadeIn(tight), FadeIn(tight_result), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 2.2)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Localized = bundle of momenta.\nHigh momentum moves faster.\nThe bundle spreads.\nTighter start: faster spread.",
                      font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
