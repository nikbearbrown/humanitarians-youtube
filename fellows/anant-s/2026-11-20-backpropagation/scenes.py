"""Manim scenes for "Backpropagation, One Error at a Time" (claude-liam-backpropagation).

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/bp_demo.py).
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
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/claude-liam-backpropagation"))


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


def V(v):
    """Any point-like to a float vector (the GATE A geometry stub returns placeholders)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def box(part, pad=0.16, min_w=0.42, min_h=1.0, color=SPARK):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '-')."""
    w = max(float(getattr(part, "width", 0.5)) + pad, min_w)
    h = max(float(getattr(part, "height", 0.5)) + pad, min_h)
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color,
                            stroke_width=6).move_to(V(part.get_center()).tolist())


# ------------------------------------------------------------------ shared chain
NODE_X = [-5.4, -2.7, 0.0, 2.7, 5.4]
NODE_T = ["x", "z", "h", "y", "L"]
OPS = [r"\times\, w_1", r"\tanh", r"\times\, w_2", r"(y-t)^2"]
SLOPES = [r"x", r"1-h^2", r"w_2", r"2(y-t)"]   # local slope of each op wrt its input / weight


def chain(y0, r=0.42):
    """Five nodes and four labelled arrows. Returns (nodes, arrows, ops) as lists of VGroups."""
    nodes, arrows, ops = [], [], []
    for x, t in zip(NODE_X, NODE_T):
        c = Circle(radius=r, color=INK, stroke_width=4).move_to([x, y0, 0])
        nodes.append(VGroup(c, tex(t, 50).move_to([x, y0, 0])))
    for i, op in enumerate(OPS):
        a, b = NODE_X[i] + r + 0.08, NODE_X[i + 1] - r - 0.08
        arrows.append(Arrow([a, y0, 0], [b, y0, 0], buff=0, color=INK, stroke_width=4,
                            max_tip_length_to_length_ratio=0.12))
        ops.append(tex(op, 44).move_to([(a + b) / 2, y0 + 0.78, 0]))
    return nodes, arrows, ops


def mid(i):
    return (NODE_X[i] + NODE_X[i + 1]) / 2


# --------------------------------------------------------------------------- B02
class B02_Chain(Scene):
    def construct(self):
        c = Clock(self, "B02")
        nodes, arrows, ops = chain(0.55)
        title = label("the whole network: four small steps", 40, SOFT).move_to([0, 2.85, 0])
        tags = [tex(s, 44).move_to([mid(i), -1.0, 0]) for i, s in enumerate(SLOPES)]
        tag_head = label("local slope of each step", 34, SOFT).move_to([0, -2.0, 0])

        ghost = VGroup(*nodes, *arrows, *ops, *tags, tag_head).copy().set_color(GHOST)
        c.at(0.2)
        c.play(FadeIn(ghost), FadeIn(nodes[0]), FadeIn(title), rt=0.8)
        c.go("first weight", GrowArrow(arrows[0]), FadeIn(ops[0]), FadeIn(nodes[1]), rt=0.7)
        c.go("Squash", GrowArrow(arrows[1]), FadeIn(ops[1]), FadeIn(nodes[2]), rt=0.7)
        c.go("second weight", GrowArrow(arrows[2]), FadeIn(ops[2]), FadeIn(nodes[3]), rt=0.6)
        c.go("score it", GrowArrow(arrows[3]), FadeIn(ops[3]), FadeIn(nodes[4]), rt=0.7)
        c.go("local slope", *[FadeIn(t, shift=UP * 0.2) for t in tags], FadeIn(tag_head), rt=0.8)
        frame = RoundedRectangle(width=12.2, height=1.1, corner_radius=0.15, color=SPARK,
                                 stroke_width=6).move_to([0, -1.0, 0])
        c.go("Backpropagation", Create(frame), rt=0.8)
        c.end()


# --------------------------------------------------------------------------- B03
class B03_ChainRule(Scene):
    def construct(self):
        c = Clock(self, "B03")
        eq = MathTex(r"\frac{\partial L}{\partial w_1}", "=",
                     r"\frac{\partial L}{\partial y}", r"\cdot", r"\frac{\partial y}{\partial h}", r"\cdot",
                     r"\frac{\partial h}{\partial z}", r"\cdot", r"\frac{\partial z}{\partial w_1}",
                     color=INK, font_size=104).move_to(UP * 1.35)
        f1, f2, f3, f4 = (eq[i] for i in (2, 4, 6, 8))
        cap = label("multiply the local slopes along the path", 40, SOFT).move_to([0, 3.05, 0])

        def tag(part, mob, row):
            y = (-0.35, -1.25)[row]
            return mob.move_to([float(np.clip(V(part.get_center())[0], -4.8, 4.8)), y, 0])

        t1 = tag(f1, label("loss vs. output", 36), 0)
        t2 = tag(f2, tex(r"= w_2", 50), 1)
        t3 = tag(f3, tex(r"= 1-h^2", 50), 0)
        t4 = tag(f4, tex(r"= x", 50), 1)

        c.at(0.2)
        c.play(Write(eq), rt=1.4)
        c.go("multiply the local", FadeIn(cap, shift=DOWN * 0.2), rt=0.6)
        spot = box(f1)
        c.go("How the loss moves", Create(spot), FadeIn(t1, shift=UP * 0.2), rt=0.6)
        c.go("How the output", Transform(spot, box(f2)), FadeIn(t2, shift=UP * 0.2), rt=0.6)
        c.go("How tanh", Transform(spot, box(f3)), FadeIn(t3, shift=UP * 0.2), rt=0.6)
        c.go("just the input", Transform(spot, box(f4)), FadeIn(t4, shift=UP * 0.2), rt=0.6)
        allf = VGroup(f1, f2, f3, f4)
        brace = Brace(allf, DOWN, color=SPARK).move_to([V(allf.get_center())[0], -2.05, 0])
        prod = label("four factors, one product", 40).move_to([V(allf.get_center())[0], -2.75, 0])
        c.go("Four factors", FadeOut(spot), GrowFromCenter(brace), FadeIn(prod), rt=0.7)
        c.end()


# --------------------------------------------------------------------------- B04
class B04_Forward(Scene):
    def construct(self):
        c = Clock(self, "B04")
        su, fw = EV["setup"], EV["forward"]
        nodes, arrows, ops = chain(0.55)
        params = VGroup(tex(rf"x = {su['x']:g}", 46), tex(rf"t = {su['t']:g}", 46),
                        tex(rf"w_1 = {su['w1']:g}", 46), tex(rf"w_2 = {su['w2']:g}", 46)
                        ).arrange(RIGHT, buff=1.1).move_to([0, 2.85, 0])
        vals = {k: num(f"{fw[k]:g}", 38, INK).move_to([min(NODE_X[i], 5.2), -0.55, 0])
                for i, k in ((1, "z"), (2, "h"), (3, "y"), (4, "L"))}
        xval = num(f"{su['x']:g}", 38).move_to([NODE_X[0], -0.55, 0])
        fwd = VGroup(label("forward", 36, SOFT), Arrow(ORIGIN, RIGHT * 1.6, buff=0, color=SOFT, stroke_width=4)
                     ).arrange(RIGHT, buff=0.25).move_to([-3.6, -2.2, 0])
        back = VGroup(Arrow(RIGHT * 1.6, ORIGIN, buff=0, color=SOFT, stroke_width=4), label("backward next", 36, SOFT)
                      ).arrange(RIGHT, buff=0.25).move_to([3.3, -2.2, 0])

        c.at(0.2)
        c.play(*[FadeIn(n) for n in nodes], *[GrowArrow(a) for a in arrows], *[FadeIn(o) for o in ops],
               FadeIn(params), rt=0.9)
        c.go("target", FadeIn(xval), FadeIn(fwd), rt=0.5)
        c.go("z is", FadeIn(vals["z"], shift=UP * 0.2), rt=0.5)
        c.go("Tanh gives", FadeIn(vals["h"], shift=UP * 0.2), rt=0.5)
        c.go("the output is", FadeIn(vals["y"], shift=UP * 0.2), rt=0.5)
        c.go("the loss is", FadeIn(vals["L"], shift=UP * 0.2), rt=0.5)
        c.play(Create(box(vals["L"], min_h=0.75)), rt=0.4)
        c.go("run it backward", FadeIn(back, shift=LEFT * 0.2), rt=0.5)
        c.end()


# --------------------------------------------------------------------------- B05
class B05_Backward(Scene):
    def construct(self):
        c = Clock(self, "B05")
        fw, g, st = EV["forward"], EV["backward"], EV["step"]
        nodes, arrows, ops = chain(1.35)
        fvals = [num(f"{v:g}", 32, SOFT).move_to([NODE_X[i], 0.5, 0])
                 for i, v in enumerate([EV["setup"]["x"], fw["z"], fw["h"], fw["y"], fw["L"]])]
        ga = [tex(s, 38).move_to([NODE_X[i], -0.95, 0]) for i, s in (
            (3, rf"\tfrac{{\partial L}}{{\partial y}}={g['dL_dy']:g}"),
            (2, rf"\tfrac{{\partial L}}{{\partial h}}={g['dL_dh']:g}"),
            (1, rf"\tfrac{{\partial L}}{{\partial z}}={g['dL_dz']:g}"))]
        back = [Arrow([NODE_X[i + 1] - 0.3, -0.25, 0], [NODE_X[i] + 0.3, -0.25, 0], buff=0, color=INK,
                      stroke_width=6, max_tip_length_to_length_ratio=0.12).move_to([mid(i), -0.25, 0])
                for i in (3, 2, 1, 0)]
        gw1 = tex(rf"\tfrac{{\partial L}}{{\partial w_1}}={g['dL_dw1']:g}", 44).move_to([-3.9, -1.9, 0])
        gw2 = tex(rf"\tfrac{{\partial L}}{{\partial w_2}}={g['dL_dw2']:g}", 44).move_to([2.6, -1.9, 0])
        step0 = VGroup(label("one step, η = 0.1:  loss", 38), num(f"{st['L_before']:g}", 40)
                       ).arrange(RIGHT, buff=0.3).move_to([0, -2.85, 0])
        step1 = VGroup(label("one step, η = 0.1:  loss", 38), num(f"{st['L_before']:g}", 40),
                       label("→", 40), num(f"{st['L_after']:g}", 40)).arrange(RIGHT, buff=0.3).move_to([0, -2.85, 0])

        c.at(0.2)
        c.play(*[FadeIn(n) for n in nodes], *[GrowArrow(a) for a in arrows], *[FadeIn(o) for o in ops],
               *[FadeIn(v) for v in fvals], rt=1.0)
        c.go("loss moves", GrowArrow(back[0]), FadeIn(ga[0], shift=UP * 0.2), rt=0.6)
        c.go("Times the second", GrowArrow(back[1]), FadeIn(ga[1], shift=UP * 0.2), rt=0.6)
        c.go("Times the tanh", GrowArrow(back[2]), FadeIn(ga[2], shift=UP * 0.2), rt=0.6)
        c.go("first weight's", GrowArrow(back[3]), FadeIn(gw1, shift=UP * 0.2), rt=0.6)
        c.play(Create(box(gw1, min_h=0.8)), rt=0.4)
        c.go("The second weight's", FadeIn(gw2, shift=UP * 0.2), rt=0.5)
        c.go("One step", FadeIn(step0, shift=UP * 0.2), rt=0.5)
        c.go("falls from", ReplacementTransform(step0, step1), rt=0.7)
        c.end()


# --------------------------------------------------------------------------- B06
class B06_Check(Scene):
    def construct(self):
        c = Clock(self, "B06")
        fd, cost = EV["fd_check"]["w1"], EV["cost"]
        head = label("the first weight's slope, two ways", 40, SOFT).move_to([0, 3.0, 0])
        lh = label("backprop", 40).move_to([-3.3, 2.1, 0])
        rh = tex(r"\frac{L(w_1+\varepsilon)-L(w_1-\varepsilon)}{2\varepsilon}", 46).move_to([3.3, 2.0, 0])
        eps = tex(r"\varepsilon = 0.00001", 38, SOFT).move_to([3.3, 0.95, 0])
        lv = num(f"{fd['backprop']:.8f}", 60).move_to([-3.3, 0.15, 0])
        rv = num(f"{fd['finite_diff']:.8f}", 60).move_to([3.3, 0.15, 0])
        diff = VGroup(label("difference", 36, SOFT), tex(r"%s\times10^{%d}" % (f"{fd['abs_diff']:.1e}".split("e")[0], int(f"{fd['abs_diff']:.1e}".split("e")[1])), 44)
                      ).arrange(RIGHT, buff=0.3).move_to([0, -0.85, 0])
        bar_l = label("nudging", 36).move_to([-5.0, -1.85, 0])
        bar = Rectangle(width=8.6, height=0.42, color=INK, fill_color=INK, fill_opacity=1, stroke_width=0)
        bar.move_to([0.75, -1.85, 0])
        bar_n = num(f"{cost['weights_1e6_forward_passes_fd']:,} passes", 32, PAGE).move_to([0.75, -1.85, 0])
        bp_l = label("backprop", 36).move_to([-5.0, -2.75, 0])
        bp = Rectangle(width=0.12, height=0.42, color=SPARK, fill_color=SPARK, fill_opacity=1,
                       stroke_width=0).move_to([-3.49, -2.75, 0])
        bp_n = label("one backward pass", 34).move_to([-1.6, -2.75, 0])
        scale = label("for a million weights", 30, SOFT).move_to([4.2, -2.75, 0])

        rows0 = VGroup(bar_l.copy(), bp_l.copy(), scale.copy()).set_color(GHOST)
        c.at(0.2)
        c.play(FadeIn(head), FadeIn(lh), FadeIn(rows0), rt=0.8)
        c.go("the slow way", Write(rh), rt=1.0)
        c.go("hundred-thousandth", FadeIn(eps), rt=0.5)
        c.go("Backprop says", FadeIn(lv, shift=UP * 0.2), rt=0.6)
        c.go("The nudge says", FadeIn(rv, shift=UP * 0.2), rt=0.6)
        c.go("eight decimal", FadeIn(diff, shift=UP * 0.2), rt=0.6)
        c.go("two passes", FadeOut(rows0), FadeIn(bar_l), FadeIn(scale), GrowFromEdge(bar, LEFT), rt=1.0)
        c.go("two million", FadeIn(bar_n), rt=0.5)
        c.go("Backprop needs", FadeIn(bp_l), GrowFromEdge(bp, LEFT), FadeIn(bp_n), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B07
class B07_Vanishing(Scene):
    def construct(self):
        c = Clock(self, "B07")
        va = EV["vanishing"]
        loc = va["local_slopes"]
        n = len(loc)
        # gradient arriving at layer i's input = product of local slopes of layers i..n
        g_in = [float(np.prod(loc[i:])) for i in range(n)]
        assert abs(g_in[0] - va["grad_at_input"]) / va["grad_at_input"] < 0.01, "B07 disagrees with evidence"
        xs = [-5.4 + i * 1.2 for i in range(n)]
        layers = VGroup(*[VGroup(RoundedRectangle(width=0.85, height=0.85, corner_radius=0.1, color=INK,
                                                  stroke_width=4).move_to([x, 1.75, 0]),
                                 tex(r"\sigma", 40).move_to([x, 1.75, 0])) for x in xs])
        base_y, top_h = -2.45, 3.1
        heights = [max(0.06, (np.log10(v) + 7.0) / 7.0 * top_h) for v in g_in]
        bars = [Rectangle(width=0.62, height=h, color=INK, fill_color=INK, fill_opacity=1,
                          stroke_width=0).move_to([x, base_y + h / 2, 0]) for x, h in zip(xs, heights)]
        axis = Line([-6.0, base_y, 0], [6.0, base_y, 0], color=GHOST, stroke_width=3)
        cap = label("gradient reaching each layer (log scale)", 32, SOFT).move_to([0, -2.95, 0])
        chip = VGroup(label("sigmoid slope", 36), tex(r"\le 0.25", 46)).arrange(RIGHT, buff=0.25).move_to([-3.6, 2.95, 0])
        per = VGroup(tex(r"\times\,0.22", 46), label("per layer", 36)).arrange(RIGHT, buff=0.25).move_to([3.4, 2.95, 0])
        first = tex(r"3.5\times10^{-7}", 46).next_to(V(bars[0].get_top()), UP, buff=0.25)
        first.move_to([-4.75, -1.15, 0])
        name = label("the vanishing gradient", 40).move_to([-2.4, 0.15, 0])

        c.at(0.2)
        c.play(Create(axis), FadeIn(cap), rt=0.6)
        c.go("Stack ten", LaggedStart(*[FadeIn(l, shift=DOWN * 0.15) for l in layers], lag_ratio=0.12), rt=1.2)
        c.go("never more", FadeIn(chip, shift=DOWN * 0.2), rt=0.6)
        c.go("multiplies the gradient", FadeIn(per, shift=DOWN * 0.2), rt=0.5)
        for b in reversed(bars):                       # error arrives from the right
            c.play(GrowFromEdge(b, DOWN), rt=0.2)
        c.go("first layer", bars[0].animate.set_color(SPARK), FadeIn(first, shift=UP * 0.2), rt=0.6)
        c.go("vanishing gradient", FadeIn(name, shift=UP * 0.2), rt=0.6)
        c.end()
