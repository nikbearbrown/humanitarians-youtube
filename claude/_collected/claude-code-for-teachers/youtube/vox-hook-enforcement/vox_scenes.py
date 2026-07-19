"""vox_scenes.py — vox-hook-enforcement
Why 'Never Generate a Grade' fails until you write a Hook.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beats (B09) get no scene — they compile as slates.
"""
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403


class B01_Title(Scene):
    def construct(self):
        eyebrow = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                       color=INK, font_size=22, weight="MEDIUM")
        eyebrow.to_edge(UP, buff=0.7)
        title = Text("Why a CLAUDE.md rule\nfails until you write a Hook",
                     font=SERIF, color=INK, font_size=40,
                     line_spacing=0.85)
        title.scale_to_fit_width(11.0)
        title.move_to(ORIGIN + UP * 0.3)
        rule = Line(title.get_corner(DL) + DOWN * 0.18,
                    title.get_corner(DR) + DOWN * 0.18,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(6.4)


class B02_ClaudeMdRule(Scene):
    def construct(self):
        # Document card showing the NEVER rule
        card_bg = Rectangle(width=8.0, height=3.6)
        card_bg.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        filename = Text("CLAUDE.md", font=DISPLAY, color=INK,
                        font_size=22, weight="MEDIUM")
        filename.move_to(card_bg.get_top() + DOWN * 0.45)
        never_heading = Text("NEVER", font=DISPLAY, color=CRIMSON,
                             font_size=28, weight="MEDIUM")
        rule_text = Text("Never generate a final grade.\nThe teacher assigns grades.",
                         font=SERIF, color=INK, font_size=28,
                         line_spacing=0.85)
        rule_group = VGroup(never_heading, rule_text)
        rule_group.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        rule_group.move_to(card_bg.get_center() + DOWN * 0.1)
        advisory_label = SerifLabel("advisory", accent=SLATE, size=26)
        advisory_label.next_to(card_bg, DOWN, buff=0.35)

        card_group = VGroup(card_bg, filename)
        self.play(FadeIn(card_group, shift=UP * 0.2), run_time=0.7)
        self.play(FadeIn(never_heading), run_time=0.4)
        self.play(FadeIn(rule_text), run_time=0.6)
        self.play(FadeIn(advisory_label, shift=UP * 0.1), run_time=0.5)
        self.wait(7.8)


class B03_ProbabilityDial(Scene):
    def construct(self):
        import numpy as np
        # Simple dial mechanic: arc + needle
        # Dial background
        arc = Arc(radius=2.0, start_angle=PI * 0.2, angle=PI * 0.6,
                  stroke_width=12, color=SLATE)
        arc.move_to(ORIGIN + UP * 0.3)

        # High probability zone label
        high_label = Text("follows rule", font=SERIF, color=INK, font_size=24)
        high_label.next_to(arc, LEFT, buff=0.3).shift(UP * 0.5)
        low_label = Text("ignores rule", font=SERIF, color=CRIMSON, font_size=24)
        low_label.next_to(arc, RIGHT, buff=0.3).shift(UP * 0.5)

        # Needle starts high (rule followed), drifts right
        center = arc.get_center()
        # Start angle: nearly at 'follows' end
        start_ang = PI * 0.65
        end_ang = PI * 0.38
        needle_start = center + 1.8 * np.array([np.cos(start_ang), np.sin(start_ang), 0])
        needle_end = center + 1.8 * np.array([np.cos(end_ang), np.sin(end_ang), 0])
        needle = Line(center, needle_start, stroke_width=5, color=CRIMSON)

        session_label = Text("session 1", font=MONO, color=INK, font_size=22)
        session_label.to_edge(DOWN, buff=1.2)
        session3_label = Text("session 3: immediate prompt pulls harder",
                              font=MONO, color=CRIMSON, font_size=22)
        session3_label.to_edge(DOWN, buff=0.5)

        self.play(Create(arc), run_time=0.6)
        self.play(FadeIn(high_label), FadeIn(low_label), run_time=0.5)
        self.play(Create(needle), FadeIn(session_label), run_time=0.7)
        # Drift the needle toward low probability
        self.play(needle.animate.put_start_and_end_on(center, needle_end),
                  run_time=2.5)
        self.play(FadeOut(session_label), FadeIn(session3_label), run_time=0.5)
        self.wait(5.2)


class B04_GradeWritten(Scene):
    def construct(self):
        # File card with grade appearing in crimson
        never_chip = LabelChip("NEVER rule", accent=SLATE, size=22)
        never_chip.to_edge(UP, buff=1.0).shift(LEFT * 2.0)
        never_chip_x = Text("overridden", font=SERIF, color=CRIMSON,
                            font_size=20, slant=ITALIC)
        never_chip_x.next_to(never_chip, RIGHT, buff=0.3)

        file_card = Rectangle(width=7.5, height=4.0)
        file_card.set_fill(WHITE, 0.07).set_stroke(SLATE, 1.2)
        file_card.move_to(ORIGIN + DOWN * 0.2)
        filename = Text("student-07.md", font=MONO, color=INK, font_size=22)
        filename.move_to(file_card.get_top() + DOWN * 0.4)

        content_lines = Text(
            "Thesis: present, focused\nEvidence: strong (3 sources)\nMechanics: minor issues",
            font=SERIF, color=INK, font_size=24, line_spacing=0.9)
        content_lines.move_to(file_card.get_center() + UP * 0.5)

        grade_line = Text("Overall performance: B+", font=SERIF,
                          color=CRIMSON, font_size=28, weight="BOLD")
        grade_line.next_to(content_lines, DOWN, buff=0.45)

        self.play(FadeIn(never_chip), run_time=0.5)
        self.play(FadeIn(file_card), FadeIn(filename), run_time=0.6)
        self.play(FadeIn(content_lines), run_time=0.7)
        self.play(FadeIn(never_chip_x), run_time=0.4)
        self.play(FadeIn(grade_line, shift=UP * 0.1), run_time=0.8)
        self.wait(6.0)


class B05_Question(Scene):
    def construct(self):
        line1 = Text("A CLAUDE.md rule said NEVER.", font=SERIF, color=INK, font_size=36)
        line2 = Text("The grade appeared anyway. Why?", font=SERIF, color=INK, font_size=36)
        question_text = VGroup(line1, line2).arrange(DOWN, center=True, buff=0.3)
        question_text.scale_to_fit_width(11.0)
        question_text.move_to(ORIGIN)
        rule = Line(question_text.get_corner(DL) + DOWN * 0.18,
                    question_text.get_corner(DR) + DOWN * 0.18,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(question_text), run_time=1.0)
        self.play(Create(rule), run_time=0.7)
        self.wait(7.3)


class B06_AdvisoryPath(Scene):
    def construct(self):
        # Vertical lane with probability meter degrading as tokens accumulate
        lane_bg = Rectangle(width=5.0, height=6.0)
        lane_bg.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.0)
        lane_bg.to_edge(LEFT, buff=1.2)

        lane_title = Text("CLAUDE.md advisory path", font=DISPLAY,
                          color=INK, font_size=22, weight="MEDIUM")
        lane_title.next_to(lane_bg, UP, buff=0.3)

        # Probability meter (simple vertical bar)
        meter_bg = Rectangle(width=0.6, height=3.8)
        meter_bg.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.0)
        meter_bg.move_to(lane_bg.get_center() + RIGHT * 1.6)
        meter_label = Text("rule\nfollowed", font=SERIF, color=INK,
                           font_size=18, line_spacing=0.8)
        meter_label.next_to(meter_bg, LEFT, buff=0.2)

        meter_fill_start = Rectangle(width=0.56, height=3.6 * 0.95)
        meter_fill_start.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        meter_fill_start.align_to(meter_bg, DOWN).shift(UP * 0.02)

        meter_fill_end = Rectangle(width=0.56, height=3.6 * 0.80)
        meter_fill_end.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        meter_fill_end.align_to(meter_bg, DOWN).shift(UP * 0.02)

        # Session token blocks stacking
        block_positions = [
            lane_bg.get_center() + LEFT * 0.8 + UP * 1.8,
            lane_bg.get_center() + LEFT * 0.8 + UP * 1.0,
            lane_bg.get_center() + LEFT * 0.8 + UP * 0.2,
        ]
        blocks = []
        for pos in block_positions:
            b = Square(0.5).set_fill(SLATE, 0.3).set_stroke(SLATE, 1.0)
            b.move_to(pos)
            blocks.append(b)

        violation_chip = LabelChip("grade leak", accent=CRIMSON, size=20)
        violation_chip.next_to(lane_bg, DOWN, buff=0.3)

        self.play(FadeIn(lane_bg), FadeIn(lane_title), run_time=0.6)
        self.play(FadeIn(meter_bg), FadeIn(meter_label),
                  FadeIn(meter_fill_start), run_time=0.6)
        for b in blocks:
            self.play(FadeIn(b, shift=DOWN * 0.2), run_time=0.4)
        # Shrink meter fill to show degradation
        self.play(Transform(meter_fill_start, meter_fill_end), run_time=1.2)
        self.play(FadeIn(violation_chip), run_time=0.5)
        self.wait(5.7)


