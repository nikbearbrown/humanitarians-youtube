"""vox_scenes.py — Why You Should Write the Test Before You Write the Prompt
(vox-criteria-before-output, slate cut, 16:9)

One Scene per GRAPHIC / CARD beat whose source is 'own'.
B02 is STILL·ai — no scene. Color law (teardown palette):
  INK     = criteria present / correct output
  CRIMSON = criteria missing / failed output
  SLATE   = neutral scaffolding

Exclusions: no rubric research, no TDD history, no four-criteria taxonomy,
no benchmark literature.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 11.0,
    "B06": 11.0, "B07": 11.0, "B08": 9.0, "B09": 12.0,
    "B10": 11.0, "B11": 13.0, "B12": 12.0, "B13": 11.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _bar(w=3.0, h=0.35, color=INK, opacity=0.8):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return r


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=22):
    return LabelChip(text, accent=accent, size=size)


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why you should write the test", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("before you write the prompt", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("output quality gives no signal about output correctness", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.45)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did output quality", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        q2 = Text("give no signal about output correctness?", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_FluencyVsCorrectness(Scene):
    """Two parallel tracks: FLUENCY and CORRECTNESS diverging."""
    def construct(self):
        total = DUR["B04"]
        # labels
        fl_label = _chip("FLUENCY", accent=INK, size=22)
        fl_label.move_to(LEFT * 4.5 + UP * 1.2)
        co_label = _chip("CORRECTNESS", accent=CRIMSON, size=22)
        co_label.move_to(LEFT * 4.5 + DOWN * 0.5)
        # fluency bar — full, solid
        fl_bar = Rectangle(width=5.5, height=0.45)
        fl_bar.set_fill(INK, 0.85).set_stroke(width=0, opacity=0)
        fl_bar.move_to(RIGHT * 0.2 + UP * 1.2)
        fl_score = _label("9/10", INK, 32)
        fl_score.next_to(fl_bar, RIGHT, buff=0.3)
        # correctness bar — short, red
        co_bar = Rectangle(width=2.2, height=0.45)
        co_bar.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        co_bar.move_to(LEFT * 1.95 + DOWN * 0.5)
        co_score = _label("4/10", CRIMSON, 32)
        co_score.next_to(co_bar.get_right() * RIGHT + DOWN * 0.5, RIGHT, buff=0.3)
        co_score.move_to(RIGHT * 0.8 + DOWN * 0.5)
        note = SerifLabel("same document — independent dimensions", CRIMSON, size=26)
        note.move_to(DOWN * 2.0)
        self.play(FadeIn(fl_label), FadeIn(co_label), run_time=0.6)
        self.play(fl_bar.animate.scale(1.0), FadeIn(fl_bar), FadeIn(fl_score), run_time=0.8)
        self.play(FadeIn(co_bar), FadeIn(co_score), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


class B05_MissingRubric(Scene):
    """Foundation rubric with empty checkboxes — criteria not in the prompt."""
    def construct(self):
        total = DUR["B05"]
        title = _label("The funder's rubric", SLATE, 28)
        title.to_edge(UP, buff=0.7)
        criteria = [
            ("equity lens", False),
            ("measurable outcomes", False),
            ("logic model", False),
        ]
        rows = VGroup()
        for text, checked in criteria:
            box = Square(0.35).set_fill(WHITE, 0).set_stroke(CRIMSON, 2.5)
            box.move_to(LEFT * 4.0)
            lbl = _label(text, CRIMSON, 28)
            lbl.next_to(box, RIGHT, buff=0.3)
            miss = _label("not in prompt", CRIMSON, 22)
            miss.next_to(lbl, RIGHT, buff=0.5)
            rows.add(VGroup(box, lbl, miss))
        rows.arrange(DOWN, buff=0.45).move_to(DOWN * 0.2)
        note = SerifLabel("existed — just never written down", CRIMSON, size=26)
        note.next_to(rows, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B06_OptimizedForNothing(Scene):
    """Claude's target when no criteria given: generic defaults."""
    def construct(self):
        total = DUR["B06"]
        title = _label("No criteria in prompt: Claude aims at defaults", INK, 28)
        title.to_edge(UP, buff=0.7)
        defaults = [
            ("fluency", INK),
            ("document shape", INK),
            ("generic completeness", INK),
        ]
        bars = VGroup()
        for text, color in defaults:
            b = _bar(3.5, 0.38, color, 0.6)
            lbl = _label(text, SLATE, 25)
            lbl.next_to(b, LEFT, buff=0.25)
            bars.add(VGroup(lbl, b))
        bars.arrange(DOWN, buff=0.3).move_to(UP * 0.2)
        your_target = _chip("YOUR CRITERIA", accent=CRIMSON, size=22)
        your_target.move_to(DOWN * 2.0)
        absent = _label("absent from the prompt", CRIMSON, 26)
        absent.next_to(your_target, RIGHT, buff=0.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, scale=0.95) for b in bars], lag_ratio=0.15),
                  run_time=1.0)
        self.play(FadeIn(your_target), FadeIn(absent), run_time=0.7)
        self.wait(max(0.5, total - 2.2))


