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
class B01_Title(Scene):
    def construct(self):
        duration = DUR.get("B01", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 1.9)
        rule1 = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.1)
        mid_box = Rectangle(width=13.5, height=1.1).set_fill(SLATE, 0.07).set_stroke(SLATE, 1)
        mid_box.move_to(UP * 0.2)
        rule2 = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 0.5)
        accent_dot1 = Dot(radius=0.12, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.0)
        accent_dot2 = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.0)
        bottom_rule = Line(LEFT * 5.0, RIGHT * 5.0, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        teal_accent = Line(LEFT * 1.5, RIGHT * 1.5, color=TEAL, stroke_width=1.2).move_to(DOWN * 2.5)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.9)
        headline = Text("Why One Photon Can Become Two Identical Twins", font=DISPLAY, font_size=26,
                        color=INK).move_to(UP * 0.2)
        sub = Text("Stimulated emission and coherence", font=SERIF, font_size=24,
                   color=TEAL).move_to(DOWN * 1.0)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule1), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(mid_box), run_time=0.4)
        self.play(Write(headline), run_time=0.5)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(accent_dot1), FadeIn(accent_dot2), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.play(Write(sub), run_time=0.4)
        self.play(Create(teal_accent), run_time=0.3)
        self.wait(max(0.1, duration - 3.7))


