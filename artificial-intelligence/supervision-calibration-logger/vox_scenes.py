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


class B04_SupervisionDots(Scene):
    def construct(self):
        import numpy as np
        rng = np.random.default_rng(42)

        USAGE_XS = [-3.0, 0.0, 3.0]
        SUPV_YS = [-1.5, 0.0, 1.5]

        # Pre-defined demo log: (usage_level_x, supervision_level_y, is_gap)
        DEMO_LOG = [
            (-3.0, -1.5, False),
            (-3.0, -1.5, False),
            (0.0,   0.0, False),
            (0.0,  -1.5, True),
            (3.0,  -1.5, True),
            (-3.0,  0.0, False),
            (0.0,  -1.5, True),
            (3.0,   0.0, True),
            (-3.0, -1.5, False),
            (0.0,   0.0, False),
            (3.0,  -1.5, True),
            (3.0,   0.0, True),
        ]

        title = Text("SUPERVISION CALIBRATION LOG — 1 WEEK", color=INK, font_size=30, weight=BOLD).move_to([0, 3.2, 0])

        # Grid lines
        grid_lines = VGroup()
        for gy in SUPV_YS:
            grid_lines.add(Line((-4.0, gy, 0), (4.0, gy, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4))
        for gx in USAGE_XS:
            grid_lines.add(Line((gx, -2.2, 0), (gx, 2.2, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4))

        # Diagonal
        diagonal = DashedLine((-3.0, -1.5, 0), (3.0, 1.5, 0), color=INK, stroke_width=2, dash_length=0.3)

        # Axis labels
        # Only y-axis label; x-axis label omitted to avoid line collision
        y_ax_bg = Rectangle(width=1.5, height=0.6, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-5.2, 0, 0])
        y_ax_lbl = Text("Supervision\nLevel", color=SLATE, font_size=20).move_to([-5.2, 0, 0])
        usage_level_bg = Rectangle(width=3.5, height=0.35, fill_color=CREAM, fill_opacity=1,
                                  stroke_width=0, stroke_opacity=0).move_to([0, 2.6, 0])
        usage_level_lbl = Text("Usage Level ->  I  /  II  /  III", color=SLATE, font_size=18).move_to([0, 2.6, 0])
        axis_labels = VGroup(y_ax_bg, y_ax_lbl, usage_level_bg, usage_level_lbl)

        # Danger corner
        danger_rect = Rectangle(width=1.8, height=1.4, fill_color=CRIMSON, fill_opacity=0.12,
                               stroke_width=0, stroke_opacity=0).move_to([3.0, -1.5, 0])
        danger_bg = Rectangle(width=1.6, height=0.35, fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0).move_to([3.0, -2.4, 0])
        danger_lbl = Text("DANGER CORNER", color=CRIMSON, font_size=20, weight=BOLD).move_to([3.0, -2.4, 0])
        danger_label = VGroup(danger_bg, danger_lbl)

        # Build dots with small jitter
        calibrated_dots = VGroup()
        gap_dots = VGroup()
        oversupervised_dots = VGroup()

        for bx, by, is_gap in DEMO_LOG:
            jx = float(rng.uniform(-0.18, 0.18))
            jy = float(rng.uniform(-0.18, 0.18))
            dx = bx + jx
            dy = by + jy
            # Determine color
            # Calibrated: on or above diagonal (supervision >= usage)
            # Over-supervised: supervision > usage (above diagonal)
            # Gap: below diagonal
            if not is_gap and by > -1.5:
                # over-supervised (above calibrated)
                color = GOLD
                fill_col = GOLD
                oversupervised_dots.add(
                    Dot(point=[dx, dy, 0], radius=0.15, color=color, fill_color=fill_col, fill_opacity=1)
                )
            elif not is_gap:
                color = PASS_CLR
                fill_col = PASS_CLR
                calibrated_dots.add(
                    Dot(point=[dx, dy, 0], radius=0.15, color=color, fill_color=fill_col, fill_opacity=1)
                )
            else:
                color = CRIMSON
                fill_col = CRIMSON
                gap_dots.add(
                    Dot(point=[dx, dy, 0], radius=0.15, color=color, fill_color=fill_col, fill_opacity=1)
                )

        # Combine calibrated and over-supervised as "calibrated_dots" group
        all_calibrated = VGroup(calibrated_dots, oversupervised_dots)

        # Calibration score labels — keep within safe area (y > -3.4)
        calibration_score = Text(
            "Calibration score: 6/12 (50%)",
            color=CRIMSON, font_size=26
        ).move_to([0, -2.6, 0])

        gap_count_label = Text(
            "3 Level III with <2 min verify — gap",
            color=CRIMSON, font_size=22
        ).move_to([0, -3.0, 0])

        # 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(grid_lines), FadeIn(diagonal), FadeIn(axis_labels))
        self.play(FadeIn(danger_rect), Write(danger_label))
        self.play(*[FadeIn(d) for d in all_calibrated])
        self.play(*[FadeIn(d) for d in gap_dots])
        self.play(Write(calibration_score), Write(gap_count_label))
