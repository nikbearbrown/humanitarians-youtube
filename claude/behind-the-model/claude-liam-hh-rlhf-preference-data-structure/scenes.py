"""
scenes.py — claude-liam-hh-rlhf-preference-data-structure
RLHF Preference Data: Chosen/Rejected Pairs and Why Pairwise Wins.
Source: Bai et al. 2022 — Training a Helpful and Harmless Assistant with RLHF
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
        "After Bai et al. 2022 — HH-RLHF, Anthropic",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_ChosenRejectedPair(Scene):
    def construct(self):
        dur = 20.0

        title = Text("One Prompt. Chosen. Rejected.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Prompt box at top
        prompt_box = RoundedRectangle(
            width=8.0, height=0.9, corner_radius=0.14,
            color=GHOST, fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([0, 2.0, 0])
        prompt_lbl = Text(
            'Prompt: "Explain RLHF in one paragraph."',
            font_size=15, color=SOFT
        )
        prompt_lbl.move_to(prompt_box)
        self.play(FadeIn(prompt_box), Write(prompt_lbl), run_time=0.4)

        # Two arrows down
        arr_l = Arrow([0, 1.5, 0], [-3.5, 0.4, 0], color=GHOST, stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.1)
        arr_r = Arrow([0, 1.5, 0], [3.5, 0.4, 0], color=GHOST, stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.1)
        self.play(GrowArrow(arr_l), GrowArrow(arr_r), run_time=0.3)

        # Chosen box
        chosen_box = RoundedRectangle(
            width=5.0, height=2.0, corner_radius=0.16,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([-3.5, -0.5, 0])
        chosen_hdr = Text("CHOSEN", font_size=16, color=INK, weight=BOLD)
        chosen_hdr.next_to(chosen_box, UP, buff=0.1)
        chosen_body = Text(
            "Clear, accurate, well-structured\nexplanation preferred by\nhuman annotator.",
            font_size=13, color=SOFT
        )
        chosen_body.move_to(chosen_box)
        self.play(FadeIn(chosen_box), Write(chosen_hdr), FadeIn(chosen_body), run_time=0.4)

        # Rejected box
        rejected_box = RoundedRectangle(
            width=5.0, height=2.0, corner_radius=0.16,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([3.5, -0.5, 0])
        rejected_hdr = Text("REJECTED", font_size=16, color=SPARK, weight=BOLD)
        rejected_hdr.next_to(rejected_box, UP, buff=0.1)
        rejected_body = Text(
            "Vague, incomplete, or subtly\nwrong response not preferred\nby human annotator.",
            font_size=13, color=SOFT
        )
        rejected_body.move_to(rejected_box)
        self.play(FadeIn(rejected_box), Write(rejected_hdr), FadeIn(rejected_body), run_time=0.4)

        note = Text(
            "Triple = (prompt, chosen, rejected). Reward model trains to predict chosen.",
            font_size=16, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.5)


class B02_PairwiseVsAbsolute(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Pairwise Beats Absolute Rating.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Method", "Task for annotator", "Problem"]
        col_xs = [-4.5, 0.0, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Absolute rating", '"Score A: 1–10"',      SPARK, "Hard to calibrate,\nhigh variance"),
            ("Pairwise",        '"Which is better, A or B?"', INK,
             "Easier, more reliable,\nscale-invariant"),
        ]
        for i, (method, task, col, prob) in enumerate(rows):
            y = 1.0 - i * 1.5
            vals = [method, task, prob]
            vcols = [col, SOFT, SOFT]
            for val, x, vcol in zip(vals, col_xs, vcols):
                t = Text(val, font_size=14, color=vcol)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.25)

        rule = Text(
            "Pairwise: no calibration, no shared scale — just which is better.",
            font_size=17, color=SPARK, weight=BOLD
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.5)


class B03_DataStructureConsequences(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Structure Has Downstream Consequences.", font_size=33, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        rules = [
            ("Same prompt required",
             "Different prompts → model learns\nprompt differences, not quality."),
            ("Margin matters",
             "Near-ties → noisy reward signal.\nClear preferences → sharper model."),
            ("Rejected distribution shapes avoidance",
             "Random rejects → model avoids noise.\nPlausible rejects → model avoids subtle errors."),
        ]
        for i, (label, detail) in enumerate(rules):
            y = 1.5 - i * 1.4
            col = SPARK if i == 0 else INK
            lbl = Text(label, font_size=16, color=col, weight=BOLD)
            lbl.move_to([-1.2, y, 0])
            dtl = Text(detail, font_size=13, color=SOFT)
            dtl.move_to([3.2, y - 0.15, 0])
            sep = Line([-6.5, y - 0.6, 0], [6.5, y - 0.6, 0], color=BORDER, stroke_width=0.8)
            self.play(FadeIn(lbl), FadeIn(dtl), run_time=0.35)
            self.play(FadeIn(sep), run_time=0.15)

        verdict = Text(
            "Garbage collected pairs → garbage reward model.",
            font_size=17, color=SPARK, weight=BOLD
        )
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.4)
        self.wait(dur - 5.5)
