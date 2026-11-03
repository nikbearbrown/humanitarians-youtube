"""Manim beats for the reel `mycroft-weekly-it-never-says-pass`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ aa0c0fe (2026-09-17), branch
feature/market-sentiment-human-report. Episode 4 — the six-step arc closes.
Every figure came from a live run of step 6, not the commit message.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over five previous reels:
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
    """A drawn check mark. Sits BESIDE a label, never across it."""
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


class B01_LedgerCloses(Scene):
    """PROBLEM: the six-step ledger, the last row closing. 14.12s."""

    STEPS = [
        ("1", "verify-provenance", True),
        ("2", "ingest-inputs", True),
        ("3", "validate-data-shape", True),
        ("4", "transform-quality-check", True),
        ("5", "run-approved-tools", True),
        ("6", "produce-human-report", False),
    ]

    def construct(self):
        page(self)
        head = kicker("THE RECIPE", "six declared steps · episode 4")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows, closing = VGroup(), None
        for num, name, done in self.STEPS:
            color = INK if done else TERRA
            n = Text(num, font=SERIF, font_size=30, color=INK_SOFT)
            box = RoundedRectangle(width=0.34, height=0.34, corner_radius=0.06,
                                   stroke_width=2.0, stroke_color=color, fill_opacity=0)
            label = Text(name, font=MONO, font_size=26, color=color)
            box.next_to(n, RIGHT, buff=0.38)
            label.next_to(box, RIGHT, buff=0.38)
            row = VGroup(n, box, label)
            if done:
                row.add(tick(INK).move_to(box.get_center()))
            else:
                closing = row
            rows.add(row)
        rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        fit(rows)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.25) for r in rows],
                              lag_ratio=0.28), run_time=2.6)
        self.wait(1.2)

        mark = tick(INK).move_to(closing[1].get_center())
        self.play(closing[1].animate.set_stroke(INK), closing[2].animate.set_color(INK),
                  Create(mark), run_time=2.2)
        self.wait(1.0)

        point = spark("Six of six")
        self.play(Write(point), run_time=1.7)
        self.wait(3.52)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: three questions for any automated report. 14.38s."""

    QS = [
        ("1", "WHAT A RECORD\nSUPPORTS", "counts, hashes,\nlocators"),
        ("2", "WHAT YOU\nINFERRED", "arithmetic, a model,\na judgment"),
        ("3", "WHO\nDECIDES", "the machine, or a\nnamed human?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS", "ask these of any automated report")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.QS:
            n = Text(num, font=SERIF, font_size=32, color=TERRA)
            t = Text(title, font=SANS, font_size=25, color=INK, line_spacing=0.7)
            b = Text(body, font=MONO, font_size=19, color=INK_SOFT, line_spacing=0.7)
            hr = VGroup(n, t).arrange(RIGHT, buff=0.28, aligned_edge=UP)
            inner = VGroup(hr, b).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.8, height=inner.height + 0.8,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.42))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=0.95)
            self.wait(1.05)

        point = spark("Most tools blur 1 and 2, then answer 3 themselves")
        self.play(Write(point), run_time=2.0)
        self.wait(3.48)


