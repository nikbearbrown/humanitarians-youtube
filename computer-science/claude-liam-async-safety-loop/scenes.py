"""scenes.py — Manim for claude-liam-async-safety-loop. Source: embedded-ai Ch. 10"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


class B01_ThreeTimelines(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Three Timelines vs 5 ms Deadline", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Deadline line
        deadline_x = 0.5  # relative position in our display
        deadline = DashedLine(
            start=[deadline_x * 6 - 3, 2.0, 0],
            end=[deadline_x * 6 - 3, -2.5, 0],
            color=INK, dash_length=0.2, stroke_width=1.5
        )
        deadline_lbl = Text("5 ms\ndeadline", font_size=13, color=INK)
        deadline_lbl.move_to([deadline_x * 6 - 3, 2.3, 0])
        self.play(Create(deadline), FadeIn(deadline_lbl))

        # Row labels
        row_ys = [1.2, 0.0, -1.2]
        row_names = ["Control loop\n(1 ms tick)", "Rule-based\ndetector", "AI inference"]
        row_colors = [SOFT, SOFT, ACC]

        for name, y, color in zip(row_names, row_ys, row_colors):
            lbl = Text(name, font_size=14, color=color)
            lbl.move_to([-5.0, y, 0])
            self.play(FadeIn(lbl), run_time=0.3)

        # Control loop: many 1ms ticks
        ticks = VGroup()
        for i in range(10):
            tick = Rectangle(width=0.12, height=0.45, fill_color=SOFT, fill_opacity=0.7, stroke_width=0)
            tick.move_to([-2.8 + i * 0.55, 1.2, 0])
            ticks.add(tick)
        self.play(FadeIn(ticks), run_time=0.5)

        # Rule-based: tiny bar, well inside deadline
        rule_bar = Rectangle(width=0.15, height=0.5, fill_color=SOFT, fill_opacity=0.85, stroke_width=0)
        rule_bar.move_to([-2.72, 0.0, 0])
        rule_lbl = Text("<1 ms", font_size=12, color=SOFT)
        rule_lbl.next_to(rule_bar, RIGHT, buff=0.1)
        self.play(GrowFromEdge(rule_bar, LEFT), FadeIn(rule_lbl))

        # AI inference: long bar (38 ms represented), overshooting deadline
        ai_bar = Rectangle(width=4.5, height=0.5, fill_color=ACC, fill_opacity=0.75, stroke_width=0)
        ai_bar.move_to([-0.55, -1.2, 0])
        ai_lbl = Text("38 ms", font_size=14, color=ACC, weight="BOLD")
        ai_lbl.next_to(ai_bar, RIGHT, buff=0.15)
        self.play(GrowFromEdge(ai_bar, LEFT), run_time=0.9)
        self.play(FadeIn(ai_lbl))

        overshoot = Text("7.6× past deadline", font_size=14, color=ACC)
        overshoot.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(overshoot))
        self.wait(1)


class B02_AsyncArch(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Async Advisory Architecture", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Control loop box
        ctrl = Rectangle(width=3.0, height=1.4, fill_color=SOFT, fill_opacity=0.15, stroke_color=SOFT, stroke_width=1.5)
        ctrl.move_to([-3.0, 0.5, 0])
        ctrl_lbl = Text("Control Loop\n1 kHz tick", font_size=16, color=INK)
        ctrl_lbl.move_to(ctrl.get_center())
        self.play(FadeIn(ctrl), FadeIn(ctrl_lbl))

        # Shared memory / probability field
        mem = Rectangle(width=2.0, height=0.9, fill_color=GHOST, fill_opacity=0.5, stroke_color=GHOST, stroke_width=1.5)
        mem.move_to([0.0, 0.5, 0])
        mem_lbl = Text("fault_prob\n= 0.3", font_size=15, color=INK)
        mem_lbl.move_to(mem.get_center())
        self.play(FadeIn(mem), FadeIn(mem_lbl))

        # AI thread box
        ai_box = Rectangle(width=3.0, height=1.4, fill_color=ACC, fill_opacity=0.12, stroke_color=ACC, stroke_width=1.5)
        ai_box.move_to([3.0, 0.5, 0])
        ai_lbl = Text("AI Thread\n38 ms async", font_size=16, color=ACC)
        ai_lbl.move_to(ai_box.get_center())
        self.play(FadeIn(ai_box), FadeIn(ai_lbl))

        # Read arrow (ctrl reads mem)
        read_arrow = Arrow(start=mem.get_left(), end=ctrl.get_right(), color=SOFT, stroke_width=2, buff=0.05)
        self.play(GrowArrow(read_arrow))
        read_lbl = Text("reads (non-blocking)", font_size=12, color=SOFT)
        read_lbl.move_to([-1.55, -0.3, 0])
        self.play(FadeIn(read_lbl))

        # Write arrow (AI writes mem)
        write_arrow = Arrow(start=ai_box.get_left(), end=mem.get_right(), color=ACC, stroke_width=2, buff=0.05)
        self.play(GrowArrow(write_arrow))
        write_lbl = Text("writes", font_size=13, color=ACC)
        write_lbl.move_to([1.55, 1.45, 0])
        self.play(FadeIn(write_lbl))

        # Rule-based detector
        rule = Rectangle(width=2.8, height=0.9, fill_color=SOFT, fill_opacity=0.2, stroke_color=SOFT, stroke_width=1.5)
        rule.move_to([-3.0, -1.2, 0])
        rule_lbl = Text("Deterministic trip wire\n<1 ms · always fires", font_size=14, color=INK)
        rule_lbl.move_to(rule.get_center())
        self.play(FadeIn(rule), FadeIn(rule_lbl))

        note = Text("AI is advisor. Guarantee never depends on AI timing.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B03_Verdict(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("What Each Guarantees", font_size=28, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        items = [
            ("Deterministic trip wire", "Hard deadline: always <1 ms", "Baseline detection rate", SOFT),
            ("AI advisory", "Improves detection rate", "No hard deadline guaranteed", ACC),
        ]

        y_pos = [0.8, -0.7]
        for (name, pro, con, color), y in zip(items, y_pos):
            box = Rectangle(width=8.5, height=1.5, fill_color=color, fill_opacity=0.1, stroke_color=color, stroke_width=1.5)
            box.move_to([0, y, 0])
            name_lbl = Text(name, font_size=16, color=color, weight="BOLD")
            name_lbl.move_to([-3.2, y + 0.25, 0])
            pro_lbl = Text(pro, font_size=13, color=INK)
            pro_lbl.move_to([1.0, y + 0.25, 0])
            con_lbl = Text(con, font_size=13, color=SOFT)
            con_lbl.move_to([1.0, y - 0.25, 0])
            self.play(FadeIn(box), FadeIn(name_lbl), FadeIn(pro_lbl), FadeIn(con_lbl), run_time=0.5)

        verdict = Text("Stack both: AI raises detection, trip wire holds the deadline.", font_size=15, color=SOFT)
        verdict.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(verdict))
        self.wait(1.2)
