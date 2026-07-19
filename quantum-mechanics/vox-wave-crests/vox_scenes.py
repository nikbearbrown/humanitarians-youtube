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


def _gaussian(x, center, sigma):
    return np.exp(-0.5 * ((x - center) / sigma) ** 2)


class B01_PacketIntro(Scene):
    """Cold open: TEAL Gaussian envelope with CRIMSON crests racing through it."""

    def construct(self):
        dur = DUR.get("B01", 9.0)
        # Build wave packet visual: envelope (TEAL filled) + carrier wave (CRIMSON)
        x_vals = np.linspace(-6, 6, 400)
        sigma = 1.2
        k0 = 3.0

        def make_wave(t_offset, center):
            pts = []
            for x in x_vals:
                env = _gaussian(x, center, sigma)
                carrier = np.sin(k0 * x - 2 * t_offset)  # phase velocity = 1
                pts.append([x, env * carrier * 1.5, 0])
            return pts

        def make_envelope(center):
            pts = []
            for x in x_vals:
                pts.append([x, _gaussian(x, center, sigma) * 1.5, 0])
            neg = [[x, -_gaussian(x, center, sigma) * 1.5, 0] for x in reversed(x_vals)]
            return pts + neg

        # Create initial objects
        wave = VMobject(color=CRIMSON, stroke_width=2.5)
        wave.set_points_smoothly([np.array(p) for p in make_wave(0, -3.0)])

        env_fill = VMobject(fill_color=TEAL, fill_opacity=0.3, stroke_width=0)
        env_pts = make_envelope(-3.0)
        env_fill.set_points_smoothly([np.array(p) for p in env_pts])
        env_fill.set_stroke(width=0, opacity=0)

        center_dot = Dot(color=TEAL, radius=0.1).move_to([-3.0, 0, 0])

        self.add(env_fill, wave, center_dot)

        # Animate: envelope moves at v_g=1, crests at v_ph=0.5
        # Over dur seconds, move envelope by dur units, crests drift at half speed
        new_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        new_wave.set_points_smoothly([np.array(p) for p in make_wave(dur * 1.5, -3.0 + dur)])

        new_env_fill = VMobject(fill_color=TEAL, fill_opacity=0.3, stroke_width=0)
        new_env_pts = make_envelope(-3.0 + dur)
        new_env_fill.set_points_smoothly([np.array(p) for p in new_env_pts])
        new_env_fill.set_stroke(width=0, opacity=0)

        new_dot = Dot(color=TEAL, radius=0.1).move_to([-3.0 + dur, 0, 0])

        self.play(
            Transform(wave, new_wave),
            Transform(env_fill, new_env_fill),
            center_dot.animate.shift(RIGHT * dur),
            run_time=dur * 0.85,
            rate_func=linear
        )
        self.wait(dur * 0.15)


class B02_ClassicalPulse(Scene):
    """Classical pulse where wiggles are locked to envelope — no separation."""

    def construct(self):
        dur = DUR.get("B02", 8.0)
        x_vals = np.linspace(-6, 6, 300)

        def make_classical(center):
            pts = []
            for x in x_vals:
                env = np.exp(-0.5 * ((x - center) / 1.0) ** 2)
                # classical: wave locked to envelope
                carrier = np.sin(3.0 * (x - center))
                pts.append([x, env * carrier * 1.5, 0])
            return pts

        pulse = VMobject(color=SLATE, stroke_width=2.5)
        pulse.set_points_smoothly([np.array(p) for p in make_classical(-2.5)])

        # A dot that stays ON a specific crest and moves WITH the pulse
        crest_dot = Dot(color=INK, radius=0.12).move_to([-2.5, 1.5, 0])

        label = Text("classical pulse", font=DISPLAY, color=INK, font_size=22).move_to([0, -2.5, 0])
        label_sub = Text("wiggles travel with the blob", font=SERIF, color=INK, font_size=20,
                         slant=ITALIC).next_to(label, DOWN, buff=0.15)

        self.add(pulse, crest_dot)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(label_sub, shift=UP * 0.2), run_time=0.5)

        new_pulse = VMobject(color=SLATE, stroke_width=2.5)
        new_pulse.set_points_smoothly([np.array(p) for p in make_classical(2.5)])

        self.play(
            Transform(pulse, new_pulse),
            crest_dot.animate.move_to([2.5, 1.5, 0]),
            run_time=dur * 0.7,
            rate_func=linear
        )
        self.wait(dur * 0.15)