class B07_HookGate(Scene):
    def construct(self):
        # Two-lane diagram: advisory (left) vs. hook enforcement (right)
        left_bg = Rectangle(width=5.0, height=5.5)
        left_bg.set_fill(SLATE, 0.05).set_stroke(SLATE, 1.0)
        left_bg.to_edge(LEFT, buff=0.5)

        right_bg = Rectangle(width=5.0, height=5.5)
        right_bg.set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        right_bg.to_edge(RIGHT, buff=0.5)

        left_title = Text("CLAUDE.md advisory", font=DISPLAY,
                          color=INK, font_size=20, weight="MEDIUM")
        left_title.next_to(left_bg, UP, buff=0.25)
        right_title = Text("Hook enforcement", font=DISPLAY,
                           color=TEAL, font_size=20, weight="MEDIUM")
        right_title.next_to(right_bg, UP, buff=0.25)

        # Left lane: probability dial + write sometimes passes
        left_dial = Text("probability\ndial", font=SERIF, color=INK,
                         font_size=24, line_spacing=0.8)
        left_dial.move_to(left_bg.get_center() + UP * 1.2)
        left_arrow = Arrow(left_bg.get_center() + UP * 0.3,
                           left_bg.get_center() + DOWN * 0.8,
                           stroke_width=3, color=INK, buff=0.1)
        left_write = Text("Write()", font=MONO, color=CRIMSON, font_size=24)
        left_write.next_to(left_arrow, DOWN, buff=0.2)

        # Right lane: gate that blocks
        right_gate = Rectangle(width=1.8, height=1.0)
        right_gate.set_fill(TEAL, 0.6).set_stroke(TEAL, 2.0)
        right_gate.move_to(right_bg.get_center() + UP * 0.3)
        right_gate_label = Text("hook gate", font=SERIF, color=INK, font_size=22)
        right_gate_label.move_to(right_gate)

        right_write = Text("Write()", font=MONO, color=INK, font_size=24)
        right_write.move_to(right_bg.get_center() + UP * 1.5)
        right_arrow = Arrow(right_write.get_bottom() + DOWN * 0.1,
                            right_gate.get_top() + UP * 0.1,
                            stroke_width=3, color=INK, buff=0.1)
        blocked_chip = LabelChip("BLOCKED", accent=TEAL, size=20)
        blocked_chip.next_to(right_gate, DOWN, buff=0.35)

        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.5)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.5)
        self.play(FadeIn(left_dial), run_time=0.4)
        self.play(GrowArrow(left_arrow), run_time=0.5)
        self.play(FadeIn(left_write), run_time=0.4)
        self.play(FadeIn(right_write), run_time=0.4)
        self.play(GrowArrow(right_arrow), run_time=0.5)
        self.play(FadeIn(right_gate), FadeIn(right_gate_label), run_time=0.5)
        self.play(FadeIn(blocked_chip), run_time=0.5)
        self.wait(7.0)


