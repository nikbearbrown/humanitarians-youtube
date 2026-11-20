"""Manim beats for the reel `twenty-percent-or-five`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Commissioned topic: "AI for learning Music", retitled.

Single primary source: Macnamara, Hambrick & Oswald (2014), "Deliberate Practice
and Performance in Music, Games, Sports, Education, and Professions: A
Meta-Analysis", Psychological Science. Every figure was read out of the paper
itself (local PDF, pdftotext -layout), never out of coverage of it. See
FACTCHECK.md for the figure-by-figure table, including the reading the reel
refuses to make ("21% practice, so 79% talent" -- the paper says UNEXPLAINED).

Bars encode the stated percentages proportionally and nothing else; every bar
carries its own r alongside, so the bar is never the only evidence on screen.

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


def tick(color=INK):
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def crossmark(color=TERRA):
    """Sits BESIDE or BETWEEN. Never drawn through text."""
    return VGroup(
        Line([-0.10, 0.10, 0], [0.10, -0.10, 0], stroke_width=3.2, color=color),
        Line([-0.10, -0.10, 0], [0.10, 0.10, 0], stroke_width=3.2, color=color),
    )


def hollow(size=0.24, color=INK_SOFT, stroke=1.8):
    return RoundedRectangle(width=size, height=size, corner_radius=0.04,
                            stroke_width=stroke, stroke_color=color, fill_opacity=0)


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




def tickrow(text, color=INK, fs=20):
    return VGroup(tick(color), Text(text, font=MONO, font_size=fs, color=INK)).arrange(
        RIGHT, buff=0.26)


def connector(height=0.32):
    return Line([0, 0, 0], [0, -height, 0], stroke_width=1.6, color=INK_SOFT)


def barset(data, maxw=6.4, fs=20, bh=0.46, gap=0.26):
    """data = [(label, fraction_of_longest, value_text, colour)].

    Bars encode the stated percentages proportionally and nothing else; every
    bar carries its own r in the value text, so the bar is never the only
    evidence on screen.
    """
    labs = [Text(d[0], font=MONO, font_size=fs, color=INK) for d in data]
    vals = [Text(d[2], font=MONO, font_size=fs, color=d[3]) for d in data]
    labw = max(l.width for l in labs)
    valw = max(v.width for v in vals)

    # Build CENTRED on the origin. Laying the rows out from x=0 rightward puts
    # explicit coordinates outside the frame before fit_src() recentres the
    # group, which GATE A rejects -- correctly, since nothing guarantees the
    # recentring happens.
    total = labw + 0.40 + maxw + 0.40 + valw
    x0 = -total / 2.0
    x_bar = x0 + labw + 0.40
    x_val = x_bar + maxw + 0.40
    y0 = (len(data) - 1) * (bh + gap) / 2.0

    rows = VGroup()
    tracks = VGroup()
    for i, ((name, frac, vtext, color), lab, val) in enumerate(zip(data, labs, vals)):
        y = y0 - i * (bh + gap)
        track = RoundedRectangle(width=maxw, height=bh, corner_radius=0.08,
                                 stroke_width=1.5, stroke_color=INK_SOFT,
                                 stroke_opacity=0.70, fill_opacity=0)
        track.move_to([x_bar + maxw / 2.0, y, 0])
        tracks.add(track)
        bar = RoundedRectangle(width=max(0.34, maxw * frac), height=bh,
                               corner_radius=0.08, stroke_width=2.8,
                               stroke_color=color, fill_opacity=0.34, fill_color=color)
        lab.move_to([x0 + labw - lab.width / 2.0, y, 0])
        bar.move_to([x_bar + bar.width / 2.0, y, 0])
        val.move_to([x_val + val.width / 2.0, y, 0])
        rows.add(VGroup(lab, bar, val))
    return rows, tracks


class B01_WhatTheToolGivesYou(Scene):
    """BLUF: three things, and the third is an instrument. 21.14s."""

    def construct(self):
        page(self)
        head = kicker("WHAT AN AI PRACTICE TOOL ACTUALLY GIVES YOU",
                      "three things · one of them has evidence attached")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = [
            chip("more repetitions — no waiting for a weekly lesson", INK_SOFT,
                 font_size=24, pad=0.46, height=0.60),
            chip("correctness feedback in the moment — that note was flat", INK_SOFT,
                 font_size=24, pad=0.46, height=0.60),
            chip("a log of every minute, timestamped, no memory in the loop", TERRA,
                 font_size=24, pad=0.46, height=0.60),
        ]
        mark = chip("this one is an instrument", TERRA, font_size=21, pad=0.40, height=0.52)
        note = Text("and an instrument can be measured against other instruments",
                    font=SANS, font_size=24, color=INK)
        body = fit_src(VGroup(VGroup(*rows).arrange(DOWN, buff=0.22),
                              mark, note).arrange(DOWN, buff=0.34))
        src = source_line("the first two are good · the third is the measurable one")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.4)
            self.wait(0.8)
        self.play(Create(mark[0]), FadeIn(mark[1]), run_time=1.5)
        self.wait(1.2)
        self.play(FadeIn(note), run_time=1.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.5)

        point = spark("The log is the part with evidence attached")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.94)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before any figure. 21.21s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CLAIM ABOUT PRACTICE",
                      "ask these before you accept a percentage")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  HOW WAS PRACTICE\n   MEASURED?", ["remembered,", "or recorded"],
                  accent=INK_SOFT),
            panel("2  HOW WAS PERFORMANCE\n   MEASURED?", ["which group someone", "belongs to, or a score"],
                  accent=INK_SOFT),
            panel("3  WHAT ABOUT\n   THE REST?", ["every result leaves", "most of the variance",
                                                  "unexplained — and people", "fill it with a story"],
                  accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in row:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=2.4)
            self.wait(2.0)

        point = spark("The third one is the one nobody asks")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.11)


class B03_TheHeadline(Scene):
    """EVIDENCE: music at 21%, in context, with the study's scale. 31.40s."""

    def construct(self):
        page(self)
        head = kicker("DELIBERATE PRACTICE, BY DOMAIN",
                      "percentage of the variance BETWEEN people, r²")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [
            ("games", 26 / 26.0, "26%    r = .51", INK),
            ("music", 21 / 26.0, "21%    r = .46", TERRA),
            ("sports", 18 / 26.0, "18%    r = .42", INK),
            ("education", 4 / 26.0, "4%    r = .21", INK),
            ("professions", 1 / 26.0, "<1%    r = .05, n.s.", INK),
        ]
        bars, tracks = barset(data)
        scale = chip("111 independent samples · 157 effect sizes · 11,135 participants",
                     INK, font_size=21, pad=0.40, height=0.52)
        body = fit_src(VGroup(VGroup(tracks, bars), scale).arrange(DOWN, buff=0.40))
        src = source_line("Macnamara, Hambrick & Oswald (2014), Psychological Science")

        self.play(Create(tracks), run_time=0.8)
        for r in bars:
            self.play(FadeIn(r[0]), Create(r[1]), FadeIn(r[2]), run_time=1.2)
            self.wait(1.0)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.4)
        self.play(Create(scale[0]), FadeIn(scale[1]), run_time=2.0)
        self.wait(7.8)

        point = spark("Music is near the top of the paper")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.5)


