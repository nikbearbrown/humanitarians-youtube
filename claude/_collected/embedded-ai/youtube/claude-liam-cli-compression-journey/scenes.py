from manim import *
import numpy as np

BG = ManimColor("#FAF9F5")
INK = ManimColor("#3D3929")
ACC = ManimColor("#D97757")
SOFT = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")
GREEN = ManimColor("#4A7C59")


def source_credit(scene):
    return Text(
        "Source: Embedded AI (Aditi & Nik Bear Brown), Ch. 12",
        font_size=11, color=GHOST
    ).to_corner(DR, buff=0.5)


class B01_FP32State(Scene):
    def construct(self):
        self.camera.background_color = BG
        src = source_credit(self)
        self.add(src)

        title = Text("FP32 Baseline — All Metrics Over Ceiling", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        metrics = ["Flash", "SRAM", "Latency", "Accuracy"]
        fp32_vals = [6.0, 1.2, 320, 89.8]
        ceilings = [2.0, 1.0, 250, 88.0]
        units = ["MB", "MB", "ms", "%"]
        # normalized values (out of ceiling*1.5 for bar scale)
        max_bar = 3.0  # ceiling multiplier for max bar height
        bar_h_scale = 2.8  # max visual bar height

        bar_w = 1.2
        gap = 0.6
        n = len(metrics)
        total_w = n * bar_w + (n - 1) * gap
        start_x = -total_w / 2 + bar_w / 2

        axes_line = Line(
            start=LEFT * (total_w / 2 + 0.3),
            end=RIGHT * (total_w / 2 + 0.3),
            color=INK, stroke_width=2
        ).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        bars = VGroup()
        ceiling_lines = VGroup()
        labels = VGroup()
        value_labels = VGroup()

        for i, (m, v, c, u) in enumerate(zip(metrics, fp32_vals, ceilings, units)):
            x = start_x + i * (bar_w + gap)
            norm_v = min(v / c, max_bar)  # cap at 3x ceiling
            norm_c = 1.0  # ceiling at normalized 1
            bar_height = norm_v * bar_h_scale / max_bar
            ceil_height = norm_c * bar_h_scale / max_bar

            bar = Rectangle(
                width=bar_w, height=bar_height,
                fill_color=ACC, fill_opacity=0.85,
                stroke_color=ACC, stroke_width=1
            ).move_to([x, -1.5 + bar_height / 2, 0])
            bars.add(bar)

            ceil_y = -1.5 + ceil_height
            ceil_line = DashedLine(
                start=[x - bar_w / 2 - 0.1, ceil_y, 0],
                end=[x + bar_w / 2 + 0.1, ceil_y, 0],
                color=INK, stroke_width=2, dash_length=0.1
            )
            ceiling_lines.add(ceil_line)

            label = Text(m, font_size=16, color=INK).move_to([x, -1.5 - 0.3, 0])
            labels.add(label)

            val_text = f"{v}{u}"
            val_label = Text(val_text, font_size=13, color=INK).move_to([x, -1.5 + bar_height + 0.2, 0])
            value_labels.add(val_label)

        over_label = Text("All over ceiling!", font_size=20, color=ACC).next_to(title, DOWN, buff=0.3)

        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2))
        self.play(Create(ceiling_lines), FadeIn(labels), FadeIn(value_labels))
        self.play(FadeIn(over_label))
        self.wait(1.5)


