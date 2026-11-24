"""Manim scenes for "Softmax and Temperature, Explained" (claude-liam-softmax-temperature).

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/softmax_demo.py).
Animation in-betweens (bars morphing between temperatures) are recomputed with the same
softmax and asserted against the evidence at every temperature the film names.
Each scene ends exactly at its beat's measured audio duration.
One Scene subclass per Manim beat, named with its beat id prefix (run.sh finds them by regex).
"""
from manim import *
import json
import math
import os
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# GATE A pre-flights an isolated copy of this file; fall back to the reel folder.
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-softmax-temperature"))


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
SEG_A, SEG_B = "#ECE8DC", "#DDD7C6"          # light warm fills for probability-strip segments
SERIF, MONO = "EB Garamond", "PT Mono"
config.background_color = PAGE

TOK, Z = EV["tokens"], EV["logits"]


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
            self.s.wait((frames + 0.01) / FPS)      # static waits floor int(d*fps): nudge up
            self.t += frames / FPS
        elif t - self.t < -0.05:
            print(f"[clock] {self.bid}: running {self.t - t:.2f}s late at t={t:.2f}")

    def play(self, *anims, rt=1.0):
        frames = max(1, int(np.ceil(rt * FPS - 1e-6)))
        self.s.play(*anims, run_time=(frames - 0.01) / FPS)   # plays ceil via arange: nudge down
        self.t += frames / FPS

    def go(self, phrase, *anims, rt=1.0, nth=0, lead=0.15):
        self.at(max(0.0, cue(self.bid, phrase, nth) - lead))
        self.play(*anims, rt=rt)

    def hold(self, phrase, nth=0, lead=0.15):
        """Wait until just before `phrase` (the next plays start on the word)."""
        self.at(max(0.0, cue(self.bid, phrase, nth) - lead))

    def end(self):
        self.at(DUR[self.bid])


# ------------------------------------------------------------------ small helpers
def label(s, size=36, color=INK, font=SERIF):
    return Text(s, font=font, font_size=size, color=color)


def num(s, size=36, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def tex(s, size=48, color=INK):
    return MathTex(s, font_size=size, color=color)


def V(v):
    """Any point-like to a float vector (the GATE A geometry stub returns placeholders)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def W(m, d=1.0):
    try:
        return float(m.width)
    except (TypeError, ValueError, AttributeError):
        return d


def P(x, y):
    return [float(x), float(y), 0.0]


def right_at(m, x_right, y):
    return m.move_to(P(x_right - W(m) / 2, y))


def left_at(m, x_left, y):
    return m.move_to(P(x_left + W(m) / 2, y))


def box(part, pad=0.16, min_w=0.42, min_h=0.9, color=SPARK):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '-')."""
    w = max(W(part, 0.5) + pad, min_w)
    try:
        h = max(float(part.height) + pad, min_h)
    except (TypeError, ValueError, AttributeError):
        h = min_h
    if color == SPARK and w > 1.4 * h:          # GATE T: a terracotta shape >= 1.5x wide reads as accent text
        h = w / 1.4
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color,
                            stroke_width=6).move_to(V(part.get_center()).tolist())


def spot(part, side="up", pad=0.16, min_h=0.62, gap=0.24):
    """Spotlight = GHOST outline (never read as text by GATE T) + one compact terracotta dot."""
    b = box(part, pad=pad, min_h=min_h, color=GHOST)
    c = V(part.get_center())
    w = max(W(part, 0.5) + pad, 0.42)
    try:
        h = max(float(part.height) + pad, min_h)
    except (TypeError, ValueError, AttributeError):
        h = min_h
    off = {"up": (0, h / 2 + gap), "down": (0, -h / 2 - gap), "left": (-w / 2 - gap, 0),
           "right": (w / 2 + gap, 0)}[side]
    x = float(np.clip(c[0] + off[0], -6.0, 6.0))   # clamp: the GATE A stub over-estimates MathTex widths
    y = float(np.clip(c[1] + off[1], -3.3, 3.3))
    return VGroup(b, Dot(P(x, y), radius=0.11, color=SPARK))


def pct(x):
    return f"{float(x):.1f}%"


def softmax(z, T):
    a = np.asarray(z, dtype=float) / T
    e = np.exp(a - a.max())
    return e / e.sum()


def ev_probs(T):
    """Evidence probabilities at an evidence temperature, cross-checked against softmax()."""
    p = EV["sweep"][str(float(T))]["p"]
    assert np.allclose(p, softmax(Z, T), atol=1e-4), f"softmax disagrees with evidence at T={T}"
    return list(p)


def hbar(value, scale, x0, y, h=0.5, color=INK, opacity=1.0):
    w = max(0.04, float(value) * scale)
    return Rectangle(width=w, height=h, stroke_width=0, fill_color=color,
                     fill_opacity=opacity).move_to(P(x0 + w / 2, y))


def bar_rows(ps, x0, ys, scale, accent=None, h=0.5, vsize=32, pcts=None):
    """Bars + value texts for a list of probabilities (values shown only when pcts given)."""
    bars, vals = VGroup(), VGroup()
    for i, (p, y) in enumerate(zip(ps, ys)):
        bars.add(hbar(p, scale, x0, y, h=h, color=INK))          # wide bars stay INK (GATE T)
        if pcts is not None:
            vals.add(left_at(num(pct(pcts[i]), vsize), x0 + max(0.04, p * scale) + 0.18, y))
    return bars, vals


