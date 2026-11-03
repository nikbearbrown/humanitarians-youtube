"""Manim beats for the reel `mycroft-weekly-it-looked-complete`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 93485c4 on branch feat/gate-records (2026-10-22). Episode 9.

Figures were recounted from the COMMITTED tree with git ls-tree. The `gate`
command WRITES a decision record, so unlike last episode it was never run --
nothing here was produced by executing the subject. The commit's "2 to 32
evidence files" could not be reproduced without running that writer and is
deliberately absent from every frame; the 26 JSON files, which is the figure
that carries the argument, reproduces exactly. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over twelve previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * columns of unequal height are CENTRE-aligned, and a connector between them
    goes in the same arrange -- top-aligning leaves it floating
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
  * _fit scales UP as well as down (FILL-THE-CANVAS)
  * a beat carried by text alone has no shape-state -- give it geometry
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, DashedLine, FadeIn, Line, RoundedRectangle,
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


def tick(color=INK):
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def hollow(size=0.26, color=INK_SOFT, stroke=1.8):
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


def stat(figure, caption_lines, accent=INK, fig_fs=50, cap_fs=18, min_w=4.0):
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


class B01_TwoRecords(Scene):
    """PROBLEM: the machine record beside the hand-written one. 20.67s."""

    def construct(self):
        page(self)
        head = kicker("THE RECORD THE COMMAND WROTE",
                      "93485c4 \u00b7 feat/gate-records")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        machine = panel("written by the command",
                        ["gate, decision, note",
                         "decided_by, decided_at",
                         "recipe, recipe_version"], accent=INK_SOFT, min_w=5.2, fs=18)
        missing = panel("absent",
                        ["evidence_files",
                         "evidence_observed",
                         "mode",
                         "run_log",
                         "scope"], accent=TERRA, min_w=4.6, fs=18)
        hand = panel("written by a human, week 5",
                     ["everything on the left,",
                      "plus the five on the right,",
                      "plus residual_risk with",
                      "the actual specifics"], accent=INK, min_w=5.2, fs=18)

        row = fit_src(VGroup(machine, missing, hand).arrange(RIGHT, buff=0.42))
        src = source_line("five fields absent \u00b7 residual_risk present but a generic default")

        self.play(Create(machine[0]), FadeIn(machine[1]), run_time=1.7)
        self.wait(1.4)
        self.play(Create(hand[0]), FadeIn(hand[1]), run_time=1.9)
        self.wait(1.6)
        self.play(Create(missing[0]), FadeIn(missing[1]), run_time=1.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Not wrong. Thinner.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.5)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 17.88s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY AUDIT RECORD",
                      "ask these before you treat one as evidence")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  DOES IT NAME WHAT\n   IT LOOKED AT?", ["the actual files,", "not a summary"],
                  accent=INK_SOFT),
            panel("2  ABSENT, OR\n   UNKNOWABLE?", ["\u201cnot found\u201d when you mean",
                                                     "\u201ccannot tell\u201d is false,",
                                                     "not incomplete"], accent=TERRA),
            panel("3  IS A DEFAULT\n   VISIBLY A DEFAULT?", ["or does boilerplate read",
                                                             "as someone's judgment"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.6)
            self.wait(1.0)
        self.wait(2.2)

        point = spark("A record is a claim about a check")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.2)


class B04_TheDepthBug(Scene):
    """QUESTION 1: the depth bug and the 26 files it skipped. 22.46s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 DOES IT NAME WHAT IT LOOKED AT?",
                      "the evidence list comes from the gate's own test")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        root = chip("gate 3's test names 2 paths", INK_SOFT, font_size=18, height=0.44)
        dirs = VGroup(
            chip("data/raw/\u2026", INK_SOFT, font_size=17, height=0.40),
            chip("data/verified/\u2026", INK_SOFT, font_size=17, height=0.40),
        ).arrange(RIGHT, buff=0.40)
        stopline = DashedLine(LEFT * 2.6, RIGHT * 2.6, stroke_width=2.2,
                              color=TERRA, dash_length=0.12)
        stoplab = Text("the first version stopped here",
                       font=MONO, font_size=17, color=TERRA)
        grandkids = VGroup(*[hollow(0.20) for _ in range(12)]).arrange(RIGHT, buff=0.13)
        gklab = Text("the files two levels down \u2014 never hashed",
                     font=MONO, font_size=17, color=INK_SOFT)

        tree = VGroup(root, dirs, VGroup(stopline, stoplab).arrange(DOWN, buff=0.10),
                      grandkids, gklab).arrange(DOWN, buff=0.26)
        count = stat("26", ["JSON files", "the gate exists", "to check"], accent=TERRA, min_w=3.8)

        body = fit_src(VGroup(tree, count).arrange(RIGHT, buff=0.70))
        src = source_line("git ls-tree -r 93485c4 \u2014 data/raw + data/verified, 14 + 12 = 26")

        self.play(Create(root[0]), FadeIn(root[1]), run_time=1.1)
        self.play(*[Create(d[0]) for d in dirs], *[FadeIn(d[1]) for d in dirs], run_time=1.2)
        self.play(Create(stopline), FadeIn(stoplab), run_time=1.3)
        self.wait(1.2)
        self.play(*[Create(g) for g in grandkids], run_time=1.4)
        self.play(FadeIn(gklab), run_time=1.1)
        self.wait(1.4)
        self.play(Create(count[0]), FadeIn(count[1]), run_time=1.7)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("It hashed the folders, not the files")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.8)