class B08_BlockedWrite(Scene):
    def construct(self):
        # Write attempt blocked by hook
        write_attempt = Text("Write('Overall performance: B+')",
                             font=MONO, color=CRIMSON, font_size=26)
        write_attempt.to_edge(UP, buff=1.2)

        arrow_down = Arrow(write_attempt.get_bottom() + DOWN * 0.1,
                           ORIGIN + UP * 0.8,
                           stroke_width=3, color=INK, buff=0.1)

        gate = Rectangle(width=5.0, height=1.2)
        gate.set_fill(TEAL, 0.7).set_stroke(TEAL, 2.0)
        gate.move_to(ORIGIN + UP * 0.2)
        gate_text = Text("PreToolUse hook fires", font=SERIF,
                         color=INK, font_size=26)
        gate_text.move_to(gate)

        blocked_chip = LabelChip("BLOCKED: grade pattern detected", accent=CRIMSON, size=20)
        blocked_chip.next_to(gate, DOWN, buff=0.4)

        file_card = Rectangle(width=4.5, height=2.0)
        file_card.set_fill(SLATE, 0.06).set_stroke(SLATE, 1.0)
        file_card.to_edge(DOWN, buff=0.7)
        empty_label = Text("student-07.md  (unchanged)", font=MONO,
                           color=SLATE, font_size=22)
        empty_label.move_to(file_card)

        self.play(FadeIn(write_attempt), run_time=0.6)
        self.play(GrowArrow(arrow_down), run_time=0.5)
        self.play(FadeIn(gate), FadeIn(gate_text), run_time=0.5)
        self.play(FadeIn(blocked_chip), run_time=0.4)
        self.play(FadeIn(file_card), FadeIn(empty_label), run_time=0.6)
        self.wait(6.9)


