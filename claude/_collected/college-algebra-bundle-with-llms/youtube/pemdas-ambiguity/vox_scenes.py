import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_PEMDASAmbiguity(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("8 ÷ 2(2+2): Two Valid Answers",
                     font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        expr = Text("8 ÷ 2(2+2)", font="Prism", font_size=36, color=INK, weight=BOLD)
        expr.move_to([0, 2.3, 0])
        self.play(FadeIn(expr), run_time=0.4)

        divider = Line(start=[0, 1.9, 0], end=[0, -2.0, 0], color=SLATE, stroke_width=1.5)
        self.play(GrowFromEdge(divider, UP), run_time=0.4)

        left_hdr = Text("Implicit mult. first:", font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        left_hdr.move_to([-3.0, 1.4, 0])
        self.play(FadeIn(left_hdr), run_time=0.3)

        for i, step in enumerate(["8 ÷ [2×(2+2)]", "8 ÷ [2×4]", "8 ÷ 8", "= 1"]):
            clr = CRIMSON if step == "= 1" else INK
            lbl = Text(step, font="Prism", font_size=18, color=clr)
            lbl.move_to([-3.0, 0.7 - i * 0.55, 0])
            self.play(FadeIn(lbl), run_time=0.3)

        right_hdr = Text("Left-to-right ÷:", font="Prism", font_size=17, color=INK, weight=BOLD)
        right_hdr.move_to([3.0, 1.4, 0])
        self.play(FadeIn(right_hdr), run_time=0.3)

        for i, step in enumerate(["8 ÷ 2 = 4, then ×4", "4 × (2+2)", "4 × 4", "= 16"]):
            clr = INK if step != "= 16" else CRIMSON
            lbl = Text(step, font="Prism", font_size=18, color=clr)
            lbl.move_to([3.0, 0.7 - i * 0.55, 0])
            self.play(FadeIn(lbl), run_time=0.3)

        verdict = Text("Both valid — expression is ambiguous. Always write explicit parentheses.",
                       font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        verdict.move_to([0, -2.5, 0])
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(max(0, dur - 6.0))


class B06_PEMDASFixed(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("The Fix: Explicit Parentheses",
                     font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("P", "Parentheses first",     "(2+2) = 4",         2.1),
            ("E", "Exponents",             "none here",          1.3),
            ("M/D", "Mult & Div left→right","depends on grouping",0.5),
            ("A/S", "Add & Sub last",       "done",             -0.3),
        ]
        for letter, rule, example, y in rows:
            dot = Dot(point=[-5.8, y, 0], color=CRIMSON, radius=0.13)
            let_lbl = Text(letter, font="Prism", font_size=20, color=CRIMSON, weight=BOLD)
            let_lbl.move_to([-5.0, y, 0])
            rule_lbl = Text(rule, font="Prism", font_size=17, color=INK)
            rule_lbl.move_to([-2.8, y, 0], aligned_edge=LEFT)
            ex_lbl = Text(example, font="Prism", font_size=15, color=SLATE)
            ex_lbl.move_to([2.0, y, 0], aligned_edge=LEFT)
            self.play(GrowFromCenter(dot), run_time=0.2)
            self.play(FadeIn(let_lbl), FadeIn(rule_lbl), FadeIn(ex_lbl), run_time=0.3)

        box_a = Rectangle(width=4.5, height=0.65, fill_color=CREAM,
                          fill_opacity=1, stroke_color=INK, stroke_width=2)
        box_a.move_to([-2.0, -1.4, 0])
        lbl_a = Text("(8÷2)(2+2) = 4×4 = 16", font="Prism", font_size=17, color=INK)
        lbl_a.move_to([-2.0, -1.4, 0])
        self.play(GrowFromCenter(box_a), run_time=0.4)
        self.play(FadeIn(lbl_a), run_time=0.2)

        box_b = Rectangle(width=4.5, height=0.65, fill_color=CREAM,
                          fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        box_b.move_to([2.8, -1.4, 0])
        lbl_b = Text("8÷(2(2+2)) = 8÷8 = 1", font="Prism", font_size=17, color=CRIMSON)
        lbl_b.move_to([2.8, -1.4, 0])
        self.play(GrowFromCenter(box_b), run_time=0.4)
        self.play(FadeIn(lbl_b), run_time=0.2)

        note = Text("Different parentheses → different answers. Write what you mean.",
                    font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0, dur - 5.0))
