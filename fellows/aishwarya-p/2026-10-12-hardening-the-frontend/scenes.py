"""
Manim scenes for patent-agent-video10-hardening-the-frontend
B01_DistinctErrorStates  — 404 / 500 / network, three real messages
B02_RealLoadingStates    — spinner, contextual hint, disabled inputs
B03_OneMoreHonestChange  — classify defaults to false
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


class B01_DistinctErrorStates(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Distinct", "Error States")
        self.add(title)

        errors = [
            ("404", "wrong format — check the publication number"),
            ("500", "server crash — likely the API key"),
            ("network", "backend not running — check port 8000"),
        ]
        rows = VGroup()
        for code, msg in errors:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=8.0, height=0.85,
                fill_color=PALETTE["crimson"], fill_opacity=0.07,
                stroke_color=PALETTE["crimson"], stroke_width=1.5
            )
            code_label = Text(code, color=PALETTE["crimson"], font_size=16, font=BODY_FONT)
            msg_label = Text(msg, color=PALETTE["ink"], font_size=13, font=BODY_FONT)
            pair = VGroup(code_label, msg_label).arrange(RIGHT, buff=0.5).move_to(row_box.get_center())
            rows.add(VGroup(row_box, pair))

        rows.arrange(DOWN, buff=0.25).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.9)
            self.wait(0.4)

        bottom = Text(
            "three real failures — three genuinely different messages",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_RealLoadingStates(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Real", "Loading States")
        self.add(title)

        improvements = [
            "visible spinner on the button",
            "contextual hint: why it's slow",
            "inputs disabled mid-fetch",
        ]
        rows = VGroup()
        for imp in improvements:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=7.0, height=0.8,
                fill_color=PALETTE["teal"], fill_opacity=0.08,
                stroke_color=PALETTE["teal"], stroke_width=1.5
            )
            label = Text(imp, color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.25).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.8)
            self.wait(0.3)

        bottom = Text(
            "BigQuery + Claude API call — several real seconds",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_OneMoreHonestChange(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("One More", "Honest Change")
        self.add(title)

        before = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.07,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        before_text = Text("before: classify=true by default\n(silent real cost every request)", color=PALETTE["crimson"], font_size=15, font=BODY_FONT, line_spacing=1.3).move_to(before.get_center())
        self.play(Create(before), Write(before_text), run_time=1.0)
        self.wait(0.8)

        after = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["sage"], fill_opacity=0.1,
            stroke_color=PALETTE["sage"], stroke_width=1.5
        ).move_to([0, -0.2, 0])
        after_text = Text("now: classify=false by default\n(free path unless you opt in)", color=PALETTE["teal"], font_size=15, font=BODY_FONT, line_spacing=1.3).move_to(after.get_center())
        self.play(Create(after), Write(after_text), run_time=1.0)
        self.wait(1.0)

        self.play(after.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "classification is one checkbox away — but deliberate now",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
