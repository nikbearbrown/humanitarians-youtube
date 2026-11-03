"""Manim beats for the reel `mycroft-weekly-green-because-it-wasnt-looking`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ fbd30b6 on branch fix/conformance-skip-list (2026-10-09),
with its companion fc645e8. Episode 7.

Every surface count on screen was reproduced from the COMMITTED tree by
re-implementing both versions of the skip rule out of scripts/conformance.mjs
(the working tree has 2117 files showing modified and was never read). Four of
the five figures matched the commit message exactly; the fifth did not, and
B08 is that correction. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over ten previous reels:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * citation beats use fit_src(), which reserves the citation strip
  * never draw a line THROUGH text
  * compose every label INTO the fitted group before fitting
  * a connector between two top-aligned columns must be centred SEPARATELY
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


def cross(color=TERRA):
    """Drawn X. Used once, in B08, for the claim that did not reproduce."""
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
    # An empty string makes a zero-height Text, and arrange() then stacks the
    # NEXT line onto the previous one -- that reads as a text-on-text error,
    # not as a gap. Use two panels for a visual break; never a blank line.
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


def vbar(height, label, figure, color, width=1.25, fig_fs=32):
    b = RoundedRectangle(width=width, height=max(height, 0.12), corner_radius=0.07,
                         stroke_width=2.0, stroke_color=color, fill_opacity=0)
    f = Text(figure, font=SERIF, font_size=fig_fs, color=color)
    l = Text(label, font=MONO, font_size=17, color=INK_SOFT)
    return VGroup(f, b, l).arrange(DOWN, buff=0.18)


class B01_TheUnaskedQuestion(Scene):
    """PROBLEM: episode 6's entry, and the follow-up I did not ask. 16.21s."""

    def construct(self):
        page(self)
        head = kicker("LAST EPISODE'S DID-NOT-TEST ENTRY",
                      "one of ten \u00b7 chased down to its cause")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        quoted = panel("episode 6 said",
                       ["there are no unit tests",
                        "for the six scripts, and",
                        "CI runs none of it"], accent=INK_SOFT, min_w=6.0)
        asked = panel("the follow-up I skipped",
                      ["the repo HAS a conformance checker",
                       "and it was passing",
                       "so what was it checking?"], accent=TERRA, min_w=6.0)
        link = Line(UP * 0.26, DOWN * 0.26, stroke_width=1.8, color=INK_SOFT)
        body = fit(VGroup(quoted, link, asked).arrange(DOWN, buff=0.34))

        self.play(Create(quoted[0]), FadeIn(quoted[1]), run_time=1.7)
        self.wait(1.6)
        self.play(Create(link), run_time=0.7)
        self.play(Create(asked[0]), FadeIn(asked[1]), run_time=1.7)
        self.wait(2.4)

        point = spark("A passing check is a claim too")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(4.0)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 16.28s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CHECK THAT PASSES",
                      "ask these before you trust the green")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  WHAT DID\n   IT OPEN?", ["count the files,", "by type"], accent=TERRA),
            panel("2  WHY IS EACH\n   EXCLUSION THERE?", ["for what it is called,",
                                                          "or where it lives"], accent=INK_SOFT),
            panel("3  HOW WOULD YOU\n   KNOW IF IT STOPPED?", ["break it on purpose",
                                                               "and see if it says so"],
                  accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.5)
            self.wait(0.9)
        self.wait(1.7)

        point = spark("Green is not a count")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(3.0)