def names(tokens, x_right, ys, size=36):
    return VGroup(*[right_at(label(t, size), x_right, y) for t, y in zip(tokens, ys)])


def badges(n, x, ys, r=0.26):
    return VGroup(*[VGroup(Circle(radius=r, color=INK, stroke_width=3).move_to(P(x, y)),
                           num(str(i + 1), 32).move_to(P(x, y))) for i, y in zip(range(n), ys)])


def strip(ps, x0, x1, y, h, tokens=TOK, min_label_w=1.0, size=32, fill=None, gap=0.05):
    """A 0-to-1 probability strip: solid INK / SOFT segments split by thin page gaps,
    labels BELOW the strip (no text inside a closed shape — GATE T 8.6b)."""
    segs, labs = VGroup(), VGroup()
    x = x0
    for i, p in enumerate(ps):
        w = max(0.02, float(p) * (x1 - x0))
        col = fill if fill else (INK if i % 2 == 0 else SOFT)
        segs.add(Rectangle(width=max(0.02, w - gap), height=h, stroke_width=0, fill_color=col,
                           fill_opacity=1).move_to(P(x + w / 2, y)))
        t = label(tokens[i], size)
        if w >= max(min_label_w, W(t) + 0.2):
            labs.add(t.move_to(P(x + w / 2, y - h / 2 - 0.3)))
        x += w
    return segs, labs


def mark(x, y_edge, h=0.45, color=SPARK, sw=4):
    """A roll marker standing on a strip's top edge (never crosses the segment labels)."""
    return Line(P(x, y_edge), P(x, y_edge + h), color=color, stroke_width=sw)


# --------------------------------------------------------------------------- B02
class B02_Machine(Scene):
    def construct(self):
        c = Clock(self, "B02")
        p1 = EV["worked"]["p"]
        pc1 = EV["worked"]["pct"]
        ys = [0.85, 0.2, -0.45, -1.1, -1.75]

        prompt = left_at(label("The cat sat on the", 40), -5.7, 2.6)
        blank = Line(P(-1.85, 2.38), P(-0.95, 2.38), color=INK, stroke_width=3)
        chip = RoundedRectangle(width=5.4, height=0.95, corner_radius=0.14, color=GHOST,
                                stroke_width=3).move_to(P(-3.33, 2.6))
        model = VGroup(RoundedRectangle(width=2.2, height=0.95, corner_radius=0.14, color=GHOST,
                                        stroke_width=4).move_to(P(1.0, 2.6)),
                       label("model", 40).move_to(P(1.0, 2.6)))
        die_sq = RoundedRectangle(width=0.95, height=0.95, corner_radius=0.14, color=INK,
                                  stroke_width=4).move_to(P(5.35, 2.6))
        die = VGroup(die_sq, *[Dot(P(5.35 + dx, 2.6 + dy), radius=0.07, color=INK)
                               for dx, dy in ((-0.24, 0.24), (0, 0), (0.24, -0.24))])
        sampler = right_at(label("sampler", 36), 4.7, 2.6)
        soft = VGroup(RoundedRectangle(width=2.1, height=0.95, corner_radius=0.14, color=GHOST,
                                       stroke_width=4).move_to(P(-0.15, -0.45)),
                      label("softmax", 40).move_to(P(-0.15, -0.45)))

        a_pm = Arrow(P(-0.6, 2.6), P(-0.1, 2.6), buff=0, color=INK, stroke_width=4,
                     max_tip_length_to_length_ratio=0.35)
        a_ml = Arrow(P(0.2, 2.1), P(-2.9, 1.5), buff=0, color=INK, stroke_width=4,
                     max_tip_length_to_length_ratio=0.08)
        a_ls = Arrow(P(-1.8, -0.45), P(-1.25, -0.45), buff=0, color=INK, stroke_width=4,
                     max_tip_length_to_length_ratio=0.35)
        a_sp = Arrow(P(0.95, -0.45), P(1.4, -0.45), buff=0, color=INK, stroke_width=4,
                     max_tip_length_to_length_ratio=0.4)
        a_pd = Arrow(P(5.35, 1.25), P(5.35, 2.08), buff=0, color=INK, stroke_width=4,
                     max_tip_length_to_length_ratio=0.25)

        lhead = label("logits", 36, SOFT).move_to(P(-3.9, 1.5))
        lnames = names(TOK, -4.55, ys)
        lbars = VGroup(*[hbar(z, 0.55, -4.4, y, h=0.42) for z, y in zip(Z, ys)])
        lvals = VGroup(*[left_at(num(f"{z:g}", 32), -4.4 + z * 0.55 + 0.15, y) for z, y in zip(Z, ys)])
        cons = VGroup(label("constructed logits:", 32, SOFT),
                      label("5 of the whole vocabulary", 32, SOFT)).arrange(DOWN, buff=0.12)
        cons.move_to(P(-3.75, -2.62))

        phead = label("probabilities", 36, SOFT).move_to(P(3.9, 1.5))
        pnames = names(TOK, 2.7, ys)
        pbars, pvals = bar_rows(p1, 2.85, ys, 3.2, h=0.42, pcts=pc1)
        pick = EV["runs20"]["by_T"]["1.0"]["picks"][0]
        word_t = label(pick, 40).move_to(P(5.35, 2.6))
        word = VGroup(word_t, box(word_t, pad=0.3, min_w=1.0, min_h=0.75))   # terracotta ring, ink text
        again = label("again, for the next token", 34, SOFT).move_to(P(3.9, -2.62))
        ghost = VGroup(lbars, pbars).copy().set_color(GHOST)          # shapes only: no low-contrast text

        c.at(0.2)
        c.play(FadeIn(model), FadeIn(soft), FadeIn(die), FadeIn(sampler), FadeIn(ghost), rt=0.3)
        c.go("You type", Create(chip), FadeIn(prompt), Create(blank), rt=0.8)
        c.go("doesn't hand back", GrowArrow(a_pm), rt=0.5)
        c.go("It hands back", GrowArrow(a_ml), FadeIn(lhead), FadeIn(lnames), rt=0.7)
        c.go("called a logit", LaggedStart(*[GrowFromEdge(b, LEFT) for b in lbars], lag_ratio=0.15),
             FadeIn(lvals), rt=0.9)
        c.go("five of them", FadeIn(cons, shift=UP * 0.15), rt=0.6)
        c.go("Softmax turns", GrowArrow(a_ls), Indicate(soft, color=INK, scale_factor=1.06), rt=0.6)
        c.play(GrowArrow(a_sp), FadeIn(phead), FadeIn(pnames),
               LaggedStart(*[GrowFromEdge(b, LEFT) for b in pbars], lag_ratio=0.15), FadeIn(pvals), rt=0.9)
        c.go("A sampler rolls", GrowArrow(a_pd), Rotate(die, angle=PI / 2), rt=0.7)
        c.go("picks one token", FadeOut(die), FadeIn(word, scale=1.3), rt=0.5)
        c.go("appends it", word.animate.move_to(P(-1.4, 2.62)), FadeOut(blank), rt=0.8)
        c.go("loop runs again", Indicate(a_pm, color=INK, scale_factor=1.4), FadeIn(again, shift=UP * 0.15),
             FadeIn(die), rt=0.8)
        c.end()


