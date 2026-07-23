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
        title = Text("Why You Don't Diffract\nWalking Through a Doorway",
                     font=DISPLAY, color=INK, font_size=32, line_spacing=1.3).move_to([0, 0.5, 0])
        sub = Text("de Broglie wavelength and the classical limit",
                   font=SERIF, color=INK, font_size=17, slant=ITALIC).move_to([0, -0.8, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.0, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 2.3)


class B02_DeBroglieFormula(Scene):
    """lambda = h/p formula with electron and person examples."""
    def construct(self):
        dur = DUR.get("B02", 10.0)
        formula = Text("lambda = h / p",
                       font=MONO, color=TEAL, font_size=36).move_to([0, 2.5, 0])
        box = SurroundingRectangle(formula, color=TEAL, buff=0.2, stroke_width=2.0)

        divider = Line([0, -3.5, 0], [0, 1.5, 0], color=INK, stroke_width=1.2)

        # Left: electron
        e_title = SerifLabel("electron (54 eV)", accent=TEAL, size=20).move_to([-3.5, 1.0, 0])
        e_p = Text("p = 3.97e-24 kg m/s",
                   font=MONO, color=TEAL, font_size=18).move_to([-3.5, 0.1, 0])
        e_l = Text("lambda = 0.167 nm",
                   font=MONO, color=TEAL, font_size=20).move_to([-3.5, -0.7, 0])
        e_chip = LabelChip("atom-sized: diffract!", accent=TEAL, size=18).move_to([-3.5, -1.6, 0])

        # Right: person
        p_title = SerifLabel("person (70 kg, 1 m/s)", accent=CRIMSON, size=20).move_to([3.5, 1.0, 0])
        p_p = Text("p = 70 kg m/s",
                   font=MONO, color=CRIMSON, font_size=18).move_to([3.5, 0.1, 0])
        p_l = Text("lambda = 1e-35 m",
                   font=MONO, color=CRIMSON, font_size=20).move_to([3.5, -0.7, 0])
        p_chip = LabelChip("sub-proton: no grating!", accent=CRIMSON, size=18).move_to([3.5, -1.6, 0])

        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.3)
        self.play(Create(box), run_time=0.2)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(e_title), run_time=0.2)
        self.play(FadeIn(e_p), run_time=0.2)
        self.play(FadeIn(e_l), run_time=0.2)
        self.play(GrowFromCenter(e_chip), run_time=0.3)
        # Visual indicator for electron wavelength
        e_bar = Rectangle(width=0.167 * 8, height=0.3, fill_color=TEAL, fill_opacity=0.8,
                          stroke_color=TEAL, stroke_width=1.0).move_to([-3.5, -2.5, 0])
        self.play(GrowFromCenter(e_bar), run_time=0.3)
        self.play(FadeIn(p_title), run_time=0.2)
        self.play(FadeIn(p_p), run_time=0.2)
        self.play(FadeIn(p_l), run_time=0.2)
        self.play(GrowFromCenter(p_chip), run_time=0.3)
        # Visual indicator for person wavelength (tiny dot)
        p_dot = Dot([3.5, -2.5, 0], color=CRIMSON, radius=0.05)
        self.play(FadeIn(p_dot), run_time=0.2)
        # Emphasize contrast
        self.play(e_chip.animate.scale(1.05), p_chip.animate.scale(1.05), run_time=0.3)
        self.wait(dur - 3.8)


