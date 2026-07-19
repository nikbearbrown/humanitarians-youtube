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


class B04_MMTaxShield(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"; AMBER="#E8A020"

        # Pre-computed values
        D_vals = [0, 100, 200, 300, 400, 500, 600, 700, 800]
        V_no_tax  = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        V_with_tax = [1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]
        V_tradeoff = [1000, 1022, 1038, 1048, 1052, 1050, 1042, 1028, 1008]

        # Plot axes mapping
        D_min, D_max = 0, 800
        V_min, V_max = 980, 1210
        x_plot_min, x_plot_max = -5.0, 5.0
        y_plot_min, y_plot_max = -2.5, 2.5

        def px(D):
            return x_plot_min + (D - D_min) / (D_max - D_min) * (x_plot_max - x_plot_min)

        def py(V):
            return y_plot_min + (V - V_min) / (V_max - V_min) * (y_plot_max - y_plot_min)

        title = Text(
            "When Does Debt Create Value? The MM Trade-Off",
            font="Georgia", font_size=20, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Axes
        x_axis = Line([-5.5, -2.7, 0], [5.5, -2.7, 0], stroke_width=2, color=ManimColor(SLATE))
        y_axis = Line([-5.5, -2.7, 0], [-5.5, 2.7, 0], stroke_width=2, color=ManimColor(SLATE))

        # x-axis ticks
        x_ticks = VGroup()
        for d_tick in [0, 200, 400, 600, 800]:
            tx = px(d_tick)
            tick = Line([tx, -2.7, 0], [tx, -2.85, 0], stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.45, height=0.22, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([tx, -3.05, 0])
            lbl = Text(str(d_tick), font="Georgia", font_size=12, color=ManimColor(SLATE)
                       ).move_to([tx, -3.05, 0])
            x_ticks.add(VGroup(tick, bg, lbl))

        xlabel_bg = Rectangle(width=1.5, height=0.26, fill_color=ManimColor(CREAM),
                              fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                              ).move_to([0, -3.3, 0])
        xlabel = Text("Debt D ($M)", font="Georgia", font_size=14, color=ManimColor(SLATE)
                      ).move_to([0, -3.3, 0])

        # y-axis ticks
        y_ticks = VGroup()
        for v_tick in [1000, 1050, 1100, 1150, 1200]:
            ty = py(v_tick)
            tick = Line([-5.5, ty, 0], [-5.65, ty, 0], stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.55, height=0.22, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([-5.9, ty, 0])
            lbl = Text(str(v_tick), font="Georgia", font_size=11, color=ManimColor(SLATE)
                       ).move_to([-5.9, ty, 0])
            y_ticks.add(VGroup(tick, bg, lbl))

        axes = VGroup(x_axis, y_axis, x_ticks, xlabel_bg, xlabel, y_ticks)

        # Build curve line segments
        def make_curve(V_data, color, dashes=False):
            pts = [[px(D_vals[i]), py(V_data[i]), 0] for i in range(len(D_vals))]
            group = VGroup()
            for i in range(len(pts) - 1):
                seg = Line(pts[i], pts[i+1], stroke_width=2.5, color=ManimColor(color))
                if dashes:
                    seg.set_dash([0.12, 0.08])
                group.add(seg)
            return group

        v_no_tax_line = make_curve(V_no_tax, SLATE, dashes=True)
        v_with_tax_line = make_curve(V_with_tax, AMBER, dashes=True)
        v_tradeoff_line = make_curve(V_tradeoff, INK, dashes=False)

        # Curve labels — placed in left margin area away from all curves
        notax_bg = Rectangle(width=1.5, height=0.26, fill_color=ManimColor(CREAM),
                             fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                             ).move_to([-2.5, py(1000) - 0.42, 0])
        notax_lbl = Text("V (no taxes)", font="Georgia", font_size=12, color=ManimColor(SLATE)
                         ).move_to([-2.5, py(1000) - 0.42, 0])

        tax_bg = Rectangle(width=2.2, height=0.26, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([-2.0, py(1100) + 0.42, 0])
        tax_lbl = Text("V (MM with tax shield)", font="Georgia", font_size=12, color=ManimColor(AMBER)
                       ).move_to([-2.0, py(1100) + 0.42, 0])

        to_bg = Rectangle(width=2.2, height=0.26, fill_color=ManimColor(CREAM),
                          fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                          ).move_to([-2.0, py(1040) - 0.42, 0])
        to_lbl = Text("V (trade-off theory)", font="Georgia", font_size=12, color=ManimColor(INK)
                      ).move_to([-2.0, py(1040) - 0.42, 0])

        v_no_tax_group = VGroup(v_no_tax_line, notax_bg, notax_lbl)
        v_with_tax_group = VGroup(v_with_tax_line, tax_bg, tax_lbl)
        v_tradeoff_group = VGroup(v_tradeoff_line, to_bg, to_lbl)

        # Optimal D marker: D*=417 -> x=0.213, V*=1052 -> y=-0.935
        D_opt = 417
        V_opt = 1052
        x_opt = px(D_opt)
        y_opt = py(V_opt)

        opt_dline = Line([x_opt, -2.7, 0], [x_opt, y_opt, 0],
                         stroke_width=1.5, color=ManimColor(CRIMSON))
        opt_dline.set_dash([0.1, 0.08])
        opt_dot = Dot([x_opt, y_opt, 0], radius=0.08, color=ManimColor(CRIMSON))
        opt_bg = Rectangle(width=1.8, height=0.28, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([x_opt + 1.1, y_opt + 0.28, 0])
        opt_lbl = Text("OPTIMAL D/V~38%", font="Georgia", font_size=12, color=ManimColor(CRIMSON)
                       ).move_to([x_opt + 1.1, y_opt + 0.28, 0])
        opt_group = VGroup(opt_dline, opt_dot, opt_bg, opt_lbl)

        # Animation
        self.play(Write(title))                                    # 1
        self.play(Create(axes))                                    # 2
        self.play(Create(v_no_tax_group))                          # 3
        self.play(Create(v_with_tax_group))                        # 4
        self.play(Create(v_tradeoff_group))                        # 5
        self.play(FadeIn(opt_group))                               # 6
