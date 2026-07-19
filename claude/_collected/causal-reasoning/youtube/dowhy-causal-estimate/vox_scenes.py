import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_DoWhyBars(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("DoWhy: Naive vs. Adjusted Estimate", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        subtitle_box = Rectangle(width=8.0, height=0.6, fill_color=CREAM,
                                 fill_opacity=1, stroke_width=0, stroke_opacity=0)
        subtitle_box.move_to([0, 2.8, 0])
        self.play(GrowFromCenter(subtitle_box), run_time=0.3)
        subtitle = Text("Synthetic: Z→T, Z→Y, T→Y  |  True effect = 0.50", font="Prism", font_size=15, color=SLATE)
        subtitle.move_to([0, 2.8, 0])
        self.play(FadeIn(subtitle), run_time=0.25)
        base_line = Line(start=[-5.5, -1.5, 0], end=[5.5, -1.5, 0], color=INK, stroke_width=2)
        self.play(Create(base_line), run_time=0.4)
        # Naive bar: 0.75 -> height proportional, CRIMSON
        naive_h = 2.8
        naive_bar = Rectangle(width=2.2, height=naive_h, fill_color=CRIMSON, fill_opacity=0.8,
                              stroke_color=CRIMSON, stroke_width=2)
        naive_bar.move_to([-2.5, -1.5 + naive_h/2, 0])
        self.play(GrowFromEdge(naive_bar, DOWN), run_time=0.5)
        naive_bg = Rectangle(width=1.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        naive_bg.move_to([-2.5, -1.5 + naive_h + 0.3, 0])
        naive_val = Text("0.75", font="Prism", font_size=20, color=CRIMSON, weight=BOLD)
        naive_val.move_to([-2.5, -1.5 + naive_h + 0.3, 0])
        self.play(GrowFromCenter(naive_bg), run_time=0.2)
        self.play(FadeIn(naive_val), run_time=0.25)
        naive_lbl_bg = Rectangle(width=2.0, height=0.45, fill_color=CREAM, fill_opacity=1,
                                  stroke_width=0, stroke_opacity=0)
        naive_lbl_bg.move_to([-2.5, -2.05, 0])
        naive_lbl = Text("Naive", font="Prism", font_size=16, color=CRIMSON)
        naive_lbl.move_to([-2.5, -2.05, 0])
        self.play(GrowFromCenter(naive_lbl_bg), run_time=0.15)
        self.play(FadeIn(naive_lbl), run_time=0.2)
        # Adjusted bar: 0.50 -> height 1.87, INK
        adj_h = 1.87
        adj_bar = Rectangle(width=2.2, height=adj_h, fill_color=GOLD, fill_opacity=0.9,
                            stroke_color=INK, stroke_width=2)
        adj_bar.move_to([2.5, -1.5 + adj_h/2, 0])
        self.play(GrowFromEdge(adj_bar, DOWN), run_time=0.5)
        adj_bg = Rectangle(width=1.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        adj_bg.move_to([2.5, -1.5 + adj_h + 0.3, 0])
        adj_val = Text("0.50", font="Prism", font_size=20, color=INK, weight=BOLD)
        adj_val.move_to([2.5, -1.5 + adj_h + 0.3, 0])
        self.play(GrowFromCenter(adj_bg), run_time=0.2)
        self.play(FadeIn(adj_val), run_time=0.25)
        adj_lbl_bg = Rectangle(width=2.4, height=0.45, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        adj_lbl_bg.move_to([2.5, -2.05, 0])
        adj_lbl = Text("Adjusted", font="Prism", font_size=16, color=INK)
        adj_lbl.move_to([2.5, -2.05, 0])
        self.play(GrowFromCenter(adj_lbl_bg), run_time=0.15)
        self.play(FadeIn(adj_lbl), run_time=0.2)
        # Delta annotation
        delta_box = Rectangle(width=5.5, height=0.65, fill_color=GOLD,
                              fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        delta_box.move_to([0, -2.8, 0])
        self.play(GrowFromCenter(delta_box), run_time=0.35)
        delta_lbl = Text("Confounding bias = 0.75 - 0.50 = 0.25  (50% inflation)", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        delta_lbl.move_to([0, -2.8, 0])
        self.play(FadeIn(delta_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))


class B06_ConfounderGap(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Adjustment Set Must Include All Confounders", font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdr_line = Line(start=[-5.5, 2.5, 0], end=[5.5, 2.5, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        hdrs = ["Scenario", "Adj Set", "True Effect", "Estimate", "Gap"]
        x_pos = [-3.5, -1.0, 1.0, 2.8, 4.3]
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=14, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.8, 0])
            self.play(FadeIn(lbl), run_time=0.12)
        data = [
            ("1 confounder Z",     "{Z}",    "0.50", "0.50", "0.00", CREAM,  INK),
            ("2 confounders,\nadj {Z1} only", "{Z1}", "0.50", "0.68", "0.18", "#FFF0F0", CRIMSON),
            ("2 confounders,\nadj {Z1,Z2}",   "{Z1,Z2}","0.50","0.50","0.00", GOLD,    INK),
        ]
        y_top = 1.8
        for i, (scen, adj, true_e, est, gap, bg, clr) in enumerate(data):
            y = y_top - i * 1.1
            row_bg = Rectangle(width=11.0, height=0.95, fill_color=bg, fill_opacity=0.7,
                               stroke_color=SLATE, stroke_width=0.5)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.25)
            scen_lbl = Text(scen, font="Prism", font_size=12, color=INK)
            scen_lbl.move_to([x_pos[0], y, 0])
            adj_lbl = Text(adj, font="Prism", font_size=13, color=SLATE)
            adj_lbl.move_to([x_pos[1], y, 0])
            true_lbl = Text(true_e, font="Prism", font_size=13, color=INK)
            true_lbl.move_to([x_pos[2], y, 0])
            est_lbl = Text(est, font="Prism", font_size=14, color=clr, weight=BOLD)
            est_lbl.move_to([x_pos[3], y, 0])
            gap_lbl = Text(gap, font="Prism", font_size=14, color=clr, weight=BOLD)
            gap_lbl.move_to([x_pos[4], y, 0])
            self.play(FadeIn(scen_lbl), FadeIn(adj_lbl), FadeIn(true_lbl),
                      FadeIn(est_lbl), FadeIn(gap_lbl), run_time=0.35)
        rule_box = Rectangle(width=8.5, height=0.65, fill_color=CREAM,
                             fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        rule_box.move_to([0, -1.5, 0])
        self.play(GrowFromCenter(rule_box), run_time=0.35)
        rule_lbl = Text("Partial adjustment leaves residual bias — set must be complete", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        rule_lbl.move_to([0, -1.5, 0])
        self.play(FadeIn(rule_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
