"""Manim scenes for "Why Neural Networks Need a Bend" (claude-liam-nonlinearity).

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/nonlinearity_demo.py).
Each scene ends exactly at its beat's measured audio duration.
Each scene class subclasses Scene directly, one per beat (run.sh finds them by regex).
"""
from manim import *
import json
import os
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# GATE A pre-flights an isolated copy of this file; fall back to the reel folder.
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-nonlinearity"))


def _load(rel):
    for base in (HERE, REEL):
        if (base / rel).exists():
            return json.loads((base / rel).read_text(encoding="utf-8"))
    raise FileNotFoundError(rel)


SHEET = _load("beat_sheet.json")
WORDS = _load("mp3/words.json")
EV = _load("demo/evidence.json")
FPS = WORDS.get("fps", 24)
DUR = {b["beat_id"]: float(b.get("actual_duration_s") or 0) for b in SHEET["beats"]}

# Claude palette (CLAUDE-BRAND.md) — one terracotta moment per beat.
PAGE, INK, SOFT, GHOST, SPARK = "#FAF9F5", "#3D3929", "#73705F", "#A9A491", "#D97757"
SERIF, MONO = "EB Garamond", "PT Mono"
config.background_color = PAGE

XOR_X = [(0, 0), (0, 1), (1, 0), (1, 1)]
XOR_Y = [0, 1, 1, 0]


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def cue(bid, phrase, nth=0):
    """Seconds (beat-local) at which `phrase` starts being spoken."""
    words = WORDS["beats"][bid]
    toks = [_norm(w["text"]) for w in words]
    want = [_norm(p) for p in phrase.split()]
    hits = [i for i in range(len(toks) - len(want) + 1) if toks[i:i + len(want)] == want]
    if len(hits) <= nth:
        raise KeyError(f"{bid}: cue {phrase!r} not in narration")
    return words[hits[nth]]["startFrame"] / FPS


class Clock:
    """Narration clock in whole frames (Manim renders ceil(run_time*fps) frames per play/wait)."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        scene.camera.background_color = PAGE

    def at(self, t):
        frames = int(np.floor((t - self.t) * FPS + 1e-6))
        if frames >= 1:
            self.s.wait(frames / FPS)
            self.t += frames / FPS
        elif t - self.t < -0.05:
            print(f"[clock] {self.bid}: running {self.t - t:.2f}s late at t={t:.2f}")

    def play(self, *anims, rt=1.0):
        frames = max(1, int(np.ceil(rt * FPS - 1e-6)))
        self.s.play(*anims, run_time=frames / FPS)
        self.t += frames / FPS

    def go(self, phrase, *anims, rt=1.0, nth=0, lead=0.15):
        self.at(max(0.0, cue(self.bid, phrase, nth) - lead))
        self.play(*anims, rt=rt)

    def until(self, phrase, nth=0, lead=0.25, floor=0.5):
        """Run time that fills the gap until `phrase` (for long continuous moves)."""
        return max(floor, cue(self.bid, phrase, nth) - lead - self.t)

    def end(self):
        self.at(DUR[self.bid])


def label(s, size=36, color=INK, font=SERIF):
    return Text(s, font=font, font_size=size, color=color)


def num(s, size=36, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def tex(s, size=48, color=INK):
    return MathTex(s, font_size=size, color=color)


def g(v):
    """Number for on-screen Text (true minus sign)."""
    return f"{v:g}".replace("-", "−")


def V(v):
    """Any point-like to a float vector (the GATE A geometry stub returns placeholders)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def P(x, y):
    return [float(x), float(y), 0.0]