class B03_QuestionCard(Scene):
    """THE QUESTION: why do crests run at twice the packet speed?"""

    def construct(self):
        dur = DUR.get("B03", 11.0)
        title = Text(
            "Why do the crests inside a quantum packet\nrace at twice the speed of the packet itself?",
            font=DISPLAY, color=INK, font_size=26, line_spacing=1.3
        ).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=22).move_to([0, -2.2, 0])

        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)


class B04_PacketBuild(Scene):
    """Superposition of component waves building the packet."""

    def construct(self):
        dur = DUR.get("B04", 9.0)
        x_vals = np.linspace(-5, 5, 300)

        def sine_wave(k, amp=0.5, y_offset=0):
            pts = [np.array([x, amp * np.sin(k * x) + y_offset, 0]) for x in x_vals]
            return pts

        def make_packet(y_offset=0):
            pts = [np.array([x, 1.2 * np.exp(-0.5 * (x / 1.2) ** 2) * np.sin(3.0 * x) + y_offset, 0])
                   for x in x_vals]
            return pts

        # Three component waves stacked
        wave1 = VMobject(color=TEAL, stroke_width=2).set_points_smoothly(sine_wave(2.5, 0.45, 2.0))
        wave2 = VMobject(color=TEAL, stroke_width=2).set_points_smoothly(sine_wave(3.0, 0.45, 0.0))
        wave3 = VMobject(color=TEAL, stroke_width=2).set_points_smoothly(sine_wave(3.5, 0.45, -2.0))

        label_top = SerifLabel("k = 2.5", accent=TEAL, size=22).move_to([5.5, 2.0, 0])
        label_mid = SerifLabel("k = 3.0", accent=TEAL, size=22).move_to([5.5, 0.0, 0])
        label_bot = SerifLabel("k = 3.5", accent=TEAL, size=22).move_to([5.5, -2.0, 0])

        self.play(
            Create(wave1), Create(wave2), Create(wave3),
            run_time=dur * 0.4
        )
        self.play(
            FadeIn(label_top), FadeIn(label_mid), FadeIn(label_bot),
            run_time=0.4
        )
        self.wait(0.5)

        # Collapse to packet
        packet = VMobject(color=TEAL, stroke_width=2.5)
        packet.set_points_smoothly(make_packet(0))

        env_fill = VMobject(fill_color=TEAL, fill_opacity=0.25, stroke_width=0)
        env_pts = []
        for x in x_vals:
            env_pts.append(np.array([x, 1.2 * np.exp(-0.5 * (x / 1.2) ** 2), 0]))
        for x in reversed(x_vals):
            env_pts.append(np.array([x, -1.2 * np.exp(-0.5 * (x / 1.2) ** 2), 0]))
        env_fill.set_points_smoothly(env_pts)
        env_fill.set_stroke(width=0, opacity=0)

        annotation = SerifLabel("many wavelengths added", accent=TEAL, size=24).move_to([0, -2.8, 0])

        self.play(
            Transform(wave1, packet),
            FadeOut(wave2), FadeOut(wave3),
            FadeOut(label_top), FadeOut(label_mid), FadeOut(label_bot),
            run_time=dur * 0.4
        )
        self.play(FadeIn(env_fill), FadeIn(annotation), run_time=0.5)
        self.wait(0.3)


