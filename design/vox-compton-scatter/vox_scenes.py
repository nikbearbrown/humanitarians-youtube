import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------------------
# B01 — Title card
# ---------------------------------------------------------------------------
class B01_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = GROUND
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22)
        chip.to_edge(UP, buff=0.55)
        title = Text(
            "Why X-Rays Change\nColor When They\nBounce Off Electrons",
            font=DISPLAY, font_size=52, color=INK,
            line_spacing=1.15
        ).center()
        sub = Text("the compton effect", font=DISPLAY, font_size=28, color=TEAL).next_to(title, DOWN, buff=0.5)
        self.play(GrowFromCenter(chip))
        self.play(FadeIn(title))
        self.play(FadeIn(sub))
        self.wait(max(0.1, DUR.get("B01", 9.0) - 3.2))


# ---------------------------------------------------------------------------
# B02 — Classical prediction: wave in, same-wavelength wave out
# ---------------------------------------------------------------------------
class B02_ClassicalPrediction(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        # Left label
        left_lbl = Text("classical\nwave theory", font=DISPLAY, font_size=26, color=INK).move_to([-5.0, 2.5, 0])

        # Incoming wave (CRIMSON) — sinusoid approaching electron
        def wave_path(x_arr, amp=0.3, freq=2.5, x_shift=0.0):
            return [[x, amp * np.sin(freq * (x - x_shift)), 0] for x in x_arr]

        xs_in = np.linspace(-6.0, -1.2, 80)
        wave_in_pts = wave_path(xs_in)
        wave_in = VMobject(color=CRIMSON, stroke_width=3)
        wave_in.set_points_as_corners(wave_in_pts)

        # Arrow showing incoming direction
        in_arrow = Arrow([-6.0, 0, 0], [-1.8, 0, 0], color=CRIMSON, buff=0.0, stroke_width=2, tip_length=0.2)

        # Electron dot at center
        electron = Dot(ORIGIN, radius=0.22, color=TEAL)
        e_lbl = Text("e⁻", font=MONO, font_size=24, color=INK).next_to(electron, UP, buff=0.12)

        # Outgoing wave — same wavelength (CRIMSON — classical: no shift)
        xs_out = np.linspace(1.2, 6.0, 80)
        wave_out_pts = wave_path(xs_out)
        wave_out = VMobject(color=CRIMSON, stroke_width=3)
        wave_out.set_points_as_corners(wave_out_pts)
        out_arrow = Arrow([1.8, 0, 0], [6.0, 0, 0], color=CRIMSON, buff=0.0, stroke_width=2, tip_length=0.2)

        # Labels
        in_wl_lbl = Text("λ = 0.071 nm", font=MONO, font_size=24, color=CRIMSON).move_to([-3.5, -0.9, 0])
        out_wl_lbl = Text("λ = 0.071 nm", font=MONO, font_size=CRIMSON).move_to([3.5, -0.9, 0])
        out_wl_lbl = Text("λ = 0.071 nm", font=MONO, font_size=24, color=CRIMSON).move_to([3.5, -0.9, 0])

        no_shift = Text("no shift", font=DISPLAY, font_size=30, color=CRIMSON).move_to([0, -2.4, 0])
        cross_line1 = Line(no_shift.get_left() + [-0.1, 0, 0], no_shift.get_right() + [0.1, 0, 0], color=CRIMSON, stroke_width=3)

        self.play(FadeIn(left_lbl))
        self.play(Create(wave_in), GrowArrow(in_arrow))
        self.play(FadeIn(electron), FadeIn(e_lbl))
        self.play(Create(wave_out), GrowArrow(out_arrow))
        self.play(FadeIn(in_wl_lbl))
        self.play(FadeIn(out_wl_lbl))
        self.play(FadeIn(no_shift))
        self.play(Create(cross_line1))
        self.wait(max(0.1, DUR.get("B02", 10.0) - 5.8))


# ---------------------------------------------------------------------------
# B03 — Question card
# ---------------------------------------------------------------------------
class B03_QuestionCard(Scene):
    def construct(self):
        self.camera.background_color = GROUND
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22)
        chip.to_edge(UP, buff=0.55)
        body = Text(
            "Incoming: 0.071 nm\nScattered at 90°: 0.073 nm\nClassical prediction: no shift. Why the shift?",
            font=SERIF, font_size=36, color=INK,
            line_spacing=1.3
        ).center()
        self.play(GrowFromCenter(chip))
        self.play(FadeIn(body))
        self.wait(max(0.1, DUR.get("B03", 9.0) - 2.5))


