import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR = "#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_ProcessAuditBars(Scene):
    def construct(self):
        # state 1: title
        title_bg = Rectangle(width=10.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("Process Audit Score", font_size=36, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.3)

        BASE_Y = -2.0    # canvas y for score=0
        SCALE  = 0.875   # canvas units per score point
        x_left  = -4.8
        x_right =  4.5

        # state 2: axes + y-axis tick labels
        y_axis = Line([x_left, BASE_Y, 0], [x_left, BASE_Y + 4*SCALE + 0.2, 0],
                      stroke_color=INK, stroke_width=2)
        x_axis = Line([x_left, BASE_Y, 0], [x_right, BASE_Y, 0],
                      stroke_color=INK, stroke_width=2)
        axes_grp = VGroup(y_axis, x_axis)
        for s in range(5):
            tick_y = BASE_Y + s * SCALE
            tick = Line([x_left - 0.12, tick_y, 0], [x_left, tick_y, 0],
                        stroke_color=INK, stroke_width=1.5)
            lbl_bg = Rectangle(width=0.45, height=0.35, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([x_left - 0.45, tick_y, 0])
            lbl = Text(str(s), font_size=16, color=INK)
            lbl.move_to([x_left - 0.45, tick_y, 0])
            axes_grp.add(tick, lbl_bg, lbl)
        self.play(FadeIn(axes_grp), run_time=0.6)
        self.wait(0.25)

        sessions = [
            (-3.0, 2, CRIMSON,  "S1"),
            (-1.0, 3, PASS_CLR, "S2"),
            ( 1.0, 4, PASS_CLR, "S3"),
            ( 3.0, 1, CRIMSON,  "S4"),
        ]
        BAR_W = 1.2

        def make_bar_grp(sess):
            sx, score, clr, lbl_str = sess
            h = score * SCALE
            bar = Rectangle(width=BAR_W, height=h, fill_color=clr, fill_opacity=1.0, stroke_width=0, stroke_opacity=0)
            bar.move_to([sx, BASE_Y + h/2, 0])
            sc_bg = Rectangle(width=0.5, height=0.38, fill_color=CREAM, fill_opacity=1.0,
                               stroke_width=0, stroke_opacity=0)
            sc_bg.move_to([sx, BASE_Y + h + 0.28, 0])
            sc_txt = Text(str(score), font_size=18, color=clr)
            sc_txt.move_to([sx, BASE_Y + h + 0.28, 0])
            lb_bg = Rectangle(width=0.6, height=0.36, fill_color=CREAM, fill_opacity=1.0,
                               stroke_width=0, stroke_opacity=0)
            lb_bg.move_to([sx, BASE_Y - 0.38, 0])
            lb_txt = Text(lbl_str, font_size=16, color=INK)
            lb_txt.move_to([sx, BASE_Y - 0.38, 0])
            return VGroup(bar, sc_bg, sc_txt, lb_bg, lb_txt)

        # state 3: bar S1
        self.play(FadeIn(make_bar_grp(sessions[0])), run_time=0.55)
        self.wait(0.2)

        # state 4: bars S2–S3
        self.play(FadeIn(VGroup(make_bar_grp(sessions[1]),
                                make_bar_grp(sessions[2]))), run_time=0.55)
        self.wait(0.2)

        # state 5: bar S4
        self.play(FadeIn(make_bar_grp(sessions[3])), run_time=0.55)
        self.wait(0.2)

        # state 6: threshold line + label
        thresh_y = BASE_Y + 3 * SCALE   # 0.625
        thresh_line = Line([x_left, thresh_y, 0], [x_right, thresh_y, 0],
                            stroke_color=CRIMSON, stroke_width=2.5)
        tl_bg = Rectangle(width=4.2, height=0.42, fill_color=CREAM, fill_opacity=1.0,
                           stroke_width=0, stroke_opacity=0)
        tl_bg.move_to([1.8, 2.2, 0])
        tl_txt = Text("threshold: 3 / 4 — shareable output", font_size=16, color=CRIMSON)
        tl_txt.move_to([1.8, 2.2, 0])
        self.play(FadeIn(VGroup(thresh_line, tl_bg, tl_txt)), run_time=0.6)
        self.wait(0.3)

        # state 7: verdict annotations below bars
        vrd_grp = VGroup()
        for sx, score, clr, _ in sessions:
            verdict = "SHAREABLE" if score >= 3 else "NOT READY"
            v_bg = Rectangle(width=1.45, height=0.38, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
            v_bg.move_to([sx, BASE_Y - 0.78, 0])
            v_txt = Text(verdict, font_size=12, color=clr)
            v_txt.move_to([sx, BASE_Y - 0.78, 0])
            vrd_grp.add(v_bg, v_txt)
        self.play(FadeIn(vrd_grp), run_time=0.5)
        self.wait(1.0)