class B10_StakesDiagram(Scene):
    def construct(self):
        # 100 session dots: 97 teal, 3 crimson
        import numpy as np
        title = Text("100 grading sessions", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        dots = VGroup()
        for i in range(100):
            col = CRIMSON if i < 3 else TEAL
            d = Dot(radius=0.18).set_fill(col, 1).set_stroke(width=0, opacity=0)
            row, col_idx = i // 10, i % 10
            d.move_to(LEFT * 2.7 + RIGHT * col_idx * 0.56 + DOWN * row * 0.46 + UP * 0.5)
            dots.add(d)

        violation_label = SerifLabel("3 violations", accent=CRIMSON, size=24)
        violation_label.next_to(dots, RIGHT, buff=0.5).shift(UP * 1.5)
        consequence_label = Text("grade leak\nparent email\nFERPA concern",
                                 font=SERIF, color=CRIMSON, font_size=22,
                                 line_spacing=0.9)
        consequence_label.next_to(violation_label, DOWN, buff=0.3)

        sub_label = SerifLabel("high probability is not enough here", accent=SLATE, size=22)
        sub_label.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(AnimationGroup(*[FadeIn(d, scale=0.8) for d in dots],
                                 lag_ratio=0.01, run_time=2.0))
        self.play(FadeIn(violation_label), FadeIn(consequence_label), run_time=0.7)
        self.play(FadeIn(sub_label), run_time=0.5)
        self.wait(7.3)


class B11_ThreeMoves(Scene):
    def construct(self):
        # Three sequential cards: Ask, Review, Test
        title = Text("The ask-Claude-to-write pattern", font=SERIF,
                     color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        steps = [
            (["Ask Claude", "to write the hook"], SLATE),
            (["Review", "the script"], SLATE),
            (["Test by triggering", "the block"], TEAL),
        ]
        cards = VGroup()
        for lines, col in steps:
            card = Rectangle(width=3.2, height=2.4)
            card.set_fill(col, 0.1).set_stroke(col, 1.5)
            text_lines = VGroup(*[Text(l, font=SERIF, color=INK, font_size=24)
                                   for l in lines])
            text_lines.arrange(DOWN, center=True, buff=0.2)
            if text_lines.width > 2.8:
                text_lines.scale_to_fit_width(2.8)
            text_lines.move_to(card)
            cards.add(VGroup(card, text_lines))

        cards.arrange(RIGHT, buff=0.6)
        cards.move_to(ORIGIN + DOWN * 0.1)

        check = Text("check", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        check.next_to(cards[-1], DOWN, buff=0.35)

        self.play(FadeIn(title), run_time=0.5)
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(check), run_time=0.4)
        self.wait(8.0)


class B12_TwoColumns(Scene):
    def construct(self):
        # Two columns: CLAUDE.md advisory vs. Hooks deterministic
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_width=1.5, color=SLATE)

        left_title = Text("CLAUDE.md", font=DISPLAY, color=INK,
                          font_size=26, weight="MEDIUM")
        left_title.move_to(LEFT * 3.5 + UP * 2.7)
        left_sub = SerifLabel("advisory", accent=SLATE, size=22)
        left_sub.next_to(left_title, DOWN, buff=0.2)

        left_items = VGroup(
            Text("Prefer ast over regex", font=SERIF, color=INK, font_size=22),
            Text("Semantic HTML", font=SERIF, color=INK, font_size=22),
            Text("Two-space indent", font=SERIF, color=INK, font_size=22),
            Text("Code style rules", font=SERIF, color=INK, font_size=22),
        )
        left_items.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        left_items.next_to(left_sub, DOWN, buff=0.5).align_to(LEFT * 5.8, LEFT)

        right_title = Text("Hooks", font=DISPLAY, color=TEAL,
                           font_size=26, weight="MEDIUM")
        right_title.move_to(RIGHT * 3.5 + UP * 2.7)
        right_sub = SerifLabel("deterministic", accent=TEAL, size=22)
        right_sub.next_to(right_title, DOWN, buff=0.2)

        right_items_texts = [
            "Block grade generation",
            "Verify after every edit",
            "Session-end audit log",
        ]
        right_items = VGroup(*[LabelChip(t, accent=TEAL, size=20)
                                for t in right_items_texts])
        right_items.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        right_items.next_to(right_sub, DOWN, buff=0.5).shift(RIGHT * 0.3)

        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.5)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(it, shift=RIGHT * 0.1) for it in left_items],
                              lag_ratio=0.2, run_time=1.2))
        self.play(LaggedStart(*[FadeIn(it, shift=LEFT * 0.1) for it in right_items],
                              lag_ratio=0.2, run_time=1.0))
        self.wait(7.4)