class B06_AbsentOrUnknowable(Scene):
    """QUESTION 2: the distinction the record now makes. 28.03s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 ABSENT, OR UNKNOWABLE?",
                      "not every token in a test is a file path")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        wrong = panel("exists: false",
                      ["asserts a file is missing",
                       "\u2014 a statement about the world"], accent=INK_SOFT, min_w=6.0, fs=19)
        right = panel("resolved: false  + a note",
                      ["cannot distinguish a loop value",
                       "from a template from a genuinely",
                       "missing file \u2014 a statement about",
                       "what the checker can tell"], accent=TERRA, min_w=6.0, fs=19)

        cases = VGroup(
            chip("gate 4: `for s in tools/verify-provenance \u2026`  \u2014 loop values",
                 INK_SOFT, font_size=17, height=0.42),
            chip("gate 6: names a [DATE] template", INK_SOFT, font_size=17, height=0.42),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        body = fit_src(VGroup(wrong, right, cases).arrange(DOWN, buff=0.34))
        src = source_line("the two real cases in this repo \u00b7 93485c4")

        self.play(Create(wrong[0]), FadeIn(wrong[1]), run_time=1.9)
        self.wait(2.2)
        self.play(Create(right[0]), FadeIn(right[1]), run_time=2.4)
        self.wait(2.4)
        for c in cases:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("A smaller claim, and the true one")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.6)


class B07_ObservedNotAssumed(Scene):
    """QUESTION 3: three fields that became observations. 20.76s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 IS A DEFAULT VISIBLY A DEFAULT?",
                      "three fields that stopped asserting and started observing")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for field, now in [
            ("residual_risk_stated", "marks whether a human supplied one"),
            ("run_log", "looks for a dated entry, records if it exists"),
            ("mode / scope", "read from the run envelope, not assumed"),
        ]:
            f = Text(field, font=MONO, font_size=20, color=INK)
            ch = chip("observed", INK, font_size=17, height=0.38)
            d = Text(now, font=MONO, font_size=18, color=INK_SOFT)
            rows.append(VGroup(f, ch, d).arrange(RIGHT, buff=0.30))
        stack = VGroup(*rows).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        note = Text("so a record can never point at a log entry nobody wrote",
                    font=MONO, font_size=19, color=TERRA)
        body = fit_src(VGroup(stack, note).arrange(DOWN, buff=0.46))
        src = source_line("93485c4 \u00b7 +147 \u22123 in scripts/snickerdoodle.mjs")

        for r in rows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), FadeIn(r[2]),
                      run_time=1.6)
            self.wait(0.8)
        self.play(FadeIn(note), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Boilerplate should look like boilerplate")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.6)


class B08_TheWrongDay(Scene):
    """FALSIFIABILITY: the UTC date bug. 21.38s."""

    def construct(self):
        page(self)
        head = kicker("AND THEN THE DATE",
                      "in a record whose purpose is who decided what, and when")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        decided = stat("22 Oct", ["decided"], accent=INK, min_w=4.4)
        recorded = stat("23 Oct", ["recorded"], accent=TERRA, min_w=4.4)
        link = Line(LEFT * 0.55, RIGHT * 0.55, stroke_width=1.8, color=INK_SOFT)
        pair = VGroup(decided, link, recorded).arrange(RIGHT, buff=0.46)
        cause = chip("toISOString() returns UTC", TERRA, font_size=19, height=0.46)
        note = Text("every other field in this commit is about evidence being real",
                    font=MONO, font_size=19, color=INK)
        body = fit_src(VGroup(pair, cause, note).arrange(DOWN, buff=0.38))
        src = source_line("dates are local now \u00b7 93485c4")

        self.play(Create(decided[0]), FadeIn(decided[1]), run_time=1.4)
        self.play(Create(link), run_time=0.6)
        self.play(Create(recorded[0]), FadeIn(recorded[1]), run_time=1.4)
        self.wait(1.8)
        self.play(Create(cause[0]), FadeIn(cause[1]), run_time=1.5)
        self.wait(1.4)
        self.play(FadeIn(note), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("One day off, in the field that says when")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.6)


class B09_WhatWasVerified(Scene):
    """SUMMARY: the post-change checks, including the unchanged ones. 20.22s."""

    def construct(self):
        page(self)
        head = kicker("VERIFIED AFTER THE CHANGE",
                      "including the half where nothing moved")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        bars = VGroup(*[
            RoundedRectangle(width=0.95, height=h, corner_radius=0.08, stroke_width=2.2,
                             stroke_color=TERRA if i == 2 else INK, fill_opacity=0)
            for i, h in enumerate([0.70, 1.00, 1.65, 0.85, 1.20, 0.75])
        ]).arrange(RIGHT, buff=0.26, aligned_edge=DOWN)
        blab = Text("all six gates produce a DIFFERENT evidence set",
                    font=MONO, font_size=18, color=INK_SOFT)
        gates = VGroup(bars, blab).arrange(DOWN, buff=0.24)

        refusals = []
        for r in ["a failing test", "a live gate without --authorize-live",
                  "a missing note", "an overwrite without --force"]:
            tk = tick(INK)
            t = Text(r, font=MONO, font_size=18, color=INK)
            refusals.append(VGroup(tk, t).arrange(RIGHT, buff=0.26))
        rstack = VGroup(*refusals).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        rlab = Text("the four refusal paths still hold",
                    font=MONO, font_size=18, color=INK_SOFT)
        refuse = VGroup(rlab, rstack).arrange(DOWN, buff=0.20, aligned_edge=LEFT)

        unchanged = panel("and unchanged",
                          ["run and check \u2014 unaffected",
                           "npm run verify \u2014 still passes"],
                          accent=INK_SOFT, min_w=6.4, fs=19, title_fs=21)

        # A tall column beside a short one leaves dead space on both sides, and
        # a narrow panel under a wide row leaves more (measured 47%). Two rows
        # of comparable width fill the frame instead.
        bottom = VGroup(refuse, unchanged).arrange(RIGHT, buff=0.60, aligned_edge=UP)
        body = fit_src(VGroup(gates, bottom).arrange(DOWN, buff=0.42))
        src = source_line("stated in the commit body \u00b7 the gate writer was not run here")

        self.play(*[Create(b) for b in bars], run_time=1.5)
        self.play(FadeIn(blab), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(rlab), run_time=0.8)
        for r in refusals:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=0.70)
        self.wait(0.9)
        self.play(Create(unchanged[0]), FadeIn(unchanged[1]), run_time=1.4)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.0)

        point = spark("Nothing moved is the quiet half")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.4)