class B05_ComponentSpeeds(Scene):
    """Three component waves with speed arrows showing different velocities."""

    def construct(self):
        dur = DUR.get("B05", 10.0)
        x_vals = np.linspace(-4, 4, 200)

        def short_wave(y):
            return [np.array([x, 0.5 * np.sin(5 * x) + y, 0]) for x in x_vals]

        def mid_wave(y):
            return [np.array([x, 0.5 * np.sin(3 * x) + y, 0]) for x in x_vals]

        def long_wave(y):
            return [np.array([x, 0.5 * np.sin(1.8 * x) + y, 0]) for x in x_vals]

        w_top = VMobject(color=TEAL, stroke_width=2.5).set_points_smoothly(short_wave(2.2))
        w_mid = VMobject(color=TEAL, stroke_width=2.2).set_points_smoothly(mid_wave(0.0))
        w_bot = VMobject(color=TEAL, stroke_width=2.0).set_points_smoothly(long_wave(-2.2))

        # Velocity arrows — top longest, bottom shortest
        arr_top = Arrow(start=[4.5, 2.2, 0], end=[6.3, 2.2, 0],
                        color=CRIMSON, stroke_width=3, buff=0)
        arr_mid = Arrow(start=[4.5, 0.0, 0], end=[5.7, 0.0, 0],
                        color=CRIMSON, stroke_width=3, buff=0)
        arr_bot = Arrow(start=[4.5, -2.2, 0], end=[5.2, -2.2, 0],
                        color=CRIMSON, stroke_width=3, buff=0)

        lbl_top = Text("short wavelength,\nhigher speed", font=SERIF, color=INK,
                       font_size=18, slant=ITALIC).move_to([-4.5, 2.2, 0])
        lbl_bot = Text("long wavelength,\nlower speed", font=SERIF, color=INK,
                       font_size=18, slant=ITALIC).move_to([-4.5, -2.2, 0])

        self.play(Create(w_top), Create(w_mid), Create(w_bot), run_time=dur * 0.35)
        self.play(
            GrowArrow(arr_top), GrowArrow(arr_mid), GrowArrow(arr_bot),
            FadeIn(lbl_top), FadeIn(lbl_bot),
            run_time=dur * 0.4
        )
        self.wait(dur * 0.25)


