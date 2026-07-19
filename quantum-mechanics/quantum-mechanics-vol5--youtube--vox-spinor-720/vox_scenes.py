"""vox_scenes.py — Rotate an electron all the way around and it comes back wrong
(vox-spinor-720, slate cut, 16:9).
Color law: TEAL=spinor/half-angle phase; CRIMSON=sign-flipped/wrong state; GOLD=dial marker.
Exclusions: no spin measurement; anchor to half-angle in the exponent.
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


def _dur(bid, fallback=8.0):
    return DUR.get(bid, fallback)


def _circle_arrow(angle, radius=1.4, color=TEAL, stroke_width=3.5):
    """Arrow on a circle at given angle (radians from UP=pi/2)."""
    tip = RIGHT * radius * np.cos(angle) + UP * radius * np.sin(angle)
    arr = Arrow(ORIGIN, tip, buff=0, stroke_width=stroke_width, color=color,
                max_tip_length_to_length_ratio=0.18)
    return arr


def _dial_arrow(angle, radius=0.85, color=GOLD, stroke_width=3.0):
    """Smaller dial arrow at half-angle."""
    tip = RIGHT * radius * np.cos(angle) + UP * radius * np.sin(angle)
    arr = Arrow(ORIGIN, tip, buff=0, stroke_width=stroke_width, color=color,
                max_tip_length_to_length_ratio=0.20)
    return arr


def _make_spinor_arrow(physical_angle_deg, center=ORIGIN, r_phys=1.4, r_dial=0.85):
    """Return (phys_arrow, dial_arrow) for a given physical rotation angle in degrees."""
    phi = np.radians(physical_angle_deg)
    half_phi = phi / 2
    # Physical arrow: starts pointing UP (pi/2), rotates by phi
    phys_angle = np.pi / 2 + phi
    dial_angle = np.pi / 2 + half_phi

    phys_tip = center + RIGHT * r_phys * np.cos(phys_angle) + UP * r_phys * np.sin(phys_angle)
    dial_tip = center + RIGHT * r_dial * np.cos(dial_angle) + UP * r_dial * np.sin(dial_angle)

    phys_arr = Arrow(center, phys_tip, buff=0, stroke_width=3.5, color=TEAL,
                     max_tip_length_to_length_ratio=0.18)
    dial_arr = Arrow(center, dial_tip, buff=0, stroke_width=3.0, color=GOLD,
                     max_tip_length_to_length_ratio=0.20)
    return phys_arr, dial_arr


def _circle_outline(radius, center=ORIGIN, color=INK, stroke_width=1.0):
    c = Circle(radius=radius, color=color, stroke_width=stroke_width, fill_opacity=0)
    c.move_to(center)
    return c


def _tick_mark(angle, r_inner, r_outer, center=ORIGIN, color=INK, stroke_width=1.5):
    p1 = center + RIGHT * r_inner * np.cos(angle) + UP * r_inner * np.sin(angle)
    p2 = center + RIGHT * r_outer * np.cos(angle) + UP * r_outer * np.sin(angle)
    return Line(p1, p2, color=color, stroke_width=stroke_width)


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        # CARD beat — simple title card
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.5)
        headline = Text("Rotate an electron all\nthe way around and it\ncomes back wrong",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B01") - 1.3)


# ── B02 CARD ──────────────────────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Why does an electron need\ntwo full turns — not one —\nto come back to itself?",
                        font=SERIF, color=INK, font_size=30, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — rotation operator formula ──────────────────────────────
class B03_RotationOperator(Scene):
    def construct(self):
        """Show rotation operator Rz(phi) and the half-angle structure."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        # State 1: Label header
        title = Text("Rotation operator for spin-½", font=SERIF, color=INK,
                     font_size=30, slant=ITALIC)
        title.move_to(UP * 3.2)

        # State 2: Two circles (physical + dial)
        cx = 0.0
        phys_circle = _circle_outline(1.4, center=RIGHT * cx, color=INK, stroke_width=1.2)
        dial_circle = _circle_outline(0.85, center=RIGHT * cx, color=SLATE, stroke_width=0.9)

        # Tick marks at 0, 90, 180, 270 degrees
        ticks = VGroup()
        for ang_deg in [0, 90, 180, 270]:
            ang = np.radians(ang_deg)
            ticks.add(_tick_mark(ang, 1.4, 1.55, center=RIGHT * cx, color=INK))
            ticks.add(_tick_mark(ang, 0.85, 0.97, center=RIGHT * cx, color=SLATE))

        circles = VGroup(phys_circle, dial_circle, ticks)

        # Labels for circles
        phys_lbl = Text("Physical rotation (φ)", font=DISPLAY, color=TEAL,
                        font_size=18, weight=BOLD)
        phys_lbl.move_to(UP * -2.2)
        dial_lbl = Text("Phase dial (φ/2)", font=DISPLAY, color=SLATE,
                        font_size=18, weight=BOLD)
        dial_lbl.move_to(UP * -2.7)

        self.play(FadeIn(title), run_time=0.6)
        self.play(Create(circles), run_time=0.8)

        # State 3: Add initial arrows at 0 deg (pointing UP)
        phys_arr0, dial_arr0 = _make_spinor_arrow(0, center=RIGHT * cx)
        self.play(FadeIn(phys_arr0), FadeIn(dial_arr0), run_time=0.6)

        # State 4: Rotate to 90 degrees (showing phase at 45)
        phys_arr1, dial_arr1 = _make_spinor_arrow(90, center=RIGHT * cx)
        ang90_lbl = Text("90° → phase: 45°", font=DISPLAY, color=INK, font_size=20)
        ang90_lbl.move_to(UP * 1.6)
        self.play(
            Transform(phys_arr0, phys_arr1),
            Transform(dial_arr0, dial_arr1),
            FadeIn(ang90_lbl),
            run_time=0.7,
        )

        # State 5: Rotate to 180 degrees (showing phase at 90)
        phys_arr2, dial_arr2 = _make_spinor_arrow(180, center=RIGHT * cx)
        ang180_lbl = Text("180° → phase: 90°", font=DISPLAY, color=INK, font_size=20)
        ang180_lbl.move_to(UP * 1.0)
        self.play(
            Transform(phys_arr0, phys_arr2),
            Transform(dial_arr0, dial_arr2),
            FadeOut(ang90_lbl),
            FadeIn(ang180_lbl),
            run_time=0.7,
        )

        # State 6: Add circle labels and equation hint
        self.play(
            FadeIn(phys_lbl), FadeIn(dial_lbl),
            run_time=0.5,
        )

        # Bracket rectangle for emphasis
        eq_box = Rectangle(width=4.5, height=0.7, color=TEAL, fill_opacity=0.10)
        eq_box.set_stroke(TEAL, width=1.5)
        eq_box.move_to(UP * 1.0)
        self.play(Create(eq_box), run_time=0.4)

        self.wait(_dur("B03") - 3.6)


