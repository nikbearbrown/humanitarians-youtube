"""
scenes.py — claude-liam-prompt-tutorial-lesson-03-role-prompting
Role Prompting: Register and Calibration, Not Costume.
Source: Anthropic Prompt Engineering Interactive Tutorial — Lesson 03
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 03",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_RegisterMatrix(Scene):
    def construct(self):
        dur = 22.0

        title = Text("Role Shifts All Four Register Axes.", font_size=35, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Axis", "Child (pediatric)", "Expert (grand rounds)"]
        col_xs = [-4.5, 0.0, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=16, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Vocabulary",       "Simple words",       "Technical terms"),
            ("Prior knowledge",  "None assumed",       "Specialist assumed"),
            ("Tone",             "Warm, reassuring",   "Precise, formal"),
            ("Depth",            "Short, concrete",    "Detailed, nuanced"),
        ]
        for i, (axis, child, expert) in enumerate(rows):
            y = 1.0 - i * 0.85
            vals = [axis, child, expert]
            vcols = [INK, SPARK, SOFT]
            for val, x, col in zip(vals, col_xs, vcols):
                t = Text(val, font_size=13, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.2)

        note = Text(
            "Same facts. Two roles. Two completely different responses.",
            font_size=17, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.5)


class B02_RoleVsPersona(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Role for Calibration. Persona for Voice.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two columns
        for side, label, body, x, col in [
            ("Role", "Functional", '"You are an expert\ntax attorney."\n\nSets: register,\nvocabulary, depth.',
             -3.2, INK),
            ("Persona", "Voice + character", '"You are Marcus, a sardonic\n1970s tax attorney who\nuses nautical metaphors."\n\nSets: register + character\n+ consistency of voice.',
             3.2, SPARK),
        ]:
            box = RoundedRectangle(
                width=5.4, height=3.4, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, 0.2, 0])
            hdr = Text(side, font_size=20, color=col, weight=BOLD)
            hdr.next_to(box, UP, buff=0.1)
            sub = Text(label, font_size=13, color=GHOST)
            sub.move_to(box).shift(UP * 1.2)
            bd = Text(body, font_size=13, color=SOFT)
            bd.move_to(box).shift(DOWN * 0.3)
            self.play(FadeIn(VGroup(box, hdr, sub, bd)), run_time=0.5)

        note = Text(
            "Know which you need. Both are valid.",
            font_size=18, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.0)


class B03_WhenRoleHelps(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Does the Role Change What Counts as Good?", font_size=31, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Task type", "Role helps?", "Why"]
        col_xs = [-4.5, 0.0, 4.5]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Technical writing\nfor specific audience", "YES", SPARK, "Register shifts output quality"),
            ("Explanation at\nknowledge level",           "YES", SPARK, "Calibration is the goal"),
            ("Factual date extraction",                   "NO",  GHOST, "Task is register-agnostic"),
            ("Filling a template",                        "NO",  GHOST, "Role adds no signal"),
        ]
        for i, (task, verdict, vcol, reason) in enumerate(rows):
            y = 1.0 - i * 0.9
            vals = [task, verdict, reason]
            vcols = [INK, vcol, SOFT]
            for val, x, col in zip(vals, col_xs, vcols):
                t = Text(val, font_size=13, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.2)

        rule = Text(
            "Test: does the role change what counts as a good answer? If yes, use it.",
            font_size=16, color=SPARK, weight=BOLD
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 6.0)
