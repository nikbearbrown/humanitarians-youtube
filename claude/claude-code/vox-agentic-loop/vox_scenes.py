"""vox_scenes.py — vox-agentic-loop
Why the Agentic Loop Can Delete Your Files Before You Finish Reading the Plan.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B04) gets no scene — compiles as slate.
"""
import sys
import pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403


class B01_Title(Scene):
    def construct(self):
        eyebrow = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                       color=INK, font_size=22, weight="MEDIUM")
        eyebrow.to_edge(UP, buff=0.7)
        t1 = Text("Why the agentic loop acts", font=SERIF, color=INK, font_size=42)
        t2 = Text("before you finish reading", font=SERIF, color=INK, font_size=42)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.2)
        title.scale_to_fit_width(12.0)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(6.4)


class B02_ChatbotVsAgent(Scene):
    def construct(self):
        # Two-column comparison
        left_bg = Rectangle(width=5.5, height=5.5)
        left_bg.set_fill(SLATE, 0.05).set_stroke(SLATE, 1.0)
        left_bg.to_edge(LEFT, buff=0.6)

        right_bg = Rectangle(width=5.5, height=5.5)
        right_bg.set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.0)
        right_bg.to_edge(RIGHT, buff=0.6)

        left_title = Text("Claude.ai", font=DISPLAY, color=INK,
                          font_size=24, weight="MEDIUM")
        left_title.next_to(left_bg, UP, buff=0.2)
        left_sub = SerifLabel("you review before action", accent=SLATE, size=20)
        left_sub.next_to(left_bg.get_top() + DOWN * 0.5, DOWN, buff=0.1)

        right_title = Text("Claude Code", font=DISPLAY, color=CRIMSON,
                           font_size=24, weight="MEDIUM")
        right_title.next_to(right_bg, UP, buff=0.2)
        right_sub = SerifLabel("loop runs before you read", accent=CRIMSON, size=20)
        right_sub.next_to(right_bg.get_top() + DOWN * 0.5, DOWN, buff=0.1)

        # Left: text -> review -> decide flow
        nodes_l = VGroup(
            Text("text", font=SERIF, color=INK, font_size=24),
            Text("review", font=SERIF, color=INK, font_size=24),
            Text("decide", font=SERIF, color=INK, font_size=24),
        )
        nodes_l.arrange(DOWN, buff=0.7)
        nodes_l.move_to(left_bg.get_center() + DOWN * 0.3)
        arr1 = Arrow(nodes_l[0].get_bottom(), nodes_l[1].get_top(),
                     stroke_width=2, color=INK, buff=0.05)
        arr2 = Arrow(nodes_l[1].get_bottom(), nodes_l[2].get_top(),
                     stroke_width=2, color=INK, buff=0.05)

        # Right: loop nodes
        loop_nodes = VGroup(
            Text("Gather", font=SERIF, color=INK, font_size=22),
            Text("Act", font=SERIF, color=CRIMSON, font_size=22, weight="BOLD"),
            Text("Verify", font=SERIF, color=INK, font_size=22),
        )
        loop_nodes.arrange(DOWN, buff=0.55)
        loop_nodes.move_to(right_bg.get_center() + DOWN * 0.3)
        ra1 = Arrow(loop_nodes[0].get_bottom(), loop_nodes[1].get_top(),
                    stroke_width=2, color=CRIMSON, buff=0.05)
        ra2 = Arrow(loop_nodes[1].get_bottom(), loop_nodes[2].get_top(),
                    stroke_width=2, color=CRIMSON, buff=0.05)

        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.5)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.4)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.1) for n in nodes_l],
                              lag_ratio=0.2, run_time=0.8))
        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.1) for n in loop_nodes],
                              lag_ratio=0.2, run_time=0.8))
        self.play(GrowArrow(ra1), GrowArrow(ra2), run_time=0.5)
        self.wait(6.6)


