"""vox_scenes.py — How to Move a Qubit Without Ever Copying It
(vox-qubit-teleport, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B05 and B13 are STILL·ai — no scene needed
(they compile as slates). Durations from beat_sheet.json.

Render (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh quantum-mechanics-vol4/youtube/vox-qubit-teleport

Color law: teal #1F6F5C = the quantum state / good resource / restored qubit;
crimson #BF3339 = blocked channel / destroyed original / scrambled form.
Never swap mid-film.

Card exclusions: NO three-qubit amplitude expansion, NO full correction table,
NO dense-coding dual.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 11.0, "B02": 9.5, "B03": 7.0, "B04": 11.0,
    "B06": 11.5, "B07": 4.5, "B08": 10.5, "B09": 10.5,
    "B10": 5.5,  "B11": 10.5, "B12": 8.5, "B14": 11.0, "B15": 9.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- helpers ---------------------------------------------------------------

def _qubit_box(label, accent=TEAL, width=2.2, height=0.9):
    """A qubit rectangle: accent border, cream fill, serif label inside."""
    rect = Rectangle(width=width, height=height)
    rect.set_fill(GROUND, 1).set_stroke(accent, 3)
    txt = Text(label, font=SERIF, color=accent, font_size=30, slant=ITALIC)
    if txt.width > width * 0.82:
        txt.scale_to_fit_width(width * 0.82)
    txt.move_to(rect)
    return VGroup(rect, txt)


def _person_node(name, accent=SLATE, radius=0.42):
    """A circle + name label below it."""
    circ = Circle(radius=radius).set_fill(accent, 0.18).set_stroke(accent, 3)
    lbl = Text(name, font=DISPLAY, color=accent, font_size=26)
    lbl.next_to(circ, DOWN, buff=0.22)
    return VGroup(circ, lbl)


def _gate_box(label, width=0.9, height=0.72, accent=SLATE):
    """A square gate box: slate fill, white label (CNOT, H, Z, X)."""
    rect = Rectangle(width=width, height=height)
    rect.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
    txt = Text(label, font=DISPLAY, color=WHITE, font_size=26, weight=BOLD)
    txt.move_to(rect)
    return VGroup(rect, txt)


def _wire(x0, x1, y, color=INK, sw=2):
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=sw)


# ---- scenes ----------------------------------------------------------------

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22)
        t1 = Text("How to Move a Qubit", font=DISPLAY, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("Without Ever Copying It", font=DISPLAY, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        chip = LabelChip("QUANTUM TELEPORTATION", accent=TEAL, size=23)
        chip.next_to(block, DOWN, buff=0.6)
        self.play(FadeIn(eye, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(block, shift=UP * 0.12), Create(u), run_time=1.0)
        self.play(FadeIn(chip, scale=0.88), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B02_AliceBob(Scene):
    def construct(self):
        total = DUR["B02"]
        alice = _person_node("Alice", SLATE)
        alice.move_to(LEFT * 4.5 + UP * 0.4)
        bob = _person_node("Bob", SLATE)
        bob.move_to(RIGHT * 4.5 + UP * 0.4)
        psi = _qubit_box("|ψ⟩ = ?", TEAL, 1.8, 0.78)
        psi.next_to(alice, UP, buff=0.28)

        # Classical phone line at bottom
        phone_line = DashedLine(
            LEFT * 4.0 + DOWN * 1.5, RIGHT * 4.0 + DOWN * 1.5,
            color=SLATE, stroke_width=2, dash_length=0.18
        )
        phone_lbl = Text("classical phone", font=SERIF, color=SLATE,
                         font_size=22, slant=ITALIC)
        phone_lbl.next_to(phone_line, DOWN, buff=0.18)

        # Blocked quantum channel (crimson X in center)
        x1 = Line(LEFT * 0.55 + UP * 0.3, RIGHT * 0.55 + DOWN * 0.3,
                  color=CRIMSON, stroke_width=5)
        x2 = Line(LEFT * 0.55 + DOWN * 0.3, RIGHT * 0.55 + UP * 0.3,
                  color=CRIMSON, stroke_width=5)
        no_q = Text("no quantum channel", font=SERIF, color=CRIMSON,
                    font_size=20, slant=ITALIC)
        no_q.move_to(UP * 0.7)

        self.play(FadeIn(alice, shift=RIGHT * 0.5),
                  FadeIn(bob, shift=LEFT * 0.5), run_time=0.8)
        self.play(FadeIn(psi, scale=0.88), run_time=0.6)
        self.play(Create(phone_line), FadeIn(phone_lbl), run_time=0.7)
        self.play(Create(x1), Create(x2), FadeIn(no_q), run_time=0.7)
        self.wait(max(0.5, total - 2.8))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Can't measure. Can't copy.", font=SERIF, color=INK,
                  font_size=44, slant=ITALIC)
        q2 = Text("How does it move?", font=SERIF, color=CRIMSON,
                  font_size=52, weight=BOLD, slant=ITALIC)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.32)
        u = Line(q2.get_corner(DL) + DOWN * 0.12,
                 q2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(q2, shift=UP * 0.1), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.5))


class B04_MeasureTrap(Scene):
    def construct(self):
        total = DUR["B04"]
        # State box on left
        state = _qubit_box("|ψ⟩ = α|0⟩+β|1⟩", TEAL, 3.2, 0.88)
        state.move_to(LEFT * 3.8 + UP * 0.3)

        # Arrow right
        arr = Arrow(LEFT * 1.8 + UP * 0.3, LEFT * 0.8 + UP * 0.3,
                    color=INK, stroke_width=3, buff=0.1)

        # Measure box
        mbox = _gate_box("MEASURE", 2.0, 0.88, SLATE)
        mbox.move_to(UP * 0.3)

        # Output: one bit
        out_lbl = Text("0  or  1", font=MONO, color=INK, font_size=42, weight=BOLD)
        out_lbl.move_to(RIGHT * 3.2 + UP * 0.3)

        # Loss label
        loss = Text("α, β: gone", font=SERIF, color=CRIMSON,
                    font_size=28, slant=ITALIC)
        loss.next_to(out_lbl, DOWN, buff=0.4)
        u_loss = Line(loss.get_corner(DL) + DOWN * 0.08,
                      loss.get_corner(DR) + DOWN * 0.08,
                      color=CRIMSON, stroke_width=1.5)

        self.play(FadeIn(state, shift=RIGHT * 0.4), run_time=0.7)
        self.play(Create(arr), run_time=0.4)
        self.play(FadeIn(mbox, scale=0.9), run_time=0.5)
        self.play(FadeIn(out_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(loss, shift=UP * 0.1), Create(u_loss), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B06_BellPair(Scene):
    def construct(self):
        total = DUR["B06"]
        alice_lbl = Text("Alice", font=DISPLAY, color=SLATE, font_size=26)
        alice_lbl.move_to(LEFT * 4.2 + UP * 2.0)
        bob_lbl = Text("Bob", font=DISPLAY, color=SLATE, font_size=26)
        bob_lbl.move_to(RIGHT * 4.2 + UP * 2.0)

        qa = _qubit_box("A", TEAL, 1.6, 0.78)
        qa.move_to(LEFT * 3.8 + UP * 0.5)
        qb = _qubit_box("B", TEAL, 1.6, 0.78)
        qb.move_to(RIGHT * 3.8 + UP * 0.5)

        # Wavy entanglement line
        pts = []
        for i in range(60):
            t = i / 59
            x = -2.4 + t * 4.8
            y = 0.5 + 0.22 * np.sin(t * TAU * 2.5)
            pts.append([x, y, 0])
        wave = VMobject(color=TEAL, stroke_width=3)
        wave.set_points_smoothly(pts)

        pair_lbl = Text("|Φ+⟩", font=SERIF, color=TEAL, font_size=34, slant=ITALIC)
        pair_lbl.move_to(DOWN * 0.1)

        sub = Text("maximally entangled · no local information", font=SERIF,
                   color=SLATE, font_size=22, slant=ITALIC)
        sub.move_to(DOWN * 1.2)

        self.play(FadeIn(alice_lbl, shift=RIGHT * 0.2),
                  FadeIn(bob_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(qa, shift=RIGHT * 0.5),
                  FadeIn(qb, shift=LEFT * 0.5), run_time=0.8)
        self.play(Create(wave), FadeIn(pair_lbl), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B07_Protocol(Scene):
    def construct(self):
        total = DUR["B07"]
        chip = LabelChip("THE PROTOCOL", accent=TEAL, size=40)
        sub = Text("four steps · no reading required", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        grp = VGroup(chip, sub).arrange(DOWN, buff=0.5)
        u = Line(sub.get_corner(DL) + DOWN * 0.1, sub.get_corner(DR) + DOWN * 0.1,
                 color=TEAL, stroke_width=1.5)
        self.play(FadeIn(chip, scale=0.88), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.1), Create(u), run_time=0.5)
        self.wait(max(0.5, total - 1.1))


class B08_Gates(Scene):
    def construct(self):
        total = DUR["B08"]
        # Three circuit wires: y positions
        y_s, y_a, y_b = 1.2, 0.0, -1.2
        x0, x1 = -5.8, 5.8

        w_s = _wire(x0, x1, y_s, INK, 2)
        w_a = _wire(x0, x1, y_a, INK, 2)
        w_b = _wire(x0, x1, y_b, SLATE, 1.5)

        lbl_s = Text("|ψ⟩", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        lbl_s.move_to([-5.4, y_s + 0.45, 0])
        lbl_a = Text("A", font=DISPLAY, color=SLATE, font_size=24)
        lbl_a.move_to([-5.4, y_a + 0.42, 0])
        lbl_b = Text("B", font=DISPLAY, color=SLATE, font_size=24)
        lbl_b.move_to([-5.4, y_b + 0.42, 0])

        alice_bracket = Text("Alice's qubits", font=SERIF, color=SLATE,
                             font_size=20, slant=ITALIC)
        alice_bracket.move_to([-4.8, (y_s + y_a) / 2, 0])

        # CNOT gate at x = -1.5
        cnot_x = -1.5
        ctrl = Dot(radius=0.16, color=INK).move_to([cnot_x, y_s, 0])
        cnot_line = Line([cnot_x, y_s, 0], [cnot_x, y_a, 0],
                         color=INK, stroke_width=2)
        target_circ = Circle(radius=0.26).set_stroke(INK, 2).set_fill(GROUND, 1)
        target_circ.move_to([cnot_x, y_a, 0])
        t_cross_h = Line([cnot_x - 0.26, y_a, 0], [cnot_x + 0.26, y_a, 0],
                         color=INK, stroke_width=2)
        t_cross_v = Line([cnot_x, y_a - 0.26, 0], [cnot_x, y_a + 0.26, 0],
                         color=INK, stroke_width=2)
        cnot_lbl = Text("CNOT", font=DISPLAY, color=SLATE, font_size=18)
        cnot_lbl.move_to([cnot_x, y_a - 0.65, 0])

        # Hadamard gate at x = 0.8
        h_gate = _gate_box("H", 0.72, 0.60, SLATE)
        h_gate.move_to([0.8, y_s, 0])

        # Four branches on right
        branch_x = 3.2
        outcomes = ["00", "01", "10", "11"]
        branches = VGroup()
        for i, oc in enumerate(outcomes):
            y_br = 1.8 - i * 1.2
            arr = Arrow([branch_x - 0.3, (y_s + y_a) / 2, 0],
                        [branch_x + 0.7, y_br, 0],
                        color=TEAL, stroke_width=2, buff=0.05,
                        max_tip_length_to_length_ratio=0.2)
            lbl = Text(oc, font=MONO, color=TEAL, font_size=24)
            lbl.next_to(arr, RIGHT, buff=0.08)
            branches.add(VGroup(arr, lbl))

        bob_lbl = Text("Bob's qubit (passive)", font=SERIF, color=SLATE,
                       font_size=20, slant=ITALIC)
        bob_lbl.move_to([1.5, y_b - 0.45, 0])

        self.play(Create(w_s), Create(w_a), Create(w_b), run_time=0.7)
        self.play(FadeIn(lbl_s), FadeIn(lbl_a), FadeIn(lbl_b),
                  FadeIn(alice_bracket), run_time=0.5)
        self.play(FadeIn(ctrl), Create(cnot_line), FadeIn(target_circ),
                  Create(t_cross_h), Create(t_cross_v), FadeIn(cnot_lbl),
                  run_time=0.8)
        self.play(FadeIn(h_gate, scale=0.88), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in branches],
                              lag_ratio=0.15), run_time=0.8)
        self.play(FadeIn(bob_lbl), run_time=0.4)
        self.wait(max(0.5, total - 3.7))


class B09_Measurement(Scene):
    def construct(self):
        total = DUR["B09"]
        # Original teal state box
        psi_box = _qubit_box("|ψ⟩", TEAL, 2.0, 0.82)
        psi_box.move_to(LEFT * 4.0 + UP * 0.8)

        # Detector boxes for S and A
        det_s = _gate_box("▶", 1.0, 0.82, SLATE)
        det_s.move_to(LEFT * 1.2 + UP * 0.8)
        det_a = _gate_box("▶", 1.0, 0.82, SLATE)
        det_a.move_to(LEFT * 1.2 + DOWN * 0.4)

        alice_lbl = Text("Alice measures S and A", font=SERIF, color=SLATE,
                         font_size=22, slant=ITALIC)
        alice_lbl.move_to(LEFT * 1.2 + DOWN * 1.4)

        # The "GONE" box replaces the teal box
        gone_box = Rectangle(width=2.0, height=0.82)
        gone_box.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 3)
        gone_lbl = Text("GONE", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        gone_lbl.move_to(gone_box)
        gone = VGroup(gone_box, gone_lbl)
        gone.move_to(LEFT * 4.0 + UP * 0.8)

        # Classical bits emerging
        b1 = LabelChip("1", accent=SLATE, size=28)
        b2 = LabelChip("0", accent=SLATE, size=28)
        bits = VGroup(b1, b2).arrange(RIGHT, buff=0.22)
        bits.move_to(RIGHT * 2.8 + UP * 0.2)

        outcome_chip = LabelChip("OUTCOME: 10", accent=SLATE, size=24)
        outcome_chip.next_to(bits, UP, buff=0.35)

        arrow_bits = Arrow(det_s.get_right() + RIGHT * 0.05,
                           bits.get_left() + LEFT * 0.05,
                           color=SLATE, stroke_width=2, buff=0.05,
                           max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(psi_box, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(det_s, scale=0.9), FadeIn(det_a, scale=0.9),
                  FadeIn(alice_lbl), run_time=0.7)
        self.play(ReplacementTransform(psi_box, gone), run_time=0.7)
        self.play(Create(arrow_bits), run_time=0.4)
        self.play(FadeIn(bits, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(outcome_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


class B10_Landed(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("It landed on Bob.", font=SERIF, color=INK,
                  font_size=52, weight=BOLD, slant=ITALIC)
        t2 = Text("In scrambled form.", font=SERIF, color=CRIMSON,
                  font_size=36, slant=ITALIC)
        grp = VGroup(t1, t2).arrange(DOWN, buff=0.38)
        u = Line(t1.get_corner(DL) + DOWN * 0.12, t1.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1, shift=DOWN * 0.1), Create(u), run_time=0.6)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.1))


class B11_BobScrambled(Scene):
    def construct(self):
        total = DUR["B11"]
        bob_lbl = Text("Bob", font=DISPLAY, color=SLATE, font_size=28)
        bob_lbl.move_to(RIGHT * 3.8 + UP * 1.8)

        # Bob's scrambled qubit
        bob_q = _qubit_box("Z|ψ⟩", CRIMSON, 2.0, 0.82)
        bob_q.move_to(RIGHT * 3.8 + UP * 0.6)

        phase_note = Text("phase flipped", font=SERIF, color=CRIMSON,
                          font_size=22, slant=ITALIC)
        phase_note.next_to(bob_q, DOWN, buff=0.28)

        # Question mark
        qmark = Text("?", font=DISPLAY, color=CRIMSON, font_size=64, weight=BOLD)
        qmark.move_to(RIGHT * 3.8 + UP * 0.6)

        # Small correction guide on left
        guide_header = Text("correction needed:", font=SERIF, color=SLATE,
                            font_size=22, slant=ITALIC)
        guide_header.move_to(LEFT * 3.2 + UP * 1.4)

        rows = [("00 →", "I"), ("01 →", "X"), ("10 →", "Z"), ("11 →", "ZX")]
        guide_rows = VGroup()
        for outcome, gate in rows:
            oc_t = Text(outcome, font=MONO, color=SLATE, font_size=22)
            gt_t = Text(gate, font=DISPLAY, color=TEAL if gate == "Z" else INK,
                        font_size=22, weight=BOLD)
            row = VGroup(oc_t, gt_t).arrange(RIGHT, buff=0.3)
            guide_rows.add(row)
        guide_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        guide_rows.next_to(guide_header, DOWN, buff=0.22)

        needs_call = Text("← needs Alice's call", font=SERIF, color=SLATE,
                          font_size=20, slant=ITALIC)
        needs_call.next_to(guide_rows, DOWN, buff=0.28)

        self.play(FadeIn(bob_lbl), FadeIn(bob_q, shift=LEFT * 0.3), run_time=0.7)
        self.play(FadeIn(phase_note), run_time=0.4)
        self.play(FadeIn(guide_header), FadeIn(guide_rows), run_time=0.7)
        self.play(FadeIn(needs_call), run_time=0.4)
        # Question mark grows — the aha: Bob can't unscramble yet
        qmark.scale(0.3)
        self.play(qmark.animate.scale(3.0), run_time=0.8)
        self.wait(max(0.5, total - 3.0))


class B12_PhoneCall(Scene):
    def construct(self):
        total = DUR["B12"]
        # Classical bits traveling left to right
        b1 = LabelChip("1", accent=SLATE, size=28)
        b2 = LabelChip("0", accent=SLATE, size=28)

        bits = VGroup(b1, b2).arrange(RIGHT, buff=0.22)
        bits.move_to(LEFT * 4.2 + UP * 1.2)

        channel = _wire(-4.5, 4.5, 1.2, SLATE, 1.5)
        alice_side = Text("Alice", font=DISPLAY, color=SLATE, font_size=22)
        alice_side.move_to(LEFT * 4.8 + UP * 1.6)
        bob_side = Text("Bob", font=DISPLAY, color=SLATE, font_size=22)
        bob_side.move_to(RIGHT * 4.8 + UP * 1.6)

        # Bob's qubit starts crimson (scrambled)
        q_scrambled = _qubit_box("Z|ψ⟩", CRIMSON, 2.0, 0.82)
        q_scrambled.move_to(RIGHT * 3.8 + DOWN * 0.5)

        # Z gate box
        z_gate = _gate_box("Z", 0.72, 0.60, TEAL)
        z_gate.move_to(RIGHT * 3.8 + UP * 0.35)

        # Restored teal qubit
        q_restored = _qubit_box("|ψ⟩", TEAL, 2.0, 0.82)
        q_restored.move_to(RIGHT * 3.8 + DOWN * 0.5)

        self.play(Create(channel), FadeIn(alice_side), FadeIn(bob_side),
                  run_time=0.5)
        self.play(FadeIn(bits), run_time=0.3)
        self.play(bits.animate.move_to(RIGHT * 3.0 + UP * 1.2), run_time=0.9)
        self.play(FadeIn(q_scrambled, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(z_gate, scale=0.9), run_time=0.4)
        self.play(ReplacementTransform(q_scrambled, q_restored),
                  z_gate.animate.shift(UP * 0.3), run_time=0.8)
        restored_lbl = Text("= original state", font=SERIF, color=TEAL,
                             font_size=24, slant=ITALIC)
        restored_lbl.next_to(q_restored, DOWN, buff=0.28)
        self.play(FadeIn(restored_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.9))


class B14_Example(Scene):
    def construct(self):
        total = DUR["B14"]
        # Row 1: Alice → outcome → Bob's initial state
        alice_q = _qubit_box("|+⟩", TEAL, 1.7, 0.78)
        alice_q.move_to(LEFT * 4.5 + UP * 1.0)
        alice_note = Text("equal 0 and 1", font=SERIF, color=SLATE,
                          font_size=20, slant=ITALIC)
        alice_note.next_to(alice_q, DOWN, buff=0.2)

        arr1 = Arrow(LEFT * 3.5 + UP * 1.0, LEFT * 2.2 + UP * 1.0,
                     color=INK, stroke_width=2, buff=0.05,
                     max_tip_length_to_length_ratio=0.2)

        oc_chip = LabelChip("OUTCOME 10", accent=SLATE, size=22)
        oc_chip.move_to(LEFT * 1.3 + UP * 1.0)

        arr2 = Arrow(LEFT * 0.3 + UP * 1.0, RIGHT * 0.9 + UP * 1.0,
                     color=INK, stroke_width=2, buff=0.05,
                     max_tip_length_to_length_ratio=0.2)

        bob_scrambled_q = _qubit_box("|-⟩", CRIMSON, 1.7, 0.78)
        bob_scrambled_q.move_to(RIGHT * 2.2 + UP * 1.0)
        bob_note1 = Text("phase flipped", font=SERIF, color=CRIMSON,
                         font_size=20, slant=ITALIC)
        bob_note1.next_to(bob_scrambled_q, DOWN, buff=0.2)

        # Row 2: Z correction → restored
        z_arrow = Arrow(RIGHT * 2.2 + UP * 0.28, RIGHT * 2.2 + DOWN * 0.5,
                        color=TEAL, stroke_width=3, buff=0.05,
                        max_tip_length_to_length_ratio=0.25)
        z_lbl = Text("apply Z", font=DISPLAY, color=TEAL, font_size=24)
        z_lbl.next_to(z_arrow, RIGHT, buff=0.18)

        bob_restored_q = _qubit_box("|+⟩", TEAL, 1.7, 0.78)
        bob_restored_q.move_to(RIGHT * 2.2 + DOWN * 1.1)

        # Final summary
        summary = SerifLabel("one moved · none copied", TEAL, size=26)
        summary.move_to(DOWN * 2.5)

        self.play(FadeIn(alice_q, shift=RIGHT * 0.3), FadeIn(alice_note),
                  run_time=0.6)
        self.play(Create(arr1), FadeIn(oc_chip), run_time=0.5)
        self.play(Create(arr2), FadeIn(bob_scrambled_q, shift=LEFT * 0.2),
                  FadeIn(bob_note1), run_time=0.6)
        self.play(Create(z_arrow), FadeIn(z_lbl), run_time=0.5)
        self.play(ReplacementTransform(bob_scrambled_q, bob_restored_q),
                  run_time=0.7)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


class B15_Endcard(Scene):
    def construct(self):
        total = DUR["B15"]
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        kicker.move_to(UP * 2.5)

        line1 = Text("1 ebit + 2 bits → 1 qubit moved.",
                     font=DISPLAY, color=INK, font_size=42, weight=BOLD)
        line2 = Text("Intact. Unread. No copy left behind.",
                     font=SERIF, color=TEAL, font_size=32, slant=ITALIC)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.32)
        block.move_to(DOWN * 0.2)

        u = Line(line1.get_corner(DL) + DOWN * 0.12,
                 line1.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2)

        source = Text("Quantum Mechanics Vol. 4 — chapter 5",
                      font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        source.move_to(DOWN * 2.5)

        self.play(FadeIn(kicker, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(line1, shift=UP * 0.1), Create(u), run_time=0.8)
        self.play(FadeIn(line2, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(source), run_time=0.4)
        self.wait(max(0.5, total - 2.3))
