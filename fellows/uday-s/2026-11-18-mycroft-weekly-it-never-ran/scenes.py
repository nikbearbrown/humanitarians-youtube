"""Manim beats for the reel `mycroft-weekly-it-never-ran`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 08b92d3 on branch fix/conformance-multidoc-yaml (2026-11-18).
Episode 13 -- the direct sequel to episode 12, which diagnosed the multi-document
YAML failure as "the defect is in our checker".

Verification, all read-only (the mycroft tree is never written to -- no `gate`,
no run of conformance.mjs, which would compile Python and leave __pycache__):
the four changed lines were counted and blamed; all THREE mechanisms were
reproduced in a standalone interpreter outside the repository -- ComposerError
on a two-document file, SyntaxError from the mangled one-line script, and the
lazy-generator silent pass. The commit's 1,039 -> 1,853 file totals could NOT be
reproduced exactly (my git-based replay gives 1,142 -> 1,955), so B08 shows both
and attributes the totals to the commit. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over sixteen previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * a cross sits BESIDE or BETWEEN what it negates, never through text
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


def tick(color=INK):
    return VGroup(
        Line([-0.10, 0.02, 0], [-0.02, -0.09, 0], stroke_width=3.2, color=color),
        Line([-0.02, -0.09, 0], [0.13, 0.13, 0], stroke_width=3.2, color=color),
    )


def crossmark(color=TERRA):
    """Sits BESIDE or BETWEEN. Never drawn through text."""
    return VGroup(
        Line([-0.10, 0.10, 0], [0.10, -0.10, 0], stroke_width=3.2, color=color),
        Line([-0.10, -0.10, 0], [0.10, 0.10, 0], stroke_width=3.2, color=color),
    )


def hollow(size=0.24, color=INK_SOFT, stroke=1.8):
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




def tickrow(text, color=INK, fs=20):
    return VGroup(tick(color), Text(text, font=MONO, font_size=fs, color=INK)).arrange(
        RIGHT, buff=0.26)


def crossrow(text, color=TERRA, fs=20):
    return VGroup(crossmark(color),
                  Text(text, font=MONO, font_size=fs, color=INK)).arrange(RIGHT, buff=0.26)


def connector(height=0.34):
    return Line([0, 0, 0], [0, -height, 0], stroke_width=1.6, color=INK_SOFT)


class B01_TheFixThatDidNothing(Scene):
    """PROBLEM: the loader changed, the output did not. 21.31s."""

    def construct(self):
        page(self)
        head = kicker("I FIXED IT, AND NOTHING MOVED",
                      "08b92d3 · fix/conformance-multidoc-yaml")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        before = panel("last week", ["yaml.safe_load(f)", "one document only"],
                       accent=INK_SOFT, min_w=5.2, fs=20, title_fs=22)
        arrow = Text("→", font=SERIF, font_size=40, color=INK_SOFT)
        after = panel("this week", ["yaml.safe_load_all(f)", "many documents"],
                      accent=TERRA, min_w=5.2, fs=20, title_fs=22)
        pair = VGroup(before, arrow, after).arrange(RIGHT, buff=0.40)

        same = panel("the output", ["byte for byte identical",
                                    "not better — the same"],
                     accent=INK, min_w=6.4, fs=20, title_fs=22)
        note = Text("the edited code was not the code producing the answer",
                    font=SANS, font_size=24, color=INK)

        body = fit_src(VGroup(pair, connector(0.40), same, note).arrange(DOWN, buff=0.36))
        src = source_line("a fix that changes nothing is evidence about what is running")

        self.play(Create(before[0]), FadeIn(before[1]), run_time=1.8)
        self.play(FadeIn(arrow), run_time=0.6)
        self.play(Create(after[0]), FadeIn(after[1]), run_time=1.8)
        self.wait(2.0)
        self.play(Create(body[1]), run_time=0.6)
        self.play(Create(same[0]), FadeIn(same[1]), run_time=2.2)
        self.wait(1.2)
        self.play(FadeIn(note), run_time=1.8)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.4)

        point = spark("It was never running")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.4)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before any evidence. 17.30s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CHECK YOU TRUST",
                      "ask these of anything that reports green")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  DID THE FIX\n   CHANGE ANYTHING?", ["if not, the thing you", "edited may not be",
                                                          "running at all"], accent=INK_SOFT),
            panel("2  WHAT DOES THE\n   FALLBACK HIDE?", ["a correct fallback", "behind a broken primary",
                                                          "is right for the wrong", "reason, forever"],
                  accent=INK_SOFT),
            panel("3  WOULD IT PASS IF\n   IT PARSED NOTHING?", ["ask any checker —", "the answer is often",
                                                                 "yes"], accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in row:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=2.0)
            self.wait(1.2)

        point = spark("Score every green run against these")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.7)


class B05_ThreeMechanisms(Scene):
    """HERO: all three mechanisms reproduced standalone. 30.07s."""

    def construct(self):
        page(self)
        head = kicker("REPRODUCED OUTSIDE THE REPOSITORY",
                      "a standalone interpreter · nothing from mycroft ran")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        p1 = panel("1  the original\n   complaint", [
            "yaml.safe_load(two_doc)",
            "ComposerError:",
            "expected a single",
            "document in the stream",
        ], accent=INK_SOFT, min_w=4.4, fs=19, title_fs=21)
        p2 = panel("2  the runner,\n   as shipped", [
            "a newline became the",
            "two characters  \\  n",
            "SyntaxError: unexpected",
            "character after line",
            "continuation character",
        ], accent=INK_SOFT, min_w=4.4, fs=19, title_fs=21)
        p3 = panel("3  the trap inside\n   the fix", [
            "safe_load_all, no list()",
            "no output.  no error.",
            "exit 0.",
            "every file passes",
        ], accent=TERRA, min_w=4.4, fs=19, title_fs=21)

        body = fit_src(VGroup(p1, p2, p3).arrange(RIGHT, buff=0.34, aligned_edge=UP))
        src = source_line("all three run standalone · see FACTCHECK.md")

        for p in (p1, p2, p3):
            self.play(Create(p[0]), FadeIn(p[1]), run_time=2.4)
            self.wait(3.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(4.0)

        point = spark("A lazy generator is a silent pass")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.3)


class B06_WhyNothingShowed(Scene):
    """QUESTION 2: the fallback was correct, so nothing ever surfaced. 21.35s."""

    def construct(self):
        page(self)
        head = kicker("WHY FIVE WEEKS OF RUNS LOOKED FINE",
                      "the catch worked — that was the problem")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        steps = [
            chip("1   the batch runner throws SyntaxError, every time", TERRA,
                 font_size=24, pad=0.46, height=0.60),
            chip("2   catch fires, silently", INK_SOFT, font_size=24, pad=0.46, height=0.60),
            chip("3   per-file fallback runs, one file at a time", INK_SOFT,
                 font_size=24, pad=0.46, height=0.60),
            chip("4   the answer is correct — for single-document files", INK,
                 font_size=24, pad=0.46, height=0.60),
        ]
        flow = VGroup(steps[0], connector(0.30), steps[1], connector(0.30),
                      steps[2], connector(0.30), steps[3]).arrange(DOWN, buff=0.16)
        tag = chip("introduced 2026-10-09 · the commit that made this check fast", TERRA,
                   font_size=21, pad=0.40, height=0.52)
        body = fit_src(VGroup(flow, tag).arrange(DOWN, buff=0.46))
        src = source_line("git blame · 3 of the 4 removed lines, one author, one day")

        for i, s in enumerate(steps):
            if i:
                self.play(Create(flow[2 * i - 1]), run_time=0.4)
            self.play(Create(s[0]), FadeIn(s[1]), run_time=1.5)
            self.wait(0.7)
        self.play(Create(tag[0]), FadeIn(tag[1]), run_time=1.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(2.0)

        point = spark("The batch was dead and nothing said so")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.65)


class B07_WhoseLines(Scene):
    """the discipline: four lines, one author, and what was left alone. 20.03s."""

    def construct(self):
        page(self)
        head = kicker("FOUR LINES, AND THE ONES LEFT ALONE",
                      "the part a diff summary does not show")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        s = stat("4", ["lines removed",
                       "all four written 2026-10-09",
                       "all four by the same author"], accent=TERRA, min_w=6.6)

        left = panel("not touched, on purpose", [
            "the per-file fallback's safe_load()",
            "another contributor's August code",
            "the shared import line — execFileSync",
            "went on a new line of its own",
        ], accent=INK_SOFT, min_w=8.6, fs=19, title_fs=22)

        body = fit_src(VGroup(s, left).arrange(DOWN, buff=0.44))
        src = source_line("git blame · counted on the committed diff")

        self.play(Create(s[0]), FadeIn(s[1]), run_time=2.0)
        self.wait(1.8)
        self.play(Create(left[0]), FadeIn(left[1]), run_time=2.6)
        self.wait(1.6)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Fix your own lines first")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.2)


class B08_TheRecount(Scene):
    """FALSIFIABILITY: what reproduced, and what did not. 34.21s."""

    def construct(self):
        page(self)
        head = kicker("THE RECOUNT",
                      "everything on screen was re-derived · one figure was not")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup(
            tickrow("4 lines removed — counted on the diff"),
            tickrow("one author, one day — git blame"),
            tickrow("all three mechanisms — run standalone"),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        rbox = RoundedRectangle(width=rows.width + 0.8, height=rows.height + 0.7,
                                corner_radius=0.12, stroke_width=1.8,
                                stroke_color=INK, fill_opacity=0).move_to(rows.get_center())
        verified = VGroup(rbox, rows)

        cmp_ = panel("the file totals did not", [
            "the commit says    1,039  ->  1,853",
            "my replay gives    1,142  ->  1,955",
            "the increase:  814  vs  813",
            "the baseline differs by ~102 — the real",
            "walker reads the disk, I walked git",
        ], accent=TERRA, min_w=9.0, fs=19, title_fs=22)

        body = fit_src(VGroup(verified, cmp_).arrange(DOWN, buff=0.40))
        src = source_line("totals are the commit's, attributed · the increase is mine")

        self.play(Create(rbox), run_time=1.0)
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.8)
            self.wait(1.6)
        self.wait(1.5)
        self.play(Create(cmp_[0]), run_time=2.8)
        self.play(FadeIn(cmp_[1]), run_time=1.8)
        self.wait(3.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(4.2)

        point = spark("Say which number is yours")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.4)


class B09_TheWidening(Scene):
    """SUMMARY: what was added, what was left out, and the recorded limit. 32.46s."""

    def construct(self):
        page(self)
        head = kicker("WHAT THE CHECK NOW WALKS",
                      "and what it still does not, with reasons on record")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        added = panel("8 subsystems added to the surface", [
            "verification-layer      multi-agents",
            "projects                provenance-gatekeeper",
            "case-study-workflows    github-assistant",
            "case-studies            my_chapters",
        ], accent=INK, min_w=9.4, fs=19, title_fs=22)

        out = panel("left out, deliberately", [
            "congressional-signals — holds the bare NaN",
            "found last episode; would fail every run",
            "archive/ — kept so it stops changing",
            "env, .venv, venv — nobody compiles their",
            "own site-packages",
        ], accent=INK_SOFT, min_w=9.4, fs=19, title_fs=22)

        limit = chip("not tested: the Python version CI uses — only the one on this machine", TERRA)

        body = fit_src(VGroup(added, out, limit).arrange(DOWN, buff=0.32))
        src = source_line("DEFAULT_PATHS and SKIP, read from the committed file")

        self.play(Create(added[0]), FadeIn(added[1]), run_time=2.6)
        self.wait(2.6)
        self.play(Create(out[0]), FadeIn(out[1]), run_time=3.0)
        self.wait(3.0)
        self.play(Create(limit[0]), FadeIn(limit[1]), run_time=2.0)
        self.wait(3.0)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(3.6)

        point = spark("Write down what you did not check")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.16)
