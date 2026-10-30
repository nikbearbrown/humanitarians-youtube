"""Manim beats for the reel `mycroft-weekly-unbuilt-is-not-broken`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 6428457 on branch chore/recipe-lifecycle-frontmatter
(2026-10-30), with companions 83793ff and 0536907. Episode 10.

Figures were obtained two ways, both read-only: by RUNNING the committed checker
(`check` reads and prints; it does not write, unlike `gate`), and by counting
the committed tree with git. The pure-prepend claim is verified independently
from the diff structure itself. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over thirteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * a cross sits BESIDE the thing it negates, never drawn through text
  * compose every label INTO the fitted group before fitting
  * columns of unequal height are CENTRE-aligned, connector in the same arrange
  * a WIDE and SHORT group is width-limited: fit() cannot scale it up, and the
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


def tick(color=INK):
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def cross(color=TERRA):
    """Sits BESIDE the figure it negates. Never drawn through text."""
    return VGroup(
        Line([-0.09, 0.09, 0], [0.09, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.09, -0.09, 0], [0.09, 0.09, 0], stroke_width=3.2, color=color),
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


class B01_SevenTwentyFive(Scene):
    """PROBLEM: the headline number, and what was actually in it. 19.69s."""

    def construct(self):
        page(self)
        head = kicker("THE NUMBER THAT WAS BEING QUOTED",
                      "chore/recipe-lifecycle-frontmatter \u00b7 6428457")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        top = stat("725", ["findings"], accent=INK_SOFT, min_w=4.0)
        fork = VGroup(
            Line(UP * 0.22, DOWN * 0.22, stroke_width=1.8, color=INK_SOFT),
        )
        unbuilt = panel("554 of them",
                        ["\u201cthis step has no script\u201d",
                         "in recipes marked DRAFT \u2014",
                         "unbuilt work, correctly described"],
                        accent=INK_SOFT, min_w=5.8, fs=18, title_fs=22)
        real = panel("171 of them",
                     ["contradicted something",
                      "the recipe actually claims"],
                     accent=TERRA, min_w=5.0, fs=18, title_fs=22)
        split = VGroup(unbuilt, real).arrange(RIGHT, buff=0.46, aligned_edge=UP)
        body = fit_src(VGroup(top, fork, split).arrange(DOWN, buff=0.30))
        src = source_line("a DRAFT recipe whose scripts do not exist is not broken \u2014 it is a draft")

        self.play(Create(top[0]), FadeIn(top[1]), run_time=1.5)
        self.wait(1.4)
        self.play(Create(fork), run_time=0.6)
        self.play(Create(unbuilt[0]), FadeIn(unbuilt[1]), run_time=2.0)
        self.wait(1.6)
        self.play(Create(real[0]), FadeIn(real[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Most of it was not a defect")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.6)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 17.00s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY COUNT OF PROBLEMS",
                      "ask these before you quote the number")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  DOES IT CONTRADICT\n   A CLAIM?", ["if nothing was claimed,", "nothing can be wrong"],
                  accent=INK_SOFT),
            panel("2  WHICH LIST DID YOU\n   MATCH AGAINST?", ["the specific one,", "or anything that",
                                                               "looked similar"], accent=TERRA),
            panel("3  DID THE GUARD\n   EVER FIRE?", ["a check that never", "triggers proves nothing",
                                                      "on its own"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.6)
            self.wait(0.9)
        self.wait(1.8)

        point = spark("Wrong, or merely unfinished")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.8)


class B04_TwoReductions(Scene):
    """QUESTION 1: 725 to 171 to 80, reproduced by running the checker. 20.27s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 DOES IT CONTRADICT A CLAIM?",
                      "reproduced by running the committed checker, read-only")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            stat("725", ["every finding"], accent=INK_SOFT),
            stat("171", ["actual defects", "after severity"], accent=INK),
            stat("80", ["after the 91 got", "their status"], accent=TERRA),
        ]
        arrows = [Arrow(LEFT * 0.26, RIGHT * 0.26, buff=0, stroke_width=3.0,
                        max_tip_length_to_length_ratio=0.35, color=INK_SOFT)
                  for _ in range(2)]
        chain = VGroup(cards[0], arrows[0], cards[1], arrows[1], cards[2]).arrange(RIGHT, buff=0.26)

        clean_x = cross(TERRA)
        clean_old = Text("0", font=SERIF, font_size=34, color=INK_SOFT)
        clean_new = Text("90 recipes now have no defects at all",
                         font=MONO, font_size=20, color=INK)
        clean = VGroup(clean_x, clean_old, clean_new).arrange(RIGHT, buff=0.26)

        body = fit_src(VGroup(chain, clean).arrange(DOWN, buff=0.52))
        src = source_line("node scripts/snickerdoodle.mjs check --all \u00b7 6428457 \u00b7 97 recipes")

        self.play(Create(cards[0][0]), FadeIn(cards[0][1]), run_time=1.3)
        for i in (1, 2):
            self.play(Create(arrows[i - 1]), run_time=0.6)
            self.play(Create(cards[i][0]), FadeIn(cards[i][1]), run_time=1.4)
            self.wait(0.8)
        self.wait(1.0)
        self.play(Create(clean_x), FadeIn(clean_old), FadeIn(clean_new), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Name the unbuilt. Count the wrong.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.9)


