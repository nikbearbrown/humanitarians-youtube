"""Manim beats for the reel `mycroft-weekly-the-lucky-case`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 0358ab9 on branch chore/recipe-lifecycle-frontmatter
(2026-11-05). Episode 11.

Verification, all read-only: the checker was RUN (`check` reads and prints;
`gate` writes and was not run); the tree was counted with git; and B05's
argparse behaviour was reproduced in a STANDALONE interpreter with nothing from
the repository executed. See FACTCHECK.md.

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
    DOWN, LEFT, RIGHT, UP, Arrow, Create, FadeIn, Line, RoundedRectangle, Scene,
    Text, VGroup,
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


class B01_NotDocumentation(Scene):
    """PROBLEM: a table column the runner executes. 17.51s."""

    def construct(self):
        page(self)
        head = kicker("A COLUMN THAT LOOKS LIKE DOCUMENTATION",
                      "0358ab9 \u00b7 chore/recipe-lifecycle-frontmatter")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cell = panel("the recipe's Flags cell",
                     ["| validate-data-shape |",
                      "|   --sample --no-write |"], accent=TERRA, min_w=5.6, fs=19, title_fs=21)
        built = panel("what the runner builds",
                      ["python3 <script> \\",
                       "    --sample --no-write"], accent=INK_SOFT, min_w=5.6, fs=19, title_fs=21)
        arrow = Arrow(LEFT * 0.34, RIGHT * 0.34, buff=0, stroke_width=3.0,
                      max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
        pair = VGroup(cell, arrow, built).arrange(RIGHT, buff=0.42)
        note = Text("not documentation \u2014 an argument list",
                    font=SANS, font_size=24, color=INK)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.46))
        src = source_line("a flag the recipe advertises and the script lacks is a live failure")

        self.play(Create(cell[0]), FadeIn(cell[1]), run_time=1.9)
        self.wait(1.2)
        self.play(Create(arrow), run_time=0.7)
        self.play(Create(built[0]), FadeIn(built[1]), run_time=1.8)
        self.wait(1.4)
        self.play(FadeIn(note), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Prose that gets parsed is not prose")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.0)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 15.74s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR A FIELD A PROGRAM READS",
                      "ask these of anything a human writes and software parses")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  IS IT READ\n   BY A MACHINE?", ["prose that is parsed", "stops being prose"],
                  accent=INK_SOFT),
            panel("2  CRASH, OR\n   SOMETHING WORSE?", ["a loud failure", "is the gift"],
                  accent=TERRA),
            panel("3  WHAT DOES THE\n   FIX INVALIDATE?", ["an edit can void a", "record that was true",
                                                           "of the old version"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.8)
        self.wait(1.6)

        point = spark("The quiet failure is the expensive one")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.4)


class B05_BothCases(Scene):
    """HERO BEAT: both argparse outcomes, reproduced standalone. 21.63s."""

    def construct(self):
        page(self)
        head = kicker("WHAT ARGPARSE DOES WITH A PREFIX",
                      "reproduced standalone \u2014 nothing from the repo was run")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        lucky = panel("CASE A \u2014 the prefix alone",
                      ["$ step --sample",
                       "error: argument --sample-dir:",
                       "       expected one argument"],
                      accent=INK_SOFT, min_w=7.0, fs=19, title_fs=22)
        lucky_tag = chip("loud. you find out immediately.", INK_SOFT, font_size=18, height=0.42)

        bad = panel("CASE B \u2014 the prefix, then a word",
                    ["$ step --sample data/real.json",
                     "sample_dir = 'data/real.json'",
                     "input      =  None"],
                    accent=TERRA, min_w=7.0, fs=19, title_fs=22)
        bad_tag = chip("no error. the run proceeds on nothing.", TERRA, font_size=18, height=0.42)

        body = fit_src(VGroup(VGroup(lucky, lucky_tag).arrange(DOWN, buff=0.20),
                              VGroup(bad, bad_tag).arrange(DOWN, buff=0.20)
                              ).arrange(DOWN, buff=0.40))
        src = source_line("python3 argparse, standalone \u00b7 the error text matches the commit exactly")

        self.play(Create(lucky[0]), FadeIn(lucky[1]), run_time=2.0)
        self.play(Create(lucky_tag[0]), FadeIn(lucky_tag[1]), run_time=1.1)
        self.wait(1.8)
        self.play(Create(bad[0]), FadeIn(bad[1]), run_time=2.2)
        self.play(Create(bad_tag[0]), FadeIn(bad_tag[1]), run_time=1.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("The crash was the lucky one")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.4)


class B06_NeverIntent(Scene):
    """QUESTION 1: the column was boilerplate, and the 1:1 fix. 27.32s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 WAS IT EVER AUTHORED INTENT?",
                      "all six built recipes carried the identical pair")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        six = VGroup(*[chip("--sample --no-write", INK_SOFT, font_size=16, height=0.38)
                       for _ in range(6)]).arrange(DOWN, buff=0.14)
        slab = Text("six built recipes \u2014 whatever was actually built",
                    font=MONO, font_size=18, color=INK_SOFT)
        left = VGroup(six, slab).arrange(DOWN, buff=0.24)

        fix = VGroup(
            stat("24", ["rows removed"], accent=INK_SOFT, min_w=3.4),
            stat("24", ["rows added"], accent=INK, min_w=3.4),
        ).arrange(DOWN, buff=0.26)
        onefor = chip("one for one \u2014 none added, none dropped", TERRA,
                      font_size=18, height=0.44)
        leave = Text("unbuilt steps untouched \u2014 there it is still a spec",
                     font=MONO, font_size=18, color=INK_SOFT)
        right = VGroup(fix, onefor, leave).arrange(DOWN, buff=0.24)

        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.64))
        src = source_line("git show --unified=0 0358ab9 -- recipes/ \u00b7 24 added, 24 removed")

        self.play(*[Create(c[0]) for c in six], run_time=1.5)
        self.play(*[FadeIn(c[1]) for c in six], run_time=1.4)
        self.play(FadeIn(slab), run_time=1.1)
        self.wait(2.2)
        for f in fix:
            self.play(Create(f[0]), FadeIn(f[1]), run_time=1.4)
        self.play(Create(onefor[0]), FadeIn(onefor[1]), run_time=1.5)
        self.wait(1.6)
        self.play(FadeIn(leave), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.8)

        point = spark("Boilerplate nobody had edited")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.0)


