"""
Manim scenes for leverage-cuts-both-ways (ai-explainer, Ch.6 Margin & Short Selling).
Claude fidelity palette: cream #FAF9F5, ink #3D3929, one terracotta #D97757.

All numbers sourced from the Computational Finance Ch.6 cheat sheet and verified:
  $10k cash, 50% Reg T -> $20k position, $10k loan (2:1 leverage)
  -20% stock -> $16k position, $10k loan, $6k equity = -40% on equity
  maintenance 30% -> margin call at portfolio value $14,285.71 (~$14,286)
  long loss capped at -100%; short loss unbounded (conceptual, correct)

Scenes auto-fill to their measured narration length via _fill() so the audio
clock (mp3/timings.json) is the master and no extreme slow-motion is needed.
"""

from manim import *

BG = "#FAF9F5"
INK = "#3D3929"
ACCENT = "#D97757"
MUTE = "#8A8578"
GOOD = "#4A7C59"
BAD = "#C0392B"
LINE = "#B8B0A0"


def _bg(scene):
    scene.camera.background_color = BG


# Measured narration lengths (mp3/timings.json) — set after audio generation.
TARGET = {
    "B01_Leverage": 18.88,
    "B02_CutsBothWays": 18.92,
    "B03_MarginCall": 20.99,
    "B04_ShortSqueeze": 21.21,
    "B05_Verdict": 15.89,
}


def _fill(scene, key, tail=1.0):
    try:
        elapsed = scene.renderer.time
    except Exception:
        elapsed = 0.0
    scene.wait(max(tail, TARGET.get(key, 0.0) - elapsed))


def _dollar(x):
    return f"${x:,.0f}"


class B01_Leverage(Scene):
    """The promise: $10k cash + $10k loan = $20k buying power (2:1)."""

    def construct(self):
        _bg(self)
        title = Text("Margin = Borrowed Buying Power", color=INK,
                     font_size=44, weight="BOLD").to_edge(UP, buff=0.5)
        sub = Text("Regulation T — 50% initial margin", color=INK,
                   font_size=30).next_to(title, DOWN, buff=0.22)
        self.play(FadeIn(title, shift=DOWN * 0.2), Write(sub), run_time=0.8)
        self.wait(2.0)

        def money_box(amount, label, color, w=2.4):
            box = Rectangle(width=w, height=1.5, fill_color=color,
                            fill_opacity=0.22, stroke_color=color, stroke_width=3)
            amt = Text(_dollar(amount), color=INK, font_size=38, weight="BOLD")
            lab = Text(label, color=INK, font_size=26)
            g = VGroup(box, amt.move_to(box.get_center() + UP * 0.18),
                       lab.next_to(box, DOWN, buff=0.18))
            return g, box

        cash_g, cash_b = money_box(10000, "your cash", INK)
        cash_g.move_to([-4.5, 0.5, 0])
        self.play(FadeIn(cash_g, shift=UP * 0.2), run_time=0.7)
        self.wait(2.2)

        plus = Text("+", color=ACCENT, font_size=56, weight="BOLD").move_to([-2.4, 0.65, 0])
        loan_g, loan_b = money_box(10000, "broker's loan", ACCENT)
        loan_g.move_to([0.0, 0.5, 0])
        self.play(Write(plus), FadeIn(loan_g, shift=UP * 0.2), run_time=0.7)
        self.wait(2.4)

        eq = Text("=", color=INK, font_size=56, weight="BOLD").move_to([2.4, 0.65, 0])
        power_g, power_b = money_box(20000, "buying power", GOOD, w=2.7)
        power_g.move_to([4.55, 0.5, 0])
        self.play(Write(eq), FadeIn(power_g, shift=UP * 0.2), run_time=0.7)
        self.wait(2.2)

        lev = Text("2 : 1 leverage", color=ACCENT, font_size=44,
                   weight="BOLD").move_to([0, -1.9, 0])
        gain = Text("stock +10%   →   +20% on your cash", color=GOOD,
                    font_size=34, weight="BOLD").move_to([0, -2.9, 0])
        self.play(Write(lev), run_time=0.6)
        self.wait(1.6)
        self.play(FadeIn(gain, shift=UP * 0.15), run_time=0.6)
        _fill(self, "B01_Leverage")


