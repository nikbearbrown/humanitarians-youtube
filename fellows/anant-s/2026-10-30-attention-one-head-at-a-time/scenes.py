"""Manim scenes for "Attention, One Head at a Time" (tldr-attention), LEARN section 1.

Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/attention_demo.py).
Each scene ends exactly at its beat's measured audio duration.
Each scene class subclasses Scene directly, one per beat, named by its positional beat id.

Transform, don't cut: the section shares one layout and one state factory. Each scene
starts on the previous beat's end state (added at t=0), so the last frame of one beat
is the first frame of the next.
"""
from manim import *
import json
import os
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# GATE A pre-flights an isolated copy of this file; fall back to the reel folder.
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/tldr-attention"))


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

# Claude stage — one terracotta moment per beat.
PAGE, INK, SOFT, GHOST, SPARK = "#FAF9F5", "#3D3929", "#73705F", "#D9D4C7", "#D97757"
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


def num(s, size=32, color=INK):
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


def W(m, default=1.0):
    """Width of a mobject as a float (stub-safe)."""
    try:
        return float(m.width)
    except (TypeError, ValueError, AttributeError):
        return default


def box(part, pad=0.18, min_w=0.42, min_h=0.62, color=SPARK, sw=6):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '-')."""
    try:
        w, h = float(part.width), float(part.height)
    except (TypeError, ValueError, AttributeError):
        w, h = 0.5, 0.5
    bw = max(w + pad, min_w)
    # GATE T §8.6b: a ring wider than 1.5x its height reads as a text run enclosing the glyph
    # (100% bbox overlap). Keep spotlights at most 1.4x as wide as tall.
    base_h = max(h + pad, min_h)
    bh = max(base_h, bw / 1.4)
    # extra height (from the width rule) grows downward, so the top edge stays clear of
    # fraction bars and lines above the spotlit glyph
    c = V(part.get_center()) + DOWN * min((bh - base_h) / 2, 0.6)   # capped: GATE A's stub reports placeholder sizes
    return spot_ring(RoundedRectangle(width=bw, height=bh, corner_radius=0.12,
                                      color=color, stroke_width=sw).move_to(c.tolist()))


def Spot(**kw):
    return spot_ring(RoundedRectangle(**kw))


def spot_ring(m):
    """Mark a spotlight box as an intentional editor's annotation (Gate B TEXT/CURVE exempt)."""
    m._qc_intentional = True
    return m


def g(x, nd=2):
    """Display number: up to nd decimals, true minus sign."""
    if isinstance(x, int) or float(x).is_integer():
        s = str(int(x))
    else:
        s = f"{float(x):.{nd}f}".rstrip("0").rstrip(".")
    return s.replace("-", "−")


def pair(v):
    return ("(" + ", ".join(f"{float(x):.2f}" for x in v) + ")").replace("-", "−")


def w2(x):
    """Attention weight, always two decimals."""
    return f"{float(x):.2f}"


# ------------------------------------------------------------------ evidence
WORD = list(EV["words"])                  # cats chase small dogs
X, K, Vv = EV["X"], EV["K"], EV["V"]
A2, O2 = EV["weights2"], EV["outputs2"]
WK = EV["worked"]
SWP = EV["swap"]
SHF = EV["shuffle"]
WPOS = EV["with_position"]
CENT = EV["naive_equal"]["outputs"][0]
HOOK_OUT, KIDS_OUT = O2[1], SWP["chase_output2"]
KIDS_V = SWP["kids_value"]
assert WK["weights"][0] > 0.5 and abs(sum(EV["weights"][1]) - 1) < 1e-3, "evidence changed"

# ------------------------------------------------------------------ layout
CW, CH = 1.15, 0.85
COLS = [-4.2 + CW * j for j in range(4)]       # grid cell centres (x)
ROWS = [1.2 - CH * i for i in range(4)]          # grid cell centres (y)
LBL_R = -5.04                                    # row labels right-aligned here
OX, OY = 2.4, -0.55                              # value-plane origin on screen (1 unit = 1)
SENT_Y = 2.95


def PX(x, y):
    return [OX + float(x), OY + float(y), 0]


# label side for each value point (clear of edges and of each other)
SIDE = {"cats": "U", "chase": "U", "small": "L", "dogs": "L", "kids": "L"}


def point_label(word, xy, color=INK):
    t = label(word, 32, color)
    x, y, _ = PX(*xy)
    if SIDE[word] == "U":
        return t.move_to([x, y + 0.5, 0])
    return t.move_to([x - 0.24 - W(t, 0.8) / 2, y, 0])


def value_points(words=None, vals=None, color=INK):
    words = words or WORD
    vals = vals or Vv
    dots = [Dot(PX(*v), radius=0.11, color=color) for v in vals]
    labs = [point_label(w, v, color) for w, v in zip(words, vals)]
    return dots, labs


def plane_frame():
    return RoundedRectangle(width=5.6, height=5.3, corner_radius=0.2, color=SOFT,
                            stroke_width=2).move_to([2.95, -0.4, 0])


def row_label(word, i, color=INK):
    t = label(word, 32, color)
    return t.move_to([LBL_R - W(t, 0.9) / 2, ROWS[i], 0])


def grid_nums(M, size=32, color=INK, rows=range(4), fmt=g):
    return [[num(fmt(M[i][j]), size, color).move_to([COLS[j], ROWS[i], 0]) for j in range(len(M[i]))]
            for i in rows]


def cell_rects(shade=None):
    """4x4 cell outlines; optional shading by weight (ink tint, never a rainbow)."""
    out = []
    for i in range(4):
        row = []
        for j in range(4):
            op = 0.0 if shade is None else 0.45 * float(shade[i][j])
            row.append(Rectangle(width=CW - 0.06, height=CH - 0.06, color=SOFT, stroke_width=1.5,
                                 fill_color=INK, fill_opacity=op).move_to([COLS[j], ROWS[i], 0]))
        out.append(row)
    return out


