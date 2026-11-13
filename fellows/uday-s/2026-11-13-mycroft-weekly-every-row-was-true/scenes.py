"""Manim beats for the reel `mycroft-weekly-every-row-was-true`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ b425b19 on branch chore/map-covers-repo (2026-11-13).
Episode 12.

Verification, all read-only: the checker was RUN (`check` reads and prints;
`gate` writes and has not been run since episode 9); every subsystem count was
recounted with git ls-tree; and the JSON failure was reproduced by running
JSON.parse over the committed file. The commit's "12 of 51 top-level paths"
could NOT be reproduced and appears in no frame. See FACTCHECK.md.

NO LaTeX anywhere (dvisvgm absent).

Layout helpers converged over fifteen previous reels:
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


class B01_TrueAndIncomplete(Scene):
    """PROBLEM: accurate and complete are different claims. 19.52s."""

    def construct(self):
        page(self)
        head = kicker("NOTHING IN THE MAP WAS WRONG",
                      "b425b19 \u00b7 chore/map-covers-repo")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        a = panel("every row", ["accurate"], accent=INK_SOFT, min_w=4.6, fs=22, title_fs=22)
        x = crossmark(TERRA)
        eq = Text("=", font=SERIF, font_size=44, color=TERRA)
        sep = VGroup(eq, x).arrange(DOWN, buff=0.02)
        b = panel("the map", ["complete"], accent=TERRA, min_w=4.6, fs=22, title_fs=22)
        pair = VGroup(a, sep, b).arrange(RIGHT, buff=0.42)

        note = panel("and nothing in the file said so",
                     ["an agent reading it as its",
                      "instructions would never have",
                      "loaded a thousand files"], accent=INK, min_w=6.6, fs=19, title_fs=21)
        body = fit_src(VGroup(pair, note).arrange(DOWN, buff=0.44))
        src = source_line("a document can be entirely true and still mislead")

        self.play(Create(a[0]), FadeIn(a[1]), run_time=1.6)
        self.play(FadeIn(eq), run_time=0.6)
        self.play(Create(x), run_time=0.8)
        self.play(Create(b[0]), FadeIn(b[1]), run_time=1.6)
        self.wait(1.8)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Accurate is not complete")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.6)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 20.29s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY INDEX OR MAP",
                      "ask these of anything that tells you what is here")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  DOES IT SAY\n   WHAT IT COVERS?", ["coverage is a claim \u2014", "silence is not",
                                                         "completeness"], accent=INK_SOFT),
            panel("2  WHAT IS OUTSIDE\n   THE SURFACE?", ["the paths your checks", "never walk"],
                  accent=INK_SOFT),
            panel("3  LISTED,\n   OR CHECKED?", ["two different facts \u2014", "collapsing them answers",
                                                 "an open question"], accent=TERRA),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=1.7)
            self.wait(1.3)
        self.wait(2.4)

        point = spark("Silence is not a coverage claim")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.0)


class B04_TheTenSubsystems(Scene):
    """QUESTION 1: what the map was missing, recounted. 19.05s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 1 \u2014 WHAT THE MAP DID NOT MENTION",
                      "ten subsystems, every one tracked and on disk")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        data = [("projects/", "435", INK), ("case-study-workflows/", "277", INK),
                ("verification-layer/", "154", INK), ("multi-agents/", "41", INK),
                ("congressional-signals/", "39", INK_SOFT),
                ("provenance-gatekeeper/", "17", INK_SOFT),
                ("case-studies/", "14", INK_SOFT), ("archive/", "12", INK_SOFT),
                ("my_chapters/", "10", INK_SOFT), ("github-assistant/", "6", INK_SOFT)]
        rows = []
        for path, n, colour in data:
            p = Text(path, font=MONO, font_size=18, color=colour)
            c = Text(n, font=SERIF, font_size=22, color=colour)
            rows.append(VGroup(p, c).arrange(RIGHT, buff=0.26))
        stack = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)

        total = stat("1,005", ["tracked files", "the map did", "not mention"],
                     accent=TERRA, min_w=4.0)
        body = fit_src(VGroup(stack, total).arrange(RIGHT, buff=0.70))
        src = source_line("git ls-tree -r b425b19 \u00b7 each count recounted, and they sum to 1,005")

        self.play(*[FadeIn(r) for r in rows[:4]], run_time=1.6)
        self.play(*[FadeIn(r) for r in rows[4:]], run_time=1.4)
        self.wait(1.6)
        self.play(Create(total[0]), FadeIn(total[1]), run_time=1.8)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.4)

        point = spark("None of it was in the map")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.6)


