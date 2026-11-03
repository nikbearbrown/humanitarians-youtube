"""
Manim scenes for claude-liam-binary-search-answer ("Claude, Halved.")
B01_BLUF        — the one-breath executive summary, text only
B02_Framework   — the answer range; a feasibility flip point
B03_Worked      — minimum ship capacity: guess, check, narrow
B04_Narrowing   — the brackets close in, log(range) guesses
B05_Monotonic   — falsifiability: this only works if feasible() is monotonic
"""

from manim import *
import numpy as np

INK = "#3D3929"
BG = "#FAF9F5"
ACCENT = "#D97757"
BLUE = "#5B7B9C"
GREEN = "#4A7C59"
RED = "#C0392B"

config.background_color = BG


class B01_BLUF(Scene):
    def construct(self):
        l1 = Text("If a yes/no question about x flips exactly once",
                   font_size=36, color=INK)
        l2 = Text("as x grows — infeasible, then feasible —",
                   font_size=36, color=INK)
        l3 = Text("binary search finds that flip point directly.",
                   font_size=36, color=ACCENT)
        for _l in (l1, l2, l3):
            if _l.width > 12.0:
                _l.scale_to_fit_width(12.0)
        l1.move_to(UP * 1.3)
        l2.move_to(UP * 0.1)
        l3.move_to(DOWN * 1.1)
        self.play(Write(l1), run_time=1.4)
        self.play(Write(l2), run_time=1.4)
        self.play(Write(l3), run_time=1.2)
        self.wait(1.2)


