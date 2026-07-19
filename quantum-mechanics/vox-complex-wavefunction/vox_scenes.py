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
        title = Text("Why the Wave Function\nHas to Be Complex",
                     font=DISPLAY, color=INK, font_size=36, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])
        sub = Text("the hidden direction", font=SERIF, color=INK, font_size=22, slant=ITALIC).move_to([0, -0.8, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_TwoHumps(Scene):
    """Two identical Gaussian humps — right-mover and left-mover."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        x_vals = np.linspace(-3.0, 3.0, 200)
        sigma = 0.7

        # Left hump: right-mover
        pts_l = [np.array([x - 3.5, 3.0 * np.exp(-x**2 / (2 * sigma**2)), 0]) for x in x_vals]
        curve_l = VMobject(color=CRIMSON, stroke_width=3)
        curve_l.set_points_smoothly(pts_l)

        lbl_l = SerifLabel("right-mover", accent=CRIMSON, size=22).move_to([-3.5, -1.5, 0])
        arrow_l = Arrow(start=[-3.5, -0.8, 0], end=[-2.0, -0.8, 0], color=CRIMSON, stroke_width=2.5, buff=0.1)

        # Right hump: left-mover (identical shape)
        pts_r = [np.array([x + 3.5, 3.0 * np.exp(-x**2 / (2 * sigma**2)), 0]) for x in x_vals]
        curve_r = VMobject(color=CRIMSON, stroke_width=3)
        curve_r.set_points_smoothly(pts_r)

        lbl_r = SerifLabel("left-mover", accent=CRIMSON, size=22).move_to([3.5, -1.5, 0])
        arrow_r = Arrow(start=[3.5, -0.8, 0], end=[2.0, -0.8, 0], color=CRIMSON, stroke_width=2.5, buff=0.1)

        equal_lbl = LabelChip("|psi|^2: identical", accent=CRIMSON, size=20).move_to([0, -2.8, 0])

        self.play(Create(curve_l), Create(curve_r), run_time=0.7)
        self.play(FadeIn(lbl_l), GrowArrow(arrow_l), run_time=0.4)
        self.play(FadeIn(lbl_r), GrowArrow(arrow_r), run_time=0.4)
        self.play(GrowFromCenter(equal_lbl), run_time=0.4)
        self.wait(dur - 2.1)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Two identical probability humps.\nOne moves right, one moves left.\nHow does the wave function know which is which?",
                     font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_TwoHelices(Scene):
    """Two wave packets: +k winds one way, -k the other, shown as Re/Im sine pairs."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        x_vals = np.linspace(-5.0, 5.0, 300)
        k0 = 3.0
        sigma = 1.5
        envelope = np.exp(-x_vals**2 / (2 * sigma**2))

        # Upper half: +k right-mover
        re_pts_p = [np.array([x, 1.5 + 1.2 * envelope[i] * np.cos(k0 * x), 0])
                    for i, x in enumerate(x_vals)]
        im_pts_p = [np.array([x, 1.5 + 1.2 * envelope[i] * np.sin(k0 * x), 0])
                    for i, x in enumerate(x_vals)]

        re_p = VMobject(color=TEAL, stroke_width=2.5)
        re_p.set_points_smoothly(re_pts_p)
        im_p = VMobject(color=TEAL, stroke_width=1.5, stroke_opacity=0.5)
        im_p.set_points_smoothly(im_pts_p)

        lbl_re_p = SerifLabel("Re (right-mover)", accent=TEAL, size=18).move_to([-4.5, 3.2, 0])
        lbl_p_dir = LabelChip("moving right", accent=TEAL, size=18).move_to([4.5, 3.2, 0])

        # Lower half: -k left-mover
        re_pts_m = [np.array([x, -1.5 + 1.2 * envelope[i] * np.cos(-k0 * x), 0])
                    for i, x in enumerate(x_vals)]
        im_pts_m = [np.array([x, -1.5 + 1.2 * envelope[i] * np.sin(-k0 * x), 0])
                    for i, x in enumerate(x_vals)]

        re_m = VMobject(color=CRIMSON, stroke_width=2.5)
        re_m.set_points_smoothly(re_pts_m)
        im_m = VMobject(color=CRIMSON, stroke_width=1.5, stroke_opacity=0.5)
        im_m.set_points_smoothly(im_pts_m)

        lbl_re_m = SerifLabel("Re (left-mover)", accent=CRIMSON, size=18).move_to([-4.5, -0.3, 0])
        lbl_m_dir = LabelChip("moving left", accent=CRIMSON, size=18).move_to([4.5, -0.3, 0])

        divider = DashedLine([-6.5, 0, 0], [6.5, 0, 0], color=INK, stroke_width=1.0, dash_length=0.2)

        self.play(Create(divider), run_time=0.2)
        self.play(Create(re_p), Create(im_p), FadeIn(lbl_re_p), run_time=0.6)
        self.play(GrowFromCenter(lbl_p_dir), run_time=0.3)
        self.play(Create(re_m), Create(im_m), FadeIn(lbl_re_m), run_time=0.6)
        self.play(GrowFromCenter(lbl_m_dir), run_time=0.3)
        self.wait(dur - 2.2)


class B05_LengthOnly(Scene):
    """Probability density |psi|^2: identical for both directions."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        x_vals = np.linspace(-5.0, 5.0, 200)
        sigma = 1.5
        envelope_sq = np.exp(-x_vals**2 / sigma**2)

        # Left: |psi|^2 of right-mover
        pts_l = [np.array([x - 3.0, 2.5 * envelope_sq[i] - 1.5, 0])
                 for i, x in enumerate(x_vals)]
        curve_l = VMobject(color=CRIMSON, stroke_width=3)
        curve_l.set_points_smoothly(pts_l)

        # Right: |psi|^2 of left-mover — identical
        pts_r = [np.array([x + 3.0, 2.5 * envelope_sq[i] - 1.5, 0])
                 for i, x in enumerate(x_vals)]
        curve_r = VMobject(color=CRIMSON, stroke_width=3)
        curve_r.set_points_smoothly(pts_r)

        lbl_l = SerifLabel("|psi|^2 right-mover", accent=CRIMSON, size=20).move_to([-3.0, 2.0, 0])
        lbl_r = SerifLabel("|psi|^2 left-mover", accent=CRIMSON, size=20).move_to([3.0, 2.0, 0])
        equal_lbl = LabelChip("no difference in |psi|^2", accent=CRIMSON, size=22).move_to([0, -3.0, 0])

        cross_note = SerifLabel("direction hidden by squaring", accent=TEAL, size=20).move_to([0, 3.2, 0])

        self.play(Create(curve_l), Create(curve_r), run_time=0.7)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.4)
        self.play(GrowFromCenter(equal_lbl), run_time=0.4)
        self.play(FadeIn(cross_note), run_time=0.4)
        self.wait(dur - 2.1)


class B06_RealPacketSymmetry(Scene):
    """A real packet is the sum of +k and -k in equal measure."""
    def construct(self):
        dur = DUR.get("B06", 11.0)
        x_vals = np.linspace(-5.0, 5.0, 300)
        k0 = 3.0
        sigma = 1.5
        envelope = np.exp(-x_vals**2 / (2 * sigma**2))

        # Real cosine packet
        cos_pts = [np.array([x, 1.5 * envelope[i] * np.cos(k0 * x) + 1.5, 0])
                   for i, x in enumerate(x_vals)]
        cos_wave = VMobject(color=INK, stroke_width=2.5)
        cos_wave.set_points_smoothly(cos_pts)
        cos_lbl = SerifLabel("real packet (cosine only)", accent=INK, size=20).move_to([-3.0, 3.3, 0])

        # k-space bars: +k and -k equally
        bar_pos = Rectangle(width=0.5, height=1.8, fill_color=TEAL, fill_opacity=0.8,
                             stroke_width=0).move_to([1.5, -1.9, 0])
        bar_neg = Rectangle(width=0.5, height=1.8, fill_color=CRIMSON, fill_opacity=0.8,
                             stroke_width=0).move_to([-1.5, -1.9, 0])
        ax_k = Line([-4.0, -2.8, 0], [4.0, -2.8, 0], color=INK, stroke_width=1.5)
        k_lbl = SerifLabel("k-space", accent=INK, size=18).move_to([4.5, -2.8, 0])
        lbl_pk = SerifLabel("+k", accent=TEAL, size=18).move_to([1.5, -3.2, 0])
        lbl_nk = SerifLabel("-k", accent=CRIMSON, size=18).move_to([-1.5, -3.2, 0])
        sym_lbl = LabelChip("symmetric: both directions equally", accent=INK, size=18).move_to([0, -3.8, 0])

        self.play(Create(cos_wave), FadeIn(cos_lbl), run_time=0.6)
        self.play(Create(ax_k), FadeIn(k_lbl), run_time=0.3)
        self.play(FadeIn(bar_pos), FadeIn(bar_neg), FadeIn(lbl_pk), FadeIn(lbl_nk), run_time=0.5)
        self.play(GrowFromCenter(sym_lbl), run_time=0.4)
        self.wait(dur - 2.0)


class B07_PhaseIsDirection(Scene):
    """Phase gradient along x encodes momentum direction."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        x_vals = np.linspace(-5.5, 5.5, 300)
        k0 = 3.0
        sigma = 1.8
        envelope = np.exp(-x_vals**2 / (2 * sigma**2))

        # Complex wave Re part
        re_pts = [np.array([x, 2.0 * envelope[i] * np.cos(k0 * x) + 0.5, 0])
                  for i, x in enumerate(x_vals)]
        re_wave = VMobject(color=TEAL, stroke_width=3)
        re_wave.set_points_smoothly(re_pts)

        # Phase gradient arrows along base
        phase_arrows = VGroup()
        for xi in np.linspace(-4.0, 4.0, 9):
            a = Arrow(start=[xi - 0.4, -1.5, 0], end=[xi + 0.4, -1.5, 0],
                      color=TEAL, stroke_width=2, buff=0)
            phase_arrows.add(a)

        phase_lbl = SerifLabel("phase advances rightward", accent=TEAL, size=20).move_to([0, -2.4, 0])
        k_lbl = LabelChip("winding rate = k = p / hbar", accent=TEAL, size=20).move_to([0, -3.2, 0])

        self.play(Create(re_wave), run_time=0.7)
        self.play(Create(phase_arrows), run_time=0.6)
        self.play(FadeIn(phase_lbl), run_time=0.3)
        self.play(GrowFromCenter(k_lbl), run_time=0.4)
        self.wait(dur - 2.2)


class B08_WithAndWithoutI(Scene):
    """With i: directional arrow. Without i: symmetric smear."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.5)

        # Left panel: with i
        left_title = SerifLabel("Schrodinger with i", accent=TEAL, size=20).move_to([-3.5, 3.0, 0])
        arrow_dir = Arrow(start=[-5.0, 0.5, 0], end=[-0.5, 0.5, 0],
                          color=TEAL, stroke_width=4, buff=0.1)
        dir_lbl = LabelChip("one direction", accent=TEAL, size=20).move_to([-3.0, -0.5, 0])

        # Right panel: without i (would spread both ways)
        right_title = SerifLabel("without i", accent=CRIMSON, size=20).move_to([3.5, 3.0, 0])
        arrow_both_r = Arrow(start=[0.5, 0.5, 0], end=[5.5, 0.5, 0],
                             color=CRIMSON, stroke_width=3, buff=0.1)
        arrow_both_l = Arrow(start=[5.5, -0.5, 0], end=[0.5, -0.5, 0],
                             color=CRIMSON, stroke_width=3, buff=0.1)
        sym_lbl = LabelChip("both directions", accent=CRIMSON, size=20).move_to([3.5, -1.5, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowArrow(arrow_dir), run_time=0.6)
        self.play(GrowFromCenter(dir_lbl), run_time=0.3)
        self.play(FadeIn(right_title), GrowArrow(arrow_both_r), GrowArrow(arrow_both_l), run_time=0.6)
        self.play(GrowFromCenter(sym_lbl), run_time=0.3)
        self.wait(dur - 2.2)


class B09_Example(Scene):
    """Illustrative: k0=+5 vs k0=-5 nm^-1."""
    def construct(self):
        dur = DUR.get("B09", 11.0)
        ill_lbl = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-5.5, 3.3, 0])

        x_vals = np.linspace(-4.0, 4.0, 200)
        k_pos = 3.0
        sigma = 1.2
        env = np.exp(-x_vals**2 / (2 * sigma**2))

        # Upper: k0=+5 (right-mover) — re part
        pts_p = [np.array([x, 1.5 * env[i] * np.cos(k_pos * x) + 1.8, 0])
                 for i, x in enumerate(x_vals)]
        wave_p = VMobject(color=TEAL, stroke_width=2.5)
        wave_p.set_points_smoothly(pts_p)
        lbl_p = SerifLabel("k0 = +5 nm^-1", accent=TEAL, size=20).move_to([-4.0, 3.0, 0])

        # Lower: k0=-5 (left-mover) — re part
        pts_m = [np.array([x, 1.5 * env[i] * np.cos(-k_pos * x) - 0.2, 0])
                 for i, x in enumerate(x_vals)]
        wave_m = VMobject(color=CRIMSON, stroke_width=2.5)
        wave_m.set_points_smoothly(pts_m)
        lbl_m = SerifLabel("k0 = -5 nm^-1", accent=CRIMSON, size=20).move_to([-4.0, -0.0, 0])

        # |psi|^2 identical — show as same envelope
        pts_env = [np.array([x, 1.5 * env[i] - 2.5, 0]) for i, x in enumerate(x_vals)]
        env_curve = VMobject(color=INK, stroke_width=2, stroke_opacity=0.6)
        env_curve.set_points_smoothly(pts_env)
        env_lbl = SerifLabel("|psi|^2: same for both", accent=INK, size=20).move_to([3.0, -2.0, 0])

        self.play(FadeIn(ill_lbl), run_time=0.3)
        self.play(Create(wave_p), FadeIn(lbl_p), run_time=0.5)
        self.play(Create(wave_m), FadeIn(lbl_m), run_time=0.5)
        self.play(Create(env_curve), FadeIn(env_lbl), run_time=0.5)
        self.wait(dur - 1.9)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Real part: where it is.\nImaginary part: where it is going.\nStrip it out — lose the direction.",
                      font=DISPLAY, color=INK, font_size=24, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
