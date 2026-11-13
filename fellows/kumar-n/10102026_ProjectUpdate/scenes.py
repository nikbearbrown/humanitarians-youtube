"""
scenes.py: sers-ml-4-5-update (landscape 16:9)

  B02_WhichBottleneck   fork: too few spectra -> augment; too few labels -> pretrain
  B03_AugmentRealism    spectrum with realistic vs excessive noise band (ILLUSTRATIVE)
  B04_CostAsymmetry     big cheap unlabeled pool vs few expensive labels
  B05_Evidence          SMAE vs ResNet; SemiRaman at 5% / 10% labels; not-SERS caveat

Lessons from sers-ml-4-4-update baked in:
  - weight/slant as strings ("BOLD"/"ITALIC"): GATE A's stub lacks the constants
  - a footer caption from second one that becomes the kicker: keeps GATE V fill > 55%
  - scene lengths sized to Kokoro's real pace (~3.25 words/s), ~1 s under the audio
Safe area (GATE B, landscape): x +/-6.3, y +/-3.4. Title to_edge(UP, 0.75),
footer/kicker to_edge(DOWN, 0.65). No text sits on a Line/Arrow/curve.
"""

from manim import *
import numpy as np

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
CARD = "#FFFFFF"
FOOTER = "Paper 2 · §4.5 Training Strategies for Limited Data"

config.background_color = PAGE


# Helpers

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


def make_caption(s, color=INK):
    c = Text(s, font_size=26, color=color)
    fit(c, 8.8)
    return c.move_to([0, -1.85, 0])


def make_card(w, h, center, stroke=INK):
    r = RoundedRectangle(corner_radius=0.12, width=w, height=h,
                         stroke_color=stroke, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1)
    return r.move_to(center)


def label_in(card, s, size=24, color=INK):
    t = Text(s, font_size=size, color=color, line_spacing=0.8)
    fit(t, card.width - 0.4)
    return t.move_to(card.get_center())


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


# B02: Which bottleneck?  (~13.0 s; narration ~45 words ≈ 14 s)
# question card y 0.85..1.75 | answer cards y -0.2..-1.6, x -5.8..-0.8 / 0.8..5.8
# footer/kicker top ~-2.95

class B02_WhichBottleneck(Scene):
    def construct(self):
        title, footer = opening(self, "Which Bottleneck?")

        q = make_card(7.0, 0.9, [0, 1.3, 0])
        grow_from_left(self, q)
        self.play(FadeIn(label_in(q, "What is actually scarce?", size=28)), run_time=0.5)
        self.wait(0.5)

        a_l = Arrow([-1.5, 0.8, 0], [-3.3, -0.15, 0], buff=0, color=SOFT, stroke_width=4)
        a_r = Arrow([1.5, 0.8, 0], [3.3, -0.15, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(a_l), GrowArrow(a_r), run_time=0.7)

        left = make_card(5.0, 1.4, [-3.3, -0.9, 0])
        grow_from_left(self, left)
        self.play(FadeIn(label_in(left, "Too few spectra\n→ data augmentation", size=26)), run_time=0.5)
        self.wait(1.5)

        right = make_card(5.0, 1.4, [3.3, -0.9, 0])
        grow_from_left(self, right)
        self.play(FadeIn(label_in(right, "Too few labels\n→ self-supervised pretraining", size=26)), run_time=0.5)
        self.wait(1.0)

        self.play(left.animate.set_stroke(color=SPARK, width=4),
                  right.animate.set_stroke(color=SPARK, width=4), run_time=0.5)
        kicker = make_kicker("Spectra scarce → augment.  Labels scarce → pretrain.")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(2.8)


# B03: Augment realistically  (~17.4 s; narration ~60 words ≈ 18.5 s)
# ILLUSTRATIVE synthetic spectrum. Curve x -5..5, y -0.8..1.0; widest band
# +/-0.45 -> y -1.25..1.45. Sub y 2.05 | caption y -1.85 | tag x ~4.8..6.0 y -1.85
# No text overlaps the curve or band.

def _spectrum_y(x):
    g = lambda mu, s: np.exp(-0.5 * ((x - mu) / s) ** 2)
    return -0.8 + 1.6 * g(-2.5, 0.25) + 1.0 * g(-0.5, 0.35) + 1.8 * g(1.2, 0.2) + 0.7 * g(3.2, 0.4)


XS = np.arange(-5.0, 5.0001, 0.05)


def make_curve():
    pts = [np.array([x, _spectrum_y(x), 0]) for x in XS]
    c = VMobject(color=INK, stroke_width=3)
    c.set_points_smoothly(pts)
    return c


def make_band(half, color, opacity):
    upper = [np.array([x, _spectrum_y(x) + half, 0]) for x in XS]
    lower = [np.array([x, _spectrum_y(x) - half, 0]) for x in XS[::-1]]
    return Polygon(*upper, *lower, stroke_width=0, fill_color=color, fill_opacity=opacity)


class B03_AugmentRealism(Scene):
    def construct(self):
        title, footer = opening(self, "Augment Realistically")

        sub = Text("Same spectrum, two noise levels", font_size=28, color=SOFT)
        sub.move_to([0, 2.05, 0])
        tag = Text("illustrative", font_size=20, color=SOFT, slant="ITALIC").move_to([5.4, -1.85, 0])
        self.play(FadeIn(sub), FadeIn(tag), run_time=0.5)

        curve = make_curve()
        grow_from_left(self, curve, run_time=1.0)
        curve.set_z_index(1)
        self.wait(1.0)

        band = make_band(0.08, INK, 0.4)
        flat = band.copy().stretch(0.05, 1)
        self.add(flat)
        self.play(ReplacementTransform(flat, band), run_time=0.8)
        cap = make_caption("Measured instrument noise: realistic")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.0)

        cap2 = make_caption("Far more noise than the instrument makes", SPARK)
        self.play(Transform(band, make_band(0.45, SPARK, 0.6)), Transform(cap, cap2), run_time=1.2)
        self.wait(3.0)

        cap3 = make_caption("Set from measured noise")
        kicker = make_kicker("Rule: set augmentation from measured instrument and substrate noise")
        self.play(Transform(band, make_band(0.08, INK, 0.4)), Transform(cap, cap3),
                  Transform(footer, kicker), run_time=1.0)
        self.wait(4.6)


