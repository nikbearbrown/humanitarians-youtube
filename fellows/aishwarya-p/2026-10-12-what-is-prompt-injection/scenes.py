"""
Manim scenes for what-is-prompt-injection STEM video
B01_DirectVsIndirect      — two real, distinct forms
B02_WhyItsDifferent       — structural difference from SQL injection
B03_TheRealScale          — Cisco 73%, OWASP #1, HiddenLayer 1-in-8
B04_WhyAgentsMakeItWorse  — severity scales with tool access
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


class B01_DirectVsIndirect(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Direct vs.", "Indirect Injection")
        self.add(title)

        direct = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.3,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.2, 0])
        direct_text = Text(
            "direct: user types adversarial\ninstructions into the interface",
            color=PALETTE["slate"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(direct.get_center())
        self.play(Create(direct), Write(direct_text), run_time=1.0)
        self.wait(0.6)

        indirect = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.3, 0])
        indirect_text = Text(
            "indirect: instructions arrive in\nexternal data the model retrieves",
            color=PALETTE["crimson"], font_size=15, font=BODY_FONT, line_spacing=1.3
        ).move_to(indirect.get_center())
        self.play(Create(indirect), Write(indirect_text), run_time=1.0)
        self.wait(1.0)

        self.play(indirect.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "a web page, a doc, an email — no user input needed",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B02_WhyItsDifferent(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why It's Different", "from SQL Injection")
        self.add(title)

        sql = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.2, 0])
        sql_text = Text("SQL: exploits poor input validation in code", color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(sql.get_center())
        self.play(Create(sql), Write(sql_text), run_time=1.0)
        self.wait(0.6)

        prompt = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.1, 0])
        prompt_text = Text("prompt: the model follows instructions by design", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(prompt.get_center())
        self.play(Create(prompt), Write(prompt_text), run_time=1.0)
        self.wait(0.8)

        self.play(prompt.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "no separator between data and instruction —\nit's all text, processed together",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT, line_spacing=1.3
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealScale(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real,", "Current Scale")
        self.add(title)

        stats = [
            ("73%", "of production AI deployments\nhave prompt injection weaknesses (Cisco, 2026)"),
            ("#1", "on OWASP's LLM Top 10 — held\nsince 2023"),
            ("1 in 8", "AI breaches involve autonomous\nagents (HiddenLayer, 2026)"),
        ]
        rows = VGroup()
        for num, desc in stats:
            row_box = RoundedRectangle(
                corner_radius=0.1, width=8.5, height=1.0,
                fill_color=PALETTE["gold"], fill_opacity=0.08,
                stroke_color=PALETTE["gold"], stroke_width=1.5
            )
            num_label = Text(num, color=PALETTE["crimson"], font_size=18, font=BODY_FONT)
            desc_label = Text(desc, color=PALETTE["ink"], font_size=12, font=BODY_FONT, line_spacing=1.2)
            pair = VGroup(num_label, desc_label).arrange(RIGHT, buff=0.5).move_to(row_box.get_center())
            rows.add(VGroup(row_box, pair))

        rows.arrange(DOWN, buff=0.2).shift(UP * 0.1)

        for r in rows:
            self.play(Create(r[0]), Write(r[1]), run_time=0.9)
            self.wait(0.4)

        self.wait(1.5)


class B04_WhyAgentsMakeItWorse(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Why Agents", "Make It Worse")
        self.add(title)

        box1 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        box1_text = Text("model that only talks → changes the response", color=PALETTE["teal"], font_size=15, font=BODY_FONT).move_to(box1.get_center())
        self.play(Create(box1), Write(box1_text), run_time=1.0)
        self.wait(0.6)

        box2 = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.0,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 0.1, 0])
        box2_text = Text("model with tool access → takes the action", color=PALETTE["crimson"], font_size=15, font=BODY_FONT).move_to(box2.get_center())
        self.play(Create(box2), Write(box2_text), run_time=1.0)
        self.wait(0.8)

        self.play(box2.animate.shift(DOWN * 0.1), run_time=0.6)
        self.wait(0.2)

        bottom = Text(
            "email, databases, code execution —\ninjection becomes real-world action",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT, line_spacing=1.3
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)
