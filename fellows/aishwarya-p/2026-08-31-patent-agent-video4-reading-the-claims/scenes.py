"""
Manim scenes for patent-agent-video4-reading-the-claims
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


class B01_TheRealEvidence(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Evidence", "")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.6,
            fill_color=PALETTE["slate"], fill_opacity=0.06,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        box_text = Text(
            "9 independent claims\nword count: 47 → 303 words",
            color=PALETTE["slate"], font_size=17, font=BODY_FONT, line_spacing=1.3
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(0.8)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        result = Text(
            "no clean line separating broad from narrow",
            color=PALETTE["crimson"], font_size=18, font=BODY_FONT
        ).move_to([0, -0.6, 0])
        self.play(Write(result), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "a real reason to reach for judgment, not a rule",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_TheFirstClassification(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The First Real", "Classification")
        self.add(title)

        stat1 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.2,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([-2.4, 0.8, 0])
        stat1_text = Text("broad", color=PALETTE["teal"], font_size=18, font=BODY_FONT).move_to(stat1.get_center())

        stat2 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.2,
            fill_color=PALETTE["crimson"], fill_opacity=0.1,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([2.4, 0.8, 0])
        stat2_text = Text("offensive", color=PALETTE["crimson"], font_size=18, font=BODY_FONT).move_to(stat2.get_center())

        self.play(Create(stat1), Write(stat1_text), run_time=0.8)
        self.play(Create(stat2), Write(stat2_text), run_time=0.8)
        self.wait(0.8)

        caveat_box = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, -1.0, 0])
        caveat_text = Text(
            "caveat: do the dependent claims narrow this term?",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).move_to(caveat_box.get_center())
        self.play(Create(caveat_box), Write(caveat_text), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "grounded in the claim language, not the word count",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealRefusal(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Refusal", "")
        self.add(title)

        box = RoundedRectangle(
            corner_radius=0.12, width=8.0, height=1.8,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.8, 0])
        box_text = Text(
            'stop_reason: "refusal"\ncategory: "bio"',
            color=PALETTE["crimson"], font_size=18, font=BODY_FONT, line_spacing=1.3
        ).move_to(box.get_center())
        self.play(Create(box), Write(box_text), run_time=1.2)
        self.wait(1.0)

        self.play(box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        subject = Text(
            "plant cell cultures → pharmaceutical compound family",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).move_to([0, -1.0, 0])
        self.play(Write(subject), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "not a bug — a real, structural limit",
            color=PALETTE["slate"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.5)


class B04_HandlingItHonestly(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Handling It", "Honestly")
        self.add(title)

        wrong = Text("✗ route around it", color=PALETTE["crimson"], font_size=17, font=BODY_FONT).move_to([0, 1.4, 0])
        self.play(Write(wrong), run_time=1.0)
        self.wait(0.6)

        right_box = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.6,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.2, 0])
        right_text = Text(
            "catch it, mark \"unclear\",\nname the real reason",
            color=PALETTE["teal"], font_size=17, font=BODY_FONT, line_spacing=1.3
        ).move_to(right_box.get_center())
        self.play(Create(right_box), Write(right_text), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "point back to the raw text — don't invent a reading",
            color=PALETTE["ink"], font_size=16, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B05_BuildingTheAgent(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Building the", "Real Agent")
        self.add(title)

        classes = [
            ("ClaimReading", "claim + multi-dep flag + scope"),
            ("PatentClaimsReading", "the full set, real counts"),
            ("ClaimsAgent", "split → flag → classify"),
        ]

        rows = VGroup()
        for name, desc in classes:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=8.5, height=1.0,
                fill_color=PALETTE["sage"], fill_opacity=0.1,
                stroke_color=PALETTE["sage"], stroke_width=1.5
            )
            name_label = Text(name, color=PALETTE["ink"], font_size=16, font=BODY_FONT)
            desc_label = Text(desc, color=PALETTE["teal"], font_size=13, font=BODY_FONT)
            text_group = VGroup(name_label, desc_label).arrange(RIGHT, buff=0.6).move_to(row_box.get_center())
            rows.add(VGroup(row_box, text_group))

        rows.arrange(DOWN, buff=0.3).shift(UP * 0.1)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=1.0)
            self.wait(0.4)

        bottom = Text(
            "classification is optional — structural reading always free",
            color=PALETTE["ink"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B06_TheEndToEndTest(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real", "End-to-End Test")
        self.add(title)

        patent_label = Text("US-11197952-B2 (cached, free)", color=PALETTE["slate"], font_size=16, font=BODY_FONT).move_to([0, 1.7, 0])
        self.play(Write(patent_label), run_time=0.8)
        self.wait(0.5)

        stat1 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.2,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([-3.0, 0.2, 0])
        stat1_text = Text("17\nclaims", color=PALETTE["ink"], font_size=18, font=BODY_FONT, line_spacing=1.2).move_to(stat1.get_center())

        stat2 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.2,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 0.2, 0])
        stat2_text = Text("1\nindependent", color=PALETTE["teal"], font_size=16, font=BODY_FONT, line_spacing=1.2).move_to(stat2.get_center())

        stat3 = RoundedRectangle(
            corner_radius=0.1, width=2.6, height=1.2,
            fill_color=PALETTE["crimson"], fill_opacity=0.1,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([3.0, 0.2, 0])
        stat3_text = Text("16\ndependent", color=PALETTE["crimson"], font_size=16, font=BODY_FONT, line_spacing=1.2).move_to(stat3.get_center())

        self.play(Create(stat1), Write(stat1_text), run_time=0.8)
        self.play(Create(stat2), Write(stat2_text), run_time=0.8)
        self.play(Create(stat3), Write(stat3_text), run_time=0.8)
        self.wait(0.8)

        self.play(Indicate(VGroup(stat1, stat2, stat3), scale_factor=1.02), run_time=1.0)
        self.wait(0.5)

        bottom = Text(
            "matches the verified count — plus one honest scope reading",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
