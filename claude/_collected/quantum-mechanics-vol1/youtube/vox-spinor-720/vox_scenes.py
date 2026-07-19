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
        title = Text("Why an Electron Needs\nTwo Full Turns to Come Back",
                     font=DISPLAY, color=INK, font_size=32, line_spacing=1.3).move_to([0, 0.5, 0])
        sub = Text("spinors and the 720° identity",
                   font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([0, -0.8, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_ClassicalRotation(Scene):
    """Classical CRIMSON arrow rotating 360°, returns to same position."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        # Circle for rotation path
        circle = Circle(radius=2.2, color=INK, stroke_width=1.5)
        # Arrow pointing right initially
        arrow = Arrow(start=ORIGIN, end=[2.2, 0, 0],
                      color=CRIMSON, stroke_width=3.0, buff=0)
        period_lbl = LabelChip("period: 360°", accent=CRIMSON, size=20).move_to([0, -3.2, 0])
        title_lbl = SerifLabel("classical vector", accent=CRIMSON, size=22).move_to([0, 3.2, 0])
        start_lbl = SerifLabel("start", accent=INK, size=18).move_to([3.2, 0.4, 0])
        same_lbl = SerifLabel("same!", accent=CRIMSON, size=20).move_to([3.2, -0.4, 0])

        self.play(Create(circle), run_time=0.3)
        self.play(FadeIn(title_lbl), run_time=0.3)
        self.play(Create(arrow), run_time=0.3)
        self.play(FadeIn(start_lbl), run_time=0.2)
        # Rotate in quarters so each quarter is a distinct state
        self.play(Rotate(arrow, angle=np.pi / 2, about_point=ORIGIN,
                         rate_func=linear), run_time=dur * 0.13)
        self.play(Rotate(arrow, angle=np.pi / 2, about_point=ORIGIN,
                         rate_func=linear), run_time=dur * 0.13)
        self.play(Rotate(arrow, angle=np.pi / 2, about_point=ORIGIN,
                         rate_func=linear), run_time=dur * 0.13)
        self.play(Rotate(arrow, angle=np.pi / 2, about_point=ORIGIN,
                         rate_func=linear), run_time=dur * 0.13)
        self.play(GrowFromCenter(period_lbl), run_time=0.4)
        self.play(FadeIn(same_lbl), run_time=0.3)
        self.wait(dur * 0.05)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 10.0)
        title = Text("Rotate an electron 360 degrees.\nThe state picks up a minus sign.\nHow can a full turn not return you to the start?",
                     font=DISPLAY, color=INK, font_size=16, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_BlochSphereHalf(Scene):
    """Bloch sphere sketch showing theta/2 parameterization."""
    def construct(self):
        dur = DUR.get("B04", 10.0)
        # Simplified sphere outline (ellipse)
        sphere_outline = Ellipse(width=4.0, height=4.0, color=INK, stroke_width=1.5)
        # Equator ellipse
        equator = Ellipse(width=4.0, height=1.2, color=INK, stroke_width=1.0, stroke_opacity=0.5)
        equator.move_to([0, 0, 0])

        # North pole
        north_dot = Dot([0, 2.0, 0], color=TEAL, radius=0.1)
        north_lbl = SerifLabel("|0>  (theta=0)", accent=TEAL, size=18).move_to([2.0, 2.3, 0])

        # South pole
        south_dot = Dot([0, -2.0, 0], color=TEAL, radius=0.1)
        south_lbl = SerifLabel("|1>  (theta=pi)", accent=TEAL, size=18).move_to([2.0, -2.3, 0])

        # State arrow
        state_arrow = Arrow(start=ORIGIN, end=[1.5, 1.5, 0],
                            color=TEAL, stroke_width=2.5, buff=0.05)
        theta_lbl = SerifLabel("state uses theta/2 not theta", accent=TEAL, size=18).move_to([0, -3.2, 0])

        # Axis
        z_axis = Arrow(start=[0, -2.5, 0], end=[0, 2.5, 0],
                       color=INK, stroke_width=1.5, buff=0)
        z_lbl = SerifLabel("z", accent=INK, size=18).move_to([-0.4, 2.5, 0])

        self.play(Create(sphere_outline), Create(equator), run_time=0.4)
        self.play(GrowArrow(z_axis), FadeIn(z_lbl), run_time=0.3)
        self.play(FadeIn(north_dot), FadeIn(north_lbl), run_time=0.3)
        self.play(FadeIn(south_dot), FadeIn(south_lbl), run_time=0.3)
        self.play(GrowArrow(state_arrow), run_time=0.4)
        self.play(FadeIn(theta_lbl), run_time=0.3)
        self.wait(dur - 2.2)


class B05_MinusSign360(Scene):
    """After 360°: Bloch arrow returned but state sign flipped to -1."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Sphere outline
        sphere = Ellipse(width=3.5, height=3.5, color=INK, stroke_width=1.5).move_to([-2.5, 0, 0])
        equator = Ellipse(width=3.5, height=1.0, color=INK, stroke_width=0.8,
                          stroke_opacity=0.5).move_to([-2.5, 0, 0])

        # Bloch arrow at north pole
        bloch_arrow = Arrow(start=[-2.5, 0, 0], end=[-2.5, 1.75, 0],
                            color=TEAL, stroke_width=2.5, buff=0.05)
        pos_lbl = SerifLabel("Bloch arrow: back at start", accent=TEAL, size=18).move_to([-2.5, -2.5, 0])

        # Divider
        div = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Sign panel
        sign_title = SerifLabel("state after 360° turn:", accent=INK, size=20).move_to([3.0, 2.0, 0])
        minus_chip = LabelChip("-1 x |original>", accent=CRIMSON, size=24).move_to([3.0, 0.5, 0])
        note = SerifLabel("probability |(-1)psi|^2 = same", accent=INK, size=18).move_to([3.0, -0.5, 0])
        hidden = SerifLabel("sign hidden in amplitude", accent=CRIMSON, size=18).move_to([3.0, -1.3, 0])

        self.play(Create(sphere), Create(equator), run_time=0.4)
        self.play(GrowArrow(bloch_arrow), run_time=0.3)
        self.play(Rotate(bloch_arrow, angle=2 * np.pi, about_point=np.array([-2.5, 0, 0]),
                         rate_func=linear), run_time=dur * 0.35)
        self.play(FadeIn(pos_lbl), run_time=0.3)
        self.play(Create(div), run_time=0.2)
        self.play(FadeIn(sign_title), run_time=0.3)
        self.play(GrowFromCenter(minus_chip), run_time=0.4)
        self.play(FadeIn(note), FadeIn(hidden), run_time=0.3)
        self.wait(dur * 0.08)


class B06_Return720(Scene):
    """Second 360°: sign becomes (-1)^2 = +1, state fully restored."""
    def construct(self):
        dur = DUR.get("B06", 10.0)
        # Sign evolution diagram — build step by step
        step1_lbl = SerifLabel("after 360°: state = -|original>", accent=CRIMSON, size=20).move_to([0, 2.5, 0])
        arrow1 = Arrow(start=[0, 2.0, 0], end=[0, 1.2, 0], color=INK, stroke_width=2.0, buff=0.05)

        step2_lbl = SerifLabel("second 360°: multiply by -1 again", accent=CRIMSON, size=20).move_to([0, 0.8, 0])
        arrow2 = Arrow(start=[0, 0.3, 0], end=[0, -0.5, 0], color=INK, stroke_width=2.0, buff=0.05)

        result = Text("(-1) x (-1) = +1",
                      font=MONO, color=TEAL, font_size=30).move_to([0, -1.0, 0])
        result_box = SurroundingRectangle(result, color=TEAL, buff=0.2, stroke_width=2.0)
        period_chip = LabelChip("spinor period: 720°", accent=TEAL, size=22).move_to([0, -2.5, 0])
        confirm_line = Line([-4.0, -3.0, 0], [4.0, -3.0, 0], color=TEAL, stroke_width=2.5)

        self.play(FadeIn(step1_lbl), run_time=0.3)
        self.play(GrowArrow(arrow1), run_time=0.3)
        self.play(FadeIn(step2_lbl), run_time=0.3)
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(FadeIn(result, shift=UP * 0.2), run_time=0.4)
        self.play(Create(result_box), run_time=0.3)
        self.play(result_box.animate.set_stroke(color=TEAL, width=3.5), run_time=0.3)
        self.play(GrowFromCenter(period_chip), run_time=0.4)
        self.play(Create(confirm_line), run_time=0.3)
        self.wait(dur - 3.2)


class B07_Interference(Scene):
    """Split beam: one path rotated 360°, destructive interference at recombiner."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        # Beam paths
        source = Dot([-5.5, 0, 0], color=TEAL, radius=0.12)
        src_lbl = SerifLabel("source", accent=INK, size=16).move_to([-5.5, -0.5, 0])

        # Beam splitter
        bs = Square(side_length=0.4, color=INK, fill_color=INK,
                    fill_opacity=0.6).move_to([-3.0, 0, 0])
        bs_lbl = SerifLabel("split", accent=INK, size=14).move_to([-3.0, -0.6, 0])

        # Upper path (no rotation — TEAL)
        up_line = Line([-3.0, 0.2, 0], [1.5, 0.2, 0], color=TEAL, stroke_width=2.5)
        up_lbl = SerifLabel("+psi (no rotation)", accent=TEAL, size=16).move_to([-0.75, 0.7, 0])

        # Lower path (360° rotation — CRIMSON)
        dn_line = Line([-3.0, -0.2, 0], [1.5, -0.2, 0], color=CRIMSON, stroke_width=2.5)
        rot_box = Rectangle(width=1.0, height=0.6, fill_color=CRIMSON, fill_opacity=0.3,
                            stroke_color=CRIMSON, stroke_width=1.5).move_to([-0.75, -0.2, 0])
        dn_lbl = SerifLabel("360° spin rotation", accent=CRIMSON, size=16).move_to([-0.75, -0.9, 0])

        # Recombiner
        rc = Square(side_length=0.4, color=INK, fill_color=INK,
                    fill_opacity=0.6).move_to([1.5, 0, 0])
        cancel = Text("+psi + (-psi) = 0",
                      font=MONO, color=CRIMSON, font_size=22).move_to([3.8, 0, 0])
        cancel_lbl = SerifLabel("destructive interference!", accent=CRIMSON, size=18).move_to([3.8, -0.8, 0])

        self.play(FadeIn(source), FadeIn(src_lbl), run_time=0.3)
        self.play(FadeIn(bs), FadeIn(bs_lbl), run_time=0.3)
        self.play(Create(up_line), FadeIn(up_lbl), run_time=0.4)
        self.play(Create(dn_line), FadeIn(rot_box), FadeIn(dn_lbl), run_time=0.4)
        self.play(FadeIn(rc), run_time=0.2)
        self.play(FadeIn(cancel), run_time=0.3)
        self.play(FadeIn(cancel_lbl), run_time=0.3)
        self.wait(dur - 2.5)


class B08_NeutronExperiment(Scene):
    """Neutron interferometer: fringe shift at 360°, reset at 720°."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Crystal/box symbols
        crystal_l = Rectangle(width=0.8, height=1.5, color=INK, fill_color=INK,
                               fill_opacity=0.5).move_to([-5.0, 0, 0])
        crystal_r = Rectangle(width=0.8, height=1.5, color=INK, fill_color=INK,
                               fill_opacity=0.5).move_to([5.0, 0, 0])
        c_lbl_l = SerifLabel("crystal", accent=INK, size=14).move_to([-5.0, -1.3, 0])
        c_lbl_r = SerifLabel("detector", accent=INK, size=14).move_to([5.0, -1.3, 0])

        # Paths
        path_up = Line([-4.6, 0.4, 0], [4.6, 0.4, 0], color=TEAL, stroke_width=2.0)
        path_dn = Line([-4.6, -0.4, 0], [4.6, -0.4, 0], color=CRIMSON, stroke_width=2.0)

        # Magnetic field region on lower path
        b_field = Rectangle(width=2.5, height=0.8, fill_color=CRIMSON, fill_opacity=0.2,
                             stroke_color=CRIMSON, stroke_width=1.5).move_to([0, -0.4, 0])
        b_lbl = SerifLabel("B-field (spin rotation)", accent=CRIMSON, size=16).move_to([0, -1.3, 0])

        # Fringe diagram (right panel)
        fringe_title = SerifLabel("fringe visibility:", accent=INK, size=18).move_to([3.5, 2.8, 0])
        # At 360°: destructive (label)
        lbl_360 = SerifLabel("360°: fringes shift (sign flip)", accent=CRIMSON, size=16).move_to([3.5, 2.0, 0])
        # At 720°: constructive (label)
        lbl_720 = SerifLabel("720°: fringes reset (sign restored)", accent=TEAL, size=16).move_to([3.5, 1.3, 0])
        year_chip = LabelChip("confirmed 1975 (Werner et al.)", accent=TEAL, size=16).move_to([0, -2.8, 0])

        self.play(FadeIn(crystal_l), FadeIn(crystal_r), FadeIn(c_lbl_l), FadeIn(c_lbl_r), run_time=0.4)
        self.play(Create(path_up), run_time=0.3)
        self.play(Create(path_dn), run_time=0.3)
        self.play(FadeIn(b_field), FadeIn(b_lbl), run_time=0.4)
        self.play(FadeIn(fringe_title), run_time=0.2)
        self.play(FadeIn(lbl_360), run_time=0.3)
        self.play(FadeIn(lbl_720), run_time=0.3)
        self.play(GrowFromCenter(year_chip), run_time=0.4)
        self.wait(dur - 2.8)


class B09_DoubleCover(Scene):
    """Two spinor states (+psi and -psi) mapping to same Bloch sphere point."""
    def construct(self):
        dur = DUR.get("B09", 9.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: spinor space — two arrows
        left_title = SerifLabel("spinor space", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        arrow_pos = Arrow(start=[-4.0, -0.5, 0], end=[-2.0, 1.5, 0],
                          color=TEAL, stroke_width=2.5, buff=0.05)
        arrow_neg = Arrow(start=[-4.0, 0.5, 0], end=[-2.0, -1.5, 0],
                          color=CRIMSON, stroke_width=2.5, buff=0.05)
        lbl_pos = SerifLabel("+|psi>", accent=TEAL, size=18).move_to([-1.5, 1.8, 0])
        lbl_neg = SerifLabel("-|psi>", accent=CRIMSON, size=18).move_to([-1.5, -1.8, 0])

        # Arrow showing mapping
        map_arrow = Arrow(start=[-0.2, 0, 0], end=[0.2, 0, 0], color=INK, stroke_width=2, buff=0)
        map_lbl = SerifLabel("2-to-1", accent=INK, size=16).move_to([0, 0.5, 0])

        # Right: Bloch sphere — single point
        right_title = SerifLabel("Bloch sphere", accent=INK, size=20).move_to([3.5, 3.2, 0])
        sphere = Ellipse(width=3.0, height=3.0, color=INK, stroke_width=1.5).move_to([3.5, 0, 0])
        bloch_pt = Dot([4.5, 1.2, 0], color=INK, radius=0.12)
        bloch_arrow = Arrow(start=[3.5, 0, 0], end=[4.5, 1.2, 0],
                            color=INK, stroke_width=2.5, buff=0.05)
        pt_lbl = SerifLabel("one point", accent=INK, size=18).move_to([5.2, 1.2, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), run_time=0.3)
        self.play(GrowArrow(arrow_pos), FadeIn(lbl_pos), run_time=0.4)
        self.play(GrowArrow(arrow_neg), FadeIn(lbl_neg), run_time=0.4)
        self.play(GrowArrow(map_arrow), FadeIn(map_lbl), run_time=0.3)
        self.play(FadeIn(right_title), Create(sphere), run_time=0.4)
        self.play(GrowArrow(bloch_arrow), FadeIn(bloch_pt), FadeIn(pt_lbl), run_time=0.4)
        self.wait(dur - 2.7)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("Classical rotation: period 360°.\nSpinor: period 720°.\nMinus sign hides in amplitudes.\nInterference makes it visible.",
                      font=DISPLAY, color=INK, font_size=20, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
