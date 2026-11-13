"""
Manim scenes for what-is-ai-red-teaming STEM video
B01_TheFormalDefinition     — the real 2023 EO definition
B02_NotOldSchoolPentest     — traditional vs AI red teaming
B03_TheStructuralDifference — non-determinism, rerun to confirm
B04_WhosActuallyDoingThis   — OpenAI's real model history
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


class B01_TheFormalDefinition(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real,", "Formal Definition")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.12, width=8.5, height=2.0,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.6, 0])
        box_text = Text(
            "structured testing to find flaws\nand vulnerabilities in an AI system,\noften with the people who built it",
            color=PALETTE["teal"], font_size=16, font=BODY_FONT, line_spacing=1.4
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(1.0)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "from the 2023 Executive Order on AI",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_NotOldSchoolPentest(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Not Old-School", "Penetration Testing")
        self.add(title)

        trad = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        trad_text = Text("traditional: misconfigurations, unpatched code", color=PALETTE["slate"], font_size=15, font=BODY_FONT).move_to(trad.get_center())
        self.play(Create(trad), Write(trad_text), run_time=1.0)
        self.wait(0.6)

        ai = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        ai_text = Text("AI: can it be talked out of its own rules?", color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(ai.get_center())
        self.play(Create(ai), Write(ai_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "plus what it leaks, plus how it acts with real tools",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheStructuralDifference(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real,", "Structural Difference")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=7.0, height=1.0,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        box1_text = Text("outputs are non-deterministic", color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=7.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        box2_text = Text("a pass is provisional, not proof", color=PALETTE["crimson"], font_size=16, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.6)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "rerun, require repeated success, before calling it closed",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_WhosActuallyDoingThis(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Who's Actually", "Doing This")
        self.add(title)

        models = ["DALL-E 2 (2022)", "GPT-4", "GPT-4V", "DALL-E 3", "GPT-4o", "o1"]
        rows = VGroup()
        for m in models:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=5.5, height=0.6,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(m, color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.15).shift(UP * 0.1)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.5)
            self.wait(0.2)

        bottom = Text(
            "OpenAI's real, published external red-team history",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
