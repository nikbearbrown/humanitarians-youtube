"""vox_scenes.py — Why the Oracle Writes Its Answer in a Phase, Not a Bit
(vox-phase-kickback, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B12 is STILL·ai — no scene (compiles as slate).
B01, B03, B05, B08, B10, B13, B16 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = phase / answer / constructive interference;
crimson #BF3339 = missing output / cancellation.
Never swap mid-film.

Exclusions: NO Deutsch-Jozsa generalization, NO phase estimation, NO Simon's/Grover's, NO gate matrices.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 12.0, "B03": 10.0, "B04": 12.0,
    "B05": 5.0,  "B06": 12.0, "B07": 13.0, "B08": 4.0,
    "B09": 12.0, "B10": 4.5,  "B11": 13.0, "B12": 12.0,
    "B13": 5.0,  "B14": 12.0, "B15": 13.0, "B16": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- helpers ---------------------------------------------------------------

def _oracle_box(label="f(x) = ?", width=2.2, height=1.1, accent=SLATE):
    """A black-box oracle: slate fill, white display label."""
    rect = Rectangle(width=width, height=height)
    rect.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
    txt = Text(label, font=DISPLAY, color=WHITE, font_size=26)
    if txt.width > width * 0.85:
        txt.scale_to_fit_width(width * 0.85)
    txt.move_to(rect)
    return VGroup(rect, txt)


def _wire_h(x0, x1, y, color=INK, sw=2.0):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=sw)


def _amp_bar(height, label, accent=TEAL, bar_w=0.7, bar_x=0.0, base_y=0.0):
    """A single amplitude bar + label below. Returns VGroup."""
    rect = Rectangle(width=bar_w, height=abs(height))
    if height >= 0:
        rect.set_fill(accent, 1)
    else:
        rect.set_fill(CRIMSON, 1)
    rect.set_stroke(width=0, opacity=0)
    # Anchor bar bottom to base_y
    rect.move_to([bar_x, base_y + abs(height) / 2 * np.sign(height), 0])
    lbl = Text(label, font=MONO, color=INK, font_size=20)
    lbl.move_to([bar_x, base_y - 0.38, 0])
    return VGroup(rect, lbl)


# ---- scenes ----------------------------------------------------------------

class B02_DeutschProblem(Scene):
    def construct(self):
        total = DUR["B02"]

        title = Text("The Deutsch Problem", font=DISPLAY, color=SLATE, font_size=24)
        title.move_to(UP * 3.1)

        # Oracle box center
        oracle = _oracle_box("f(x) = ?", 2.4, 1.0)
        oracle.move_to(ORIGIN)

        # Constant function panel (left)
        const_chip = LabelChip("CONSTANT", accent=TEAL, size=22)
        const_chip.move_to(LEFT * 4.5 + UP * 2.0)

        arr_c0 = Arrow(LEFT * 4.5 + UP * 0.8, LEFT * 4.5 + UP * 0.2,
                       color=TEAL, stroke_width=2, tip_length=0.15, buff=0.05)
        arr_c1 = Arrow(LEFT * 4.5 + DOWN * 0.2, LEFT * 4.5 + DOWN * 0.8,
                       color=TEAL, stroke_width=2, tip_length=0.15, buff=0.05)

        in0_c = Text("0", font=MONO, color=INK, font_size=28)
        in0_c.move_to(LEFT * 4.5 + UP * 1.1)
        in1_c = Text("1", font=MONO, color=INK, font_size=28)
        in1_c.move_to(LEFT * 4.5 + DOWN * 0.0)
        out_c = Text("0 (both)", font=MONO, color=TEAL, font_size=26)
        out_c.move_to(LEFT * 4.5 + DOWN * 1.3)

        # Balanced function panel (right)
        bal_chip = LabelChip("BALANCED", accent=CRIMSON, size=22)
        bal_chip.move_to(RIGHT * 4.5 + UP * 2.0)

        arr_b0 = Arrow(RIGHT * 4.5 + UP * 0.8, RIGHT * 3.8 + UP * 0.2,
                       color=TEAL, stroke_width=2, tip_length=0.15, buff=0.05)
        arr_b1 = Arrow(RIGHT * 4.5 + DOWN * 0.2, RIGHT * 5.2 + DOWN * 0.8,
                       color=CRIMSON, stroke_width=2, tip_length=0.15, buff=0.05)

        in0_b = Text("0", font=MONO, color=INK, font_size=28)
        in0_b.move_to(RIGHT * 4.5 + UP * 1.1)
        in1_b = Text("1", font=MONO, color=INK, font_size=28)
        in1_b.move_to(RIGHT * 4.5 + DOWN * 0.0)
        out0_b = Text("0", font=MONO, color=TEAL, font_size=26)
        out0_b.move_to(RIGHT * 3.6 + DOWN * 1.3)
        out1_b = Text("1", font=MONO, color=CRIMSON, font_size=26)
        out1_b.move_to(RIGHT * 5.4 + DOWN * 1.3)

        self.play(FadeIn(title, shift=DOWN * 0.1), FadeIn(oracle, scale=0.88), run_time=0.7)
        self.play(FadeIn(const_chip), FadeIn(bal_chip), run_time=0.5)
        self.play(FadeIn(in0_c), FadeIn(in1_c), FadeIn(in0_b), FadeIn(in1_b), run_time=0.4)
        self.play(GrowArrow(arr_c0), GrowArrow(arr_c1),
                  GrowArrow(arr_b0), GrowArrow(arr_b1), run_time=0.7)
        self.play(FadeIn(out_c), FadeIn(out0_b), FadeIn(out1_b), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


class B04_NaiveFail(Scene):
    def construct(self):
        total = DUR["B04"]

        # Query wire
        w = _wire_h(-5.5, 5.5, 0.5, INK, 2)
        q_lbl = Text("|+>", font=MONO, color=TEAL, font_size=30)
        q_lbl.move_to([-5.0, 1.0, 0])

        # Oracle box
        oracle = _oracle_box("f(x) = ?", 2.2, 0.9)
        oracle.move_to([0.0, 0.5, 0])

        # Arrow from query into oracle
        arr_in = Arrow([-2.8, 0.5, 0], [-1.2, 0.5, 0],
                       color=INK, stroke_width=2, tip_length=0.15, buff=0.05)

        # Output
        out_lbl = Text("0  or  1", font=MONO, color=INK, font_size=32)
        out_lbl.move_to([3.8, 0.5, 0])
        arr_out = Arrow([1.2, 0.5, 0], [2.6, 0.5, 0],
                        color=INK, stroke_width=2, tip_length=0.15, buff=0.05)

        # Random label
        random_lbl = Text("still random", font=SERIF, color=CRIMSON,
                          font_size=26, slant=ITALIC)
        random_lbl.move_to([3.8, -0.2, 0])

        # Crimson X
        x1 = Line([3.2, -1.0, 0], [4.4, -1.8, 0], color=CRIMSON, stroke_width=5)
        x2 = Line([3.2, -1.8, 0], [4.4, -1.0, 0], color=CRIMSON, stroke_width=5)

        self.play(Create(w), FadeIn(q_lbl), run_time=0.6)
        self.play(FadeIn(oracle, scale=0.9), GrowArrow(arr_in), run_time=0.5)
        self.play(GrowArrow(arr_out), FadeIn(out_lbl), run_time=0.5)
        self.play(FadeIn(random_lbl, shift=UP * 0.1), run_time=0.4)
        self.play(Create(x1), Create(x2), run_time=0.5)
        self.wait(max(0.5, total - 2.5))


class B06_AncillaSetup(Scene):
    def construct(self):
        total = DUR["B06"]

        # Two-wire circuit
        y_q, y_a = 1.0, -0.8
        x0, x1 = -5.5, 5.5

        w_q = _wire_h(x0, x1, y_q, INK, 2)
        w_a = _wire_h(x0, x1, y_a, SLATE, 2)

        q_lbl = Text("|x>", font=MONO, color=TEAL, font_size=28)
        q_lbl.move_to([x0 + 0.7, y_q + 0.45, 0])
        q_eyebrow = Text("query qubit", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        q_eyebrow.move_to([x0 + 0.7, y_q + 0.85, 0])

        a_lbl = Text("|->=", font=MONO, color=SLATE, font_size=24)
        a_lbl.move_to([x0 + 0.7, y_a - 0.45, 0])
        a_form = Text("(|0>-|1>)/sqrt(2)", font=MONO, color=SLATE, font_size=20)
        a_form.move_to([x0 + 2.3, y_a - 0.45, 0])

        # Oracle box spanning both wires
        oracle = _oracle_box("ORACLE", 2.4, 2.1)
        oracle.move_to([0.5, (y_q + y_a) / 2, 0])

        antenna_lbl = SerifLabel("phase antenna", accent=SLATE, size=24)
        antenna_lbl.move_to([x0 + 1.8, y_a - 1.0, 0])

        self.play(Create(w_q), Create(w_a), run_time=0.6)
        self.play(FadeIn(q_lbl), FadeIn(q_eyebrow), run_time=0.4)
        self.play(FadeIn(a_lbl), FadeIn(a_form), run_time=0.4)
        self.play(FadeIn(oracle, scale=0.88), run_time=0.5)
        self.play(FadeIn(antenna_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.3))


class B07_KickbackMechanism(Scene):
    def construct(self):
        total = DUR["B07"]

        y_q, y_a = 1.0, -0.8
        x0 = -5.5

        # Left side: input labels
        q_in = Text("|x>", font=MONO, color=TEAL, font_size=28)
        q_in.move_to([x0 + 0.5, y_q + 0.45, 0])
        a_in = Text("|->", font=MONO, color=SLATE, font_size=26)
        a_in.move_to([x0 + 0.5, y_a - 0.4, 0])

        # Wires
        w_q = _wire_h(x0, 5.5, y_q, INK, 2)
        w_a = _wire_h(x0, 5.5, y_a, SLATE, 2)

        # Oracle box
        oracle = _oracle_box("ORACLE", 2.2, 2.0)
        oracle.move_to([-0.5, (y_q + y_a) / 2, 0])

        # Output labels
        q_out = Text("(-1)^f(x)|x>", font=MONO, color=TEAL, font_size=26)
        q_out.move_to([3.8, y_q + 0.45, 0])

        a_out = Text("|-> (unchanged)", font=MONO, color=SLATE, font_size=22)
        a_out.move_to([3.8, y_a - 0.4, 0])

        # Kickback arrow: curving from ancilla output up to query
        kick_pts = []
        for i in range(40):
            t = i / 39
            x = 1.4 + t * 2.2
            y = y_a + (y_q - y_a) * (3 * t * t - 2 * t * t * t)  # smooth step
            kick_pts.append([x, y, 0])
        kick_curve = VMobject(color=TEAL, stroke_width=3.5)
        kick_curve.set_points_smoothly(kick_pts)
        kick_lbl = Text("kickback", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        kick_lbl.move_to([2.5, (y_q + y_a) / 2 + 0.1, 0])

        sign_chip = LabelChip("+/-1", accent=TEAL, size=22)
        sign_chip.move_to([3.8, y_q - 0.35, 0])

        self.play(Create(w_q), Create(w_a), run_time=0.5)
        self.play(FadeIn(q_in), FadeIn(a_in), run_time=0.4)
        self.play(FadeIn(oracle, scale=0.88), run_time=0.5)
        self.play(FadeIn(a_out, shift=LEFT * 0.2), run_time=0.4)
        self.play(Create(kick_curve), FadeIn(kick_lbl), run_time=0.9)
        self.play(FadeIn(q_out, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(sign_chip, scale=0.88), run_time=0.4)
        self.wait(max(0.5, total - 3.5))


class B09_TwoCases(Scene):
    def construct(self):
        total = DUR["B09"]

        # Divider
        divider = DashedLine(UP * 3.2, DOWN * 3.2, color=SLATE,
                             stroke_width=1.5, dash_length=0.15)

        # Left panel: CONSTANT — both bars teal, same height
        const_chip = LabelChip("CONSTANT", accent=TEAL, size=26)
        const_chip.move_to(LEFT * 3.5 + UP * 2.8)

        bar_h = 1.8
        b0_const = Rectangle(width=0.85, height=bar_h)
        b0_const.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        b0_const.move_to(LEFT * 4.2 + UP * (bar_h / 2 - 0.5))
        l0_const = Text("|0>", font=MONO, color=INK, font_size=22)
        l0_const.move_to(LEFT * 4.2 + DOWN * 1.0)

        b1_const = Rectangle(width=0.85, height=bar_h)
        b1_const.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        b1_const.move_to(LEFT * 2.8 + UP * (bar_h / 2 - 0.5))
        l1_const = Text("|1>", font=MONO, color=INK, font_size=22)
        l1_const.move_to(LEFT * 2.8 + DOWN * 1.0)

        same_lbl = SerifLabel("same sign", accent=TEAL, size=24)
        same_lbl.move_to(LEFT * 3.5 + DOWN * 1.8)

        # Right panel: BALANCED — one teal (plus), one crimson (minus)
        bal_chip = LabelChip("BALANCED", accent=CRIMSON, size=26)
        bal_chip.move_to(RIGHT * 3.5 + UP * 2.8)

        b0_bal = Rectangle(width=0.85, height=bar_h)
        b0_bal.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        b0_bal.move_to(RIGHT * 2.8 + UP * (bar_h / 2 - 0.5))
        l0_bal = Text("|0>", font=MONO, color=INK, font_size=22)
        l0_bal.move_to(RIGHT * 2.8 + DOWN * 1.0)

        b1_bal = Rectangle(width=0.85, height=bar_h)
        b1_bal.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        b1_bal.move_to(RIGHT * 4.2 + DOWN * (bar_h / 2 - 0.5))
        l1_bal = Text("|1>", font=MONO, color=INK, font_size=22)
        l1_bal.move_to(RIGHT * 4.2 + DOWN * 1.0)

        # Minus sign for the negative bar
        minus_lbl = Text("-", font=MONO, color=CRIMSON, font_size=38)
        minus_lbl.move_to(RIGHT * 4.2 + DOWN * 2.4)

        opp_lbl = SerifLabel("opposite sign", accent=CRIMSON, size=24)
        opp_lbl.move_to(RIGHT * 3.5 + DOWN * 1.8)

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(const_chip), FadeIn(bal_chip), run_time=0.5)
        self.play(
            FadeIn(b0_const, scale=0.2),
            FadeIn(b1_const, scale=0.2),
            FadeIn(b0_bal, scale=0.2),
            FadeIn(b1_bal, scale=0.2),
            run_time=0.8
        )
        self.play(FadeIn(l0_const), FadeIn(l1_const), FadeIn(l0_bal), FadeIn(l1_bal),
                  FadeIn(minus_lbl), run_time=0.4)
        self.play(FadeIn(same_lbl, shift=UP * 0.1), FadeIn(opp_lbl, shift=UP * 0.1),
                  run_time=0.5)
        self.wait(max(0.5, total - 2.6))


class B11_HadamardReadout(Scene):
    def construct(self):
        total = DUR["B11"]

        divider = DashedLine(UP * 3.2, DOWN * 3.2, color=SLATE,
                             stroke_width=1.5, dash_length=0.15)

        # Left panel: constant case (same-sign bars -> H -> all at |0>)
        const_eyebrow = Text("CONSTANT", font=DISPLAY, color=TEAL, font_size=22)
        const_eyebrow.move_to(LEFT * 3.5 + UP * 3.0)

        # Input bars (same sign)
        bar_h = 1.2
        in0_c = Rectangle(width=0.6, height=bar_h)
        in0_c.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        in0_c.move_to(LEFT * 5.0 + UP * (bar_h / 2))
        in1_c = Rectangle(width=0.6, height=bar_h)
        in1_c.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        in1_c.move_to(LEFT * 4.0 + UP * (bar_h / 2))

        # H gate box
        h_gate_c = Rectangle(width=0.8, height=0.7)
        h_gate_c.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        h_gate_c.move_to(LEFT * 3.0 + UP * 0.5)
        h_txt_c = Text("H", font=DISPLAY, color=WHITE, font_size=24)
        h_txt_c.move_to(LEFT * 3.0 + UP * 0.5)

        # Output bars: all amplitude at |0>
        out0_c = Rectangle(width=0.6, height=2.0)
        out0_c.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        out0_c.move_to(LEFT * 2.0 + UP * (2.0 / 2))
        out0_lbl_c = Text("|0>", font=MONO, color=INK, font_size=20)
        out0_lbl_c.move_to(LEFT * 2.0 + DOWN * 0.6)
        out1_c = Rectangle(width=0.6, height=0.08)
        out1_c.set_fill(SLATE, 0.4).set_stroke(width=0, opacity=0)
        out1_c.move_to(LEFT * 1.0 + DOWN * 0.6)
        out1_lbl_c = Text("|1>", font=MONO, color=INK, font_size=20)
        out1_lbl_c.move_to(LEFT * 1.0 + DOWN * 1.0)

        result_c = LabelChip("0 = CONSTANT", accent=TEAL, size=20)
        result_c.move_to(LEFT * 1.5 + DOWN * 2.2)

        # Right panel: balanced case (opposite sign -> H -> all at |1>)
        bal_eyebrow = Text("BALANCED", font=DISPLAY, color=CRIMSON, font_size=22)
        bal_eyebrow.move_to(RIGHT * 3.5 + UP * 3.0)

        in0_b = Rectangle(width=0.6, height=bar_h)
        in0_b.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        in0_b.move_to(RIGHT * 4.0 + UP * (bar_h / 2))
        in1_b = Rectangle(width=0.6, height=bar_h)
        in1_b.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        in1_b.move_to(RIGHT * 5.0 + DOWN * (bar_h / 2))

        h_gate_b = Rectangle(width=0.8, height=0.7)
        h_gate_b.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        h_gate_b.move_to(RIGHT * 3.0 + UP * 0.5)
        h_txt_b = Text("H", font=DISPLAY, color=WHITE, font_size=24)
        h_txt_b.move_to(RIGHT * 3.0 + UP * 0.5)

        out0_b = Rectangle(width=0.6, height=0.08)
        out0_b.set_fill(SLATE, 0.4).set_stroke(width=0, opacity=0)
        out0_b.move_to(RIGHT * 2.0 + DOWN * 0.6)
        out0_lbl_b = Text("|0>", font=MONO, color=INK, font_size=20)
        out0_lbl_b.move_to(RIGHT * 2.0 + DOWN * 1.0)
        out1_b = Rectangle(width=0.6, height=2.0)
        out1_b.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        out1_b.move_to(RIGHT * 1.0 + UP * (2.0 / 2))
        out1_lbl_b = Text("|1>", font=MONO, color=INK, font_size=20)
        out1_lbl_b.move_to(RIGHT * 1.0 + DOWN * 0.6)

        result_b = LabelChip("1 = BALANCED", accent=CRIMSON, size=20)
        result_b.move_to(RIGHT * 1.5 + DOWN * 2.2)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(const_eyebrow), FadeIn(bal_eyebrow), run_time=0.4)
        self.play(FadeIn(in0_c, scale=0.3), FadeIn(in1_c, scale=0.3),
                  FadeIn(in0_b, scale=0.3), FadeIn(in1_b, scale=0.3), run_time=0.5)
        self.play(FadeIn(h_gate_c), FadeIn(h_txt_c),
                  FadeIn(h_gate_b), FadeIn(h_txt_b), run_time=0.4)
        self.play(
            ReplacementTransform(in0_c.copy(), out0_c),
            ReplacementTransform(in1_c.copy(), out1_c),
            ReplacementTransform(in0_b.copy(), out1_b),
            ReplacementTransform(in1_b.copy(), out0_b),
            run_time=1.2
        )
        self.play(FadeIn(out0_lbl_c), FadeIn(out1_lbl_c),
                  FadeIn(out0_lbl_b), FadeIn(out1_lbl_b), run_time=0.4)
        self.play(FadeIn(result_c, scale=0.88), FadeIn(result_b, scale=0.88), run_time=0.5)
        self.wait(max(0.5, total - 4.2))


class B14_Pattern(Scene):
    def construct(self):
        total = DUR["B14"]

        # Three boxes with arrows
        box_w, box_h = 2.6, 1.6

        box1 = Rectangle(width=box_w, height=box_h)
        box1.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        box1.move_to(LEFT * 4.5)
        lbl1a = Text("SUPERPOSITION", font=DISPLAY, color=TEAL, font_size=18)
        lbl1a.move_to(LEFT * 4.5 + UP * 0.3)
        lbl1b = Text("many inputs", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        lbl1b.move_to(LEFT * 4.5 + DOWN * 0.3)

        box2 = Rectangle(width=box_w, height=box_h)
        box2.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        box2.move_to(ORIGIN)
        lbl2a = Text("PHASE ENCODING", font=DISPLAY, color=SLATE, font_size=17)
        lbl2a.move_to(UP * 0.3)
        lbl2b = Text("oracle writes sign", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        lbl2b.move_to(DOWN * 0.3)

        box3 = Rectangle(width=box_w, height=box_h)
        box3.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        box3.move_to(RIGHT * 4.5)
        lbl3a = Text("INTERFERENCE", font=DISPLAY, color=TEAL, font_size=18)
        lbl3a.move_to(RIGHT * 4.5 + UP * 0.3)
        lbl3b = Text("Hadamard reads it", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        lbl3b.move_to(RIGHT * 4.5 + DOWN * 0.3)

        arr12 = Arrow(LEFT * 3.1, LEFT * 1.4, color=INK, stroke_width=2,
                      tip_length=0.15, buff=0.05)
        lbl_oracle = Text("oracle", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        lbl_oracle.next_to(arr12, UP, buff=0.12)

        arr23 = Arrow(RIGHT * 1.4, RIGHT * 3.1, color=INK, stroke_width=2,
                      tip_length=0.15, buff=0.05)
        lbl_hadamard = Text("Hadamard", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        lbl_hadamard.next_to(arr23, UP, buff=0.12)

        template_lbl = SerifLabel("the algorithmic template", accent=TEAL, size=24)
        template_lbl.move_to(DOWN * 2.8)

        self.play(FadeIn(box1), FadeIn(lbl1a), FadeIn(lbl1b), run_time=0.5)
        self.play(GrowArrow(arr12), FadeIn(lbl_oracle), run_time=0.4)
        self.play(FadeIn(box2), FadeIn(lbl2a), FadeIn(lbl2b), run_time=0.5)
        self.play(GrowArrow(arr23), FadeIn(lbl_hadamard), run_time=0.4)
        self.play(FadeIn(box3), FadeIn(lbl3a), FadeIn(lbl3b), run_time=0.5)
        self.play(FadeIn(template_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.7))


class B15_Example(Scene):
    def construct(self):
        total = DUR["B15"]

        title = Text("Worked Example: constant function", font=SERIF, color=INK,
                     font_size=26, slant=ITALIC)
        title.move_to(UP * 3.2)

        # Full Deutsch circuit
        y_q, y_a = 1.0, -0.8
        x0 = -6.0

        w_q = _wire_h(x0, 6.0, y_q, INK, 2)
        w_a = _wire_h(x0, 6.0, y_a, SLATE, 2)

        # Input labels
        in_q = Text("|+>", font=MONO, color=TEAL, font_size=26)
        in_q.move_to([x0 + 0.65, y_q + 0.45, 0])
        in_a = Text("|->", font=MONO, color=SLATE, font_size=24)
        in_a.move_to([x0 + 0.65, y_a - 0.4, 0])

        # Oracle box
        oracle = _oracle_box("ORACLE", 2.1, 2.0)
        oracle.move_to([-1.0, (y_q + y_a) / 2, 0])

        # Hadamard on query
        h_gate = Rectangle(width=0.75, height=0.65)
        h_gate.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        h_gate.move_to([1.8, y_q, 0])
        h_txt = Text("H", font=DISPLAY, color=WHITE, font_size=24)
        h_txt.move_to([1.8, y_q, 0])

        # Measure symbol (detector box)
        m_box = Rectangle(width=0.75, height=0.65)
        m_box.set_fill(SLATE, 0.5).set_stroke(SLATE, 1.5)
        m_box.move_to([3.2, y_q, 0])
        m_txt = Text("M", font=DISPLAY, color=WHITE, font_size=24)
        m_txt.move_to([3.2, y_q, 0])

        # Outcome
        outcome_lbl = Text("0", font=MONO, color=TEAL, font_size=38)
        outcome_lbl.move_to([4.6, y_q, 0])

        # Ancilla unchanged
        anc_out = Text("|-> (unchanged)", font=MONO, color=SLATE, font_size=20)
        anc_out.move_to([3.5, y_a - 0.4, 0])

        # Result chip
        result = LabelChip("CONSTANT", accent=TEAL, size=26)
        result.move_to([5.5, y_q + 0.6, 0])

        # Note below
        note = SerifLabel("one query · answer in the phase", accent=TEAL, size=24)
        note.move_to(DOWN * 2.5)

        self.play(FadeIn(title, shift=DOWN * 0.1), run_time=0.4)
        self.play(Create(w_q), Create(w_a), run_time=0.5)
        self.play(FadeIn(in_q), FadeIn(in_a), run_time=0.4)
        self.play(FadeIn(oracle, scale=0.88), run_time=0.4)
        self.play(FadeIn(anc_out, shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(h_gate), FadeIn(h_txt), run_time=0.3)
        self.play(FadeIn(m_box), FadeIn(m_txt), run_time=0.3)
        self.play(FadeIn(outcome_lbl, scale=1.2), run_time=0.4)
        self.play(FadeIn(result, scale=0.88), run_time=0.4)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 4.0))
