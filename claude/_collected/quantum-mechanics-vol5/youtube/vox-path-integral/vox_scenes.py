"""vox_scenes.py — All paths at once, and only the classical one survives
(vox-path-integral, slate cut, 16:9).
Color law: TEAL=constructive/classical; CRIMSON=canceling/off-paths; GOLD=resultant.
Exclusions: no Euler-Lagrange derivation.
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


def _wiggly_path(x0, x1, y0, y1, amplitude, n_bumps, n_pts=60):
    """Generate a wiggly path from (x0,y0) to (x1,y1) with sine bumps."""
    t = np.linspace(0, 1, n_pts)
    x = x0 + (x1 - x0) * t
    # Envelope that goes to zero at endpoints
    envelope = np.sin(np.pi * t)
    y_base = y0 + (y1 - y0) * t
    y = y_base + amplitude * envelope * np.sin(n_bumps * np.pi * t)
    return list(zip(x, y))


def _make_path_curve(pts, color=TEAL, width=2.5):
    coords = [RIGHT * x + UP * y for x, y in pts]
    c = VMobject()
    c.set_points_smoothly(coords)
    c.set_stroke(color, width=width)
    return c


def _phasor_arrow(center, angle, length=0.5, color=TEAL):
    """A small arrow representing a phasor at given angle."""
    tip = center + RIGHT * length * np.cos(angle) + UP * length * np.sin(angle)
    arr = Arrow(center, tip, buff=0, stroke_width=2.5, color=color,
                max_tip_length_to_length_ratio=0.4)
    return arr


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("All paths at once,\nand only the classical one survives",
                     font=DISPLAY, color=INK, font_size=32, weight="BOLD", line_spacing=1.2)
        title.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(d - 1.3)


# ── B02 CARD — THE QUESTION ───────────────────────────────────────────────────
class B02_TheQuestion(Scene):
    def construct(self):
        d = _dur("B02", 10.0)
        chip = LabelChip("THE QUESTION", accent=CRIMSON, size=24)
        chip.move_to(UP * 2.8)
        line1 = Text("All paths taken.", font=SERIF, color=CRIMSON, font_size=28)
        line1.move_to(UP * 0.8)
        line2 = Text("One path seen.", font=SERIF, color=TEAL, font_size=28)
        line2.move_to(DOWN * 0.1)
        line3 = Text("Why does only the classical path survive?", font=SERIF,
                     color=INK, font_size=24, slant=ITALIC)
        line3.move_to(DOWN * 1.2)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(d - 1.6)


# ── B03 GRAPHIC — phasors introduced: each path has a phasor ─────────────────
class B03_PhasorIntro(Scene):
    def construct(self):
        d = _dur("B03", 11.0)

        # Show 5 paths from A to B with associated phasors
        ax = LEFT * 5.5
        bx = RIGHT * 2.5
        ay = 0.0
        by = 0.0

        n_paths = 5
        amplitudes = [-0.8, -0.4, 0.0, 0.4, 0.8]  # 0.0 = classical
        colors = [CRIMSON, CRIMSON, TEAL, CRIMSON, CRIMSON]
        # Phase angles: classical = 0, others spread out
        phases = [2.8, 1.4, 0.0, -1.4, -2.8]

        path_curves = []
        phasors = []
        phasor_centers_x = [ax[0] + 1.0 + i * 1.2 for i in range(n_paths)]

        for i, (amp, col, ph) in enumerate(zip(amplitudes, colors, phases)):
            pts = _wiggly_path(ax[0], bx[0], ay, by, amp, 2)
            c = _make_path_curve(pts, color=col, width=2.0 if col == CRIMSON else 3.0)
            path_curves.append(c)

        # Phasor cluster below paths
        phasor_y = -2.0
        phasor_grp = VGroup()
        for i, (ph, col) in enumerate(zip(phases, colors)):
            cx = -2.0 + i * 1.0
            center = RIGHT * cx + UP * phasor_y
            arr = _phasor_arrow(center, ph, length=0.45, color=col)
            phasor_grp.add(arr)

        # Endpoint dots
        dot_a = Dot(ax, color=INK, radius=0.15)
        dot_b = Dot(bx, color=INK, radius=0.15)
        label_a = Text("A", font=MONO, color=INK, font_size=22)
        label_a.move_to(ax + DOWN * 0.4)
        label_b = Text("B", font=MONO, color=INK, font_size=22)
        label_b.move_to(bx + DOWN * 0.4)

        phasor_label = Text("each path → one phasor (angle = action/hbar)",
                            font=SERIF, color=SLATE, font_size=20)
        phasor_label.move_to(DOWN * 3.0)

        step = (d - 0.3) / 7
        self.play(FadeIn(dot_a), FadeIn(dot_b), FadeIn(label_a), FadeIn(label_b), run_time=0.3)
        self.play(FadeIn(path_curves[2]), run_time=step)  # classical first
        self.play(FadeIn(path_curves[0]), FadeIn(path_curves[1]), run_time=step)
        self.play(FadeIn(path_curves[3]), FadeIn(path_curves[4]), run_time=step)
        self.play(FadeIn(phasor_grp), run_time=step)
        self.play(FadeIn(phasor_label), run_time=step)
        # Show a circle for context
        unit_c = Circle(radius=0.5, color=SLATE, stroke_width=1.0)
        unit_c.move_to(UP * phasor_y + RIGHT * 0.0)
        self.play(Create(unit_c), run_time=step * 2)


# ── B04 GRAPHIC — off-paths: phasors pointing every which way → cancel ────────
class B04_OffPathCancel(Scene):
    def construct(self):
        d = _dur("B04", 11.0)

        # Show off-path phasors pointing in many directions, sum = 0
        n = 8
        phases = np.linspace(0, 2 * np.pi * (1 - 1/n), n)
        colors = [CRIMSON] * n

        phasor_y = 0.3
        center_x = 0.0
        circle = Circle(radius=1.0, color=SLATE, stroke_width=1.2)
        circle.move_to(RIGHT * center_x + UP * phasor_y)

        arrows = []
        for ph in phases:
            center = RIGHT * center_x + UP * phasor_y
            arr = _phasor_arrow(center, ph, length=0.85, color=CRIMSON)
            arrows.append(arr)

        label_cancel = Text("off-path phasors: spread in all directions",
                            font=SERIF, color=CRIMSON, font_size=22)
        label_cancel.move_to(DOWN * 1.8)
        label_sum = Text("sum → zero", font=SERIF, color=CRIMSON, font_size=24, weight="BOLD")
        label_sum.move_to(DOWN * 2.5)

        # Sum vector: near-zero
        sum_arr = Arrow(RIGHT * center_x + UP * phasor_y,
                        RIGHT * center_x + UP * phasor_y + RIGHT * 0.05 + UP * 0.05,
                        buff=0, stroke_width=3, color=CRIMSON)
        zero_dot = Dot(RIGHT * center_x + UP * phasor_y, color=CRIMSON, radius=0.1)

        step = (d - 0.3) / 7
        self.play(Create(circle), run_time=0.3)
        for i in range(0, n, 2):
            self.play(FadeIn(arrows[i]), FadeIn(arrows[i+1]), run_time=step)
        self.play(FadeIn(label_cancel), run_time=step)
        self.play(FadeIn(sum_arr), FadeIn(zero_dot), FadeIn(label_sum), run_time=step)


# ── B05 GRAPHIC — near-classical phasors: nearly same phase → add ─────────────
class B05_NearClassicalAdd(Scene):
    def construct(self):
        d = _dur("B05", 12.0)

        # Show near-classical phasors nearly aligned → large resultant
        n = 7
        phase_center = 0.3  # slightly above zero
        spread = 0.15  # small spread
        phases = np.linspace(phase_center - spread * (n//2), phase_center + spread * (n//2), n)

        circle = Circle(radius=1.0, color=SLATE, stroke_width=1.2)
        circle.move_to(LEFT * 2.5)

        arrows = []
        for ph in phases:
            arr = _phasor_arrow(LEFT * 2.5, ph, length=0.85, color=TEAL)
            arrows.append(arr)

        # Resultant arrow: large, pointing in phase_center direction
        resultant = Arrow(LEFT * 2.5,
                          LEFT * 2.5 + RIGHT * n * 0.85 * np.cos(phase_center) * 0.35
                          + UP * n * 0.85 * np.sin(phase_center) * 0.35,
                          buff=0, stroke_width=5, color=GOLD,
                          max_tip_length_to_length_ratio=0.2)

        label_add = Text("near-classical phasors: nearly aligned",
                         font=SERIF, color=TEAL, font_size=22)
        label_add.move_to(RIGHT * 2.0 + UP * 1.5)
        label_result = Text("sum → large resultant", font=SERIF, color=TEAL, font_size=24)
        label_result.move_to(RIGHT * 2.0 + UP * 0.5)

        # Show "stationary action" concept with a small rectangle
        stat_box = Rectangle(width=3.5, height=0.7, color=TEAL, fill_opacity=0.12)
        stat_box.set_stroke(TEAL, width=1.5)
        stat_box.move_to(RIGHT * 2.0 + DOWN * 0.5)
        stat_label = Text("action barely changes here", font=MONO, color=TEAL, font_size=18)
        stat_label.move_to(RIGHT * 2.0 + DOWN * 0.5)

        step = (d - 0.3) / 6
        self.play(Create(circle), run_time=0.3)
        self.play(*[FadeIn(a) for a in arrows[:3]], run_time=step)
        self.play(*[FadeIn(a) for a in arrows[3:]], run_time=step)
        self.play(FadeIn(label_add), run_time=step)
        self.play(FadeIn(resultant), run_time=step)
        self.play(FadeIn(stat_box), FadeIn(stat_label), run_time=step)
        self.play(FadeIn(label_result), run_time=step)


# ── B06 GRAPHIC — classical = stationary phase summary ────────────────────────
class B06_StationaryPhase(Scene):
    def construct(self):
        d = _dur("B06", 11.0)

        # Two side-by-side: OFF (cancel) vs NEAR-CLASSICAL (add)
        # Left: cancel
        circ_l = Circle(radius=0.9, color=CRIMSON, stroke_width=1.2)
        circ_l.move_to(LEFT * 3.5 + UP * 0.5)
        phases_off = np.linspace(0, 2 * np.pi * 0.9, 6)
        arrows_l = VGroup()
        for ph in phases_off:
            arr = _phasor_arrow(LEFT * 3.5 + UP * 0.5, ph, length=0.75, color=CRIMSON)
            arrows_l.add(arr)
        label_l = Text("off-path:\ncancel", font=SERIF, color=CRIMSON, font_size=22,
                       line_spacing=1.2)
        label_l.move_to(LEFT * 3.5 + DOWN * 0.9)

        # Right: add
        circ_r = Circle(radius=0.9, color=TEAL, stroke_width=1.2)
        circ_r.move_to(RIGHT * 3.5 + UP * 0.5)
        phases_near = np.linspace(-0.2, 0.2, 6)
        arrows_r = VGroup()
        for ph in phases_near:
            arr = _phasor_arrow(RIGHT * 3.5 + UP * 0.5, ph, length=0.75, color=TEAL)
            arrows_r.add(arr)
        resultant_r = Arrow(RIGHT * 3.5 + UP * 0.5,
                            RIGHT * 3.5 + UP * 0.5 + RIGHT * 2.2,
                            buff=0, stroke_width=5, color=GOLD,
                            max_tip_length_to_length_ratio=0.15)
        label_r = Text("near-classical:\nadd", font=SERIF, color=TEAL, font_size=22,
                       line_spacing=1.2)
        label_r.move_to(RIGHT * 3.5 + DOWN * 0.9)

        divider = Line(UP * 2.0, DOWN * 2.0, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        conclusion = Text("classical path = stationary action = large quantum amplitude",
                          font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        conclusion.move_to(DOWN * 2.5)

        # Extra geometric shapes for variety
        highlight = Rectangle(width=3.0, height=3.5, color=TEAL, fill_opacity=0.06)
        highlight.set_stroke(TEAL, width=1.5)
        highlight.move_to(RIGHT * 3.5 + UP * 0.0)
        cancel_rect = Rectangle(width=3.0, height=3.5, color=CRIMSON, fill_opacity=0.04)
        cancel_rect.set_stroke(CRIMSON, width=1.0)
        cancel_rect.move_to(LEFT * 3.5 + UP * 0.0)

        step = (d - 0.3) / 7
        self.play(Create(circ_l), Create(circ_r), FadeIn(divider), run_time=0.3)
        self.play(FadeIn(arrows_l), run_time=step)
        self.play(FadeIn(arrows_r), FadeIn(label_l), run_time=step)
        self.play(FadeIn(resultant_r), FadeIn(label_r), run_time=step)
        self.play(FadeIn(highlight), run_time=step)
        self.play(FadeIn(cancel_rect), run_time=step)
        self.play(FadeIn(conclusion), run_time=step * 2)


# ── B07 GRAPHIC — least action emerges from interference ─────────────────────
class B07_LeastActionEmerges(Scene):
    def construct(self):
        d = _dur("B07", 10.0)

        # Path diagram: many wiggly paths, classical highlighted
        ax = LEFT * 5.0
        bx = RIGHT * 3.0
        ay = by = 0.0

        amplitudes = [-1.2, -0.7, -0.3, 0.0, 0.3, 0.7, 1.2]
        colors_p = [CRIMSON, CRIMSON, CRIMSON, TEAL, CRIMSON, CRIMSON, CRIMSON]
        widths = [1.5, 1.5, 1.5, 4.0, 1.5, 1.5, 1.5]

        path_curves = []
        for amp, col, w in zip(amplitudes, colors_p, widths):
            pts = _wiggly_path(ax[0], bx[0], ay, by, amp, 2)
            c = _make_path_curve(pts, color=col, width=w)
            path_curves.append(c)

        dot_a = Dot(ax, color=INK, radius=0.15)
        dot_b = Dot(bx, color=INK, radius=0.15)

        label = Text("least action = region of constructive interference",
                     font=SERIF, color=TEAL, font_size=21, slant=ITALIC)
        label.move_to(DOWN * 2.5)

        # Highlight band around classical path
        band = Rectangle(width=8.2, height=0.7, color=TEAL, fill_opacity=0.12)
        band.set_stroke(TEAL, width=0)
        band.move_to(RIGHT * (-1.0) + UP * 0.0)

        step = (d - 0.3) / 6
        self.play(FadeIn(dot_a), FadeIn(dot_b), run_time=0.3)
        for c in path_curves[1:6:2]:
            self.play(FadeIn(c), run_time=step)
        for c in [path_curves[0], path_curves[2], path_curves[4], path_curves[6]]:
            self.play(FadeIn(c), run_time=step)
        self.play(FadeIn(band), run_time=step)
        self.play(FadeIn(label), run_time=step * 2)


# ── B09 GRAPHIC — illustrative: 5 paths, phasor sum ──────────────────────────
class B09_FivePathExample(Scene):
    def construct(self):
        d = _dur("B09", 13.0)

        title = Text("Illustrative: 5 paths A through E",
                     font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        # Phasor phases: A and E are opposite, B and D flank C
        path_names = ["A", "B", "C", "D", "E"]
        phases = [np.pi, np.pi * 0.5, 0.0, -np.pi * 0.5, -np.pi]
        colors_p = [CRIMSON, CRIMSON, TEAL, CRIMSON, CRIMSON]

        circle = Circle(radius=1.1, color=SLATE, stroke_width=1.2)
        circle.move_to(LEFT * 3.5)

        phasors_drawn = []
        phasor_labels = []
        for name, ph, col in zip(path_names, phases, colors_p):
            arr = _phasor_arrow(LEFT * 3.5, ph, length=0.95, color=col)
            phasors_drawn.append(arr)
            lbl = Text(name, font=MONO, color=col, font_size=18)
            tip = LEFT * 3.5 + RIGHT * 1.1 * np.cos(ph) + UP * 1.1 * np.sin(ph)
            lbl.move_to(tip + RIGHT * 0.2 + UP * 0.1)
            phasor_labels.append(lbl)

        # Cancellation: A and E
        cancel_box = Rectangle(width=3.0, height=0.6, color=CRIMSON, fill_opacity=0.1)
        cancel_box.set_stroke(CRIMSON, width=1.5)
        cancel_box.move_to(RIGHT * 1.5 + UP * 1.2)
        cancel_label = Text("A + E = 0  (opposite phases)", font=MONO, color=CRIMSON, font_size=18)
        cancel_label.move_to(RIGHT * 1.5 + UP * 1.2)

        # Addition: B, C, D
        add_box = Rectangle(width=3.0, height=0.6, color=TEAL, fill_opacity=0.1)
        add_box.set_stroke(TEAL, width=1.5)
        add_box.move_to(RIGHT * 1.5 + UP * 0.2)
        add_label = Text("B + C + D add: resultant = C direction",
                         font=MONO, color=TEAL, font_size=18)
        add_label.move_to(RIGHT * 1.5 + UP * 0.2)

        # Resultant arrow
        resultant = Arrow(RIGHT * 1.5 + DOWN * 0.8,
                          RIGHT * 1.5 + DOWN * 0.8 + RIGHT * 1.8,
                          buff=0, stroke_width=5, color=GOLD,
                          max_tip_length_to_length_ratio=0.2)
        result_lbl = Text("resultant: along C (classical)", font=SERIF, color=TEAL, font_size=20)
        result_lbl.move_to(RIGHT * 2.5 + DOWN * 1.4)

        step = (d - 0.3) / 7
        self.play(FadeIn(title), Create(circle), run_time=0.3)
        for arr, lbl in zip(phasors_drawn[:3], phasor_labels[:3]):
            self.play(FadeIn(arr), FadeIn(lbl), run_time=step)
        for arr, lbl in zip(phasors_drawn[3:], phasor_labels[3:]):
            self.play(FadeIn(arr), FadeIn(lbl), run_time=step)
        self.play(FadeIn(cancel_box), FadeIn(cancel_label), run_time=step)
        self.play(FadeIn(add_box), FadeIn(add_label), run_time=step)
        self.play(FadeIn(resultant), FadeIn(result_lbl), run_time=step)


# ── B10 CARD — RECAP ──────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Stationary action = constructive interference.\nAll other paths cancel.\nClassical physics emerges.",
                      font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
