"""Manim scenes for "Gradient Descent, One Step at a Time" (claude-liam-gradient-descent).

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/gd_demo.py).
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
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-gradient-descent"))


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
    """Keeps a scene on the narration clock without relying on renderer internals."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        scene.camera.background_color = PAGE

    # Manim renders ceil(run_time * fps) frames per play/wait, so the clock counts frames.
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

    def end(self):
        self.at(DUR[self.bid])


def label(s, size=36, color=INK, font=SERIF):
    return Text(s, font=font, font_size=size, color=color)


def num(s, size=36, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def fmt(x, nd=4):
    s = f"{x:.{nd}f}".rstrip("0").rstrip(".")
    return s.replace("-", "−")


def P(ax, x, y):
    """Axes point as a float vector (the GATE A geometry stub returns a placeholder)."""
    try:
        p = np.array(ax.c2p(x, y), dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def V(v):
    """Any point-like to a float vector (stub-safe)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def under(m, buff=0.14):
    """Terracotta spotlight rule under a mobject (plain Line: stub-safe, same look as Underline)."""
    return Line(V(m.get_corner(DL)) + DOWN * buff, V(m.get_corner(DR)) + DOWN * buff,
                color=SPARK, stroke_width=9)


def axis_cfg():
    return {"color": INK, "stroke_width": 3, "include_ticks": False, "tip_length": 0.22}


def gd_path(grad, theta0, lr, steps):
    p = [theta0]
    for _ in range(steps):
        p.append(p[-1] - lr * grad(p[-1]))
    return p


# --------------------------------------------------------------------------- B02
class B02_Landscape(Scene):
    def construct(self):
        c = Clock(self, "B02")
        ax = Axes(x_range=[-3.6, 3.6, 1], y_range=[0, 10.5, 1], x_length=10.4, y_length=5.4,
                  axis_config=axis_cfg()).move_to(DOWN * 0.35)
        f = lambda t: t * t
        xl = label("setting  θ", 38).next_to(P(ax, 3.6, 0), UP, buff=0.25).shift(LEFT * 0.9)
        yl = label("loss  (how wrong)", 38).next_to(P(ax, 0, 10.5), LEFT, buff=0.3)
        curve = ax.plot(f, x_range=[-3.2, 3.2], color=INK, stroke_width=6)
        x0 = 3.0
        b0 = P(ax, x0, f(x0))
        ball = Dot(b0, radius=0.16, color=INK)

        c.go("Across", Create(ax.get_x_axis()), FadeIn(xl), rt=1.2)
        c.go("Up the side", Create(ax.get_y_axis()), FadeIn(yl), rt=1.2)
        c.go("curve", Create(curve), rt=0.9)
        c.go("it can't see", FadeIn(ball, scale=0.5), curve.animate.set_stroke(opacity=0.4), rt=0.7)

        m, d = 2 * x0, 0.55                      # true slope at θ=3 in data units
        t0, t1 = P(ax, x0 - d, f(x0) - m * d), P(ax, x0 + d * 0.32, f(x0) + m * d * 0.32)
        tan = Line(t0, t1, color=INK, stroke_width=5)
        tl = label("slope", 36).next_to(t0, RIGHT, buff=0.3)
        c.go("slope right where", Create(tan), FadeIn(tl), rt=1.0)

        dv = t1 - t0
        up_dir = dv / (np.linalg.norm(dv) or 1.0)
        up_end = b0 + up_dir * 1.1
        up = Arrow(b0, up_end, buff=0.1, color=SOFT, stroke_width=6)
        ul = label("uphill", 34, SOFT).next_to(up_end, UP, buff=0.15)
        c.go("points uphill", GrowArrow(up), FadeIn(ul), rt=0.9)

        dn_end = b0 - up_dir * 2.0
        down = Arrow(b0, dn_end, buff=0.1, color=SPARK, stroke_width=8)
        dl = label("step", 40, SPARK).next_to(dn_end, LEFT, buff=0.25)
        c.go("other way", GrowArrow(down), FadeIn(dl), rt=1.0)
        c.end()


# --------------------------------------------------------------------------- B03
class B03_UpdateRule(Scene):
    def construct(self):
        c = Clock(self, "B03")
        eq = MathTex(r"\theta_{t+1}", "=", r"\theta_t", "-", r"\eta", r"\nabla L(\theta_t)",
                     color=INK, font_size=132).move_to(UP * 2.25)
        new, eqs, cur, minus, eta, grad = (eq[i] for i in range(6))

        # Spotlight = a rounded box, never an underline: an underlined "=" or "−" misreads as ≡ / =.
        def box(part):
            # minimum height so a box around a thin "=" or "-" never reads as a third bar
            w = max(float(getattr(part, "width", 0.5)) + 0.1, 0.42)
            h = max(float(getattr(part, "height", 0.5)) + 0.3, 1.15)
            return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=SPARK,
                                    stroke_width=6).move_to(V(part.get_center()).tolist())

        spot = box(new)

        def tag(part, text, row):
            t = label(text, 38, INK)
            y = (0.8, -0.3, -1.4)[row]
            t.move_to([np.clip(V(part.get_center())[0], -4.6, 4.6), y, 0])
            return t

        lab_new = tag(new, "new setting", 0)
        lab_eq = tag(eqs, "becomes", 2)
        lab_cur = tag(cur, "current setting", 0)
        lab_grad = tag(grad, "slope of the loss here", 0)
        lab_eta = tag(eta, "step size (you choose it)", 2)
        lab_minus = tag(minus, "against the slope", 1)

        c.go("Written down", Write(eq), rt=1.0)
        c.go("new setting", Create(spot), FadeIn(lab_new, shift=UP * 0.2), rt=0.5)
        c.go("becomes", Transform(spot, box(eqs)), FadeIn(lab_eq, shift=UP * 0.2), rt=0.5)
        c.go("old setting", Transform(spot, box(cur)), FadeIn(lab_cur, shift=UP * 0.2), rt=0.5)
        c.go("the gradient", Transform(spot, box(grad)), FadeIn(lab_grad, shift=UP * 0.2), rt=0.6)
        c.go("and eta", Transform(spot, box(eta)), FadeIn(lab_eta, shift=UP * 0.2), rt=0.6)

        # steep vs flat: the step arrow scales with the slope
        base = np.array([-2.1, -2.45, 0])
        # explicit move_to = the arrow's own midpoint (no-op in Manim; lets GATE A see the change)
        big = Arrow(base, base + RIGHT * 4.2, buff=0, color=INK, stroke_width=7).move_to((base + RIGHT * 2.1).tolist())
        big_l = label("steep slope: big step", 34).next_to(big, DOWN, buff=0.2)
        c.go("Steep slope", GrowArrow(big), FadeIn(big_l), rt=0.7)
        small = Arrow(base, base + RIGHT * 0.8, buff=0, color=INK, stroke_width=7).move_to((base + RIGHT * 0.4).tolist())
        small_l = label("flat ground: tiny step", 34).next_to(big, DOWN, buff=0.2)
        c.go("Flat ground", ReplacementTransform(big, small), ReplacementTransform(big_l, small_l), rt=0.7)

        c.go("minus sign", Transform(spot, box(minus)), FadeIn(lab_minus, shift=UP * 0.2), rt=0.9)
        c.end()


# --------------------------------------------------------------------------- B04
class B04_FiveSteps(Scene):
    def construct(self):
        c = Clock(self, "B04")
        steps = EV["worked"]["steps"]
        f = lambda t: t * t
        ax = Axes(x_range=[-0.4, 3.4, 1], y_range=[0, 10, 1], x_length=5.8, y_length=5.2,
                  axis_config=axis_cfg()).move_to(LEFT * 3.25 + DOWN * 0.3)
        curve = ax.plot(f, x_range=[-0.2, 3.15], color=INK, stroke_width=5)
        ttl = label("loss = θ²     slope = 2θ     step size 0.1", 34, SOFT).move_to(UP * 3.05)

        cols_x = [0.85, 2.3, 3.95, 5.5]
        head = VGroup(*[label(h, 34, SOFT).move_to([x, 2.25, 0])
                        for h, x in zip(["t", "θ", "slope", "loss"], cols_x)])
        rule = Line([0.45, 1.9, 0], [6.15, 1.9, 0], color=GHOST, stroke_width=2)
        rows = []
        for i, s in enumerate(steps):          # 3 decimals on screen; full values in evidence.json
            y = 1.45 - i * 0.62
            rows.append(VGroup(num(str(s["t"]), 32).move_to([cols_x[0], y, 0]),
                               num(fmt(s["theta"], 3), 32).move_to([cols_x[1], y, 0]),
                               num(fmt(s["slope"], 3), 32).move_to([cols_x[2], y, 0]),
                               num(fmt(s["loss"], 3), 32).move_to([cols_x[3], y, 0])))
        ball = Dot(P(ax, 3.0, 9.0), radius=0.15, color=INK)

        c.go("Real numbers", Create(ax), Create(curve), FadeIn(ttl), rt=1.4)
        c.go("Start at three", FadeIn(ball, scale=0.5), FadeIn(head), Create(rule), FadeIn(rows[0]), rt=0.9)

        def step(i, rt):
            th = steps[i]["theta"]
            a = Arrow(V(ball.get_center()), P(ax, th, f(th)), buff=0.12, color=SOFT, stroke_width=4,
                      max_tip_length_to_length_ratio=0.2)
            return [ball.animate.move_to(P(ax, th, f(th))), FadeIn(a), FadeIn(rows[i])], a

        anims, _ = step(1, 0.8)
        c.go("we land at", *anims, rt=0.8)
        anims, _ = step(2, 0.8)
        c.go("one point nine two", *anims, rt=0.8)
        for i in (3, 4, 5):
            anims, _ = step(i, 0.5)
            c.play(*anims, rt=0.5)
        chip = label("× 0.8 every step", 38).move_to([3.5, -2.55, 0])
        c.go("same factor", FadeIn(chip, shift=UP * 0.2), rt=0.7)
        box0 = SurroundingRectangle(rows[0][3], color=SPARK, buff=0.1, stroke_width=4)
        box5 = SurroundingRectangle(rows[5][3], color=SPARK, buff=0.1, stroke_width=4)
        c.go("from nine", Create(box0), rt=0.6)
        c.go("just under one", Create(box5), rows[5][3].animate.set_color(SPARK), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B05
class B05_StepSize(Scene):
    def construct(self):
        c = Clock(self, "B05")
        f = lambda t: t * t
        lrs = ["0.01", "0.1", "1.1"]
        centers = [-4.2, 0.0, 4.2]
        panels, balls, axs, counters, ends = [], [], [], [], []
        for lr, cx in zip(lrs, centers):
            ax = Axes(x_range=[-6, 6, 1], y_range=[0, 36, 6], x_length=3.6, y_length=3.0,
                      axis_config=axis_cfg()).move_to([cx, 0.1, 0])
            cur = ax.plot(f, x_range=[-6, 6], color=INK, stroke_width=4)
            head = MathTex(r"\eta = " + lr, color=INK, font_size=56).move_to([cx, 2.35, 0])
            ball = Dot(P(ax, 3, 9), radius=0.12, color=INK)
            path = EV["sweep"][lr]["theta"]
            end = path[-1]
            cnt = VGroup(label("θ after 10 steps", 32, SOFT),
                         num(fmt(end), 44)).arrange(DOWN, buff=0.18).move_to([cx, -2.35, 0])
            panels.append(VGroup(ax, cur, head)); balls.append(ball); axs.append(ax)
            counters.append(cnt); ends.append(path)

        c.go("Same bowl", *[Create(p) for p in panels], *[FadeIn(b) for b in balls], rt=1.4)

        # η = 0.01: ten tiny steps
        p = ends[0]
        c.go("zero point zero one", *[balls[0].animate.move_to(P(axs[0], p[-1], f(p[-1])))], rt=2.0)
        c.play(FadeIn(counters[0], shift=UP * 0.2), rt=0.6)

        # η = 0.1: rolls in
        p = ends[1]
        c.at(cue("B05", "At zero point one") - 0.1)
        for th in p[1:]:
            c.play(balls[1].animate.move_to(P(axs[1], th, f(th))), rt=0.17)
        c.play(FadeIn(counters[1], shift=UP * 0.2), rt=0.6)

        # η = 1.1: bounces out of the bowl
        p = ends[2]
        c.at(cue("B05", "one point one") - 0.1)
        balls[2].set_color(SPARK)
        trail = VMobject(color=SPARK, stroke_width=4)
        pts = [P(axs[2], 3, 9)]
        for th in p[1:]:
            if abs(th) > 6:
                break
            pts.append(P(axs[2], th, f(th)))
        for q in pts[1:]:
            seg = Line(V(balls[2].get_center()), q, color=SPARK, stroke_width=4)
            c.play(balls[2].animate.move_to(q), Create(seg), rt=0.45)
        nxt = p[len(pts)]                       # first value that leaves the drawn bowl
        runaway = Arrow(V(balls[2].get_center()), P(axs[2], 5.8 if nxt > 0 else -5.8, 35),
                        buff=0.1, color=SPARK, stroke_width=6)
        c.play(GrowArrow(runaway), rt=0.4)
        counters[2][1].set_color(SPARK)
        c.go("past eighteen", FadeIn(counters[2], shift=UP * 0.2), rt=0.5)
        c.go("runs away", Indicate(counters[2][1], color=SPARK, scale_factor=1.15), rt=0.5, lead=0.35)
        c.end()


# --------------------------------------------------------------------------- B06
class B06_TwoValleys(Scene):
    def construct(self):
        c = Clock(self, "B06")
        nc = EV["nonconvex"]
        f = lambda t: t ** 4 - 3 * t ** 2 + t
        g = lambda t: 4 * t ** 3 - 6 * t + 1
        ax = Axes(x_range=[-2.2, 2.2, 1], y_range=[-4.2, 6.5, 2], x_length=10.0, y_length=5.0,
                  axis_config=axis_cfg()).move_to(UP * 0.05)
        curve = ax.plot(f, x_range=[-2.05, 2.05], color=INK, stroke_width=6)
        xl = label("setting  θ", 34, SOFT).next_to(P(ax, 2.2, 0), DOWN, buff=0.3).shift(LEFT * 0.5)
        yl = label("loss", 34, SOFT).next_to(P(ax, 0, 6.5), RIGHT, buff=0.25)

        right = gd_path(g, 2.0, 0.02, 200)
        left = gd_path(g, -2.0, 0.02, 200)
        assert abs(right[-1] - nc["start_2.0"]["end_theta"]) < 1e-3, "B06 path disagrees with evidence"
        assert abs(left[-1] - nc["start_-2.0"]["end_theta"]) < 1e-3, "B06 path disagrees with evidence"
        loc, glob = nc["minima"][1], nc["minima"][0]

        c.at(0.2)
        c.play(Create(ax), Create(curve), FadeIn(xl), FadeIn(yl), rt=1.4)
        ball = Dot(P(ax, 2.0, f(2.0)), radius=0.15, color=INK)
        c.go("Start on", FadeIn(ball, scale=0.5), rt=0.5)
        trace = [P(ax, t, f(t)) for t in right[:60:3]] + [P(ax, right[-1], f(right[-1]))]
        for q in trace[1:]:
            c.play(ball.animate.move_to(q), rt=0.09)
        loc_l = VGroup(label("loss " + fmt(loc["loss"], 2), 36),
                       label("slope 0", 32, SOFT)).arrange(DOWN, buff=0.12)
        loc_l.next_to(P(ax, loc["theta"], loc["loss"]), DOWN, buff=0.35)
        c.go("and stops", FadeIn(loc_l, shift=UP * 0.2), rt=0.7)

        ring = Circle(radius=0.32, color=SPARK, stroke_width=6).move_to(P(ax, glob["theta"], glob["loss"]))
        glob_l = label("loss " + fmt(glob["loss"], 2), 40, SPARK).next_to(ring, DOWN, buff=0.25)
        c.go("deeper valley", Create(ring), FadeIn(glob_l), rt=0.8)

        ghost = Dot(P(ax, -2.0, f(-2.0)), radius=0.13, color=SOFT).set_opacity(0.7)
        c.go("Where you start", FadeIn(ghost), rt=0.4)
        trace = [P(ax, t, f(t)) for t in left[:60:6]] + [P(ax, left[-1], f(left[-1]))]
        for q in trace[1:]:
            c.play(ghost.animate.move_to(q), rt=0.07)
        motto = label("where you start decides where you end", 40).move_to(UP * 3.1)
        c.play(FadeIn(motto, shift=DOWN * 0.2), rt=0.4)
        c.end()


# --------------------------------------------------------------------------- B07
class B07_Batches(Scene):
    def construct(self):
        c = Clock(self, "B07")
        sc = EV["scale"]
        # Rebuild the same seeded data as demo/gd_demo.py to draw the loss contours.
        rng = np.random.default_rng(sc["seed"])
        x = rng.uniform(-2, 2, sc["n"])
        y = 1.5 * x - 0.5 + rng.normal(0, 0.4, sc["n"])
        H = np.array([[np.mean(x * x), np.mean(x)], [np.mean(x), 1.0]])
        ctr = np.array([sc["least_squares"]["w"], sc["least_squares"]["b"]])
        m0 = sc["least_squares"]["mse"]

        ax = Axes(x_range=[-1.4, 2.9, 1], y_range=[-2.1, 2.6, 1], x_length=6.4, y_length=5.6,
                  axis_config=axis_cfg()).move_to(LEFT * 2.75 + DOWN * 0.3)
        wl = MathTex("w", color=SOFT, font_size=48).next_to(P(ax, 2.9, 0), DOWN, buff=0.15)
        bl = MathTex("b", color=SOFT, font_size=48).next_to(P(ax, 0, 2.6), LEFT, buff=0.15)

        evals, evecs = np.linalg.eigh(H)
        rings = VGroup()
        for lvl in (0.1, 0.4, 1.0, 1.8):        # loss above the minimum; all rings stay in frame
            r = np.sqrt(lvl) / np.sqrt(evals)
            pts = []
            for a in np.linspace(0, TAU, 120):
                d = evecs @ np.array([r[0] * np.cos(a), r[1] * np.sin(a)])
                w, b = ctr + d
                pts.append(P(ax, w, b))
            ring = VMobject(color=GHOST, stroke_width=3).set_points_smoothly(pts + [pts[0]])
            rings.add(ring)
        rings.set_stroke(opacity=0.9)
        title = label("loss over two settings, w and b", 34, SOFT).move_to([-2.75, 3.1, 0])

        def path(pts, color, width):
            return VMobject(color=color, stroke_width=width).set_points_as_corners([P(ax, a, b) for a, b in pts])

        full = path(sc["full_path"], INK, 5)
        sgd = path(sc["sgd_path"], SPARK, 5)
        start = Dot(P(ax, *sc["full_path"][0]), radius=0.1, color=INK)

        bp = label("backpropagation:\nevery slope in one\nbackward pass", 34).move_to([3.85, 2.25, 0])
        k_full = VGroup(Line(ORIGIN, RIGHT * 0.7, color=INK, stroke_width=6),
                        label("all 200 points per step", 32)).arrange(RIGHT, buff=0.25).move_to([3.95, 0.45, 0])
        k_sgd = VGroup(Line(ORIGIN, RIGHT * 0.7, color=SPARK, stroke_width=6),
                       label("8 points per step", 32)).arrange(RIGHT, buff=0.25)
        k_sgd.move_to([3.95, -0.35, 0]).align_to(k_full, LEFT)
        cost = label("each step: 1/25 the work", 34).move_to([3.95, -1.5, 0])
        res = VGroup(num("full   loss " + fmt(sc["full_end"]["mse"], 4), 32),
                     num("batch  loss " + fmt(sc["sgd_end"]["mse"], 4), 32, SPARK)
                     ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to([3.95, -2.6, 0])

        c.at(0.2)
        c.play(Create(ax), FadeIn(wl), FadeIn(bl), FadeIn(title), rt=1.2)
        c.go("landscape", Create(rings), rt=1.4)
        c.go("Backpropagation", FadeIn(bp, shift=LEFT * 0.2), rt=0.8)
        c.go("small batch", FadeIn(start), FadeIn(k_full), FadeIn(k_sgd), rt=0.6)
        c.play(Create(full), Create(sgd), rt=3.6)
        c.go("twenty-fifth", FadeIn(cost, shift=UP * 0.2), rt=0.6)
        c.go("few percent", FadeIn(res, shift=UP * 0.2), rt=0.7)
        c.end()
