"""cognitive-friction-loop — vox_scenes.py
Why Students Who Practice With AI Score Lower on the Exam
"""
from vox_graphics import *
import numpy as np


class B03_TwoCurves(Scene):
    """THE PROBLEM — two learning curves: AI-assisted collapses at exam."""
    def construct(self):
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 100, 25],
            x_length=9.5,
            y_length=5.0,
            axis_config={"color": INK, "stroke_width": 2.0, "include_tip": False},
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        )
        axes.move_to(ORIGIN + DOWN * 0.3)

        # X-axis labels
        x_labels = VGroup(
            Text("WEEK 1", font=DISPLAY, color=INK, font_size=16, weight="MEDIUM"),
            Text("WEEK 2", font=DISPLAY, color=INK, font_size=16, weight="MEDIUM"),
            Text("WEEK 3", font=DISPLAY, color=INK, font_size=16, weight="MEDIUM"),
            Text("EXAM", font=DISPLAY, color=CRIMSON, font_size=18, weight="BOLD"),
        )
        for i, lbl in enumerate(x_labels):
            lbl.move_to(axes.c2p(i + 1, -10))

        y_label = Text("Score", font=SERIF, color=INK, font_size=19)
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.3)

        # CRIMSON curve: shoots up, collapses at exam (x=4)
        crimson_points = [
            axes.c2p(1, 35),
            axes.c2p(2, 60),
            axes.c2p(3, 83),
            axes.c2p(4, 51),
        ]
        crimson_curve = VMobject(color=CRIMSON, stroke_width=3.5)
        crimson_curve.set_points_as_corners(crimson_points)
        crimson_curve.make_smooth()

        # TEAL curve: modest climb, holds at exam
        teal_points = [
            axes.c2p(1, 32),
            axes.c2p(2, 46),
            axes.c2p(3, 58),
            axes.c2p(4, 64),
        ]
        teal_curve = VMobject(color=TEAL, stroke_width=3.5)
        teal_curve.set_points_as_corners(teal_points)
        teal_curve.make_smooth()

        # Labels for curves
        crimson_lbl = Text("AI-assisted practice", font=SERIF, color=CRIMSON, font_size=19)
        crimson_lbl.move_to(axes.c2p(2.5, 92))

        teal_lbl = Text("No-AI practice", font=SERIF, color=TEAL, font_size=19)
        teal_lbl.move_to(axes.c2p(2.5, 74))

        # Collapse arrow label
        collapse_lbl = Text("17pp lower", font=DISPLAY, color=CRIMSON,
                            font_size=18, weight="MEDIUM")
        collapse_lbl.move_to(axes.c2p(4.35, 57))
        collapse_arr = Arrow(
            axes.c2p(4, 62),
            axes.c2p(4, 52),
            buff=0.05, color=CRIMSON, stroke_width=2,
        )

        self.play(Create(axes), FadeIn(x_labels), FadeIn(y_label), run_time=0.7)
        self.play(Create(teal_curve), FadeIn(teal_lbl), run_time=1.2)
        self.play(Create(crimson_curve), FadeIn(crimson_lbl), run_time=1.5)
        self.play(GrowArrow(collapse_arr), FadeIn(collapse_lbl), run_time=0.8)
        self.wait(9.8)


