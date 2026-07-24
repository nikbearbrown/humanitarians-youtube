import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_CognitiveLaborChart(Scene):
    def construct(self):
        # Title — state 1
        title_bg = Rectangle(width=9.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("Cognitive Labor Audit", font_size=36, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.4)

        objectives = [
            "Summarize Claude output",
            "Compare AI responses",
            "Evaluate source credibility",
            "Form claim with evidence",
        ]
        splits = [
            (0.10, 0.10, 0.80),
            (0.20, 0.30, 0.50),
            (0.70, 0.20, 0.10),
            (0.60, 0.30, 0.10),
        ]

        BAR_W     = 7.5
        BAR_H     = 0.50
        x_bar_lft = -2.0
        lbl_cx    = -4.0
        y_pos     = [2.2, 1.3, 0.4, -0.5]

        for i, (obj, (s_f, sh_f, a_f)) in enumerate(zip(objectives, splits)):
            y = y_pos[i]

            lbl_bg = Rectangle(width=3.4, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([lbl_cx, y, 0])
            lbl_txt = Text(obj, font_size=19, color=INK)
            lbl_txt.move_to([lbl_cx, y, 0])

            s_w  = BAR_W * s_f
            sh_w = BAR_W * sh_f
            a_w  = BAR_W * a_f

            s_rect  = Rectangle(width=s_w,  height=BAR_H, fill_color=GOLD,    fill_opacity=1.0, stroke_width=0)
            sh_rect = Rectangle(width=sh_w, height=BAR_H, fill_color=SLATE,   fill_opacity=0.85, stroke_width=0)
            a_rect  = Rectangle(width=a_w,  height=BAR_H, fill_color=CRIMSON, fill_opacity=1.0, stroke_width=0)
            s_rect.move_to( [x_bar_lft + s_w/2,              y, 0])
            sh_rect.move_to([x_bar_lft + s_w + sh_w/2,       y, 0])
            a_rect.move_to( [x_bar_lft + s_w + sh_w + a_w/2, y, 0])

            # states 2–5
            self.play(FadeIn(VGroup(lbl_bg, lbl_txt, s_rect, sh_rect, a_rect)), run_time=0.65)
            self.wait(0.2)

        # Summary bar — state 6
        y_sum = -1.65
        sep = Line([-5.8, y_sum + 0.48, 0], [5.8, y_sum + 0.48, 0],
                   stroke_color=INK, stroke_width=1.5)

        sum_lbl_bg = Rectangle(width=3.4, height=0.58, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
        sum_lbl_bg.move_to([lbl_cx, y_sum, 0])
        sum_lbl = Text("OVERALL RATIO", font_size=19, color=INK, weight=BOLD)
        sum_lbl.move_to([lbl_cx, y_sum, 0])

        BIG_H = BAR_H * 1.3
        s_w   = BAR_W * 0.40
        sh_w  = BAR_W * 0.225
        a_w   = BAR_W * 0.375

        sum_s  = Rectangle(width=s_w,  height=BIG_H, fill_color=GOLD,    fill_opacity=1.0, stroke_width=0)
        sum_sh = Rectangle(width=sh_w, height=BIG_H, fill_color=SLATE,   fill_opacity=0.85, stroke_width=0)
        sum_a  = Rectangle(width=a_w,  height=BIG_H, fill_color=CRIMSON, fill_opacity=1.0, stroke_width=0)
        sum_s.move_to( [x_bar_lft + s_w/2,              y_sum, 0])
        sum_sh.move_to([x_bar_lft + s_w + sh_w/2,       y_sum, 0])
        sum_a.move_to( [x_bar_lft + s_w + sh_w + a_w/2, y_sum, 0])

        ratio_bg  = Rectangle(width=2.0, height=0.44, fill_color=CREAM, fill_opacity=1.0,
                               stroke_width=0, stroke_opacity=0)
        ratio_txt = Text("40% student", font_size=17, color=INK)
        ratio_bg.move_to( [x_bar_lft + s_w/2, y_sum, 0])
        ratio_txt.move_to([x_bar_lft + s_w/2, y_sum, 0])

        self.play(FadeIn(VGroup(sep, sum_lbl_bg, sum_lbl, sum_s, sum_sh, sum_a,
                                ratio_bg, ratio_txt)), run_time=0.9)
        self.wait(0.5)

        # Legend — state 7
        leg_y = -3.1
        lg = VGroup()
        leg_x = -5.0
        for clr, label in [(GOLD, "Student"), (SLATE, "Shared"), (CRIMSON, "AI-performed")]:
            box = Rectangle(width=0.44, height=0.36, fill_color=clr, fill_opacity=1.0, stroke_width=0)
            box.move_to([leg_x, leg_y, 0])
            lb_bg = Rectangle(width=2.2, height=0.38, fill_color=CREAM, fill_opacity=1.0,
                               stroke_width=0, stroke_opacity=0)
            lb_bg.move_to([leg_x + 1.35, leg_y, 0])
            lb = Text(label, font_size=19, color=INK)
            lb.move_to([leg_x + 1.35, leg_y, 0])
            lg.add(box, lb_bg, lb)
            leg_x += 4.0

        self.play(FadeIn(lg), run_time=0.5)
        self.wait(1.0)
