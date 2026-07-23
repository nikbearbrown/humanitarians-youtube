"""short/vox_scenes.py — PORTRAIT (9:16) relayouts, The Wave Function.

Generated graphics re-band top-and-bottom for the 4.5 x 8 frame — never cut.
B05/B09 use hand -916 media overrides; B01/B03/B10 are focus-aware cuts;
B11 dropped (--no-endcard: the Short ends on the dice-letter kicker).
Render:  bash scripts/vox_run.sh reels/vox-wave-function/short
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _math
import numpy as np

SAFE_W = 3.8
GRAY_IM = "#8A8A8A"


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def serif_lines(lines, size=26, color=INK, buff=0.16):
    g = VGroup(*[Text(t, font=SERIF, color=color, font_size=size)
                 for t in lines]).arrange(DOWN, buff=buff)
    return fit(g)


def anchor_card(spotlight=None):
    return EquationCard(r"P(a \le x \le b) = \int_a^b |\psi|^2\,dx",
                        spotlight=spotlight, width=4.2,
                        plain="P = ∫ |ψ|² dx").to_edge(UP, buff=1.1)


# ---------- curve helpers (portrait x-range) ----------

def _env(x, x0, a):
    return np.exp(-((x - x0) ** 2) / (2 * a * a))


def _density_poly(x0, a, height, y0, color=NAVY, x_lo=-2.1, x_hi=2.1):
    xs = np.linspace(x_lo, x_hi, 70)
    top = [np.array([x, y0 + height * _env(x, x0, a) ** 2, 0]) for x in xs]
    pts = top + [np.array([x_hi, y0, 0]), np.array([x_lo, y0, 0])]
    return Polygon(*pts).set_fill(color, 0.35).set_stroke(color, 2.5)


def _wave_curve(x0, a, k, amp, y0, color, phase=0.0, x_lo=-2.1, x_hi=2.1):
    xs = np.linspace(x_lo, x_hi, 160)
    vm = VMobject(color=color, stroke_width=3)
    vm.set_points_smoothly(
        [np.array([x, y0 + amp * _env(x, x0, a) *
                   np.cos(k * (x - x0) + phase), 0]) for x in xs])
    return vm


# ------------------------------------------------------------- the beats

class B02_Title(Scene):            # 8.67s
    def construct(self):
        eye = Text("QUANTUM MECHANICS", font=SERIF, color=BLUE, font_size=22)
        eye.to_edge(UP, buff=1.4)
        title = VGroup(Text("THE WAVE", font=SERIF, color=INK, font_size=52,
                            weight=BOLD),
                       Text("FUNCTION", font=SERIF, color=INK, font_size=52,
                            weight=BOLD)).arrange(DOWN, buff=0.18)
        fit(title)
        u = Line(title.get_corner(DL) + DOWN * 0.2,
                 title.get_corner(DR) + DOWN * 0.2, color=CRIMSON,
                 stroke_width=2)
        sub = serif_lines(["what ψ", "actually means"], size=26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(title), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(6.5)


class B04_TheCurves(Scene):        # 10.34s — legend top, curves mid-band
    def construct(self):
        legend = VGroup(
            LabelChip("|ψ|²", accent=NAVY, size=18),
            LabelChip("Re ψ", accent=TERRA, size=18),
            LabelChip("Im ψ", accent=SLATE, size=18),
        ).arrange(RIGHT, buff=0.25)
        fit(legend).to_edge(UP, buff=1.2)
        y0 = -0.6
        base = Line([-2.1, y0, 0], [2.1, y0, 0], color=INK, stroke_width=1.8)

        def state(x0, a, amp):
            dens = _density_poly(x0, a, 1.7 * amp, y0)
            re = _wave_curve(x0, a, 6.0, 0.8 * amp, y0 + 0.75 * amp, TERRA)
            im = DashedVMobject(
                _wave_curve(x0, a, 6.0, 0.8 * amp, y0 + 0.75 * amp, GRAY_IM,
                            phase=PI / 2), num_dashes=40)
            return VGroup(dens, re, im)

        start = state(-1.1, 0.45, 1.0)
        end = state(0.9, 0.75, 0.62)
        self.play(Create(base), FadeIn(legend), run_time=0.8)
        self.play(FadeIn(start), run_time=1.4)
        self.play(Transform(start, end), run_time=5.2, rate_func=linear)
        q = Text("?", font=SERIF, color=CRIMSON, font_size=64, weight=BOLD)
        q.move_to([1.35, 1.9, 0])
        self.play(FadeIn(q, scale=1.4), run_time=0.7)
        self.wait(2.2)


class T01_EqSentences(Scene):      # 9.43s
    def construct(self):
        anchor = anchor_card(spotlight="P")
        eye = LabelChip("BORN'S RULE · TANGENT", accent=CRIMSON, size=16)
        eye.next_to(anchor, UP, buff=0.18).align_to(anchor, LEFT)
        rows = VGroup()
        for tag, sentence in (("LHS", ["The odds of finding it", "between a and b."]),
                              ("RHS", ["Add up psi squared", "across that stretch."])):
            c = Text(tag, font=SERIF, color=WHITE, font_size=15)
            box = SurroundingRectangle(c, buff=0.08).set_fill(NAVY, 1).set_stroke(width=0)
            body = serif_lines(sentence, size=23, buff=0.1)
            rows.add(fit(VGroup(VGroup(box, c), body).arrange(RIGHT, buff=0.25,
                                                              aligned_edge=UP)))
        claim = serif_lines(["Odds,", "not certainty."], size=25)
        cu = Line(claim.get_corner(DL) + DOWN * 0.1,
                  claim.get_corner(DR) + DOWN * 0.1, color=CRIMSON,
                  stroke_width=1.6)
        rows.add(VGroup(claim, cu))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.15)
        fit(rows)
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.7)
            self.wait(1.2)
        self.wait(1.5)


class T02_EqGlossary(Scene):       # 10.21s — glossary re-banded as blocks
    def construct(self):
        anchor = anchor_card(spotlight=r"\psi")
        self.add(anchor)
        data = [
            {"sym_tex": r"\psi", "sym": "ψ", "role": "the object",
             "mean": "the wave function", "dom": "complex", "hot": True},
            {"sym_tex": r"|\psi|^2", "sym": "|ψ|²", "role": "the density",
             "mean": "probability per nanometer", "dom": "nm⁻¹", "hot": False},
            {"sym_tex": r"\int_a^b", "sym": "∫ₐᵇ", "role": "the extraction",
             "mean": "sum it over your region", "dom": "0–1", "hot": False},
        ]
        blocks = VGroup()
        for r in data:
            sym = _math(r["sym_tex"], font_size=32,
                        color=CRIMSON if r["hot"] else INK, plain=r["sym"])
            role = Text(r["role"], font=SERIF, font_size=17, slant=ITALIC,
                        color=TERRA if r["hot"] else BLUE)
            topline = VGroup(sym, role).arrange(RIGHT, buff=0.28,
                                                aligned_edge=DOWN)
            mean = Text(r["mean"], font=SERIF, color=INK, font_size=19)
            dom = Text(r["dom"], font=MONO, color=INK, font_size=14)
            blocks.add(fit(VGroup(topline, fit(mean), dom)
                           .arrange(DOWN, aligned_edge=LEFT, buff=0.12)))
        blocks.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 1.2)
        fit(blocks)
        self.play(FadeIn(blocks, shift=UP * 0.15), run_time=1.0)
        self.wait(9.2)


class T03_EqExample(Scene):        # 10.63s
    def construct(self):
        anchor = anchor_card()
        self.add(anchor)
        scenario = serif_lines(["ψ = e^(−|x|/a),", "a = 0.5 nm."], size=22)
        lv = Text("inside ±a: 86.5%", font=MONO, color=CRIMSON, font_size=28)
        rv = Text("peak: 2 nm⁻¹", font=MONO, color=NAVY, font_size=28)
        pair = VGroup(fit(lv), fit(rv)).arrange(DOWN, buff=0.2)
        verdict = serif_lines(["a density may exceed 1 —", "a probability never does"],
                              size=22)
        vu = Line(verdict.get_corner(DL) + DOWN * 0.1,
                  verdict.get_corner(DR) + DOWN * 0.1, color=TERRA,
                  stroke_width=1.6)
        cost = serif_lines(["read it as probability", "and it's a units error"],
                           size=19)
        stack = VGroup(scenario, pair, VGroup(verdict, vu), cost)
        stack.arrange(DOWN, buff=0.42).move_to(DOWN * 1.15)
        fit(stack)
        self.play(FadeIn(stack[0]), run_time=0.8)
        self.wait(1.8)
        self.play(FadeIn(stack[1], shift=UP * 0.15), run_time=0.9)
        self.wait(1.9)
        self.play(FadeIn(stack[2]), run_time=0.7)
        self.wait(1.5)
        self.play(FadeIn(stack[3]), run_time=0.7)
        self.wait(2.3)


class B06_TwoPackets(Scene):       # 10.76s — TOP AND BOTTOM (the law)
    def construct(self):
        title = fit(Text("identical humps — opposite motion", font=SERIF,
                         color=NAVY, font_size=24))
        title.to_edge(UP, buff=0.7)               # ONE line: y ≈ 3.0..3.3, far above the label band

        def panel(cy, k_sign):
            dens = _density_poly(0.0, 0.50, 1.15, cy, x_lo=-1.6, x_hi=1.6)
            rip = _wave_curve(0.0, 0.50, 7.0 * k_sign, 0.5, cy + 0.5, TERRA,
                              x_lo=-1.6, x_hi=1.6)
            return VGroup(dens, rip)

        top = panel(0.55, -1.0)      # hump peaks ≈ 1.7 — clear of the label band
        bottom = panel(-2.3, 1.0)    # hump peaks ≈ -1.15
        la = Arrow([0.8, 2.0, 0], [-0.8, 2.0, 0], color=CRIMSON, buff=0,
                   stroke_width=5)
        ll = Text("moving left", font=SERIF, color=CRIMSON, font_size=20)
        ll.next_to(la, UP, buff=0.12)             # centered ABOVE — stays in frame
        ra = Arrow([-0.8, -0.75, 0], [0.8, -0.75, 0], color=NAVY, buff=0,
                   stroke_width=5)
        rl = Text("moving right", font=SERIF, color=NAVY, font_size=20)
        rl.next_to(ra, UP, buff=0.12)
        self.play(FadeIn(title), run_time=1.0)
        self.play(FadeIn(top[0]), FadeIn(bottom[0]), run_time=1.2)
        self.wait(0.8)
        self.play(Create(top[1]), Create(bottom[1]), run_time=1.4,
                  rate_func=linear)
        self.play(FadeIn(la), FadeIn(ll), FadeIn(ra), FadeIn(rl), run_time=0.8)
        self.play(top.animate.shift(LEFT * 0.45),
                  bottom.animate.shift(RIGHT * 0.45),
                  run_time=3.0, rate_func=linear)
        bl = serif_lines(["same |ψ|² — the phase", "knows the direction"],
                         size=21)
        bl.to_edge(DOWN, buff=0.68)               # bottom edge ≥ −3.32, inside ±3.4 safe
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.7)
        self.wait(1.8)


class B07_TheStructuralI(Scene):   # 10.53s
    def construct(self):
        ipart = _math(r"i\hbar", font_size=40, color=WHITE, plain="iℏ")
        rest = _math(r"\,\frac{\partial \psi}{\partial t} = \hat{H}\,\psi",
                     font_size=40, color=WHITE, plain="∂ψ/∂t = Ĥψ")
        row = VGroup(ipart, rest).arrange(RIGHT, buff=0.12)
        if row.width > 3.7:
            row.scale_to_fit_width(3.7)
        card = Rectangle(width=4.2, height=row.height + 0.7)
        card.set_fill(SLATE, 1).set_stroke(width=0)
        row.move_to(card)
        eq = VGroup(card, row).to_edge(UP, buff=1.1)
        self.play(FadeIn(eq), run_time=1.0)
        ring = HandRing(ipart, color=TERRA)
        self.play(Create(ring), run_time=0.9)
        self.wait(0.6)

        y0 = -1.6
        base = Line([-1.9, y0, 0], [1.9, y0, 0], color=INK, stroke_width=1.8)
        im = DashedVMobject(
            _wave_curve(0.0, 0.75, 6.0, 0.75, y0, GRAY_IM, phase=PI / 2,
                        x_lo=-1.85, x_hi=1.85), num_dashes=40)
        iml = LabelChip("Im ψ", accent=SLATE, size=18)
        iml.next_to(base, UP, buff=1.1).align_to(base, LEFT)
        self.play(Create(base), Create(im), FadeIn(iml), run_time=1.2)
        flat = Line([-1.85, y0, 0], [1.85, y0, 0], color=GRAY_IM,
                    stroke_width=3)
        chip1 = LabelChip("erase it", accent=CRIMSON, size=18)
        chip2 = LabelChip("one time-step", accent=NAVY, size=18)
        chips = VGroup(chip1, chip2).arrange(DOWN, buff=0.2)
        fit(chips).move_to([0, 0.2, 0])
        self.play(FadeIn(chip1), Transform(im, flat), run_time=1.0)
        self.play(FadeIn(chip2), run_time=0.5)
        regrown = DashedVMobject(
            _wave_curve(0.0, 0.75, 6.0, 0.75, y0, GRAY_IM, phase=PI / 2,
                        x_lo=-1.85, x_hi=1.85), num_dashes=40)
        self.play(Transform(im, regrown), run_time=1.2, rate_func=linear)
        bl = serif_lines(["it grows right back —", "motion lives in the phase"],
                         size=21, color=TERRA)
        bl.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(bl), run_time=0.9)
        self.wait(3.2)


class B08_DotsBuildTheCurve(Scene):  # 10.21s — curve top, histogram beneath
    def construct(self):
        rng = np.random.default_rng(31)
        y0 = -2.2
        sigma = 0.75
        curve_h = 2.6
        xs = np.linspace(-1.9, 1.9, 70)
        curve = VMobject(color=NAVY, stroke_width=3.5)
        curve.set_points_smoothly(
            [np.array([x, y0 + curve_h * np.exp(-x * x / (2 * sigma ** 2)), 0])
             for x in xs])
        cl = LabelChip("|ψ|²", accent=NAVY, size=18)
        cl.move_to([-1.35, 1.6, 0])
        lb = serif_lines(["one dot at a time —", "the histogram is ψ²"],
                         size=22, color=CRIMSON)
        lb.to_edge(UP, buff=1.1)
        self.play(Create(curve), FadeIn(cl), run_time=1.2, rate_func=linear)

        edges = np.linspace(-1.9, 1.9, 14)          # 13 bins
        counts = np.zeros(13)
        waves = [15, 60, 240]
        scale = 2.4 / 90
        bars = VGroup(*[Rectangle(width=0.26, height=0.001)
                        .set_fill(NAVY, 0.30).set_stroke(width=0)
                        .move_to([(edges[i] + edges[i + 1]) / 2, y0, 0],
                                 aligned_edge=DOWN) for i in range(13)])
        self.add(bars)
        for wi, n in enumerate(waves):
            pts = np.clip(rng.normal(0, sigma, n), -1.85, 1.85)
            dots = VGroup(*[Dot([x, y0 + 0.1 + 0.05 * rng.uniform(0, 1), 0],
                                radius=0.025, color=INK) for x in pts])
            hist, _ = np.histogram(pts, bins=edges)
            counts += hist
            grown = VGroup(*[Rectangle(width=0.26,
                                       height=max(float(c) * scale, 0.001))
                             .set_fill(NAVY, 0.30).set_stroke(width=0)
                             .move_to([(edges[i] + edges[i + 1]) / 2, y0, 0],
                                      aligned_edge=DOWN)
                             for i, c in enumerate(counts)])
            self.play(FadeIn(dots, lag_ratio=0.02),
                      run_time=0.9 if wi < 2 else 1.3)
            self.play(Transform(bars, grown), FadeOut(dots),
                      run_time=0.8 if wi < 2 else 1.0)
        self.play(FadeIn(lb), run_time=0.9)
        self.wait(1.9)
