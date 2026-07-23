import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_BudgetBars(Scene):
    def construct(self):
        # ── palette ──────────────────────────────────────────────────────
        bg = Rectangle(width=16, height=9, fill_color=CREAM,
                        fill_opacity=1, stroke_width=0, stroke_opacity=0)
        self.add(bg)

        # ── title ─────────────────────────────────────────────────────────
        title = Text("BUDGET STRESS TEST", color=INK, weight=BOLD, font_size=40)
        title.move_to([0, 3.2, 0])

        # ── axes ─────────────────────────────────────────────────────────
        y_axis = Line([-5.0, -2.5, 0], [-5.0, 2.5, 0], color=INK, stroke_width=2)
        x_axis = Line([-5.0, -2.5, 0], [5.0, -2.5, 0], color=INK, stroke_width=2)

        # ── y-tick labels with CREAM background ───────────────────────────
        def make_label_with_bg(text_str, pos, color=INK, font_size=22):
            lbl = Text(text_str, color=color, font_size=font_size)
            lbl.move_to(pos)
            bg_rect = Rectangle(
                width=lbl.width + 0.1,
                height=lbl.height + 0.05,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bg_rect.move_to(pos)
            return VGroup(bg_rect, lbl)

        y_label_0   = make_label_with_bg("$0",   [-5.4, -2.5, 0])
        y_label_125 = make_label_with_bg("$125", [-5.4,  0.0, 0])
        y_label_250 = make_label_with_bg("$250", [-5.4,  2.5, 0])
        y_tick_labels = VGroup(y_label_0, y_label_125, y_label_250)

        # ── category labels BELOW x-axis ────────────────────────────────
        cat_restaurants = make_label_with_bg("Restaurants", [-3.5, -2.9, 0])
        cat_phone       = make_label_with_bg("Phone",       [ 0.0, -2.9, 0])
        cat_gas         = make_label_with_bg("Gas",         [ 3.5, -2.9, 0])
        cat_labels = VGroup(cat_restaurants, cat_phone, cat_gas)

        # ── bars (all stroke_width=0, stroke_opacity=0) ────────────────
        # Coordinate mapping: y_plot = -2.5 + (amount/250)*5.0
        # height = (amount/250)*5.0
        # center_y = -2.5 + height/2

        def make_bar(amount, x_center, color):
            height = (amount / 250.0) * 5.0
            center_y = -2.5 + height / 2.0
            bar = Rectangle(
                width=0.9, height=height,
                fill_color=color, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bar.move_to([x_center, center_y, 0])
            return bar

        # Restaurants: before x=-4.05, after x=-2.95
        bar_rest_before = make_bar(100, -4.05, PASS_CLR)
        bar_rest_after  = make_bar(120, -2.95, CRIMSON)
        # Phone: before x=-0.55, after x=0.55
        bar_phone_before = make_bar(120, -0.55, PASS_CLR)
        bar_phone_after  = make_bar(144,  0.55, CRIMSON)
        # Gas: before x=2.95, after x=4.05
        bar_gas_before = make_bar(200, 2.95, PASS_CLR)
        bar_gas_after  = make_bar(240, 4.05, CRIMSON)

        before_bars = [bar_rest_before, bar_phone_before, bar_gas_before]
        after_bars  = [bar_rest_after,  bar_phone_after,  bar_gas_after]

        # ── amount labels above each bar ────────────────────────────────
        # label pos = bar top + 0.25
        # bar top = center_y + height/2

        def bar_top(amount):
            height = (amount / 250.0) * 5.0
            center_y = -2.5 + height / 2.0
            return center_y + height / 2.0

        lbl_rest_before  = make_label_with_bg("$100", [-4.05, bar_top(100) + 0.25, 0])
        lbl_rest_after   = make_label_with_bg("$120", [-2.95, bar_top(120) + 0.25, 0], color=CRIMSON)
        lbl_phone_before = make_label_with_bg("$120", [-0.55, bar_top(120) + 0.25, 0])
        lbl_phone_after  = make_label_with_bg("$144", [ 0.55, bar_top(144) + 0.25, 0], color=CRIMSON)
        lbl_gas_before   = make_label_with_bg("$200", [ 2.95, bar_top(200) + 0.25, 0])
        lbl_gas_after    = make_label_with_bg("$240", [ 4.05, bar_top(240) + 0.25, 0], color=CRIMSON)

        before_amount_labels = [lbl_rest_before,  lbl_phone_before, lbl_gas_before]
        after_amount_labels  = [lbl_rest_after,   lbl_phone_after,  lbl_gas_after]

        # ── legend (top-right) ───────────────────────────────────────────
        leg_box_before = Rectangle(width=0.4, height=0.25,
                                    fill_color=PASS_CLR, fill_opacity=1,
                                    stroke_width=0, stroke_opacity=0)
        leg_txt_before = Text("Baseline", color=INK, font_size=22)
        leg_row_before = VGroup(leg_box_before, leg_txt_before).arrange(RIGHT, buff=0.15)
        leg_row_before.move_to([0.5, 2.85, 0])

        leg_box_after = Rectangle(width=0.4, height=0.25,
                                   fill_color=CRIMSON, fill_opacity=1,
                                   stroke_width=0, stroke_opacity=0)
        leg_txt_after = Text("+20% Stressed", color=CRIMSON, font_size=22)
        leg_row_after = VGroup(leg_box_after, leg_txt_after).arrange(RIGHT, buff=0.15)
        leg_row_after.move_to([0.5, 2.55, 0])

        before_legend = leg_row_before
        after_legend  = leg_row_after

        # ── deficit text at y=-3.2 ────────────────────────────────────────
        deficit_str = "Stress test deficit: -$190"
        deficit_lbl = Text(deficit_str, color=CRIMSON, weight=BOLD, font_size=32)
        deficit_lbl.move_to([0, -3.2, 0])
        deficit_bg = Rectangle(
            width=deficit_lbl.width + 0.2,
            height=deficit_lbl.height + 0.1,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        )
        deficit_bg.move_to([0, -3.2, 0])
        deficit_text = VGroup(deficit_bg, deficit_lbl)

        # ── 7 play() calls ────────────────────────────────────────────────
        # 1. title
        self.play(Write(title))
        # 2. axes + tick labels + category labels
        self.play(
            FadeIn(y_axis), FadeIn(x_axis),
            FadeIn(y_tick_labels), FadeIn(cat_labels)
        )
        # 3. baseline bars grow from bottom
        self.play(*[GrowFromEdge(b, DOWN) for b in before_bars])
        # 4. baseline legend + baseline amount labels
        self.play(
            Write(before_legend),
            *[Write(lbl) for lbl in before_amount_labels]
        )
        # 5. stressed bars grow from bottom
        self.play(*[GrowFromEdge(b, DOWN) for b in after_bars])
        # 6. stressed legend + stressed amount labels
        self.play(
            Write(after_legend),
            *[Write(lbl) for lbl in after_amount_labels]
        )
        # 7. deficit text
        self.play(Write(deficit_text))