def col_heads(words=None):
    words = words or WORD
    return [label(w, 32, SOFT).move_to([COLS[j], ROWS[0] + 0.72, 0]) for j, w in enumerate(words)]


def sentence(words=None, y=SENT_Y):
    words = words or WORD
    xs = [-3.9, -1.3, 1.3, 3.9]
    return [label(w, 44).move_to([x, y, 0]) for w, x in zip(words, xs)]


def flat(rows):
    return [m for r in rows for m in r]


def caption(s, x=-3.1, y=-2.95, size=32):
    return label(s, size, SOFT).move_to([x, y, 0])


def caption2(a, b, x=-3.1, y=-2.55):
    """Two-line dim caption in the left panel (clear of the value-plane frame)."""
    return VGroup(label(a, 32, SOFT).move_to([x, y, 0]), label(b, 32, SOFT).move_to([x, y - 0.45, 0]))


# --------------------------------------------------------------- state factory
def state_after_B10():
    """End of the HOOK: kids sentence, X rows (kids row swapped in), plane, ghost + dot."""
    words = ["kids"] + WORD[1:]
    rows = [SWP["kids_embedding"]] + X[1:]
    s = {
        "sent": sentence(words),
        "labs": [row_label(w, i) for i, w in enumerate(words)],
        "nums": grid_nums(rows),
        "frame": plane_frame(),
        "ghost": Circle(radius=0.17, color=SOFT, stroke_width=3).move_to(PX(*HOOK_OUT)),
        "dot": Dot(PX(*KIDS_OUT), radius=0.13, color=SPARK),
        "readout": num("chase out: " + pair(KIDS_OUT), 32).move_to([-3.0, -2.3, 0]),
        "cap": caption("toy numbers, not a trained model"),
    }
    return s


def value_plane_state():
    dots, labs = value_points()
    return {"frame": plane_frame(), "vdots": dots, "vlabs": labs}


def heat_state(words=None, A=None, box_row=1, box_color=SPARK):
    words = words or WORD
    A = A or A2
    rects = cell_rects(A)
    nums = grid_nums(A, fmt=w2)
    s = {"labs": [row_label(w, i) for i, w in enumerate(words)], "heads": col_heads(words),
         "rects": rects, "nums": nums}
    if box_row is not None:
        s["rowbox"] = Spot(width=4 * CW + 0.25, height=CH + 0.08, corner_radius=0.1,
                                       color=box_color, stroke_width=6).move_to([np.mean(COLS), ROWS[box_row], 0])
    return s


def mobs(state):
    out = []
    for v in state.values():
        if isinstance(v, list):
            out += flat(v) if v and isinstance(v[0], list) else v
        else:
            out.append(v)
    return out


# --------------------------------------------------------------------------- B10
class B10_ChaseMoves(Scene):
    def construct(self):
        c = Clock(self, "B10")
        sent = sentence()
        labs = [row_label(w, i) for i, w in enumerate(WORD)]
        nums = grid_nums(X)
        frame = plane_frame()
        head_arrow = Arrow([-0.15, 2.12, 0], [1.0, 2.12, 0], buff=0, color=INK, stroke_width=4,
                           max_tip_length_to_length_ratio=0.2)
        head_lab = label("one attention head", 32).move_to([-1.75, 2.12, 0])
        chase_box = Spot(width=4 * CW + 1.55, height=CH, corner_radius=0.1, color=INK,
                         stroke_width=6).move_to([float(np.mean(COLS)) - 0.62, ROWS[1], 0])
        dot = Dot(PX(*HOOK_OUT), radius=0.13, color=SPARK)
        read1 = num("chase out: " + pair(HOOK_OUT), 32).move_to([-3.0, -2.3, 0])
        read2 = num("chase out: " + pair(KIDS_OUT), 32).move_to([-3.0, -2.3, 0])
        ghost = Circle(radius=0.17, color=SOFT, stroke_width=3).move_to(PX(*HOOK_OUT))
        kids_lab = row_label("kids", 0)
        kids_sent = label("kids", 44).move_to(V(sent[0].get_center()).tolist())
        kids_nums = [num(g(SWP["kids_embedding"][j])).move_to([COLS[j], ROWS[0], 0]) for j in range(4)]
        cap = caption("toy numbers, not a trained model")

        c.at(0.2)
        c.play(LaggedStart(*[Write(w) for w in sent], lag_ratio=0.25), rt=1.4)
        c.go("attention head", Create(frame), GrowArrow(head_arrow), FadeIn(head_lab), rt=0.6)
        c.go("list of four numbers", LaggedStart(*[FadeIn(VGroup(l, *r), shift=RIGHT * 0.2)
                                                  for l, r in zip(labs, nums)], lag_ratio=0.2), rt=0.95)
        c.go("Follow chase", Create(chase_box), rt=0.6)
        start = Dot(V(nums[1][3].get_center()) + RIGHT * 0.6, radius=0.13, color=SPARK)
        c.go("comes out", FadeIn(start), rt=0.2)
        c.play(ReplacementTransform(start, dot, path_arc=-0.6), rt=0.55)
        c.go("right here", FadeIn(read1, shift=UP * 0.15), rt=0.5)
        c.go("swap cats for kids", Transform(sent[0], kids_sent), Transform(labs[0], kids_lab),
             *[Transform(a, b) for a, b in zip(nums[0], kids_nums)], rt=1.0)
        self.add(ghost)
        c.go("somewhere else", dot.animate.move_to(PX(*KIDS_OUT)), Transform(read1, read2), rt=1.2)
        c.go("only sees", FadeIn(cap), rt=0.6)
        c.go("neighbours", Indicate(dot, color=SPARK, scale_factor=1.3), rt=0.5)
        c.end()


