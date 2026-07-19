"""vox_scenes.py — Why the Most Dangerous Claude Output Is the One That Passes Every Test
(pagination-bug-dangerous-middle, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B05 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = tests passing but wrong / dangerous middle / missing handoff.
INK = the handoff condition / non-obvious case / verified output. Single accent. Never swap.

Exclusions: no formal Hoare triples, no security taxonomy, no property-based testing frameworks.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 20.0, "B02": 10.0, "B03": 22.0, "B04": 20.0,
    "B06": 22.0, "B07": 18.0, "B08": 20.0, "B09": 20.0, "B10": 16.0,
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


def _node(label, color=INK, w=3.2, h=0.6):
    box = Rectangle(width=w, height=h).set_fill(color, 0.09).set_stroke(color, 1.8)
    txt = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _row(text, color=INK, w=6.0, h=0.54):
    box = Rectangle(width=w, height=h).set_fill(color, 0.07).set_stroke(color, 1.4)
    txt = Text(text, font=SERIF, color=color, font_size=20, slant=ITALIC)
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
        t1 = Text("Compiles. Passes all tests.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("Six days later: Avery's flashlight", font=SERIF, color=INK,
                  font_size=36)
        t3 = Text("doesn't exist.", font=SERIF, color=CRIMSON, font_size=44,
                  weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.26).move_to(UP * 0.1)
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
        t1 = Text("All tests passed.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("Why did 251 items fail in production?", font=SERIF,
                  color=CRIMSON, font_size=38, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.42).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_TestGap(Scene):
    def construct(self):
        total = DUR["B03"]
        # Number line: multiples of 50 in INK, 251 in CRIMSON
        line = Line(LEFT * 5.5, RIGHT * 5.5, color=HAIRLINE, stroke_width=1.5)
        line.move_to(ORIGIN)

        ticks_ink = [50, 100, 150, 200, 247, 250]
        ticks_crimson = [251]

        tick_marks = VGroup()
        tick_labels = VGroup()

        for v in ticks_ink:
            x = -5.5 + (v / 300) * 11.0
            tick = Line(UP * 0.22, DOWN * 0.22, color=INK, stroke_width=1.6)
            tick.move_to(RIGHT * x)
            lbl = Text(str(v), font=MONO, color=INK, font_size=16).next_to(tick, DOWN, buff=0.18)
            tick_marks.add(tick)
            tick_labels.add(lbl)

        for v in ticks_crimson:
            x = -5.5 + (v / 300) * 11.0
            tick = Line(UP * 0.36, DOWN * 0.36, color=CRIMSON, stroke_width=2.4)
            tick.move_to(RIGHT * x)
            lbl = Text(str(v), font=MONO, color=CRIMSON, font_size=20,
                       weight="BOLD").next_to(tick, DOWN, buff=0.18)
            tick_marks.add(tick)
            tick_labels.add(lbl)

        head = Text("every test was a multiple of 50", font=SERIF, color=INK,
                    font_size=26, slant=ITALIC).to_edge(UP, buff=0.65)
        err_lbl = Text("bug fires here", font=SERIF, color=CRIMSON, font_size=22,
                       slant=ITALIC).move_to(RIGHT * 4.1 + UP * 0.9)
        err_arr = _arrow(err_lbl.get_bottom(), RIGHT * 4.1 + DOWN * 0.3, CRIMSON)

        self.play(FadeIn(head), Create(line), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t) for t in tick_marks[:6]], lag_ratio=0.1),
                  LaggedStart(*[FadeIn(l) for l in tick_labels[:6]], lag_ratio=0.1),
                  run_time=0.8)
        self.play(FadeIn(tick_marks[6]), FadeIn(tick_labels[6]), run_time=0.5)
        self.play(FadeIn(err_lbl), Create(err_arr), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


class B04_DangerousMiddle(Scene):
    def construct(self):
        total = DUR["B04"]
        rows_data = [
            ("250 items: passes.", INK),
            ("251 items: bug fires.", CRIMSON),
            ("The gap is one item.", CRIMSON),
        ]
        rows = VGroup(*[_row(t, c, w=7.0) for t, c in rows_data])
        rows.arrange(DOWN, buff=0.4).move_to(UP * 0.3)

        dm_lbl = SerifLabel("the dangerous middle", CRIMSON, size=26)
        dm_lbl.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(rows[0]), run_time=0.7)
        self.play(FadeIn(rows[1]), run_time=0.7)
        self.play(FadeIn(rows[2]), run_time=0.7)
        self.play(FadeIn(dm_lbl), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


class B06_HandoffCondition(Scene):
    def construct(self):
        total = DUR["B06"]
        head = Text("The missing handoff condition:", font=DISPLAY, color=INK,
                    font_size=24, weight="MEDIUM").to_edge(UP, buff=0.6)

        cond_lines = VGroup(
            Text("total = page_size × 3 + 1:", font=MONO, color=INK, font_size=20),
            Text("calling loop terminates", font=MONO, color=INK, font_size=20),
            Text("after the final 1-item page.", font=MONO, color=INK, font_size=20),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(UP * 0.1)
        for line in cond_lines:
            if line.width > 10.2:
                line.scale_to_fit_width(10.2)
        cond = cond_lines

        cond_box = SurroundingRectangle(cond, color=INK, stroke_width=1.8, buff=0.22)

        label_above = Text("SPECIFIC    TESTABLE    BINARY", font=DISPLAY,
                           color=INK, font_size=20, weight="MEDIUM")
        label_above.next_to(cond_box, DOWN, buff=0.35)

        weak = Text("weak: 'tests pass'", font=SERIF, color=CRIMSON, font_size=22,
                    slant=ITALIC).next_to(label_above, DOWN, buff=0.4)
        weak_cross = Line(weak.get_left() + LEFT * 0.1, weak.get_right() + RIGHT * 0.1,
                          color=CRIMSON, stroke_width=2)

        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(cond), run_time=0.7)
        self.play(Create(cond_box), run_time=0.5)
        self.play(FadeIn(label_above), run_time=0.4)
        self.play(FadeIn(weak), Create(weak_cross), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


class B07_BeforeNotAfter(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("Write the handoff condition", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("before Claude runs the step.", font=SERIF, color=INK,
                  font_size=42)
        t3 = Text("Not after.", font=SERIF, color=CRIMSON, font_size=48,
                  weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.5))


class B08_PriyaLeaderboard(Scene):
    def construct(self):
        total = DUR["B08"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)
        head = Text("Priya's leaderboard", font=DISPLAY, color=INK,
                    font_size=26, weight="MEDIUM").to_edge(UP, buff=0.6)

        rows = [
            ("test: page 1 of 20 — passes", INK),
            ("test: page 2 of 40 — passes", INK),
            ("deploy", INK),
            ("tournament: 41 players", CRIMSON),
            ("41st player: never appears on any page", CRIMSON),
            ("test set: all multiples of 20", CRIMSON),
        ]
        items = VGroup()
        for text, color in rows:
            dot = Dot(color=color, radius=0.09)
            lbl = Text(text, font=SERIF, color=color, font_size=21, slant=ITALIC)
            if lbl.width > 9.0:
                lbl.scale_to_fit_width(9.0)
            row = VGroup(dot, lbl).arrange(RIGHT, buff=0.3)
            items.add(row)
        items.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to(DOWN * 0.1)

        self.play(FadeIn(label), FadeIn(head), run_time=0.5)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.12), run_time=0.38)
        self.wait(max(0.5, total - 0.5 - len(rows) * 0.38))


class B09_Practice(Scene):
    def construct(self):
        total = DUR["B09"]
        head = Text("Before shipping a paginated function:", font=DISPLAY,
                    color=INK, font_size=24, weight="MEDIUM").to_edge(UP, buff=0.65)

        formula = Text("page_size × n + 1", font=MONO, color=CRIMSON,
                       font_size=36, weight="BOLD").move_to(UP * 0.8)

        steps = [
            ("ASK", "What is the smallest input\nwhere this could be wrong?"),
            ("WRITE", "Write the handoff condition\nfor that input."),
            ("RUN", "Run it. If it fails, you found\nthe dangerous middle before it shipped."),
        ]
        nodes = VGroup()
        for label, desc in steps:
            chip = LabelChip(label, accent=INK, size=22)
            desc_txt = Text(desc, font=SERIF, color=INK, font_size=19, slant=ITALIC)
            row = VGroup(chip, desc_txt).arrange(RIGHT, buff=0.4)
            nodes.add(row)
        nodes.arrange(DOWN, buff=0.44, aligned_edge=LEFT).move_to(DOWN * 0.7)

        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(nodes[i].get_bottom() + DOWN * 0.05,
                      nodes[i+1].get_top() + UP * 0.05,
                      color=INK, stroke_width=2.0,
                      max_tip_length_to_length_ratio=0.18)
            arrows.add(a)

        self.play(FadeIn(head), run_time=0.4)
        self.play(FadeIn(formula), run_time=0.5)
        for i, node in enumerate(nodes):
            self.play(FadeIn(node), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)
        self.wait(max(0.5, total - 0.9 - len(nodes) * 0.8))


class B10_End(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("The most dangerous output", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("is the one that passes every test", font=SERIF, color=INK,
                  font_size=40)
        t3 = Text("you thought to write.", font=SERIF, color=CRIMSON,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.26).move_to(UP * 0.1)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.0))
