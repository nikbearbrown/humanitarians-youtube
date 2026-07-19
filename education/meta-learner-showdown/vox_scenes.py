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


class B04_MetaLearnerMAE(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # ---- Title ----
        title = Text(
            "Meta-Learner Showdown: Who Estimates CATE Best?",
            color=INK, weight=BOLD, font_size=30
        )
        title.move_to([0, 3.2, 0])

        # ---- Data ----
        # MAE by age quartile for S/T/X learners
        s_mae = [3.2, 4.5, 5.8, 7.1]
        t_mae = [1.8, 2.2, 2.8, 3.5]
        x_mae = [1.2, 1.5, 1.9, 2.1]

        group_centers = [-3.75, -1.25, 1.25, 3.75]
        offsets = [-0.5, 0.0, 0.5]
        bar_colors = [SLATE, GOLD, PASS_CLR]
        bar_width = 0.38

        y_base = -2.5
        y_scale = 5.0 / 8.0  # units per MAE unit (max=8, height=5)

        # ---- Axes ----
        x_axis = Line(start=[-5.5,-2.5,0], end=[5.5,-2.5,0], color=INK, stroke_width=2)
        y_axis = Line(start=[-5.5,-2.5,0], end=[-5.5,2.6,0], color=INK, stroke_width=2)

        # y-ticks at MAE=0,2,4,6,8
        ytick_data = [(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8")]
        yticks = VGroup()
        for mae_val, lbl in ytick_data:
            yp = y_base + mae_val * y_scale
            tick = Line(start=[-5.5,yp,0], end=[-5.65,yp,0], color=INK, stroke_width=1.5)
            bg = Rectangle(width=0.4, height=0.28,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([-5.9, yp, 0])
            t = Text(lbl, font_size=18, color=INK)
            t.move_to([-5.9, yp, 0])
            yticks.add(tick, bg, t)

        # y-axis label
        yax_bg = Rectangle(width=2.8, height=0.35,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
        yax_bg.move_to([-5.0, 0.0, 0])
        yax_bg.rotate(PI/2)
        yax_lbl = Text("MAE vs. Ground Truth", font_size=18, color=SLATE)
        yax_lbl.rotate(PI/2)
        yax_lbl.move_to([-5.4, 0.0, 0])
        axes_grp = VGroup(x_axis, y_axis, yticks, yax_lbl)

        # ---- Build bars grouped by quartile ----
        all_mae_data = [s_mae, t_mae, x_mae]
        q_labels_text = ["Q1\n18-30", "Q2\n30-43", "Q3\n43-55", "Q4\n55-65"]

        q1_grp = VGroup()
        q2_grp = VGroup()
        q3_grp = VGroup()
        q4_grp = VGroup()
        q_groups = [q1_grp, q2_grp, q3_grp, q4_grp]

        for qi, (gc, ql) in enumerate(zip(group_centers, q_labels_text)):
            for li, (offset, color, mae_list) in enumerate(zip(offsets, bar_colors, all_mae_data)):
                mae = mae_list[qi]
                ht = mae * y_scale
                bar = Rectangle(
                    width=bar_width,
                    height=ht,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_width=0,
                    stroke_opacity=0
                )
                bar.move_to([gc + offset, y_base + ht/2, 0])
                q_groups[qi].add(bar)

            # Group label
            bg = Rectangle(width=1.2, height=0.55,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([gc, -2.85, 0])
            lbl = Text(ql, font_size=16, color=INK)
            lbl.move_to([gc, -2.85, 0])
            q_groups[qi].add(bg, lbl)

        # ---- Verdict annotation ----
        verdict_bg = Rectangle(width=3.2, height=1.0,
                               fill_color=GOLD, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0)
        verdict_bg.move_to([3.5, 2.2, 0])
        verdict_txt = Text("X-learner\n-66% error\nvs S-learner", font_size=20, color=INK)
        verdict_txt.move_to([3.5, 2.2, 0])
        verdict = VGroup(verdict_bg, verdict_txt)

        # ---- Legend ----
        legend_items = [
            (SLATE, "S-learner"),
            (GOLD, "T-learner"),
            (PASS_CLR, "X-learner"),
        ]
        legend = VGroup()
        lx = -2.5
        for color, label in legend_items:
            box = Rectangle(width=0.3, height=0.3,
                            fill_color=color, fill_opacity=1,
                            stroke_width=0, stroke_opacity=0)
            box.move_to([lx, -3.2, 0])
            bg = Rectangle(width=1.4, height=0.32,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0)
            bg.move_to([lx + 0.85, -3.2, 0])
            txt = Text(label, font_size=18, color=INK)
            txt.move_to([lx + 0.85, -3.2, 0])
            legend.add(box, bg, txt)
            lx += 2.5

        # ---- Animation ----
        self.play(Write(title))
        self.play(Create(axes_grp))
        self.play(FadeIn(q1_grp))
        self.play(FadeIn(q2_grp))
        self.play(FadeIn(q3_grp))
        self.play(FadeIn(q4_grp))
        self.play(FadeIn(legend), FadeIn(verdict))
        self.wait(1)
