"""
Manim scenes for patent-agent-video5-broadening-the-test
B01_TheRealGap        — the "1." vs "1 ." formatting difference
B02_TracingTheFix     — the real fix, verified both ways
B03_TheRealResults    — 8 claims, 4 domains, zero refusals
B04_TheOpenQuestion   — the honest "always narrow/defensive" pattern
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


class B01_TheRealGap(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Gap", "")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=6.0, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        box1_text = Text('"1." — matches', color=PALETTE["teal"], font_size=17, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=6.0, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.1,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        box2_text = Text('"1 ." — silently missed', color=PALETTE["crimson"], font_size=17, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.8)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "one space, one silent failure — 0 of 14 real claims parsed",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_TracingTheFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Tracing the", "Fix")
        self.add(title)

        fix_box = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 1.2, 0])
        fix_text = Text(
            'allow optional whitespace between digits and period',
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).move_to(fix_box.get_center())
        self.play(Create(fix_box), Write(fix_text), run_time=1.2)
        self.wait(0.8)

        check1 = Text("✓ new format: 14/14 claims", color=PALETTE["teal"], font_size=17, font=BODY_FONT).move_to([0, -0.4, 0])
        self.play(Write(check1), run_time=1.0)
        self.wait(0.5)

        check2 = Text("✓ original format: still correct", color=PALETTE["teal"], font_size=17, font=BODY_FONT).move_to([0, -1.2, 0])
        self.play(Write(check2), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "verified both ways before trusting it",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealResults(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Results", "")
        self.add(title)

        domains = ["semiconductor", "mechanical", "robotics", "medical device"]
        rows = VGroup()
        for d in domains:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=6.0, height=0.8,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            label = Text(d, color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.25).shift(UP * 0.3)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.7)
            self.wait(0.3)

        bottom = Text(
            "8 independent claims, zero refusals on this batch",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_TheOpenQuestion(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Honest", "Open Question")
        self.add(title)

        stat_box = RoundedRectangle(
            corner_radius=0.1, width=6.5, height=1.4,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.2, 0])
        stat_text = Text(
            "8 of 8 readings: narrow / defensive",
            color=PALETTE["crimson"], font_size=18, font=BODY_FONT
        ).move_to(stat_box.get_center())
        self.play(Create(stat_box), Write(stat_text), run_time=1.2)
        self.wait(1.0)

        self.play(stat_box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        q1 = Text("real pattern in the patents?", color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to([0, -0.2, 0])
        self.play(Write(q1), run_time=1.0)
        self.wait(0.5)

        q2 = Text("or a bias toward the safer answer?", color=PALETTE["ink"], font_size=16, font=BODY_FONT).move_to([0, -0.9, 0])
        self.play(Write(q2), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "not concluded — flagged, and left open",
            color=PALETTE["slate"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
