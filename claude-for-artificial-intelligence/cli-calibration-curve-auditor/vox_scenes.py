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


class B04_CalibrationCurve(Scene):
    def construct(self):
        # Pre-computed calibration data points (hardcoded — no runtime random)
        LR_PTS = [
            (0.05, 0.06), (0.15, 0.15), (0.25, 0.24), (0.35, 0.34),
            (0.45, 0.44), (0.55, 0.54), (0.65, 0.63), (0.75, 0.74),
            (0.85, 0.85), (0.95, 0.94),
        ]
        RF_PTS = [
            (0.05, 0.02), (0.15, 0.07), (0.25, 0.12), (0.35, 0.22),
            (0.45, 0.35), (0.55, 0.48), (0.65, 0.63), (0.75, 0.73),
            (0.85, 0.78), (0.95, 0.82),
        ]

        def to_plot(p, frac):
            return (-5.0 + p * 10, -2.5 + frac * 5.0, 0)

        # ── Title ─────────────────────────────────────────────────────────────
        title = Text("CALIBRATION CURVE AUDIT", color=INK, weight=BOLD,
                     font_size=34).move_to([0, 3.2, 0])

        # ── Axes ──────────────────────────────────────────────────────────────
        x_axis = Line([-5.0, -2.5, 0], [5.0, -2.5, 0], color=INK, stroke_width=2)
        y_axis = Line([-5.0, -2.5, 0], [-5.0, 2.5, 0], color=INK, stroke_width=2)

        def tick_label(txt, pos, anchor="CENTER"):
            bg = Rectangle(width=0.65, height=0.32,
                            fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text(txt, color=SLATE, font_size=18).move_to(pos)
            return VGroup(bg, t)

        x_ticks = VGroup(
            tick_label("0%",   [-5.0, -2.9, 0]),
            tick_label("50%",  [ 0.0, -2.9, 0]),
            tick_label("100%", [ 5.0, -2.9, 0]),
        )
        y_ticks = VGroup(
            tick_label("0%",   [-5.55, -2.5, 0]),
            tick_label("50%",  [-5.55,  0.0, 0]),
            tick_label("100%", [-5.55,  2.5, 0]),
        )
        tick_labels = VGroup(x_ticks, y_ticks)

        # x-axis label: place at bottom, right half of screen, inside safe zone
        x_ax_bg = Rectangle(width=3.6, height=0.30, fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to([3.2, -3.1, 0])
        x_axis_label = Text("Mean Predicted Probability", color=SLATE, font_size=18
                            ).move_to([3.2, -3.1, 0])
        # y-axis label: inside frame at x=-4.8, no rotation to avoid line crossings
        y_bg = Rectangle(width=2.4, height=0.30, fill_color=CREAM, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([-4.2, 2.85, 0])
        y_axis_label = Text("Fraction of Positives", color=SLATE, font_size=16
                            ).move_to([-4.2, 2.85, 0])
        axis_labels = VGroup(VGroup(x_ax_bg, x_axis_label), VGroup(y_bg, y_axis_label))

        # ── Perfect-calibration diagonal ──────────────────────────────────────
        perfect_diagonal = Line([-5.0, -2.5, 0], [5.0, 2.5, 0],
                                color=SLATE, stroke_width=2, stroke_opacity=0.7)
        diag_bg = Rectangle(width=2.5, height=0.35,
                            fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to([-2.5, 0.5, 0])
        diagonal_label = Text("Perfect calibration", color=SLATE, font_size=22
                              ).move_to([-2.5, 0.5, 0])

        # ── LR curve (well-calibrated, green) ─────────────────────────────────
        lr_plot_pts = [to_plot(p, frac) for p, frac in LR_PTS]
        lr_segs = VGroup(*[
            Line(lr_plot_pts[i], lr_plot_pts[i + 1],
                 color=PASS_CLR, stroke_width=2.5)
            for i in range(len(lr_plot_pts) - 1)
        ])
        lr_dots = VGroup(*[Dot(pt, radius=0.10, color=PASS_CLR) for pt in lr_plot_pts])

        # ── RF curve (overconfident, crimson) ─────────────────────────────────
        rf_plot_pts = [to_plot(p, frac) for p, frac in RF_PTS]
        rf_segs = VGroup(*[
            Line(rf_plot_pts[i], rf_plot_pts[i + 1],
                 color=CRIMSON, stroke_width=2.5)
            for i in range(len(rf_plot_pts) - 1)
        ])
        rf_dots = VGroup(*[Dot(pt, radius=0.10, color=CRIMSON) for pt in rf_plot_pts])

        # ── Brier score annotations ────────────────────────────────────────────
        def brier_label(txt, pos, clr):
            w = len(txt) * 0.14 + 0.3
            bg = Rectangle(width=w, height=0.38,
                            fill_color=CREAM, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text(txt, color=clr, font_size=24).move_to(pos)
            return VGroup(bg, t)

        lr_brier = brier_label("Logistic Reg: Brier=0.08", [-2.0, 2.1, 0], PASS_CLR)
        rf_brier = brier_label("Random Forest: Brier=0.12", [-2.0, 1.6, 0], CRIMSON)

        # ── Gap arrow — overconfident zone (x=3.0: pred≈0.80) ────────────────
        # diagonal y at pred=0.80 → -2.5+0.80*5 = 1.5
        # RF empirical at pred~0.75-0.80 → y = -2.5+0.73*5 = 1.15
        gap_arrow = Arrow([4.2, 1.5, 0], [4.2, 1.15, 0],
                          color=CRIMSON, stroke_width=3,
                          buff=0, tip_length=0.2)
        gap_bg = Rectangle(width=2.1, height=0.32,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([4.5, 0.55, 0])
        gap_label = Text("overconfident gap", color=CRIMSON, font_size=20
                         ).move_to([4.5, 0.55, 0])

        # verdict at bottom-left, well separated from x_axis_label (right side)
        verdict_bg = Rectangle(width=4.4, height=0.40,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([-2.8, -3.2, 0])
        verdict_text = Text("High AUC != good calibration",
                            color=CRIMSON, weight=BOLD, font_size=26
                            ).move_to([-2.8, -3.2, 0])

        # ── 7 play() calls ────────────────────────────────────────────────────
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(y_axis),
                  FadeIn(tick_labels), FadeIn(axis_labels))
        self.play(Create(perfect_diagonal),
                  FadeIn(diag_bg), Write(diagonal_label))
        self.play(Create(lr_segs),
                  *[FadeIn(d) for d in lr_dots])
        self.play(Create(rf_segs),
                  *[FadeIn(d) for d in rf_dots])
        self.play(FadeIn(lr_brier), FadeIn(rf_brier))
        self.play(FadeIn(gap_arrow),
                  FadeIn(gap_bg), Write(gap_label),
                  FadeIn(verdict_bg), Write(verdict_text))
        self.wait(1)
