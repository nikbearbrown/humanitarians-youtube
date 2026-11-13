"""Manim beats for the reel `likely-false-likely-true`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: whether a published return predictor should be believed.

SCOPE: a research-methodology explainer. NOT investment advice. No tradable
instrument is named, no strategy is described or recommended, and nothing here
is personalized financial advice.

Primary sources. Factor counts and growth rates: Harvey, Liu, Zhu, "...and the
Cross-Section of Expected Returns", Review of Financial Studies 29(1), 5-68
(2016) -- read out of the author-hosted PDF with pdftotext. The t > 3.0 hurdle
and the "likely false" wording: the NBER WP 20592 abstract, verbatim. The
rebuttal: Andrew Y. Chen (Federal Reserve Board), "Most claimed statistical
findings in cross-sectional return predictability are likely true", arXiv
2206.15365 v10.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over fifteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * a cross sits BESIDE or BETWEEN the things it negates, never through text
  * compose every label INTO the fitted group before fitting
  * columns of unequal height are CENTRE-aligned, connector in the same arrange
  * a WIDE and SHORT group is width-limited: fit() cannot scale it up and the
    frame underfills. Prefer compositions taller than they are wide.
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
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


def crossmark(color=TERRA):
    """Sits BETWEEN the two things it separates. Never drawn through text."""
    return VGroup(
        Line([-0.10, 0.10, 0], [0.10, -0.10, 0], stroke_width=3.2, color=color),
        Line([-0.10, -0.10, 0], [0.10, 0.10, 0], stroke_width=3.2, color=color),
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


def stat(figure, caption_lines, accent=INK, fig_fs=50, cap_fs=18, min_w=3.8):
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


def hbar(length, label, figure, color, height=0.50, fig_fs=26):
    l = Text(label, font=MONO, font_size=19, color=INK_SOFT)
    box = RoundedRectangle(width=max(length, 0.14), height=height, corner_radius=0.07,
                           stroke_width=2.2, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    return VGroup(l, box, f).arrange(RIGHT, buff=0.26)


def vbar(height, label, figure, color, width=1.15, fig_fs=25):
    b = RoundedRectangle(width=width, height=max(height, 0.12), corner_radius=0.07,
                         stroke_width=2.2, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    l = Text(label, font=MONO, font_size=17, color=INK_SOFT)
    return VGroup(f, b, l).arrange(DOWN, buff=0.16)


class B01_TwoTitles(Scene):
    """BLUF: the two published titles, set against each other."""

    def construct(self):
        page(self)
        head = kicker("TWO PAPERS, ONE LITERATURE",
                      "their titles contradict each other almost word for word")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = panel("Review of Financial Studies, 2016",
                  ["\u201cmost claimed research findings",
                   "in financial economics are",
                   "likely FALSE\u201d"], accent=INK_SOFT, min_w=7.2, fs=20, title_fs=21)
        b = panel("Federal Reserve Board, arXiv 2206.15365",
                  ["\u201cmost claimed statistical findings",
                   "in cross-sectional return",
                   "predictability are likely TRUE\u201d"], accent=TERRA, min_w=7.2, fs=20, title_fs=21)
        link = Text("same literature", font=MONO, font_size=19, color=INK_SOFT)
        body = fit_src(VGroup(a, link, b).arrange(DOWN, buff=0.30))
        src = source_line("Harvey, Liu, Zhu (2016) \u00b7 and Chen, Federal Reserve Board")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=2.2)
        self.wait(2.0)
        self.play(FadeIn(link), run_time=0.9)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Both serious. Both peer-reviewed.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.2)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CLAIMED EDGE",
                      "ask these before you believe a backtest, or a paper")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  HOW MANY THINGS\n   WERE TRIED?", ["the more candidates,", "the higher the best",
                                                         "scores by luck alone"], accent=INK_SOFT),
            panel("2  WHAT DOES\n   \u2018FALSE\u2019 MEAN?", ["failing a significance", "test is not the same",
                                                        "as being untrue"], accent=TERRA),
            panel("3  WHOSE BAR,\n   AND WHY THAT ONE?", ["the threshold is a", "choice, and moving it",
                                                          "moves the headline"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.8)
            self.wait(1.6)
        self.wait(3.2)

        point = spark("Question two is where they part company")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.5)


class B03_TheFactorZoo(Scene):
    """EVIDENCE: the catalogue and its growth rate, from the paper's text."""

    def construct(self):
        page(self)
        head = kicker("THE SCALE OF IT",
                      "what the 2016 paper catalogued")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        counts = VGroup(
            stat("316", ["different factors"], accent=TERRA, min_w=4.2),
            stat("313", ["articles,", "250 of them published"], accent=INK, min_w=4.6),
        ).arrange(DOWN, buff=0.28)

        bars = VGroup(
            vbar(0.40, "1980\u201391", "~1/yr", INK_SOFT),
            vbar(1.05, "1991\u20132003", "~5/yr", INK),
            vbar(2.30, "last 9 yrs", "~18/yr", TERRA),
        ).arrange(RIGHT, buff=0.34, aligned_edge=DOWN)
        blab = Text("the discovery rate", font=MONO, font_size=18, color=INK_SOFT)
        right = VGroup(bars, blab).arrange(DOWN, buff=0.24)

        pair = VGroup(counts, right).arrange(RIGHT, buff=0.70)
        note = Text("164 factors in those nine years \u2014 roughly double the 84 from all prior years",
                    font=MONO, font_size=19, color=INK)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.40))
        src = source_line("Harvey, Liu, Zhu \u00b7 Review of Financial Studies 29(1), 5\u201368 \u00b7 read from the PDF")

        for c in counts:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.8)
        for b in bars:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=1.2)
        self.play(FadeIn(blab), run_time=0.9)
        self.wait(1.8)
        self.play(FadeIn(note), run_time=2.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Eighteen a year, and accelerating")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(8.5)


class B04_RaiseTheBar(Scene):
    """EVIDENCE: the proposed threshold, and the filter observation."""

    def construct(self):
        page(self)
        head = kicker("THE MULTIPLE-TESTING ARGUMENT",
                      "a bar built for one test, used for hundreds")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        old = chip("the customary bar:  t > 2.0", INK_SOFT, font_size=21, height=0.52)
        gap = Line(LEFT * 0.0, RIGHT * 0.0, stroke_width=0.0, color=CREAM)
        new = chip("what they propose:  t > 3.0", TERRA, font_size=21, height=0.52)
        bars = VGroup(old, new).arrange(DOWN, buff=0.34)

        obs = panel("and the observation that gives it force",
                    ["in their sample, the overwhelming",
                     "majority of published t-statistics",
                     "exceed the 1.96 benchmark.",
                     "",
                     "nearly everything published passes \u2014",
                     "which describes the filter, not the world"],
                    accent=INK, min_w=6.8, fs=19, title_fs=21)
        body = fit_src(VGroup(bars, obs).arrange(DOWN, buff=0.42))
        src = source_line("NBER WP 20592 abstract, verbatim \u00b7 and the paper's own section 5")

        self.play(Create(old[0]), FadeIn(old[1]), run_time=2.0)
        self.wait(2.4)
        self.play(Create(new[0]), FadeIn(new[1]), run_time=2.0)
        self.wait(3.4)
        self.play(Create(obs[0]), FadeIn(obs[1]), run_time=3.6)
        self.play(FadeIn(src), run_time=1.1)
        self.wait(6.0)

        point = spark("Everything published clears the bar")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.6)
        self.wait(6.0)


