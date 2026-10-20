"""
scenes.py: sers-ml-4-6-update (landscape 16:9)

  B02_ComputeReframed      model block shrinks (prune / quantize / distill) -> field device -> "untested" card
  B03_InterpretUpdated     noisy point-by-point attribution -> region-grouped (ILLUSTRATIVE)
  B04_GeneralizeQualified  train site -> new device / new site / new batch; device gets early SERS work

Baked-in lessons from 4.4 / 4.5:
  - weight/slant as strings; footer from t=0 that becomes the kicker (GATE V fill)
  - captions that change in place are built by a helper (GATE W reads literal coords)
  - translucent fills >= 0.4 opacity (GATE V contrast)
  - scene length ~1 s under Kokoro audio at ~3.1 words/s
Safe area x +/-6.3, y +/-3.4. No text sits on a Line/Arrow/curve.
"""

from manim import *
import numpy as np

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
CARD = "#FFFFFF"
FOOTER = "Paper 2 · §4.6 Practical Deployment Considerations"

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


# B02: Compute, reframed  (~18.5 s; narration ~60 words ≈ 19.4 s)
# caption y 1.95 | block x -5.4..-1.8, y -1.0..1.4 (shrinks in place)
# arrow y 0.2, x -2.7..2.1 | device x 2.2..5.4, y -0.6..1.0 | question x 2.0..5.6, y -2.0..-1.2

class B02_ComputeReframed(Scene):
    def construct(self):
        title, footer = opening(self, "Compute: Reframed")

        block = VGroup(*[Square(side_length=0.55, stroke_width=0, fill_color=INK, fill_opacity=0.85)
                         .move_to([-5.1 + 0.6 * c, 1.1 - 0.6 * r, 0]) for r in range(4) for c in range(6)])
        grow_from_point(self, block, run_time=0.8)
        self.wait(1.0)

        cap = make_caption("Pruning", 1.95)
        self.play(FadeIn(cap), block.animate.scale(0.75), run_time=0.9)
        self.wait(1.2)
        self.play(Transform(cap, make_caption("Quantization", 1.95)),
                  block.animate.scale(0.75).set_fill(color=SOFT), run_time=0.9)
        self.wait(1.2)
        self.play(Transform(cap, make_caption("Distillation", 1.95)),
                  block.animate.scale(0.7), run_time=0.9)
        self.wait(1.5)

        arrow = Arrow([-2.7, 0.2, 0], [2.1, 0.2, 0], buff=0, color=SOFT, stroke_width=4)
        self.play(GrowArrow(arrow), run_time=0.6)
        device = make_card(3.2, 1.6, [3.8, 0.2, 0])
        grow_from_left(self, device)
        self.play(FadeIn(label_in(device, "Field device\nphone · edge chip", size=26)), run_time=0.5)
        self.wait(1.5)

        q = make_card(3.6, 0.8, [3.8, -1.6, 0], stroke=SPARK)
        grow_from_left(self, q)
        self.play(FadeIn(label_in(q, "Accuracy on real SERS? Untested", size=22, color=SPARK)), run_time=0.5)
        self.wait(1.5)

        kicker = make_kicker("Compress for the field, but budget for an accuracy cost")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(2.3)


# B03: Interpretability, updated  (~19.6 s; narration ~64 words ≈ 20.6 s)
# ILLUSTRATIVE spectrum + attributions. sub y 2.05 | curve x -5..5, y 0.5..1.6
# bars baseline y -0.9, tops <= 0.0 | caption y -1.5 | tag x ~4.8..6.0, y -1.5

def _spec(x):
    g = lambda mu, s: np.exp(-0.5 * ((x - mu) / s) ** 2)
    return 0.5 + 0.9 * g(-2.5, 0.25) + 0.6 * g(-0.5, 0.35) + 1.1 * g(1.2, 0.2) + 0.45 * g(3.2, 0.4)


XS = np.arange(-5.0, 5.0001, 0.05)
BAR_BASE = -0.9


def make_curve():
    c = VMobject(color=INK, stroke_width=3)
    c.set_points_smoothly([np.array([x, _spec(x), 0]) for x in XS])
    return c


def _bar(x, h, w, color, op=0.85):
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=op).move_to([x, BAR_BASE + h / 2, 0])


