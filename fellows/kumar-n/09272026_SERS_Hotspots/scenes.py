"""
scenes.py: sers-hot-spots (landscape 16:9)

  B02_FourthPower    log-scale bars: field x2 -> signal x16, field x10 -> signal ~x10,000
  B03_GapHotSpot     two nanoparticles, glowing nanometre gap (SCHEMATIC)
  B04_SixtyThree     share of molecules (0.0063%) vs share of signal (24%), Fang et al. 2008
  B05_WhyModelCares  three spots on one substrate -> three different spectra (ILLUSTRATIVE)

Lessons baked in: string weights, footer->kicker from t=0, helper-built captions,
fills >= 0.4 opacity, scene ~1 s under audio at ~3.1 words/s.
Safe area x +/-6.3, y +/-3.4. No text sits on a Line/Arrow/curve.
"""

from manim import *
import numpy as np

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
CARD = "#FFFFFF"
FOOTER = "SERS physics · Hot spots"

config.background_color = PAGE


def fit(m, maxw):
    if m.width > maxw:
        m.scale_to_fit_width(maxw)
    return m


def make_title(s):
    t = Text(s, font_size=40, color=INK, weight="BOLD")
    fit(t, 11.5)
    return t.to_edge(UP, buff=0.75)


def make_kicker(s, color=INK):
    k = Text(s, font_size=28, color=color)
    fit(k, 11.5)
    return k.to_edge(DOWN, buff=0.65)


def make_caption(s, y, color=INK, size=26, maxw=8.8):
    c = Text(s, font_size=size, color=color)
    fit(c, maxw)
    return c.move_to([0, y, 0])


def grow_from_left(scene, m, run_time=0.8):
    s = m.copy()
    s.stretch_to_fit_width(0.04)
    s.move_to(m.get_left() + RIGHT * 0.02)
    scene.add(s)
    scene.play(ReplacementTransform(s, m), run_time=run_time)


def grow_from_point(scene, m, run_time=0.5):
    s = m.copy().scale(0.04)
    scene.add(s)
    scene.play(ReplacementTransform(s, m), run_time=run_time)


def opening(scene, title_text):
    title = make_title(title_text)
    footer = make_kicker(FOOTER)
    scene.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(footer), run_time=0.8)
    return title, footer


def hbar(x0, y, length, color, h=0.35, op=0.9):
    r = Rectangle(width=max(length, 0.04), height=h, stroke_width=0, fill_color=color, fill_opacity=op)
    return r.move_to([x0 + max(length, 0.04) / 2, y, 0])


def right_label(s, x_right, y, size=24, color=INK):
    t = Text(s, font_size=size, color=color)
    return t.move_to([0, y, 0]).align_to([x_right, 0, 0], RIGHT)


# B02: The fourth-power rule  (~14.8 s; narration ~49 words ≈ 15.8 s)
# formula y 1.95 | bars from x -2.0 (log10 scale, 1.2 units per decade):
#   field x2 -> 0.36, signal x16 -> 1.44, field x10 -> 1.2, signal x10^4 -> 4.8 (right end 2.8)
# rows y 0.95 / 0.45 / -0.55 / -1.05 | labels right-aligned at x -2.2 | tag (5.0, -1.75)

class B02_FourthPower(Scene):
    def construct(self):
        title, footer = opening(self, "The Fourth-Power Rule")

        formula = Text("signal  ∝  |E|⁴   (approximately)", font_size=32, color=INK).move_to([0, 1.95, 0])
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(0.4)

        X0, U = -1.5, 1.6
        tracks = VGroup(*[Rectangle(width=4 * U, height=0.35, stroke_color=SOFT, stroke_width=1.5, fill_opacity=0)
                          .move_to([X0 + 2 * U, y, 0]) for y in (0.95, 0.45, -0.55, -1.05)])
        grow_from_left(self, tracks, run_time=0.6)
        rows = [
            ("field ×2", np.log10(2), 0.95, SOFT),
            ("signal ×16", np.log10(16), 0.45, SPARK),
            ("field ×10", np.log10(10), -0.55, SOFT),
            ("signal ≈ ×10,000", np.log10(10000), -1.05, SPARK),
        ]
        waits = [0.0, 2.0, 0.0, 2.5]
        for (lab, lg, y, col), w in zip(rows, waits):
            b = hbar(X0, y, lg * U, col)
            grow_from_left(self, b, run_time=0.9 if col == SPARK else 0.7)
            self.play(FadeIn(right_label(lab, X0 - 0.2, y)), run_time=0.4)
            if w:
                self.wait(w)

        tag = Text("log scale", font_size=20, color=SOFT, slant="ITALIC").move_to([5.0, -1.75, 0])
        self.play(FadeIn(tag), run_time=0.4)
        kicker = make_kicker("A small field boost becomes a huge signal boost")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.9)