# ── B04 THE PROBLEM — half-speed dial tracking ───────────────────────────────
class B04_HalfSpeedDial(Scene):
    def construct(self):
        """Physical arrow returns to start; dial only halfway around."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        cx = -2.0
        phys_circle = _circle_outline(1.4, center=RIGHT * cx, color=INK, stroke_width=1.2)
        dial_circle = _circle_outline(0.85, center=RIGHT * cx, color=SLATE, stroke_width=0.9)
        ticks = VGroup()
        for ang_deg in [0, 90, 180, 270]:
            ang = np.radians(ang_deg)
            ticks.add(_tick_mark(ang, 1.4, 1.55, center=RIGHT * cx, color=INK))
        circles = VGroup(phys_circle, dial_circle, ticks)

        # State 1: Title + circles
        title = Text("One full turn: where does the dial end?",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), Create(circles), run_time=0.7)

        # State 2: Start at 0 degrees
        phys_arr0, dial_arr0 = _make_spinor_arrow(0, center=RIGHT * cx)
        start_lbl = Text("φ = 0°", font=DISPLAY, color=INK, font_size=22)
        start_lbl.move_to(RIGHT * 2.0 + UP * 3.0)
        self.play(FadeIn(phys_arr0), FadeIn(dial_arr0), FadeIn(start_lbl), run_time=0.5)

        # State 3: At 90 degrees — show the lag beginning
        phys_arr_90, dial_arr_90 = _make_spinor_arrow(90, center=RIGHT * cx)
        lbl_90 = Text("φ = 90°  →  dial: 45°", font=DISPLAY, color=INK, font_size=20)
        lbl_90.move_to(RIGHT * 2.5 + UP * 2.3)
        self.play(
            Transform(phys_arr0, phys_arr_90),
            Transform(dial_arr0, dial_arr_90),
            FadeOut(start_lbl),
            FadeIn(lbl_90),
            run_time=0.6,
        )

        # State 4: At 180 degrees — physical halfway, dial at 90
        phys_arr1, dial_arr1 = _make_spinor_arrow(180, center=RIGHT * cx)
        mid_lbl = Text("φ = 180°  →  dial: 90°", font=DISPLAY, color=INK, font_size=20)
        mid_lbl.move_to(RIGHT * 2.5 + UP * 1.5)
        self.play(
            Transform(phys_arr0, phys_arr1),
            Transform(dial_arr0, dial_arr1),
            FadeOut(lbl_90),
            FadeIn(mid_lbl),
            run_time=0.7,
        )

        # State 5: At 360 degrees — physical back to top, dial at 180 (pointing DOWN)
        phys_arr2, dial_arr2 = _make_spinor_arrow(360, center=RIGHT * cx)
        full_lbl = Text("φ = 360°  →  dial: 180°", font=DISPLAY, color=CRIMSON, font_size=20)
        full_lbl.move_to(RIGHT * 2.5 + UP * 0.5)
        self.play(
            Transform(phys_arr0, phys_arr2),
            Transform(dial_arr0, dial_arr2),
            FadeOut(mid_lbl),
            FadeIn(full_lbl),
            run_time=0.9,
        )

        # State 6: Highlight that dial points DOWN — a rectangle + CRIMSON underline
        dial_down_box = Rectangle(width=3.2, height=0.5, color=CRIMSON, fill_opacity=0.10)
        dial_down_box.set_stroke(CRIMSON, width=1.5)
        dial_down_box.move_to(RIGHT * 2.5 + UP * 0.5)
        halfway_note = Text("Dial only halfway around!", font=DISPLAY, color=CRIMSON,
                            font_size=19, weight=BOLD)
        halfway_note.move_to(RIGHT * 2.5 + UP * -0.3)
        self.play(Create(dial_down_box), FadeIn(halfway_note), run_time=0.5)

        self.wait(_dur("B04") - 3.4)


# ── B05 THE MECHANISM — sign flip at 360 ────────────────────────────────────
class B05_SignFlip(Scene):
    def construct(self):
        """e^(i*pi) = -1: spinor sign-flipped after one full turn."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        # State 1: Setup two panels: left = arrow diagram, right = equation
        title = Text("What e^(iπ) = −1 means for the spinor",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.6)

        # Left panel: circle with arrow at 180 degrees (dial pointing DOWN)
        cx_left = -3.0
        phys_circle = _circle_outline(1.3, center=RIGHT * cx_left, color=INK, stroke_width=1.2)
        dial_circle = _circle_outline(0.8, center=RIGHT * cx_left, color=SLATE, stroke_width=0.9)
        ticks = VGroup()
        for ang_deg in [0, 90, 180, 270]:
            ang = np.radians(ang_deg)
            ticks.add(_tick_mark(ang, 1.3, 1.45, center=RIGHT * cx_left, color=INK))
        circles = VGroup(phys_circle, dial_circle, ticks)
        self.play(Create(circles), run_time=0.6)

        # State 2: Physical arrow pointing UP (returned after 360), dial pointing DOWN (at 180)
        phys_arr, dial_arr = _make_spinor_arrow(360, center=RIGHT * cx_left, r_phys=1.3, r_dial=0.8)
        phys_lbl = Text("Physical: back to top", font=DISPLAY, color=TEAL, font_size=17)
        phys_lbl.move_to(RIGHT * cx_left + UP * -2.3)
        dial_lbl = Text("Phase dial: pointing DOWN", font=DISPLAY, color=CRIMSON, font_size=17)
        dial_lbl.move_to(RIGHT * cx_left + UP * -2.9)
        self.play(FadeIn(phys_arr), FadeIn(dial_arr), run_time=0.5)
        self.play(FadeIn(phys_lbl), FadeIn(dial_lbl), run_time=0.5)

        # State 3: Right panel — equation boxes showing result
        eq1 = Text("Phase argument: π", font=DISPLAY, color=INK, font_size=24)
        eq1.move_to(RIGHT * 2.5 + UP * 1.5)
        eq2 = Text("e^(iπ) = −1", font=SERIF, color=CRIMSON, font_size=36, slant=ITALIC)
        eq2.move_to(RIGHT * 2.5 + UP * 0.4)
        eq_box = Rectangle(width=3.8, height=0.9, color=CRIMSON, fill_opacity=0.08)
        eq_box.set_stroke(CRIMSON, width=1.8)
        eq_box.move_to(RIGHT * 2.5 + UP * 0.4)
        self.play(FadeIn(eq1), Create(eq_box), FadeIn(eq2), run_time=0.7)

        # State 4: Conclusion label
        concl = Text("Spinor → −1 × original", font=DISPLAY, color=CRIMSON, font_size=22,
                     weight=BOLD)
        concl.move_to(RIGHT * 2.5 + UP * -0.8)
        concl_box = Rectangle(width=4.2, height=0.65, color=CRIMSON, fill_opacity=0.08)
        concl_box.set_stroke(CRIMSON, width=1.5)
        concl_box.move_to(RIGHT * 2.5 + UP * -0.8)
        self.play(Create(concl_box), FadeIn(concl), run_time=0.6)

        # State 5: Gold highlight bar for "360° = sign flip"
        flip_bar = Rectangle(width=5.5, height=0.5, color=GOLD, fill_opacity=0.30)
        flip_bar.set_stroke(GOLD, width=0)
        flip_bar.move_to(RIGHT * 2.5 + UP * -1.8)
        flip_note = Text("360° rotation = sign flip", font=DISPLAY, color=INK,
                         font_size=20, weight=BOLD)
        flip_note.move_to(RIGHT * 2.5 + UP * -1.8)
        self.play(FadeIn(flip_bar), FadeIn(flip_note), run_time=0.5)

        self.wait(_dur("B05") - 4.0)


