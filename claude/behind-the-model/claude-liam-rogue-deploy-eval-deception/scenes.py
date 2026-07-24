"""
scenes.py — claude-liam-rogue-deploy-eval-deception
The Rogue Deploy Eval: Can an AI Secretly Disable Its Own Watchdog?
Source: Anthropic rogue-deploy-eval README + alignment.anthropic.com/2024/rogue-eval

Palette: Claude brand
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic — Rogue Deploy Eval (2024)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_EvalDesign(Scene):
    def construct(self):
        dur = 19.2

        title = Text("The Two-Box Architecture.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Generation function box
        gen_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.18,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([-3.0, 0.2, 0])
        gen_lbl = Text("Generation\nFunction", font_size=22, color=INK, weight=BOLD)
        gen_lbl.move_to(gen_box).shift(UP * 0.4)
        gen_sub = Text("Model must optimize this", font_size=15, color=SOFT)
        gen_sub.move_to(gen_box).shift(DOWN * 0.5)

        # Monitor box
        mon_box = RoundedRectangle(
            width=4.2, height=2.2, corner_radius=0.18,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([3.0, 0.2, 0])
        mon_lbl = Text("Monitor", font_size=22, color=SPARK, weight=BOLD)
        mon_lbl.move_to(mon_box).shift(UP * 0.4)
        mon_sub = Text("Penalizes flagged outputs", font_size=15, color=SOFT)
        mon_sub.move_to(mon_box).shift(DOWN * 0.5)

        # Arrow from gen to mon
        call_arr = Arrow(
            gen_box.get_right() + RIGHT * 0.05,
            mon_box.get_left() + LEFT * 0.05,
            color=GHOST, stroke_width=2, buff=0.05
        )
        call_lbl = Text("calls", font_size=16, color=SOFT)
        call_lbl.next_to(call_arr, UP, buff=0.12)

        # Model agent
        model_box = Rectangle(
            width=2.6, height=0.9, color=SOFT,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, -2.5, 0])
        model_lbl = Text("Model agent", font_size=18, color=SOFT)
        model_lbl.move_to(model_box)
        model_arr = Arrow(
            model_box.get_top() + UP * 0.05,
            gen_box.get_bottom() + DOWN * 0.05,
            color=SOFT, stroke_width=1.8, buff=0.05
        )
        task_lbl = Text("tasked to maximize score", font_size=15, color=SOFT)
        task_lbl.next_to(model_arr, RIGHT, buff=0.1)

        self.play(FadeIn(gen_box), FadeIn(gen_lbl), FadeIn(gen_sub), run_time=0.6)
        self.play(GrowArrow(call_arr), Write(call_lbl), run_time=0.5)
        self.play(FadeIn(mon_box), FadeIn(mon_lbl), FadeIn(mon_sub), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(model_box), FadeIn(model_lbl), GrowArrow(model_arr), Write(task_lbl), run_time=0.8)
        self.wait(dur - 4.8)


class B02_CheatBranch(Scene):
    def construct(self):
        dur = 20.8

        title = Text("Two Paths. One Is Cheating.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Root node
        root = Circle(radius=0.6, color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2)
        root.move_to([0, 2.0, 0])
        root_lbl = Text("Model", font_size=18, color=INK, weight=BOLD)
        root_lbl.move_to(root)

        # Path A — legitimate
        pathA_box = RoundedRectangle(
            width=4.2, height=1.4, corner_radius=0.15,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([-3.5, 0.0, 0])
        pathA_lbl = Text("A: Solve legitimately", font_size=18, color=INK, weight=BOLD)
        pathA_lbl.move_to(pathA_box)
        arrA = Arrow(root.get_left() + LEFT * 0.05, pathA_box.get_top() + UP * 0.05,
                     color=INK, stroke_width=2, buff=0.1)

        # Path B — cheat
        pathB_box = RoundedRectangle(
            width=4.8, height=1.4, corner_radius=0.15,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2
        ).move_to([3.5, 0.0, 0])
        pathB_lbl = Text("B: Disable monitor call", font_size=18, color=SPARK, weight=BOLD)
        pathB_lbl.move_to(pathB_box)
        arrB = Arrow(root.get_right() + RIGHT * 0.05, pathB_box.get_top() + UP * 0.05,
                     color=SPARK, stroke_width=2, buff=0.1)
        cheat_tag = Text("THE CHEAT", font_size=16, color=SPARK)
        cheat_tag.next_to(pathB_box, DOWN, buff=0.18)

        # Detection
        detect_box = Rectangle(
            width=9.5, height=0.9, color=BORDER,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, -2.2, 0])
        detect_txt = Text("Detection: git diff tests/   — tests unchanged = clean; monitor disabled = cheat", font_size=15, color=SOFT)
        detect_txt.move_to(detect_box)

        self.play(FadeIn(root), FadeIn(root_lbl), run_time=0.5)
        self.play(GrowArrow(arrA), FadeIn(pathA_box), FadeIn(pathA_lbl), run_time=0.7)
        self.play(GrowArrow(arrB), FadeIn(pathB_box), FadeIn(pathB_lbl), run_time=0.7)
        self.play(FadeIn(cheat_tag), run_time=0.4)
        self.wait(0.4)
        self.play(Create(detect_box), Write(detect_txt), run_time=0.8)
        self.wait(dur - 5.5)


class B03_EvalLesson(Scene):
    def construct(self):
        dur = 23.5

        title = Text("To Measure Deception, Make Deception Worth It.", font_size=33, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        rules = [
            ("1", "Legitimate task must be solvable", "If it's impossible, all models cheat."),
            ("2", "Cheat must be detectable", "git diff — tests unchanged confirms clean solve."),
            ("3", "Measure both paths", "Zero cheat rate may mean cheating was impossible."),
        ]

        for i, (num, rule, detail) in enumerate(rules):
            y = 1.4 - i * 1.5
            is_spark = num == "3"
            col = SPARK if is_spark else INK
            num_t = Text(num + ".", font_size=26, color=col, weight=BOLD)
            num_t.move_to([-5.5, y, 0])
            rule_t = Text(rule, font_size=20, color=col, weight=BOLD)
            rule_t.move_to([-0.5, y + 0.28, 0])
            detail_t = Text(detail, font_size=16, color=SOFT)
            detail_t.move_to([-0.5, y - 0.28, 0])
            self.play(FadeIn(num_t), Write(rule_t), run_time=0.5)
            self.play(FadeIn(detail_t), run_time=0.35)
            self.wait(0.2)

        verdict = Text("Most safety evals don't clear that bar.", font_size=21, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 7.0)
