"""vox_scenes.py — Eigenvectors: the directions a matrix can't turn
(vox-eigen-directions, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat. B08 is STILL·ai — no scene.
Color law: TEAL = eigenvectors (invariant); CRIMSON = all other rotating arrows.
GOLD = eigenvalue stretch marker (B06 only).
Exclusions: no characteristic polynomial algebra on screen.
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


def _arrow(start, end, color, sw=3.5, tip=0.2):
    return Arrow(start, end, color=color, buff=0,
                 stroke_width=sw, tip_length=tip)


# ── B01 CARD — title card (COLD OPEN) ────────────────────────────────────────
class B01_TitleCard(Scene):
    def construct(self):
        d = _dur("B01", 8.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 1.8)
        title = Text("Eigenvectors:\nthe directions a matrix can't turn",
                     font=DISPLAY, color=INK, font_size=40, weight="BOLD",
                     line_spacing=1.2)
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
        line1 = Text("Every matrix rotates most arrows —", font=SERIF, color=INK, font_size=30)
        line1.move_to(UP * 0.6)
        line2 = Text("but some it can only stretch.", font=SERIF, color=TEAL, font_size=30)
        line2.move_to(DOWN * 0.2)
        line3 = Text("Why must those directions exist?", font=SERIF, color=CRIMSON,
                     font_size=28, slant=ITALIC)
        line3.move_to(DOWN * 1.3)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.5)
        self.play(FadeIn(line2), run_time=0.5)
        self.play(FadeIn(line3), run_time=0.5)
        self.wait(d - 1.9)


# ── B03 GRAPHIC — fan of arrows transformed ──────────────────────────────────
class B03_FanTransform(Scene):
    def construct(self):
        d = _dur("B03", 11.0)
        # illustrative matrix A = [[2, 1],[1, 2]] — has eigenvectors along (1,1) and (1,-1)
        A = np.array([[2.0, 1.0], [1.0, 2.0]])
        n = 8
        scale = 1.4
        origin = LEFT * 2.0

        # create a fan of 8 arrows
        angles = [i * TAU / n for i in range(n)]
        arrows_before = []
        arrows_after = []
        for theta in angles:
            v = np.array([np.cos(theta), np.sin(theta)])
            Av = A @ v
            Av_n = Av / np.linalg.norm(Av)
            arrows_before.append(_arrow(origin,
                                        origin + RIGHT * v[0] * scale + UP * v[1] * scale,
                                        SLATE, sw=2.5))
            arrows_after.append(_arrow(origin,
                                       origin + RIGHT * Av_n[0] * scale + UP * Av_n[1] * scale,
                                       CRIMSON, sw=2.5))

        label_before = Text("before", font=MONO, color=SLATE, font_size=22)
        label_before.move_to(LEFT * 2.0 + UP * 2.8)
        label_after = Text("after", font=MONO, color=CRIMSON, font_size=22)
        label_after.move_to(LEFT * 2.0 + UP * 3.5)  # distinct y

        dot = Dot(origin, color=INK, radius=0.08)
        self.play(FadeIn(dot), run_time=0.3)
        for a in arrows_before:
            self.play(GrowArrow(a), run_time=0.05)
        self.play(FadeIn(label_before), run_time=0.3)
        # transform all
        anims = [Transform(ab, aa) for ab, aa in zip(arrows_before, arrows_after)]
        self.play(*anims, Transform(label_before, label_after),
                  run_time=d - 1.2, rate_func=smooth)


# ── B04 GRAPHIC — show one arrow staying on its line ─────────────────────────
class B04_InvariantSearch(Scene):
    def construct(self):
        d = _dur("B04", 10.0)
        A = np.array([[2.0, 1.0], [1.0, 2.0]])
        origin = LEFT * 2.0
        scale = 1.6

        # eigenvectors: (1/sqrt2, 1/sqrt2) and (1/sqrt2, -1/sqrt2)
        e1 = np.array([1.0, 1.0]) / np.sqrt(2)
        e2 = np.array([1.0, -1.0]) / np.sqrt(2)

        # show a non-eigen arrow rotating
        v_gen = np.array([1.0, 0.2]) / np.linalg.norm(np.array([1.0, 0.2]))
        Av_gen = A @ v_gen
        Av_gen_n = Av_gen / np.linalg.norm(Av_gen)

        arr_gen_before = _arrow(origin, origin + RIGHT * v_gen[0] * scale + UP * v_gen[1] * scale,
                                CRIMSON, sw=3)
        arr_gen_after = _arrow(origin, origin + RIGHT * Av_gen_n[0] * scale + UP * Av_gen_n[1] * scale,
                               CRIMSON, sw=3)

        # and one eigenvector staying on line
        arr_eig = _arrow(origin, origin + RIGHT * e1[0] * scale + UP * e1[1] * scale, TEAL, sw=4)
        eig_after = _arrow(origin, origin + RIGHT * e1[0] * scale * 1.3 + UP * e1[1] * scale * 1.3,
                           TEAL, sw=4)

        eq_label = Text("A v = lambda v", font=MONO, color=TEAL, font_size=28)
        eq_label.move_to(RIGHT * 3.5 + UP * 1.0)
        note = Text("stays on its own line", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        note.move_to(RIGHT * 3.5 + DOWN * 0.3)

        dot = Dot(origin, color=INK, radius=0.08)
        self.play(FadeIn(dot), run_time=0.3)
        self.play(GrowArrow(arr_gen_before), GrowArrow(arr_eig), run_time=0.6)
        self.play(Transform(arr_gen_before, arr_gen_after),
                  Transform(arr_eig, eig_after), run_time=(d - 0.9) * 0.5, rate_func=smooth)
        self.play(FadeIn(eq_label), FadeIn(note), run_time=(d - 0.9) * 0.5)


# ── B05 GRAPHIC — full transform showing eigenvectors highlighted ─────────────
class B05_EigenvectorsHighlighted(Scene):
    def construct(self):
        d = _dur("B05", 12.0)
        A = np.array([[2.0, 1.0], [1.0, 2.0]])
        origin = ORIGIN
        scale = 1.5

        n = 6
        angles = [i * TAU / n for i in range(n)]
        e_directions = [np.array([1.0, 1.0]) / np.sqrt(2),
                        np.array([1.0, -1.0]) / np.sqrt(2)]

        # non-eigen arrows (red)
        gen_arrows = []
        gen_afters = []
        for theta in angles:
            v = np.array([np.cos(theta), np.sin(theta)])
            # skip if close to eigenvectors
            if min(abs(np.dot(v, e)) for e in e_directions) > 0.85:
                continue
            Av = A @ v
            Av_n = Av / np.linalg.norm(Av) * scale
            gen_arrows.append(_arrow(origin, origin + RIGHT * v[0] * scale + UP * v[1] * scale,
                                     SLATE, sw=2))
            gen_afters.append(_arrow(origin, origin + RIGHT * Av_n[0] + UP * Av_n[1],
                                     CRIMSON, sw=2))

        # eigenvectors (teal)
        eig1_b = _arrow(origin, origin + RIGHT * e_directions[0][0] * scale + UP * e_directions[0][1] * scale, TEAL, sw=4.5)
        eig1_a = _arrow(origin, origin + RIGHT * e_directions[0][0] * 1.3 * scale + UP * e_directions[0][1] * 1.3 * scale, TEAL, sw=4.5)
        eig2_b = _arrow(origin, origin + RIGHT * e_directions[1][0] * scale + UP * e_directions[1][1] * scale, TEAL, sw=4.5)
        eig2_a = _arrow(origin, origin + RIGHT * e_directions[1][0] * 1.3 * scale + UP * e_directions[1][1] * 1.3 * scale, TEAL, sw=4.5)

        chip1 = LabelChip("EIGENVECTOR", accent=TEAL, size=20)
        chip1.move_to(RIGHT * 3.2 + UP * 2.0)
        chip2 = LabelChip("EIGENVECTOR", accent=TEAL, size=20)
        chip2.move_to(RIGHT * 3.2 + DOWN * 2.0)

        dot = Dot(origin, color=INK, radius=0.08)
        self.play(FadeIn(dot), run_time=0.2)
        for a in gen_arrows:
            self.play(GrowArrow(a), run_time=0.05)
        self.play(GrowArrow(eig1_b), GrowArrow(eig2_b), run_time=0.4)
        # transform
        gen_anims = [Transform(ab, aa) for ab, aa in zip(gen_arrows, gen_afters)]
        self.play(*gen_anims,
                  Transform(eig1_b, eig1_a), Transform(eig2_b, eig2_a),
                  run_time=(d - 0.8) * 0.6, rate_func=smooth)
        self.play(FadeIn(chip1), FadeIn(chip2), run_time=(d - 0.8) * 0.4)


# ── B06 GRAPHIC — eigenvalue = stretch factor ─────────────────────────────────
class B06_EigenvalueStretch(Scene):
    def construct(self):
        d = _dur("B06", 11.0)
        origin = LEFT * 2.5

        # positive eigenvalue: arrow scales up
        v_pos = np.array([1.0, 0.7]) / np.linalg.norm(np.array([1.0, 0.7]))
        scale_before = 1.2
        scale_after = 1.2 * 3.0  # eigenvalue ~3

        pos_b = _arrow(origin, origin + RIGHT * v_pos[0] * scale_before + UP * v_pos[1] * scale_before,
                       TEAL, sw=4)
        pos_a = _arrow(origin, origin + RIGHT * v_pos[0] * scale_after * 0.6 + UP * v_pos[1] * scale_after * 0.6,
                       TEAL, sw=4)

        # negative eigenvalue: arrow flips
        v_neg = np.array([1.0, -0.6]) / np.linalg.norm(np.array([1.0, -0.6]))
        neg_b = _arrow(origin + RIGHT * 5.0,
                       origin + RIGHT * 5.0 + RIGHT * v_neg[0] * 1.2 + UP * v_neg[1] * 1.2,
                       CRIMSON, sw=4)
        neg_a = _arrow(origin + RIGHT * 5.0,
                       origin + RIGHT * 5.0 - RIGHT * v_neg[0] * 1.0 - UP * v_neg[1] * 1.0,
                       CRIMSON, sw=4)

        lam_pos = Text("lambda = +3", font=MONO, color=TEAL, font_size=24)
        lam_pos.move_to(LEFT * 2.5 + DOWN * 2.2)
        lam_neg = Text("lambda = -1", font=MONO, color=CRIMSON, font_size=24)
        lam_neg.move_to(RIGHT * 2.5 + DOWN * 2.2)

        gold_box = Rectangle(width=3.8, height=0.7)
        gold_box.set_fill(GOLD, 0.3).set_stroke(width=0, opacity=0)
        gold_box.move_to(UP * 2.5)
        note = Text("eigenvalue = stretch factor (negative = flip)", font=SERIF,
                    color=INK, font_size=22)
        note.move_to(UP * 2.5)

        dot1 = Dot(origin, color=INK, radius=0.07)
        dot2 = Dot(origin + RIGHT * 5.0, color=INK, radius=0.07)

        self.play(FadeIn(dot1), FadeIn(dot2), FadeIn(gold_box), FadeIn(note), run_time=0.5)
        self.play(GrowArrow(pos_b), GrowArrow(neg_b),
                  FadeIn(lam_pos), FadeIn(lam_neg), run_time=0.6)
        self.play(Transform(pos_b, pos_a), Transform(neg_b, neg_a),
                  run_time=d - 1.1, rate_func=smooth)


# ── B07 GRAPHIC — QM connection: observable → eigenstate ─────────────────────
class B07_QMConnection(Scene):
    def construct(self):
        d = _dur("B07", 11.0)
        # two-column layout: math left, QM right
        left_title = Text("Math", font=DISPLAY, color=SLATE, font_size=26, weight="BOLD")
        left_title.move_to(LEFT * 3.5 + UP * 2.6)
        right_title = Text("Quantum Mechanics", font=DISPLAY, color=TEAL, font_size=26, weight="BOLD")
        right_title.move_to(RIGHT * 2.5 + UP * 2.6)

        divider = Line(UP * 3.0, DOWN * 3.0, color=SLATE, stroke_width=1.0)
        divider.move_to(ORIGIN)

        rows = [
            ("matrix A", "observable (e.g. energy)", UP * 1.4),
            ("eigenvector v", "eigenstate", UP * 0.4),
            ("eigenvalue lambda", "measurement outcome", DOWN * 0.6),
        ]
        for lft, rgt, y in rows:
            lt = Text(lft, font=MONO, color=INK, font_size=24)
            lt.move_to(LEFT * 3.2 + y)
            rt = Text(rgt, font=MONO, color=TEAL, font_size=24)
            rt.move_to(RIGHT * 2.8 + y)
            self.play(FadeIn(lt), FadeIn(rt), run_time=0.5)

        self.play(FadeIn(left_title), FadeIn(right_title), Create(divider), run_time=0.6)
        self.play(left_title.animate.scale(1.05), run_time=(d - 2.1) * 0.5, rate_func=there_and_back)
        self.play(left_title.animate.scale(1.0), run_time=(d - 2.1) * 0.5)


# ── B09 GRAPHIC — illustrative 2x2 example ────────────────────────────────────
class B09_Example2x2(Scene):
    def construct(self):
        d = _dur("B09", 13.0)
        title = Text("Illustrative example", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        title.move_to(UP * 3.2)

        # A = [[2,1],[1,2]]; eigenvectors (1,1)/sqrt2 (lam=3), (1,-1)/sqrt2 (lam=1)
        A = np.array([[2.0, 1.0], [1.0, 2.0]])
        origin = LEFT * 1.0
        scale = 1.3
        n = 8

        arrows_b = []
        arrows_a = []
        colors_b = []
        e_dirs = [np.array([1.0, 1.0]) / np.sqrt(2), np.array([1.0, -1.0]) / np.sqrt(2)]

        for i in range(n):
            theta = i * TAU / n
            v = np.array([np.cos(theta), np.sin(theta)])
            is_eig = any(abs(np.dot(v, e)) > 0.9 for e in e_dirs)
            color = TEAL if is_eig else CRIMSON
            Av = A @ v
            Av_unit = Av / np.linalg.norm(Av)
            arrows_b.append(_arrow(origin,
                                   origin + RIGHT * v[0] * scale + UP * v[1] * scale,
                                   SLATE if not is_eig else TEAL, sw=2.5 if not is_eig else 4))
            arrows_a.append(_arrow(origin,
                                   origin + RIGHT * Av_unit[0] * scale * (1.3 if is_eig else 1.0)
                                   + UP * Av_unit[1] * scale * (1.3 if is_eig else 1.0),
                                   color, sw=2.5 if not is_eig else 4))

        lam_label = Text("eigenvalues: 3 and 1", font=MONO, color=TEAL, font_size=22)
        lam_label.move_to(RIGHT * 4.0 + UP * 0.6)
        count_label = Text("6 arrows rotate\n2 arrows stay on line", font=SERIF, color=INK, font_size=22,
                           line_spacing=1.2)
        count_label.move_to(RIGHT * 4.0 + DOWN * 1.2)

        dot = Dot(origin, color=INK, radius=0.08)
        self.play(FadeIn(title), FadeIn(dot), run_time=0.4)
        for a in arrows_b:
            self.play(GrowArrow(a), run_time=0.04)
        anims = [Transform(ab, aa) for ab, aa in zip(arrows_b, arrows_a)]
        self.play(*anims, run_time=(d - 0.8) * 0.6, rate_func=smooth)
        self.play(FadeIn(lam_label), FadeIn(count_label), run_time=(d - 0.8) * 0.4)


# ── B10 CARD — RECAP endcard ──────────────────────────────────────────────────
class B10_Recap(Scene):
    def construct(self):
        d = _dur("B10", 9.0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, color=SLATE,
                       font_size=22, weight="MEDIUM")
        eyebrow.move_to(UP * 2.5)
        answer = Text("Eigenvectors: invariant directions, only stretched.\nMeasurement = projection onto one.",
                      font=SERIF, color=INK, font_size=26, line_spacing=1.3)
        answer.move_to(ORIGIN)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.8)
        self.wait(d - 1.3)