# B03: Where the field piles up  (~11.0 s; narration ~37 words ≈ 12 s)
# SCHEMATIC. circles r 1.4 at x ±1.6, y 0.1 -> x -3.0..3.0, y -1.3..1.5; gap x -0.2..0.2
# labels y 1.95 | caption y -1.85 | tag (5.4, -1.85)

class B03_GapHotSpot(Scene):
    def construct(self):
        title, footer = opening(self, "Where the Field Piles Up")

        left = Circle(radius=1.4, stroke_width=0, fill_color=SOFT, fill_opacity=0.85).move_to([-1.6, 0.1, 0])
        right = Circle(radius=1.4, stroke_width=0, fill_color=SOFT, fill_opacity=0.85).move_to([1.6, 0.1, 0])
        grow_from_point(self, left, run_time=0.8)
        grow_from_point(self, right, run_time=0.8)
        lab_l = Text("metal nanoparticles", font_size=24, color=INK).move_to([-3.6, 1.95, 0])
        tag = Text("schematic", font_size=20, color=SOFT, slant="ITALIC").move_to([5.4, -1.85, 0])
        self.play(FadeIn(lab_l), FadeIn(tag), run_time=0.4)
        self.wait(0.8)

        core = Ellipse(width=0.3, height=0.9, stroke_width=0, fill_color=SPARK, fill_opacity=0.95).move_to([0, 0.1, 0])
        grow_from_point(self, core, run_time=0.8)
        halo = Ellipse(width=0.9, height=1.6, stroke_width=0, fill_color=SPARK, fill_opacity=0.45).move_to([0, 0.1, 0])
        halo.set_z_index(-1)
        grow_from_point(self, halo, run_time=0.6)

        lab_r = Text("nanometre-scale gap: the hot spot", font_size=24, color=SPARK).move_to([3.4, 1.95, 0])
        fit(lab_r, 5.4)
        arrow = Arrow([2.3, 1.7, 0], [0.35, 0.55, 0], buff=0, color=SPARK, stroke_width=4)
        self.play(FadeIn(lab_r), GrowArrow(arrow), run_time=0.9)
        self.wait(1.5)

        cap = make_caption("Everywhere else: far weaker enhancement", -1.85)
        self.play(FadeIn(cap), run_time=0.5)
        self.play(halo.animate.scale(1.15), run_time=0.6)
        self.wait(1.0)

        kicker = make_kicker("Hot spots: nanometre gaps where light concentrates")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.7)


# B04: 63 in a million  (~13.5 s; narration ~45 words ≈ 14.5 s)
# tracks x -1.0..5.0 (100% = 6.0 units), rows y 0.7 / -0.6 (h 0.45)
# values above tracks at y 1.25 / -0.05 | row labels right-aligned at x -1.2 | source y -1.6