class B07_CriteriaReveal(Scene):
    """Writing criteria forces articulation of hidden requirements."""
    def construct(self):
        total = DUR["B07"]
        title = _label("Writing criteria reveals what you actually need", INK, 28)
        title.to_edge(UP, buff=0.7)
        # question flow
        q = _label("What does success look like?", INK, 30)
        q.move_to(UP * 0.8)
        arrow = Arrow(UP * 0.3, DOWN * 0.1, color=INK, stroke_width=3, buff=0.1)
        arrow.move_to(UP * 0.35)
        revealed = VGroup(
            _label("equity lens required", INK, 26),
            _label("measurable outcomes required", INK, 26),
            _label("logic model required", INK, 26),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.0)
        note = SerifLabel("requirements you had, not yet stated", INK, size=26)
        note.next_to(revealed, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(q), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in revealed], lag_ratio=0.2),
                  run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


class B08_SectionCard(Scene):
    """Section card: Criteria = specification + checklist."""
    def construct(self):
        total = DUR["B08"]
        t1 = Text("Criteria =", font=DISPLAY, color=INK, font_size=52, weight=BOLD)
        t2 = Text("specification + checklist", font=DISPLAY, color=CRIMSON,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B09_CriteriaAdded(Scene):
    """Criteria added to prompt; checkmarks accumulate."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Criteria in the prompt: Claude has targets", INK, 28)
        title.to_edge(UP, buff=0.7)
        criteria = [
            "address equity explicitly",
            "name three measurable outcomes",
            "include a logic model",
        ]
        rows = VGroup()
        checks = VGroup()
        for text in criteria:
            box = Square(0.35).set_fill(INK, 0).set_stroke(INK, 2.5)
            box.move_to(LEFT * 4.0)
            lbl = _label(text, INK, 27)
            lbl.next_to(box, RIGHT, buff=0.3)
            tick = Text("v", font=SERIF, color=INK, font_size=26, weight=BOLD)
            tick.move_to(box.get_center())
            rows.add(VGroup(box, lbl))
            checks.add(tick)
        rows.arrange(DOWN, buff=0.45).move_to(DOWN * 0.1)
        # reposition checks
        for i, (row, tick) in enumerate(zip(rows, checks)):
            tick.move_to(row[0].get_center())
        result = SerifLabel("proposal meets all three — correct and polished", INK, size=26)
        result.next_to(rows, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2), run_time=0.9)
        for tick in checks:
            self.play(FadeIn(tick, scale=1.2), run_time=0.4)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 0.5 - 0.9 - len(checks) * 0.4 - 0.6))


class B10_CriteriaTransfer(Scene):
    """Criteria-writing as a thinking skill that transfers."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Criteria-writing teaches you what you actually need", INK, 28)
        title.to_edge(UP, buff=0.7)
        examples = [
            ("grant writers", "learn what the funder requires"),
            ("analysts", "learn what they won't accept"),
            ("teachers", "learn what materials must do"),
        ]
        rows = VGroup()
        for role, result in examples:
            role_chip = _chip(role.upper(), accent=SLATE, size=20)
            arrow = Arrow(RIGHT * 0.1, RIGHT * 0.5, color=INK,
                          stroke_width=2, buff=0.05, max_tip_length_to_length_ratio=0.3)
            result_lbl = _label(result, INK, 24)
            row = VGroup(role_chip, arrow, result_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(DOWN * 0.2)
        note = SerifLabel("the discipline transfers beyond Claude", INK, size=26)
        note.next_to(rows, DOWN, buff=0.45)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B11_LiExample(Scene):
    """Li's status report: polished but missing flagged risks."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Li's status report: polished and incomplete", INK, 28)
        title.to_edge(UP, buff=0.7)
        # report chip + word count
        report_chip = _chip("STATUS REPORT", accent=SLATE, size=22)
        report_chip.move_to(LEFT * 3.5 + UP * 0.5)
        word_count = _label("800 words — organized, thorough", INK, 26)
        word_count.next_to(report_chip, DOWN, buff=0.3)
        # missing items
        missing_head = _chip("NOT IN REPORT", accent=CRIMSON, size=22)
        missing_head.move_to(RIGHT * 2.5 + UP * 0.5)
        risks = VGroup(
            _label("Risk 1 status", CRIMSON, 24),
            _label("Risk 2 status", CRIMSON, 24),
            _label("Risk 3 status", CRIMSON, 24),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + DOWN * 0.4)
        note = _label("not in the prompt — not in the output", CRIMSON, 26)
        note.move_to(DOWN * 2.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(report_chip), FadeIn(word_count), run_time=0.7)
        self.play(FadeIn(missing_head),
                  LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in risks], lag_ratio=0.2),
                  run_time=0.9)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B12_LiFixed(Scene):
    """Li adds three criteria; report covers all risks."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Criteria added: report covers all three risks", INK, 28)
        title.to_edge(UP, buff=0.7)
        # criteria chips
        criteria_head = _chip("CRITERIA IN PROMPT", accent=INK, size=22)
        criteria_head.move_to(LEFT * 3.5 + UP * 0.8)
        criteria = VGroup(
            _label("name each flagged risk", INK, 24),
            _label("state current status", INK, 24),
            _label("one action per risk", INK, 24),
        ).arrange(DOWN, buff=0.2).move_to(LEFT * 3.5 + DOWN * 0.1)
        # output chip
        out_head = _chip("OUTPUT", accent=INK, size=22)
        out_head.move_to(RIGHT * 2.5 + UP * 0.8)
        out_items = VGroup(
            _label("Risk 1 — resolved", INK, 24),
            _label("Risk 2 — monitoring", INK, 24),
            _label("Risk 3 — action: escalate", INK, 24),
        ).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.5 + DOWN * 0.1)
        arr = Arrow(LEFT * 0.8, RIGHT * 0.8, color=INK, stroke_width=4, buff=0.2)
        result = SerifLabel("polished and correct — because correct had a target", INK, size=26)
        result.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(criteria_head),
                  LaggedStart(*[FadeIn(c) for c in criteria], lag_ratio=0.15),
                  run_time=0.9)
        self.play(GrowArrow(arr), run_time=0.5)
        self.play(FadeIn(out_head),
                  LaggedStart(*[FadeIn(o) for o in out_items], lag_ratio=0.15),
                  run_time=0.9)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.4))