def box(part, pad=0.16, min_w=0.42, min_h=1.0, color=SPARK):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '-')."""
    w = max(float(getattr(part, "width", 0.5)) + pad, min_w)
    h = max(float(getattr(part, "height", 0.5)) + pad, min_h)
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color,
                            stroke_width=6).move_to(V(part.get_center()).tolist())


def bmat(m):
    return r"\begin{bmatrix}" + r"\\".join("&".join(str(a) for a in row) for row in m) + r"\end{bmatrix}"


def bcol(v):
    return r"\begin{bmatrix}" + r"\\".join(str(a) for a in v) + r"\end{bmatrix}"


def xor_marker(target, at, r=0.2):
    """Zeros are hollow ink rings, ones are filled ink dots (shape, not colour, carries the class)."""
    if target:
        return Dot(point=at, radius=r, color=INK)
    return Circle(radius=r, color=INK, stroke_width=5).move_to(at)


# --------------------------------------------------------------------------- B02
class B02_TwoMoves(Scene):
    def construct(self):
        c = Clock(self, "B02")
        O = np.array([-3.4, 0.0, 0.0])
        U = 0.92
        lines = VGroup()
        for k in np.arange(-2.0, 2.01, 0.5):
            if abs(k) < 1e-9:
                continue
            lines.add(Line(P(O[0] + U * k, O[1] - 2 * U), P(O[0] + U * k, O[1] + 2 * U), color=SOFT, stroke_width=3))
            lines.add(Line(P(O[0] - 2 * U, O[1] + U * k), P(O[0] + 2 * U, O[1] + U * k), color=SOFT, stroke_width=3))
        axx = Line(P(O[0] - 2 * U, O[1]), P(O[0] + 2 * U, O[1]), color=INK, stroke_width=5)
        axy = Line(P(O[0], O[1] - 2 * U), P(O[0], O[1] + 2 * U), color=INK, stroke_width=5)
        grid = VGroup(lines, axx, axy)
        for m in [*lines, axx, axy]:
            m.insert_n_curves(48)

        head_l = VGroup(label("layer", 36), tex(r"\mathbf{x}\mapsto W\mathbf{x}", 44)).arrange(RIGHT, buff=0.3)
        head_l.move_to(P(-3.4, 2.85))
        keep = label("straight stays straight", 32, SOFT).move_to(P(-3.4, -2.7))

        # ReLU panel: z in [-2, 2], y in [-0.5, 2]
        cx, cy, xl, yl = 3.3, -0.1, 4.4, 3.4
        kx, ky = xl / 4.0, yl / 2.5
        o = P(cx, cy + (0.0 - 0.75) * ky)            # axes origin (z=0, y=0) in scene units
        ax = VGroup(Arrow(P(cx - xl / 2, o[1]), P(cx + xl / 2, o[1]), buff=0, color=INK, stroke_width=4,
                          max_tip_length_to_length_ratio=0.06),
                    Arrow(P(cx, cy - yl / 2), P(cx, cy + yl / 2), buff=0, color=INK, stroke_width=4,
                          max_tip_length_to_length_ratio=0.08))
        relu_l = Line(P(o[0] - 2 * kx, o[1]), o, color=INK, stroke_width=7)
        relu_r = Line(o, P(o[0] + 1.9 * kx, o[1] + 1.9 * ky), color=INK, stroke_width=7)
        head_r = VGroup(label("bend", 36), tex(r"\mathrm{ReLU}(z)=\max(0,\,z)", 42)).arrange(RIGHT, buff=0.3)
        head_r.move_to(P(3.2, 2.85))
        neg = label("negatives → 0", 32, SOFT).move_to(P(1.95, o[1] - 0.45))
        pos = label("positives pass", 32, SOFT).move_to(P(4.6, o[1] - 0.45))

        slot = box(head_r[0], min_h=0.75, color=INK)

        A = np.array([[0.9, 0.5], [-0.35, 0.85]])
        ext = np.abs(A).sum(axis=1) * 2 * U          # positive half-extents of the sheared grid

        def fold(p):
            return np.array([O[0] + max(p[0] - O[0], 0.0), O[1] + max(p[1] - O[1], 0.0), 0.0])

        crease = VGroup(Line(P(O[0], O[1]), P(O[0] + ext[0], O[1]), color=SPARK, stroke_width=8),
                        Line(P(O[0], O[1]), P(O[0], O[1] + ext[1]), color=SPARK, stroke_width=8))

        c.at(0.2)
        c.play(Create(grid), Create(ax), rt=1.2)
        c.go("The first is a layer", FadeIn(head_l, shift=DOWN * 0.2), rt=0.6)
        c.go("stretch rotate and shear", grid.animate.apply_matrix(A, about_point=O), rt=1.5)
        c.go("straight lines stay straight", FadeIn(keep, shift=UP * 0.2), rt=0.5)
        c.go("The second is the bend", FadeIn(head_r, shift=DOWN * 0.2), rt=0.6)
        c.go("keep positive numbers", Create(relu_r), FadeIn(pos), rt=0.6)
        c.go("flatten negatives to zero", Create(relu_l), FadeIn(neg), rt=0.6)
        c.go("creases the plane", grid.animate.apply_function(fold), FadeOut(keep), rt=1.0)
        c.play(Create(crease), rt=0.3)
        c.go("layer bend layer", Create(slot), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B03
class B03_Collapse(Scene):
    def construct(self):
        c = Clock(self, "B03")
        C = EV["collapse"]
        top = VGroup(tex(r"W_1=" + bmat(C["W1"]), 50), tex(r"W_2=" + bmat(C["W2"]), 50),
                     tex(r"\mathbf{x}=" + bcol(C["x"]), 50)).arrange(RIGHT, buff=1.1).move_to(P(0, 2.3))
        seed = label("seeded random (seed 0)", 32, SOFT).move_to(P(0, 1.35))
        hl = label("two layers", 36, SOFT).move_to(P(-3.3, 0.95))
        hr = label("one matrix", 36, SOFT).move_to(P(3.3, 0.95))
        div = DashedLine(P(0, 0.9), P(0, -1.9), color=GHOST, stroke_width=3)
        l1 = tex(r"W_1\mathbf{x}=" + bcol(C["W1x"]), 50).move_to(P(-3.3, -0.05))
        l2 = tex(r"W_2(W_1\mathbf{x})=" + bcol(C["W2_W1x"]), 50).move_to(P(-3.3, -1.35))
        r1 = tex(r"W_2W_1=" + bmat(C["W2W1"]), 50).move_to(P(3.3, -0.05))
        r2 = tex(r"(W_2W_1)\mathbf{x}=" + bcol(C["W2W1_x"]), 50).move_to(P(3.3, -1.35))
        eq = MathTex(r"W_2(W_1\mathbf{x})", "=", r"(W_2W_1)\mathbf{x}", font_size=64, color=INK).move_to(P(0, -2.65))
        assert C["W2_W1x"] == C["W2W1_x"], "B03: the two paths disagree"

        c.at(0.2)
        c.play(Write(top), rt=1.4)
        c.go("seeded random matrices", FadeIn(seed), rt=0.5)
        c.go("through the first layer", FadeIn(hl), Create(div), FadeIn(l1, shift=DOWN * 0.2), rt=0.7)
        c.go("Then the second", FadeIn(l2, shift=DOWN * 0.2), rt=0.7)
        c.go("multiply the two matrices", FadeIn(hr), FadeIn(r1, shift=DOWN * 0.2), rt=0.7)
        c.go("through that single matrix", FadeIn(r2, shift=DOWN * 0.2), rt=0.7)
        c.go("Identical", Write(eq), rt=0.6)
        c.play(Create(box(eq[1], min_h=0.9)), rt=0.35)
        c.end()


# --------------------------------------------------------------------------- B04
class B04_TenLayers(Scene):
    def construct(self):
        c = Clock(self, "B04")
        S = EV["scale"]
        # Re-run the evidence draw (same seed, same order as demo/nonlinearity_demo.py).
        rng = np.random.default_rng(S["seed"])
        A1, A2 = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
        pts = rng.normal(size=(2, S["n_inputs"]))
        layers = [rng.normal(size=(2, 2)) for _ in range(10)]
        states = [pts]
        for L in layers:
            states.append(L @ states[-1])
        M = np.eye(2)
        for L in layers:
            M = L @ M
        one = M @ pts
        d10 = float(np.max(np.abs(states[-1] - one)))
        assert abs(d10 - S["ten_layer_max_abs_diff"]) <= 0.02 * S["ten_layer_max_abs_diff"], "B04 disagrees with evidence"
        assert np.allclose(np.round(M, 4), np.array(S["ten_layer_matrix"])), "B04 matrix disagrees with evidence"

        Q, R = np.array([-3.0, 0.3]), 2.15

        def cloud(st, s, radius, color):
            sc = R / s
            return VGroup(*[Dot(point=P(Q[0] + sc * st[0, i], Q[1] + sc * st[1, i]), radius=radius, color=color)
                            for i in range(st.shape[1])])

        s_last = float(np.max(np.abs(states[-1])))
        clouds = [cloud(st, float(np.max(np.abs(st))), 0.05, GHOST) for st in states]
        ink = cloud(one, s_last, 0.022, INK)
        start_ink = cloud(pts, float(np.max(np.abs(pts))), 0.022, INK)

        head = label(f"{S['n_inputs']:,} random inputs", 36).move_to(P(-3.0, 2.85))
        note = label("each frame rescaled to fit", 32, SOFT).move_to(P(-3.0, -2.15))
        counters = [VGroup(label("layers applied:", 36), num(str(k), 40)).arrange(RIGHT, buff=0.3).move_to(P(3.3, 2.4))
                    for k in range(11)]
        leg1 = VGroup(Dot(radius=0.09, color=GHOST), label("ten layers, one by one", 34)).arrange(RIGHT, buff=0.25)
        leg2 = VGroup(Dot(radius=0.06, color=INK), label("one multiplied-out matrix", 34)).arrange(RIGHT, buff=0.25)
        leg1.move_to(P(3.3, 1.45))
        leg2.move_to(P(3.3, 0.8))
        m, e = f"{S['ten_layer_max_abs_diff']:.2e}".split("e")
        gap = tex(r"\max|\Delta| = %s\times10^{%d}" % (m, int(e)), 50).move_to(P(3.3, -0.25))
        why = label("rounding, not structure", 34, SOFT).move_to(P(3.3, -0.95))
        bias = MathTex(r"W_2(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2", "=",
                       r"(W_2W_1)\mathbf{x}+(W_2\mathbf{b}_1+\mathbf{b}_2)", font_size=46, color=INK).move_to(P(0, -2.75))

        c.at(0.2)
        c.play(FadeIn(clouds[0]), FadeIn(head), FadeIn(counters[0]), rt=0.9)
        c.at(max(c.t, cue("B04", "ten random layers") - 0.1))
        for k in range(1, 11):
            c.play(Transform(clouds[0], clouds[k]), Transform(counters[0], counters[k]), rt=0.125)
        c.go("Multiply the ten matrices", FadeIn(note), FadeIn(leg1), rt=0.5)
        c.play(Transform(start_ink, ink), FadeIn(leg2), rt=1.2)
        c.go("The largest gap", FadeIn(gap, shift=UP * 0.2), rt=0.6)
        c.go("rounding not structure", FadeIn(why), rt=0.5)
        c.go("Add a shift", Write(bias), rt=0.9)
        c.go("one matrix plus one shift", Create(box(bias[2], min_h=0.85)), rt=0.4)
        c.end()


# --------------------------------------------------------------------------- B05
class B05_NoLine(Scene):
    def construct(self):
        c = Clock(self, "B05")
        XL = EV["xor_line"]
        O, S = np.array([-4.75, -1.65]), 3.3

        def U(u0, u1):
            return P(O[0] + S * u0, O[1] + S * u1)

        sq = Square(side_length=S, color=GHOST, stroke_width=3).move_to(U(0.5, 0.5))
        marks = VGroup(*[xor_marker(y, U(*x)) for x, y in zip(XOR_X, XOR_Y)])
        off = {(0, 0): (-0.5, -0.35), (0, 1): (-0.5, 0.35), (1, 0): (0.5, -0.35), (1, 1): (0.62, 0.42)}
        tags = VGroup(*[num(str(y), 36).move_to(P(U(*x)[0] + off[x][0], U(*x)[1] + off[x][1]))
                        for x, y in zip(XOR_X, XOR_Y)])
        head = label("XOR: exactly one input on → 1", 32).move_to(P(-3.1, 2.85))

        trk = ValueTracker(0.0)
        best_th, best_c = np.deg2rad(45.0), 0.5 / np.sqrt(2.0)   # the line x1 + x2 = 1/2

        mid = np.array([0.5, 0.5])

        def geom(s):
            # normal angle sweeps to 45 deg; offset from the square's centre stays inside the square
            th = np.deg2rad(-100.0 + 145.0 * s)
            n = np.array([np.cos(th), np.sin(th)])
            off = (best_c - np.sqrt(0.5)) * s + 0.4 * np.sin(3 * np.pi * s) * (1 - s)
            return n, float(np.dot(n, mid)) + off

        def seg(s):
            n, cc = geom(s)
            d = np.array([-n[1], n[0]])
            p0 = mid + (cc - np.dot(n, mid)) * n
            a, b = p0 - 0.62 * d, p0 + 0.62 * d
            return Line(U(*a), U(*b), color=INK, stroke_width=6)

        def correct(s):
            n, cc = geom(s)
            k = sum(int((np.dot(n, x) > cc) == bool(y)) for x, y in zip(XOR_X, XOR_Y))
            return max(k, 4 - k)

        def sval(t):
            try:
                return float(t.get_value())
            except (TypeError, ValueError):
                return 0.0

        line = always_redraw(lambda: seg(sval(trk)))
        now = always_redraw(lambda: label(f"this line: {correct(sval(trk))} of 4 correct", 36).move_to(P(3.3, 2.7)))
        tried = always_redraw(lambda: VGroup(label("lines tried:", 36),
                                             num(f"{int(round(sval(trk) * XL['lines_tried'])):,}", 38)
                                             ).arrange(RIGHT, buff=0.3).move_to(P(3.3, 2.05)))
        best = VGroup(label("best of all:", 36), num(f"{XL['best_correct']} of 4", 38)).arrange(RIGHT, buff=0.3)
        best.move_to(P(3.3, 1.4))
        ring = Circle(radius=0.4, color=SPARK, stroke_width=7).move_to(U(1, 1))

        rows = VGroup(tex(r"(0,0):\ \ b\le 0", 42), tex(r"(0,1):\ \ w_2+b>0", 42),
                      tex(r"(1,0):\ \ w_1+b>0", 42), tex(r"(1,1):\ \ w_1+w_2+b\le 0", 42))
        for i, r in enumerate(rows):
            r.move_to(P(0.9, 0.6 - 0.68 * i), aligned_edge=LEFT)
        add = tex(r"\text{rows 2+3:}\ \ w_1+w_2+b>-b\ge 0", 36).move_to(P(0.2, -2.2), aligned_edge=LEFT)
        clash = label("contradicts row 4", 34, SOFT).move_to(P(0.9, -2.85), aligned_edge=LEFT)
        assert XL["best_correct"] == 3 and correct(1.0) == 3

        c.at(0.2)
        c.play(Create(sq), FadeIn(head), rt=0.9)
        c.go("Four corners of a square", LaggedStart(*[FadeIn(m, scale=0.6) for m in marks], lag_ratio=0.25),
             FadeIn(tags), rt=1.2)
        c.go("Find a single line", Create(line), FadeIn(now), FadeIn(tried), rt=0.6)
        c.play(trk.animate.set_value(1.0), rt=c.until("The best gets"))
        c.go("The best gets", FadeIn(best, shift=UP * 0.2), Create(ring), rt=0.7)
        c.go("four lines of algebra", LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.3), rt=1.0)
        c.go("no line ever gets", FadeIn(add, shift=UP * 0.2), FadeIn(clash), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B06
class B06_StuckAtHalf(Scene):
    def construct(self):
        c = Clock(self, "B06")
        DL, XL = EV["deep_linear"], EV["xor_line"]
        run = DL["run"]
        slot = DashedVMobject(RoundedRectangle(width=1.6, height=0.8, corner_radius=0.12, color=SOFT,
                                               stroke_width=4), num_dashes=24)
        strip = VGroup(tex(r"\mathbf{x}\to W_1\to", 50), slot, tex(r"\to W_2\to y", 50)).arrange(RIGHT, buff=0.25)
        strip.move_to(P(0, 2.75))
        nob = label("no bend", 32, SOFT).move_to(V(slot.get_center()).tolist())

        # loss curve (executed, every 250 steps)
        x0, x1, y0, y1 = -5.6, -0.4, -2.05, 1.45
        ymax = 0.45
        X = lambda s: x0 + (x1 - x0) * s / DL["steps"]
        Y = lambda v: y0 + (y1 - y0) * v / ymax
        axes = VGroup(Line(P(x0, y0), P(x1, y0), color=INK, stroke_width=4),
                      Line(P(x0, y0), P(x0, y1), color=INK, stroke_width=4))
        curve = VMobject(color=INK, stroke_width=6)
        curve.set_points_as_corners([P(X(250 * i), Y(v)) for i, v in enumerate(run["curve"])])
        floor = DashedLine(P(x0, Y(run["loss"])), P(x1, Y(run["loss"])), color=SOFT, stroke_width=3)
        flab = tex(r"\text{loss}=%s" % f"{run['loss']:g}", 42).move_to(P(-2.6, Y(run["loss"]) + 0.55))
        xl = label(f"{DL['steps']:,} steps of gradient descent", 32, SOFT).move_to(P(-3.0, -2.5))
        yl = label("loss", 32, SOFT).move_to(P(-5.25, 1.85))

        # outputs: trained net vs least-squares best line, with target ticks
        base, H = -1.95, 2.7
        def bars(cx, vals):
            out, ticks = VGroup(), VGroup()
            for i, (v, t) in enumerate(zip(vals, XOR_Y)):
                x = cx + (i - 1.5) * 0.5
                out.add(Rectangle(width=0.36, height=max(0.02, H * v), color=INK, fill_color=INK, fill_opacity=1,
                                  stroke_width=0).move_to(P(x, base + H * v / 2)))
                ticks.add(Line(P(x - 0.26, base + H * t), P(x + 0.26, base + H * t), color=SOFT, stroke_width=5))
            return out, ticks
        ga, ta = bars(1.6, run["pred"])
        gb, tb = bars(4.6, XL["least_squares"]["pred"])
        baseline = Line(P(0.7, base), P(5.5, base), color=INK, stroke_width=3)
        la = label("trained, no bend", 32).move_to(P(1.6, -2.45))
        lb = label("best single line", 32).move_to(P(4.6, -2.45))
        va = label(f"each {g(run['pred'][0])}", 32).move_to(P(1.6, base + H * run["pred"][0] + 0.35))
        vb = label(f"each {g(XL['least_squares']['pred'][0])}", 32).move_to(P(4.6, base + H * XL["least_squares"]["pred"][0] + 0.35))
        tick_lab = label("ticks mark the targets 0, 1, 1, 0", 32, SOFT).move_to(P(3.1, 1.4))
        eqs = tex("=", 80).move_to(P(3.1, base + H * 0.25))
        over = DL["over_100_seeds"]
        chip = label(f"100 seeds: lowest loss {over['min_loss']:g}, all four right: {over['reached_4_of_4']}",
                     32).move_to(P(0, -2.95))
        assert all(abs(p - 0.5) < 1e-3 for p in run["pred"]) and all(abs(p - 0.5) < 1e-6 for p in XL["least_squares"]["pred"])

        c.at(0.2)
        c.play(FadeIn(strip), FadeIn(nob), rt=0.9)
        c.go("trained by gradient descent", Create(axes), FadeIn(xl), FadeIn(yl), rt=0.8)
        c.go("The loss sinks", Create(curve), rt=1.4)
        c.go("and flattens", Create(floor), FadeIn(flab), rt=0.6)
        c.go("Every output settles", Create(baseline), FadeIn(ta), FadeIn(tick_lab),
             *[GrowFromEdge(b, DOWN) for b in ga], FadeIn(la), rt=0.9)
        c.go("a shrug", FadeIn(va), rt=0.5)
        c.go("exactly what the best single line", FadeIn(tb), *[GrowFromEdge(b, DOWN) for b in gb], FadeIn(lb),
             FadeIn(vb), rt=0.9)
        c.go("because this network is", FadeIn(eqs), Create(box(eqs, min_h=0.9)), rt=0.6)
        c.go("A hundred seeds", FadeIn(chip, shift=UP * 0.2), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B07
class B07_ReluFix(Scene):
    def construct(self):
        c = Clock(self, "B07")
        RH = EV["relu_hand"]
        eq1 = tex(r"\mathbf{h}=\mathrm{ReLU}(W\mathbf{x}+\mathbf{c})", 48).move_to(P(-3.3, 2.75))
        eq2 = tex(r"y=\mathbf{w}^{\top}\mathbf{h}", 48).move_to(P(-3.3, 1.95))
        mats = VGroup(tex(r"W=" + bmat(RH["W"]), 42), tex(r"\mathbf{c}=" + bcol(RH["c"]), 42),
                      tex(r"\mathbf{w}=" + bcol(RH["w"]), 42)).arrange(RIGHT, buff=0.35).move_to(P(2.65, 2.35))
        cite = label("weights: Goodfellow, Bengio & Courville (2016), §6.1", 32, SOFT).move_to(P(0, 1.3))

        xs = [-4.8, -2.4, 0.2, 2.6, 4.4, 5.55]
        head = VGroup(tex(r"\mathbf{x}", 44).move_to(P(xs[0], 0.6)), tex(r"W\mathbf{x}+\mathbf{c}", 44).move_to(P(xs[1], 0.6)),
                      tex(r"\mathrm{ReLU}", 44).move_to(P(xs[2], 0.6)), tex(r"y", 44).move_to(P(xs[3], 0.6)),
                      label("target", 34, SOFT).move_to(P(xs[4], 0.6)))
        rule = Line(P(-5.8, 0.2), P(5.8, 0.2), color=GHOST, stroke_width=3)

        def vt(v):
            return r"(%s,\,%s)" % tuple(v)

        rows = []
        for i, r in enumerate(RH["rows"]):
            y = -0.3 - 0.75 * i
            if i == 0:
                z = MathTex(r"(%s,\," % r["z"][0], str(r["z"][1]), r")", font_size=44, color=INK).move_to(P(xs[1], y))
            else:
                z = tex(vt(r["z"]), 44).move_to(P(xs[1], y))
            rows.append({"x": tex(vt(r["x"]), 44).move_to(P(xs[0], y)), "z": z,
                         "h": tex(vt(r["h"]), 44).move_to(P(xs[2], y)),
                         "y": tex(str(r["y"]), 44).move_to(P(xs[3], y)),
                         "t": tex(str(r["target"]), 44, SOFT).move_to(P(xs[4], y)),
                         "ok": tex(r"\checkmark", 44).move_to(P(xs[5], y))})
            assert r["y"] == r["target"], "B07: hand-set net disagrees with XOR"
        clip = box(rows[0]["z"][1], min_h=0.62, min_w=0.6)

        c.at(0.2)
        c.play(Write(eq1), Write(eq2), rt=0.7)
        c.go("Two hidden units", FadeIn(mats, shift=DOWN * 0.2), rt=0.8)
        c.go("Deep Learning textbook", FadeIn(cite), rt=0.5)
        c.go("Each unit adds up", FadeIn(head), Create(rule), *[FadeIn(r["x"]) for r in rows], rt=0.7)
        c.go("At zero zero", FadeIn(rows[0]["z"]), rt=0.6)
        c.go("reads minus one", Create(clip), rt=0.5)
        c.go("flattens it to zero", FadeIn(rows[0]["h"], shift=RIGHT * 0.2), rt=0.6)
        c.go("The output takes", LaggedStart(*[FadeIn(VGroup(r["z"], r["h"])) for r in rows[1:]],
                                            lag_ratio=0.35), rt=1.3)
        c.go("Zero one one zero", LaggedStart(*[FadeIn(VGroup(r["y"], r["t"])) for r in rows], lag_ratio=0.3), rt=1.4)
        c.go("XOR exactly", LaggedStart(*[FadeIn(r["ok"], scale=0.6) for r in rows], lag_ratio=0.2), rt=0.8)
        c.end()


# --------------------------------------------------------------------------- B08
class B08_Fold(Scene):
    def construct(self):
        c = Clock(self, "B08")
        RH = EV["relu_hand"]
        O, S = np.array([-5.2, -1.5]), 3.0

        def U(u0, u1):
            return P(O[0] + S * u0, O[1] + S * u1)

        hx0, hy0, ux, uy = 0.6, -2.05, 5.0 / 3.0, 4.4 / 3.0

        def H(a, b):
            return P(hx0 + (a + 0.5) * ux, hy0 + (b + 1.5) * uy)

        sq = Square(side_length=S, color=GHOST, stroke_width=3).move_to(U(0.5, 0.5))
        marks = VGroup(*[xor_marker(y, U(*x), 0.18) for x, y in zip(XOR_X, XOR_Y)])
        hin = label("input square", 36, SOFT).move_to(P(-3.7, 2.85))
        hh = label("hidden layer", 36, SOFT).move_to(P(3.1, 2.85))
        axes = VGroup(Line(H(-0.5, 0), H(2.5, 0), color=INK, stroke_width=4),
                      Line(H(0, -1.5), H(0, 1.5), color=INK, stroke_width=4))
        a1 = tex(r"h_1", 40).move_to(P(H(2.5, 0)[0] + 0.0, H(2.5, 0)[1] - 0.4))
        a2 = tex(r"h_2", 40).move_to(P(H(0, 1.5)[0] + 0.45, H(0, 1.5)[1] - 0.1))

        zs = [r["z"] for r in RH["rows"]]
        hs = [r["h"] for r in RH["rows"]]
        movers = VGroup(*[xor_marker(y, U(*x), 0.18) for x, y in zip(XOR_X, XOR_Y)])
        at_z = VGroup(*[xor_marker(y, H(*z), 0.18) for z, y in zip(zs, XOR_Y)])
        at_h = VGroup(*[xor_marker(y, H(*h), 0.18) for h, y in zip(hs, XOR_Y)])
        lo = Line(H(-0.3, -1.3), H(1, 0), color=SOFT, stroke_width=4)
        hi = Line(H(1, 0), H(2.4, 1.4), color=SOFT, stroke_width=4)
        both = label("both 1s land here", 32).move_to(P(H(1, 0)[0] + 0.9, H(1, 0)[1] - 0.55))
        folded = Line(H(0, 0), H(1, 0), color=SPARK, stroke_width=9)
        sep = Line(H(-0.4, -0.45), H(2.4, 0.95), color=INK, stroke_width=6)
        sep_l = tex(r"h_1-2h_2=\tfrac12", 42).move_to(P(3.4, -2.6))

        band_pts = [(0.5, 0), (1, 0), (1, 0.5), (0.5, 1), (0, 1), (0, 0.5)]
        band = Polygon(*[U(*p) for p in band_pts], color=SOFT, fill_color=SOFT, fill_opacity=0.5, stroke_width=0)
        e1 = DashedLine(U(0.5, 0), U(0, 0.5), color=INK, stroke_width=4)
        e2 = DashedLine(U(1, 0.5), U(0.5, 1), color=INK, stroke_width=4)
        band_l = tex(r"\tfrac12<x_1+x_2<\tfrac32", 42).move_to(P(-3.7, -2.6))
        hid = [tuple(p) for p in RH["hidden_points"]]
        assert sorted(set(tuple(h) for h in hs)) == sorted(hid) and len(hid) == 3

        c.at(0.2)
        c.play(Create(sq), FadeIn(marks), FadeIn(hin), FadeIn(hh), Create(axes), FadeIn(a1), FadeIn(a2), rt=1.2)
        c.go("lays all four points on one line", Transform(movers, at_z), Create(lo), Create(hi), rt=1.6)
        c.go("land on the same spot", FadeIn(both), rt=0.5)
        c.go("ReLU folds that line", Transform(movers, at_h), Transform(lo, folded), FadeOut(both), rt=1.5)
        c.go("Now one straight line", Create(sep), FadeIn(sep_l), rt=0.9)
        c.go("Unfold it back", FadeIn(band), Create(e1), Create(e2), rt=1.0)
        c.go("ones inside", FadeIn(band_l), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B09
class B09_HundredSeeds(Scene):
    def construct(self):
        c = Clock(self, "B09")
        SD = EV["seeds"]
        two, eight = SD["two_units"], SD["eight_units"]
        assert sum(two["solved_mask"]) == two["solved"] and sum(eight["solved_mask"]) == eight["solved"]

        def grid(cx, mask):
            ph, fin = VGroup(), VGroup()
            for s in range(100):
                r, q = divmod(s, 10)
                p = P(cx + (q - 4.5) * 0.44, -0.05 + (4.5 - r) * 0.44)
                ph.add(Square(side_length=0.38, color=GHOST, stroke_width=2).move_to(p))
                if mask[s]:
                    fin.add(Square(side_length=0.38, color=INK, fill_color=INK, fill_opacity=1, stroke_width=0).move_to(p))
                else:
                    fin.add(Square(side_length=0.38, color=SOFT, stroke_width=3).move_to(p))
            return ph, fin

        ph2, fin2 = grid(-3.2, two["solved_mask"])
        ph8, fin8 = grid(3.2, eight["solved_mask"])
        h2 = label("2 hidden units, seeds 0–99", 34).move_to(P(-3.2, 2.75))
        h8 = label("8 hidden units, seeds 0–99", 34).move_to(P(3.2, 2.75))
        def key(n, word, solved):
            sw = (Square(side_length=0.32, color=INK, fill_color=INK, fill_opacity=1, stroke_width=0) if solved
                  else Square(side_length=0.32, color=SOFT, stroke_width=3))
            return VGroup(sw, label(f"{n} {word}", 40)).arrange(RIGHT, buff=0.2)
        k2 = key(two["solved"], "solved", True).move_to(P(-4.55, -2.75))
        k2b = key(two["failed"], "stuck", False).move_to(P(-1.75, -2.75))
        k8 = key(eight["solved"], "solved", True).move_to(P(3.2, -2.75))

        fs = two["example_fail_seed"]
        ex = two["example_fail"]
        Xa = np.array(XOR_X, dtype=float)
        hid = np.maximum(Xa @ np.array(ex["W"]).T + np.array(ex["c"]), 0.0)
        dead = [j for j in range(hid.shape[1]) if np.all(hid[:, j] <= 0)]
        assert dead and ex["dead_units"] == len(dead)
        j = dead[0]
        # a callout card over the (still ghosted) right grid
        card = RoundedRectangle(width=5.5, height=4.7, corner_radius=0.15, color=INK, stroke_width=3,
                                fill_color=PAGE, fill_opacity=1).move_to(P(3.2, -0.05))
        ins_t = label(f"seed {fs}: stuck", 36).move_to(P(3.2, 1.75))
        ins_u = VGroup(label(f"hidden unit {j + 1} outputs:", 34),
                       num(", ".join(g(v) for v in hid[:, j]), 38)).arrange(DOWN, buff=0.22).move_to(P(3.2, 0.75))
        flat = box(ins_u[1], min_h=0.62)
        ins_o = VGroup(label("network output:", 34), num(", ".join(g(p) for p in ex["pred"]), 38)
                       ).arrange(DOWN, buff=0.22).move_to(P(3.2, -0.6))
        ins_d = VGroup(label(f"{two['failed_with_dead_unit']} of {two['failed']} stuck runs", 32, SOFT),
                       label("have a dead unit", 32, SOFT)).arrange(DOWN, buff=0.15).move_to(P(3.2, -1.75))
        tile0 = Square(side_length=0.5, color=INK, stroke_width=6).move_to(V(ph2[fs].get_center()).tolist())
        inset = VGroup(card, ins_t, ins_u, flat, ins_o, ins_d)

        c.at(0.2)
        c.play(FadeIn(h2), FadeIn(ph2), FadeIn(ph8), rt=0.9)
        c.go("trained from a hundred", LaggedStart(*[FadeIn(t) for t in fin2], lag_ratio=0.03), rt=2.2)
        c.go("eighteen find XOR", FadeIn(k2, shift=UP * 0.2), rt=0.6)
        c.go("Eighty-two get stuck", FadeIn(k2b, shift=UP * 0.2), Create(tile0), rt=0.6)
        c.go("hidden unit that went flat", FadeOut(ph8), FadeIn(card), FadeIn(ins_t), FadeIn(ins_u), FadeIn(ins_o), rt=0.8)
        c.play(Create(flat), FadeIn(ins_d), rt=0.6)
        c.go("Give it eight units", FadeOut(inset), FadeIn(h8), FadeIn(ph8), rt=0.4)
        c.play(LaggedStart(*[FadeIn(t) for t in fin8], lag_ratio=0.03), rt=c.until("ninety-one", floor=0.6))
        c.go("ninety-one", FadeIn(k8, shift=UP * 0.2), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B10
class B10_StraightAgain(Scene):
    def construct(self):
        c = Clock(self, "B10")
        K, RH = EV["kinks"], EV["relu_hand"]
        W, cc, w = np.array(RH["W"], float), np.array(RH["c"], float), np.array(RH["w"], float)

        def f(t):
            return float(w @ np.maximum(W @ np.array([t, t]) + cc, 0.0))

        for s in K["samples"]:
            assert abs(f(s["t"]) - s["y"]) < 1e-9, "B10 disagrees with evidence"

        def T(t, y):
            return P(-3.0 + (t + 1.0) * 2.0, -2.95 + (y + 4.5) * (5.6 / 6.0))

        axes = VGroup(Line(T(-1, 0), T(3.2, 0), color=GHOST, stroke_width=4),
                      Line(T(0, -4.5), T(0, 1.5), color=GHOST, stroke_width=4))
        at = tex("t", 42).move_to(P(T(3.2, 0)[0] + 0.3, T(3.2, 0)[1]))
        ay = tex("y", 42).move_to(P(T(0, 1.5)[0] - 0.35, T(0, 1.5)[1] - 0.1))
        q, s = np.array([-5.55, 1.25]), 1.35
        insq = Square(side_length=s, color=GHOST, stroke_width=3).move_to(P(q[0] + s / 2, q[1] + s / 2))
        inmk = VGroup(*[xor_marker(y, P(q[0] + s * x[0], q[1] + s * x[1]), 0.1) for x, y in zip(XOR_X, XOR_Y)])
        diag = Arrow(P(q[0] - 0.2, q[1] - 0.2), P(q[0] + s + 0.25, q[1] + s + 0.25), buff=0, color=INK,
                     stroke_width=5, max_tip_length_to_length_ratio=0.15)
        dlab = tex(r"\mathbf{x}=(t,\,t)", 40).move_to(P(-4.85, 0.75))

        knots = [-1.0, 0.0, 0.5, 1.0, 3.0]
        segs = [Line(T(a, f(a)), T(b, f(b)), color=INK, stroke_width=7) for a, b in zip(knots, knots[1:])]
        k0, k1 = K["kinks_at_t"]
        dots = VGroup(Dot(point=T(k0, f(k0)), radius=0.13, color=SPARK), Dot(point=T(k1, f(k1)), radius=0.13, color=SPARK))
        kl0 = label("unit 1 on", 32).move_to(P(T(k0, 0)[0] - 0.85, T(k0, 0)[1] + 0.45))
        kl1 = label("unit 2 on", 32).move_to(P(T(k1, f(k1))[0] + 1.1, T(k1, f(k1))[1] + 0.35))
        far = K["far"]["(3,3)"]
        endp = Dot(point=T(3, far), radius=0.1, color=INK)
        endl = tex(r"(3,\,3)\mapsto %s" % f"{far:g}", 42).move_to(P(T(3, far)[0] - 1.9, T(3, far)[1] - 0.05))
        pieces = VGroup(tex(r"t\le 0:\ \ y=0", 38), tex(r"0\le t\le\tfrac12:\ \ y=2t", 38),
                        tex(r"t\ge\tfrac12:\ \ y=2-2t", 38))
        for i, p in enumerate(pieces):
            p.move_to(P(-5.7, -0.55 - 0.7 * i), aligned_edge=LEFT)
        assert abs(far - f(3.0)) < 1e-9

        c.at(0.2)
        c.play(Create(axes), FadeIn(at), FadeIn(ay), Create(insq), FadeIn(inmk), rt=1.0)
        c.go("along the square's diagonal", GrowArrow(diag), FadeIn(dlab), rt=0.8)
        c.go("The output is flat", Create(segs[0]), rt=0.7)
        c.go("then climbs", Create(segs[1]), rt=0.7)
        c.go("then falls", Create(segs[2]), rt=0.7)
        c.go("Two kinks", FadeIn(dots, scale=0.5), FadeIn(kl0), FadeIn(kl1), rt=0.7)
        c.go("Keep walking", Create(segs[3]), rt=1.6)
        c.go("it says minus four", FadeIn(endp), FadeIn(endl), rt=0.6)
        c.go("Between and beyond", LaggedStart(*[FadeIn(p, shift=LEFT * 0.2) for p in pieces], lag_ratio=0.3), rt=0.8)
        c.end()