class B05_VerifiedInferred(Scene):
    """OUTPUT 1: the findings split — and where the 64 lands. 21.01s."""

    def construct(self):
        page(self)
        head = kicker("STEP 6 — THE FINDINGS SPLIT", "defective set · live run")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        ver = panel("VERIFIED  ·  10", [
            "rows seen / promoted / withheld",
            "envelope declared 7, holds 8",
            "defect locators · file hashes",
        ], INK_SOFT, min_w=5.4)
        inf = panel("INFERRED  ·  5", [
            "overall sentiment 64/100",
            "news 67 · social 67 · price 60",
            "4 flagged rows fed the score",
        ], TERRA, min_w=5.4)
        pair = VGroup(ver, inf).arrange(RIGHT, buff=0.85, aligned_edge=UP)

        note = Text("last episode's 64 is not a verified finding",
                    font=SANS, font_size=25, color=TERRA)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.6))
        src = source_line("live run · produce-human-report.py --fixture-set defective")

        self.play(Create(ver[0]), FadeIn(ver[1][0]), run_time=1.5)
        for line in ver[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.85)
        self.wait(0.9)
        self.play(Create(inf[0]), FadeIn(inf[1][0]), run_time=1.5)
        for line in inf[1][1]:
            self.play(FadeIn(line, shift=RIGHT * 0.18), run_time=0.85)
        self.wait(1.2)
        self.play(Write(note), run_time=2.1)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.0)

        point = spark("Evidence on the left. Arithmetic on the right.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.7)
        self.wait(3.36)


class B08_SixGates(Scene):
    """OUTPUT 2: the centrepiece — six gates, none passed. 18.90s."""

    def construct(self):
        page(self)
        head = kicker("THE GATES", "what the report says about each one")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        counts = VGroup(
            chip("15 / 15 sections", INK_SOFT, font_size=21, pad=0.4, height=0.46),
            chip("16 / 16 log fields", INK_SOFT, font_size=21, pad=0.4, height=0.46),
        ).arrange(RIGHT, buff=0.5)

        gates = VGroup()
        for i in range(1, 7):
            g = Text(f"gate {i}", font=MONO, font_size=21, color=INK)
            st = chip("evidence recorded; awaiting a named human", TERRA,
                      font_size=18, pad=0.34, height=0.38)
            gates.add(VGroup(g, st))
        lw = max(r[0].width for r in gates)
        for r in gates:
            r[1].next_to(r[0], RIGHT, buff=0.5 + (lw - r[0].width))
        gates.arrange(DOWN, buff=0.17, aligned_edge=LEFT)

        body = fit_src(VGroup(counts, gates).arrange(DOWN, buff=0.5))
        src = source_line("live run · gate_results · cleared_by: null on all six")

        self.play(LaggedStart(*[Create(c[0]) for c in counts],
                              *[FadeIn(c[1]) for c in counts], lag_ratio=0.3),
                  run_time=1.6)
        self.wait(0.8)
        for r in gates:
            self.play(FadeIn(r[0], shift=RIGHT * 0.15), Create(r[1][0]), FadeIn(r[1][1]),
                      run_time=0.72)
        self.wait(1.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(0.9)

        point = spark("Not one marked passed")
        self.play(Write(point), run_time=1.8)
        self.wait(4.58)


class B09_GateFour(Scene):
    """FALSIFIABILITY: a gate that cannot fail. 28.39s."""

    def construct(self):
        page(self)
        head = kicker("THE ONE IT CAUGHT ON ITSELF", "gate 4 · script-readiness")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cond = Text("\"Every step script exists  OR  is represented\nby a typed development TODO.\"",
                    font=MONO, font_size=23, color=INK, line_spacing=0.8)
        cond_box = RoundedRectangle(width=cond.width + 1.0, height=cond.height + 0.7,
                                    corner_radius=0.12, stroke_width=1.8,
                                    stroke_color=INK_SOFT, fill_opacity=0)
        cond_box.move_to(cond.get_center())
        condition = VGroup(cond_box, cond)

        left = panel("the script exists", ["TRUE"], TERRA, min_w=4.4, fs=24)
        right = panel("the TODO is still in the recipe", ["TRUE"], TERRA, min_w=4.4, fs=24)
        branches = VGroup(left, right).arrange(RIGHT, buff=0.85, aligned_edge=UP)

        verdict = Text("satisfiable by doing nothing", font=SANS, font_size=27, color=TERRA)
        body = fit_src(VGroup(condition, branches, verdict).arrange(DOWN, buff=0.5))
        src = source_line("live run · gate_results[3].note, verbatim")

        self.play(Create(cond_box), FadeIn(cond), run_time=2.2)
        self.wait(1.8)
        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.6)
        self.wait(1.0)
        self.play(Create(right[0]), FadeIn(right[1]), run_time=1.6)
        self.wait(1.4)
        self.play(Write(verdict), run_time=2.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.2)

        point = spark("A gate with nothing to fail")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(9.89)


class B10_SeriesLedger(Scene):
    """SUMMARY: the arc closes — done versus deliberately open. 18.11s."""

    DONE = ["6 of 6 steps written", "runs on both fixture sets",
            "all six gate tests check out", "report + audit byte-identical"]
    OPEN = ["gate 5 unapproved — live execution blocked",
            "9 typed TODOs carried forward",
            "a reader mismatch, logged not hidden"]

    def construct(self):
        page(self)
        head = kicker("THE ARC", "mycroft · commit aa0c0fe")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(title, items, color):
            t = Text(title, font=SANS, font_size=25, color=INK_SOFT)
            body = VGroup(*[Text(i, font=MONO, font_size=21, color=color)
                            for i in items])
            body.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
            rule = Line(LEFT * (max(body.width, t.width) / 2),
                        RIGHT * (max(body.width, t.width) / 2),
                        stroke_width=1.3, color=INK_SOFT)
            col = VGroup(t, rule, body).arrange(DOWN, buff=0.26)
            for part in (t, rule, body):
                part.align_to(col, LEFT)
            return col

        left = column("COMPLETE", self.DONE, INK)
        right = column("DELIBERATELY OPEN", self.OPEN, TERRA)
        fit(VGroup(left, right).arrange(RIGHT, buff=1.3, aligned_edge=UP))

        self.play(FadeIn(left, shift=UP * 0.2), run_time=1.7)
        self.wait(1.7)
        self.play(FadeIn(right, shift=UP * 0.2), run_time=1.7)
        self.wait(1.5)

        point = spark("Finished is not the same as decided")
        self.play(Write(point), run_time=2.0)
        self.wait(6.61)
