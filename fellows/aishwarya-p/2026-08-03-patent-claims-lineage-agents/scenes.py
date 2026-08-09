"""
Manim scenes for patent-claims-lineage-agents
B01_ClaimsVsAbstract — split screen: marketing abstract vs. legal claims
B04_HonestBlock      — the correct blocked state: no fake output, clear error
B06_SchemaConfirmed  — the real BigQuery schema, confirmed by hand
B07_TwoAgentsSummary — the closing lesson: two readings, earned complexity
"""
from manim import *

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

BODY_FONT = "Menlo"
MONO_FONT = "Menlo"


class B01_ClaimsVsAbstract(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Abstract vs. Claims", color=PALETTE["ink"], font_size=26, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        left_card = RoundedRectangle(
            corner_radius=0.12, width=5.8, height=4.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.06,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).shift(LEFT * 3.3)
        left_title = Text(
            "Abstract", color=PALETTE["crimson"], font_size=20, font=BODY_FONT
        ).move_to(left_card.get_top() + DOWN * 0.4)
        left_body = Text(
            "\"A method for cooling\nintegrated circuits using\nthermally conductive\nsubstrates.\"",
            color=PALETTE["ink"], font_size=16, line_spacing=1.3, font=BODY_FONT
        ).move_to(left_card.get_center() + DOWN * 0.1)
        left_tag = Text(
            "marketing language", color=PALETTE["crimson"], font_size=15, font=BODY_FONT
        ).move_to(left_card.get_bottom() + UP * 0.4)

        right_card = RoundedRectangle(
            corner_radius=0.12, width=5.8, height=4.0,
            fill_color=PALETTE["teal"], fill_opacity=0.06,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).shift(RIGHT * 3.3)
        right_title = Text(
            "Claims", color=PALETTE["teal"], font_size=20, font=BODY_FONT
        ).move_to(right_card.get_top() + DOWN * 0.4)
        right_body = Text(
            "1. A thermal substrate\n   comprising [X], [Y]...\n2. The substrate of\n   claim 1, wherein...",
            color=PALETTE["ink"], font_size=16, font=MONO_FONT, line_spacing=1.3
        ).move_to(right_card.get_center() + DOWN * 0.1)
        right_tag = Text(
            "the legal artifact", color=PALETTE["teal"], font_size=15, font=BODY_FONT
        ).move_to(right_card.get_bottom() + UP * 0.4)

        self.play(Create(left_card), Write(left_title), run_time=0.8)
        self.play(Write(left_body), run_time=1.6)
        self.wait(0.6)
        self.play(Write(left_tag), run_time=0.8)
        self.wait(1.2)

        self.play(Create(right_card), Write(right_title), run_time=0.8)
        self.play(Write(right_body), run_time=1.8)
        self.wait(0.6)
        self.play(Write(right_tag), run_time=0.8)
        self.wait(1.0)

        # highlight the broad/narrow distinction the narration names
        broad_narrow = Text(
            "broad and offensive, or narrow and defensive",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).shift(DOWN * 2.5)
        self.play(Write(broad_narrow), run_time=1.4)
        self.wait(1.5)

        # briefly indicate each card to give the eye time to compare
        self.play(Indicate(left_card, scale_factor=1.03), run_time=1.2)
        self.wait(0.4)
        self.play(Indicate(right_card, scale_factor=1.03), run_time=1.2)
        self.wait(0.8)

        self.play(FadeOut(broad_narrow), run_time=0.6)

        arrow = Text(
            "most tools only read this side ->", color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).shift(DOWN * 3.1)
        self.play(Write(arrow), run_time=1.0)
        self.wait(2.5)