class B06_PhaseDef(Scene):
    """Single CRIMSON sine wave; one crest tracked with velocity arrow labeled 'phase velocity'."""

    def construct(self):
        dur = DUR.get("B06", 10.0)
        x_vals = np.linspace(-6, 6, 300)
        k = 2.5

        def wave_at(t):
            return [np.array([x, 1.0 * np.sin(k * x - k * 0.5 * t), 0]) for x in x_vals]

        wave = VMobject(color=CRIMSON, stroke_width=2.5)
        wave.set_points_smoothly(wave_at(0))

        # Crest starts at x where sin=1: x_crest = pi/2/k at t=0
        x0_crest = np.pi / (2 * k)
        crest_dot = Dot(color=CRIMSON, radius=0.13).move_to([x0_crest, 1.0, 0])

        lbl_phase = Text("phase velocity", font=DISPLAY, color=CRIMSON, font_size=24).move_to([0, 2.5, 0])
        mono_val = Text("= p / 2m", font=MONO, color=INK, font_size=28).next_to(lbl_phase, DOWN, buff=0.2)

        self.add(wave, crest_dot)
        self.play(FadeIn(lbl_phase, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(mono_val, shift=DOWN * 0.3), run_time=0.5)

        t_end = dur * 0.65
        new_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        new_wave.set_points_smoothly(wave_at(t_end))
        x1_crest = x0_crest + 0.5 * t_end

        # Arrow showing crest movement
        arr = Arrow(start=[x0_crest, -1.5, 0], end=[min(x1_crest, 5.5), -1.5, 0],
                    color=CRIMSON, stroke_width=2.5, buff=0)
        arr_lbl = SerifLabel("crest moves here", accent=CRIMSON, size=20).next_to(arr, DOWN, buff=0.1)

        self.play(
            Transform(wave, new_wave),
            crest_dot.animate.move_to([min(x1_crest, 5.5), 1.0, 0]),
            GrowArrow(arr),
            run_time=t_end * 0.8,
            rate_func=linear
        )
        self.play(FadeIn(arr_lbl), run_time=0.4)
        self.wait(0.4)


class B07_TwoArrows(Scene):
    """TEAL envelope blob + two velocity arrows: TEAL (group) and CRIMSON (phase) at 2:1 ratio."""

    def construct(self):
        dur = DUR.get("B07", 10.0)
        x_vals = np.linspace(-5, 5, 250)

        # Envelope blob (TEAL)
        env_pts = []
        for x in x_vals:
            env_pts.append(np.array([x - 1, 1.2 * np.exp(-0.5 * (x / 1.2) ** 2), 0]))
        for x in reversed(x_vals):
            env_pts.append(np.array([x - 1, -1.2 * np.exp(-0.5 * (x / 1.2) ** 2), 0]))
        env_blob = VMobject(fill_color=TEAL, fill_opacity=0.35, stroke_color=TEAL, stroke_width=1.5)
        env_blob.set_points_smoothly(env_pts)

        center_label = SerifLabel("envelope\n(the particle)", accent=TEAL, size=22).move_to([-1, -2.0, 0])

        # Two arrows from center, right
        arr_group = Arrow(start=[-1, 0.3, 0], end=[2.6, 0.3, 0],
                          color=TEAL, stroke_width=4, buff=0)
        arr_phase = Arrow(start=[-1, -0.3, 0], end=[0.8, -0.3, 0],
                          color=CRIMSON, stroke_width=4, buff=0)

        lbl_g = Text("group velocity = p/m", font=DISPLAY, color=TEAL, font_size=22).move_to([3.8, 0.3, 0])
        lbl_p = Text("phase velocity = p/2m", font=DISPLAY, color=CRIMSON, font_size=22).move_to([3.0, -0.3, 0])

        # bracket showing 2:1
        brace_label = Text("2 : 1", font=MONO, color=INK, font_size=28).move_to([5.5, 0, 0])

        self.play(FadeIn(env_blob), FadeIn(center_label), run_time=0.6)
        self.play(GrowArrow(arr_group), FadeIn(lbl_g), run_time=0.6)
        self.play(GrowArrow(arr_phase), FadeIn(lbl_p), run_time=0.6)
        self.play(FadeIn(brace_label, scale=1.2), run_time=0.5)
        self.wait(dur - 2.3)


class B08_CrestsThrough(Scene):
    """TEAL envelope advancing; CRIMSON crests appear at rear, travel through, vanish at front."""

    def construct(self):
        dur = DUR.get("B08", 9.0)
        x_vals = np.linspace(-7, 7, 400)
        sigma = 1.3
        center0 = -2.5
        v_group = 1.2
        v_phase = 0.6

        def wave_at(t):
            c = center0 + v_group * t
            pts = []
            for x in x_vals:
                env = np.exp(-0.5 * ((x - c) / sigma) ** 2)
                carrier = np.sin(3.0 * x - v_phase * 3.0 * t * 2)
                pts.append(np.array([x, env * carrier * 1.4, 0]))
            return pts

        def env_at(t):
            c = center0 + v_group * t
            pts = []
            for x in x_vals:
                pts.append(np.array([x, 1.4 * np.exp(-0.5 * ((x - c) / sigma) ** 2), 0]))
            for x in reversed(x_vals):
                pts.append(np.array([x, -1.4 * np.exp(-0.5 * ((x - c) / sigma) ** 2), 0]))
            return pts

        wave = VMobject(color=CRIMSON, stroke_width=2.5)
        wave.set_points_smoothly(wave_at(0))
        env = VMobject(fill_color=TEAL, fill_opacity=0.25, stroke_width=0)
        env.set_points_smoothly(env_at(0))
        env.set_stroke(width=0, opacity=0)

        # Labels for crest birth/death zones
        rear_lbl = LabelChip("born here", accent=CRIMSON, size=18).move_to([-4.0, -2.2, 0])
        front_lbl = LabelChip("die here", accent=TEAL, size=18).move_to([1.0, -2.2, 0])

        self.add(env, wave)
        self.play(FadeIn(rear_lbl), FadeIn(front_lbl), run_time=0.5)

        t_end = dur * 0.7
        new_wave = VMobject(color=CRIMSON, stroke_width=2.5)
        new_wave.set_points_smoothly(wave_at(t_end))
        new_env = VMobject(fill_color=TEAL, fill_opacity=0.25, stroke_width=0)
        new_env.set_points_smoothly(env_at(t_end))
        new_env.set_stroke(width=0, opacity=0)
        new_rear = LabelChip("born here", accent=CRIMSON, size=18).move_to(
            [max(-6.3, -4.0 + v_group * t_end), -2.2, 0])
        new_front = LabelChip("die here", accent=TEAL, size=18).move_to(
            [min(6.3, 1.0 + v_group * t_end), -2.2, 0])

        self.play(
            Transform(wave, new_wave),
            Transform(env, new_env),
            Transform(rear_lbl, new_rear),
            Transform(front_lbl, new_front),
            run_time=t_end,
            rate_func=linear
        )
        self.wait(dur * 0.2)


class B10_OceanAnalogy(Scene):
    """Ocean wave group: slow group (TEAL region), fast individual crests (CRIMSON markers)."""

    def construct(self):
        dur = DUR.get("B10", 9.0)
        x_vals = np.linspace(-6, 6, 300)

        def ocean_wave(t, v_g=0.5, v_ph=1.2):
            c = -2.0 + v_g * t
            pts = []
            for x in x_vals:
                env = np.exp(-0.5 * ((x - c) / 2.0) ** 2)
                carrier = np.sin(2.5 * x - v_ph * t * 2.5)
                pts.append(np.array([x, env * 1.2 * carrier + (-2.5), 0]))
            return pts

        def make_sea_floor():
            return [np.array([x, -3.5, 0]) for x in x_vals]

        sea_floor = VMobject(color=SLATE, stroke_width=1.5)
        sea_floor.set_points_smoothly(make_sea_floor())
        sea_fill = Rectangle(width=13, height=1, color=SLATE, fill_opacity=0.2, stroke_width=0)
        sea_fill.move_to([0, -3.8, 0])

        wave = VMobject(color=TEAL, stroke_width=2.5)
        wave.set_points_smoothly(ocean_wave(0))

        # Envelope region indicator
        env_box = Rectangle(width=3.5, height=2.2, color=TEAL, fill_opacity=0.15, stroke_width=1.5)
        env_box.move_to([-2.0, -2.0, 0])
        env_lbl = SerifLabel("group\n(energy)", accent=TEAL, size=20).move_to([-4.5, 0.3, 0])

        crest_dot = Dot(color=CRIMSON, radius=0.13).move_to([-2.5, -2.5 + 0.5, 0])
        crest_arr = Arrow(start=[-2.5, -1.1, 0], end=[-0.8, -1.1, 0],
                          color=CRIMSON, stroke_width=2.5, buff=0)
        crest_lbl = SerifLabel("crest speed", accent=CRIMSON, size=20).move_to([1.5, 0.3, 0])

        self.add(sea_fill, sea_floor, wave, env_box)
        self.play(
            FadeIn(env_lbl), FadeIn(crest_dot), GrowArrow(crest_arr), FadeIn(crest_lbl),
            run_time=0.8
        )

        t_end = dur * 0.65
        new_wave = VMobject(color=TEAL, stroke_width=2.5)
        new_wave.set_points_smoothly(ocean_wave(t_end))
        new_env_box = Rectangle(width=3.5, height=2.2, color=TEAL,
                                fill_opacity=0.15, stroke_width=1.5)
        new_env_box.move_to([-2.0 + 0.5 * t_end, -2.0, 0])
        new_dot = Dot(color=CRIMSON, radius=0.13).move_to(
            [-2.5 + 1.2 * t_end, -2.5 + 0.5, 0])

        self.play(
            Transform(wave, new_wave),
            Transform(env_box, new_env_box),
            crest_dot.animate.move_to([-2.5 + 1.2 * t_end, -2.5 + 0.5, 0]),
            run_time=t_end * 0.8,
            rate_func=linear
        )
        self.wait(dur * 0.15)


class B11_Implication(Scene):
    """TEAL envelope + CRIMSON crests; two SerifLabels: 'particle here' vs 'phase only'."""

    def construct(self):
        dur = DUR.get("B11", 9.0)
        x_vals = np.linspace(-5, 5, 250)

        env_pts = []
        for x in x_vals:
            env_pts.append(np.array([x, 1.5 * np.exp(-0.5 * (x / 1.3) ** 2), 0]))
        for x in reversed(x_vals):
            env_pts.append(np.array([x, -1.5 * np.exp(-0.5 * (x / 1.3) ** 2), 0]))

        env_blob = VMobject(fill_color=TEAL, fill_opacity=0.35, stroke_color=TEAL, stroke_width=2)
        env_blob.set_points_smoothly(env_pts)

        carrier_pts = [np.array([x, 1.5 * np.exp(-0.5 * (x / 1.3) ** 2) * np.sin(3 * x), 0])
                       for x in x_vals]
        carrier = VMobject(color=CRIMSON, stroke_width=2.5)
        carrier.set_points_smoothly(carrier_pts)

        # Labels
        particle_lbl = SerifLabel("particle here", accent=TEAL, size=26).move_to([0, 2.5, 0])
        # Arrow from label down to envelope
        particle_arr = Arrow(start=[0, 2.1, 0], end=[0, 1.5, 0], color=TEAL,
                             stroke_width=2, buff=0.05)

        phase_lbl = SerifLabel("phase only", accent=CRIMSON, size=26).move_to([2.8, -2.2, 0])
        # Arrow from label up to a crest
        phase_arr = Arrow(start=[2.0, -1.9, 0], end=[1.2, -0.5, 0], color=CRIMSON,
                          stroke_width=2, buff=0.05)

        # Strike through "phase only" label to show it's excluded from physical meaning
        strike = Line(
            phase_lbl.get_left() + LEFT * 0.1,
            phase_lbl.get_right() + RIGHT * 0.1,
            color=CRIMSON, stroke_width=2.5
        )

        self.play(FadeIn(env_blob), Create(carrier), run_time=0.6)
        self.play(FadeIn(particle_lbl), GrowArrow(particle_arr), run_time=0.5)
        self.play(FadeIn(phase_lbl), GrowArrow(phase_arr), run_time=0.5)
        self.play(Create(strike), run_time=0.4)
        self.wait(dur - 2.0)


class B12_ExampleTrace(Scene):
    """Illustrative example: p=1, v_g=1, v_ph=0.5. Timeline showing blob vs crest positions."""

    def construct(self):
        dur = DUR.get("B12", 14.0)
        # Timeline axis
        axis = Line([-5.5, -1.5, 0], [5.5, -1.5, 0], color=INK, stroke_width=2)
        tick0 = Line([0, -1.7, 0], [0, -1.3, 0], color=INK, stroke_width=1.5)
        tick1 = Line([3.5, -1.7, 0], [3.5, -1.3, 0], color=INK, stroke_width=1.5)
        lbl0 = Text("x = 0", font=MONO, color=INK, font_size=20).move_to([0, -2.0, 0])
        lbl1 = Text("x = 1 unit", font=MONO, color=INK, font_size=20).move_to([3.5, -2.0, 0])
        t_label = Text("illustrative", font=SERIF, color=INK, font_size=18, slant=ITALIC).move_to([-4.5, 3.3, 0])

        # t=0 state
        x_vals = np.linspace(-5, 5, 200)
        env0_pts = []
        for x in x_vals:
            env0_pts.append(np.array([x, 1.3 * np.exp(-0.5 * (x / 1.0) ** 2) + 1.5, 0]))
        for x in reversed(x_vals):
            env0_pts.append(np.array([x, -1.3 * np.exp(-0.5 * (x / 1.0) ** 2) + 1.5, 0]))

        env_t0 = VMobject(fill_color=TEAL, fill_opacity=0.3, stroke_color=TEAL, stroke_width=1.5)
        env_t0.set_points_smoothly(env0_pts)

        crest_dot_t0 = Dot(color=CRIMSON, radius=0.13).move_to([0, 1.5 + 1.3, 0])
        crest_lbl_t0 = Text("crest at x=0\n(t=0)", font=MONO, color=CRIMSON, font_size=18).move_to([0, 3.3, 0])

        # Label the two velocities
        vg_lbl = Text("v_group = 1", font=MONO, color=TEAL, font_size=22).move_to([-4.5, 0.5, 0])
        vp_lbl = Text("v_phase = 0.5", font=MONO, color=CRIMSON, font_size=22).move_to([-4.5, -0.0, 0])

        self.play(
            Create(axis), FadeIn(tick0), FadeIn(tick1), FadeIn(lbl0), FadeIn(lbl1),
            FadeIn(t_label),
            run_time=0.8
        )
        self.play(FadeIn(env_t0), FadeIn(crest_dot_t0), FadeIn(crest_lbl_t0), run_time=0.5)
        self.play(FadeIn(vg_lbl), FadeIn(vp_lbl), run_time=0.5)
        self.wait(0.5)

        # Animate: move blob by 3.5 units (representing 1 unit), crests by 1.75 units (0.5 unit)
        env1_pts = []
        for x in x_vals:
            env1_pts.append(np.array([x - 3.5, 1.3 * np.exp(-0.5 * (x / 1.0) ** 2) + 1.5, 0]))
        for x in reversed(x_vals):
            env1_pts.append(np.array([x - 3.5, -1.3 * np.exp(-0.5 * (x / 1.0) ** 2) + 1.5, 0]))

        env_t1 = VMobject(fill_color=TEAL, fill_opacity=0.3, stroke_color=TEAL, stroke_width=1.5)
        env_t1.set_points_smoothly(env1_pts)

        # Place final labels well-separated: blob at far right, crest halfway, neither overlapping t=0 label
        blob_final_lbl = Text("blob at x=1\n(t=1)", font=MONO, color=TEAL, font_size=18).move_to([4.5, 3.3, 0])
        crest_final_lbl = Text("crest at x=0.5\n(t=1)", font=MONO, color=CRIMSON, font_size=18).move_to([1.75, -0.5, 0])

        self.play(
            Transform(env_t0, env_t1),
            crest_dot_t0.animate.move_to([1.75, 1.5 + 1.3, 0]),
            run_time=dur * 0.45,
            rate_func=smooth
        )
        self.play(
            FadeIn(blob_final_lbl), FadeIn(crest_final_lbl),
            run_time=0.5
        )
        self.wait(dur * 0.2)


class B13_RecapCard(Scene):
    """RECAP endcard: answer in one line + QUANTUM MECHANICS kicker."""

    def construct(self):
        dur = DUR.get("B13", 9.0)
        answer = Text(
            "The crests run at half-speed —\nthe packet runs at full speed.",
            font=DISPLAY, color=INK, font_size=36, line_spacing=1.3
        ).move_to([0, 0.5, 0])
        chip = LabelChip("QUANTUM MECHANICS", accent=TEAL, size=24).move_to([0, -2.0, 0])

        self.play(FadeIn(answer, shift=UP * 0.3), run_time=1.0)
        self.play(GrowFromCenter(chip), run_time=0.6)
        self.wait(dur - 1.8)
