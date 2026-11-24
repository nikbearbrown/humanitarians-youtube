"""Manim scenes for "Overfitting, When a Perfect Score Lies" (claude-liam-overfitting).

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers and curves: every on-screen value comes from demo/evidence.json (demo/overfit_demo.py).
Each scene ends exactly at its beat's measured audio duration.
Each scene class subclasses Scene directly, one per beat (run.sh finds them by regex).
Geometry is computed with numpy (Plot.p), never read back from mobjects, so the GATE A stub runs it.
"""
from manim import *
import json
import os
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# GATE A pre-flights an isolated copy of this file; fall back to the reel folder.
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-overfitting"))


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

    def end(self):
        self.at(DUR[self.bid])


def label(s, size=36, color=INK, font=SERIF):
    return Text(s, font=font, font_size=size, color=color)


def num(s, size=36, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def tex(s, size=48, color=INK):
    return MathTex(s, font_size=size, color=color)


def fmt(x, nd=3):
    """On-screen number: thousands separators, trailing zeros trimmed, true minus sign."""
    if abs(x) >= 1000:
        s = f"{x:,.1f}"
    elif x == 0:
        s = "0"
    else:
        s = f"{x:.{nd}f}".rstrip("0").rstrip(".")
    return s.replace("-", "−")


def tfmt(x, nd=3):
    """fmt() for MathTex: ASCII minus (LaTeX typesets it as a true minus)."""
    return fmt(x, nd).replace("−", "-")


def V(v):
    """Any point-like to a float vector (the GATE A geometry stub returns placeholders)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def box(part, pad=0.4, min_w=0.6, min_h=1.0, color=SPARK):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '−')."""
    w = max(float(getattr(part, "width", 0.5)) + pad, min_w)
    h = max(float(getattr(part, "height", 0.5)) + pad, min_h)
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color,
                            stroke_width=6).move_to(V(part.get_center()).tolist())