class B04_HowPracticeWasMeasured(Scene):
    """HERO: the practice-measurement moderator. 31.52s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 — HOW WAS THE PRACTICE MEASURED?",
                      "the same question, measured three ways")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [
            ("recalled: interview", 20 / 20.0, "20%    r = .45", INK),
            ("recalled: questionnaire", 12 / 20.0, "12%    r = .34", INK),
            ("logged as it happened", 5 / 20.0, "5%    r = .22", TERRA),
        ]
        # labels kept short so the track can stay wide without pushing the
        # value column past the safe x-edge
        bars, tracks = barset(data, maxw=6.0)
        mod = chip("a significant difference between methods · Q(2) = 16.19, p < .001",
                   INK, font_size=21, pad=0.40, height=0.52)
        quote = chip("the paper's own view: the log method \"yields more valid estimates\"",
                     TERRA, font_size=21, pad=0.40, height=0.52)
        body = fit_src(VGroup(VGroup(tracks, bars), mod, quote).arrange(DOWN, buff=0.34))
        src = source_line("Macnamara, Hambrick & Oswald (2014) · moderator analysis")

        self.play(Create(tracks), run_time=0.8)
        for r in bars:
            self.play(FadeIn(r[0]), Create(r[1]), FadeIn(r[2]), run_time=1.6)
            self.wait(1.6)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.0)
        self.play(Create(mod[0]), FadeIn(mod[1]), run_time=1.8)
        self.wait(1.6)
        self.play(Create(quote[0]), FadeIn(quote[1]), run_time=2.4)
        self.wait(6.5)

        point = spark("Measure it better, and it shrinks")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.9)


class B05_HowPerformanceWasMeasured(Scene):
    """the second moderator, pointing the same way. 22.87s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 — HOW WAS PERFORMANCE MEASURED?",
                      "the other axis, and it does the same thing")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [
            ("group membership", 26 / 26.0, "26%    r = .51", INK),
            ("laboratory tasks", 14 / 26.0, "14%    r = .37", INK),
            ("expert ratings", 9 / 26.0, "9%    r = .30", INK),
            ("a measured score", 8 / 26.0, "8%    r = .28", TERRA),
        ]
        bars, tracks = barset(data)
        mod = chip("Q(3) = 14.41, p = .002", INK, font_size=21, pad=0.40, height=0.52)
        line = Text("two independent moderators, both pointing the same way",
                    font=SANS, font_size=24, color=INK)
        body = fit_src(VGroup(VGroup(tracks, bars), mod, line).arrange(DOWN, buff=0.32))
        src = source_line("Macnamara, Hambrick & Oswald (2014) · moderator analysis")

        self.play(Create(tracks), run_time=0.7)
        for r in bars:
            self.play(FadeIn(r[0]), Create(r[1]), FadeIn(r[2]), run_time=1.1)
            self.wait(0.9)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(1.0)
        self.play(Create(mod[0]), FadeIn(mod[1]), run_time=1.6)
        self.wait(1.3)
        self.play(FadeIn(line), run_time=1.4)
        self.wait(1.6)

        point = spark("Sharper instrument, smaller effect")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.47)


