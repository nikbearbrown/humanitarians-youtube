"""Manim beats for the reel `weekly-fixtures-before-validators`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json -- audio is
the master clock, never these numbers.

Every value on screen is verified against mycroft commit 9ef4e7f and a live run
of the verify-provenance script; see SOURCES.md / FACTCHECK.md. No LaTeX is used
anywhere here (no MathTex/Tex): dvisvgm is not installed, so Text/Pango only.

Palette is the Claude fidelity skin -- cream page, warm ink, ONE terracotta
accent. Never retint.

Layout: the safe area is +/-6.3 x, +/-3.4 y (GATE B). The kicker owns the top
~1.1 units and the spark line the bottom ~0.9, so body content lives between
BODY_TOP and BODY_BOTTOM and is SCALED to fit rather than trusted to fit.

PROOF note: B02_Method is the framework graphic. It lands at 19.05s -- before
any example -- and is the rubric every later beat is scored against.
"""

import glob
import os

import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, RoundedRectangle,
    Scene, Text, VGroup, Write,
)

# The toolkit's bundled brand fonts are not installed into the Windows font
# store; register them with Pango at runtime so Manim can use them anyway.
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
INK_SOFT = "#6B6559"   # never below ~40% opacity against cream
TERRA = "#D97757"      # the ONE accent

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    # buff 0.72 keeps the cap line inside the +/-3.4 safe box (GATE B warned at 0.55)
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(
        k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
        stroke_width=1.4, color=INK_SOFT,
    )
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=38, color=TERRA).to_edge(DOWN, buff=0.62)


def fit(group, w=BODY_W, h=BODY_H):
    """Scale a body group into the safe body band, then centre it there."""
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
        head = kicker("THE RECIPE", "recipes/market-sentiment-analysis-part-1.md")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Each step carries a HOLLOW status box: six boxes that never fill say
        # "none implemented" better than the words do.
        rows = VGroup()
        for num, name in self.STEPS:
            n = Text(num, font=SERIF, font_size=30, color=INK_SOFT)
            box = RoundedRectangle(
                width=0.34, height=0.34, corner_radius=0.06,
                stroke_width=2.0, stroke_color=INK_SOFT, fill_opacity=0,
            )
            label = Text(name, font=MONO, font_size=27, color=INK)
            tag = Text("[TODO: DEV]", font=MONO, font_size=22, color=TERRA)
            box.next_to(n, RIGHT, buff=0.38)
            label.next_to(box, RIGHT, buff=0.38)
            rows.add(VGroup(n, box, label, tag))
        widest = max(r[2].width for r in rows)
        for r in rows:
            r[3].next_to(r[2], RIGHT, buff=0.65 + (widest - r[2].width))
        rows.arrange(DOWN, buff=0.30, aligned_edge=LEFT)

        cells = VGroup(*[
            RoundedRectangle(width=1.35, height=0.28, corner_radius=0.05,
                             stroke_width=1.6, stroke_color=INK_SOFT, fill_opacity=0)
            for _ in self.STEPS
        ]).arrange(RIGHT, buff=0.12)
        fit(VGroup(rows, cells).arrange(DOWN, buff=0.55))

        for r in rows:
            self.play(Create(r[1]), FadeIn(VGroup(r[0], r[2], r[3]), shift=RIGHT * 0.26),
                      run_time=0.55)
        self.wait(0.6)
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.35), run_time=1.2)
        self.wait(0.5)

        point = spark("Six declared. Zero implemented.")
        self.play(Write(point), run_time=1.6)
        self.wait(2.97)


