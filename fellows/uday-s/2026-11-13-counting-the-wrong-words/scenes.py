"""Manim beats for the reel `counting-the-wrong-words`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: market sentiment analysis -- the measurement decision upstream of the
model.

SCOPE: NOT investment advice. No tradable instrument is named, no strategy is
described, no return or performance figure appears, and no claim is made that
sentiment predicts prices.

Primary source: Loughran & McDonald, "When Is a Liability Not a Liability?
Textual Analysis, Dictionaries, and 10-Ks", The Journal of Finance LXVI(1),
February 2011 -- every figure read out of the PDF with pdftotext. A search
summary had attributed 73.8% to distinct WORDS; the paper says word COUNTS, and
B03 carries that distinction on screen.

B08 quotes the mycroft repository's own market-sentiment attestation, verified
present at commit b425b19.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over sixteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * a cross sits BESIDE or BETWEEN what it negates, never through text
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
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, Line, RoundedRectangle, Scene, Text,
    VGroup,
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
    """Sits BESIDE what it negates. Never drawn through text."""
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


class B01_TheFourSteps(Scene):
    """BLUF: three steps are engineering; one is a measurement decision."""

    def construct(self):
        page(self)
        head = kicker("WHAT THE JOB ACTUALLY IS",
                      "four steps, and only one of them is a judgement")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        steps = [("1  get the text", False), ("2  count what counts as negative", True),
                 ("3  turn that into a score", False), ("4  act on it", False)]
        rows, links = [], []
        for label, key in steps:
            colour = TERRA if key else INK_SOFT
            t = Text(label, font=MONO, font_size=21 if key else 19, color=colour)
            box = RoundedRectangle(width=t.width + (1.0 if key else 0.6), height=0.56,
                                   corner_radius=0.09, stroke_width=2.2 if key else 1.6,
                                   stroke_color=colour, fill_opacity=0)
            box.move_to(t.get_center())
            rows.append(VGroup(box, t))
        cells = []
        for i, r in enumerate(rows):
            cells.append(r)
            if i < 3:
                l = Line(UP * 0.11, DOWN * 0.11, stroke_width=1.6, color=INK_SOFT)
                links.append(l)
                cells.append(l)
        chain = VGroup(*cells).arrange(DOWN, buff=0.12)

        tag = chip("a measurement decision \u2014 made once, usually inherited",
                   TERRA, font_size=19, height=0.46)
        body = fit_src(VGroup(chain, tag).arrange(DOWN, buff=0.36))
        src = source_line("if the list is wrong, a better model makes the wrong number more precisely")

        for i, r in enumerate(rows):
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.0)
            if i < 3:
                self.play(Create(links[i]), run_time=0.35)
        self.wait(2.2)
        self.play(Create(tag[0]), FadeIn(tag[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Three are engineering. One is a judgement.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.9)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS BEFORE YOU TRUST A SENTIMENT NUMBER",
                      "ask these of your own pipeline, or anyone else's")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT COUNTS AS\n   NEGATIVE?", ["and who decided \u2014", "name the list"],
                  accent=TERRA),
            panel("2  HOW MUCH IS A FEW\n   COMMON WORDS?", ["a handful of frequent", "terms can carry",
                                                             "most of the score"], accent=INK_SOFT),
            panel("3  HAS ANYONE CHECKED\n   IT PREDICTS?", ["separate from whether", "it measures tone \u2014",
                                                             "and usually unanswered"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.8)
            self.wait(1.5)
        self.wait(3.0)

        point = spark("Name the list, before anything else")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.8)


class B03_SeventyThreeEight(Scene):
    """EVIDENCE: the headline, with what the percentage is OF."""

    def construct(self):
        page(self)
        head = kicker("THE MEASUREMENT",
                      "Journal of Finance, 2011 \u00b7 Loughran & McDonald")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        big = stat("73.8%", ["of the negative", "word COUNTS"], accent=TERRA, min_w=5.0)
        side = VGroup(
            stat("121,217", ["annual filings"], accent=INK_SOFT, min_w=4.2),
            stat("1994\u20132008", ["the sample period"], accent=INK_SOFT, min_w=4.2),
        ).arrange(DOWN, buff=0.26)
        pair = VGroup(big, side).arrange(RIGHT, buff=0.56)

        note = panel("note what that is a percentage OF",
                     ["not 73.8% of the word list.",
                      "73.8% of the score itself \u2014 words",
                      "that are not typically negative",
                      "in a financial context."], accent=INK, min_w=6.8, fs=19, title_fs=21)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.40))
        src = source_line("The Journal of Finance LXVI(1), Feb 2011 \u00b7 read from the PDF, not a summary")

        self.play(Create(big[0]), FadeIn(big[1]), run_time=1.8)
        self.wait(1.4)
        for c in side:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.2)
        self.wait(1.6)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=2.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("Of the score, not of the list")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.1)


class B04_SevenWords(Scene):
    """EVIDENCE: the seven words that carry a quarter of it."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 HOW MUCH IS A FEW COMMON WORDS?",
                      "the seven most frequent, from the same table")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        words = ["tax", "costs", "loss", "capital", "cost", "expense", "expenses"]
        chips = [chip(w, TERRA, font_size=24, height=0.56, pad=0.52) for w in words]
        r1 = VGroup(*chips[:4]).arrange(RIGHT, buff=0.26)
        r2 = VGroup(*chips[4:]).arrange(RIGHT, buff=0.26)
        grid = VGroup(r1, r2).arrange(DOWN, buff=0.26)

        share = panel("together",
                      ["more than ONE QUARTER of the",
                       "total count of \u201cnegative\u201d words"], accent=INK, min_w=6.6, fs=20, title_fs=22)
        alone = chip("costs, on its own \u2014 4.61% of the total", INK_SOFT,
                     font_size=19, height=0.46)
        body = fit_src(VGroup(grid, share, alone).arrange(DOWN, buff=0.32))
        src = source_line("a company describing its tax position is doing accounting, not complaining")

        for c in chips:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=0.55)
        self.wait(1.8)
        self.play(Create(share[0]), FadeIn(share[1]), run_time=2.2)
        self.wait(1.6)
        self.play(Create(alone[0]), FadeIn(alone[1]), run_time=1.5)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("A balance sheet, read as a complaint")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.6)


