"""vox_scenes.py — Why the Script Made the Extemporization Possible
(vox-script-extemporization, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is own. STILL beats (B01
archive, B09 ai) have no scene here — they compile as slates until the
human fills media/. Durations read from this reel's beat_sheet.json
(actuals after audio lock; estimates as fallback).

Color law (teardown palette):
  CRIMSON (#C8102E) = the page-prose form that fails the ear
  INK     (#2A1A0E) = the spoken / ear-adapted technique (TEAL = INK in teardown)
  GOLD    = fill only, once per graphic — never text
  SLATE   = structure / neutral scaffolding

Gate conventions:
  - Single-method .animate chains only (no chained .animate.set_X().set_Y())
  - Every scene has real shape motion (Grow/Create/Transform/shift/scale)
  - Zero-width strokes also zero-opacity
  - Font-safe glyphs: no arrows, checks, not-equal, multiply-sign in strings
  - GOLD never as text color (W1)
  - No chapter number or book title on screen (W7)
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 10.0, "B03": 13.0, "B04": 11.0, "B05": 11.0, "B06": 12.0,
    "B07": 12.0, "B08": 13.0, "B10": 13.0, "B11": 14.0, "B12": 13.0,
    "B13": 13.0, "B14": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _pill(text, color=INK, size=26):
    """A rounded chip label in the given color with white text."""
    return LabelChip(text, accent=color, size=size)


def _line_bar(color=CRIMSON, width=5.5, height=0.28):
    """A single filled row-bar representing a sentence or clause."""
    b = Rectangle(width=width, height=height)
    b.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return b


def _sentence_block(n, color, width=5.5, height=0.28, gap=0.16):
    """Stack of n sentence-bars."""
    bars = VGroup(*[_line_bar(color, width, height) for _ in range(n)])
    bars.arrange(DOWN, buff=gap)
    return bars


# ---------------------------------------------------------------- scenes

class B02_UsualStory(Scene):
    """COLD OPEN — the usual story: inspiration struck."""
    def construct(self):
        total = DUR["B02"]
        eye = Text("WRITING", font=DISPLAY, color=SLATE,
                   font_size=22, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        label_usual = Text("The usual story", font=SERIF,
                           color=INK, font_size=46, slant=ITALIC)
        label_inspo = Text("inspiration struck", font=SERIF,
                           color=CRIMSON, font_size=38)
        block = VGroup(label_usual, label_inspo).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN + DOWN * 0.1)

        u = Line(label_usual.get_corner(DL) + DOWN * 0.12,
                 label_usual.get_corner(DR) + DOWN * 0.12,
                 stroke_width=1.8, color=SLATE)

        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(label_usual), Create(u), run_time=0.9)
        self.play(FadeIn(label_inspo, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 2.2))


class B03_TheQuestion(Scene):
    """THE QUESTION — page vs. ear: why different architecture?"""
    def construct(self):
        total = DUR["B03"]

        # Two column headers
        page_label = _pill("PAGE", CRIMSON, size=28)
        ear_label = _pill("EAR", INK, size=28)
        VGroup(page_label, ear_label).arrange(RIGHT, buff=3.8)
        VGroup(page_label, ear_label).to_edge(UP, buff=0.9)

        # Divider
        divider = Line(UP * 3.0, DOWN * 1.8,
                       stroke_width=2, color=SLATE)
        divider.move_to(ORIGIN + UP * 0.6)

        # The question
        q1 = Text("Why does writing for the ear", font=SERIF,
                  color=INK, font_size=32)
        q2 = Text("require a different architecture?", font=SERIF,
                  color=INK, font_size=32)
        question = VGroup(q1, q2).arrange(DOWN, buff=0.18)
        question.move_to(DOWN * 2.0)

        self.play(FadeIn(page_label, shift=RIGHT * 0.3),
                  FadeIn(ear_label, shift=LEFT * 0.3), run_time=0.8)
        self.play(Create(divider), run_time=0.6)
        self.play(FadeIn(q1), run_time=0.7)
        self.play(FadeIn(q2, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.8))


class B04_CannotReread(Scene):
    """THE PROBLEM — reader can go back; listener cannot."""
    def construct(self):
        total = DUR["B04"]

        # Page column — has a back-arrow (shown as "<-" text in SERIF)
        page_head = _pill("PAGE", CRIMSON, size=26)
        page_head.move_to(LEFT * 3.2 + UP * 2.5)

        # Sentence bars for page reader
        page_bars = _sentence_block(3, CRIMSON, width=3.6)
        page_bars.move_to(LEFT * 3.2 + UP * 0.3)

        # Back arrow label (text, not a glyph arrow)
        back_label = Text("re-read", font=SERIF, color=CRIMSON,
                          font_size=26, slant=ITALIC)
        back_label.next_to(page_bars, DOWN, buff=0.4)
        back_box = SurroundingRectangle(back_label, buff=0.12,
                                        color=CRIMSON, stroke_width=2)
        back_box.set_fill(opacity=0).set_stroke(CRIMSON, 2)

        # Ear column — one-way only
        ear_head = _pill("EAR", INK, size=26)
        ear_head.move_to(RIGHT * 3.2 + UP * 2.5)

        ear_bars = _sentence_block(3, INK, width=3.6)
        ear_bars.move_to(RIGHT * 3.2 + UP * 0.3)

        gone_label = Text("gone", font=SERIF, color=SLATE,
                          font_size=26, slant=ITALIC)
        gone_label.next_to(ear_bars, DOWN, buff=0.4)

        # Divider
        div = Line(UP * 3.2, DOWN * 2.5,
                   stroke_width=1.6, color=SLATE)
        div.set_opacity(0.4)
        div.move_to(ORIGIN)

        self.play(FadeIn(page_head, shift=DOWN * 0.15),
                  FadeIn(ear_head, shift=DOWN * 0.15), run_time=0.6)
        self.play(Create(div), run_time=0.4)
        self.play(LaggedStart(
            *[FadeIn(b, shift=RIGHT * 0.2) for b in page_bars],
            lag_ratio=0.18, run_time=1.0))
        self.play(FadeIn(back_label), Create(back_box), run_time=0.7)
        self.play(LaggedStart(
            *[FadeIn(b, shift=LEFT * 0.2) for b in ear_bars],
            lag_ratio=0.18, run_time=1.0))
        self.play(FadeIn(gone_label, scale=0.85), run_time=0.6)
        self.wait(max(0.5, total - 4.3))


class B05_WorkingMemory(Scene):
    """THE PROBLEM — working memory as the bottleneck."""
    def construct(self):
        total = DUR["B05"]

        # Working memory container
        wm_box = Rectangle(width=8.0, height=1.4)
        wm_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 2)
        wm_box.move_to(ORIGIN)
        wm_label = Text("working memory", font=DISPLAY,
                        color=SLATE, font_size=24, weight="MEDIUM")
        wm_label.next_to(wm_box, UP, buff=0.25)

        # Arriving sentence bar
        arriving = _line_bar(INK, width=4.5, height=0.55)
        arriving.move_to(LEFT * 6.5 + ORIGIN)

        # Fade-out fragment (what gets dropped)
        faded_bar = _line_bar(CRIMSON, width=2.2, height=0.55)
        faded_bar.move_to(ORIGIN + RIGHT * 1.6)
        faded_bar.set_opacity(0)

        lost_label = Text("lost", font=SERIF, color=CRIMSON,
                          font_size=28, slant=ITALIC)
        lost_label.next_to(faded_bar, DOWN, buff=0.35)
        lost_label.set_opacity(0)

        constraint = SerifLabel("listeners cannot re-read", CRIMSON, size=28)
        constraint.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(wm_label), Create(wm_box), run_time=0.8)
        # Sentence arrives into working memory
        self.play(arriving.animate.move_to(ORIGIN + LEFT * 1.8), run_time=1.0)
        # Next sentence pushes it — fragment fades
        self.play(arriving.animate.move_to(ORIGIN + LEFT * 3.0),
                  faded_bar.animate.set_opacity(1),
                  lost_label.animate.set_opacity(1),
                  run_time=1.0)
        self.play(faded_bar.animate.set_opacity(0.15),
                  run_time=0.7)
        self.play(FadeIn(constraint, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 4.2))


class B06_SentenceLength(Scene):
    """THE MECHANISM — technique 1: sentence length."""
    def construct(self):
        total = DUR["B06"]

        # Technique chip
        chip = _pill("TECHNIQUE 1", SLATE, size=22)
        chip.to_corner(UL, buff=0.6)
        label_t = Text("Sentence length", font=DISPLAY,
                       color=INK, font_size=32, weight="MEDIUM")
        label_t.next_to(chip, DOWN, buff=0.3, aligned_edge=LEFT)

        # Long page-form sentence — 5 bars wide, crimson
        long_bars = _sentence_block(1, CRIMSON, width=8.5, height=0.38)
        long_bars.move_to(UP * 0.8)
        page_chip = _pill("PAGE", CRIMSON, size=20)
        page_chip.next_to(long_bars, LEFT, buff=0.35)

        # Short spoken-form — 1 bar + 2 short bars, ink
        short_bar1 = _line_bar(INK, width=3.5, height=0.38)
        short_bar2 = _line_bar(INK, width=2.8, height=0.38)
        short_bar3 = _line_bar(INK, width=3.2, height=0.38)
        spoken = VGroup(short_bar1, short_bar2, short_bar3)
        spoken.arrange(DOWN, buff=0.2)
        spoken.move_to(DOWN * 1.2)
        ear_chip = _pill("EAR", INK, size=20)
        ear_chip.next_to(spoken, LEFT, buff=0.35)

        self.play(FadeIn(chip), FadeIn(label_t), run_time=0.7)
        self.play(FadeIn(long_bars, shift=RIGHT * 0.3),
                  FadeIn(page_chip), run_time=0.8)
        # Long bar "breaks" — scale down and split
        self.play(long_bars.animate.scale(0.55), run_time=0.9)
        self.play(FadeIn(spoken, shift=UP * 0.3),
                  FadeIn(ear_chip), run_time=0.9)
        self.wait(max(0.5, total - 3.3))


class B07_Repetition(Scene):
    """THE MECHANISM — technique 2: repetition as structural necessity."""
    def construct(self):
        total = DUR["B07"]

        chip = _pill("TECHNIQUE 2", SLATE, size=22)
        chip.to_corner(UL, buff=0.6)
        label_t = Text("Repetition", font=DISPLAY,
                       color=INK, font_size=32, weight="MEDIUM")
        label_t.next_to(chip, DOWN, buff=0.3, aligned_edge=LEFT)

        # Three sentence lines with a shared opening phrase
        anchor_w = 2.4
        anchor1 = Rectangle(width=anchor_w, height=0.32)
        anchor1.set_fill(INK, 1).set_stroke(width=0, opacity=0)
        anchor2 = anchor1.copy()
        anchor3 = anchor1.copy()

        tail1 = _line_bar(SLATE, width=3.6, height=0.32)
        tail2 = _line_bar(SLATE, width=2.9, height=0.32)
        tail3 = _line_bar(SLATE, width=3.2, height=0.32)

        row1 = VGroup(anchor1, tail1).arrange(RIGHT, buff=0.18)
        row2 = VGroup(anchor2, tail2).arrange(RIGHT, buff=0.18)
        row3 = VGroup(anchor3, tail3).arrange(RIGHT, buff=0.18)
        rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.35)
        rows.move_to(DOWN * 0.3)

        # Labels
        struct_label = SerifLabel("structural", INK, size=26)
        struct_label.to_edge(RIGHT, buff=0.9).align_to(rows, UP)

        page_bad = _pill("PAGE: padding", CRIMSON, size=20)
        page_bad.to_corner(DR, buff=0.7)

        self.play(FadeIn(chip), FadeIn(label_t), run_time=0.7)
        self.play(LaggedStart(
            FadeIn(row1, shift=RIGHT * 0.3),
            FadeIn(row2, shift=RIGHT * 0.3),
            FadeIn(row3, shift=RIGHT * 0.3),
            lag_ratio=0.3, run_time=1.2))
        self.play(FadeIn(struct_label, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(page_bad, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


class B08_ConcreteAbstract(Scene):
    """THE MECHANISM — technique 3: concrete over abstract."""
    def construct(self):
        total = DUR["B08"]

        chip = _pill("TECHNIQUE 3", SLATE, size=22)
        chip.to_corner(UL, buff=0.6)
        label_t = Text("Concrete language", font=DISPLAY,
                       color=INK, font_size=32, weight="MEDIUM")
        label_t.next_to(chip, DOWN, buff=0.3, aligned_edge=LEFT)

        # Abstract sentence bar — wide, crimson, partially transparent
        abstract_bar = _line_bar(CRIMSON, width=9.0, height=0.52)
        abstract_bar.move_to(UP * 0.9)
        abstract_chip = _pill("abstract", CRIMSON, size=20)
        abstract_chip.next_to(abstract_bar, LEFT, buff=0.35)

        blur_label = Text("arrives as a blur", font=SERIF,
                          color=CRIMSON, font_size=26, slant=ITALIC)
        blur_label.next_to(abstract_bar, DOWN, buff=0.3)

        # Concrete replacement — three short bars, ink
        conc1 = _line_bar(INK, width=3.8, height=0.38)
        conc2 = _line_bar(INK, width=2.6, height=0.38)
        conc3 = _line_bar(INK, width=3.1, height=0.38)
        concrete = VGroup(conc1, conc2, conc3).arrange(DOWN, buff=0.18)
        concrete.move_to(DOWN * 1.5)
        conc_chip = _pill("concrete", INK, size=20)
        conc_chip.next_to(concrete, LEFT, buff=0.35)

        lands_label = Text("enters and lands", font=SERIF,
                           color=INK, font_size=26, slant=ITALIC)
        lands_label.next_to(concrete, DOWN, buff=0.3)

        self.play(FadeIn(chip), FadeIn(label_t), run_time=0.7)
        self.play(FadeIn(abstract_bar, shift=RIGHT * 0.3),
                  FadeIn(abstract_chip), run_time=0.8)
        self.play(FadeIn(blur_label, scale=0.9), run_time=0.6)
        # Abstract bar fades to near-transparent (blur effect)
        self.play(abstract_bar.animate.set_opacity(0.22), run_time=0.8)
        self.play(FadeIn(concrete, shift=UP * 0.3),
                  FadeIn(conc_chip), run_time=0.8)
        self.play(FadeIn(lands_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.3))


class B10_GettysburgDiagram(Scene):
    """THE IMPLICATION — Gettysburg passage annotated as engineering."""
    def construct(self):
        total = DUR["B10"]

        # The three lines of the Gettysburg passage
        line1 = Text("we cannot dedicate", font=SERIF, color=INK, font_size=36)
        line2 = Text("we cannot consecrate", font=SERIF, color=INK, font_size=36)
        line3 = Text("we cannot hallow", font=SERIF, color=INK, font_size=36)
        lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        lines.move_to(LEFT * 1.5 + UP * 0.2)

        # Repetition bracket/label — a vertical line on the left + label
        rep_line = Line(
            line1.get_corner(UL) + LEFT * 0.5 + UP * 0.1,
            line3.get_corner(DL) + LEFT * 0.5 + DOWN * 0.1,
            stroke_width=3, color=CRIMSON)
        rep_label = Text("REPETITION", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        rep_label.next_to(rep_line, LEFT, buff=0.25)

        # Parallelism bracket — vertical line on the right
        par_line = Line(
            line1.get_corner(UR) + RIGHT * 0.5 + UP * 0.1,
            line3.get_corner(DR) + RIGHT * 0.5 + DOWN * 0.1,
            stroke_width=3, color=INK)
        par_label = Text("PARALLELISM", font=DISPLAY, color=INK,
                         font_size=20, weight="MEDIUM")
        par_label.next_to(par_line, RIGHT, buff=0.25)

        # Cadence stress marks — dots under stressed syllables (key verbs)
        def _dot(obj):
            d = Dot(radius=0.09).set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
            d.next_to(obj, DOWN, buff=0.12)
            return d

        dot1 = _dot(line1)
        dot2 = _dot(line2)
        dot3 = _dot(line3)
        cadence_label = Text("CADENCE", font=DISPLAY, color=SLATE,
                             font_size=20, weight="MEDIUM")
        cadence_label.next_to(VGroup(dot1, dot2, dot3), DOWN, buff=0.35)

        self.play(LaggedStart(
            FadeIn(line1, shift=RIGHT * 0.3),
            FadeIn(line2, shift=RIGHT * 0.3),
            FadeIn(line3, shift=RIGHT * 0.3),
            lag_ratio=0.3, run_time=1.2))
        self.play(Create(rep_line), FadeIn(rep_label, shift=RIGHT * 0.2),
                  run_time=0.8)
        self.play(Create(par_line), FadeIn(par_label, shift=LEFT * 0.2),
                  run_time=0.8)
        self.play(LaggedStart(
            FadeIn(dot1, scale=0.7),
            FadeIn(dot2, scale=0.7),
            FadeIn(dot3, scale=0.7),
            lag_ratio=0.3, run_time=0.9))
        self.play(FadeIn(cadence_label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.3))


class B11_Transform1(Scene):
    """THE EXAMPLE — transform step 1: shorten the page-prose sentence."""
    def construct(self):
        total = DUR["B11"]

        step_chip = _pill("STEP 1: SHORTEN", SLATE, size=22)
        step_chip.to_corner(UL, buff=0.6)

        # Page-form: one very long bar (crimson)
        page_bar = _line_bar(CRIMSON, width=9.0, height=0.52)
        page_bar.move_to(UP * 1.4)
        page_chip = _pill("PAGE", CRIMSON, size=20)
        page_chip.next_to(page_bar, LEFT, buff=0.3)

        # After shortening: one shorter bar (ink)
        short_bar = _line_bar(INK, width=4.8, height=0.52)
        short_bar.move_to(DOWN * 0.4)
        short_chip = _pill("SHORTER", INK, size=20)
        short_chip.next_to(short_bar, LEFT, buff=0.3)

        # Words dropped — shown as faded fragment
        dropped = _line_bar(CRIMSON, width=4.0, height=0.52)
        dropped.next_to(short_bar, RIGHT, buff=0.18)
        dropped.set_opacity(0.18)
        drop_label = Text("dropped", font=SERIF, color=CRIMSON,
                          font_size=22, slant=ITALIC)
        drop_label.next_to(dropped, DOWN, buff=0.2)
        drop_label.set_opacity(0.55)

        self.play(FadeIn(step_chip), run_time=0.5)
        self.play(FadeIn(page_bar, shift=RIGHT * 0.3),
                  FadeIn(page_chip), run_time=0.8)
        # Shrink the long bar toward its shortened form
        self.play(page_bar.animate.scale_to_fit_width(4.8), run_time=1.0)
        self.play(ReplacementTransform(page_bar, short_bar),
                  FadeIn(short_chip), run_time=0.8)
        self.play(FadeIn(dropped), FadeIn(drop_label), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B12_Transform23(Scene):
    """THE EXAMPLE — transform steps 2+3: parallel + concrete spoken form."""
    def construct(self):
        total = DUR["B12"]

        step_chip = _pill("STEP 2+3: PARALLEL + CONCRETE", SLATE, size=20)
        step_chip.to_corner(UL, buff=0.6)

        # Three parallel bars appear (step 2: parallelism)
        bar_a = _line_bar(INK, width=4.8, height=0.38)
        bar_b = _line_bar(INK, width=4.0, height=0.38)
        bar_c = _line_bar(INK, width=3.6, height=0.38)
        parallel = VGroup(bar_a, bar_b, bar_c).arrange(DOWN, buff=0.28)
        parallel.move_to(ORIGIN + RIGHT * 0.5)

        # Step 3: concrete — the bars transform (become slightly shorter, INK)
        conc_a = _line_bar(INK, width=4.2, height=0.38)
        conc_b = _line_bar(INK, width=2.8, height=0.38)
        conc_c = _line_bar(INK, width=3.0, height=0.38)
        concrete = VGroup(conc_a, conc_b, conc_c).arrange(DOWN, buff=0.28)
        concrete.move_to(ORIGIN + RIGHT * 0.5)

        ear_chip = _pill("EAR", INK, size=22)
        ear_chip.next_to(parallel, LEFT, buff=0.4)

        lands_label = SerifLabel("enters and lands", INK, size=26)
        lands_label.to_edge(DOWN, buff=0.85)

        self.play(FadeIn(step_chip), run_time=0.5)
        self.play(LaggedStart(
            FadeIn(bar_a, shift=UP * 0.2),
            FadeIn(bar_b, shift=UP * 0.2),
            FadeIn(bar_c, shift=UP * 0.2),
            lag_ratio=0.25, run_time=1.1))
        self.play(FadeIn(ear_chip, shift=RIGHT * 0.2), run_time=0.6)
        # Transform to concrete (step 3)
        self.play(
            ReplacementTransform(bar_a, conc_a),
            ReplacementTransform(bar_b, conc_b),
            ReplacementTransform(bar_c, conc_c),
            run_time=1.0)
        self.play(FadeIn(lands_label, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.9))


class B13_Practice(Scene):
    """THE PRACTICE — three checkable rules for spoken writing."""
    def construct(self):
        total = DUR["B13"]

        head = Text("THE PRACTICE", font=DISPLAY, color=SLATE,
                    font_size=28, weight="MEDIUM")
        head.to_edge(UP, buff=0.75)
        u = Line(head.get_corner(DL) + DOWN * 0.1,
                 head.get_corner(DR) + DOWN * 0.1,
                 stroke_width=1.6, color=SLATE)

        # Three rules as chip + serif label pairs
        rules = [
            ("CUT", "every sentence that needs a re-read to parse", CRIMSON),
            ("ADD", "one recurring phrase", INK),
            ("REPLACE", "abstractions that take more than two seconds to unpack", INK),
        ]

        rule_group = VGroup()
        for keyword, explanation, color in rules:
            chip = _pill(keyword, color, size=24)
            expl = Text(explanation, font=SERIF, color=INK, font_size=26)
            expl.next_to(chip, RIGHT, buff=0.35)
            row = VGroup(chip, expl)
            rule_group.add(row)

        rule_group.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        rule_group.move_to(DOWN * 0.3)

        # Align all explanations to the same left edge
        for row in rule_group:
            row[1].align_to(rule_group[0][1], LEFT)

        self.play(FadeIn(head), Create(u), run_time=0.7)
        self.play(LaggedStart(
            *[FadeIn(row, shift=UP * 0.2) for row in rule_group],
            lag_ratio=0.35, run_time=1.4))
        self.wait(max(0.5, total - 2.1))


class B14_Endcard(Scene):
    """RECAP — endcard: listeners cannot re-read / WRITING kicker."""
    def construct(self):
        total = DUR["B14"]

        topic = Text("WRITING", font=DISPLAY, color=SLATE,
                     font_size=22, weight="MEDIUM")
        topic.to_edge(UP, buff=0.55)

        t1 = Text("Listeners cannot re-read.", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        t1.move_to(UP * 0.2)
        u = Line(t1.get_corner(DL) + DOWN * 0.16,
                 t1.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)

        sub = Text("That constraint is the whole architecture.",
                   font=SERIF, color=SLATE, font_size=30)
        sub.next_to(u, DOWN, buff=0.55)

        self.play(FadeIn(topic, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 2.3))
