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


class B04_ExponentProof(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Proof: Why a⁰ = 1", font="Prism", font_size=30, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("Start with:",  "a³ ÷ a³",      INK),
            ("Quotient rule:","a^(3−3) = a⁰", INK),
            ("But also:",    "a³ ÷ a³ = 1",   INK),
            ("Therefore:",   "a⁰ = 1  ✓",     CRIMSON),
        ]
        y_start = 1.8
        for i, (prefix, expr, clr) in enumerate(steps):
            y = y_start - i * 0.9
            pre = Text(prefix, font="Prism", font_size=20, color=SLATE)
            pre.move_to([-1.8, y, 0], aligned_edge=RIGHT)
            exp = Text(expr, font="Prism", font_size=26, color=clr)
            exp.move_to([-1.5, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(pre), run_time=0.2)
            self.play(FadeIn(exp), run_time=0.35)

        box = Rectangle(width=4.0, height=0.7, fill_color=GOLD,
                        fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        box.move_to([0, -1.5, 0])
        box_lbl = Text("a⁰ = 1  for any a ≠ 0", font="Prism", font_size=22,
                       color=CRIMSON, weight=BOLD)
        box_lbl.move_to([0, -1.5, 0])
        self.play(GrowFromCenter(box), run_time=0.4)
        self.play(FadeIn(box_lbl), run_time=0.3)

        caveat = Text("Exception: 0⁰ is indeterminate (not covered by this rule).",
                      font="Prism", font_size=14, color=SLATE)
        caveat.move_to([0, -2.7, 0])
        self.play(FadeIn(caveat), run_time=0.3)
        self.wait(max(0, dur - 5.5))


class B06_ExponentRules(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("All Six Exponent Rules", font="Prism", font_size=28, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        rules = [
            ("Product:",      "aᵐ · aⁿ = aᵐ⁺ⁿ",   "2³·2²=2⁵=32"),
            ("Quotient:",     "aᵐ ÷ aⁿ = aᵐ⁻ⁿ",   "2⁵÷2²=2³=8"),
            ("Power:",        "(aᵐ)ⁿ = aᵐⁿ",       "(2³)²=2⁶=64"),
            ("Zero exp.:",    "a⁰ = 1",             "7⁰=1"),
            ("Negative exp.:", "a⁻ⁿ = 1/aⁿ",       "2⁻³=1/8"),
            ("Fract. exp.:",  "a^(1/n) = ⁿ√a",      "8^(1/3)=2"),
        ]
        y_top = 2.2
        for i, (name, rule, example) in enumerate(rules):
            y = y_top - i * 0.75
            dot = Dot(point=[-6.2, y, 0], color=CRIMSON, radius=0.10)
            n_lbl = Text(name, font="Prism", font_size=14, color=SLATE)
            n_lbl.move_to([-5.6, y, 0], aligned_edge=LEFT)
            r_lbl = Text(rule, font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
            r_lbl.move_to([-1.8, y, 0], aligned_edge=LEFT)
            e_lbl = Text(example, font="Prism", font_size=15, color=INK)
            e_lbl.move_to([2.5, y, 0], aligned_edge=LEFT)
            self.play(GrowFromCenter(dot), run_time=0.15)
            self.play(FadeIn(n_lbl), FadeIn(r_lbl), FadeIn(e_lbl), run_time=0.3)

        self.wait(max(0, dur - len(rules) * 0.45 - 1.0))
