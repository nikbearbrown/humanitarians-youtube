"""vox_scenes.py — Why Most Proposals Fail Before the Solution:
The Problem Definition Test (vox-proposal-problem-definition, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is own. B01 is the only STILL
(ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh writing-guide/youtube/vox-proposal-problem-definition

Color law (newsprint palette):
  TEAL (#1F6F5C) = the passing diagnostic (specific, real, unsolved)
  CRIMSON (#BF3339) = the failing diagnostic versions (too big, fake, solved)
  GOLD (#F5D061) = editor's-pen highlight on B10 blank brackets — fill only, NEVER text
  Never swap mid-film.

Gate B convention: every zero-width stroke is also zero-opacity, or the layout
audit strikes it.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 9.5, "B03": 10.0, "B04": 10.5, "B05": 11.5,
    "B06": 11.0, "B07": 10.0, "B08": 10.5, "B09": 13.5,
    "B10": 11.5, "B11": 10.0
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _bracket_rect(center, w=2.8, h=0.52):
    """A rounded bracket placeholder box (GOLD fill, INK stroke)."""
    r = RoundedRectangle(corner_radius=0.08, width=w, height=h)
    r.set_fill(GOLD, 0.45).set_stroke(INK, 1.2)
    r.move_to(center)
    return r


def _fail_chip():
    return LabelChip("FAIL", accent=CRIMSON, size=22)


def _pass_chip():
    return LabelChip("PASS", accent=TEAL, size=22)


def _divider(center, h=3.2):
    """Thin vertical hairline divider between columns."""
    d = Line(center + UP * h / 2, center + DOWN * h / 2,
             color=INK, stroke_width=0.8)
    d.set_stroke(opacity=0.35)
    return d


# ---------------------------------------------------------------- scenes

class B02_Checklist(Scene):
    """COLD OPEN — five checklist items draw on one by one in TEAL."""
    def construct(self):
        total = DUR["B02"]
        items = [
            "1. Wash hands with soap",
            "2. Clean skin with chlorhexidine",
            "3. Use sterile drapes over patient",
            "4. Wear sterile mask, gown, gloves",
            "5. Cover catheter site with sterile dressing",
        ]
        eye = Text("PRONOVOST'S CENTRAL-LINE CHECKLIST", font=DISPLAY,
                   color=SLATE, font_size=22)
        eye.to_edge(UP, buff=0.7)
        checks = VGroup(*[
            Text(item, font=SERIF, color=INK, font_size=28)
            for item in items
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        checks.move_to(DOWN * 0.15)
        # TEAL accent bars alongside each item
        bars = VGroup(*[
            Rectangle(width=0.12, height=0.28)
            .set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            .next_to(t, LEFT, buff=0.2)
            for t in checks
        ])
        self.play(FadeIn(eye), run_time=0.6)
        for bar, item in zip(bars, checks):
            self.play(FadeIn(bar, shift=RIGHT * 0.15),
                      FadeIn(item, shift=RIGHT * 0.15),
                      run_time=0.55)
        brace = Brace(checks, RIGHT, color=INK)
        blabel = SerifLabel("one piece of paper", TEAL, size=26)
        blabel.next_to(brace, RIGHT, buff=0.25)
        self.play(FadeIn(brace), FadeIn(blabel), run_time=0.7)
        self.wait(max(0.5, total - 0.6 - 5 * 0.55 - 0.7))


class B03_Question(Scene):
    """THE QUESTION — card with the film's one question."""
    def construct(self):
        total = DUR["B03"]
        kicker = Text("WRITING", font=DISPLAY, color=SLATE, font_size=22)
        kicker.to_edge(UP, buff=0.7)
        q = Text("What is the one sentence", font=SERIF, color=INK,
                 font_size=46, weight=BOLD)
        q2 = Text("that separates a proposal from a topic?", font=SERIF,
                  color=INK, font_size=46, weight=BOLD)
        block = VGroup(q, q2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(q2.get_corner(DL) + DOWN * 0.14,
                 q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B04_SectionCard(Scene):
    """THE PROBLEM — section card. Anchor: 'where most proposals fail'."""
    def construct(self):
        total = DUR["B04"]
        top = Text("WHERE MOST PROPOSALS FAIL", font=DISPLAY,
                   color=INK, font_size=36)
        sub = Text("before the solution", font=SERIF, color=SLATE,
                   font_size=28, slant=ITALIC)
        block = VGroup(top, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        accent = Line(top.get_corner(DL) + DOWN * 0.16,
                      top.get_corner(DR) + DOWN * 0.16,
                      color=CRIMSON, stroke_width=2.5)
        self.play(FadeIn(top), Create(accent), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.5))


class B05_TooBig(Scene):
    """MECHANISM 1 — the problem is too big (CRIMSON)."""
    def construct(self):
        total = DUR["B05"]
        label = Text("FAILURE 1", font=DISPLAY, color=CRIMSON, font_size=22)
        label.to_edge(UP, buff=0.7)
        # Problem box wider than the frame — overflow metaphor
        big_box = Rectangle(width=15.0, height=1.9)
        big_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.5)
        big_box.move_to(UP * 0.8)
        box_label = Text("Climate change", font=SERIF, color=CRIMSON,
                         font_size=38, weight=BOLD)
        box_label.move_to(big_box)
        bullets = [
            "no single audience",
            "no single solution",
            "no evaluable recommendation",
        ]
        items = VGroup(*[
            Text("- " + b, font=SERIF, color=CRIMSON, font_size=28)
            for b in bullets
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        items.move_to(DOWN * 1.5)
        self.play(FadeIn(label), run_time=0.5)
        self.play(FadeIn(big_box), FadeIn(box_label), run_time=0.9)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.45)
        self.wait(max(0.5, total - 0.5 - 0.9 - 3 * 0.45))


class B06_FakeProblem(Scene):
    """MECHANISM 2 — the problem is fake (CRIMSON vague-language chips)."""
    def construct(self):
        total = DUR["B06"]
        label = Text("FAILURE 2", font=DISPLAY, color=CRIMSON, font_size=22)
        label.to_edge(UP, buff=0.7)
        phrase1 = LabelChip("Many students struggle with...", accent=CRIMSON, size=22)
        phrase2 = LabelChip("It is well known that...", accent=CRIMSON, size=22)
        phrase1.move_to(UP * 0.7 + LEFT * 2.2)
        phrase2.move_to(UP * 0.7 + RIGHT * 2.2)
        ring1 = HandRing(phrase1, color=CRIMSON)
        no_group = SerifLabel("no specific group named", CRIMSON, size=26)
        no_group.move_to(DOWN * 1.5)
        no_evidence = SerifLabel("no verifiable affected population", CRIMSON, size=26)
        no_evidence.next_to(no_group, DOWN, buff=0.3)
        self.play(FadeIn(label), run_time=0.5)
        self.play(FadeIn(phrase1, shift=UP * 0.2),
                  FadeIn(phrase2, shift=UP * 0.2), run_time=0.8)
        self.play(Create(ring1), run_time=1.0)
        self.play(FadeIn(no_group, shift=UP * 0.1),
                  FadeIn(no_evidence, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 0.5 - 0.8 - 1.0 - 0.7))


class B07_AlreadySolved(Scene):
    """MECHANISM 3 — the problem is already solved (timeline, TEAL + CRIMSON).
    Chips placed above the arrow so they do not cross it (W5 fix)."""
    def construct(self):
        total = DUR["B07"]
        label = Text("FAILURE 3", font=DISPLAY, color=CRIMSON, font_size=22)
        label.to_edge(UP, buff=0.7)
        # Timeline arrow — centered, horizontal, below the chips
        arrow = Arrow(LEFT * 5.2 + DOWN * 0.4, RIGHT * 5.2 + DOWN * 0.4,
                      color=INK, stroke_width=3, buff=0)
        time_label = SerifLabel("time", INK, size=22)
        time_label.next_to(arrow.get_end(), RIGHT, buff=0.15)
        # Chips ABOVE the arrow (clear of the line)
        exist_chip = LabelChip("existing intervention", accent=TEAL, size=22)
        exist_chip.move_to(LEFT * 1.8 + UP * 0.55)
        your_chip = LabelChip("your proposal", accent=CRIMSON, size=22)
        your_chip.move_to(RIGHT * 2.5 + UP * 0.55)
        # Tick marks on the timeline below each chip
        tick1 = Line(LEFT * 1.8 + DOWN * 0.25, LEFT * 1.8 + DOWN * 0.5,
                     color=TEAL, stroke_width=2.5)
        tick2 = Line(RIGHT * 2.5 + DOWN * 0.25, RIGHT * 2.5 + DOWN * 0.5,
                     color=CRIMSON, stroke_width=2.5)
        # No-gap label
        no_gap = SerifLabel("no gap to fill", CRIMSON, size=28)
        no_gap.move_to(DOWN * 1.8)
        self.play(FadeIn(label), run_time=0.5)
        self.play(Create(arrow), FadeIn(time_label), run_time=0.8)
        self.play(FadeIn(exist_chip, shift=DOWN * 0.2),
                  Create(tick1), run_time=0.5)
        self.play(FadeIn(your_chip, shift=DOWN * 0.2),
                  Create(tick2), run_time=0.5)
        self.play(FadeIn(no_gap, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 0.5 - 0.8 - 0.5 - 0.5 - 0.6))


class B08_PronovostDiagnostic(Scene):
    """IMPLICATION — the diagnostic sentence filled in correctly (TEAL)."""
    def construct(self):
        total = DUR["B08"]
        eye = Text("THE DIAGNOSTIC FILLED IN", font=DISPLAY,
                   color=SLATE, font_size=22)
        eye.to_edge(UP, buff=0.7)
        template = Text("Right now,  [         ]  is experiencing",
                        font=SERIF, color=INK, font_size=30)
        line2 = Text("[              ]  because of  [                    ].",
                     font=SERIF, color=INK, font_size=30)
        template.move_to(UP * 0.8)
        line2.next_to(template, DOWN, buff=0.28)
        # TEAL accent bar that grows taller as each slot fills in
        bar = Rectangle(width=0.18, height=0.5)
        bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        bar.move_to(LEFT * 5.8 + UP * 0.1)
        # The three filled-in slots
        slot1 = Text("ICU patients receiving central lines", font=SERIF,
                     color=TEAL, font_size=28, weight=BOLD)
        slot1.move_to(UP * 0.1)
        slot2 = Text("15,000 preventable deaths per year", font=SERIF,
                     color=TEAL, font_size=28, weight=BOLD)
        slot2.next_to(slot1, DOWN, buff=0.28)
        slot3 = Text("five steps omitted under pressure", font=SERIF,
                     color=TEAL, font_size=28, weight=BOLD)
        slot3.next_to(slot2, DOWN, buff=0.28)
        self.play(FadeIn(eye), FadeIn(bar), run_time=0.5)
        self.play(FadeIn(template), FadeIn(line2), run_time=0.8)
        self.play(FadeIn(slot1, shift=RIGHT * 0.25),
                  bar.animate.scale_to_fit_height(0.9),
                  run_time=0.7)
        self.play(FadeIn(slot2, shift=RIGHT * 0.25),
                  bar.animate.scale_to_fit_height(1.5),
                  run_time=0.7)
        self.play(FadeIn(slot3, shift=RIGHT * 0.25),
                  bar.animate.scale_to_fit_height(2.1),
                  run_time=0.7)
        self.wait(max(0.5, total - 0.5 - 0.8 - 3 * 0.7))


class B09_ThreeVersions(Scene):
    """THE EXAMPLE — three versions stacked vertically: two FAIL, one PASS (16:9 only).
    Three-column layout was too wide; vertical stack fits within safe area."""
    def construct(self):
        total = DUR["B09"]
        eye = Text("THE DIAGNOSTIC TEST", font=DISPLAY,
                   color=SLATE, font_size=22)
        eye.to_edge(UP, buff=0.55)

        def _row(chip_label, chip_accent, text_str, text_color, verdict):
            chip = LabelChip(chip_label, accent=chip_accent, size=20)
            chip.width  # ensure rendered
            body = Text(text_str, font=SERIF, color=text_color,
                        font_size=25)
            verdict_chip = (_fail_chip() if verdict == "fail" else _pass_chip())
            row = VGroup(chip, body, verdict_chip).arrange(
                RIGHT, buff=0.45, aligned_edge=ORIGIN
            )
            return row

        # Row 1 — too big
        r1 = _row("too big", CRIMSON,
                  '"Climate change is a serious problem."',
                  CRIMSON, "fail")
        # Row 2 — fake
        r2 = _row("fake", CRIMSON,
                  '"Campus recycling fails to divert organic waste."',
                  CRIMSON, "fail")
        # Row 3 — specific (pass)
        r3 = _row("specific", TEAL,
                  '"Right now, 8,000 dining-hall users produce\n400 lbs of compostable waste daily because\nthe university has no composting contract."',
                  TEAL, "pass")
        note = Text("[illustrative]", font=MONO, color=SLATE, font_size=18)
        note.next_to(r3, DOWN, buff=0.12)

        stack = VGroup(r1, r2, r3).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        stack.move_to(DOWN * 0.1)

        # TEAL progress bar that grows as each version is revealed (shape motion)
        prog = Rectangle(width=0.15, height=0.4)
        prog.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        prog.move_to(LEFT * 6.5 + UP * 1.5)

        self.play(FadeIn(eye), FadeIn(prog), run_time=0.5)
        self.play(FadeIn(r1, shift=RIGHT * 0.2), run_time=0.7)
        self.play(FadeIn(r2, shift=RIGHT * 0.2),
                  prog.animate.scale_to_fit_height(1.0), run_time=0.7)
        self.play(FadeIn(r3, shift=RIGHT * 0.2),
                  prog.animate.scale_to_fit_height(2.0), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 0.5 - 0.7 - 0.7 - 0.8 - 0.5))


class B10_DiagnosticBlank(Scene):
    """THE PRACTICE — the diagnostic sentence with blank brackets (GOLD highlight)."""
    def construct(self):
        total = DUR["B10"]
        eye = Text("THE PRE-DRAFT TEST", font=DISPLAY, color=SLATE, font_size=22)
        eye.to_edge(UP, buff=0.7)

        # The sentence in three lines
        line1 = Text("Right now,", font=SERIF, color=INK, font_size=32)
        br1 = _bracket_rect(ORIGIN, w=3.0, h=0.5)
        br1_label = Text("specific group", font=MONO, color=INK,
                         font_size=22)
        br1_label.move_to(br1)
        line2 = Text("is experiencing", font=SERIF, color=INK, font_size=32)
        br2 = _bracket_rect(ORIGIN, w=3.4, h=0.5)
        br2_label = Text("specific consequence", font=MONO, color=INK,
                         font_size=22)
        br2_label.move_to(br2)
        line3 = Text("because of", font=SERIF, color=INK, font_size=32)
        br3 = _bracket_rect(ORIGIN, w=3.0, h=0.5)
        br3_label = Text("specific cause", font=MONO, color=INK,
                         font_size=22)
        br3_label.move_to(br3)

        row1 = VGroup(line1, VGroup(br1, br1_label), line2).arrange(RIGHT, buff=0.3)
        row2 = VGroup(VGroup(br2, br2_label), line3, VGroup(br3, br3_label)).arrange(RIGHT, buff=0.3)
        block = VGroup(row1, row2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        block.move_to(UP * 0.3)

        rule = SerifLabel("If a bracket stays empty: topic, not proposal.", CRIMSON, size=26)
        rule.next_to(block, DOWN, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(row1), run_time=0.8)
        self.play(FadeIn(row2), run_time=0.8)
        self.play(FadeIn(rule, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 0.5 - 0.8 - 0.8 - 0.7))


class B11_End(Scene):
    """RECAP endcard — question to answer, WRITING kicker."""
    def construct(self):
        total = DUR["B11"]
        kicker = Text("WRITING", font=DISPLAY, color=SLATE, font_size=22)
        kicker.to_edge(UP, buff=0.7)
        t1 = Text("A topic has no diagnostic sentence.", font=SERIF,
                  color=INK, font_size=48, weight=BOLD)
        t1.move_to(UP * 0.2)
        u = Line(t1.get_corner(DL) + DOWN * 0.16,
                 t1.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))