class B03_InterpretUpdated(Scene):
    def construct(self):
        title, footer = opening(self, "Interpretability: Updated")

        sub = Text("Which wavenumbers drove the prediction?", font_size=28, color=SOFT).move_to([0, 2.05, 0])
        fit(sub, 10.0)
        tag = Text("illustrative", font_size=20, color=SOFT, slant="ITALIC").move_to([5.4, -1.5, 0])
        self.play(FadeIn(sub), FadeIn(tag), run_time=0.5)

        curve = make_curve()
        grow_from_left(self, curve, run_time=1.0)
        self.wait(1.0)

        rng = np.random.default_rng(7)
        noisy = VGroup(*[_bar(x, 0.12 + 0.75 * rng.random(), 0.12, SPARK)
                         for x in np.arange(-4.9, 4.91, 0.2)])
        flat = noisy.copy().stretch(0.05, 1).move_to([0, BAR_BASE, 0])
        self.add(flat)
        self.play(ReplacementTransform(flat, noisy), run_time=1.0)
        cap = make_caption("Point-by-point attribution: noisy", -1.5)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.0)

        regions = VGroup(_bar(-2.5, 0.85, 1.0, SPARK), _bar(-0.5, 0.5, 1.1, SPARK),
                         _bar(1.2, 0.9, 0.9, SPARK), _bar(3.2, 0.35, 1.3, SPARK))
        self.play(ReplacementTransform(noisy, regions),
                  Transform(cap, make_caption("Region-grouped attribution (as in GRASS): cleaner", -1.5)),
                  run_time=1.2)
        self.wait(3.5)

        self.play(regions.animate.set_fill(color=INK, opacity=0.75),
                  Transform(cap, make_caption("CRIME (Zaki et al.): built for SERS mixtures", -1.5)),
                  run_time=0.6)
        self.wait(2.0)

        kicker = make_kicker("Use a dedicated spectral method, not unmodified GradCAM")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(3.7)


# B04: Generalization, qualified  (~19.4 s; narration ~62 words ≈ 20 s)
# sub y 2.05 | train card x -5.6..-2.8, y 0.35..1.45 | arrows x -2.8..1.8
# target cards x 1.8..5.4 at y 1.2 / 0.0 / -1.2 (h 0.9) | kicker top ~-2.95

class B04_GeneralizeQualified(Scene):
    def construct(self):
        title, footer = opening(self, "Generalization: Qualified")

        sub = Text("Train once. Deploy somewhere new.", font_size=28, color=SOFT).move_to([0, 2.05, 0])
        self.play(FadeIn(sub), run_time=0.5)

        train = make_card(2.8, 1.1, [-4.2, 0.9, 0])
        grow_from_left(self, train)
        self.play(FadeIn(label_in(train, "Trained here\nsite · instrument · batch", size=22)), run_time=0.5)
        self.wait(1.0)

        ys = [1.2, 0.0, -1.2]
        arrows = [Arrow([-2.8, 0.9, 0], [1.8, y, 0], buff=0, color=SOFT, stroke_width=4) for y in ys]
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.8)

        names = ["New instrument", "New site", "New substrate batch"]
        cards, labels = [], []
        for y, n in zip(ys, names):
            c = make_card(3.6, 0.9, [3.6, y, 0])
            grow_from_left(self, c, run_time=0.6)
            lab = label_in(c, n, size=24)
            self.play(FadeIn(lab), run_time=0.4)
            cards.append(c)
            labels.append(lab)
        self.wait(1.5)

        self.play(*[c.animate.set_stroke(color=SPARK, width=4) for c in cards], run_time=0.6)
        self.wait(2.5)

        self.play(cards[0].animate.set_stroke(color=INK, width=4),
                  Transform(labels[0], label_in(cards[0], "New instrument\nearly SERS work (Mahmud et al.)", size=22)),
                  run_time=1.0)
        self.wait(3.0)

        self.play(Transform(labels[1], label_in(cards[1], "New site\nstill open", size=22, color=SPARK)),
                  Transform(labels[2], label_in(cards[2], "New substrate batch\nstill open", size=22, color=SPARK)),
                  run_time=0.8)
        self.wait(1.0)

        kicker = make_kicker("Cross-device: early SERS work.  Cross-site and cross-substrate: still open.")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.8)
