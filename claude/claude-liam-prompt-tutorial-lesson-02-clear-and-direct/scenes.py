"""
scenes.py — claude-liam-prompt-tutorial-lesson-02-clear-and-direct
Clear and Direct: Why Vague Prompts Produce Vague Outputs.
Source: Anthropic Prompt Engineering Interactive Tutorial — Lesson 02
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
        "After Anthropic Prompt Engineering Tutorial — Lesson 02",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_VagueVsSpecific(Scene):
    def construct(self):
        dur = 21.0

        title = Text("Specificity Eliminates Interpretations.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two prompt boxes
        vague_box = RoundedRectangle(
            width=5.5, height=1.2, corner_radius=0.14,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([-3.0, 1.5, 0])
        vague_hdr = Text("Vague", font_size=15, color=SPARK, weight=BOLD)
        vague_hdr.next_to(vague_box, UP, buff=0.1)
        vague_text = Text('"Write a summary."', font_size=15, color=SOFT)
        vague_text.move_to(vague_box)
        self.play(FadeIn(vague_box), Write(vague_hdr), FadeIn(vague_text), run_time=0.4)

        # Interpretations fan
        interps = [
            "One sentence?  Five pages?",
            "Bullet points or prose?",
            "For an expert or layperson?",
            "What to include?",
        ]
        for i, interp in enumerate(interps):
            t = Text(interp, font_size=13, color=GHOST)
            t.move_to([-3.0, 0.5 - i * 0.45, 0])
            self.play(FadeIn(t), run_time=0.15)

        # Specific box
        specific_box = RoundedRectangle(
            width=5.5, height=2.6, corner_radius=0.14,
            color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
        ).move_to([3.2, 0.6, 0])
        specific_hdr = Text("Specific", font_size=15, color=INK, weight=BOLD)
        specific_hdr.next_to(specific_box, UP, buff=0.1)
        specific_text = Text(
            '"Write a 3-sentence summary.\nPlain language. Non-expert reader.\nInclude: finding, method, limit."',
            font_size=13, color=SOFT
        )
        specific_text.move_to(specific_box)
        self.play(FadeIn(specific_box), Write(specific_hdr), FadeIn(specific_text), run_time=0.5)

        note = Text(
            "The second prompt eliminates dozens of valid interpretations.",
            font_size=17, color=SPARK, weight=BOLD
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 6.0)


class B02_SpecificityDimensions(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Four Dimensions. Specify What You Care About.", font_size=32, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        dims = [
            ("Length",             "How long? Sentences, words, pages."),
            ("Format",             "Prose, bullets, table, JSON?"),
            ("Audience",           "Expert, layperson, child?"),
            ("Required components","What must appear in the output?"),
        ]
        for i, (dim, desc) in enumerate(dims):
            y = 1.5 - i * 1.1
            col = SPARK if i % 2 == 0 else INK
            box = RoundedRectangle(
                width=3.2, height=0.8, corner_radius=0.12,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([-3.2, y, 0])
            lbl = Text(dim, font_size=15, color=col, weight=BOLD)
            lbl.move_to(box)
            dtl = Text(desc, font_size=14, color=SOFT)
            dtl.move_to([2.8, y, 0])
            self.play(FadeIn(VGroup(box, lbl)), FadeIn(dtl), run_time=0.3)

        note = Text(
            "Each unspecified dimension = a default Claude fills. Default may not be what you need.",
            font_size=15, color=SOFT
        )
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(dur - 5.5)


class B03_GoldenRule(Scene):
    def construct(self):
        dur = 19.0

        title = Text("Treat Claude Like a Capable New Employee.", font_size=32, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two columns: new employee vs prompt
        headers = ["New employee doesn't know", "Your prompt must tell them"]
        col_xs = [-3.2, 3.2]
        for hdr, x in zip(headers, col_xs):
            col = SPARK if x < 0 else INK
            t = Text(hdr, font_size=15, color=col, weight=BOLD)
            t.move_to([x, 2.0, 0])
            self.add(t)
        div = Line([0, 2.3, 0], [0, -2.3, 0], color=BORDER, stroke_width=1.2)
        self.play(FadeIn(div), run_time=0.2)

        pairs = [
            ("House style",          "Register and tone"),
            ("Audience assumptions", "Who is reading"),
            ("Edge-case preferences","How to handle exceptions"),
            ("Output format",        "Structure and length"),
        ]
        for i, (left, right) in enumerate(pairs):
            y = 1.2 - i * 1.0
            lt = Text(left, font_size=14, color=SPARK)
            lt.move_to([-3.2, y, 0])
            rt = Text(right, font_size=14, color=INK)
            rt.move_to([3.2, y, 0])
            self.play(FadeIn(lt), FadeIn(rt), run_time=0.3)

        rule = Text(
            'Vague prompt = "help with this".  Specific prompt = proper brief.',
            font_size=16, color=SPARK, weight=BOLD
        )
        rule.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(rule), run_time=0.4)
        self.wait(dur - 5.5)
