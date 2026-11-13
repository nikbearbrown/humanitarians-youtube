"""Manim beats for the reel `right-answer-wrong-chain`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: process supervision and multi-hop agents -- what outcome grading cannot
see.

Primary sources. DiRe figures: Trivedi, Balasubramanian, Khot, Sabharwal,
"MuSiQue: Multihop Questions via Single-hop Question Composition", TACL
(10.1162/tacl_a_00475) -- read out of the paper's own Table 4 by extracting the
PDF text, not from a summary. Process supervision: Lightman, Kosaraju, Burda,
Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe, "Let's Verify Step by
Step", arXiv 2305.20050.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over fourteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * a cross sits BESIDE the thing it negates, never drawn through text
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


def vbar(height, label, figure, color, width=1.05, fig_fs=24):
    b = RoundedRectangle(width=width, height=max(height, 0.12), corner_radius=0.07,
                         stroke_width=2.2, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    l = Text(label, font=MONO, font_size=17, color=INK_SOFT)
    return VGroup(f, b, l).arrange(DOWN, buff=0.16)


class B01_TwoDifferentThings(Scene):
    """BLUF: a grading method and a task type, joined by one failure."""

    def construct(self):
        page(self)
        head = kicker("WHAT THE PHRASE ACTUALLY JOINS",
                      "a way of grading, and a kind of question")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = panel("PROCESS SUPERVISION",
                  ["how you grade \u2014 score every",
                   "intermediate step, not just",
                   "the final answer"], accent=INK_SOFT, min_w=5.6, fs=19, title_fs=22)
        b = panel("MULTI-HOP",
                  ["what you asked \u2014 a question",
                   "that needs several facts",
                   "chained together"], accent=INK_SOFT, min_w=5.6, fs=19, title_fs=22)
        pair = VGroup(a, b).arrange(RIGHT, buff=0.50, aligned_edge=UP)

        links = VGroup(
            Line(UP * 0.20, DOWN * 0.20, stroke_width=1.8, color=TERRA),
            Line(UP * 0.20, DOWN * 0.20, stroke_width=1.8, color=TERRA),
        )
        join = panel("what connects them",
                     ["the right answer, from a chain",
                      "that was never followed"], accent=TERRA, min_w=7.2, fs=20, title_fs=22)
        body = fit_src(VGroup(pair, links, join).arrange(DOWN, buff=0.28))
        src = source_line("outcome grading, by construction, cannot tell the difference")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=2.0)
        self.wait(1.4)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=2.0)
        self.wait(1.8)
        self.play(*[Create(l) for l in links], run_time=0.8)
        self.play(Create(join[0]), FadeIn(join[1]), run_time=2.2)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Two categories, one failure")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.2)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY PROCESS-SUPERVISION CLAIM",
                      "ask these before you believe it transfers")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT COUNTS\n   AS A STEP?", ["checkable in arithmetic;", "a design decision",
                                                    "in an agent run"], accent=INK_SOFT),
            panel("2  WHO LABELLED\n   THE STEPS?", ["a human, or a process", "that inferred it from",
                                                     "how things turned out"], accent=TERRA),
            panel("3  FUNDAMENTAL,\n   OR PRACTICAL?", ["those have different", "consequences for",
                                                        "your setting"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.8)
            self.wait(1.5)
        self.wait(3.0)

        point = spark("Question two decides whether it is process supervision at all")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B03_DisconnectedReasoning(Scene):
    """EVIDENCE: the DiRe scores, from the paper's own table."""

    def construct(self):
        page(self)
        head = kicker("SCORING WITHOUT REASONING, MEASURED",
                      "the disconnected-reasoning probe \u00b7 answer F1")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = [
            hbar(3.30, "HotpotQA", "68.8", TERRA),
            hbar(3.04, "2WikiMultihopQA", "63.4", INK),
            hbar(1.81, "MuSiQue", "37.8", INK_SOFT),
        ]
        stack = VGroup(*rows).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        caption = Text("lower is harder to cheat \u2014 MuSiQue was built to resist shortcuts",
                       font=MONO, font_size=19, color=INK_SOFT)
        punch = Text("a reasoning benchmark, scored on without the reasoning",
                     font=SANS, font_size=23, color=TERRA)
        body = fit_src(VGroup(stack, caption, punch).arrange(DOWN, buff=0.34))
        src = source_line("Trivedi, Balasubramanian, Khot, Sabharwal \u00b7 MuSiQue \u00b7 TACL \u00b7 Table 4")

        for r in rows:
            self.play(Create(r[1]), FadeIn(r[0]), FadeIn(r[2]), run_time=1.5)
            self.wait(1.0)
        self.play(FadeIn(caption), run_time=1.5)
        self.wait(1.6)
        self.play(FadeIn(punch), run_time=1.8)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Sixty-eight point eight, bypassing the steps")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.8)