# --------------------------------------------------------------------------- B03
class B03_Formula(Scene):
    def construct(self):
        c = Clock(self, "B03")
        lhs = tex(r"p_i =", 120).move_to(P(-2.9, 0.55))
        bar = Line(P(-1.4, 0.55), P(3.2, 0.55), color=INK, stroke_width=6)
        numer = tex(r"e^{z_i/T}", 110).next_to(bar, UP, buff=0.24)
        denom = tex(r"\sum_j e^{z_j/T}", 110).next_to(bar, DOWN, buff=0.2)
        g = numer[0]
        zi = VGroup(g[1], g[2])
        tt = g[4]
        zt = VGroup(g[1], g[2], g[3], g[4])

        lab_z = label("logit (a score)", 36).move_to(P(-0.4, 2.8))
        lab_t = VGroup(label("temperature,", 36), tex(r"T > 0", 44)).arrange(RIGHT, buff=0.2).move_to(P(4.1, 2.8))
        lab_n = label("always positive", 36).move_to(P(4.6, 1.25))
        lab_d = VGroup(label("same thing, summed", 34),
                       label("over every token", 34)).arrange(DOWN, buff=0.1).move_to(P(-3.8, -1.25))
        one = tex(r"\textstyle\sum_i p_i = 1", 60).move_to(P(-3.8, -2.6))
        mono = tex(r"z_a > z_b \;\Rightarrow\; p_a > p_b", 52).move_to(P(3.2, -2.7))
        first = label("temperature acts first", 36).move_to(P(-0.4, 2.8))

        c.at(0.2)
        # ghost slots where the side labels will land (canvas fill before they are spoken)
        slots = VGroup(RoundedRectangle(width=2.9, height=0.62, corner_radius=0.1, color=GHOST,
                                        stroke_width=3).move_to(P(4.6, 1.25)),
                       RoundedRectangle(width=3.9, height=1.05, corner_radius=0.1, color=GHOST,
                                        stroke_width=3).move_to(P(-3.8, -1.25)))
        c.play(Write(lhs), Write(numer), Create(bar), Write(denom), FadeIn(slots), rt=0.8)
        sp = spot(zi, "up", pad=0.05)
        c.go("Take each", Create(sp[0]), FadeIn(sp[1]), FadeIn(lab_z, shift=DOWN * 0.15), rt=0.6)
        c.go("divide it by", Transform(sp, spot(tt, "up")), FadeIn(lab_t, shift=DOWN * 0.15), rt=0.6)
        c.go("Raise e", Transform(sp, spot(numer, "up")), FadeIn(lab_n, shift=LEFT * 0.15), FadeOut(slots[0]), rt=0.6)
        c.go("Then divide", Transform(sp, spot(denom, "left")), FadeIn(lab_d, shift=RIGHT * 0.15), FadeOut(slots[1]), rt=0.6)
        c.go("add up to", FadeIn(one, shift=UP * 0.15), rt=0.6)
        c.go("A bigger logit", FadeIn(mono, shift=UP * 0.15), rt=0.6)
        c.go("temperature acts first", Transform(sp, spot(zt, "up", pad=0.05)), FadeOut(lab_z), rt=0.35)
        c.play(FadeIn(first), rt=0.35)
        c.end()


