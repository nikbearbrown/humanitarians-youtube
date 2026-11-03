"""Manim beats for the reel `refusal-is-one-direction`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: what the technique commonly called "abliteration" actually removes.

SCOPE: deliberately non-operational. This file draws a published finding and its
safety implications. There is no code, no layer index, no hyperparameter, no
model or repository to clone, and no procedure anywhere in it. The conceptual
result is in a NeurIPS paper; the recipe for applying it is withheld. The
practical guidance in B07 is defensive.

Primary source: Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda,
"Refusal in Language Models Is Mediated by a Single Direction", arXiv 2406.11717,
NeurIPS 2024. Follow-up: Joad, Hawasly, Boughorbel, Durrani, Sencar, "There Is
More to Refusal in Large Language Models than a Single Direction", arXiv
2602.02132, EMNLP 2026. Supply-chain figures: Cloud Security Alliance research
note, 2026-10-21, scoped on screen to what it actually demonstrated.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over thirteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text -- a cross sits BESIDE the phrase it negates
  * compose every label INTO the fitted group before fitting
  * columns of unequal height are CENTRE-aligned, connector in the same arrange
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, Line, Polygon, RoundedRectangle,
    Scene, Text, VGroup,
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
    """Sits BESIDE the phrase it negates. Never drawn across text."""
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


class B01_TwoCorrections(Scene):
    """BLUF: it is not a neuron, and it does not uncensor. 30s-ish."""

    def construct(self):
        page(self)
        head = kicker("TWO CORRECTIONS, BEFORE ANYTHING ELSE",
                      "the usual description gets both halves wrong")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for wrong, right in [
            ("\u201ca neuron\u201d", "a DIRECTION in activation space"),
            ("\u201cunlocks hidden knowledge\u201d", "removes a BEHAVIOUR"),
        ]:
            x = cross(TERRA)
            w = Text(wrong, font=MONO, font_size=22, color=INK_SOFT)
            arrow = Line(LEFT * 0.26, RIGHT * 0.26, stroke_width=1.8, color=INK_SOFT)
            r = Text(right, font=SANS, font_size=23, color=TERRA)
            rows.append(VGroup(x, w, arrow, r).arrange(RIGHT, buff=0.30))
        stack = VGroup(*rows).arrange(DOWN, buff=0.44, aligned_edge=LEFT)

        note = panel("so",
                     ["one axis, spread across many",
                      "neurons and many layers \u2014",
                      "no single unit owns it.",
                      "what it knew, it still knows."],
                     accent=INK_SOFT, min_w=6.0, fs=19, title_fs=21)
        body = fit_src(VGroup(stack, note).arrange(DOWN, buff=0.44))
        src = source_line("the common phrasing \u00b7 corrected against the source paper")

        for r in rows:
            self.play(FadeIn(r[1]), run_time=1.0)
            self.play(Create(r[0]), Create(r[2]), run_time=0.8)
            self.play(FadeIn(r[3]), run_time=1.3)
            self.wait(2.2)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=2.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(4.5)

        point = spark("A behaviour, not a vault")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.5)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY \u201cSAFETY REMOVED\u201d CLAIM",
                      "ask these before you believe one, or run one")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT WAS\n   ACTUALLY CHANGED?", ["weights, activations,", "or just the prompt"],
                  accent=INK_SOFT),
            panel("2  WHAT DID\n   IT COST?", ["removing a behaviour", "can take structure",
                                               "with it \u2014 measure it"], accent=INK_SOFT),
            panel("3  WHO ELSE TOUCHED\n   THE WEIGHTS?", ["a downloaded edit is",
                                                           "someone else's edit"], accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(1.3)
        self.wait(2.8)

        point = spark("You cannot inspect it by using it")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.8)


class B03_TheFinding(Scene):
    """EVIDENCE: the published result, and the symmetry that proves it is a control."""

    def construct(self):
        page(self)
        head = kicker("THE PUBLISHED FINDING",
                      "NeurIPS 2024 \u00b7 Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        tops = VGroup(
            stat("13", ["open chat models"], accent=INK),
            stat("up to 72B", ["parameters"], accent=INK),
            stat("1", ["dimensional subspace", "\u2014 one direction each"], accent=TERRA),
        ).arrange(RIGHT, buff=0.44, aligned_edge=UP)

        sym = []
        for label, result, colour in [
            ("erase it", "the model stops refusing harmful instructions", INK),
            ("add it", "the model starts refusing harmless ones", TERRA),
        ]:
            c = chip(label, colour, font_size=19, height=0.44)
            a = Line(LEFT * 0.26, RIGHT * 0.26, stroke_width=1.8, color=INK_SOFT)
            t = Text(result, font=MONO, font_size=19, color=INK)
            sym.append(VGroup(c, a, t).arrange(RIGHT, buff=0.28))
        srows = VGroup(*sym).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        body = fit_src(VGroup(tops, srows).arrange(DOWN, buff=0.46))
        src = source_line("arXiv 2406.11717 \u00b7 \u201cRefusal in Language Models Is Mediated by a Single Direction\u201d")

        for c in tops:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.4)
            self.wait(0.4)
        self.wait(1.0)
        for r in sym:
            self.play(Create(r[0][0]), FadeIn(r[0][1]), Create(r[1]), run_time=0.9)
            self.play(FadeIn(r[2]), run_time=1.2)
            self.wait(1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(3.4)

        point = spark("The second half is what makes it a control")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B04_Brittleness(Scene):
    """EVIDENCE: the authors' own conclusion."""

    def construct(self):
        page(self)
        head = kicker("WHY THIS IS A SAFETY RESULT",
                      "the sentence the authors ended on")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        quote = Text("\u201c\u2026 underscore the brittleness of current\nsafety fine-tuning methods\u201d",
                     font=SERIF, font_size=34, color=INK, line_spacing=0.9)
        qbox = RoundedRectangle(width=quote.width + 1.0, height=quote.height + 0.86,
                                corner_radius=0.14, stroke_width=1.8,
                                stroke_color=INK_SOFT, fill_opacity=0)
        qbox.move_to(quote.get_center())
        attrib = Text("\u2014 Arditi et al., NeurIPS 2024", font=MONO, font_size=18, color=INK_SOFT)
        qpack = VGroup(VGroup(qbox, quote), attrib).arrange(DOWN, buff=0.26)

        wide = RoundedRectangle(width=2.9, height=0.80, corner_radius=0.10,
                                stroke_width=2.0, stroke_color=INK_SOFT, fill_opacity=0)
        wlab = Text("safety fine-tuning", font=MONO, font_size=17, color=INK_SOFT)
        funnel = Polygon([-1.45, 0.0, 0], [1.45, 0.0, 0], [0.10, -0.95, 0], [-0.10, -0.95, 0],
                         stroke_width=1.6, stroke_color=INK_SOFT, fill_opacity=0)
        thin = RoundedRectangle(width=0.22, height=0.46, corner_radius=0.06,
                                stroke_width=2.6, stroke_color=TERRA, fill_opacity=0)
        tlab = Text("one direction", font=MONO, font_size=17, color=TERRA)
        diagram = VGroup(VGroup(wide, wlab).arrange(DOWN, buff=0.14),
                         funnel,
                         VGroup(thin, tlab).arrange(DOWN, buff=0.14)).arrange(DOWN, buff=0.10)

        body = fit_src(VGroup(qpack, diagram).arrange(RIGHT, buff=0.80))
        src = source_line("arXiv 2406.11717 \u00b7 the paper's own conclusion, not a commentator's")

        self.play(Create(qbox), run_time=1.2)
        self.play(FadeIn(quote), run_time=3.0)
        self.play(FadeIn(attrib), run_time=0.9)
        self.wait(3.6)
        self.play(Create(wide), FadeIn(wlab), run_time=1.8)
        self.play(Create(funnel), run_time=1.7)
        self.play(Create(thin), FadeIn(tlab), run_time=1.8)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(5.0)

        point = spark("An expensive behaviour on a single axis")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B05_MoreThanOne(Scene):
    """FALSIFIABILITY: the EMNLP 2026 follow-up, stated precisely."""

    def construct(self):
        page(self)
        head = kicker("AND THE SINGLE-DIRECTION ACCOUNT IS INCOMPLETE",
                      "EMNLP 2026 \u00b7 Joad, Hawasly, Boughorbel, Durrani, Sencar")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        claims = [
            ("different refusal categories map to", "geometrically distinct directions", INK),
            ("but steering along any of them gives", "nearly identical trade-offs", INK),
            ("so they affect", "not WHETHER it refuses, but HOW", TERRA),
        ]
        rows = []
        for lead, result, colour in claims:
            a = Text(lead, font=MONO, font_size=19, color=INK_SOFT)
            b = Text(result, font=SANS, font_size=22, color=colour)
            inner = VGroup(a, b).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.70, height=inner.height + 0.52,
                                   corner_radius=0.10, stroke_width=1.8,
                                   stroke_color=colour, fill_opacity=0)
            box.move_to(inner.get_center())
            rows.append(VGroup(box, inner))
        stack = VGroup(*rows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        note = Text("a linear intervention collapses that structure into uniform control",
                    font=MONO, font_size=19, color=TERRA)
        body = fit_src(VGroup(stack, note).arrange(DOWN, buff=0.40))
        src = source_line("arXiv 2602.02132 \u00b7 the knob really is shared; what sits behind it is not")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=2.1)
            self.wait(2.6)
        self.play(FadeIn(note), run_time=2.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(5.0)

        point = spark("Right about the knob. Wrong about the mechanism.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B06_WhatItDoesNotDo(Scene):
    """EVIDENCE: the three non-effects, and the unquantified claim."""

    def construct(self):
        page(self)
        head = kicker("WHAT IT DOES NOT DO", "and the one claim with no number behind it")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        nots = []
        for t in ["it adds no capability",
                  "it reveals no hidden training data",
                  "it is the same model, minus one behaviour"]:
            x = cross(TERRA)
            a = Text(t, font=SANS, font_size=23, color=INK)
            nots.append(VGroup(x, a).arrange(RIGHT, buff=0.30))
        nstack = VGroup(*nots).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        claim = panel("the paper says",
                      ["\u201cminimal effect on",
                       "other capabilities\u201d"], accent=TERRA, min_w=5.2, fs=21, title_fs=21)
        flag = chip("no benchmark figure in the abstract", TERRA, font_size=18, height=0.44)
        cpack = VGroup(claim, flag).arrange(DOWN, buff=0.26)

        # Side by side these two are wide and short, so fit() is width-limited
        # and cannot scale up -- measured 50% fill with a dead lower half.
        # Stacked, the group is taller than it is wide and fills the band.
        body = fit_src(VGroup(nstack, cpack).arrange(DOWN, buff=0.46))
        src = source_line("arXiv 2406.11717 abstract \u00b7 \u201cminimal\u201d is a word, not a measurement")

        for n in nots:
            self.play(Create(n[0]), FadeIn(n[1]), run_time=1.5)
            self.wait(1.9)
        self.wait(1.8)
        self.play(Create(claim[0]), FadeIn(claim[1]), run_time=2.0)
        self.wait(2.8)
        self.play(Create(flag[0]), FadeIn(flag[1]), run_time=1.5)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.0)

        point = spark("Ask for that number first")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.0)