# B04: The cost asymmetry  (~15.0 s; narration ~52 words ≈ 16 s)
# pool x -5.45..-1.95, y -0.8..1.0 | labeled dots x 2.0..3.2, y 0.1
# labels y 1.75 | process card x -2.2..2.2, y -2.1..-1.4 | kicker top ~-2.95

class B04_CostAsymmetry(Scene):
    def construct(self):
        title, footer = opening(self, "The Cost Asymmetry")

        pool = VGroup(*[Dot([-5.45 + 0.5 * c, 1.0 - 0.45 * r, 0], radius=0.09, color=SOFT)
                        for r in range(5) for c in range(8)])
        grow_from_point(self, pool, run_time=1.0)
        pl = Text("Unlabeled spectra · cheap", font_size=26, color=INK).move_to([-3.7, 1.75, 0])
        fit(pl, 4.6)
        self.play(FadeIn(pl), run_time=0.5)
        self.wait(2.0)

        labeled = VGroup(*[Dot([x, 0.1, 0], radius=0.14, color=SPARK) for x in (2.0, 2.6, 3.2)])
        grow_from_point(self, labeled, run_time=0.6)
        ll = Text("Labeled · needs a reference method", font_size=26, color=SPARK).move_to([3.3, 1.75, 0])
        fit(ll, 5.4)
        self.play(FadeIn(ll), run_time=0.5)
        self.wait(2.5)

        a1 = Arrow([-3.0, -1.05, 0], [-2.25, -1.6, 0], buff=0, color=SOFT, stroke_width=4)
        a2 = Arrow([2.6, -0.25, 0], [2.25, -1.45, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.7)

        card = make_card(4.4, 0.7, [0, -1.75, 0], stroke=SPARK)
        grow_from_left(self, card)
        self.play(FadeIn(label_in(card, "Pretrain on the pool → fine-tune on the few", size=24)), run_time=0.5)
        self.wait(1.5)

        kicker = make_kicker("Pretrain where data is cheap.  Fine-tune where labels are scarce.")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(2.8)


# B05: The evidence  (~20.5 s; narration ~70 words ≈ 21.5 s)
# bars baseline y -1.6, 3.0 units per 100% -> tops <= 1.16 | values ~0.3 above
# panel titles y 1.95 | names y -1.95 | kicker top ~-2.95
# Figures: Ren et al. 2025 (SMAE 83.90 vs ResNet 83.40), Sun & Wang 2026
# (SemiRaman 89.2% @5% labels, 92.0% @10% labels; checked by author).

BASE = -1.6
UNIT = 3.0 / 100.0


def bar(x, pct, color):
    h = pct * UNIT
    return Rectangle(width=0.9, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=0.9).move_to([x, BASE + h / 2, 0])


def grow_bar(scene, b, run_time=0.6):
    seed = Rectangle(width=0.9, height=0.02, stroke_width=0, fill_color=b.get_fill_color(),
                     fill_opacity=0.9).move_to([b.get_center()[0], BASE, 0])
    scene.add(seed)
    scene.play(ReplacementTransform(seed, b), run_time=run_time)


class B05_Evidence(Scene):
    def construct(self):
        title, footer = opening(self, "The Evidence")

        specs_l = [(-4.6, 83.90, SPARK, "SMAE", "83.90%"), (-3.0, 83.40, SOFT, "ResNet\n(supervised)", "83.40%")]
        specs_r = [(2.6, 89.2, SPARK, "5% labels", "89.2%"), (4.2, 92.0, SPARK, "10% labels", "92.0%")]

        def panel(head, x_head, specs, extra_wait):
            h = Text(head, font_size=26, color=INK, weight="BOLD").move_to([x_head, 1.95, 0])
            fit(h, 5.0)
            self.play(FadeIn(h), run_time=0.5)
            bars = []
            for x, pct, col, _, _ in specs:
                b = bar(x, pct, col)
                grow_bar(self, b)
                bars.append(b)
            vals = VGroup(*[Text(v, font_size=24, color=INK).next_to(b, UP, buff=0.15)
                            for b, (_, _, _, _, v) in zip(bars, specs)])
            names = VGroup(*[fit(Text(n, font_size=20, color=INK, line_spacing=0.8), 1.5).move_to([x, -1.98, 0])
                             for x, _, _, n, _ in specs])
            self.play(FadeIn(vals), run_time=0.5)
            self.play(FadeIn(names), run_time=0.5)
            self.wait(extra_wait)
            return bars

        bl = panel("Ren et al. · SMAE", -3.8, specs_l, 3.5)
        br = panel("Sun & Wang · SemiRaman", 3.4, specs_r, 4.0)

        kicker = make_kicker("Both studies: conventional Raman of bacteria, not SERS", color=SPARK)
        self.play(*[b.animate.set_fill(opacity=0.65) for b in bl + br],
                  Transform(footer, kicker), run_time=1.0)
        self.wait(5.8)