# ---------------------------------------------------------------------------
# B02 — Spontaneous emission: two levels, photon in, random photon out
# ---------------------------------------------------------------------------
class B02_SpontaneousEmission(Scene):
    def construct(self):
        duration = DUR.get("B02", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Ground and excited level
        gnd_line = Line(LEFT * 3.5, RIGHT * 0.5, color=INK, stroke_width=3).move_to(DOWN * 1.8 + LEFT * 1.5)
        exc_line = Line(LEFT * 3.5, RIGHT * 0.5, color=INK, stroke_width=3).move_to(UP * 1.2 + LEFT * 1.5)
        gnd_label = Text("ground", font=SERIF, font_size=22, color=INK).move_to(DOWN * 1.8 + RIGHT * 1.2)
        exc_label = Text("excited", font=SERIF, font_size=22, color=INK).move_to(UP * 1.2 + RIGHT * 1.2)

        # Atom dot on excited level
        atom = Dot(radius=0.28, color=CRIMSON).move_to(LEFT * 1.5 + UP * 1.2)
        atom_label = Text("atom", font=DISPLAY, font_size=18, color=INK).move_to(LEFT * 1.5 + UP * 1.75)

        # Photon in (left arrow)
        photon_in = Arrow(np.array([-6.5, -1.8, 0.0]), np.array([-2.1, -1.8, 0.0]),
                          color=TEAL, buff=0, stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.18)
        photon_in_label = Text("photon in", font=SERIF, font_size=20, color=TEAL).move_to(LEFT * 4.5 + DOWN * 1.3)

        # Absorption arrow (up)
        absorb_arrow = Arrow(np.array([-1.5, -1.5, 0.0]), np.array([-1.5, 0.95, 0.0]),
                             color=CRIMSON, buff=0, stroke_width=2.5,
                             max_tip_length_to_length_ratio=0.2)

        # Spontaneous emission: random arrow (down + right diagonal)
        emit_arrow = Arrow(np.array([-1.5, 0.95, 0.0]), np.array([1.5, -0.8, 0.0]),
                           color=CRIMSON, buff=0, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.18)
        emit_label = Text("random direction", font=SERIF, font_size=20, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 0.8)

        # "Spontaneous" label
        spont_box = Rectangle(width=5.5, height=0.7).set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        spont_box.move_to(DOWN * 3.0 + LEFT * 1.0)
        spont_text = Text("spontaneous emission", font=DISPLAY, font_size=22, color=CRIMSON).move_to(DOWN * 3.0 + LEFT * 1.0)

        self.play(Create(gnd_line), Create(exc_line), run_time=0.4)
        self.play(Write(gnd_label), Write(exc_label), run_time=0.3)
        self.play(GrowFromCenter(atom), run_time=0.3)
        self.play(Write(atom_label), run_time=0.3)
        self.play(GrowArrow(photon_in), run_time=0.4)
        self.play(Write(photon_in_label), run_time=0.3)
        self.play(GrowArrow(absorb_arrow), run_time=0.4)
        self.play(GrowArrow(emit_arrow), run_time=0.4)
        self.play(Write(emit_label), run_time=0.3)
        self.play(FadeIn(spont_box), run_time=0.3)
        self.play(Write(spont_text), run_time=0.4)
        self.wait(max(0.1, duration - 4.2))


# ---------------------------------------------------------------------------
# B03 — The Question card
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        accent_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        accent_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.0, RIGHT * 6.0, color=TEAL, stroke_width=2.5).move_to(UP * 1.6)
        q_box = Rectangle(width=11, height=2.0).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=1.5).move_to(DOWN * 1.2)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + UP * 2.8)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + UP * 2.8)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        question = Text("Absorption predicts random re-emission.\nA laser beam is not random. Why?",
                        font=DISPLAY, font_size=26, color=INK,
                        line_spacing=1.3).move_to(UP * 0.2)
        self.add(bg)
        self.play(FadeIn(accent_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(GrowFromCenter(q_box), run_time=0.4)
        self.play(Write(question), run_time=0.5)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.wait(max(0.1, duration - 2.6))


# ---------------------------------------------------------------------------
# B04 — Stimulated emission: photon in + excited atom → two photons same direction
# ---------------------------------------------------------------------------
class B04_StimulatedEmission(Scene):
    def construct(self):
        duration = DUR.get("B04", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Energy levels
        gnd = Line(LEFT * 3.5, RIGHT * 0.5, color=INK, stroke_width=3).move_to(DOWN * 1.5 + LEFT * 1.5)
        exc = Line(LEFT * 3.5, RIGHT * 0.5, color=INK, stroke_width=3).move_to(UP * 1.5 + LEFT * 1.5)
        gnd_lbl = Text("ground", font=SERIF, font_size=20, color=INK).move_to(DOWN * 2.2 + RIGHT * 0.5)
        exc_lbl = Text("excited", font=SERIF, font_size=20, color=INK).move_to(UP * 2.0 + RIGHT * 0.5)

        # Excited atom
        atom = Dot(radius=0.28, color=TEAL).move_to(LEFT * 1.5 + UP * 1.5)

        # Incoming photon
        photon1 = Arrow(np.array([-6.5, -1.5, 0.0]), np.array([-2.1, -1.5, 0.0]),
                        color=TEAL, buff=0, stroke_width=2.5,
                        max_tip_length_to_length_ratio=0.18)
        photon1_lbl = Text("photon 1", font=SERIF, font_size=20, color=TEAL).move_to(LEFT * 4.5 + DOWN * 1.0)

        # Stimulated: two photons emerge same direction
        photon2a = Arrow(np.array([-1.2, -1.5, 0.0]), np.array([3.0, -1.5, 0.0]),
                         color=TEAL, buff=0, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.15)
        photon2b = Arrow(np.array([-1.2, -1.0, 0.0]), np.array([3.0, -1.0, 0.0]),
                         color=TEAL, buff=0, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.15)
        photon2a_lbl = Text("photon 1 (unchanged)", font=SERIF, font_size=18, color=TEAL).move_to(RIGHT * 2.0 + DOWN * 2.0)
        photon2b_lbl = Text("photon 2 (copy)", font=SERIF, font_size=18, color=TEAL).move_to(RIGHT * 2.0 + DOWN * 0.4)

        # Atom drops to ground
        drop_arrow = Arrow(np.array([-1.5, 1.2, 0.0]), np.array([-1.5, -1.2, 0.0]),
                           color=INK, buff=0, stroke_width=2,
                           max_tip_length_to_length_ratio=0.2)

        # "Stimulated emission" banner
        stim_box = Rectangle(width=6.0, height=0.7).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        stim_box.move_to(DOWN * 3.2 + LEFT * 1.0)
        stim_text = Text("stimulated emission", font=DISPLAY, font_size=22, color=TEAL).move_to(DOWN * 3.2 + LEFT * 1.0)

        # Coherent label
        coh_line = Line(RIGHT * 3.2 + DOWN * 1.5, RIGHT * 5.8 + DOWN * 1.5, color=TEAL, stroke_width=1.5)
        coh_lbl = Text("same phase", font=SERIF, font_size=18, color=TEAL).move_to(RIGHT * 5.2 + DOWN * 1.1)

        self.play(Create(gnd), Create(exc), run_time=0.4)
        self.play(Write(gnd_lbl), Write(exc_lbl), run_time=0.3)
        self.play(GrowFromCenter(atom), run_time=0.3)
        self.play(GrowArrow(photon1), run_time=0.4)
        self.play(Write(photon1_lbl), run_time=0.3)
        self.play(GrowArrow(drop_arrow), run_time=0.4)
        self.play(GrowArrow(photon2a), run_time=0.4)
        self.play(GrowArrow(photon2b), run_time=0.4)
        self.play(Write(photon2a_lbl), Write(photon2b_lbl), run_time=0.3)
        self.play(Create(coh_line), Write(coh_lbl), run_time=0.3)
        self.play(FadeIn(stim_box), run_time=0.3)
        self.play(Write(stim_text), run_time=0.4)
        self.wait(max(0.1, duration - 5.2))


# ---------------------------------------------------------------------------
# B05 — Section card: The Mechanism
# ---------------------------------------------------------------------------
class B05_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B05", 4.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 2.5)
        rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.6)
        content_box = Rectangle(width=13, height=1.0).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.2)
        teal_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 1.8)
        section_label = Text("THE MECHANISM", font=DISPLAY, font_size=22,
                             color=TEAL).move_to(UP * 2.5)
        headline = Text("A passing photon triggers an exact copy of itself.",
                        font=DISPLAY, font_size=26, color=INK).move_to(UP * 0.2)
        left_accent = Rectangle(width=0.18, height=1.5).set_fill(TEAL, 0.4).set_stroke(width=0)
        left_accent.move_to(LEFT * 6.6 + UP * 0.2)
        self.add(bg, headline)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_accent), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.0))