# ---------------------------------------------------------------------------
# B04 — Photon-as-particle: collision with electron
# ---------------------------------------------------------------------------
class B04_PhotonMomentum(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        title = Text("photon-as-particle", font=DISPLAY, font_size=30, color=INK).to_edge(UP, buff=0.5)

        # Incoming photon arrow (TEAL, horizontal)
        photon_in = Arrow([-5.5, 0.5, 0], [-1.2, 0.5, 0], color=TEAL, buff=0.0, stroke_width=3, tip_length=0.25)
        p_in_lbl = Text("p = h/λ", font=MONO, font_size=24, color=TEAL).next_to(photon_in, UP, buff=0.12)

        # Electron at rest
        electron = Dot(ORIGIN, radius=0.22, color=INK)
        e_lbl = Text("e⁻", font=MONO, font_size=24, color=INK).next_to(electron, UP, buff=0.12)

        # Deflected photon at 90° (TEAL, going up-right)
        photon_out = Arrow([0.3, 0.3, 0], [2.8, 2.8, 0], color=TEAL, buff=0.0, stroke_width=3, tip_length=0.25)
        p_out_lbl = Text("λ' > λ", font=MONO, font_size=24, color=TEAL).next_to(photon_out.get_end(), UR, buff=0.12)

        # Electron recoil arrow (down-right)
        recoil_arrow = Arrow([0, -0.3, 0], [2.5, -2.0, 0], color=INK, buff=0.0, stroke_width=2.5, tip_length=0.22)
        recoil_lbl = Text("electron\nrecoil", font=DISPLAY, font_size=24, color=INK).next_to(recoil_arrow.get_end(), DR, buff=0.1)

        # Angle label
        theta_lbl = Text("θ = 90°", font=MONO, font_size=26, color=GOLD).move_to([1.5, 0.9, 0])

        self.play(FadeIn(title))
        self.play(GrowArrow(photon_in), FadeIn(p_in_lbl))
        self.play(FadeIn(electron), FadeIn(e_lbl))
        self.play(GrowArrow(photon_out), FadeIn(p_out_lbl))
        self.play(GrowArrow(recoil_arrow), FadeIn(recoil_lbl))
        self.play(FadeIn(theta_lbl))
        self.wait(max(0.1, DUR.get("B04", 10.0) - 4.8))


# ---------------------------------------------------------------------------
# B05 — Compton formula and Compton wavelength
# ---------------------------------------------------------------------------
class B05_ComptonFormula(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        # Formula
        formula = Text("Δλ = (h / mₑc)(1 − cos θ)", font=MONO, font_size=40, color=INK).move_to([0, 1.5, 0])

        # Underline formula
        formula_line = Line(formula.get_left() + [0, -0.1, 0], formula.get_right() + [0, -0.1, 0], color=TEAL, stroke_width=2)

        # Compton wavelength value
        comp_lbl = Text("h / mₑc  =  2.426 pm", font=MONO, font_size=32, color=TEAL).move_to([0, 0.3, 0])

        # Angle diagram: small arc
        angle_arc = Arc(radius=1.2, start_angle=0, angle=PI/2, color=GOLD, stroke_width=2).move_to([-4.0, -1.5, 0])
        h_ray = Arrow([-4.0, -1.5, 0], [-2.4, -1.5, 0], color=INK, buff=0.0, stroke_width=2, tip_length=0.18)
        v_ray = Arrow([-4.0, -1.5, 0], [-4.0, 0.1, 0], color=TEAL, buff=0.0, stroke_width=2, tip_length=0.18)
        theta_arc_lbl = Text("θ", font=MONO, font_size=28, color=GOLD).move_to([-3.5, -1.1, 0])

        # Table
        table_lines = VGroup(
            Text("θ = 0°    →   Δλ = 0", font=MONO, font_size=26, color=INK),
            Text("θ = 90°  →   Δλ = 2.4 pm", font=MONO, font_size=26, color=TEAL),
            Text("θ = 180° →   Δλ = 4.85 pm", font=MONO, font_size=26, color=INK),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([2.2, -1.8, 0])

        self.play(FadeIn(formula))
        self.play(Create(formula_line))
        self.play(FadeIn(comp_lbl))
        self.play(Create(angle_arc), GrowArrow(h_ray), GrowArrow(v_ray), FadeIn(theta_arc_lbl))
        self.play(FadeIn(table_lines[0]))
        self.play(FadeIn(table_lines[1]))
        self.play(FadeIn(table_lines[2]))
        self.wait(max(0.1, DUR.get("B05", 10.0) - 5.5))


# ---------------------------------------------------------------------------
# B06 — Angle dependence: three collision diagrams
# ---------------------------------------------------------------------------
class B06_AngleDependence(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        title = Text("shift depends on scattering angle", font=DISPLAY, font_size=28, color=INK).to_edge(UP, buff=0.45)

        centers = [np.array([-4.5, -0.3, 0]), np.array([0, -0.3, 0]), np.array([4.5, -0.3, 0])]
        angles = [0, PI/2, PI]
        shifts = ["Δλ = 0", "Δλ = 2.4 pm", "Δλ = 4.85 pm"]
        angle_lbls = ["θ = 0°", "θ = 90°", "θ = 180°"]
        colors = [CRIMSON, TEAL, TEAL]

        electrons = VGroup()
        in_arrows = VGroup()
        out_arrows = VGroup()
        angle_texts = VGroup()
        shift_texts = VGroup()

        for c, ang, shift, albl, col in zip(centers, angles, shifts, angle_lbls, colors):
            e = Dot(c, radius=0.18, color=INK)
            in_arr = Arrow(c + np.array([-1.6, 0, 0]), c + np.array([-0.22, 0, 0]), color=TEAL, buff=0.0, stroke_width=2, tip_length=0.18)
            out_dir = np.array([np.cos(ang), np.sin(ang), 0])
            out_arr = Arrow(c + 0.22 * out_dir, c + 1.6 * out_dir, color=col, buff=0.0, stroke_width=2, tip_length=0.18)
            a_txt = Text(albl, font=MONO, font_size=22, color=GOLD).next_to(e, UP, buff=0.85)
            s_txt = Text(shift, font=MONO, font_size=22, color=col).next_to(e, DOWN, buff=1.0)
            electrons.add(e)
            in_arrows.add(in_arr)
            out_arrows.add(out_arr)
            angle_texts.add(a_txt)
            shift_texts.add(s_txt)

        self.play(FadeIn(title))
        self.play(FadeIn(electrons[0]), GrowArrow(in_arrows[0]))
        self.play(GrowArrow(out_arrows[0]), FadeIn(angle_texts[0]), FadeIn(shift_texts[0]))
        self.play(FadeIn(electrons[1]), GrowArrow(in_arrows[1]))
        self.play(GrowArrow(out_arrows[1]), FadeIn(angle_texts[1]), FadeIn(shift_texts[1]))
        self.play(FadeIn(electrons[2]), GrowArrow(in_arrows[2]))
        self.play(GrowArrow(out_arrows[2]), FadeIn(angle_texts[2]), FadeIn(shift_texts[2]))
        self.wait(max(0.1, DUR.get("B06", 10.0) - 6.0))


# ---------------------------------------------------------------------------
# B07 — Full collision diagram with numbers
# ---------------------------------------------------------------------------
class B07_ElectronRecoil(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        title = Text("θ = 90° — the numbers", font=DISPLAY, font_size=30, color=INK).to_edge(UP, buff=0.5)

        # Electron
        electron = Dot(ORIGIN, radius=0.22, color=INK)
        e_lbl = Text("e⁻\n(at rest)", font=MONO, font_size=22, color=INK).next_to(electron, RIGHT, buff=0.18)

        # Incoming photon
        photon_in = Arrow([-5.0, 0, 0], [-0.25, 0, 0], color=TEAL, buff=0.0, stroke_width=3, tip_length=0.25)
        in_lbl = Text("λ = 0.071 nm\nE = 17.5 keV", font=MONO, font_size=22, color=TEAL).next_to(photon_in, UP, buff=0.1)

        # Scattered photon (90°, upward)
        photon_out = Arrow([0, 0.25, 0], [0, 2.8, 0], color=TEAL, buff=0.0, stroke_width=3, tip_length=0.25)
        out_lbl = Text("λ' = 0.073 nm\nE' = 17.26 keV", font=MONO, font_size=22, color=TEAL).next_to(photon_out, RIGHT, buff=0.1)

        # Recoil electron
        recoil_arrow = Arrow([0.25, 0, 0], [3.5, -1.8, 0], color=GOLD, buff=0.0, stroke_width=2.5, tip_length=0.22)
        recoil_lbl = Text("KE = 0.24 keV", font=MONO, font_size=24, color=GOLD).next_to(recoil_arrow.get_end(), DOWN + RIGHT, buff=0.1)

        # Separator dot
        center_dot = Dot(ORIGIN, radius=0.07, color=GOLD)

        self.play(FadeIn(title))
        self.play(GrowArrow(photon_in), FadeIn(in_lbl))
        self.play(FadeIn(electron), FadeIn(e_lbl))
        self.play(GrowArrow(photon_out), FadeIn(out_lbl))
        self.play(GrowArrow(recoil_arrow), FadeIn(recoil_lbl))
        self.play(FadeIn(center_dot))
        self.wait(max(0.1, DUR.get("B07", 10.0) - 4.5))


# ---------------------------------------------------------------------------
# B08 — Compton Nobel citation
# ---------------------------------------------------------------------------
class B08_ComptonNobel(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        # Citation chip
        chip = LabelChip("Compton  ·  Physical Review  ·  1923", accent=TEAL, size=22)
        chip.move_to([0, 2.6, 0])

        # Nobel label
        nobel_lbl = Text("Nobel Prize in Physics — 1927", font=DISPLAY, font_size=30, color=GOLD).move_to([0, 1.6, 0])

        # Wave prediction: CROSS
        wave_box_rect = Rectangle(width=4.5, height=1.4, fill_color=SLATE, fill_opacity=0.4, stroke_color=CRIMSON, stroke_width=2).move_to([-2.8, 0.0, 0])
        wave_lbl = Text("wave theory:\nno wavelength shift", font=SERIF, font_size=24, color=INK).move_to(wave_box_rect)
        cross1 = Line(wave_box_rect.get_corner(UL), wave_box_rect.get_corner(DR), color=CRIMSON, stroke_width=2)
        cross2 = Line(wave_box_rect.get_corner(UR), wave_box_rect.get_corner(DL), color=CRIMSON, stroke_width=2)

        # Particle prediction: CHECK
        part_box_rect = Rectangle(width=4.5, height=1.4, fill_color=SLATE, fill_opacity=0.4, stroke_color=TEAL, stroke_width=2).move_to([2.8, 0.0, 0])
        part_lbl = Text("particle model:\nmatches Δλ = 2.4 pm", font=SERIF, font_size=24, color=INK).move_to(part_box_rect)
        check_mark = Text("✓", font=DISPLAY, font_size=40, color=TEAL).next_to(part_box_rect, DOWN, buff=0.15)

        self.play(GrowFromCenter(chip))
        self.play(FadeIn(nobel_lbl))
        self.play(FadeIn(wave_box_rect), FadeIn(wave_lbl))
        self.play(Create(cross1), Create(cross2))
        self.play(FadeIn(part_box_rect), FadeIn(part_lbl))
        self.play(FadeIn(check_mark))
        self.wait(max(0.1, DUR.get("B08", 9.0) - 5.0))


# ---------------------------------------------------------------------------
# B09 — Duality bridge: photoelectric + Compton
# ---------------------------------------------------------------------------
class B09_DualityBridge(Scene):
    def construct(self):
        self.camera.background_color = GROUND

        title = Text("two experiments, one conclusion", font=DISPLAY, font_size=28, color=INK).to_edge(UP, buff=0.5)

        # Left column: photoelectric
        left_box = Rectangle(width=4.8, height=3.2, fill_color=SLATE, fill_opacity=0.3, stroke_color=TEAL, stroke_width=2).move_to([-3.2, -0.3, 0])
        left_title = Text("photoelectric\neffect", font=DISPLAY, font_size=26, color=TEAL).move_to([-3.2, 0.9, 0])
        left_formula = Text("KE = hν − Φ", font=MONO, font_size=26, color=INK).move_to([-3.2, -0.1, 0])
        left_note = Text("energy in packets", font=SERIF, font_size=22, color=INK).move_to([-3.2, -1.0, 0])

        # Right column: Compton
        right_box = Rectangle(width=4.8, height=3.2, fill_color=SLATE, fill_opacity=0.3, stroke_color=TEAL, stroke_width=2).move_to([3.2, -0.3, 0])
        right_title = Text("compton\neffect", font=DISPLAY, font_size=26, color=TEAL).move_to([3.2, 0.9, 0])
        right_formula = Text("p = h / λ", font=MONO, font_size=26, color=INK).move_to([3.2, -0.1, 0])
        right_note = Text("momentum in packets", font=SERIF, font_size=22, color=INK).move_to([3.2, -1.0, 0])

        # Shared conclusion
        conclusion = Text("light = discrete packets", font=DISPLAY, font_size=30, color=TEAL).move_to([0, -2.8, 0])

        # Connecting dot
        center_dot = Dot([0, -0.3, 0], radius=0.06, color=GOLD)

        self.play(FadeIn(title))
        self.play(FadeIn(left_box), FadeIn(left_title))
        self.play(FadeIn(left_formula), FadeIn(left_note))
        self.play(FadeIn(right_box), FadeIn(right_title))
        self.play(FadeIn(right_formula), FadeIn(right_note))
        self.play(FadeIn(center_dot))
        self.play(FadeIn(conclusion))
        self.wait(max(0.1, DUR.get("B09", 9.0) - 5.5))


# ---------------------------------------------------------------------------
# B10 — Recap endcard
# ---------------------------------------------------------------------------
class B10_RecapCard(Scene):
    def construct(self):
        self.camera.background_color = GROUND
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22)
        chip.to_edge(UP, buff=0.55)
        body = Text(
            "Photon momentum: p = h/λ.\nShift Δλ = (h/mₑc)(1−cosθ).\nAt 90°: Δλ = 2.4 pm (Compton 1923).",
            font=SERIF, font_size=36, color=INK,
            line_spacing=1.35
        ).center()
        self.play(GrowFromCenter(chip))
        self.play(FadeIn(body))
        self.wait(max(0.1, DUR.get("B10", 9.0) - 2.5))