class B03_LoopCycle(Scene):
    def construct(self):
        # Animated three-node cycle
        radius = 1.6
        angles = [PI / 2, PI / 2 - 2 * PI / 3, PI / 2 + 2 * PI / 3]
        positions = [radius * np.array([np.cos(a), np.sin(a), 0]) for a in angles]
        labels = ["Gather", "Verify", "Act"]
        colors = [INK, INK, CRIMSON]

        nodes = VGroup()
        texts = VGroup()
        for pos, label, col in zip(positions, labels, colors):
            circle = Circle(radius=0.5).set_fill(GROUND, 1).set_stroke(col, 2.5)
            circle.move_to(pos)
            t = Text(label, font=SERIF, color=col, font_size=22)
            t.move_to(pos)
            nodes.add(circle)
            texts.add(t)

        # Arrows between nodes
        arrows = VGroup()
        for i in range(3):
            j = (i + 1) % 3
            start = positions[i] + 0.55 * (positions[j] - positions[i]) / np.linalg.norm(positions[j] - positions[i])
            end = positions[j] - 0.55 * (positions[j] - positions[i]) / np.linalg.norm(positions[j] - positions[i])
            arr = Arrow(start, end, stroke_width=2.5, color=SLATE, buff=0.0)
            arrows.add(arr)

        # Act node blink effect: file icon label
        file_label = LabelChip("file edited", accent=CRIMSON, size=18)
        file_label.next_to(texts[2], RIGHT, buff=0.4)

        title = Text("the agentic loop", font=SERIF, color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.15, run_time=0.7))
        self.play(LaggedStart(*[FadeIn(t) for t in texts], lag_ratio=0.15, run_time=0.6))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2, run_time=0.8))
        # Loop animation: cycle through arrows
        self.play(arrows[0].animate.set_color(CRIMSON), run_time=0.4)
        self.play(arrows[1].animate.set_color(CRIMSON), run_time=0.4)
        self.play(FadeIn(file_label), run_time=0.3)
        self.play(arrows[2].animate.set_color(CRIMSON), run_time=0.4)
        self.wait(6.4)


class B05_Question(Scene):
    def construct(self):
        line1 = Text("Files changed while the explanation", font=SERIF,
                     color=INK, font_size=36)
        line2 = Text("was still scrolling. Why?", font=SERIF,
                     color=INK, font_size=36)
        question = VGroup(line1, line2).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(11.5)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.15,
                    question.get_corner(DR) + DOWN * 0.15,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(question), run_time=1.0)
        self.play(Create(rule), run_time=0.7)
        self.wait(7.3)


class B06_LoopAndOutput(Scene):
    def construct(self):
        # Loop on left, terminal buffer on right, async
        loop_label = Text("agentic loop", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        loop_label.move_to(LEFT * 3.8 + UP * 2.8)

        term_label = Text("your terminal", font=DISPLAY, color=INK,
                          font_size=22, weight="MEDIUM")
        term_label.move_to(RIGHT * 3.0 + UP * 2.8)

        # Loop nodes (small)
        radius = 1.0
        angles_loop = [PI / 2, PI / 2 - 2 * PI / 3, PI / 2 + 2 * PI / 3]
        positions_loop = [LEFT * 3.8 + radius * np.array([np.cos(a), np.sin(a), 0])
                          for a in angles_loop]
        node_labels = ["G", "V", "A"]
        node_cols = [INK, INK, CRIMSON]
        loop_nodes = VGroup()
        for pos, label, col in zip(positions_loop, node_labels, node_cols):
            c = Circle(radius=0.35).set_fill(GROUND, 1).set_stroke(col, 2)
            c.move_to(pos)
            t = Text(label, font=SERIF, color=col, font_size=18)
            t.move_to(pos)
            loop_nodes.add(VGroup(c, t))

        # File change icons appearing
        file_icons = VGroup()
        for i, pos in enumerate(positions_loop):
            icon = LabelChip(f"file {i+1}", accent=CRIMSON, size=14)
            icon.next_to(loop_nodes[i], RIGHT, buff=0.2)
            file_icons.add(icon)

        # Terminal buffer (right side, filling with lines)
        term_bg = Rectangle(width=4.5, height=5.0)
        term_bg.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.0)
        term_bg.move_to(RIGHT * 3.2)

        term_lines = VGroup()
        for i, text in enumerate(["Gathering context...",
                                   "Reading index.html",
                                   "Writing contact.html",
                                   "Modifying nav...",
                                   "Installing..."]):
            col = CRIMSON if i >= 2 else INK
            t = Text(text, font=MONO, color=col, font_size=18)
            t.move_to(term_bg.get_top() + DOWN * (0.55 + i * 0.7))
            t.align_to(term_bg.get_left() + RIGHT * 0.2, LEFT)
            term_lines.add(t)

        async_label = SerifLabel("explanation and actions share the same loop",
                                 accent=SLATE, size=20)
        async_label.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(loop_label), FadeIn(term_label), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n) for n in loop_nodes],
                              lag_ratio=0.15, run_time=0.6))
        self.play(FadeIn(term_bg), run_time=0.3)
        # Interleave loop action with terminal lines appearing
        for i in range(3):
            self.play(FadeIn(file_icons[i]), FadeIn(term_lines[i]), run_time=0.4)
        self.play(FadeIn(term_lines[3]), FadeIn(term_lines[4]), run_time=0.6)
        self.play(FadeIn(async_label), run_time=0.5)
        self.wait(7.1)


