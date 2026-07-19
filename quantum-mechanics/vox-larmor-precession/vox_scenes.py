"""vox_scenes.py — The Spinning Compass Inside Every MRI
(vox-larmor-precession, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat. B09 is STILL·ai — no scene here.
Color law: TEAL = fixed z-component; CRIMSON = precessing azimuthal motion.
Exclusions: no Hamiltonian diagonalization, no g-factor, no pulse sequences.
"""
import sys, json, pathlib, numpy as np
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def _dur(bid, fallback=9.0):
    return DUR.get(bid, fallback)


# ── B01 — Title card ─────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        total = _dur("B01", 10.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        title = Text("The Spinning Compass", font=DISPLAY, color=INK, font_size=52)
        sub = Text("Inside Every MRI", font=SERIF, color=CRIMSON, font_size=44, slant=ITALIC)
        content = VGroup(title, sub)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=CRIMSON, stroke_width=2.5)
        rule.next_to(content, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title, shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(total - 3.5)


# ── B02 — Cold open: spin arrow precessing on Bloch sphere ───────────────────
class B02_SpinPrecessing(Scene):
    def construct(self):
        total = _dur("B02", 11.0)
        eyebrow = LabelChip("proton spin in B field", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # z-axis (vertical)
        z_axis = Arrow(DOWN * 2.4, UP * 2.4, color=TEAL, stroke_width=3.5, buff=0)
        z_lbl = Text("B", font=MONO, color=TEAL, font_size=32)
        z_lbl.next_to(z_axis.get_end(), UR, buff=0.15)

        # Tilted spin arrow — starts at 45° from z toward right
        angle_from_z = 45 * DEGREES
        spin_tip = UP * 1.8 * np.cos(angle_from_z) + RIGHT * 1.8 * np.sin(angle_from_z)
        spin_arrow = Arrow(ORIGIN, spin_tip, color=CRIMSON, stroke_width=4, buff=0)
        spin_lbl = Text("spin", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        spin_lbl.next_to(spin_arrow.get_end(), UR, buff=0.15)

        # Dashed circle at latitude of spin tip (radius = horizontal component)
        r_lat = 1.8 * np.sin(angle_from_z)
        y_lat = 1.8 * np.cos(angle_from_z)
        # Ellipse approximates a tilted circle in 2D: full width = 2*r_lat, height squished
        lat_circle = Ellipse(width=2 * r_lat * 2, height=2 * r_lat * 0.4,
                             color=CRIMSON, stroke_width=1.5)
        lat_circle.move_to(UP * y_lat)
        lat_circle.set_stroke(opacity=0.55)

        label_precess = LabelChip("precession", accent=CRIMSON, size=24)
        label_precess.to_corner(DR, buff=0.6)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(z_axis), FadeIn(z_lbl), run_time=0.7)
        self.play(GrowArrow(spin_arrow), FadeIn(spin_lbl), run_time=0.8)
        self.play(Create(lat_circle), run_time=0.7)
        self.play(
            Rotate(spin_arrow, angle=TAU, about_point=ORIGIN, run_time=2.5, rate_func=linear),
            Rotate(spin_lbl, angle=TAU, about_point=ORIGIN, run_time=2.5, rate_func=linear),
        )
        self.play(FadeIn(label_precess, shift=UP * 0.1), run_time=0.6)
        self.wait(total - (0.5 + 0.7 + 0.8 + 0.7 + 2.5 + 0.6 + 0.3))


# ── B03 — z-component frozen, only azimuth moves ────────────────────────────
class B03_ZFrozen(Scene):
    def construct(self):
        total = _dur("B03", 10.0)
        eyebrow = LabelChip("constant latitude", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # LEFT: z-component diagram
        z_axis = Arrow(DOWN * 2.0, UP * 2.0, color=TEAL, stroke_width=3, buff=0)
        z_axis.move_to(LEFT * 3.2)

        angle_from_z = 45 * DEGREES
        tip_y = 1.6 * np.cos(angle_from_z)
        tip_x_off = 1.6 * np.sin(angle_from_z)
        spin_tip = z_axis.get_start() + UP * (2.0 + tip_y) + RIGHT * tip_x_off
        spin_a = Arrow(z_axis.get_start() + UP * 2.0, spin_tip, color=CRIMSON,
                       stroke_width=3.5, buff=0)

        # Dashed horizontal bracket for Lz
        lz_line = DashedLine(
            z_axis.get_start() + UP * 2.0,
            z_axis.get_start() + UP * (2.0 + tip_y),
            color=TEAL, stroke_width=2.5, dash_length=0.12
        )
        lz_label = Text("Lz", font=MONO, color=TEAL, font_size=30)
        lz_label.next_to(lz_line, LEFT, buff=0.25)

        # RIGHT: annotation panel
        ann_frozen = Text("z-component:", font=SERIF, color=INK, font_size=30)
        ann_val = Text("frozen", font=DISPLAY, color=TEAL, font_size=38)
        ann_az = Text("azimuth:", font=SERIF, color=INK, font_size=30)
        ann_rot = Text("rotates", font=DISPLAY, color=CRIMSON, font_size=38)
        ann = VGroup(ann_frozen, ann_val, ann_az, ann_rot)
        ann.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ann.move_to(RIGHT * 2.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(z_axis), run_time=0.6)
        self.play(GrowArrow(spin_a), run_time=0.6)
        self.play(Create(lz_line), FadeIn(lz_label), run_time=0.7)
        self.play(FadeIn(ann_frozen), FadeIn(ann_val), run_time=0.7)
        self.play(FadeIn(ann_az), FadeIn(ann_rot), run_time=0.7)
        self.wait(total - 4.5)


# ── B04 — THE QUESTION card ──────────────────────────────────────────────────
class B04_QuestionCard(Scene):
    def construct(self):
        total = _dur("B04", 11.0)
        eyebrow = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)
        q1 = Text("Lz is frozen.", font=DISPLAY, color=TEAL, font_size=42)
        q2 = Text("The azimuth rotates.", font=DISPLAY, color=CRIMSON, font_size=42)
        q3 = Text("What sets the rate,", font=SERIF, color=INK, font_size=36, slant=ITALIC)
        q4 = Text("and why the split?", font=SERIF, color=INK, font_size=36, slant=ITALIC)
        content = VGroup(q1, q2, q3, q4)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.move_to(ORIGIN).shift(DOWN * 0.1)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=SLATE, stroke_width=2.0)
        rule.next_to(q2, DOWN, buff=0.18)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(q2, shift=DOWN * 0.1), run_time=0.7)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(q3), FadeIn(q4), run_time=0.8)
        self.wait(total - 4.0)


