"""
scenes.py: sers-gold-vs-silver (landscape 16:9)

  B02_RideResonance    laser line slides onto a plasmon band; enhancement meter rises (SCHEMATIC)
  B03_CommonPairing    silver + 532 nm, gold + 785 nm cards; Mikac et al. 2022 caption
  B04_ClusterShift     isolated vs clustered particles; resonance red-shifts (SCHEMATIC)
  B05_ShelfLife        silver signal fades with oxidation, gold holds (SCHEMATIC)

Lessons baked in: string weights, footer->kicker from t=0, helper-built labels,
fills >= 0.4 opacity, wide content from early frames, scene ~1 s under audio.
Safe area x +/-6.3, y +/-3.4. No text sits on a Line/Arrow/curve.
"""

from manim import *
import numpy as np

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
CARD = "#FFFFFF"
FOOTER = "SERS · Gold vs silver: matching the metal to the laser"

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


def label_at(s, x, y, color=INK, size=24, maxw=8.8, slant="NORMAL"):
    c = Text(s, font_size=size, color=color, slant=slant)
    fit(c, maxw)
    return c.move_to([x, y, 0])


def make_card(w, h, center, stroke=INK):
    r = RoundedRectangle(corner_radius=0.12, width=w, height=h, stroke_color=stroke, stroke_width=2.5,
                         fill_color=CARD, fill_opacity=1)
    return r.move_to(center)


def label_in(card, s, size=26, color=INK):
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


def band(center, height, sigma, base, color, x0, x1, op_stroke=5):
    xs = np.linspace(x0, x1, 120)
    c = VMobject(color=color, stroke_width=op_stroke)
    c.set_points_smoothly([np.array([x, base + height * np.exp(-0.5 * ((x - center) / sigma) ** 2), 0]) for x in xs])
    return c


# B02: Ride the resonance  (~13.2 s; narration ~44 words ≈ 14.2 s)
# axis y -1.2, x -5..4.2 | band center 0, sigma 1.0, top 1.0 | laser line y -1.2..1.5
# laser label y 1.85 | resonance label (2.6, 1.0) | meter x 5.2, base -1.2, max top 1.2, label (5.2, 1.6)
# axis label (0, -1.6) | tag (4.2, -1.6)

class B02_RideResonance(Scene):
    def construct(self):
        title, footer = opening(self, "Ride the Resonance")
        BASE = -1.2

        axis = Line([-5, BASE, 0], [4.2, BASE, 0], color=SOFT, stroke_width=3)
        grow_from_left(self, axis, run_time=0.6)
        self.play(FadeIn(label_at("wavelength →", 0, -1.6, color=SOFT, size=22)),
                  FadeIn(label_at("schematic", 4.2, -1.6, color=SOFT, size=20, slant="ITALIC")), run_time=0.4)

        res = band(0, 2.2, 1.0, BASE, SOFT, -4.5, 4.0)
        grow_from_left(self, res, run_time=1.0)
        self.play(FadeIn(label_at("plasmon resonance", 2.6, 1.0, size=24, maxw=2.8)), run_time=0.4)

        laser = Line([-4, BASE, 0], [-4, 1.5, 0], color=SPARK, stroke_width=6)
        grow_from_point(self, laser, run_time=0.5)
        lab = label_at("laser", -4, 1.85, color=SPARK, size=24)
        self.play(FadeIn(lab), run_time=0.4)

        def meter(f):
            h = max(2.4 * f, 0.04)
            return Rectangle(width=0.6, height=h, stroke_width=0, fill_color=SPARK, fill_opacity=0.9).move_to([5.2, BASE + h / 2, 0])

        m = meter(np.exp(-0.5 * 16))
        self.play(FadeIn(m), FadeIn(label_at("enhancement", 5.2, 1.6, size=22, maxw=2.0)), run_time=0.4)
        self.wait(1.0)

        for x in (-2.0, 0.0):
            self.play(laser.animate.move_to([x, (BASE + 1.5) / 2, 0]),
                      Transform(m, meter(np.exp(-0.5 * x * x))),
                      Transform(lab, label_at("laser", x, 1.85, color=SPARK, size=24)),
                      run_time=1.2)
            self.wait(1.0 if x < 0 else 2.0)

        kicker = make_kicker("Strongest enhancement where laser meets resonance")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.5)


# B03: The common pairing  (~12.2 s; narration ~41 words ≈ 13.2 s)
# cards x -5.2..-0.8 / 0.8..5.2, y -0.3..1.3 | caption y -1.3

class B03_CommonPairing(Scene):
    def construct(self):
        title, footer = opening(self, "The Common Pairing")

        ag = make_card(4.4, 1.6, [-3.0, 0.5, 0], stroke=SOFT)
        grow_from_left(self, ag)
        self.play(FadeIn(label_in(ag, "Silver\n+ 532 nm laser (green)")), run_time=0.5)
        self.wait(1.5)

        au = make_card(4.4, 1.6, [3.0, 0.5, 0], stroke=SPARK)
        grow_from_left(self, au)
        self.play(FadeIn(label_in(au, "Gold\n+ 785 nm laser (near-infrared)")), run_time=0.5)
        self.wait(1.5)

        cap = label_at("Glyphosate study (Mikac et al., 2022): best results with these two pairings", 0, -1.3,
                       size=24, maxw=10.8)
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(2.5)
        self.play(ag.animate.set_stroke(width=4), au.animate.set_stroke(width=4), run_time=0.5)

        kicker = make_kicker("Good defaults, not laws")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.4)


