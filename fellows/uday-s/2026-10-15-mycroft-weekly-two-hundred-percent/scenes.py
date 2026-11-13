"""Manim beats for the reel `mycroft-weekly-two-hundred-percent`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ d85106b on branch feat/snickerdoodle-cli (2026-10-15), with
its companion a18d1c1. Episode 8.

Every figure was reproduced by RUNNING the committed checker read-only
(`node scripts/snickerdoodle.mjs check --all`, which only reads and prints) and
by counting the committed tree with git ls-tree / git grep. The working tree has
2108 files showing modified and was not relied on. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over eleven previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * a connector between two top-aligned columns must be centred SEPARATELY
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
  * _fit scales UP as well as down (FILL-THE-CANVAS)
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


def stat(figure, caption_lines, accent=INK, fig_fs=50, cap_fs=18, min_w=3.6):
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


class B01_NeverExisted(Scene):
    """PROBLEM: a command documented 1444 times that was never built. 18.60s."""

    def construct(self):
        page(self)
        head = kicker("THE COMMAND EVERY RECIPE DOCUMENTS",
                      "feat/snickerdoodle-cli \u00b7 a18d1c1, d85106b")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cmd = panel("every recipe ends with this",
                    ["snickerdoodle run <recipe> --step <name>",
                     "snickerdoodle gate <recipe> --gate N \\",
                     "            --decision approve --note \"...\""],
                    accent=INK_SOFT, min_w=7.4, fs=19)
        counts = VGroup(
            stat("1444", ["times written"], accent=INK),
            stat("97", ["recipes"], accent=INK),
        ).arrange(RIGHT, buff=0.42)
        never = chip("the command had never existed", TERRA, font_size=21, height=0.46)

        link = Line(UP * 0.24, DOWN * 0.24, stroke_width=1.8, color=INK_SOFT)
        body = fit(VGroup(cmd, counts, link, never).arrange(DOWN, buff=0.30))

        self.play(Create(cmd[0]), FadeIn(cmd[1]), run_time=2.0)
        self.wait(1.4)
        for c in counts:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.2)
        self.wait(1.0)
        self.play(Create(link), run_time=0.6)
        self.play(Create(never[0]), FadeIn(never[1]), run_time=1.6)
        self.wait(1.8)

        point = spark("The spec was written. Nothing read it.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.9)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the numbers. 19.18s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY PERCENTAGE",
                      "ask these before you believe a share")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT IS THE\n   DENOMINATOR?", ["name the population", "out loud"],
                  accent=INK_SOFT),
            panel("2  COULD EVERY ITEM\n   HAVE BEEN FOUND?", ["or are some sitting",
                                                               "there as silent passes"],
                  accent=TERRA),
            panel("3  ONE DEFECT,\n   OR MANY?", ["a shared template", "is one defect"],
                  accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(1.1)
        self.wait(2.6)

        point = spark("A share without its population is a mood")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.4)


class B04_WhatCheckFound(Scene):
    """OUTPUT: the repo-wide result, reproduced by running the checker. 13.25s."""

    def construct(self):
        page(self)
        head = kicker("WHAT CHECK FOUND", "reproduced by running the committed checker")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        top = VGroup(
            stat("97", ["recipes"], accent=INK_SOFT),
            stat("616", ["findings"], accent=INK),
            stat("94 / 97", ["name scripts", "that do not exist"], accent=INK),
        ).arrange(RIGHT, buff=0.42, aligned_edge=UP)
        zero = stat("0", ["recipes came back clean"], accent=TERRA, min_w=5.4)
        body = fit_src(VGroup(top, zero).arrange(DOWN, buff=0.40))
        src = source_line("node scripts/snickerdoodle.mjs check --all \u00b7 d85106b \u00b7 read-only")

        for c in top:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.1)
        self.wait(0.8)
        self.play(Create(zero[0]), FadeIn(zero[1]), run_time=1.5)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.6)

        point = spark("Zero")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.8)
        self.wait(1.9)


class B05_ThreeDenominators(Scene):
    """HERO BEAT: one numerator, three denominators. 31.33s."""

    def construct(self):
        page(self)
        head = kicker("THE SAME FINDING, THREE DENOMINATORS",
                      "4 recipes advertise a flag no script implements")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows_spec = [
            ("4 / 97", "4%", "out of every recipe", "plausible, and wrong", INK_SOFT),
            ("4 / 2", "200%", "out of recipes with no missing scripts",
             "impossible \u2014 and therefore useful", TERRA),
            ("4 / 4", "100%", "out of recipes with a script to compare", "right", INK),
        ]
        rows, frac_boxes = [], []
        for frac, pct, popn, verdict, colour in rows_spec:
            f = Text(frac, font=MONO, font_size=26, color=colour)
            box = RoundedRectangle(width=f.width + 0.60, height=0.70, corner_radius=0.09,
                                   stroke_width=2.0, stroke_color=colour, fill_opacity=0)
            box.move_to(f.get_center())
            fb = VGroup(box, f)
            p = Text(pct, font=SERIF, font_size=46, color=colour)
            right = VGroup(
                Text(popn, font=MONO, font_size=18, color=INK_SOFT),
                Text(verdict, font=MONO, font_size=18, color=colour),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            rows.append(VGroup(fb, p, right).arrange(RIGHT, buff=0.42))
            frac_boxes.append(box)
        stack = fit_src(VGroup(*rows).arrange(DOWN, buff=0.38, aligned_edge=LEFT))
        src = source_line("the 93 recipes with no scripts on disk could never produce this finding")

        for r in rows:
            self.play(Create(r[0][0]), FadeIn(r[0][1]), run_time=1.1)
            self.play(FadeIn(r[1]), run_time=1.0)
            self.play(FadeIn(r[2]), run_time=1.3)
            self.wait(1.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.6)

        point = spark("An impossible number is a gift")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(7.2)


class B07_OneDefectOrMany(Scene):
    """QUESTION 3: the same 94, read two ways. 18.03s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 ONE DEFECT, OR NINETY-FOUR?",
                      "94 recipes name a script that does not exist")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        squares = VGroup(*[hollow(0.22) for _ in range(94)])
        squares.arrange_in_grid(rows=7, cols=14, buff=0.11)

        parent = hollow(0.40, TERRA, stroke=2.4)

        read_a = Text("read as 94 defects          \u2192  a quarter's work",
                      font=MONO, font_size=20, color=INK_SOFT)
        read_b = Text("read as 1 template defect   \u2192  an afternoon",
                      font=MONO, font_size=20, color=TERRA)

        col = VGroup(parent, squares, read_a, read_b).arrange(DOWN, buff=0.26)
        # the connectors are built AFTER the arrange so they span the real gap,
        # then folded into the group before fitting
        links = VGroup(*[
            Line(parent.get_bottom(),
                 squares[i].get_top(), stroke_width=1.2, color=TERRA)
            for i in (0, 3, 6, 9, 12, 13)])
        body = fit_src(VGroup(col, links))
        src = source_line("they all inherit one template \u00b7 fix it there and it closes everywhere")

        self.play(*[Create(s) for s in squares], run_time=2.0)
        self.play(FadeIn(read_a), run_time=1.2)
        self.wait(1.8)
        self.play(Create(parent), run_time=1.0)
        self.play(*[Create(l) for l in links], run_time=1.2)
        self.play(FadeIn(read_b), run_time=1.3)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(1.8)

        point = spark("Ninety-four copies of one mistake")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.1)


