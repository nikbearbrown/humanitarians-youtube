"""vox_scenes.py — Why Adding Any Perturbation Always Pushes the Ground State Down
(vox-second-order-negative, slate cut, 16:9)

Color law: TEAL = downward contribution (negative, correct for ground state)
           CRIMSON = would-be upward contribution (absent for ground state)
EXCLUSIONS: no formula derivation, no sum-over-states, no variational comparison,
            no excited-state behavior.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _level(y, w=5.0, color=INK, sw=2.5):
    ln = Line(LEFT * w / 2, RIGHT * w / 2, color=color, stroke_width=sw)
    ln.move_to(UP * y)
    return ln


def _down_arrow(x, y_top, y_bot, color=TEAL):
    a = Arrow(start=UP * y_top + RIGHT * x, end=UP * y_bot + RIGHT * x,
              color=color, stroke_width=3, buff=0.05,
              max_tip_length_to_length_ratio=0.25)
    return a


# ── B01: COLD OPEN — physicist tries electric field, gets negative ────────────
class B01_ElectricField(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Hydrogen + electric field", font=DISPLAY,
                     font_size=32, color=INK).move_to(UP * 3.1)
        # Two rows: first-order and second-order
        row1 = Text("First-order correction:", font=SERIF, font_size=26,
                    color=INK, slant=ITALIC).move_to(LEFT * 2.5 + UP * 0.8)
        val1 = Text("0  (symmetry)", font=MONO, font_size=26,
                    color=INK).move_to(RIGHT * 2.2 + UP * 0.8)
        row2 = Text("Second-order correction:", font=SERIF, font_size=26,
                    color=INK, slant=ITALIC).move_to(LEFT * 2.0 + DOWN * 0.4)
        val2 = Text("negative", font=MONO, font_size=26,
                    color=TEAL).move_to(RIGHT * 2.8 + DOWN * 0.4)
        arrow_down = Arrow(start=RIGHT * 2.8 + DOWN * 0.1,
                           end=RIGHT * 2.8 + DOWN * 1.1,
                           color=TEAL, stroke_width=3, buff=0.0,
                           max_tip_length_to_length_ratio=0.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(row1), FadeIn(val1), run_time=dur * 0.30)
        self.play(FadeIn(row2), FadeIn(val2), GrowArrow(arrow_down), run_time=dur * 0.40)
        self.wait(dur * 0.30)


# ── B02: COLD OPEN — tries quartic, random: always negative ──────────────────
class B02_AlwaysNegative(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        perturbations = ["Electric field", "Quartic bump", "Random H'"]
        results = ["negative", "negative", "negative"]
        rows = VGroup()
        for i, (pert, res) in enumerate(zip(perturbations, results)):
            y = 1.2 - i * 1.2
            lbl = Text(pert + ":", font=SERIF, font_size=24, color=INK,
                       slant=ITALIC).move_to(LEFT * 2.8 + UP * y)
            val = Text(res, font=DISPLAY, font_size=24, color=TEAL).move_to(RIGHT * 1.5 + UP * y)
            arr = Arrow(start=RIGHT * 2.6 + UP * y,
                        end=RIGHT * 2.6 + UP * (y - 0.5),
                        color=TEAL, stroke_width=2.5, buff=0.0,
                        max_tip_length_to_length_ratio=0.35)
            rows.add(VGroup(lbl, val, arr))
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=dur * 0.25)
        self.wait(dur * 0.25)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────


# ── B04: THE PROBLEM — sum structure ─────────────────────────────────────────
class B04_SumStructure(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("Second-order energy correction", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        # Show the schematic: sum over m≠n of (numerator / denominator)
        eq_parts = [
            ("E", INK), ("(2)", INK), ("  =  sum over m ", INK),
            ("[", INK), (" |matrix element|^2 ", TEAL),
            (" / ", INK), (" (E_0 - E_m) ", CRIMSON), ("]", INK)
        ]
        line = VGroup()
        x = -5.5
        for txt, col in eq_parts:
            t = Text(txt, font=MONO, font_size=22, color=col)
            t.move_to(RIGHT * x + t.width / 2 * RIGHT + DOWN * 0.1)
            x += t.width + 0.05
            line.add(t)
        line.center()
        num_lbl = Text("numerator", font=SERIF, font_size=20, color=TEAL,
                       slant=ITALIC).move_to(LEFT * 1.2 + DOWN * 1.4)
        den_lbl = Text("denominator", font=SERIF, font_size=20, color=CRIMSON,
                       slant=ITALIC).move_to(RIGHT * 1.8 + DOWN * 1.4)
        num_arrow = Arrow(num_lbl.get_top(), LEFT * 1.5 + UP * 0.1,
                          color=TEAL, stroke_width=2, buff=0.05)
        den_arrow = Arrow(den_lbl.get_top(), RIGHT * 2.2 + UP * 0.1,
                          color=CRIMSON, stroke_width=2, buff=0.05)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(line), run_time=dur * 0.45)
        self.play(FadeIn(num_lbl), GrowArrow(num_arrow),
                  FadeIn(den_lbl), GrowArrow(den_arrow), run_time=dur * 0.35)
        self.wait(dur * 0.20)


# ── B05: THE PROBLEM — numerator is always non-negative ──────────────────────
class B05_NumeratorSign(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        title = Text("The numerator: always >= 0", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        box = Rectangle(width=6.5, height=2.0)
        box.set_fill(TEAL, 0.08).set_stroke(TEAL, 2.0)
        box.move_to(UP * 0.3)
        expr = Text("|<m | H' | n>|^2  =  z * conjugate(z)  >=  0",
                    font=MONO, font_size=24, color=TEAL).move_to(UP * 0.3)
        note = Text("A number times its own conjugate is never negative.",
                    font=SERIF, font_size=22, color=INK,
                    slant=ITALIC).move_to(DOWN * 1.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(box), FadeIn(expr), run_time=dur * 0.40)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=dur * 0.30)
        self.wait(dur * 0.30)


# ── B06: STILL·ai — every excited level sits above ground state ──────────────
# STILL beat — no scene class


# ── B07: THE MECHANISM — energy level diagram ────────────────────────────────
class B07_LevelDiagram(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Ground state at bottom, excited states stacked above
        ys = [-2.0, -0.5, 0.8, 1.9, 2.8]
        labels = ["ground state", "E_1", "E_2", "E_3", "..."]
        colors = [TEAL, INK, INK, INK, INK]
        levels = VGroup()
        level_labels = VGroup()
        for y, lbl, col in zip(ys, labels, colors):
            ln = _level(y, w=4.5, color=col, sw=2.5 if y == -2.0 else 1.8)
            lbl_t = Text(lbl, font=SERIF, font_size=20, color=col,
                         slant=ITALIC).move_to(RIGHT * 3.2 + UP * y)
            levels.add(ln)
            level_labels.add(lbl_t)
        bracket = Brace(VGroup(levels[1], levels[-1]), RIGHT, color=INK)
        brace_lbl = SerifLabel("excited levels", INK, size=22).next_to(bracket, RIGHT, buff=0.15)
        self.play(Create(levels[0]), FadeIn(level_labels[0]), run_time=0.5)
        self.play(LaggedStart(*[Create(levels[i]) for i in range(1, 5)],
                              lag_ratio=0.2), run_time=dur * 0.40)
        self.play(LaggedStart(*[FadeIn(level_labels[i]) for i in range(1, 5)],
                              lag_ratio=0.15), run_time=dur * 0.25)
        self.play(FadeIn(bracket), FadeIn(brace_lbl), run_time=dur * 0.15)
        self.wait(dur * 0.20)


# ── B08: THE MECHANISM — each term: positive / negative = negative ───────────
class B08_SignAnalysis(Scene):
    def construct(self):
        dur = DUR.get("B08", 11.0)
        # Level diagram with downward arrows from each excited state to ground
        ys_excited = [-0.5, 0.8, 1.9, 2.8]
        y_ground = -2.0
        gnd = _level(y_ground, w=5.5, color=TEAL, sw=3.0)
        excited_levels = VGroup(*[_level(y, w=5.5, color=INK, sw=1.8) for y in ys_excited])
        arrows = VGroup()
        for y in ys_excited:
            arr = _down_arrow(x=0.0, y_top=y - 0.12, y_bot=y_ground + 0.18,
                              color=TEAL)
            arrows.add(arr)
        neg_label = LabelChip("E_0 - E_m < 0", accent=CRIMSON, size=22)
        neg_label.move_to(RIGHT * 4.0 + UP * 0.2)
        pos_label = LabelChip("|...|^2 >= 0", accent=TEAL, size=22)
        pos_label.move_to(RIGHT * 4.0 + UP * 1.1)
        result = Text("Each term: positive / negative = negative",
                      font=SERIF, font_size=22, color=TEAL,
                      slant=ITALIC).move_to(DOWN * 3.2)
        self.play(Create(gnd), Create(excited_levels), run_time=0.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
                  run_time=dur * 0.40)
        self.play(FadeIn(pos_label), FadeIn(neg_label), run_time=dur * 0.20)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B09: THE MECHANISM — sum of all negatives is negative ────────────────────
class B09_SumNegative(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        # Accumulate negative terms visually as a stack of downward bars
        bar_values = [0.9, 0.5, 0.3, 0.18, 0.12, 0.08]  # bar heights (all go down)
        x_start = -4.5
        bar_w = 0.9
        gap = 0.25
        y_baseline = 1.8
        bars = VGroup()
        for i, h in enumerate(bar_values):
            x = x_start + i * (bar_w + gap)
            bar = Rectangle(width=bar_w, height=h)
            bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
            bar.move_to(RIGHT * x + UP * (y_baseline - h / 2))
            bars.add(bar)
        baseline = Line(LEFT * 5.5, RIGHT * 3.0, color=INK, stroke_width=1.5)
        baseline.move_to(UP * y_baseline)
        total_bar = Rectangle(width=1.2, height=sum(bar_values))
        total_bar.set_fill(TEAL, 0.5).set_stroke(TEAL, 2.0)
        total_bar.move_to(RIGHT * 3.5 + UP * (y_baseline - sum(bar_values) / 2))
        total_lbl = LabelChip("total < 0", accent=TEAL, size=26)
        total_lbl.next_to(total_bar, DOWN, buff=0.3)
        # Arrow pointing down from total bar
        total_arr = Arrow(start=RIGHT * 3.5 + UP * y_baseline,
                          end=RIGHT * 3.5 + UP * (y_baseline - sum(bar_values) - 0.1),
                          color=TEAL, stroke_width=3, buff=0.0)
        self.play(Create(baseline), run_time=0.4)
        self.play(LaggedStart(*[GrowFromEdge(b, UP) for b in bars], lag_ratio=0.12),
                  run_time=dur * 0.45)
        self.play(FadeIn(total_bar), GrowArrow(total_arr), run_time=dur * 0.25)
        self.play(FadeIn(total_lbl), run_time=dur * 0.15)
        self.wait(dur * 0.15)


# ── B10: THE MECHANISM — section CARD, no scene class ───────────────────────


# ── B11: THE IMPLICATION — connection to variational principle ────────────────
class B11_VariationalConnection(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        # Show the energy floor E0 with a marker sliding toward it from above
        floor = _level(-2.0, w=7.0, color=TEAL, sw=3.0)
        floor_lbl = LabelChip("E_0 (ground state)", accent=TEAL, size=24)
        floor_lbl.next_to(floor, RIGHT, buff=0.3)
        marker = Dot(radius=0.18, color=CRIMSON).move_to(UP * 2.0)
        marker_lbl = SerifLabel("any trial energy", CRIMSON, size=22)
        marker_lbl.next_to(marker, RIGHT, buff=0.2)
        arrow_down = Arrow(start=UP * 2.0, end=UP * (-1.7),
                           color=CRIMSON, stroke_width=3, buff=0.0,
                           max_tip_length_to_length_ratio=0.2)
        note = Text("Never goes below E_0", font=DISPLAY, font_size=26,
                    color=TEAL).move_to(DOWN * 3.2)
        self.play(Create(floor), FadeIn(floor_lbl), run_time=0.5)
        self.play(FadeIn(marker), FadeIn(marker_lbl), run_time=dur * 0.25)
        self.play(GrowArrow(arrow_down), run_time=dur * 0.35)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B12: THE IMPLICATION — universal floor for ground state ──────────────────
class B12_UniversalFloor(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        # Three systems, each with an arrow pointing down from ground state
        systems = ["atom", "molecule", "oscillator"]
        x_positions = [-3.8, 0.0, 3.8]
        all_items = VGroup()
        for x, sys_name in zip(x_positions, systems):
            lbl = LabelChip(sys_name, accent=SLATE, size=22).move_to(RIGHT * x + UP * 1.5)
            gnd = _level(-0.2, w=2.5, color=TEAL, sw=2.5)
            gnd.move_to(RIGHT * x + UP * 0.3)
            arr = Arrow(start=RIGHT * x + UP * 0.2,
                        end=RIGHT * x + DOWN * 1.2,
                        color=TEAL, stroke_width=3, buff=0.0,
                        max_tip_length_to_length_ratio=0.3)
            note = Text("E^(2) < 0", font=MONO, font_size=20, color=TEAL)
            note.next_to(arr, DOWN, buff=0.15)
            all_items.add(VGroup(lbl, gnd, arr, note))
        rule = Text("Add any perturbation: ground state can only go down.",
                    font=SERIF, font_size=22, color=INK,
                    slant=ITALIC).move_to(DOWN * 3.2)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.3) for item in all_items],
                              lag_ratio=0.25), run_time=dur * 0.55)
        self.play(FadeIn(rule, shift=UP * 0.1), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B13: THE EXAMPLE — illustrative particle-in-a-box terms ─────────────────
class B13_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 16.0)
        title = Text("Illustrative: particle-in-a-box + tilt", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.1)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        # Linear tilt terms
        linear_title = SerifLabel("linear tilt  V = eps*x/L", TEAL, size=22)
        linear_title.move_to(LEFT * 3.5 + UP * 1.5)
        linear_terms = [("term 1:", "-0.031"),
                        ("term 2:", "-0.0014"),
                        ("term 3:", "-0.00018"),
                        ("total:", "-0.034")]
        lin_group = VGroup()
        for i, (t_lbl, val) in enumerate(linear_terms):
            y = 0.8 - i * 0.65
            tl = Text(t_lbl, font=MONO, font_size=20, color=INK).move_to(LEFT * 4.6 + UP * y)
            tv = Text(val + " eps^2", font=MONO, font_size=20, color=TEAL).move_to(LEFT * 2.0 + UP * y)
            lin_group.add(VGroup(tl, tv))
        # Quadratic tilt result
        quad_title = SerifLabel("quadratic tilt  V = eps*(x/L)^2", CRIMSON, size=22)
        quad_title.move_to(RIGHT * 2.8 + UP * 1.5)
        quad_note = Text("every term:\n still negative", font=DISPLAY,
                         font_size=24, color=TEAL).move_to(RIGHT * 2.8 + UP * 0.0)
        divider = Line(UP * 2.0, DOWN * 2.2, color=INK, stroke_width=1.5).move_to(ORIGIN)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(linear_title), run_time=0.3)
        self.play(Create(lin_group), run_time=dur * 0.40)
        self.play(FadeIn(quad_title), run_time=dur * 0.15)
        self.play(FadeIn(quad_note, scale=0.9), run_time=dur * 0.20)
        self.wait(dur * 0.10)


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