class B05_IndustryNotMood(Scene):
    """EVIDENCE: the words that identify an industry."""

    def construct(self):
        page(self)
        head = kicker("AND A SECOND FAILURE, WHICH IS WORSE",
                      "words that identify an industry, not an event")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        pairs = [("foreign", "international operations"),
                 ("vice", "vice-presidents")]
        rows = []
        for w, means in pairs:
            c = chip(w, INK_SOFT, font_size=22, height=0.50, pad=0.46)
            a = Line(LEFT * 0.22, RIGHT * 0.22, stroke_width=1.6, color=INK_SOFT)
            t = Text(means, font=MONO, font_size=20, color=INK)
            rows.append(VGroup(c, a, t).arrange(RIGHT, buff=0.26))
        top = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        ind = VGroup(*[chip(w, TERRA, font_size=22, height=0.50, pad=0.46)
                       for w in ["mine", "crude", "tire", "cancer"]]).arrange(RIGHT, buff=0.26)
        ilab = Text("these identify an INDUSTRY, not a negative event",
                    font=MONO, font_size=19, color=TERRA)
        bottom = VGroup(ind, ilab).arrange(DOWN, buff=0.22)

        warn = Text("so a mining company scores gloomy by construction, every quarter",
                    font=SANS, font_size=22, color=INK)
        body = fit_src(VGroup(top, bottom, warn).arrange(DOWN, buff=0.36))
        src = source_line("a bias that lines up with what you are measuring does not average out")

        for r in rows:
            self.play(Create(r[0][0]), FadeIn(r[0][1]), Create(r[1]), FadeIn(r[2]), run_time=1.4)
            self.wait(1.4)
        self.wait(1.0)
        for c in ind:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=0.6)
        self.play(FadeIn(ilab), run_time=1.4)
        self.wait(2.5)
        self.play(FadeIn(warn), run_time=2.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(4.0)

        point = spark("Not noise. Bias.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B06_SmallerNotBigger(Scene):
    """EVIDENCE: the replacement list, and that it is smaller."""

    def construct(self):
        page(self)
        head = kicker("THE FIX, AND WHY IT IS INTERESTING",
                      "a replacement list built for the domain")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        h_bar = RoundedRectangle(width=6.4, height=0.74, corner_radius=0.10,
                                 stroke_width=2.0, stroke_color=INK_SOFT, fill_opacity=0)
        h_lab = Text("the borrowed general-purpose list", font=MONO, font_size=19, color=INK_SOFT)
        top = VGroup(h_bar, h_lab).arrange(DOWN, buff=0.16)

        f_bar = RoundedRectangle(width=3.2, height=0.74, corner_radius=0.10,
                                 stroke_width=2.4, stroke_color=TERRA, fill_opacity=0)
        f_fig = Text("2,337 words", font=SERIF, font_size=28, color=TERRA)
        f_fig.move_to(f_bar.get_center())
        f_lab = Text("the finance list \u2014 about half the size", font=MONO, font_size=19, color=TERRA)
        bottom = VGroup(VGroup(f_bar, f_fig), f_lab).arrange(DOWN, buff=0.16)

        note = Text("not a bigger vocabulary, and not a bigger model \u2014 someone deciding, word by word",
                    font=SANS, font_size=21, color=INK)
        body = fit_src(VGroup(top, bottom, note).arrange(DOWN, buff=0.40))
        src = source_line("Fin-Neg, 2,337 words including inflections \u00b7 same paper")

        self.play(Create(h_bar), FadeIn(h_lab), run_time=1.6)
        self.wait(1.4)
        self.play(Create(f_bar), FadeIn(f_fig), run_time=1.6)
        self.play(FadeIn(f_lab), run_time=1.2)
        self.wait(1.8)
        self.play(FadeIn(note), run_time=2.2)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("Smaller, and built by hand")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.6)


class B07_TheLimits(Scene):
    """FALSIFIABILITY: measurement is not prediction, and this is about filings."""

    def construct(self):
        page(self)
        head = kicker("THE LIMITS",
                      "where the original question gets its honest answer")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        items = [("this result is about ANNUAL FILINGS",
                  "headlines, posts and earnings calls have other vocabularies"),
                 ("a better lexicon measures TONE better",
                  "it does not establish that tone predicts prices")]
        rows = []
        for headline, sub in items:
            x = crossmark(TERRA)
            h = Text(headline, font=SANS, font_size=23, color=INK)
            s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
            stack = VGroup(h, s).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            rows.append(VGroup(x, stack).arrange(RIGHT, buff=0.30))
        stack = VGroup(*rows).arrange(DOWN, buff=0.40, aligned_edge=LEFT)

        close = Text("measuring well is a precondition for predicting \u2014 not a substitute for testing it",
                     font=SANS, font_size=22, color=INK)
        body = fit_src(VGroup(stack, close).arrange(DOWN, buff=0.44))
        src = source_line("two different claims \u00b7 only the first one is settled here")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=2.0)
            self.wait(3.2)
        self.play(FadeIn(close), run_time=3.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(4.3)

        point = spark("Measured well is not predicted")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B08_LiveExample(Scene):
    """VERDICT: question 3 against a real pipeline, then both sides."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 HAS ANYONE CHECKED?",
                      "a live pipeline, and what its own record says")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        quote = panel("from the repository's own attestation",
                      ["\u201cNothing here asserts the number",
                       "means anything. The weights,",
                       "thresholds and keyword lists are",
                       "inherited from the source workflow",
                       "with no derivation, backtest,",
                       "or author.\u201d"], accent=TERRA, min_w=7.0, fs=19, title_fs=21)
        attrib = Text("\u2014 recorded by the person who built it",
                      font=MONO, font_size=18, color=INK_SOFT)
        left = VGroup(quote, attrib).arrange(DOWN, buff=0.20)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  the fix costs domain attention, not compute",
                 font=SANS, font_size=21, color=INK),
            Text("BE SCEPTICAL OF:  any sentiment number whose word list nobody can name",
                 font=SANS, font_size=21, color=TERRA),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        body = fit_src(VGroup(left, verdict).arrange(DOWN, buff=0.44))
        src = source_line("mycroft @ b425b19 \u00b7 Loughran & McDonald 2011 \u00b7 not investment advice")

        self.play(Create(quote[0]), run_time=1.4)
        self.play(FadeIn(quote[1]), run_time=3.8)
        self.play(FadeIn(attrib), run_time=1.5)
        self.wait(5.0)
        self.play(FadeIn(src), run_time=1.6)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=2.6)
            self.wait(2.6)

        point = spark("This exact failure, live, written down")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)
