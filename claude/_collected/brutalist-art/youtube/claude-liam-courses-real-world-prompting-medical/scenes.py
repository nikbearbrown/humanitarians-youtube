"""
scenes.py — claude-liam-courses-real-world-prompting-medical
Medical Prompting: Role, Uncertainty, Escalation, Disclaimer.
Source: Anthropic Courses — Real-World Prompting: Medical Applications
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
        "After Anthropic Courses — Real-World Prompting",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_RoleCalibration(Scene):
    def construct(self):
        dur = 19.0

        title = Text("Role Is the Frame Selector.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two role boxes side by side
        roles = [
            ("Role: Emergency Physician", "Clinical, terse,\nassumes expertise,\nno over-explanation."),
            ("Role: Patient Educator",    "Plain language,\nanalogies, step-by-step,\nmore context."),
        ]
        xs = [-3.2, 3.2]
        cols = [SPARK, INK]
        for (role_hdr, role_body), x, col in zip(roles, xs, cols):
            box = RoundedRectangle(
                width=4.8, height=2.8, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, 0.4, 0])
            hdr = Text(role_hdr, font_size=16, color=col, weight=BOLD)
            hdr.move_to(box).shift(UP * 0.8)
            body = Text(role_body, font_size=15, color=SOFT)
            body.move_to(box).shift(DOWN * 0.2)
            self.play(FadeIn(VGroup(box, hdr, body)), run_time=0.4)

        fact = Text("Same clinical fact. Different frame.", font_size=18, color=SOFT)
        fact.move_to([0, -1.6, 0])
        self.play(FadeIn(fact), run_time=0.4)

        rule = Text("Role = calibration, not decoration.", font_size=20, color=SPARK, weight=BOLD)
        rule.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.0)


class B02_UncertaintyEscalation(Scene):
    def construct(self):
        dur = 22.0

        title = Text("Two Instructions. Two Separate Problems.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        headers = ["Instruction", "Problem it solves", "Example phrase"]
        col_xs = [-4.8, 0.0, 4.8]
        y_hdr = 2.1
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=17, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.75)
        self.add(div)

        rows = [
            ("Uncertainty language", "False confidence",  "SPARK", '"This may indicate..."'),
            ("Uncertainty language", "Overconfident dx",   "SPARK", '"Evidence is mixed..."'),
            ("Escalation trigger",   "In-scope overreach", "INK",   '"See a clinician today."'),
            ("Escalation trigger",   "Cannot resolve",     "INK",   '"This is out of scope."'),
        ]
        color_map = {"SPARK": SPARK, "INK": INK}
        for i, (inst, prob, col_key, example) in enumerate(rows):
            y = 1.0 - i * 0.75
            vals = [inst, prob, example]
            vcols = [color_map[col_key], SOFT, SOFT]
            for val, x, col in zip(vals, col_xs, vcols):
                t = Text(val, font_size=13, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.18)

        note = Text(
            "Without escalation, the model resolves everything in-context. That's wrong.",
            font_size=16, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 7.0)


class B03_FourGuardrails(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Four Guardrails. Every Medical Prompt.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        guardrails = [
            ("1. Role",              "Set clinical register\nand knowledge level."),
            ("2. Uncertainty",       "Hedge confidence;\nnever assert dx."),
            ("3. Escalation",        "Trigger: see clinician\nif red-flag present."),
            ("4. Disclaimer",        "Not medical advice.\nConsult a clinician."),
        ]

        for i, (label, detail) in enumerate(guardrails):
            y = 1.6 - i * 1.1
            num_col = SPARK if i % 2 == 0 else INK
            lbl = Text(label, font_size=18, color=num_col, weight=BOLD)
            lbl.move_to([-3.0, y, 0])
            dtl = Text(detail, font_size=15, color=SOFT)
            dtl.move_to([2.5, y, 0])
            line = Line([-6.0, y - 0.45, 0], [6.0, y - 0.45, 0], color=BORDER, stroke_width=0.8)
            self.play(FadeIn(lbl), FadeIn(dtl), run_time=0.3)
            self.play(FadeIn(line), run_time=0.15)

        note = Text(
            "Bake all four into the system prompt. Applied every turn, not just once.",
            font_size=16, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.5)