# --------------------------------------------------------------------------- B04
class B04_WorkedT1(Scene):
    def construct(self):
        c = Clock(self, "B04")
        wk = EV["worked"]
        assert np.allclose(wk["p"], softmax(Z, 1.0), atol=1e-4), "B04 disagrees with softmax"
        ys = [1.25, 0.5, -0.25, -1.0, -1.75]
        XT, XZ, XE, XP, X0, SC = -5.0, -3.2, -1.0, 1.3, 2.55, 6.0

        title = VGroup(label("at temperature", 36, SOFT), tex(r"T = 1", 52)).arrange(RIGHT, buff=0.25)
        title.move_to(P(-3.6, 2.85))
        formula = tex(r"p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}", 46).move_to(P(4.3, 2.45))
        heads = VGroup(label("token", 36, SOFT).move_to(P(XT, 1.95)), tex("z", 50).move_to(P(XZ, 1.95)),
                       tex("e^{z}", 50).move_to(P(XE, 1.95)), tex("p", 50).move_to(P(XP, 1.95)))
        rule = Line(P(-6.0, 1.66), P(2.2, 1.66), color=GHOST, stroke_width=3)
        toks = VGroup(*[label(t, 38).move_to(P(XT, y)) for t, y in zip(TOK, ys)])
        zs = VGroup(*[num(f"{z:g}", 38).move_to(P(XZ, y)) for z, y in zip(Z, ys)])
        es = VGroup(*[num(f"{e:.2f}", 38).move_to(P(XE, y)) for e, y in zip(wk["exp"], ys)])
        ps = VGroup(*[num(pct(p), 38).move_to(P(XP, y)) for p, y in zip(wk["pct"], ys)])
        sum_rule = Line(P(-2.1, -2.2), P(0.1, -2.2), color=INK, stroke_width=3)
        total = VGroup(label("sum", 34, SOFT), num(f"{wk['sum']:.2f}", 40)).arrange(RIGHT, buff=0.25)
        total.move_to(P(-1.0, -2.72))
        ring = spot(total, "left", pad=0.24, min_h=0.66)           # ghost outline + terracotta dot
        div = tex(r"\div\; " + f"{wk['sum']:.2f}", 44).move_to(P(XP + 0.3, -2.72))
        bars, _ = bar_rows(wk["p"], X0, ys, SC, h=0.46)
        ghost = bars.copy().set_color(GHOST)
        dice = label("the dice", 40).move_to(P(4.3, -2.72))

        c.at(0.2)
        c.play(FadeIn(title), FadeIn(formula), FadeIn(heads), Create(rule), FadeIn(toks), FadeIn(ghost), rt=0.9)
        c.go("Mat scores", LaggedStart(*[FadeIn(z, shift=LEFT * 0.15) for z in zs], lag_ratio=0.15), rt=0.9)
        c.go("Raise e", LaggedStart(*[FadeIn(e, shift=LEFT * 0.15) for e in es], lag_ratio=0.15), rt=1.0)
        c.go("Add all five", Create(sum_rule), FadeIn(total, shift=UP * 0.15), rt=0.7)
        c.play(Create(ring), rt=0.4)
        c.go("Divide each", FadeIn(div, shift=LEFT * 0.15), rt=0.6)
        c.go("Mat gets", LaggedStart(*[FadeIn(p, shift=LEFT * 0.15) for p in ps], lag_ratio=0.2), rt=1.4)
        c.go("Those shares", LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.1),
             FadeIn(dice), rt=1.0)
        c.end()


# --------------------------------------------------------------------------- B05
YS5 = [1.9, 0.95, 0.0, -0.95, -1.9]
X05, SC5 = -3.6, 5.6
SX, SY0, SY1 = 4.95, -1.9, 1.9


def slider_y(T):
    return SY0 + math.log(T / 0.2) / math.log(10.0) * (SY1 - SY0)


