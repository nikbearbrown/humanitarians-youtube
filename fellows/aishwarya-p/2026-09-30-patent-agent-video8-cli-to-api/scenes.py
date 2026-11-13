"""
Manim scenes for patent-agent-video8-cli-to-api
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


class B01_WhyAnAPI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why an API,", "Not Just the CLI")
        self.add(title)

        cli = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        cli_text = Text("CLI — only works from a terminal", color=PALETTE["slate"], font_size=16, font=BODY_FONT).move_to(cli.get_center())
        self.play(Create(cli), Write(cli_text), run_time=1.0)
        self.wait(0.6)

        api = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        api_text = Text("HTTP endpoint — any real client can call it", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(api.get_center())
        self.play(Create(api), Write(api_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "browser, frontend, another service — same real answer",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_WrappingTheLogic(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Wrapping the Same,", "Already-Verified Logic")
        self.add(title)

        flow = ["GET /patent/{number}", "ClaimsAgent + LineageAgent", "classify=true|false"]
        boxes = VGroup()
        for f in flow:
            b = RoundedRectangle(
                corner_radius=0.1, width=7.5, height=0.85,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(f, color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(b.get_center())
            boxes.add(VGroup(b, label))

        boxes.arrange(DOWN, buff=0.3).shift(UP * 0.2)

        for b in boxes:
            self.play(Create(b[0]), Write(b[1]), run_time=0.8)
            self.wait(0.3)

        bottom = Text(
            "no reimplementation — the same tested agents, called the same way",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealMistake(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Mistake")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        box1_text = Text("git pull: diverged branches, forced update", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 0.2, 0])
        box2_text = Text("fix: reset main, rebase the work branch", color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.6)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        box3 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -1.0, 0])
        box3_text = Text("api.py: staged, not committed — wiped out", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(box3.get_center())
        self.play(Create(box3), Write(box3_text), run_time=1.2)
        self.wait(1.5)


class B04_WhatProtectedIt(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("What Actually", "Protected It")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.12, width=8.5, height=1.6,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.8, 0])
        box_text = Text(
            "same real content still on disk,\noutside git, from testing minutes earlier",
            color=PALETTE["teal"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(1.0)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "recreated, committed immediately, re-verified against 2 real patents",
            color=PALETTE["ink"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B05_TheSecondFind(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("A Second Real Find,", "While Fixing the First")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 0.8, 0])
        box_text = Text(
            "an earlier README update\nnever actually merged into main",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(1.0)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "fixed in the same pass — not left for later",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