class B04_TwoSurfaces(Scene):
    """QUESTION 1: the two checked surfaces, recounted. 20.59s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 WHAT DID IT OPEN?",
                      "both surfaces recounted from the committed tree")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        before = stat("187", ["files checked", "before"], accent=INK_SOFT)
        after = stat("743", ["files checked", "after"], accent=INK)
        gap = panel("the difference",
                    ["476 Python files",
                     "the executable surface",
                     "of 99 recipes"], accent=TERRA, min_w=5.2)

        arrow = Line(LEFT * 0.34, RIGHT * 0.34, stroke_width=1.8, color=INK_SOFT)
        row = VGroup(before, arrow, after).arrange(RIGHT, buff=0.42)
        body = fit_src(VGroup(row, gap).arrange(DOWN, buff=0.44))
        src = source_line("recounted from fc645e8^ and fc645e8 \u00b7 scripts/conformance.mjs")

        self.play(Create(before[0]), FadeIn(before[1]), run_time=1.4)
        self.play(Create(arrow), run_time=0.6)
        self.play(Create(after[0]), FadeIn(after[1]), run_time=1.4)
        self.wait(1.5)
        self.play(Create(gap[0]), FadeIn(gap[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Every step script the pipeline runs")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(5.4)


class B06_TheSpeedTrap(Scene):
    """the speed path, and the fallback that hid itself. 31.95s."""

    def construct(self):
        page(self)
        head = kicker("THE TRAP IN MAKING IT FAST",
                      "a fallback that restores the slow path without saying so")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        bars = VGroup(
            vbar(0.80, "before", "6.0s", INK_SOFT),
            vbar(2.40, "unbatched", "63s", INK),
            vbar(0.55, "batched", "3.9s", TERRA),
        ).arrange(RIGHT, buff=0.55, aligned_edge=DOWN)
        bcap = Text("187 files \u00b7 187 files \u00b7 743 files",
                    font=MONO, font_size=18, color=INK_SOFT)
        left = VGroup(bars, bcap).arrange(DOWN, buff=0.26)

        limits = panel("the Windows command line",
                       ["6000  chunk cap used",
                        "8191  cmd.exe real limit",
                        "32767 the number usually",
                        "      quoted, and wrong"], accent=INK_SOFT, min_w=5.6, fs=18)
        consequence = panel("past ~150 paths",
                            ["spawn fails",
                             "falls back to one-at-a-time",
                             "speed-up gone, still passes"], accent=TERRA, min_w=5.6, fs=18)
        right = VGroup(limits, consequence).arrange(DOWN, buff=0.30)

        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.70, aligned_edge=UP))
        src = source_line("scripts/conformance.mjs @ fc645e8 \u00b7 ARG_BUDGET = 6000")

        for b in bars:
            self.play(Create(b[1]), FadeIn(b[0]), FadeIn(b[2]), run_time=1.25)
            self.wait(0.5)
        self.play(FadeIn(bcap), run_time=0.8)
        self.wait(1.6)
        self.play(Create(limits[0]), FadeIn(limits[1]), run_time=2.0)
        self.wait(2.0)
        self.play(Create(consequence[0]), FadeIn(consequence[1]), run_time=2.0)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(3.0)

        point = spark("Four times the files, and faster")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.6)


class B07_BreakItOnPurpose(Scene):
    """QUESTION 3: the five break tests. 20.63s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 HOW WOULD YOU KNOW IF IT STOPPED?",
                      "five things broken on purpose")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        plain = [("syntax error in a step script", "caught, and named"),
                 ("truncated run envelope", "caught, and named"),
                 ("quarantined + private trees", "zero leaked in")]
        boxed = [("a named file inside a skipped tree", "still checked"),
                 (".json.broken fixtures", "stayed invisible")]

        def rows(items, colour):
            out = []
            for what, got in items:
                tk = tick(colour)
                a = Text(what, font=MONO, font_size=18, color=INK)
                b = Text(got, font=MONO, font_size=18, color=colour)
                out.append(VGroup(tk, a, b).arrange(RIGHT, buff=0.30))
            return out

        rp = rows(plain, INK)
        rb = rows(boxed, TERRA)
        bbody = VGroup(*rb).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        bbox = RoundedRectangle(width=bbody.width + 0.6, height=bbody.height + 0.6,
                                corner_radius=0.10, stroke_width=1.8,
                                stroke_color=TERRA, fill_opacity=0)
        bbox.move_to(bbody.get_center())
        pack = VGroup(bbox, bbody)

        body = fit_src(VGroup(*(rp + [pack])).arrange(DOWN, buff=0.30, aligned_edge=LEFT))
        src = source_line("fc645e8 commit body \u00b7 \u201cVerified by breaking things\u201d")

        for r in rp:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=1.1)
            self.wait(0.3)
        self.wait(0.8)
        self.play(Create(bbox), run_time=1.0)
        for r in rb:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=1.1)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.0)

        point = spark("The exclusions behave, not just the checker")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=1.9)
        self.wait(4.2)