# ---------------------------------------------------------------------------
# B06 — Cascade: 1 photon → 2 → 4 (coherent copies multiplying)
# ---------------------------------------------------------------------------
class B06_CascadeCoherence(Scene):
    def construct(self):
        duration = DUR.get("B06", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Stage 1: one photon
        s1_label = Text("1 photon", font=DISPLAY, font_size=22, color=TEAL).move_to(LEFT * 5.0 + UP * 2.5)
        s1_dot = Dot(radius=0.22, color=TEAL).move_to(LEFT * 5.0 + UP * 1.5)

        # Arrow 1
        arr1 = Arrow(np.array([-4.3, 1.5, 0.0]), np.array([-2.5, 1.5, 0.0]),
                     color=INK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.2)

        # Stage 2: two photons
        s2_label = Text("2 photons", font=DISPLAY, font_size=22, color=TEAL).move_to(LEFT * 1.5 + UP * 2.5)
        s2_dot1 = Dot(radius=0.22, color=TEAL).move_to(LEFT * 1.8 + UP * 1.8)
        s2_dot2 = Dot(radius=0.22, color=TEAL).move_to(LEFT * 1.2 + UP * 1.2)

        # Arrow 2
        arr2 = Arrow(np.array([-0.5, 1.5, 0.0]), np.array([1.3, 1.5, 0.0]),
                     color=INK, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.2)

        # Stage 3: four photons
        s3_label = Text("4 photons", font=DISPLAY, font_size=22, color=TEAL).move_to(RIGHT * 3.0 + UP * 2.5)
        s3_dots = VGroup(
            Dot(radius=0.22, color=TEAL).move_to(RIGHT * 2.5 + UP * 2.0),
            Dot(radius=0.22, color=TEAL).move_to(RIGHT * 3.5 + UP * 2.0),
            Dot(radius=0.22, color=TEAL).move_to(RIGHT * 2.5 + UP * 1.0),
            Dot(radius=0.22, color=TEAL).move_to(RIGHT * 3.5 + UP * 1.0),
        )

        # Bottom: coherent label
        coh_box = Rectangle(width=8, height=0.7).set_fill(TEAL, 0.1).set_stroke(TEAL, 1.5)
        coh_box.move_to(DOWN * 1.5)
        coh_text = Text("all copies: same direction, same phase", font=SERIF, font_size=22, color=TEAL).move_to(DOWN * 1.5)

        # Population inversion note
        inv_box = Rectangle(width=9, height=0.7).set_fill(SLATE, 0.1).set_stroke(SLATE, 1)
        inv_box.move_to(DOWN * 2.8)
        inv_text = Text("requires population inversion: more excited than ground", font=SERIF, font_size=20, color=INK).move_to(DOWN * 2.8)

        # Ground rule
        ground_rule = Line(LEFT * 7, RIGHT * 7, color=INK, stroke_width=1).move_to(DOWN * 3.8)

        self.play(Write(s1_label), run_time=0.3)
        self.play(GrowFromCenter(s1_dot), run_time=0.3)
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(Write(s2_label), run_time=0.3)
        self.play(GrowFromCenter(s2_dot1), GrowFromCenter(s2_dot2), run_time=0.3)
        self.play(GrowArrow(arr2), run_time=0.3)
        self.play(Write(s3_label), run_time=0.3)
        self.play(GrowFromCenter(s3_dots), run_time=0.4)
        self.play(FadeIn(coh_box), run_time=0.3)
        self.play(Write(coh_text), run_time=0.4)
        self.play(FadeIn(inv_box), run_time=0.3)
        self.play(Write(inv_text), run_time=0.4)
        self.play(Create(ground_rule), run_time=0.3)
        self.wait(max(0.1, duration - 4.8))


# ---------------------------------------------------------------------------
# B07 — Population inversion: excited > ground
# ---------------------------------------------------------------------------
class B07_PopulationInversion(Scene):
    def construct(self):
        duration = DUR.get("B07", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title rule
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.0)

        # Left column: thermal (Boltzmann — more in ground)
        left_box = Rectangle(width=6.5, height=5.5).set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.5)
        left_box.move_to(LEFT * 3.5 + UP * 0.0)
        left_title = Text("Thermal", font=DISPLAY, font_size=24, color=CRIMSON).move_to(LEFT * 3.5 + UP * 2.3)

        # Ground atoms: many dots
        gnd_dots_l = VGroup(*[Dot(radius=0.18, color=CRIMSON).move_to(LEFT * (4.5 - i*0.7) + DOWN * 0.5)
                               for i in range(5)])
        # Excited atoms: few dots
        exc_dots_l = VGroup(*[Dot(radius=0.18, color=SLATE).move_to(LEFT * (4.5 - i*1.1) + UP * 1.2)
                               for i in range(2)])
        gnd_lbl_l = Text("ground: 5", font=MONO, font_size=20, color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 1.3)
        exc_lbl_l = Text("excited: 2", font=MONO, font_size=20, color=SLATE).move_to(LEFT * 3.5 + UP * 1.9)

        # Right column: inverted (more excited)
        right_box = Rectangle(width=6.5, height=5.5).set_fill(TEAL, 0.05).set_stroke(TEAL, 1.5)
        right_box.move_to(RIGHT * 3.5 + UP * 0.0)
        right_title = Text("Inverted", font=DISPLAY, font_size=24, color=TEAL).move_to(RIGHT * 3.5 + UP * 2.3)

        # Excited atoms: many dots
        exc_dots_r = VGroup(*[Dot(radius=0.18, color=TEAL).move_to(RIGHT * (2.5 + i*0.7) + UP * 1.2)
                               for i in range(5)])
        # Ground atoms: few dots
        gnd_dots_r = VGroup(*[Dot(radius=0.18, color=SLATE).move_to(RIGHT * (3.0 + i*1.1) + DOWN * 0.5)
                               for i in range(2)])
        gnd_lbl_r = Text("ground: 2", font=MONO, font_size=20, color=SLATE).move_to(RIGHT * 3.5 + DOWN * 1.3)
        exc_lbl_r = Text("excited: 5", font=MONO, font_size=20, color=TEAL).move_to(RIGHT * 3.5 + UP * 1.9)

        # Separator rule
        sep = Line(UP * 2.8, DOWN * 3.0, color=INK, stroke_width=1.5).move_to(ORIGIN)

        # Bottom note
        bottom_box = Rectangle(width=9, height=0.7).set_fill(TEAL, 0.1).set_stroke(TEAL, 1)
        bottom_box.move_to(DOWN * 3.3)
        bottom_text = Text("pumping required — inversion is non-equilibrium", font=SERIF, font_size=18, color=TEAL).move_to(DOWN * 3.3)

        self.play(Create(title_rule), run_time=0.3)
        self.play(FadeIn(left_box), run_time=0.3)
        self.play(Write(left_title), run_time=0.3)
        self.play(GrowFromCenter(gnd_dots_l), run_time=0.4)
        self.play(GrowFromCenter(exc_dots_l), run_time=0.3)
        self.play(Write(gnd_lbl_l), Write(exc_lbl_l), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(right_box), run_time=0.3)
        self.play(Write(right_title), run_time=0.3)
        self.play(GrowFromCenter(exc_dots_r), run_time=0.4)
        self.play(GrowFromCenter(gnd_dots_r), run_time=0.3)
        self.play(Write(gnd_lbl_r), Write(exc_lbl_r), run_time=0.3)
        self.play(FadeIn(bottom_box), run_time=0.3)
        self.play(Write(bottom_text), run_time=0.4)
        self.wait(max(0.1, duration - 5.0))


