"""Manim beats for the reel `mycroft-weekly-passing-for-the-wrong-reason`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 4157a8e (2026-09-25), branch
feature/market-sentiment-human-report. Episode 5.

Every result on screen was produced by running the old and new gate tests
live; the three break-test cases were reproduced in a scratch tree so the
subject repo was never written to. See SOURCES.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over seven previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, RoundedRectangle,
    Scene, Text, VGroup, Write,
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
    """A drawn check mark. Sits inside or beside a box, never across text."""
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def chip(label, color, font_size=19, pad=0.32, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(box, t)


def panel(title, lines, accent=INK_SOFT, min_w=4.4, fs=20, title_fs=24):
    t = Text(title, font=SANS, font_size=title_fs, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=fs, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_EpisodeFourTask(Scene):
    """PROBLEM: last episode's viewer task, turned inward. 15.40s."""

    def construct(self):
        page(self)
        head = kicker("LAST EPISODE'S QUESTION", "asked of the viewer · then of this repo")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        q = Text("\"For every green indicator you trust:\nwhat makes it red, and when did it last go red?\"",
                 font=MONO, font_size=23, color=INK, line_spacing=0.8)
        q_box = RoundedRectangle(width=q.width + 1.0, height=q.height + 0.7,
                                 corner_radius=0.12, stroke_width=1.8,
                                 stroke_color=INK_SOFT, fill_opacity=0)
        q_box.move_to(q.get_center())
        question = VGroup(q_box, q)

        g4 = panel("GATE 4", ["named on camera"], INK_SOFT, min_w=4.6, fs=22)
        g5 = panel("GATE 5", ["never examined"], TERRA, min_w=4.6, fs=22)
        gates = VGroup(g4, g5).arrange(RIGHT, buff=0.9, aligned_edge=UP)

        fit(VGroup(question, gates).arrange(DOWN, buff=0.7))

        self.play(Create(q_box), FadeIn(q), run_time=2.2)
        self.wait(1.6)
        self.play(Create(g4[0]), FadeIn(g4[1]), run_time=1.5)
        self.wait(0.8)
        self.play(Create(g5[0]), FadeIn(g5[1]), run_time=1.5)
        self.wait(1.2)

        point = spark("The one I didn't look at was worse")
        self.play(Write(point), run_time=2.0)
        self.wait(3.68)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: three questions for any automated check. 17.19s."""

    QS = [
        ("1", "WHAT MAKES\nIT FAIL?", "name the condition,\nprecisely"),
        ("2", "HAS IT EVER\nFAILED?", "has anything exercised\nthat condition?"),
        ("3", "WHY IS IT\nPASSING NOW?", "the reason may not be\nthe one you assume"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS", "ask these of any automated check")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for i, (num, title, body) in enumerate(self.QS):
            accent = TERRA if i == 2 else INK_SOFT
            n = Text(num, font=SERIF, font_size=32, color=TERRA)
            t = Text(title, font=SANS, font_size=25, color=INK, line_spacing=0.7)
            b = Text(body, font=MONO, font_size=19, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.28, aligned_edge=UP)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.8, height=inner.height + 0.8,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=accent, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.42))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.0)
            self.wait(1.25)

        point = spark("Question three is the one that catches you")
        self.play(Write(point), run_time=2.0)
        self.wait(3.54)


class B05_OldGatePasses(Scene):
    """OUTPUT 1: the centrepiece — the old test passes, beside the missing record. 20.86s."""

    RECORDS = [("gate-1.json", True), ("gate-2.json", True),
               ("gate-3.json", True), ("gate-4.json", True),
               ("gate-5.json", False)]

    def construct(self):
        page(self)
        head = kicker("THE OLD TEST, RUN TODAY", "against the repository as it stands")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        result = panel("OLD GATE 5", ["PASS", "on the marker alone",
                                      "nothing was approved"], TERRA, min_w=5.0, fs=22)

        # A present record gets a TICK; the absent one stays hollow. Colour alone
        # does not carry the difference — the whole beat is four that exist and
        # one that does not, so the geometry has to say so.
        rows = VGroup()
        for name, present in self.RECORDS:
            c = INK if present else TERRA
            box = RoundedRectangle(width=0.32, height=0.32, corner_radius=0.06,
                                   stroke_width=2.0, stroke_color=c, fill_opacity=0)
            t = Text(name, font=MONO, font_size=20, color=c)
            t.next_to(box, RIGHT, buff=0.34)
            row = VGroup(box, t)
            if present:
                row.add(tick(INK).scale(1.05).move_to(box.get_center()))
            rows.add(row)
        rows.arrange(DOWN, buff=0.20, aligned_edge=LEFT)
        folder = VGroup(Text("logs/gate-decisions/", font=SANS, font_size=22,
                             color=INK_SOFT), rows).arrange(DOWN, buff=0.30)
        rows.align_to(folder, LEFT)
        folder[0].align_to(folder, LEFT)

        pair = VGroup(result, folder).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        note = Text("the folder looks full — the file is absent",
                    font=SANS, font_size=25, color=TERRA)
        fit_src(VGroup(pair, note).arrange(DOWN, buff=0.55))
        src = source_line("old test from commit aa0c0fe, run against the tree at 4157a8e")

        self.play(Create(result[0]), FadeIn(result[1]), run_time=1.8)
        self.wait(1.4)
        self.play(FadeIn(folder[0]), run_time=0.8)
        for r in rows:
            # r[2] is the tick, and only present rows have one — it has to be
            # animated in explicitly or it never reaches the screen at all
            anims = [Create(r[0]), FadeIn(r[1])]
            if len(r) > 2:
                anims.append(Create(r[2]))
            self.play(*anims, run_time=0.62)
        self.wait(1.4)
        self.play(Write(note), run_time=2.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.2)

        point = spark("A pass for a clearance that never happened")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(3.72)


class B08_BreakTest(Scene):
    """OUTPUT 2: the three break-test cases. 16.17s."""

    CASES = [
        ("no live call  ·  no approval", "PASS", INK_SOFT, ""),
        ("live call  ·  NO approval", "FAIL", TERRA, "the new path"),
        ("live call  ·  approval on disk", "PASS", INK_SOFT, ""),
    ]

    def construct(self):
        page(self)
        head = kicker("BREAK-TESTED", "every branch, proved by breaking it")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for cond, result, color, tag in self.CASES:
            c = Text(cond, font=MONO, font_size=22, color=INK)
            r = chip(result, color, font_size=21, pad=0.4, height=0.44)
            t = Text(tag, font=SANS, font_size=20, color=TERRA)
            rows.add(VGroup(c, r, t))
        cw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.7 + (cw - r[0].width))
            r[2].next_to(r[1], RIGHT, buff=0.45)
        rows.arrange(DOWN, buff=0.44, aligned_edge=LEFT)
        fit_src(rows)
        src = source_line("reproduced in a scratch tree — the subject repo was never written to")

        for r in rows:
            self.play(FadeIn(r[0], shift=RIGHT * 0.2), Create(r[1][0]),
                      FadeIn(r[1][1]), FadeIn(r[2]), run_time=1.5)
            self.wait(0.7)
        self.wait(0.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(0.9)

        point = spark("Only one of the three is a real clearance")
        self.play(Write(point), run_time=2.1)
        self.wait(2.98)


class B09_TwoMeanings(Scene):
    """FALSIFIABILITY: the same green, two very different meanings. 21.63s."""

    def construct(self):
        page(self)
        head = kicker("WHY IS IT PASSING RIGHT NOW?",
                      "question 3, answered honestly")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        result = chip("gate 5  ·  PASS", INK_SOFT, font_size=24, pad=0.55, height=0.58)

        cleared = panel("COULD MEAN: CLEARED", ["a named human", "signed the record"],
                        INK_SOFT, min_w=5.0, fs=21)
        na = panel("ACTUALLY MEANS: NOT APPLICABLE",
                   ["live mode is unimplemented", "no live call is possible",
                    "the failing condition cannot occur"], TERRA, min_w=5.4, fs=21)
        pair = VGroup(cleared, na).arrange(RIGHT, buff=0.85, aligned_edge=UP)

        body = fit_src(VGroup(result, pair).arrange(DOWN, buff=0.6))
        src = source_line("stated in the commit: it passes because no live call is possible")

        self.play(Create(result[0]), FadeIn(result[1]), run_time=1.5)
        self.wait(1.2)
        self.play(Create(cleared[0]), FadeIn(cleared[1]), run_time=1.6)
        self.wait(1.2)
        self.play(Create(na[0]), FadeIn(na[1]), run_time=1.8)
        self.wait(1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.0)

        point = spark("Capable of working is not the same as working")
        self.play(Write(point), run_time=2.2)
        self.wait(5.83)


class B10_Ledger(Scene):
    """SUMMARY: the promotion, and the series loops now closed. 18.50s."""

    FRONT = ["status: RUNNABLE-SAMPLE", "recipe_version: 0.2.0",
             "todos_open: 2", "attestation: null"]
    CLOSED = ["step 3 gained type_errors  (ep 3)",
              "report Reader corrected  (ep 4)",
              "gates 4 and 5 can now fail  (ep 5)"]

    def construct(self):
        page(self)
        head = kicker("THE LEDGER", "mycroft · commit 4157a8e")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("DECLARED", self.FRONT, INK_SOFT, min_w=5.2, fs=21)
        right = panel("LOOPS THIS SERIES OPENED", self.CLOSED, TERRA, min_w=5.4, fs=20)
        pair = VGroup(left, right).arrange(RIGHT, buff=0.85, aligned_edge=UP)

        note = Text("RUNNABLE-LIVE is explicitly not claimed",
                    font=SANS, font_size=24, color=TERRA)
        fit(VGroup(pair, note).arrange(DOWN, buff=0.55))

        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.8)
        self.wait(1.4)
        self.play(Create(right[0]), FadeIn(right[1][0]), run_time=1.4)
        for line in right[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.9)
        self.wait(1.2)
        self.play(Write(note), run_time=2.0)
        self.wait(1.2)

        point = spark("Logged, then closed")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.7)
        self.wait(3.16)
