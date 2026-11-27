"""Manim beats for the reel `mycroft-weekly-the-fourth-gate`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json.

Subject: mycroft @ 20795b2 on branch chore/promote-scenariostresstestingagent
(2026-11-27). Episode 14.

Verification, all read-only (the mycroft tree is never written to -- no `gate`,
no `run`, no conformance pass, nothing that would leave a decision record or a
__pycache__): every gate test was reproduced OUTSIDE the repository, in a
scratch folder, against files broken on purpose. Two findings are the reel's
own rather than the commit's:

  * B06 -- gate 4 cannot fail either, and the commit does not say so. Its
    fallback greps the recipe for "[TODO: DEV]", and that string sits inside
    gate 4's own test command, which is written in the file being searched.
  * B07 -- the commit groups gate 6 with "cannot fail as written". Measured, it
    exits 1: it cannot PASS. Opposite defect, opposite consequence.

See FACTCHECK.md for the figure-by-figure table.

NO LaTeX anywhere (dvisvgm absent).

Layout, learned the hard way over seventeen reels. GATE V scores `cover` as the
ink BOUNDING BOX over the safe area, so two things decide whether a beat passes:

  * the fitted body must FILL its band. fit_src() centres the group in a
    4.2-unit band; if the group's natural aspect is much wider than ~2.9:1 it
    comes back height-starved and leaves dead bands top and bottom. Keep panel
    lines SHORT so a 3-across row stays about 11.5 units wide, not 15.
  * the citation strip is the lowest element on the frame, so it must land
    BEFORE the midpoint sample or that frame reads as half-empty. Every beat
    here brings src in by ~45%.

Other rules that still hold:
  * kicker at buff 0.72 -- 0.55 breaks the +/-3.4 safe box
  * a box is NEVER hard-coded narrower than its own text
  * a cross sits BESIDE or BETWEEN what it negates, never through text
  * compose every label INTO the fitted group before fitting
  * panel() drops blank lines -- a zero-height Text stacks the next line on it
  * faint ink (low stroke_opacity) drags GATE V's contrast metric down; one
    accent colour, everything else full INK
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


def connector(height=0.32):
    return Line([0, 0, 0], [0, -height, 0], stroke_width=1.6, color=INK_SOFT)


def boxed(rows, accent=INK, pad_x=0.8, pad_y=0.7):
    box = RoundedRectangle(width=rows.width + pad_x, height=rows.height + pad_y,
                           corner_radius=0.12, stroke_width=1.8,
                           stroke_color=accent, fill_opacity=0)
    box.move_to(rows.get_center())
    return VGroup(box, rows)


class B01_ThePromotion(Scene):
    """PROBLEM: a promotion that documents its own weaknesses. 22.89s."""

    def construct(self):
        page(self)
        head = kicker("A PROMOTION, SIGNED WITH ITS FLAWS ATTACHED",
                      "20795b2 · chore/promote-scenariostresstestingagent")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        moved = panel("one recipe, one step", [
            "DRAFT  →  RUNNABLE-SAMPLE",
            "status and last_gate",
            "two lines changed",
        ], accent=INK, min_w=5.2, fs=20, title_fs=22)

        flaws = panel("what the sign-off says about itself", [
            "3 gate tests cannot fail",
            "steps 3-6 read the fixture folder,",
            "not step 2's output",
        ], accent=TERRA, min_w=6.2, fs=20, title_fs=22)

        pair = VGroup(moved, flaws).arrange(RIGHT, buff=0.42, aligned_edge=UP)
        blocked = chip("live execution stays blocked — there is no approval record", INK,
                       font_size=21, pad=0.40, height=0.52)
        body = fit_src(VGroup(pair, blocked).arrange(DOWN, buff=0.40))
        src = source_line("nobody required the signer to write any of that down")

        self.play(Create(moved[0]), FadeIn(moved[1]), run_time=2.0)
        self.wait(1.4)
        self.play(Create(flaws[0]), FadeIn(flaws[1]), run_time=2.8)
        self.wait(1.0)
        self.play(Create(blocked[0]), FadeIn(blocked[1]), run_time=1.6)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(5.2)

        point = spark("The evidence came with its own warnings")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.99)


class B02_ThreeQuestions(Scene):
    """FRAMEWORK: the rubric, as a structure, before the evidence. 18.22s."""

    def construct(self):
        page(self)
        head = kicker("THREE QUESTIONS FOR ANY CHECK THAT GUARDS ANYTHING",
                      "ask these before you trust a green run")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = [
            panel("1  CAN IT FAIL?", ["not in theory —", "run it against", "something you broke",
                                      "on purpose"], accent=TERRA),
            panel("2  WHAT HAPPENS TO\n   A FAILURE IT\n   CANNOT JUDGE?", ["a check that discards",
                                                                            "what it cannot classify",
                                                                            "reports clean forever"],
                  accent=INK_SOFT),
            panel("3  WHAT WAS WRITTEN\n   DOWN UNASKED?", ["the weaknesses nobody", "required anyone",
                                                            "to record"], accent=INK_SOFT),
        ]
        row = fit(VGroup(*cards).arrange(RIGHT, buff=0.42, aligned_edge=UP))

        for c in row:
            self.play(Create(c[0]), FadeIn(c[1]), run_time=2.2)
            self.wait(1.6)

        point = spark("Break it on purpose, then look")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(3.92)


class B05_ThreeGates(Scene):
    """HERO: the three gates run against planted defects. 22.06s."""

    def construct(self):
        page(self)
        head = kicker("RUN AGAINST SOMETHING BROKEN ON PURPOSE",
                      "a scratch folder · nothing from mycroft ran")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        p1 = panel("gate 1 · || true", [
            "pattern present  0",
            "pattern absent   0",
            "file missing     0",
            "it always passes",
        ], accent=INK, min_w=3.6, fs=19, title_fs=21)
        p2 = panel("gate 3 · find -exec", [
            "bad json: exit 1",
            "find says: exit 0",
            "the real failure",
            "is swallowed",
        ], accent=INK, min_w=3.6, fs=19, title_fs=21)
        p3 = panel("gate 6 · [DATE]", [
            "no file by that",
            "name exists",
            "exit 1 — it cannot",
            "ever pass",
        ], accent=TERRA, min_w=3.6, fs=19, title_fs=21)

        body = fit_src(VGroup(p1, p2, p3).arrange(RIGHT, buff=0.34, aligned_edge=UP))
        src = source_line("reproduced standalone, outside the repository · FACTCHECK.md")

        for p in (p1, p2, p3):
            self.play(Create(p[0]), FadeIn(p[1]), run_time=1.6)
            self.wait(1.0)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(5.4)

        point = spark("Two cannot fail. One cannot pass.")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.96)


class B06_TheFourthGate(Scene):
    """the finding that is not in the commit: gate 4 greps itself. 22.66s."""

    def construct(self):
        page(self)
        head = kicker("THE ONE NOBODY NAMED",
                      "gate 4: the script exists, OR there is a typed TODO")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cmd = panel("gate 4's fallback, as written", [
            "test -f scripts/.../ingest-inputs.py",
            "  || rg -F \"[TODO: DEV]\" recipes/<recipe>.md",
        ], accent=INK, min_w=8.4, fs=19, title_fs=22)

        selfref = chip("that pattern is inside gate 4's own test line — in the file it searches",
                       TERRA, font_size=21, pad=0.40, height=0.52)

        result = panel("so I deleted the script and every real TODO", [
            "9 occurrences of [TODO: DEV] in the recipe",
            "6 of them marked Closed · 1 is the gate itself",
            "exit 0.  the gate passes on its own definition.",
        ], accent=TERRA, min_w=8.4, fs=19, title_fs=22)

        body = fit_src(VGroup(cmd, selfref, result).arrange(DOWN, buff=0.34))
        src = source_line("reproduced standalone · a fourth gate that cannot fail")

        self.play(Create(cmd[0]), FadeIn(cmd[1]), run_time=2.4)
        self.wait(1.2)
        self.play(Create(selfref[0]), FadeIn(selfref[1]), run_time=1.8)
        self.wait(1.2)
        self.play(Create(result[0]), FadeIn(result[1]), run_time=2.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(5.0)

        point = spark("The gate greps for itself")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.96)


class B07_TheRecount(Scene):
    """FALSIFIABILITY: the recount corrects my own commit message. 35.19s."""

    def construct(self):
        page(self)
        head = kicker("THE RECOUNT",
                      "this time it corrects the commit message I wrote")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        claim = panel("the commit says", ["gates 1, 3 and 6", "\"cannot fail as written\""],
                      accent=INK, min_w=5.0, fs=20, title_fs=22)
        found = panel("gate 6, measured", ["exit 1, every time", "it cannot ever PASS"],
                      accent=TERRA, min_w=5.0, fs=20, title_fs=22)
        pair = VGroup(claim, found).arrange(RIGHT, buff=0.42, aligned_edge=UP)

        why = Text("stuck on pass hides quietly · stuck on fail gets noticed",
                   font=SANS, font_size=24, color=INK)

        rows = VGroup(
            tickrow("parity: 24 of 24 match — but there are 25 rows, 1 not modelled"),
            tickrow("self-test skipped: 1 in the run log, 0 in the committed result"),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        body = fit_src(VGroup(pair, why, rows).arrange(DOWN, buff=0.34))
        src = source_line("two runs, two machines · recorded in FACTCHECK.md")

        self.play(Create(claim[0]), FadeIn(claim[1]), run_time=1.6)
        self.play(Create(found[0]), FadeIn(found[1]), run_time=1.6)
        self.wait(2.6)
        self.play(FadeIn(why), run_time=2.0)
        self.play(FadeIn(src), run_time=1.2)
        self.wait(2.4)
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=2.0)
            self.wait(2.6)
        self.wait(4.6)

        point = spark("Not the same bug")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(5.09)


class B08_WhatHeldUp(Scene):
    """what reproduced: every figure recounted independently. 33.42s."""

    def construct(self):
        page(self)
        head = kicker("WHAT SURVIVED THE RECOUNT",
                      "every figure re-derived from the committed artifacts")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup(
            tickrow("clean corpus:  12 records, 12 accepted, 0 rejected"),
            tickrow("defective:     10 planted, 10 rejected, 0 accepted"),
            tickrow("both runs declare mode: sample — nothing live"),
            tickrow("self-tests:    27/27 · 31/31 · 37/37 committed"),
            tickrow("lifecycle:     94 DRAFT + 3 RUNNABLE-SAMPLE = 97"),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        box = boxed(rows, accent=INK)

        note = chip("99 .md files in recipes/ — the other 2 are a README and a shared include",
                    TERRA, font_size=21, pad=0.40, height=0.52)

        body = fit_src(VGroup(box, note).arrange(DOWN, buff=0.40))
        src = source_line("recounted from the tree at 20795b2, read-only")

        self.play(Create(box[0]), run_time=1.0)
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), run_time=1.2)
            self.wait(0.9)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(3.0)
        self.play(Create(note[0]), FadeIn(note[1]), run_time=2.0)
        self.wait(6.0)

        point = spark("The counts land exactly")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(4.92)


class B09_WhySignIt(Scene):
    """SUMMARY: what a good sign-off does even on weak evidence. 29.37s."""

    def construct(self):
        page(self)
        head = kicker("SO WHY SIGN IT AT ALL",
                      "three things this promotion got right")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        r1 = panel("live stays blocked", ["no gate 5 approval record,", "and the status does not pretend"],
                   accent=INK, min_w=7.6, fs=19, title_fs=21)
        r2 = panel("recipe_version frozen at 0.4.0", ["so the evidence binds to the exact",
                                                      "text that was reviewed"],
                   accent=INK, min_w=7.6, fs=19, title_fs=21)
        r3 = panel("the next action changed", ["was:  promote this recipe",
                                               "now:  make its gate tests real"],
                   accent=TERRA, min_w=7.6, fs=19, title_fs=21)

        # The closing line is composed INTO the fitted group. Positioning it
        # absolutely with to_edge() put it inside the body band, on top of r3 --
        # GATE B caught it as a 100% text-on-text overlap.
        closing = Text("the promotion did not close an item — it opened a better one",
                       font=SANS, font_size=25, color=INK)
        body = fit_src(VGroup(r1, r2, r3, closing).arrange(DOWN, buff=0.30))
        src = source_line("session-handoff.md, before and after the promotion")

        self.play(Create(r1[0]), FadeIn(r1[1]), run_time=2.0)
        self.wait(1.6)
        self.play(Create(r2[0]), FadeIn(r2[1]), run_time=2.0)
        self.wait(1.6)
        self.play(Create(r3[0]), FadeIn(r3[1]), run_time=2.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(3.0)

        self.play(FadeIn(closing), run_time=2.0)
        self.wait(8.4)

        point = spark("Sign it, and say what is weak")
        self.play(FadeIn(point, shift=UP * 0.2), run_time=2.0)
        self.wait(2.47)