# --------------------------------------------------------------------------- B11
class B11_MixingPoints(Scene):
    def construct(self):
        c = Clock(self, "B11")
        s = state_after_B10()
        self.add(*mobs(s))
        # restore the original sentence; the HOOK's marks leave for now (they return in B15/B18)
        labs = [row_label(w, i) for i, w in enumerate(WORD)]
        nums = grid_nums(X)
        dots, vlabs = value_points()
        fixed = label("fixed weights", 32, SOFT).move_to([-2.6, -2.3, 0])
        cap = caption2("values drawn with 2 numbers", "(real heads use 64)")

        c.at(0.2)
        c.play(*[FadeOut(m) for m in s["sent"]], Transform(s["labs"][0], labs[0]),
               *[Transform(a, b) for a, b in zip(s["nums"][0], nums[0])],
               FadeOut(s["ghost"]), FadeOut(s["dot"]), FadeOut(s["readout"]), FadeOut(s["cap"]), rt=0.6)
        c.go("fixed grid", FadeIn(fixed), rt=0.5)
        c.go("giving each word", *[ReplacementTransform(VGroup(*s["nums"][i]).copy(), dots[i]) for i in range(4)],
             *[FadeIn(l) for l in vlabs], rt=0.9)
        c.play(*[FadeOut(m) for m in flat(s["nums"]) + s["labs"]], FadeOut(fixed), FadeIn(cap), rt=0.4)

        # two-point blend on the cats–small segment, driven by one tracker
        w = ValueTracker(0.5)
        a, b = np.array(PX(*Vv[0])), np.array(PX(*Vv[2]))
        seg = DashedLine(a, b, color=SOFT, stroke_width=2)
        blend = Dot(radius=0.13, color=SPARK).add_updater(
            lambda m: m.move_to(w.get_value() * a + (1 - w.get_value()) * b))
        blend.move_to((a + b) / 2)
        f05 = tex(r"0.5\,\text{cats} + 0.5\,\text{small}", 44).move_to([-3.0, 0.3, 0])
        f08 = tex(r"0.8\,\text{cats} + 0.2\,\text{small}", 44).move_to([-3.0, 0.3, 0])
        c.go("Mix two points", Create(seg), rt=0.6)
        c.go("Half and half", FadeIn(blend), Write(f05), rt=0.8)
        c.go("zero point eight", w.animate.set_value(0.8), TransformMatchingTex(f05, f08), rt=1.2)

        # four points: weights from the evidence sequence, bars on the left
        hull = Polygon(*[PX(*Vv[i]) for i in (1, 0, 3, 2)], color=SOFT, stroke_width=2)
        ts = [ValueTracker(x) for x in (0.8, 0.0, 0.2, 0.0)]
        P = [np.array(PX(*v)) for v in Vv]

        def mix():
            ws = np.array([t.get_value() for t in ts])
            return (ws[:, None] * np.array(P)).sum(0) / max(ws.sum(), 1e-6)

        base = -1.7

        def bar(j):
            return always_redraw(lambda j=j: Rectangle(
                width=0.7, height=max(0.04, 2.4 * ts[j].get_value()), color=INK, fill_color=INK,
                fill_opacity=0.85, stroke_width=0).move_to([COLS[j], base + max(0.04, 2.4 * ts[j].get_value()) / 2, 0]))

        bars = [bar(j) for j in range(4)]
        bar_l = [label(wd, 32).move_to([COLS[j], base - 0.32, 0]) for j, wd in enumerate(WORD)]
        c.go("With all four", Create(hull), FadeOut(seg), FadeOut(f08), *[FadeIn(l) for l in bar_l], rt=0.8)
        blend.clear_updaters()
        blend.add_updater(lambda m: m.move_to(mix()))
        self.add(*bars)
        for wts in EV["blend_four"]:
            c.play(*[t.animate.set_value(x) for t, x in zip(ts, wts["w"])], rt=1.1)
        c.end()