class B13_Practice(Scene):
    """Two questions before every prompt."""
    def construct(self):
        total = DUR["B13"]
        title = _label("Before writing any prompt:", INK, 30)
        title.to_edge(UP, buff=0.7)
        q1_chip = _chip("QUESTION 1", accent=INK, size=22)
        q1_text = _label("What does good look like?", INK, 34)
        q1 = VGroup(q1_chip, q1_text).arrange(DOWN, buff=0.25).move_to(UP * 0.5)
        q2_chip = _chip("QUESTION 2", accent=CRIMSON, size=22)
        q2_text = _label("What would make this wrong?", CRIMSON, 34)
        q2 = VGroup(q2_chip, q2_text).arrange(DOWN, buff=0.25).move_to(DOWN * 1.1)
        note = SerifLabel("those answers are the criteria — and the specification", INK, size=26)
        note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(q1_chip), FadeIn(q1_text), run_time=0.7)
        self.play(FadeIn(q2_chip), FadeIn(q2_text), run_time=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B14_End(Scene):
    """Endcard."""
    def construct(self):
        total = DUR["B14"]
        t1 = Text("Fluency and correctness are independent.", font=SERIF,
                  color=INK, font_size=42, weight=BOLD)
        t2 = Text("Write the criteria. Then generate.", font=SERIF,
                  color=INK, font_size=42, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.1))
