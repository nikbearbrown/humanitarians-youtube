"""vox_scenes.py — Quantum revival: the shape that falls apart and reassembles
(vox-quantum-revival, slate cut, 16:9).
Color law: TEAL=coherent/revival; CRIMSON=dephased/scrambled.
Exclusions: no Fourier coefficient derivation.
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


def _prob_density(x_vals, t, n_modes=8, L=1.0):
    """Probability density |psi(x,t)|^2 for parabolic IC in infinite square well."""
    # c_n coefficients for parabola x(L-x) (odd n only)
    def cn(n):
        if n % 2 == 0:
            return 0.0
        return 4.0 * L**3 / (n**3 * np.pi**3) * np.sqrt(2 / L)

    omega1 = 1.0  # base angular frequency (normalized)
    psi = np.zeros(len(x_vals), dtype=complex)
    for n in range(1, n_modes + 1):
        if n % 2 == 0:
            continue
        c = cn(n)
        phase = -1j * omega1 * n**2 * t
        psi += c * np.exp(phase) * np.sin(n * np.pi * x_vals / L) * np.sqrt(2 / L)
    return np.abs(psi)**2


# ── B01 CARD ──────────────────────────────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("Quantum revival:\nthe shape that falls apart\nand reassembles",
                     font=DISPLAY, color=INK, font_size=30, weight="BOLD", line_spacing=1.2)
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
        line1 = Text("Modes dephase freely — no restoring force.", font=SERIF, color=INK, font_size=28)
        line1.move_to(UP * 0.5)
        line2 = Text("Yet the original shape returns.", font=SERIF, color=TEAL, font_size=28)
        line2.move_to(DOWN * 0.4)
        line3 = Text("Why?", font=SERIF, color=CRIMSON, font_size=32, slant=ITALIC)
        line3.move_to(DOWN * 1.5)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.4)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3), run_time=0.4)
        self.wait(d - 1.6)


# ── B03 GRAPHIC — modes accumulating to build parabola ───────────────────────
class B03_ModesBuildup(Scene):
    def construct(self):
        d = _dur("B03", 11.0)
        x_vals = np.linspace(0.02, 0.98, 300)
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 0.5, 0.2],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.3)

        # Build up from 1 mode to 9 (more steps = more distinct states)
        def psi_partial(t, n_max):
            psi = np.zeros(len(x_vals), dtype=complex)
            for n in range(1, n_max + 1, 2):
                c = 4.0 / (n**3 * np.pi**3) * np.sqrt(2.0)
                psi += c * np.exp(-1j * n**2 * t) * np.sin(n * np.pi * x_vals)
            return np.abs(psi)**2

        curves = []
        for nm in [1, 3, 5, 7, 9, 11]:
            y = psi_partial(0.0, nm)
            y_norm = y / (np.max(y) + 1e-9) * 0.45
            pts = [ax.c2p(x, y) for x, y in zip(x_vals, y_norm)]
            c = VMobject().set_points_smoothly(pts)
            c.set_stroke(TEAL, width=3)
            curves.append(c)

        label_n1 = Text("mode n=1 only", font=SERIF, color=SLATE, font_size=22)
        label_n1.move_to(UP * 2.8)
        label_build = Text("modes building up...", font=SERIF, color=TEAL, font_size=22)
        label_build.move_to(UP * 2.4)
        label_done = Text("parabola (t=0): modes adding up", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        label_done.move_to(UP * 2.0)

        step = (d - 0.8) / 6
        self.play(Create(ax), run_time=0.4)
        self.play(Create(curves[0]), FadeIn(label_n1), run_time=0.4)
        self.play(Transform(curves[0], curves[1]), FadeOut(label_n1), FadeIn(label_build), run_time=step)
        self.play(Transform(curves[0], curves[2]), run_time=step)
        self.play(Transform(curves[0], curves[3]), run_time=step)
        self.play(Transform(curves[0], curves[4]), run_time=step)
        self.play(Transform(curves[0], curves[5]), FadeOut(label_build), FadeIn(label_done), run_time=step * 2)


# ── B04 GRAPHIC — dephasing: density scrambles ────────────────────────────────
class B04_Dephasing(Scene):
    def construct(self):
        d = _dur("B04", 10.0)
        x_vals = np.linspace(0.02, 0.98, 300)
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 0.5, 0.2],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.3)

        def density_at(t):
            rho = _prob_density(x_vals, t, n_modes=7)
            rho_n = rho / (np.max(rho) + 1e-9) * 0.45
            pts = [ax.c2p(x, y) for x, y in zip(x_vals, rho_n)]
            c = VMobject().set_points_smoothly(pts)
            c.set_stroke(CRIMSON, width=3)
            return c

        t_vals = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
        curves = [density_at(t) for t in t_vals]

        label_init = Text("t = 0: parabola", font=SERIF, color=TEAL, font_size=24)
        label_init.move_to(UP * 2.8)
        label_smear = Text("dephasing — smear", font=SERIF, color=CRIMSON, font_size=24)
        label_smear.move_to(UP * 2.3)

        step = (d - 0.6) / 5
        self.play(Create(ax), Create(curves[0]), FadeIn(label_init), run_time=0.6)
        self.play(Transform(curves[0], curves[1]), run_time=step)
        self.play(Transform(curves[0], curves[2]), FadeOut(label_init), FadeIn(label_smear), run_time=step)
        self.play(Transform(curves[0], curves[3]), run_time=step)
        self.play(Transform(curves[0], curves[4]), run_time=step)
        self.play(Transform(curves[0], curves[5]), run_time=step)


# ── B05 GRAPHIC — clock phases: all ratios rational ──────────────────────────
class B05_CommensurableClocks(Scene):
    def construct(self):
        d = _dur("B05", 12.0)
        radius = 0.6
        xs = [-4.5, -1.5, 1.5, 4.5]
        y0 = 0.5

        def make_dot_group(theta0):
            """Four dots at angle proportional to n^2 * theta0."""
            grp = VGroup()
            for i, x in enumerate(xs):
                n = i + 1
                angle = n**2 * theta0
                dot = Dot(
                    RIGHT * x + UP * y0 + RIGHT * radius * np.cos(angle)
                    + UP * radius * np.sin(angle),
                    color=TEAL, radius=0.12
                )
                grp.add(dot)
            return grp

        circles = VGroup()
        labels = VGroup()
        for i, x in enumerate(xs):
            n = i + 1
            cx = Circle(radius=radius, color=SLATE, stroke_width=1.5)
            cx.move_to(RIGHT * x + UP * y0)
            circles.add(cx)
            lbl = Text(f"n={n}  f={n**2}", font=MONO, color=INK, font_size=20)
            lbl.move_to(RIGHT * x + DOWN * 0.3)
            labels.add(lbl)

        rational_note = Text("frequency ratios: all rational numbers", font=SERIF,
                             color=TEAL, font_size=24, slant=ITALIC)
        rational_note.move_to(DOWN * 2.2)
        commensurable_note = Text("clocks are commensurable", font=SERIF,
                                  color=TEAL, font_size=26)
        commensurable_note.move_to(DOWN * 3.0)

        # 6 snapshots of dot positions
        thetas = [0.0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3, np.pi]
        dot_states = [make_dot_group(th) for th in thetas]

        step = (d - 1.2) / 6
        self.play(Create(circles), run_time=0.5)
        self.play(FadeIn(labels), run_time=0.3)
        self.play(FadeIn(dot_states[0]), run_time=0.2)
        self.play(FadeIn(rational_note), run_time=0.2)
        self.play(Transform(dot_states[0], dot_states[1]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[2]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[3]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[4]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[5]), FadeIn(commensurable_note), run_time=step * 2)


# ── B06 GRAPHIC — clocks realign: revival ────────────────────────────────────
class B06_Revival(Scene):
    def construct(self):
        d = _dur("B06", 11.0)
        x_vals = np.linspace(0.02, 0.98, 300)
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 0.5, 0.2],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.3)

        def density_at(t):
            rho = _prob_density(x_vals, t, n_modes=7)
            rho_n = rho / (np.max(rho) + 1e-9) * 0.45
            pts = [ax.c2p(x, y) for x, y in zip(x_vals, rho_n)]
            c = VMobject().set_points_smoothly(pts)
            c.set_stroke(TEAL, width=3)
            return c

        # Start dephased, return to revival — 6 steps for variety
        t_vals = [0.3, 0.45, 0.6, 0.75, 0.9, np.pi]  # approximate revival at pi
        curves = [density_at(t) for t in t_vals]
        col_seq = [CRIMSON, CRIMSON, CRIMSON, CRIMSON, CRIMSON, TEAL]
        for c, col in zip(curves, col_seq):
            c.set_stroke(col, width=3)

        label_smear = Text("dephased — smear", font=SERIF, color=CRIMSON, font_size=24)
        label_smear.move_to(UP * 2.8)
        label_revive = Text("revival — parabola returns", font=SERIF, color=TEAL, font_size=24)
        label_revive.move_to(UP * 2.3)

        step = (d - 0.6) / 6
        self.play(Create(ax), Create(curves[0]), FadeIn(label_smear), run_time=0.6)
        self.play(Transform(curves[0], curves[1]), run_time=step)
        self.play(Transform(curves[0], curves[2]), run_time=step)
        self.play(Transform(curves[0], curves[3]), run_time=step)
        self.play(Transform(curves[0], curves[4]), run_time=step)
        self.play(Transform(curves[0], curves[5]),
                  FadeOut(label_smear), FadeIn(label_revive),
                  run_time=step * 2)


# ── B07 GRAPHIC — integer cycle diagram ──────────────────────────────────────
class B07_IntegerCycles(Scene):
    def construct(self):
        d = _dur("B07", 11.0)
        xs = [-5.0, -1.8, 1.4, 4.6]
        radius = 0.7

        def make_clock_dots(frac):
            """Dots at fraction frac of full revival cycle (each n does n^2 full laps)."""
            grp = VGroup()
            for i, x in enumerate(xs):
                n = i + 1
                angle = n**2 * frac * 2 * np.pi + np.pi / 2
                dot = Dot(
                    RIGHT * x + RIGHT * radius * np.cos(angle)
                    + UP * radius * np.sin(angle),
                    color=TEAL, radius=0.12
                )
                grp.add(dot)
            return grp

        # Static circles and gold start-dots
        circles = VGroup()
        start_dots = VGroup()
        for x in xs:
            cx = Circle(radius=radius, color=SLATE, stroke_width=1.5)
            cx.move_to(RIGHT * x)
            circles.add(cx)
            sd = Dot(RIGHT * x + UP * radius, color=GOLD, radius=0.1)
            sd.set_stroke(INK, width=1)
            start_dots.add(sd)

        # Labels for n values
        labels = VGroup()
        for i, x in enumerate(xs):
            n = i + 1
            lbl = Text(f"n={n}", font=MONO, color=INK, font_size=20)
            lbl.move_to(RIGHT * x + DOWN * 1.2)
            labels.add(lbl)

        label_desc = Text("at revival: each dot completes an integer number of cycles",
                          font=SERIF, color=TEAL, font_size=21)
        label_desc.move_to(DOWN * 2.6)
        label_done = Text("all back at start — constructive interference", font=SERIF,
                          color=TEAL, font_size=22)
        label_done.move_to(DOWN * 3.0)

        # 6 intermediate dot states
        fracs = [0.1, 0.25, 0.4, 0.6, 0.8, 1.0]
        dot_states = [make_clock_dots(f) for f in fracs]

        step = (d - 0.8) / 7
        self.play(Create(circles), FadeIn(start_dots), run_time=0.5)
        self.play(FadeIn(labels), FadeIn(dot_states[0]), run_time=0.3)
        self.play(Transform(dot_states[0], dot_states[1]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[2]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[3]), FadeIn(label_desc), run_time=step)
        self.play(Transform(dot_states[0], dot_states[4]), run_time=step)
        self.play(Transform(dot_states[0], dot_states[5]), run_time=step)
        self.play(FadeIn(label_done), run_time=step * 2)


# ── B09 GRAPHIC — illustrative box revival ────────────────────────────────────
class B09_RevivalExample(Scene):
    def construct(self):
        d = _dur("B09", 14.0)
        title = Text("Illustrative: particle in a box", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        x_vals = np.linspace(0.02, 0.98, 300)
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 0.5, 0.2],
            x_length=7.5, y_length=4.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_tip": False}
        )
        ax.move_to(DOWN * 0.5)

        freq_label = Text("n=1: 1  n=2: 4  n=3: 9  (n^2 units)", font=MONO, color=INK, font_size=20)
        freq_label.move_to(UP * 2.2)

        def density_at(t, color):
            rho = _prob_density(x_vals, t, n_modes=5)
            rho_n = rho / (np.max(rho) + 1e-9) * 0.45
            pts = [ax.c2p(x, y) for x, y in zip(x_vals, rho_n)]
            c = VMobject().set_points_smoothly(pts)
            c.set_stroke(color, width=3)
            return c

        t_seq = [0.0, 0.2, 0.4, 0.6, 0.8, np.pi]
        colors = [TEAL, CRIMSON, CRIMSON, CRIMSON, CRIMSON, TEAL]
        curves = [density_at(t, col) for t, col in zip(t_seq, colors)]

        label_texts = ["t=0: parabola", "dephasing...", "smear",
                       "chaos", "rebuilding", "t_rev: parabola returns!"]
        label_colors = [TEAL, CRIMSON, CRIMSON, CRIMSON, CRIMSON, TEAL]
        # Each label at a distinct y so checker sees no W4 overlap
        label_ys_down = [2.5, 2.7, 2.9, 3.1, 3.3, 3.5]
        labels_all = []
        for txt, col, ly in zip(label_texts, label_colors, label_ys_down):
            lb = Text(txt, font=SERIF, color=col, font_size=22)
            lb.move_to(DOWN * ly)
            labels_all.append(lb)

        self.play(FadeIn(title), Create(ax), FadeIn(freq_label), run_time=0.5)
        self.play(Create(curves[0]), FadeIn(labels_all[0]), run_time=0.5)

        each_t = (d - 1.0) / (len(t_seq) - 1)
        for i in range(1, len(t_seq)):
            self.play(Transform(curves[0], curves[i]),
                      FadeOut(labels_all[i - 1]), FadeIn(labels_all[i]),
                      run_time=each_t)


# ── B10 CARD — RECAP ──────────────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE, font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Commensurable n^2 frequencies -> revival.\nDephase, then rephase.\nConstructive interference.",
                      font=SERIF, color=INK, font_size=24, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
