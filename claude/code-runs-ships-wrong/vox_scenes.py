"""vox_scenes.py — Why the Code Runs Fine and Still Ships Wrong
(code-runs-ships-wrong, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B04 is the STILL (ai media slot) — no scene here.

Color law (teardown palette): CRIMSON = the bug / wrong output / invisible failure.
INK = verified / correct / the supervisory move. Single accent. Never swap.

Exclusions: no proof theory, no hallucination taxonomy, no Copilot stats, no RAG.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 10.0, "B03": 11.0, "B05": 11.0, "B06": 10.0,
    "B07": 11.0, "B08": 10.0, "B09": 10.0, "B10": 10.0, "B11": 13.0,
    "B12": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _node(label, color=INK, w=2.4, h=0.58):
    box = Rectangle(width=w, height=h).set_fill(color, 0.10).set_stroke(color, 1.8)
    txt = Text(label, font=DISPLAY, color=color, font_size=20, weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=2.5,
                 max_tip_length_to_length_ratio=0.18, buff=0.08)


def _chip_row(label, color=CRIMSON, w=3.6, h=0.5):
    box = Rectangle(width=w, height=h).set_fill(color, 0.09).set_stroke(color, 1.6)
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
        t1 = Text("Compiled. Tests passed.", font=SERIF, color=INK,
                  font_size=52, weight="BOLD")
        t2 = Text("Quietly wrong.", font=SERIF, color=CRIMSON,
                  font_size=52, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.2)
        sub = Text("the gap Claude cannot see", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.45)
        eye.next_to(block, UP, buff=0.65)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.08), run_time=0.5)
        self.wait(max(0.5, total - 2.4))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("The audit said: looks good.", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("Why was it still wrong?", font=SERIF, color=CRIMSON,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.4))


class B03_ClaudeStrengths(Scene):
    def construct(self):
        total = DUR["B03"]
        head = Text("Claude does this:", font=DISPLAY, color=INK, font_size=26,
                    weight="MEDIUM").to_edge(UP, buff=0.65)
        items = [
            "SORT ALGORITHMS",
            "LIBRARY IDIOMS",
            "BOILERPLATE",
            "SYNTAX RECALL",
            "FIRST DRAFTS",
        ]
        chips = VGroup(*[LabelChip(it, accent=INK, size=24) for it in items])
        chips.arrange(DOWN, buff=0.32).move_to(DOWN * 0.1)
        # background bar that grows to show "Claude is ahead" — provides shape motion
        bar = Rectangle(width=0.1, height=chips.height + 0.3)
        bar.set_fill(INK, 0.07).set_stroke(INK, 1.0)
        bar.move_to(chips.get_center() + LEFT * 3.8)
        self.play(FadeIn(head), run_time=0.4)
        self.play(bar.animate.scale(20), run_time=0.5)
        for chip in chips:
            self.play(FadeIn(chip, shift=RIGHT * 0.15), run_time=0.35)
        self.wait(max(0.5, total - 0.4 - 0.5 - len(items) * 0.35))


class B05_SameWeights(Scene):
    def construct(self):
        total = DUR["B05"]
        # Central box: CLAUDE WEIGHTS
        weights_box = Rectangle(width=3.2, height=1.0)
        weights_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2.0)
        weights_lbl = Text("CLAUDE WEIGHTS", font=DISPLAY, color=SLATE,
                           font_size=22, weight="MEDIUM")
        weights_lbl.move_to(weights_box)
        weights = VGroup(weights_box, weights_lbl).move_to(LEFT * 1.5)

        # Two arrows: WRITE FUNCTION and AUDIT FUNCTION
        out_pt = RIGHT * 2.8 + UP * 1.0
        audit_pt = RIGHT * 2.8 + DOWN * 1.0

        write_arrow = _arrow(weights.get_right() + UP * 0.25,
                             out_pt + LEFT * 0.1, INK)
        write_lbl = Text("WRITE FUNCTION", font=DISPLAY, color=INK,
                         font_size=20, weight="MEDIUM")
        write_lbl.next_to(write_arrow, UP, buff=0.15)

        audit_arrow = _arrow(weights.get_right() + DOWN * 0.25,
                             audit_pt + LEFT * 0.1, CRIMSON)
        audit_lbl = Text("AUDIT FUNCTION", font=DISPLAY, color=CRIMSON,
                         font_size=20, weight="MEDIUM")
        audit_lbl.next_to(audit_arrow, DOWN, buff=0.15)

        not_indep = SerifLabel("not independent", CRIMSON, size=24)
        not_indep.move_to(RIGHT * 4.2 + DOWN * 1.6)

        self.play(FadeIn(weights), run_time=0.6)
        self.play(Create(write_arrow), FadeIn(write_lbl), run_time=0.7)
        self.play(Create(audit_arrow), FadeIn(audit_lbl), run_time=0.7)
        self.play(FadeIn(not_indep, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 2.6))


class B06_AuditRequires(Scene):
    def construct(self):
        total = DUR["B06"]
        t1 = Text("An audit needs access", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("to what Claude cannot see.", font=SERIF, color=CRIMSON,
                  font_size=46, weight="BOLD")
        t3 = Text("the spec that lives in your head", font=SERIF, color=INK,
                  font_size=30, slant=ITALIC)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.8))


class B07_PriyaTimeline(Scene):
    def construct(self):
        total = DUR["B07"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)
        eye = Text("Priya's leaderboard", font=DISPLAY, color=INK,
                   font_size=24, weight="MEDIUM").to_edge(UP, buff=0.65)

        spine = Line(LEFT * 5.5 + UP * 0.3, RIGHT * 5.5 + UP * 0.3,
                     color=HAIRLINE, stroke_width=1.5)

        n1 = _node("WRITE", INK, w=1.8).move_to(LEFT * 4.2 + UP * 0.3)
        n2 = _node("TESTS PASS", INK, w=2.0).move_to(LEFT * 1.8 + UP * 0.3)
        n3 = _node("DEPLOY", INK, w=1.8).move_to(RIGHT * 0.6 + UP * 0.3)

        gap_lbl = Text("1 week", font=SERIF, color=INK, font_size=20,
                       slant=ITALIC).move_to(RIGHT * 2.6 + UP * 0.85)
        gap_tick = Line(RIGHT * 2.6 + UP * 0.55, RIGHT * 2.6 + UP * 0.05,
                        color=HAIRLINE, stroke_width=1.5)

        n4 = _node("ZHAO ABOVE AMIR", CRIMSON, w=2.6).move_to(RIGHT * 4.3 + UP * 0.3)
        n4_sub = Text("parent emails teacher", font=SERIF, color=CRIMSON,
                      font_size=20, slant=ITALIC)
        n4_sub.next_to(n4, DOWN, buff=0.3)

        day_one = SerifLabel("bug was there from day one", CRIMSON, size=22)
        day_one.move_to(DOWN * 1.8)

        self.play(FadeIn(label), FadeIn(eye), run_time=0.5)
        self.play(Create(spine), run_time=0.5)
        for n in (n1, n2, n3):
            self.play(FadeIn(n), run_time=0.35)
        self.play(FadeIn(gap_lbl), Create(gap_tick), run_time=0.5)
        self.play(FadeIn(n4), run_time=0.4)
        self.play(FadeIn(n4_sub), run_time=0.4)
        self.play(FadeIn(day_one, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.6))


class B08_GapVisible(Scene):
    def construct(self):
        total = DUR["B08"]
        # Two columns: test set (left) and real data (right)
        lhead = LabelChip("TEST SET", accent=INK, size=24).move_to(LEFT * 3.5 + UP * 2.4)
        rhead = LabelChip("REAL DATA", accent=CRIMSON, size=24).move_to(RIGHT * 3.5 + UP * 2.4)

        # Test set rows — all ink (unique)
        test_rows = VGroup(
            *[Rectangle(width=2.8, height=0.32).set_fill(INK, 0.8).set_stroke(width=0, opacity=0)
              for _ in range(5)]
        ).arrange(DOWN, buff=0.12).move_to(LEFT * 3.5 + UP * 0.7)

        test_chip = LabelChip("UNIQUE GPAs", accent=INK, size=20)
        test_chip.next_to(test_rows, DOWN, buff=0.25)
        test_pass = LabelChip("TESTS PASS", accent=INK, size=22)
        test_pass.next_to(test_chip, DOWN, buff=0.2)

        # Real data rows — 4 ink + 2 crimson (tie)
        real_rows_ink = VGroup(
            *[Rectangle(width=2.8, height=0.32).set_fill(INK, 0.8).set_stroke(width=0, opacity=0)
              for _ in range(4)]
        ).arrange(DOWN, buff=0.12)
        real_rows_crimson = VGroup(
            *[Rectangle(width=2.8, height=0.32).set_fill(CRIMSON, 0.8).set_stroke(width=0, opacity=0)
              for _ in range(2)]
        ).arrange(DOWN, buff=0.12)
        real_rows = VGroup(real_rows_ink, real_rows_crimson).arrange(DOWN, buff=0.12)
        real_rows.move_to(RIGHT * 3.5 + UP * 0.7)

        tie_lbl = SerifLabel("TIE", CRIMSON, size=22)
        tie_lbl.next_to(real_rows_crimson, RIGHT, buff=0.25)
        real_bug = LabelChip("BUG FIRES", accent=CRIMSON, size=22)
        real_bug.next_to(real_rows, DOWN, buff=0.25)

        # Gap arrow
        gap_arrow = Arrow(test_rows.get_right() + RIGHT * 0.1,
                          real_rows.get_left() + LEFT * 0.1,
                          color=CRIMSON, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.18)
        gap_lbl = Text("invisible until\na tie appeared", font=SERIF,
                       color=CRIMSON, font_size=20, slant=ITALIC)
        gap_lbl.move_to(gap_arrow.get_center() + UP * 0.7)

        div = Line(UP * 3.0, DOWN * 3.0, color=HAIRLINE, stroke_width=1.3)

        self.play(FadeIn(lhead), FadeIn(rhead), FadeIn(div), run_time=0.5)
        self.play(FadeIn(test_rows), run_time=0.5)
        self.play(FadeIn(test_chip), FadeIn(test_pass), run_time=0.5)
        self.play(FadeIn(real_rows_ink), FadeIn(real_rows_crimson), FadeIn(tie_lbl),
                  run_time=0.6)
        self.play(FadeIn(real_bug), run_time=0.4)
        self.play(Create(gap_arrow), FadeIn(gap_lbl), run_time=0.7)
        self.wait(max(0.5, total - 3.2))


class B09_SolveVerify(Scene):
    def construct(self):
        total = DUR["B09"]
        # Two lines on a time axis
        ax_w = 9.0
        ax = Line(LEFT * ax_w / 2 + DOWN * 1.5, RIGHT * ax_w / 2 + DOWN * 1.5,
                  color=HAIRLINE, stroke_width=1.8)
        ax_lbl = Text("time", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        ax_lbl.next_to(ax, RIGHT, buff=0.2)

        # Claude solve speed — steep rise
        pts_c = [LEFT * ax_w / 2 + DOWN * 1.5,
                 LEFT * 1.5 + DOWN * 0.5,
                 RIGHT * 1.5 + UP * 1.4,
                 RIGHT * ax_w / 2 + UP * 2.6]
        solve_line = VMobject(color=CRIMSON, stroke_width=3.5)
        solve_line.set_points_smoothly([np.array([p[0], p[1], 0]) for p in pts_c])
        solve_lbl = LabelChip("CLAUDE SOLVE SPEED", accent=CRIMSON, size=22)
        solve_lbl.next_to(solve_line.get_end(), RIGHT, buff=0.2)

        # Human verification — roughly flat
        pts_h = [LEFT * ax_w / 2 + DOWN * 1.2,
                 LEFT * 1.5 + DOWN * 1.0,
                 RIGHT * 1.5 + DOWN * 0.7,
                 RIGHT * ax_w / 2 + DOWN * 0.6]
        verify_line = VMobject(color=INK, stroke_width=3.5)
        verify_line.set_points_smoothly([np.array([p[0], p[1], 0]) for p in pts_h])
        verify_lbl = LabelChip("HUMAN VERIFICATION", accent=INK, size=22)
        verify_lbl.next_to(verify_line.get_end() + RIGHT * 0.5, DOWN, buff=0.2)

        # Gap bracket
        gap_brace = Brace(
            VGroup(
                Dot(radius=0.01).move_to(verify_line.get_end()),
                Dot(radius=0.01).move_to(solve_line.get_end())
            ), RIGHT, color=CRIMSON
        )
        gap_lbl = SerifLabel("widening gap", CRIMSON, size=24)
        gap_lbl.next_to(gap_brace, RIGHT, buff=0.2)

        self.play(Create(ax), FadeIn(ax_lbl), run_time=0.5)
        self.play(Create(verify_line), FadeIn(verify_lbl), run_time=0.9)
        self.play(Create(solve_line), FadeIn(solve_lbl), run_time=0.9)
        self.play(FadeIn(gap_brace), FadeIn(gap_lbl), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B10_NameTheMove(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("Name the supervisory move", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("before you accept the output.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t3 = Text("if you can name it, you'll exercise it", font=SERIF,
                  color=INK, font_size=28, slant=ITALIC)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.36).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(t3, shift=UP * 0.08), run_time=0.5)
        self.wait(max(0.5, total - 1.8))


class B11_RunTwo(Scene):
    def construct(self):
        total = DUR["B11"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)
        head = Text("Run Two", font=DISPLAY, color=INK, font_size=26,
                    weight="MEDIUM").to_edge(UP, buff=0.65)

        steps = [
            ("PROBLEM FORMULATION", "add the tie-case first"),
            ("PLAUSIBILITY AUDIT", "Bell before Adams — wrong"),
            ("SPECIFIC FAILURE", "Adams first on GPA tie"),
            ("FIX + SHIPS CORRECT", "Adams ranks first"),
        ]

        nodes = VGroup()
        for label_text, sub_text in steps:
            chip = LabelChip(label_text, accent=INK, size=22)
            sub = Text(sub_text, font=SERIF, color=INK, font_size=20, slant=ITALIC)
            row = VGroup(chip, sub).arrange(RIGHT, buff=0.4)
            nodes.add(row)
        nodes.arrange(DOWN, buff=0.45).move_to(DOWN * 0.2)

        # arrows between steps
        arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = _arrow(nodes[i].get_bottom() + DOWN * 0.04,
                       nodes[i+1].get_top() + UP * 0.04, INK)
            arrows.add(a)

        self.play(FadeIn(label), FadeIn(head), run_time=0.5)
        for i, node in enumerate(nodes):
            self.play(FadeIn(node), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.35)
        self.wait(max(0.5, total - 0.5 - len(nodes) * 0.85))


class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("The model is fine.", font=SERIF, color=INK,
                  font_size=50, weight="BOLD")
        t2 = Text("The supervision is missing.", font=SERIF, color=CRIMSON,
                  font_size=50, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        eye.next_to(block, UP, buff=0.65)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