class B02_Method(Scene):
    """FRAMEWORK: the reusable four-step method. 18.15s.

    PROOF requires the organizing idea shown AS A STRUCTURE before any example.
    This beat starts at 19.05s in the cut -- ahead of the first fixture.
    The four cards are the axes a viewer applies to their own suite.
    """

    STEPS = [
        ("1", "ENUMERATE", "what kinds of wrong\ncan this data be?"),
        ("2", "PLANT", "one instance of each,\nwith an exact locator"),
        ("3", "NAME THE CATCHER", "which check must\nsurface it"),
        ("4", "FREEZE", "pin timestamps, so two\nruns stay comparable"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE METHOD", "run this on any validator suite")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, verb, rule in self.STEPS:
            n = Text(num, font=SERIF, font_size=34, color=TERRA)
            v = Text(verb, font=SANS, font_size=27, color=INK)
            r = Text(rule, font=MONO, font_size=21, color=INK_SOFT, line_spacing=0.7)
            head_row = VGroup(n, v).arrange(RIGHT, buff=0.32)
            inner = VGroup(head_row, r).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
            box = RoundedRectangle(
                width=5.5, height=inner.height + 0.85, corner_radius=0.12,
                stroke_width=1.8, stroke_color=INK_SOFT, fill_opacity=0,
            ).move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        grid = VGroup(*cards).arrange_in_grid(rows=2, cols=2, buff=(0.55, 0.5))
        fit(grid)

        # one card per narration step, so the structure assembles as it is named
        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.2)
            self.wait(1.6)

        point = spark("Gradeable, not merely runnable")
        self.play(Write(point), run_time=1.8)
        self.wait(4.25)


class B05_DefectCatalogue(Scene):
    """OUTPUT 1: 18 catalogued defects across 7 classes. 18.05s."""

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

        n = 0
        rows = VGroup()
        for name, count in self.CLASSES:
            label = Text(name, font=MONO, font_size=24, color=INK)
            chips = VGroup()
            for _ in range(count):
                n += 1
                chips.add(chip(f"D{n:02d}", INK_SOFT, font_size=19, pad=0.30, height=0.34))
            chips.arrange(RIGHT, buff=0.18)
            rows.add(VGroup(label, chips))
        width = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.45 + (width - r[0].width))
        rows.arrange(DOWN, buff=0.26, aligned_edge=LEFT)

        total = Text("18 defects  ·  7 classes", font=SERIF, font_size=34, color=INK)
        fit(VGroup(rows, total).arrange(DOWN, buff=0.45))

        # structure first (all seven class labels), then the data resolves into it
        self.play(
            LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.2) for r in rows], lag_ratio=0.12),
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


class B08_ProvenanceRun(Scene):
    """OUTPUT 2: the real verify-provenance run over 14 declared sources. 18.84s.

    Two columns of seven -- fourteen single-column rows overflow the safe box.
    Paths are shortened for legibility; the full paths are listed in SOURCES.md.
    """

    SOURCES = [
        ("recipes/…part-1.md", "PRESENT"),
        ("conductor/…part-1.md", "PRESENT"),
        ("originals/market_sentiment.json", "OK"),
        ("sample/fixture-manifest.json", "OK"),
        ("sample/FIXTURE_MANIFEST.md", "PRESENT"),
        ("clean/price-alpha-vantage.json", "OK"),
        ("clean/news-finnhub.json", "OK"),
        ("clean/reddit-wallstreetbets.json", "OK"),
        ("defective/price-alpha-vantage.json", "OK"),
        ("defective/news-finnhub.json", "OK"),
        ("defective/reddit-wallstreetbets.json", "OK"),
        ("defective/…unparseable.json.broken", "UNPARSEABLE"),
        ("raw/run-envelope.json", "MISSING"),
        ("gate-decisions/…approval.json", "MISSING"),
    ]

    def construct(self):
        page(self)
        head = kicker("STEP 1 — VERIFY PROVENANCE",
                      "existence · size · sha256 · parseability")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(entries):
            rows = VGroup()
            for path, verdict in entries:
                accent = TERRA if verdict == "MISSING" else INK_SOFT
                p = Text(path, font=MONO, font_size=17, color=INK)
                rows.add(VGroup(p, chip(verdict, accent, font_size=15,
                                        pad=0.26, height=0.30)))
            col = max(r[0].width for r in rows)
            for r in rows:
                r[1].next_to(r[0], RIGHT, buff=0.35 + (col - r[0].width))
            return rows.arrange(DOWN, buff=0.19, aligned_edge=LEFT)

        left, right = column(self.SOURCES[:7]), column(self.SOURCES[7:])
        cols = VGroup(left, right).arrange(RIGHT, buff=0.75, aligned_edge=UP)

        segs = [(8, INK), (3, INK_SOFT), (1, INK_SOFT), (2, TERRA)]
        bar = VGroup(*[
            RoundedRectangle(width=count * 0.62, height=0.34, corner_radius=0.05,
                             stroke_width=1.8, stroke_color=color, fill_opacity=0)
            for count, color in segs
        ]).arrange(RIGHT, buff=0.09)
        caption = Text("8 parse clean · 3 present · 1 unparseable as declared · 2 absent",
                       font=SANS, font_size=21, color=INK)
        tally = VGroup(bar, caption).arrange(DOWN, buff=0.24)
        fit(VGroup(cols, tally).arrange(DOWN, buff=0.5))

        # the manifest of what WILL be checked, then each row resolves to a verdict
        self.play(
            LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.15) for r in left], lag_ratio=0.1),
            LaggedStart(*[FadeIn(r[0], shift=RIGHT * 0.15) for r in right], lag_ratio=0.1),
            run_time=1.5,
        )
        self.wait(0.4)
        for a, b in zip(left, right):
            self.play(Create(a[1][0]), FadeIn(a[1][1]),
                      Create(b[1][0]), FadeIn(b[1][1]), run_time=0.55)
        self.wait(1.0)
        self.play(LaggedStart(*[Create(s) for s in bar], lag_ratio=0.4), run_time=1.4)
        self.play(FadeIn(caption), run_time=0.8)
        self.wait(0.8)

        stop = spark("A missing required source exits 1")
        self.play(FadeIn(stop, shift=UP * 0.2), run_time=1.5)
        self.wait(6.69)


