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


class B04_WACCSensitivity(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        AMBER="#E8A020"

        # Pre-computed histogram data
        wacc_bins = [7.6, 7.9, 8.2, 8.5, 8.8, 9.1, 9.4]
        wacc_counts = [300, 900, 1800, 2800, 2400, 1400, 400]
        ev_bins = [1600, 1800, 2000, 2200, 2400, 2600, 2800]
        ev_counts = [200, 700, 1700, 2800, 2600, 1500, 500]

        max_count = 2800
        bar_max_h = 3.0
        bar_w = 0.55

        def count_to_h(c):
            return c / max_count * bar_max_h

        # Left panel bounds
        lx0 = -5.5; lx1 = -0.5; ly_base = -2.0
        # Right panel bounds
        rx0 = 0.5; rx1 = 5.5; ry_base = -2.0

        # x positions for left bars (7 bars across [lx0+0.5, lx1-0.5])
        lx_span = lx1 - lx0 - 1.0  # 4.5
        lx_step = lx_span / 6  # 0.75
        lx_centers = [lx0 + 0.5 + i * lx_step for i in range(7)]

        # x positions for right bars
        rx_span = rx1 - rx0 - 1.0  # 4.5
        rx_step = rx_span / 6
        rx_centers = [rx0 + 0.5 + i * rx_step for i in range(7)]

        title = Text(
            "8.3% WACC Is Not 8.3% Enterprise Value",
            font="Georgia", font_size=21, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Left panel axes
        left_xaxis = Line([lx0, ly_base, 0], [lx1, ly_base, 0],
                          stroke_width=2, color=ManimColor(SLATE))
        left_yaxis = Line([lx0, ly_base, 0], [lx0, ly_base + bar_max_h + 0.3, 0],
                          stroke_width=2, color=ManimColor(SLATE))
        left_title_bg = Rectangle(
            width=3.2, height=0.32,
            fill_color=ManimColor(CREAM), fill_opacity=1.0,
            stroke_width=0, stroke_opacity=0
        ).move_to([-3.0, ly_base + bar_max_h + 0.55, 0])
        left_title = Text("WACC Distribution", font="Georgia", font_size=18,
                          color=ManimColor(INK)).move_to([-3.0, ly_base + bar_max_h + 0.55, 0])

        # Right panel axes
        right_xaxis = Line([rx0, ry_base, 0], [rx1, ry_base, 0],
                           stroke_width=2, color=ManimColor(SLATE))
        right_yaxis = Line([rx0, ry_base, 0], [rx0, ry_base + bar_max_h + 0.3, 0],
                           stroke_width=2, color=ManimColor(SLATE))
        right_title_bg = Rectangle(
            width=3.6, height=0.32,
            fill_color=ManimColor(CREAM), fill_opacity=1.0,
            stroke_width=0, stroke_opacity=0
        ).move_to([3.0, ry_base + bar_max_h + 0.55, 0])
        right_title = Text("Enterprise Value Distribution", font="Georgia", font_size=18,
                           color=ManimColor(INK)).move_to([3.0, ry_base + bar_max_h + 0.55, 0])

        # Dividing line — ends at y=-2.4 so verdict band is clear
        divider = Line([0, -2.4, 0], [0, 2.8, 0], stroke_width=1, color=ManimColor(SLATE))

        left_axes = VGroup(left_xaxis, left_yaxis, left_title_bg, left_title)
        right_axes = VGroup(right_xaxis, right_yaxis, right_title_bg, right_title)

        # Build left bars
        left_bars = VGroup()
        for i, (cnt, cx) in enumerate(zip(wacc_counts, lx_centers)):
            h = count_to_h(cnt)
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=ManimColor(CRIMSON), fill_opacity=0.75,
                stroke_width=0, stroke_opacity=0
            )
            bar.move_to([cx, ly_base + h / 2, 0])
            # x tick label
            bg = Rectangle(
                width=0.45, height=0.22,
                fill_color=ManimColor(CREAM), fill_opacity=1.0,
                stroke_width=0, stroke_opacity=0
            ).move_to([cx, ly_base - 0.25, 0])
            lbl = Text(f"{wacc_bins[i]:.1f}%", font="Georgia", font_size=10,
                       color=ManimColor(INK)).move_to([cx, ly_base - 0.25, 0])
            left_bars.add(VGroup(bar, bg, lbl))

        # Build right bars
        right_bars = VGroup()
        for i, (cnt, cx) in enumerate(zip(ev_counts, rx_centers)):
            h = count_to_h(cnt)
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=ManimColor(SLATE), fill_opacity=0.75,
                stroke_width=0, stroke_opacity=0
            )
            bar.move_to([cx, ry_base + h / 2, 0])
            bg = Rectangle(
                width=0.5, height=0.22,
                fill_color=ManimColor(CREAM), fill_opacity=1.0,
                stroke_width=0, stroke_opacity=0
            ).move_to([cx, ry_base - 0.25, 0])
            lbl = Text(str(ev_bins[i]), font="Georgia", font_size=10,
                       color=ManimColor(INK)).move_to([cx, ry_base - 0.25, 0])
            right_bars.add(VGroup(bar, bg, lbl))

        # p10/p90 lines: left
        # p10 at 7.6% -> index 0 -> lx_centers[0]; p90 at 9.4% -> lx_centers[6]
        lp10_x = lx_centers[0]
        lp90_x = lx_centers[6]
        left_p10_line = Line([lp10_x, ly_base, 0], [lp10_x, ly_base + 2.2, 0],
                             stroke_width=1.5, color=ManimColor(INK))
        left_p10_line.set_dash([0.1, 0.1])
        left_p90_line = Line([lp90_x, ly_base, 0], [lp90_x, ly_base + 1.5, 0],
                             stroke_width=1.5, color=ManimColor(INK))
        left_p90_line.set_dash([0.1, 0.1])
        lp10_bg = Rectangle(width=0.8, height=0.22, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                            ).move_to([lp10_x, ly_base + 2.45, 0])
        lp10_lbl = Text("p10=7.5%", font="Georgia", font_size=10, color=ManimColor(INK)
                        ).move_to([lp10_x, ly_base + 2.45, 0])
        lp90_bg = Rectangle(width=0.8, height=0.22, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                            ).move_to([lp90_x, ly_base + 1.75, 0])
        lp90_lbl = Text("p90=9.6%", font="Georgia", font_size=10, color=ManimColor(INK)
                        ).move_to([lp90_x, ly_base + 1.75, 0])
        left_p10p90 = VGroup(left_p10_line, left_p90_line,
                             lp10_bg, lp10_lbl, lp90_bg, lp90_lbl)

        # p10/p90 lines: right
        rp10_x = rx_centers[0]
        rp90_x = rx_centers[6]
        right_p10_line = Line([rp10_x, ry_base, 0], [rp10_x, ry_base + 1.2, 0],
                              stroke_width=1.5, color=ManimColor(INK))
        right_p10_line.set_dash([0.1, 0.1])
        right_p90_line = Line([rp90_x, ry_base, 0], [rp90_x, ry_base + 1.5, 0],
                              stroke_width=1.5, color=ManimColor(INK))
        right_p90_line.set_dash([0.1, 0.1])
        rp10_bg = Rectangle(width=1.1, height=0.22, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                            ).move_to([rp10_x, ry_base + 1.45, 0])
        rp10_lbl = Text("p10=$1,640M", font="Georgia", font_size=10, color=ManimColor(INK)
                        ).move_to([rp10_x, ry_base + 1.45, 0])
        rp90_bg = Rectangle(width=1.1, height=0.22, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                            ).move_to([rp90_x, ry_base + 1.75, 0])
        rp90_lbl = Text("p90=$2,720M", font="Georgia", font_size=10, color=ManimColor(INK)
                        ).move_to([rp90_x, ry_base + 1.75, 0])
        right_p10p90 = VGroup(right_p10_line, right_p90_line,
                              rp10_bg, rp10_lbl, rp90_bg, rp90_lbl)

        # Verdict — placed at y=-2.75 to stay clear of divider and safe-area edge
        verdict_bg = Rectangle(width=8.0, height=0.40, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([0, -2.75, 0])
        verdict = Text(
            "Precision illusion: 8.3% WACC -> $1,640M-$2,720M EV range (66% spread)",
            font="Georgia", font_size=13, color=ManimColor(CRIMSON)
        ).move_to([0, -2.75, 0])

        # Animation
        self.play(Write(title))                                              # 1
        self.play(FadeIn(left_axes), FadeIn(left_bars), FadeIn(divider))    # 2
        self.play(FadeIn(left_p10p90))                                       # 3
        self.play(FadeIn(right_axes), FadeIn(right_bars))                   # 4
        self.play(FadeIn(right_p10p90))                                      # 5
        self.play(FadeIn(verdict_bg), FadeIn(verdict))                       # 6
