"""
Manim scenes for what-is-an-agent-harness STEM video
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


class B01_TheComputerAnalogy(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Computer Analogy")
        self.add(title)

        pairs = [
            ("Model", "CPU"),
            ("Context Window", "RAM"),
            ("Agent Harness", "Operating System"),
            ("Agent", "Application"),
        ]
        rows = VGroup()
        for left, right in pairs:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=7.5, height=0.75,
                fill_color=PALETTE["teal"], fill_opacity=0.08,
                stroke_color=PALETTE["teal"], stroke_width=1.5
            )
            left_label = Text(left, color=PALETTE["teal"], font_size=15, font=BODY_FONT)
            right_label = Text(right, color=PALETTE["ink"], font_size=15, font=BODY_FONT)
            pair_group = VGroup(left_label, right_label).arrange(RIGHT, buff=0.8).move_to(row_box.get_center())
            rows.add(VGroup(row_box, pair_group))

        rows.arrange(DOWN, buff=0.18).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "the harness curates context and boots the agent's tools",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_HarnessVsFrameworkVsSDK(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Harness vs.", "Framework vs. SDK")
        self.add(title)

        rows_data = [
            ("Framework", "building blocks for agent logic"),
            ("SDK", "a vendor's library for one model"),
            ("Harness", "runs, constrains, observes the agent"),
        ]
        rows = VGroup()
        for name, desc in rows_data:
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
            "three real, different layers — often confused",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_WhyRealInfrastructure(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why This Became", "Real Infrastructure")
        self.add(title)

        failures = ["API timeouts", "memory limits", "tool calls out of sequence", "calls to functions that don't exist"]
        rows = VGroup()
        for f in failures:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=6.5, height=0.7,
                fill_color=PALETTE["crimson"], fill_opacity=0.08,
                stroke_color=PALETTE["crimson"], stroke_width=1.5
            )
            label = Text(f, color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.2).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "a harness makes a non-deterministic model governed and verifiable",
            color=PALETTE["ink"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_TheRealMarketSignal(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Market Signal")
        self.add(title)

        companies = ["Harvey", "Legora", "Sierra"]
        boxes = VGroup()
        for c in companies:
            b = RoundedRectangle(
                corner_radius=0.1, width=2.4, height=1.2,
                fill_color=PALETTE["gold"], fill_opacity=0.1,
                stroke_color=PALETTE["gold"], stroke_width=1.5
            )
            label = Text(c, color=PALETTE["ink"], font_size=18, font=BODY_FONT).move_to(b.get_center())
            boxes.add(VGroup(b, label))

        boxes.arrange(RIGHT, buff=0.4).shift(UP * 1.0)

        for b in boxes:
            self.play(Create(b[0]), Write(b[1]), run_time=0.8)
            self.wait(0.3)

        self.play(Indicate(boxes, scale_factor=1.03), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "each crossed $100M ARR in 2026 selling the harness layer",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
