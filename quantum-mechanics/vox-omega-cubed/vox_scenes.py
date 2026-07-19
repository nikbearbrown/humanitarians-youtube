"""vox_scenes.py — Why Spontaneous Emission Never Happens on a Radio Antenna
(vox-omega-cubed, slate cut, 16:9)

Color law: TEAL = fast / optical (high omega, high rate)
           CRIMSON = slow / radio (low omega, low rate)
EXCLUSIONS: no density-of-states derivation, no A-coefficient integral,
            no Einstein B thermodynamics, no laser/stimulated emission detail.
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


def _two_level(center, label, color, excited_y=0.8, ground_y=-0.8, w=1.8):
    """Simple two-level system diagram."""
    gnd = Line(LEFT * w / 2 + RIGHT * center[0],
               RIGHT * w / 2 + RIGHT * center[0],
               color=color, stroke_width=2.5)
    gnd.move_to(np.array([center[0], center[1] + ground_y, 0]))
    exc = Line(LEFT * w / 2 + RIGHT * center[0],
               RIGHT * w / 2 + RIGHT * center[0],
               color=color, stroke_width=2.5)
    exc.move_to(np.array([center[0], center[1] + excited_y, 0]))
    lbl = LabelChip(label, accent=color, size=20)
    lbl.move_to(np.array([center[0], center[1] + excited_y + 0.65, 0]))
    return VGroup(gnd, exc, lbl)


# ── B01: COLD OPEN — hydrogen atom emits in 1 ns ─────────────────────────────
class B01_AtomEmits(Scene):
    def construct(self):
        dur = DUR.get("B01", 9.0)
        title = Text("Hydrogen atom in empty space", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        system = _two_level([0, 0.5, 0], "H atom  (optical)", TEAL)
        dot = Dot(radius=0.14, color=TEAL).move_to(UP * 1.3)
        photon_wave = ArcBetweenPoints(UP * 1.3, UP * 1.3 + RIGHT * 3.5,
                                       angle=-0.8, color=TEAL, stroke_width=3)
        time_lbl = Text("1 nanosecond later...", font=SERIF, font_size=24,
                        color=INK, slant=ITALIC).move_to(DOWN * 2.2)
        result = LabelChip("photon emitted", accent=TEAL, size=24).move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(system), FadeIn(dot), run_time=dur * 0.30)
        self.play(FadeIn(time_lbl), run_time=dur * 0.20)
        self.play(Create(photon_wave), FadeIn(result), run_time=dur * 0.30)
        self.wait(dur * 0.20)


# ── B02: COLD OPEN — NMR proton stable for 30 s ──────────────────────────────
class B02_ProtonStable(Scene):
    def construct(self):
        dur = DUR.get("B02", 9.0)
        title = Text("Proton in 10-tesla NMR magnet", font=DISPLAY,
                     font_size=30, color=INK).move_to(UP * 3.0)
        system = _two_level([0, 0.5, 0], "proton  (radio)", CRIMSON)
        dot = Dot(radius=0.14, color=CRIMSON).move_to(UP * 1.3)
        # Clock ticking: 30 seconds
        # Use single clock label, replaced by FadeOut/FadeIn
        clock_lbl = Text("10 sec  -->  30 sec  -->  still excited",
                         font=SERIF, font_size=24,
                         color=INK, slant=ITALIC).move_to(DOWN * 2.0)
        still_lbl = LabelChip("still excited", accent=CRIMSON, size=24).move_to(DOWN * 3.0)
        same_note = Text("Same vacuum. Same physics.", font=SERIF, font_size=22,
                         color=INK, slant=ITALIC).move_to(DOWN * 3.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(system), FadeIn(dot), run_time=dur * 0.30)
        self.play(FadeIn(clock_lbl), run_time=dur * 0.20)
        self.play(FadeIn(still_lbl), run_time=dur * 0.20)
        self.play(FadeIn(same_note, shift=UP * 0.1), run_time=dur * 0.20)


# ── B03: THE QUESTION — CARD beat, no scene class ────────────────────────────


# ── B04: STILL·ai — same vacuum, both couple identically ─────────────────────
# STILL beat — no scene class


# ── B05: THE PROBLEM — frequency comparison ───────────────────────────────────
class B05_FrequencyGap(Scene):
    def construct(self):
        dur = DUR.get("B05", 9.0)
        # Frequency axis with two markers
        axis = NumberLine(x_range=[0, 10, 2], length=8.5,
                          include_numbers=False, color=INK, stroke_width=2)
        axis.move_to(DOWN * 0.3)
        # Optical (teal) at right end, NMR (crimson) at left
        opt_x = axis.n2p(8.5)
        nmr_x = axis.n2p(0.3)
        opt_dot = Dot(opt_x, radius=0.18, color=TEAL)
        nmr_dot = Dot(nmr_x, radius=0.18, color=CRIMSON)
        opt_lbl = LabelChip("optical  600 THz", accent=TEAL, size=22)
        opt_lbl.next_to(opt_dot, UP, buff=0.35)
        nmr_lbl = LabelChip("NMR  400 MHz", accent=CRIMSON, size=22)
        nmr_lbl.next_to(nmr_dot, UP, buff=0.35)
        freq_lbl = SerifLabel("frequency", INK, size=22).next_to(axis, RIGHT, buff=0.2)
        ratio_lbl = Text("x 1,500,000", font=MONO, font_size=28, color=INK)
        ratio_lbl.move_to(DOWN * 2.2)
        brace = BraceBetweenPoints(nmr_x, opt_x, direction=DOWN)
        self.play(Create(axis), FadeIn(freq_lbl), run_time=0.4)
        self.play(FadeIn(nmr_dot), FadeIn(nmr_lbl), run_time=dur * 0.25)
        self.play(FadeIn(opt_dot), FadeIn(opt_lbl), run_time=dur * 0.25)
        self.play(Create(brace), FadeIn(ratio_lbl), run_time=dur * 0.30)
        self.wait(dur * 0.20)


# ── B06: THE PROBLEM — naive expectation vs reality ──────────────────────────
class B06_NaiveVsReal(Scene):
    def construct(self):
        dur = DUR.get("B06", 9.0)
        naive_lbl = Text("naive: rate", font=SERIF, font_size=26,
                         color=CRIMSON, slant=ITALIC).move_to(LEFT * 3.0 + UP * 1.2)
        naive_val = Text("x 1,500,000", font=MONO, font_size=28,
                         color=CRIMSON).move_to(LEFT * 3.0 + UP * 0.3)
        real_lbl = Text("actual: rate", font=SERIF, font_size=26,
                        color=TEAL, slant=ITALIC).move_to(RIGHT * 3.0 + UP * 1.2)
        real_val = Text("x 10,000,000,000", font=MONO, font_size=26,
                        color=TEAL).move_to(RIGHT * 3.0 + UP * 0.3)
        divider = Line(UP * 2.0, DOWN * 1.8, color=INK, stroke_width=1.5).move_to(ORIGIN)
        q_lbl = Text("rate grows faster than frequency", font=DISPLAY,
                     font_size=24, color=INK).move_to(DOWN * 2.8)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(naive_lbl), FadeIn(naive_val), run_time=dur * 0.30)
        self.play(FadeIn(real_lbl), FadeIn(real_val), run_time=dur * 0.30)
        self.play(FadeIn(q_lbl, shift=UP * 0.2), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B07: THE MECHANISM — golden rule structure ────────────────────────────────
class B07_GoldenRule(Scene):
    def construct(self):
        dur = DUR.get("B07", 10.0)
        title = Text("Fermi's golden rule", font=DISPLAY,
                     font_size=32, color=INK).move_to(UP * 3.0)
        # Rate = matrix element^2 * density of states
        parts = [("Rate  =  ", INK), ("|matrix element|^2", TEAL),
                 ("  x  ", INK), ("density of final states", TEAL)]
        line = VGroup()
        x = -5.2
        for txt, col in parts:
            t = Text(txt, font=MONO, font_size=24, color=col)
            t.move_to(RIGHT * x + t.width / 2 * RIGHT)
            x += t.width + 0.05
            line.add(t)
        line.center()
        mat_lbl = SerifLabel("set by dipole coupling", TEAL, size=20)
        mat_lbl.move_to(LEFT * 2.0 + DOWN * 1.5)
        dos_lbl = SerifLabel("counts available photon modes", TEAL, size=20)
        dos_lbl.move_to(RIGHT * 2.8 + DOWN * 1.5)
        mat_arr = Arrow(mat_lbl.get_top(), LEFT * 2.5 + UP * 0.2,
                        color=TEAL, stroke_width=2, buff=0.05)
        dos_arr = Arrow(dos_lbl.get_top(), RIGHT * 2.2 + UP * 0.2,
                        color=TEAL, stroke_width=2, buff=0.05)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(line), run_time=dur * 0.40)
        self.play(FadeIn(mat_lbl), GrowArrow(mat_arr),
                  FadeIn(dos_lbl), GrowArrow(dos_arr), run_time=dur * 0.40)
        self.wait(dur * 0.20)


# ── B08: THE MECHANISM — omega^2 from density of states + one more omega ──────
class B08_OmegaSquaredPlus(Scene):
    def construct(self):
        dur = DUR.get("B08", 10.0)
        title = Text("Why the rate grows faster than omega", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        # Two contributions stacked
        row1_lbl = SerifLabel("density of photon states:", INK, size=24)
        row1_lbl.move_to(LEFT * 2.5 + UP * 1.0)
        row1_val = Text("proportional to omega^2", font=MONO, font_size=24,
                        color=TEAL).move_to(RIGHT * 2.0 + UP * 1.0)
        row2_lbl = SerifLabel("matrix element coupling:", INK, size=24)
        row2_lbl.move_to(LEFT * 2.5 + DOWN * 0.2)
        row2_val = Text("one more factor of omega", font=MONO, font_size=24,
                        color=TEAL).move_to(RIGHT * 2.2 + DOWN * 0.2)
        divider_h = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5)
        divider_h.move_to(DOWN * 1.0)
        total_lbl = SerifLabel("total rate:", INK, size=26)
        total_lbl.move_to(LEFT * 4.0 + DOWN * 1.8)
        total_val = Text("omega^2  x  omega  =  omega^3", font=MONO, font_size=26,
                         color=TEAL).move_to(RIGHT * 0.5 + DOWN * 1.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(row1_lbl), FadeIn(row1_val), run_time=dur * 0.30)
        self.play(FadeIn(row2_lbl), FadeIn(row2_val), run_time=dur * 0.25)
        self.play(Create(divider_h), run_time=dur * 0.10)
        self.play(FadeIn(total_lbl), FadeIn(total_val, scale=0.9), run_time=dur * 0.20)
        self.wait(dur * 0.15)


# ── B09: THE MECHANISM — section CARD — no scene class ───────────────────────


# ── B10: THE MECHANISM — log-scale frequency curve ───────────────────────────
class B10_OmegaCubedCurve(Scene):
    def construct(self):
        dur = DUR.get("B10", 12.0)
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 8, 2],
                    x_length=8.0, y_length=5.5,
                    axis_config={"color": INK, "stroke_width": 1.5},
                    tips=False)
        axes.move_to(DOWN * 0.2)
        # omega^3 curve on log-log scale (display as straight line with slope 3)
        curve = axes.plot(lambda x: 0.008 * x**3, x_range=[0.5, 9.5],
                          color=INK, stroke_width=3)
        # NMR point at low x (crimson)
        nmr_pt = axes.c2p(1.0, 0.008 * 1.0**3)
        nmr_dot = Dot(nmr_pt, radius=0.18, color=CRIMSON)
        nmr_lbl = LabelChip("NMR  (radio)", accent=CRIMSON, size=22)
        nmr_lbl.next_to(nmr_dot, DOWN, buff=0.35)
        # Optical point at high x (teal)
        opt_pt = axes.c2p(9.0, 0.008 * 9.0**3)
        opt_dot = Dot(opt_pt, radius=0.18, color=TEAL)
        opt_lbl = LabelChip("optical", accent=TEAL, size=22)
        opt_lbl.next_to(opt_dot, UP + LEFT, buff=0.3)
        x_lbl = SerifLabel("frequency", INK, size=20).next_to(axes, RIGHT, buff=0.1)
        y_lbl = SerifLabel("rate", INK, size=20).next_to(axes, UP + LEFT * 4.5, buff=0.1)
        slope_lbl = Text("slope = omega^3", font=SERIF, font_size=22, color=INK,
                         slant=ITALIC).move_to(LEFT * 0.5 + UP * 1.5)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.5)
        self.play(Create(curve), run_time=dur * 0.35)
        self.play(FadeIn(nmr_dot), FadeIn(nmr_lbl), run_time=dur * 0.20)
        self.play(FadeIn(opt_dot), FadeIn(opt_lbl), run_time=dur * 0.20)
        self.play(FadeIn(slope_lbl), run_time=dur * 0.15)
        self.wait(dur * 0.10)


# ── B11: THE IMPLICATION — NMR stability ─────────────────────────────────────
class B11_NMRStability(Scene):
    def construct(self):
        dur = DUR.get("B11", 11.0)
        title = Text("NMR spin states: stable because of omega^3", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.0)
        # Show NMR frequency vs lifetime comparison
        freq_lbl = SerifLabel("NMR frequency:", INK, size=24)
        freq_lbl.move_to(LEFT * 2.5 + UP * 1.0)
        freq_val = Text("400 MHz  (radio)", font=MONO, font_size=24, color=CRIMSON)
        freq_val.move_to(RIGHT * 2.0 + UP * 1.0)
        life_lbl = SerifLabel("spontaneous lifetime:", INK, size=24)
        life_lbl.move_to(LEFT * 2.5 + DOWN * 0.2)
        life_val = Text("~10^7 years", font=MONO, font_size=24, color=CRIMSON)
        life_val.move_to(RIGHT * 1.8 + DOWN * 0.2)
        implication = Text("Long enough to measure with a detector.",
                           font=DISPLAY, font_size=24, color=TEAL)
        implication.move_to(DOWN * 1.8)
        highlight = Rectangle(width=8.0, height=0.55, fill_color=GOLD,
                              fill_opacity=0.35, stroke_width=0)
        highlight.move_to(DOWN * 1.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(freq_lbl), FadeIn(freq_val), run_time=dur * 0.30)
        self.play(FadeIn(life_lbl), FadeIn(life_val), run_time=dur * 0.25)
        self.play(FadeIn(highlight), FadeIn(implication, shift=UP * 0.1), run_time=dur * 0.25)
        self.wait(dur * 0.20)


# ── B12: THE IMPLICATION — laser window ──────────────────────────────────────
class B12_LaserWindow(Scene):
    def construct(self):
        dur = DUR.get("B12", 10.0)
        # Show two levels with lifetime label, compare optical vs radio
        title = Text("Optical excited states: emit before they can be used",
                     font=DISPLAY, font_size=26, color=INK).move_to(UP * 3.0)
        opt_sys = _two_level([-3.5, 0.3, 0], "optical", TEAL,
                             excited_y=0.8, ground_y=-0.8)
        opt_life = Text("lifetime ~1 ns", font=MONO, font_size=20, color=TEAL)
        opt_life.move_to(LEFT * 3.5 + DOWN * 2.0)
        nmr_sys = _two_level([3.5, 0.3, 0], "radio", CRIMSON,
                             excited_y=0.8, ground_y=-0.8)
        nmr_life = Text("lifetime ~10^7 yr", font=MONO, font_size=20, color=CRIMSON)
        nmr_life.move_to(RIGHT * 3.5 + DOWN * 2.0)
        divider = Line(UP * 2.0, DOWN * 2.8, color=INK, stroke_width=1.5)
        note = SerifLabel("omega^3 sets the window", INK, size=22)
        note.move_to(DOWN * 3.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(opt_sys), FadeIn(nmr_sys), run_time=dur * 0.35)
        self.play(FadeIn(opt_life), FadeIn(nmr_life), run_time=dur * 0.30)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=dur * 0.20)
        self.wait(dur * 0.15)


# ── B13: THE EXAMPLE — illustrative A-coefficient numbers ────────────────────
class B13_IllustrativeExample(Scene):
    def construct(self):
        dur = DUR.get("B13", 18.0)
        title = Text("Illustrative: Einstein A-coefficient", font=DISPLAY,
                     font_size=28, color=INK).move_to(UP * 3.1)
        subtitle = Text("(invented numbers, labeled illustrative)", font=SERIF,
                        font_size=20, color=INK, slant=ITALIC).move_to(UP * 2.5)
        # Two-column: NMR vs optical
        nmr_col = VGroup(
            LabelChip("300 MHz (radio)", accent=CRIMSON, size=22),
            Text("dipole = a_0", font=MONO, font_size=20, color=INK),
            Text("A ~ 3 x 10^-17 /s", font=MONO, font_size=22, color=CRIMSON),
            Text("lifetime ~ 10^9 yr", font=MONO, font_size=20, color=CRIMSON),
        )
        nmr_col.arrange(DOWN, buff=0.38).move_to(LEFT * 3.2 + DOWN * 0.5)
        opt_col = VGroup(
            LabelChip("600 THz (optical)", accent=TEAL, size=22),
            Text("dipole = a_0", font=MONO, font_size=20, color=INK),
            Text("A ~ 10^8 /s", font=MONO, font_size=22, color=TEAL),
            Text("lifetime ~ 10 ns", font=MONO, font_size=20, color=TEAL),
        )
        opt_col.arrange(DOWN, buff=0.38).move_to(RIGHT * 3.2 + DOWN * 0.5)
        divider = Line(UP * 2.0, DOWN * 2.5, color=INK, stroke_width=1.5)
        ratio = LabelChip("rate ratio ~ 3 x 10^24", accent=TEAL, size=22)
        ratio.move_to(DOWN * 3.2)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(nmr_col), run_time=dur * 0.30)
        self.play(FadeIn(opt_col), run_time=dur * 0.30)
        self.play(FadeIn(ratio, shift=UP * 0.1), run_time=dur * 0.20)
        self.wait(dur * 0.20)


# ── B14: RECAP — CARD beat, no scene class ───────────────────────────────────
