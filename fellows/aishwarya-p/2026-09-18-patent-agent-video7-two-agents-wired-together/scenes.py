"""
Manim scenes for patent-agent-video7-two-agents-wired-together
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


class B01_WhereItStarted(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Where It", "Actually Started")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        box1_text = Text('checked: npl_text is not None', color=PALETTE["crimson"], font_size=16, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, -0.1, 0])
        box2_text = Text('real value: always a string, never None', color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.8)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "fixed, verified on one patent — a small sample",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_BroadeningOnPurpose(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Broadening the Test,", "On Purpose")
        self.add(title)

        p1 = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        p1_text = Text("OpenAI — language model patent", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(p1.get_center())
        self.play(Create(p1), Write(p1_text), run_time=1.0)
        self.wait(0.6)

        p2 = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["sage"], fill_opacity=0.1,
            stroke_color=PALETTE["sage"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        p2_text = Text("Shopify — generative AI filtering patent", color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(p2.get_center())
        self.play(Create(p2), Write(p2_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "chosen deliberately — different domains, different profiles",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_WhatItFound(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("What It", "Actually Found")
        self.add(title)

        stat1 = RoundedRectangle(
            corner_radius=0.1, width=3.6, height=1.3,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([-2.0, 1.3, 0])
        stat1_text = Text("20 citations\n18 patents", color=PALETTE["teal"], font_size=15, font=BODY_FONT, line_spacing=1.2).move_to(stat1.get_center())

        stat2 = RoundedRectangle(
            corner_radius=0.1, width=3.6, height=1.3,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([2.0, 1.3, 0])
        stat2_text = Text("3 citations\nsmallest yet", color=PALETTE["ink"], font_size=15, font=BODY_FONT, line_spacing=1.2).move_to(stat2.get_center())

        self.play(Create(stat1), Write(stat1_text), run_time=0.9)
        self.play(Create(stat2), Write(stat2_text), run_time=0.9)
        self.wait(0.6)

        intl = Text("CN · WO formats — correctly parsed", color=PALETTE["slate"], font_size=15, font=BODY_FONT).move_to([0, -0.2, 0])
        self.play(Write(intl), run_time=1.0)
        self.wait(0.6)

        quirk = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.06,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -1.4, 0])
        quirk_text = Text("same reissue, two kind codes — a real quirk, not a bug", color=PALETTE["crimson"], font_size=14, font=BODY_FONT).move_to(quirk.get_center())
        self.play(Create(quirk), Write(quirk_text), run_time=1.2)
        self.wait(1.5)


class B04_WiringThemTogether(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Wiring the Two", "Agents Together")
        self.add(title)

        flow = ["publication number", "ClaimsAgent", "LineageAgent", "combined JSON"]
        boxes = VGroup()
        for f in flow:
            b = RoundedRectangle(
                corner_radius=0.1, width=7.5, height=0.85,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(f, color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(b.get_center())
            boxes.add(VGroup(b, label))

        boxes.arrange(DOWN, buff=0.25).shift(UP * 0.2)

        for b in boxes:
            self.play(Create(b[0]), Write(b[1]), run_time=0.8)
            self.wait(0.3)

        bottom = Text(
            "one script — a flag skips classification for free",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