class B04_TheFlatLine(Scene):
    """EVIDENCE: degradation with hops, against a model that does not move."""

    def construct(self):
        page(self)
        head = kicker("THE SECOND TELL",
                      "what it looks like when a model really is chaining")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        real = VGroup(
            vbar(2.05, "2-hop", "57.9", INK),
            vbar(1.70, "3-hop", "47.9", INK),
            vbar(1.00, "4-hop", "28.1", INK),
        ).arrange(RIGHT, buff=0.30, aligned_edge=DOWN)
        rlab = Text("degrades as the chain lengthens", font=MONO, font_size=18, color=INK_SOFT)
        left = VGroup(real, rlab).arrange(DOWN, buff=0.24)

        flat = VGroup(
            vbar(1.50, "2-hop", "~42", TERRA),
            vbar(1.50, "3-hop", "~42", TERRA),
            vbar(1.50, "4-hop", "~42", TERRA),
        ).arrange(RIGHT, buff=0.30, aligned_edge=DOWN)
        flab = Text("flat, whatever the question needs", font=MONO, font_size=18, color=TERRA)
        right = VGroup(flat, flab).arrange(DOWN, buff=0.24)

        pair = VGroup(left, right).arrange(RIGHT, buff=0.80, aligned_edge=DOWN)
        verdict = Text("a flat line across hop count is not robustness \u2014 it is not hopping",
                       font=SANS, font_size=22, color=TERRA)
        body = fit_src(VGroup(pair, verdict).arrange(DOWN, buff=0.40))
        src = source_line("same paper \u00b7 best model EX(SA) against the EE model \u00b7 answer F1")

        for b in real:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=1.1)
        self.play(FadeIn(rlab), run_time=1.0)
        self.wait(1.8)
        for b in flat:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=1.1)
        self.play(FadeIn(flab), run_time=1.0)
        self.wait(1.8)
        self.play(FadeIn(verdict), run_time=1.9)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("The tell is the slope")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.6)


