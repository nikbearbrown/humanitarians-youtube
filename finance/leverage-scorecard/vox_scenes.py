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


class B04_LeverageScorecard(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"; AMBER="#E8A020"

        title = Text(
            "Leverage Scorecard: Inside View vs. Outside View",
            font="Georgia", font_size=20, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Panel divider — ends at y=-2.4 so net-benefit band is clear
        panel_divider = Line([0.0, -2.4, 0], [0.0, 3.0, 0],
                             stroke_width=1, color=ManimColor(SLATE))

        # ============================================================
        # LEFT PANEL: 3 coverage ratio gauges
        # Gauge x range: -5.5 to -0.5 (width=5.0)
        # ============================================================
        gauge_h = 0.45
        gauge_x0 = -5.5
        gauge_x1 = -0.5
        gauge_w = gauge_x1 - gauge_x0  # 5.0

        # Gauges: (name, value, scale_max, thresholds, direction)
        # direction: "higher_better" (coverage) or "lower_better" (D/E, D/EBITDA)
        gauges_data = [
            # (label, val, scale_max, red_thresh, amber_thresh, direction, y_center)
            ("COV.", 11.43, 15.0, 3.0, 6.0, "higher_better", 1.5),
            ("D/EBITDA", 1.25, 5.0, 3.0, 2.0, "lower_better", 0.4),
            ("D/E", 0.47, 1.5, 1.0, 0.5, "lower_better", -0.7),
        ]

        gauge_row_labels = VGroup()
        gauges_all = VGroup()
        markers_labels = VGroup()

        for (gname, val, scale_max, thresh_outer, thresh_mid, direction, y_center) in gauges_data:
            # Row label — placed INSIDE gauge bar to stay within safe area ±6.3x
            lbl_bg = Rectangle(width=1.1, height=0.32, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([gauge_x0 + 0.7, y_center, 0])
            lbl = Text(gname, font="Georgia", font_size=13, color=ManimColor(INK)
                       ).move_to([gauge_x0 + 0.7, y_center, 0])
            gauge_row_labels.add(VGroup(lbl_bg, lbl))

            # Compute zone boundaries
            if direction == "higher_better":
                # RED zone: 0 to thresh_outer (e.g., 0-3)
                # AMBER zone: thresh_outer to thresh_mid (3-6)
                # GREEN zone: thresh_mid to scale_max (6-15)
                x_red_end = gauge_x0 + (thresh_outer / scale_max) * gauge_w
                x_amb_end = gauge_x0 + (thresh_mid / scale_max) * gauge_w
                red_zone = Rectangle(
                    width=x_red_end - gauge_x0, height=gauge_h,
                    fill_color=ManimColor(CRIMSON), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(gauge_x0 + x_red_end) / 2, y_center, 0])
                amb_zone = Rectangle(
                    width=x_amb_end - x_red_end, height=gauge_h,
                    fill_color=ManimColor(AMBER), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(x_red_end + x_amb_end) / 2, y_center, 0])
                grn_zone = Rectangle(
                    width=gauge_x1 - x_amb_end, height=gauge_h,
                    fill_color=ManimColor(PASS_CLR), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(x_amb_end + gauge_x1) / 2, y_center, 0])
                marker_x = gauge_x0 + (val / scale_max) * gauge_w
            else:
                # GREEN zone: 0 to thresh_mid (0-0.5 for D/E)
                # AMBER zone: thresh_mid to thresh_outer
                # RED zone: thresh_outer to scale_max
                x_grn_end = gauge_x0 + (thresh_mid / scale_max) * gauge_w
                x_amb_end = gauge_x0 + (thresh_outer / scale_max) * gauge_w
                grn_zone = Rectangle(
                    width=x_grn_end - gauge_x0, height=gauge_h,
                    fill_color=ManimColor(PASS_CLR), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(gauge_x0 + x_grn_end) / 2, y_center, 0])
                amb_zone = Rectangle(
                    width=x_amb_end - x_grn_end, height=gauge_h,
                    fill_color=ManimColor(AMBER), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(x_grn_end + x_amb_end) / 2, y_center, 0])
                red_zone = Rectangle(
                    width=gauge_x1 - x_amb_end, height=gauge_h,
                    fill_color=ManimColor(CRIMSON), fill_opacity=0.6,
                    stroke_width=0, stroke_opacity=0
                ).move_to([(x_amb_end + gauge_x1) / 2, y_center, 0])
                marker_x = gauge_x0 + (val / scale_max) * gauge_w

            gauges_all.add(VGroup(red_zone, amb_zone, grn_zone))

            # Marker line at val position
            marker = Line([marker_x, y_center - gauge_h / 2 - 0.08, 0],
                          [marker_x, y_center + gauge_h / 2 + 0.08, 0],
                          stroke_width=2.5, color=ManimColor(INK))
            mlbl_bg = Rectangle(width=1.0, height=0.28, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([marker_x, y_center + gauge_h / 2 + 0.35, 0])
            mlbl = Text(f"{val:.2f}x V", font="Georgia", font_size=12, color=ManimColor(PASS_CLR)
                        ).move_to([marker_x, y_center + gauge_h / 2 + 0.35, 0])
            markers_labels.add(VGroup(marker, mlbl_bg, mlbl))

        # ============================================================
        # RIGHT PANEL: MM trade-off curve (D: 0-800, V: 980-1210)
        # x range: 0.5 to 5.5; y range: -2.3 to 2.3
        # ============================================================
        D_vals = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        V_no_tax = [1000] * 9
        V_tradeoff = [1000, 1022, 1038, 1048, 1052, 1050, 1042, 1028, 1008]

        rx0 = 0.5; rx1 = 5.5
        ry_base = -2.3; ry_top = 2.3
        D_min, D_max = 0, 800
        V_min, V_max = 980, 1210

        def rpx(D):
            return rx0 + (D - D_min) / (D_max - D_min) * (rx1 - rx0)

        def rpy(V):
            return ry_base + (V - V_min) / (V_max - V_min) * (ry_top - ry_base)

        right_xaxis = Line([rx0, ry_base, 0], [rx1, ry_base, 0],
                           stroke_width=2, color=ManimColor(SLATE))
        right_yaxis = Line([rx0, ry_base, 0], [rx0, ry_top, 0],
                           stroke_width=2, color=ManimColor(SLATE))

        # x ticks at D=0, 400, 800
        right_xticks = VGroup()
        for d in [0, 400, 800]:
            tx = rpx(d)
            tick = Line([tx, ry_base, 0], [tx, ry_base - 0.1, 0],
                        stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.4, height=0.22, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([tx, ry_base - 0.3, 0])
            lbl = Text(str(d), font="Georgia", font_size=11, color=ManimColor(SLATE)
                       ).move_to([tx, ry_base - 0.3, 0])
            right_xticks.add(VGroup(tick, bg, lbl))

        right_axes = VGroup(right_xaxis, right_yaxis, right_xticks)

        # Panel title
        rp_title_bg = Rectangle(width=2.0, height=0.26, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([3.0, 2.0, 0])
        rp_title = Text("V vs. D ($M)", font="Georgia", font_size=14, color=ManimColor(SLATE)
                        ).move_to([3.0, 2.0, 0])

        # V_no_tax line (SLATE horizontal)
        v_notax_y = rpy(1000)
        v_no_tax_line = Line([rpx(0), v_notax_y, 0], [rpx(800), v_notax_y, 0],
                             stroke_width=2, color=ManimColor(SLATE))
        v_no_tax_line.set_dash([0.1, 0.07])

        # V_tradeoff curve
        tradeoff_pts = [[rpx(D_vals[i]), rpy(V_tradeoff[i]), 0] for i in range(9)]
        tradeoff_segs = VGroup()
        for i in range(8):
            seg = Line(tradeoff_pts[i], tradeoff_pts[i+1],
                       stroke_width=2.5, color=ManimColor(INK))
            tradeoff_segs.add(seg)

        # Halverson marker at D=400
        halv_x = rpx(400)
        halv_y = rpy(1052)
        halv_dot = Dot([halv_x, halv_y, 0], radius=0.09, color=ManimColor(CRIMSON))
        halv_bg = Rectangle(width=2.0, height=0.28, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                            ).move_to([halv_x + 1.2, halv_y + 0.3, 0])
        halv_lbl = Text("HALVERSON D/V=32%", font="Georgia", font_size=11, color=ManimColor(CRIMSON)
                        ).move_to([halv_x + 1.2, halv_y + 0.3, 0])

        halverson_group = VGroup(halv_dot, halv_bg, halv_lbl)

        right_panel = VGroup(right_axes, rp_title_bg, rp_title,
                             v_no_tax_line, tradeoff_segs)

        # Net benefit box spanning both panels
        nb_bg = Rectangle(width=10.0, height=0.32, fill_color=ManimColor(CREAM),
                          fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                          ).move_to([0, -2.75, 0])
        nb_text = Text(
            "Tax shield: $100M  |  Distress cost (1%): $3.75M  |  Net benefit: +$96M",
            font="Georgia", font_size=12, color=ManimColor(PASS_CLR)
        ).move_to([0, -2.75, 0])
        net_benefit_box = VGroup(nb_bg, nb_text)

        # Animation
        self.play(Write(title))                                              # 1
        self.play(Create(panel_divider), FadeIn(gauge_row_labels))           # 2
        self.play(FadeIn(gauges_all.submobjects[0]), FadeIn(markers_labels.submobjects[0]))  # 3
        self.play(FadeIn(gauges_all.submobjects[1]), FadeIn(markers_labels.submobjects[1]))  # 4
        self.play(FadeIn(gauges_all.submobjects[2]), FadeIn(markers_labels.submobjects[2]))  # 5
        self.play(Create(right_panel))                                        # 6
        self.play(FadeIn(halverson_group))                                    # 7
        self.play(FadeIn(net_benefit_box))                                    # 8
