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


class B04_DiscriminantThree(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)

        # Three panels: left (D>0), center (D=0), right (D<0)
        panel_data = [
            (-4.0, "D > 0\n2 real roots",   CRIMSON,  "Δ = b²−4ac > 0"),
            ( 0.0, "D = 0\n1 real root",    INK,      "Δ = b²−4ac = 0"),
            ( 4.0, "D < 0\n0 real roots",   SLATE,    "Δ = b²−4ac < 0"),
        ]

        # Draw panel boxes first
        for cx, desc, clr, formula in panel_data:
            box = Rectangle(width=3.5, height=5.5, fill_color=CREAM,
                           fill_opacity=1, stroke_color=clr, stroke_width=2)
            box.move_to([cx, -0.2, 0])
            self.play(GrowFromCenter(box), run_time=0.35)

        # Add x-axis baseline in each panel
        for cx, desc, clr, formula in panel_data:
            ax_line = Line(start=[cx - 1.5, -1.0, 0], end=[cx + 1.5, -1.0, 0],
                          color=SLATE, stroke_width=1.5)
            self.play(GrowFromCenter(ax_line), run_time=0.2)

        # Panel 1 (D>0): two x-intercepts — dots on the axis
        dot_l = Dot(point=[-4.8, -1.0, 0], color=CRIMSON, radius=0.13)
        dot_r = Dot(point=[-3.2, -1.0, 0], color=CRIMSON, radius=0.13)
        self.play(GrowFromCenter(dot_l), run_time=0.25)
        self.play(GrowFromCenter(dot_r), run_time=0.25)

        # Panel 1 label: "2 roots"
        lbl1 = Text("D > 0\n2 real roots", font="Prism", font_size=14, color=CRIMSON, weight=BOLD)
        lbl1.move_to([-4.0, -2.3, 0])
        self.play(FadeIn(lbl1), run_time=0.3)

        # Panel 2 (D=0): one tangent point — single dot on axis
        dot_t = Dot(point=[0.0, -1.0, 0], color=INK, radius=0.13)
        self.play(GrowFromCenter(dot_t), run_time=0.25)

        # Panel 2 label: "1 root"
        lbl2 = Text("D = 0\n1 real root", font="Prism", font_size=14, color=INK, weight=BOLD)
        lbl2.move_to([0.0, -2.3, 0])
        self.play(FadeIn(lbl2), run_time=0.3)

        # Panel 3 (D<0): no intercepts — X mark above axis
        x_box = Rectangle(width=0.5, height=0.5, fill_color=CREAM,
                          fill_opacity=1, stroke_color=SLATE, stroke_width=2)
        x_box.move_to([4.0, -1.0, 0])
        self.play(GrowFromCenter(x_box), run_time=0.25)

        # Panel 3 label: "0 roots"
        lbl3 = Text("D < 0\n0 real roots", font="Prism", font_size=14, color=SLATE, weight=BOLD)
        lbl3.move_to([4.0, -2.3, 0])
        self.play(FadeIn(lbl3), run_time=0.3)

        # Formulas in each panel
        for cx, desc, clr, formula in panel_data:
            fml = Text(formula, font="Prism", font_size=12, color=clr)
            fml.move_to([cx, -2.9, 0])
            self.play(FadeIn(fml), run_time=0.25)

        # Title at top
        title = Text("The Discriminant: Three Stories",
                     font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 2.8, 0])
        self.play(FadeIn(title), run_time=0.4)

        self.wait(max(0, dur - 6.0))


class B06_DiscriminantFormula(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("The Quadratic Formula and Its Diagnostic",
                     font="Prism", font_size=22, color=INK, weight=BOLD)
        title.move_to([0, 3.0, 0])
        self.play(FadeIn(title), run_time=0.4)

        formula = Text("x = (−b ± √(b²−4ac)) / 2a",
                       font="Prism", font_size=26, color=INK, weight=BOLD)
        formula.move_to([0, 2.1, 0])
        self.play(FadeIn(formula), run_time=0.5)

        # Gold highlight box for the discriminant (slightly ABOVE the label)
        disc_box = Rectangle(width=5.2, height=0.6, fill_color=GOLD,
                             fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        disc_box.move_to([0, 1.2, 0])
        self.play(GrowFromCenter(disc_box), run_time=0.4)

        # Label for discriminant placed clearly BELOW the box (not on it)
        disc_lbl = Text("b²−4ac  =  Δ  (the Discriminant)",
                        font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
        disc_lbl.move_to([0, 1.2, 0])
        self.play(FadeIn(disc_lbl), run_time=0.3)

        arr = Arrow(start=[0, 0.90, 0], end=[0, 0.30, 0], color=CRIMSON, stroke_width=2)
        self.play(GrowArrow(arr), run_time=0.3)

        cases = [
            ("Δ > 0", "two distinct real roots",   CRIMSON,  0.0),
            ("Δ = 0", "one repeated real root",     INK,     -0.75),
            ("Δ < 0", "no real roots (complex)",    SLATE,   -1.5),
        ]
        for d_str, desc, clr, y in cases:
            d = Text(d_str, font="Prism", font_size=20, color=clr, weight=BOLD)
            d.move_to([-3.5, y, 0])
            a = Arrow(start=[-2.8, y, 0], end=[-2.0, y, 0], color=clr, stroke_width=1.5)
            dt = Text(desc, font="Prism", font_size=17, color=clr)
            dt.move_to([-1.5, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(d), run_time=0.2)
            self.play(GrowArrow(a), run_time=0.3)
            self.play(FadeIn(dt), run_time=0.2)

        # Bottom dot as visual anchor
        bottom_dot = Dot(point=[0, -2.5, 0], color=CRIMSON, radius=0.12)
        self.play(GrowFromCenter(bottom_dot), run_time=0.2)

        self.wait(max(0, dur - 5.5))