class B05_TheSurveyThatSaid42(Scene):
    """HERO BEAT: one question, two lists, two answers. 29.73s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 WHICH LIST DID YOU MATCH AGAINST?",
                      "do any of the 91 actually have working scripts?")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for query, answer, note, colour in [
            ("any scripts/ path the recipe mentions", "42",
             "includes legacy node scaffolds \u2014 74 lines, and they do nothing", INK_SOFT),
            ("the six canonical steps in Script Locations", "0",
             "all 91 \u2014 so DRAFT is measured, not assumed", TERRA),
        ]:
            q = Text(query, font=MONO, font_size=20, color=INK)
            a = Text(answer, font=SERIF, font_size=46, color=colour)
            n = Text(note, font=MONO, font_size=17, color=INK_SOFT)
            inner = VGroup(VGroup(q, a).arrange(RIGHT, buff=0.44), n)
            inner.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            box = RoundedRectangle(width=inner.width + 0.72, height=inner.height + 0.56,
                                   corner_radius=0.11, stroke_width=1.9,
                                   stroke_color=colour, fill_opacity=0)
            box.move_to(inner.get_center())
            rows.append(VGroup(box, inner))
        stack = VGroup(*rows).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        warn = Text("half the batch would have been mislabelled",
                    font=SANS, font_size=23, color=TERRA)
        body = fit_src(VGroup(stack, warn).arrange(DOWN, buff=0.40))
        src = source_line("the same question, asked of two different lists")

        self.play(Create(rows[0][0]), run_time=1.2)
        self.play(FadeIn(rows[0][1]), run_time=1.8)
        self.wait(2.6)
        self.play(Create(rows[1][0]), run_time=1.2)
        self.play(FadeIn(rows[1][1]), run_time=1.8)
        self.wait(2.4)
        self.play(FadeIn(warn), run_time=1.8)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("A file existing is not the thing existing")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)


class B07_TheGuardThatNeverFired(Scene):
    """QUESTION 3: when a silent guard is evidence. 21.01s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 DID THE GUARD EVER FIRE?",
                      "the generator refuses to stamp DRAFT on a built recipe")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        guard = panel("the refusal",
                      ["if a recipe has canonical",
                       "scripts on disk, the generator",
                       "stops instead of writing DRAFT"],
                      accent=INK_SOFT, min_w=6.0, fs=19)
        fired = chip("fired 0 times across 91", INK_SOFT, font_size=19, height=0.46)
        left = VGroup(guard, fired).arrange(DOWN, buff=0.28)

        why = panel("and why that counts here",
                    ["a guard that never triggers",
                     "is usually worth nothing \u2014",
                     "the 42 survey is what proves",
                     "it could have fired"],
                    accent=TERRA, min_w=5.8, fs=19)

        body = fit_src(VGroup(left, why).arrange(RIGHT, buff=0.62))
        src = source_line("6428457 \u00b7 the refusal never fired, which is the point")

        self.play(Create(guard[0]), FadeIn(guard[1]), run_time=2.2)
        self.wait(1.2)
        self.play(Create(fired[0]), FadeIn(fired[1]), run_time=1.4)
        self.wait(1.6)
        self.play(Create(why[0]), FadeIn(why[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("Silence is evidence only if it could have spoken")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.1)


class B08_IDidItToo(Scene):
    """FALSIFIABILITY: my own fact-check made the same error. 21.61s."""

    def construct(self):
        page(self)
        head = kicker("AND I MADE THE SAME MISTAKE",
                      "while fact-checking this episode")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = []
        for label, value, colour in [
            ("my grep over recipes/", "98", INK_SOFT),
            ("the checker", "97", INK),
        ]:
            t = Text(label, font=MONO, font_size=21, color=INK)
            v = Text(value, font=SERIF, font_size=40, color=colour)
            inner = VGroup(t, v).arrange(RIGHT, buff=0.40)
            # The beat compares two counts, so they should LOOK like two
            # compared things. Bare text here measured 53% fill.
            box = RoundedRectangle(width=inner.width + 0.70, height=inner.height + 0.46,
                                   corner_radius=0.10, stroke_width=1.9,
                                   stroke_color=colour, fill_opacity=0)
            box.move_to(inner.get_center())
            rows.append(VGroup(box, inner))
        stack = VGroup(*rows).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        culprit = chip("recipes/vendor-intelligence-brief.yaml \u2014 not a recipe",
                       TERRA, font_size=18, height=0.46)
        same = Text("the same error as the 42 \u2014 matching a folder, not a list",
                    font=SANS, font_size=23, color=TERRA)

        body = fit_src(VGroup(stack, culprit, same).arrange(DOWN, buff=0.36))
        src = source_line("git grep -l '^status:' -- recipes/ matches .yaml too")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.5)
            self.wait(1.0)
        self.wait(1.0)
        self.play(Create(culprit[0]), FadeIn(culprit[1]), run_time=1.8)
        self.wait(1.3)
        self.play(FadeIn(same), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.2)

        point = spark("Same week. Same shape.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.5)


class B09_PurePrepend(Scene):
    """SUMMARY: the prepend verified from the diff, and the two-high todos. 30.22s."""

    def construct(self):
        page(self)
        head = kicker("VERIFIED FROM THE DIFF ITSELF",
                      "the claim: nothing below line one changed")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        facts = []
        for f in ["91 files changed",
                  "728 insertions",
                  "0 deletions, anywhere",
                  "every hunk:  @@ -0,0 +1,8 @@"]:
            tk = tick(INK)
            t = Text(f, font=MONO, font_size=20, color=INK)
            facts.append(VGroup(tk, t).arrange(RIGHT, buff=0.28))
        fstack = VGroup(*facts).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        todos = panel("and one worth stealing",
                      ["todos_open is counted per",
                       "recipe, not copied \u2014 and",
                       "markers inside gate tests",
                       "are excluded, because gate 1",
                       "and gate 5 grep FOR them.",
                       "a naive count reads two high."],
                      accent=TERRA, min_w=6.0, fs=18, title_fs=21)

        body = fit_src(VGroup(fstack, todos).arrange(RIGHT, buff=0.66))
        src = source_line("git show --unified=0 6428457 \u00b7 728 / 91 = exactly 8 lines each")

        for f in facts:
            self.play(Create(f[0]), FadeIn(f[1]), run_time=1.3)
            self.wait(0.7)
        self.wait(1.4)
        self.play(Create(todos[0]), FadeIn(todos[1]), run_time=2.8)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("A prepend you can check without trusting me")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.2)
