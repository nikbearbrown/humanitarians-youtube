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


class B04_EfficientFrontier(Scene):
    def construct(self):
        # Coordinate mapping:
        # x: volatility sigma in [0.05, 0.30] -> x_plot = -5.0 + (sigma-0.05)/0.25*10
        # y: return mu in [0.04, 0.14] -> y_plot = -2.5 + (mu-0.04)/0.10*5

        def to_x(sigma):
            return -5.0 + (sigma - 0.05) / 0.25 * 10.0

        def to_y(mu):
            return -2.5 + (mu - 0.04) / 0.10 * 5.0

        def cream_label(txt, pos, font_size=20, txt_color=INK):
            t = Text(txt, color=txt_color, font_size=font_size)
            t.move_to(pos)
            bg = Rectangle(
                width=t.width + 0.18, height=t.height + 0.12,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bg.move_to(pos)
            return VGroup(bg, t)

        # ---- Title ----
        title = Text("EFFICIENT FRONTIER (MARKOWITZ)", color=INK, font_size=32, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # ---- Axes ----
        x_axis = Line((-5.0, -2.5, 0), (5.0, -2.5, 0), color=INK, stroke_width=2)
        y_axis = Line((-5.0, -2.5, 0), (-5.0, 2.5, 0), color=INK, stroke_width=2)

        # Tick labels — y-axis ticks on right side of y-axis to avoid overlap with axis label
        tick_labels = VGroup(
            cream_label("5%",   [-5.0, -2.9, 0]),
            cream_label("17.5%",[0.0, -2.9, 0]),
            cream_label("30%",  [5.0, -2.9, 0]),
            cream_label("4%",   [-4.3, -2.85, 0]),
            cream_label("9%",   [-4.3,  0.0, 0]),
            cream_label("14%",  [-4.3,  2.5, 0]),
        )

        # Axis labels placed in clear space
        x_axis_label = Text("Volatility (sigma)", color=SLATE, font_size=20)
        x_axis_label.move_to([0, -3.2, 0])
        # y-axis label positioned away from tick labels and frontier
        y_axis_label = Text("Return (mu)", color=SLATE, font_size=18)
        y_axis_label.rotate(1.5708)
        y_axis_label.move_to([-5.7, 0, 0])
        axis_labels = VGroup(x_axis_label, y_axis_label)

        # ---- Feasible dots (hardcoded) ----
        FEASIBLE_PTS = [
            (0.12,0.068),(0.14,0.072),(0.16,0.079),(0.18,0.085),(0.20,0.089),
            (0.22,0.092),(0.12,0.062),(0.15,0.074),(0.17,0.082),(0.20,0.084),
            (0.10,0.064),(0.13,0.071),(0.21,0.095),(0.24,0.107),(0.11,0.067),
        ]
        feasible_dots = []
        for sig, mu in FEASIBLE_PTS:
            d = Dot(radius=0.07, color=SLATE, fill_opacity=0.3)
            d.move_to([to_x(sig), to_y(mu), 0])
            feasible_dots.append(d)

        # ---- Individual asset dots ----
        # A1: sigma=0.10, mu=0.06  -> x=-3.0, y=-1.5
        # A2: sigma=0.15, mu=0.08  -> x=0.0,  y=-0.5
        # A3: sigma=0.20, mu=0.10  -> x=3.0 ... wait: to_x(0.20)=-5+(0.15/0.25)*10=1.0; to_y(0.10)=0.5
        # A4: sigma=0.25, mu=0.12  -> to_x(0.25)=3.0; to_y(0.12)=1.5
        ASSETS = [
            ("A1",  0.10, 0.06, "right"),    # x=-3.0, y=-1.5
            ("A2",  0.15, 0.08, "above"),    # x=0.0,  y=-0.5 (on frontier; place label differently)
            ("A3",  0.20, 0.10, "right"),    # x=1.0,  y=0.5
            ("A4",  0.25, 0.12, "right"),    # x=3.0,  y=1.5
        ]
        asset_dots = []
        asset_labels = []
        for name, sig, mu, side in ASSETS:
            px, py = to_x(sig), to_y(mu)
            d = Dot(radius=0.12, color=INK)
            d.move_to([px, py, 0])
            asset_dots.append(d)
            # Offset labels to avoid curves
            if side == "above":
                lbl_pos = [px - 0.7, py + 0.45, 0]  # A2 offset left and up
            else:
                lbl_pos = [px + 0.55, py + 0.25, 0]
            lbl = cream_label(name, lbl_pos, font_size=20, txt_color=INK)
            asset_labels.append(lbl)

        # ---- Min-variance and Max-Sharpe dots ----
        minvar_x, minvar_y = to_x(0.095), to_y(0.065)
        maxsharpe_x, maxsharpe_y = to_x(0.15), to_y(0.090)

        minvar_dot = Dot(radius=0.15, color="#0055AA")
        minvar_dot.move_to([minvar_x, minvar_y, 0])
        # Place min-var label lower-left, away from frontier
        minvar_label = cream_label("Min-Var", [minvar_x - 1.2, minvar_y - 0.5, 0], font_size=20, txt_color="#0055AA")

        maxsharpe_dot = Dot(radius=0.15, color=PASS_CLR)
        maxsharpe_dot.move_to([maxsharpe_x, maxsharpe_y, 0])
        # Place max-Sharpe label to upper-right, clear of the frontier line at that x
        maxsharpe_label = cream_label("Max-Sharpe", [maxsharpe_x + 1.5, maxsharpe_y + 0.7, 0], font_size=20, txt_color=PASS_CLR)

        # ---- Efficient frontier curve ----
        FRONTIER = [
            (0.095,0.065),(0.10,0.070),(0.11,0.076),(0.13,0.083),
            (0.15,0.090),(0.18,0.098),(0.22,0.108),(0.25,0.115)
        ]
        frontier_pts = [[to_x(s), to_y(m), 0] for s, m in FRONTIER]
        frontier_segs = VGroup()
        for i in range(len(frontier_pts) - 1):
            frontier_segs.add(Line(frontier_pts[i], frontier_pts[i+1], color=CRIMSON, stroke_width=3))
        frontier_curve = frontier_segs

        # Verdict placed at upper-left, clear of x-axis area
        verdict_text = cream_label("Max Sharpe: best return per unit of risk",
                                   [0.5, 2.0, 0], font_size=22, txt_color=INK)

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(*[FadeIn(d) for d in feasible_dots])
        self.play(*[FadeIn(d) for d in asset_dots], *[Write(l) for l in asset_labels])
        self.play(Create(frontier_curve))
        self.play(FadeIn(minvar_dot), Write(minvar_label), FadeIn(maxsharpe_dot), Write(maxsharpe_label))
        self.play(Write(verdict_text))
