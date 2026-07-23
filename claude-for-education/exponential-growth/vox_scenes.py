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


class B04_ExponentialGrowth(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Exponential vs Linear Growth", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        header_line = Line(start=[-5.5, 2.0, 0], end=[5.5, 2.0, 0], color=INK, stroke_width=2)
        self.play(Create(header_line), run_time=0.4)
        hdr_x = Text("x", font="Prism", font_size=18, color=SLATE, weight=BOLD)
        hdr_x.move_to([-4.0, 2.3, 0])
        hdr_lin = Text("2x (linear)", font="Prism", font_size=18, color=SLATE, weight=BOLD)
        hdr_lin.move_to([-1.5, 2.3, 0])
        hdr_exp = Text("2^x (exponential)", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        hdr_exp.move_to([2.5, 2.3, 0])
        self.play(FadeIn(hdr_x), FadeIn(hdr_lin), FadeIn(hdr_exp), run_time=0.3)
        data = [(0,0,1),(1,2,2),(2,4,4),(3,6,8),(4,8,16),(5,10,32)]
        y_top = 1.5; row_gap = 0.65
        for i, (x, lin, exp) in enumerate(data):
            y = y_top - i * row_gap
            row_line = Line(start=[-5.5, y-0.32, 0], end=[5.5, y-0.32, 0], color=SLATE, stroke_width=0.7)
            x_lbl = Text(str(x), font="Prism", font_size=18, color=INK)
            x_lbl.move_to([-4.0, y, 0])
            lin_lbl = Text(str(lin), font="Prism", font_size=18, color=INK)
            lin_lbl.move_to([-1.5, y, 0])
            clr = CRIMSON if exp > lin else INK
            exp_lbl = Text(str(exp), font="Prism", font_size=18, color=clr)
            exp_lbl.move_to([2.5, y, 0])
            self.play(Create(row_line), FadeIn(x_lbl), FadeIn(lin_lbl), FadeIn(exp_lbl), run_time=0.3)
        tie_box = Rectangle(width=11.0, height=0.55, fill_color=GOLD,
                            fill_opacity=0.4, stroke_color=CRIMSON, stroke_width=1.5)
        tie_box.move_to([0, 1.5 - 2*0.65, 0])
        self.play(GrowFromCenter(tie_box), run_time=0.35)
        self.wait(max(0, dur - 5.0))


class B06_CompoundInterest(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("A = P(1+r/n)^(nt)", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        formula_box = Rectangle(width=8.0, height=0.7, fill_color=CREAM,
                                fill_opacity=1, stroke_color=INK, stroke_width=2)
        formula_box.move_to([0, 2.5, 0])
        self.play(GrowFromCenter(formula_box), run_time=0.35)
        formula_lbl = Text("P=$1000, r=10%, t=10 yrs", font="Prism", font_size=17, color=INK)
        formula_lbl.move_to([0, 2.5, 0])
        self.play(FadeIn(formula_lbl), run_time=0.3)
        data = [
            ("n=1","annual","$2,594"),
            ("n=4","quarterly","$2,685"),
            ("n=12","monthly","$2,707"),
            ("n=365","daily","$2,718"),
        ]
        header_line = Line(start=[-5.5, 1.9, 0], end=[5.5, 1.9, 0], color=INK, stroke_width=2)
        self.play(Create(header_line), run_time=0.3)
        y_top = 1.5
        for i, (n_str, freq, A_str) in enumerate(data):
            y = y_top - i * 0.65
            n_lbl = Text(n_str, font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
            n_lbl.move_to([-4.0, y, 0])
            freq_lbl = Text(freq, font="Prism", font_size=16, color=SLATE)
            freq_lbl.move_to([0.0, y, 0])
            A_lbl = Text(A_str, font="Prism", font_size=16, color=INK)
            A_lbl.move_to([3.5, y, 0])
            row_line = Line(start=[-5.5, y-0.32, 0], end=[5.5, y-0.32, 0], color=SLATE, stroke_width=0.7)
            self.play(Create(row_line), FadeIn(n_lbl), FadeIn(freq_lbl), FadeIn(A_lbl), run_time=0.3)
        cont_box = Rectangle(width=11.0, height=0.7, fill_color=GOLD,
                             fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        cont_box.move_to([0, y_top - 4*0.65, 0])
        self.play(GrowFromCenter(cont_box), run_time=0.35)
        cont_n = Text("n=inf", font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        cont_n.move_to([-4.0, y_top - 4*0.65, 0])
        cont_freq = Text("continuous", font="Prism", font_size=16, color=SLATE)
        cont_freq.move_to([0.0, y_top - 4*0.65, 0])
        cont_A = Text("$2,718", font="Prism", font_size=16, color=INK)
        cont_A.move_to([3.5, y_top - 4*0.65, 0])
        self.play(FadeIn(cont_n), FadeIn(cont_freq), FadeIn(cont_A), run_time=0.3)
        euler_lbl = Text("A = Pe^(rt) at n = inf", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        euler_lbl.move_to([0, -2.8, 0])
        self.play(FadeIn(euler_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