class B02_Framework(Scene):
    def construct(self):
        title = Text("The answer range, laid out on a line", font_size=32, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        line = NumberLine(x_range=[0, 10, 1], length=9, color=INK, include_numbers=False)
        line.move_to(ORIGIN)
        self.play(Create(line), run_time=1.0)

        infeasible = Line(line.n2p(0), line.n2p(4.6), color=RED, stroke_width=10)
        feasible = Line(line.n2p(4.6), line.n2p(10), color=GREEN, stroke_width=10)
        self.play(Create(infeasible), Create(feasible), run_time=1.2)

        flip_dot = Dot(line.n2p(4.6), radius=0.12, color=ACCENT)
        flip_lbl = Text("the answer", font_size=24, color=ACCENT).next_to(flip_dot, UP, buff=0.3)
        self.play(FadeIn(flip_dot, scale=0.5), FadeIn(flip_lbl), run_time=0.8)

        lo_lbl = Text("infeasible", font_size=24, color=RED).next_to(infeasible, DOWN, buff=0.3)
        hi_lbl = Text("feasible", font_size=24, color=GREEN).next_to(feasible, DOWN, buff=0.3)
        self.play(FadeIn(lo_lbl), FadeIn(hi_lbl), run_time=0.6)

        cap = Text("Find the flip in log(range) guesses, not by scanning.",
                    font_size=24, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.3)


class B03_Worked(Scene):
    def construct(self):
        title = Text("Minimum capacity to ship in D days", font_size=30, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        weights = [3, 5, 2, 6, 4, 7]
        boxes = VGroup(*[
            VGroup(Square(0.55, color=BLUE, fill_color=BLUE, fill_opacity=0.15),
                   Text(str(w), font_size=22, color=INK))
            for w in weights
        ])
        for grp in boxes:
            grp[1].move_to(grp[0].get_center())
        boxes.arrange(RIGHT, buff=0.3).move_to(UP * 1.2)
        self.play(*[FadeIn(b) for b in boxes], run_time=0.8)

        day1_bracket = Line(boxes[0].get_corner(DL) + DOWN * 0.15,
                             boxes[2].get_corner(DR) + DOWN * 0.15,
                             color=GREEN, stroke_width=4)
        self.play(Create(day1_bracket), run_time=0.6)

        guess = Text("guess capacity = 10", font_size=28, color=ACCENT).move_to(UP * 0.1)
        self.play(Write(guess), run_time=0.8)

        sim = Text("day 1: [3,5,2] = 10   day 2: [6,4] = 10   day 3: [7] = 7",
                    font_size=24, color=INK).move_to(DOWN * 0.6)
        self.play(FadeIn(sim), run_time=0.9)

        result = Text("3 days used, feasible for D=3 -> try smaller", font_size=26, color=GREEN)
        result.move_to(DOWN * 1.4)
        self.play(FadeIn(result), run_time=0.8)
        self.wait(1.4)


class B04_Narrowing(Scene):
    def construct(self):
        title = Text("Each guess cuts the range in half", font_size=32, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        line = NumberLine(x_range=[0, 20, 2], length=9, color=INK)
        line.move_to(UP * 0.3)
        self.play(Create(line), run_time=0.9)

        lo_val, hi_val = 0, 20
        lo_marker = Triangle(color=RED, fill_color=RED, fill_opacity=1).scale(0.15)
        hi_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.15).rotate(PI)
        lo_marker.next_to(line.n2p(lo_val), DOWN, buff=0.1)
        hi_marker.next_to(line.n2p(hi_val), DOWN, buff=0.1)
        self.play(FadeIn(lo_marker), FadeIn(hi_marker), run_time=0.6)

        steps = [(0, 20, 10, True), (0, 10, 5, False), (5, 10, 7, True), (5, 7, 6, True)]
        for lo, hi, mid, feasible in steps:
            mid_dot = Dot(line.n2p(mid), radius=0.1, color=ACCENT)
            mid_lbl = Text(str(mid), font_size=20, color=ACCENT).next_to(mid_dot, UP, buff=0.15)
            self.play(FadeIn(mid_dot, scale=0.6), FadeIn(mid_lbl), run_time=0.4)
            self.wait(0.2)
            self.play(FadeOut(mid_dot), FadeOut(mid_lbl), run_time=0.2)
            new_lo, new_hi = (lo, mid) if feasible else (mid, hi)
            self.play(
                lo_marker.animate.next_to(line.n2p(new_lo), DOWN, buff=0.1) if not feasible else lo_marker.animate,
                hi_marker.animate.next_to(line.n2p(new_hi), DOWN, buff=0.1) if feasible else hi_marker.animate,
                run_time=0.5,
            )

        cap = Text("Four guesses covered a range of twenty.",
                    font_size=26, color=INK).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=0.8)
        self.wait(1.3)


class B05_Monotonic(Scene):
    def construct(self):
        title = Text("Only works if feasible() truly flips once", font_size=30, color=INK)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.8)

        good_label = Text("monotonic — safe", font_size=24, color=GREEN).move_to(UP * 1.0 + LEFT * 3.2)
        good_line = NumberLine(x_range=[0, 8, 1], length=5, color=INK).move_to(UP * 0.3 + LEFT * 3.2)
        good_seq = ["F", "F", "F", "T", "T", "T", "T"]
        self.play(FadeIn(good_label), Create(good_line), run_time=0.8)
        for i, v in enumerate(good_seq):
            col = RED if v == "F" else GREEN
            dot = Dot(good_line.n2p(i + 0.5), radius=0.08, color=col)
            self.add(dot)
        self.wait(0.4)

        bad_label = Text("NOT monotonic — breaks", font_size=24, color=RED).move_to(UP * 1.0 + RIGHT * 3.2)
        bad_line = NumberLine(x_range=[0, 8, 1], length=5, color=INK).move_to(UP * 0.3 + RIGHT * 3.2)
        bad_seq = ["F", "T", "F", "T", "T", "F", "T"]
        self.play(FadeIn(bad_label), Create(bad_line), run_time=0.8)
        for i, v in enumerate(bad_seq):
            col = RED if v == "F" else GREEN
            dot = Dot(bad_line.n2p(i + 0.5), radius=0.08, color=col)
            self.add(dot)
        self.wait(0.4)

        cap = Text("A non-monotonic flip gives binary search a wrong,\nconfident-looking answer — check monotonicity first.",
                    font_size=18, color=INK, line_spacing=1.2).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cap), run_time=1.0)
        self.wait(1.6)