# --------------------------------------------------------------------------- B12
class B12_RequestMeetsOffer(Scene):
    def construct(self):
        c = Clock(self, "B12")
        # B11 end state: plane, points, hull, blend dot at the last mix, bars, caption
        ps = value_plane_state()
        last = EV["blend_four"][-1]["point"]
        hull = Polygon(*[PX(*Vv[i]) for i in (1, 0, 3, 2)], color=SOFT, stroke_width=2)
        blend = Dot(PX(*last), radius=0.13, color=SPARK)
        base = -1.7
        bars = [Rectangle(width=0.7, height=max(0.04, 2.4 * x), color=INK, fill_color=INK, fill_opacity=0.85,
                          stroke_width=0).move_to([COLS[j], base + max(0.04, 2.4 * x) / 2, 0])
                for j, x in enumerate(EV["blend_four"][-1]["w"])]
        bar_l = [label(wd, 32).move_to([COLS[j], base - 0.32, 0]) for j, wd in enumerate(WORD)]
        cap = caption2("values drawn with 2 numbers", "(real heads use 64)")
        self.add(*mobs(ps), hull, blend, *bars, *bar_l, cap)

        labs = [row_label(w, i) for i, w in enumerate(WORD)]
        offers = grid_nums(K)
        heads = [label(s, 32, SOFT).move_to([x, ROWS[0] + 0.72, 0]) for s, x in
                 (("offers", float(np.mean(COLS))), ("products", 1.8), ("score", 4.4))]
        req_y = ROWS[0] + 1.25
        q = WK["query"]
        req = [num(g(q[j]), 32).move_to([COLS[j], req_y, 0]) for j in range(4)]
        req_lab = label("chase asks", 32).move_to([float(np.mean(COLS)), req_y + 0.5, 0])
        PXS = [0.75, 1.45, 2.15, 2.85]

        def products(i, query):
            return [num(g(query[j] * K[i][j]), 32).move_to([PXS[j], ROWS[i], 0]) for j in range(4)]

        def score(i, val, color=INK):
            return num(g(val), 36, color).move_to([4.4, ROWS[i], 0])

        prods = [products(i, q) for i in range(4)]
        scores = [score(i, d["score"]) for i, d in enumerate(WK["dots"])]
        rowbox = Spot(width=4 * CW + 0.2, height=CH - 0.02, corner_radius=0.1, color=INK,
                                  stroke_width=3).move_to([float(np.mean(COLS)), ROWS[0], 0])

        c.at(0.2)
        c.play(*[FadeOut(m) for m in mobs(ps) + [hull, blend, cap] + bars + bar_l], rt=0.5)
        c.go("Two more grids", LaggedStart(*[FadeIn(VGroup(l, *r), shift=RIGHT * 0.2)
                                            for l, r in zip(labs, offers)], lag_ratio=0.15),
             FadeIn(heads[0]), rt=1.2)
        req_box = Spot(width=4 * CW + 0.2, height=0.5, corner_radius=0.1, color=INK,
                       stroke_width=6).move_to([float(np.mean(COLS)), req_y, 0])
        rule = tex(r"\text{request}\cdot\text{offer} = \text{sum of the products}", 44).move_to([-0.6, -2.45, 0])
        c.go("Chase requests", FadeIn(req_lab), LaggedStart(*[FadeIn(m, shift=DOWN * 0.15) for m in req],
                                                             lag_ratio=0.15), Create(req_box), rt=0.9)
        c.go("Against cats", Create(rowbox), FadeIn(heads[1]), FadeIn(heads[2]), FadeIn(rule, shift=UP * 0.15),
             *[TransformFromCopy(req[j], prods[0][j]) for j in range(4)], rt=1.0)
        score_ring = spot_ring(Circle(radius=0.36, color=SPARK, stroke_width=6).move_to([4.4, ROWS[0], 0]))
        c.go("add", FadeIn(scores[0], shift=LEFT * 0.2), Create(score_ring), rt=0.5)
        c.go("Against its own", rowbox.animate.move_to([float(np.mean(COLS)), ROWS[1], 0]),
             *[TransformFromCopy(req[j], prods[1][j]) for j in range(4)], FadeIn(scores[1]), rt=0.8)
        c.go("Small and dogs", rowbox.animate.stretch_to_fit_height(2 * CH).move_to(
            [float(np.mean(COLS)), (ROWS[2] + ROWS[3]) / 2, 0]),
             *[TransformFromCopy(req[j], prods[i][j]) for i in (2, 3) for j in range(4)],
             FadeIn(scores[2]), FadeIn(scores[3]), rt=0.9)
        q2 = EV["match_small"]["query"]
        req2 = [num(g(q2[j]), 32).move_to([COLS[j], req_y, 0]) for j in range(4)]
        req_lab2 = label("small asks", 32).move_to([float(np.mean(COLS)), req_y + 0.5, 0])
        prods2 = [products(i, q2) for i in range(4)]
        scores2 = [score(i, v) for i, v in enumerate(EV["match_small"]["scores"])]
        c.go("Ask from small", FadeOut(rowbox), FadeOut(score_ring), Transform(req_lab, req_lab2),
             *[Transform(a, b) for a, b in zip(req, req2)], rt=0.8)
        c.go("reshuffle", *[Transform(a, b) for a, b in zip(flat(prods), flat(prods2))],
             *[Transform(a, b) for a, b in zip(scores, scores2)], rt=1.0)
        c.end()


