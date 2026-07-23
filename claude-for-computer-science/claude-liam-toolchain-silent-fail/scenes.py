"""scenes.py — Manim for claude-liam-toolchain-silent-fail. Source: embedded-ai Ch. 13"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")
GREEN = ManimColor("#5B8A5F")


class B01_GreenPipeline(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Six Gates — All Green", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        stages = [
            "Source\nmodel",
            "ONNX\nexport",
            "TFLite\nfloat",
            "int8\ncalib",
            "Device\ncompile",
            "Deploy",
        ]

        n = len(stages)
        x_step = 1.9
        x_start = -(n - 1) * x_step / 2
        y_box = 0.3

        boxes = []
        for i, stage in enumerate(stages):
            x = x_start + i * x_step
            box = Rectangle(width=1.5, height=1.1, fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN, stroke_width=2)
            box.move_to([x, y_box, 0])
            lbl = Text(stage, font_size=13, color=INK)
            lbl.move_to(box.get_center())
            check = Text("OK", font_size=14, color=GREEN, weight="BOLD")
            check.next_to(box, DOWN, buff=0.15)
            boxes.append((box, lbl, check))

        for box, lbl, check in boxes:
            self.play(FadeIn(box), FadeIn(lbl), run_time=0.3)
            self.play(FadeIn(check), run_time=0.2)

        # Arrows between boxes
        for i in range(n - 1):
            x1 = x_start + i * x_step + 0.75
            x2 = x_start + (i + 1) * x_step - 0.75
            arr = Arrow(start=[x1, y_box, 0], end=[x2, y_box, 0], color=GHOST, stroke_width=1.5, buff=0.0)
            self.play(GrowArrow(arr), run_time=0.2)

        note = Text("Every gate: SUCCESS. No error codes. No warnings.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.7)
        sub = Text("Green = conversion completed. Not: result is correct.", font_size=14, color=GHOST)
        sub.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note), FadeIn(sub))
        self.wait(1.2)


class B02_AccuracyTrace(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Accuracy Traces Downward", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        stages = ["Source", "ONNX", "TFLite\nfloat", "int8", "Device"]
        accuracies = [91.5, 91.0, 91.0, 89.8, 72.0]
        n = len(stages)
        x_step = 2.0
        x_start = -(n - 1) * x_step / 2
        y_base = -2.0
        max_h = 3.5
        max_acc = 95.0

        # Draw stage labels
        for i, stage in enumerate(stages):
            x = x_start + i * x_step
            lbl = Text(stage, font_size=14, color=INK)
            lbl.move_to([x, y_base - 0.35, 0])
            self.play(FadeIn(lbl), run_time=0.2)

        # Accuracy bars
        bars = VGroup()
        acc_lbls = VGroup()
        for i, (stage, acc) in enumerate(zip(stages, accuracies)):
            x = x_start + i * x_step
            h = (acc / max_acc) * max_h
            color = ACC if i == 4 else SOFT
            bar = Rectangle(width=1.5, height=h, fill_color=color, fill_opacity=0.75, stroke_width=0)
            bar.move_to([x, y_base + h / 2, 0])
            bars.add(bar)

            acc_lbl = Text(f"{acc}%", font_size=15, color=color if i == 4 else INK)
            acc_lbl.next_to(bar, UP, buff=0.1)
            acc_lbls.add(acc_lbl)

        for b, lbl in zip(bars, acc_lbls):
            self.play(GrowFromEdge(b, DOWN), FadeIn(lbl), run_time=0.35)

        # Trace line
        trace_pts = [
            [x_start + i * x_step, y_base + (acc / max_acc) * max_h, 0]
            for i, acc in enumerate(accuracies)
        ]
        trace = VMobject()
        trace.set_points_as_corners(trace_pts)
        trace.set_stroke(color=ACC, width=2.5)
        self.play(Create(trace), run_time=0.7)

        crash_lbl = Text("-19.8 pts in one step", font_size=15, color=ACC, weight="BOLD")
        crash_lbl.move_to([x_start + 4 * x_step + 0.5, y_base + (72 / max_acc) * max_h + 0.8, 0])
        self.play(FadeIn(crash_lbl))

        note = Text("Toolchain bug: unsupported op fusion produced wrong outputs.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B03_Bisection(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Bisect to Find the Drop", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title))

        stages = ["Source", "ONNX", "TFLite\nfloat", "int8", "Device"]
        accuracies = [91.5, 91.0, 91.0, 89.8, 72.0]
        n = len(stages)
        x_step = 2.0
        x_start = -(n - 1) * x_step / 2
        y_base = -1.8
        max_h = 3.0
        max_acc = 95.0

        # Stage labels and bars
        for i, (stage, acc) in enumerate(zip(stages, accuracies)):
            x = x_start + i * x_step
            lbl = Text(stage, font_size=14, color=INK)
            lbl.move_to([x, y_base - 0.35, 0])
            h = (acc / max_acc) * max_h
            color = ACC if i == 4 else SOFT
            bar = Rectangle(width=1.4, height=h, fill_color=color, fill_opacity=0.6, stroke_width=0)
            bar.move_to([x, y_base + h / 2, 0])
            self.play(FadeIn(lbl), GrowFromEdge(bar, DOWN), run_time=0.25)

        # Bracket closing in on the drop between int8 and device
        x_int8 = x_start + 3 * x_step
        x_device = x_start + 4 * x_step

        bracket_top = 1.8
        bracket_bottom = -1.8

        left_brace = Line(
            start=[x_int8 - 0.05, bracket_top, 0],
            end=[x_int8 - 0.05, bracket_bottom, 0],
            color=ACC, stroke_width=3
        )
        right_brace = Line(
            start=[x_device + 0.05, bracket_top, 0],
            end=[x_device + 0.05, bracket_bottom, 0],
            color=ACC, stroke_width=3
        )
        bracket_lbl = Text("drop here", font_size=16, color=ACC, weight="BOLD")
        bracket_lbl.move_to([(x_int8 + x_device) / 2, bracket_top + 0.35, 0])

        self.play(Create(left_brace), Create(right_brace), run_time=0.6)
        self.play(FadeIn(bracket_lbl))

        cause = Text("Cause: unsupported GELU fusion at int8 compilation", font_size=13, color=ACC)
        cause.move_to([0, -2.8, 0])
        fix = Text("Fix: disable fusion or replace with supported op.", font_size=13, color=SOFT)
        fix.move_to([0, -3.1, 0])
        self.play(FadeIn(cause), FadeIn(fix))
        self.wait(1.2)