class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        title = Text("Electrons: lambda = 0.167 nm — atom-sized. Diffract.\nYou at 1 m/s: lambda = ?\nWhy does the same formula not give you fringes?",
                     font=DISPLAY, color=INK, font_size=16, line_spacing=1.3).move_to([0, 0.3, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.5, 0])
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_HumanCalculation(Scene):
    """Step-by-step de Broglie calculation for a human."""
    def construct(self):
        dur = DUR.get("B04", 9.0)
        step1 = Text("m = 70 kg,  v = 1 m/s",
                     font=MONO, color=INK, font_size=24).move_to([0, 2.5, 0])
        arrow1 = Arrow(start=[0, 2.0, 0], end=[0, 1.3, 0], color=INK, stroke_width=2.0, buff=0.05)
        step2 = Text("p = m * v = 70 kg m/s",
                     font=MONO, color=INK, font_size=24).move_to([0, 0.9, 0])
        arrow2 = Arrow(start=[0, 0.4, 0], end=[0, -0.3, 0], color=INK, stroke_width=2.0, buff=0.05)
        step3 = Text("lambda = h / p",
                     font=MONO, color=TEAL, font_size=24).move_to([0, -0.7, 0])
        arrow3 = Arrow(start=[0, -1.2, 0], end=[0, -1.9, 0], color=INK, stroke_width=2.0, buff=0.05)
        result = Text("= 6.626e-34 / 70",
                      font=MONO, color=TEAL, font_size=24).move_to([0, -2.3, 0])
        final = Text("= 9.5 x 10^-36 m",
                     font=MONO, color=CRIMSON, font_size=28).move_to([0, -3.2, 0])

        # Background axis for visual variety
        axis_line = Line([-5.5, 0, 0], [5.5, 0, 0], color=INK, stroke_width=1.0, stroke_opacity=0.3)
        self.play(Create(axis_line), run_time=0.2)
        self.play(FadeIn(step1), run_time=0.2)
        self.play(GrowArrow(arrow1), run_time=0.2)
        self.play(FadeIn(step2), run_time=0.2)
        self.play(GrowArrow(arrow2), run_time=0.2)
        self.play(FadeIn(step3), run_time=0.2)
        self.play(GrowArrow(arrow3), run_time=0.2)
        self.play(FadeIn(result), run_time=0.2)
        self.play(FadeIn(final, shift=DOWN * 0.1), run_time=0.3)
        # Highlight final result
        final_box = SurroundingRectangle(final, color=CRIMSON, buff=0.15, stroke_width=2.0)
        self.play(Create(final_box), run_time=0.3)
        # Add comparison dot
        proton_dot = Dot([-3.0, -3.5, 0], color=INK, radius=0.1)
        proton_note = SerifLabel("proton: 1e-15 m", accent=INK, size=16).move_to([1.0, -3.5, 0])
        self.play(FadeIn(proton_dot), FadeIn(proton_note), run_time=0.3)
        self.wait(dur - 3.2)


class B05_ScaleComparison(Scene):
    """Logarithmic scale bar comparing wavelengths."""
    def construct(self):
        dur = DUR.get("B05", 10.0)
        # Scale bar axis
        ax = Arrow(start=[-5.5, 0, 0], end=[5.5, 0, 0], color=INK, stroke_width=2.0, buff=0)
        ax_lbl = SerifLabel("wavelength (log scale)", accent=INK, size=18).move_to([0, -0.6, 0])

        # Markers: position them along -5 to +5
        markers = [
            (-4.5, "1e-35 m\n(you)", CRIMSON),
            (-1.5, "1e-12 m\nbuckyball", TEAL),
            (0.5, "0.167 nm\nelectron", TEAL),
            (3.5, "400 nm\nvisible light", INK),
        ]

        dots = VGroup()
        labels = VGroup()
        for x, lbl, color in markers:
            d = Dot([x, 0, 0], color=color, radius=0.12)
            t = Text(lbl, font=SERIF, color=color, font_size=14, line_spacing=1.1).move_to([x, -1.4, 0])
            dots.add(d)
            labels.add(t)

        # Proton radius line
        proton_tick = Line([-4.5, -0.2, 0], [-4.5, 0.2, 0], color=INK, stroke_width=1.5)
        proton_lbl = SerifLabel("proton: 1e-15 m", accent=INK, size=14).move_to([-4.5, 0.6, 0])

        gap_brace = DoubleArrow(start=[-4.5, 1.5, 0], end=[-3.5, 1.5, 0],
                                 color=CRIMSON, stroke_width=1.5, buff=0)
        gap_lbl = SerifLabel("20 orders of magnitude", accent=CRIMSON, size=16).move_to([-1.5, 1.5, 0])

        self.play(GrowArrow(ax), FadeIn(ax_lbl), run_time=0.3)
        # Add dots one by one
        for d in dots:
            self.play(FadeIn(d), run_time=0.2)
        self.play(FadeIn(labels), run_time=0.4)
        self.play(FadeIn(proton_tick), FadeIn(proton_lbl), run_time=0.3)
        self.play(GrowFromCenter(gap_brace), FadeIn(gap_lbl), run_time=0.4)
        self.wait(dur - 0.3 - 4 * 0.2 - 0.4 - 0.3 - 0.4)