# ── B06 THE MECHANISM — restoration at 720 ──────────────────────────────────
class B06_Restoration720(Scene):
    def construct(self):
        """Continue to 720 degrees: phase reaches 2pi, spinor restored."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("Second full turn: phase reaches 2π",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        cx = -2.5
        phys_circle = _circle_outline(1.3, center=RIGHT * cx, color=INK, stroke_width=1.2)
        dial_circle = _circle_outline(0.8, center=RIGHT * cx, color=SLATE, stroke_width=0.9)
        ticks = VGroup()
        for ang_deg in [0, 90, 180, 270]:
            ang = np.radians(ang_deg)
            ticks.add(_tick_mark(ang, 1.3, 1.45, center=RIGHT * cx, color=INK))
        circles = VGroup(phys_circle, dial_circle, ticks)
        self.play(Create(circles), run_time=0.5)

        # State 1: Start from 360 position (arrow up, dial down)
        phys_arr0, dial_arr0 = _make_spinor_arrow(360, center=RIGHT * cx, r_phys=1.3, r_dial=0.8)
        lbl360 = Text("φ = 360°  →  dial at 180°  →  sign: −1",
                      font=DISPLAY, color=CRIMSON, font_size=18)
        lbl360.move_to(RIGHT * 1.2 + UP * 2.0)
        self.play(FadeIn(phys_arr0), FadeIn(dial_arr0), FadeIn(lbl360), run_time=0.6)

        # State 2: At 540 degrees — arrow pointing down, dial at 270
        phys_arr1, dial_arr1 = _make_spinor_arrow(540, center=RIGHT * cx, r_phys=1.3, r_dial=0.8)
        lbl540 = Text("φ = 540°  →  dial at 270°", font=DISPLAY, color=INK, font_size=18)
        lbl540.move_to(RIGHT * 1.2 + UP * 1.0)
        self.play(
            Transform(phys_arr0, phys_arr1),
            Transform(dial_arr0, dial_arr1),
            FadeIn(lbl540),
            run_time=0.8,
        )

        # State 3: At 720 degrees — physical arrow back UP, dial completed full circle
        phys_arr2, dial_arr2 = _make_spinor_arrow(720, center=RIGHT * cx, r_phys=1.3, r_dial=0.8)
        lbl720 = Text("φ = 720°  →  dial at 360°  →  sign: +1",
                      font=DISPLAY, color=TEAL, font_size=18)
        lbl720.move_to(RIGHT * 1.2 + UP * -0.2)
        self.play(
            Transform(phys_arr0, phys_arr2),
            Transform(dial_arr0, dial_arr2),
            FadeIn(lbl720),
            run_time=0.9,
        )

        # State 4: e^(i*2pi) = +1 equation box
        eq = Text("e^(i·2π) = +1", font=SERIF, color=TEAL, font_size=32, slant=ITALIC)
        eq.move_to(RIGHT * 1.2 + UP * -1.5)
        eq_box = Rectangle(width=3.5, height=0.85, color=TEAL, fill_opacity=0.08)
        eq_box.set_stroke(TEAL, width=1.8)
        eq_box.move_to(RIGHT * 1.2 + UP * -1.5)
        self.play(Create(eq_box), FadeIn(eq), run_time=0.6)

        # State 5: Gold highlight bar — "720° = restored"
        restore_bar = Rectangle(width=4.5, height=0.5, color=GOLD, fill_opacity=0.30)
        restore_bar.set_stroke(GOLD, width=0)
        restore_bar.move_to(RIGHT * 1.2 + UP * -2.5)
        restore_lbl = Text("720° rotation = spinor restored", font=DISPLAY, color=INK,
                           font_size=20, weight=BOLD)
        restore_lbl.move_to(RIGHT * 1.2 + UP * -2.5)
        self.play(FadeIn(restore_bar), FadeIn(restore_lbl), run_time=0.5)

        self.wait(_dur("B06") - 4.4)


# ── B07 THE IMPLICATION — interference visibility of the sign ─────────────────
class B07_Interference(Scene):
    def construct(self):
        """Show that sign flip is visible in interference."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("The sign flip is observable in interference",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 1: Two vertical bars representing spinor amplitudes
        bar_orig = Rectangle(width=1.4, height=2.2, color=TEAL, fill_opacity=0.70)
        bar_orig.set_stroke(TEAL, width=0.8)
        bar_orig.move_to(LEFT * 3.5 + UP * 0.5)
        lbl_orig = Text("|ψ⟩", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        lbl_orig.move_to(LEFT * 3.5 + UP * -0.8)

        bar_flip = Rectangle(width=1.4, height=2.2, color=CRIMSON, fill_opacity=0.70)
        bar_flip.set_stroke(CRIMSON, width=0.8)
        bar_flip.move_to(LEFT * 1.5 + UP * 0.5)
        lbl_flip = Text("−|ψ⟩", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        lbl_flip.move_to(LEFT * 1.5 + UP * -0.8)

        self.play(FadeIn(bar_orig), FadeIn(lbl_orig), run_time=0.5)
        self.play(FadeIn(bar_flip), FadeIn(lbl_flip), run_time=0.5)

        # State 2: Add plus sign and equals to show sum
        plus_sign = Text("+", font=DISPLAY, color=INK, font_size=36)
        plus_sign.move_to(LEFT * 2.5 + UP * 0.5)
        equals_sign = Text("=", font=DISPLAY, color=INK, font_size=36)
        equals_sign.move_to(RIGHT * 0.4 + UP * 0.5)
        self.play(FadeIn(plus_sign), FadeIn(equals_sign), run_time=0.4)

        # State 3: Zero bar — destructive interference
        zero_bar = Rectangle(width=1.4, height=0.04, color=INK, fill_opacity=0.90)
        zero_bar.set_stroke(INK, width=1.0)
        zero_bar.move_to(RIGHT * 1.8 + UP * -1.05)
        zero_lbl = Text("0  (cancels)", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        zero_lbl.move_to(RIGHT * 1.8 + UP * -0.8)
        self.play(FadeIn(zero_bar), FadeIn(zero_lbl), run_time=0.6)

        # State 4: Probabilities note
        prob_box = Rectangle(width=5.8, height=0.7, color=SLATE, fill_opacity=0.08)
        prob_box.set_stroke(SLATE, width=1.2)
        prob_box.move_to(RIGHT * 2.5 + UP * 1.2)
        prob_note = Text("|ψ|² = |−ψ|²  (same probability)", font=DISPLAY, color=INK,
                         font_size=20)
        prob_note.move_to(RIGHT * 2.5 + UP * 1.2)
        self.play(Create(prob_box), FadeIn(prob_note), run_time=0.6)

        # State 5: Arrow showing interference is the detector
        int_arrow = Arrow(RIGHT * 2.5 + UP * 0.5, RIGHT * 2.5 + UP * -0.3,
                          buff=0, stroke_width=2.0, color=GOLD,
                          max_tip_length_to_length_ratio=0.20)
        int_note = Text("Mix them → interference measures the sign",
                        font=DISPLAY, color=INK, font_size=18)
        int_note.move_to(RIGHT * 2.5 + UP * -1.6)
        self.play(Create(int_arrow), FadeIn(int_note), run_time=0.5)

        self.wait(_dur("B07") - 3.6)


# ── B08 STILL·ai — neutron interferometry ────────────────────────────────────
class B08_NeutronInterferometry(Scene):
    def construct(self):
        # Slate — ai image placeholder
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        slate_box = Rectangle(width=12.0, height=6.5, color=SLATE, fill_opacity=0.12)
        slate_box.set_stroke(SLATE, width=1.5)
        slate_box.move_to(UP * 0.2)
        slate_lbl = Text("SLATE · ai image", font=DISPLAY, color=SLATE, font_size=26, weight=BOLD)
        slate_lbl.move_to(UP * 0.2)
        caption = Text("Neutron interferometer (Rauch/Werner 1975)", font=SERIF,
                       color=INK, font_size=20, slant=ITALIC)
        caption.move_to(UP * -2.8)
        self.add(bg, slate_box, slate_lbl, caption)
        self.wait(_dur("B08"))


# ── B09 THE EXAMPLE — SU(2) double cover ─────────────────────────────────────
class B09_SU2DoubleCover(Scene):
    def construct(self):
        """SU(2) covers SO(3) twice: two spinor rotations per classical rotation."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        self.add(bg)

        title = Text("SU(2) is the double cover of SO(3)",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.3)
        self.play(FadeIn(title), run_time=0.5)

        # State 1: SO(3) circle on left, SU(2) on right with two points per SO(3) point
        so3_circle = Circle(radius=1.3, color=INK, stroke_width=1.5, fill_opacity=0)
        so3_circle.move_to(LEFT * 3.5 + UP * 0.8)
        so3_lbl = Text("SO(3)", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        so3_lbl.move_to(LEFT * 3.5 + UP * -0.8)
        so3_sub = Text("Classical rotations", font=DISPLAY, color=SLATE, font_size=17)
        so3_sub.move_to(LEFT * 3.5 + UP * -1.4)

        su2_circle = Circle(radius=1.3, color=TEAL, stroke_width=1.5, fill_opacity=0)
        su2_circle.move_to(RIGHT * 3.5 + UP * 0.8)
        su2_lbl = Text("SU(2)", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        su2_lbl.move_to(RIGHT * 3.5 + UP * -0.8)
        su2_sub = Text("Spinor rotations", font=DISPLAY, color=TEAL, font_size=17)
        su2_sub.move_to(RIGHT * 3.5 + UP * -1.4)

        self.play(Create(so3_circle), FadeIn(so3_lbl), FadeIn(so3_sub), run_time=0.6)
        self.play(Create(su2_circle), FadeIn(su2_lbl), FadeIn(su2_sub), run_time=0.6)

        # State 2: A dot in SO(3) — one rotation
        so3_dot = Dot(LEFT * 3.5 + UP * 2.1, color=INK, radius=0.12)
        self.play(FadeIn(so3_dot), run_time=0.4)

        # State 3: Two corresponding dots in SU(2): +psi and -psi
        su2_dot1 = Dot(RIGHT * 3.5 + UP * 2.1, color=TEAL, radius=0.12)
        su2_dot2 = Dot(RIGHT * 3.5 + UP * -0.5, color=CRIMSON, radius=0.12)
        su2_dot1_lbl = Text("+|ψ⟩", font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        su2_dot1_lbl.move_to(RIGHT * 4.2 + UP * 2.1)
        su2_dot2_lbl = Text("−|ψ⟩", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        su2_dot2_lbl.move_to(RIGHT * 4.2 + UP * -0.5)
        # Arrows from SO(3) dot to both SU(2) dots
        arr1 = Arrow(LEFT * 3.5 + UP * 2.1, RIGHT * 3.5 + UP * 2.1,
                     buff=0.15, stroke_width=1.8, color=SLATE,
                     max_tip_length_to_length_ratio=0.12)
        arr2 = Arrow(LEFT * 3.5 + UP * 2.1, RIGHT * 3.5 + UP * -0.5,
                     buff=0.15, stroke_width=1.8, color=SLATE,
                     max_tip_length_to_length_ratio=0.12)
        self.play(
            FadeIn(su2_dot1), FadeIn(su2_dot2),
            Create(arr1), Create(arr2),
            FadeIn(su2_dot1_lbl), FadeIn(su2_dot2_lbl),
            run_time=0.8,
        )

        # State 4: Note — "2:1 map"
        ratio_lbl = Text("2 : 1 mapping", font=DISPLAY, color=INK, font_size=22,
                         weight=BOLD)
        ratio_lbl.move_to(UP * -2.4)
        ratio_bar = Rectangle(width=3.0, height=0.55, color=GOLD, fill_opacity=0.28)
        ratio_bar.set_stroke(GOLD, width=0)
        ratio_bar.move_to(UP * -2.4)
        self.play(FadeIn(ratio_bar), FadeIn(ratio_lbl), run_time=0.5)

        # State 5: Final note box
        note_box = Rectangle(width=7.0, height=0.65, color=SLATE, fill_opacity=0.08)
        note_box.set_stroke(SLATE, width=1.2)
        note_box.move_to(UP * -3.2)
        note_txt = Text("Electrons live in SU(2) — not in ordinary rotation space",
                        font=DISPLAY, color=INK, font_size=18)
        note_txt.move_to(UP * -3.2)
        self.play(Create(note_box), FadeIn(note_txt), run_time=0.5)

        self.wait(_dur("B09") - 4.4)


# ── B10 CARD ──────────────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                        color=GROUND, fill_opacity=1).set_stroke(width=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Half-angle in the exponent.\n360° = sign flip.\n720° = restored.",
                        font=SERIF, color=INK, font_size=34, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B10") - 1.3)
