"""Manim beats for the reel `small-models-coding-rl`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: making smaller models good at coding with agentic scaffolds and RL.
Primary sources: the DeepSWE-Preview release (Agentica / Together AI, Qwen3-32B
base, RL only) and Yang et al., SWE-smith (SWE-agent-LM-32B). Every figure comes
from the primary source; aggregator pages were not used for any number.

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
    DOWN, LEFT, RIGHT, UP, Create, DashedVMobject, FadeIn, Line,
    RoundedRectangle, Scene, Text, VGroup,
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


def dashchip(label, color, font_size=19, pad=0.32, height=0.36):
    """A chip with a DASHED border. Used for the one score that is an upper
    bound rather than a result, so the difference is visible, not just said."""
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(width=t.width + pad, height=height, corner_radius=0.07,
                           stroke_width=1.5, stroke_color=color, fill_opacity=0)
    box.move_to(t.get_center())
    return VGroup(DashedVMobject(box, num_dashes=28), t)


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


def stat(figure, caption_lines, accent=INK, fig_fs=54, cap_fs=19, min_w=4.2):
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


def hbar(length, label, figure, color, height=0.46, fig_fs=25, dashed=False):
    """Horizontal bar: label left, bar, figure right. All composed into one
    group BEFORE fitting."""
    l = Text(label, font=MONO, font_size=18, color=INK_SOFT)
    box = RoundedRectangle(width=max(length, 0.14), height=height, corner_radius=0.07,
                           stroke_width=2.0, stroke_color=color, fill_opacity=0)
    b = DashedVMobject(box, num_dashes=34) if dashed else box
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    return VGroup(l, b, f).arrange(RIGHT, buff=0.26)


class B01_ThreeNumbers(Scene):
    """BLUF: three published scores, one model, one benchmark."""

    def construct(self):
        page(self)
        head = kicker("ONE MODEL \u00b7 ONE BENCHMARK \u00b7 THREE PUBLISHED SCORES",
                      "DeepSWE-Preview (32B) on SWE-bench Verified")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            stat("42.2", ["what a user gets"], accent=TERRA),
            stat("59.0", ["also published"], accent=INK_SOFT),
            stat("71.0", ["also published"], accent=INK_SOFT),
        ]
        row = fit_src(VGroup(*cards).arrange(RIGHT, buff=0.55))
        src = source_line("Agentica / Together AI \u00b7 DeepSWE-Preview release \u00b7 500 problems")

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.6)
            self.wait(0.9)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Three measurements, not three attempts")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(7.2)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CODING-AGENT SCORE",
                      "ask these before you compare two models")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  ONE RUN, OR\n   BEST OF N?", ["best-of-N is", "a different product"],
                  accent=INK_SOFT),
            panel("2  WHICH SCAFFOLD,\n   HOW MUCH CONTEXT?", ["the harness", "is not neutral"],
                  accent=INK_SOFT),
            panel("3  WHO PICKED\n   THE WINNER?", ["a verifier you can run,", "or an oracle that",
                                                    "already knows"], accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(1.1)
        self.wait(2.6)

        point = spark("Question three is where the inflation lives")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.9)


class B03_TheRecipe(Scene):
    """EVIDENCE: what 'trained with RL' actually meant here."""

    def construct(self):
        page(self)
        head = kicker("WHAT WAS ACTUALLY DONE",
                      "so \u201ctrained with RL\u201d stops being a slogan")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        recipe = panel("the recipe",
                       ["base      Qwen3-32B",
                        "method    RL only \u2014 no distillation",
                        "algorithm modified GRPO",
                        "tasks     4,500 real SWE problems",
                        "source    R2E-Gym subset",
                        "compute   64 x H100, 6 days"], accent=INK, min_w=6.6, fs=19)
        clean = panel("and first, this",
                      ["every repo that appears in",
                       "the benchmark was filtered",
                       "out of training"], accent=TERRA, min_w=5.0, fs=18, title_fs=21)

        body = fit_src(VGroup(recipe, clean).arrange(RIGHT, buff=0.60, aligned_edge=UP))
        src = source_line("DeepSWE-Preview release \u00b7 training setup")

        self.play(Create(recipe[0]), run_time=1.3)
        self.play(FadeIn(recipe[1]), run_time=2.4)
        self.wait(2.4)
        self.play(Create(clean[0]), FadeIn(clean[1]), run_time=2.2)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.8)

        point = spark("No distillation. That part is unusual.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.6)


class B04_Decomposed(Scene):
    """QUESTION 1: the scores decomposed, each labelled with what it measures."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 ONE RUN, OR BEST OF N?",
                      "the same model, four published settings")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = [
            hbar(1.69, "pass@1", "42.2", TERRA),
            hbar(2.32, "best@8", "57.9", INK),
            hbar(2.36, "best@16", "59.0", INK),
            hbar(2.84, "pass@16", "71.0", INK_SOFT, dashed=True),
        ]
        notes = [
            Text("one attempt \u2014 what a user gets", font=MONO, font_size=17, color=INK_SOFT),
            Text("8 tries, a verifier picks", font=MONO, font_size=17, color=INK_SOFT),
            Text("16 tries, a verifier picks", font=MONO, font_size=17, color=INK_SOFT),
            Text("16 tries, an ORACLE picks \u2014 upper bound, not shippable",
                 font=MONO, font_size=17, color=TERRA),
        ]
        pairs = [VGroup(r, n).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
                 for r, n in zip(rows, notes)]
        body = fit_src(VGroup(*pairs).arrange(DOWN, buff=0.26, aligned_edge=LEFT))
        src = source_line("DeepSWE-Preview release \u00b7 SWE-bench Verified \u00b7 pass@1 averaged over 16 runs")

        for p in pairs:
            self.play(Create(p[0][1]), FadeIn(p[0][0]), FadeIn(p[0][2]), run_time=1.3)
            self.play(FadeIn(p[1]), run_time=0.9)
            self.wait(0.6)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Only the first one is a product")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.1)


