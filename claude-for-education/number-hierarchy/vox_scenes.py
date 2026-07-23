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


class B04_NumberHierarchy(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("The Number Hierarchy: N ⊂ Z ⊂ Q ⊂ R ⊂ C",
                     font="Prism", font_size=24, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        sets = [
            ("ℕ", "Natural\n{1,2,3…}",      CRIMSON),
            ("ℤ", "Integer\n{…−2,−1,0…}",   CRIMSON),
            ("ℚ", "Rational\n{p/q}",         INK),
            ("ℝ", "Real\n{+π,√2…}",          INK),
            ("ℂ", "Complex\n{a+bi}",         SLATE),
        ]
        xs = [-4.8, -2.4, 0.0, 2.4, 4.8]

        for i, ((sym, desc, clr), x) in enumerate(zip(sets, xs)):
            box = Rectangle(width=2.1, height=1.9, fill_color=CREAM,
                            fill_opacity=1, stroke_color=clr, stroke_width=2)
            box.move_to([x, 0.4, 0])
            sym_lbl = Text(sym, font="Prism", font_size=26, color=clr, weight=BOLD)
            sym_lbl.move_to([x, 0.9, 0])
            desc_lbl = Text(desc, font="Prism", font_size=12, color=SLATE)
            desc_lbl.move_to([x, 0.1, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(FadeIn(sym_lbl), FadeIn(desc_lbl), run_time=0.2)
            if i < len(sets) - 1:
                arr = Arrow(start=[x + 1.05, 0.4, 0], end=[xs[i+1] - 1.05, 0.4, 0],
                           color=INK, stroke_width=2)
                self.play(GrowArrow(arr), run_time=0.3)

        sub = Text("Each set is a proper subset of the next  (N ⊂ Z ⊂ Q ⊂ R ⊂ C)",
                   font="Prism", font_size=15, color=SLATE)
        sub.move_to([0, -1.4, 0])
        self.play(FadeIn(sub), run_time=0.3)
        self.wait(max(0, dur - 5.0))


class B06_NumberHierarchy2(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("Where Does Each Number Live?",
                     font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)

        rows = [
            ("3",      "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ  (all sets)", INK),
            ("−2",     "ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ  (not ℕ)",         INK),
            ("½",      "ℚ ⊂ ℝ ⊂ ℂ  (not ℤ or ℕ)",         INK),
            ("π",      "ℝ ⊂ ℂ  (irrational — not ℚ)",      CRIMSON),
            ("√−1",   "ℂ only  (not real)",                CRIMSON),
        ]
        y_top = 2.1
        for i, (num, membership, clr) in enumerate(rows):
            y = y_top - i * 0.85
            num_lbl = Text(num, font="Prism", font_size=24, color=clr, weight=BOLD)
            num_lbl.move_to([-5.2, y, 0])
            arr = Arrow(start=[-4.7, y, 0], end=[-3.9, y, 0], color=SLATE, stroke_width=1.5)
            mem_lbl = Text(membership, font="Prism", font_size=16, color=SLATE)
            mem_lbl.move_to([-3.6, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(num_lbl), run_time=0.2)
            self.play(GrowArrow(arr), run_time=0.3)
            self.play(FadeIn(mem_lbl), run_time=0.2)

        note = Text("π cannot be written as p/q — that is the definition of irrational.",
                    font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        note.move_to([0, -2.5, 0])
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0, dur - len(rows) * 0.7 - 1.5))