class B02_INT8Step(Scene):
    def construct(self):
        self.camera.background_color = BG
        src = source_credit(self)
        self.add(src)

        title = Text("INT8 PTQ — Flash Drops, Latency Unchanged", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        metrics = ["Flash", "SRAM", "Latency", "Accuracy"]
        fp32_vals = [6.0, 1.2, 320, 89.8]
        int8_vals = [1.5, 0.8, 320, 89.8]
        ceilings = [2.0, 1.0, 250, 88.0]
        units = ["MB", "MB", "ms", "%"]
        bar_h_scale = 2.8
        max_bar = 3.0
        bar_w = 1.1
        gap = 0.5
        n = len(metrics)
        total_w = n * (bar_w * 2 + 0.15) + (n - 1) * gap
        start_x = -total_w / 2 + bar_w

        axes_line = Line(
            start=LEFT * (total_w / 2 + 0.3),
            end=RIGHT * (total_w / 2 + 0.3),
            color=INK, stroke_width=2
        ).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        for i, (m, fv, iv, c, u) in enumerate(zip(metrics, fp32_vals, int8_vals, ceilings, units)):
            x_center = start_x + i * (bar_w * 2 + 0.15 + gap)
            x_fp32 = x_center - bar_w / 2 - 0.05
            x_int8 = x_center + bar_w / 2 + 0.05

            norm_fv = min(fv / c, max_bar)
            norm_iv = min(iv / c, max_bar)
            fh = norm_fv * bar_h_scale / max_bar
            ih = norm_iv * bar_h_scale / max_bar
            ceil_h = bar_h_scale / max_bar

            fp32_bar = Rectangle(
                width=bar_w * 0.9, height=fh,
                fill_color=SOFT, fill_opacity=0.5,
                stroke_color=SOFT, stroke_width=1
            ).move_to([x_fp32, -1.5 + fh / 2, 0])

            # Flash and SRAM drop — terracotta; Latency unchanged — accent on ceiling miss
            bar_color = ACC if iv > c else GREEN
            int8_bar = Rectangle(
                width=bar_w * 0.9, height=ih,
                fill_color=bar_color, fill_opacity=0.85,
                stroke_color=bar_color, stroke_width=1
            ).move_to([x_int8, -1.5 + ih / 2, 0])

            ceil_y = -1.5 + ceil_h
            ceil_line = DashedLine(
                start=[x_center - bar_w - 0.2, ceil_y, 0],
                end=[x_center + bar_w + 0.2, ceil_y, 0],
                color=INK, stroke_width=2, dash_length=0.1
            )

            label = Text(m, font_size=14, color=INK).move_to([x_center, -1.5 - 0.3, 0])
            val_label = Text(f"{iv}{u}", font_size=12, color=INK).move_to([x_int8, -1.5 + ih + 0.2, 0])

            self.play(
                GrowFromEdge(fp32_bar, DOWN),
                GrowFromEdge(int8_bar, DOWN),
                Create(ceil_line),
                FadeIn(label), FadeIn(val_label),
                run_time=0.5
            )

        note = Text("Latency stays at 320 ms — quantization doesn't move compute", font_size=16, color=ACC).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note))
        self.wait(1.5)


