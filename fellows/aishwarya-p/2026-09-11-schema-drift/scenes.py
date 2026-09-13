"""
Manim scenes for schema-drift STEM video
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


class B01_WhatItIs(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("What Schema", "Drift Actually Is")
        self.add(title)

        changes = ["field added", "field removed", "field renamed", "meaning quietly shifted"]
        rows = VGroup()
        for c in changes:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=6.5, height=0.8,
                fill_color=PALETTE["teal"], fill_opacity=0.08,
                stroke_color=PALETTE["teal"], stroke_width=1.5
            )
            label = Text(c, color=PALETTE["teal"], font_size=17, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.25).shift(UP * 0.2)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "unplanned — and downstream, nobody's warned first",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_ARealCase(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("A Real,", "Documented Case")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.2,
            fill_color=PALETTE["slate"], fill_opacity=0.06,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        box1_text = Text(
            'a supplier adds "Lot_Batch_Notes"\nto their CSV export',
            color=PALETTE["slate"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.2)
        self.wait(0.8)

        self.play(box1.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.2,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        box2_text = Text(
            "Power BI dashboards:\nkey KPIs → NULL, overnight",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the data wasn't wrong — its shape had changed",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheSamePattern(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Same Pattern,", "One Field Deep")
        self.add(title)

        expected = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        expected_text = Text("check written for: missing = null", color=PALETTE["teal"], font_size=16, font=BODY_FONT).move_to(expected.get_center())
        self.play(Create(expected), Write(expected_text), run_time=1.0)
        self.wait(0.6)

        real = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.1,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        real_text = Text('real system returns: missing = ""', color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(real.get_center())
        self.play(Create(real), Write(real_text), run_time=1.0)
        self.wait(0.8)

        self.play(real.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "same field, same position — the meaning of empty drifted",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_WhyItMatters(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why It Matters", "More Over Time")
        self.add(title)

        stages = ["source A", "source B", "your pipeline", "your dashboard"]
        boxes = VGroup()
        for s in stages:
            b = RoundedRectangle(
                corner_radius=0.1, width=1.9, height=1.0,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(s, color=PALETTE["ink"], font_size=13, font=BODY_FONT).move_to(b.get_center())
            boxes.add(VGroup(b, label))

        boxes.arrange(RIGHT, buff=0.4).shift(UP * 0.6)

        for b in boxes:
            self.play(Create(b[0]), Write(b[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "more hops, more chances one quietly redefines a value",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.9)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