class B07_TheRightList(Scene):
    """the safety check, and matching the right population. 25.59s."""

    def construct(self):
        page(self)
        head = kicker("COULD A SAMPLE RUN HAVE BECOME A LIVE ONE?",
                      "the check before dropping the flag")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        good = stat("0", ["of the 70 built scripts", "import a network library"],
                    accent=TERRA, min_w=5.4)
        other = stat("9", ["repo-wide \u2014 and none of", "them is among the 70"],
                     accent=INK_SOFT, min_w=5.4)
        pair = VGroup(good, other).arrange(RIGHT, buff=0.56, aligned_edge=UP)

        lesson = panel("the same distinction as last week",
                       ["a grep over the folder answers",
                        "a different question than a grep",
                        "over the list that matters"],
                       accent=INK_SOFT, min_w=6.4, fs=19, title_fs=21)
        body = fit_src(VGroup(pair, lesson).arrange(DOWN, buff=0.44))
        src = source_line("the 6 built recipes name 82 scripts; 70 exist on disk; 0 reach the network")

        self.play(Create(good[0]), FadeIn(good[1]), run_time=1.8)
        self.wait(1.8)
        self.play(Create(other[0]), FadeIn(other[1]), run_time=1.8)
        self.wait(2.0)
        self.play(Create(lesson[0]), FadeIn(lesson[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.8)

        point = spark("Checked the right list, first time")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.2)


class B08_TheLoopCloses(Scene):
    """QUESTION 3: the attestation voids itself, as episode 6 said. 32.02s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 WHAT DOES THE FIX INVALIDATE?",
                      "a rule this series put on screen five episodes ago")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rule = panel("written in episode 6",
                     ["\u201cany edit to the recipe or its",
                      "scripts voids this attestation\u201d",
                      "\u2014 its own point 5"], accent=INK_SOFT, min_w=6.2, fs=19, title_fs=21)
        now = panel("and this week, the edit",
                    ["attestation:   null",
                     "recipe_version: 0.2.1",
                     "the v0.2.0 record kept in full,",
                     "with the voiding appended"], accent=TERRA, min_w=6.2, fs=19, title_fs=21)
        pair = VGroup(rule, now).arrange(RIGHT, buff=0.56, aligned_edge=UP)

        chain = Text("editing the recipe changed its SHA-256 \u2014 the report cites that hash "
                     "as the head of its trace chain, so both were regenerated",
                     font=MONO, font_size=18, color=INK)
        body = fit_src(VGroup(pair, chain).arrange(DOWN, buff=0.44))
        src = source_line("recipes/market-sentiment-analysis-part-1.md \u00b7 frontmatter at 0358ab9")

        self.play(Create(rule[0]), FadeIn(rule[1]), run_time=2.4)
        self.wait(2.4)
        self.play(Create(now[0]), FadeIn(now[1]), run_time=2.6)
        self.wait(2.6)
        self.play(FadeIn(chain), run_time=2.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("The rule fired on schedule")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(9.2)


class B09_EightyFiveToFive(Scene):
    """SUMMARY: the result, reproduced read-only. 18.33s."""

    def construct(self):
        page(self)
        head = kicker("THE RESULT", "reproduced by running the checker, read-only")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = stat("85", ["defects before"], accent=INK_SOFT, min_w=3.8)
        arrow = Arrow(LEFT * 0.26, RIGHT * 0.26, buff=0, stroke_width=3.0,
                      max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
        b = stat("5", ["defects after"], accent=TERRA, min_w=3.8)
        chain = VGroup(a, arrow, b).arrange(RIGHT, buff=0.34)

        where = panel("and all five in one recipe",
                      ["recipes/gru.md",
                       "2 gates with no testable condition",
                       "2 gates naming no human capacity",
                       "and it declares no steps at all"],
                      accent=INK_SOFT, min_w=6.4, fs=18, title_fs=21)
        clean = chip("96 of 97 recipes now contradict nothing they claim",
                     INK, font_size=19, height=0.46)
        body = fit_src(VGroup(chain, where, clean).arrange(DOWN, buff=0.34))
        src = source_line("node scripts/snickerdoodle.mjs check --all \u00b7 and check gru")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=1.3)
        self.play(Create(arrow), run_time=0.6)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=1.3)
        self.wait(1.2)
        self.play(Create(where[0]), FadeIn(where[1]), run_time=2.4)
        self.wait(1.4)
        self.play(Create(clean[0]), FadeIn(clean[1]), run_time=1.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.0)

        point = spark("Five left, and they are all in one file")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.4)
