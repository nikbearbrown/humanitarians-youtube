"""vox_scenes.py — The Shrinking Arrow: How Quantum Becomes Classical
(vox-bloch-decoherence, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B05 and B14 are STILL·ai — no scene (compile as slates).
B01, B04, B06, B09, B11, B16, B17 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = quantum / pure / surface of Bloch ball;
crimson #BF3339 = classical / mixed / center / decohered.
Never swap mid-film.

Exclusions: NO Lindblad equation, NO T2=1/(2T1)+1/Tphi algebra, NO jump operators.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 11.0, "B03": 10.0, "B04": 10.0,
    "B05": 12.0, "B06": 5.0,  "B07": 12.0, "B08": 13.0,
    "B09": 4.0,  "B10": 11.0, "B11": 5.0,  "B12": 12.0,
    "B13": 11.0, "B14": 11.0, "B15": 13.0, "B16": 9.0, "B17": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- helpers ---------------------------------------------------------------

def _bloch_circle(radius=2.2, accent=TEAL):
    """A 2D Bloch sphere cross-section (circle with poles)."""
    circ = Circle(radius=radius)
    circ.set_stroke(accent, 2.5).set_fill(GROUND, 0)
    top = Dot(radius=0.08, color=INK).move_to(UP * radius)
    bot = Dot(radius=0.08, color=INK).move_to(DOWN * radius)
    top_lbl = Text("|0>", font=MONO, color=INK, font_size=22)
    top_lbl.next_to(top, UP, buff=0.12)
    bot_lbl = Text("|1>", font=MONO, color=INK, font_size=22)
    bot_lbl.next_to(bot, DOWN, buff=0.12)
    return VGroup(circ, top, bot, top_lbl, bot_lbl)


def _bloch_arrow(length=2.2, angle_deg=45, accent=TEAL):
    """An arrow from center at given angle (from +x axis), given length."""
    angle = angle_deg * DEGREES
    tip = np.array([length * np.cos(angle), length * np.sin(angle), 0])
    arr = Arrow(ORIGIN, tip, color=accent, stroke_width=4,
                buff=0, tip_length=0.22)
    return arr


# ---- scenes ----------------------------------------------------------------

class B02_BlochIntro(Scene):
    def construct(self):
        total = DUR["B02"]

        bloch = _bloch_circle(radius=2.0, accent=TEAL)
        bloch.move_to(LEFT * 1.5)

        # Arrow pointing to the surface at ~45 degrees
        arr = Arrow(LEFT * 1.5, LEFT * 1.5 + np.array([1.42, 1.42, 0]),
                    color=TEAL, stroke_width=4, buff=0, tip_length=0.22)

        surface_lbl = SerifLabel("pure — superposition", accent=TEAL, size=26)
        surface_lbl.move_to(RIGHT * 3.2 + UP * 1.6)

        # Center dot (classical)
        center_dot = Dot(radius=0.15, color=CRIMSON)
        center_dot.move_to(LEFT * 1.5)
        classical_lbl = SerifLabel("classical coin", accent=CRIMSON, size=26)
        classical_lbl.move_to(RIGHT * 3.2 + DOWN * 0.2)

        eyebrow = Text("THE BLOCH SPHERE", font=DISPLAY, color=SLATE, font_size=20)
        eyebrow.move_to(UP * 3.2)

        self.play(FadeIn(eyebrow, shift=DOWN * 0.1), run_time=0.4)
        self.play(Create(bloch), run_time=0.8)
        self.play(GrowArrow(arr), run_time=0.7)
        self.play(FadeIn(surface_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(center_dot, scale=1.4), run_time=0.4)
        self.play(FadeIn(classical_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 3.3))


class B03_Precession(Scene):
    def construct(self):
        total = DUR["B03"]

        bloch = _bloch_circle(radius=2.0, accent=TEAL)
        bloch.move_to(LEFT * 1.5)

        # Arrow pointing to surface
        arr = Arrow(LEFT * 1.5, LEFT * 1.5 + np.array([1.42, 1.42, 0]),
                    color=TEAL, stroke_width=4, buff=0, tip_length=0.22)

        # Dashed arc suggesting precession orbit around z-axis (top)
        arc_pts = []
        for i in range(40):
            angle = (np.pi * 0.25) + (i / 39) * (np.pi * 1.5)
            r = 1.95
            arc_pts.append(LEFT * 1.5 + np.array([r * np.cos(angle), r * np.sin(angle), 0]))
        orbit_arc = DashedVMobject(
            VMobject(color=TEAL, stroke_width=2).set_points_smoothly(arc_pts),
            num_dashes=18
        )

        prec_lbl = SerifLabel("free precession — stays quantum", accent=TEAL, size=25)
        prec_lbl.move_to(RIGHT * 2.8 + UP * 0.2)

        self.play(Create(bloch), GrowArrow(arr), run_time=0.8)
        self.play(Create(orbit_arc), run_time=0.9)
        self.play(arr.animate.shift(LEFT * 0.4 + UP * 0.3), run_time=0.6)
        self.play(FadeIn(prec_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


class B07_Branching(Scene):
    def construct(self):
        total = DUR["B07"]

        # Bloch circle on left
        bloch = _bloch_circle(radius=1.5, accent=TEAL)
        bloch.move_to(LEFT * 4.5)

        # Central node (qubit)
        node = Dot(radius=0.15, color=INK).move_to(LEFT * 0.2)

        # Two branches forking right
        branch0 = Line(LEFT * 0.2, RIGHT * 2.5 + UP * 1.4,
                       color=TEAL, stroke_width=3)
        branch1 = Line(LEFT * 0.2, RIGHT * 2.5 + DOWN * 1.4,
                       color=TEAL, stroke_width=3)

        lbl0 = Text("|0> branch", font=MONO, color=TEAL, font_size=24)
        lbl0.move_to(RIGHT * 3.6 + UP * 1.4)
        lbl1 = Text("|1> branch", font=MONO, color=TEAL, font_size=24)
        lbl1.move_to(RIGHT * 3.6 + DOWN * 1.4)

        # Overlap bracket between endpoint tips
        bracket_line = Line(RIGHT * 2.5 + UP * 1.4, RIGHT * 2.5 + DOWN * 1.4,
                            color=SLATE, stroke_width=2.5)
        overlap_lbl = Text("overlap", font=MONO, color=SLATE, font_size=22)
        overlap_lbl.next_to(bracket_line, RIGHT, buff=0.22)

        arrow_length_note = SerifLabel("arrow length = overlap", accent=TEAL, size=24)
        arrow_length_note.move_to(DOWN * 2.6)

        env_lbl = LabelChip("ENVIRONMENT", accent=SLATE, size=22)
        env_lbl.move_to(LEFT * 4.5 + DOWN * 2.8)

        self.play(Create(bloch), FadeIn(node), run_time=0.7)
        self.play(FadeIn(env_lbl, scale=0.88), run_time=0.4)
        self.play(Create(branch0), Create(branch1), run_time=0.8)
        self.play(FadeIn(lbl0), FadeIn(lbl1), run_time=0.5)
        self.play(Create(bracket_line), FadeIn(overlap_lbl), run_time=0.5)
        self.play(FadeIn(arrow_length_note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


class B08_ArrowShrinks(Scene):
    def construct(self):
        total = DUR["B08"]

        # Bloch circle
        bloch = _bloch_circle(radius=2.1, accent=TEAL)
        bloch.move_to(LEFT * 2.0)

        # Arrow at full length to surface
        arr_tip = LEFT * 2.0 + np.array([1.49, 1.49, 0])
        arr = Arrow(LEFT * 2.0, arr_tip, color=TEAL, stroke_width=4,
                    buff=0, tip_length=0.22)

        # Two environment branches starting close together
        b0 = Line(RIGHT * 1.5, RIGHT * 3.8 + UP * 0.6,
                  color=TEAL, stroke_width=2.5)
        b1 = Line(RIGHT * 1.5, RIGHT * 3.8 + DOWN * 0.6,
                  color=TEAL, stroke_width=2.5)
        node_env = Dot(radius=0.12, color=SLATE).move_to(RIGHT * 1.5)

        drain_lbl = SerifLabel("coherence drains", accent=CRIMSON, size=26)
        drain_lbl.move_to(LEFT * 2.0 + DOWN * 3.0)

        # Ghost arc (pale) showing original arrow position
        ghost_arc = Arc(radius=2.1, start_angle=PI / 4 - 0.22,
                        angle=0.44, color=TEAL, stroke_width=1.5,
                        stroke_opacity=0.35)
        ghost_arc.move_to(LEFT * 2.0)

        self.play(Create(bloch), GrowArrow(arr), run_time=0.8)
        self.play(FadeIn(node_env), Create(b0), Create(b1), run_time=0.6)

        # Branches spread apart as arrow shrinks
        self.play(
            b0.animate.put_start_and_end_on(RIGHT * 1.5, RIGHT * 3.8 + UP * 1.6),
            b1.animate.put_start_and_end_on(RIGHT * 1.5, RIGHT * 3.8 + DOWN * 1.6),
            arr.animate.scale(0.25, about_point=LEFT * 2.0),
            FadeIn(ghost_arc),
            run_time=2.0
        )
        self.play(FadeIn(drain_lbl, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B10_Center(Scene):
    def construct(self):
        total = DUR["B10"]

        bloch = _bloch_circle(radius=2.1, accent=SLATE)
        bloch.move_to(ORIGIN)

        # Short arrow (shrunk)
        short_arr = Arrow(ORIGIN, UP * 0.55, color=TEAL, stroke_width=3,
                          buff=0, tip_length=0.18)

        # Crimson center dot (endpoint)
        center_dot = Dot(radius=0.2, color=CRIMSON)
        center_dot.move_to(ORIGIN)

        mixed_lbl = Text("maximally mixed", font=SERIF, color=CRIMSON,
                         font_size=30, slant=ITALIC)
        mixed_lbl.move_to(RIGHT * 3.8 + UP * 0.5)

        coin_chip = LabelChip("CLASSICAL COIN", accent=CRIMSON, size=26)
        coin_chip.move_to(RIGHT * 3.8 + DOWN * 0.6)

        equal_lbl = SerifLabel("equal probability — every direction", accent=SLATE, size=22)
        equal_lbl.move_to(DOWN * 3.2)

        self.play(Create(bloch), FadeIn(short_arr), run_time=0.7)
        self.play(ReplacementTransform(short_arr, center_dot), run_time=0.9)
        self.play(FadeIn(mixed_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(coin_chip, scale=0.88), run_time=0.5)
        self.play(FadeIn(equal_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.1))


class B12_T2Decay(Scene):
    def construct(self):
        total = DUR["B12"]

        # Manual axes using Lines (avoids Axes attribute mock issues)
        # Frame: x from -5.5 to 5.5 mapped to t=0..2.2; y from -3.0 to 1.8 mapped to 0..1
        ox, oy = -4.5, -2.8          # origin in scene coords
        ax_w, ax_h = 8.5, 4.0        # width and height in scene units
        t_max = 2.2

        def tx(t):
            return ox + (t / t_max) * ax_w

        def ty(v):
            return oy + v * ax_h

        x_axis = Line([ox, oy, 0], [ox + ax_w + 0.4, oy, 0],
                      color=INK, stroke_width=2)
        y_axis = Line([ox, oy, 0], [ox, oy + ax_h + 0.4, 0],
                      color=INK, stroke_width=2)

        x_lbl = Text("time", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        x_lbl.move_to([ox + ax_w + 0.9, oy, 0])
        y_lbl = Text("coherence", font=SERIF, color=INK, font_size=26, slant=ITALIC)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([ox - 0.9, oy + ax_h / 2, 0])

        # Exponential decay curve
        n_pts = 60
        curve_pts = []
        for i in range(n_pts):
            t = (i / (n_pts - 1)) * t_max
            curve_pts.append([tx(t), ty(np.exp(-t)), 0])
        decay_curve = VMobject(color=TEAL, stroke_width=3)
        decay_curve.set_points_smoothly(curve_pts)

        # Dashed vertical at T2 (t=1)
        t2_x_pos = tx(1)
        t2_y_pos = ty(np.exp(-1))
        t2_line = DashedLine([t2_x_pos, oy, 0], [t2_x_pos, t2_y_pos, 0],
                             color=SLATE, stroke_width=2, dash_length=0.15)
        t2_lbl = Text("T2", font=MONO, color=SLATE, font_size=28)
        t2_lbl.move_to([t2_x_pos, oy - 0.42, 0])

        # Crimson dot at e^-1
        e1_dot = Dot(radius=0.12, color=CRIMSON).move_to([t2_x_pos, t2_y_pos, 0])
        e1_lbl = SerifLabel("coherence = 1/e", accent=CRIMSON, size=22)
        e1_lbl.move_to([tx(1.65), t2_y_pos + 0.32, 0])

        self.play(Create(x_axis), Create(y_axis), FadeIn(x_lbl), FadeIn(y_lbl),
                  run_time=0.7)
        self.play(Create(decay_curve), run_time=1.2)
        self.play(Create(t2_line), FadeIn(t2_lbl), run_time=0.5)
        self.play(FadeIn(e1_dot, scale=1.3), FadeIn(e1_lbl), run_time=0.5)
        self.wait(max(0.5, total - 2.9))


class B13_T2Scale(Scene):
    def construct(self):
        total = DUR["B13"]

        # Title
        title = Text("Coherence times across platforms", font=SERIF, color=INK,
                     font_size=28, slant=ITALIC)
        title.move_to(UP * 3.2)

        # Log-scale spine
        spine = Line(LEFT * 5.8 + UP * 1.2, LEFT * 5.8 + DOWN * 2.2,
                     color=SLATE, stroke_width=2)

        # Three bars (horizontal), ordered top to bottom: transmon, ion, cat
        # "transmon ~200 us" — large teal bar
        bar_w_transmon = 5.5
        bar_transmon = Rectangle(width=bar_w_transmon, height=0.55)
        bar_transmon.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        bar_transmon.move_to(LEFT * 5.8 + RIGHT * bar_w_transmon / 2 + UP * 1.2)

        lbl_transmon = Text("transmon   ~200 us", font=MONO, color=INK,
                            font_size=22)
        lbl_transmon.next_to(bar_transmon, RIGHT, buff=0.22)

        # "trapped ion ~seconds" — larger teal bar
        bar_w_ion = 7.0
        bar_ion = Rectangle(width=bar_w_ion, height=0.55)
        bar_ion.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        bar_ion.move_to(LEFT * 5.8 + RIGHT * bar_w_ion / 2 + DOWN * 0.0)

        lbl_ion = Text("trapped ion   ~seconds", font=MONO, color=INK,
                       font_size=22)
        lbl_ion.next_to(bar_ion, RIGHT, buff=0.22)

        # "cat-sized ~10^-36 s" — tiny crimson bar (barely visible)
        bar_w_cat = 0.6
        bar_cat = Rectangle(width=bar_w_cat, height=0.55)
        bar_cat.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        bar_cat.move_to(LEFT * 5.8 + RIGHT * bar_w_cat / 2 + DOWN * 1.2)

        lbl_cat = Text("cat-sized   ~10^-36 s", font=MONO, color=CRIMSON,
                       font_size=22)
        lbl_cat.move_to(RIGHT * 1.2 + DOWN * 1.2)
        arrow_cat = Arrow(lbl_cat.get_left() + LEFT * 0.1, bar_cat.get_right(),
                          color=CRIMSON, stroke_width=2, tip_length=0.14, buff=0.05)

        self.play(FadeIn(title, shift=DOWN * 0.1), Create(spine), run_time=0.6)
        self.play(FadeIn(bar_transmon, scale=0.88), FadeIn(lbl_transmon), run_time=0.5)
        self.play(FadeIn(bar_ion, scale=0.88), FadeIn(lbl_ion), run_time=0.5)
        self.play(FadeIn(bar_cat, scale=0.88), FadeIn(lbl_cat),
                  GrowArrow(arrow_cat), run_time=0.5)
        self.wait(max(0.5, total - 2.1))


class B15_Example(Scene):
    def construct(self):
        total = DUR["B15"]

        # Left panel: Bloch circle
        bloch = _bloch_circle(radius=1.8, accent=TEAL)
        bloch.move_to(LEFT * 3.8 + UP * 0.5)

        # Arrow at equator (pointing right = |+> state)
        arr = Arrow(LEFT * 3.8 + UP * 0.5, LEFT * 3.8 + UP * 0.5 + RIGHT * 1.8,
                    color=TEAL, stroke_width=4, buff=0, tip_length=0.22)
        start_lbl = Text("start: |+>", font=MONO, color=TEAL, font_size=22)
        start_lbl.next_to(arr.get_tip(), RIGHT, buff=0.18)

        # Divider
        divider = DashedLine(UP * 3.5, DOWN * 3.5, color=SLATE,
                             stroke_width=1.5, dash_length=0.15)
        divider.move_to(ORIGIN)

        # Right panel: timeline bar
        tl_start = RIGHT * 0.6 + DOWN * 0.2
        tl_end = RIGHT * 6.0 + DOWN * 0.2
        timeline = Line(tl_start, tl_end, color=INK, stroke_width=2.5)
        tl_start_lbl = Text("0", font=MONO, color=INK, font_size=22)
        tl_start_lbl.next_to(tl_start, DOWN, buff=0.15)
        tl_end_lbl = Text("200 us", font=MONO, color=CRIMSON, font_size=22)
        tl_end_lbl.next_to(tl_end, DOWN, buff=0.15)

        # Chip at end
        done_chip = LabelChip("T2 DONE", accent=CRIMSON, size=22)
        done_chip.next_to(tl_end, UP, buff=0.28)

        # Timeline cursor that sweeps
        cursor = Line(tl_start, tl_start + UP * 0.45, color=TEAL, stroke_width=3)

        note_lbl = SerifLabel("computation must finish before this", accent=CRIMSON, size=23)
        note_lbl.move_to(RIGHT * 3.3 + DOWN * 1.8)

        self.play(Create(bloch), GrowArrow(arr), FadeIn(start_lbl), run_time=0.8)
        self.play(Create(divider), run_time=0.3)
        self.play(Create(timeline), FadeIn(tl_start_lbl), FadeIn(tl_end_lbl), run_time=0.5)
        self.play(FadeIn(cursor), run_time=0.3)

        # Simultaneous: cursor sweeps right + arrow shrinks to near-zero dot
        center_dot = Dot(radius=0.12, color=CRIMSON).move_to(LEFT * 3.8 + UP * 0.5)
        self.play(
            cursor.animate.put_start_and_end_on(tl_end, tl_end + UP * 0.45),
            ReplacementTransform(arr, center_dot),
            FadeOut(start_lbl),
            run_time=2.5
        )
        self.play(FadeIn(done_chip, scale=0.88), run_time=0.4)
        self.play(FadeIn(note_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 5.3))
