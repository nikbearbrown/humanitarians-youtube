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


class B04_PolicyWelfare(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "Policy Learning: Budget-Constrained Welfare Maximization",
            color=INK, weight=BOLD, font_size=26
        )
        title.move_to([0, 3.2, 0])

        # ====================================================
        # Three bars: Random / Top-k / Threshold
        # y_base=-2.0; scale=0.05; max=88
        # ====================================================
        y_base = -2.0
        bar_scale = 0.05
        bar_width = 2.5
        bar_centers = [-3.5, 0.0, 3.5]
        bar_vals = [50, 85, 88]
        bar_colors_list = [SLATE, GOLD, PASS_CLR]
        bar_value_strs = ["50", "85 (+70%)", "88 (+76%)"]
        bar_label_strs = ["Random\n30%", "Top-k by\nCATE", "Threshold\n(optimal)"]

        # Axes
        x_axis = Line(start=[-5.0,-2.0,0], end=[5.0,-2.0,0], color=INK, stroke_width=2)
        y_axis = Line(start=[-5.0,-2.0,0], end=[-5.0,2.5,0], color=INK, stroke_width=2)

        # y-ticks at 0, 25, 50, 75
        ytick_data = [(0, "0", -2.0), (25, "25", -0.75), (50, "50", 0.5), (75, "75", 1.75)]
        yticks = VGroup()
        for val, lbl, yp in ytick_data:
            tick = Line(start=[-5.0,yp,0], end=[-5.15,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.45, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([-5.4, yp, 0])
            t = Text(lbl, font_size=18, color=INK)
            t.move_to([-5.4, yp, 0])
            yticks.add(tick, bg, t)

        # y-axis title — placed at top-left corner well away from axis line
        yax_bg = Rectangle(width=3.0, height=0.55,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        yax_bg.move_to([-3.5, 2.8, 0])
        yax_lbl = Text("Incremental outcomes per 1000 users", font_size=17, color=SLATE)
        yax_lbl.move_to([-3.5, 2.8, 0])

        axes_grp = VGroup(x_axis, y_axis, yticks, yax_bg, yax_lbl)

        # ---- Bars ----
        random_bar_grp = VGroup()
        topk_bar_grp = VGroup()
        threshold_bar_grp = VGroup()
        bar_groups = [random_bar_grp, topk_bar_grp, threshold_bar_grp]

        for i, (xc, val, color, val_str, lbl_str) in enumerate(zip(
                bar_centers, bar_vals, bar_colors_list,
                bar_value_strs, bar_label_strs)):
            ht = val * bar_scale
            bar = Rectangle(
                width=bar_width, height=ht,
                fill_color=color, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bar.move_to([xc, y_base + ht/2, 0])

            # Value label above bar
            val_y = y_base + ht + 0.2
            val_bg = Rectangle(width=1.8, height=0.3,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
            val_bg.move_to([xc, val_y, 0])
            val_lbl = Text(val_str, font_size=19, color=INK, weight=BOLD)
            val_lbl.move_to([xc, val_y, 0])

            # Group label below x-axis
            lbl_bg = Rectangle(width=1.8, height=0.55,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([xc, -2.45, 0])
            lbl_txt = Text(lbl_str, font_size=19, color=INK)
            lbl_txt.move_to([xc, -2.45, 0])

            bar_groups[i].add(bar, val_bg, val_lbl, lbl_bg, lbl_txt)

        # Budget annotation
        budget_bg = Rectangle(width=9.0, height=0.35,
                              fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0)
        budget_bg.move_to([0, -3.1, 0])
        budget_ann = Text(
            "All policies use same 30% treatment budget — 3,000 users of 10,000",
            font_size=19, color=SLATE
        )
        budget_ann.move_to([0, -3.1, 0])
        budget_annotation = VGroup(budget_bg, budget_ann)

        # Improvement annotation: CRIMSON Rectangle framing top-k and threshold
        improvement_rect = Rectangle(
            width=5.5, height=4.8,
            fill_opacity=0,
            stroke_color=CRIMSON,
            stroke_width=2
        )
        improvement_rect.move_to([1.75, 0.3, 0])

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(axes_grp))
        self.play(FadeIn(random_bar_grp))
        self.play(FadeIn(topk_bar_grp))
        self.play(FadeIn(threshold_bar_grp))
        self.play(FadeIn(budget_annotation))
        self.play(FadeIn(improvement_rect))
        self.wait(1)
