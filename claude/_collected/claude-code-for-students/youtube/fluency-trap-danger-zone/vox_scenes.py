"""vox_scenes.py — Why the Student Who Knows More Than the Teacher Is in the Most Danger
(fluency-trap-danger-zone, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B05 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = fluency / surface plausibility / danger zone.
INK = domain depth / evaluated output / safe zone. Single accent. Never swap.

Exclusions: no institutional AI policy, no hallucination rate statistics,
no Illich / Vygotsky citation, no RAND/Pew data in narration.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 20.0, "B02": 12.0, "B03": 28.0, "B04": 22.0,
    "B06": 22.0, "B07": 14.0, "B08": 22.0,
    "B09": 25.0, "B10": 28.0, "B11": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=2.5,
                 max_tip_length_to_length_ratio=0.18, buff=0.06)


def _node(label, color=INK, w=2.4, h=0.58):
    box = Rectangle(width=w, height=h).set_fill(color, 0.10).set_stroke(color, 1.8)
    txt = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _row(text, color=INK, w=4.0, h=0.5):
    box = Rectangle(width=w, height=h).set_fill(color, 0.07).set_stroke(color, 1.4)
    txt = Text(text, font=SERIF, color=INK, font_size=20, slant=ITALIC)
    if txt.width > w * 0.90:
        txt.scale_to_fit_width(w * 0.90)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("The student in the back row", font=SERIF, color=INK,
                  font_size=38, weight="BOLD")
        t2 = Text("runs Claude better than his teacher.", font=SERIF, color=INK,
                  font_size=38)
        t3 = Text("He is also less safe.", font=SERIF, color=CRIMSON,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(UP * 0.1)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.0))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("Technical fluency should make AI safer.", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        t2 = Text("Why did it make Seth less safe?", font=SERIF,
                  color=CRIMSON, font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.42).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_TwoSkills(Scene):
    def construct(self):
        total = DUR["B03"]
        # Two columns drawn in
        lhead = Text("TECHNICAL FLUENCY", font=DISPLAY, color=CRIMSON,
                     font_size=26, weight="MEDIUM").move_to(LEFT * 3.5 + UP * 2.6)
        rhead = Text("DOMAIN DEPTH", font=DISPLAY, color=INK,
                     font_size=26, weight="MEDIUM").move_to(RIGHT * 3.5 + UP * 2.6)

        l1 = _row("operate the tool", CRIMSON, w=4.2)
        l2 = _row("know which model to use", CRIMSON, w=4.2)
        l3 = _row("recognize confabulation\n(in domains you know)", CRIMSON, w=4.2, h=0.72)
        l4 = _row("transfers across domains", CRIMSON, w=4.2)
        left_col = VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.25)
        left_col.move_to(LEFT * 3.5 + DOWN * 0.4)

        r1 = _row("evaluate output vs. the world", INK, w=4.2)
        r2 = _row("catch the wrong clause", INK, w=4.2)
        r3 = _row("cite only what exists", INK, w=4.2)
        r4 = _row("does NOT transfer", INK, w=4.2)
        right_col = VGroup(r1, r2, r3, r4).arrange(DOWN, buff=0.25)
        right_col.move_to(RIGHT * 3.5 + DOWN * 0.4)

        div = Line(UP * 3.2, DOWN * 2.8, color=HAIRLINE, stroke_width=1.3)

        self.play(FadeIn(div), FadeIn(lhead), FadeIn(rhead), run_time=0.6)
        for la, ra in zip(left_col, right_col):
            self.play(FadeIn(la), FadeIn(ra), run_time=0.5)
        self.wait(max(0.5, total - 0.6 - 4 * 0.5))


class B04_DangerZone(Scene):
    def construct(self):
        total = DUR["B04"]
        # Four-quadrant drawn: axes first, then labels, then dots
        h = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.8)
        v = Line(DOWN * 3.5, UP * 3.5, color=INK, stroke_width=1.8)

        xl = Text("low", font=MONO, color=INK, font_size=18).next_to(h.get_left(), UP, buff=0.15)
        xr = Text("high", font=MONO, color=INK, font_size=18).next_to(h.get_right(), UP, buff=0.15)
        xa = Text("TECHNICAL FLUENCY →", font=DISPLAY, color=INK, font_size=20,
                  weight="MEDIUM").next_to(h, DOWN, buff=0.3)
        yl = Text("low", font=MONO, color=INK, font_size=18).next_to(v.get_bottom(), RIGHT, buff=0.15)
        yh = Text("high", font=MONO, color=INK, font_size=18).next_to(v.get_top(), RIGHT, buff=0.15)
        ya = Text("DOMAIN DEPTH ↑", font=DISPLAY, color=INK, font_size=20,
                  weight="MEDIUM").rotate(PI / 2).next_to(v, LEFT, buff=0.3)

        # Teacher dot: Q2 (low fluency, high depth)
        teacher_dot = Dot(LEFT * 2.8 + UP * 1.6, color=INK, radius=0.14)
        teacher_lbl = Text("Teacher", font=SERIF, color=INK, font_size=22,
                           slant=ITALIC).next_to(teacher_dot, UR, buff=0.12)

        # Student dot: Q4 (high fluency, low depth) — DANGER ZONE
        student_dot = Dot(RIGHT * 2.8 + DOWN * 1.6, color=CRIMSON, radius=0.14)
        student_lbl = Text("Student", font=SERIF, color=CRIMSON, font_size=22,
                           slant=ITALIC).next_to(student_dot, UL, buff=0.12)

        dz_box = Rectangle(width=2.8, height=1.8).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.6)
        dz_box.move_to(RIGHT * 2.8 + DOWN * 1.6)
        dz_lbl = Text("DANGER ZONE", font=DISPLAY, color=CRIMSON, font_size=20,
                      weight="MEDIUM").next_to(dz_box, DOWN, buff=0.2)

        self.play(Create(h), Create(v), run_time=0.7)
        self.play(FadeIn(xl), FadeIn(xr), FadeIn(xa), FadeIn(yl), FadeIn(yh), FadeIn(ya), run_time=0.6)
        self.play(FadeIn(teacher_dot), FadeIn(teacher_lbl), run_time=0.5)
        self.play(FadeIn(dz_box), run_time=0.5)
        self.play(FadeIn(student_dot), FadeIn(student_lbl), FadeIn(dz_lbl), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B06_MisplacedSentence(Scene):
    def construct(self):
        total = DUR["B06"]
        # Timeline of Seth's error
        events = [
            ("midnight", "reads Claude paragraph", INK),
            ("", "shape matches — nods, closes tab", INK),
            ("next morning", "on the test", INK),
            ("", "writes correct answer (no shift)...", INK),
            ("", "justification smears both cases", CRIMSON),
            ("", "loses most explanation points", CRIMSON),
        ]
        dots = VGroup()
        labels = VGroup()
        times_grp = VGroup()

        start_y = 2.2
        step = 0.78
        for i, (time, desc, color) in enumerate(events):
            y = start_y - i * step
            dot = Dot(LEFT * 5.0 + UP * y, color=color, radius=0.1)
            if i < len(events) - 1:
                ln = Line(dot.get_center(), dot.get_center() + DOWN * step,
                          color=HAIRLINE, stroke_width=1.2)
                dots.add(VGroup(dot, ln))
            else:
                dots.add(dot)

            lbl = Text(desc, font=SERIF, color=color, font_size=20)
            lbl.next_to(dot, RIGHT, buff=0.35)
            if lbl.width > 8.5:
                lbl.scale_to_fit_width(8.5)
            labels.add(lbl)

            if time:
                tlbl = Text(time, font=MONO, color=INK, font_size=18)
                tlbl.next_to(dot, LEFT, buff=0.2)
                times_grp.add(tlbl)

        for dot_grp, lbl in zip(dots, labels):
            self.play(FadeIn(dot_grp), FadeIn(lbl), run_time=0.4)
        self.play(FadeIn(times_grp), run_time=0.4)
        self.wait(max(0.5, total - len(events) * 0.4 - 0.4))


class B07_DeeperThanFluency(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The most dangerous error", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("is one level deeper than your fluency.", font=SERIF,
                  color=CRIMSON, font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_JadaCitation(Scene):
    def construct(self):
        total = DUR["B08"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)

        head = Text("Jada's history essay", font=DISPLAY, color=INK,
                    font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        rows = [
            ("high fluency: knows how to prompt Claude", INK),
            ("knows Claude sometimes hallucinates", INK),
            ("no depth in this historical period", CRIMSON),
            ("citation sounds real — she includes it", INK),
            ("teacher marks it incorrect", CRIMSON),
            ("citation never existed", CRIMSON),
        ]
        items = VGroup()
        for text, color in rows:
            dot = Dot(color=color, radius=0.09)
            lbl = Text(text, font=SERIF, color=color, font_size=22, slant=ITALIC)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.3)
            items.add(row)
        items.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to(DOWN * 0.2)

        self.play(FadeIn(label), FadeIn(head), run_time=0.5)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.12), run_time=0.4)
        self.wait(max(0.5, total - 0.5 - len(rows) * 0.4))


class B09_DepthTest(Scene):
    def construct(self):
        total = DUR["B09"]
        t1 = Text("You have depth when one clause feels off.", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        t2 = Text("before you know why.", font=SERIF, color=CRIMSON,
                  font_size=38, slant=ITALIC)
        sub = Text("fluent agreement = depth not there yet", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        block = VGroup(t1, t2, sub).arrange(DOWN, buff=0.40).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.9))


class B10_ChoiceFork(Scene):
    def construct(self):
        total = DUR["B10"]
        head = Text("Choose one domain. Build it the slow way.", font=DISPLAY,
                    color=INK, font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        # Fork: left = chemistry student, right = writer
        fork_top = Dot(ORIGIN + UP * 0.5, color=INK, radius=0.1)
        fork_label = Text("YOU", font=DISPLAY, color=INK, font_size=22,
                          weight="MEDIUM").next_to(fork_top, UP, buff=0.2)

        left_arr = _arrow(fork_top.get_center(), LEFT * 3.2 + DOWN * 0.4)
        right_arr = _arrow(fork_top.get_center(), RIGHT * 3.2 + DOWN * 0.4)

        left_box = _node("chemistry student\nbuild chemistry slow", INK, w=3.8, h=0.9)
        left_box.move_to(LEFT * 3.5 + DOWN * 1.2)
        left_sub = Text("run Claude on English", font=SERIF, color=INK,
                        font_size=18, slant=ITALIC).next_to(left_box, DOWN, buff=0.2)

        right_box = _node("writer\nbuild writing slow", INK, w=3.8, h=0.9)
        right_box.move_to(RIGHT * 3.5 + DOWN * 1.2)
        right_sub = Text("run Claude on chemistry", font=SERIF, color=INK,
                         font_size=18, slant=ITALIC).next_to(right_box, DOWN, buff=0.2)

        bottom = Text("Neither gets to skip depth in something.", font=SERIF,
                      color=CRIMSON, font_size=24, weight="BOLD").to_edge(DOWN, buff=0.5)

        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(fork_top), FadeIn(fork_label), run_time=0.4)
        self.play(Create(left_arr), Create(right_arr), run_time=0.6)
        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.6)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.5)
        self.play(FadeIn(bottom), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("Fluency gets you the output.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Depth tells you if it is right.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.28).move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.65)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
