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


# ── B01 Title Card ────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 2.4, 0])
        title = Text("Why a Blinding Red Lamp Releases\nFewer Electrons Than a Dim UV Torch",
                     font=DISPLAY, font_size=25, color=INK, weight=BOLD, line_spacing=1.2).move_to([0, 0.6, 0])
        sub = Text("the photoelectric effect", font=SERIF, font_size=22, color=SLATE, slant=ITALIC).move_to([0, -1.1, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(dur - 1.3)


# ── B02 Three Facts ───────────────────────────────────────────────────────────
class B02_ThreeFacts(Scene):
    def construct(self):
        dur = DUR.get("B02", 10.0)

        facts = [
            ("1", "Threshold frequency", "Below ν₀: zero electrons, any intensity", -2.5),
            ("2", "No time delay", "Above threshold: electrons instantly", 0.0),
            ("3", "KE depends on frequency", "Not on intensity — only on ν", 2.5),
        ]

        header = Text("Three facts classical waves cannot explain",
                      font=DISPLAY, font_size=17, color=INK, weight=BOLD).move_to([0, 3.2, 0])
        header_line = Line([-5.5, 2.9, 0], [5.5, 2.9, 0], color=INK, stroke_width=1)

        boxes = VGroup()
        num_labels = VGroup()
        title_labels = VGroup()
        body_labels = VGroup()
        dots = VGroup()

        for num, title, body, y in facts:
            box = Rectangle(width=12.5, height=1.4, color=TEAL, fill_color=TEAL, fill_opacity=0.08).move_to([0, y, 0])
            num_lbl = Text(num, font=DISPLAY, font_size=28, color=TEAL, weight=BOLD).move_to([-5.8, y + 0.2, 0])
            title_lbl = Text(title, font=DISPLAY, font_size=17, color=INK, weight=BOLD).move_to([-1.5, y + 0.25, 0])
            body_lbl = Text(body, font=SERIF, font_size=15, color=SLATE, slant=ITALIC).move_to([0.2, y - 0.25, 0])
            d = Dot([-5.8, y - 0.25, 0], color=TEAL, radius=0.06)
            boxes.add(box)
            num_labels.add(num_lbl)
            title_labels.add(title_lbl)
            body_labels.add(body_lbl)
            dots.add(d)

        # Extra geometric variety: checkmarks and cross lines
        cross_line = Line([-6.0, -3.6, 0], [6.0, -3.6, 0], color=CRIMSON, stroke_width=1.5)
        confirm_arrow = Arrow([-1.5, -3.9, 0], [1.5, -3.9, 0], color=TEAL, stroke_width=2,
                              max_tip_length_to_length_ratio=0.2, buff=0)

        self.play(FadeIn(header), run_time=0.35)
        self.play(Create(header_line), run_time=0.2)
        self.play(Create(boxes[0]), FadeIn(num_labels[0]), run_time=0.3)
        self.play(FadeIn(title_labels[0]), FadeIn(body_labels[0]), run_time=0.3)
        self.play(Create(boxes[1]), FadeIn(num_labels[1]), run_time=0.3)
        self.play(FadeIn(title_labels[1]), FadeIn(body_labels[1]), run_time=0.3)
        self.play(Create(boxes[2]), FadeIn(num_labels[2]), run_time=0.3)
        self.play(FadeIn(title_labels[2]), FadeIn(body_labels[2]), run_time=0.3)
        self.play(FadeIn(dots), run_time=0.25)
        self.play(Create(cross_line), run_time=0.25)
        self.play(GrowArrow(confirm_arrow), run_time=0.25)
        self.wait(dur - 3.05)


# ── B03 Question Card ─────────────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        q = Text("Classical waves: more intensity = more energy.\nBelow threshold: zero electrons at any intensity.\nWhy?",
                 font=SERIF, font_size=17, color=INK, line_spacing=1.4).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(dur - 0.9)


# ── B04 Photon Packets ────────────────────────────────────────────────────────
class B04_PhotonPackets(Scene):
    def construct(self):
        dur = DUR.get("B04", 10.0)

        # Metal surface
        metal = Rectangle(width=13.0, height=1.0, color=INK, fill_color=SLATE, fill_opacity=0.5).move_to([0, -2.0, 0])
        metal_lbl = Text("metal surface", font=DISPLAY, font_size=14, color=INK).move_to([0, -2.0, 0])

        # Left side: red photons bouncing
        red_label = Text("red photon (hν < Φ)", font=DISPLAY, font_size=16, color=CRIMSON).move_to([-3.5, 3.0, 0])
        red_arrow_in = Arrow([-3.5, 2.5, 0], [-3.5, -1.3, 0], color=CRIMSON, stroke_width=3,
                             max_tip_length_to_length_ratio=0.15, buff=0)
        red_arrow_out = Arrow([-3.5, -1.3, 0], [-4.5, 0.5, 0], color=CRIMSON, stroke_width=3,
                              max_tip_length_to_length_ratio=0.15, buff=0)
        red_x = Text("✗", font=DISPLAY, font_size=32, color=CRIMSON).move_to([-3.5, 0.8, 0])
        red_block_lbl = Text("blocked", font=SERIF, font_size=16, color=CRIMSON, slant=ITALIC).move_to([-5.0, 1.0, 0])

        # Right side: UV photon ejecting electron
        uv_label = Text("UV photon (hν > Φ)", font=DISPLAY, font_size=16, color=TEAL).move_to([3.5, 3.0, 0])
        uv_arrow_in = Arrow([3.5, 2.5, 0], [3.5, -1.3, 0], color=TEAL, stroke_width=3,
                            max_tip_length_to_length_ratio=0.15, buff=0)
        electron_dot = Dot([3.5, -1.3, 0], color=TEAL, radius=0.2)
        electron_out = Arrow([3.5, -1.3, 0], [5.0, 1.0, 0], color=TEAL, stroke_width=3,
                             max_tip_length_to_length_ratio=0.15, buff=0)
        uv_check = Text("✓", font=DISPLAY, font_size=32, color=TEAL).move_to([3.5, 0.8, 0])
        uv_eject_lbl = Text("ejected", font=SERIF, font_size=16, color=TEAL, slant=ITALIC).move_to([5.0, 0.5, 0])

        # Divider
        div = Line([0, -1.0, 0], [0, 3.3, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        self.play(FadeIn(metal), FadeIn(metal_lbl), run_time=0.4)
        self.play(Create(div), run_time=0.2)
        self.play(FadeIn(red_label), FadeIn(uv_label), run_time=0.35)
        self.play(GrowArrow(red_arrow_in), GrowArrow(uv_arrow_in), run_time=0.5)
        self.play(FadeIn(electron_dot), run_time=0.2)
        self.play(GrowArrow(red_arrow_out), GrowArrow(electron_out), run_time=0.4)
        self.play(FadeIn(red_x), FadeIn(uv_check), run_time=0.3)
        self.play(FadeIn(red_block_lbl), FadeIn(uv_eject_lbl), run_time=0.3)
        self.wait(dur - 2.55)


# ── B05 Einstein Equation ─────────────────────────────────────────────────────
class B05_EinsteinEquation(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        # Vertical energy axis
        energy_axis = Arrow([0, -3.0, 0], [0, 3.5, 0], color=INK, stroke_width=2,
                            max_tip_length_to_length_ratio=0.08, buff=0)
        energy_lbl = Text("energy", font=DISPLAY, font_size=16, color=INK).next_to(energy_axis, UP, buff=0.2)

        # Work function threshold line
        phi_y = 0.0
        phi_line = DashedLine([-4.0, phi_y, 0], [4.0, phi_y, 0], color=INK, stroke_width=2, dash_length=0.15)
        phi_lbl = Text("Φ (work function)", font=MONO, font_size=16, color=INK).move_to([3.2, 0.35, 0])

        # Below threshold region
        below_rect = Rectangle(width=8.0, height=3.0, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.1).move_to([0, -1.5, 0])
        below_lbl = Text("hν < Φ  →  no escape", font=DISPLAY, font_size=17, color=CRIMSON).move_to([0, -1.5, 0])

        # Above threshold region
        above_rect = Rectangle(width=8.0, height=3.5, color=TEAL, fill_color=TEAL, fill_opacity=0.1).move_to([0, 1.75, 0])
        above_lbl = Text("hν > Φ  →  KE = hν − Φ", font=DISPLAY, font_size=17, color=TEAL).move_to([0, 1.75, 0])

        # KE arrow
        ke_arrow = Arrow([2.0, 0.1, 0], [2.0, 2.5, 0], color=TEAL, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.2, buff=0)
        ke_lbl = Text("KE", font=MONO, font_size=18, color=TEAL).next_to(ke_arrow, RIGHT, buff=0.15)

        self.play(GrowArrow(energy_axis), FadeIn(energy_lbl), run_time=0.4)
        self.play(Create(phi_line), FadeIn(phi_lbl), run_time=0.4)
        self.play(FadeIn(below_rect), run_time=0.3)
        self.play(FadeIn(below_lbl), run_time=0.3)
        self.play(FadeIn(above_rect), run_time=0.3)
        self.play(FadeIn(above_lbl), run_time=0.3)
        self.play(GrowArrow(ke_arrow), FadeIn(ke_lbl), run_time=0.4)
        self.wait(dur - 2.4)


# ── B06 Sodium Example ────────────────────────────────────────────────────────
class B06_SodiumExample(Scene):
    def construct(self):
        dur = DUR.get("B06", 11.0)

        # Sodium surface
        na_rect = Rectangle(width=13.0, height=1.5, color=INK, fill_color=SLATE, fill_opacity=0.5).move_to([0, -2.5, 0])
        na_lbl = Text("sodium  (Φ = 2.28 eV)", font=DISPLAY, font_size=16, color=INK, weight=BOLD).move_to([0, -2.5, 0])

        # Energy bar
        e_axis = Arrow([-6.0, -0.5, 0], [-6.0, 3.5, 0], color=INK, stroke_width=1.5,
                       max_tip_length_to_length_ratio=0.1, buff=0)
        e_axis_lbl = Text("eV", font=MONO, font_size=14, color=INK).move_to([-5.5, 3.6, 0])

        # Threshold line
        phi_y = 0.6  # maps to 2.28 eV
        phi_line = DashedLine([-5.8, phi_y, 0], [6.0, phi_y, 0], color=INK, stroke_width=1.5, dash_length=0.12)
        phi_lbl = Text("2.28 eV (threshold)", font=MONO, font_size=14, color=INK).move_to([3.5, 0.95, 0])

        # Green photon bar (just below threshold)
        green_bar = Rectangle(width=1.4, height=phi_y - 0.05, color=CRIMSON,
                              fill_color=CRIMSON, fill_opacity=0.7).move_to([-2.0, (phi_y - 0.05) / 2 - 0.5, 0])
        green_lbl = Text("546 nm\n2.27 eV", font=MONO, font_size=14, color=CRIMSON).move_to([-2.0, -1.2, 0])
        green_x = Text("✗", font=DISPLAY, font_size=28, color=CRIMSON).move_to([-2.0, 1.2, 0])

        # UV photon bar (well above threshold)
        uv_bar_h = 2.2  # maps to 4.13 eV
        uv_bar = Rectangle(width=1.4, height=uv_bar_h, color=TEAL,
                           fill_color=TEAL, fill_opacity=0.7).move_to([2.0, uv_bar_h / 2 - 0.5, 0])
        uv_lbl = Text("300 nm\n4.13 eV", font=MONO, font_size=14, color=TEAL).move_to([2.0, -1.2, 0])
        uv_check = Text("✓", font=DISPLAY, font_size=28, color=TEAL).move_to([2.0, 2.4, 0])

        # KE indicator
        ke_arrow = Arrow([2.7, phi_y, 0], [2.7, uv_bar_h - 0.5, 0], color=TEAL, stroke_width=2,
                         max_tip_length_to_length_ratio=0.25, buff=0)
        ke_lbl = Text("KE = 1.85 eV", font=MONO, font_size=13, color=TEAL).move_to([4.4, 1.5, 0])

        self.play(FadeIn(na_rect), FadeIn(na_lbl), run_time=0.4)
        self.play(GrowArrow(e_axis), FadeIn(e_axis_lbl), run_time=0.3)
        self.play(Create(phi_line), FadeIn(phi_lbl), run_time=0.35)
        self.play(FadeIn(green_bar), run_time=0.3)
        self.play(FadeIn(green_lbl), FadeIn(green_x), run_time=0.3)
        self.play(FadeIn(uv_bar), run_time=0.3)
        self.play(FadeIn(uv_lbl), FadeIn(uv_check), run_time=0.3)
        self.play(GrowArrow(ke_arrow), FadeIn(ke_lbl), run_time=0.4)
        self.wait(dur - 2.65)


# ── B07 Photons Cannot Pool ───────────────────────────────────────────────────
class B07_PhotonsCannotPool(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)

        # Metal surface
        metal = Rectangle(width=13.0, height=0.8, color=INK, fill_color=SLATE, fill_opacity=0.5).move_to([0, -2.4, 0])
        metal_lbl = Text("metal surface", font=DISPLAY, font_size=13, color=INK).move_to([0, -2.4, 0])

        # Left: many red photons — all bounce
        left_title = Text("1000 red photons  (hν < Φ each)", font=DISPLAY, font_size=14, color=CRIMSON).move_to([-3.5, 3.0, 0])
        red_dots = VGroup()
        red_arrows = VGroup()
        positions = [(-5.5, 2.2), (-4.5, 2.5), (-3.5, 2.2), (-2.5, 2.5), (-1.5, 2.2)]
        for x, y in positions:
            d = Dot([x, y, 0], color=CRIMSON, radius=0.13)
            a = Arrow([x, y - 0.15, 0], [x, -1.7, 0], color=CRIMSON, stroke_width=1.5,
                      max_tip_length_to_length_ratio=0.15, buff=0)
            red_dots.add(d)
            red_arrows.add(a)
        no_electron = Text("→  0 electrons", font=DISPLAY, font_size=16, color=CRIMSON).move_to([-3.5, -0.8, 0])
        no_pool_lbl = Text("cannot pool", font=SERIF, font_size=14, color=CRIMSON, slant=ITALIC).move_to([-3.5, -1.4, 0])

        # Right: 1 UV photon — ejects electron
        right_title = Text("1 UV photon  (hν > Φ)", font=DISPLAY, font_size=14, color=TEAL).move_to([3.5, 3.0, 0])
        uv_dot = Dot([3.5, 2.3, 0], color=TEAL, radius=0.18)
        uv_arrow = Arrow([3.5, 2.1, 0], [3.5, -1.7, 0], color=TEAL, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.15, buff=0)
        electron_out = Dot([4.5, 0.5, 0], color=TEAL, radius=0.18)
        electron_arrow = Arrow([3.5, -1.7, 0], [5.0, 1.0, 0], color=TEAL, stroke_width=2.5,
                               max_tip_length_to_length_ratio=0.15, buff=0)
        yes_lbl = Text("→  1 electron", font=DISPLAY, font_size=16, color=TEAL).move_to([3.5, -0.8, 0])

        # Divider
        div = Line([0, -1.5, 0], [0, 3.3, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        self.play(FadeIn(metal), FadeIn(metal_lbl), run_time=0.3)
        self.play(Create(div), run_time=0.2)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.35)
        self.play(FadeIn(red_dots), FadeIn(uv_dot), run_time=0.35)
        self.play(*[GrowArrow(a) for a in red_arrows], GrowArrow(uv_arrow), run_time=0.5)
        self.play(FadeIn(electron_out), run_time=0.2)
        self.play(GrowArrow(electron_arrow), run_time=0.3)
        self.play(FadeIn(no_electron), FadeIn(yes_lbl), run_time=0.3)
        self.play(FadeIn(no_pool_lbl), run_time=0.25)
        self.wait(dur - 2.7)


# ── B08 Intensity vs Frequency ────────────────────────────────────────────────
class B08_IntensityVsFrequency(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        # Header
        header = Text("Intensity and frequency are independent", font=DISPLAY, font_size=18, color=INK, weight=BOLD).move_to([0, 3.1, 0])
        h_line = Line([-5.0, 2.8, 0], [5.0, 2.8, 0], color=INK, stroke_width=1)

        # Left column: intensity → count rate
        left_box = Rectangle(width=5.5, height=4.8, color=SLATE, fill_color=SLATE, fill_opacity=0.07).move_to([-3.4, 0.2, 0])
        left_title = Text("Intensity", font=DISPLAY, font_size=18, color=SLATE, weight=BOLD).move_to([-3.4, 2.2, 0])
        left_sub = Text("controls count rate", font=SERIF, font_size=15, color=SLATE, slant=ITALIC).move_to([-3.4, 1.65, 0])
        left_divider = Line([-6.0, 1.35, 0], [-0.8, 1.35, 0], color=SLATE, stroke_width=0.8)
        left_up = Arrow([-3.4, 0.4, 0], [-3.4, 1.1, 0], color=SLATE, stroke_width=2,
                        max_tip_length_to_length_ratio=0.25, buff=0)
        left_up_lbl = Text("more photons/s\n= more electrons/s", font=DISPLAY, font_size=13, color=SLATE).move_to([-3.4, -0.4, 0])
        left_dot = Dot([-3.4, -1.5, 0], color=SLATE, radius=0.08)

        # Right column: frequency → KE
        right_box = Rectangle(width=5.5, height=4.8, color=TEAL, fill_color=TEAL, fill_opacity=0.07).move_to([3.4, 0.2, 0])
        right_title = Text("Frequency", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD).move_to([3.4, 2.2, 0])
        right_sub = Text("controls KE per electron", font=SERIF, font_size=15, color=TEAL, slant=ITALIC).move_to([3.4, 1.65, 0])
        right_divider = Line([0.8, 1.35, 0], [6.0, 1.35, 0], color=TEAL, stroke_width=0.8)
        right_up = Arrow([3.4, 0.4, 0], [3.4, 1.1, 0], color=TEAL, stroke_width=2,
                         max_tip_length_to_length_ratio=0.25, buff=0)
        right_up_lbl = Text("higher freq\n= higher KE", font=DISPLAY, font_size=13, color=TEAL).move_to([3.4, -0.4, 0])
        right_dot = Dot([3.4, -1.5, 0], color=TEAL, radius=0.08)

        self.play(FadeIn(header), Create(h_line), run_time=0.4)
        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.4)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.35)
        self.play(Create(left_divider), Create(right_divider), run_time=0.25)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.35)
        self.play(GrowArrow(left_up), GrowArrow(right_up), run_time=0.35)
        self.play(FadeIn(left_up_lbl), FadeIn(right_up_lbl), run_time=0.35)
        self.play(FadeIn(left_dot), FadeIn(right_dot), run_time=0.25)
        self.wait(dur - 2.7)


# ── B09 Millikan Confirmation ─────────────────────────────────────────────────
class B09_MillikanConfirm(Scene):
    def construct(self):
        dur = DUR.get("B09", 9.0)

        # Axes: stopping potential vs frequency
        ax = Axes(
            x_range=[4, 14, 2], y_range=[0, 3.5, 1],
            x_length=7.0, y_length=3.5,
            axis_config={"color": INK, "stroke_width": 1.5}, tips=False
        ).move_to([0.0, -0.5, 0])
        x_lbl = Text("frequency ν (×10¹⁴ Hz)", font=DISPLAY, font_size=13, color=INK).next_to(ax, DOWN, buff=0.3)
        y_lbl = Text("V_stop (V)", font=DISPLAY, font_size=13, color=INK).next_to(ax, LEFT, buff=0.3)

        # Three metal lines (same slope h/e)
        h_over_e = 4.136e-15  # V·s
        metals = [
            ("Na  Φ=2.28eV", 5.5, TEAL),
            ("Li  Φ=2.9eV", 7.0, SLATE),
            ("Cu  Φ=4.7eV", 11.4, CRIMSON),
        ]

        lines_obj = VGroup()
        dots_obj = VGroup()
        for name, nu0, color in metals:
            line = ax.plot(
                lambda x, n0=nu0: max(0, h_over_e * (x * 1e14 - n0 * 1e14)),
                x_range=[nu0, 13.5],
                color=color, stroke_width=2.5
            )
            d = Dot(ax.coords_to_point(nu0, 0), color=color, radius=0.09)
            lines_obj.add(line)
            dots_obj.add(d)

        # Labels
        na_lbl = Text("Na", font=MONO, font_size=13, color=TEAL).move_to(ax.coords_to_point(6.5, 0.5))
        slope_lbl = Text("slope = h/e (same for all metals)", font=SERIF, font_size=13, color=INK, slant=ITALIC).move_to([0, 2.8, 0])

        # Citation chip
        cite_chip = LabelChip("Einstein Nobel 1921", accent=TEAL, size=18).move_to([-3.2, -3.2, 0])
        millikan_chip = LabelChip("Millikan Nobel 1923", accent=SLATE, size=18).move_to([3.2, -3.2, 0])

        # Add slope indicator arrow for variety
        slope_arrow = Arrow(
            ax.coords_to_point(6.5, 0.3),
            ax.coords_to_point(10.0, 2.1),
            color=TEAL, stroke_width=2,
            max_tip_length_to_length_ratio=0.15, buff=0
        )
        # Threshold dots for each metal
        threshold_line = Line(ax.coords_to_point(5.5, 0), ax.coords_to_point(5.5, -0.2),
                              color=TEAL, stroke_width=2)

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(lines_obj[0]), FadeIn(dots_obj[0]), run_time=0.4)
        self.play(Create(lines_obj[1]), FadeIn(dots_obj[1]), run_time=0.35)
        self.play(Create(lines_obj[2]), FadeIn(dots_obj[2]), run_time=0.35)
        self.play(FadeIn(na_lbl), run_time=0.25)
        self.play(GrowArrow(slope_arrow), FadeIn(slope_lbl), run_time=0.35)
        self.play(Create(threshold_line), run_time=0.2)
        self.play(GrowFromCenter(cite_chip), run_time=0.3)
        self.play(GrowFromCenter(millikan_chip), run_time=0.3)
        self.wait(dur - 3.0)


# ── B10 Recap Card ────────────────────────────────────────────────────────────
class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        recap = Text(
            "KE = hnu - phi. Below threshold: no electrons ever.\nIntensity = count, not energy.\nOne photon acts alone.",
            font=SERIF, font_size=18, color=INK, line_spacing=1.5
        ).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(dur - 0.9)