class B02_CutsBothWays(Scene):
    """The trap: -20% stock = -40% equity, because the loan doesn't shrink."""

    def construct(self):
        _bg(self)
        title = Text("The Loan Doesn't Shrink", color=INK,
                     font_size=54, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.8)

        base_y = -2.5
        scale = 0.00022  # units per dollar (20000 -> 4.4 tall, top at ~1.9)

        def stack(x, value, loan, caption):
            loan_h = loan * scale
            eq_h = max(0.001, (value - loan) * scale)
            loan_rect = Rectangle(width=1.6, height=loan_h, fill_color=MUTE,
                                  fill_opacity=0.55, stroke_width=0)
            loan_rect.move_to([x, base_y + loan_h / 2, 0])
            eq_rect = Rectangle(width=1.6, height=eq_h, fill_color=ACCENT,
                                fill_opacity=0.9, stroke_width=0)
            eq_rect.move_to([x, base_y + loan_h + eq_h / 2, 0])
            cap = Text(caption, color=INK, font_size=26).next_to([x, base_y, 0], DOWN, buff=0.2)
            return VGroup(loan_rect, eq_rect, cap), eq_rect

        before, eq_b = stack(-3.3, 20000, 10000, "before")
        after, eq_a = stack(1.3, 16000, 10000, "after −20%")

        legend = VGroup(
            VGroup(Square(0.3, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0),
                   Text("your equity", color=INK, font_size=24)).arrange(RIGHT, buff=0.2),
            VGroup(Square(0.3, fill_color=MUTE, fill_opacity=0.55, stroke_width=0),
                   Text("the loan", color=INK, font_size=24)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to([4.5, 0.9, 0])

        self.play(FadeIn(before, shift=UP * 0.2), FadeIn(legend), run_time=0.8)
        e1 = Text("$10,000", color=ACCENT, font_size=28, weight="BOLD").next_to(eq_b, UP, buff=0.15)
        self.play(Write(e1), run_time=0.4)
        self.wait(2.6)

        self.play(FadeIn(after, shift=UP * 0.2), run_time=0.8)
        e2 = Text("$6,000", color=BAD, font_size=28, weight="BOLD").next_to(eq_a, UP, buff=0.15)
        self.play(Write(e2), run_time=0.4)
        self.wait(2.6)

        punch = Text("stock −20%   →   your equity −40%", color=BAD,
                     font_size=40, weight="BOLD").move_to([0, -3.15, 0])
        self.play(Write(punch), run_time=0.7)
        _fill(self, "B02_CutsBothWays")


class B03_MarginCall(Scene):
    """The forced exit: maintenance 30% -> margin call at $14,286 value."""

    def construct(self):
        _bg(self)
        title = Text("You Don't Control the Exit", color=INK,
                     font_size=54, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.8)

        ax_l, ax_r = -5.2, 3.2
        top, bot = 1.9, -2.6
        axis = Line([ax_l, bot, 0], [ax_r, bot, 0], color=LINE, stroke_width=3)
        yaxis = Line([ax_l, bot, 0], [ax_l, top + 0.3, 0], color=LINE, stroke_width=3)
        self.play(Create(axis), Create(yaxis), run_time=0.5)

        # falling portfolio-value curve
        pts = [[ax_l, top, 0], [-3.0, 1.1, 0], [-1.2, 0.2, 0],
               [0.4, -0.7, 0], [1.8, -1.5, 0], [ax_r, -2.0, 0]]
        curve = VMobject(color=INK, stroke_width=5).set_points_as_corners(pts)
        self.play(Create(curve), run_time=1.6)
        self.wait(1.2)

        # margin readout falling
        for i, (val, x, y) in enumerate([("margin 50%", -4.6, top),
                                         ("37.5%", -1.2, 0.2)]):
            t = Text(val, color=INK if i == 0 else MUTE, font_size=26).move_to([x, y + 0.5, 0])
            self.play(FadeIn(t), run_time=0.4)
            self.wait(1.6)

        # maintenance line
        m_y = -1.5
        m_line = DashedLine([ax_l, m_y, 0], [ax_r, m_y, 0], color=BAD,
                            stroke_width=3, dash_length=0.15)
        m_lab = Text("maintenance margin 30%", color=BAD, font_size=26).next_to(
            [ax_r, m_y, 0], UP, buff=0.1).align_to([ax_r, m_y, 0], RIGHT)
        self.play(Create(m_line), Write(m_lab), run_time=0.7)
        self.wait(2.0)

        # the call fires
        call_pt = [1.8, -1.5, 0]
        dot = Dot(call_pt, color=BAD, radius=0.14)
        call = Text("MARGIN CALL", color=BAD, font_size=40, weight="BOLD").move_to([1.4, -0.55, 0])
        val = Text("forced sale at $14,286", color=INK, font_size=30,
                   weight="BOLD").move_to([0, -3.4, 0])
        self.play(FadeIn(dot, scale=1.5), Write(call), run_time=0.7)
        self.wait(1.6)
        self.play(Write(val), run_time=0.6)
        _fill(self, "B03_MarginCall")


class B04_ShortSqueeze(Scene):
    """Short selling: long loss capped at -100%, short loss unbounded."""

    def construct(self):
        _bg(self)
        title = Text("Short Selling Has No Floor", color=INK,
                     font_size=48, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(2.0)

        base_y = 1.5
        # LONG: capped at -100%
        long_lab = Text("BUY a stock", color=INK, font_size=32, weight="BOLD").move_to([-3.5, base_y + 0.5, 0])
        long_bar = Rectangle(width=2.0, height=1.3, fill_color=MUTE, fill_opacity=0.6,
                             stroke_width=0).move_to([-3.5, base_y - 0.85, 0])
        long_cap = Text("worst case −100%", color=INK, font_size=26).next_to(long_bar, DOWN, buff=0.2)
        floor = Text("can only reach zero", color=MUTE, font_size=24).next_to(long_cap, DOWN, buff=0.15)
        self.play(Write(long_lab), GrowFromEdge(long_bar, UP), run_time=0.7)
        self.play(FadeIn(long_cap), FadeIn(floor), run_time=0.5)
        self.wait(2.6)

        # SHORT: unbounded
        short_lab = Text("SHORT a stock", color=ACCENT, font_size=32, weight="BOLD").move_to([3.3, base_y + 0.5, 0])
        short_bar = Rectangle(width=2.0, height=3.2, fill_color=BAD, fill_opacity=0.85,
                              stroke_width=0).move_to([3.3, base_y - 1.8, 0])
        self.play(Write(short_lab), GrowFromEdge(short_bar, UP), run_time=0.8)
        arrow = Arrow([3.3, base_y - 0.1, 0], [3.3, 3.0, 0],
                      color=BAD, stroke_width=8, buff=0.0, max_tip_length_to_length_ratio=0.12)
        unl = Text("past −100% — no limit", color=BAD, font_size=26,
                   weight="BOLD").next_to(short_bar, DOWN, buff=0.2)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(unl), run_time=0.5)
        self.wait(2.4)

        punch = Text("The price can rise forever.", color=INK,
                     font_size=38, weight="BOLD").move_to([0, -3.2, 0])
        self.play(Write(punch), run_time=0.7)
        _fill(self, "B04_ShortSqueeze")


class B05_Verdict(Scene):
    """The verdict: a multiplier, not a strategy."""

    def construct(self):
        _bg(self)
        title = Text("The Verdict", color=INK, font_size=72, weight="BOLD").to_edge(UP, buff=0.45)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(1.4)

        rows = [
            "amplifies your gains",
            "amplifies your losses",
            "hands the broker your exit",
        ]
        items = VGroup()
        for r in rows:
            bullet = Square(side_length=0.54, fill_color=ACCENT, fill_opacity=1.0,
                            stroke_width=0).rotate(PI / 4)
            t = Text(r, color=INK, font_size=60)
            items.add(VGroup(bullet, t).arrange(RIGHT, buff=0.55))
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.95).move_to([0, 0.5, 0])
        for it in items:
            self.play(GrowFromCenter(it[0]), FadeIn(it[1], shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.6)

        punch = Text("A multiplier, not a strategy.", color=ACCENT,
                     font_size=60, weight="BOLD").move_to([0, -3.05, 0])
        self.play(Write(punch), run_time=0.8)
        _fill(self, "B05_Verdict")