class B04_SixtyThree(Scene):
    def construct(self):
        title, footer = opening(self, "63 in a Million")

        X0, W = -1.0, 6.0
        ys = [0.7, -0.6]
        tracks = VGroup(*[Rectangle(width=W, height=0.45, stroke_color=SOFT, stroke_width=2,
                                    fill_opacity=0).move_to([X0 + W / 2, y, 0]) for y in ys])
        grow_from_left(self, tracks)
        labs = VGroup(right_label("Share of molecules", X0 - 0.2, ys[0], size=26),
                      right_label("Share of signal", X0 - 0.2, ys[1], size=26))
        self.play(FadeIn(labs), run_time=0.5)
        self.wait(1.0)

        b1 = hbar(X0, ys[0], 0.0063 / 100 * W, SPARK, h=0.45)
        grow_from_left(self, b1, run_time=0.6)
        v1 = Text("0.0063%  (63 per million)", font_size=24, color=INK).move_to([0, 1.25, 0]).align_to([X0, 0, 0], LEFT)
        self.play(FadeIn(v1), run_time=0.5)
        self.wait(2.2)

        b2 = hbar(X0, ys[1], 0.24 * W, SPARK, h=0.45)
        grow_from_left(self, b2, run_time=1.0)
        v2 = Text("24% of the total SERS signal", font_size=24, color=INK).move_to([0, -0.05, 0]).align_to([X0, 0, 0], LEFT)
        self.play(FadeIn(v2), run_time=0.5)
        self.wait(2.2)

        src = make_caption("Fang, Seong & Dlott, Science 2008 · silver-coated nanospheres", -1.6, color=SOFT, size=22, maxw=10.5)
        self.play(FadeIn(src), run_time=0.5)
        box = SurroundingRectangle(b2, color=INK, buff=0.08, stroke_width=3)
        grow_from_left(self, box, run_time=0.6)
        self.wait(1.0)

        kicker = make_kicker("Almost none of the molecules. A quarter of the signal.")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.5)


# B05: Why your model cares  (~17.7 s; narration ~58 words ≈ 18.7 s)
# ILLUSTRATIVE. strip x -5.7..-1.5, y 0.35..0.85; rings r 0.45 at x -5.0/-3.6/-2.2
# spectra x 1.2..4.6, baselines y 0.95 / -0.05 / -1.05, tops <= +0.7 | labels x ~0.6
# caption y -1.75 | kicker top ~-2.95

def _mini(x, scale):
    g = lambda mu, s: np.exp(-0.5 * ((x - mu) / s) ** 2)
    return scale * (0.55 * g(1.8, 0.12) + 0.35 * g(2.7, 0.18) + 0.7 * g(3.5, 0.1) + 0.25 * g(4.2, 0.15))


class B05_WhyModelCares(Scene):
    def construct(self):
        title, footer = opening(self, "Why Your Model Cares")

        strip = Rectangle(width=4.2, height=0.5, stroke_width=0, fill_color=SOFT, fill_opacity=0.5).move_to([-3.6, 0.6, 0])
        grow_from_left(self, strip)
        rng = np.random.default_rng(11)
        dots = VGroup(*[Dot([-5.6 + 4.0 * rng.random(), 0.42 + 0.36 * rng.random(), 0], radius=0.05, color=SPARK)
                        for _ in range(14)])
        grow_from_point(self, dots, run_time=0.6)
        sub_lab = Text("one substrate", font_size=24, color=INK).move_to([-3.6, 1.35, 0])
        self.add(sub_lab)
        self.wait(0.8)

        rings = VGroup()
        for x in (-5.0, -3.6, -2.2):
            r = Circle(radius=0.45, stroke_color=INK, stroke_width=3).move_to([x, 0.6, 0])
            grow_from_point(self, r, run_time=0.4)
            rings.add(r)
        self.wait(0.8)

        xs = np.arange(1.2, 4.6001, 0.04)
        for i, (base, sc) in enumerate([(0.95, 1.0), (-0.05, 0.45), (-1.05, 0.75)]):
            c = VMobject(color=INK, stroke_width=3)
            c.set_points_smoothly([np.array([x, base + _mini(x, sc), 0]) for x in xs])
            grow_from_left(self, c, run_time=0.7)
            self.add(Text(f"spot {i + 1}", font_size=22, color=SOFT).move_to([0.6, base + 0.3, 0]))

        cap = make_caption("Same substrate, different hot spots, different spectra", -1.75)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.0)

        self.play(rings.animate.set_stroke(color=SPARK),
                  Transform(cap, make_caption("Split by sample, not by spectrum · test on new batches", -1.75, color=SPARK)),
                  run_time=0.8)
        self.wait(3.0)

        kicker = make_kicker("Keep each sample's spectra together. Test on new substrate batches.")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.5)
