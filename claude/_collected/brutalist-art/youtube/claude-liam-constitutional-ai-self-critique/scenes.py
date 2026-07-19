"""
scenes.py — claude-liam-constitutional-ai-self-critique
Constitutional AI: Teaching an AI to Grade Its Own Homework.
Source: Anthropic — arXiv 2212.08073

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider
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
        "After Bai et al. 2022 — Constitutional AI (Anthropic)",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_LabelingProblem(Scene):
    def construct(self):
        dur = 17.7

        title = Text("Human Labeling Has Three Problems.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        problems = [
            ("Expensive", "Thousands of annotators\nper training run."),
            ("Inconsistent", "Annotators disagree on\nwhat 'harmful' means."),
            ("Pattern-matching", "Model learns what annotators\ndisliked, not why."),
        ]

        xs = [-4.2, 0.0, 4.2]
        for (label, detail), x in zip(problems, xs):
            is_spark = label == "Pattern-matching"
            col = SPARK if is_spark else INK
            box = RoundedRectangle(
                width=3.5, height=2.8, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, -0.1, 0])
            lbl = Text(label, font_size=20, color=col, weight=BOLD)
            lbl.move_to(box).shift(UP * 0.8)
            dtl = Text(detail, font_size=16, color=SOFT)
            dtl.move_to(box).shift(DOWN * 0.3)
            self.play(FadeIn(VGroup(box, lbl, dtl)), run_time=0.6)
            self.wait(0.2)

        verdict = Text("Pattern-matching is the deepest problem.", font_size=20, color=SPARK, weight=BOLD)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 5.3)


class B02_CritiqueLoop(Scene):
    def construct(self):
        dur = 21.2

        title = Text("The Critique-Revision Loop.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Three stages in a loop
        stages = ["Harmful\nresponse", "Critique\nvs principle", "Revised\nresponse"]
        xs = [-4.5, 0.0, 4.5]
        boxes = []
        for s, x in zip(stages, xs):
            col = SPARK if s == "Revised\nresponse" else INK
            b = Circle(radius=0.9, color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.2)
            b.move_to([x, 0.6, 0])
            t = Text(s, font_size=17, color=col)
            t.move_to(b)
            boxes.append(VGroup(b, t))

        arr1 = Arrow(boxes[0].get_right() + RIGHT * 0.05, boxes[1].get_left() + LEFT * 0.05,
                     color=GHOST, stroke_width=2, buff=0.05)
        arr2 = Arrow(boxes[1].get_right() + RIGHT * 0.05, boxes[2].get_left() + LEFT * 0.05,
                     color=GHOST, stroke_width=2, buff=0.05)
        loop_arr = CurvedArrow(
            boxes[2].get_bottom() + DOWN * 0.05,
            boxes[0].get_bottom() + DOWN * 0.05,
            color=SOFT, stroke_width=1.8, angle=-TAU / 3
        )
        iter_lbl = Text("× 3 iterations", font_size=18, color=SOFT)
        iter_lbl.move_to([0, -1.6, 0])

        # Constitution doc
        const_box = Rectangle(
            width=3.0, height=1.4, color=SPARK,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.8
        ).move_to([0, 2.5, 0]).shift(DOWN * 0.2)
        const_lbl = Text("16 principles\n(the constitution)", font_size=16, color=SPARK)
        const_lbl.move_to(const_box)
        const_arrow = Arrow(const_box.get_bottom(), boxes[1].get_top() + UP * 0.05,
                            color=SPARK, stroke_width=1.8, buff=0.1)

        training = Text("Self-revised responses become training data.", font_size=19, color=SPARK, weight=BOLD)
        training.to_edge(DOWN, buff=0.55)

        for grp in boxes:
            self.play(FadeIn(grp), run_time=0.4)
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.6)
        self.play(Create(loop_arr), Write(iter_lbl), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(const_box), Write(const_lbl), GrowArrow(const_arrow), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(training), run_time=0.5)
        self.wait(dur - 6.7)


class B03_RLAIFResult(Scene):
    def construct(self):
        dur = 21.2

        title = Text("Same Harmlessness. Slightly Better Helpfulness.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        ground_y = -2.2
        ground = Line(LEFT * 5.5, RIGHT * 5.5, color=BORDER, stroke_width=1.5).shift(DOWN * 2.2)
        self.add(ground)

        y_lbl = Text("Score", font_size=18, color=SOFT)
        y_lbl.to_edge(LEFT, buff=0.4).shift(UP * 0.5)
        self.add(y_lbl)

        # Legend
        lb = Rectangle(width=0.28, height=0.28, color=INK, fill_color=INK, fill_opacity=1, stroke_width=0)
        lt = Text("RLHF (human labels)", font_size=17, color=INK)
        leg1 = VGroup(lb, lt).arrange(RIGHT, buff=0.15).to_corner(UR, buff=0.6)
        la = Rectangle(width=0.28, height=0.28, color=SPARK, fill_color=SPARK, fill_opacity=1, stroke_width=0)
        lta = Text("CAI (self-critique)", font_size=17, color=SPARK)
        leg2 = VGroup(la, lta).arrange(RIGHT, buff=0.15)
        leg2.next_to(leg1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(leg1, leg2)

        def make_bar(x_center, bar_w, height_frac, color):
            h = height_frac * 4.0
            r = Rectangle(
                width=bar_w, height=h,
                color=color, fill_color=color, fill_opacity=0.88, stroke_width=0
            )
            r.move_to([x_center, ground_y + h / 2, 0])
            return r

        bw = 0.8
        gp = 0.14
        xa, xb = -1.8, 1.8

        # Harmlessness — equal
        bfr_h = make_bar(xa - bw / 2 - gp / 2, bw, 0.72, INK)
        aft_h = make_bar(xa + bw / 2 + gp / 2, bw, 0.72, SPARK)
        # Helpfulness — CAI slightly better
        bfr_p = make_bar(xb - bw / 2 - gp / 2, bw, 0.58, INK)
        aft_p = make_bar(xb + bw / 2 + gp / 2, bw, 0.65, SPARK)

        harm_lbl = Text("Harmlessness", font_size=17, color=SOFT)
        harm_lbl.move_to([xa, ground_y - 0.45, 0])
        help_lbl = Text("Helpfulness", font_size=17, color=SOFT)
        help_lbl.move_to([xb, ground_y - 0.45, 0])
        self.add(harm_lbl, help_lbl)

        spark_arr = Arrow(aft_p.get_top() + UP * 0.05, aft_p.get_top() + UP * 0.7,
                          color=SPARK, stroke_width=2.5, buff=0)
        spark_note = Text("Slightly better", font_size=17, color=SPARK)
        spark_note.next_to(spark_arr, RIGHT, buff=0.15)

        caveat = Text("Human values are still in the loop — now they're written down.", font_size=18, color=SOFT)
        caveat.to_edge(DOWN, buff=0.55)

        self.play(Create(bfr_h), Create(bfr_p), run_time=0.7)
        self.play(Create(aft_h), Create(aft_p), run_time=0.8)
        self.wait(0.3)
        self.play(GrowArrow(spark_arr), Write(spark_note), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(caveat), run_time=0.5)
        self.wait(dur - 5.3)
