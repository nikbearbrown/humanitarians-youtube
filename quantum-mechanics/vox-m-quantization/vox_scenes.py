"""vox_scenes.py — Why m has to be a whole number
(vox-m-quantization, slate cut, 16:9)
Color law: TEAL=integer-m closed wave / good closure; CRIMSON=non-integer m broken wave;
           GOLD=closure-point highlight.
Exclusions: no spin-half expansion; no Legendre equation; no ell/n mechanisms.
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


def _ring_wave_points(m_val, n_pts=300, ring_radius=2.0, wave_amplitude=0.35):
    """Generate points for a phase wave wrapped around a ring.
    Returns array of (x, y) points.
    """
    angles = np.linspace(0, 2 * np.pi, n_pts, endpoint=False)
    # Phase of e^(i*m*phi): real part is cos(m*phi)
    phase = np.cos(m_val * angles)
    r = ring_radius + wave_amplitude * phase
    x = r * np.cos(angles)
    y = r * np.sin(angles)
    return x, y


def _make_ring_wave(m_val, color=TEAL, stroke_width=2.5, ring_radius=2.0,
                    wave_amplitude=0.35, n_pts=300, center=ORIGIN):
    x, y = _ring_wave_points(m_val, n_pts, ring_radius, wave_amplitude)
    points = [center + RIGHT * x[i] + UP * y[i] for i in range(len(x))]
    points.append(points[0])  # close the loop
    wave = VMobject(color=color, stroke_width=stroke_width, fill_opacity=0)
    wave.set_stroke(color=color, width=stroke_width, opacity=1)
    wave.set_points_smoothly(points)
    return wave


def _make_ring_wave_open(m_val, color=TEAL, stroke_width=2.5, ring_radius=2.0,
                         wave_amplitude=0.35, n_pts=300, center=ORIGIN):
    """Ring wave that does NOT close the loop — for non-integer m."""
    x, y = _ring_wave_points(m_val, n_pts, ring_radius, wave_amplitude)
    points = [center + RIGHT * x[i] + UP * y[i] for i in range(len(x))]
    # Do not append points[0]; leave open
    wave = VMobject(color=color, stroke_width=stroke_width, fill_opacity=0)
    wave.set_stroke(color=color, width=stroke_width, opacity=1)
    wave.set_points_smoothly(points)
    return wave


def _make_ring_outline(ring_radius=2.0, center=ORIGIN, color=INK, stroke_width=0.8):
    c = Circle(radius=ring_radius, color=color, stroke_width=stroke_width, fill_opacity=0)
    c.move_to(center)
    c.set_stroke(color=color, width=stroke_width, opacity=1)
    return c


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_ColdOpen(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("The magnetic quantum\nnumber is an integer —\nand nobody had to say so.",
                        font=SERIF, color=INK, font_size=30, line_spacing=1.2)
        headline.move_to(DOWN * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B01") - 1.3)


# ── B02 CARD ──────────────────────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("The Schrodinger equation\nnever says m must be\nan integer. Why is it?",
                        font=SERIF, color=INK, font_size=30, line_spacing=1.2)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B02") - 1.3)


# ── B03 THE PROBLEM — wave on ring, going around ─────────────────────────────
class B03_WaveOnRing(Scene):
    def construct(self):
        """Show azimuthal wave Phi=e^(imphi) wrapped on a ring; phi goes 0 to 2pi."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("The azimuthal wavefunction wraps around the atom",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.6)

        # Ring outline on left
        cx = -2.5
        ring = _make_ring_outline(ring_radius=1.8, center=RIGHT * cx, color=INK)
        nucleus = Dot(RIGHT * cx, color=INK, radius=0.10)
        nucleus_lbl = Text("nucleus", font=DISPLAY, color=INK, font_size=16)
        nucleus_lbl.move_to(RIGHT * cx + UP * -0.35)

        self.play(Create(ring), FadeIn(nucleus), run_time=0.6)
        self.play(FadeIn(nucleus_lbl), run_time=0.4)

        # Wave at m=2 on the ring (integer) — green/teal, good
        wave = _make_ring_wave(m_val=2, color=TEAL, stroke_width=2.8,
                               ring_radius=1.8, wave_amplitude=0.28,
                               center=RIGHT * cx)

        # Equation label on right
        eq_lbl = Text("Phi(phi) = e^(i m phi)", font=SERIF, color=INK,
                      font_size=28, slant=ITALIC)
        eq_lbl.move_to(RIGHT * 2.5 + UP * 1.5)
        phi_lbl = Text("phi = azimuthal angle", font=DISPLAY, color=SLATE, font_size=20)
        phi_lbl.move_to(RIGHT * 2.5 + UP * 0.6)
        range_lbl = Text("0 to 2pi around the ring", font=DISPLAY, color=SLATE, font_size=20)
        range_lbl.move_to(RIGHT * 2.5 + UP * 0.0)

        self.play(FadeIn(eq_lbl), run_time=0.5)
        self.play(FadeIn(phi_lbl), FadeIn(range_lbl), run_time=0.5)
        self.play(Create(wave), run_time=1.2)

        # Arrow tracing the circle — start dot
        start_dot = Dot(RIGHT * cx + RIGHT * 1.8, color=GOLD, radius=0.13)
        start_dot.set_stroke(width=0, opacity=0)
        self.play(FadeIn(start_dot), run_time=0.4)

        # Move a dot around the ring to show round trip
        tracker = ValueTracker(0)
        dot = Dot(color=CRIMSON, radius=0.10)
        dot.set_stroke(width=0, opacity=0)

        def update_dot(d):
            angle = tracker.get_value()
            d.move_to(RIGHT * cx + RIGHT * 1.8 * np.cos(angle) + UP * 1.8 * np.sin(angle))

        dot.add_updater(update_dot)
        self.add(dot)
        self.play(tracker.animate.set_value(2 * np.pi), run_time=1.5)
        dot.remove_updater(update_dot)

        return_lbl = Text("Back to start", font=DISPLAY, color=CRIMSON, font_size=18)
        return_lbl.move_to(RIGHT * cx + DOWN * 2.6)
        self.play(FadeIn(return_lbl), run_time=0.4)

        self.wait(_dur("B03") - 5.6)