class B05_TheRebuttal(Scene):
    """FALSIFIABILITY: the Fed paper's bounds."""

    def construct(self):
        page(self)
        head = kicker("AND THE DIRECT REBUTTAL",
                      "a Federal Reserve Board economist, with bounds")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = [
            hbar(2.50, "across 8 of 9 prior studies", "\u2264 25%", INK_SOFT),
            hbar(0.90, "a more refined bound", "\u2264 9%", INK),
            hbar(0.85, "the main specification", "\u2264 8.5%", TERRA),
        ]
        stack = VGroup(*rows).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        cap = Text("bounds on the FALSE DISCOVERY RATE \u2014 lower means more of them are real",
                   font=MONO, font_size=19, color=INK_SOFT)
        punch = Text("at least 91.5% of those published findings are true",
                     font=SANS, font_size=24, color=TERRA)
        body = fit_src(VGroup(stack, cap, punch).arrange(DOWN, buff=0.32))
        src = source_line("Andrew Y. Chen, Federal Reserve Board \u00b7 arXiv 2206.15365 v10")

        for r in rows:
            self.play(Create(r[1]), FadeIn(r[0]), FadeIn(r[2]), run_time=1.5)
            self.wait(1.1)
        self.play(FadeIn(cap), run_time=1.6)
        self.wait(1.6)
        self.play(FadeIn(punch), run_time=1.9)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("Not a blog post. A bound.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.4)


class B06_TheDefinition(Scene):
    """EVIDENCE: why they disagree -- and it is not the arithmetic."""

    def construct(self):
        page(self)
        head = kicker("SO WHICH IS RIGHT?",
                      "the rebuttal does not dispute the arithmetic")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = panel("failed a significance test", ["insignificant"],
                  accent=INK_SOFT, min_w=5.4, fs=21, title_fs=22)
        x = crossmark(TERRA)
        eq = Text("=", font=SERIF, font_size=46, color=TERRA)
        sep = VGroup(eq, x).arrange(DOWN, buff=0.02)
        b = panel("is not true", ["a false discovery"],
                  accent=TERRA, min_w=5.4, fs=21, title_fs=22)
        pair = VGroup(a, sep, b).arrange(RIGHT, buff=0.42)

        note = panel("what the rebuttal says",
                     ["the 2016 paper's own methods",
                      "imply a false rate of about 9%.",
                      "the gap came from counting every",
                      "insignificant factor as a false one."],
                     accent=INK, min_w=7.0, fs=19, title_fs=21)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.42))
        src = source_line("arXiv 2206.15365 \u00b7 a disagreement about a definition, read for a decade as one about facts")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=2.2)
        self.play(FadeIn(eq), run_time=1.1)
        self.play(Create(x), run_time=1.2)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=2.2)
        self.wait(4.0)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=3.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(5.4)

        point = spark("A definition, not a fact")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B07_WhatSurvives(Scene):
    """EVIDENCE: the premise neither side contests."""

    def construct(self):
        page(self)
        head = kicker("WHAT SURVIVES THE DISAGREEMENT",
                      "the part neither side contests")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        tops = VGroup(*[RoundedRectangle(width=0.22, height=0.22, corner_radius=0.04,
                                         stroke_width=1.6, stroke_color=INK_SOFT,
                                         fill_opacity=0) for _ in range(11)])
        tops.arrange(RIGHT, buff=0.12)
        funnel = Polygon([-1.70, 0.0, 0], [1.70, 0.0, 0], [0.30, -1.05, 0], [-0.30, -1.05, 0],
                         stroke_width=1.8, stroke_color=INK_SOFT, fill_opacity=0)
        flab = Text("only the winners are written up", font=MONO, font_size=17, color=INK_SOFT)
        outs = VGroup(*[RoundedRectangle(width=0.22, height=0.22, corner_radius=0.04,
                                         stroke_width=1.8, stroke_color=INK,
                                         fill_opacity=0) for _ in range(3)])
        outs.arrange(RIGHT, buff=0.14)
        diagram = VGroup(tops, funnel, flab, outs).arrange(DOWN, buff=0.16)

        miss = panel("the number that would settle it",
                     ["how many specifications were",
                      "tried and discarded \u2014 the one",
                      "number no paper reports.",
                      "",
                      "which is why the 2016 authors",
                      "had to estimate it from the",
                      "size of the literature"],
                     accent=TERRA, min_w=6.2, fs=18, title_fs=21)

        body = fit_src(VGroup(diagram, miss).arrange(RIGHT, buff=0.70))
        src = source_line("the published record is a filtered sample \u2014 both papers agree on this")

        self.play(*[Create(t) for t in tops], run_time=1.4)
        self.play(Create(funnel), run_time=1.3)
        self.play(FadeIn(flab), run_time=1.0)
        self.play(*[Create(o) for o in outs], run_time=1.0)
        self.wait(2.0)
        self.play(Create(miss[0]), FadeIn(miss[1]), run_time=3.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("Nobody publishes the trials they ran")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.0)


class B08_Verdict(Scene):
    """VERDICT: rubric scored, then both sides."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, answered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("HOW MANY WERE TRIED", "316 published, an unknown multiple discarded", INK),
              ("WHAT DOES FALSE MEAN", "two definitions \u2014 most of the gap", TERRA),
              ("WHOSE BAR", "3.0 proposed, 2.0 habitual, 2.0 used deliberately", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=17)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.32))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  the argument is being had with arithmetic",
                 font=SANS, font_size=21, color=INK),
            Text("BE SCEPTICAL OF:  either headline quoted without its definition",
                 font=SANS, font_size=21, color=TERRA),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        body = fit_src(VGroup(scored, verdict).arrange(DOWN, buff=0.50, aligned_edge=LEFT))
        src = source_line("RFS 29(1), 5\u201368 \u00b7 arXiv 2206.15365 \u00b7 not investment advice")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.6)
            self.wait(1.4)
        self.wait(1.8)
        self.play(FadeIn(src), run_time=1.0)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=2.0)
            self.wait(1.6)

        point = spark("Ask how many they ran")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(8.4)