# --------------------------------------------------------------------------- B13
class B13_EqualWeights(Scene):
    def construct(self):
        c = Clock(self, "B13")
        # B12 end state (small's request, its products and scores)
        labs = [row_label(w, i) for i, w in enumerate(WORD)]
        offers = grid_nums(K)
        q2 = EV["match_small"]["query"]
        req_y = ROWS[0] + 1.25
        req = [num(g(q2[j]), 32).move_to([COLS[j], req_y, 0]) for j in range(4)]
        req_lab = label("small asks", 32).move_to([float(np.mean(COLS)), req_y + 0.5, 0])
        PXS = [0.75, 1.45, 2.15, 2.85]
        prods = [num(g(q2[j] * K[i][j]), 32).move_to([PXS[j], ROWS[i], 0]) for i in range(4) for j in range(4)]
        scores = [num(g(v), 36).move_to([4.4, ROWS[i], 0]) for i, v in enumerate(EV["match_small"]["scores"])]
        heads = [label(s, 32, SOFT).move_to([x, ROWS[0] + 0.72, 0]) for s, x in
                 (("offers", float(np.mean(COLS))), ("products", 1.8), ("score", 4.4))]
        req_box = Spot(width=4 * CW + 0.2, height=0.5, corner_radius=0.1, color=INK,
                       stroke_width=6).move_to([float(np.mean(COLS)), req_y, 0])
        rule = tex(r"\text{request}\cdot\text{offer} = \text{sum of the products}", 44).move_to([-0.6, -2.45, 0])
        old = flat(offers) + req + [req_lab, req_box, rule] + prods + scores + heads
        self.add(*labs, *old)

        ps = value_plane_state()
        quarter = [[0.25] * 4 for _ in range(4)]
        rects = flat(cell_rects())
        qnums = flat(grid_nums(quarter))
        heads2 = col_heads()
        movers = [Dot(PX(*v), radius=0.12, color=INK) for v in Vv]
        cent = PX(*CENT)
        cap = caption("equal weights: every word identical", x=-3.1, y=-2.45)

        c.at(0.2)
        c.play(*[FadeOut(m) for m in old], FadeIn(VGroup(*mobs(ps))), rt=0.8)
        c.go("a quarter each", *[FadeIn(r) for r in rects], *[FadeIn(n) for n in qnums],
             *[FadeIn(h) for h in heads2], rt=0.9)
        c.go("Watch all four", *[GrowFromCenter(m) for m in movers], rt=0.6)
        c.go("Cats chase small", LaggedStart(*[m.animate.move_to(cent) for m in movers], lag_ratio=0.3),
             rt=1.4, lead=0.05)
        spot = Spot(width=0.62, height=0.62, corner_radius=0.12, color=SPARK,
                                stroke_width=6).move_to(cent)
        c.go("one meaning", Create(spot), rt=0.6)
        c.go("Equal weights erase", FadeIn(cap), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B14
class B14_HeatMap(Scene):
    def construct(self):
        c = Clock(self, "B14")
        ps = value_plane_state()
        labs = [row_label(w, i) for i, w in enumerate(WORD)]
        heads = col_heads()
        quarter = [[0.25] * 4 for _ in range(4)]
        rects0 = flat(cell_rects())
        qnums = flat(grid_nums(quarter))
        cent = PX(*CENT)
        stack = Dot(cent, radius=0.12, color=INK)
        spot = Spot(width=0.62, height=0.62, corner_radius=0.12, color=SPARK,
                                stroke_width=6).move_to(cent)
        cap0 = caption("equal weights: every word identical", x=-3.1, y=-2.45)
        self.add(*mobs(ps), *labs, *heads, *rects0, *qnums, stack, spot, cap0)

        S = EV["scores"]
        raw = grid_nums(S)
        half = grid_nums(EV["scaled"])
        wts = grid_nums(A2, fmt=w2)
        rects = cell_rects(A2)
        plain = flat(cell_rects())
        div = tex(r"\div\,2", 48).move_to([-2.6, -2.35, 0])
        sm = label("softmax, row by row", 32, SOFT).move_to([-2.6, -2.35, 0])
        cap = caption("rounded; every row sums to 1", x=-3.1, y=-2.95)
        rowbox = Spot(width=4 * CW + 0.25, height=CH + 0.08, corner_radius=0.1, color=SPARK,
                                  stroke_width=6).move_to([float(np.mean(COLS)), ROWS[1], 0])

        c.at(0.2)
        c.play(FadeOut(stack), FadeOut(spot), FadeOut(cap0), *[FadeOut(n) for n in qnums],
               *[ReplacementTransform(a, b) for a, b in zip(rects0, plain)], rt=0.7)
        c.go("every request", LaggedStart(*[FadeIn(VGroup(*r)) for r in raw], lag_ratio=0.25), rt=1.4)
        c.go("Divide each score", FadeIn(div), *[Transform(a, b) for a, b in zip(flat(raw), flat(half))], rt=1.0)
        c.go("softmax each row", FadeOut(div), FadeIn(sm), rt=0.4)
        for i in range(4):
            c.play(*[Transform(raw[i][j], wts[i][j]) for j in range(4)],
                   *[Transform(plain[4 * i + j], rects[i][j]) for j in range(4)], rt=0.45)
        c.go("heat map", FadeIn(cap), rt=0.5)
        c.go("Chase's row", Create(rowbox), rt=0.6)
        c.end()


# --------------------------------------------------------------------------- B15
class B15_LetTheMatchMix(Scene):
    def construct(self):
        c = Clock(self, "B15")
        ps = value_plane_state()
        hs = heat_state()
        sm = label("softmax, row by row", 32, SOFT).move_to([-2.6, -2.35, 0])
        cap = caption("rounded; every row sums to 1", x=-3.1, y=-2.95)
        self.add(*mobs(ps), *mobs(hs), sm, cap)

        w = np.array(EV["weights"][1])
        P = [np.array(PX(*v)) for v in Vv]
        t = ValueTracker(0.0)          # 0 = equal weights, 1 = chase's heat-map row

        def cur():
            a = t.get_value()
            return (1 - a) * np.full(4, 0.25) + a * w

        def mix():
            ws = cur()
            return (ws[:, None] * np.array(P)).sum(0)

        masses = [always_redraw(lambda j=j: Circle(radius=0.12 + 0.35 * cur()[j], color=SPARK, stroke_width=4)
                                .move_to(P[j])) for j in range(4)]
        blend = Dot(PX(*CENT), radius=0.14, color=SPARK)
        pulls = [always_redraw(lambda j=j: Line(blend.get_center(), P[j], color=SOFT, stroke_width=2))
                 for j in range(4)]
        flyers = [hs["nums"][1][j].copy() for j in range(4)]
        ring = Circle(radius=0.24, color=INK, stroke_width=4).move_to(PX(*HOOK_OUT))
        read = num("chase out: " + pair(HOOK_OUT), 32).move_to([-3.0, -2.35, 0])
        others = [Circle(radius=0.11, color=INK, stroke_width=4).move_to(PX(*O2[i])) for i in (0, 2, 3)]

        c.at(0.2)
        c.go("set the mix", *[f.animate.move_to(P[j]).scale(0.6).set_opacity(0) for j, f in enumerate(flyers)],
             FadeIn(blend), hs["rowbox"].animate.set_color(INK), rt=1.0)
        self.add(*pulls, *masses)
        blend.add_updater(lambda m: m.move_to(mix()))
        c.go("Zero point five three", t.animate.set_value(1.0), rt=3.0)
        blend.clear_updaters()
        c.go("Exactly where", Create(ring), FadeOut(sm), FadeIn(read), rt=0.7)
        c.go("every other row", LaggedStart(*[GrowFromCenter(o) for o in others], lag_ratio=0.3), rt=1.2)
        c.end()


# --------------------------------------------------------------------------- B16
def qkv_row(hs):
    """Q, K, V as matrices across the top band, with letters above and role names below."""
    def mat(M):
        rows = r"\\".join(" & ".join(g(x).replace("−", "-") for x in r) for r in M)
        return MathTex(r"\begin{bmatrix}" + rows + r"\end{bmatrix}", font_size=36, color=INK)

    Qm = mat(EV["Q"]).move_to([-4.2, 1.4, 0])
    Km = mat(K).move_to([-0.45, 1.4, 0])
    Vm = mat(Vv).move_to([2.4, 1.4, 0])
    letters = [tex(s, 56).next_to(m, UP, buff=0.25) for s, m in (("Q", Qm), ("K", Km), ("V", Vm))]
    names = [label(s, 36).next_to(m, DOWN, buff=0.25) for s, m in (("query", Qm), ("key", Km), ("value", Vm))]
    hm = VGroup(*flat(hs["rects"]))          # shaded cells only: shrunk numerals would fall below the type floor
    return Qm, Km, Vm, letters, names, hm


def big_eq():
    return MathTex(r"\mathrm{Attention}(Q,K,V)", "=", r"\mathrm{softmax}\!\left(", r"{Q K^{\top}", r"\over",
                   r"\sqrt{d_k}}", r"\right)", "V", font_size=60, color=INK).move_to([0, -1.45, 0])


class B16_NameIt(Scene):
    def construct(self):
        c = Clock(self, "B16")
        ps = value_plane_state()
        hs = heat_state(box_color=INK)
        cap = caption("rounded; every row sums to 1", x=-3.1, y=-2.95)
        P = [np.array(PX(*v)) for v in Vv]
        w = EV["weights"][1]
        masses = [Circle(radius=0.12 + 0.35 * w[j], color=SPARK, stroke_width=4).move_to(P[j]) for j in range(4)]
        blend = Dot(PX(*HOOK_OUT), radius=0.14, color=SPARK)
        pulls = [Line(PX(*HOOK_OUT), P[j], color=SOFT, stroke_width=2) for j in range(4)]
        ring = Circle(radius=0.24, color=INK, stroke_width=4).move_to(PX(*HOOK_OUT))
        read = num("chase out: " + pair(HOOK_OUT), 32).move_to([-3.0, -2.35, 0])
        others = [Circle(radius=0.11, color=INK, stroke_width=4).move_to(PX(*O2[i])) for i in (0, 2, 3)]
        old = mobs(ps) + mobs(hs) + [cap, blend, ring, read] + masses + pulls + others
        self.add(*old)

        Qm, Km, Vm, letters, names, hm = qkv_row(hs)
        eq = big_eq()
        slot = RoundedRectangle(width=11.9, height=2.05, corner_radius=0.2, color=GHOST,
                                stroke_width=2).move_to([0, -1.45, 0])
        name = label("attention", 44).move_to([0, -2.93, 0])
        name_box = box(name, pad=0.3)

        c.at(0.2)
        c.play(*[FadeOut(m) for m in old if m not in hm.submobjects], hm.animate.scale(0.42).move_to([4.85, 1.4, 0]),
               FadeIn(Qm), FadeIn(Km), FadeIn(Vm), Create(slot), rt=1.0)
        c.go("the query", FadeIn(letters[0], shift=DOWN * 0.15), FadeIn(names[0]), rt=0.6)
        c.go("the key", FadeIn(letters[1], shift=DOWN * 0.15), FadeIn(names[1]), rt=0.6)
        c.go("its value", FadeIn(letters[2], shift=DOWN * 0.15), FadeIn(names[2]), rt=0.6)
        c.go("softmax of Q", TransformFromCopy(VGroup(Qm, letters[0], Km, letters[1]), eq[3]),
             TransformFromCopy(hm, VGroup(eq[2], eq[6])),
             TransformFromCopy(VGroup(Vm, letters[2]), eq[7]), rt=1.4)
        c.play(Write(eq[4]), Write(eq[5]), rt=0.6)
        c.go("That's attention", Write(eq[0]), Write(eq[1]), FadeOut(slot), FadeIn(name, shift=UP * 0.2),
             Create(name_box), rt=1.0)
        c.end()


# --------------------------------------------------------------------------- B17
def tangent_eq(size=44):
    return MathTex(r"\mathrm{Attention}(Q,K,V)", r"=\;", r"\mathrm{softmax}\!\left(", r"{Q K^{\top}", r"\over",
                   r"\sqrt{d_k}}", r"\right)", "V", font_size=size, color=INK)


def line(s, y, size=34, color=INK):
    """Left-aligned side-band sentence (left edge at x = -5.9)."""
    t = label(s, size, color)
    return t.move_to([-5.9 + W(t, 6) / 2, y, 0])


def ibox(part, **kw):
    """INK spotlight box (GATE T §8.3: no wide terracotta shapes at a beat's midpoint)."""
    return box(part, color=INK, **kw)


def span_box(a, b, padx=0.07, pady=0.09):
    """INK spotlight spanning from the left edge of `a` to the right edge of `b` (exact, no clipping)."""
    l, r = V(a.get_left())[0] - padx, V(b.get_right())[0] + padx
    g = VGroup(a, b)
    try:
        h = float(g.height) + 2 * pady
    except (TypeError, ValueError):
        h = 1.0
    return spot_ring(RoundedRectangle(width=max(r - l, 0.5), height=h, corner_radius=0.12, color=INK,
                                      stroke_width=6).move_to([(l + r) / 2, V(g.get_center())[1], 0]))


class B17_Tangent(Scene):
    def construct(self):
        c = Clock(self, "B17")
        Qm, Km, Vm, letters, names, hm = qkv_row(heat_state())
        hm.scale(0.42).move_to([4.85, 1.4, 0])
        eq0 = big_eq()
        name = label("attention", 44).move_to([0, -2.93, 0])
        name_box = box(name, pad=0.3)
        top = VGroup(Qm, Km, Vm, *letters, *names, hm)
        self.add(top, eq0, name, name_box)

        eq = tangent_eq(44).move_to([0.9, 2.5, 0])
        brow = label("tangent", 32, SOFT).move_to([-5.3, 2.5, 0])
        lhs = line("Left: what the head hands each word.", 1.2)
        rhs = line("Right: score every query against every key, shrink,", 0.45)
        rhs2 = line("turn each row into weights, blend the values.", -0.15)
        claim = line("=  the same thing, row for row.", -0.95)
        z2 = VGroup(lhs, rhs, rhs2, claim)

        gl_rows = [("Q", "matrix", "one query per word", "4 × 4"),
                   ("K", "matrix", "one key per word", "4 × 4"),
                   ("V", "matrix", "one value per word", "4 × 2"),
                   ("d_k", "fixed size", "length of a key", None)]
        gys = [1.15, 0.45, -0.25, -0.95]
        gl = []
        for (sym, role, mean, dom), y in zip(gl_rows, gys):
            gl.append(VGroup(tex(sym, 44).move_to([-5.3, y, 0]),
                             label(role, 32, SOFT).move_to([-3.5, y, 0]),
                             label(mean, 32).move_to([-0.2, y, 0]),
                             (label(dom, 32, SOFT) if dom else tex(r"4,\ \sqrt{d_k}=2", 38, SOFT)).move_to([3.6, y, 0])))
        sc = [d["score"] for d in WK["dots"]]
        hv = [d["scaled"] for d in WK["dots"]]
        xs = [-1.0, 0.6, 2.2, 3.8]
        wrow = []
        for y, head, vals, f in ((1.1, "scores", sc, g), (0.3, "÷ 2", hv, g), (-0.5, "softmax", A2[1], w2)):
            wrow.append(VGroup(label(head, 34, SOFT).move_to([-4.4, y, 0]),
                               *[num(f(v), 36).move_to([x, y, 0]) for v, x in zip(vals, xs)]))
        un = [round(x, 2) for x in EV["unscaled_focus_row"]]
        claim_box = Rectangle(width=11.6, height=1.25, color=GHOST, fill_color=SPARK, fill_opacity=0.0,
                              stroke_width=2).move_to([0, -2.15, 0])
        vc1a = tex(r"\div\sqrt{d_k}", 40).move_to([-5.1, -1.85, 0])
        vc1b = label("is a design choice. Without it, chase gets:", 32).move_to([-0.55, -1.85, 0])
        vc2 = num("   ".join(w2(x) for x in un), 32).move_to([-2.15, -2.45, 0])
        vc3 = label("picking, not blending", 32, SOFT).move_to([3.15, -2.45, 0])
        vc1 = VGroup(vc1a, vc1b, vc3)

        spot = ibox(eq[0])

        c.at(0.2)
        c.play(FadeOut(top), FadeOut(name), FadeOut(name_box), ReplacementTransform(eq0, eq), FadeIn(brow),
               Create(claim_box), rt=0.6)
        c.go("The left side", FadeIn(lhs), Create(spot), rt=0.7)
        c.go("The right side", FadeIn(rhs), FadeIn(rhs2), Transform(spot, span_box(eq[2], eq[7])), rt=0.8)
        c.go("The equals sign", FadeIn(claim), Transform(spot, ibox(eq[1], min_w=0.62)), rt=0.7)
        c.go("Q holds", FadeOut(z2), FadeIn(gl[0]), Transform(spot, ibox(eq[3])), rt=0.6)
        c.go("K the keys", FadeIn(gl[1]), rt=0.4)
        c.go("V the values", FadeIn(gl[2]), Transform(spot, ibox(eq[7])), rt=0.4)
        c.go("d k is", FadeIn(gl[3]), Transform(spot, ibox(eq[5])), rt=0.6)
        c.go("For chase", FadeOut(VGroup(*gl)), FadeIn(wrow[0]), rt=0.6)
        c.go("Halved", FadeIn(wrow[1]), rt=0.5)
        c.go("softmaxed", FadeIn(wrow[2]), Transform(spot, ibox(eq[2], min_w=0.62)), rt=0.6)
        c.go("design choice", claim_box.animate.set_fill(SPARK, opacity=0.10), FadeIn(vc1), FadeIn(vc2), Transform(spot, ibox(eq[5])), rt=0.8)
        c.go("Back to chase", FadeOut(spot), rt=0.5)
        c.end()


# --------------------------------------------------------------------------- B18
def strip_state(words, weights, scores_txt):
    """Chase's heat-map row as a one-row strip with column words and the cats/kids score chip."""
    y = ROWS[1]
    rects = [Rectangle(width=CW - 0.06, height=CH - 0.06, color=SOFT, stroke_width=1.5, fill_color=INK,
                       fill_opacity=0.45 * weights[j]).move_to([COLS[j], y, 0]) for j in range(4)]
    nums = [num(w2(weights[j]), 32).move_to([COLS[j], y, 0]) for j in range(4)]
    heads = [label(w, 32, SOFT).move_to([COLS[j], y + 0.72, 0]) for j, w in enumerate(words)]
    lab = row_label("chase", 1)
    chip = num(scores_txt, 32).move_to([-3.0, -0.75, 0])
    return rects, nums, heads, lab, chip


class B18_Payoff(Scene):
    def construct(self):
        c = Clock(self, "B18")
        # B17 end: equation at the top, worked row, values claim
        eq = tangent_eq(44).move_to([0.9, 2.5, 0])
        brow = label("tangent", 32, SOFT).move_to([-5.3, 2.5, 0])
        self.add(eq, brow)

        sent = sentence()
        ps = value_plane_state()
        w1 = EV["weights"][1]
        rects, nums, heads, lab, chip = strip_state(WORD, w1, "chase · cats offer:  3")
        P = [np.array(PX(*v)) for v in Vv]
        dot = Dot(PX(*HOOK_OUT), radius=0.14, color=SPARK)
        g1 = Circle(radius=0.2, color=SOFT, stroke_width=3).move_to(PX(*HOOK_OUT))
        g2 = Circle(radius=0.2, color=SOFT, stroke_width=3).move_to(PX(*KIDS_OUT))
        targets = [list(P[0]), list(P[1]), list(P[2]), list(P[3])]
        pulls = [always_redraw(lambda j=j: Line(dot.get_center(), targets[j], color=SOFT, stroke_width=2))
                 for j in range(4)]
        read = num("chase out: " + pair(HOOK_OUT), 32).move_to([-3.0, -2.35, 0])

        c.at(0.2)
        c.play(FadeOut(eq), FadeOut(brow), *[FadeIn(m) for m in sent + mobs(ps)], rt=0.55)
        c.go("mystery", FadeIn(dot), FadeIn(g1), FadeIn(g2), *[FadeIn(r) for r in rects],
             *[FadeIn(n) for n in nums], *[FadeIn(h) for h in heads], FadeIn(lab), FadeIn(read), rt=0.8)
        self.add(*pulls)

        kw = SWP["chase_weights"]
        kwords = ["kids"] + WORD[1:]
        r2, n2, h2, _, chip2 = strip_state(kwords, kw, "chase · kids offer:  −1")
        kdot = Dot(PX(*KIDS_V), radius=0.11, color=INK)
        klab = point_label("kids", KIDS_V)
        ksent = label("kids", 44).move_to(V(sent[0].get_center()).tolist())
        c.go("Swap cats for kids", Transform(sent[0], ksent), Transform(heads[0], h2[0]),
             ps["vdots"][0].animate.set_color(GHOST), ps["vlabs"][0].animate.set_color(GHOST),
             FadeIn(kdot), FadeIn(klab), rt=0.9)
        targets[0] = list(PX(*KIDS_V))
        c.go("scored three", FadeIn(chip), rt=0.5)
        c.go("only minus one", Transform(chip, chip2), rt=0.6)
        c.go("drains away", *[Transform(a, b) for a, b in zip(rects, r2)],
             *[Transform(a, b) for a, b in zip(nums, n2)], rt=1.0)
        read2 = num("chase out: " + pair(KIDS_OUT), 32).move_to([-3.0, -2.35, 0])
        c.go("point slides", dot.animate.move_to(PX(*KIDS_OUT)), Transform(read, read2), rt=1.2)
        c.end()


# --------------------------------------------------------------------------- B19
class B19_OrderBlind(Scene):
    def construct(self):
        c = Clock(self, "B19")
        # B18 end state
        ksent = sentence(["kids"] + WORD[1:])
        ps = value_plane_state()
        ps["vdots"][0].set_color(GHOST)
        ps["vlabs"][0].set_color(GHOST)
        kw = SWP["chase_weights"]
        r2, n2, h2, lab, chip2 = strip_state(["kids"] + WORD[1:], kw, "chase · kids offer:  −1")
        kdot = Dot(PX(*KIDS_V), radius=0.11, color=INK)
        klab = point_label("kids", KIDS_V)
        dot = Dot(PX(*KIDS_OUT), radius=0.14, color=SPARK)
        g1 = Circle(radius=0.2, color=SOFT, stroke_width=3).move_to(PX(*HOOK_OUT))
        g2 = Circle(radius=0.2, color=SOFT, stroke_width=3).move_to(PX(*KIDS_OUT))
        pulls = [Line(PX(*KIDS_OUT), PX(*v), color=SOFT, stroke_width=2) for v in [KIDS_V] + Vv[1:]]
        read = num("chase out: " + pair(KIDS_OUT), 32).move_to([-3.0, -2.35, 0])
        old = ksent + r2 + n2 + h2 + [lab, chip2, kdot, klab, dot, g1, g2, read] + pulls
        self.add(*mobs(ps), *old)

        sent = sentence()
        hs = heat_state(box_row=None)
        outs = [Circle(radius=0.12, color=INK, stroke_width=4).move_to(PX(*O2[i])) for i in range(4)]
        olab = label("cats", 32).move_to([PX(*O2[0])[0] + 0.62, PX(*O2[0])[1] - 0.05, 0])

        c.at(0.2)
        c.play(*[FadeOut(m) for m in old], ps["vdots"][0].animate.set_color(INK),
               ps["vlabs"][0].animate.set_color(INK), *[FadeIn(m) for m in sent + mobs(hs)],
               *[FadeIn(o) for o in outs], FadeIn(olab), rt=1.0)

        # reorder: cats <-> dogs in the sentence, then rows and columns of the heat map
        s0, s3 = V(sent[0].get_center()), V(sent[3].get_center())
        c.go("dogs chase small cats", sent[0].animate.move_to(s3.tolist()), sent[3].animate.move_to(s0.tolist()),
             rt=1.0)
        swap_rows = [hs["labs"][0].animate.move_to([V(hs["labs"][0].get_center())[0], ROWS[3], 0]),
                     hs["labs"][3].animate.move_to([V(hs["labs"][3].get_center())[0], ROWS[0], 0])]
        for j in range(4):
            for a, b in ((0, 3), (3, 0)):
                swap_rows.append(hs["rects"][a][j].animate.move_to([COLS[j], ROWS[b], 0]))
                swap_rows.append(hs["nums"][a][j].animate.move_to([COLS[j], ROWS[b], 0]))
        c.go("rows and columns", *swap_rows, rt=1.0)
        swap_cols = [hs["heads"][0].animate.move_to([COLS[3], ROWS[0] + 0.72, 0]),
                     hs["heads"][3].animate.move_to([COLS[0], ROWS[0] + 0.72, 0])]
        for i in range(4):
            for a, b in ((0, 3), (3, 0)):
                swap_cols.append(hs["rects"][i][a].animate.move_to([COLS[b], V(hs["rects"][i][a].get_center())[1], 0]))
                swap_cols.append(hs["nums"][i][a].animate.move_to([COLS[b], V(hs["nums"][i][a].get_center())[1], 0]))
        c.play(*swap_cols, rt=0.9)
        spot = Spot(width=0.62, height=0.62, corner_radius=0.12, color=SPARK,
                                stroke_width=6).move_to(PX(*O2[0]))
        c.go("exactly the same point", Create(spot), rt=0.6)

        pos = [label("+ position", 32, SOFT).move_to([V(s.get_center())[0], SENT_Y - 0.48, 0]) for s in sent]
        c.go("position signal", *[FadeIn(p, shift=DOWN * 0.1) for p in pos],
             *[o.animate.set_color(GHOST) for o in outs], olab.animate.set_color(GHOST), FadeOut(spot), rt=0.8)
        head = label("positional encoding (not taught here):", 32, SOFT).move_to([-3.05, -2.18, 0])
        r1 = VGroup(label("cats, original", 32), num(pair(WPOS["cats_output_order1"]), 30)
                    ).arrange(RIGHT, buff=0.3).move_to([-3.05, -2.57, 0])
        r2 = VGroup(label("cats, reordered", 32), num(pair(WPOS["cats_output_order2"]), 30)
                    ).arrange(RIGHT, buff=0.3).move_to([-3.05, -2.95, 0])
        c.go("somewhere new", FadeIn(head), FadeIn(r1), FadeIn(r2, shift=UP * 0.1), rt=0.9)
        c.end()