class B07_PlanModeGate(Scene):
    def construct(self):
        # Three-node loop with teal gate between Gather and Act
        radius = 1.5
        angles = [PI / 2, PI / 2 - 2 * PI / 3, PI / 2 + 2 * PI / 3]
        positions = [radius * np.array([np.cos(a), np.sin(a), 0]) for a in angles]
        node_labels = ["Gather", "Verify", "Act"]
        node_cols = [INK, INK, SLATE]  # Act grayed out (not yet approved)

        nodes = VGroup()
        texts = VGroup()
        for pos, label, col in zip(positions, node_labels, node_cols):
            c = Circle(radius=0.55).set_fill(GROUND, 1).set_stroke(col, 2.5)
            c.move_to(pos)
            t = Text(label, font=SERIF, color=col, font_size=22)
            t.move_to(pos)
            nodes.add(c)
            texts.add(t)

        # Arrow from Gather to Act (blocked by gate)
        mid_gather_act = (positions[0] + positions[2]) / 2
        gate = Rectangle(width=1.6, height=0.7)
        gate.set_fill(TEAL, 0.8).set_stroke(TEAL, 2.0)
        gate.move_to(mid_gather_act)
        gate_text = Text("PLAN MODE", font=DISPLAY, color=INK,
                         font_size=16, weight="MEDIUM")
        gate_text.move_to(gate)

        title = Text("plan mode: the interruption point", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        approved_chip = LabelChip("APPROVED", accent=TEAL, size=18)
        approved_chip.next_to(gate, RIGHT, buff=0.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.15, run_time=0.6))
        self.play(LaggedStart(*[FadeIn(t) for t in texts], lag_ratio=0.15, run_time=0.6))
        self.play(FadeIn(gate), FadeIn(gate_text), run_time=0.7)
        self.play(FadeIn(approved_chip), run_time=0.5)
        # Now Act becomes active
        self.play(texts[2].animate.set_color(TEAL),
                  nodes[2].animate.set_stroke(TEAL, 2.5), run_time=0.7)
        self.wait(7.5)


class B08_PlanReview(Scene):
    def construct(self):
        title = Text("plan on screen before execution", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Plan card with three steps
        card = Rectangle(width=8.0, height=4.5)
        card.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.2)
        card.move_to(ORIGIN + DOWN * 0.2)

        plan_header = Text("Proposed plan:", font=DISPLAY, color=INK,
                           font_size=22, weight="MEDIUM")
        plan_header.move_to(card.get_top() + DOWN * 0.5).align_to(card.get_left() + RIGHT * 0.5, LEFT)

        steps = [
            ("1. create contact.html", INK),
            ("2. add nav entry in index.html", INK),
            ("3. install form library (npm)", CRIMSON),
        ]
        step_texts = VGroup()
        for text, col in steps:
            t = Text(text, font=SERIF, color=col, font_size=24)
            step_texts.add(t)
        step_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step_texts.next_to(plan_header, DOWN, buff=0.35)
        step_texts.align_to(plan_header, LEFT)

        # Strike through step 3
        strike = Line(step_texts[2].get_left() + LEFT * 0.1,
                      step_texts[2].get_right() + RIGHT * 0.1,
                      stroke_width=2.5, color=TEAL)

        approved = LabelChip("APPROVED", accent=TEAL, size=20)
        approved.next_to(card, DOWN, buff=0.35)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(card), FadeIn(plan_header), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(t) for t in step_texts],
                              lag_ratio=0.2, run_time=0.8))
        self.play(Create(strike), run_time=0.5)
        self.play(FadeIn(approved), run_time=0.4)
        self.wait(7.3)