# ---------------------------------------------------------------------------
# B08 — Resonant cavity turns one coherent seed into an avalanche
# ---------------------------------------------------------------------------
class B08_LaserCavity(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.5)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)
        title = Text("POPULATION INVERSION + FEEDBACK = LASER", font=DISPLAY, font_size=29, color=INK).move_to(UP * 3.35)
        left_mirror = Rectangle(width=0.22, height=4.4).set_fill(INK, 0.65).set_stroke(INK, 1).move_to(LEFT * 6.0)
        right_mirror = Rectangle(width=0.22, height=4.4).set_fill(TEAL, 0.35).set_stroke(TEAL, 1).move_to(RIGHT * 5.4)
        cavity = RoundedRectangle(width=10.8, height=3.8, corner_radius=0.18).set_fill(TEAL, 0.04).set_stroke(INK, 1.5).move_to(LEFT * 0.3)
        mirror_l = Text("mirror", font=MONO, font_size=18, color=INK).next_to(left_mirror, DOWN, buff=0.2)
        mirror_r = Text("output coupler", font=MONO, font_size=18, color=TEAL).next_to(right_mirror, DOWN, buff=0.2)
        atoms = VGroup(*[Circle(radius=0.16, color=CRIMSON, fill_opacity=0.7).move_to([x,y,0])
                         for y in (-1.0,0.0,1.0) for x in (-4.5,-2.7,-0.9,0.9,2.7,4.2)])
        inversion = Text("excited atoms", font=DISPLAY, font_size=21, color=CRIMSON).move_to(UP * 2.45)
        def photon(x, yoff=0):
            return Arrow([x-0.45,yoff,0], [x+0.45,yoff,0], color=TEAL, stroke_width=4,
                         buff=0, max_tip_length_to_length_ratio=0.25)
        seed = photon(-5.2)
        copies2 = VGroup(photon(-2.8,-0.22), photon(-2.8,0.22))
        copies4 = VGroup(*[photon(0.0,y) for y in (-0.6,-0.2,0.2,0.6)])
        copies8 = VGroup(*[photon(3.2,y) for y in np.linspace(-1.25,1.25,8)])
        beam = VGroup(*[Arrow([5.5,y,0], [7.1,y,0], color=TEAL, stroke_width=3,
                              buff=0, max_tip_length_to_length_ratio=0.16)
                        for y in np.linspace(-1.25,1.25,8)])
        counter = Text("1 → 2 → 4 → 8 coherent photons", font=MONO, font_size=25, color=TEAL).move_to(DOWN * 3.25)
        maiman = Text("ruby laser • Theodore Maiman • 1960", font=SERIF, font_size=22, color=INK).move_to(UP * 2.85)
        self.play(FadeIn(title), FadeIn(maiman), run_time=0.7)
        self.play(Create(cavity), FadeIn(left_mirror), FadeIn(right_mirror), FadeIn(mirror_l), FadeIn(mirror_r), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(a) for a in atoms], lag_ratio=0.025), FadeIn(inversion), run_time=1.2)
        self.play(GrowArrow(seed), run_time=0.7)
        self.play(ReplacementTransform(seed.copy(), copies2), run_time=1.0)
        self.play(ReplacementTransform(copies2.copy(), copies4), run_time=1.0)
        self.play(ReplacementTransform(copies4.copy(), copies8), run_time=1.0)
        self.play(LaggedStart(*[GrowArrow(p) for p in beam], lag_ratio=0.05), FadeIn(counter), run_time=1.2)
        self.play(Indicate(beam, color=TEAL), run_time=0.8)
        self.wait(max(0.1, duration - 8.4))