class B09_WrongEntity(Scene):
    """FALSIFIABILITY: the case that breaks the method. 17.77s.

    The four passing checks and the failing verdict are on screen TOGETHER and
    held, so the comparison is visible at the moment it is asserted (PROOF
    production gate: side-by-side at the moment of comparison).
    """

    CHECKS = ["well-formed", "fresh", "unique", "required fields complete"]

    def construct(self):
        page(self)
        head = kicker("WHAT THE METHOD CANNOT ENUMERATE",
                      "fixture-manifest.json → not_covered")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        row = Text('{ "ticker": "FAKE", "headline": "…", "ts": "2026-08-27" }',
                   font=MONO, font_size=23, color=INK)
        card = RoundedRectangle(
            width=row.width + 1.0, height=1.15, corner_radius=0.12,
            stroke_width=1.8, stroke_color=INK_SOFT, fill_opacity=0,
        ).move_to(row.get_center())
        record = VGroup(card, row)

        checks = VGroup()
        for c in self.CHECKS:
            mark = Text("✓", font=SANS, font_size=27, color=INK_SOFT)
            label = Text(c, font=SANS, font_size=25, color=INK_SOFT)
            label.next_to(mark, RIGHT, buff=0.30)
            checks.add(VGroup(mark, label))
        checks.arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        wrong = Text("…but it is the\nwrong company", font=SERIF, font_size=38,
                     color=TERRA, line_spacing=0.8)
        verdict_box = RoundedRectangle(
            width=wrong.width + 0.7, height=wrong.height + 0.5, corner_radius=0.12,
            stroke_width=2.0, stroke_color=TERRA, fill_opacity=0,
        ).move_to(wrong.get_center())
        verdict = VGroup(verdict_box, wrong)

        lower = VGroup(checks, verdict).arrange(RIGHT, buff=1.2)
        fit(VGroup(record, lower).arrange(DOWN, buff=0.6))

        self.play(Create(card), FadeIn(row), run_time=1.4)
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.28) for c in checks], lag_ratio=0.6),
            run_time=3.6,
        )
        self.wait(1.0)
        self.play(Create(verdict_box), Write(wrong), run_time=2.0)
        self.wait(1.0)

        note = spark("No shape check finds this one")
        self.play(FadeIn(note, shift=UP * 0.2), run_time=1.5)
        self.wait(6.37)


class B10_WeekLedger(Scene):
    """SUMMARY: what shipped, what is still open. 12.37s."""

    SHIPPED = ["10 files", "≈1,200 lines", "step 1 of 6 closed",
               "18/18 defect locators resolve"]
    OPEN = ["5 steps unwritten", "run-envelope.json absent",
            "gate 2 cannot clear", "6 TODO markers still stand"]

    def construct(self):
        page(self)
        head = kicker("THE WEEK", "mycroft · commit 9ef4e7f")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        def column(title, items, color):
            t = Text(title, font=SANS, font_size=25, color=INK_SOFT)
            body = VGroup(*[Text(i, font=MONO, font_size=23, color=color)
                            for i in items])
            body.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
            rule = Line(LEFT * (max(body.width, t.width) / 2),
                        RIGHT * (max(body.width, t.width) / 2),
                        stroke_width=1.3, color=INK_SOFT)
            col = VGroup(t, rule, body).arrange(DOWN, buff=0.26)
            for part in (t, rule, body):
                part.align_to(col, LEFT)
            return col

        left = column("SHIPPED", self.SHIPPED, INK)
        right = column("STILL OPEN", self.OPEN, TERRA)
        fit(VGroup(left, right).arrange(RIGHT, buff=1.5, aligned_edge=UP))

        self.play(FadeIn(left, shift=UP * 0.2), run_time=1.6)
        self.wait(1.4)
        self.play(FadeIn(right, shift=UP * 0.2), run_time=1.6)
        self.wait(1.2)

        point = spark("One of six. Openly.")
        self.play(Write(point), run_time=1.7)
        self.wait(3.97)
