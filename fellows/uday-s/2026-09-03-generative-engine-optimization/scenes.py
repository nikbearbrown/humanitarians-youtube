"""Manim beats for the reel `generative-engine-optimization`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

EVERY number here is recomputed from the shipped results/ files of the GEO
project, not from the paper abstract (whose figures are not reproducible from
that data -- see FACTCHECK.md). Provenance:
  Condition A  no RAG            results/report_20260415_133752.json
  Condition C  RAG + neutral     results/report_20260415_133654.json  (rag_version=baseline)
  Condition B  RAG + optimized   results/report_20260415_133611.json  (rag_version=optimized)
  pseudo-brand                   results/pseudo_brand_2026041 5_{095028,103941,131814}.json

No author names appear anywhere: this is a topic explainer.

Layout lessons already paid for, kept here:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * beats carrying a citation use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line,
    RoundedRectangle, Scene, Text, VGroup, Write,
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
FULL = 5.4          # bar length for 100%


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
    return Text(text, font=SERIF, font_size=36, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=16, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def _fit(group, w, h, centre_y, grow=2.2):
    """Scale a body group to FILL its band — up as well as down.

    FILL-THE-CANVAS LAW: a graphic that leaves the safe area half empty is a
    defect, not a neutral choice. Scaling only downward (the obvious
    implementation) silently produces exactly that on any sparse beat, so this
    scales toward the band in both directions, capped by `grow` so a two-element
    beat does not balloon into a poster.
    """
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


def bar_row(label, pct, color=INK, h=0.34, fs=22):
    """label | proportional bar | value. The value sits OUTSIDE the bar."""
    lab = Text(label, font=MONO, font_size=fs, color=INK)
    bar = RoundedRectangle(width=max(0.12, FULL * pct / 100.0), height=h,
                           corner_radius=0.06, stroke_width=1.8,
                           stroke_color=color, fill_opacity=0)
    val = Text(f"{pct:g}%", font=MONO, font_size=fs, color=color)
    return VGroup(lab, bar, val)


def align_rows(rows, gap=0.45):
    """Put every bar on one baseline column, value hung off each bar's end."""
    lw = max(r[0].width for r in rows)
    for r in rows:
        r[1].next_to(r[0], RIGHT, buff=gap + (lw - r[0].width))
        r[2].next_to(r[1], RIGHT, buff=0.28)
    return rows


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=21):
    t = Text(title, font=SANS, font_size=24, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_VisibilityGap(Scene):
    """BLUF: the gap, in one picture. 14.06s."""

    def construct(self):
        page(self)
        head = kicker("SAME QUESTION, SAME MODELS", "how often each brand is named")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = align_rows(VGroup(bar_row("brand A", 95, INK, h=0.52, fs=26),
                                 bar_row("brand B", 15, TERRA, h=0.52, fs=26)))
        rows.arrange(DOWN, buff=1.25, aligned_edge=LEFT)
        fit(rows)

        for r in rows:
            self.play(FadeIn(r[0], shift=RIGHT * 0.2), Create(r[1]), FadeIn(r[2]),
                      run_time=1.5)
        self.wait(1.6)

        point = spark("The ranking is not fixed")
        self.play(Write(point), run_time=1.8)
        self.wait(4.86)


class B02_ThreeLevers(Scene):
    """FRAMEWORK: the three levers, before any result. 18.41s."""

    LEVERS = [
        ("1", "PARAMETRIC", "what training left behind\n— you cannot edit it"),
        ("2", "PRESENCE", "is your content in the\ncontext window at all?"),
        ("3", "QUALITY", "what that content says\nonce it is there"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE LEVERS", "everything that follows is one of these moving")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.LEVERS:
            n = Text(num, font=SERIF, font_size=34, color=TERRA)
            t = Text(title, font=SANS, font_size=28, color=INK)
            b = Text(body, font=MONO, font_size=20, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.30)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.85, height=inner.height + 0.85,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.45))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.1)
            self.wait(1.5)

        point = spark("They do not move by the same amount")
        self.play(Write(point), run_time=1.8)
        self.wait(5.51)


