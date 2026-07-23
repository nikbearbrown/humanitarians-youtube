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


class B04_LLNConvergence(Scene):
    def construct(self):
        # Pre-computed simulation runs (log_n, empirical_p)
        RUN1 = [(0,1.0),(1,0.7),(2,0.55),(3,0.508),(4,0.501),(5,0.4998)]
        RUN2 = [(0,0.0),(1,0.3),(2,0.46),(3,0.492),(4,0.499),(5,0.5003)]
        RUN3 = [(0,1.0),(1,0.6),(2,0.51),(3,0.505),(4,0.500),(5,0.5000)]

        def to_xy(log_n, p):
            x = -5.0 + (log_n / 5.0) * 10.0
            y = -2.2 + p * 4.4   # y range: -2.2 to 2.2 (keeps content in safe area)
            return (x, y, 0)

        def make_run_lines(pts, color, sw=1.0, opacity=0.6):
            segs = VGroup()
            for i in range(len(pts) - 1):
                x1, y1, _ = to_xy(*pts[i])
                x2, y2, _ = to_xy(*pts[i+1])
                segs.add(Line((x1,y1,0),(x2,y2,0),
                              color=color, stroke_width=sw, stroke_opacity=opacity))
            return segs

        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=len(txt)*0.12+0.15, height=0.32,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "LAW OF LARGE NUMBERS — CONVERGENCE",
            font_size=30, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Axes — shifted up slightly, y range -2.2 to 2.2
        AXIS_BOTTOM = -2.2
        AXIS_TOP    =  2.2
        x_axis = Line((-5.0, AXIS_BOTTOM,0),(5.0, AXIS_BOTTOM,0), color=INK, stroke_width=1.5)
        y_axis = Line((-5.0, AXIS_BOTTOM,0),(-5.0, AXIS_TOP,0), color=INK, stroke_width=1.5)

        # y=0 is now at p=0.5: to_xy(any, 0.5) → y = -2.2 + 0.5*4.4 = 0.0 ✓

        # x-tick labels at y = AXIS_BOTTOM - 0.38
        xt_y = AXIS_BOTTOM - 0.38
        x_lbl_1   = tick_label("n=1",       (-5.0, xt_y, 0))
        x_lbl_100 = tick_label("n=100",     (-1.0, xt_y, 0))
        x_lbl_100k= tick_label("n=100k",    ( 5.0, xt_y, 0))
        # x-axis description inline with ticks (no separate floating label)
        x_lbl_desc = tick_label("(log scale)", (1.7, xt_y, 0), fontsize=14)
        tick_labels = VGroup(x_lbl_1, x_lbl_100, x_lbl_100k, x_lbl_desc)

        # y-tick labels at x=-5.6
        y_lbl_0   = tick_label("0%",   (-5.6, AXIS_BOTTOM, 0))
        y_lbl_50  = tick_label("50%",  (-5.6, 0.0,         0))
        y_lbl_100 = tick_label("100%", (-5.6, AXIS_TOP,    0))
        axis_labels = VGroup(y_lbl_0, y_lbl_50, y_lbl_100)

        # Theoretical line at p=0.5 → y=0.0
        theoretical_line = DashedLine((-5.0,0.0,0),(5.0,0.0,0),
                                       color=INK, stroke_width=2, dash_length=0.12)
        # p=0.5 label at upper right, band label separated below
        th_lbl_bg = Rectangle(width=1.8, height=0.30, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((4.2, 0.28, 0))
        th_lbl = Text("p=0.5", font_size=17, color=INK).move_to((4.2, 0.28, 0))
        theoretical_label = VGroup(th_lbl_bg, th_lbl)

        # ±5% band: height=0.44 in y-space (0.1*4.4=0.44, i.e. ±5% of p)
        band_h = 0.1 * 4.4   # 0.44
        band = Rectangle(width=10.0, height=band_h,
                         fill_color=GOLD, fill_opacity=0.35,
                         stroke_width=0, stroke_opacity=0).move_to((0.0, 0.0, 0))
        # Band label at left side to avoid overlap with p=0.5 label
        band_lbl = tick_label("5% band", (-3.5, 0.32, 0), fontsize=15)

        # Simulation run lines
        run1_lines = make_run_lines(RUN1, SLATE)
        run2_lines = make_run_lines(RUN2, SLATE)
        run3_lines = make_run_lines(RUN3, SLATE)

        # Verdict at y=-2.9 (safe: ±3.4, height 0.32 → box from -2.74 to -3.06, fine)
        verdict_bg = Rectangle(width=8.8, height=0.38, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0, -2.9, 0))
        verdict_txt = Text("At n=100,000: all runs converge within 1% of truth",
                           font_size=22, color=CRIMSON, weight=BOLD).move_to((0, -2.9, 0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (6 play() calls) ---
        self.play(Write(title))
        self.play(
            FadeIn(x_axis), FadeIn(y_axis),
            FadeIn(tick_labels), FadeIn(axis_labels)
        )
        self.play(FadeIn(theoretical_line), Write(theoretical_label), FadeIn(band), FadeIn(band_lbl))
        self.play(Create(run1_lines))
        self.play(Create(run2_lines), Create(run3_lines))
        self.play(Write(verdict_text))
        self.wait(1)