class B05_TempSweep(Scene):
    def construct(self):
        c = Clock(self, "B05")
        sw = EV["sweep"]
        p = {T: ev_probs(T) for T in (0.2, 1.0, 2.0)}
        pc = {T: sw[str(T)]["pct"] for T in (0.2, 1.0, 2.0)}
        assert EV["order_preserved"]

        head = label("The cat sat on the ___", 34, SOFT).move_to(P(-2.4, 2.85))
        bdg = badges(5, -5.6, YS5)
        nm = names(TOK, -3.75, YS5)
        rail = Line(P(SX, SY0), P(SX, SY1), color=INK, stroke_width=4)
        ticks = VGroup(*[Line(P(SX - 0.14, slider_y(T)), P(SX + 0.14, slider_y(T)), color=INK, stroke_width=4)
                         for T in (0.2, 1.0, 2.0)])
        tlabs = VGroup(*[right_at(tex(s, 40), SX - 0.3, slider_y(T))
                         for s, T in (("0.2", 0.2), ("1", 1.0), ("2", 2.0))])
        tname = tex("T", 46).move_to(P(SX, 2.35))
        knob = Circle(radius=0.2, color=INK, fill_color=INK, fill_opacity=1).move_to(P(SX, slider_y(1.0)))
        flat = label("flattens", 34).move_to(P(5.25, 2.95))
        sharp = label("sharpens", 34).move_to(P(SX, -2.5))

        def state(T, accent=None, values=True):
            pp = p[T] if T in p else list(softmax(Z, T))
            return bar_rows(pp, X05, YS5, SC5, accent=accent, h=0.55, pcts=pc[T] if values else None)

        bars, vals = state(1.0)
        g5 = tex(r"\text{every gap} \times 5", 44).move_to(P(1.6, 2.85))
        gh = tex(r"\text{every gap} \times \tfrac{1}{2}", 44).move_to(P(1.6, 2.85))
        order = label("the order never changes", 38).move_to(P(-0.8, -2.75))

        def sweep(T_from, T_to, accent, steps=5, rt=1.2):
            """Bars morph through in-between temperatures; values hidden until the end state."""
            Ts = np.geomspace(T_from, T_to, steps + 1)[1:]
            for T in Ts:
                tgt, _ = state(float(T), accent=accent, values=False)
                c.play(Transform(bars, tgt), knob.animate.move_to(P(SX, slider_y(float(T)))), rt=rt / steps)

        c.at(0.2)
        c.play(FadeIn(head), FadeIn(bdg), FadeIn(nm), FadeIn(bars), FadeIn(vals), Create(rail),
               FadeIn(ticks), FadeIn(tlabs), FadeIn(tname), FadeIn(knob), rt=0.6)
        c.go("At zero point two", FadeOut(vals), rt=0.25)
        sweep(1.0, 0.2, None, steps=4, rt=0.8)
        _, vals = state(0.2)
        c.go("every gap grows", FadeIn(vals), FadeIn(g5, shift=DOWN * 0.15), rt=0.5)
        mdot = Dot(P(V(nm[0].get_left())[0] - 0.3, YS5[0]), radius=0.12, color=SPARK)   # the one accent
        c.go("mat takes", FadeIn(mdot, scale=1.6), Indicate(vals[0], color=INK), rt=0.6)
        c.go("At two", FadeOut(vals), FadeOut(g5), FadeIn(gh, shift=DOWN * 0.15), rt=0.25)
        sweep(0.2, 2.0, 0, steps=5, rt=0.9)
        _, vals = state(2.0)
        c.go("mat falls", FadeIn(vals), rt=0.4)
        c.go("roof climbs", Indicate(vals[4], color=INK, scale_factor=1.4), rt=0.7)
        c.go("Low temperature sharpens", FadeIn(sharp, shift=UP * 0.15), rt=0.5)
        c.go("High temperature flattens", FadeIn(flat, shift=DOWN * 0.15), rt=0.5)
        frame = SurroundingRectangle(bdg, color=INK, buff=0.15, stroke_width=3)
        c.go("watch the order", Create(frame), FadeOut(vals), FadeOut(gh), rt=0.4)
        sweep(2.0, 0.2, 0, steps=4, rt=0.6)
        sweep(0.2, 1.0, 0, steps=3, rt=0.5)
        _, vals = state(1.0, accent=0)
        c.play(FadeIn(vals), FadeIn(order, shift=UP * 0.15), rt=0.4)
        c.end()