class B09_TwoOutcomes(Scene):
    def construct(self):
        # Two paths: plan mode vs. no plan mode
        left_bg = Rectangle(width=5.5, height=5.2)
        left_bg.set_fill(TEAL, 0.05).set_stroke(TEAL, 1.2)
        left_bg.to_edge(LEFT, buff=0.6)

        right_bg = Rectangle(width=5.5, height=5.2)
        right_bg.set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.2)
        right_bg.to_edge(RIGHT, buff=0.6)

        left_t = Text("with plan mode", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        left_t.next_to(left_bg, UP, buff=0.2)
        right_t = Text("without plan mode", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight="MEDIUM")
        right_t.next_to(right_bg, UP, buff=0.2)

        left_items = VGroup(
            Text("contact.html created", font=SERIF, color=INK, font_size=20),
            Text("nav updated", font=SERIF, color=INK, font_size=20),
            Text("existing styles used", font=SERIF, color=TEAL, font_size=20),
        )
        left_items.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        left_items.move_to(left_bg.get_center())

        right_items = VGroup(
            Text("contact.html created", font=SERIF, color=INK, font_size=20),
            Text("nav updated", font=SERIF, color=INK, font_size=20),
            Text("form library installed", font=SERIF, color=CRIMSON, font_size=20),
        )
        right_items.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        right_items.move_to(right_bg.get_center())

        surprise = SerifLabel("school server blocks it", accent=CRIMSON, size=18)
        surprise.next_to(right_items[2], DOWN, buff=0.25)

        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.5)
        self.play(FadeIn(left_t), FadeIn(right_t), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(it) for it in left_items],
                              lag_ratio=0.15, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(it) for it in right_items],
                              lag_ratio=0.15, run_time=0.8))
        self.play(FadeIn(surprise), run_time=0.5)
        self.wait(7.5)


class B10_HeuristicCard(Scene):
    def construct(self):
        title = Text("when to use plan mode", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Two-row table
        rows_data = [
            ("first session on any project", TEAL),
            ("any operation costly to undo", TEAL),
        ]
        rows = VGroup()
        for text, col in rows_data:
            row_bg = Rectangle(width=9.0, height=1.2)
            row_bg.set_fill(col, 0.07).set_stroke(col, 1.2)
            row_text = Text(text, font=SERIF, color=INK, font_size=28)
            row_text.move_to(row_bg.get_center() + LEFT * 0.5)
            chip = LabelChip("plan mode", accent=col, size=18)
            chip.next_to(row_bg.get_right() + LEFT * 1.2, ORIGIN)
            rows.add(VGroup(row_bg, row_text, chip))

        rows.arrange(DOWN, buff=0.45)
        rows.move_to(ORIGIN + DOWN * 0.3)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.7)
        self.wait(8.1)


class B11_SupervisionDial(Scene):
    def construct(self):
        import numpy as np
        title = Text("plan mode: supervision dial, not overhead", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Dial
        arc = Arc(radius=1.8, start_angle=PI * 0.15, angle=PI * 0.7,
                  stroke_width=14, color=SLATE)
        arc.move_to(ORIGIN + DOWN * 0.3)

        plan_on_label = Text("plan mode on", font=SERIF, color=TEAL, font_size=24)
        plan_on_label.next_to(arc, LEFT, buff=0.3).shift(UP * 0.5)
        plan_off_label = Text("plan mode off", font=SERIF, color=INK, font_size=24)
        plan_off_label.next_to(arc, RIGHT, buff=0.3).shift(UP * 0.5)

        center = arc.get_center()
        start_ang = PI * 0.72
        needle = Line(center, center + 1.6 * np.array([np.cos(start_ang), np.sin(start_ang), 0]),
                      stroke_width=5, color=TEAL)

        cap_label = SerifLabel("same loop capability, different interruption", accent=SLATE, size=22)
        cap_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(arc), run_time=0.6)
        self.play(FadeIn(plan_on_label), FadeIn(plan_off_label), run_time=0.5)
        self.play(Create(needle), run_time=0.6)
        # Move needle from plan-on to plan-off to illustrate it's a choice
        end_ang = PI * 0.28
        needle_end = center + 1.6 * np.array([np.cos(end_ang), np.sin(end_ang), 0])
        self.play(needle.animate.put_start_and_end_on(center, needle_end),
                  run_time=1.5)
        self.play(needle.animate.set_color(INK), run_time=0.3)
        self.play(FadeIn(cap_label), run_time=0.5)
        self.wait(7.0)


class B12_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("The loop acts.", font=SERIF, color=CRIMSON, font_size=46)
        m2 = Text("Plan mode lets you read first.", font=SERIF, color=TEAL, font_size=46)
        main_text = VGroup(m1, m2).arrange(DOWN, center=True, buff=0.35)
        main_text.scale_to_fit_width(12.0)
        main_text.move_to(ORIGIN + UP * 0.2)

        rule = Line(main_text.get_corner(DL) + DOWN * 0.15,
                    main_text.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=TEAL)

        handle = Text("@nikbearbrown", font=SERIF, color=CRIMSON, font_size=24)
        handle.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(main_text), Create(rule), run_time=1.0)
        self.play(FadeIn(handle), run_time=0.5)
        self.wait(8.0)
