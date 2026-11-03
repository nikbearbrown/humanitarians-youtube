"""
Manim scenes for patent-agent-video3-real-cost-of-a-query
B01_TheRealError       — the real 403 quota error, explained
B02_TheInvestigation   — wrong assumption vs. real cause
B03_TheRealMath        — $6.25/TiB, ~$0.71/lookup, billing added
B04_TheHonestDeadEnd   — the smaller table, checked and rejected
B05_TheSecondInvestment — the Anthropic API key, real cost, real refusal handling
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
    """Build a genuinely centered two-line title using separate Text
    objects grouped and arranged, avoiding Text()'s internal left-bias
    on multi-line strings."""
    t1 = Text(line1, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    t2 = Text(line2, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    title = VGroup(t1, t2).arrange(DOWN, buff=0.15)
    title.to_edge(UP, buff=0.7)
    title.move_to([0, title.get_y(), 0])
    return title


class B01_TheRealError(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Error", "")
        self.add(title)

        error_box = RoundedRectangle(
            corner_radius=0.12, width=9.0, height=1.8,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.0, 0])
        error_text = Text(
            '403 Forbidden\n"Quota exceeded: free query bytes scanned"',
            color=PALETTE["crimson"], font_size=17, font=BODY_FONT, line_spacing=1.3
        ).move_to(error_box.get_center())
        self.play(Create(error_box), Write(error_text), run_time=1.2)
        self.wait(1.0)

        self.play(error_box.animate.shift(UP * 0.1), run_time=0.6)
        self.wait(0.2)

        stat = Text(
            "1 TiB free per month — then real, billed usage",
            color=PALETTE["ink"], font_size=18, font=BODY_FONT
        ).move_to([0, -0.8, 0])
        self.play(Write(stat), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the free tier was genuinely gone",
            color=PALETTE["slate"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.5)


class B02_TheInvestigation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Investigation", "")
        self.add(title)

        wrong = RoundedRectangle(
            corner_radius=0.1, width=8.0, height=1.1,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, 1.6, 0])
        wrong_text = Text(
            "assumption: LIKE wildcards are the expensive part",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).move_to(wrong.get_center())
        self.play(Create(wrong), Write(wrong_text), run_time=1.0)
        self.wait(0.8)

        x_mark = Text("✗ wrong", color=PALETTE["crimson"], font_size=18, font=BODY_FONT).next_to(wrong, RIGHT, buff=0.3)
        self.play(Write(x_mark), run_time=0.6)
        self.wait(0.6)

        real = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.6,
            fill_color=PALETTE["teal"], fill_opacity=0.08,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.4, 0])
        real_text = Text(
            "exact match: 116.58 GB scanned\nsame query repeated: 0 B (cached)",
            color=PALETTE["teal"], font_size=16, font=BODY_FONT, line_spacing=1.3
        ).move_to(real.get_center())
        self.play(Create(real), Write(real_text), run_time=1.2)
        self.wait(1.0)

        bottom = Text(
            "the table itself: 98M rows, no clustering on the field searched",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B03_TheRealMath(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Real Math", "")
        self.add(title)

        rate = RoundedRectangle(
            corner_radius=0.1, width=6.0, height=1.2,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 1.6, 0])
        rate_text = Text("$6.25 per TiB scanned", color=PALETTE["ink"], font_size=20, font=BODY_FONT).move_to(rate.get_center())
        self.play(Create(rate), Write(rate_text), run_time=1.0)
        self.wait(0.6)

        arrow = Arrow([0, 0.9, 0], [0, 0.3, 0], color=PALETTE["ink"], stroke_width=3)
        self.play(Create(arrow), run_time=0.5)

        cost = RoundedRectangle(
            corner_radius=0.1, width=6.0, height=1.2,
            fill_color=PALETTE["teal"], fill_opacity=0.1,
            stroke_color=PALETTE["teal"], stroke_width=1.5
        ).move_to([0, -0.6, 0])
        cost_text = Text("≈ $0.71 per lookup", color=PALETTE["teal"], font_size=20, font=BODY_FONT).move_to(cost.get_center())
        self.play(Create(cost), Write(cost_text), run_time=1.0)
        self.wait(0.8)

        decision = Text(
            "real money → a real decision: add billing",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).move_to([0, -1.8, 0])
        self.play(Write(decision), run_time=1.2)
        self.wait(1.5)


class B04_TheHonestDeadEnd(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Honest", "Dead End")
        self.add(title)

        promising = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.3,
            fill_color=PALETTE["sage"], fill_opacity=0.1,
            stroke_color=PALETTE["sage"], stroke_width=1.5
        ).move_to([0, 1.4, 0])
        promising_text = Text(
            "patent_claims_fulltext — 29 GB total, dependencies field",
            color=PALETTE["ink"], font_size=15, font=BODY_FONT
        ).move_to(promising.get_center())
        self.play(Create(promising), Write(promising_text), run_time=1.0)
        self.wait(0.8)

        checked = RoundedRectangle(
            corner_radius=0.1, width=8.5, height=1.3,
            fill_color=PALETTE["crimson"], fill_opacity=0.08,
            stroke_color=PALETTE["crimson"], stroke_width=1.5
        ).move_to([0, -0.2, 0])
        checked_text = Text(
            "last updated: 2017 — doesn't cover our patents",
            color=PALETTE["crimson"], font_size=16, font=BODY_FONT
        ).move_to(checked.get_center())
        self.play(Create(checked), Write(checked_text), run_time=1.0)
        self.wait(1.0)

        bottom = Text(
            "a real, honest dead end — not a shortcut",
            color=PALETTE["ink"], font_size=17, font=BODY_FONT
        ).to_edge(DOWN, buff=0.8)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.5)


class B05_TheSecondInvestment(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The Second", "Investment")
        self.add(title)

        api = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.2,
            fill_color=PALETTE["slate"], fill_opacity=0.08,
            stroke_color=PALETTE["slate"], stroke_width=1.5
        ).move_to([0, 1.5, 0])
        api_text = Text("Anthropic API key — real per-token cost", color=PALETTE["slate"], font_size=16, font=BODY_FONT).move_to(api.get_center())
        self.play(Create(api), Write(api_text), run_time=1.0)
        self.wait(0.8)

        refusal = RoundedRectangle(
            corner_radius=0.1, width=7.5, height=1.4,
            fill_color=PALETTE["gold"], fill_opacity=0.1,
            stroke_color=PALETTE["gold"], stroke_width=1.5
        ).move_to([0, 0.0, 0])
        refusal_text = Text(
            'stop_reason: "refusal" — category "bio"',
            color=PALETTE["ink"], font_size=14, font=BODY_FONT
        ).move_to(refusal.get_center())
        self.play(Create(refusal), Write(refusal_text), run_time=1.2)
        self.wait(1.0)

        handled = Text(
            "handled gracefully — marked unclear, not a crash",
            color=PALETTE["teal"], font_size=16, font=BODY_FONT
        ).move_to([0, -1.4, 0])
        self.play(Write(handled), run_time=1.2)
        self.wait(1.5)