class B05_SmallerAndHigher(Scene):
    """QUESTION 2: the authors' own table has a smaller model above them."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 WHICH SCAFFOLD?",
                      "from the same table the authors published")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        left = panel("DeepSWE-Preview",
                     ["32B parameters",
                      "scaffold   R2E-Gym",
                      "setting    one attempt",
                      "score      42.2"], accent=INK_SOFT, min_w=5.8, fs=19)
        right = panel("Devstral-Small",
                      ["24B parameters",
                       "scaffold   OpenHands",
                       "setting    one attempt",
                       "score      46.6"], accent=TERRA, min_w=5.8, fs=19)

        pair = VGroup(left, right).arrange(RIGHT, buff=1.50, aligned_edge=UP)
        link = Line(LEFT * 0.45, RIGHT * 0.45, stroke_width=1.8, color=INK_SOFT)
        link.move_to([(left.get_right()[0] + right.get_left()[0]) / 2,
                      pair.get_center()[1], 0])
        note = Text("8B smaller, 4.4 points higher \u2014 and a different harness",
                    font=MONO, font_size=19, color=INK)
        body = fit_src(VGroup(VGroup(pair, link), note).arrange(DOWN, buff=0.40))
        src = source_line("DeepSWE-Preview release \u00b7 comparison table \u00b7 R2E-Gym at 64k ctx, 100 steps")

        self.play(Create(left[0]), FadeIn(left[1]), run_time=1.7)
        self.play(Create(link), run_time=0.6)
        self.play(Create(right[0]), FadeIn(right[1]), run_time=1.7)
        self.wait(2.0)
        self.play(FadeIn(note), run_time=1.5)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Change the harness and the number moves")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.9)


class B06_NotALeaderboard(Scene):
    """FALSIFIABILITY: four scaffolds and three settings in one table."""

    def construct(self):
        page(self)
        head = kicker("THE TABLE IS NOT A LEADERBOARD",
                      "ten rows \u00b7 four scaffolds \u00b7 three test-time settings")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [
            ("DeepSWE-Preview 32B", "R2E-Gym", "best@16", "59.0", True),
            ("Skywork-SWE 32B", "OpenHands", "best@8", "47.0", True),
            ("Devstral-Small 24B", "OpenHands", "one run", "46.6", False),
            ("DeepSWE-Preview 32B", "R2E-Gym", "one run", "42.2", False),
            ("SWE-Agent-LM 32B", "SWE-Agent", "one run", "40.2", False),
            ("R2EGym-Agent 32B", "R2E-Gym", "one run", "34.4", False),
        ]
        rows = []
        for name, scaf, setting, score, isN in data:
            n = Text(name, font=MONO, font_size=18, color=INK)
            s = chip(scaf, INK_SOFT, font_size=16, height=0.34)
            t = chip(setting, TERRA if isN else INK_SOFT, font_size=16, height=0.34)
            v = Text(score, font=SERIF, font_size=23,
                     color=TERRA if isN else INK)
            rows.append(VGroup(n, s, t, v).arrange(RIGHT, buff=0.28))
        stack = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        warn = Text("ranking these top to bottom compares different things",
                    font=SANS, font_size=21, color=INK)
        body = fit_src(VGroup(stack, warn).arrange(DOWN, buff=0.34))
        src = source_line("DeepSWE-Preview release \u00b7 6 of the 10 rows shown \u00b7 scaffold is their own column")

        for r in rows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]),
                      Create(r[2][0]), FadeIn(r[2][1]), FadeIn(r[3]), run_time=1.15)
            self.wait(0.35)
        self.wait(1.6)
        self.play(FadeIn(warn), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.1)

        point = spark("The scaffold is a column. Almost nobody reads it.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.0)


class B07_WhichLever(Scene):
    """EVIDENCE: RL vs distillation, against what selection actually bought."""

    def construct(self):
        page(self)
        head = kicker("WHICH LEVER MOVED THE NUMBER?",
                      "two training roads, then the thing that dwarfed both")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rl = panel("RL",
                   ["DeepSWE-Preview",
                    "no distillation",
                    "42.2  one run"], accent=INK, min_w=5.0, fs=18, title_fs=22)
        sft = panel("distillation",
                    ["SWE-smith \u2014 50k tasks",
                     "across 128 repos",
                     "40.2  one run"], accent=INK_SOFT, min_w=5.0, fs=18, title_fs=22)
        delta = chip("2.0 apart", INK_SOFT, font_size=17)
        top = VGroup(rl, delta, sft).arrange(RIGHT, buff=0.42)

        big = RoundedRectangle(width=9.2, height=0.70, corner_radius=0.10,
                               stroke_width=2.2, stroke_color=TERRA, fill_opacity=0)
        biglab = Text("+16.8  \u2014  turning on best-of-16, same model",
                      font=MONO, font_size=20, color=TERRA)
        biglab.move_to(big.get_center())
        bottom = VGroup(big, biglab)

        body = fit_src(VGroup(top, bottom).arrange(DOWN, buff=0.48))
        src = source_line("DeepSWE-Preview release \u00b7 Yang et al., SWE-smith (SWE-agent-LM-32B)")

        self.play(Create(rl[0]), FadeIn(rl[1]), run_time=1.6)
        self.play(Create(sft[0]), FadeIn(sft[1]), run_time=1.6)
        self.wait(2.2)
        self.play(Create(delta[0]), FadeIn(delta[1]), run_time=1.2)
        self.wait(2.8)
        self.play(Create(big), run_time=2.0)
        self.play(FadeIn(biglab), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(3.6)

        point = spark("Not the training method")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(8.0)


class B08_Verdict(Scene):
    """VERDICT: rubric scored, both sides, and the cost of the big number."""

    def construct(self):
        page(self)
        head = kicker("SCORED", "and what the big number costs to actually run")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        qa = [("ONE RUN OR BEST OF N", "3 of the 4 are best-of-N", TERRA),
              ("WHICH SCAFFOLD", "four of them, one table", TERRA),
              ("WHO PICKED THE WINNER", "verifier at 59, oracle at 71", TERRA)]
        qrows = []
        for label, answer, colour in qa:
            t = Text(label, font=SANS, font_size=21, color=INK_SOFT)
            ch = chip(answer, colour, font_size=17)
            qrows.append(VGroup(t, ch).arrange(RIGHT, buff=0.32))
        scored = VGroup(*qrows).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        verdict = VGroup(
            Text("BE EXCITED ABOUT:  32B, open, RL-only, real repositories",
                 font=SANS, font_size=22, color=INK),
            Text("BE SCEPTICAL OF:  any score quoted without its scaffold and its N",
                 font=SANS, font_size=22, color=TERRA),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        cost = panel("and if you want the 59",
                     ["best-of-16 means",
                      "16x the inference"], accent=TERRA, min_w=4.6, fs=18, title_fs=21)

        lower = VGroup(verdict, cost).arrange(RIGHT, buff=0.60, aligned_edge=UP)
        body = fit_src(VGroup(scored, lower).arrange(DOWN, buff=0.44, aligned_edge=LEFT))
        src = source_line("all figures from the DeepSWE-Preview release and SWE-smith")

        for r in qrows:
            self.play(FadeIn(r[0]), Create(r[1][0]), FadeIn(r[1][1]), run_time=1.3)
            self.wait(0.6)
        self.wait(1.8)
        for v in verdict:
            self.play(FadeIn(v, shift=UP * 0.1), run_time=1.5)
            self.wait(1.1)
        self.play(Create(cost[0]), FadeIn(cost[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(3.2)

        point = spark("Budget for the number you quote")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(7.9)
