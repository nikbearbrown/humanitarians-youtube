"""
scenes.py: sers-quantitative (landscape 16:9)

  B02_SurfaceFills     Langmuir-type calibration curve + surface sites filling (ILLUSTRATIVE)
  B03_HotSpotLottery   same sample, three spots, three intensities (ILLUSTRATIVE)
  B04_InternalStandard analyte + standard bars per spot; ratio steadier (IDEALIZED)

Lessons baked in: string weights, footer->kicker from t=0, helper-built captions,
fills >= 0.4 opacity, wide content from early frames, scene ~1 s under audio.
Safe area x +/-6.3, y +/-3.4. No text sits on a Line/Arrow/curve.
"""

from manim import *
import numpy as np

PAGE = "#FAF9F5"
INK = "#3D3929"
SOFT = "#7A766A"
SPARK = "#D97757"
FOOTER = "SERS · Why quantitation is hard"

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


def label_at(s, x, y, color=INK, size=26, maxw=8.8):
    c = Text(s, font_size=size, color=color)
    fit(c, maxw)
    return c.move_to([x, y, 0])


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


def vbar(x, base, h, color, w=0.6, op=0.9):
    h = max(h, 0.03)
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color, fill_opacity=op).move_to([x, base + h / 2, 0])


def grow_up(scene, b, base, run_time=0.5):
    seed = Rectangle(width=b.width, height=0.02, stroke_width=0, fill_color=b.get_fill_color(),
                     fill_opacity=0.9).move_to([b.get_center()[0], base, 0])
    scene.add(seed)
    scene.play(ReplacementTransform(seed, b), run_time=run_time)


# B02: The surface fills up  (~17.7 s; narration ~58 words ≈ 18.7 s)
# axes: origin (-5,-1.3), x to 1.0, y to 1.6 | curve y = -1.3 + 2.7*Kx/(1+Kx), K 0.9, x 0..6
# axis labels: "signal" (-5.6,1.6), "concentration →" (-2.0,-1.65) | plateau label (-1.0,1.6)
# right panel: caption (3.7,0.9), sites y -0.55, strip y -0.9 (x 1.9..5.5) | tag (5.4,-1.85)

def _lang(u):
    return -1.3 + 2.7 * (0.9 * u) / (1 + 0.9 * u)


def _seg(u0, u1):
    c = VMobject(color=SPARK, stroke_width=5)
    c.set_points_smoothly([np.array([-5 + u, _lang(u), 0]) for u in np.linspace(u0, u1, 40)])
    return c


class B02_SurfaceFills(Scene):
    def construct(self):
        title, footer = opening(self, "The Surface Fills Up")

        axes = VGroup(Line([-5, -1.3, 0], [1.0, -1.3, 0], color=SOFT, stroke_width=3),
                      Line([-5, -1.3, 0], [-5, 1.6, 0], color=SOFT, stroke_width=3))
        grow_from_left(self, axes)
        tag = Text("illustrative", font_size=20, color=SOFT, slant="ITALIC").move_to([5.4, -1.85, 0])
        self.play(FadeIn(Text("signal", font_size=22, color=SOFT).move_to([-5.6, 1.6, 0])),
                  FadeIn(Text("concentration →", font_size=22, color=SOFT).move_to([-2.0, -1.65, 0])),
                  FadeIn(tag), run_time=0.4)

        strip = Rectangle(width=3.6, height=0.3, stroke_width=0, fill_color=SOFT, fill_opacity=0.6).move_to([3.7, -0.9, 0])
        sites = VGroup(*[Circle(radius=0.16, stroke_color=INK, stroke_width=2.5, fill_opacity=0)
                         .move_to([2.15 + 0.443 * i, -0.55, 0]) for i in range(8)])
        grow_from_left(self, VGroup(strip, sites))
        cap = label_at("Low concentration: free sites", 3.7, 0.9, size=24, maxw=3.8)
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.0)

        steps = [((0.0, 1.5), range(0, 2), "Sites filling: signal climbs"),
                 ((1.5, 3.5), range(2, 5), "Fewer free sites: slowing"),
                 ((3.5, 6.0), range(5, 8), "Surface full: plateau")]
        for i, ((u0, u1), idx, text) in enumerate(steps):
            seg = _seg(u0, u1)
            s = seg.copy().stretch_to_fit_width(0.04).move_to(seg.get_left() + RIGHT * 0.02)
            self.add(s)
            self.play(ReplacementTransform(s, seg),
                      *[sites[j].animate.set_fill(color=SPARK, opacity=0.9) for j in idx],
                      Transform(cap, label_at(text, 3.7, 0.9, size=24, maxw=3.8)),
                      run_time=1.5)
            if i < 2:
                self.wait(1.5)

        self.play(FadeIn(Text("Langmuir-type plateau", font_size=22, color=INK).move_to([-1.0, 1.6, 0])), run_time=0.4)
        self.wait(2.0)
        kicker = make_kicker("More analyte, barely more signal, once the surface is full")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(2.8)


