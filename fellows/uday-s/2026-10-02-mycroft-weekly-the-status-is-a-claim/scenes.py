"""Manim beats for the reel `mycroft-weekly-the-status-is-a-claim`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 8c13b87 (2026-10-02), branch
feature/market-sentiment-human-report -- the branch head, and identical to
origin's. Episode 6.

Every figure on screen was recounted from
logs/attestations/market-sentiment-analysis-part-1-v0.2.0.md and from the
commit itself. The subject repo was never written to. See SOURCES.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over eight previous reels:
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
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, Line, RoundedRectangle, Scene, Text,
    VGroup, Write,
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


def hollow(size=0.26, color=INK_SOFT):
    """An UNticked box. In B05 the emptiness is the content."""
    return RoundedRectangle(width=size, height=size, corner_radius=0.04,
                            stroke_width=1.8, stroke_color=color, fill_opacity=0)


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


def stat(figure, caption_lines, accent=INK, fig_fs=54, cap_fs=19, min_w=4.2):
    """A bordered stat card. The figure is the evidence; the caption names it."""
    f = Text(figure, font=SERIF, font_size=fig_fs, color=accent)
    caps = VGroup(*[Text(c, font=MONO, font_size=cap_fs, color=INK_SOFT)
                    for c in caption_lines])
    caps.arrange(DOWN, buff=0.16)
    inner = VGroup(f, caps).arrange(DOWN, buff=0.24)
    box = RoundedRectangle(width=max(min_w, inner.width + 0.7),
                           height=inner.height + 0.6, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


class B01_CommitAndTheField(Scene):
    """PROBLEM: the commit, and the one field it refused to change. 15.02s."""

    def construct(self):
        page(self)
        head = kicker("THE COMMIT, AND THE FIELD IT LEFT ALONE",
                      "8c13b87 \u00b7 feature/market-sentiment-human-report")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("the commit", ["7 files changed",
                                    "+177  -12",
                                    "attestation   125 lines",
                                    "RUN_LOG        40 lines"], accent=INK_SOFT)
        right = panel("status:", ["RUNNABLE-SAMPLE", "unchanged"], accent=TERRA, min_w=4.6)

        link = Line(LEFT * 0.75, RIGHT * 0.75, stroke_width=1.8, color=INK_SOFT)
        bar = Line(DOWN * 0.42, UP * 0.42, stroke_width=5.0, color=TERRA)
        pair = VGroup(left, link, right).arrange(RIGHT, buff=0.5)
        bar.move_to(link.get_center())
        body = fit(VGroup(pair, bar))

        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.5)
        self.play(Create(link), run_time=0.7)
        self.play(Create(right[0]), FadeIn(right[1]), run_time=1.4)
        self.wait(1.3)
        self.play(Create(bar), run_time=1.1)
        self.wait(1.6)

        point = spark("The write that did not happen")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(3.7)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before any evidence. 16.11s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY STATUS FIELD",
                      "ask these before you type the word")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT DID\n   YOU RUN?", ["named rows,", "not a feeling"], accent=INK_SOFT),
            panel("2  WHAT DID YOU\n   NOT RUN?", ["written down", "where a reviewer", "will see it"],
                  accent=INK_SOFT),
            panel("3  DID A GATE\n   SAY NO?", ["a refusal outranks", "your own judgment"], accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.46, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.9)
        self.wait(1.6)

        point = spark("Or it was never a gate")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(2.7)


class B04_TestedTable(Scene):
    """QUESTION 1: what did you run. Counted from the Tested table. 17.94s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 WHAT DID YOU RUN?",
                      "the attestation's Tested table, counted")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            stat("17", ["rows tested"], accent=INK),
            stat("7", ["of them deliberate", "attempts to break it"], accent=TERRA),
            stat("18 / 18", ["catalogued defects found", "8 in step 3 \u00b7 10 in step 4"], accent=INK),
            stat("0", ["of step 4's defects", "leaked into step 3"], accent=TERRA),
        ]
        top = VGroup(cards[0], cards[1]).arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        bot = VGroup(cards[2], cards[3]).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        grid = fit_src(VGroup(top, bot).arrange(DOWN, buff=0.42))
        src = source_line("logs/attestations/market-sentiment-analysis-part-1-v0.2.0.md \u00b7 Tested")

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.55)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.5)

        point = spark("Seven of seventeen were trying to break it")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(2.4)


