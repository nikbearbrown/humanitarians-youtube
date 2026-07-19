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


class B04_ColliderSim(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Collider Bias: Hiring as Collider", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        # DAG structure
        dag_box = Rectangle(width=7.0, height=0.65, fill_color=CREAM,
                            fill_opacity=1, stroke_color=SLATE, stroke_width=1.5)
        dag_box.move_to([0, 2.7, 0])
        self.play(GrowFromCenter(dag_box), run_time=0.3)
        dag_lbl = Text("Skill -> Hire <- Personality  (Hire is the collider)", font="Prism", font_size=15, color=SLATE)
        dag_lbl.move_to([0, 2.7, 0])
        self.play(FadeIn(dag_lbl), run_time=0.25)
        div = Line(start=[0, 2.2, 0], end=[0, -0.8, 0], color=SLATE, stroke_width=1.5)
        self.play(GrowFromEdge(div, UP), run_time=0.4)
        # Left panel: full population
        lh = Text("Full Population", font="Prism", font_size=17, color=INK, weight=BOLD)
        lh.move_to([-3.0, 1.9, 0])
        self.play(FadeIn(lh), run_time=0.25)
        lpop_box = Rectangle(width=4.5, height=0.6, fill_color=CREAM,
                             fill_opacity=1, stroke_width=0, stroke_opacity=0)
        lpop_box.move_to([-3.0, 1.3, 0])
        self.play(GrowFromCenter(lpop_box), run_time=0.3)
        lpop_lbl = Text("N = 5,000 candidates", font="Prism", font_size=14, color=SLATE)
        lpop_lbl.move_to([-3.0, 1.3, 0])
        self.play(FadeIn(lpop_lbl), run_time=0.2)
        lind_box = Rectangle(width=4.5, height=0.6, fill_color=CREAM,
                             fill_opacity=1, stroke_width=0, stroke_opacity=0)
        lind_box.move_to([-3.0, 0.6, 0])
        self.play(GrowFromCenter(lind_box), run_time=0.25)
        lind_lbl = Text("Skill, Personality: independent", font="Prism", font_size=14, color=SLATE)
        lind_lbl.move_to([-3.0, 0.6, 0])
        self.play(FadeIn(lind_lbl), run_time=0.2)
        lr_box = Rectangle(width=3.0, height=0.75, fill_color=CREAM,
                           fill_opacity=1, stroke_color=INK, stroke_width=2)
        lr_box.move_to([-3.0, -0.2, 0])
        self.play(GrowFromCenter(lr_box), run_time=0.35)
        lr_lbl = Text("r = 0.01", font="Prism", font_size=22, color=INK, weight=BOLD)
        lr_lbl.move_to([-3.0, -0.2, 0])
        self.play(FadeIn(lr_lbl), run_time=0.3)
        # Right panel: hired subset
        rh = Text("Hired Subset", font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        rh.move_to([3.0, 1.9, 0])
        self.play(FadeIn(rh), run_time=0.25)
        rsel_box = Rectangle(width=4.5, height=0.6, fill_color=CREAM,
                             fill_opacity=1, stroke_width=0, stroke_opacity=0)
        rsel_box.move_to([3.0, 1.3, 0])
        self.play(GrowFromCenter(rsel_box), run_time=0.3)
        rsel_lbl = Text("Hired: skill + personality > 1", font="Prism", font_size=14, color=CRIMSON)
        rsel_lbl.move_to([3.0, 1.3, 0])
        self.play(FadeIn(rsel_lbl), run_time=0.2)
        rn_box = Rectangle(width=4.5, height=0.6, fill_color=CREAM,
                           fill_opacity=1, stroke_width=0, stroke_opacity=0)
        rn_box.move_to([3.0, 0.6, 0])
        self.play(GrowFromCenter(rn_box), run_time=0.25)
        rn_lbl = Text("N ~1,600 (top ~32%)", font="Prism", font_size=14, color=SLATE)
        rn_lbl.move_to([3.0, 0.6, 0])
        self.play(FadeIn(rn_lbl), run_time=0.2)
        rr_box = Rectangle(width=3.0, height=0.75, fill_color=GOLD,
                           fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        rr_box.move_to([3.0, -0.2, 0])
        self.play(GrowFromCenter(rr_box), run_time=0.35)
        rr_lbl = Text("r = -0.65", font="Prism", font_size=22, color=CRIMSON, weight=BOLD)
        rr_lbl.move_to([3.0, -0.2, 0])
        self.play(FadeIn(rr_lbl), run_time=0.3)
        verdict_box = Rectangle(width=8.0, height=0.65, fill_color=CREAM,
                                fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        verdict_box.move_to([0, -1.2, 0])
        self.play(GrowFromCenter(verdict_box), run_time=0.35)
        verdict_lbl = Text("Conditioning on Hire opened the Skill-Personality path", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        verdict_lbl.move_to([0, -1.2, 0])
        self.play(FadeIn(verdict_lbl), run_time=0.3)
        self.wait(max(0, dur - 6.0))


class B06_ThresholdEffect(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Collider Bias vs. Hiring Threshold", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdr_line = Line(start=[-5.5, 2.4, 0], end=[5.5, 2.4, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        hdrs = ["Threshold", "Hired %", "Subset r", "Bias strength"]
        x_pos = [-3.5, -0.8, 1.5, 3.8]
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=15, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.7, 0])
            self.play(FadeIn(lbl), run_time=0.12)
        data = [
            ("strict (top 10%)",   "10%",  "-0.82", "STRONGEST",  CRIMSON, "#FFF0F0"),
            ("moderate (top 30%)", "30%",  "-0.65", "strong",     CRIMSON, CREAM),
            ("lenient (top 60%)",  "60%",  "-0.35", "moderate",   SLATE,   CREAM),
            ("no filter (100%)",   "100%", "0.01",  "none",       INK,     CREAM),
        ]
        y_top = 1.8
        for i, (thresh, pct, r_str, bias, clr, bg) in enumerate(data):
            y = y_top - i * 0.72
            row_bg = Rectangle(width=11.0, height=0.62, fill_color=bg, fill_opacity=0.7,
                               stroke_width=0, stroke_opacity=0)
            row_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(row_bg), run_time=0.2)
            th_lbl = Text(thresh, font="Prism", font_size=13, color=INK)
            th_lbl.move_to([x_pos[0], y, 0])
            pct_lbl = Text(pct, font="Prism", font_size=14, color=SLATE)
            pct_lbl.move_to([x_pos[1], y, 0])
            r_lbl = Text(r_str, font="Prism", font_size=15, color=clr, weight=BOLD)
            r_lbl.move_to([x_pos[2], y, 0])
            bias_lbl = Text(bias, font="Prism", font_size=13, color=clr, weight=BOLD if clr == CRIMSON else "NORMAL")
            bias_lbl.move_to([x_pos[3], y, 0])
            self.play(FadeIn(th_lbl), FadeIn(pct_lbl), FadeIn(r_lbl), FadeIn(bias_lbl), run_time=0.3)
        rule_box = Rectangle(width=8.0, height=0.65, fill_color=GOLD,
                             fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        rule_box.move_to([0, -1.1, 0])
        self.play(GrowFromCenter(rule_box), run_time=0.4)
        rule_lbl = Text("Stricter selection = stronger collider bias", font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        rule_lbl.move_to([0, -1.1, 0])
        self.play(FadeIn(rule_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
