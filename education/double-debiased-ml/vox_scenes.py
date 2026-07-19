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


class B04_DMLNumberLine(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "Double ML: Partialling Out Confounders with Two Stages",
            color=INK, weight=BOLD, font_size=26
        )
        title.move_to([0, 3.2, 0])

        # ====================================================
        # TOP: DML Pipeline Boxes
        # Three boxes at y=1.8, connected by arrows
        # ====================================================
        box_y = 1.8
        box_centers = [-3.5, 0.0, 3.5]
        box_w = 3.0
        box_h = 0.65

        box1 = Rectangle(width=box_w, height=box_h,
                         fill_color=GOLD, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0)
        box1.move_to([-3.5, box_y, 0])
        txt1a = Text("RF: predict Y from X", font_size=19, color=INK, weight=BOLD)
        txt1a.move_to([-3.5, box_y + 0.1, 0])
        txt1b = Text("(Y residuals)", font_size=17, color=INK)
        txt1b.move_to([-3.5, box_y - 0.15, 0])

        box2 = Rectangle(width=box_w, height=box_h,
                         fill_color=GOLD, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0)
        box2.move_to([0.0, box_y, 0])
        txt2a = Text("RF: predict D from X", font_size=19, color=INK, weight=BOLD)
        txt2a.move_to([0.0, box_y + 0.1, 0])
        txt2b = Text("(D residuals)", font_size=17, color=INK)
        txt2b.move_to([0.0, box_y - 0.15, 0])

        box3 = Rectangle(width=box_w, height=box_h,
                         fill_color=CREAM, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0)
        box3.move_to([3.5, box_y, 0])
        txt3a = Text("OLS: Y-resid ~ D-resid", font_size=19, color=PASS_CLR, weight=BOLD)
        txt3a.move_to([3.5, box_y + 0.1, 0])
        txt3b = Text("-> causal estimate", font_size=17, color=PASS_CLR)
        txt3b.move_to([3.5, box_y - 0.15, 0])

        # Arrows between boxes
        arr1 = Arrow(start=[-2.0, box_y, 0], end=[-1.5, box_y, 0],
                     color=SLATE, buff=0, tip_length=0.2, stroke_width=2)
        arr2 = Arrow(start=[1.5, box_y, 0], end=[2.0, box_y, 0],
                     color=SLATE, buff=0, tip_length=0.2, stroke_width=2)

        # Step labels
        step1_bg = Rectangle(width=1.0, height=0.28,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        step1_bg.move_to([-3.5, 2.25, 0])
        step1 = Text("STEP 1", font_size=17, color=SLATE)
        step1.move_to([-3.5, 2.25, 0])

        step2_bg = Rectangle(width=1.0, height=0.28,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        step2_bg.move_to([0.0, 2.25, 0])
        step2 = Text("STEP 2", font_size=17, color=SLATE)
        step2.move_to([0.0, 2.25, 0])

        step3_bg = Rectangle(width=1.0, height=0.28,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        step3_bg.move_to([3.5, 2.25, 0])
        step3 = Text("STEP 3", font_size=17, color=SLATE)
        step3.move_to([3.5, 2.25, 0])

        dml_boxes = VGroup(
            box1, txt1a, txt1b,
            box2, txt2a, txt2b,
            box3, txt3a, txt3b,
            arr1, arr2,
            step1_bg, step1, step2_bg, step2, step3_bg, step3
        )

        # ====================================================
        # BOTTOM: Number Line
        # Range 0.8 to 2.4; x: -5.0 to 5.0; scale=6.25
        # x(v) = -5.0 + (v - 0.8) * 6.25
        # ====================================================
        nl_y = -1.2

        number_line = Line(start=[-5.5, nl_y, 0], end=[5.5, nl_y, 0],
                           color=INK, stroke_width=3)

        # Tick marks at 1.0, 1.2, 1.4, 1.6, 1.8, 2.0
        tick_vals = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
        tick_labels_str = ["1.0", "1.2", "1.4", "1.6", "1.8", "2.0"]
        tick_xs = [-5.0 + (v - 0.8)*6.25 for v in tick_vals]
        # = [-3.75, -2.5, -1.25, 0.0, 1.25, 2.5]

        ticks_grp = VGroup()
        for xp, lbl in zip(tick_xs, tick_labels_str):
            tick = Line(start=[xp, nl_y-0.1, 0], end=[xp, nl_y+0.1, 0],
                        color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.55, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, nl_y - 0.35, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([xp, nl_y - 0.35, 0])
            ticks_grp.add(tick, bg, t)

        # Markers
        # x(1.50) = -5.0 + 0.70*6.25 = -0.625 (Truth)
        # x(1.48) = -5.0 + 0.68*6.25 = -0.75 (DML)
        # x(1.95) = -5.0 + 1.15*6.25 = 2.1875 (OLS)
        x_truth = -5.0 + (1.50 - 0.8)*6.25
        x_dml = -5.0 + (1.48 - 0.8)*6.25
        x_ols = -5.0 + (1.95 - 0.8)*6.25

        # Truth: dashed vertical line
        truth_line = VGroup()
        y_lo = nl_y - 0.05
        y_hi = -0.3
        dash_step = 0.18
        yc = y_lo
        while yc < y_hi:
            y_end_seg = min(yc + 0.12, y_hi)
            truth_line.add(Line(start=[x_truth, yc, 0], end=[x_truth, y_end_seg, 0],
                                color=PASS_CLR, stroke_width=2))
            yc += dash_step

        truth_bg = Rectangle(width=1.4, height=0.3,
                             fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0)
        truth_bg.move_to([x_truth, -0.1, 0])
        truth_lbl = Text("Truth=1.50", font_size=18, color=PASS_CLR)
        truth_lbl.move_to([x_truth, -0.1, 0])
        truth_marker = VGroup(truth_line, truth_bg, truth_lbl)

        # DML: solid dot — label raised to 0.9 above line to clear number line
        dml_dot = Circle(radius=0.12, fill_color=INK, fill_opacity=1,
                         stroke_width=0)
        dml_dot.move_to([x_dml, nl_y, 0])
        dml_bg = Rectangle(width=1.3, height=0.3,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        dml_bg.move_to([x_dml, nl_y + 0.9, 0])
        dml_lbl = Text("DML=1.48", font_size=18, color=INK)
        dml_lbl.move_to([x_dml, nl_y + 0.9, 0])
        dml_marker = VGroup(dml_dot, dml_bg, dml_lbl)

        # OLS: solid dot (CRIMSON) — label shifted right to avoid tick "2.0" overlap
        ols_dot = Circle(radius=0.12, fill_color=CRIMSON, fill_opacity=1,
                         stroke_width=0)
        ols_dot.move_to([x_ols, nl_y, 0])
        ols_bg = Rectangle(width=1.3, height=0.3,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        # Shift label right by 0.6 to avoid overlap with "2.0" tick label
        ols_bg.move_to([x_ols + 0.6, nl_y - 0.6, 0])
        ols_lbl = Text("OLS=1.95", font_size=18, color=CRIMSON)
        ols_lbl.move_to([x_ols + 0.6, nl_y - 0.6, 0])
        ols_marker = VGroup(ols_dot, ols_bg, ols_lbl)

        # CI bracket: x(1.32)=-1.75; x(1.64)=0.25
        x_ci_lo = -5.0 + (1.32 - 0.8)*6.25
        x_ci_hi = -5.0 + (1.64 - 0.8)*6.25
        ci_y = nl_y - 0.5
        ci_line = Line(start=[x_ci_lo, ci_y, 0], end=[x_ci_hi, ci_y, 0],
                       color=INK, stroke_width=2)
        ci_cap_lo = Line(start=[x_ci_lo, ci_y-0.1, 0], end=[x_ci_lo, ci_y+0.1, 0],
                         color=INK, stroke_width=2)
        ci_cap_hi = Line(start=[x_ci_hi, ci_y-0.1, 0], end=[x_ci_hi, ci_y+0.1, 0],
                         color=INK, stroke_width=2)
        ci_bg = Rectangle(width=2.5, height=0.3,
                          fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        ci_bg.move_to([(x_ci_lo+x_ci_hi)/2, ci_y - 0.35, 0])
        ci_lbl = Text("95% CI [1.32, 1.64]", font_size=17, color=INK)
        ci_lbl.move_to([(x_ci_lo+x_ci_hi)/2, ci_y - 0.35, 0])
        ci_bracket = VGroup(ci_line, ci_cap_lo, ci_cap_hi, ci_bg, ci_lbl)

        # Verdicts
        v1_bg = Rectangle(width=7.5, height=0.35,
                          fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        v1_bg.move_to([0, -2.5, 0])
        v1 = Text("OLS BIAS: +0.45 (confounders inflate estimate)", font_size=19, color=CRIMSON)
        v1.move_to([0, -2.5, 0])

        v2_bg = Rectangle(width=7.5, height=0.35,
                          fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0)
        v2_bg.move_to([0, -2.9, 0])
        v2 = Text("DML ERROR: +0.02 (partialling out removes bias)", font_size=19, color=PASS_CLR)
        v2.move_to([0, -2.9, 0])

        verdicts = VGroup(v1_bg, v1, v2_bg, v2)

        # ---- Animation ----
        self.play(Write(title))
        self.play(FadeIn(dml_boxes))
        self.play(Create(number_line), Create(ticks_grp))
        self.play(FadeIn(truth_marker))
        self.play(FadeIn(dml_marker))
        self.play(FadeIn(ols_marker))
        self.play(FadeIn(ci_bracket), FadeIn(verdicts))
        self.wait(1)
