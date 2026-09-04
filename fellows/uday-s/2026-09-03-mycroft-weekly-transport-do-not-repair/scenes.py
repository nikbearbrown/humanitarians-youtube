"""Manim beats for the reel `mycroft-weekly-transport-do-not-repair`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json -- audio is
the master clock, never these numbers.

Subject: mycroft @ bdc1bc1 (2026-09-03). Every number here was verified against
a live run of the step-2/step-3 scripts, not read off the commit message; see
SOURCES.md / FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent). Layout lessons already paid for, kept here:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text (GATE B reads the
    overflow as label-on-a-line)
  * beats carrying a citation use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text -- mark the connector, not the label
"""

import glob
import os

import manimpango
import numpy as np
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
    return Text(text, font=SERIF, font_size=38, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    return Text(text, font=MONO, font_size=17, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def fit(group, w=BODY_W, h=BODY_H):
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + BODY_BOTTOM) / 2, 0])
    return group


def fit_src(group, w=BODY_W):
    h = BODY_TOP - SRC_BOTTOM
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + SRC_BOTTOM) / 2, 0])
    return group


def tick(color=INK):
    """A drawn check mark. Sits BESIDE a label, never across it."""
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def panel(title, lines, accent=INK_SOFT, min_w=4.6):
    """A bordered result panel: geometry, so the beat is more than text."""
    t = Text(title, font=SANS, font_size=25, color=accent)
    body = VGroup(*[Text(l, font=MONO, font_size=21, color=INK) for l in lines])
    body.arrange(DOWN, buff=0.26, aligned_edge=LEFT)
    inner = VGroup(t, body).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.8),
                           height=inner.height + 0.85, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_LedgerMoves(Scene):
    """PROBLEM: last week's open ledger, two rows closing. 12.25s."""

    ROWS = [
        ("run-envelope.json absent", True),
        ("gate 2 cannot clear", True),
        ("5 steps unwritten", False),
        ("6 TODO markers still stand", False),
    ]

    def construct(self):
        page(self)
        head = kicker("LAST WEEK'S LEDGER", "what was still open")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for label, closes in self.ROWS:
            box = RoundedRectangle(width=0.34, height=0.34, corner_radius=0.06,
                                   stroke_width=2.0, stroke_color=TERRA, fill_opacity=0)
            t = Text(label, font=MONO, font_size=26, color=TERRA)
            t.next_to(box, RIGHT, buff=0.4)
            rows.add(VGroup(box, t))
        rows.arrange(DOWN, buff=0.40, aligned_edge=LEFT)
        fit(rows)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.25) for r in rows],
                              lag_ratio=0.35), run_time=2.2)
        self.wait(1.0)

        # the two that close: recolour to ink and gain a tick BESIDE the box
        anims = []
        for r, (_l, closes) in zip(rows, self.ROWS):
            if closes:
                mark = tick(INK).scale(1.1).move_to(r[0].get_center())
                anims += [r[0].animate.set_stroke(INK), r[1].animate.set_color(INK),
                          Create(mark)]
        self.play(*anims, run_time=2.4)
        self.wait(0.8)

        point = spark("Two of four, closed")
        self.play(Write(point), run_time=1.6)
        self.wait(2.35)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: three questions for any pipeline stage. 16.83s.

    PROOF requires the rubric shown as a structure before any example. This
    beat opens at 20.16s in the cut, ahead of step 2 at 47.10s.
    """

    QS = [
        ("1", "DECIDES", "what does this\nstage decide?"),
        ("2", "REFUSES", "what must it NOT decide,\nthough it easily could?"),
        ("3", "EVIDENCE", "what can a reviewer\nre-check afterwards?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS", "ask these of any pipeline stage")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.QS:
            n = Text(num, font=SERIF, font_size=34, color=TERRA)
            t = Text(title, font=SANS, font_size=29, color=INK)
            b = Text(body, font=MONO, font_size=20, color=INK_SOFT, line_spacing=0.7)
            head_row = VGroup(n, t).arrange(RIGHT, buff=0.30)
            inner = VGroup(head_row, b).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.85, height=inner.height + 0.85,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.45))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.0)
            self.wait(1.4)

        point = spark("Question two is the load-bearing one")
        self.play(Write(point), run_time=1.8)
        self.wait(5.93)


class B05_ScoreIngest(Scene):
    """OUTPUT 1: step 2 scored on the three axes. 15.83s."""

    SCORES = [
        ("DECIDES", "nothing about content", INK),
        ("REFUSES", "every repair it could make", TERRA),
        ("EVIDENCE", "an envelope of what it moved", INK),
    ]

    def construct(self):
        page(self)
        head = kicker("STEP 2 — INGEST", "scored on the three questions")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # each answer lands in a bordered cell — a scorecard is geometry, and a
        # beat carried by text alone has no shape-state to change (GATE A)
        rows = VGroup()
        for axis, answer, color in self.SCORES:
            a = Text(axis, font=SANS, font_size=27, color=INK_SOFT)
            v = Text(answer, font=MONO, font_size=24, color=color)
            cell = RoundedRectangle(width=v.width + 0.7, height=0.78,
                                    corner_radius=0.10, stroke_width=1.8,
                                    stroke_color=color, fill_opacity=0)
            cell.move_to(v.get_center())
            rows.add(VGroup(a, VGroup(cell, v)))
        col = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.7 + (col - r[0].width))
        rows.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        fit(rows)

        self.play(LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.2) for r in rows],
                              lag_ratio=0.2), run_time=1.0)
        for r in rows:
            self.play(Create(r[1][0]), FadeIn(r[1][1], shift=RIGHT * 0.2), run_time=1.3)
        self.wait(1.2)

        point = spark("The discipline is the refusal")
        self.play(Write(point), run_time=1.7)
        self.wait(6.13)


class B08_ShapeRun(Scene):
    """OUTPUT 2: the live step-3 run, both fixture sets. 27.51s.

    Counts are from an actual run, not the commit message:
    missing_fields 4 · parse_errors 3 · count_mismatches 1 = 8, exit 1.
    """

    def construct(self):
        page(self)
        head = kicker("STEP 3 — VALIDATE SHAPE", "one run per fixture set")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        clean = panel("CLEAN SET", ["0 findings", "exit 0"], INK_SOFT)
        defective = panel("DEFECTIVE SET", [
            "4  missing required fields",
            "3  parse errors",
            "1  count mismatch",
            "exit 1  — hard stop",
        ], TERRA)
        pair = VGroup(clean, defective).arrange(RIGHT, buff=0.8, aligned_edge=UP)

        deferred = Text("10 defects belong to step 4 — and types have no field at all",
                        font=SANS, font_size=24, color=TERRA)
        body = fit(VGroup(pair, deferred).arrange(DOWN, buff=0.6))

        self.play(Create(clean[0]), FadeIn(clean[1]), run_time=1.8)
        self.wait(1.4)
        self.play(Create(defective[0]), FadeIn(defective[1][0]), run_time=1.6)
        for line in defective[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.95)
        self.wait(1.6)
        self.play(FadeIn(deferred, shift=UP * 0.2), run_time=1.6)
        self.wait(1.6)

        point = spark("It reports everything, then halts")
        self.play(Write(point), run_time=1.9)
        self.wait(9.86)


class B09_HashDrift(Scene):
    """FALSIFIABILITY: the evidence axis, silently broken. 28.58s."""

    def construct(self):
        page(self)
        head = kicker("WHAT THE FRAMEWORK PREDICTS",
                      "axis 3 — evidence a reviewer can re-check")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        src_file = panel("one file, one commit",
                         ["sample/clean/news-finnhub.json"], INK_SOFT, min_w=5.0)

        # REAL digests, recomputed from the real file's bytes with each line
        # ending — never an invented figure (REBUILD LAW). Reproduce with:
        #   raw.replace(b'\r\n', b'\n')  ->  sha256   vs   ... b'\n' -> b'\r\n'
        linux = panel("checked out on Linux",
                      ["eol = LF    ·  3,180 bytes", "sha256  441291ec…"], INK_SOFT)
        win = panel("checked out on Windows",
                    ["eol = CRLF  ·  3,261 bytes", "sha256  42fdf8fc…"], TERRA)
        pair = VGroup(linux, win).arrange(RIGHT, buff=0.9, aligned_edge=UP)

        verdict = Text("same bytes committed — different hash",
                       font=SANS, font_size=27, color=TERRA)
        body = fit_src(VGroup(src_file, pair, verdict).arrange(DOWN, buff=0.5))
        src = source_line("mycroft · bdc1bc1 · .gitattributes + newline='\\n' at 5 write sites")

        self.play(Create(src_file[0]), FadeIn(src_file[1]), run_time=1.5)
        self.wait(0.8)
        self.play(Create(linux[0]), FadeIn(linux[1]), run_time=1.6)
        self.play(Create(win[0]), FadeIn(win[1]), run_time=1.6)
        self.wait(1.4)
        self.play(Write(verdict), run_time=2.2)
        self.wait(1.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.0)

        point = spark("Evidence that moves is not evidence")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.6)
        self.wait(12.78)


class B10_WeekLedger(Scene):
    """SUMMARY: what closed, what is still open. 15.66s."""

    CLOSED = ["gate 2 clears", "gate 3 clears", "3 of 6 steps written",
              "reruns byte-identical"]
    OPEN = ["3 steps unwritten", "type-violation gap logged", "step 4 not started"]

    def construct(self):
        page(self)
        head = kicker("THE WEEK", "mycroft · commit bdc1bc1")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(title, items, color):
            t = Text(title, font=SANS, font_size=25, color=INK_SOFT)
            body = VGroup(*[Text(i, font=MONO, font_size=23, color=color)
                            for i in items])
            body.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
            rule = Line(LEFT * (max(body.width, t.width) / 2),
                        RIGHT * (max(body.width, t.width) / 2),
                        stroke_width=1.3, color=INK_SOFT)
            col = VGroup(t, rule, body).arrange(DOWN, buff=0.26)
            for part in (t, rule, body):
                part.align_to(col, LEFT)
            return col

        left = column("CLOSED THIS WEEK", self.CLOSED, INK)
        right = column("STILL OPEN", self.OPEN, TERRA)
        fit(VGroup(left, right).arrange(RIGHT, buff=1.5, aligned_edge=UP))

        self.play(FadeIn(left, shift=UP * 0.2), run_time=1.6)
        self.wait(1.6)
        self.play(FadeIn(right, shift=UP * 0.2), run_time=1.6)
        self.wait(1.4)

        point = spark("Three of six. Openly.")
        self.play(Write(point), run_time=1.7)
        self.wait(4.96)