class B03_BaselineSpread(Scene):
    """EVIDENCE: lever 1 — the parametric starting line. 19.75s."""

    BRANDS = [("HubSpot", 95), ("ClickUp", 85), ("Asana", 82.5), ("Salesforce", 57.5),
              ("Jira", 42.5), ("Freshsales", 30), ("Less Annoying CRM", 25),
              ("Notion", 20), ("Copper", 15)]

    def construct(self):
        page(self)
        head = kicker("LEVER 1 — PARAMETRIC", "20 prompts · 4 models · no extra context")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = align_rows(VGroup(*[
            bar_row(n, p, TERRA if p <= 30 else INK, h=0.26, fs=19)
            for n, p in self.BRANDS
        ]))
        rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        # the mean label is composed INTO the fitted group — anything positioned
        # relative to a group AFTER fit can land on the citation strip
        mean = Text("mean 50.3%", font=SANS, font_size=24, color=INK_SOFT)
        body = fit_src(VGroup(rows, mean).arrange(DOWN, buff=0.30))
        src = source_line("results/report_20260415_133752.json · condition A")

        self.play(LaggedStart(*[
            LaggedStart(FadeIn(r[0], shift=RIGHT * 0.15), Create(r[1]), FadeIn(r[2]),
                        lag_ratio=0.3)
            for r in rows], lag_ratio=0.45), run_time=7.4)
        self.wait(1.0)

        self.play(FadeIn(mean), FadeIn(src), run_time=1.2)
        self.wait(1.0)

        point = spark("A six-fold gap, before anyone writes a word")
        self.play(Write(point), run_time=2.0)
        self.wait(5.25)


class B04_PresenceLever(Scene):
    """EVIDENCE: lever 2 — presence alone. 16.23s."""

    def construct(self):
        page(self)
        head = kicker("LEVER 2 — PRESENCE", "plain factual descriptions, retrieved into the prompt")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        base = bar_row("no context", 50.3, INK, h=0.5, fs=24)
        with_ctx = bar_row("neutral content", 86.7, TERRA, h=0.5, fs=24)
        rows = align_rows(VGroup(base, with_ctx))
        rows.arrange(DOWN, buff=1.25, aligned_edge=LEFT)

        delta = Text("+36.4 points — for being in the room", font=SANS,
                     font_size=25, color=TERRA)
        body = fit_src(VGroup(rows, delta).arrange(DOWN, buff=0.95))
        src = source_line("results/report_20260415_133654.json · condition C · mean of 9 brands")

        self.play(FadeIn(base[0], shift=RIGHT * 0.2), Create(base[1]), FadeIn(base[2]),
                  run_time=1.5)
        self.wait(0.9)
        self.play(FadeIn(with_ctx[0], shift=RIGHT * 0.2), Create(with_ctx[1]),
                  FadeIn(with_ctx[2]), run_time=1.8)
        self.wait(0.8)
        self.play(FadeIn(delta, shift=UP * 0.2), FadeIn(src), run_time=1.4)
        self.wait(1.0)

        point = spark("Not for being convincing")
        self.play(Write(point), run_time=1.7)
        self.wait(4.23)


class B05_QualityLever(Scene):
    """EVIDENCE: lever 3 — the average hides the distribution. 23.30s."""

    def construct(self):
        page(self)
        head = kicker("LEVER 3 — QUALITY", "statistics · expert quotations · source citations")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("THE MEAN", ["86.7%  →  91.1%", "+4.4 points"], INK_SOFT, min_w=4.6)
        right = panel("THE DISTRIBUTION", [
            "started invisible   +69.4",
            "already dominant    +11.7",
        ], TERRA, min_w=5.4)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        body = fit_src(pair)
        src = source_line("results/report_20260415_133611.json · condition B · GEO strategies: KDD 2024, arXiv:2311.09735")

        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.8)
        self.wait(1.8)
        self.play(Create(right[0]), FadeIn(right[1][0]), run_time=1.5)
        for line in right[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=1.2)
        self.wait(1.2)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.0)

        point = spark("It does not lift everyone. It lifts the bottom.")
        self.play(Write(point), run_time=2.1)
        self.wait(7.68)


