"""
Manim scenes for mycroft-credit-rating
B04_RatingSweep    — scoreToRating() boundary table swept across a number line
B07_AdditiveMerge  — the 14 untouched original keys beside the new camelCaseReport

Both use the real values from Humanitariansai/Mycroft PR #16:
  n8n_Workflows/Risk_Management_Agent/format-report.js (scoreToRating, formatReport)
  n8n_Workflows/Risk_Management_Agent/test-format-report.js (RATING_CASES, ORIGINAL_KEYS, CAMEL_KEYS)
"""

from manim import *

# nbb teardown palette (brands/nbb.md) — red is the ONE accent.
PALETTE = {
    "bg":     "#FFFFFF",
    "ink":    "#2A1A0E",
    "crimson": "#C8102E",
    "slate":  "#545454",
    "gold":   "#F6D8DC",
    "hair":   "#D4D4D4",
}

# (floor score, rating, band start, band end) — literal RATING_CASES boundaries
BANDS = [
    (0,   "AAA", 0,   10),
    (10,  "AA",  10,  20),
    (20,  "A",   20,  30),
    (30,  "BBB", 30,  40),
    (40,  "BB",  40,  55),
    (55,  "B",   55,  70),
    (70,  "CCC", 70,  85),
    (85,  "CC",  85,  100),
    (100, "D",   100, 150),
]

# the exact snap points read in B04's narration
SWEEP_POINTS = [9, 10, 20, 30, 40, 55, 70, 85, 100]

MAX_SCORE = 150


def _band_color(i, n):
    # good/kept stays plain ink (deepening toward the worst tier);
    # only the final (worst) band gets the one crimson accent.
    if i == n - 1:
        return PALETTE["crimson"]
    t = i / (n - 1)
    return interpolate_color(ManimColor(PALETTE["ink"]), ManimColor(PALETTE["slate"]), t)


