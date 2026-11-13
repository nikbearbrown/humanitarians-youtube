"""Manim beats for the reel `energy-recycling-photonics`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: what "energy-recycling photonic hardware" actually names.

Primary source for every figure on screen: Dean, Park, Stokowski, Qi, Robison,
Hwang, Herrmann, Fejer and Safavi-Naeini, "Low-power integrated optical
parametric amplification via second-harmonic resonance", arXiv 2509.26425;
published as Nature 649, 1159-1164 (28 January 2026). Figures were read from the
paper's own abstract, not from press coverage or aggregator pages.

B07 names two further research directions and deliberately carries NO figures
for either -- see FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over twelve previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * a connector between two top-aligned columns must be centred SEPARATELY
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Arrow, Create, FadeIn, Line, RoundedRectangle, Scene,
    Text, VGroup,
)

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR",
    "D:/Projects/brutalist.art/.claude/worktrees/video-creation-setup-4c85fe/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"
TERRA = "#D97757"

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM
SRC_BOTTOM = -1.95


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=37, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=16, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def _fit(group, w, h, centre_y, grow=1.9):
    if group.width <= 0 or group.height <= 0:
        return group
    k = min(w / group.width, h / group.height)
    k = min(k, grow) if k > 1 else k
    group.scale(k)
    group.move_to([0, centre_y, 0])
    return group


def fit(group, w=BODY_W, h=BODY_H):
    return _fit(group, w, h, (BODY_TOP + BODY_BOTTOM) / 2)


def fit_src(group, w=BODY_W):
    return _fit(group, w, BODY_TOP - SRC_BOTTOM, (BODY_TOP + SRC_BOTTOM) / 2)


def cross(color=TERRA):
    return VGroup(
        Line([-0.09, 0.09, 0], [0.09, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.09, -0.09, 0], [0.09, 0.09, 0], stroke_width=3.2, color=color),
    )


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=20, title_fs=24):
    lines = [l for l in lines if l.strip()]
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


def stat(figure, caption_lines, accent=INK, fig_fs=48, cap_fs=18, min_w=4.0):
    f = Text(figure, font=SERIF, font_size=fig_fs, color=accent)
    caps = VGroup(*[Text(c, font=MONO, font_size=cap_fs, color=INK_SOFT)
                    for c in caption_lines])
    caps.arrange(DOWN, buff=0.14)
    inner = VGroup(f, caps).arrange(DOWN, buff=0.22)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.6),
                           height=inner.height + 0.56, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


def band(label, sub, accent=INK_SOFT, w=7.0):
    """A horizontal layer band. The three things the phrase conflates."""
    t = Text(label, font=SANS, font_size=23, color=accent)
    s = Text(sub, font=MONO, font_size=18, color=INK_SOFT)
    inner = VGroup(t, s).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(w, inner.width + 0.8), height=inner.height + 0.52,
                           corner_radius=0.10, stroke_width=1.8, stroke_color=accent,
                           fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_ThreeLayers(Scene):
    """BLUF: the phrase names three different things. 29s-ish."""

    def construct(self):
        page(self)
        head = kicker("ONE PHRASE, THREE DIFFERENT CLAIMS",
                      "\u201cenergy-recycling photonic hardware\u201d")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        bands = VGroup(
            band("reuse the PUMP LIGHT", "the light that drives the device", TERRA),
            band("reuse the PHOTONS", "before anything measures them", INK),
            band("recover WASTE HEAT", "downstream \u2014 not optical at all", INK_SOFT),
        ).arrange(DOWN, buff=0.30)

        brace = Line(UP * 1.5, DOWN * 1.5, stroke_width=2.0, color=INK_SOFT)
        blabel = Text("all three get called\n\u201crecycling\u201d",
                      font=MONO, font_size=19, color=INK_SOFT)
        right = VGroup(brace, blabel).arrange(RIGHT, buff=0.26)
        body = fit(VGroup(bands, right).arrange(RIGHT, buff=0.50))

        for b in bands:
            self.play(Create(b[0]), FadeIn(b[1]), run_time=1.6)
            self.wait(0.9)
        self.play(Create(brace), FadeIn(blabel), run_time=1.5)
        self.wait(2.6)

        point = spark("Different layers. Different baselines.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.8)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY RECYCLING CLAIM",
                      "ask these before you believe a saving")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT IS\n   REUSED?", ["pump power,", "photons, or heat"], accent=INK_SOFT),
            panel("2  BEFORE OR AFTER\n   DETECTION?", ["detection destroys", "the photon \u2014 that is",
                                                        "physics, not design"], accent=TERRA),
            panel("3  COMPARED\n   AGAINST WHAT?", ["the laser alone,", "or the whole system"],
                  accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(1.2)
        self.wait(3.0)

        point = spark("Question two is a wall, not a gap")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.9)


class B03_RoundAgain(Scene):
    """EVIDENCE: single pass versus resonant recirculation."""

    def construct(self):
        page(self)
        head = kicker("THE CLEAREST REAL DEVICE",
                      "an optical amplifier on thin-film lithium niobate")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        guide = RoundedRectangle(width=3.4, height=0.70, corner_radius=0.35,
                                 stroke_width=2.0, stroke_color=INK_SOFT, fill_opacity=0)
        a_in = Arrow(LEFT * 0.9, LEFT * 0.12, buff=0, stroke_width=3.0,
                     max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
        a_out = Arrow(RIGHT * 0.12, RIGHT * 0.9, buff=0, stroke_width=3.0,
                      max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
        single = VGroup(a_in, guide, a_out).arrange(RIGHT, buff=0.14)
        s_cap = Text("single pass \u2014 what is left leaves",
                     font=MONO, font_size=19, color=INK_SOFT)
        s_fate = chip("leftover pump → lost", INK_SOFT, font_size=17, height=0.40)
        left = VGroup(single, s_cap, s_fate).arrange(DOWN, buff=0.26)

        track = RoundedRectangle(width=3.3, height=1.75, corner_radius=0.86,
                                 stroke_width=2.4, stroke_color=TERRA, fill_opacity=0)
        r_in = Arrow(LEFT * 0.85, LEFT * 0.08, buff=0, stroke_width=3.0,
                     max_tip_length_to_length_ratio=0.35, color=TERRA)
        ring = VGroup(r_in, track).arrange(RIGHT, buff=0.14)
        r_cap = Text("resonant \u2014 the pump goes round again",
                     font=MONO, font_size=19, color=TERRA)
        r_fate = chip("leftover pump → next pass", TERRA, font_size=17, height=0.40)
        right = VGroup(ring, r_cap, r_fate).arrange(DOWN, buff=0.26)

        # The two columns have very different heights (a flat waveguide against a
        # tall racetrack). Top-aligning them leaves the diagrams at different
        # heights with the connector floating between nothing -- measured 53%
        # fill. Centre-aligning, with the link inside the same arrange, puts the
        # two diagrams level and the connector between them.
        link = Line(LEFT * 0.38, RIGHT * 0.38, stroke_width=1.8, color=INK_SOFT)
        pair = VGroup(left, link, right).arrange(RIGHT, buff=0.70)
        note = Text("nothing is reclaimed from waste \u2014 the same light is put back to work",
                    font=MONO, font_size=18, color=INK)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.44))
        src = source_line("Dean et al. \u00b7 Nature 649, 1159\u20131164 (28 Jan 2026) \u00b7 arXiv 2509.26425")

        self.play(Create(guide), run_time=1.0)
        self.play(Create(a_in), Create(a_out), run_time=0.9)
        self.play(FadeIn(s_cap), run_time=1.0)
        self.play(Create(s_fate[0]), FadeIn(s_fate[1]), run_time=1.0)
        self.wait(1.2)
        self.play(Create(link), run_time=0.6)
        self.play(Create(track), run_time=1.6)
        self.play(Create(r_in), FadeIn(r_cap), run_time=1.4)
        self.play(Create(r_fate[0]), FadeIn(r_fate[1]), run_time=1.1)
        self.wait(1.4)
        self.play(FadeIn(note), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Round again, before it can escape")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.5)


class B04_TheNumbers(Scene):
    """EVIDENCE: the four headline figures, from the abstract."""

    def construct(self):
        page(self)
        head = kicker("THE NUMBERS", "from the paper's own abstract")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            stat("> 17 dB", ["gain"], accent=INK),
            stat("< 200 mW", ["input power"], accent=INK),
            stat("95%", ["of the input becomes", "the pump that works"], accent=TERRA),
            stat("110 nm", ["of flat, near-quantum-", "limited noise"], accent=INK),
        ]
        top = VGroup(cards[0], cards[1]).arrange(RIGHT, buff=0.46, aligned_edge=DOWN)
        bot = VGroup(cards[2], cards[3]).arrange(RIGHT, buff=0.46, aligned_edge=UP)
        grid = fit_src(VGroup(top, bot).arrange(DOWN, buff=0.40))
        src = source_line("arXiv 2509.26425 abstract \u00b7 thin-film lithium niobate")

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("Gain without buying it in noise")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.4)


class B05_WhatItBought(Scene):
    """EVIDENCE: the two order-of-magnitude comparisons, each with its baseline."""

    def construct(self):
        page(self)
        head = kicker("WHAT GOING ROUND AGAIN BOUGHT",
                      "two comparisons, each against a named baseline")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for base, result in [
            ("vs conventional single-pass", "effective pump power  \u2191 ~10x"),
            ("vs previous demonstrations", "power needed for this gain  \u2193 ~10x"),
        ]:
            b = chip(base, INK_SOFT, font_size=18, height=0.44)
            a = Arrow(LEFT * 0.34, RIGHT * 0.34, buff=0, stroke_width=3.0,
                      max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
            r = chip(result, TERRA, font_size=19, height=0.48)
            rows.append(VGroup(b, a, r).arrange(RIGHT, buff=0.30))
        stack = VGroup(*rows).arrange(DOWN, buff=0.40, aligned_edge=LEFT)
        note = Text("both comparisons are about PUMP LIGHT \u2014 neither is about a computation",
                    font=MONO, font_size=19, color=INK)
        body = fit_src(VGroup(stack, note).arrange(DOWN, buff=0.52))
        src = source_line("arXiv 2509.26425 abstract \u00b7 same laser, used roughly ten times as well")

        for r in rows:
            self.play(Create(r[0][0]), FadeIn(r[0][1]), run_time=1.1)
            self.play(Create(r[1]), run_time=0.6)
            self.play(Create(r[2][0]), FadeIn(r[2][1]), run_time=1.3)
            self.wait(1.5)
        self.play(FadeIn(note), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("A claim about pump light")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.7)


class B06_TheBoundary(Scene):
    """FALSIFIABILITY: three boundaries the phrase crosses."""

    def construct(self):
        page(self)
        head = kicker("WHAT THIS RESULT IS NOT",
                      "three places the phrase outruns the evidence")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # a photon arriving at a detector, with NO onward path drawn
        wg = Line(LEFT * 1.0, RIGHT * 0.0, stroke_width=3.0, color=INK_SOFT)
        det = RoundedRectangle(width=0.52, height=0.62, corner_radius=0.08,
                               stroke_width=2.2, stroke_color=TERRA, fill_opacity=0)
        diagram = VGroup(wg, det).arrange(RIGHT, buff=0.06)
        dlabel = Text("detector \u2014 nothing continues past it",
                      font=MONO, font_size=17, color=TERRA)
        dgrp = VGroup(diagram, dlabel).arrange(RIGHT, buff=0.34)

        items = [
            ("it is an AMPLIFIER, not a processor", "it makes a signal bigger; it computes nothing"),
            ("detection destroys the photon", None),
            ("most \u201cefficient photonics\u201d is tuning power", "less power to tune and move data \u2014 a different claim"),
        ]
        rows = []
        for i, (headline, sub) in enumerate(items):
            x = cross(TERRA)
            h = Text(headline, font=SANS, font_size=22, color=INK)
            if sub:
                s = Text(sub, font=MONO, font_size=18, color=INK_SOFT)
                stack = VGroup(h, s).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            else:
                stack = VGroup(h, dgrp).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            rows.append(VGroup(x, stack).arrange(RIGHT, buff=0.32))
        body = fit_src(VGroup(*rows).arrange(DOWN, buff=0.34, aligned_edge=LEFT))
        src = source_line("the first search for the phrase returned mostly phase-shifter power results")

        self.play(Create(rows[0][0]), FadeIn(rows[0][1]), run_time=2.2)
        self.wait(3.0)
        self.play(Create(rows[1][0]), FadeIn(rows[1][1][0]), run_time=1.6)
        self.play(Create(wg), Create(det), run_time=1.2)
        self.play(FadeIn(dlabel), run_time=1.2)
        self.wait(3.4)
        self.play(Create(rows[2][0]), FadeIn(rows[2][1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(4.2)

        point = spark("You cannot recycle what you have measured")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(8.3)


class B07_OtherLayers(Scene):
    """EVIDENCE: two further layers, named, with no figures claimed."""

    def construct(self):
        page(self)
        head = kicker("THE OTHER TWO LAYERS",
                      "they exist \u2014 and they carry no numbers here")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = panel("photon-recycling accelerator",
                  ["light left over after it has",
                   "pushed an electron is looped",
                   "back for the next cycle",
                   "",
                   "a proposal, not a device"], accent=INK_SOFT, min_w=5.8, fs=18, title_fs=21)
        b = panel("recirculating mesh",
                  ["photonic neural networks that",
                   "reuse the optical path",
                   "before anything is detected",
                   "",
                   "architecture work, early"], accent=INK_SOFT, min_w=5.8, fs=18, title_fs=21)
        pair = VGroup(a, b).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        note = Text("no figures are claimed for either \u2014 I could not verify any from a primary source",
                    font=MONO, font_size=18, color=TERRA)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.44))
        src = source_line("named so the category is complete, not to support the verdict")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=2.2)
        self.wait(1.8)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=2.2)
        self.wait(1.8)
        self.play(FadeIn(note), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Same word, different layer")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.8)


class B08_Verdict(Scene):
    """VERDICT: rubric scored, then both sides."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, answered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("WHAT IS REUSED", "pump light", INK),
              ("BEFORE OR AFTER DETECTION", "before \u2014 after is physics", TERRA),
              ("COMPARED AGAINST WHAT", "single-pass, and prior amplifiers", INK)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=18)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.32))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  a ~10x power saving, in a real device",
                 font=SANS, font_size=22, color=INK),
            Text("BE SCEPTICAL OF:  the phrase \u2014 it will be reused for tuning power and heat",
                 font=SANS, font_size=22, color=TERRA),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        body = fit_src(VGroup(scored, verdict).arrange(DOWN, buff=0.50, aligned_edge=LEFT))
        src = source_line("Dean et al., Nature 649 (2026) \u00b7 arXiv 2509.26425")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.4)
            self.wait(1.4)
        self.wait(2.2)
        self.play(FadeIn(src), run_time=1.1)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=2.0)
            self.wait(1.6)

        point = spark("Ask which layer, every time")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(8.5)