# ── B04 THE PROBLEM — single-valuedness requirement ──────────────────────────
class B04_SingleValued(Scene):
    def construct(self):
        """Show what single-valuedness means: same value at phi=0 and phi=2pi."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("The wavefunction must be single-valued",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Left: good single-valued function on a segment (same at start and end)
        cx_l = -3.5
        seg_line = Line(LEFT * 1.3 + UP * 0.0 + RIGHT * cx_l,
                        RIGHT * 1.3 + UP * 0.0 + RIGHT * cx_l,
                        color=INK, stroke_width=1.0)
        seg_line.set_stroke(color=INK, width=1.0, opacity=1)
        start_tick = Line(LEFT * 1.3 + UP * 0.2 + RIGHT * cx_l,
                          LEFT * 1.3 + DOWN * 0.2 + RIGHT * cx_l,
                          color=INK, stroke_width=1.5)
        start_tick.set_stroke(color=INK, width=1.5, opacity=1)
        end_tick = Line(RIGHT * 1.3 + UP * 0.2 + RIGHT * cx_l,
                        RIGHT * 1.3 + DOWN * 0.2 + RIGHT * cx_l,
                        color=INK, stroke_width=1.5)
        end_tick.set_stroke(color=INK, width=1.5, opacity=1)

        # Draw a wave that starts and ends at same height (integer m)
        n_pts = 80
        t = np.linspace(0, 2 * np.pi, n_pts)
        good_x = np.linspace(-1.3, 1.3, n_pts)
        good_y = 0.5 * np.cos(2 * t)  # 2 full cycles, matches
        good_pts = [RIGHT * (cx_l + good_x[i]) + UP * (good_y[i] + 0.5) for i in range(n_pts)]
        good_wave = VMobject(color=TEAL, stroke_width=2.8, fill_opacity=0)
        good_wave.set_stroke(color=TEAL, width=2.8, opacity=1)
        good_wave.set_points_smoothly(good_pts)

        good_dot_start = Dot(RIGHT * cx_l + LEFT * 1.3 + UP * (good_y[0] + 0.5),
                             color=TEAL, radius=0.12)
        good_dot_start.set_stroke(width=0, opacity=0)
        good_dot_end = Dot(RIGHT * cx_l + RIGHT * 1.3 + UP * (good_y[-1] + 0.5),
                           color=TEAL, radius=0.12)
        good_dot_end.set_stroke(width=0, opacity=0)

        # Label
        good_lbl = Text("match", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        good_lbl.move_to(RIGHT * cx_l + DOWN * 1.0)

        self.play(Create(seg_line), Create(start_tick), Create(end_tick), run_time=0.5)
        self.play(Create(good_wave), FadeIn(good_dot_start), FadeIn(good_dot_end),
                  run_time=0.8)
        self.play(FadeIn(good_lbl), run_time=0.4)

        # Right: bad — non-integer m, start != end
        cx_r = 2.5
        seg_line2 = Line(LEFT * 1.3 + UP * 0.0 + RIGHT * cx_r,
                         RIGHT * 1.3 + UP * 0.0 + RIGHT * cx_r,
                         color=INK, stroke_width=1.0)
        seg_line2.set_stroke(color=INK, width=1.0, opacity=1)
        start_tick2 = Line(LEFT * 1.3 + UP * 0.2 + RIGHT * cx_r,
                           LEFT * 1.3 + DOWN * 0.2 + RIGHT * cx_r,
                           color=INK, stroke_width=1.5)
        start_tick2.set_stroke(color=INK, width=1.5, opacity=1)
        end_tick2 = Line(RIGHT * 1.3 + UP * 0.2 + RIGHT * cx_r,
                         RIGHT * 1.3 + DOWN * 0.2 + RIGHT * cx_r,
                         color=INK, stroke_width=1.5)
        end_tick2.set_stroke(color=INK, width=1.5, opacity=1)

        bad_m = 1.7
        bad_x = np.linspace(0, 2 * np.pi, n_pts)
        bad_y = 0.5 * np.cos(bad_m * bad_x)
        # Start value
        bad_start_y = bad_y[0] + 0.5
        # End value (after 2pi, with non-integer m)
        bad_end_val = 0.5 * np.cos(bad_m * 2 * np.pi) + 0.5
        bad_pts = [RIGHT * (cx_r - 1.3 + 2.6 * i / (n_pts - 1)) + UP * (bad_y[i] + 0.5)
                   for i in range(n_pts)]
        bad_wave = VMobject(color=CRIMSON, stroke_width=2.8, fill_opacity=0)
        bad_wave.set_stroke(color=CRIMSON, width=2.8, opacity=1)
        bad_wave.set_points_smoothly(bad_pts)

        bad_dot_start = Dot(RIGHT * cx_r + LEFT * 1.3 + UP * bad_start_y,
                            color=CRIMSON, radius=0.12)
        bad_dot_start.set_stroke(width=0, opacity=0)
        bad_dot_end = Dot(RIGHT * cx_r + RIGHT * 1.3 + UP * bad_end_val,
                          color=CRIMSON, radius=0.12)
        bad_dot_end.set_stroke(width=0, opacity=0)

        # Jump line showing mismatch
        jump_line = DashedLine(
            RIGHT * cx_r + RIGHT * 1.3 + UP * bad_start_y,
            RIGHT * cx_r + RIGHT * 1.3 + UP * bad_end_val,
            color=CRIMSON, stroke_width=2.0, dash_length=0.1
        )
        jump_line.set_stroke(color=CRIMSON, width=2.0, opacity=1)

        bad_lbl = Text("mismatch", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        bad_lbl.move_to(RIGHT * cx_r + DOWN * 1.0)

        self.play(Create(seg_line2), Create(start_tick2), Create(end_tick2), run_time=0.5)
        self.play(Create(bad_wave), FadeIn(bad_dot_start), FadeIn(bad_dot_end),
                  run_time=0.8)
        self.play(Create(jump_line), FadeIn(bad_lbl), run_time=0.5)

        # Bottom note
        note = Text("Same point in space — two different values: rejected",
                    font=DISPLAY, color=INK, font_size=20)
        note.move_to(DOWN * 2.8)
        self.play(FadeIn(note), run_time=0.5)

        self.wait(_dur("B04") - 4.0)


# ── B05 THE MECHANISM — closure condition derivation ─────────────────────────
class B05_ClosureCondition(Scene):
    def construct(self):
        """Show the algebra: Phi(phi+2pi)=Phi(phi) => e^(2pi*i*m)=1 => m in Z."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("The closure condition forces m to be an integer",
                     font=SERIF, color=INK, font_size=27, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Step 1: single-valuedness demand
        step1 = Text("Demand:  Phi(phi + 2pi) = Phi(phi)",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        step1.move_to(UP * 2.2)
        step1_box = Rectangle(width=7.2, height=0.7, color=SLATE, fill_opacity=0.07)
        step1_box.set_stroke(SLATE, width=1.2)
        step1_box.move_to(UP * 2.2)
        self.play(Create(step1_box), FadeIn(step1), run_time=0.6)

        # Step 2: substitute Phi = e^(imphi)
        step2 = Text("Substitute:  e^(i m (phi + 2pi)) = e^(i m phi)",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        step2.move_to(UP * 1.1)
        self.play(FadeIn(step2), run_time=0.5)

        # Step 3: factor
        step3 = Text("Factor:  e^(i m phi) * e^(2 pi i m) = e^(i m phi)",
                     font=SERIF, color=INK, font_size=26, slant=ITALIC)
        step3.move_to(UP * 0.0)
        self.play(FadeIn(step3), run_time=0.5)

        # Step 4: requirement
        step4 = Text("Requirement:  e^(2 pi i m) = 1",
                     font=SERIF, color=TEAL, font_size=30, slant=ITALIC)
        step4.move_to(DOWN * 1.2)
        box4 = Rectangle(width=5.8, height=0.8, color=TEAL, fill_opacity=0.08)
        box4.set_stroke(TEAL, width=1.8)
        box4.move_to(DOWN * 1.2)
        self.play(Create(box4), FadeIn(step4), run_time=0.6)

        # Step 5: conclusion
        step5 = Text("Only when m is a whole number (integer)",
                     font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        step5.move_to(DOWN * 2.4)
        gold_bar = Rectangle(width=6.0, height=0.6, color=GOLD, fill_opacity=0.28)
        gold_bar.set_stroke(GOLD, width=0, opacity=0)
        gold_bar.move_to(DOWN * 2.4)
        self.play(FadeIn(gold_bar), FadeIn(step5), run_time=0.6)

        self.wait(_dur("B05") - 3.3)


# ── B06 THE MECHANISM — integer m closes the ring ────────────────────────────
class B06_IntegerClose(Scene):
    def construct(self):
        """Phase wave with integer m=2 wraps cleanly around the ring."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("m = 2: wave closes on itself",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Left: ring with m=2 wave (teal, closed)
        cx = -2.0
        ring = _make_ring_outline(ring_radius=1.8, center=RIGHT * cx, color=INK)
        nucleus = Dot(RIGHT * cx, color=INK, radius=0.10)
        nucleus.set_stroke(width=0, opacity=0)
        self.play(Create(ring), FadeIn(nucleus), run_time=0.5)

        wave2 = _make_ring_wave(m_val=2, color=TEAL, stroke_width=2.8,
                                ring_radius=1.8, wave_amplitude=0.30,
                                center=RIGHT * cx)
        self.play(Create(wave2), run_time=1.2)

        # Closure point highlight
        closure_dot = Dot(RIGHT * cx + RIGHT * 1.8, color=GOLD, radius=0.16)
        closure_dot.set_stroke(width=0, opacity=0)
        closure_lbl = Text("join point", font=DISPLAY, color=INK, font_size=18)
        closure_lbl.move_to(RIGHT * cx + RIGHT * 2.4 + UP * 0.3)
        self.play(FadeIn(closure_dot), FadeIn(closure_lbl), run_time=0.5)

        # Right side labels
        m_lbl = Text("m = 2", font=DISPLAY, color=TEAL, font_size=28, weight=BOLD)
        m_lbl.move_to(RIGHT * 3.2 + UP * 2.0)

        cycles_lbl = Text("2 complete cycles", font=DISPLAY, color=TEAL, font_size=22)
        cycles_lbl.move_to(RIGHT * 3.2 + UP * 1.0)

        close_lbl = Text("Endpoint = Start point", font=DISPLAY, color=TEAL, font_size=22)
        close_lbl.move_to(RIGHT * 3.2 + UP * 0.0)

        status = Text("Physics accepts this", font=DISPLAY, color=TEAL,
                      font_size=24, weight=BOLD)
        status.move_to(RIGHT * 3.2 + DOWN * 1.2)
        status_box = Rectangle(width=4.0, height=0.7, color=TEAL, fill_opacity=0.08)
        status_box.set_stroke(TEAL, width=1.5)
        status_box.move_to(RIGHT * 3.2 + DOWN * 1.2)

        self.play(FadeIn(m_lbl), run_time=0.4)
        self.play(FadeIn(cycles_lbl), run_time=0.4)
        self.play(FadeIn(close_lbl), run_time=0.4)
        self.play(Create(status_box), FadeIn(status), run_time=0.5)

        self.wait(_dur("B06") - 4.4)


# ── B07 THE MECHANISM — non-integer m breaks the ring ────────────────────────
class B07_NonIntegerBreak(Scene):
    def construct(self):
        """Phase wave with m=1.7 shows visible discontinuity at join point."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("m = 1.7: wave has a jump at the join",
                     font=SERIF, color=INK, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Left: ring with m=1.7 wave (crimson, open/broken)
        cx = -2.0
        ring = _make_ring_outline(ring_radius=1.8, center=RIGHT * cx, color=INK)
        nucleus = Dot(RIGHT * cx, color=INK, radius=0.10)
        nucleus.set_stroke(width=0, opacity=0)
        self.play(Create(ring), FadeIn(nucleus), run_time=0.5)

        wave_bad = _make_ring_wave(m_val=1.7, color=CRIMSON, stroke_width=2.8,
                                   ring_radius=1.8, wave_amplitude=0.30,
                                   center=RIGHT * cx)
        self.play(Create(wave_bad), run_time=1.2)

        # Show start and end points at phi=0 and phi=2pi
        # Start point: angle=0, wave at cos(0)=1 -> r = 1.8 + 0.30
        r_start = 1.8 + 0.30 * np.cos(0)
        r_end = 1.8 + 0.30 * np.cos(1.7 * 2 * np.pi)
        start_pt = RIGHT * cx + RIGHT * r_start
        end_pt = RIGHT * cx + RIGHT * r_end

        start_dot = Dot(start_pt, color=TEAL, radius=0.13)
        start_dot.set_stroke(width=0, opacity=0)
        end_dot = Dot(end_pt, color=CRIMSON, radius=0.13)
        end_dot.set_stroke(width=0, opacity=0)

        self.play(FadeIn(start_dot), FadeIn(end_dot), run_time=0.4)

        # Jump marker
        jump_seg = DashedLine(start_pt, end_pt,
                              color=CRIMSON, stroke_width=2.5, dash_length=0.1)
        jump_seg.set_stroke(color=CRIMSON, width=2.5, opacity=1)
        jump_lbl = Text("jump!", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        jump_lbl.move_to(RIGHT * cx + RIGHT * 2.7 + UP * 0.4)
        self.play(Create(jump_seg), FadeIn(jump_lbl), run_time=0.6)

        # Right side labels
        m_lbl = Text("m = 1.7", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        m_lbl.move_to(RIGHT * 3.2 + UP * 2.0)

        mismatch_lbl = Text("1.7 cycles -- not complete", font=DISPLAY, color=CRIMSON,
                            font_size=20)
        mismatch_lbl.move_to(RIGHT * 3.2 + UP * 1.0)

        broken_lbl = Text("Endpoint does not equal\nStart point", font=DISPLAY,
                          color=CRIMSON, font_size=20, line_spacing=1.2)
        broken_lbl.move_to(RIGHT * 3.2 + UP * 0.0)

        status = Text("Physics rejects this", font=DISPLAY, color=CRIMSON,
                      font_size=24, weight=BOLD)
        status.move_to(RIGHT * 3.2 + DOWN * 1.4)
        status_box = Rectangle(width=4.0, height=0.7, color=CRIMSON, fill_opacity=0.08)
        status_box.set_stroke(CRIMSON, width=1.5)
        status_box.move_to(RIGHT * 3.2 + DOWN * 1.4)

        self.play(FadeIn(m_lbl), run_time=0.4)
        self.play(FadeIn(mismatch_lbl), FadeIn(broken_lbl), run_time=0.5)
        self.play(Create(status_box), FadeIn(status), run_time=0.5)

        self.wait(_dur("B07") - 4.6)


# ── B08 THE IMPLICATION — regularity condition, not postulate ─────────────────
class B08_RegularityCondition(Scene):
    def construct(self):
        """Compare: textbook 'rule' vs. derived regularity condition."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("This is a regularity condition, not a postulate",
                     font=SERIF, color=INK, font_size=27, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Two columns: textbook rule vs. derived
        col_l = -3.3
        col_r = 2.8

        # Left: textbook box (cross it out)
        tb_box = Rectangle(width=4.5, height=2.2, color=CRIMSON, fill_opacity=0.07)
        tb_box.set_stroke(CRIMSON, width=1.5)
        tb_box.move_to(RIGHT * col_l + UP * 0.8)
        tb_hdr = Text("Textbook rule", font=DISPLAY, color=CRIMSON, font_size=20,
                      weight=BOLD)
        tb_hdr.move_to(RIGHT * col_l + UP * 1.9)
        tb_body = Text("m is an integer\n(assumed)", font=DISPLAY, color=CRIMSON,
                       font_size=22, line_spacing=1.3)
        tb_body.move_to(RIGHT * col_l + UP * 0.8)
        self.play(Create(tb_box), FadeIn(tb_hdr), run_time=0.5)
        self.play(FadeIn(tb_body), run_time=0.4)

        # Right: derived result
        dr_box = Rectangle(width=4.5, height=2.2, color=TEAL, fill_opacity=0.07)
        dr_box.set_stroke(TEAL, width=1.5)
        dr_box.move_to(RIGHT * col_r + UP * 0.8)
        dr_hdr = Text("Derived result", font=DISPLAY, color=TEAL, font_size=20,
                      weight=BOLD)
        dr_hdr.move_to(RIGHT * col_r + UP * 1.9)
        dr_body = Text("m is an integer\nbecause single-\nvaluedness demands it",
                       font=DISPLAY, color=TEAL, font_size=20, line_spacing=1.3)
        dr_body.move_to(RIGHT * col_r + UP * 0.8)
        self.play(Create(dr_box), FadeIn(dr_hdr), run_time=0.5)
        self.play(FadeIn(dr_body), run_time=0.4)

        # Arrow from left to right
        arrow = Arrow(np.array([-1.1, 0.8, 0.0]),
                      np.array([0.6, 0.8, 0.0]),
                      buff=0, stroke_width=2.5, color=INK,
                      max_tip_length_to_length_ratio=0.20)
        self.play(Create(arrow), run_time=0.4)

        # Bottom: drum head analogy
        analogy_lbl = Text("Same logic rules a vibrating drum head's nodal patterns",
                           font=DISPLAY, color=INK, font_size=20)
        analogy_lbl.move_to(DOWN * 2.4)
        analogy_box = Rectangle(width=7.5, height=0.6, color=SLATE, fill_opacity=0.07)
        analogy_box.set_stroke(SLATE, width=1.0)
        analogy_box.move_to(DOWN * 2.4)
        self.play(Create(analogy_box), FadeIn(analogy_lbl), run_time=0.5)

        self.wait(_dur("B08") - 3.7)


# ── B09 STILL·ai — spin-half caveat ──────────────────────────────────────────
class B09_SpinCaveat(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        slate_box = Rectangle(width=12.0, height=6.5, color=SLATE, fill_opacity=0.12)
        slate_box.set_stroke(SLATE, width=1.5)
        slate_box.move_to(UP * 0.2)
        slate_lbl = Text("SLATE · ai image", font=DISPLAY, color=SLATE,
                         font_size=26, weight=BOLD)
        slate_lbl.move_to(UP * 0.2)
        caption = Text("Spin-half: spinors on SU(2) admit half-integers (separate argument)",
                       font=SERIF, color=INK, font_size=20, slant=ITALIC)
        caption.move_to(DOWN * 2.8)
        self.add(bg, slate_box, slate_lbl, caption)
        self.wait(_dur("B09"))


# ── B10 THE EXAMPLE — student tries m=0.7 ───────────────────────────────────
class B10_ExampleFractional(Scene):
    def construct(self):
        """Student tries m=0.7; sees discontinuity; physics rejects it."""
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("A student tries m = 0.7  (illustrative)",
                     font=SERIF, color=INK, font_size=27, slant=ITALIC)
        title.move_to(UP * 3.1)
        self.play(FadeIn(title), run_time=0.5)

        # Ring on left
        cx = -2.5
        ring = _make_ring_outline(ring_radius=1.75, center=RIGHT * cx, color=INK)
        nucleus = Dot(RIGHT * cx, color=INK, radius=0.10)
        nucleus.set_stroke(width=0, opacity=0)
        self.play(Create(ring), FadeIn(nucleus), run_time=0.5)

        # Wave with m=0.7
        wave07 = _make_ring_wave(m_val=0.7, color=CRIMSON, stroke_width=2.8,
                                 ring_radius=1.75, wave_amplitude=0.28,
                                 center=RIGHT * cx)
        self.play(Create(wave07), run_time=1.2)

        # Start and end points
        r0 = 1.75 + 0.28 * np.cos(0)
        r1 = 1.75 + 0.28 * np.cos(0.7 * 2 * np.pi)
        p_start = RIGHT * cx + RIGHT * r0
        p_end = RIGHT * cx + RIGHT * r1

        dot_start = Dot(p_start, color=TEAL, radius=0.13)
        dot_start.set_stroke(width=0, opacity=0)
        dot_end = Dot(p_end, color=CRIMSON, radius=0.13)
        dot_end.set_stroke(width=0, opacity=0)
        self.play(FadeIn(dot_start), FadeIn(dot_end), run_time=0.4)

        # Jump line
        jump = DashedLine(p_start, p_end, color=CRIMSON,
                          stroke_width=2.5, dash_length=0.1)
        jump.set_stroke(color=CRIMSON, width=2.5, opacity=1)
        self.play(Create(jump), run_time=0.5)

        # Right side: verdict
        try_lbl = Text("Trial value: m = 0.7", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight=BOLD)
        try_lbl.move_to(RIGHT * 3.0 + UP * 1.8)

        disc_lbl = Text("Wavefunction is\nmultivalued at the\njoin point",
                        font=DISPLAY, color=CRIMSON, font_size=20, line_spacing=1.3)
        disc_lbl.move_to(RIGHT * 3.0 + UP * 0.3)

        verdict = Text("Rejected by physics", font=DISPLAY, color=CRIMSON,
                       font_size=24, weight=BOLD)
        verdict.move_to(RIGHT * 3.0 + DOWN * 1.5)
        verdict_box = Rectangle(width=4.2, height=0.7, color=CRIMSON, fill_opacity=0.08)
        verdict_box.set_stroke(CRIMSON, width=1.5)
        verdict_box.move_to(RIGHT * 3.0 + DOWN * 1.5)

        self.play(FadeIn(try_lbl), run_time=0.4)
        self.play(FadeIn(disc_lbl), run_time=0.5)
        self.play(Create(verdict_box), FadeIn(verdict), run_time=0.5)

        self.wait(_dur("B10") - 4.4)


# ── B11 RECAP ─────────────────────────────────────────────────────────────────
class B11_Recap(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height,
                       color=GROUND, fill_opacity=1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight=BOLD)
        eyebrow.move_to(UP * 1.8)
        headline = Text("Single-valuedness\nforces m to be\nan integer.",
                        font=SERIF, color=INK, font_size=36, line_spacing=1.25)
        headline.move_to(UP * 0.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(headline), run_time=0.8)
        self.wait(_dur("B11") - 1.3)
