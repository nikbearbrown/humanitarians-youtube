"""
Manim scenes for finance-fluency-trap
B01_MissingEvidence  — a fluent sentence, marked missing source/period/owner
B02_PhaseGate        — the preparation/judgment gate
B03_VerifiedChecklist — the four things verified requires
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


class B01_MissingEvidence(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        card = RoundedRectangle(
            corner_radius=0.15, width=9.0, height=1.6,
            fill_color=PALETTE["ink"], fill_opacity=0.05,
            stroke_color=PALETTE["ink"], stroke_width=1.5
        ).shift(UP * 1.4)
        sentence = Text(
            "\"Revenue is down 8% QoQ, driven by\nenterprise renewal timing.\"",
            color=PALETTE["ink"], font_size=20, line_spacing=1.2, font=BODY_FONT
        ).move_to(card.get_center())

        self.play(Create(card), Write(sentence), run_time=1.0)
        self.wait(0.4)

        tags = VGroup(
            Text("no source", color=PALETTE["crimson"], font_size=18, font=BODY_FONT),
            Text("no period", color=PALETTE["crimson"], font_size=18, font=BODY_FONT),
            Text("no owner", color=PALETTE["crimson"], font_size=18, font=BODY_FONT),
        ).arrange(RIGHT, buff=0.8).shift(DOWN * 1.0)

        for tag in tags:
            underline = Rectangle(
                width=1.4, height=0.05,
                fill_color=PALETTE["crimson"], fill_opacity=0.9, stroke_width=0
            ).next_to(tag, DOWN, buff=0.1)
            self.play(Write(tag), Create(underline), run_time=0.5)
            self.wait(0.2)

        bottom = Text(
            "confidence is not the same as evidence",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).shift(DOWN * 2.6)
        self.play(Write(bottom), run_time=0.6)
        self.wait(1.2)


class B02_PhaseGate(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "Preparation vs. Judgment", color=PALETTE["ink"], font_size=24, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        left_box = RoundedRectangle(
            corner_radius=0.12, width=5.2, height=3.2,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).shift(LEFT * 3.0)
        left_title = Text("Machine prepares", color=PALETTE["teal"], font_size=18, font=BODY_FONT).move_to(
            left_box.get_top() + DOWN * 0.4
        )
        left_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=15, font=BODY_FONT)
            for t in ["drafts the note", "computes the delta", "flags anomalies"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(left_box.get_center() + DOWN * 0.1)

        right_box = RoundedRectangle(
            corner_radius=0.12, width=5.2, height=3.2,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).shift(RIGHT * 3.0)
        right_title = Text("Human decides", color=PALETTE["slate"], font_size=18, font=BODY_FONT).move_to(
            right_box.get_top() + DOWN * 0.4
        )
        right_items = VGroup(*[
            Text(t, color=PALETTE["ink"], font_size=15, font=BODY_FONT)
            for t in ["ties it to a source", "confirms the owner", "approves or blocks"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(right_box.get_center() + DOWN * 0.1)

        gate_line = Line(
            start=[0, 1.8, 0], end=[0, -1.8, 0],
            color=PALETTE["crimson"], stroke_width=3
        )
        gate_label = Text("the gate", color=PALETTE["crimson"], font_size=14, font=BODY_FONT).next_to(
            gate_line, DOWN, buff=0.3
        ).shift(DOWN * 0.7)

        self.play(Create(left_box), Write(left_title), run_time=0.6)
        self.play(Write(left_items), run_time=0.8)
        self.play(Create(right_box), Write(right_title), run_time=0.6)
        self.play(Write(right_items), run_time=0.8)
        self.wait(0.2)

        # "a phase gate splits preparation from judgment" — gate named early, appears now
        self.play(Create(gate_line), Write(gate_label), run_time=0.8)
        self.wait(0.8)

        # "the machine drafts, computes, and flags" — highlight left
        self.play(Indicate(left_box, scale_factor=1.03), run_time=1.4)
        self.wait(1.8)

        # "a named human reads... ties them to a source... decides" — highlight right
        self.play(Indicate(right_box, scale_factor=1.03), run_time=1.4)
        self.wait(1.8)

        # "the gate is not a formality..." — hold on the gate through the close
        self.play(Indicate(gate_line, scale_factor=1.05), run_time=1.0)
        self.wait(3.5)


class B03_VerifiedChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text(
            "What \"Verified\" Requires", color=PALETTE["ink"], font_size=24, font=BODY_FONT
        ).to_edge(UP, buff=0.7)
        self.add(title)

        items = ["Source file", "Period", "Control total", "Owner"]
        cards = VGroup()
        for i, item in enumerate(items):
            card = RoundedRectangle(
                corner_radius=0.1, width=2.6, height=1.4,
                fill_color=PALETTE["sage"], fill_opacity=0.12,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(item, color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(card.get_center())
            group = VGroup(card, label)
            cards.add(group)

        cards.arrange(RIGHT, buff=0.4).shift(UP * 0.3)

        for c in cards:
            self.play(Create(c[0]), Write(c[1]), run_time=0.5)
            self.wait(0.15)

        self.wait(0.3)
        self.play(Indicate(cards, scale_factor=1.02), run_time=1.0)
        self.wait(0.5)
        bottom = Text(
            "missing any one — it's an assertion, not evidence",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).shift(DOWN * 2.3)
        self.play(Write(bottom), run_time=0.6)
        self.wait(1.2)