# ── B05 — THE PROBLEM: classical vs quantum spin ──────────────────────────────
class B05_ClassicalVsQuantum(Scene):
    def construct(self):
        total = _dur("B05", 11.0)
        eyebrow = LabelChip("NAIVE EXPECTATION", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # LEFT column: classical magnet
        col_cl_lbl = LabelChip("classical magnet", accent=SLATE, size=22)
        mag_arrow = Arrow(DOWN * 1.2 + LEFT * 3.2, UP * 1.2 + LEFT * 3.2,
                          color=INK, stroke_width=4, buff=0)
        b_arrow = Arrow(DOWN * 1.4 + LEFT * 3.2, UP * 1.4 + LEFT * 3.2,
                        color=TEAL, stroke_width=2.5, buff=0)
        cl_result = Text("aligns with B", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        cl_result.next_to(mag_arrow, DOWN, buff=0.3)
        col_cl_lbl.next_to(mag_arrow, UP, buff=0.3)

        # RIGHT column: quantum spin (circles)
        col_q_lbl = LabelChip("quantum spin", accent=CRIMSON, size=22)
        lat_ell = Ellipse(width=2.4, height=0.6, color=CRIMSON, stroke_width=2)
        lat_ell.move_to(RIGHT * 3.2 + UP * 0.6)
        lat_ell.set_stroke(opacity=0.7)
        q_result = Text("just circles", font=DISPLAY, color=CRIMSON, font_size=28)
        q_result.next_to(lat_ell, DOWN, buff=0.4)
        col_q_lbl.next_to(lat_ell, UP, buff=0.3)

        # Divider
        div = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_cl_lbl), GrowArrow(b_arrow), run_time=0.6)
        self.play(GrowArrow(mag_arrow), run_time=0.6)
        self.play(FadeIn(cl_result), run_time=0.6)
        self.play(FadeIn(col_q_lbl), Create(lat_ell), run_time=0.7)
        self.play(FadeIn(q_result), run_time=0.6)
        self.wait(total - 5.0)


