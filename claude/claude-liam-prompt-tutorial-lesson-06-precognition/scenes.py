"""
scenes.py — claude-liam-prompt-tutorial-lesson-06-precognition
Precognition: Give Claude a Scratchpad Before the Answer.
Source: Anthropic Prompt Engineering Interactive Tutorial — Lesson 06
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 06",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_TokenConstraint(Scene):
    def construct(self):
        dur = 18.0

        title = Text("The First Token Is a Trap.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Token sequence showing early commitment
        tokens = ["The", "answer", "is", "42", "because", "...", "(rationalize)"]
        colors  = [INK, INK, INK, SPARK, SOFT, SOFT, GHOST]
        boxes = VGroup()
        for i, (tok, col) in enumerate(zip(tokens, colors)):
            box = RoundedRectangle(
                width=1.5, height=0.7, corner_radius=0.1,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            )
            lbl = Text(tok, font_size=14, color=col)
            lbl.move_to(box)
            grp = VGroup(box, lbl)
            grp.move_to([i * 1.7 - 5.1, 0.8, 0])
            boxes.add(grp)

        for grp in boxes:
            self.play(FadeIn(grp), run_time=0.25)

        # Arrow under commit token
        commit_arrow = Arrow(
            start=[boxes[3].get_center()[0], 0.1, 0],
            end=[boxes[3].get_center()[0], -0.5, 0],
            color=SPARK, stroke_width=2.0,
            max_tip_length_to_length_ratio=0.2
        )
        commit_lbl = Text("committed early", font_size=14, color=SPARK)
        commit_lbl.next_to(commit_arrow, DOWN, buff=0.1)
        self.play(GrowArrow(commit_arrow), Write(commit_lbl), run_time=0.4)

        # Consequence label
        consequence = Text(
            "Subsequent tokens rationalize — they can't contradict the commit.",
            font_size=17, color=SOFT
        )
        consequence.move_to([0, -1.6, 0])
        self.play(FadeIn(consequence), run_time=0.5)

        rule = Text("Answer first = reasoning last = reasoning fake.", font_size=19, color=SPARK, weight=BOLD)
        rule.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.0)


class B02_ScratchpadStructure(Scene):
    def construct(self):
        dur = 20.0

        title = Text("The <thinking>/<answer> Scratchpad.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Before column
        before_hdr = Text("Without scratchpad", font_size=17, color=SPARK, weight=BOLD)
        before_hdr.move_to([-3.8, 2.2, 0])
        self.play(FadeIn(before_hdr), run_time=0.3)

        before_lines = [
            ("[ANSWER]", SPARK),
            ("The contract is valid.", INK),
            ("(reasoning implicit,", GHOST),
            (" unverifiable)", GHOST),
        ]
        for i, (line, col) in enumerate(before_lines):
            t = Text(line, font_size=15, color=col)
            t.move_to([-3.8, 1.5 - i * 0.55, 0])
            self.play(FadeIn(t), run_time=0.2)

        # Divider
        div = Line([0, 2.5, 0], [0, -2.5, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        # After column
        after_hdr = Text("With scratchpad", font_size=17, color=INK, weight=BOLD)
        after_hdr.move_to([3.5, 2.2, 0])
        self.play(FadeIn(after_hdr), run_time=0.3)

        after_lines = [
            ("<thinking>", SPARK),
            ("  Clause 4 says X.", INK),
            ("  But clause 7 overrides.", INK),
            ("  So the answer is: invalid.", INK),
            ("</thinking>", SPARK),
            ("<answer>", SOFT),
            ("  The contract is invalid.", INK),
            ("</answer>", SOFT),
        ]
        for i, (line, col) in enumerate(after_lines):
            t = Text(line, font_size=14, color=col)
            t.move_to([3.5, 1.6 - i * 0.5, 0])
            self.play(FadeIn(t), run_time=0.15)

        # Bottom note
        note = Text(
            "Scratchpad = inspectable, steerable intermediate reasoning.",
            font_size=17, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 7.0)


class B03_WhenItHelps(Scene):
    def construct(self):
        dur = 19.0

        title = Text("Scratchpad: When to Add It, When to Skip It.", font_size=32, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Task type", "Use <thinking>?", "Reason"]
        col_xs = [-4.5, 0.2, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Multi-step logic",       "YES",  SPARK,  "Backtracking needed"),
            ("Ambiguous classification","YES",  SPARK,  "Contradictions surface"),
            ("Factual lookup",          "NO",   GHOST,  "No reasoning chain"),
            ("Simple retrieval",        "NO",   GHOST,  "Tokens wasted"),
            ("Reach for scratch paper?","YES",  SPARK,  "Human heuristic"),
        ]
        for i, (task, verdict, vcol, reason) in enumerate(rows):
            y = 1.0 - i * 0.75
            vals  = [task, verdict, reason]
            cols  = [INK, vcol, SOFT]
            for val, x, col in zip(vals, col_xs, cols):
                t = Text(val, font_size=14, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.18)

        rule = Text(
            "Rule: if a human expert would reach for scratch paper, add <thinking>.",
            font_size=17, color=SPARK, weight=BOLD
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.0)