class B04_FrictionChain(Scene):
    """THE MECHANISM — two chains: genuine learning vs. AI-removed friction."""
    def construct(self):
        # Top chain (TEAL): genuine learning
        top_labels = ["STRUGGLE", "PREDICTION\nERROR", "DOPAMINE", "SYNAPSE\nSTRENGTH", "MEMORY"]
        top_chain_parts = []
        top_blocks = VGroup()
        for lbl in top_labels:
            box = Rectangle(width=2.0, height=0.85)
            box.set_fill(TEAL, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=14, weight="MEDIUM",
                       line_spacing=1.15)
            if txt.width > 1.8:
                txt.scale_to_fit_width(1.8)
            txt.move_to(box)
            top_blocks.add(VGroup(box, txt))

        for i, blk in enumerate(top_blocks):
            top_chain_parts.append(blk)
            if i < len(top_blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.35, buff=0, color=TEAL, stroke_width=2)
                top_chain_parts.append(arr)

        top_chain = VGroup(*top_chain_parts)
        top_chain.arrange(RIGHT, buff=0.15)
        top_chain.move_to(UP * 0.9)

        top_header = Text("WITH cognitive friction", font=DISPLAY, color=TEAL,
                          font_size=17, weight="MEDIUM")
        top_header.next_to(top_chain, UP, buff=0.25)

        # Bottom chain (CRIMSON): AI removes struggle
        bot_labels = ["AI REMOVES\nSTRUGGLE", "NO\nTRIGGER", "NO\nCONSOLIDATION"]
        bot_blocks = VGroup()
        bot_chain_parts = []
        for lbl in bot_labels:
            box = Rectangle(width=2.3, height=0.85)
            box.set_fill(CRIMSON, 1).set_stroke(width=0)
            txt = Text(lbl, font=DISPLAY, color=WHITE, font_size=14, weight="MEDIUM",
                       line_spacing=1.15)
            if txt.width > 2.1:
                txt.scale_to_fit_width(2.1)
            txt.move_to(box)
            bot_blocks.add(VGroup(box, txt))

        for i, blk in enumerate(bot_blocks):
            bot_chain_parts.append(blk)
            if i < len(bot_blocks) - 1:
                arr = Arrow(ORIGIN, RIGHT * 0.35, buff=0, color=CRIMSON, stroke_width=2)
                bot_chain_parts.append(arr)

        bot_chain = VGroup(*bot_chain_parts)
        bot_chain.arrange(RIGHT, buff=0.15)
        bot_chain.move_to(DOWN * 1.0)

        bot_header = Text("WITHOUT cognitive friction", font=DISPLAY, color=CRIMSON,
                          font_size=17, weight="MEDIUM")
        bot_header.next_to(bot_chain, UP, buff=0.25)

        # Divider line
        divider = Line(LEFT * 5.5, RIGHT * 5.5, color=SLATE, stroke_width=0.8, stroke_opacity=0.4)
        divider.move_to(ORIGIN)

        self.play(FadeIn(top_header), run_time=0.4)
        for part in top_chain_parts:
            if isinstance(part, Arrow):
                self.play(GrowArrow(part), run_time=0.3)
            else:
                self.play(FadeIn(part, scale=0.9), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(bot_header), run_time=0.4)
        for part in bot_chain_parts:
            if isinstance(part, Arrow):
                self.play(GrowArrow(part), run_time=0.3)
            else:
                self.play(FadeIn(part, scale=0.9), run_time=0.4)
        self.wait(5.5)


class B06_PhaseGate(Scene):
    """THE PRACTICE — phase gate: AI side vs. student side."""
    def construct(self):
        # Full bar background
        bar = Rectangle(width=11.5, height=3.2)
        bar.set_fill(GROUND, 1).set_stroke(INK, 1.5)
        bar.move_to(UP * 0.3)

        # Gate line in center
        gate_line = Line(
            bar.get_top() + DOWN * 0.01,
            bar.get_bottom() + UP * 0.01,
            color=INK, stroke_width=2.5,
        )
        gate_line.move_to(bar.get_center())

        # Left side: AI HANDLES (lighter TEAL fill)
        left_fill = Rectangle(width=5.6, height=3.2)
        left_fill.set_fill(TEAL, 0.12).set_stroke(width=0)
        left_fill.move_to(bar.get_center() + LEFT * 2.95)

        ai_header = Text("AI HANDLES", font=DISPLAY, color=TEAL, font_size=20, weight="BOLD")
        ai_header.move_to(bar.get_center() + LEFT * 2.95 + UP * 0.85)

        ai_items = Text(
            "scaffolding · sources · feedback",
            font=SERIF, color=INK, font_size=21, line_spacing=1.3,
        )
        ai_items.move_to(bar.get_center() + LEFT * 2.95 + DOWN * 0.1)

        # Right side: STUDENT HANDLES (deeper TEAL fill)
        right_fill = Rectangle(width=5.6, height=3.2)
        right_fill.set_fill(TEAL, 0.22).set_stroke(width=0)
        right_fill.move_to(bar.get_center() + RIGHT * 2.95)

        student_header = Text("STUDENT HANDLES", font=DISPLAY, color=TEAL,
                              font_size=20, weight="BOLD")
        student_header.move_to(bar.get_center() + RIGHT * 2.95 + UP * 0.85)

        student_items = Text(
            "synthesis · argument · explanation",
            font=SERIF, color=INK, font_size=21, line_spacing=1.3,
        )
        student_items.move_to(bar.get_center() + RIGHT * 2.95 + DOWN * 0.1)

        # Gate label below bar
        gate_lbl = SerifLabel("struggle is here", accent=TEAL, size=22)
        gate_lbl.next_to(bar, DOWN, buff=0.4)

        self.play(FadeIn(bar), FadeIn(left_fill), FadeIn(right_fill), run_time=0.5)
        self.play(Create(gate_line), run_time=0.5)
        self.play(
            FadeIn(ai_header, shift=RIGHT * 0.1),
            FadeIn(student_header, shift=LEFT * 0.1),
            run_time=0.7,
        )
        self.play(
            FadeIn(ai_items, shift=UP * 0.1),
            FadeIn(student_items, shift=UP * 0.1),
            run_time=0.7,
        )
        self.play(
            Write(gate_lbl[0]),
            Create(gate_lbl[1]),
            run_time=0.7,
        )
        self.wait(7.6)