# --------------------------------------------------------------------------- B06
class B06_Rolls(Scene):
    def construct(self):
        c = Clock(self, "B06")
        R = EV["runs20"]
        U = R["u"]
        p1 = ev_probs(1.0)
        rows = [(0.2, 2.1), (1.0, 0.0), (2.0, -2.1)]
        SX0, SX1 = -4.3, 1.5
        BX0, BX1 = -5.6, 5.6                       # the single big strip, full width
        H = 0.62

        bdg_n = names(TOK, -3.75, YS5)
        bars0, _ = bar_rows(p1, X05, YS5, SC5, h=0.55)

        big, big_l = strip(p1, BX0, BX1, 0.0, 0.9, size=36)
        mat_l = big_l[0]                           # the widest segment is always labelled first
        mat_win = label(f"{R['by_T']['1.0']['picks'][0]} wins", 36).move_to(V(mat_l.get_center()).tolist())
        zero = tex("0", 44).move_to(P(BX0, 0.8))
        onel = tex("1", 44).move_to(P(BX1, 0.8))
        u0 = U[0]
        x_u0 = BX0 + (BX1 - BX0) * u0
        t0 = mark(x_u0, 0.45, 0.5, sw=6)
        ulab = tex(rf"u = {u0:.2f}", 44).move_to(P(x_u0, 1.25))

        strips, ticksets, rlabs = [], [], []
        for T, y in rows:
            s, l = strip(ev_probs(T), SX0, SX1, y, H, size=32)
            strips.append(VGroup(s, l))
            ticksets.append(VGroup(*[mark(SX0 + (SX1 - SX0) * u, y + H / 2, 0.55, sw=3) for u in U]))
            rlabs.append(tex(rf"T = {T:g}", 44).move_to(P(-5.25, y)))

        def detail(T):
            cnt = R["by_T"][str(T)]["counts"]
            items = [f"{k} {v}" for k, v in cnt.items() if v]
            return [" · ".join(items[i:i + 3]) for i in range(0, len(items), 3)]

        heads = {0.2: f"1 word: mat, {R['by_T']['0.2']['counts']['mat']} of 20",
                 1.0: f"{R['by_T']['1.0']['distinct']} different words",
                 2.0: f"all {R['by_T']['2.0']['distinct']}, even roof"}
        results = []
        for T, y in rows:
            texts = [(heads[T], 36, INK)] + [(s, 32, SOFT) for s in (detail(T) if T != 0.2 else [])]
            y_top = y + 0.23 * (len(texts) - 1)
            results.append(VGroup(*[label(s, sz, col).move_to(P(3.85, y_top - 0.46 * k))
                                    for k, (s, sz, col) in enumerate(texts)]))

        # ghost of the three-row layout (outlines only) while the single strip is explained:
        # keeps the canvas filled at the beat midpoint without adding low-contrast mass
        ghost = VGroup(*[Rectangle(width=SX1 - SX0, height=H, color=GHOST, stroke_width=3).move_to(P((SX0 + SX1) / 2, y))
                         for T, y in rows if T != 1.0],
                       *[Rectangle(width=3.9, height=0.5, color=GHOST, stroke_width=3).move_to(P(3.85, y))
                         for T, y in rows if T != 1.0])

        c.at(0.2)
        c.play(FadeIn(bdg_n), FadeIn(bars0), rt=0.7)
        c.go("Lay the probabilities", ReplacementTransform(bars0, big), FadeOut(bdg_n), FadeIn(ghost), rt=1.0)
        c.play(FadeIn(big_l), FadeIn(zero), FadeIn(onel), rt=0.5)
        c.go("A seeded random", Create(t0), FadeIn(ulab), rt=0.6)
        c.go("whichever token", FadeOut(mat_l), FadeIn(mat_win), rt=0.6)
        c.go("the same twenty", FadeOut(VGroup(t0, ulab, mat_win, zero, onel, big_l[1:], ghost)),
             ReplacementTransform(big, strips[1][0]), FadeIn(strips[1][1]),
             FadeIn(strips[0]), FadeIn(strips[2]), *[FadeIn(r) for r in rlabs], rt=0.9)
        c.play(*[LaggedStart(*[Create(t) for t in ts], lag_ratio=0.05) for ts in ticksets], rt=1.2)
        c.go("At zero point two", FadeIn(results[0], shift=LEFT * 0.15), rt=0.6)
        c.go("At one", FadeIn(results[1], shift=LEFT * 0.15), rt=0.6)
        c.go("At two", FadeIn(results[2], shift=LEFT * 0.15), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B07
class B07_TenThousand(Scene):
    def construct(self):
        c = Clock(self, "B07")
        K = EV["draws10k"]
        k1 = K["1.0"]
        ys = [1.4, 0.6, -0.2, -1.0, -1.8]
        X0, SC = -4.1, 5.5
        pred = [x / 100 for x in k1["predicted_pct"]]
        obs = [x / 100 for x in k1["observed_pct"]]

        leg1 = label("outline: softmax prediction", 32).move_to(P(-3.4, 2.85))
        leg2 = label(f"solid: {k1['n']:,} seeded rolls", 32).move_to(P(-3.6, 2.35))
        tlab = tex(r"T = 1", 44).move_to(P(-0.6, 2.35))
        nm = names(TOK, -4.3, ys)
        outl = VGroup(*[Rectangle(width=max(0.04, q * SC), height=0.55, color=GHOST, stroke_width=4,
                                  fill_opacity=0).move_to(P(X0 + max(0.04, q * SC) / 2, y))
                        for q, y in zip(pred, ys)])
        solid = VGroup(*[hbar(q, SC, X0, y, h=0.34, opacity=0.8) for q, y in zip(obs, ys)])
        mat = TOK.index("mat")
        mcount = VGroup(label("mat", 36), num(pct(k1["predicted_pct"][mat]), 36), tex(r"\to", 44),
                        num(pct(k1["observed_pct"][mat]), 36)).arrange(RIGHT, buff=0.22)
        mcount.move_to(P(-3.1, -2.75))

        def panel(T, base, lab_xy, gap_y):
            d = K[str(T)]
            xs = [1.9 + 0.85 * i for i in range(5)]
            o = VGroup(*[Rectangle(width=0.55, height=max(0.03, q / 100 * 1.6), color=GHOST, stroke_width=4,
                                   fill_opacity=0).move_to(P(x, base + max(0.03, q / 100 * 1.6) / 2))
                         for q, x in zip(d["predicted_pct"], xs)])
            s = VGroup(*[Rectangle(width=0.16, height=max(0.03, q / 100 * 1.6), stroke_width=0, fill_color=INK,
                                   fill_opacity=0.8).move_to(P(x, base + max(0.03, q / 100 * 1.6) / 2))
                         for q, x in zip(d["observed_pct"], xs)])
            axis = Line(P(1.45, base), P(5.75, base), color=GHOST, stroke_width=3)
            lab = tex(rf"T = {T:g}", 44).move_to(P(*lab_xy))
            gap = label(f"largest gap {d['max_abs_gap_pct']:g} pts", 32, SOFT).move_to(P(3.6, gap_y))
            return VGroup(axis, o, s, lab), gap

        pa, ga = panel(0.2, 1.0, (5.0, 2.35), 0.55)
        pb, gb = panel(2.0, -1.5, (2.3, -0.45), -1.95)
        g1 = label(f"largest gap {k1['max_abs_gap_pct']:g} pts", 32, SOFT).move_to(P(-1.0, -2.2))
        verdict = label("prediction survives", 40).move_to(P(3.6, -2.75))
        vring = spot(verdict, "left", pad=0.3, min_h=0.72)         # ghost outline + terracotta dot
        ghost = VGroup(*pa[:3], *pb[:3]).copy().set_color(GHOST)      # axes + columns, no text

        c.at(0.2)
        c.play(FadeIn(tlab), FadeIn(nm), FadeIn(ghost), rt=0.7)
        c.go("test the claim", FadeIn(leg1), FadeIn(leg2), rt=0.6)
        c.go("ten thousand rolls", LaggedStart(*[Create(o) for o in outl], lag_ratio=0.12), rt=1.0)
        c.go("the count comes", LaggedStart(*[GrowFromEdge(s, LEFT) for s in solid], lag_ratio=0.1),
             FadeIn(mcount, shift=UP * 0.15), rt=1.0)
        c.go("Across all three", FadeIn(pa), FadeIn(pb), FadeOut(ghost), rt=0.9)
        c.go("nothing misses", FadeIn(g1), FadeIn(ga), FadeIn(gb), rt=0.6)
        c.play(FadeIn(verdict), Create(vring), rt=0.5)
        c.end()


# --------------------------------------------------------------------------- B08
class B08_Greedy(Scene):
    def construct(self):
        c = Clock(self, "B08")
        tz = {g["T"]: g for g in EV["toward_zero"]}
        for T in (1.0, 0.5, 0.1):
            assert abs(softmax(Z, T)[0] - tz[T]["p_top"]) < 1e-5, f"B08 disagrees with evidence at T={T}"
        X0, X1, Y, Hh = -5.5, 5.5, 1.15, 0.9
        u = EV["runs20"]["u"][0]

        def st(T):
            return strip(list(softmax(Z, T)), X0, X1, Y, Hh, size=36, min_label_w=1.2)

        segs, labs = st(1.0)
        tread = tex(r"T = 1", 64).move_to(P(-4.2, 2.65))
        share = VGroup(label("mat", 40), num(f"{tz[1.0]['pct_top']:.1f}%", 44)).arrange(RIGHT, buff=0.3)
        share.move_to(P(3.6, 2.65))
        tk = mark(X0 + (X1 - X0) * u, Y + Hh / 2, 0.6, color=INK, sw=5)
        held = {"labs": labs}
        limit = tex(r"T \to 0^{+}:\quad p_i \to \begin{cases} 1 & \text{if } i = \arg\max_j z_j \\ "
                    r"0 & \text{otherwise} \end{cases}", 44).move_to(P(0, -0.85))
        greedy = label("greedy decoding: take the top token", 36).move_to(P(-2.6, -2.95))
        chip_x = [-5.5 + 0.4 * k for k in range(20)]
        chips_g = VGroup(*[Square(side_length=0.32, color=GHOST, stroke_width=3).move_to(P(x, -2.15))
                           for x in chip_x])                       # ghost: 20 run slots, filled later
        chips = VGroup(*[Square(side_length=0.32, stroke_color=INK, stroke_width=2, fill_color=INK,
                                fill_opacity=1).move_to(P(x, -2.15)) for x in chip_x])
        runs = label("20 runs: mat × 20", 34).move_to(P(4.3, -2.15))
        same = label("same answer (in principle)", 32, SOFT).move_to(P(3.75, -2.95))

        def to(T, txt, val, rt=0.8):
            s2, l2 = st(T)
            # labels fade (their count changes as segments shrink); segments morph
            c.play(Transform(segs, s2), FadeOut(held["labs"]), FadeIn(l2),
                   Transform(tread, tex(txt, 64).move_to(P(-4.2, 2.65))),
                   Transform(share[1], num(val, 44).move_to(V(share[1].get_center()).tolist())), rt=rt)
            held["labs"] = l2

        c.at(0.2)
        limit_g = RoundedRectangle(width=11.0, height=1.7, corner_radius=0.18, color=GHOST,
                                   stroke_width=3).move_to(P(0, -0.85))   # slot for the limit
        c.play(FadeIn(segs), FadeIn(labs), FadeIn(tread), FadeIn(share), Create(tk), FadeIn(limit_g),
               FadeIn(chips_g), rt=0.9)
        c.hold("At zero point five")
        to(0.5, r"T = 0.5", f"{tz[0.5]['pct_top']:.1f}%")
        c.hold("At zero point one")
        to(0.1, r"T = 0.1", f"{tz[0.1]['pct_top']:.2f}%")
        solid = Rectangle(width=X1 - X0, height=Hh, stroke_width=0, fill_color=INK,
                          fill_opacity=1).move_to(P((X0 + X1) / 2, Y))       # wide shapes stay INK (GATE T)
        mat_l = label("mat", 40).move_to(P((X0 + X1) / 2, Y - Hh / 2 - 0.3))
        gdot = Dot(P(V(share[0].get_left())[0] - 0.32, 2.65), radius=0.12, color=SPARK)   # the one accent
        every = left_at(label("every time", 40), V(share[0].get_right())[0] + 0.3, 2.65)
        c.go("no roll at all", FadeOut(tk), FadeOut(held["labs"]), FadeOut(segs), FadeIn(solid), FadeIn(mat_l),
             Transform(tread, tex(r"T \to 0", 64).move_to(P(-4.2, 2.65))),
             FadeOut(share[1]), FadeIn(every), FadeIn(gdot, scale=1.6), rt=0.8)
        c.go("greedy decoding", FadeIn(greedy, shift=UP * 0.15), rt=0.6)
        c.go("the formula itself", Write(limit), rt=1.0)
        c.go("Same prompt", LaggedStart(*[FadeIn(q) for q in chips], lag_ratio=0.05),
             FadeIn(runs, shift=UP * 0.15), rt=0.7)
        c.go("at least in principle", FadeIn(same, shift=UP * 0.15), rt=0.5)
        c.end()


# --------------------------------------------------------------------------- B09
class B09_WrongRanking(Scene):
    def construct(self):
        c = Clock(self, "B09")
        WR = EV["wrong_ranking"]
        wt, wz = WR["tokens"], WR["logits"]
        for T in ("0.2", "1.0", "2.0"):
            assert np.allclose([x / 100 for x in WR[T]["pct"]], softmax(wz, float(T)), atol=1e-3)
        assert WR["greedy_pick"] == wt[0]
        ys = [1.3, 0.25, -0.8, -1.85]
        X0, SC = -2.55, 4.3
        XN = -2.75                                                  # right edge of the city names

        prompt = left_at(label(f"{WR['prompt']} ___", 38), -5.9, 2.85)
        cap = left_at(label("hypothetical model · constructed logits", 32, SOFT), -5.9, 2.25)
        bdg = badges(4, -5.65, ys)
        nm = VGroup()
        for t, y in zip(wt, ys):
            if t == WR["correct"]:
                nm.add(right_at(VGroup(label(t, 36), tex(r"\checkmark", 40)).arrange(RIGHT, buff=0.15), XN, y))
            else:
                nm.add(right_at(label(t, 36), XN, y))

        def state(T):
            if T == "greedy":
                pp, pc = [1.0, 0.0, 0.0, 0.0], [100.0, 0.0, 0.0, 0.0]
            else:
                pc = WR[T]["pct"]
                pp = [x / 100 for x in pc]
            return bar_rows(pp, X0, ys, SC, h=0.55, pcts=pc)

        bars, vals = state("1.0")
        tread = tex(r"T = 1", 56).move_to(P(4.45, 1.8))
        wl = label("wrong", 40).move_to(P(4.45, 0.85))
        wv = num(pct(WR["1.0"]["pct_wrong_cities"]), 64).move_to(P(4.45, -0.15))
        wring = spot(wv, "left", pad=0.4, min_h=1.05)             # ghost outline + terracotta dot
        moral = label("spread changes; ranking never does", 38).move_to(P(0, -2.85))

        def to(T, txt, wrong, rt=0.8):
            b2, v2 = state(T)
            c.play(Transform(bars, b2), Transform(vals, v2), Transform(tread, tex(txt, 56).move_to(P(4.45, 1.8))),
                   Transform(wv, num(wrong, 64).move_to(P(4.45, -0.15))), rt=rt)

        c.at(0.2)
        c.play(FadeIn(prompt), rt=0.6)
        c.go("Suppose a model", FadeIn(cap), FadeIn(bdg), FadeIn(nm), FadeIn(bars), FadeIn(vals),
             FadeIn(tread), rt=0.9)
        c.go("wrong two times", FadeIn(wl), FadeIn(wv, scale=1.2), Create(wring), rt=0.6)
        c.hold("Turn it down")
        to("0.2", r"T = 0.2", pct(WR["0.2"]["pct_wrong_cities"]))
        c.hold("Greedy")
        to("greedy", r"T \to 0", "100%")
        c.hold("Turn it up")
        to("2.0", r"T = 2", pct(WR["2.0"]["pct_wrong_cities"]))
        c.go("Canberra actually slips", Indicate(vals[1], color=INK, scale_factor=1.4), rt=0.6)
        c.go("Melbourne and Perth", Indicate(vals[2], color=INK, scale_factor=1.4),
             Indicate(vals[3], color=INK, scale_factor=1.4), rt=0.7)
        frame = SurroundingRectangle(bdg, color=INK, buff=0.15, stroke_width=3)
        c.go("Temperature changes", FadeIn(moral, shift=UP * 0.15), Create(frame), rt=0.7)
        c.end()