# ---------------------------------------------------------------------------
# B09 — Coherent vs spontaneous beam comparison
# ---------------------------------------------------------------------------
class B09_CoherentVsSpontaneous(Scene):
    def construct(self):
        duration = DUR.get("B09", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title
        title_rule = Line(LEFT * 7, RIGHT * 7, color=TEAL, stroke_width=2).move_to(UP * 3.0)

        # Left side: laser (coherent)
        left_box = Rectangle(width=6.5, height=4.5).set_fill(TEAL, 0.06).set_stroke(TEAL, 1.5)
        left_box.move_to(LEFT * 3.5 + UP * 0.3)
        left_title = Text("laser (stimulated)", font=DISPLAY, font_size=22, color=TEAL).move_to(LEFT * 3.5 + UP * 2.2)

        # Parallel arrows (coherent)
        for i, dy in enumerate([-0.3, 0.0, 0.3]):
            arr = Arrow(np.array([-6.0, dy + 0.3, 0.0]), np.array([-1.5, dy + 0.3, 0.0]),
                        color=TEAL, buff=0, stroke_width=2.5,
                        max_tip_length_to_length_ratio=0.12)
            if i == 0:
                self.play(GrowArrow(arr), run_time=0.3)
            else:
                self.play(GrowArrow(arr), run_time=0.25)

        left_note = Text("all in lockstep", font=SERIF, font_size=20, color=TEAL).move_to(LEFT * 3.5 + DOWN * 1.3)

        # Vertical separator
        sep = Line(UP * 2.8, DOWN * 2.5, color=INK, stroke_width=1.5).move_to(ORIGIN)

        # Right side: lamp (spontaneous)
        right_box = Rectangle(width=6.5, height=4.5).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        right_box.move_to(RIGHT * 3.5 + UP * 0.3)
        right_title = Text("lamp (spontaneous)", font=DISPLAY, font_size=22, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 2.2)

        # Random arrows from center
        random_dirs = [
            (np.array([0.3, 0.3, 0.0]), np.array([2.5, 2.0, 0.0])),
            (np.array([0.3, 0.3, 0.0]), np.array([2.8, 0.3, 0.0])),
            (np.array([0.3, 0.3, 0.0]), np.array([2.5, -1.3, 0.0])),
            (np.array([0.3, 0.3, 0.0]), np.array([5.8, 1.5, 0.0])),
        ]
        for start, end in random_dirs:
            arr = Arrow(start, end, color=CRIMSON, buff=0, stroke_width=2,
                        max_tip_length_to_length_ratio=0.15)
            self.play(GrowArrow(arr), run_time=0.2)

        right_note = Text("scatter in all directions", font=SERIF, font_size=20, color=CRIMSON).move_to(RIGHT * 3.5 + DOWN * 1.3)

        self.play(Create(title_rule), run_time=0.3)
        self.play(FadeIn(left_box), run_time=0.3)
        self.play(Write(left_title), run_time=0.3)
        self.play(Write(left_note), run_time=0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(right_box), run_time=0.3)
        self.play(Write(right_title), run_time=0.3)
        self.play(Write(right_note), run_time=0.3)
        self.wait(max(0.1, duration - 4.5))


# ---------------------------------------------------------------------------
# B10 — Implication card
# ---------------------------------------------------------------------------
class B10_ImplicationCard(Scene):
    def construct(self):
        duration = DUR.get("B10", 3.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        accent_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.12).set_stroke(width=0)
        accent_bar.move_to(UP * 2.5)
        rule_top = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.4)
        q_box = Rectangle(width=10, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        q_box.move_to(UP * 0.2)
        rule_bot = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.8)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.5)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.5)
        teal_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        text = Text("Stimulated copies add.  Spontaneous emissions scatter.",
                    font=DISPLAY, font_size=26, color=INK).move_to(UP * 0.2)
        self.add(bg)
        self.play(FadeIn(accent_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(GrowFromCenter(q_box), run_time=0.4)
        self.play(Write(text), run_time=0.4)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(Create(teal_rule), run_time=0.3)
        self.wait(max(0.1, duration - 2.9))


# ---------------------------------------------------------------------------
# B11 — Example card
# ---------------------------------------------------------------------------
class B11_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B11", 4.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.15).set_stroke(width=0)
        top_bar.move_to(UP * 2.5)
        rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=2.5).move_to(UP * 1.5)
        content_box = Rectangle(width=11, height=1.2).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        content_box.move_to(UP * 0.3)
        rule2 = Line(LEFT * 6, RIGHT * 6, color=INK, stroke_width=1.5).move_to(DOWN * 0.7)
        dot_l = Dot(radius=0.1, color=TEAL).move_to(LEFT * 5.8 + DOWN * 1.2)
        dot_r = Dot(radius=0.1, color=TEAL).move_to(RIGHT * 5.8 + DOWN * 1.2)
        accent_rule = Line(LEFT * 4, RIGHT * 4, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.0)
        left_bar = Rectangle(width=0.15, height=1.2).set_fill(TEAL, 0.5).set_stroke(width=0)
        left_bar.move_to(LEFT * 6.6 + UP * 0.3)
        section_label = Text("WORKED EXAMPLE", font=DISPLAY, font_size=22,
                             color=TEAL).move_to(UP * 2.5)
        headline = Text("One seed photon, three atoms, one chain",
                        font=DISPLAY, font_size=30, color=INK).move_to(UP * 0.3)
        self.add(bg, headline)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(section_label), run_time=0.3)
        self.play(GrowFromCenter(content_box), run_time=0.4)
        self.play(FadeIn(left_bar), run_time=0.3)
        self.play(Create(rule2), run_time=0.3)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.play(Create(accent_rule), run_time=0.3)
        self.wait(max(0.1, duration - 3.5))


