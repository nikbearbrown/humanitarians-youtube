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


class B04_IPWBalance(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "Propensity Score Weighting: Balancing the Groups",
            color=INK, weight=BOLD, font_size=28
        )
        title.move_to([0, 3.2, 0])

        # ---- Divider ----
        divider = Line(start=[0.0,-2.5,0], end=[0.0,2.8,0],
                       color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # ====================================================
        # LEFT PANEL: SMD Balance Plot
        # y_base=-2.0; scale=6.667; max=0.6
        # ====================================================
        y_base = -2.0
        smd_scale = 6.667

        # Bar positions:
        # AGE group center x=-4.0: before x=-4.35, after x=-3.65
        # INCOME group center x=-2.0: before x=-2.35, after x=-1.65
        bar_data = [
            # (x_center, smd_val, color)
            (-4.35, 0.45, CRIMSON),
            (-3.65, 0.06, PASS_CLR),
            (-2.35, 0.52, CRIMSON),
            (-1.65, 0.08, PASS_CLR),
        ]
        bar_w = 0.6

        before_bars = VGroup()
        after_bars = VGroup()

        for i, (xc, smd, color) in enumerate(bar_data):
            ht = smd * smd_scale
            bar = Rectangle(
                width=bar_w, height=ht,
                fill_color=color, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bar.move_to([xc, y_base + ht/2, 0])
            if color == CRIMSON:
                before_bars.add(bar)
            else:
                after_bars.add(bar)

        # Threshold dashed line at y = -2.0 + 0.10*6.667 = -1.333
        thresh_y = -2.0 + 0.10 * 6.667
        thresh_dash = VGroup()
        xc = -5.5
        while xc < -0.3:
            xe = min(xc + 0.3, -0.3)
            thresh_dash.add(Line(start=[xc, thresh_y, 0], end=[xe, thresh_y, 0],
                                 color=SLATE, stroke_width=1.5))
            xc += 0.48

        thresh_bg = Rectangle(width=2.6, height=0.28,
                              fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0)
        thresh_bg.move_to([-1.5, thresh_y + 0.22, 0])
        thresh_lbl = Text("SMD=0.1 threshold", font_size=17, color=SLATE)
        thresh_lbl.move_to([-1.5, thresh_y + 0.22, 0])
        threshold_line = VGroup(thresh_dash, thresh_bg, thresh_lbl)

        # Left axes
        l_x_axis = Line(start=[-5.5,-2.0,0], end=[-0.3,-2.0,0], color=INK, stroke_width=2)
        l_y_axis = Line(start=[-5.5,-2.0,0], end=[-5.5,2.1,0], color=INK, stroke_width=2)

        # y-ticks at 0, 0.2, 0.4
        l_ytick_data = [(0, "0", -2.0), (0.2, "0.2", -2.0+0.2*6.667), (0.4, "0.4", -2.0+0.4*6.667)]
        l_yticks = VGroup()
        for val, lbl, yp in l_ytick_data:
            tick = Line(start=[-5.5,yp,0], end=[-5.65,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.5, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([-5.9, yp, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([-5.9, yp, 0])
            l_yticks.add(tick, bg, t)

        # Group labels
        grp_label_data = [(-4.0, "AGE"), (-2.0, "INCOME")]
        grp_labels = VGroup()
        for xp, lbl in grp_label_data:
            bg = Rectangle(width=1.2, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, -2.4, 0])
            t = Text(lbl, font_size=18, color=INK)
            t.move_to([xp, -2.4, 0])
            grp_labels.add(bg, t)

        left_panel_title_bg = Rectangle(width=2.8, height=0.32,
                                        fill_color=CREAM, fill_opacity=1,
                                        stroke_width=0, stroke_opacity=0)
        left_panel_title_bg.move_to([-3.0, 2.4, 0])
        left_panel_title = Text("Covariate Balance", font_size=22, color=SLATE, weight=BOLD)
        left_panel_title.move_to([-3.0, 2.4, 0])

        left_axes = VGroup(l_x_axis, l_y_axis, l_yticks, grp_labels,
                           left_panel_title_bg, left_panel_title)

        # ====================================================
        # RIGHT PANEL: ATE Number Line
        # Range 2.5 to 4.0; x: 0.5 to 5.5; scale=3.333
        # x(v) = 0.5 + (v-2.5)*3.333
        # ====================================================
        nl_y = -0.5

        def ate_to_x(v):
            return 0.5 + (v - 2.5) * 3.333

        x_truth_r = ate_to_x(3.0)
        x_ipw_r = ate_to_x(3.05)
        x_naive_r = ate_to_x(3.72)

        number_line = Line(start=[0.5, nl_y, 0], end=[5.5, nl_y, 0],
                           color=INK, stroke_width=3)

        # Ticks at 2.5, 3.0, 3.5, 4.0
        r_tick_data = [(2.5, "2.5"), (3.0, "3.0"), (3.5, "3.5"), (4.0, "4.0")]
        r_ticks = VGroup()
        for v, lbl in r_tick_data:
            xp = ate_to_x(v)
            tick = Line(start=[xp,nl_y-0.1,0], end=[xp,nl_y+0.1,0],
                        color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.55, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, nl_y-0.35, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([xp, nl_y-0.35, 0])
            r_ticks.add(tick, bg, t)

        # Truth marker (dashed vertical)
        truth_vline = VGroup()
        ylo = nl_y - 0.05; yhi = 0.2
        yc = ylo
        while yc < yhi:
            ye = min(yc + 0.1, yhi)
            truth_vline.add(Line(start=[x_truth_r, yc, 0], end=[x_truth_r, ye, 0],
                                 color=PASS_CLR, stroke_width=2))
            yc += 0.18

        truth_bg_r = Rectangle(width=1.3, height=0.3,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        truth_bg_r.move_to([x_truth_r, 0.35, 0])
        truth_lbl_r = Text("Truth=3.0", font_size=18, color=PASS_CLR)
        truth_lbl_r.move_to([x_truth_r, 0.35, 0])
        truth_marker_r = VGroup(truth_vline, truth_bg_r, truth_lbl_r)

        # IPW marker — label shifted to avoid truth marker overlap
        ipw_dot = Circle(radius=0.12, fill_color=INK, fill_opacity=1, stroke_width=0)
        ipw_dot.move_to([x_ipw_r, nl_y, 0])
        ipw_bg = Rectangle(width=1.3, height=0.3,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        # Place IPW label below the number line to avoid overlap with Truth above
        ipw_bg.move_to([x_ipw_r, nl_y - 0.55, 0])
        ipw_lbl = Text("IPW=3.05", font_size=18, color=INK)
        ipw_lbl.move_to([x_ipw_r, nl_y - 0.55, 0])
        ipw_marker = VGroup(ipw_dot, ipw_bg, ipw_lbl)

        # Naive marker
        naive_dot = Circle(radius=0.12, fill_color=CRIMSON, fill_opacity=1, stroke_width=0)
        naive_dot.move_to([x_naive_r, nl_y, 0])
        naive_bg = Rectangle(width=1.4, height=0.3,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        naive_bg.move_to([x_naive_r, nl_y - 0.45, 0])
        naive_lbl = Text("Naive=3.72", font_size=18, color=CRIMSON)
        naive_lbl.move_to([x_naive_r, nl_y - 0.45, 0])
        naive_marker = VGroup(naive_dot, naive_bg, naive_lbl)

        all_labels = VGroup(truth_marker_r, ipw_marker, naive_marker)

        # Bias arrow (double-headed line)
        bias_y = nl_y - 0.8
        bias_line = Line(start=[x_truth_r, bias_y, 0], end=[x_naive_r, bias_y, 0],
                         color=CRIMSON, stroke_width=2)
        bias_cap_l = Line(start=[x_truth_r, bias_y-0.1, 0], end=[x_truth_r, bias_y+0.1, 0],
                          color=CRIMSON, stroke_width=2)
        bias_cap_r = Line(start=[x_naive_r, bias_y-0.1, 0], end=[x_naive_r, bias_y+0.1, 0],
                          color=CRIMSON, stroke_width=2)
        bias_bg = Rectangle(width=1.8, height=0.28,
                            fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0)
        bias_bg.move_to([(x_truth_r+x_naive_r)/2, bias_y - 0.3, 0])
        bias_lbl = Text("BIAS: +0.72", font_size=17, color=CRIMSON)
        bias_lbl.move_to([(x_truth_r+x_naive_r)/2, bias_y - 0.3, 0])
        bias_arrow = VGroup(bias_line, bias_cap_l, bias_cap_r, bias_bg, bias_lbl)

        right_panel_title_bg = Rectangle(width=2.4, height=0.32,
                                         fill_color=CREAM, fill_opacity=1,
                                         stroke_width=0, stroke_opacity=0)
        right_panel_title_bg.move_to([3.0, 2.4, 0])
        right_panel_title = Text("ATE Estimates", font_size=22, color=SLATE, weight=BOLD)
        right_panel_title.move_to([3.0, 2.4, 0])

        right_panel = VGroup(right_panel_title_bg, right_panel_title)

        # ---- Legend ----
        legend_items = [(CRIMSON, "Before IPW"), (PASS_CLR, "After IPW")]
        legend = VGroup()
        lx = -5.0
        for color, label in legend_items:
            box = Rectangle(width=0.3, height=0.3,
                            fill_color=color, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0)
            box.move_to([lx, -3.1, 0])
            bg = Rectangle(width=1.5, height=0.3,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([lx + 0.95, -3.1, 0])
            txt = Text(label, font_size=18, color=INK)
            txt.move_to([lx + 0.95, -3.1, 0])
            legend.add(box, bg, txt)
            lx += 3.0

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(left_axes), Create(divider))
        self.play(FadeIn(before_bars), FadeIn(grp_labels))
        self.play(FadeIn(after_bars), FadeIn(threshold_line))
        self.play(Create(number_line), Create(r_ticks), FadeIn(right_panel))
        self.play(FadeIn(all_labels))
        self.play(FadeIn(bias_arrow), FadeIn(legend))
        self.wait(1)