class B06_SlitCondition(Scene):
    """Electron fits through atom slit; person needs impossibly small slit."""
    def construct(self):
        dur = DUR.get("B06", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: electron + atom slit (TEAL)
        left_title = SerifLabel("electron: lambda ~ slit size", accent=TEAL, size=18).move_to([-3.5, 3.2, 0])
        # Slit
        slit_l1 = Rectangle(width=0.5, height=2.5, fill_color=INK, fill_opacity=0.7,
                             stroke_color=INK, stroke_width=1.5).move_to([-4.0, 0, 0])
        slit_l2 = Rectangle(width=0.5, height=2.5, fill_color=INK, fill_opacity=0.7,
                             stroke_color=INK, stroke_width=1.5).move_to([-3.0, 0, 0])
        # Gap label
        gap_l = DoubleArrow(start=[-3.95, -1.7, 0], end=[-3.05, -1.7, 0],
                             color=TEAL, stroke_width=1.5, buff=0)
        gap_l_lbl = SerifLabel("0.167 nm gap", accent=TEAL, size=16).move_to([-3.5, -2.2, 0])
        # Diffraction lines
        diff_lines = VGroup(*[
            Line([-2.8, 0, 0], [-1.5 + 0.3 * i, 1.5 * np.sin(i * 0.3), 0],
                 color=TEAL, stroke_width=1.5, stroke_opacity=0.7)
            for i in range(-3, 4)
        ])
        works_chip = LabelChip("diffraction: YES", accent=TEAL, size=18).move_to([-3.5, -3.2, 0])

        # Right: person + impossible slit (CRIMSON)
        right_title = SerifLabel("person: need impossible slit", accent=CRIMSON, size=18).move_to([3.5, 3.2, 0])
        impossible_lbl = Text("required slit:\n1e-35 m",
                              font=MONO, color=CRIMSON, font_size=20, line_spacing=1.2).move_to([3.5, 0.5, 0])
        sub_lbl = SerifLabel("20x smaller than proton", accent=CRIMSON, size=16).move_to([3.5, -0.5, 0])
        cross = VGroup(
            Line([1.5, -1.5, 0], [5.5, 1.5, 0], color=CRIMSON, stroke_width=3.5),
            Line([1.5, 1.5, 0], [5.5, -1.5, 0], color=CRIMSON, stroke_width=3.5),
        )

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), run_time=0.3)
        self.play(FadeIn(slit_l1), FadeIn(slit_l2), run_time=0.3)
        self.play(GrowFromCenter(gap_l), FadeIn(gap_l_lbl), run_time=0.3)
        self.play(Create(diff_lines), run_time=0.4)
        self.play(GrowFromCenter(works_chip), run_time=0.3)
        self.play(FadeIn(right_title), run_time=0.3)
        self.play(FadeIn(impossible_lbl), FadeIn(sub_lbl), run_time=0.3)
        self.play(Create(cross), run_time=0.3)
        self.wait(dur - 2.8)