class B06_YourAppIsTheLog(Scene):
    """the application, with the paper's own conclusion quoted. 29.18s."""

    def construct(self):
        page(self)
        head = kicker("SO WHICH ROW IS YOUR APP'S ROW?",
                      "not somebody asked how many hours they did last year")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = chip("your practice app  =  the log method", INK, font_size=24,
                    pad=0.46, height=0.62)
        arrow = Text("→", font=SERIF, font_size=40, color=INK_SOFT)
        right = stat("5%", ["the row that describes", "its own measurements"],
                     accent=TERRA, fig_fs=56, min_w=4.6)
        top = VGroup(left, arrow, right).arrange(RIGHT, buff=0.40)

        quote = panel("which does not mean practice does not work", [
            "\"deliberate practice is important, but not as",
            "important as has been argued\"",
            "— the paper's own conclusion",
        ], accent=INK, min_w=9.0, fs=20, title_fs=22)

        body = fit_src(VGroup(top, quote).arrange(DOWN, buff=0.40))
        src = source_line("a rising hours chart promises what this data cannot")

        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.8)
        self.play(FadeIn(arrow), run_time=0.6)
        self.play(Create(right[0]), FadeIn(right[1]), run_time=2.0)
        self.wait(3.0)
        self.play(Create(quote[0]), FadeIn(quote[1]), run_time=3.4)
        self.wait(4.5)
        self.play(FadeIn(src), run_time=1.2)
        self.wait(5.0)

        point = spark("The honest number is the smallest one")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.78)