# ---------------------------------------------------------------------------
# B12 — Worked example: 1 → 2 → 4 photon chain (illustrative)
# ---------------------------------------------------------------------------
class B12_WorkedExample(Scene):
    def construct(self):
        duration = DUR.get("B12", 22.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        # Title bar
        title_bar = Rectangle(width=14, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
        title_bar.move_to(UP * 3.7)
        title_text = Text("illustrative — one seed photon, three excited atoms",
                          font=SERIF, font_size=18, color=INK).move_to(UP * 3.7)

        # Step row 1
        step1_box = Rectangle(width=13, height=0.85).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        step1_box.move_to(UP * 2.5)
        step1 = Text("seed: 1 photon  +  atom 1 (excited)  =  2 photons (same direction)",
                     font=MONO, font_size=20, color=TEAL).move_to(UP * 2.5)

        # Arrow 1
        arr1 = Arrow(np.array([0.0, 1.95, 0.0]), np.array([0.0, 1.55, 0.0]),
                     color=TEAL, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.25)

        # Step row 2
        step2_box = Rectangle(width=13, height=0.85).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        step2_box.move_to(UP * 1.1)
        step2 = Text("2 photons  +  atoms 2 and 3  =  4 photons (same direction)",
                     font=MONO, font_size=20, color=TEAL).move_to(UP * 1.1)

        # Arrow 2
        arr2 = Arrow(np.array([0.0, 0.55, 0.0]), np.array([0.0, 0.1, 0.0]),
                     color=TEAL, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.25)

        # Result
        result_box = Rectangle(width=11, height=0.85).set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        result_box.move_to(DOWN * 0.35)
        result = Text("4 coherent photons out from 1 seed photon in",
                      font=MONO, font_size=22, color=TEAL).move_to(DOWN * 0.35)

        # Key point
        key_box = Rectangle(width=11, height=0.85).set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        key_box.move_to(DOWN * 1.6)
        key_text = Text("double the excited atoms  =  double the output per pass",
                        font=MONO, font_size=20, color=INK).move_to(DOWN * 1.6)

        # Gain label
        gain_box = Rectangle(width=4, height=0.7).set_fill(TEAL, 0.12).set_stroke(TEAL, 1)
        gain_box.move_to(DOWN * 2.8)
        gain_text = Text("this is gain", font=DISPLAY, font_size=24, color=TEAL).move_to(DOWN * 2.8)

        # Bottom rule
        bottom_rule = Line(LEFT * 6, RIGHT * 6, color=TEAL, stroke_width=1.5).move_to(DOWN * 3.7)

        self.play(FadeIn(title_bar), run_time=0.3)
        self.play(Write(title_text), run_time=0.4)
        self.play(FadeIn(step1_box), run_time=0.3)
        self.play(Write(step1), run_time=0.4)
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(FadeIn(step2_box), run_time=0.3)
        self.play(Write(step2), run_time=0.4)
        self.play(GrowArrow(arr2), run_time=0.3)
        self.play(FadeIn(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.4)
        self.play(FadeIn(key_box), run_time=0.3)
        self.play(Write(key_text), run_time=0.4)
        self.play(FadeIn(gain_box), run_time=0.3)
        self.play(Write(gain_text), run_time=0.3)
        self.play(Create(bottom_rule), run_time=0.3)
        self.wait(max(0.1, duration - 5.5))


# ---------------------------------------------------------------------------
# B13 — Recap card
# ---------------------------------------------------------------------------
class B13_Recap(Scene):
    def construct(self):
        duration = DUR.get("B13", 14.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        top_bar = Rectangle(width=14, height=0.45).set_fill(TEAL, 0.18).set_stroke(width=0)
        top_bar.move_to(UP * 2.8)
        rule_top = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=2.5).move_to(UP * 1.8)
        answer_box = Rectangle(width=13, height=2.5).set_fill(SLATE, 0.08).set_stroke(TEAL, 1.5)
        answer_box.move_to(UP * 0.5)
        rule_bot = Line(LEFT * 6.2, RIGHT * 6.2, color=INK, stroke_width=1.5).move_to(DOWN * 1.2)
        kicker_box = Rectangle(width=6.5, height=0.6).set_fill(TEAL, 0.12).set_stroke(TEAL, 1)
        kicker_box.move_to(DOWN * 2.0)
        bottom_rule = Line(LEFT * 5, RIGHT * 5, color=TEAL, stroke_width=1.0).move_to(DOWN * 2.8)
        left_accent = Dot(radius=0.12, color=TEAL).move_to(LEFT * 6.0 + UP * 2.8)
        right_accent = Dot(radius=0.12, color=TEAL).move_to(RIGHT * 6.0 + UP * 2.8)
        eyebrow = Text("THE ANSWER", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        answer = Text("A passing photon triggers a coherent copy.\nThat copy-on-demand, with inversion,\nis why a laser exists.",
                      font=DISPLAY, font_size=22, color=INK,
                      line_spacing=1.25).move_to(UP * 0.5)
        kicker = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                      color=TEAL).move_to(DOWN * 2.0)
        self.add(bg)
        self.play(FadeIn(top_bar), run_time=0.3)
        self.play(Create(rule_top), run_time=0.3)
        self.play(FadeIn(eyebrow), run_time=0.3)
        self.play(GrowFromCenter(answer_box), run_time=0.4)
        self.play(Write(answer), run_time=0.5)
        self.play(Create(rule_bot), run_time=0.3)
        self.play(FadeIn(kicker_box), run_time=0.3)
        self.play(Write(kicker), run_time=0.4)
        self.play(Create(bottom_rule), run_time=0.3)
        self.play(FadeIn(left_accent), FadeIn(right_accent), run_time=0.3)
        self.wait(max(0.1, duration - 3.8))