class B07_TheWeightsAreSomeoneElses(Scene):
    """QUESTION 3: the supply-chain finding, scoped exactly."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 WHO ELSE TOUCHED THE WEIGHTS?",
                      "a security note published this month")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        scope = panel("what they actually did",
                      ["a controlled experiment",
                       "NOT a survey of model hubs",
                       "NOT an abliterated model \u2014 they",
                       "poisoned a 7B model by fine-tuning,",
                       "as a stand-in for a weight edit"],
                      accent=INK_SOFT, min_w=6.2, fs=18, title_fs=21)

        cards = VGroup(
            stat("up to 100%", ["fires on its", "trigger phrase"], accent=TERRA, min_w=4.2),
            stat("99\u2013100%", ["accuracy on", "ordinary tasks"], accent=INK, min_w=4.2),
        ).arrange(RIGHT, buff=0.46)
        punch = Text("it passes your benchmarks \u2014 that is the point",
                     font=SANS, font_size=22, color=TERRA)
        right = VGroup(cards, punch).arrange(DOWN, buff=0.34)

        body = fit_src(VGroup(scope, right).arrange(RIGHT, buff=0.66))
        src = source_line("Cloud Security Alliance research note, 2026-10-21 \u00b7 small test sets, single vendor")

        self.play(Create(scope[0]), FadeIn(scope[1]), run_time=3.2)
        self.wait(4.4)
        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.9)
            self.wait(1.4)
        self.play(FadeIn(punch), run_time=2.4)
        self.play(FadeIn(src), run_time=1.2)
        self.wait(6.0)

        point = spark("Clean benchmarks cannot rule out a trigger")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B08_Verdict(Scene):
    """VERDICT: rubric scored, then both sides."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, answered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("WHAT CHANGED", "a direction, by editing weights", INK),
              ("WHAT IT COST", "structure \u2014 and a claim with no number", TERRA),
              ("WHO ELSE TOUCHED IT", "whoever published it", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=18)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.32))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  interpretability locating a trained behaviour this precisely",
                 font=SANS, font_size=21, color=INK),
            Text("BE SCEPTICAL OF:  any \u201cuncensored\u201d model you can download",
                 font=SANS, font_size=21, color=TERRA),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        body = fit_src(VGroup(scored, verdict).arrange(DOWN, buff=0.50, aligned_edge=LEFT))
        src = source_line("arXiv 2406.11717 \u00b7 arXiv 2602.02132 \u00b7 CSA research note 2026-10-21")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.5)
            self.wait(1.8)
        self.wait(2.6)
        self.play(FadeIn(src), run_time=1.2)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=2.4)
            self.wait(2.3)

        point = spark("It is an unverifiable edit from a stranger")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)