class B03_PruneStep(Scene):
    def construct(self):
        self.camera.background_color = BG
        src = source_credit(self)
        self.add(src)

        title = Text("+ 25% Structured Prune — All Under Ceiling", font_size=26, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        states = ["FP32", "INT8", "+Prune"]
        metrics = ["Flash (MB)", "SRAM (MB)", "Latency (ms)", "Accuracy (%)"]
        vals = [
            [6.0, 1.2, 320, 89.8],
            [1.5, 0.8, 320, 89.8],
            [1.125, 0.6, 240, 89.0],
        ]
        ceilings = [2.0, 1.0, 250, 88.0]

        rows = VGroup()
        for i, (state, row) in enumerate(zip(states, vals)):
            cells = VGroup()
            state_label = Text(state, font_size=16, color=SOFT if i < 2 else INK, weight=BOLD if i == 2 else NORMAL)
            cells.add(state_label)
            for j, (v, c) in enumerate(zip(row, ceilings)):
                col = ACC if v > c else (GREEN if i == 2 else INK)
                t = Text(f"{v}", font_size=15, color=col)
                cells.add(t)
            cells.arrange(RIGHT, buff=0.7)
            cells.shift(UP * (0.8 - i * 0.85))
            rows.add(cells)

        header = VGroup(
            Text("State", font_size=14, color=SOFT),
            *[Text(m, font_size=12, color=SOFT) for m in metrics]
        ).arrange(RIGHT, buff=0.5)
        header.shift(UP * 1.8)

        self.play(FadeIn(header))
        for r in rows:
            self.play(FadeIn(r), run_time=0.6)

        check = Text("All ceilings met at +Prune state", font_size=18, color=GREEN).to_edge(DOWN, buff=1.0)
        box = SurroundingRectangle(rows[2], color=ACC, buff=0.1)
        self.play(Create(box), FadeIn(check))
        self.wait(1.5)


class B04_DistillShip(Scene):
    def construct(self):
        self.camera.background_color = BG
        src = source_credit(self)
        self.add(src)

        title = Text("+ Distillation — Accuracy Climbs, Ship State Reached", font_size=24, color=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        states = ["FP32", "INT8", "+Prune", "+Distill"]
        acc_vals = [89.8, 89.8, 89.0, 90.6]
        colors = [SOFT, SOFT, INK, ACC]

        bar_w = 1.5
        gap = 0.4
        bar_h_scale = 2.5
        acc_min = 88.0
        acc_max = 92.0
        acc_range = acc_max - acc_min

        axes_line = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=2).shift(DOWN * 1.5)
        self.play(Create(axes_line))

        start_x = -((len(states) * bar_w + (len(states) - 1) * gap) / 2) + bar_w / 2

        for i, (state, acc, col) in enumerate(zip(states, acc_vals, colors)):
            x = start_x + i * (bar_w + gap)
            norm = (acc - acc_min) / acc_range
            h = norm * bar_h_scale

            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1
            ).move_to([x, -1.5 + h / 2, 0])

            label = Text(state, font_size=14, color=INK).move_to([x, -1.5 - 0.3, 0])
            val = Text(f"{acc}%", font_size=13, color=col).move_to([x, -1.5 + h + 0.25, 0])

            self.play(GrowFromEdge(bar, DOWN), FadeIn(label), FadeIn(val), run_time=0.6)

        # Ceiling line at 88%
        ceil_norm = (88.0 - acc_min) / acc_range
        ceil_y = -1.5 + ceil_norm * bar_h_scale
        ceil_line = DashedLine(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=2, dash_length=0.12).shift(UP * ceil_y)
        ceil_text = Text("88% floor", font_size=13, color=SOFT).next_to(ceil_line, LEFT, buff=0.1)
        self.play(Create(ceil_line), FadeIn(ceil_text))

        ship = Text("SHIPS", font_size=28, color=ACC, weight=BOLD).shift(RIGHT * 2.5 + UP * 0.5)
        self.play(FadeIn(ship))
        self.wait(1.5)


class B05_HonestyBeat(Scene):
    def construct(self):
        self.camera.background_color = BG
        src = source_credit(self)
        self.add(src)

        title = Text("What Claude Can and Cannot Do", font_size=28, color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title))

        can_items = [
            "Generate the compression_journey.py script",
            "Compute compression ratios from parameters",
            "Print a four-state comparison table",
            "Check each state against ceilings",
        ]
        cannot_items = [
            "Train or fine-tune a neural network",
            "Measure real hardware latency",
            "Validate on a real defect-detection dataset",
        ]

        can_title = Text("Claude CAN:", font_size=18, color=GREEN).shift(LEFT * 3.0 + UP * 0.8)
        cannot_title = Text("Claude CANNOT:", font_size=18, color=ACC).shift(RIGHT * 0.8 + UP * 0.8)

        self.play(FadeIn(can_title), FadeIn(cannot_title))

        for i, item in enumerate(can_items):
            t = Text(f"+ {item}", font_size=13, color=INK).shift(LEFT * 3.0 + UP * (0.3 - i * 0.45))
            self.play(FadeIn(t), run_time=0.4)

        for i, item in enumerate(cannot_items):
            t = Text(f"- {item}", font_size=13, color=ACC).shift(RIGHT * 0.8 + UP * (0.3 - i * 0.45))
            self.play(FadeIn(t), run_time=0.4)

        note = Text("Figures are illustrative — real validation needs hardware + dataset", font_size=14, color=SOFT).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note))
        self.wait(1.5)