class B07_FringeTooFine(Scene):
    """Two fringe patterns: wide (visible) vs compressed (invisible)."""
    def construct(self):
        dur = DUR.get("B07", 10.0)
        divider = Line([0, -3.5, 0], [0, 3.5, 0], color=INK, stroke_width=1.2)

        # Left: electron — wide fringes (TEAL)
        left_title = SerifLabel("electron fringes", accent=TEAL, size=20).move_to([-3.5, 3.2, 0])
        base_l = Arrow([-5.8, -2.0, 0], [-0.2, -2.0, 0], color=INK, stroke_width=1.5, buff=0)
        for i, x in enumerate(np.linspace(-5.5, -0.5, 8)):
            h = 2.0 * abs(np.cos(i * np.pi / 2))
            self.add(Rectangle(width=0.45, height=h,
                               fill_color=TEAL, fill_opacity=0.7,
                               stroke_color=TEAL, stroke_width=1.0
                               ).move_to([x, -2.0 + h / 2, 0]))
        fringe_lbl_l = SerifLabel("spacing: visible!", accent=TEAL, size=18).move_to([-3.5, -2.8, 0])

        # Right: person — invisible fringes (CRIMSON)
        right_title = SerifLabel("person fringes", accent=CRIMSON, size=20).move_to([3.5, 3.2, 0])
        base_r = Arrow([0.2, -2.0, 0], [5.8, -2.0, 0], color=INK, stroke_width=1.5, buff=0)
        # Draw as a blur to represent unresolvable fringes
        blur = Rectangle(width=5.0, height=2.5, fill_color=CRIMSON, fill_opacity=0.2,
                         stroke_color=CRIMSON, stroke_width=1.5).move_to([3.0, -0.75, 0])
        fringe_lbl_r = SerifLabel("spacing: 1e-35 m (invisible)", accent=CRIMSON, size=16).move_to([3.0, -2.8, 0])

        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(left_title), GrowArrow(base_l), run_time=0.3)
        self.play(GrowFromCenter(fringe_lbl_l), run_time=0.3)
        self.play(FadeIn(right_title), GrowArrow(base_r), run_time=0.3)
        self.play(FadeIn(blur), run_time=0.3)
        self.play(FadeIn(fringe_lbl_r), run_time=0.3)
        self.wait(dur - 2.0)


class B08_BuckyballDiffraction(Scene):
    """C60 buckyball + 50 nm grating + diffraction pattern."""
    def construct(self):
        dur = DUR.get("B08", 10.0)
        # Buckyball label
        bucky_circle = Circle(radius=0.6, color=TEAL, stroke_width=2.0).move_to([-4.5, 0, 0])
        bucky_lbl = Text("C60\nbuckyball",
                         font=SERIF, color=TEAL, font_size=16, line_spacing=1.1).move_to([-4.5, -1.3, 0])
        lambda_lbl = SerifLabel("lambda ~ 2.5 pm", accent=TEAL, size=18).move_to([-4.5, 1.2, 0])

        # Arrow to grating
        to_grating = Arrow(start=[-3.6, 0, 0], end=[-1.5, 0, 0],
                           color=TEAL, stroke_width=2.0, buff=0.05)

        # Grating (multiple slits)
        grating_lines = VGroup(*[
            Line([-1.5, -2.5 + i * 0.5, 0], [-1.5, -2.0 + i * 0.5, 0],
                 color=INK, stroke_width=3.0)
            for i in range(10)
        ])
        grating_lbl = SerifLabel("50 nm slit grating", accent=INK, size=16).move_to([-1.5, -3.0, 0])

        # Diffraction pattern
        pattern_title = SerifLabel("fringe pattern (1999)", accent=TEAL, size=18).move_to([3.5, 3.0, 0])
        for i, x in enumerate(np.linspace(1.0, 5.5, 9)):
            h = 2.5 * abs(np.cos((i - 4) * np.pi / 4))
            self.add(Rectangle(width=0.35, height=h,
                               fill_color=TEAL, fill_opacity=0.8 * abs(np.cos((i - 4) * np.pi / 4)) + 0.1,
                               stroke_color=TEAL, stroke_width=0.5
                               ).move_to([x, -2.0 + h / 2, 0]))

        base_r = Arrow([0.8, -2.0, 0], [5.8, -2.0, 0], color=INK, stroke_width=1.5, buff=0)
        year_chip = LabelChip("Zeilinger group, Vienna 1999", accent=TEAL, size=18).move_to([3.5, -3.0, 0])

        self.play(FadeIn(bucky_circle), run_time=0.3)
        self.play(FadeIn(bucky_lbl), FadeIn(lambda_lbl), run_time=0.3)
        self.play(GrowArrow(to_grating), run_time=0.3)
        self.play(Create(grating_lines), run_time=0.3)
        self.play(FadeIn(grating_lbl), run_time=0.2)
        self.play(FadeIn(pattern_title), run_time=0.2)
        self.play(GrowArrow(base_r), run_time=0.3)
        self.play(GrowFromCenter(year_chip), run_time=0.4)
        self.wait(dur - 2.6)


