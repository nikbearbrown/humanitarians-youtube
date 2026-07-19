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


class B04_QiniValidation(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "CATE Validation: Qini + Calibration Beat Single-Model AUC",
            color=INK, weight=BOLD, font_size=24
        )
        title.move_to([0, 3.2, 0])

        # ---- Divider ----
        divider = Line(start=[0.0,-2.5,0], end=[0.0,2.7,0],
                       color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # ====================================================
        # LEFT PANEL: Qini Curves
        # x(d) = -5.5 + d*0.5  (d=0..10)
        # y(v) = -2.2 + v*4.5
        # ====================================================
        good_vals = [0, 0.22, 0.38, 0.50, 0.60, 0.68, 0.75, 0.82, 0.88, 0.94, 1.0]
        bad_vals  = [0, 0.11, 0.22, 0.33, 0.44, 0.52, 0.61, 0.71, 0.82, 0.91, 1.0]
        rnd_vals  = [0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0]

        def to_pt(d, v):
            return (-5.5 + d*0.5, -2.2 + v*4.5)

        good_pts = [to_pt(d, v) for d, v in enumerate(good_vals)]
        bad_pts  = [to_pt(d, v) for d, v in enumerate(bad_vals)]
        rnd_pts  = [to_pt(d, v) for d, v in enumerate(rnd_vals)]

        # Good T-learner: INK, solid, stroke_width=4
        good_lines = VGroup()
        for i in range(len(good_pts)-1):
            good_lines.add(Line(
                start=[good_pts[i][0], good_pts[i][1], 0],
                end=[good_pts[i+1][0], good_pts[i+1][1], 0],
                color=INK, stroke_width=4
            ))

        # Bad model: CRIMSON, dashed, stroke_width=3
        bad_lines = VGroup()
        for i in range(len(bad_pts)-1):
            x0, y0 = bad_pts[i]
            x1, y1 = bad_pts[i+1]
            xm = x0 + (x1-x0)*0.65
            ym = y0 + (y1-y0)*0.65
            bad_lines.add(Line(start=[x0, y0, 0], end=[xm, ym, 0],
                               color=CRIMSON, stroke_width=3))

        # Random: SLATE, dashed, stroke_width=2
        rnd_lines = VGroup()
        for i in range(len(rnd_pts)-1):
            x0, y0 = rnd_pts[i]
            x1, y1 = rnd_pts[i+1]
            xm = x0 + (x1-x0)*0.6
            ym = y0 + (y1-y0)*0.6
            rnd_lines.add(Line(start=[x0, y0, 0], end=[xm, ym, 0],
                               color=SLATE, stroke_width=2))

        # Left axes
        l_x_axis = Line(start=[-5.5,-2.2,0], end=[-0.3,-2.2,0], color=INK, stroke_width=2)
        l_y_axis = Line(start=[-5.5,-2.2,0], end=[-5.5,2.4,0], color=INK, stroke_width=2)

        # x-ticks
        l_xtick_data = [(-5.5, "0"), (-3.0, "5"), (-0.5, "10")]
        l_xticks = VGroup()
        for xp, lbl in l_xtick_data:
            tick = Line(start=[xp,-2.2,0], end=[xp,-2.35,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.4, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, -2.55, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([xp, -2.55, 0])
            l_xticks.add(tick, bg, t)

        left_panel_title_bg = Rectangle(width=1.9, height=0.32,
                                        fill_color=CREAM, fill_opacity=1,
                                        stroke_width=0, stroke_opacity=0)
        left_panel_title_bg.move_to([-3.0, 2.6, 0])
        left_panel_title = Text("Qini Curves", font_size=22, color=SLATE, weight=BOLD)
        left_panel_title.move_to([-3.0, 2.6, 0])

        left_axes = VGroup(l_x_axis, l_y_axis, l_xticks,
                           left_panel_title_bg, left_panel_title)

        # Qini annotations — stacked just below the panel title in upper-left
        # Top of chart area left side is clear of curves
        good_qini_bg = Rectangle(width=2.8, height=0.3,
                                 fill_color=CREAM, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0)
        good_qini_bg.move_to([-3.5, 2.1, 0])
        good_qini_txt = Text("T-learner Qini=0.31", font_size=18, color=INK)
        good_qini_txt.move_to([-3.5, 2.1, 0])
        good_qini_label = VGroup(good_qini_bg, good_qini_txt)

        bad_qini_bg = Rectangle(width=2.8, height=0.3,
                                fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0)
        bad_qini_bg.move_to([-3.5, 1.7, 0])
        bad_qini_txt = Text("Bad model Qini=0.04", font_size=18, color=CRIMSON)
        bad_qini_txt.move_to([-3.5, 1.7, 0])
        bad_qini_label = VGroup(bad_qini_bg, bad_qini_txt)

        # ====================================================
        # RIGHT PANEL: Calibration Line Chart
        # y(v) = -2.2 + v*10; x: 0.5+i*0.5 (i=0..9)
        # ====================================================
        T_pred  = [0.21, 0.16, 0.13, 0.11, 0.09, 0.07, 0.06, 0.05, 0.04, 0.03]
        T_obs   = [0.20, 0.15, 0.12, 0.10, 0.08, 0.07, 0.05, 0.04, 0.04, 0.02]
        Bd_pred = [0.35, 0.28, 0.24, 0.20, 0.16, 0.13, 0.10, 0.07, 0.04, 0.02]
        Bd_obs  = [0.12, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.04, 0.02]

        cal_xs = [0.5 + i*0.5 for i in range(10)]

        def cal_y(v):
            return -2.2 + v * 10.0

        def make_line_chart(vals, color, sw, dash=False):
            grp = VGroup()
            for i in range(len(vals)-1):
                x0 = cal_xs[i]; y0 = cal_y(vals[i])
                x1 = cal_xs[i+1]; y1 = cal_y(vals[i+1])
                if dash:
                    xm = x0 + (x1-x0)*0.65
                    ym = y0 + (y1-y0)*0.65
                    grp.add(Line(start=[x0,y0,0], end=[xm,ym,0],
                                 color=color, stroke_width=sw))
                else:
                    grp.add(Line(start=[x0,y0,0], end=[x1,y1,0],
                                 color=color, stroke_width=sw))
            return grp

        t_pred_lines  = make_line_chart(T_pred, INK, 3, dash=False)
        t_obs_lines   = make_line_chart(T_obs, PASS_CLR, 2, dash=False)
        bad_pred_lines = make_line_chart(Bd_pred, CRIMSON, 3, dash=True)
        bad_obs_lines  = make_line_chart(Bd_obs, SLATE, 2, dash=False)

        right_t_learner_lines = VGroup(t_pred_lines, t_obs_lines)
        right_bad_model_lines = VGroup(bad_pred_lines, bad_obs_lines)

        # Right axes
        r_x_axis = Line(start=[0.3,-2.2,0], end=[5.3,-2.2,0], color=INK, stroke_width=2)
        r_y_axis = Line(start=[0.3,-2.2,0], end=[0.3,2.0,0], color=INK, stroke_width=2)

        # y-ticks at 0, 0.1, 0.2, 0.3
        # Labels placed at x=5.5 (right of chart) to avoid y-axis line overlap
        r_ytick_data = [(0.0, "0", -2.2), (0.1, "0.1", -1.2), (0.2, "0.2", -0.2), (0.3, "0.3", 0.8)]
        r_yticks = VGroup()
        for val, lbl, yp in r_ytick_data:
            tick = Line(start=[0.3,yp,0], end=[0.15,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.5, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            # Place tick labels to the right of the chart (5.5) to avoid axis overlap
            bg.move_to([5.5, yp, 0])
            t = Text(lbl, font_size=16, color=INK)
            t.move_to([5.5, yp, 0])
            r_yticks.add(tick, bg, t)

        right_panel_title_bg = Rectangle(width=2.6, height=0.32,
                                         fill_color=CREAM, fill_opacity=1,
                                         stroke_width=0, stroke_opacity=0)
        right_panel_title_bg.move_to([3.0, 2.4, 0])
        right_panel_title = Text("CATE Calibration", font_size=22, color=SLATE, weight=BOLD)
        right_panel_title.move_to([3.0, 2.4, 0])

        right_axes = VGroup(r_x_axis, r_y_axis, r_yticks,
                            right_panel_title_bg, right_panel_title)

        # ---- Legend — placed right side, stacked vertically ----
        legend_items = [
            (INK, "T-pred CATE"),
            (PASS_CLR, "T-observed"),
            (CRIMSON, "Bad-pred CATE"),
            (SLATE, "Bad-observed"),
        ]
        legend = VGroup()
        ly = 1.8
        for color, label in legend_items:
            box = Rectangle(width=0.28, height=0.28,
                            fill_color=color, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0)
            box.move_to([0.7, ly, 0])
            bg = Rectangle(width=1.8, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([1.7, ly, 0])
            txt = Text(label, font_size=16, color=INK)
            txt.move_to([1.7, ly, 0])
            legend.add(box, bg, txt)
            ly -= 0.4

        # ---- Verdict — at bottom, single line ----
        verdict_bg = Rectangle(width=11.0, height=0.35,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0, -3.2, 0])
        verdict_txt = Text(
            "T-learner: Qini=0.31, calibrated | Bad model: Qini=0.04, overclaims top decile",
            font_size=17, color=INK
        )
        verdict_txt.move_to([0, -3.2, 0])
        verdict = VGroup(verdict_bg, verdict_txt)

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(left_axes), Create(divider))
        self.play(Create(rnd_lines))
        self.play(Create(good_lines), FadeIn(good_qini_label))
        self.play(Create(bad_lines), FadeIn(bad_qini_label))
        self.play(Create(right_axes), Create(right_t_learner_lines))
        self.play(Create(right_bad_model_lines), FadeIn(legend), FadeIn(verdict))
        self.wait(1)
