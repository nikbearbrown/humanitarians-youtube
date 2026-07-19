"""vox_scenes.py — Attractive Pulls the Wave In, Repulsive Pushes It Out
(vox-phase-shift, slate cut, 16:9)

Color law: TEAL = attractive potential (delta > 0, wave pulled in, crests advanced)
           CRIMSON = repulsive potential (delta < 0, wave pushed out, crests behind)
EXCLUSIONS: no partial-wave-sum formula, no cross-section derivation,
            no Levinson theorem.
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


# ── B01: COLD OPEN — beam hits hidden object, shifted wave emerges ─────────────
class B01_HiddenObject(Scene):
    def construct(self):
        dur = DUR.get("B01", 10.0)
        title = Text("A hidden object. A shifted wave.", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Incident beam: horizontal arrow
        beam_arrow = Arrow(LEFT * 5.5, LEFT * 1.5, color=INK, stroke_width=2.5,
                           buff=0)
        beam_lbl = Text("incident beam", font=SERIF, font_size=20, color=INK,
                        slant=ITALIC)
        beam_lbl.next_to(beam_arrow, UP, buff=0.2)
        # Hidden object: question-mark box
        obj_box = Square(side_length=1.0, color=SLATE, stroke_width=2.5)
        obj_box.move_to(ORIGIN)
        obj_q = Text("?", font=DISPLAY, font_size=36, color=SLATE)
        obj_q.move_to(ORIGIN)
        # Outgoing shifted wave: wiggly line to the right
        # Draw as a series of arcs approximating a sine wave
        wave_pts = [np.array([1.5 + 0.45 * i, 0.4 * np.sin(i * PI / 1.5), 0])
                    for i in range(12)]
        wave_line = VMobject(color=TEAL, stroke_width=2.5)
        wave_line.set_points_smoothly(wave_pts)
        wave_lbl = Text("shifted wave", font=SERIF, font_size=20, color=TEAL,
                        slant=ITALIC)
        wave_lbl.move_to(RIGHT * 4.0 + DOWN * 1.2)

        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowArrow(beam_arrow), FadeIn(beam_lbl), run_time=dur * 0.25)
        self.play(FadeIn(obj_box), FadeIn(obj_q), run_time=dur * 0.20)
        self.play(Create(wave_line), run_time=dur * 0.35)
        self.play(FadeIn(wave_lbl), run_time=dur * 0.20)


# ── B02: COLD OPEN — attractive vs repulsive: crests forward vs behind ─────────
class B02_AttractiveRepulsive(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        title = Text("Same beam. Two different forces. Two different shifts.",
                     font=DISPLAY, font_size=24, color=INK).move_to(UP * 3.0)
        divider = Line(UP * 2.2, DOWN * 2.8, color=INK, stroke_width=1.5)

        # Left: attractive — crests shifted forward (teal)
        att_lbl = LabelChip("attractive", accent=TEAL, size=22)
        att_lbl.move_to(LEFT * 3.5 + UP * 1.8)
        # Reference crest mark (dashed)
        ref_dash_L = DashedLine(LEFT * 3.5 + UP * 1.1, LEFT * 3.5 + DOWN * 0.5,
                                color=INK, stroke_width=1.5, dash_length=0.12)
        ref_lbl_L = Text("free", font=SERIF, font_size=18, color=INK, slant=ITALIC)
        ref_lbl_L.next_to(ref_dash_L, UP, buff=0.1)
        # Shifted crest mark (teal, ahead)
        att_dash = Line(LEFT * 2.7 + UP * 1.1, LEFT * 2.7 + DOWN * 0.5,
                        color=TEAL, stroke_width=2.5)
        att_crest_lbl = Text("scattered", font=SERIF, font_size=18, color=TEAL,
                             slant=ITALIC)
        att_crest_lbl.next_to(att_dash, UP, buff=0.1)
        # Arrow showing advance
        att_arr = Arrow(LEFT * 3.5 + DOWN * 0.8, LEFT * 2.7 + DOWN * 0.8,
                        color=TEAL, stroke_width=2.0, buff=0)
        att_delta = Text("delta > 0", font=MONO, font_size=20, color=TEAL)
        att_delta.move_to(LEFT * 3.1 + DOWN * 1.5)

        # Right: repulsive — crests shifted backward (crimson)
        rep_lbl = LabelChip("repulsive", accent=CRIMSON, size=22)
        rep_lbl.move_to(RIGHT * 3.5 + UP * 1.8)
        ref_dash_R = DashedLine(RIGHT * 3.5 + UP * 1.1, RIGHT * 3.5 + DOWN * 0.5,
                                color=INK, stroke_width=1.5, dash_length=0.12)
        ref_lbl_R = Text("free", font=SERIF, font_size=18, color=INK, slant=ITALIC)
        ref_lbl_R.next_to(ref_dash_R, UP, buff=0.1)
        rep_dash = Line(RIGHT * 4.3 + UP * 1.1, RIGHT * 4.3 + DOWN * 0.5,
                        color=CRIMSON, stroke_width=2.5)
        rep_crest_lbl = Text("scattered", font=SERIF, font_size=18, color=CRIMSON,
                             slant=ITALIC)
        rep_crest_lbl.next_to(rep_dash, UP, buff=0.1)
        rep_arr = Arrow(RIGHT * 3.5 + DOWN * 0.8, RIGHT * 4.3 + DOWN * 0.8,
                        color=CRIMSON, stroke_width=2.0, buff=0)
        rep_delta = Text("delta < 0", font=MONO, font_size=20, color=CRIMSON)
        rep_delta.move_to(RIGHT * 3.9 + DOWN * 1.5)

        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(att_lbl), Create(ref_dash_L), FadeIn(ref_lbl_L),
                  run_time=dur * 0.20)
        self.play(Create(att_dash), FadeIn(att_crest_lbl), GrowArrow(att_arr),
                  FadeIn(att_delta), run_time=dur * 0.30)
        self.play(FadeIn(rep_lbl), Create(ref_dash_R), FadeIn(ref_lbl_R),
                  run_time=dur * 0.20)
        self.play(Create(rep_dash), FadeIn(rep_crest_lbl), GrowArrow(rep_arr),
                  FadeIn(rep_delta), run_time=dur * 0.30)


# ── B04: THE PROBLEM — free-particle reference wave ───────────────────────────
class B04_ReferenceWave(Scene):
    def construct(self):
        dur = DUR.get("B04", 9.0)
        title = Text("The reference: no scatterer, no force", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Draw a sine wave as the free-particle reference
        axes = Axes(
            x_range=[0, 10, 2], y_range=[-1.5, 1.5, 1],
            x_length=10.0, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.5,
                         "include_tip": False, "include_numbers": False},
        )
        axes.move_to(DOWN * 0.5)
        free_wave = axes.plot(
            lambda x: np.sin(x), x_range=[0, 10, 0.05],
            color=INK, stroke_width=2.5
        )
        free_lbl = Text("free particle wave: sin(kr)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC)
        free_lbl.move_to(DOWN * 2.4)
        # Mark one crest — use fixed coords (axes.c2p returns stub in static check)
        # crest at x=PI/2 ~ 1.57 in data; axes x_length=10 over x_range [0,10]
        # => pixel x = axes_origin_x + (1.57/10)*10 units = left edge + ~1.57 units
        # Axes centered at DOWN*0.5, x from -5 to +5 in scene units
        # x=PI/2 data -> scene x = -5.0 + (PI/2)/10.0*10.0 = -5 + PI/2 ~ -3.43
        crest_dash = DashedLine(
            np.array([-3.43, -0.5 - 1.2, 0]),
            np.array([-3.43, -0.5 + 1.2, 0]),
            color=INK, stroke_width=1.5, dash_length=0.10
        )
        crest_lbl = Text("crest", font=SERIF, font_size=18, color=INK, slant=ITALIC)
        crest_lbl.move_to(UP * 1.7 + LEFT * 3.0)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(axes), run_time=dur * 0.20)
        self.play(Create(free_wave), run_time=dur * 0.45)
        self.play(FadeIn(free_lbl), run_time=dur * 0.15)
        self.play(Create(crest_dash), FadeIn(crest_lbl), run_time=dur * 0.20)


# ── B05: THE PROBLEM — reference vs scattered wave, showing phase shift ────────
class B05_PhaseShiftDiagram(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        title = Text("Same wavelength — but shifted", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        axes = Axes(
            x_range=[0, 10, 2], y_range=[-1.5, 1.5, 1],
            x_length=10.0, y_length=2.8,
            axis_config={"color": INK, "stroke_width": 1.5,
                         "include_tip": False, "include_numbers": False},
        )
        axes.move_to(DOWN * 0.3)
        delta_val = 1.2   # radians, positive shift (attractive)
        free_wave = axes.plot(
            lambda x: np.sin(x), x_range=[0, 10, 0.05],
            color=INK, stroke_width=2.0
        )
        scat_wave = axes.plot(
            lambda x: np.sin(x + delta_val), x_range=[0, 10, 0.05],
            color=TEAL, stroke_width=2.5
        )
        free_lbl = Text("free wave", font=SERIF, font_size=18, color=INK, slant=ITALIC)
        free_lbl.move_to(UP * 1.9 + LEFT * 4.5)
        scat_lbl = Text("scattered wave", font=SERIF, font_size=18, color=TEAL,
                        slant=ITALIC)
        scat_lbl.move_to(UP * 1.9 + LEFT * 1.2)

        # Crest markers — use fixed coords (axes.c2p returns stub in static check)
        # Axes x_range [0,10], x_length=10.0, centered at DOWN*0.3
        # scene_x = -5.0 + data_x; scene_y_center = -0.3
        # free crest at data_x = PI/2 ~ 1.57 => scene_x ~ -5.0+1.57 = -3.43
        # scat crest at data_x = PI/2 - delta_val ~ 1.57-1.2 = 0.37 => scene_x ~ -4.63
        free_cx_sc = -5.0 + PI / 2.0       # ~ -3.43
        scat_cx_sc = -5.0 + PI / 2.0 - delta_val  # ~ -4.63
        free_dash = DashedLine(
            np.array([free_cx_sc, -0.3 - 1.3, 0]),
            np.array([free_cx_sc, -0.3 + 1.3, 0]),
            color=INK, stroke_width=1.5, dash_length=0.10
        )
        scat_dash = DashedLine(
            np.array([scat_cx_sc, -0.3 - 1.3, 0]),
            np.array([scat_cx_sc, -0.3 + 1.3, 0]),
            color=TEAL, stroke_width=2.0, dash_length=0.10
        )
        # Delta label between the two dashes
        delta_lbl = Text("delta", font=MONO, font_size=22, color=TEAL)
        mid_cx_sc = (free_cx_sc + scat_cx_sc) / 2.0
        delta_lbl.move_to(np.array([mid_cx_sc, -0.3 - 1.7, 0]))

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(axes), run_time=dur * 0.15)
        self.play(Create(free_wave), FadeIn(free_lbl), run_time=dur * 0.30)
        self.play(Create(scat_wave), FadeIn(scat_lbl), run_time=dur * 0.30)
        self.play(Create(free_dash), Create(scat_dash), run_time=dur * 0.15)
        self.play(FadeIn(delta_lbl), run_time=dur * 0.10)


# ── B07: THE MECHANISM — attractive well, wave faster inside ──────────────────
class B07_AttractiveWell(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        title = Text("Attractive well: faster inside, crests advance",
                     font=DISPLAY, font_size=24, color=INK).move_to(UP * 3.0)
        # Draw a potential well schematically
        well_pts = [
            np.array([-5.5, 0.0, 0]), np.array([-1.5, 0.0, 0]),
            np.array([-1.5, -1.8, 0]), np.array([1.5, -1.8, 0]),
            np.array([1.5, 0.0, 0]), np.array([5.5, 0.0, 0])
        ]
        well = VMobject(color=TEAL, stroke_width=2.5)
        well.set_points_smoothly(well_pts)
        v_zero_lbl = Text("V = 0", font=MONO, font_size=18, color=INK)
        v_zero_lbl.move_to(LEFT * 4.5 + UP * 0.4)
        well_lbl = Text("attractive well: V < 0", font=MONO, font_size=18, color=TEAL)
        well_lbl.move_to(DOWN * 2.3)

        # Wave outside: normal spacing; inside: compressed
        # Outside left: wide sine
        outside_left_pts = [
            np.array([-5.5 + 0.55 * i, 0.5 * np.sin(i * PI / 1.2) + 0.6, 0])
            for i in range(7)
        ]
        outside_left = VMobject(color=INK, stroke_width=2.0)
        outside_left.set_points_smoothly(outside_left_pts)
        # Inside: compressed sine
        inside_pts = [
            np.array([-1.5 + 0.38 * i, 0.5 * np.sin(i * PI / 0.9) + 0.6, 0])
            for i in range(9)
        ]
        inside_wave = VMobject(color=TEAL, stroke_width=2.5)
        inside_wave.set_points_smoothly(inside_pts)
        inside_note = SerifLabel("shorter lambda inside", TEAL, size=18)
        inside_note.move_to(ORIGIN + UP * 1.5)
        # Outside right: normal spacing but crests advanced
        outside_right_pts = [
            np.array([1.7 + 0.55 * i, 0.5 * np.sin(i * PI / 1.2 + 0.9) + 0.6, 0])
            for i in range(7)
        ]
        outside_right = VMobject(color=TEAL, stroke_width=2.0)
        outside_right.set_points_smoothly(outside_right_pts)
        advance_lbl = LabelChip("crests ahead: delta > 0", accent=TEAL, size=20)
        advance_lbl.move_to(RIGHT * 3.5 + DOWN * 0.0)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(well), FadeIn(v_zero_lbl), FadeIn(well_lbl),
                  run_time=dur * 0.25)
        self.play(Create(outside_left), run_time=dur * 0.20)
        self.play(Create(inside_wave), FadeIn(inside_note), run_time=dur * 0.25)
        self.play(Create(outside_right), run_time=dur * 0.20)
        self.play(FadeIn(advance_lbl), run_time=dur * 0.10)


# ── B08: THE MECHANISM — repulsive barrier, wave slower inside ────────────────
class B08_RepulsiveBarrier(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("Repulsive barrier: slower inside, crests fall behind",
                     font=DISPLAY, font_size=24, color=INK).move_to(UP * 3.0)
        # Potential barrier
        barrier_pts = [
            np.array([-5.5, 0.0, 0]), np.array([-1.5, 0.0, 0]),
            np.array([-1.5, 1.6, 0]), np.array([1.5, 1.6, 0]),
            np.array([1.5, 0.0, 0]), np.array([5.5, 0.0, 0])
        ]
        barrier = VMobject(color=CRIMSON, stroke_width=2.5)
        barrier.set_points_smoothly(barrier_pts)
        v_zero_lbl = Text("V = 0", font=MONO, font_size=18, color=INK)
        v_zero_lbl.move_to(LEFT * 4.5 + DOWN * 0.4)
        barrier_lbl = Text("repulsive barrier: V > 0", font=MONO, font_size=18,
                           color=CRIMSON)
        barrier_lbl.move_to(UP * 2.3)

        # Outside left: normal sine
        outside_left_pts = [
            np.array([-5.5 + 0.55 * i, 0.5 * np.sin(i * PI / 1.2) - 0.8, 0])
            for i in range(7)
        ]
        outside_left = VMobject(color=INK, stroke_width=2.0)
        outside_left.set_points_smoothly(outside_left_pts)
        # Inside: stretched sine
        inside_pts = [
            np.array([-1.5 + 0.5 * i, 0.4 * np.sin(i * PI / 1.4) - 0.8, 0])
            for i in range(7)
        ]
        inside_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        inside_wave.set_points_smoothly(inside_pts)
        inside_note = SerifLabel("longer lambda inside", CRIMSON, size=18)
        inside_note.move_to(ORIGIN + DOWN * 1.6)
        # Outside right: normal spacing but crests behind
        outside_right_pts = [
            np.array([1.7 + 0.55 * i, 0.5 * np.sin(i * PI / 1.2 - 0.8) - 0.8, 0])
            for i in range(7)
        ]
        outside_right = VMobject(color=CRIMSON, stroke_width=2.0)
        outside_right.set_points_smoothly(outside_right_pts)
        behind_lbl = LabelChip("crests behind: delta < 0", accent=CRIMSON, size=20)
        behind_lbl.move_to(RIGHT * 3.5 + DOWN * 0.0)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(barrier), FadeIn(v_zero_lbl), FadeIn(barrier_lbl),
                  run_time=dur * 0.25)
        self.play(Create(outside_left), run_time=dur * 0.20)
        self.play(Create(inside_wave), FadeIn(inside_note), run_time=dur * 0.25)
        self.play(Create(outside_right), run_time=dur * 0.20)
        self.play(FadeIn(behind_lbl), run_time=dur * 0.10)


# ── B09: THE MECHANISM — summary table: sign and magnitude ────────────────────
class B09_SignMagnitudeSummary(Scene):
    def construct(self):
        dur = DUR.get("B09", 10.0)
        title = Text("Sign = type. Size = strength.", font=DISPLAY,
                     font_size=26, color=INK).move_to(UP * 3.0)
        # Four rows: strong att, weak att, weak rep, strong rep
        rows = [
            ("strong attractive", "delta >> 0", TEAL),
            ("weak attractive",   "delta > 0",  TEAL),
            ("weak repulsive",    "delta < 0",  CRIMSON),
            ("strong repulsive",  "delta << 0", CRIMSON),
        ]
        row_groups = VGroup()
        for label, delta_str, col in rows:
            left_txt = Text(label, font=SERIF, font_size=22, color=col, slant=ITALIC)
            right_txt = Text(delta_str, font=MONO, font_size=22, color=col)
            row_grp = VGroup(left_txt, right_txt)
            row_grp.arrange(RIGHT, buff=1.2)
            row_groups.add(row_grp)
        row_groups.arrange(DOWN, buff=0.55).move_to(DOWN * 0.2)
        # Divider line provides shape motion
        divider = Line(LEFT * 0.5 + UP * 2.8, LEFT * 0.5 + DOWN * 2.8,
                       color=INK, stroke_width=1.5)
        self.play(FadeIn(title), Create(divider), run_time=0.4)
        for rg in row_groups:
            self.play(FadeIn(rg), run_time=dur * 0.20)
        self.wait(dur * 0.05)


# ── B11: THE IMPLICATION — phase-shift analysis reconstructs force ────────────
class B11_PhaseShiftAnalysis(Scene):
    def construct(self):
        dur = DUR.get("B11", 10.0)
        title = Text("Measure angles. Extract phase shifts. Know the force.",
                     font=DISPLAY, font_size=24, color=INK).move_to(UP * 3.0)
        # Central scatterer dot
        center = Dot(ORIGIN, color=SLATE, radius=0.15)
        center_lbl = LabelChip("hidden force", accent=SLATE, size=20)
        center_lbl.move_to(DOWN * 0.55)
        # Incident arrow
        inc_arr = Arrow(LEFT * 5.0, LEFT * 0.3, color=INK, stroke_width=2.0, buff=0)
        # Scattered rays at various angles
        angles = [30, 60, 90, 120, 150]
        rays = VGroup()
        angle_lbls = VGroup()
        for ang in angles:
            rad = ang * PI / 180.0
            end_pt = np.array([2.5 * np.cos(rad), 2.5 * np.sin(rad), 0])
            ray = Arrow(ORIGIN, end_pt, color=TEAL, stroke_width=1.8, buff=0.2)
            rays.add(ray)
            ang_lbl = Text(f"{ang}deg", font=MONO, font_size=16, color=INK)
            ang_lbl.move_to(end_pt * 1.25)
            angle_lbls.add(ang_lbl)
        extract_lbl = SerifLabel("angles -> phase shifts -> force", TEAL, size=20)
        extract_lbl.move_to(DOWN * 2.8)

        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowArrow(inc_arr), FadeIn(center), FadeIn(center_lbl),
                  run_time=dur * 0.25)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.1),
                  run_time=dur * 0.30)
        self.play(LaggedStart(*[FadeIn(l) for l in angle_lbls], lag_ratio=0.1),
                  run_time=dur * 0.25)
        self.play(FadeIn(extract_lbl), run_time=dur * 0.20)


# ── B12: THE IMPLICATION — nuclear physics phase-shift analysis ───────────────
class B12_NuclearPhaseShifts(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        title = Text("Nuclear forces — read from phase shifts before any theory",
                     font=DISPLAY, font_size=23, color=INK).move_to(UP * 3.0)
        # Simple bar chart: phase shifts at different energies (illustrative)
        energies = [10, 50, 100, 200, 300]
        # s-wave (ell=0) phase shifts for pp scattering (schematic, positive = attractive)
        deltas = [60, 42, 30, 18, 8]   # degrees, schematic
        bar_width = 0.7
        bar_color = TEAL
        bars = VGroup()
        e_lbls = VGroup()
        d_lbls = VGroup()
        for i, (e, d) in enumerate(zip(energies, deltas)):
            x = -3.5 + i * 1.6
            bar_h = d / 25.0  # scale
            bar = Rectangle(width=bar_width, height=bar_h, color=bar_color,
                            fill_color=bar_color, fill_opacity=0.5,
                            stroke_width=1.5)
            bar.move_to(np.array([x, bar_h / 2.0 - 1.8, 0]))
            bars.add(bar)
            e_lbl = Text(f"{e}", font=MONO, font_size=16, color=INK)
            e_lbl.move_to(np.array([x, -2.2, 0]))
            e_lbls.add(e_lbl)
            d_lbl = Text(f"{d}d", font=MONO, font_size=16, color=TEAL)
            d_lbl.move_to(np.array([x, bar_h / 2.0 - 1.8 + bar_h / 2.0 + 0.2, 0]))
            d_lbls.add(d_lbl)

        baseline = Line(LEFT * 5.0 + DOWN * 1.8, RIGHT * 5.0 + DOWN * 1.8,
                        color=INK, stroke_width=1.5)
        e_axis_lbl = Text("energy (MeV)", font=SERIF, font_size=18, color=INK,
                          slant=ITALIC)
        e_axis_lbl.move_to(DOWN * 2.7)
        delta_axis_lbl = Text("phase shift (degrees)", font=SERIF, font_size=18,
                              color=TEAL, slant=ITALIC)
        delta_axis_lbl.move_to(UP * 1.5 + LEFT * 4.5)
        note = SerifLabel("p-p s-wave: schematic", INK, size=17)
        note.move_to(UP * 1.0 + RIGHT * 3.5)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(baseline), FadeIn(e_axis_lbl), FadeIn(delta_axis_lbl),
                  run_time=dur * 0.20)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.1),
                  run_time=dur * 0.40)
        self.play(LaggedStart(*[FadeIn(l) for l in e_lbls], lag_ratio=0.05),
                  LaggedStart(*[FadeIn(l) for l in d_lbls], lag_ratio=0.05),
                  run_time=dur * 0.20)
        self.play(FadeIn(note), run_time=dur * 0.20)


# ── B13: THE EXAMPLE — worked example with numbers ────────────────────────────
class B13_WorkedExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 17.0)
        title = Text("Illustrative: 2 eV well, 0.5 nm radius", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.0)
        # Two-panel comparison
        divider = Line(UP * 2.2, DOWN * 2.8, color=INK, stroke_width=1.5)

        # Left panel: attractive well
        att_title = LabelChip("attractive well", accent=TEAL, size=20)
        att_title.move_to(LEFT * 3.2 + UP * 1.9)
        att_lines = VGroup(
            Text("KE inside: 3 eV", font=MONO, font_size=18, color=TEAL),
            Text("lambda inside: shorter", font=MONO, font_size=18, color=TEAL),
            Text("extra cycles in well", font=MONO, font_size=18, color=TEAL),
            Text("crests advance", font=MONO, font_size=18, color=TEAL),
        )
        att_lines.arrange(DOWN, buff=0.3).move_to(LEFT * 3.2 + DOWN * 0.3)
        att_result = LabelChip("delta ~ +30 degrees", accent=TEAL, size=22)
        att_result.move_to(LEFT * 3.2 + DOWN * 2.3)

        # Right panel: repulsive barrier
        rep_title = LabelChip("repulsive barrier", accent=CRIMSON, size=20)
        rep_title.move_to(RIGHT * 3.2 + UP * 1.9)
        rep_lines = VGroup(
            Text("KE inside: -1 eV*", font=MONO, font_size=18, color=CRIMSON),
            Text("  (* evanescent region)", font=SERIF, font_size=15, color=INK,
                 slant=ITALIC),
            Text("lambda inside: longer", font=MONO, font_size=18, color=CRIMSON),
            Text("fewer cycles in barrier", font=MONO, font_size=18, color=CRIMSON),
            Text("crests fall behind", font=MONO, font_size=18, color=CRIMSON),
        )
        rep_lines.arrange(DOWN, buff=0.22).move_to(RIGHT * 3.2 + DOWN * 0.2)
        rep_result = LabelChip("delta ~ -30 degrees", accent=CRIMSON, size=22)
        rep_result.move_to(RIGHT * 3.2 + DOWN * 2.3)

        self.play(FadeIn(title), Create(divider), run_time=0.4)
        self.play(FadeIn(att_title), run_time=dur * 0.08)
        self.play(LaggedStart(*[FadeIn(l) for l in att_lines], lag_ratio=0.15),
                  run_time=dur * 0.28)
        self.play(FadeIn(att_result), run_time=dur * 0.10)
        self.play(FadeIn(rep_title), run_time=dur * 0.08)
        self.play(LaggedStart(*[FadeIn(l) for l in rep_lines], lag_ratio=0.12),
                  run_time=dur * 0.30)
        self.play(FadeIn(rep_result), run_time=dur * 0.10)
        self.wait(dur * 0.06)
