"""
Manim scenes for finance-agent-market-2026 STEM video
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


def make_title(line1, line2, font_size=22):
    t1 = Text(line1, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    if line2:
        t2 = Text(line2, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.15)
    else:
        title = VGroup(t1)
    title.to_edge(UP, buff=0.7)
    title.move_to([0, title.get_y(), 0])
    return title


class B01_TwoKinds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Two Real Kinds", "of Agent")
        self.add(title)

        assistive = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.3,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        assistive_text = Text(
            "assistive — surfaces insights,\nwaits for approval before acting",
            color=PALETTE["teal"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(assistive.get_center())
        self.play(Create(assistive), Write(assistive_text), run_time=1.2)
        self.wait(0.8)

        self.play(assistive.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        autonomous = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.3,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        autonomous_text = Text(
            "autonomous — completes the\nworkflow itself, inside guardrails",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(autonomous.get_center())
        self.play(Create(autonomous), Write(autonomous_text), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the distinction is where the human sits",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_WhatsShipping(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("What's Actually", "Shipping")
        self.add(title)

        vendors = [
            ("Prophix", "Architect + Consolidation Agents"),
            ("Sana", "FP&A, vendor mgmt, compliance"),
            ("Experian", "Agent Operating System"),
        ]
        rows = VGroup()
        for name, desc in vendors:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=8.0, height=0.9,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            name_label = Text(name, color=PALETTE["ink"], font_size=16, font=BODY_FONT)
            desc_label = Text(desc, color=PALETTE["teal"], font_size=13, font=BODY_FONT)
            text_group = VGroup(name_label, desc_label).arrange(RIGHT, buff=0.5).move_to(row_box.get_center())
            rows.add(VGroup(row_box, text_group))

        rows.arrange(DOWN, buff=0.3).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.9)
            self.wait(0.4)

        bottom = Text(
            "real releases, this year — not roadmap",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheHonestLine(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Honest Line", "")
        self.add(title)

        quote_box = RoundedRectangle(
            corner_radius=0.12, width=8.5, height=1.8,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.6, 0])
        quote_text = Text(
            '"99% accuracy is 0% trust"\n— Alok Ajmera, CEO, Prophix',
            color=PALETTE["crimson"], font_size=18, font=BODY_FONT, line_spacing=1.4
        ).move_to(quote_box.get_center())
        self.play(Create(quote_box), Write(quote_text), run_time=1.2)
        self.wait(1.0)

        self.play(quote_box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "the real differentiator: showing the work, knowing the limits",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_TheOpenGap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real,", "Still-Open Gap")
        self.add(title)

        stat1 = RoundedRectangle(
            corner_radius=0.1, width=3.6, height=1.4,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([-2.0, 0.5, 0])
        stat1_text = Text("87%\nsay essential", color=PALETTE["teal"], font_size=18, font=BODY_FONT, line_spacing=1.2).move_to(stat1.get_center())

        stat2 = RoundedRectangle(
            corner_radius=0.1, width=3.6, height=1.4,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([2.0, 0.5, 0])
        stat2_text = Text("most\nstill experimenting", color=PALETTE["crimson"], font_size=15, font=BODY_FONT, line_spacing=1.2).move_to(stat2.get_center())

        self.play(Create(stat1), Write(stat1_text), run_time=1.0)
        self.play(Create(stat2), Write(stat2_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "the tools exist — the trust hasn't caught up yet",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
