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


class B04_UnitCircle(Scene):
    def construct(self):
        import math
        dur = DUR.get("B04", 20.0)
        title = Text("The Unit Circle", font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        R = 1.8; cx, cy = -2.0, 0.0
        circle = Circle(radius=R, color=INK, stroke_width=2.5, fill_opacity=0)
        circle.move_to([cx, cy, 0])
        self.play(Create(circle), run_time=0.5)
        x_ax = Line(start=[cx-2.2, cy, 0], end=[cx+2.2, cy, 0], color=SLATE, stroke_width=1.5)
        y_ax = Line(start=[cx, cy-2.2, 0], end=[cx, cy+2.2, 0], color=SLATE, stroke_width=1.5)
        self.play(Create(x_ax), Create(y_ax), run_time=0.4)
        theta = math.pi / 4
        px = cx + R * math.cos(theta)
        py = cy + R * math.sin(theta)
        pt = Dot(point=[px, py, 0], color=CRIMSON, radius=0.14)
        self.play(GrowFromCenter(pt), run_time=0.25)
        radius_line = Line(start=[cx, cy, 0], end=[px, py, 0], color=CRIMSON, stroke_width=2.5)
        self.play(Create(radius_line), run_time=0.4)
        cos_line = Line(start=[cx, cy, 0], end=[px, cy, 0], color=INK, stroke_width=2)
        self.play(Create(cos_line), run_time=0.3)
        sin_line = Line(start=[px, cy, 0], end=[px, py, 0], color=CRIMSON, stroke_width=3)
        self.play(Create(sin_line), run_time=0.3)
        cos_box = Rectangle(width=3.5, height=0.5, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        cos_box.move_to([2.5, 1.0, 0])
        self.play(FadeIn(cos_box), run_time=0.1)
        cos_lbl = Text("cos = sqrt(2)/2", font="Prism", font_size=17, color=INK)
        cos_lbl.move_to([2.5, 1.0, 0])
        self.play(FadeIn(cos_lbl), run_time=0.25)
        sin_box = Rectangle(width=3.5, height=0.5, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        sin_box.move_to([2.5, 0.2, 0])
        self.play(FadeIn(sin_box), run_time=0.1)
        sin_lbl = Text("sin = sqrt(2)/2", font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        sin_lbl.move_to([2.5, 0.2, 0])
        self.play(FadeIn(sin_lbl), run_time=0.25)
        theta_arc = Arc(radius=0.4, start_angle=0, angle=theta, arc_center=[cx, cy, 0],
                        color=SLATE, stroke_width=2)
        self.play(Create(theta_arc), run_time=0.35)
        theta_bg = Rectangle(width=1.2, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        theta_bg.move_to([cx+0.6, cy+0.18, 0])
        self.play(FadeIn(theta_bg), run_time=0.1)
        theta_lbl = Text("45 deg", font="Prism", font_size=15, color=SLATE)
        theta_lbl.move_to([cx+0.6, cy+0.18, 0])
        self.play(FadeIn(theta_lbl), run_time=0.25)
        pt_bg = Rectangle(width=1.8, height=0.35, fill_color=CREAM, fill_opacity=1, stroke_width=0)
        pt_bg.move_to([px+0.9, py+0.3, 0])
        self.play(FadeIn(pt_bg), run_time=0.1)
        pt_lbl = Text("(cos, sin)", font="Prism", font_size=14, color=CRIMSON)
        pt_lbl.move_to([px+0.9, py+0.3, 0])
        self.play(FadeIn(pt_lbl), run_time=0.25)
        self.wait(max(0, dur - 6.0))


class B06_SineWave(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Key Angles and Exact Values", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.1, 0])
        self.play(FadeIn(title), run_time=0.4)
        hdr_line = Line(start=[-5.5, 2.3, 0], end=[5.5, 2.3, 0], color=INK, stroke_width=2)
        self.play(Create(hdr_line), run_time=0.3)
        hdrs = ["theta", "deg", "sin", "cos", "tan"]
        x_pos = [-4.0, -2.0, 0.0, 2.0, 4.0]
        for h, xp in zip(hdrs, x_pos):
            lbl = Text(h, font="Prism", font_size=17, color=SLATE, weight=BOLD)
            lbl.move_to([xp, 2.6, 0])
            self.play(FadeIn(lbl), run_time=0.15)
        data = [
            ("0","0","0","1","0"),
            ("pi/6","30","1/2","sqrt3/2","1/sqrt3"),
            ("pi/4","45","sqrt2/2","sqrt2/2","1"),
            ("pi/3","60","sqrt3/2","1/2","sqrt3"),
            ("pi/2","90","1","0","undef"),
            ("pi","180","0","-1","0"),
        ]
        y_top = 1.8
        for i, row in enumerate(data):
            y = y_top - i * 0.67
            row_line = Line(start=[-5.5, y-0.33, 0], end=[5.5, y-0.33, 0], color=SLATE, stroke_width=0.8)
            self.play(Create(row_line), run_time=0.1)
            for j, (val, xp) in enumerate(zip(row, x_pos)):
                clr = CRIMSON if j in [2, 3] else INK
                bg = Rectangle(width=1.6, height=0.5, fill_color=CREAM, fill_opacity=1, stroke_width=0)
                bg.move_to([xp, y, 0])
                self.play(FadeIn(bg), run_time=0.05)
                lbl = Text(val, font="Prism", font_size=16, color=clr)
                lbl.move_to([xp, y, 0])
                self.play(FadeIn(lbl), run_time=0.08)
        special_box = Rectangle(width=11.0, height=0.6, fill_color=GOLD,
                                fill_opacity=0.5, stroke_color=CRIMSON, stroke_width=1.5)
        special_box.move_to([0, y_top - 2*0.67, 0])
        self.play(GrowFromCenter(special_box), run_time=0.35)
        self.wait(max(0, dur - 5.0))