class B05_OutsideTheSurface(Scene):
    """QUESTION 2: never walked by verify. 27.79s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 2 \u2014 WHAT IS OUTSIDE THE DEFAULT SURFACE",
                      "the consequence of not being on the map")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        one = panel("the ten subsystems",
                    ["not one of them is inside",
                     "conformance's DEFAULT_PATHS"], accent=INK_SOFT, min_w=7.0, fs=20, title_fs=22)
        one_tag = chip("npm run verify has never opened a file in any of them",
                       TERRA, font_size=18, height=0.44)

        two = panel("and eight scoped instruction files",
                    ["CLAUDE.md files below the root \u2014",
                     "not generated, not checked,",
                     "not reviewed"], accent=INK_SOFT, min_w=7.0, fs=20, title_fs=22)
        two_tag = chip("outside the generated set manifest-check verifies",
                       INK_SOFT, font_size=18, height=0.44)

        body = fit_src(VGroup(VGroup(one, one_tag).arrange(DOWN, buff=0.20),
                              VGroup(two, two_tag).arrange(DOWN, buff=0.20)
                              ).arrange(DOWN, buff=0.40))
        src = source_line("neither is a bug in anyone's code \u2014 both are an undrawn boundary")

        self.play(Create(one[0]), FadeIn(one[1]), run_time=2.0)
        self.play(Create(one_tag[0]), FadeIn(one_tag[1]), run_time=1.5)
        self.wait(2.6)
        self.play(Create(two[0]), FadeIn(two[1]), run_time=2.2)
        self.play(Create(two_tag[0]), FadeIn(two_tag[1]), run_time=1.5)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.2)

        point = spark("A boundary nobody had drawn")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.4)


class B07_ListedNotReviewed(Scene):
    """QUESTION 3: the restraint. 20.86s."""

    def construct(self):
        page(self)
        head = kicker("QUESTION 3 \u2014 LISTED, OR CHECKED?",
                      "the field that stays false")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rec = panel("what was recorded",
                    ["reviewed: false",
                     "",
                     "they have been listed."], accent=TERRA, min_w=5.2, fs=21, title_fs=22)

        would = ["read against SNICKERDOODLE.md",
                 "judged against its rules",
                 "accepted by a human"]
        rows = []
        for w in would:
            h = hollow()
            t = Text(w, font=MONO, font_size=19, color=INK)
            rows.append(VGroup(h, t).arrange(RIGHT, buff=0.26))
        wstack = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        wlab = Text("what \u201creviewed\u201d would have asserted \u2014 none of it happened",
                    font=MONO, font_size=18, color=INK_SOFT)
        right = VGroup(wlab, wstack).arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        # Side by side these two are wide and short, so fit() is width-limited
        # and cannot scale up -- measured 53% with dead bands top and bottom.
        # Stacked, the group is taller than it is wide and fills the band.
        body = fit_src(VGroup(rec, right).arrange(DOWN, buff=0.44))
        src = source_line("writing reviewed: true would resolve an open question by typing an answer")

        self.play(Create(rec[0]), FadeIn(rec[1]), run_time=2.0)
        self.wait(1.8)
        self.play(FadeIn(wlab), run_time=1.2)
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.1)
        self.play(FadeIn(src), run_time=0.8)
        self.wait(2.6)

        point = spark("Three boxes nobody gets to tick")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.2)


class B08_TheRecount(Scene):
    """FALSIFIABILITY: four reproduce, one does not. 28.05s."""

    def construct(self):
        page(self)
        head = kicker("THE RECOUNT", "every figure, checked against the tree")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        oks = [("all ten counts match, one for one", "10/10"),
               ("and they sum to", "1,005"),
               ("97 recipes \u2014 95 DRAFT, 2 RUNNABLE-SAMPLE", "97"),
               ("defects, all in one file", "5")]
        rows = []
        for claim, got in oks:
            m = tick(INK)
            a = Text(claim, font=MONO, font_size=18, color=INK)
            b = Text(got, font=SERIF, font_size=23, color=INK)
            rows.append(VGroup(m, a, b).arrange(RIGHT, buff=0.26))
        stack = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        miss = panel("one figure did not reproduce",
                     ["the commit says the old map",
                      "classified 12 of 51 top-level paths.",
                      "",
                      "I count 56 tracked entries \u2014 or 48",
                      "excluding the dot-directories.",
                      "",
                      "neither is 51, so it is not on screen."],
                     accent=TERRA, min_w=6.2, fs=18, title_fs=21)
        body = fit_src(VGroup(stack, miss).arrange(RIGHT, buff=0.62))
        src = source_line("git ls-tree b425b19 \u00b7 31 trees + 25 blobs at the top level")

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=1.2)
            self.wait(0.6)
        self.wait(1.2)
        self.play(Create(miss[0]), FadeIn(miss[1]), run_time=3.0)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Four reproduced. One withheld.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.4)


class B09_TheStaleFile(Scene):
    """SUMMARY: the five-month-stale Tier 1 file. 28.99s."""

    def construct(self):
        page(self)
        head = kicker("AND THE FILE PEOPLE READ FIRST",
                      "status.md was Tier 1, and five months stale")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        old_rows = []
        for t in ["reported 99 recipes",
                  "listed the recipe lifecycle",
                  "as still an open question"]:
            x = crossmark(TERRA)
            a = Text(t, font=MONO, font_size=19, color=INK)
            old_rows.append(VGroup(x, a).arrange(RIGHT, buff=0.26))
        old = VGroup(*old_rows).arrange(DOWN, buff=0.20, aligned_edge=LEFT)
        olab = Text("what the stale file claimed", font=MONO, font_size=18, color=INK_SOFT)
        left = VGroup(olab, old).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        now = panel("refreshed against measured counts",
                    ["97 recipes \u2014 95 DRAFT, 2 RUNNABLE-SAMPLE",
                     "check --all = 5 defects, all in gru.md"],
                    accent=INK, min_w=6.6, fs=19, title_fs=21)
        keep = chip("the June snapshot kept verbatim \u2014 24 of 24 lines verified present",
                    TERRA, font_size=18, height=0.44)
        verify = chip("npm run verify passes \u00b7 993 files conform", INK_SOFT,
                      font_size=18, height=0.44)
        right = VGroup(now, keep, verify).arrange(DOWN, buff=0.22)

        body = fit_src(VGroup(left, right).arrange(RIGHT, buff=0.62))
        src = source_line("nothing was deleted \u2014 the old content sits beneath the new")

        self.play(FadeIn(olab), run_time=0.9)
        for r in old_rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.1)
        self.wait(1.6)
        self.play(Create(now[0]), FadeIn(now[1]), run_time=2.4)
        self.wait(1.4)
        self.play(Create(keep[0]), FadeIn(keep[1]), run_time=1.6)
        self.play(Create(verify[0]), FadeIn(verify[1]), run_time=1.4)
        self.play(FadeIn(src), run_time=0.9)
        self.wait(3.0)

        point = spark("Stale, in the file read first")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(6.0)