class Plot:
    """A data rectangle mapped onto a screen rectangle, in pure numpy (stub-safe)."""

    def __init__(self, x0, x1, y0, y1, xr, yr):
        self.x0, self.x1, self.y0, self.y1, self.xr, self.yr = x0, x1, y0, y1, xr, yr

    def p(self, x, y):
        sx = self.x0 + (x - self.xr[0]) / (self.xr[1] - self.xr[0]) * (self.x1 - self.x0)
        sy = self.y0 + (y - self.yr[0]) / (self.yr[1] - self.yr[0]) * (self.y1 - self.y0)
        return np.array([sx, sy, 0.0])

    def P(self, x, y):
        return self.p(x, y).tolist()

    def frame(self, color=GHOST, width=3):
        return Rectangle(width=self.x1 - self.x0, height=self.y1 - self.y0, color=color,
                         stroke_width=width).move_to([(self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2, 0])

    def axes(self, color=INK, width=4):
        return VGroup(Line(self.P(self.xr[0], self.yr[0]), self.P(self.xr[1], self.yr[0]), color=color,
                           stroke_width=width),
                      Line(self.P(self.xr[0], self.yr[0]), self.P(self.xr[0], self.yr[1]), color=color,
                           stroke_width=width))

    def curve(self, xs, ys, color=INK, width=6, opacity=1.0):
        """Polyline through (xs, ys), clipped to the y range: exits are cut at the frame edge."""
        lo, hi = self.yr
        segs, cur = [], []
        for i in range(len(xs)):
            x, y = float(xs[i]), float(ys[i])
            inside = lo <= y <= hi
            if i > 0:
                xp, yp = float(xs[i - 1]), float(ys[i - 1])
                was = lo <= yp <= hi
                if was != inside:                      # crossing: add the boundary point
                    edge = hi if (y > hi or yp > hi) else lo
                    xe = xp + (edge - yp) / (y - yp) * (x - xp)
                    cur.append(self.p(xe, edge))
                    if was:
                        segs.append(cur)
                        cur = []
            if inside:
                cur.append(self.p(x, y))
        if cur:
            segs.append(cur)
        g = VGroup()
        for s in segs:
            if len(s) >= 2:
                g.add(VMobject(stroke_color=color, stroke_width=width, stroke_opacity=opacity)
                      .set_points_as_corners(s))
        return g

    def dots(self, pts, r=0.07, color=INK, fill=1.0):
        return VGroup(*[Dot(self.P(x, y), radius=r, color=color, fill_opacity=fill) for x, y in pts])


GRID = np.array(EV["grid"])
TRUTH = np.array(EV["truth_curve"])
TRAIN = EV["data"]["train"]


def dashed(plot, xs, ys, color=SOFT, width=4, n=48):
    return DashedVMobject(plot.curve(xs, ys, color=color, width=width)[0], num_dashes=n)


# --------------------------------------------------------------------------- B02
class B02_Setup(Scene):
    def construct(self):
        c = Clock(self, "B02")
        wide = Plot(-6.0, 6.0, -2.55, 2.45, (-1.05, 1.05), (-1.7, 1.7))     # alone on screen first
        narrow = Plot(-6.0, 1.3, -2.55, 2.45, (-1.05, 1.05), (-1.7, 1.7))   # makes room for the test set

        def parts(pl):
            ax = pl.axes()
            truth = dashed(pl, GRID, TRUTH)
            noisy = pl.dots(TRAIN, r=0.09)
            ticks = VGroup(*[Line(pl.P(x, float(np.sin(np.pi * x))), pl.P(x, y), color=GHOST, stroke_width=3)
                             for x, y in TRAIN])
            return ax, truth, noisy, ticks

        ax, truth, noisy, ticks = parts(wide)
        ax2, truth2, noisy2, ticks2 = parts(narrow)
        on_curve = VGroup(*[Dot(wide.P(x, float(np.sin(np.pi * x))), radius=0.09, color=INK) for x, _ in TRAIN])
        tag = label("the truth, hidden from the model", 36, SOFT).move_to([0, -3.0, 0])
        tag2 = label("the truth, hidden from the model", 34, SOFT).move_to([-2.35, -3.0, 0])
        tr_lab = label("training set · 16 points", 42).move_to([0, 2.95, 0])
        tr_lab2 = label("training set · 16 points", 40).move_to([-2.35, 2.95, 0])

        bx = Plot(2.35, 6.0, -2.15, 2.15, (-1.05, 1.05), (-1.7, 1.7))
        tbox = RoundedRectangle(width=3.85, height=4.5, corner_radius=0.15, color=INK, stroke_width=4
                                ).move_to([4.175, 0.0, 0])
        tdots = VGroup(*[Circle(radius=0.06, color=SOFT, stroke_width=2.5).move_to(bx.P(x, y))
                         for x, y in EV["data"]["test_preview"]])
        te_lab = label("test set · 1,000 points", 40).move_to([4.175, 2.95, 0])
        lock = label("locked away", 36, SOFT).move_to([4.175, -2.65, 0])
        fit = label("fit on these", 36).move_to([-2.35, -3.0, 0])
        grade = label("grade on these", 36).move_to([4.175, -2.65, 0])

        c.at(0.2)
        c.play(Create(ax), rt=0.6)
        c.go("smooth curve", Create(truth), rt=1.0)
        c.go("never gets", FadeIn(tag, shift=UP * 0.2), rt=0.6)
        c.go("Sixteen points", LaggedStart(*[FadeIn(d, scale=0.5) for d in on_curve], lag_ratio=0.06), rt=1.0)
        c.go("knocked off", ReplacementTransform(on_curve, noisy), Create(ticks), rt=1.0)
        c.go("training set", FadeIn(tr_lab, shift=DOWN * 0.2), rt=0.6)
        c.go("thousand more", ReplacementTransform(ax, ax2), ReplacementTransform(truth, truth2),
             ReplacementTransform(noisy, noisy2), ReplacementTransform(ticks, ticks2),
             ReplacementTransform(tag, tag2), ReplacementTransform(tr_lab, tr_lab2), rt=0.8)
        c.play(Create(tbox), LaggedStart(*[FadeIn(d) for d in tdots], lag_ratio=0.02), rt=0.9)
        c.go("locked away", tbox.animate.set_stroke(width=8), FadeIn(lock), rt=0.6)
        c.go("the test set", FadeIn(te_lab, shift=DOWN * 0.2), rt=0.6)
        c.go("model fits", truth2.animate.set_stroke(opacity=0.4), FadeOut(ticks2), FadeOut(lock),
             ReplacementTransform(tag2, fit), rt=0.8)
        c.go("We grade", FadeIn(grade, shift=UP * 0.2), tbox.animate.set_stroke(color=SPARK, width=8), rt=0.7)
        c.end()


# --------------------------------------------------------------------------- B03
class B03_ErrorMeasure(Scene):
    def construct(self):
        c = Clock(self, "B03")
        mx = EV["mse_example"]
        eq = MathTex(r"\mathrm{MSE}", "=", r"\frac{1}{n}", r"\sum_{i=1}^{n}", r"\Big(", "y_i", "-",
                     r"f(x_i)", r"\Big)^{2}", color=INK, font_size=92).move_to([0, 1.95, 0])
        mse_p, frac, sig, y_p, minus, fhat, sq = eq[0], eq[2], eq[3], eq[5], eq[6], eq[7], eq[8]

        def tag(part, text, y=0.3):
            x = float(np.clip(V(part.get_center())[0], -4.6, 4.6))
            return label(text, 36).move_to([x, y, 0])

        t_y = tag(y_p, "real value")
        t_f = tag(fhat, "model's guess")
        t_sq = label("gap, squared", 36).move_to([float(np.clip(V(sq.get_center())[0], -4.6, 4.6)), 0.3, 0])
        t_avg = tag(sig, "average over every point")

        w_lab = label("one term: the line's worst miss", 36, SOFT).move_to([0, -0.65, 0])
        w_eq = tex(r"\big({%s} - ({%s})\big)^{2} = ({%s})^{2} = {%s}" % (
            tfmt(mx["y"]), tfmt(mx["guess"]), tfmt(mx["gap"]), tfmt(mx["gap_squared"])), 60).move_to([0, -1.5, 0])
        a_lab = label("average over all 16:", 36, SOFT).move_to([-2.1, -2.55, 0])
        a_eq = tex(r"%s \div %d = %s" % (tfmt(mx["sum_squared"]), mx["n"], tfmt(mx["mse"])), 48).move_to([2.2, -2.55, 0])

        ch_tr = label("on the training points  →  training error", 40).move_to([0, -0.75, 0])
        ch_te = label("on the test points  →  test error", 40).move_to([0, -1.6, 0])
        zero = VGroup(tex(r"\mathrm{MSE} = 0", 54), label("every point hit exactly", 38)
                      ).arrange(RIGHT, buff=0.5).move_to([0, -2.65, 0])

        c.at(0.2)
        c.play(Write(eq), rt=1.3)
        spot = box(y_p, color=INK)
        c.go("real value", Create(spot), FadeIn(t_y, shift=UP * 0.2), rt=0.6)
        c.go("model's guess", Transform(spot, box(fhat, color=INK)), FadeOut(t_y), FadeIn(t_f, shift=UP * 0.2), rt=0.6)
        c.go("square it", Transform(spot, box(VGroup(minus, fhat, sq), color=INK)), FadeOut(t_f),
             FadeIn(t_sq, shift=UP * 0.2), rt=0.6)
        c.go("above and below", FadeIn(w_lab), FadeIn(w_eq, shift=UP * 0.2), rt=0.8)
        c.go("Then average", Transform(spot, box(VGroup(frac, sig), color=INK)), FadeOut(t_sq),
             FadeIn(t_avg, shift=UP * 0.2), FadeIn(a_lab), FadeIn(a_eq, shift=UP * 0.2), rt=0.8)
        c.go("On the training", FadeOut(w_lab), FadeOut(w_eq), FadeOut(a_lab), FadeOut(a_eq), FadeOut(t_avg),
             Transform(spot, box(mse_p, pad=0.16, min_w=0.42, color=INK)), FadeIn(ch_tr, shift=UP * 0.2), rt=0.7)
        c.go("On the test", FadeIn(ch_te, shift=UP * 0.2), rt=0.6)
        c.go("Zero means", FadeIn(zero, shift=UP * 0.2), Transform(spot, box(zero[0])), rt=0.8)
        c.end()


# --------------------------------------------------------------------------- B04
PANEL_X = (-4.15, 0.0, 4.15)


def panel(cx, y0=-1.55, y1=2.35):
    return Plot(cx - 1.85, cx + 1.85, y0, y1, (-1.05, 1.05), (-1.8, 1.8))


def counter(cx, y, name, value, color=INK):
    return VGroup(label(name, 36, SOFT).move_to([cx - 1.0, y, 0]),
                  num(value, 38, color).move_to([cx + 0.75, y, 0]))


class B04_ThreeFits(Scene):
    def construct(self):
        c = Clock(self, "B04")
        W = EV["worked"]
        pls = [panel(x) for x in PANEL_X]
        frames = VGroup(*[p.frame() for p in pls])
        truths = VGroup(*[dashed(p, GRID, TRUTH, color=GHOST, width=3, n=30) for p in pls])
        dots = [p.dots(TRAIN, r=0.075) for p in pls]
        heads = [label(f"degree {d}", 44).move_to([x, 2.85, 0]) for d, x in zip((1, 3, 15), PANEL_X)]
        fits = [p.curve(GRID, W[str(d)]["curve"], color=INK, width=6) for p, d in zip(pls, (1, 3, 15))]
        tr = [counter(x, -2.15, "train", fmt(W[str(d)]["train_mse"])) for d, x in zip((1, 3, 15), PANEL_X)]
        te = [counter(x, -2.9, "test", fmt(W[str(d)]["test_mse"]))
              for d, x in zip((1, 3, 15), PANEL_X)]

        c.at(0.2)
        c.play(Create(frames), FadeIn(truths), *[FadeIn(d) for d in dots], *[FadeIn(h) for h in heads], rt=0.9)
        c.go("straight line", Create(fits[0]), rt=0.9)
        c.go("two eight", FadeIn(tr[0], shift=UP * 0.2), rt=0.5)
        c.go("two seven", FadeIn(te[0], shift=UP * 0.2), rt=0.5)
        c.go("Degree three", Create(fits[1]), rt=0.9)
        c.go("zero six", FadeIn(tr[1], shift=UP * 0.2), rt=0.5)
        c.go("four seven", FadeIn(te[1], shift=UP * 0.2), rt=0.5)
        c.go("Degree fifteen", Create(fits[2]), rt=1.6)
        c.go("threads every", Indicate(dots[2], color=INK, scale_factor=1.25), rt=0.8)
        c.go("Training error zero", FadeIn(tr[2], shift=UP * 0.2), rt=0.5)
        c.go("almost ten thousand", FadeIn(te[2], scale=1.3), Create(box(te[2][1], min_h=0.7)), rt=0.7)
        c.end()


# --------------------------------------------------------------------------- B05
class B05_TheU(Scene):
    def construct(self):
        c = Clock(self, "B05")
        sw, floor = EV["sweep"], EV["setup"]["truth_test_mse"]
        pl = Plot(-5.3, 4.6, -2.45, 2.55, (0, 15), (0, 0.6))
        ax = pl.axes()
        xt = VGroup(*[num(str(d), 32, SOFT).move_to([V(pl.p(d, 0))[0], -2.8, 0]) for d in (0, 3, 6, 9, 12, 15)])
        xl = label("degree", 36, SOFT).move_to([5.35, -2.45, 0])
        yt = VGroup(*[num(s, 32, SOFT).move_to([-5.85, V(pl.p(0, v))[1], 0])
                      for s, v in (("0", 0), ("0.2", 0.2), ("0.4", 0.4), ("0.6", 0.6))])
        yl = label("error", 36, SOFT).move_to([-4.6, 2.95, 0])

        deg = np.arange(16)
        trv = np.array([s["train_mse"] for s in sw])
        tev = np.array([s["test_mse"] for s in sw])
        tr_line = pl.curve(deg, trv, color=INK, width=5)
        tr_dots = VGroup(*[Dot(pl.P(d, v), radius=0.08, color=INK) for d, v in zip(deg, trv)])
        inside = [d for d in deg if tev[d] <= 0.6]
        te_dots = VGroup(*[Dot(pl.P(d, tev[d]), radius=0.09, color=SPARK) for d in inside])
        te_fall = pl.curve(deg[:6], tev[:6], color=SPARK, width=5)
        te_rise = pl.curve(deg[5:12], tev[5:12], color=SPARK, width=5)
        exits = [d for d in deg if tev[d] > 0.6]
        arrows = VGroup(*[Arrow(pl.P(d, 0.5), pl.P(d, 0.6) + np.array([0, 0.15, 0]), buff=0, color=INK,
                                stroke_width=5, max_tip_length_to_length_ratio=0.35) for d in exits])
        exit_txt = label(" · ".join(fmt(tev[d], 1) for d in exits), 34).move_to([2.35, 3.02, 0])

        fl_y = V(pl.p(0, floor))[1]
        fl = DashedLine(pl.P(0, floor), pl.P(15, floor), color=SOFT, stroke_width=4, dash_length=0.16)
        fl_lab = label(f"noise floor {fmt(floor)}", 32, SOFT).move_to([3.0, fl_y + 0.35, 0])
        best = RoundedRectangle(width=V(pl.p(6.4, 0))[0] - V(pl.p(2.6, 0))[0], height=0.9, corner_radius=0.12,
                                color=INK, stroke_width=4).move_to([(V(pl.p(2.6, 0))[0] + V(pl.p(6.4, 0))[0]) / 2,
                                                                    fl_y + 0.12, 0])
        best_lab = label("best: degrees 3 to 6", 34).move_to([-1.15, -0.95, 0])
        leg = VGroup(VGroup(Dot([0, 0, 0], radius=0.09, color=INK), label("training error", 36)).arrange(RIGHT, buff=0.25),
                     VGroup(Dot([0, 0, 0], radius=0.09, color=SPARK), label("test error", 36)).arrange(RIGHT, buff=0.25)
                     ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([-1.6, 1.55, 0])
        over = label("overfitting", 44).move_to([3.2, 0.75, 0])
        chk = VGroup(label("same shape in", 32, SOFT), label("500 fresh datasets", 32, SOFT)
                     ).arrange(DOWN, buff=0.12).move_to([3.2, -0.2, 0])

        c.at(0.2)
        c.play(Create(ax), FadeIn(xt), FadeIn(yt), FadeIn(xl), FadeIn(yl), rt=0.8)
        c.go("Training error", FadeIn(leg[0]), LaggedStart(*[FadeIn(d, scale=0.5) for d in tr_dots], lag_ratio=0.08),
             Create(tr_line), rt=1.8)
        c.go("Test error falls", FadeIn(leg[1]), LaggedStart(*[FadeIn(te_dots[i], scale=0.5) for i in range(6)],
                                                           lag_ratio=0.15), Create(te_fall), rt=1.4)
        c.go("bottoms out", Create(best), FadeIn(best_lab, shift=UP * 0.2), rt=0.7)
        c.go("dashed line", Create(fl), FadeIn(fl_lab), rt=0.8)
        c.go("turns", LaggedStart(*[FadeIn(te_dots[i], scale=0.5) for i in range(6, len(inside))], lag_ratio=0.2),
             Create(te_rise), rt=0.9)
        c.go("leaves the chart", LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), FadeIn(exit_txt), rt=0.6)
        c.go("That U", FadeIn(over, shift=UP * 0.2), FadeIn(chk), rt=0.7)
        c.end()


# --------------------------------------------------------------------------- B06
class B06_MoreData(Scene):
    def construct(self):
        c = Clock(self, "B06")
        md = {m["n_train"]: m for m in EV["more_data"]}
        pool = EV["pool_preview"]
        floor = EV["setup"]["noise_floor_mse"]
        pl = Plot(-6.0, 0.7, -2.75, 2.25, (-1.05, 1.05), (-1.8, 1.8))
        fr = pl.frame()
        truth = dashed(pl, GRID, TRUTH, color=GHOST, width=4, n=40)

        def dots_for(n):
            r = 0.075 if n <= 30 else (0.05 if n <= 200 else 0.03)
            col = INK if n <= 30 else SOFT
            return VGroup(*[Dot(pl.P(x, y), radius=r, color=col) for x, y in pool[:n]])

        def head(n):
            return label(f"degree 15 · {n:,} points", 42).move_to([-2.65, 2.85, 0])

        cols = (1.75, 3.45, 5.1)
        hdr = VGroup(*[label(t, 34, SOFT).move_to([x, 2.85, 0]) for t, x in zip(("points", "train", "test"), cols)])
        ns = [16, 20, 30, 50, 100, 200, 1000]
        ys = [2.15 - 0.62 * i for i in range(len(ns))]
        rows = {n: VGroup(label(f"{n:,}", 38).move_to([cols[0], y, 0]),
                          label(fmt(md[n]["train_mse"]), 38).move_to([cols[1], y, 0]),
                          label(fmt(md[n]["test_mse"], 3 if md[n]["test_mse"] < 1 else 1), 38).move_to([cols[2], y, 0]))
                for n, y in zip(ns, ys)}
        fl_row = VGroup(label("noise floor", 36, SOFT).move_to([2.6, -2.6, 0]),
                        label(fmt(floor, 3), 38, SOFT).move_to([cols[2], -2.6, 0]))
        meet = RoundedRectangle(width=3.3, height=0.6, corner_radius=0.12, color=SPARK, stroke_width=6
                                ).move_to([(cols[1] + cols[2]) / 2, ys[-1], 0])  # spans 2.63..5.93

        d16, cur = dots_for(16), pl.curve(GRID, md[16]["curve"], width=6)
        h = head(16)
        c.at(0.2)
        c.play(Create(fr), FadeIn(truth), FadeIn(d16), FadeIn(h), FadeIn(hdr), FadeIn(rows[16]), rt=0.8)
        c.play(Create(cur), rt=1.2)

        def step(phrase, n, extra_rows, rt=1.0):
            nonlocal cur, h, d16
            nd, nc, nh = dots_for(n), pl.curve(GRID, md[n]["curve"], width=6), head(n)
            c.go(phrase, ReplacementTransform(d16, nd), ReplacementTransform(cur, nc), ReplacementTransform(h, nh),
                 *[FadeIn(rows[k], shift=UP * 0.15) for k in extra_rows], rt=rt)
            d16, cur, h = nd, nc, nh

        step("twenty points", 20, [20])
        step("At a hundred", 100, [30, 50, 100])
        step("At a thousand", 1000, [200, 1000])
        c.go("noise floor", FadeIn(fl_row, shift=UP * 0.15), rt=0.6)
        c.go("training error has risen", Create(meet), rt=0.8)
        c.end()


# --------------------------------------------------------------------------- B07
def trial_grid(cx, cy, bits, cell=0.29, gap=0.04):
    g = VGroup()
    step = cell + gap
    for i, b in enumerate(bits):
        r, col = divmod(i, 10)
        x = cx + (col - 4.5) * step
        y = cy + (4.5 - r) * step
        g.add(Square(side_length=cell, stroke_width=0, fill_color=SPARK if b else GHOST,
                     fill_opacity=1.0 if b else 0.5).move_to([x, y, 0]))
    return g


def split_strip(y, h, size, se):
    """The train / validation / test split, block widths proportional to their sizes."""
    tot = se["n_train"] + se["n_validation"] + se["n_test"]
    widths = [11.8 * k / tot for k in (se["n_train"], se["n_validation"], se["n_test"])]
    xs, x = [], -5.9
    for w in widths:
        xs.append(x + w / 2)
        x += w
    names = (f"train · {se['n_train']}", f"validation · {se['n_validation']}", f"test · {se['n_test']}")
    blocks = VGroup(*[VGroup(Rectangle(width=w - 0.08, height=h, color=INK, stroke_width=3).move_to([cx, y, 0]),
                             label(t, size).move_to([cx, y, 0])) for w, cx, t in zip(widths, xs, names)])
    hi = [Rectangle(width=w - 0.08, height=h, color=INK, stroke_width=7).move_to([cx, y, 0])
          for w, cx in zip(widths, xs)]
    return blocks, hi


class B07_PeekedScore(Scene):
    def construct(self):
        c = Clock(self, "B07")
        se = EV["selection"]
        big, big_hi = split_strip(1.85, 1.2, 44, se)          # intro: the split fills the middle
        top, top_hi = split_strip(2.75, 0.72, 34, se)         # later: parked at the top
        step = 0.74
        cx = [-5.55 + d * step for d in range(16)]
        chips = VGroup(*[VGroup(RoundedRectangle(width=0.66, height=0.66, corner_radius=0.08, color=GHOST,
                                                 stroke_width=3).move_to([x, -0.15, 0]),
                                num(str(d), 34).move_to([x, -0.15, 0])) for d, x in enumerate(cx)])
        chips_lab = label("sixteen candidates, each fitted on train, scored on validation", 36, SOFT
                          ).move_to([0, -1.2, 0])
        pick_d = se["most_picked_degree"]
        pick = RoundedRectangle(width=0.86, height=0.86, corner_radius=0.1, color=INK, stroke_width=6
                                ).move_to([cx[pick_d], -0.15, 0])
        pick_lab = label(f"keep the best validation score (most often degree {pick_d})", 38).move_to([0, -2.3, 0])

        gx = (-3.45, 1.75)
        cap = label("one square per repeat · terracotta: looked better than real", 32, SOFT).move_to([0, 1.95, 0])
        t_l = label("report on validation", 36).move_to([gx[0], 1.4, 0])
        t_r = label("report on untouched test", 36).move_to([gx[1], 1.4, 0])
        g_l = trial_grid(gx[0], -0.55, se["grid100_peek"])
        g_r = trial_grid(gx[1], -0.55, se["grid100_untouched"])
        ghosts = VGroup(*[Square(side_length=0.29, color=GHOST, stroke_width=2).move_to(V(q.get_center()).tolist())
                          for q in [*g_l, *g_r]])
        pk, ut, ctl = se["peek"], se["untouched_test"], se["control_fixed_degree_3"]
        n_l = label(f"{round(pk['share_optimistic'] * 100)}% of 1,000 repeats too rosy", 36).move_to([gx[0], -2.55, 0])
        n_r = label(f"{round(ut['share_optimistic'] * 100)}% of 1,000 repeats", 36).move_to([gx[1], -2.55, 0])
        m_l = label(f"median {fmt(pk['median_reported'], 4)} vs real {fmt(pk['median_real'], 4)}", 32, SOFT
                    ).move_to([gx[0], -3.05, 0])
        m_r = label(f"median {fmt(ut['median_reported'], 4)} vs real {fmt(ut['median_real'], 4)}", 32, SOFT
                    ).move_to([gx[1], -3.05, 0])
        ctl_t = VGroup(label("degree fixed", 34, SOFT), label("in advance:", 34, SOFT),
                       label(f"{round(ctl['share_optimistic'] * 100)}%", 40, SOFT)
                       ).arrange(DOWN, buff=0.15).move_to([4.95, -0.55, 0])

        c.at(0.2)
        c.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in big], lag_ratio=0.25), rt=0.9)
        c.go("all sixteen degrees", LaggedStart(*[FadeIn(ch, shift=UP * 0.15) for ch in chips], lag_ratio=0.05),
             FadeIn(chips_lab), rt=1.0)
        c.go("scores best", Create(big_hi[1]), Create(pick), FadeIn(pick_lab, shift=UP * 0.15), rt=0.7)
        c.go("Across a thousand", FadeOut(chips), FadeOut(chips_lab), FadeOut(pick), FadeOut(pick_lab),
             ReplacementTransform(big, top), ReplacementTransform(big_hi[1], top_hi[1]),
             FadeIn(cap), FadeIn(t_l), FadeIn(ghosts), rt=0.7)
        c.play(LaggedStart(*[FadeIn(q) for q in g_l], lag_ratio=0.01), rt=1.2)
        c.go("seven times", FadeIn(n_l, shift=UP * 0.15), FadeIn(m_l), rt=0.6)
        c.go("The fix", FadeIn(t_r), Create(top_hi[2]), rt=0.6)
        c.go("nobody touched", LaggedStart(*[FadeIn(q) for q in g_r], lag_ratio=0.01), rt=1.2)
        c.go("half and half", FadeIn(n_r, shift=UP * 0.15), FadeIn(m_r), FadeIn(ctl_t), rt=0.7)
        c.end()
