"""vox_scenes.py — Why Doing Homework With AI Makes You Worse at the Test
(ai-homework-fluency-trap, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
B07 is the only STILL (ai media slot) and has no scene here.

Color law (teardown palette): CRIMSON = delegation / atrophy / fluency trap.
INK = struggle / consolidation / durable skill. Single accent. Never swap.

Exclusions honored: no synaptic plasticity detail, no effect-size formula,
no Bjork full taxonomy, no GPT Tutor arm, no EEG data.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 11.0, "B02": 10.0, "B03": 8.0, "B04": 10.0, "B05": 9.0,
    "B06": 12.0, "B08": 11.0, "B09": 10.0, "B10": 10.0, "B11": 11.0,
    "B12": 14.0, "B13": 9.0, "B14": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _node(label, color=INK, w=2.2, h=0.6):
    box = Rectangle(width=w, height=h).set_fill(color, 0.12).set_stroke(color, 2.0)
    txt = Text(label, font=DISPLAY, color=color, font_size=22, weight="MEDIUM")
    if txt.width > w * 0.88:
        txt.scale_to_fit_width(w * 0.88)
    txt.move_to(box)
    return VGroup(box, txt)


def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=2.5,
                 max_tip_length_to_length_ratio=0.18, buff=0.08)


def _row_chip(label, color=CRIMSON, w=3.2, h=0.52):
    box = Rectangle(width=w, height=h).set_fill(color, 0.10).set_stroke(color, 1.8)
    txt = Text(label, font=SERIF, color=INK, font_size=22, slant=ITALIC)
    if txt.width > w * 0.88:
        txt.scale_to_fit_width(w * 0.88)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("100 on homework.", font=SERIF, color=INK,
                  font_size=56, weight="BOLD")
        t2 = Text("41 on the quiz.", font=SERIF, color=CRIMSON,
                  font_size=56, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        sub = Text("same student. same material.", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        eye.next_to(block, UP, buff=0.7)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.08), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B02_PracticeExamGap(Scene):
    def construct(self):
        total = DUR["B02"]
        # Two grouped bar pairs: Practice (left) and Exam (right)
        bar_w = 0.9
        gap_inner = 0.18
        gap_outer = 1.6

        # Control bars (baseline = 2.4 units tall)
        base_h = 2.4
        practice_ai_h = base_h * 1.48   # 48% higher
        exam_ai_h = base_h * 0.83       # ~17pts lower (illustrative proportion)

        def _bar(h, color, label_top, label_bottom, x_offset):
            bar = Rectangle(width=bar_w, height=h)
            bar.set_fill(color, 0.85).set_stroke(width=0, opacity=0)
            bar.move_to(RIGHT * x_offset + UP * (h / 2 - 2.0))
            top_lbl = Text(label_top, font=MONO, color=color, font_size=22)
            top_lbl.next_to(bar, UP, buff=0.12)
            bot_lbl = Text(label_bottom, font=SERIF, color=INK, font_size=20,
                           slant=ITALIC)
            bot_lbl.next_to(bar, DOWN, buff=0.14)
            return VGroup(bar, top_lbl, bot_lbl)

        # x positions
        ctrl_practice_x = -3.2
        ai_practice_x = ctrl_practice_x + bar_w + gap_inner
        ctrl_exam_x = ai_practice_x + gap_outer
        ai_exam_x = ctrl_exam_x + bar_w + gap_inner

        ctrl_p = _bar(base_h, INK, "control", "practice", ctrl_practice_x)
        ai_p = _bar(practice_ai_h, CRIMSON, "+48%", "AI group", ai_practice_x)
        ctrl_e = _bar(base_h, INK, "control", "exam", ctrl_exam_x)
        ai_e = _bar(exam_ai_h, CRIMSON, "-17 pts", "AI group", ai_exam_x)

        phead = Text("PRACTICE", font=DISPLAY, color=INK, font_size=24,
                     weight="MEDIUM")
        phead.move_to(RIGHT * ((ctrl_practice_x + ai_practice_x) / 2) + UP * 3.0)
        ehead = Text("EXAM", font=DISPLAY, color=INK, font_size=24, weight="MEDIUM")
        ehead.move_to(RIGHT * ((ctrl_exam_x + ai_exam_x) / 2) + UP * 3.0)

        self.play(FadeIn(ctrl_p), FadeIn(ctrl_e), run_time=0.7)
        self.play(FadeIn(phead), FadeIn(ehead), run_time=0.5)
        self.play(FadeIn(ai_p), run_time=0.7)
        self.play(FadeIn(ai_e), run_time=0.7)
        # gap arrow
        gap_arrow = Arrow(ai_p[0].get_right() + RIGHT * 0.15 + UP * 0.3,
                          ai_e[0].get_right() + RIGHT * 0.15 + UP * 0.3,
                          color=CRIMSON, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.18)
        gap_label = Text("the gap", font=SERIF, color=CRIMSON, font_size=22,
                         slant=ITALIC)
        gap_label.next_to(gap_arrow, RIGHT, buff=0.2)
        self.play(Create(gap_arrow), FadeIn(gap_label), run_time=0.8)
        self.wait(max(0.5, total - 3.4))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        t1 = Text("Practice should predict the exam.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("Here it predicted the opposite.", font=SERIF, color=CRIMSON,
                  font_size=38)
        t3 = Text("Why?", font=SERIF, color=INK, font_size=52, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), run_time=0.6)
        self.play(FadeIn(t3, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B04_StruggleCycle(Scene):
    def construct(self):
        total = DUR["B04"]
        # Three nodes in a triangle, then CONSOLIDATION below
        n_try = _node("TRY", INK).move_to(LEFT * 2.5 + UP * 1.0)
        n_fail = _node("FAIL", INK).move_to(RIGHT * 2.5 + UP * 1.0)
        n_adj = _node("ADJUST", INK).move_to(ORIGIN + DOWN * 1.0)
        a1 = _arrow(n_try.get_right(), n_fail.get_left())
        a2 = _arrow(n_fail.get_bottom(), n_adj.get_right() + UP * 0.05)
        a3 = _arrow(n_adj.get_left() + UP * 0.05, n_try.get_bottom())
        loop_label = Text("the struggle cycle", font=SERIF, color=INK,
                          font_size=24, slant=ITALIC).move_to(UP * 2.4)
        n_cons = _node("CONSOLIDATION", INK, w=3.0, h=0.65).move_to(DOWN * 2.6)
        a4 = _arrow(n_adj.get_bottom(), n_cons.get_top())
        cons_label = SerifLabel("durable skill", INK, size=26)
        cons_label.next_to(n_cons, RIGHT, buff=0.4)
        self.play(FadeIn(loop_label), run_time=0.5)
        self.play(FadeIn(n_try), run_time=0.4)
        self.play(Create(a1), FadeIn(n_fail), run_time=0.6)
        self.play(Create(a2), FadeIn(n_adj), run_time=0.6)
        self.play(Create(a3), run_time=0.5)
        self.play(Create(a4), FadeIn(n_cons), FadeIn(cons_label), run_time=0.7)
        self.wait(max(0.5, total - 3.3))


class B05_ComprehensionVsLearning(Scene):
    def construct(self):
        total = DUR["B05"]
        t1 = Text("Following correct code", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("feels like learning.", font=SERIF, color=INK, font_size=46,
                  weight="BOLD")
        t3 = Text("It is not.", font=SERIF, color=CRIMSON, font_size=52,
                  weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.12, t3.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.5))


class B06_TwoPaths(Scene):
    def construct(self):
        total = DUR["B06"]
        # Path A (INK): STRUGGLE -> CONSOLIDATION -> SKILL
        # Path B (CRIMSON): DELEGATION -> OUTPUT -> ATROPHY
        y_a = 1.2
        y_b = -1.2
        xs = [-4.8, -1.6, 1.6, 4.8]

        def _path_node(label, color, x, y, w=2.2, h=0.58):
            return _node(label, color, w, h).move_to(RIGHT * x + UP * y)

        # Path A
        pa1 = _path_node("STRUGGLE", INK, xs[0], y_a)
        pa2 = _path_node("CONSOLIDATION", INK, xs[1], y_a, w=2.8)
        pa3 = _path_node("SKILL", INK, xs[2], y_a)
        aa1 = _arrow(pa1.get_right(), pa2.get_left())
        aa2 = _arrow(pa2.get_right(), pa3.get_left())
        chip_a = LabelChip("PATH A", accent=INK, size=22)
        chip_a.move_to(RIGHT * xs[3] + UP * y_a)

        # Path B
        pb1 = _path_node("DELEGATION", CRIMSON, xs[0], y_b)
        pb2 = _path_node("OUTPUT", CRIMSON, xs[1], y_b)
        pb3 = _path_node("ATROPHY", CRIMSON, xs[2], y_b)
        ab1 = _arrow(pb1.get_right(), pb2.get_left(), CRIMSON)
        ab2 = _arrow(pb2.get_right(), pb3.get_left(), CRIMSON)
        chip_b = LabelChip("PATH B", accent=CRIMSON, size=22)
        chip_b.move_to(RIGHT * xs[3] + UP * y_b)

        # divider
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=HAIRLINE, stroke_width=1.2)

        self.play(FadeIn(pa1), run_time=0.4)
        self.play(Create(aa1), FadeIn(pa2), run_time=0.5)
        self.play(Create(aa2), FadeIn(pa3), FadeIn(chip_a), run_time=0.5)
        self.play(FadeIn(div), run_time=0.4)
        self.play(FadeIn(pb1), run_time=0.4)
        self.play(Create(ab1), FadeIn(pb2), run_time=0.5)
        self.play(Create(ab2), FadeIn(pb3), FadeIn(chip_b), run_time=0.5)
        self.wait(max(0.5, total - 3.7))


class B08_MayaTimeline(Scene):
    def construct(self):
        total = DUR["B08"]
        # Horizontal timeline: nodes at left side, then gap, then quiz at right
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)
        eye = Text("Maya", font=DISPLAY, color=INK, font_size=26,
                   weight="MEDIUM").to_edge(UP, buff=0.7)

        # Timeline spine
        line = Line(LEFT * 5.5 + UP * 0.2, RIGHT * 5.5 + UP * 0.2,
                    color=HAIRLINE, stroke_width=1.5)

        n1 = _node("PASTE CODE", CRIMSON, w=2.0, h=0.55).move_to(LEFT * 4.0 + UP * 0.2)
        n2 = _node("READ + NOD", INK, w=2.0, h=0.55).move_to(LEFT * 1.2 + UP * 0.2)
        n3 = _node("SCORE: 100", INK, w=2.0, h=0.55).move_to(RIGHT * 1.6 + UP * 0.2)

        gap_lbl = Text("3 weeks", font=SERIF, color=INK, font_size=20,
                       slant=ITALIC).move_to(RIGHT * 3.5 + UP * 0.75)
        gap_tick = Line(RIGHT * 3.5 + UP * 0.45, RIGHT * 3.5 + DOWN * 0.05,
                        color=HAIRLINE, stroke_width=1.5)

        n4 = _node("QUIZ: blank", CRIMSON, w=2.0, h=0.55).move_to(RIGHT * 5.1 + UP * 0.2)
        n4_sub = Text("for i in range...", font=MONO, color=CRIMSON,
                      font_size=18).next_to(n4, DOWN, buff=0.3)
        cross = Line(n4_sub.get_left(), n4_sub.get_right(),
                     color=CRIMSON, stroke_width=2)
        cross._qc_intentional = True  # deliberate strikethrough

        self.play(FadeIn(eye), FadeIn(label), run_time=0.5)
        self.play(Create(line), run_time=0.6)
        self.play(FadeIn(n1), run_time=0.4)
        self.play(FadeIn(n2), run_time=0.4)
        self.play(FadeIn(n3), run_time=0.4)
        self.play(FadeIn(gap_lbl), Create(gap_tick), run_time=0.5)
        self.play(FadeIn(n4), run_time=0.4)
        self.play(FadeIn(n4_sub), Create(cross), run_time=0.5)
        self.wait(max(0.5, total - 3.7))


class B09_ThreePatterns(Scene):
    def construct(self):
        total = DUR["B09"]
        head = Text("Three low-score patterns", font=DISPLAY, color=INK,
                    font_size=28, weight="MEDIUM").to_edge(UP, buff=0.7)

        rows = VGroup(
            _row_chip("DELEGATION — hand whole task, move on"),
            _row_chip("PROGRESSIVE RELIANCE — start alone, hand off at friction"),
            _row_chip("ITERATIVE DEBUGGING — paste error, accept fix, repeat"),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 0.2)

        source = Text("Shen & Tamkin 2026 (Anthropic, preprint)", font=SERIF,
                      color=INK, font_size=18, slant=ITALIC).to_corner(DR, buff=0.4)

        self.play(FadeIn(head), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(source), run_time=0.4)
        self.wait(max(0.5, total - 2.4))


class B10_QuestionsBeforeCode(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Questions before code.", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        t2 = Text("what the high scorers did differently", font=SERIF,
                  color=INK, font_size=30, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.14, t1.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.5))


class B11_DiagnosticGap(Scene):
    def construct(self):
        total = DUR["B11"]
        # Two columns: PRODUCTION (left) and DIAGNOSTIC (right)
        prod_head = LabelChip("PRODUCTION", accent=INK, size=26)
        prod_head.move_to(LEFT * 3.2 + UP * 2.0)
        prod_body = Text("delegation works —\noutput is indistinguishable",
                         font=SERIF, color=INK, font_size=26)
        prod_body.next_to(prod_head, DOWN, buff=0.4)
        prod_check = SerifLabel("fakes it", INK, size=24)
        prod_check.next_to(prod_body, DOWN, buff=0.3)

        diag_head = LabelChip("DIAGNOSTIC", accent=CRIMSON, size=26)
        diag_head.move_to(RIGHT * 3.2 + UP * 2.0)
        diag_body = Text("requires an internal model\nof why the code behaves",
                         font=SERIF, color=INK, font_size=26)
        diag_body.next_to(diag_head, DOWN, buff=0.4)
        diag_fail = SerifLabel("delegation fails", CRIMSON, size=24)
        diag_fail.next_to(diag_body, DOWN, buff=0.3)

        divider = Line(UP * 3.0, DOWN * 3.0, color=HAIRLINE, stroke_width=1.5)

        self.play(FadeIn(prod_head), run_time=0.5)
        self.play(FadeIn(prod_body), FadeIn(prod_check), run_time=0.7)
        self.play(FadeIn(divider), run_time=0.4)
        self.play(FadeIn(diag_head), run_time=0.5)
        self.play(FadeIn(diag_body), FadeIn(diag_fail), run_time=0.7)
        self.wait(max(0.5, total - 2.8))


class B12_TwoStudents(Scene):
    def construct(self):
        total = DUR["B12"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)

        # Column headers
        ha = LabelChip("STUDENT A", accent=INK, size=24).move_to(LEFT * 3.4 + UP * 2.8)
        hb = LabelChip("STUDENT B", accent=CRIMSON, size=24).move_to(RIGHT * 3.4 + UP * 2.8)

        def _step(text, color, y, x_center):
            t = Text(text, font=SERIF, color=color, font_size=22)
            if t.width > 4.8:
                t.scale_to_fit_width(4.8)
            t.move_to(RIGHT * x_center + UP * y)
            return t

        # Steps for Student A (INK)
        sa1 = _step("draws entities", INK, 1.9, -3.4)
        sa2 = _step("finds co-author bug", INK, 1.2, -3.4)
        sa3 = _step("rewrites schema", INK, 0.5, -3.4)
        sa4 = _step("score: A", INK, -0.2, -3.4)

        # Steps for Student B (CRIMSON)
        sb1 = _step("pastes to Claude", CRIMSON, 1.9, 3.4)
        sb2 = _step("reads clean schema", CRIMSON, 1.2, 3.4)
        sb3 = _step("score: A", CRIMSON, 0.5, 3.4)
        sb_blank = _step("", CRIMSON, -0.2, 3.4)

        # Divider + time jump
        div_h = Line(LEFT * 6.5, RIGHT * 6.5, color=HAIRLINE, stroke_width=1.5)
        div_h.move_to(DOWN * 0.6)
        later = Text("6 WEEKS LATER", font=DISPLAY, color=INK, font_size=20,
                     weight="MEDIUM").move_to(DOWN * 0.6)
        later._qc_intentional = True   # text sits on the divider row by design

        # After
        sa5 = _step("draws entities — new domain", INK, -1.3, -3.4)
        sa6 = _step("is it a join table? yes.", INK, -2.0, -3.4)

        sb5 = _step("writes: Users, Posts...", CRIMSON, -1.3, 3.4)
        sb6 = _step("stops. blank page.", CRIMSON, -2.0, 3.4)

        div_v = Line(UP * 3.2, DOWN * 3.0, color=HAIRLINE, stroke_width=1.5)

        self.play(FadeIn(label), FadeIn(ha), FadeIn(hb), FadeIn(div_v), run_time=0.7)
        for step in (sa1, sb1, sa2, sb2, sa3, sb3, sa4):
            self.play(FadeIn(step), run_time=0.3)
        self.play(FadeIn(sb4 := _step("", CRIMSON, -0.2, 3.4)), run_time=0.1)
        self.play(FadeIn(div_h), FadeIn(later), run_time=0.6)
        for step in (sa5, sb5, sa6, sb6):
            self.play(FadeIn(step), run_time=0.35)
        self.wait(max(0.5, total - 5.0))


class B13_Practice(Scene):
    def construct(self):
        total = DUR["B13"]
        t1 = Text("10 minutes of questions.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("Then code.", font=SERIF, color=INK, font_size=50,
                  weight="BOLD")
        t3 = Text("every time. even when you think you know.", font=SERIF,
                  color=INK, font_size=28, slant=ITALIC)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.9))


class B14_End(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Borrowed capability disappears", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("when the tool does.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.7)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