class B08_TheRecount(Scene):
    """FALSIFIABILITY: every figure reproduced, and 99 vs 97 reconciled. 29.86s."""

    def construct(self):
        page(self)
        head = kicker("THE RECOUNT", "the committed checker, run read-only")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        claims = [("97 recipes", "97"),
                  ("616 findings", "616"),
                  ("94 of 97 missing scripts", "94"),
                  ("flag findings 4 of 4", "100%")]
        rows = []
        for claim, got in claims:
            m = tick(INK)
            a = Text(claim, font=MONO, font_size=19, color=INK)
            b = Text(got, font=SERIF, font_size=25, color=INK)
            rows.append(VGroup(m, a, b).arrange(RIGHT, buff=0.32))
        stack = VGroup(*rows).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        recon = panel("and last week said 99",
                      ["99 .md files under recipes/",
                       "97 carry the snickerdoodle",
                       "contract \u2014 1444 occurrences",
                       "both counts were right"], accent=TERRA, min_w=5.8, fs=18,
                      title_fs=21)

        body = fit_src(VGroup(stack, recon).arrange(RIGHT, buff=0.70))
        src = source_line("git grep -c \u00b7 git ls-tree -r d85106b \u00b7 nothing written to the repo")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=1.2)
            self.wait(0.5)
        self.wait(1.6)
        self.play(Create(recon[0]), FadeIn(recon[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.8)

        point = spark("Counting different things, both correctly")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.4)


class B09_WhatTheCliRefuses(Scene):
    """SUMMARY: the gate's refusals, and the false-failure bug. 30.22s."""

    def construct(self):
        page(self)
        head = kicker("THE COMMAND IT BUILT",
                      "extracted from the recipes, not invented")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        refuses = panel("gate refuses to",
                        ["approve when the test fails",
                         "record a decision with no note",
                         "overwrite without --force",
                         "act without a named human",
                         "touch live without --authorize-live"],
                        accent=INK, min_w=6.2, fs=19)
        bug = panel("and one bug worth the commit",
                    ["gate tests are POSIX shell",
                     "Windows ran them under cmd.exe",
                     "gate 3 reported a FAILURE",
                     "for a test that passes"],
                    accent=TERRA, min_w=6.2, fs=19)

        body = fit_src(VGroup(refuses, bug).arrange(RIGHT, buff=0.60, aligned_edge=UP))
        src = source_line("a18d1c1 \u00b7 snickerdoodle: build the CLI 97 recipes already document")

        self.play(Create(refuses[0]), run_time=1.2)
        self.play(FadeIn(refuses[1]), run_time=2.6)
        self.wait(2.6)
        self.play(Create(bug[0]), run_time=1.2)
        self.play(FadeIn(bug[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.8)

        point = spark("A false failure, written down as evidence")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(7.8)