class B06_PseudoBrand(Scene):
    """EVIDENCE: the brand that does not exist. 21.08s."""

    def construct(self):
        page(self)
        head = kicker("A BRAND THAT DOES NOT EXIST",
                      "no website · no customers · no training data")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cold = panel("ASKED COLD", ["8.6%", "3 of 35 answers"], INK_SOFT, min_w=4.4)
        warm = panel("WITH RETRIEVED CONTENT", ["90%  and  95%", "across two runs"],
                     TERRA, min_w=5.0)
        pair = VGroup(cold, warm).arrange(RIGHT, buff=0.9, aligned_edge=UP)

        rank = Text("ranked #1 in every case where it appeared", font=SANS,
                    font_size=26, color=TERRA)
        body = fit_src(VGroup(pair, rank).arrange(DOWN, buff=1.05))
        src = source_line("results/pseudo_brand_*.json · three runs")

        self.play(Create(cold[0]), FadeIn(cold[1]), run_time=1.6)
        self.wait(1.4)
        self.play(Create(warm[0]), FadeIn(warm[1]), run_time=1.8)
        self.wait(1.4)
        self.play(Write(rank), run_time=2.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.0)

        point = spark("Zero to the top of the list")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.6)
        self.wait(7.48)


class B07_WhatItMeasures(Scene):
    """FALSIFIABILITY: what the metric does and does not measure. 21.89s."""

    DOES = ["presence in the context", "position in the list",
            "consistency across models"]
    DOES_NOT = ["product quality", "fit for the person asking",
                "whether the brand exists"]

    def construct(self):
        page(self)
        head = kicker("WHAT THE FRAMEWORK PREDICTS",
                      "if presence dominates, anything in the context wins")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("MENTION RATE MEASURES", self.DOES, INK_SOFT, min_w=5.2, fs=22)
        right = panel("IT DOES NOT MEASURE", self.DOES_NOT, TERRA, min_w=5.2, fs=22)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.85, aligned_edge=UP)
        fit(pair)

        self.play(Create(left[0]), FadeIn(left[1][0]), run_time=1.4)
        for line in left[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.85)
        self.wait(1.0)
        self.play(Create(right[0]), FadeIn(right[1][0]), run_time=1.4)
        for line in right[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.85)
        self.wait(1.6)

        point = spark("A brand you could not buy outranked eight real ones")
        self.play(Write(point), run_time=2.3)
        self.wait(5.44)


class B08_Verdict(Scene):
    """VERDICT: the three levers scored, and the boundary. 19.39s."""

    SCORES = [
        ("PARAMETRIC", "fixed and unequal — the starting line", INK),
        ("PRESENCE", "+36.4 points — the biggest lever here", TERRA),
        ("QUALITY", "+4.4 mean, but +69 from invisible", INK),
    ]

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three levers, measured")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for axis, answer, color in self.SCORES:
            a = Text(axis, font=SANS, font_size=25, color=INK_SOFT)
            v = Text(answer, font=MONO, font_size=22, color=color)
            cell = RoundedRectangle(width=v.width + 0.6, height=0.7, corner_radius=0.09,
                                    stroke_width=1.7, stroke_color=color, fill_opacity=0)
            cell.move_to(v.get_center())
            rows.add(VGroup(a, VGroup(cell, v)))
        lw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.6 + (lw - r[0].width))
        rows.arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        use = Text("USE IT FOR:  explaining why a recommendation happened",
                   font=SANS, font_size=22, color=INK)
        not_for = Text("NOT FOR:  deciding whether a product is any good",
                       font=SANS, font_size=22, color=TERRA)
        tail = VGroup(use, not_for).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        fit(VGroup(rows, tail).arrange(DOWN, buff=0.55))

        self.play(LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.18) for r in rows],
                              lag_ratio=0.2), run_time=1.0)
        for r in rows:
            self.play(Create(r[1][0]), FadeIn(r[1][1], shift=RIGHT * 0.18), run_time=1.1)
        self.wait(1.0)
        self.play(FadeIn(use, shift=UP * 0.15), run_time=1.0)
        self.play(FadeIn(not_for, shift=UP * 0.15), run_time=1.0)
        self.wait(1.2)

        point = spark("Different questions. One was measured.")
        self.play(Write(point), run_time=1.9)
        self.wait(4.99)