class B07_TheLimits(Scene):
    """FALSIFIABILITY: four limits, the first against my own argument. 31.70s."""

    def construct(self):
        page(self)
        head = kicker("THE LIMITS",
                      "the first one cuts against everything I just said")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        r1 = VGroup(hollow(color=TERRA),
                    Text("variance BETWEEN people — not a promise about your next hour",
                         font=MONO, font_size=22, color=INK)).arrange(RIGHT, buff=0.26)
        r2 = VGroup(hollow(),
                    Text("correlational — nobody randomly assigned ten thousand hours",
                         font=MONO, font_size=22, color=INK)).arrange(RIGHT, buff=0.26)
        r3 = VGroup(hollow(),
                    Text("expert samples have restricted range, which pushes r down",
                         font=MONO, font_size=22, color=INK)).arrange(RIGHT, buff=0.26)
        r4 = VGroup(hollow(),
                    Text("the remainder is UNEXPLAINED", font=MONO, font_size=22, color=INK),
                    crossmark(TERRA),
                    Text("talent", font=MONO, font_size=22, color=INK_SOFT)).arrange(
                        RIGHT, buff=0.26)

        mark = chip("this one limits my own argument", TERRA, font_size=20,
                    pad=0.38, height=0.50)
        rows = VGroup(r1, r2, r3, r4).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        body = fit_src(VGroup(rows, mark).arrange(DOWN, buff=0.38))
        src = source_line("the paper says unexplained · those are not the same word")

        for r in (r1, r2, r3, r4):
            self.play(Create(r[0]), FadeIn(r[1:]), run_time=1.6)
            self.wait(1.9)
        self.play(Create(mark[0]), FadeIn(mark[1]), run_time=1.6)
        self.wait(2.0)
        self.play(FadeIn(src), run_time=1.2)
        self.wait(6.2)

        point = spark("Unexplained is not a synonym for talent")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.8)


class B08_Verdict(Scene):
    """VERDICT: the rubric scored, then both sides. 31.46s."""

    def construct(self):
        page(self)
        head = kicker("SCORED",
                      "three questions, three answers, then both sides")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup(
            tickrow("practice measured:  by log — the accurate method, smallest number"),
            tickrow("performance measured:  harder measure, smaller effect, twice over"),
            tickrow("the rest:  unexplained, and left that way"),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        good = panel("BE EXCITED", ["these tools produce the most",
                                    "honest practice data anyone",
                                    "studying this has had",
                                    "— and the data set is posted"],
                     accent=INK, min_w=5.4, fs=19, title_fs=23)
        bad = panel("BE SCEPTICAL", ["of any hours chart implying",
                                     "the hours are the answer",
                                     "— for the method your app",
                                     "actually uses, about 5%"],
                    accent=TERRA, min_w=5.4, fs=19, title_fs=23)
        pair = VGroup(good, bad).arrange(RIGHT, buff=0.44, aligned_edge=UP)

        body = fit_src(VGroup(rows, pair).arrange(DOWN, buff=0.40))
        src = source_line("Macnamara, Hambrick & Oswald (2014) · data openly posted")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.5)
            self.wait(1.5)
        self.wait(1.5)
        self.play(Create(good[0]), FadeIn(good[1]), run_time=2.6)
        self.wait(2.0)
        self.play(Create(bad[0]), FadeIn(bad[1]), run_time=2.6)
        self.wait(3.0)
        self.play(FadeIn(src), run_time=1.2)
        self.wait(4.0)

        point = spark("Ask what the number is a percentage of")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.66)