class B05_DidNotTest(Scene):
    """QUESTION 2: the Did-not-test section -- ten unticked boxes. 21.93s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 WHAT DID YOU NOT RUN?",
                      "ten entries, and three of them have a price")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        items = [
            ("live execution", "never run \u2014 step 2 stops before any fetch"),
            ("whether the score means anything", "weights inherited: no derivation, no author"),
            ("wrong-entity rows", "cost 782 purged rows, reached a finished brief"),
            ("upstream HTTP failures", None),
            ("encoding defects", None),
            ("volume and pagination", None),
            ("the redditMentions > 20 branch", None),
            ("any independent test suite", None),
            ("cross-platform behaviour", None),
            ("interrupted or partial runs", None),
        ]

        rows, boxes, labels, costs = [], [], [], []
        for label, cost in items:
            b = hollow()
            t = Text(label, font=MONO, font_size=18, color=INK)
            cells = [b, t]
            if cost:
                c = Text(cost, font=MONO, font_size=17,
                         color=TERRA if "782" in cost else INK_SOFT)
                cells.append(c)
                costs.append(c)
            r = VGroup(*cells).arrange(RIGHT, buff=0.30)
            rows.append(r)
            boxes.append(b)
            labels.append(t)
        stack = fit_src(VGroup(*rows).arrange(DOWN, buff=0.17, aligned_edge=LEFT))
        src = source_line("same file \u00b7 Did not test \u00b7 DATA_CONTRACT.md for the 782")

        # the boxes land first and stay empty -- the emptiness is the content
        self.play(*[Create(b) for b in boxes], run_time=1.4)
        self.play(*[FadeIn(t) for t in labels], run_time=1.6)
        self.wait(1.2)
        for c in costs:
            self.play(FadeIn(c, shift=RIGHT * 0.15), run_time=1.5)
            self.wait(1.1)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.4)

        point = spark("Ten boxes nobody gets to tick")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(2.9)


class B07_Lifecycle(Scene):
    """the verdict the rubric forces -- the ladder, and where it stops. 21.89s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 DID A GATE SAY NO?",
                      "SNICKERDOODLE.md \u00b7 the recipe lifecycle")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # The ladder runs DOWN, the way SNICKERDOODLE.md writes it. Laid out
        # horizontally the group is width-limited, so fit() cannot scale it up
        # and the beat underfills (measured: 47%).
        names = ["DRAFT", "SPECIFIED", "RUNNABLE-SAMPLE", "RUNNABLE-LIVE", "VERIFIED"]
        chips = [chip(n, TERRA if n == "RUNNABLE-SAMPLE" else INK_SOFT,
                      font_size=22, height=0.50, pad=0.44)
                 for n in names]
        links = [Line(UP * 0.17, DOWN * 0.17, stroke_width=1.6, color=INK_SOFT)
                 for _ in range(4)]

        cells = []
        for i, c in enumerate(chips):
            cells.append(c)
            if i < 4:
                cells.append(links[i])
        ladder = VGroup(*cells).arrange(DOWN, buff=0.14)

        bar = Line(LEFT * 0.60, RIGHT * 0.60, stroke_width=5.0, color=TERRA)
        reasons = panel("why it stops here",
                        ["no live run has ever happened",
                         "gate 5 \u00b7 decision: deny",
                         "approved_for_live_action: false"],
                        accent=TERRA, min_w=5.4, fs=19, title_fs=22)

        body = fit_src(VGroup(ladder, reasons).arrange(RIGHT, buff=0.95))
        bar.move_to(links[2].get_center())
        src = source_line("logs/gate-decisions/market-sentiment-analysis-part-1-gate-5.json")

        self.play(*[Create(c[0]) for c in chips], run_time=1.3)
        self.play(*[FadeIn(c[1]) for c in chips],
                  *[Create(l) for l in links], run_time=1.5)
        self.wait(1.4)
        self.play(Create(bar), run_time=1.2)
        self.wait(0.7)
        self.play(Create(reasons[0]), run_time=1.0)
        self.play(FadeIn(reasons[1]), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("A run that never happened, a clearance that was refused")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(2.6)


class B08_NineDefects(Scene):
    """FALSIFIABILITY: nine broke during testing -- two were last week's gates. 22.21s."""

    def construct(self):
        page(self)
        head = kicker("BROKE DURING TESTING, FIXED",
                      "nine of them \u00b7 two were the gates from episode 5")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        col_a = ["python3 resolved to a Store alias stub",
                 "write_text emitted CRLF on Windows",
                 ".gitattributes scoped too narrowly",
                 "news dedupe short-circuited",
                 "\"yesterday\" double-flagged"]
        col_b = ["step 5 claimed raw_layer_access: none",
                 "step 6 claimed byte-identical reruns"]
        gates = ["gate 4 satisfiable by doing nothing",
                 "gate 5 satisfiable \u2014 fixed TWICE"]

        def rows(labels, color=INK):
            out = []
            for l in labels:
                tk = tick(color)
                t = Text(l, font=MONO, font_size=17, color=INK)
                out.append(VGroup(tk, t).arrange(RIGHT, buff=0.26))
            return out

        ra = rows(col_a)
        rb = rows(col_b)
        rg = rows(gates, TERRA)

        gbody = VGroup(*rg).arrange(DOWN, buff=0.20, aligned_edge=LEFT)
        gbox = RoundedRectangle(width=gbody.width + 0.6, height=gbody.height + 0.6,
                                corner_radius=0.10, stroke_width=1.8,
                                stroke_color=TERRA, fill_opacity=0)
        gbox.move_to(gbody.get_center())
        gpack = VGroup(gbox, gbody)

        right = VGroup(*rb, gpack).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        left = VGroup(*ra).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.70, aligned_edge=UP))
        src = source_line("same file \u00b7 Broke during testing, fixed")

        for r in ra:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=0.60)
        for r in rb:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=0.60)
        self.wait(0.8)
        self.play(Create(gbox), run_time=1.0)
        for r in rg:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=0.85)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.0)

        point = spark("Last week I called that gate fixed")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(5.6)


