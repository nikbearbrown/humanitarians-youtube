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


class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Why Every Qubit Lives on a Globe",
                     font=DISPLAY, color=INK, font_size=34, line_spacing=1.3).move_to([0, 0.5, 0])
        sub = Text("the Bloch sphere",
                   font=SERIF, color=INK, font_size=20, slant=ITALIC).move_to([0, -0.6, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_ParameterCount(Scene):
    """Parameter counting: 4 real → -normalization → -global phase = 2 = sphere."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        # Step boxes
        box4 = Rectangle(width=2.5, height=1.0, fill_color=INK, fill_opacity=0.08,
                         stroke_color=INK, stroke_width=2.0).move_to([-4.5, 1.5, 0])
        lbl4 = Text("4 real\nparameters", font=SERIF, color=INK, font_size=18,
                    line_spacing=1.1).move_to([-4.5, 1.5, 0])

        ar1 = Arrow(start=[-3.2, 1.5, 0], end=[-2.0, 1.5, 0],
                    color=INK, stroke_width=2.0, buff=0.05)
        minus1_lbl = SerifLabel("-1 (norm)", accent=INK, size=16).move_to([-2.6, 2.2, 0])

        box3 = Rectangle(width=2.5, height=1.0, fill_color=INK, fill_opacity=0.08,
                         stroke_color=INK, stroke_width=2.0).move_to([-0.5, 1.5, 0])
        lbl3 = Text("3 real\nparameters", font=SERIF, color=INK, font_size=18,
                    line_spacing=1.1).move_to([-0.5, 1.5, 0])

        ar2 = Arrow(start=[0.8, 1.5, 0], end=[2.0, 1.5, 0],
                    color=INK, stroke_width=2.0, buff=0.05)
        minus2_lbl = SerifLabel("-1 (global phase)", accent=CRIMSON, size=16).move_to([1.4, 2.2, 0])

        box2 = Rectangle(width=2.5, height=1.0, fill_color=TEAL, fill_opacity=0.12,
                         stroke_color=TEAL, stroke_width=2.5).move_to([3.5, 1.5, 0])
        lbl2 = Text("2 real\nparameters", font=SERIF, color=TEAL, font_size=18,
                    line_spacing=1.1).move_to([3.5, 1.5, 0])

        # Result
        result = SerifLabel("2 angles = one point on a sphere", accent=TEAL, size=22).move_to([0, -0.5, 0])
        theta_lbl = SerifLabel("theta = polar angle", accent=TEAL, size=18).move_to([-2.0, -1.5, 0])
        phi_lbl = SerifLabel("phi = azimuthal angle", accent=TEAL, size=18).move_to([2.0, -1.5, 0])

        # Small sphere sketch
        sphere_sm = Ellipse(width=3.0, height=3.0, color=TEAL, stroke_width=2.0).move_to([0, -3.0, 0])

        self.play(FadeIn(box4), FadeIn(lbl4), run_time=0.3)
        self.play(GrowArrow(ar1), FadeIn(minus1_lbl), run_time=0.3)
        self.play(FadeIn(box3), FadeIn(lbl3), run_time=0.3)
        self.play(GrowArrow(ar2), FadeIn(minus2_lbl), run_time=0.3)
        self.play(FadeIn(box2), FadeIn(lbl2), run_time=0.3)
        self.play(FadeIn(result), run_time=0.3)
        self.play(FadeIn(theta_lbl), FadeIn(phi_lbl), run_time=0.3)
        self.play(Create(sphere_sm), run_time=0.4)
        self.wait(dur - 2.7)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        title = Text("A qubit has 4 real parameters.\nNormalization removes 1. Global phase removes 1.\n2 remain. Why a sphere?",
                     font=DISPLAY, color=INK, font_size=18, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_BlochSphere(Scene):
    """Bloch sphere with theta/phi angles and formula."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Sphere outline
        sphere = Ellipse(width=4.5, height=4.5, color=TEAL, stroke_width=2.0).move_to([0, 0, 0])
        equator = Ellipse(width=4.5, height=1.5, color=TEAL, stroke_width=1.2,
                          stroke_opacity=0.5).move_to([0, 0, 0])
        z_axis = Arrow(start=[0, -2.8, 0], end=[0, 2.8, 0],
                       color=INK, stroke_width=1.5, buff=0)
        z_lbl = SerifLabel("z", accent=INK, size=18).move_to([-0.4, 3.0, 0])

        # State arrow
        state = Arrow(start=[0, 0, 0], end=[1.8, 1.5, 0],
                      color=TEAL, stroke_width=2.5, buff=0.05)
        state_lbl = SerifLabel("|psi>", accent=TEAL, size=18).move_to([2.5, 1.8, 0])

        # Theta arc (polar)
        theta_arc = Arc(radius=0.8, start_angle=np.pi / 2, angle=-np.pi / 4,
                        color=TEAL, stroke_width=2.0)
        theta_lbl = SerifLabel("theta", accent=TEAL, size=16).move_to([0.7, 0.8, 0])

        # Formula
        formula = Text("|psi> = cos(theta/2)|0> + e^i*phi sin(theta/2)|1>",
                       font=MONO, color=TEAL, font_size=18).move_to([0, -3.5, 0])

        self.play(Create(sphere), run_time=0.3)
        self.play(Create(equator), run_time=0.3)
        self.play(GrowArrow(z_axis), run_time=0.3)
        self.play(FadeIn(z_lbl), run_time=0.2)
        self.play(GrowArrow(state), run_time=0.3)
        self.play(FadeIn(state_lbl), run_time=0.2)
        self.play(Create(theta_arc), run_time=0.3)
        self.play(FadeIn(theta_lbl), run_time=0.2)
        self.play(FadeIn(formula), run_time=0.4)
        self.wait(dur - 2.7)


class B05_PolesEquator(Scene):
    """Sphere with north pole |0⟩, south pole |1⟩, equator labeled."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        sphere = Ellipse(width=4.5, height=4.5, color=INK, stroke_width=1.5).move_to([0, 0, 0])
        equator = Ellipse(width=4.5, height=1.5, color=TEAL, stroke_width=2.0).move_to([0, 0, 0])

        # Poles
        north_dot = Dot([0, 2.25, 0], color=TEAL, radius=0.14)
        north_lbl = SerifLabel("|0>  (theta=0)", accent=TEAL, size=20).move_to([2.5, 2.5, 0])
        south_dot = Dot([0, -2.25, 0], color=TEAL, radius=0.14)
        south_lbl = SerifLabel("|1>  (theta=pi)", accent=TEAL, size=20).move_to([2.5, -2.5, 0])

        # Equator label
        eq_lbl = SerifLabel("equator: equal superpositions", accent=TEAL, size=18).move_to([0, 0.6, 0])
        eq_sub = SerifLabel("(theta = pi/2, any phi)", accent=TEAL, size=16).move_to([0, 0.0, 0])

        # Arrows to poles
        arr_n = Arrow(start=[1.5, 2.4, 0], end=[0.2, 2.25, 0],
                      color=TEAL, stroke_width=1.5, buff=0.05)
        arr_s = Arrow(start=[1.5, -2.4, 0], end=[0.2, -2.25, 0],
                      color=TEAL, stroke_width=1.5, buff=0.05)

        self.play(Create(sphere), run_time=0.4)
        self.play(Create(equator), run_time=0.3)
        self.play(FadeIn(north_dot), GrowArrow(arr_n), FadeIn(north_lbl), run_time=0.4)
        self.play(FadeIn(south_dot), GrowArrow(arr_s), FadeIn(south_lbl), run_time=0.4)
        self.play(FadeIn(eq_lbl), FadeIn(eq_sub), run_time=0.3)
        self.wait(dur - 2.0)


class B06_RelativePhase(Scene):
    """Two state arrows at same theta, different phi — different sigma_x outcomes."""
    def construct(self):
        dur = DUR.get("B06", 10.0)
        sphere = Ellipse(width=4.0, height=4.0, color=INK, stroke_width=1.5).move_to([-1.0, 0, 0])
        equator_ring = Ellipse(width=4.0, height=1.3, color=INK, stroke_width=1.0,
                               stroke_opacity=0.5).move_to([-1.0, 0, 0])

        # Two arrows at equator (same theta = pi/2), different phi
        arrow_phi0 = Arrow(start=[-1.0, 0, 0], end=[1.0, 0, 0],
                           color=TEAL, stroke_width=2.5, buff=0.05)
        arrow_phi90 = Arrow(start=[-1.0, 0, 0], end=[-3.0, 0, 0],
                            color=CRIMSON, stroke_width=2.5, buff=0.05)

        phi0_lbl = SerifLabel("phi=0: sigma_x = +1", accent=TEAL, size=18).move_to([3.5, 0.8, 0])
        phi90_lbl = SerifLabel("phi=pi: sigma_x = -1", accent=CRIMSON, size=18).move_to([3.5, -0.8, 0])
        same_theta = SerifLabel("same theta, different phi -> different outcomes", accent=INK, size=18).move_to([0, -3.0, 0])

        self.play(Create(sphere), run_time=0.3)
        self.play(Create(equator_ring), run_time=0.3)
        self.play(GrowArrow(arrow_phi0), run_time=0.3)
        self.play(FadeIn(phi0_lbl), run_time=0.2)
        self.play(GrowArrow(arrow_phi90), run_time=0.3)
        self.play(FadeIn(phi90_lbl), run_time=0.2)
        self.play(FadeIn(same_theta), run_time=0.4)
        self.wait(dur - 2.2)


class B07_GlobalPhase(Scene):
    """States differing by global e^iγ map to same Bloch point."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Left: two states with global phase difference
        left_title = SerifLabel("two states differ by global phase:", accent=INK, size=18).move_to([0, 3.0, 0])

        state1 = Text("|psi>  =  cos(θ/2)|0> + e^iφ sin(θ/2)|1>",
                      font=MONO, color=TEAL, font_size=18).move_to([0, 1.8, 0])
        vs_lbl = SerifLabel("vs.", accent=INK, size=18).move_to([0, 0.8, 0])
        state2 = Text("e^iγ|psi>  =  e^iγ cos(θ/2)|0> + e^i(γ+φ) sin(θ/2)|1>",
                      font=MONO, color=CRIMSON, font_size=16).move_to([0, -0.2, 0])
        cross = VGroup(
            Line([-1.5, -0.9, 0], [1.5, 0.5, 0], color=CRIMSON, stroke_width=3.0),
            Line([-1.5, 0.5, 0], [1.5, -0.9, 0], color=CRIMSON, stroke_width=3.0),
        ).move_to([0, -0.2, 0])
        note = SerifLabel("e^iγ cancels in every |<obs>|^2", accent=CRIMSON, size=18).move_to([0, -1.5, 0])

        # Both map to same Bloch point
        divider = Line([-5.5, -2.0, 0], [5.5, -2.0, 0], color=INK, stroke_width=1.2)
        same_lbl = SerifLabel("both map to the same Bloch sphere point", accent=TEAL, size=20).move_to([0, -2.8, 0])
        sphere_sm = Ellipse(width=1.8, height=1.8, color=TEAL, stroke_width=1.5).move_to([-4.0, -3.2, 0])
        dot1 = Dot([-3.5, -2.8, 0], color=TEAL, radius=0.12)
        dot1_lbl = SerifLabel("one point", accent=TEAL, size=14).move_to([-2.5, -3.2, 0])

        self.play(FadeIn(left_title), run_time=0.3)
        self.play(FadeIn(state1), run_time=0.3)
        self.play(FadeIn(vs_lbl), run_time=0.2)
        self.play(FadeIn(state2), run_time=0.3)
        self.play(Create(cross), run_time=0.3)
        self.play(FadeIn(note), run_time=0.3)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(same_lbl), run_time=0.3)
        self.play(Create(sphere_sm), FadeIn(dot1), FadeIn(dot1_lbl), run_time=0.4)
        self.wait(dur - 2.8)


class B08_BlochVector(Scene):
    """Bloch vector r = (sigma_x, sigma_y, sigma_z); |r|=1 for pure states."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        formula_title = SerifLabel("Bloch vector:", accent=TEAL, size=22).move_to([0, 2.5, 0])
        formula = Text("r = ( <sigma_x>, <sigma_y>, <sigma_z> )",
                       font=MONO, color=TEAL, font_size=22).move_to([0, 1.6, 0])
        formula_box = SurroundingRectangle(formula, color=TEAL, buff=0.2, stroke_width=2.0)

        check_lbl = SerifLabel("purity check:", accent=INK, size=20).move_to([0, 0.2, 0])
        check_formula = Text("|r|^2 = <sx>^2 + <sy>^2 + <sz>^2 = 1",
                             font=MONO, color=TEAL, font_size=20).move_to([0, -0.5, 0])

        note1 = SerifLabel("if |r|^2 < 1 : error in your calculation", accent=CRIMSON, size=18).move_to([0, -1.5, 0])
        note2 = SerifLabel("if |r|^2 = 1 : pure state confirmed", accent=TEAL, size=18).move_to([0, -2.2, 0])

        # Unit sphere
        sphere_sm = Ellipse(width=2.5, height=2.5, color=TEAL, stroke_width=1.5).move_to([4.0, 0, 0])
        r_arrow = Arrow(start=[4.0, 0, 0], end=[5.1, 0.9, 0],
                        color=TEAL, stroke_width=2.5, buff=0.05)
        r_lbl = SerifLabel("|r|=1", accent=TEAL, size=16).move_to([5.5, 1.3, 0])

        self.play(FadeIn(formula_title), run_time=0.3)
        self.play(FadeIn(formula), run_time=0.3)
        self.play(Create(formula_box), run_time=0.3)
        self.play(FadeIn(check_lbl), run_time=0.2)
        self.play(FadeIn(check_formula), run_time=0.3)
        self.play(FadeIn(note1), run_time=0.3)
        self.play(FadeIn(note2), run_time=0.3)
        self.play(Create(sphere_sm), GrowArrow(r_arrow), FadeIn(r_lbl), run_time=0.4)
        self.wait(dur - 2.6)


class B09_PhysicalQubits(Scene):
    """Three physical qubit systems each with their own Bloch sphere."""
    def construct(self):
        dur = DUR.get("B09", 9.0)
        title = SerifLabel("physical qubits — same math, different physics", accent=INK, size=20).move_to([0, 3.3, 0])

        systems = [
            ("electron spin\n|up> / |down>", -4.5),
            ("photon polarization\n|H> / |V>", 0),
            ("superconducting\ncircuit |0> / |1>", 4.5),
        ]

        spheres = VGroup()
        rings = VGroup()
        arrows = VGroup()
        dots_all = VGroup()
        lbls_all = VGroup()
        for name, x in systems:
            box = Ellipse(width=2.2, height=2.2, color=TEAL, stroke_width=1.8).move_to([x, 0.5, 0])
            eq_ring = Ellipse(width=2.2, height=0.7, color=TEAL, stroke_width=1.0,
                              stroke_opacity=0.6).move_to([x, 0.5, 0])
            state_arr = Arrow(start=[x, 0.5, 0], end=[x + 0.8, 1.2, 0],
                              color=TEAL, stroke_width=2.0, buff=0.05)
            n_dot = Dot([x, 1.6, 0], color=TEAL, radius=0.1)
            s_dot = Dot([x, -0.6, 0], color=TEAL, radius=0.1)
            lbl = Text(name, font=SERIF, color=INK, font_size=14, line_spacing=1.1).move_to([x, -1.8, 0])
            spheres.add(box)
            rings.add(eq_ring)
            arrows.add(state_arr)
            dots_all.add(n_dot, s_dot)
            lbls_all.add(lbl)

        self.play(FadeIn(title), run_time=0.3)
        self.play(Create(spheres), run_time=0.4)
        self.play(Create(rings), run_time=0.3)
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.4)
        self.play(FadeIn(dots_all), run_time=0.3)
        self.play(FadeIn(lbls_all), run_time=0.4)
        self.wait(dur - 2.2)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("4 params minus norm minus global phase = 2.\nTheta and phi place you on a sphere.\nPoles: |0> and |1>.\nEquator: equal superpositions.",
                      font=DISPLAY, color=INK, font_size=17, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
