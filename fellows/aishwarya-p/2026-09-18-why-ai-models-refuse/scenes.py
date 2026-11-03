"""
Manim scenes for why-ai-models-refuse STEM video
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


class B01_HowItsTrained(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("How Refusal Gets", "Trained In")
        self.add(title)

        steps = ["pretraining", "supervised fine-tuning", "reward model training", "RL fine-tuning"]
        rows = VGroup()
        for s in steps:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=6.0, height=0.75,
                fill_color=PALETTE["teal"], fill_opacity=0.08,
                stroke_color=PALETTE["teal"], stroke_width=1.5
            )
            label = Text(s, color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.2).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "by deployment, refusal is baked into the weights",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_TheSurprisingFinding(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real,", "Surprising Finding")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.12, width=8.5, height=1.8,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 0.8, 0])
        box_text = Text(
            "refusal = one single direction\nin activation space",
            color=PALETTE["ink"], font_size=18, font=BODY_FONT, line_spacing=1.4
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(1.0)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "erase it: refusal drops. inject it: even harmless prompts get refused.",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_WhyOverRefusal(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why That Leads", "to Over-Refusal")
        self.add(title)

        stat = RoundedRectangle(
            corner_radius=0.1, width=6.0, height=1.3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        stat_text = Text("0.89 correlation\nsafety score ↔ over-refusal", color=PALETTE["crimson"], font_size=15, font=BODY_FONT, line_spacing=1.3).move_to(stat.get_center())
        self.play(Create(stat), Write(stat_text), run_time=1.2)
        self.wait(1.0)

        analogy = Text(
            "the bouncer isn't reading intent —\nit's matching \"weapon-shaped\"",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to([0, -0.6, 0])
        self.play(Write(analogy), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "a chef's knife matches the pattern anyway",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_TheRealTradeoff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Tradeoff")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        box1_text = Text("structural, not a bug someone forgot to fix", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.8)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["sage"], fill_opacity=0.1,
            stroke_color=PALETTE["sage"], stroke_width=1.5
        ).move_to([0, -0.1, 0])
        box2_text = Text("newer approach: scale help to actual risk", color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(1.0)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "moving away from a hard refuse-or-comply line",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