class B08_TheRecount(Scene):
    """FALSIFIABILITY: four claims reproduce, one does not. 31.35s."""

    def construct(self):
        page(self)
        head = kicker("THE RECOUNT",
                      "five claims in my own commit message, checked against the tree")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        ok = [("187 files before", "187"),
              ("743 files after", "743"),
              ("476 Python revealed", "476"),
              ("99 recipes", "99")]
        rows, marks = [], []
        for claim, got in ok:
            m = tick(INK)
            a = Text(claim, font=MONO, font_size=19, color=INK)
            b = Text(got, font=SERIF, font_size=25, color=INK)
            r = VGroup(m, a, b).arrange(RIGHT, buff=0.32)
            rows.append(r)
            marks.append(m)

        xm = cross(TERRA)
        xa = Text("\u201cand zero Python\u201d", font=MONO, font_size=19, color=INK)
        xb = Text("39", font=SERIF, font_size=25, color=TERRA)
        xrow = VGroup(xm, xa, xb).arrange(RIGHT, buff=0.32)

        note = panel("all 39 are one subsystem",
                     ["scripts/gateway/ \u2014 mostly",
                      "that subsystem's own tests.",
                      "no recipe step script."], accent=TERRA, min_w=5.6, fs=18, title_fs=21)

        stack = VGroup(*(rows + [xrow])).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        body = fit_src(VGroup(stack, note).arrange(RIGHT, buff=0.70))
        src = source_line("re-implemented both skip rules against git ls-tree fbd30b6")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=1.15)
            self.wait(0.35)
        self.wait(1.4)
        self.play(Create(xm), FadeIn(xa), FadeIn(xb), run_time=1.8)
        self.wait(1.6)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=2.0)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("And it is my commit message")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.2)


class B09_HashesAsEvidence(Scene):
    """SUMMARY: the companion commit -- a hash that only works here. 27.98s."""

    def construct(self):
        page(self)
        head = kicker("WHY THE SECOND COMMIT EXISTS",
                      "a report cites the hash of every script it ran")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        f = chip("one committed file", INK_SOFT, font_size=18, height=0.44, pad=0.40)
        h1 = chip("hash on Linux", INK_SOFT, font_size=17, height=0.40)
        h2 = chip("hash on Windows", INK_SOFT, font_size=17, height=0.40)
        hs = VGroup(h1, h2).arrange(DOWN, buff=0.30)
        fork = Line(LEFT * 0.30, RIGHT * 0.30, stroke_width=1.8, color=INK_SOFT)
        strike = Line(DOWN * 0.30, UP * 0.30, stroke_width=5.0, color=TERRA)
        pairs = VGroup(f, fork, hs).arrange(RIGHT, buff=0.34)
        strike.move_to(fork.get_center())
        lcap = Text("autocrlf stored LF, checked out CRLF",
                    font=MONO, font_size=17, color=INK_SOFT)
        # What the hashes are FOR -- counted from the market-sentiment
        # attestation in episode 6. Without this the left column is 49% fill
        # and the stakes are only said, never shown.
        cites = panel("one report cites",
                      ["6 step-script hashes",
                       "3 source-file hashes"], accent=INK_SOFT, min_w=5.0, fs=18,
                      title_fs=21)
        left = VGroup(VGroup(pairs, strike), lcap, cites).arrange(DOWN, buff=0.32)

        rules = panel("pinned repo-wide",
                      ["* text=auto eol=lf",
                       "*.sh  eol=lf   (shebang)",
                       "*.bat eol=crlf (the one case)",
                       "21 extensions declared binary"], accent=INK, min_w=6.0, fs=18)
        checked = panel("and verified",
                        ["2120 files normalised",
                         "250 of 250 sampled hash"], accent=TERRA, min_w=6.0, fs=18,
                        title_fs=21)
        right = VGroup(rules, checked).arrange(DOWN, buff=0.32)

        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.70))
        src = source_line("fbd30b6 \u00b7 .gitattributes \u00b7 +101 \u221229")

        self.play(Create(f[0]), FadeIn(f[1]), run_time=1.1)
        self.play(Create(fork), run_time=0.6)
        self.play(Create(h1[0]), FadeIn(h1[1]), Create(h2[0]), FadeIn(h2[1]), run_time=1.5)
        self.wait(1.4)
        self.play(Create(strike), run_time=1.1)
        self.play(FadeIn(lcap), run_time=1.0)
        self.play(Create(cites[0]), FadeIn(cites[1]), run_time=1.8)
        self.wait(1.6)
        self.play(Create(rules[0]), FadeIn(rules[1]), run_time=2.2)
        self.wait(1.4)
        self.play(Create(checked[0]), FadeIn(checked[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("A hash that only reproduces here proves nothing")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.3)