# ── B06 — MECHANISM: differential phase advance ───────────────────────────────
class B06_PhaseAdvance(Scene):
    def construct(self):
        total = _dur("B06", 11.0)
        eyebrow = LabelChip("THE MECHANISM", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two phasors: spin-up (TEAL) and spin-down (CRIMSON)
        origin_up = LEFT * 2.8 + DOWN * 0.3
        origin_dn = RIGHT * 0.8 + DOWN * 0.3

        label_up = LabelChip("spin-up", accent=TEAL, size=22)
        label_up.move_to(origin_up + UP * 1.5)
        phasor_up = Arrow(origin_up, origin_up + RIGHT * 1.4, color=TEAL, stroke_width=3.5, buff=0)

        label_dn = LabelChip("spin-down", accent=CRIMSON, size=22)
        label_dn.move_to(origin_dn + UP * 1.5)
        phasor_dn = Arrow(origin_dn, origin_dn + RIGHT * 1.4, color=CRIMSON, stroke_width=3.5, buff=0)

        desc = VGroup(
            Text("each eigenstate advances phase", font=SERIF, color=INK, font_size=26),
            Text("at a different rate", font=SERIF, color=INK, font_size=26),
            Text("relative phase = azimuth", font=MONO, color=CRIMSON, font_size=26),
        )
        desc.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        desc.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(label_up), FadeIn(label_dn), run_time=0.6)
        self.play(GrowArrow(phasor_up), GrowArrow(phasor_dn), run_time=0.8)
        # Rotate phasors at different rates to show differential advance
        self.play(
            Rotate(phasor_up, angle=PI, about_point=origin_up, run_time=1.8, rate_func=linear),
            Rotate(phasor_dn, angle=PI * 0.5, about_point=origin_dn, run_time=1.8, rate_func=linear),
        )
        self.play(FadeIn(desc[0]), run_time=0.5)
        self.play(FadeIn(desc[1]), run_time=0.5)
        self.play(FadeIn(desc[2], shift=UP * 0.1), run_time=0.6)
        self.wait(total - (0.5 + 0.6 + 0.8 + 1.8 + 0.5 + 0.5 + 0.6 + 0.3))


# ── B07 — Larmor frequency formula ───────────────────────────────────────────
class B07_LarmorFormula(Scene):
    def construct(self):
        total = _dur("B07", 11.0)
        eyebrow = LabelChip("LARMOR FREQUENCY", accent=CRIMSON, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        formula = Text("ω  =  γ · B", font=MONO, color=INK, font_size=62)
        formula.move_to(UP * 0.6)

        omega_lbl = SerifLabel("ω = precession rate", accent=CRIMSON, size=26)
        gamma_lbl = SerifLabel("γ = gyromagnetic ratio (particle species)", accent=SLATE, size=26)
        b_lbl = SerifLabel("B = field strength", accent=TEAL, size=26)
        legend = VGroup(omega_lbl, gamma_lbl, b_lbl)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        legend.to_edge(DOWN, buff=0.7)

        rule = Line(LEFT * 3.5, RIGHT * 3.5, color=CRIMSON, stroke_width=2.0)
        rule.next_to(formula, DOWN, buff=0.35)

        double = Text("double B  →  double ω", font=SERIF, color=INK, font_size=30, slant=ITALIC)
        double.next_to(rule, DOWN, buff=0.35)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(formula, shift=UP * 0.15), run_time=0.9)
        self.play(Create(rule), run_time=0.5)
        self.play(FadeIn(double), run_time=0.7)
        self.play(FadeIn(omega_lbl), run_time=0.4)
        self.play(FadeIn(gamma_lbl), run_time=0.4)
        self.play(FadeIn(b_lbl), run_time=0.4)
        self.wait(total - 5.0)


# ── B08 — Why Lz stays frozen: amplitudes unchanged ──────────────────────────
class B08_AmplitudesFixed(Scene):
    def construct(self):
        total = _dur("B08", 11.0)
        eyebrow = LabelChip("WHY Lz IS FROZEN", accent=TEAL, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Two-column: LEFT = phase changes; RIGHT = amplitudes don't
        col_phase = VGroup(
            LabelChip("phase", accent=CRIMSON, size=22),
            Text("e^{-iωt/2}", font=MONO, color=CRIMSON, font_size=34),
            Text("changes", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC),
        )
        col_phase.arrange(DOWN, buff=0.38)
        col_phase.move_to(LEFT * 3.0)

        col_amp = VGroup(
            LabelChip("amplitude", accent=TEAL, size=22),
            Text("|c_↑|², |c_↓|²", font=MONO, color=TEAL, font_size=34),
            Text("unchanged", font=DISPLAY, color=TEAL, font_size=28),
        )
        col_amp.arrange(DOWN, buff=0.38)
        col_amp.move_to(RIGHT * 3.0)

        div = Line(UP * 1.6, DOWN * 1.6, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN)

        conclusion = Text("polar angle fixed  →  Lz fixed", font=MONO, color=TEAL, font_size=28)
        conclusion.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(col_phase[0]), FadeIn(col_amp[0]), run_time=0.6)
        self.play(FadeIn(col_phase[1]), FadeIn(col_amp[1]), run_time=0.7)
        self.play(FadeIn(col_phase[2]), FadeIn(col_amp[2]), run_time=0.7)
        self.play(FadeIn(conclusion, shift=UP * 0.12), run_time=0.7)
        self.wait(total - 4.5)


