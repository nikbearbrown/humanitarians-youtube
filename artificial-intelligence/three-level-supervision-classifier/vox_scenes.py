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


class B04_SupervisionGrid(Scene):
    def construct(self):
        # Grid axes: x={-3,0,3} usage levels I/II/III; y={-1.5,0,1.5} supervision I/II/III
        USAGE_XS = [-3.0, 0.0, 3.0]
        SUPV_YS = [-1.5, 0.0, 1.5]

        title = Text("THREE LEVELS OF AI SUPERVISION", color=INK, font_size=34, weight=BOLD).move_to([0, 3.2, 0])

        # Horizontal grid lines
        h_grid = VGroup()
        for gy in SUPV_YS:
            h_grid.add(Line((-4.0, gy, 0), (4.0, gy, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4))

        # Vertical grid lines — only from y=0.0 to 2.0 to avoid crossing dot labels
        v_grid = VGroup()
        for gx in USAGE_XS:
            v_grid.add(Line((gx, 0.0, 0), (gx, 2.0, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4))

        grid_lines = VGroup(h_grid, v_grid)

        # Calibrated diagonal
        diagonal = DashedLine((-3.0, -1.5, 0), (3.0, 1.5, 0), color=INK, stroke_width=2, dash_length=0.3)
        diag_bg = Rectangle(width=2.4, height=0.35, fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to([1.5, 0.8, 0])
        diag_lbl = Text("Calibrated diagonal", color=INK, font_size=22).move_to([1.5, 0.8, 0])
        diagonal_label = VGroup(diag_bg, diag_lbl)

        # Danger corner rectangle (bottom-right: usage=III, supervision=I)
        danger_rect = Rectangle(width=1.6, height=1.2, fill_color=CRIMSON, fill_opacity=0.12,
                                stroke_width=0, stroke_opacity=0).move_to([3.0, -1.5, 0])
        # Place danger label at x=1.5 (left of the III column) to avoid overlap with level "3" label
        danger_bg = Rectangle(width=1.8, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([1.8, -2.2, 0])
        danger_lbl = Text("DANGER CORNER", color=CRIMSON, font_size=20, weight=BOLD).move_to([1.8, -2.2, 0])
        danger_label = VGroup(danger_bg, danger_lbl)

        # Axis labels — keep y-axis label; x-axis label omitted (level numbers suffice)
        y_axis_bg = Rectangle(width=1.5, height=0.6, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([-5.3, 0, 0])
        y_axis_lbl = Text("Supervision\nLevel", color=SLATE, font_size=18).move_to([-5.3, 0, 0])
        x_usage_bg = Rectangle(width=1.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -3.2, 0])
        x_usage_lbl = Text("Usage Level", color=SLATE, font_size=18).move_to([0, -3.2, 0])
        axis_labels = VGroup(y_axis_bg, y_axis_lbl, x_usage_bg, x_usage_lbl)

        # Level number labels on axes
        level_labels = VGroup()
        for i, (lbl_x, lbl_y) in enumerate([(-3.0, -2.6), (0.0, -2.6), (3.0, -2.6)]):
            bg = Rectangle(width=0.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([lbl_x, lbl_y, 0])
            txt = Text(str(i+1), color=INK, font_size=26).move_to([lbl_x, lbl_y, 0])
            level_labels.add(bg, txt)
        for i, sy in enumerate(SUPV_YS):
            bg = Rectangle(width=0.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([-4.5, sy, 0])
            txt = Text(str(i+1), color=INK, font_size=26).move_to([-4.5, sy, 0])
            level_labels.add(bg, txt)

        # Priya's 3 interaction dots — flat supervision at y=-1.5
        dot_a = Dot(point=[-3.0, -1.5, 0], radius=0.18, color=PASS_CLR,
                    fill_color=PASS_CLR, fill_opacity=1)
        dot_b = Dot(point=[0.0, -1.5, 0], radius=0.18, color=CRIMSON,
                    fill_color=CRIMSON, fill_opacity=1)
        dot_c = Dot(point=[3.0, -1.5, 0], radius=0.18, color=CRIMSON,
                    fill_color=CRIMSON, fill_opacity=1)

        priya_path_line = Line((-3.0, -1.5, 0), (3.0, -1.5, 0), color=SLATE, stroke_width=2)

        # Dot labels — placed ABOVE the dots at y=-0.9 (above the horizontal grid line at y=-1.5)
        dot_labels = VGroup()
        lbl_data = [
            ("Rename variables", -3.0, -0.9, INK),
            ("Market size claim", 0.0, -0.9, CRIMSON),
            ("Architecture proposal", 3.0, -0.9, CRIMSON),
        ]
        for txt_str, dx, dy, col in lbl_data:
            bg = Rectangle(width=2.4, height=0.35, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([dx, dy, 0])
            txt = Text(txt_str, color=col, font_size=18).move_to([dx, dy, 0])
            dot_labels.add(bg, txt)

        verdict_bg = Rectangle(width=5.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -2.8, 0])
        verdict_text = Text(
            "Same interface — three different supervision needs",
            color=INK, font_size=22
        ).move_to([0, -2.8, 0])

        # 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(grid_lines), FadeIn(axis_labels), FadeIn(level_labels))
        self.play(FadeIn(diagonal), Write(diagonal_label))
        self.play(FadeIn(danger_rect), Write(danger_label))
        self.play(
            FadeIn(dot_a), FadeIn(dot_b), FadeIn(dot_c),
            FadeIn(priya_path_line),
            *[Write(l) for l in dot_labels]
        )
        self.play(FadeIn(verdict_bg), Write(verdict_text))