class B13_HeuristicCard(Scene):
    def construct(self):
        h1 = Text("Real problem = Hook.", font=SERIF, color=INK, font_size=48)
        h2 = Text("Annoying = CLAUDE.md.", font=SERIF, color=INK, font_size=48)
        heuristic = VGroup(h1, h2).arrange(DOWN, center=True, buff=0.3)
        heuristic.move_to(ORIGIN)
        rule_teal = Line(heuristic.get_corner(DL) + DOWN * 0.18,
                         heuristic.get_corner(DR) + DOWN * 0.18,
                         stroke_width=2.0, color=TEAL)
        self.play(FadeIn(heuristic), run_time=1.0)
        self.play(Create(rule_teal), run_time=0.7)
        self.wait(10.3)


class B14_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("do not (advisory)", font=SERIF, color=INK, font_size=44)
        m2 = Text("vs.", font=SERIF, color=SLATE, font_size=36)
        m3 = Text("cannot (hook)", font=SERIF, color=TEAL, font_size=44)
        main_text = VGroup(m1, m2, m3).arrange(DOWN, center=True, buff=0.25)
        main_text.move_to(ORIGIN + UP * 0.2)

        rule = Line(main_text.get_corner(DL) + DOWN * 0.18,
                    main_text.get_corner(DR) + DOWN * 0.18,
                    stroke_width=2.0, color=TEAL)

        handle = Text("@nikbearbrown", font=SERIF, color=CRIMSON, font_size=24)
        handle.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(main_text), Create(rule), run_time=1.0)
        self.play(FadeIn(handle), run_time=0.5)
        self.wait(8.0)