# B03: The hot-spot lottery  (~12.0 s; narration ~40 words ≈ 13 s)
# sub y 2.0 | bars x -2.0 / 0 / 2.0, base -1.0, tops <= 1.4 | spot labels y -1.35
# caption y -2.0 | tag (5.4, -2.0)

class B03_HotSpotLottery(Scene):
    def construct(self):
        title, footer = opening(self, "The Hot-Spot Lottery")

        sub = Text("Same sample · same concentration · three spots", font_size=28, color=SOFT).move_to([0, 2.0, 0])
        fit(sub, 10.5)
        tag = Text("illustrative", font_size=20, color=SOFT, slant="ITALIC").move_to([5.4, -2.0, 0])
        self.play(FadeIn(sub), FadeIn(tag), run_time=0.5)

        BASE = -1.0
        xs, hs = (-2.0, 0.0, 2.0), (1.0, 2.4, 1.6)
        bars = []
        for x, h in zip(xs, hs):
            b = vbar(x, BASE, h, SPARK, w=1.0)
            grow_up(self, b, BASE, run_time=0.6)
            bars.append(b)
        self.play(*[FadeIn(Text(f"spot {i + 1}", font_size=24, color=INK).move_to([x, -1.35, 0]))
                    for i, x in enumerate(xs)], run_time=0.4)
        self.wait(1.5)

        cap = label_at("Raw intensity alone is a noisy ruler", 0, -2.0)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2.0)

        self.play(*[Transform(b, vbar(x, BASE, h, SPARK, w=1.0)) for b, x, h in zip(bars, xs, (2.0, 0.9, 1.7))],
                  run_time=1.0)
        self.wait(1.5)

        kicker = make_kicker("Each spot samples different hot spots")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.2)


# B04: The internal standard  (~17.4 s; narration ~57 words ≈ 18.4 s)
# sub y 1.85 | pairs at x -4.0 / -2.4 / -0.8 (analyte -0.3, standard +0.3), base -1.0, tops <= 0.98
# ratio bars x 2.8 / 3.8 / 4.8, height 1.2 | labels y -1.35 | caption y -2.0 | tag (5.6, 1.85)

class B04_InternalStandard(Scene):
    def construct(self):
        title, footer = opening(self, "The Internal Standard")

        sub = Text("Same spots, now with a reference molecule", font_size=28, color=SOFT).move_to([-0.6, 1.85, 0])
        fit(sub, 9.5)
        tag = Text("idealized", font_size=20, color=SOFT, slant="ITALIC").move_to([5.6, 1.85, 0])
        self.play(FadeIn(sub), FadeIn(tag), run_time=0.5)

        BASE = -1.0
        centers, hot = (-4.0, -2.4, -0.8), (1.0, 2.2, 1.5)
        for c, k in zip(centers, hot):
            grow_up(self, vbar(c - 0.3, BASE, 0.9 * k, SPARK, w=0.5), BASE)
        for c, k in zip(centers, hot):
            grow_up(self, vbar(c + 0.3, BASE, 0.75 * k, SOFT, w=0.5), BASE)
        self.play(*[FadeIn(Text(f"spot {i + 1}", font_size=22, color=INK).move_to([c, -1.35, 0]))
                    for i, c in enumerate(centers)],
                  FadeIn(Text("analyte", font_size=20, color=SPARK).move_to([-2.4, 1.3, 0])),
                  FadeIn(Text("standard", font_size=20, color=SOFT).move_to([-1.0, 1.3, 0])),
                  run_time=0.4)
        self.wait(2.0)

        ratios = VGroup(*[vbar(x, BASE, 1.2, INK, w=0.6) for x in (2.8, 3.8, 4.8)])
        seed = ratios.copy().stretch(0.02, 1).move_to([3.8, BASE, 0])
        self.add(seed)
        self.play(ReplacementTransform(seed, ratios), run_time=1.0)
        self.play(FadeIn(Text("analyte ÷ standard", font_size=22, color=INK).move_to([3.8, -1.35, 0])), run_time=0.4)
        self.wait(2.5)

        cap = label_at("Caveats: competes for sites · can overlap peaks · can photodegrade", 0, -2.0,
                       color=SPARK, size=24, maxw=11.0)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.0)
        self.play(ratios.animate.set_fill(color=SPARK, opacity=0.8), run_time=0.6)

        kicker = make_kicker("Ratio to a reference: steadier than raw intensity, not free")
        self.play(Transform(footer, kicker), run_time=0.8)
        self.wait(1.9)
