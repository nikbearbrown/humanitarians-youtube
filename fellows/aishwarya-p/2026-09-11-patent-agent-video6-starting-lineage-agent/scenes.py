"""
Manim scenes for patent-agent-video6-starting-lineage-agent
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


class B01_CheckingTheSchema(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Checking the", "Schema")
        self.add(title)

        fields = ["publication_number", "npl_text", "type", "category", "filing_date"]
        rows = VGroup()
        for f in fields:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=6.0, height=0.7,
                fill_color=PALETTE["teal"], fill_opacity=0.08,
                stroke_color=PALETTE["teal"], stroke_width=1.5
            )
            label = Text(f, color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(row_box.get_center())
            rows.add(VGroup(row_box, label))

        rows.arrange(DOWN, buff=0.2).shift(UP * 0.3)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.6)
            self.wait(0.2)

        bottom = Text(
            "free to check — no query cost for a schema",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_ScopingItHonestly(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Scoping It", "Honestly")
        self.add(title)

        backward = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.4,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.3, 0])
        backward_text = Text(
            "backward — what this patent cites\n(already on the row — cheap)",
            color=PALETTE["teal"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(backward.get_center())
        self.play(Create(backward), Write(backward_text), run_time=1.2)
        self.wait(0.8)

        forward = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.4,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.5, 0])
        forward_text = Text(
            "forward — who cites this patent\n(a different, untested query)",
            color=PALETTE["crimson"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(forward.get_center())
        self.play(Create(forward), Write(forward_text), run_time=1.2)
        self.wait(0.8)

        self.play(forward.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "backward first — deferred what's untested",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealBug(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Bug", "")
        self.add(title)

        wrong = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        wrong_text = Text(
            'checked: npl_text is not None',
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).move_to(wrong.get_center())
        self.play(Create(wrong), Write(wrong_text), run_time=1.0)
        self.wait(0.6)

        real = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, -0.2, 0])
        real_text = Text(
            "real value when missing:\nan empty string, never None",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(real.get_center())
        self.play(Create(real), Write(real_text), run_time=1.2)
        self.wait(1.0)

        self.play(real.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "the check silently never fired as intended",
            color=PALETTE["slate"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B04_VerifyingTheFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Verifying the", "Fix")
        self.add(title)

        before = RoundedRectangle(
            corner_radius=0.1, width=6.5, height=1.0,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.5, 0])
        before_text = Text("before fix: 1 patent, 11 papers", color=PALETTE["slate"], font_size=15, font=BODY_FONT).move_to(before.get_center())
        self.play(Create(before), Write(before_text), run_time=1.0)
        self.wait(0.6)

        after = RoundedRectangle(
            corner_radius=0.1, width=6.5, height=1.0,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.2, 0])
        after_text = Text("after fix: 1 patent, 11 papers", color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(after.get_center())
        self.play(Create(after), Write(after_text), run_time=1.0)
        self.wait(0.8)

        self.play(after.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        verified = Text(
            "verified by hand: genuinely correct both times",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).move_to([0, -1.3, 0])
        self.play(Write(verified), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "same answer — but only one was actually checked",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