class B05_GradeTheSteps(Scene):
    """EVIDENCE: what process supervision is, the headline result, and its cost."""

    def construct(self):
        page(self)
        head = kicker("THE PROPOSED ANSWER",
                      "grade every step; stop at the first one that is wrong")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup(
            stat("78%", ["of a representative", "MATH test subset"], accent=INK, min_w=4.6),
            stat("800,000", ["step-level labels,", "written by humans"], accent=TERRA, min_w=5.0),
        ).arrange(RIGHT, buff=0.50, aligned_edge=UP)
        claim = Text("\u201cprocess supervision significantly outperforms outcome supervision\u201d",
                     font=SANS, font_size=22, color=INK)
        cost = Text("that second number is what it took",
                    font=MONO, font_size=19, color=TERRA)
        body = fit_src(VGroup(cards, claim, cost).arrange(DOWN, buff=0.34))
        src = source_line("Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe \u00b7 arXiv 2305.20050")

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(2.0)
        self.play(FadeIn(claim), run_time=2.6)
        self.wait(3.0)
        self.play(FadeIn(cost), run_time=2.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(4.2)

        point = spark("Eight hundred thousand human judgements")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B06_NotALaw(Scene):
    """FALSIFIABILITY: parity on easier maths, and the statistical result."""

    def construct(self):
        page(self)
        head = kicker("BUT IT IS NOT A LAW",
                      "two results that bound the claim")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for lead, result, colour in [
            ("on grade-school maths, an earlier study found",
             "outcome and process reached similar final performance", INK_SOFT),
            ("and under standard data-coverage assumptions,",
             "outcome supervision is no harder statistically \u2014\nup to polynomial factors in horizon", TERRA),
        ]:
            a = Text(lead, font=MONO, font_size=19, color=INK_SOFT)
            b = Text(result, font=SANS, font_size=22, color=colour, line_spacing=0.9)
            inner = VGroup(a, b).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.74, height=inner.height + 0.56,
                                   corner_radius=0.11, stroke_width=1.9,
                                   stroke_color=colour, fill_opacity=0)
            box.move_to(inner.get_center())
            rows.append(VGroup(box, inner))
        stack = VGroup(*rows).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        close = Text("then the advantage is practical, not informational \u2014 a different claim",
                     font=SANS, font_size=22, color=INK)
        body = fit_src(VGroup(stack, close).arrange(DOWN, buff=0.38))
        src = source_line("Uesato et al. 2022 \u00b7 and the theoretical analysis of step-level verification")

        for r in rows:
            self.play(Create(r[0]), run_time=1.2)
            self.play(FadeIn(r[1]), run_time=1.9)
            self.wait(3.4)
        self.play(FadeIn(close), run_time=2.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(5.2)

        point = spark("Still worth having. Not the same claim.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B07_WhatIsAStep(Scene):
    """QUESTION 2: what breaks when you move from maths to agents."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 AND 2, WHERE THEY BITE",
                      "a step in arithmetic, and a step in an agent run")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        math = panel("a step in arithmetic",
                     ["one line",
                      "a human can read it and say",
                      "whether it follows",
                      "correctness is LOCAL"], accent=INK, min_w=5.8, fs=19, title_fs=22)
        agent = panel("a step in an agent run",
                      ["a tool call? a thought?",
                       "whoever cut the trajectory decides",
                       "whether it was right often is not",
                       "knowable until the end"], accent=TERRA, min_w=6.2, fs=19, title_fs=22)
        pair = VGroup(math, agent).arrange(RIGHT, buff=0.52, aligned_edge=UP)

        note = chip("800,000 human labels existed for one of these",
                    INK_SOFT, font_size=19, height=0.48)
        warn = Text("labels inferred from how the episode ended are outcome labels",
                    font=SANS, font_size=22, color=TERRA)
        body = fit_src(VGroup(pair, note, warn).arrange(DOWN, buff=0.32))
        src = source_line("the contrast is sourced; the inference about agent labelling is reasoning \u2014 see FACTCHECK")

        self.play(Create(math[0]), FadeIn(math[1]), run_time=2.2)
        self.wait(3.0)
        self.play(Create(agent[0]), FadeIn(agent[1]), run_time=2.4)
        self.wait(3.2)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=1.6)
        self.wait(2.4)
        self.play(FadeIn(warn), run_time=1.9)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(4.2)

        point = spark("Outcome supervision, with extra steps")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B08_Verdict(Scene):
    """VERDICT: rubric scored, then both sides."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, answered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("WHAT COUNTS AS A STEP", "clear in maths, a choice in an agent", INK),
              ("WHO LABELLED THEM", "humans \u2014 800,000 times", TERRA),
              ("FUNDAMENTAL OR PRACTICAL", "theory says information is not the bottleneck", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=18)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.32))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  a measured way to catch a right answer on a broken chain",
                 font=SANS, font_size=21, color=INK),
            Text("BE SCEPTICAL OF:  process supervision for an agent, with no step defined",
                 font=SANS, font_size=21, color=TERRA),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        body = fit_src(VGroup(scored, verdict).arrange(DOWN, buff=0.50, aligned_edge=LEFT))
        src = source_line("MuSiQue, TACL \u00b7 Let's Verify Step by Step, arXiv 2305.20050")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.6)
            self.wait(1.3)
        self.wait(1.6)
        self.play(FadeIn(src), run_time=1.0)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=2.0)
            self.wait(1.5)

        point = spark("Say what a step is, and who decided")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(7.8)