class B04_HonestBlock(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "python3 claims_agent.py --patent US-XXXXXXXX",
            color=PALETTE["ink"], font_size=20, font=MONO_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        error_box = Rectangle(
            width=8.5, height=1.8,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).shift(UP * 0.3)

        error_text = Text(
            "NotImplementedError:",
            color=PALETTE["crimson"], font_size=18, font=MONO_FONT
        ).move_to(error_box.get_top() + DOWN * 0.4)

        error_detail = Text(
            "Waiting on real claims text from USPTOClient\nbefore this is implemented and tested.",
            color=PALETTE["ink"], font_size=15, font=MONO_FONT, line_spacing=1.2
        ).move_to(error_box.get_center() + DOWN * 0.15)

        self.play(Create(error_box), run_time=1.0)
        self.play(Write(error_text), run_time=1.0)
        self.wait(0.5)
        self.play(Write(error_detail), run_time=1.6)
        self.wait(1.5)

        self.play(Indicate(error_box, scale_factor=1.02), run_time=1.2)
        self.wait(0.8)

        blocked_chip = RoundedRectangle(
            corner_radius=0.15, width=2.2, height=0.55,
            fill_color=PALETTE["crimson"], fill_opacity=0.85, stroke_width=0
        ).shift(DOWN * 1.7 + LEFT * 2.5)
        blocked_label = Text(
            "BLOCKED", color=PALETTE["bg"], font_size=18, font=BODY_FONT
        ).move_to(blocked_chip.get_center())

        pass_chip = RoundedRectangle(
            corner_radius=0.15, width=4.4, height=0.55,
            fill_color=PALETTE["teal"], fill_opacity=0.85, stroke_width=0
        ).shift(DOWN * 1.7 + RIGHT * 1.6)
        pass_label = Text(
            "correctly stopped, not faked", color=PALETTE["bg"], font_size=16, font=BODY_FONT
        ).move_to(pass_chip.get_center())

        self.play(
            FadeIn(blocked_chip), Write(blocked_label),
            run_time=1.0
        )
        self.wait(0.8)
        self.play(
            FadeIn(pass_chip), Write(pass_label),
            run_time=1.2
        )
        self.wait(2.0)


class B06_SchemaConfirmed(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "patents-public-data.patents.publications — confirmed schema",
            color=PALETTE["ink"], font_size=19, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        claims_card = RoundedRectangle(
            corner_radius=0.12, width=5.6, height=2.4,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).shift(LEFT * 3.1 + DOWN * 0.3)
        claims_title = Text(
            "claims_localized", color=PALETTE["slate"], font_size=20, font=BODY_FONT
        ).move_to(claims_card.get_top() + DOWN * 0.4)
        claims_fields = VGroup(*[
            Text(f, color=PALETTE["ink"], font_size=16, font=MONO_FONT)
            for f in ["text: STRING", "language: STRING", "truncated: BOOLEAN"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(claims_card.get_center() + DOWN * 0.1)

        citation_card = RoundedRectangle(
            corner_radius=0.12, width=5.6, height=2.4,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).shift(RIGHT * 3.1 + DOWN * 0.3)
        citation_title = Text(
            "citation", color=PALETTE["slate"], font_size=20, font=BODY_FONT
        ).move_to(citation_card.get_top() + DOWN * 0.4)
        citation_fields = VGroup(*[
            Text(f, color=PALETTE["ink"], font_size=16, font=MONO_FONT)
            for f in ["publication_number: STRING", "category: STRING", "npl_text: STRING"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(citation_card.get_center() + DOWN * 0.1)

        self.play(Create(claims_card), Write(claims_title), run_time=1.0)
        self.play(Write(claims_fields), run_time=1.6)
        self.wait(1.0)
        self.play(Create(citation_card), Write(citation_title), run_time=1.0)
        self.play(Write(citation_fields), run_time=1.6)
        self.wait(1.2)

        self.play(Indicate(claims_card, scale_factor=1.02), run_time=1.0)
        self.wait(0.4)
        self.play(Indicate(citation_card, scale_factor=1.02), run_time=1.0)
        self.wait(1.0)

        fail_row = VGroup(
            Text("X", color=PALETTE["crimson"], font_size=26, font=BODY_FONT),
            Text("guessed format 'US-2019...-A1'", color=PALETTE["crimson"], font_size=15, font=BODY_FONT)
        ).arrange(RIGHT, buff=0.2).shift(DOWN * 2.1)
        self.play(Write(fail_row), run_time=1.2)
        self.wait(1.2)

        pass_row = VGroup(
            Text("OK", color=PALETTE["teal"], font_size=26, font=BODY_FONT),
            Text("real format 'US-XXXXXX-A' — found in 5 sample rows", color=PALETTE["teal"], font_size=15, font=BODY_FONT)
        ).arrange(RIGHT, buff=0.2).shift(DOWN * 2.7)
        self.play(Write(pass_row), run_time=1.4)
        self.wait(2.5)


class B07_TwoAgentsSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "When Two Readings Earn the Complexity",
            color=PALETTE["ink"], font_size=22, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        claims_circle = Circle(
            radius=1.7, fill_color=PALETTE["teal"], fill_opacity=0.12,
            stroke_color=PALETTE["teal"], stroke_width=2
        ).shift(LEFT * 1.3 + UP * 0.3)
        lineage_circle = Circle(
            radius=1.7, fill_color=PALETTE["slate"], fill_opacity=0.12,
            stroke_color=PALETTE["slate"], stroke_width=2
        ).shift(RIGHT * 1.3 + UP * 0.3)

        claims_label = Text(
            "Claims\nAgent", color=PALETTE["teal"], font_size=18, line_spacing=1.1, font=BODY_FONT
        ).move_to(claims_circle.get_center() + LEFT * 0.9)
        lineage_label = Text(
            "Lineage\nAgent", color=PALETTE["slate"], font_size=18, line_spacing=1.1, font=BODY_FONT
        ).move_to(lineage_circle.get_center() + RIGHT * 0.9)

        coordinator_dot = Dot(
            point=[0, -1.9, 0], radius=0.12, color=PALETTE["crimson"]
        )
        coordinator_label = Text(
            "flags disagreement,\ndoesn't resolve it",
            color=PALETTE["ink"], font_size=16, line_spacing=1.1, font=BODY_FONT
        ).move_to(coordinator_dot.get_center() + DOWN * 0.5)

        self.play(Create(claims_circle), Write(claims_label), run_time=1.2)
        self.wait(0.6)
        self.play(Create(lineage_circle), Write(lineage_label), run_time=1.2)
        self.wait(1.0)
        self.play(Indicate(claims_circle, scale_factor=1.03), run_time=1.0)
        self.wait(0.4)
        self.play(Indicate(lineage_circle, scale_factor=1.03), run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(coordinator_dot), run_time=0.8)
        self.play(Write(coordinator_label), run_time=1.4)
        self.wait(1.5)

        bottom_line = Text(
            "earned complexity, not default complexity",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).shift(DOWN * 2.9)
        self.play(Write(bottom_line), run_time=1.4)
        self.wait(1.2)