# B04: Clusters shift the peak  (~15.8 s; narration ~52 words ≈ 16.8 s)
# particles x ~-5.2..-4.0 (labels y 1.55 / -1.55) | axis y -1.3, x -1.5..5.5
# curve A center 0.8 sigma .7 top 0.7 | curve B center 3.0 sigma 1.0 top 0.5
# arrow y 1.3, x 0.8..3.0 | arrow label (1.9, 1.85) | tag (5.6, 1.85) | legend (2.0, -1.75)

class B04_ClusterShift(Scene):
    def construct(self):
        title, footer = opening(self, "Clusters Shift the Peak")
        BASE = -1.3

        axis = Line([-1.5, BASE, 0], [5.5, BASE, 0], color=SOFT, stroke_width=3)
        grow_from_left(self, axis, run_time=0.6)

        single = Circle(radius=0.45, stroke_width=0, fill_color=SOFT, fill_opacity=0.85).move_to([-4.6, 0.8, 0])
        grow_from_point(self, single, run_time=0.5)
        self.play(FadeIn(label_at("isolated", -4.6, 1.55, size=22)), run_time=0.3)
        a = band(0.8, 2.0, 0.7, BASE, SOFT, -1.4, 3.8)
        grow_from_left(self, a, run_time=0.9)
        self.wait(1.2)

        cluster = VGroup(*[Circle(radius=0.38, stroke_width=0, fill_color=SPARK, fill_opacity=0.85).move_to(p)
                           for p in ([-5.0, -0.75, 0], [-4.24, -0.75, 0], [-4.62, -0.1, 0])])
        grow_from_point(self, cluster, run_time=0.6)
        self.play(FadeIn(label_at("clustered", -4.6, -1.55, size=22, color=SPARK)), run_time=0.3)
        b = band(3.0, 1.8, 1.0, BASE, SPARK, -0.4, 5.4)
        grow_from_left(self, b, run_time=1.0)
        self.wait(1.0)

        arrow = Arrow([0.8, 1.3, 0], [3.0, 1.3, 0], buff=0, color=INK, stroke_width=4)
        self.play(GrowArrow(arrow), FadeIn(label_at("red-shift as particles cluster", 1.9, 1.85, size=22, maxw=4.2)),
                  FadeIn(label_at("schematic", 5.6, 1.85, color=SOFT, size=20, slant="ITALIC")), run_time=1.0)
        self.play(FadeIn(label_at("grey: suspension absorbance · orange: where hot spots resonate", 2.0, -1.75,
                                  color=SOFT, size=20, maxw=6.6)), run_time=0.4)
        self.wait(2.0)

        laser = Line([0.8, BASE, 0], [0.8, 1.0, 0], color=INK, stroke_width=5)
        grow_from_point(self, laser, run_time=0.5)
        self.play(laser.animate.move_to([3.0, (BASE + 1.0) / 2, 0]), run_time=1.0)
        self.wait(2.0)

        kicker = make_kicker("Test your actual substrate at your actual wavelength")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.9)


# B05: Brightness vs shelf life  (~11.6 s; narration ~39 words ≈ 12.6 s)
# top caption y 1.75 | bars from x -2.5: silver 7.5 -> 3.0, gold 6.0 -> 5.6 | rows y 0.6 / -0.6
# labels right-aligned at x -2.7 | bottom caption y -1.75 | tag (5.4, -1.75)

class B05_ShelfLife(Scene):
    def construct(self):
        title, footer = opening(self, "Brightness vs Shelf Life")
        X0 = -2.5

        def hb(length, y, color):
            return Rectangle(width=length, height=0.5, stroke_width=0, fill_color=color, fill_opacity=0.9).move_to([X0 + length / 2, y, 0])

        self.play(FadeIn(label_at("Signal from a stored substrate, over time", 0, 1.75, color=SOFT, size=26)),
                  FadeIn(label_at("schematic", 5.4, -1.75, color=SOFT, size=20, slant="ITALIC")), run_time=0.4)
        ag = hb(7.5, 0.6, SOFT)
        au = hb(6.0, -0.6, SPARK)
        grow_from_left(self, ag)
        grow_from_left(self, au)
        self.play(FadeIn(Text("Silver", font_size=26, color=INK).move_to([0, 0.6, 0]).align_to([-2.7, 0, 0], RIGHT)),
                  FadeIn(Text("Gold", font_size=26, color=INK).move_to([0, -0.6, 0]).align_to([-2.7, 0, 0], RIGHT)),
                  run_time=0.4)
        self.wait(1.5)

        for s_len, g_len in ((5.0, 5.85), (3.0, 5.6)):
            self.play(Transform(ag, hb(s_len, 0.6, SOFT)), Transform(au, hb(g_len, -0.6, SPARK)), run_time=1.2)
            self.wait(0.8)

        self.play(FadeIn(label_at("Silver: often brighter, but it oxidizes · Gold: more stable", 0, -1.75, size=24)),
                  run_time=0.5)
        self.wait(1.2)

        kicker = make_kicker("Weigh brightness against how long it lasts")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(0.4)
