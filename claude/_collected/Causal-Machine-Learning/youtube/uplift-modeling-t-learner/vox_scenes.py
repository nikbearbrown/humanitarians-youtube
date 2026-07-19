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


class B04_UpliftQini(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "T-Learner Uplift Model: Who Buys Because of the Ad?",
            color=INK, weight=BOLD, font_size=26
        )
        title.move_to([0, 3.2, 0])

        # ---- Divider ----
        divider = Line(start=[0.0, -2.5, 0], end=[0.0, 2.8, 0],
                       color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # ====================================================
        # LEFT PANEL: Qini Curve
        # x(d) = -5.5 + d*0.5
        # y(v) = -2.2 + v*4.5
        # ====================================================
        tl_pts = [
            (-5.5,-2.2), (-5.0,-1.21), (-4.5,-0.49), (-4.0,0.05),
            (-3.5,0.50), (-3.0,0.86), (-2.5,1.18), (-2.0,1.49),
            (-1.5,1.76), (-1.0,2.03), (-0.5,2.3)
        ]
        rnd_pts = [
            (-5.5,-2.2), (-5.0,-1.75), (-4.5,-1.3), (-4.0,-0.85),
            (-3.5,-0.4), (-3.0,0.05), (-2.5,0.5), (-2.0,0.95),
            (-1.5,1.4), (-1.0,1.85), (-0.5,2.3)
        ]

        # Shaded polygon between T-learner and Random
        poly_pts = [list(p) + [0] for p in tl_pts] + [list(p) + [0] for p in reversed(rnd_pts)]
        shaded_area = Polygon(*poly_pts,
                              fill_color=GOLD, fill_opacity=0.4,
                              stroke_width=0, stroke_opacity=0)

        # T-learner curve (connected Line segments)
        tl_lines = VGroup()
        for i in range(len(tl_pts) - 1):
            seg = Line(
                start=[tl_pts[i][0], tl_pts[i][1], 0],
                end=[tl_pts[i+1][0], tl_pts[i+1][1], 0],
                color=INK, stroke_width=4
            )
            tl_lines.add(seg)

        # Random curve (dashed — short segments with gaps)
        rnd_lines = VGroup()
        for i in range(len(rnd_pts) - 1):
            x0, y0 = rnd_pts[i]
            x1, y1 = rnd_pts[i+1]
            # dash: draw 2/3 of each segment, skip 1/3
            xm = x0 + (x1-x0)*0.65
            ym = y0 + (y1-y0)*0.65
            seg = Line(start=[x0, y0, 0], end=[xm, ym, 0],
                       color=SLATE, stroke_width=2)
            rnd_lines.add(seg)

        # Left axes
        left_x_axis = Line(start=[-5.5,-2.2,0], end=[-0.3,-2.2,0], color=INK, stroke_width=2)
        left_y_axis = Line(start=[-5.5,-2.2,0], end=[-5.5,2.4,0], color=INK, stroke_width=2)

        # X-tick labels at d=0,5,10
        left_xtick_data = [(-5.5, "0"), (-3.0, "5"), (-0.5, "10")]
        left_xticks = VGroup()
        for xp, lbl in left_xtick_data:
            tick = Line(start=[xp,-2.2,0], end=[xp,-2.35,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.4, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, -2.55, 0])
            t = Text(lbl, font_size=18, color=INK)
            t.move_to([xp, -2.55, 0])
            left_xticks.add(tick, bg, t)

        # Y-tick labels at v=0,0.5,1.0
        left_ytick_data = [(-2.2, "0"), (0.05, "0.5"), (2.3, "1.0")]
        left_yticks = VGroup()
        for yp, lbl in left_ytick_data:
            tick = Line(start=[-5.5,yp,0], end=[-5.65,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.55, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([-5.9, yp, 0])
            t = Text(lbl, font_size=18, color=INK)
            t.move_to([-5.9, yp, 0])
            left_yticks.add(tick, bg, t)

        left_panel_title_bg = Rectangle(width=2.0, height=0.35,
                                        fill_color=CREAM, fill_opacity=1,
                                        stroke_width=0, stroke_opacity=0)
        left_panel_title_bg.move_to([-3.0, 2.6, 0])
        left_panel_title = Text("Qini Curve", font_size=22, color=SLATE, weight=BOLD)
        left_panel_title.move_to([-3.0, 2.6, 0])

        left_axes = VGroup(left_x_axis, left_y_axis, left_xticks, left_yticks,
                           left_panel_title_bg, left_panel_title)

        # Qini annotation — placed in lower-left away from curve overlap zone
        qini_bg = Rectangle(width=1.8, height=0.35,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        qini_bg.move_to([-4.0, -1.5, 0])
        qini_ann = Text("Qini = 0.31", font_size=20, color=INK)
        qini_ann.move_to([-4.0, -1.5, 0])
        qini_annotation = VGroup(qini_bg, qini_ann)

        # ====================================================
        # RIGHT PANEL: Per-Decile Uplift Bars
        # Bar positions: 0.5 + i*0.5 for i=0..9
        # y_base=-2.2; scale=18 units per unit
        # ====================================================
        model_uplift = [0.22, 0.16, 0.12, 0.10, 0.08, 0.07, 0.07, 0.06, 0.06, 0.06]
        # Colors: deciles 1-4: PASS_CLR; deciles 5-10: GOLD
        bar_colors = [PASS_CLR, PASS_CLR, PASS_CLR, PASS_CLR,
                      GOLD, GOLD, GOLD, GOLD, GOLD, GOLD]

        right_bars = VGroup()
        right_xlabels = VGroup()
        y_base = -2.2
        bar_scale = 18.0
        bar_width = 0.35

        for i in range(10):
            xc = 0.5 + i * 0.5
            ht = model_uplift[i] * bar_scale
            top_y = y_base + ht
            bar = Rectangle(
                width=bar_width,
                height=ht,
                fill_color=bar_colors[i],
                fill_opacity=1,
                stroke_width=0,
                stroke_opacity=0
            )
            bar.move_to([xc, y_base + ht/2, 0])
            right_bars.add(bar)

            # x-label
            bg = Rectangle(width=0.35, height=0.25,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xc, -2.5, 0])
            lbl = Text(str(i+1), font_size=16, color=INK)
            lbl.move_to([xc, -2.5, 0])
            right_xlabels.add(bg, lbl)

        # Random baseline dashed line at y = -2.2 + 0.10*18 = -0.4
        random_baseline_line = Line(
            start=[0.3, -0.4, 0], end=[5.3, -0.4, 0],
            color=SLATE, stroke_width=2
        )
        # Make it dashed by using DashedLine equivalent (short segments)
        rand_dash = VGroup()
        x_start = 0.3
        x_end = 5.3
        dash_len = 0.25
        gap_len = 0.12
        xc = x_start
        while xc < x_end:
            x_end_seg = min(xc + dash_len, x_end)
            rand_dash.add(Line(start=[xc, -0.4, 0], end=[x_end_seg, -0.4, 0],
                               color=SLATE, stroke_width=2))
            xc += dash_len + gap_len

        # Right panel axes
        right_x_axis = Line(start=[0.3,-2.2,0], end=[5.3,-2.2,0], color=INK, stroke_width=2)
        right_y_axis = Line(start=[0.3,-2.2,0], end=[0.3,2.1,0], color=INK, stroke_width=2)

        right_panel_title_bg = Rectangle(width=2.6, height=0.35,
                                         fill_color=CREAM, fill_opacity=1,
                                         stroke_width=0, stroke_opacity=0)
        right_panel_title_bg.move_to([2.9, 2.6, 0])
        right_panel_title = Text("Uplift by Decile", font_size=22, color=SLATE, weight=BOLD)
        right_panel_title.move_to([2.9, 2.6, 0])

        right_axes = VGroup(right_x_axis, right_y_axis,
                            right_panel_title_bg, right_panel_title)

        # ---- Verdict ----
        verdict_bg = Rectangle(width=11.0, height=0.4,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([0, -3.0, 0])
        verdict = Text(
            "Top decile: 2.2x random | T-learner CATE = E[Y|T=1,X] - E[Y|T=0,X]",
            font_size=20, color=INK
        )
        verdict.move_to([0, -3.0, 0])
        verdict_grp = VGroup(verdict_bg, verdict)

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(left_axes), Create(right_axes), Create(divider))
        self.play(Create(rnd_lines))
        self.play(Create(shaded_area), Create(tl_lines))
        self.play(FadeIn(qini_annotation))
        self.play(FadeIn(right_bars), FadeIn(right_xlabels), FadeIn(rand_dash))
        self.play(FadeIn(verdict_grp))
        self.wait(1)
