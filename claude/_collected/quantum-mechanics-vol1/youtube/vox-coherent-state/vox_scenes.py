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


def gaussian(x, center, sigma, height=1.0):
    return height * np.exp(-0.5 * ((x - center) / sigma) ** 2)


# ── B01 Title Card ────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 2.2, 0])
        title = Text("Why One Quantum Packet\nCan Slosh Without Spreading",
                     font=DISPLAY, font_size=28, color=INK, weight=BOLD, line_spacing=1.2).move_to([0, 0.4, 0])
        sub = Text("coherent states", font=SERIF, font_size=22, color=SLATE, slant=ITALIC).move_to([0, -1.2, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(dur - 1.3)


# ── B02 Free Packet Spreads ───────────────────────────────────────────────────
class B02_FreePacketSpreads(Scene):
    def construct(self):
        dur = DUR.get("B02", 11.0)

        # Axes
        ax = Axes(
            x_range=[-5, 5, 1], y_range=[0, 1.2, 0.5],
            x_length=10, y_length=3.2,
            axis_config={"color": INK, "stroke_width": 1.5}, tips=False
        ).move_to([0, -0.6, 0])
        x_lbl = Text("x", font=DISPLAY, font_size=16, color=INK).next_to(ax, RIGHT, buff=0.2)
        y_lbl = Text("|ψ|²", font=MONO, font_size=16, color=INK).next_to(ax, UP, buff=0.15)

        sigma0 = 0.55
        sigma1 = 1.4

        curve0 = ax.plot(lambda x: gaussian(x, 0, sigma0), color=TEAL, stroke_width=3)
        curve1 = ax.plot(lambda x: gaussian(x, 1.5, sigma1, height=sigma0/sigma1),
                         color=CRIMSON, stroke_width=3)

        # Width arrows
        w0_left = ax.coords_to_point(-sigma0, 0.6)
        w0_right = ax.coords_to_point(sigma0, 0.6)
        w1_left = ax.coords_to_point(1.5 - sigma1, 0.3)
        w1_right = ax.coords_to_point(1.5 + sigma1, 0.3)

        width0_arrow = DoubleArrow(w0_left, w0_right, color=TEAL, stroke_width=2,
                                   max_tip_length_to_length_ratio=0.15, buff=0)
        width1_arrow = DoubleArrow(w1_left, w1_right, color=CRIMSON, stroke_width=2,
                                   max_tip_length_to_length_ratio=0.15, buff=0)

        t0_lbl = Text("t = 0", font=DISPLAY, font_size=16, color=TEAL).move_to([0, 2.0, 0])
        t1_lbl = Text("t = T", font=DISPLAY, font_size=16, color=CRIMSON).move_to([3.5, 2.0, 0])
        spread_lbl = Text("spreads!", font=SERIF, font_size=18, color=CRIMSON, slant=ITALIC).move_to([3.5, 1.4, 0])

        # extra geometric: time arrow and midpoint curve
        time_arrow = Arrow([-1.5, 2.8, 0], [1.5, 2.8, 0], color=INK, stroke_width=2,
                           max_tip_length_to_length_ratio=0.15, buff=0)
        time_lbl_obj = Text("time →", font=DISPLAY, font_size=13, color=INK).move_to([0, 3.2, 0])

        # intermediate curve (t = T/2)
        sigma_mid = 0.95
        curve_mid = ax.plot(lambda x: gaussian(x, 0.7, sigma_mid, height=sigma0/sigma_mid),
                            color=GOLD, stroke_width=2)

        # Peak dot marker for each curve
        peak0_dot = Dot(ax.coords_to_point(0, 1.0), color=TEAL, radius=0.1)
        peak1_dot = Dot(ax.coords_to_point(1.5, sigma0/sigma1), color=CRIMSON, radius=0.1)

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.4)
        self.play(Create(curve0), FadeIn(t0_lbl), run_time=0.4)
        self.play(FadeIn(peak0_dot), run_time=0.2)
        self.play(Create(width0_arrow), run_time=0.25)
        self.play(GrowArrow(time_arrow), FadeIn(time_lbl_obj), run_time=0.35)
        self.play(Create(curve_mid), run_time=0.4)
        self.play(Create(curve1), FadeIn(t1_lbl), run_time=0.4)
        self.play(FadeIn(peak1_dot), run_time=0.2)
        self.play(Create(width1_arrow), run_time=0.25)
        self.play(FadeIn(spread_lbl), run_time=0.3)
        self.wait(dur - 2.95 - 0.4)


# ── B03 Question Card ─────────────────────────────────────────────────────────
class B03_QuestionCard(Scene):
    def construct(self):
        dur = DUR.get("B03", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        q = Text("Free particle: spreads forever.\nIn a parabolic well: never spreads.\nWhy not?",
                 font=SERIF, font_size=17, color=INK, line_spacing=1.4).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(dur - 0.9)


# ── B04 Restoring Force ───────────────────────────────────────────────────────
class B04_RestoringForce(Scene):
    def construct(self):
        dur = DUR.get("B04", 11.0)

        # Left panel: free packet fanning
        left_title = Text("free particle", font=DISPLAY, font_size=18, color=CRIMSON).move_to([-3.8, 2.8, 0])
        left_border = Rectangle(width=5.5, height=5.2, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.04).move_to([-3.8, 0.0, 0])

        # Central Gaussian
        center_dot = Dot([-3.8, 0.0, 0], color=TEAL, radius=0.12)
        fan_arrows = VGroup()
        for angle in np.linspace(-np.pi / 4, np.pi / 4, 5):
            dx = 1.5 * np.cos(angle)
            dy = 1.5 * np.sin(angle)
            arr = Arrow([-3.8, 0.0, 0], [-3.8 + dx, dy, 0],
                        color=CRIMSON, stroke_width=2,
                        max_tip_length_to_length_ratio=0.2, buff=0)
            fan_arrows.add(arr)
        fan_lbl = Text("components fan apart", font=SERIF, font_size=13, color=CRIMSON, slant=ITALIC).move_to([-3.8, -2.2, 0])

        # Right panel: harmonic well restoring
        right_title = Text("harmonic well", font=DISPLAY, font_size=18, color=TEAL).move_to([3.2, 2.8, 0])
        right_border = Rectangle(width=5.5, height=5.2, color=TEAL, fill_color=TEAL, fill_opacity=0.04).move_to([3.2, 0.0, 0])

        # Parabola
        parabola = FunctionGraph(
            lambda x: (x - 3.2) ** 2 * 0.4 - 2.2,
            x_range=[0.7, 5.7],
            color=INK, stroke_width=2
        )
        restore_dot = Dot([3.2, 0.0, 0], color=TEAL, radius=0.12)
        restore_arrows = VGroup()
        for dx_sign, label_x in [(-1, -0.5), (1, 0.5)]:
            arr = Arrow(
                [3.2 + dx_sign * 1.0, 0.2, 0],
                [3.2 + dx_sign * 0.2, 0.2, 0],
                color=TEAL, stroke_width=2,
                max_tip_length_to_length_ratio=0.2, buff=0
            )
            restore_arrows.add(arr)
        restore_lbl = Text("restoring force cancels spread", font=SERIF, font_size=12, color=TEAL, slant=ITALIC).move_to([3.2, -2.2, 0])

        # Separator line
        sep_line = Line([0, -2.8, 0], [0, 2.8, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        self.play(FadeIn(left_border), FadeIn(right_border), run_time=0.4)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.3)
        self.play(Create(sep_line), run_time=0.2)
        self.play(FadeIn(center_dot), FadeIn(restore_dot), run_time=0.3)
        self.play(*[GrowArrow(a) for a in fan_arrows], run_time=0.5)
        self.play(Create(parabola), run_time=0.4)
        self.play(*[GrowArrow(a) for a in restore_arrows], run_time=0.4)
        self.play(FadeIn(fan_lbl), FadeIn(restore_lbl), run_time=0.4)
        self.wait(dur - 2.9)


# ── B05 Coherent Slosh ────────────────────────────────────────────────────────
class B05_CoherentSlosh(Scene):
    def construct(self):
        dur = DUR.get("B05", 10.0)

        # Parabola (bowl)
        parabola = FunctionGraph(
            lambda x: 0.35 * x ** 2 - 2.5,
            x_range=[-4.0, 4.0],
            color=INK, stroke_width=2.5
        )

        # Gaussian packet at different positions
        sigma = 0.7
        positions = [-2.5, 0.0, 2.5, 0.0, -2.5]

        initial_curve = FunctionGraph(
            lambda x: gaussian(x, positions[0], sigma, height=1.4),
            x_range=[-5.5, 5.5], color=TEAL, stroke_width=3
        )

        # Width indicator arrows
        def width_arrows(cx):
            left = np.array([cx - sigma, 0.7, 0])
            right = np.array([cx + sigma, 0.7, 0])
            return DoubleArrow(left, right, color=TEAL, stroke_width=2,
                               max_tip_length_to_length_ratio=0.15, buff=0)

        wa = width_arrows(positions[0])
        sigma_lbl = Text("σ = constant", font=MONO, font_size=16, color=TEAL).move_to([0, 1.4, 0])
        min_unc_lbl = Text("σₓσₚ = ℏ/2  (minimum uncertainty)", font=MONO, font_size=14, color=TEAL).move_to([0, 2.1, 0])

        # Classical frequency label
        omega_lbl = Text("oscillates at ω (classical frequency)", font=SERIF, font_size=15, color=INK, slant=ITALIC).move_to([0, -2.8, 0])

        self.play(Create(parabola), run_time=0.4)
        self.play(Create(initial_curve), run_time=0.4)
        self.play(Create(wa), run_time=0.3)
        self.play(FadeIn(sigma_lbl), run_time=0.3)
        self.play(FadeIn(min_unc_lbl), run_time=0.3)

        # Animate slosh: move the packet
        for pos in positions[1:]:
            new_curve = FunctionGraph(
                lambda x, p=pos: gaussian(x, p, sigma, height=1.4),
                x_range=[-5.5, 5.5], color=TEAL, stroke_width=3
            )
            new_wa = width_arrows(pos)
            self.play(
                Transform(initial_curve, new_curve),
                Transform(wa, new_wa),
                run_time=0.5
            )

        self.play(FadeIn(omega_lbl), run_time=0.3)
        self.wait(dur - 3.8)


# ── B06 Coherent vs Other ─────────────────────────────────────────────────────
class B06_CoherentVsOther(Scene):
    def construct(self):
        dur = DUR.get("B06", 11.0)

        # Left: coherent state
        left_box = Rectangle(width=5.2, height=5.6, color=TEAL, fill_color=TEAL, fill_opacity=0.05).move_to([-3.4, 0.0, 0])
        left_title = Text("coherent state", font=DISPLAY, font_size=17, color=TEAL, weight=BOLD).move_to([-3.4, 2.5, 0])
        left_curve = FunctionGraph(
            lambda x: 1.2 * np.exp(-0.5 * ((x + 3.4) / 0.65) ** 2),
            x_range=[-6.0, -0.8], color=TEAL, stroke_width=3
        )
        left_wa = DoubleArrow([-4.05, 0.7, 0], [-2.75, 0.7, 0], color=TEAL, stroke_width=2,
                              max_tip_length_to_length_ratio=0.15, buff=0)
        left_lbl = Text("σ fixed", font=MONO, font_size=15, color=TEAL).move_to([-3.4, -1.5, 0])

        # Right: excited state (distorted)
        right_box = Rectangle(width=5.2, height=5.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.05).move_to([3.4, 0.0, 0])
        right_title = Text("excited state n=2", font=DISPLAY, font_size=17, color=CRIMSON, weight=BOLD).move_to([3.4, 2.5, 0])
        # n=2 Hermite-Gauss: (2x²−1)² * Gaussian — simplified two-hump shape
        right_curve = FunctionGraph(
            lambda x: 0.9 * (2 * ((x - 3.4) / 0.8) ** 2 - 1) ** 2 * np.exp(-((x - 3.4) / 0.8) ** 2) * 0.5,
            x_range=[0.8, 6.0], color=CRIMSON, stroke_width=3
        )
        right_lbl = Text("σ not fixed, shape distorts", font=MONO, font_size=13, color=CRIMSON).move_to([3.4, -1.5, 0])

        # Divider
        div = Line([0, -2.8, 0], [0, 2.8, 0], color=INK, stroke_width=1, stroke_opacity=0.3)

        # Extra geometric objects for variety
        left_dot = Dot([-3.4, 0.0, 0], color=TEAL, radius=0.09)
        right_dot = Dot([3.4, 0.1, 0], color=CRIMSON, radius=0.09)
        right_dot2 = Dot([2.7, 0.3, 0], color=CRIMSON, radius=0.07)
        check_line = Line([-4.8, -2.0, 0], [-2.0, -2.0, 0], color=TEAL, stroke_width=2)
        cross_line1 = Line([2.0, -1.8, 0], [4.8, -2.2, 0], color=CRIMSON, stroke_width=2)

        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.4)
        self.play(FadeIn(left_title), FadeIn(right_title), run_time=0.35)
        self.play(Create(div), run_time=0.2)
        self.play(Create(left_curve), run_time=0.4)
        self.play(Create(right_curve), run_time=0.4)
        self.play(Create(left_wa), FadeIn(left_dot), run_time=0.3)
        self.play(FadeIn(right_dot), FadeIn(right_dot2), run_time=0.25)
        self.play(Create(check_line), run_time=0.25)
        self.play(Create(cross_line1), run_time=0.25)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.35)
        self.wait(dur - 3.13)


# ── B07 Classical Analogy ─────────────────────────────────────────────────────
class B07_ClassicalAnalogy(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)

        # Parabola
        parabola = FunctionGraph(
            lambda x: 0.35 * x ** 2 - 2.0,
            x_range=[-4.5, 4.5],
            color=INK, stroke_width=2.5
        )
        parabola_fill = parabola.copy().set_stroke(opacity=0)

        # Bowl label
        bowl_lbl = Text("harmonic potential V = ½mω²x²", font=MONO, font_size=14, color=INK).move_to([0, 2.8, 0])

        # Classical ball
        ball = Circle(radius=0.22, color=TEAL, fill_color=TEAL, fill_opacity=0.9).move_to([-3.0, 1.15, 0])
        ball_lbl = Text("ball = ⟨x⟩(t)", font=SERIF, font_size=15, color=TEAL, slant=ITALIC).next_to(ball, UP, buff=0.2)

        # Orbit trace line
        orbit_line = Arc(radius=3.0, start_angle=np.pi * 0.85, angle=-np.pi * 0.7,
                         color=TEAL, stroke_width=2, stroke_opacity=0.5)

        # Quantum packet below
        packet_curve = FunctionGraph(
            lambda x: gaussian(x, -3.0, 0.6, height=1.0),
            x_range=[-5.5, 5.5], color=TEAL, stroke_width=3
        )
        packet_lbl = Text("quantum packet width: σ fixed", font=SERIF, font_size=14, color=TEAL, slant=ITALIC).move_to([0, -3.0, 0])
        packet_arrow = Arrow([0, -2.7, 0], [0, -1.5, 0], color=TEAL, stroke_width=2,
                             max_tip_length_to_length_ratio=0.2, buff=0)

        self.play(Create(parabola), FadeIn(bowl_lbl), run_time=0.4)
        self.play(FadeIn(ball), FadeIn(ball_lbl), run_time=0.4)
        self.play(Create(orbit_line), run_time=0.5)
        self.play(ball.animate.move_to([3.0, 1.15, 0]), ball_lbl.animate.move_to([3.8, 1.35, 0]),
                  run_time=0.8, rate_func=there_and_back)
        self.play(Create(packet_curve), run_time=0.4)
        self.play(GrowArrow(packet_arrow), FadeIn(packet_lbl), run_time=0.4)
        self.wait(dur - 2.9)


# ── B08 Laser Coherent ────────────────────────────────────────────────────────
class B08_LaserCoherent(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)

        # Laser box
        laser_box = Rectangle(width=2.2, height=1.0, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.15).move_to([-4.5, 1.0, 0])
        laser_lbl = Text("LASER", font=DISPLAY, font_size=18, color=CRIMSON, weight=BOLD).move_to(laser_box)

        # Beam arrow
        beam = Arrow([-3.4, 1.0, 0], [2.5, 1.0, 0], color=TEAL, stroke_width=4,
                     max_tip_length_to_length_ratio=0.12, buff=0)
        beam_lbl = Text("coherent state", font=SERIF, font_size=16, color=TEAL, slant=ITALIC).move_to([0, 1.55, 0])

        # Glauber citation box
        cite_box = Rectangle(width=7.0, height=1.3, color=SLATE, fill_color=SLATE, fill_opacity=0.08).move_to([0, -0.5, 0])
        cite_lbl = Text("R.J. Glauber, Phys. Rev. 130, 2529 (1963)", font=MONO, font_size=14, color=SLATE).move_to([0, -0.4, 0])
        cite_sub = Text("Nobel Prize in Physics, 2005", font=DISPLAY, font_size=15, color=SLATE).move_to([0, -0.9, 0])

        # Min-unc reminder
        unc_box = Rectangle(width=5.5, height=0.7, color=TEAL, fill_color=TEAL, fill_opacity=0.1).move_to([0, -2.0, 0])
        unc_lbl = Text("σₓσₚ = ℏ/2 at all times", font=MONO, font_size=16, color=TEAL).move_to(unc_box)

        # Non-blurring label
        travel_lbl = Text("doesn't blur over distance", font=SERIF, font_size=15, color=TEAL, slant=ITALIC).move_to([0, -2.8, 0])

        # Extra geometric objects for variety
        laser_end_dot = Dot([2.5, 1.0, 0], color=TEAL, radius=0.1)
        unc_left_dot = Dot([-2.0, -2.0, 0], color=TEAL, radius=0.08)
        unc_right_dot = Dot([2.0, -2.0, 0], color=TEAL, radius=0.08)
        connector = Line([-2.0, -2.0, 0], [2.0, -2.0, 0], color=TEAL, stroke_width=1.2)

        self.play(FadeIn(laser_box), FadeIn(laser_lbl), run_time=0.4)
        self.play(GrowArrow(beam), run_time=0.4)
        self.play(FadeIn(laser_end_dot), FadeIn(beam_lbl), run_time=0.3)
        self.play(FadeIn(cite_box), FadeIn(cite_lbl), run_time=0.35)
        self.play(FadeIn(cite_sub), run_time=0.3)
        self.play(FadeIn(unc_box), FadeIn(unc_lbl), run_time=0.35)
        self.play(FadeIn(unc_left_dot), FadeIn(unc_right_dot), run_time=0.25)
        self.play(Create(connector), run_time=0.25)
        self.play(FadeIn(travel_lbl), run_time=0.3)
        self.wait(dur - 2.93)


# ── B09 Applications ─────────────────────────────────────────────────────────
class B09_Applications(Scene):
    def construct(self):
        dur = DUR.get("B09", 9.0)

        systems = [
            ("laser", -4.5),
            ("optical fiber", 0.0),
            ("quantum optics", 4.5),
        ]

        boxes = VGroup()
        labels = VGroup()
        chip_marks = VGroup()
        dividers = VGroup()
        check_arrows = VGroup()

        for name, x in systems:
            box = Rectangle(width=3.3, height=3.2, color=TEAL, fill_color=TEAL, fill_opacity=0.07).move_to([x, 0.2, 0])
            lbl = Text(name, font=DISPLAY, font_size=15, color=INK, weight=BOLD).move_to([x, 1.55, 0])
            div = Line([x - 1.4, 1.15, 0], [x + 1.4, 1.15, 0], color=TEAL, stroke_width=0.8)
            cs_lbl = Text("coherent state", font=MONO, font_size=13, color=TEAL).move_to([x, 0.4, 0])
            arr = Arrow([x, -0.5, 0], [x, -1.0, 0], color=TEAL, stroke_width=2,
                        max_tip_length_to_length_ratio=0.3, buff=0)
            boxes.add(box)
            labels.add(lbl)
            dividers.add(div)
            chip_marks.add(cs_lbl)
            check_arrows.add(arr)

        title_line = Text("coherent states power all of quantum optics",
                          font=SERIF, font_size=18, color=INK, slant=ITALIC).move_to([0, -2.2, 0])
        underline = Line([-4.2, -2.5, 0], [4.2, -2.5, 0], color=TEAL, stroke_width=1.5)

        # Additional geometric variety
        corner_dots = VGroup()
        for name, x in systems:
            d = Dot([x - 1.3, -1.2, 0], color=TEAL, radius=0.07)
            corner_dots.add(d)

        self.play(Create(boxes), run_time=0.4)
        self.play(FadeIn(labels), run_time=0.35)
        self.play(Create(dividers), run_time=0.3)
        self.play(FadeIn(chip_marks), run_time=0.35)
        self.play(*[GrowArrow(a) for a in check_arrows], run_time=0.4)
        self.play(FadeIn(corner_dots), run_time=0.25)
        self.play(FadeIn(title_line), run_time=0.3)
        self.play(Create(underline), run_time=0.25)
        self.wait(dur - 2.6)


# ── B10 Recap Card ────────────────────────────────────────────────────────────
class B10_RecapCard(Scene):
    def construct(self):
        dur = DUR.get("B10", 9.0)
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, 1.8, 0])
        recap = Text(
            "Free packet: spreads.\nCoherent state: sigma_x sigma_p = hbar/2, always.\nClassical orbit, quantum width locked.",
            font=SERIF, font_size=17, color=INK, line_spacing=1.5
        ).move_to([0, 0.0, 0])
        self.play(GrowFromCenter(chip), run_time=0.4)
        self.play(FadeIn(recap), run_time=0.5)
        self.wait(dur - 0.9)