# ── B10 — THE EXAMPLE: 60° tilt at 1.5 T ────────────────────────────────────
class B10_Example(Scene):
    def construct(self):
        total = _dur("B10", 12.0)
        eyebrow = LabelChip("EXAMPLE (illustrative)", accent=SLATE, size=22)
        eyebrow.to_corner(UL, buff=0.6)

        # Setup label
        setup = VGroup(
            Text("θ = 60° from z-axis", font=MONO, color=INK, font_size=30),
            Text("B = 1.5 T", font=MONO, color=TEAL, font_size=30),
        )
        setup.arrange(RIGHT, buff=1.0)
        setup.move_to(UP * 1.5)

        rule_setup = Line(LEFT * 5.0, RIGHT * 5.0, color=SLATE, stroke_width=1.5)
        rule_setup.next_to(setup, DOWN, buff=0.25)

        # Two result columns
        col_lz = VGroup(
            LabelChip("Lz", accent=TEAL, size=24),
            Text("ℏ · cos 60°", font=MONO, color=INK, font_size=32),
            Text("= ℏ/2", font=MONO, color=TEAL, font_size=38),
            Text("never changes", font=SERIF, color=TEAL, font_size=26, slant=ITALIC),
        )
        col_lz.arrange(DOWN, buff=0.3)
        col_lz.move_to(LEFT * 2.8 + DOWN * 0.4)

        col_freq = VGroup(
            LabelChip("transverse signal", accent=CRIMSON, size=22),
            Text("63.9 MHz", font=MONO, color=CRIMSON, font_size=38),
            Text("= γ · 1.5 T", font=MONO, color=INK, font_size=28),
            Text("azimuth circles at this rate", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC),
        )
        col_freq.arrange(DOWN, buff=0.3)
        col_freq.move_to(RIGHT * 2.8 + DOWN * 0.4)

        div = Line(UP * 0.8, DOWN * 2.4, color=INK, stroke_width=1.2)
        div.move_to(ORIGIN + DOWN * 0.8)

        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(Create(rule_setup), run_time=0.4)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(col_lz[0]), FadeIn(col_freq[0]), run_time=0.6)
        self.play(FadeIn(col_lz[1]), FadeIn(col_freq[1]), run_time=0.7)
        self.play(FadeIn(col_lz[2]), FadeIn(col_freq[2]), run_time=0.7)
        self.play(FadeIn(col_lz[3]), FadeIn(col_freq[3]), run_time=0.7)
        self.wait(total - 5.5)


# ── B11 — RECAP endcard ──────────────────────────────────────────────────────
class B11_Endcard(Scene):
    def construct(self):
        total = _dur("B11", 10.0)
        kicker = LabelChip("QUANTUM MECHANICS", accent=SLATE, size=24)
        kicker.to_corner(UL, buff=0.6)
        line1 = Text("ω  =  γ · B.", font=MONO, color=INK, font_size=44)
        line1.move_to(UP * 0.8)
        line2 = Text("The z-component is frozen.", font=MONO, color=TEAL, font_size=34)
        line2.move_to(UP * 0.05)
        line3 = Text("The azimuth circles.", font=MONO, color=CRIMSON, font_size=34)
        line3.move_to(DOWN * 0.7)
        sub = Text("Phase advances. Amplitudes don't.", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        sub.to_edge(DOWN, buff=0.9)

        end_box = Rectangle(width=0.6, height=0.6).set_fill(SLATE, 0.8).set_stroke(SLATE, 2.0)
        end_box.to_corner(DR, buff=0.6)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.8)
        self.play(FadeIn(line2, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(line3, shift=DOWN * 0.1), run_time=0.7)
        self.play(GrowFromCenter(end_box), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
        self.wait(total - 4.5)
