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

# Coordinate mapping:
# gamma 1.0->3.0 maps to x=-5.0->5.0: x_plot = -5.0 + (gamma-1.0)/2.0 * 10.0
# p-value 0->0.20 maps to y=-2.5->2.5: y_plot = -2.5 + (p/0.20)*5.0

_CURVE_POINTS = [
    (1.0, 0.004),
    (1.5, 0.018),
    (2.0, 0.052),
    (2.5, 0.110),
    (3.0, 0.190),
]


def _to_plot(gamma, p):
    x = -5.0 + (gamma - 1.0) / 2.0 * 10.0
    y = -2.5 + (p / 0.20) * 5.0
    return [x, y, 0]


class B04_SensitivityLine(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title
        title_bg = Rectangle(width=9.0, height=0.5, fill_color=CREAM,
                              fill_opacity=1, stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title_txt = Text("SENSITIVITY ANALYSIS (ROSENBAUM BOUNDS)",
                         color=INK, weight=BOLD, font_size=30)
        title_txt.move_to([0, 3.2, 0])
        title = VGroup(title_bg, title_txt)

        # Axes (manual Lines — NO Axes class)
        x_axis = Line(start=[-5.0, -2.5, 0], end=[5.0, -2.5, 0],
                      color=INK, stroke_width=2)
        y_axis = Line(start=[-5.0, -2.5, 0], end=[-5.0, 2.5, 0],
                      color=INK, stroke_width=2)

        # Axis labels
        x_label_bg = Rectangle(width=5.5, height=0.35, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        x_label_bg.move_to([0, -3.0, 0])
        x_label_txt = Text("gamma (unmeasured confounding strength)",
                           color=SLATE, font_size=22)
        x_label_txt.move_to([0, -3.0, 0])
        x_label = VGroup(x_label_bg, x_label_txt)

        y_label_bg = Rectangle(width=1.2, height=0.35, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        y_label_bg.move_to([-5.8, 0.8, 0])
        y_label_txt = Text("p-value", color=SLATE, font_size=22)
        y_label_txt.rotate(PI / 2)
        y_label_txt.move_to([-5.8, 0.8, 0])
        y_label = VGroup(y_label_bg, y_label_txt)

        axis_labels = VGroup(x_label, y_label)

        # Tick labels with CREAM Rectangle backgrounds
        def tick_label(txt, pos):
            bg = Rectangle(width=0.7, height=0.3, fill_color=CREAM,
                            fill_opacity=1, stroke_width=0, stroke_opacity=0)
            bg.move_to(pos)
            t = Text(txt, color=SLATE, font_size=20)
            t.move_to(pos)
            return VGroup(bg, t)

        x_tick_1 = tick_label("1.0", [-5.0, -2.8, 0])
        x_tick_2 = tick_label("2.0", [0.0, -2.8, 0])
        x_tick_3 = tick_label("3.0", [5.0, -2.8, 0])

        # y_plot for p=0.05: -2.5 + (0.05/0.20)*5.0 = -2.5 + 1.25 = -1.25
        # y_plot for p=0.10: -2.5 + (0.10/0.20)*5.0 = -2.5 + 2.50 = 0.0
        # y_plot for p=0.20: -2.5 + (0.20/0.20)*5.0 = 2.5
        y_tick_0 = tick_label("0.00", [-5.4, -2.5, 0])
        y_tick_5 = tick_label("0.05", [-5.4, -1.25, 0])
        y_tick_10 = tick_label("0.10", [-5.4, 0.0, 0])
        y_tick_20 = tick_label("0.20", [-5.4, 2.5, 0])

        tick_labels = VGroup(x_tick_1, x_tick_2, x_tick_3,
                             y_tick_0, y_tick_5, y_tick_10, y_tick_20)

        # Significance dashed line at p=0.05 -> y=-1.25
        sig_line = DashedLine(start=[-5.0, -1.25, 0], end=[5.0, -1.25, 0],
                              color=CRIMSON, dash_length=0.2, stroke_width=2)
        sig_bg = Rectangle(width=1.2, height=0.35, fill_color=CREAM,
                            fill_opacity=1, stroke_width=0, stroke_opacity=0)
        sig_bg.move_to([4.5, -0.95, 0])
        sig_txt = Text("p = 0.05", color=CRIMSON, font_size=24)
        sig_txt.move_to([4.5, -0.95, 0])
        sig_label = VGroup(sig_bg, sig_txt)

        # Rising p-value line segments
        plot_pts = [_to_plot(g, p) for g, p in _CURVE_POINTS]
        line_segs = VGroup()
        for i in range(len(plot_pts) - 1):
            seg = Line(start=plot_pts[i], end=plot_pts[i + 1],
                       color=INK, stroke_width=3)
            line_segs.add(seg)
        p_value_line_group = line_segs

        # gamma* crossing: gamma=1.9, p=0.05 -> x=-0.5, y=-1.25
        # x_star = -5.0 + (1.9-1.0)/2.0 * 10.0 = -5.0 + 4.5 = -0.5
        gamma_star_dot = Dot(point=[-0.5, -1.25, 0], radius=0.12, color=CRIMSON)

        gamma_star_arrow = Arrow(start=[1.5, 1.5, 0], end=[-0.3, -1.1, 0],
                                 color=CRIMSON, buff=0, tip_length=0.15, stroke_width=2)

        gs_bg = Rectangle(width=2.5, height=0.4, fill_color=CREAM,
                           fill_opacity=1, stroke_width=0, stroke_opacity=0)
        gs_bg.move_to([3.0, 1.8, 0])
        gs_txt = Text("gamma* = 1.9", color=CRIMSON, weight=BOLD, font_size=28)
        gs_txt.move_to([3.0, 1.8, 0])
        gamma_star_label = VGroup(gs_bg, gs_txt)

        # Interpretation text
        interp_bg = Rectangle(width=7.0, height=0.35, fill_color=CREAM,
                               fill_opacity=1, stroke_width=0, stroke_opacity=0)
        interp_bg.move_to([0, -3.5, 0])
        interp_txt = Text("confounding factor of 1.9x would overturn result",
                          color=SLATE, font_size=26)
        interp_txt.move_to([0, -3.5, 0])
        interpretation_text = VGroup(interp_bg, interp_txt)

        # Sequence — 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis), FadeIn(axis_labels), FadeIn(tick_labels))
        self.play(FadeIn(sig_line), Write(sig_label))
        self.play(Create(p_value_line_group))
        self.play(FadeIn(gamma_star_dot), FadeIn(gamma_star_arrow), Write(gamma_star_label))
        self.play(Write(interpretation_text))
        self.wait(1)