class B04_RatingSweep(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("scoreToRating() — the boundary table", color=PALETTE["ink"], font_size=40
                      ).to_edge(UP, buff=0.45)
        sub = Text("test-format-report.js — RATING_CASES", color=PALETTE["slate"], font_size=22
                    ).next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        line_y = -0.2
        left_x, right_x = -6.4, 6.4
        line_w = right_x - left_x

        def x_of(score):
            return left_x + line_w * (min(score, MAX_SCORE) / MAX_SCORE)

        axis = Line([left_x, line_y, 0], [right_x, line_y, 0], color=PALETTE["hair"], stroke_width=3)
        self.play(Create(axis), run_time=0.4)

        band_mobs = VGroup()
        for i, (_lo, rating, start, end) in enumerate(BANDS):
            x0, x1 = x_of(start), x_of(end)
            seg = Line([x0, line_y, 0], [x1, line_y, 0],
                       color=_band_color(i, len(BANDS)), stroke_width=16)
            band_mobs.add(seg)
        self.play(*[Create(s) for s in band_mobs], run_time=1.0)

        band_labels = VGroup()
        for i, (_lo, rating, start, end) in enumerate(BANDS):
            xm = (x_of(start) + x_of(end)) / 2
            lbl = Text(rating, color=_band_color(i, len(BANDS)), font_size=24
                        ).move_to([xm, line_y + 0.55, 0])
            band_labels.add(lbl)
        self.play(*[FadeIn(l, shift=UP * 0.1) for l in band_labels], run_time=0.7)

        ticks = VGroup()
        tick_labels = VGroup()
        for t in (0, 50, 100, 150):
            x = x_of(t)
            tick = Line([x, line_y - 0.12, 0], [x, line_y - 0.32, 0], color=PALETTE["slate"], stroke_width=2)
            lbl = Text(str(t), color=PALETTE["slate"], font_size=18).next_to(tick, DOWN, buff=0.08)
            ticks.add(tick)
            tick_labels.add(lbl)
        self.play(Create(ticks), FadeIn(tick_labels), run_time=0.5)

        marker = Dot(point=[x_of(0), line_y, 0], color=PALETTE["ink"], radius=0.13)
        readout = Text("score 0 → AAA", color=PALETTE["ink"], font_size=34
                        ).next_to(axis, DOWN, buff=1.15)
        self.play(FadeIn(marker), Write(readout), run_time=0.4)

        def rating_for(score):
            for lo, rating, start, end in reversed(BANDS):
                if score >= start:
                    return rating
            return "AAA"

        for score in SWEEP_POINTS:
            rating = rating_for(score)
            band_i = BANDS.index(next(b for b in BANDS if b[1] == rating))
            new_readout = Text(f"score {score} → {rating}",
                                color=_band_color(band_i, len(BANDS)),
                                font_size=34).move_to(readout)
            self.play(
                marker.animate.move_to([x_of(score), line_y, 0]),
                Transform(readout, new_readout),
                run_time=0.9,
            )
            self.wait(0.25)

        note = Text("nine tiers, checked top-down from 100", color=PALETTE["slate"], font_size=20
                     ).next_to(readout, DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.6)

        self.wait(1.8)


ORIGINAL_KEYS = [
    "timestamp", "ticker", "risk_score", "alert_level", "current_price",
    "position_value", "unrealized_pl", "risk_factors", "action", "urgency",
    "position_percent", "stop_loss_price", "volatility", "ai_analysis",
]

CAMEL_KEYS = [
    "timestamp", "ticker", "riskScore", "alertLevel", "currentPrice",
    "positionValue", "unrealizedPl", "riskFactors", "action", "urgency",
    "positionPercent", "stopLossPrice", "volatility", "aiAnalysis", "creditRating",
]

EXAMPLE_SCORE = 90
EXAMPLE_RATING = "CC"  # scoreToRating(90) — matches the B04 sweep


class B07_AdditiveMerge(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = Text("formatReport() — additive, not replaced", color=PALETTE["ink"], font_size=36
                      ).to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.9)

        left_cx, right_cx = -3.9, 3.9
        box_top, box_bottom = 2.55, -3.15
        box_h = box_top - box_bottom
        box_w = 5.6

        left_header = Text("original — 14 keys", color=PALETTE["ink"], font_size=22
                            ).move_to([left_cx, box_top + 0.35, 0])
        right_header = Text("camelCaseReport — 15 keys", color=PALETTE["crimson"], font_size=22
                             ).move_to([right_cx, box_top + 0.35, 0])
        self.play(Write(left_header), Write(right_header), run_time=0.7)

        left_box = Rectangle(width=box_w, height=box_h, stroke_color=PALETTE["hair"], stroke_width=2
                              ).move_to([left_cx, (box_top + box_bottom) / 2, 0])
        right_box = Rectangle(width=box_w, height=box_h, stroke_color=PALETTE["crimson"], stroke_width=2
                               ).move_to([right_cx, (box_top + box_bottom) / 2, 0])
        self.play(Create(left_box), Create(right_box), run_time=0.7)

        arrow = Text("≡", color=PALETTE["slate"], font_size=44).move_to([0, (box_top + box_bottom) / 2, 0])
        self.play(FadeIn(arrow), run_time=0.4)

        left_rows = VGroup()
        top_y = box_top - 0.55
        bottom_y = box_bottom + 0.35
        step = (top_y - bottom_y) / (len(ORIGINAL_KEYS) - 1)
        for i, k in enumerate(ORIGINAL_KEYS):
            t = Text(k, color=PALETTE["ink"], font_size=20
                      ).move_to([left_cx, top_y - i * step, 0])
            left_rows.add(t)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.1) for t in left_rows], lag_ratio=0.12), run_time=2.8)
        untouched = Text("untouched", color=PALETTE["ink"], font_size=20
                          ).next_to(left_box, DOWN, buff=0.3)
        self.play(Write(untouched), run_time=0.6)

        right_rows = VGroup()
        step_r = (top_y - bottom_y) / (len(CAMEL_KEYS) - 1)
        for i, k in enumerate(CAMEL_KEYS):
            color = PALETTE["crimson"] if k == "creditRating" else PALETTE["ink"]
            t = Text(k, color=color, font_size=20
                      ).move_to([right_cx, top_y - i * step_r, 0])
            right_rows.add(t)

        body_rows = right_rows[:-1]
        credit_row = right_rows[-1]
        self.play(LaggedStart(*[FadeIn(t, shift=LEFT * 0.1) for t in body_rows], lag_ratio=0.12), run_time=3.0)

        example = Text(f"score {EXAMPLE_SCORE} → creditRating: \"{EXAMPLE_RATING}\"",
                        color=PALETTE["crimson"], font_size=22
                        ).next_to(right_box, DOWN, buff=0.3)
        self.play(FadeIn(credit_row, scale=1.3), Write(example), run_time=1.1)

        verdict = Text("14 keys unchanged · 15 camelCase keys · rating correct",
                        color=PALETTE["ink"], font_size=22
                        ).to_edge(DOWN, buff=0.3)
        self.play(Write(verdict), run_time=1.0)

        self.wait(3.5)