class B09_ClassicalLimit(Scene):
    """As mass grows, lambda shrinks, fringes unresolvable — classical behavior."""
    def construct(self):
        dur = DUR.get("B09", 9.0)
        # Header
        header_mass = SerifLabel("particle", accent=INK, size=18).move_to([-2.5, 3.5, 0])
        header_lambda = SerifLabel("de Broglie wavelength", accent=INK, size=18).move_to([2.5, 3.5, 0])
        divider_h = Line([-5.5, 3.0, 0], [5.5, 3.0, 0], color=INK, stroke_width=1.5)

        row1_m = Text("electron", font=MONO, color=TEAL, font_size=16).move_to([-2.5, 2.4, 0])
        row1_l = Text("0.167 nm", font=MONO, color=TEAL, font_size=16).move_to([2.5, 2.4, 0])

        row2_m = Text("proton", font=MONO, color=TEAL, font_size=16).move_to([-2.5, 1.5, 0])
        row2_l = Text("4 pm", font=MONO, color=TEAL, font_size=16).move_to([2.5, 1.5, 0])

        row3_m = Text("C60 buckyball", font=MONO, color=TEAL, font_size=16).move_to([-2.5, 0.6, 0])
        row3_l = Text("2.5 pm", font=MONO, color=TEAL, font_size=16).move_to([2.5, 0.6, 0])

        row4_m = Text("dust grain", font=MONO, color=CRIMSON, font_size=16).move_to([-2.5, -0.3, 0])
        row4_l = Text("7e-19 m", font=MONO, color=CRIMSON, font_size=16).move_to([2.5, -0.3, 0])

        row5_m = Text("person (70 kg)", font=MONO, color=CRIMSON, font_size=16).move_to([-2.5, -1.2, 0])
        row5_l = Text("1e-35 m", font=MONO, color=CRIMSON, font_size=16).move_to([2.5, -1.2, 0])

        conclusion = SerifLabel("quantum never turns off — wavelength just shrinks", accent=INK, size=18).move_to([0, -2.5, 0])

        # Arrow showing trend
        trend_arrow = Arrow(start=[-5.0, 2.0, 0], end=[-5.0, -2.0, 0],
                            color=INK, stroke_width=2.0, buff=0)
        trend_lbl = SerifLabel("mass up", accent=INK, size=14).move_to([-5.8, 0, 0])
        lambda_arrow = Arrow(start=[5.0, 2.0, 0], end=[5.0, -2.0, 0],
                             color=CRIMSON, stroke_width=2.0, buff=0)
        lambda_trend = SerifLabel("lambda down", accent=CRIMSON, size=14).move_to([5.8, 0, 0])

        self.play(GrowArrow(trend_arrow), FadeIn(trend_lbl), run_time=0.3)
        self.play(GrowArrow(lambda_arrow), FadeIn(lambda_trend), run_time=0.3)
        self.play(FadeIn(header_mass), FadeIn(header_lambda), run_time=0.2)
        self.play(Create(divider_h), run_time=0.2)
        self.play(FadeIn(row1_m), FadeIn(row1_l), run_time=0.2)
        self.play(FadeIn(row2_m), FadeIn(row2_l), run_time=0.2)
        self.play(FadeIn(row3_m), FadeIn(row3_l), run_time=0.2)
        self.play(FadeIn(row4_m), FadeIn(row4_l), run_time=0.2)
        self.play(FadeIn(row5_m), FadeIn(row5_l), run_time=0.2)
        self.play(FadeIn(conclusion), run_time=0.3)
        self.wait(dur - 2.5)


class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        answer = Text("lambda = h / p for everything.\nElectron: 0.167 nm — diffraction visible.\nPerson: 1e-35 m — no grating exists.\nQuantum never turns off.",
                      font=DISPLAY, color=INK, font_size=17, line_spacing=1.3).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.5, 0])
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