class B09_Scored(Scene):
    """SUMMARY: the rubric scored, and the five steps VERIFIED would take. 28.41s."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "the three questions, then what VERIFIED would cost")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("WHAT YOU RAN", "17 rows \u00b7 7 adversarial", INK),
              ("WHAT YOU DIDN'T", "10 entries \u00b7 written down", INK),
              ("DID A GATE SAY NO", "yes \u2014 status did not move", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=17)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.34))
        left = VGroup(*qrows).arrange(DOWN, buff=0.40, aligned_edge=LEFT)

        steps = ["1  implement live mode in step 2",
                 "2  a second fixture set: 401/403/429/timeout",
                 "3  reopen gate 5 \u2014 already answered: no",
                 "4  a live run, every gate cleared",
                 "5  a fresh attestation, bound to that version"]
        srows, sboxes = [], []
        for i, s in enumerate(steps):
            colour = TERRA if i == 2 else INK_SOFT
            t = Text(s, font=MONO, font_size=17, color=INK)
            box = RoundedRectangle(width=t.width + 0.44, height=0.44, corner_radius=0.08,
                                   stroke_width=1.5, stroke_color=colour, fill_opacity=0)
            box.move_to(t.get_center())
            srows.append(VGroup(box, t))
            sboxes.append(box)
        right = VGroup(*srows).arrange(DOWN, buff=0.20, aligned_edge=LEFT)

        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.80))
        src = source_line("same file \u00b7 What VERIFIED would require, in order")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.5)
            self.wait(0.7)
        self.wait(0.8)
        for r in srows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=0.80)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Step three is a judgment, and it was no")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(6.6)
