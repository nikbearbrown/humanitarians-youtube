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


class B04_CCCTimeline(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"; AMBER="#E8A020"

        # Scale: 1 unit = 15 days; x_start = -5.0
        # max_days = 160 => 10.67 units but we'll cap display at x_end=5.5
        scale = 10.0 / 160.0  # units per day
        x_start = -5.0

        data = [
            (2021, 60, 90, 45, 105, 323, 38, 1.2),
            (2022, 58, 92, 47, 103, 317, 37, 0.0),
            (2023, 62, 88, 43, 107, 330, 38, -1.2),
        ]
        bar_h = 0.55

        title = Text(
            "Cash Conversion Cycle: $323M Locked in Transit",
            font="Georgia", font_size=20, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Axis baseline at y=-2.1
        axis_y = -2.1
        axis = Line([x_start - 0.1, axis_y, 0], [5.6, axis_y, 0],
                    stroke_width=1.5, color=ManimColor(SLATE))

        # Day tick labels
        ticks = VGroup()
        for day in [0, 40, 80, 120, 160]:
            tx = x_start + day * scale
            tick = Line([tx, axis_y, 0], [tx, axis_y - 0.12, 0],
                        stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.45, height=0.22, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([tx, axis_y - 0.32, 0])
            lbl = Text(f"{day}d", font="Georgia", font_size=11, color=ManimColor(SLATE)
                       ).move_to([tx, axis_y - 0.32, 0])
            ticks.add(VGroup(tick, bg, lbl))

        year_labels = VGroup()
        dso_bars = VGroup()
        dio_bars = VGroup()
        dpo_bars = VGroup()
        ccc_ticks = VGroup()

        for (yr, dso, dio, dpo, ccc, locked, release, y_center) in data:
            # Year label
            yr_bg = Rectangle(width=0.6, height=0.35, fill_color=ManimColor(CREAM),
                              fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                              ).move_to([x_start - 0.5, y_center, 0])
            yr_lbl = Text(str(yr), font="Georgia", font_size=14, color=ManimColor(INK)
                          ).move_to([x_start - 0.5, y_center, 0])
            year_labels.add(VGroup(yr_bg, yr_lbl))

            # DSO bar: x_start to x_start + dso*scale
            dso_w = dso * scale
            dso_x0 = x_start
            dso_cx = dso_x0 + dso_w / 2
            dso_bar = Rectangle(
                width=dso_w, height=bar_h,
                fill_color=ManimColor(PASS_CLR), fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to([dso_cx, y_center, 0])
            dso_lbl_bg = Rectangle(width=0.5, height=0.22, fill_color=ManimColor(PASS_CLR),
                                   fill_opacity=0.9, stroke_width=0, stroke_opacity=0
                                   ).move_to([dso_cx, y_center, 0])
            dso_lbl = Text("DSO", font="Georgia", font_size=11, color=ManimColor(CREAM)
                           ).move_to([dso_cx, y_center, 0])
            dso_bars.add(VGroup(dso_bar, dso_lbl_bg, dso_lbl))

            # DIO bar: from x_start+dso*scale to x_start+(dso+dio)*scale
            dio_x0 = x_start + dso * scale
            dio_w = dio * scale
            dio_cx = dio_x0 + dio_w / 2
            dio_bar = Rectangle(
                width=dio_w, height=bar_h,
                fill_color=ManimColor(AMBER), fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to([dio_cx, y_center, 0])
            # Place DIO label at 1/4 of the bar (left half) to avoid DPO bar edge overlap
            dio_lbl_x = dio_x0 + dio_w * 0.25
            dio_lbl_bg = Rectangle(width=0.4, height=0.22, fill_color=ManimColor(AMBER),
                                   fill_opacity=0.9, stroke_width=0, stroke_opacity=0
                                   ).move_to([dio_lbl_x, y_center, 0])
            dio_lbl = Text("DIO", font="Georgia", font_size=11, color=ManimColor(INK)
                           ).move_to([dio_lbl_x, y_center, 0])
            dio_bars.add(VGroup(dio_bar, dio_lbl_bg, dio_lbl))

            # DPO bar: drawn from x_start+(dso+dio)*scale going LEFT by dpo*scale
            dpo_right = x_start + (dso + dio) * scale
            dpo_w = dpo * scale
            dpo_cx = dpo_right - dpo_w / 2
            dpo_bar = Rectangle(
                width=dpo_w, height=bar_h * 0.6,
                fill_color=ManimColor(CRIMSON), fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to([dpo_cx, y_center - bar_h * 0.3, 0])
            dpo_lbl_bg = Rectangle(width=0.4, height=0.22, fill_color=ManimColor(CRIMSON),
                                   fill_opacity=0.9, stroke_width=0, stroke_opacity=0
                                   ).move_to([dpo_cx, y_center - bar_h * 0.3, 0])
            dpo_lbl = Text("DPO", font="Georgia", font_size=11, color=ManimColor(CREAM)
                           ).move_to([dpo_cx, y_center - bar_h * 0.3, 0])
            dpo_bars.add(VGroup(dpo_bar, dpo_lbl_bg, dpo_lbl))

            # CCC endpoint tick
            ccc_x = x_start + ccc * scale
            ccc_tick = Line([ccc_x, y_center + bar_h / 2 + 0.08, 0],
                            [ccc_x, y_center - bar_h / 2 - 0.08, 0],
                            stroke_width=2, color=ManimColor(INK))
            ccc_ann_bg = Rectangle(width=1.1, height=0.28, fill_color=ManimColor(CREAM),
                                   fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                   ).move_to([ccc_x + 0.7, y_center + bar_h / 2 + 0.28, 0])
            ccc_ann = Text(f"${locked}M", font="Georgia", font_size=12, color=ManimColor(INK)
                           ).move_to([ccc_x + 0.7, y_center + bar_h / 2 + 0.28, 0])
            ccc_ticks.add(VGroup(ccc_tick, ccc_ann_bg, ccc_ann))

        # Legend
        legend = VGroup()
        items = [(PASS_CLR, "DSO"), (AMBER, "DIO"), (CRIMSON, "DPO (offset)")]
        for li, (clr, lbl) in enumerate(items):
            swatch = Rectangle(width=0.3, height=0.22, fill_color=ManimColor(clr),
                               fill_opacity=0.85, stroke_width=0, stroke_opacity=0
                               ).move_to([-4.0 + li * 2.5, -2.85, 0])
            ltxt = Text(lbl, font="Georgia", font_size=12, color=ManimColor(INK))
            ltxt.next_to(swatch, RIGHT, buff=0.08)
            legend.add(VGroup(swatch, ltxt))

        verdict_bg = Rectangle(width=6.0, height=0.3, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([0, -3.2, 0])
        verdict = Text(
            "10-day CCC improvement = $38M released -- no banker required",
            font="Georgia", font_size=13, color=ManimColor(PASS_CLR)
        ).move_to([0, -3.2, 0])

        # Animation
        self.play(Write(title))                              # 1
        self.play(FadeIn(year_labels), FadeIn(axis), FadeIn(ticks))  # 2
        self.play(FadeIn(dso_bars))                          # 3
        self.play(FadeIn(dio_bars))                          # 4
        self.play(FadeIn(dpo_bars))                          # 5
        self.play(FadeIn(ccc_ticks))                         # 6
        self.play(FadeIn(legend), FadeIn(verdict_bg), FadeIn(verdict))  # 7
