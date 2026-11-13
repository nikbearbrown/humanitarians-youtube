"""
Manim scenes for patent-agent-video9-building-the-frontend
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


class B01_WhyAFrontend(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why a", "Frontend")
        self.add(title)

        api = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        api_text = Text("API — only works if you know the exact URL + query", color=PALETTE["slate"], font_size=15, font=BODY_FONT).move_to(api.get_center())
        self.play(Create(api), Write(api_text), run_time=1.0)
        self.wait(0.6)

        ui = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        ui_text = Text("one input, one toggle, one button", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(ui.get_center())
        self.play(Create(ui), Write(ui_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "same real claims and lineage data, readable by anyone",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_BuildingAgainstTheRealShape(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Building Against", "the Real Shape")
        self.add(title)

        flow = ["GET classify=false", "GET classify=true", "design the screen from the actual JSON"]
        boxes = VGroup()
        for f in flow:
            b = RoundedRectangle(
                corner_radius=0.1, width=7.5, height=0.85,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(f, color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(b.get_center())
            boxes.add(VGroup(b, label))

        boxes.arrange(DOWN, buff=0.3).shift(UP * 0.2)

        for b in boxes:
            self.play(Create(b[0]), Write(b[1]), run_time=0.8)
            self.wait(0.3)

        bottom = Text(
            "not assumptions — the result view was built after seeing both real responses",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealBug(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Bug")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        box1_text = Text(".env file, with the key, sitting there since day one", color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.2, 0])
        box2_text = Text("no python-dotenv, no load_dotenv() — anywhere", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.6)

        box3 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -1.0, 0])
        box3_text = Text("worked only via manual export — broke every closed terminal", color=PALETTE["crimson"], font_size=14, font=BODY_FONT).move_to(box3.get_center())
        self.play(Create(box3), Write(box3_text), run_time=1.2)
        self.wait(1.5)


class B04_TheRealFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "Fix")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        box1_text = Text("one import: from dotenv import load_dotenv", color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["sage"], fill_opacity=0.1,
            stroke_color=PALETTE["sage"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        box2_text = Text("one call: load_dotenv() at the top of api.py", color=PALETTE["ink"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "key loads from the file itself now — every session, no manual export",
            color=PALETTE["ink"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B05_Handoff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Your", "Turn")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        box1_text = Text("if a project has a .env file —", color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        box2_text = Text("check something actually calls load_dotenv()", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "a config file nobody reads is worse than no config file at all",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
