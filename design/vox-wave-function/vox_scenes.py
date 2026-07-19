"""vox_scenes.py — The Wave Function (film four, 16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Durations from beat_sheet.json (audio locked 2026-07-05):
B02 8.67 · B04 10.34 · T01 10.06 · T02 10.29 · T03 10.81 · B06 10.71 ·
B07 10.53 · B08 10.03 · B11 5.33.
Render:  bash scripts/vox_run.sh reels/vox-wave-function
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

GRAY_IM = "#8A8A8A"   # Im ψ — the ch-0 simulation's gray dashed

TANGENT = EquationTangent({
    "eyebrow": "Born's rule · equation · tangent",
    "equation": "P(a≤x≤b) = ∫ |ψ|² dx",
    "equation_tex": r"P(a \le x \le b) = \int_a^b |\psi(x,t)|^2\,dx",
    "lhs": "The odds of finding it between a and b.",
    "rhs": "Add up psi squared across that stretch.",
    "claim": "Psi never says where it IS — only the odds of where you'll FIND it.",
    "glossary": [
        {"sym": "ψ", "sym_tex": r"\psi", "role": "the object",
         "mean": "the wave function — what Schrödinger moves", "dom": "complex"},
        {"sym": "|ψ|²", "sym_tex": r"|\psi|^2", "role": "the density",
         "mean": "probability per nanometer — not a probability", "dom": "nm⁻¹"},
        {"sym": "∫ₐᵇ", "sym_tex": r"\int_a^b", "role": "the extraction",
         "mean": "sum the density over your region", "dom": "0–1"},
    ],
    "example": {
        "scenario": "ψ = e^(−|x|/a), normalized, a = 0.5 nm.",
        "lhs_val": "P(−a ≤ x ≤ a) ≈ 86.5%", "rhs_val": "peak: 2 nm⁻¹",
        "verdict": "a density may exceed 1 — a probability never does",
        "cost": "Read density as probability and you've made a units error.",
    },
    "values_claim": "(merged into the sentences claim — simple equation)",
})


# ---------- shared curve helpers (Gaussian packet, ch-0 palette) ----------

def _env(x, x0, a):
    return np.exp(-((x - x0) ** 2) / (2 * a * a))


def _density_poly(x0, a, height, y0, color=NAVY, x_lo=-6.2, x_hi=6.2):
    """Filled |ψ|² polygon seated on the baseline y0."""
    xs = np.linspace(x_lo, x_hi, 90)
    top = [np.array([x, y0 + height * _env(x, x0, a) ** 2, 0]) for x in xs]
    pts = top + [np.array([x_hi, y0, 0]), np.array([x_lo, y0, 0])]
    poly = Polygon(*pts)
    poly.set_fill(color, 0.35).set_stroke(color, 3)
    return poly


def _wave_curve(x0, a, k, amp, y0, color, phase=0.0, x_lo=-6.2, x_hi=6.2):
    """Re/Im ψ: envelope × cos(k(x−x0)+phase), centered on the baseline."""
    xs = np.linspace(x_lo, x_hi, 200)
    vm = VMobject(color=color, stroke_width=3.5)
    vm.set_points_smoothly(
        [np.array([x, y0 + amp * _env(x, x0, a) *
                   np.cos(k * (x - x0) + phase), 0]) for x in xs])
    return vm


# ------------------------------------------------------------- the beats

class B02_Title(Scene):            # 8.67s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE WAVE FUNCTION", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("what ψ actually means", font=SERIF, color=INK, font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(6.4)


class B04_TheCurves(Scene):        # 10.34s — the ch-0 simulation, restated
    def construct(self):
        y0 = -1.6
        base = Line([-6.2, y0, 0], [6.2, y0, 0], color=INK, stroke_width=2)
        legend = VGroup(
            LabelChip("|ψ|²", accent=NAVY, size=22),
            LabelChip("Re ψ", accent=TERRA, size=22),
            LabelChip("Im ψ", accent=SLATE, size=22),
        ).arrange(RIGHT, buff=0.4).to_edge(UP, buff=0.7).to_edge(LEFT, buff=0.9)

        def state(x0, a, amp):
            dens = _density_poly(x0, a, 2.3 * amp, y0)
            re = _wave_curve(x0, a, 4.2, 1.1 * amp, y0 + 1.0 * amp, TERRA)
            im = DashedVMobject(
                _wave_curve(x0, a, 4.2, 1.1 * amp, y0 + 1.0 * amp, GRAY_IM,
                            phase=PI / 2), num_dashes=48)
            return VGroup(dens, re, im)

        start = state(-2.8, 0.9, 1.0)
        end = state(2.4, 1.5, 0.62)          # drifts right, spreads, flattens
        self.play(Create(base), FadeIn(legend), run_time=0.8)
        self.play(FadeIn(start), run_time=1.4)
        self.play(Transform(start, end), run_time=5.2, rate_func=linear)
        q = Text("?", font=SERIF, color=CRIMSON, font_size=72, weight=BOLD)
        q.move_to([4.9, 1.9, 0])
        # word-keyed upgrade: lands on the spoken "mean" when the plane ships
        self.play(FadeIn(q, scale=1.4), run_time=0.7)
        self.wait(2.2)


class T01_EqSentences(Scene):      # 10.06s
    def construct(self):
        anchor = TANGENT.anchor(spotlight="P")
        eye = TANGENT.eyebrow()
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        z = TANGENT.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.2)
        self.wait(3.4)


class T02_EqGlossary(Scene):       # 10.29s
    def construct(self):
        anchor = TANGENT.anchor(spotlight=r"\psi")
        z = TANGENT.zone("glossary", spotlight="ψ")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(9.3)


class T03_EqExample(Scene):        # 10.81s
    def construct(self):
        anchor = TANGENT.anchor()
        z = TANGENT.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)
        self.wait(1.6)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)
        self.wait(1.8)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.wait(1.4)
        self.play(FadeIn(rows[3]), run_time=0.7)
        self.wait(2.9)


class B06_TwoPackets(Scene):       # 10.71s — identical humps, opposite motion
    def construct(self):
        y0 = -1.5
        title = SerifLabel("identical humps — opposite motion", NAVY, size=30)
        title.to_edge(UP, buff=0.75)

        def panel(cx, k_sign):
            dens = _density_poly(cx, 0.75, 2.0, y0, x_lo=cx - 2.6, x_hi=cx + 2.6)
            rip = _wave_curve(cx, 0.75, 5.0 * k_sign, 0.9, y0 + 0.85, TERRA,
                              x_lo=cx - 2.6, x_hi=cx + 2.6)
            return VGroup(dens, rip)

        left = panel(-3.4, -1.0)
        right = panel(3.4, 1.0)
        self.play(Write(title[0]), Create(title[1]), run_time=1.0)
        self.play(FadeIn(left[0]), FadeIn(right[0]), run_time=1.2)
        self.wait(0.8)
        self.play(Create(left[1]), Create(right[1]), run_time=1.4,
                  rate_func=linear)
        la = Arrow([-2.6, 1.3, 0], [-4.2, 1.3, 0], color=CRIMSON, buff=0,
                   stroke_width=6)
        ra = Arrow([2.6, 1.3, 0], [4.2, 1.3, 0], color=NAVY, buff=0,
                   stroke_width=6)
        ll = Text("moving left", font=SERIF, color=CRIMSON, font_size=24)
        rl = Text("moving right", font=SERIF, color=NAVY, font_size=24)
        ll.next_to(la, UP, buff=0.2)
        rl.next_to(ra, UP, buff=0.2)
        self.play(FadeIn(la), FadeIn(ll), FadeIn(ra), FadeIn(rl), run_time=0.8)
        self.play(left.animate.shift(LEFT * 1.1),
                  right.animate.shift(RIGHT * 1.1),
                  run_time=3.0, rate_func=linear)
        bl = Text("same |ψ|² — the phase knows the direction", font=SERIF,
                  color=INK, font_size=26, slant=ITALIC)
        bl.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)


class B07_TheStructuralI(Scene):   # 10.53s — the i is load-bearing
    def construct(self):
        ipart = _math(r"i\hbar", font_size=56, color=WHITE, plain="iℏ")
        rest = _math(r"\,\frac{\partial \psi}{\partial t} = \hat{H}\,\psi",
                     font_size=56, color=WHITE, plain="∂ψ/∂t = Ĥψ")
        row = VGroup(ipart, rest).arrange(RIGHT, buff=0.15)
        card = Rectangle(width=9.0, height=row.height + 1.0)
        card.set_fill(SLATE, 1).set_stroke(width=0)
        row.move_to(card)
        eq = VGroup(card, row).to_edge(UP, buff=0.9)
        self.play(FadeIn(eq), run_time=1.0)
        ring = HandRing(ipart, color=TERRA)
        self.play(Create(ring), run_time=0.9)
        self.wait(0.6)

        y0 = -1.9
        base = Line([-6.0, y0, 0], [6.0, y0, 0], color=INK, stroke_width=2)
        im = DashedVMobject(
            _wave_curve(0.0, 1.3, 4.0, 1.1, y0, GRAY_IM, phase=PI / 2,
                        x_lo=-5.8, x_hi=5.8), num_dashes=48)
        iml = LabelChip("Im ψ", accent=SLATE, size=22)
        iml.next_to(base, UP, buff=1.6).to_edge(LEFT, buff=0.9)
        self.play(Create(base), Create(im), FadeIn(iml), run_time=1.2)
        flat = Line([-5.8, y0, 0], [5.8, y0, 0], color=GRAY_IM,
                    stroke_width=3.5)
        chip1 = LabelChip("erase it", accent=CRIMSON, size=22)
        chip1.move_to([4.4, 0.4, 0])
        self.play(FadeIn(chip1), Transform(im, flat), run_time=1.0)
        chip2 = LabelChip("one time-step", accent=NAVY, size=22)
        chip2.next_to(chip1, DOWN, buff=0.25)
        self.play(FadeIn(chip2), run_time=0.5)
        regrown = DashedVMobject(
            _wave_curve(0.0, 1.3, 4.0, 1.1, y0, GRAY_IM, phase=PI / 2,
                        x_lo=-5.8, x_hi=5.8), num_dashes=48)
        self.play(Transform(im, regrown), run_time=1.2, rate_func=linear)
        bl = SerifLabel("it grows right back", TERRA, size=30)
        bl.to_edge(DOWN, buff=0.6)
        self.play(Write(bl[0]), Create(bl[1]), run_time=0.9)
        self.wait(3.2)


class B08_DotsBuildTheCurve(Scene):  # 10.03s — the histogram is the physics
    def construct(self):
        rng = np.random.default_rng(31)
        y0 = -2.5
        sigma = 1.5
        curve_h = 3.6
        xs = np.linspace(-5.4, 5.4, 90)
        curve = VMobject(color=NAVY, stroke_width=4)
        curve.set_points_smoothly(
            [np.array([x, y0 + curve_h * np.exp(-x * x / (2 * sigma ** 2)), 0])
             for x in xs])
        cl = LabelChip("|ψ|²", accent=NAVY, size=22)
        cl.move_to([-4.6, 1.6, 0])
        self.play(Create(curve), FadeIn(cl), run_time=1.2, rate_func=linear)

        # three waves of detections; bars grow into the curve
        edges = np.linspace(-5.4, 5.4, 19)          # 18 bins
        counts = np.zeros(18)
        waves = [15, 60, 240]
        scale = curve_h / (waves[-1] + waves[0] + waves[1]) * 5.6
        bars = VGroup(*[Rectangle(width=0.56, height=0.001)
                        .set_fill(NAVY, 0.30).set_stroke(width=0)
                        .move_to([(edges[i] + edges[i + 1]) / 2, y0, 0],
                                 aligned_edge=DOWN) for i in range(18)])
        self.add(bars)
        for wi, n in enumerate(waves):
            pts = np.clip(rng.normal(0, sigma, n), -5.3, 5.3)
            dots = VGroup(*[Dot([x, y0 + 0.12 + 0.05 * rng.uniform(0, 1), 0],
                                radius=0.03, color=INK) for x in pts])
            hist, _ = np.histogram(pts, bins=edges)
            counts += hist
            grown = VGroup(*[Rectangle(width=0.56,
                                       height=max(float(c) * scale, 0.001))
                             .set_fill(NAVY, 0.30).set_stroke(width=0)
                             .move_to([(edges[i] + edges[i + 1]) / 2, y0, 0],
                                      aligned_edge=DOWN)
                             for i, c in enumerate(counts)])
            self.play(FadeIn(dots, lag_ratio=0.02),
                      run_time=0.9 if wi < 2 else 1.3)
            self.play(Transform(bars, grown), FadeOut(dots),
                      run_time=0.8 if wi < 2 else 1.0)
        bl = SerifLabel("one dot at a time — the histogram is ψ²", CRIMSON,
                        size=30)
        bl.to_edge(UP, buff=0.75)
        self.play(Write(bl[0]), Create(bl[1]), run_time=0.9)
        self.wait(1.7)


class B11_Next(Scene):             # 5.33s — outro law replaces this slot
    def construct(self):
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE SCHRÖDINGER EQUATION", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        s = Text("quantum, vol. 1 · chapter 4", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(3.4)
