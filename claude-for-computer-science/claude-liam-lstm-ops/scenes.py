"""scenes.py — Manim for claude-liam-lstm-ops. Source: embedded-ai Ch. 06"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")  # ONE per scene
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_CnnSinglePass(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("CNN: One Pass", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Single input block → output block (one pass)
        input_box = Rectangle(width=2.0, height=1.5,
                             fill_color=SOFT, fill_opacity=0.3,
                             stroke_width=2, stroke_color=INK)
        input_box.move_to([-3.5, 0, 0])
        input_label = Text("Input", font_size=14, color=INK)
        input_label.move_to(input_box.get_center())

        arrow = Arrow([-2.4, 0, 0], [-0.6, 0, 0], color=INK, stroke_width=2)

        cnn_box = Rectangle(width=2.0, height=1.5,
                           fill_color=SOFT, fill_opacity=0.6,
                           stroke_width=2, stroke_color=INK)
        cnn_box.move_to([0.5, 0, 0])
        cnn_label = Text("CNN\n17M MACs", font_size=13, color=INK)
        cnn_label.move_to(cnn_box.get_center())

        arrow2 = Arrow([1.6, 0, 0], [3.0, 0, 0], color=INK, stroke_width=2)

        out_box = Rectangle(width=1.5, height=1.5,
                           fill_color=SOFT, fill_opacity=0.8,
                           stroke_width=2, stroke_color=INK)
        out_box.move_to([3.8, 0, 0])
        out_label = Text("Output", font_size=13, color=INK)
        out_label.move_to(out_box.get_center())

        self.play(FadeIn(input_box), FadeIn(input_label))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(cnn_box), FadeIn(cnn_label))
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(out_box), FadeIn(out_label))

        # Counter
        counter = Text("Total MACs: 17,000,000  (done)", font_size=16, color=INK)
        counter.move_to([0, -1.8, 0])
        self.play(FadeIn(counter))

        params_note = Text("Parameters: 1.4 M", font_size=14, color=SOFT)
        params_note.move_to([0, -2.5, 0])
        self.play(FadeIn(params_note))
        self.wait(1)


class B02_LstmAccumulate(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("LSTM: Runs Every Step", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Show 5 time steps (represent 100)
        n_show = 5
        box_w = 1.4
        spacing = 1.6
        start_x = -4.0
        box_y = 0.5

        total_counter_val = [0]

        counter_text = Text("MACs: 0", font_size=18, color=ACC)
        counter_text.move_to([2.5, -1.5, 0])
        self.play(FadeIn(counter_text))

        for i in range(n_show):
            step_box = Rectangle(width=box_w, height=1.2,
                                fill_color=SOFT, fill_opacity=0.5 + i * 0.08,
                                stroke_width=1, stroke_color=INK)
            step_box.move_to([start_x + i * spacing, box_y, 0])
            step_label = Text(f"t={i+1}\n14M", font_size=11, color=INK)
            step_label.move_to(step_box.get_center())

            self.play(FadeIn(step_box), FadeIn(step_label), run_time=0.4)

            total_counter_val[0] += 14
            new_text = Text(f"MACs: {total_counter_val[0]}M", font_size=18, color=ACC)
            new_text.move_to([2.5, -1.5, 0])
            self.play(Transform(counter_text, new_text), run_time=0.3)

        # Ellipsis for remaining steps
        dots = Text("... × 100 steps", font_size=16, color=INK)
        dots.move_to([start_x + n_show * spacing + 0.5, box_y, 0])
        self.play(FadeIn(dots))

        final = Text("Total: 1.4 BILLION MACs", font_size=17, color=ACC, weight=BOLD)
        final.move_to([0, -2.5, 0])
        self.play(FadeIn(final))

        params_note = Text("Parameters: 0.2 M  (smaller than CNN)", font_size=14, color=SOFT)
        params_note.move_to([0, -3.1, 0])
        self.play(FadeIn(params_note))
        self.wait(1)


class B03_Inversion(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 06", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("The Inversion", font_size=28, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Two grouped bar charts: Params vs Ops
        # Left group: Parameters (LSTM smaller)
        # Right group: Operations (LSTM 80× larger)

        col_labels = ["Parameters", "Total Ops"]
        col_xs = [-2.5, 2.5]

        col_label_objs = []
        for lbl, x in zip(col_labels, col_xs):
            t = Text(lbl, font_size=16, color=INK, weight=BOLD)
            t.move_to([x, 2.0, 0])
            col_label_objs.append(t)
        self.play(*[FadeIn(t) for t in col_label_objs])

        bar_w = 0.9
        bottom_y = -2.2
        max_h = 3.5

        # Parameters: LSTM 0.2M, CNN 1.4M → max_h corresponds to 1.4M
        lstm_param_h = (0.2 / 1.4) * max_h
        cnn_param_h = max_h

        # Ops: CNN 17M, LSTM 1400M → max_h corresponds to 1400M
        lstm_ops_h = max_h
        cnn_ops_h = (17.0 / 1400.0) * max_h

        specs = [
            # (x_offset, h, color, label_text)
            (-2.5 - bar_w * 0.55, lstm_param_h, SOFT, "LSTM\n0.2M"),
            (-2.5 + bar_w * 0.55, cnn_param_h, INK, "CNN\n1.4M"),
            (2.5 - bar_w * 0.55, cnn_ops_h, INK, "CNN\n17M"),
            (2.5 + bar_w * 0.55, lstm_ops_h, ACC, "LSTM\n1.4B"),
        ]

        for x, h, color, lbl in specs:
            bar = Rectangle(width=bar_w, height=h,
                           fill_color=color, fill_opacity=0.75, stroke_width=0)
            bar.move_to([x, bottom_y + h / 2, 0])
            label = Text(lbl, font_size=11, color=INK)
            label.next_to(bar, DOWN, buff=0.1)
            self.play(GrowFromEdge(bar, DOWN), FadeIn(label), run_time=0.5)

        annotation = Text("82× more ops. 7× fewer params.", font_size=15, color=ACC, weight=BOLD)
        annotation.move_to([0, -3.1, 0])
        self.play(FadeIn(annotation))
        self.wait(1)
