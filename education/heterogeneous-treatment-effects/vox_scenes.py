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


class B04_HTEScatter(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Define AMBER inside construct to avoid class-level issues
        AMBER = "#E8A020"

        # ---- Title ----
        title = Text(
            "HTE: The Average Effect Hides the Subgroup Story",
            color=INK, weight=BOLD, font_size=28
        )
        title.move_to([0, 3.2, 0])

        # ====================================================
        # Scatter plot: biomarker vs CATE
        # x(b) = -5.0 + b*10.0
        # y(cate) = -2.5 + (cate + 0.05) * 13.51
        # ====================================================

        # Pre-computed dots (biomarker, CATE, color)
        DOTS = [
            (0.05, 0.06, SLATE),   (0.10, 0.04, SLATE),   (0.15, 0.09, GOLD),
            (0.20, 0.07, SLATE),   (0.25, 0.11, GOLD),     (0.30, 0.08, SLATE),
            (0.35, 0.12, GOLD),    (0.40, 0.14, GOLD),     (0.45, 0.10, GOLD),
            (0.50, 0.16, AMBER),   (0.55, 0.17, AMBER),    (0.60, 0.13, GOLD),
            (0.65, 0.18, AMBER),   (0.70, 0.19, AMBER),    (0.75, 0.22, PASS_CLR),
            (0.80, 0.21, PASS_CLR),(0.85, 0.25, PASS_CLR), (0.90, 0.24, PASS_CLR),
            (0.95, 0.27, PASS_CLR),(1.00, 0.23, PASS_CLR), (0.12, 0.05, SLATE),
            (0.58, 0.15, AMBER),   (0.78, 0.23, PASS_CLR), (0.42, 0.13, GOLD),
        ]

        def bm_to_x(b):
            return -5.0 + b * 10.0

        def cate_to_y(c):
            return -2.5 + (c + 0.05) * 13.51

        # Separate dots by quartile
        q1_dots = VGroup()
        q2_q3_dots = VGroup()
        q4_dots = VGroup()

        for (bm, cate, color) in DOTS:
            xp = bm_to_x(bm)
            yp = cate_to_y(cate)
            dot = Circle(radius=0.2, fill_color=color, fill_opacity=0.85, stroke_width=0)
            dot.move_to([xp, yp, 0])
            if color == SLATE:
                q1_dots.add(dot)
            elif color == PASS_CLR:
                q4_dots.add(dot)
            else:
                q2_q3_dots.add(dot)

        # Trend line: from (b=0, CATE=0.05) to (b=1.0, CATE=0.25)
        # y(0.05) = -2.5 + 0.10*13.51 = -1.149; at x=-5.0
        # y(0.25) = -2.5 + 0.30*13.51 = 1.553; at x=5.0
        trend_line = VGroup()
        t_x0 = -5.0; t_y0 = -1.149
        t_x1 = 5.0;  t_y1 = 1.553
        dash_step_x = 0.6
        x = t_x0
        while x < t_x1:
            x_end = min(x + 0.4, t_x1)
            frac0 = (x - t_x0) / (t_x1 - t_x0)
            frac1 = (x_end - t_x0) / (t_x1 - t_x0)
            y0 = t_y0 + frac0 * (t_y1 - t_y0)
            y1 = t_y0 + frac1 * (t_y1 - t_y0)
            trend_line.add(Line(start=[x, y0, 0], end=[x_end, y1, 0],
                                color=SLATE, stroke_width=2))
            x += dash_step_x

        # ---- Axes ----
        x_axis = Line(start=[-5.5,-2.5,0], end=[5.5,-2.5,0], color=INK, stroke_width=2)
        y_axis = Line(start=[-5.5,-2.5,0], end=[-5.5,2.5,0], color=INK, stroke_width=2)

        # x-ticks at biomarker 0, 0.25, 0.50, 0.75, 1.0
        xtick_data = [(0.0, "0"), (0.25, "0.25"), (0.50, "0.50"), (0.75, "0.75"), (1.0, "1.0")]
        xticks = VGroup()
        for bm, lbl in xtick_data:
            xp = bm_to_x(bm)
            tick = Line(start=[xp,-2.5,0], end=[xp,-2.65,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.65, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([xp, -2.85, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([xp, -2.85, 0])
            xticks.add(tick, bg, t)

        # y-ticks at CATE 0.0, 0.10, 0.20, 0.30
        ytick_data = [(0.0, "0"), (0.10, "0.10"), (0.20, "0.20"), (0.30, "0.30")]
        ytick_ys = [
            -2.5 + 0.05*13.51,   # -1.824  (CATE=0.0)
            -2.5 + 0.15*13.51,   # -0.474  (CATE=0.10)
            -2.5 + 0.25*13.51,   #  0.878  (CATE=0.20)
            -2.5 + 0.35*13.51,   #  2.229  (CATE=0.30)
        ]
        yticks = VGroup()
        for yp, lbl in zip(ytick_ys, [d[1] for d in ytick_data]):
            tick = Line(start=[-5.5,yp,0], end=[-5.65,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.65, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([-5.95, yp, 0])
            t = Text(lbl, font_size=17, color=INK)
            t.move_to([-5.95, yp, 0])
            yticks.add(tick, bg, t)

        # x-axis label
        xax_bg = Rectangle(width=2.2, height=0.30,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        xax_bg.move_to([0.0, -3.1, 0])
        xax_lbl = Text("Biomarker Score", font_size=20, color=INK)
        xax_lbl.move_to([0.0, -3.1, 0])

        axes = VGroup(x_axis, y_axis, xticks, yticks, xax_bg, xax_lbl)

        # ---- Annotation Boxes ----
        # Top quartile box
        top_bg = Rectangle(width=2.8, height=0.85,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        top_bg.move_to([3.5, 2.0, 0])
        top_txt = Text("TOP QUARTILE\nmean CATE: 0.23\n(biomarker>0.70)",
                       font_size=17, color=PASS_CLR)
        top_txt.move_to([3.5, 2.0, 0])
        top_ann = VGroup(top_bg, top_txt)

        # Bottom quartile box
        bot_bg = Rectangle(width=2.8, height=0.85,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        bot_bg.move_to([-3.5, 1.5, 0])
        bot_txt = Text("BOT QUARTILE\nmean CATE: 0.06\n(biomarker<0.25)",
                       font_size=17, color=SLATE)
        bot_txt.move_to([-3.5, 1.5, 0])
        bot_ann = VGroup(bot_bg, bot_txt)

        annotation_boxes = VGroup(top_ann, bot_ann)

        # ---- Legend ----
        legend_items = [
            (SLATE, "Low benefit (Q1)"),
            (GOLD, "Moderate (Q2)"),
            (AMBER, "High (Q3)"),
            (PASS_CLR, "Top benefit (Q4)"),
        ]
        legend = VGroup()
        lx = -4.5
        for color, label in legend_items:
            dot_l = Circle(radius=0.12, fill_color=color, fill_opacity=0.85, stroke_width=0)
            dot_l.move_to([lx, -3.3, 0])
            bg = Rectangle(width=2.0, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([lx + 1.2, -3.3, 0])
            txt = Text(label, font_size=16, color=INK)
            txt.move_to([lx + 1.2, -3.3, 0])
            legend.add(dot_l, bg, txt)
            lx += 2.8

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(trend_line))
        self.play(FadeIn(q1_dots))
        self.play(FadeIn(q2_q3_dots))
        self.play(FadeIn(q4_dots))
        self.play(FadeIn(legend), FadeIn(annotation_boxes))
        self.wait(1)
