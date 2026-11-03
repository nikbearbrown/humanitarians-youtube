"""Portrait 9:16 Manim beats for the SHORT cut of `weekly-fixtures-before-validators`.

Four beats survive the cut: B01 PROBLEM, B02 FRAMEWORK, B05 OUTPUT,
B09 FALSIFIABILITY. The bookends (B00, B12) are Remotion 916 compositions.

These are RE-LAID-OUT, not re-timed. The audio is unchanged from the parent
reel, so every run_time and wait below is copied verbatim from the landscape
scenes.py -- audio is the master clock and the short reuses the parent's mp3s.
Only geometry changes.

THE PORTRAIT FRAME: manim renders 9:16 at 2160x3840, which is a 4.5 x 8 frame
(x +/-2.25, y +/-4.0); GATE B's title-safe box inside that is +/-1.95 x,
+/-3.4 y -- a THIRD of the landscape width. Nothing that was a row
in the landscape cut survives as a row here:

    landscape                    portrait
    2x2 card grid (B02)   ->     4 cards stacked in one column
    label + chips row     ->     label ABOVE its chips
    checks | verdict      ->     checks ABOVE verdict

The B09 side-by-side is preserved in substance: both the passing checks and the
failing verdict are on screen TOGETHER and held to the end of the beat, which
is what the PROOF production gate asks for. Only the axis changed.

Palette is the Claude fidelity skin -- cream page, warm ink, ONE terracotta
accent. Never retint. No LaTeX anywhere (dvisvgm absent): Text/Pango only.
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, RoundedRectangle,
    Scene, Text, VGroup, Write, config,
)

# THE PORTRAIT FRAME MUST BE DECLARED. Given `-r 2160,3840` alone, manim keeps
# the landscape frame_width (14.22) and stretches the frame anisotropically —
# the authored layout then renders as a squashed band in the middle of the
# canvas. Setting both explicitly gives a true 4.5 x 8 frame at ~477 px/unit
# on both axes, which is what every coordinate below assumes.
config.frame_width = 4.5
config.frame_height = 8.0

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR", "D:/Projects/brutalist.art/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"   # never below ~40% opacity against cream
TERRA = "#D97757"      # the ONE accent

# Portrait safe band. The kicker owns the top ~1.2 units and the spark line the
# bottom ~0.9, so the body lives between these and is SCALED to fit.
BODY_TOP = 2.35        # clears the kicker subtitle, which bottoms out at 2.55
BODY_BOTTOM = -2.85
BODY_W = 3.8           # GATE B safe half-width is +/-1.95, so 3.9 is the ceiling
BODY_H = BODY_TOP - BODY_BOTTOM


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    """Same anatomy as the landscape kicker, but the rule spans a 4.5 frame."""
    k = Text(text, font=SANS, font_size=19, color=INK_SOFT)
    # a kicker headline that fits landscape can run clean off a 4.5-wide frame;
    # clamp BEFORE positioning so the rule still starts at the text's left edge
    if k.width > 3.7:
        k.scale_to_fit_width(3.7)
    k.to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.32)
    rule = Line(
        k.get_left() + DOWN * 0.26, k.get_left() + RIGHT * 3.7 + DOWN * 0.26,
        stroke_width=1.4, color=INK_SOFT,
    )
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=15, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.18).align_to(k, LEFT)
        if s.width > 3.7:
            s.scale_to_fit_width(3.7)
        grp.add(s)
    return grp


def spark(text):
    t = Text(text, font=SERIF, font_size=31, color=TERRA).to_edge(DOWN, buff=0.62)
    if t.width > BODY_W:
        t.scale_to_fit_width(BODY_W)
    return t


def fit(group, w=BODY_W, h=BODY_H):
    """Scale a body group into the portrait safe band, then centre it there."""
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + BODY_BOTTOM) / 2, 0])
    return group


def chip(label, color, font_size=19, pad=0.34, height=0.36):
    t = Text(label, font=MONO, font_size=font_size, color=color)
    box = RoundedRectangle(
        width=t.width + pad, height=height, corner_radius=0.07,
        stroke_width=1.5, stroke_color=color, fill_opacity=0,
    ).move_to(t.get_center())
    return VGroup(box, t)


class B01_TodoSteps(Scene):
    """PROBLEM: six declared steps, none implemented. 11.07s."""

    STEPS = [
        ("1", "verify-provenance"),
        ("2", "ingest-inputs"),
        ("3", "validate-data-shape"),
        ("4", "transform-quality-check"),
        ("5", "run-approved-tools"),
        ("6", "produce-human-report"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE RECIPE", "market-sentiment-analysis-part-1.md")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Six HOLLOW status boxes that never fill say "none implemented" better
        # than the words do. In portrait the [TODO: DEV] tag cannot ride on the
        # same line as the longest step name, so it becomes a trailing column.
        rows = VGroup()
        for num, name in self.STEPS:
            n = Text(num, font=SERIF, font_size=24, color=INK_SOFT)
            box = RoundedRectangle(
                width=0.30, height=0.30, corner_radius=0.06,
                stroke_width=2.0, stroke_color=INK_SOFT, fill_opacity=0,
            )
            label = Text(name, font=MONO, font_size=20, color=INK)
            tag = Text("TODO", font=MONO, font_size=16, color=TERRA)
            box.next_to(n, RIGHT, buff=0.26)
            label.next_to(box, RIGHT, buff=0.26)
            rows.add(VGroup(n, box, label, tag))
        widest = max(r[2].width for r in rows)
        for r in rows:
            r[3].next_to(r[2], RIGHT, buff=0.34 + (widest - r[2].width))
        rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT)

        # the empty ledger: six cells, nothing in any of them
        cells = VGroup(*[
            RoundedRectangle(width=0.58, height=0.26, corner_radius=0.05,
                             stroke_width=1.6, stroke_color=INK_SOFT, fill_opacity=0)
            for _ in self.STEPS
        ]).arrange(RIGHT, buff=0.10)
        fit(VGroup(rows, cells).arrange(DOWN, buff=0.60))

        for r in rows:
            self.play(Create(r[1]), FadeIn(VGroup(r[0], r[2], r[3]), shift=RIGHT * 0.10),
                      run_time=0.55)
        self.wait(0.6)
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.35), run_time=1.2)
        self.wait(0.5)

        point = spark("Six declared. Zero implemented.")
        self.play(Write(point), run_time=1.6)
        self.wait(2.97)


class B02_Method(Scene):
    """FRAMEWORK: the reusable four-step method. 18.15s.

    The hero beat of the short. PROOF requires the organizing idea shown AS A
    STRUCTURE before any example; in portrait the 2x2 grid becomes a single
    column, which also matches the way the narration counts them off.
    """

    STEPS = [
        ("1", "ENUMERATE", "what kinds of wrong can this data be?"),
        ("2", "PLANT", "one instance of each, with an exact locator"),
        ("3", "NAME THE CATCHER", "which check must surface it"),
        ("4", "FREEZE", "pin timestamps, so two runs stay comparable"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE METHOD", "run this on any validator suite")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, verb, rule in self.STEPS:
            n = Text(num, font=SERIF, font_size=26, color=TERRA)
            v = Text(verb, font=SANS, font_size=21, color=INK)
            r = Text(rule, font=MONO, font_size=15, color=INK_SOFT, line_spacing=0.7)
            if r.width > 3.05:
                r.scale_to_fit_width(3.05)
            head_row = VGroup(n, v).arrange(RIGHT, buff=0.26)
            inner = VGroup(head_row, r).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            # never narrower than its own content — a fixed width smaller than
            # the text puts the text across the border stroke (GATE B)
            box = RoundedRectangle(
                width=max(3.55, inner.width + 0.5), height=inner.height + 0.55,
                corner_radius=0.12, stroke_width=1.8, stroke_color=INK_SOFT,
                fill_opacity=0,
            ).move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(DOWN, buff=0.30))

        # one card per narration step, so the structure assembles as it is named
        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.2)
            self.wait(1.6)

        point = spark("Gradeable, not merely runnable")
        self.play(Write(point), run_time=1.8)
        self.wait(4.25)


class B05_DefectCatalogue(Scene):
    """OUTPUT: 18 catalogued defects across 7 classes. 18.05s."""

    CLASSES = [
        ("duplicate", 4),
        ("missing_required_field", 4),
        ("type_violation", 3),
        ("stale_timestamp", 3),
        ("malformed_row", 2),
        ("count_mismatch", 1),
        ("unparseable_file", 1),
    ]

    def construct(self):
        page(self)
        head = kicker("THE DEFECT CATALOGUE", "sample/fixture-manifest.json")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Portrait: the class label sits ABOVE its chips rather than beside them.
        # `missing_required_field` plus four chips is wider than the whole frame.
        n = 0
        rows = VGroup()
        for name, count in self.CLASSES:
            label = Text(name, font=MONO, font_size=17, color=INK)
            chips = VGroup()
            for _ in range(count):
                n += 1
                chips.add(chip(f"D{n:02d}", INK_SOFT, font_size=15, pad=0.24, height=0.28))
            chips.arrange(RIGHT, buff=0.14)
            rows.add(VGroup(label, chips).arrange(DOWN, buff=0.13, aligned_edge=LEFT))
        rows.arrange(DOWN, buff=0.24, aligned_edge=LEFT)

        total = Text("18 defects  ·  7 classes", font=SERIF, font_size=27, color=INK)
        fit(VGroup(rows, total).arrange(DOWN, buff=0.40))

        # structure first (all seven class labels), then the data resolves into it
        self.play(
            LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.08) for r in rows], lag_ratio=0.12),
            run_time=1.2,
        )
        self.play(
            LaggedStart(*[
                LaggedStart(*[Create(c[0]) for c in r[1]],
                            *[FadeIn(c[1]) for c in r[1]], lag_ratio=0.22)
                for r in rows
            ], lag_ratio=0.5),
            run_time=4.0,
        )
        self.wait(1.4)
        self.play(Write(total), run_time=1.6)
        self.wait(1.0)

        pin = spark("Pinned to frozen_at, never now()")
        self.play(FadeIn(pin, shift=UP * 0.2), run_time=1.6)
        self.wait(6.35)


class B09_WrongEntity(Scene):
    """FALSIFIABILITY: the case that breaks the method. 17.77s.

    The four passing checks and the failing verdict are on screen TOGETHER and
    held to the end of the beat, so the comparison is visible at the moment it
    is asserted (PROOF production gate). Portrait stacks them instead of
    placing them side by side; both are still simultaneously on screen.
    """

    CHECKS = ["well-formed", "fresh", "unique", "required fields complete"]

    def construct(self):
        page(self)
        head = kicker("CANNOT BE ENUMERATED",
                      "fixture-manifest.json → not_covered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # the record wraps to three lines — one line is far wider than the frame
        row = Text('{ "ticker": "FAKE",\n  "headline": "…",\n  "ts": "2026-08-27" }',
                   font=MONO, font_size=18, color=INK, line_spacing=0.7)
        card = RoundedRectangle(
            width=row.width + 0.6, height=row.height + 0.5, corner_radius=0.12,
            stroke_width=1.8, stroke_color=INK_SOFT, fill_opacity=0,
        ).move_to(row.get_center())
        record = VGroup(card, row)

        checks = VGroup()
        for c in self.CHECKS:
            mark = Text("✓", font=SANS, font_size=21, color=INK_SOFT)
            label = Text(c, font=SANS, font_size=19, color=INK_SOFT)
            label.next_to(mark, RIGHT, buff=0.24)
            checks.add(VGroup(mark, label))
        checks.arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        wrong = Text("…but it is the\nwrong company", font=SERIF, font_size=29,
                     color=TERRA, line_spacing=0.8)
        verdict_box = RoundedRectangle(
            width=wrong.width + 0.6, height=wrong.height + 0.45, corner_radius=0.12,
            stroke_width=2.0, stroke_color=TERRA, fill_opacity=0,
        ).move_to(wrong.get_center())
        verdict = VGroup(verdict_box, wrong)

        fit(VGroup(record, checks, verdict).arrange(DOWN, buff=0.45))

        self.play(Create(card), FadeIn(row), run_time=1.4)
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.10) for c in checks], lag_ratio=0.6),
            run_time=3.6,
        )
        self.wait(1.0)
        self.play(Create(verdict_box), Write(wrong), run_time=2.0)
        self.wait(1.0)

        note = spark("No shape check finds this one")
        self.play(FadeIn(note, shift=UP * 0.2), run_time=1.5)
        self.wait(6.37)
