"""Manim scenes for "Bayes' Theorem: The Positive That's Usually Wrong" (tldr-bayes-theorem).

LEARN section 1, beats B10-B19, one Scene per beat (tldr positional names; run.sh finds them by regex).
Timing: every reveal is placed on a spoken word from mp3/words.json (align.py).
Numbers: every on-screen value comes from demo/evidence.json (demo/bayes_demo.py).
Transform, don't cut: each scene opens on the previous scene's end state (the state
factories below) and morphs persistent objects; each ends at its beat's measured audio.
"""
from manim import *
import json
import os
import random
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
# GATE A pre-flights an isolated copy of this file; fall back to the reel folder.
REEL = Path(os.environ.get("ART_REEL", r"C:/Users/anant/stem-films/youtube/tldr-bayes-theorem"))


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
SLUG = SHEET["metadata"]["slug"]

C = EV["counts"]                 # n, sick, healthy, tp, fn, fp, tn, positives
PPV = EV["ppv"]
SWEEP = {d["base_rate"]: d for d in EV["base_rate_sweep"]}
CURVE = EV["base_rate_curve"]    # [[base_rate, P(D|+)], ...] log-spaced 0.1% .. 50%

# tldr LEARN stage (SKILL.md): cream, ink object, dim foil, ghost scaffold, ONE terracotta per beat.
PAGE, INK, SOFT, DIM, GHOST, SPARK = "#F2F0E9", "#3D3929", "#73705F", "#7A7E86", "#D9D4C7", "#D97757"
# DIM is one step darker than the skill's #8B8F96: a 10,000-mark grid at #8B8F96 anti-aliases below
# GATE V's 0.30 luminance separation at preview size (measured 0.277); #7A7E86 keeps the foil role.
CLEAR = "#E6E2D8"                 # a cleared (negative) person: lighter than scaffolding so lit marks read
SERIF = "EB Garamond"
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


def label(s, size=36, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color)


def tex(s, size=56, color=INK):
    return MathTex(s, font_size=size, color=color)


def V(v):
    """Any point-like to a float vector (the GATE A geometry stub returns placeholders)."""
    try:
        p = np.array(v, dtype=float)
        return p if p.shape == (3,) else np.zeros(3)
    except (TypeError, ValueError):
        return np.zeros(3)


def W(m, default=1.0):
    try:
        return float(m.width)
    except (TypeError, ValueError, AttributeError):
        return default


def box(part, pad=0.16, min_w=0.42, min_h=0.9, color=INK, sw=5):
    """Rounded spotlight box with a minimum height (never an underline on '=' / '-')."""
    w = max(W(part, 0.5) + pad, min_w)
    try:
        h = max(float(part.height) + pad, min_h)
    except (TypeError, ValueError, AttributeError):
        h = min_h
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, color=color,
                            stroke_width=sw).move_to(V(part.get_center()).tolist())


def ghost(m):
    """The layout-to-come in scaffold ghost (GATE V fill): drawn at t=0.2, replaced by the real thing."""
    return m.copy().set_color(GHOST)


def left_at(m, x):
    """Left-align a mobject at x (stub-safe)."""
    m.shift(RIGHT * (x - V(m.get_left())[0]))
    return m


def frac(top, bot, size=56, color=INK):
    """A fraction built from parts, so numerator and denominator can morph separately."""
    t = tex(top, size, color) if isinstance(top, str) else top
    b = tex(bot, size, color) if isinstance(bot, str) else bot
    w = max(W(t), W(b)) + 0.2
    bar = Line(LEFT * w / 2, RIGHT * w / 2, color=color, stroke_width=4)
    return VGroup(t, bar, b).arrange(DOWN, buff=0.14)


# ======================================================================= the grid
COLS, ROWS = 125, 80
PITCH, MARK = 0.068, 0.058
GX0, GY0 = -5.713, 2.533          # centre of cell 0 (grid spans x -5.74..2.74, y -2.86..2.56)
SIDE = 10                          # the sick: a 10 x 10 block in the top-left corner
SICK = [r * COLS + c for r in range(SIDE) for c in range(SIDE)]
FN_K = random.Random(f"{SLUG}-fn").randrange(C["sick"])   # index (into SICK) of the one the test misses
_sick_set = set(SICK)
FP_CELLS = sorted(random.Random(f"{SLUG}-fp").sample([i for i in range(C["n"]) if i not in _sick_set], C["fp"]))
TP_K = [k for k in range(C["sick"]) if k != FN_K]
assert len(SICK) == C["sick"] and len(TP_K) == C["tp"] and len(FP_CELLS) == C["fp"]

BLOCK_COLS, BLOCK_ROWS = 27, 22    # 594 positives regrouped (B14)
BPITCH, BMARK = 0.2, 0.16
BX0, BY0 = -4.2, 1.85              # centre of block cell 0 (block spans x -4.28..1.08, y -2.43..1.93)
assert BLOCK_COLS * BLOCK_ROWS == C["positives"]


def cell_xy(i):
    return GX0 + (i % COLS) * PITCH, GY0 - (i // COLS) * PITCH


def block_xy(k):
    return BX0 + (k % BLOCK_COLS) * BPITCH, BY0 - (k // BLOCK_COLS) * BPITCH


def cells_vm(idx, color, size=MARK):
    """Many squares as ONE VMobject (one subpath each): 10,000 marks stay cheap to render."""
    vm = VMobject(fill_color=color, fill_opacity=1, stroke_width=0)
    h = size / 2
    pts = []
    for i in idx:
        x, y = cell_xy(i)
        cs = [np.array([x - h, y - h, 0.0]), np.array([x + h, y - h, 0.0]),
              np.array([x + h, y + h, 0.0]), np.array([x - h, y + h, 0.0])]
        for k in range(4):
            a, b = cs[k], cs[(k + 1) % 4]
            pts += [a, a + (b - a) / 3, a + 2 * (b - a) / 3, b]
    try:
        vm.set_points(np.array(pts))
    except Exception:
        pass
    return vm


def grid_rows():
    """The 10,000-person base layer: one VMobject per row (80), all healthy-dim."""
    return VGroup(*[cells_vm(range(r * COLS, (r + 1) * COLS), DIM) for r in range(ROWS)])


def sq(x, y, size, color):
    return Square(side_length=size, fill_color=color, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


def sick_marks():
    """The 100 sick as individual squares (they move later). Index order = SICK."""
    return VGroup(*[sq(*cell_xy(i), MARK, INK) for i in SICK])


def fp_marks(color=DIM):
    return VGroup(*[sq(*cell_xy(i), MARK, color) for i in FP_CELLS])


def block_marks():
    """The 594 positives in the B14 block: 99 sick (ink) first, then 495 healthy (dim)."""
    tp = VGroup(*[sq(*block_xy(k), BMARK, INK) for k in range(C["tp"])])
    fp = VGroup(*[sq(*block_xy(C["tp"] + k), BMARK, DIM) for k in range(C["fp"])])
    return tp, fp


# ------------------------------------------------------------------ "you"
def you_big():
    """The HOOK's persistent object: one person, a positive result, an open question."""
    sqr = Square(side_length=2.3, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-4.6, -0.15, 0])
    name = label("you", 44).move_to([-4.6, -1.75, 0])
    stamp_t = label("positive", 60, INK)
    stamp = VGroup(RoundedRectangle(width=W(stamp_t, 2.4) + 0.6, height=1.05, corner_radius=0.14,
                                    color=SPARK, stroke_width=6), stamp_t).move_to([-1.55, -0.15, 0])
    q = tex(r"P(\text{sick}) = \,?", 100).move_to([3.15, -0.15, 0])
    return VGroup(sqr, name), stamp, q


def hook_chip(x=-1.55):
    t = label(f"catches {EV['test']['sensitivity_pct']:g}% of cases", 40)
    return VGroup(RoundedRectangle(width=W(t, 4.2) + 0.6, height=0.85, corner_radius=0.14,
                                   color=INK, stroke_width=4), t).move_to([x, 2.55, 0])


def you_badge():
    """'you' carried through the grid beats, top right."""
    s = Square(side_length=0.34, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([3.35, 2.8, 0])
    t = left_at(label("you: positive", 34).move_to([4.6, 2.8, 0]), 3.7)
    return VGroup(s, t)


def counter(s, y, color=INK, size=34):
    return left_at(label(s, size, color).move_to([4.6, y, 0]), 3.1)


def counters_b11():
    return VGroup(counter(f"{C['n']:,} people", 1.85, SOFT, 34),
                  counter(f"sick: {C['sick']}", 1.15),
                  counter(f"positive: {C['tp']}", 0.5),
                  counter(f"missed: {C['fn']}", -0.15, SOFT, 34))


def counters_b12():
    return VGroup(counter(f"healthy: {C['healthy']:,}", -0.95),
                  counter(f"false alarms: {C['fp']}", -1.6))


SICK_X0, SICK_X1 = GX0, GX0 + (SIDE - 1) * PITCH
SICK_Y0, SICK_Y1 = GY0, GY0 - (SIDE - 1) * PITCH
SICK_CY = (SICK_Y0 + SICK_Y1) / 2


def scan_v(x):
    return Rectangle(width=0.06, height=SIDE * PITCH + 0.14, fill_color=SOFT, fill_opacity=0.9,
                     stroke_width=0).move_to([x, SICK_CY, 0])


def sick_box():
    return Rectangle(width=SICK_X1 - SICK_X0 + 0.2, height=SICK_Y0 - SICK_Y1 + 0.2, color=INK,
                     stroke_width=6).move_to([(SICK_X0 + SICK_X1) / 2, SICK_CY, 0])


def sick_link():
    return Line([SICK_X1 + 0.12, SICK_CY, 0], [3.4, 1.0, 0], color=INK, stroke_width=3)


def scan_h(y):
    return Rectangle(width=8.6, height=0.07, fill_color=SOFT, fill_opacity=0.9,
                     stroke_width=0).move_to([-1.5, y, 0])


# ----------------------------------------------------------- state factories
def state_b12_end():
    """Grid after both tests: cleared rows ghost, sick ink (one missed, ghost), 495 lit dim."""
    rows = grid_rows().set_fill(CLEAR, 1)
    sick = sick_marks()
    sick[FN_K].set_fill(CLEAR, 1)
    fps = fp_marks()
    return rows, sick, fps, you_badge(), VGroup(*counters_b11(), *counters_b12())


def state_b14_end():
    tp, fp = block_marks()
    cap = label("each square = one person (expected counts)", 32, SOFT).move_to([-1.6, 2.75, 0])
    cnt = VGroup(counter(f"positives: {C['positives']}", 1.5),
                 counter(f"sick: {C['tp']}", 0.85),
                 counter(f"healthy: {C['fp']}", 0.2))
    ask = VGroup(label("what share", 44), label("are sick?", 44)).arrange(DOWN, buff=0.12).move_to([4.45, -1.2, 0])
    qm = label("?", 96, INK).move_to([4.45, -2.55, 0])
    return tp, fp, cap, cnt, you_badge(), ask, qm


def ask_box(ask, qm):
    return box(VGroup(ask, qm), pad=0.35, color=SPARK, sw=6)


def frac_one_sixth(size=150, color=INK):
    a, b = PPV["reduced"]
    return frac(str(a), str(b), size, color).move_to([3.9, 0.35, 0])


def sixth_box(sixth):
    return box(sixth, pad=0.4, color=SPARK, sw=6)


def pct_chip():
    f = C["positives"] - C["tp"]
    return VGroup(label(f"≈ {PPV['pct']:g}% sick", 34, SOFT), label(f"{f // C['tp']} in 6 are false alarms", 34, SOFT)
                  ).arrange(DOWN, buff=0.1).move_to([3.9, -2.35, 0])


def eq_counts():
    """Top row of B16: 99/594 = (99 ÷ 10,000)/(594 ÷ 10,000) = 0.99 × 0.01 / 0.0594."""
    f1 = frac(str(C["tp"]), str(C["positives"]), 64)
    f2 = frac(rf"{C['tp']} \div 10\,000", rf"{C['positives']} \div 10\,000", 56)
    f3 = frac(r"0.99 \times 0.01", rf"{EV['bayes']['p_pos_decimal']:g}", 56)
    row = VGroup(f1, tex("=", 64), f2, tex("=", 64), f3).arrange(RIGHT, buff=0.5).move_to([0, 1.8, 0])
    return row


def eq_bayes(general=False, size=72):
    if general:
        lhs, num, den = tex(r"P(A \mid B)", size), MathTex(r"P(B \mid A)", r"\,P(A)", font_size=size, color=INK), tex(r"P(B)", size)
    else:
        lhs, num, den = tex(r"P(D \mid +)", size), MathTex(r"P(+ \mid D)", r"\,P(D)", font_size=size, color=INK), tex(r"P(+)", size)
    f = frac(num, den, size)
    return VGroup(lhs, tex("=", size), f).arrange(RIGHT, buff=0.3)


def state_b16_end():
    top = eq_counts()
    eq = eq_bayes(True).move_to([0, -0.85, 0])
    name = label("Bayes' theorem", 52, INK).move_to([0, -2.75, 0])
    return top, eq, name, theorem_box(eq)


def theorem_box(eq):
    return box(eq, pad=0.45, color=SPARK, sw=6)


GLOSS = [(r"A", "the disease"), (r"B", "a positive test"),
         (r"P(B \mid A)", f"sensitivity · {EV['test']['sensitivity_pct'] / 100:g}"),
         (r"P(A)", f"base rate · {EV['test']['base_rate_pct'] / 100:g}"),
         (r"P(B)", f"all positives · {EV['bayes']['p_pos_decimal']:g}")]


def sentence(lines):
    return VGroup(*[label(t, 34) for t in lines]).arrange(DOWN, buff=0.08).move_to([3.1, 0.5, 0])


SENT1 = ["the chance of disease,", "given a positive"]
SENT2 = ["the chance of a positive,", "given disease, times the", "base rate, over all positives"]


def state_b17_parts():
    eq = eq_bayes(True, 60).move_to([0, 2.3, 0])
    rows = VGroup()
    for k, (sym, txt) in enumerate(GLOSS):
        y = 0.95 - 0.72 * k
        sm = tex(sym, 42).move_to([-5.0, y, 0])
        sm.shift(RIGHT * (-4.2 - V(sm.get_right())[0]))
        t = left_at(label(txt, 34).move_to([-2.4, y, 0]), -3.95)
        rows.add(VGroup(sm, t))
    sent = sentence(SENT1)
    worked = VGroup(frac(r"0.99 \times 0.01", rf"{EV['bayes']['p_pos_decimal']:g}", 46), tex("=", 52),
                    frac("1", "6", 52)).arrange(RIGHT, buff=0.28).move_to([3.1, -1.05, 0])
    claim = MathTex(r"P(B \mid A)", r"\neq", r"P(A \mid B)", font_size=56, color=INK).move_to([3.1, -2.2, 0])
    here = label(f"here: {EV['test']['sensitivity_pct'] / 100:g} vs. about {round(PPV['pct'] / 100, 2):g}", 32, SOFT
                 ).move_to([3.1, -2.95, 0])
    return eq, rows, sent, worked, claim, here


def state_b18_end():
    tp, fp = block_marks()
    ring = Square(side_length=0.5, color=INK, stroke_width=6).move_to([1.55, -2.2, 0])
    you = label("you", 40).move_to([1.55, -2.85, 0])
    a = frac("1", "100", 72).move_to([3.0, 2.2, 0])
    b = frac("1", "6", 72).move_to([5.3, 2.2, 0])
    arr = Arrow([3.65, 2.2, 0], [4.7, 2.2, 0], buff=0, color=INK, stroke_width=5,
                max_tip_length_to_length_ratio=0.25)
    ratio = MathTex(rf"{C['healthy']:,}".replace(",", "{,}"), ":", str(C["sick"]), font_size=64, color=INK
                    ).move_to([4.15, -0.75, 0])
    rlab = label("healthy : sick", 34, SOFT).move_to([4.15, -1.65, 0])
    return tp, fp, VGroup(ring, you), VGroup(a, arr, b), ratio, rlab


# ====================================================================== scenes
class B10_YouArePositive(Scene):
    def construct(self):
        c = Clock(self, "B10")
        you, stamp, q = you_big()
        chip = hook_chip(-3.8)
        gq = ghost(q)
        c.at(0.2)
        c.play(FadeIn(you[0], scale=0.9), FadeIn(you[1]), FadeIn(gq), rt=0.8)
        c.go("It catches", FadeIn(chip, shift=RIGHT * 0.6), rt=0.8)
        c.play(chip.animate.move_to([-1.55, 2.55, 0]), rt=1.2)
        c.go("positive", FadeIn(stamp, scale=1.15), rt=0.6)
        c.go("So how worried", FadeOut(gq), Write(q), rt=1.2)
        c.go("Hold on", Indicate(q[0][-1], color=INK, scale_factor=1.25), rt=0.8)
        c.end()


class B11_TenThousand(Scene):
    def construct(self):
        c = Clock(self, "B11")
        you, stamp, q = you_big()
        chip = hook_chip()
        self.add(you, stamp, q, chip)                             # B10's last frame
        rows = grid_rows()
        sick = sick_marks()
        badge = you_badge()
        cnt = counters_b11()
        c.at(0.2)
        c.play(ReplacementTransform(VGroup(you, stamp), badge), FadeOut(q), FadeOut(chip), rt=0.45)
        c.go("Ten thousand", LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.03), FadeIn(cnt[0]), rt=2.2)
        c.go("one hundred squares", FadeIn(sick), FadeIn(cnt[1]), rt=0.8)
        bar = scan_v(SICK_X0 - 0.1)
        c.go("Run the test", FadeIn(bar), rt=0.3)
        c.play(bar.animate.move_to([SICK_X1 + 0.1, SICK_CY, 0]), rt=1.0)
        c.go("It catches", FadeOut(bar), FadeIn(cnt[2]), rt=0.6)
        miss = sick[FN_K]
        ring = box(miss, pad=0.0, min_w=0.3, min_h=0.3, color=SPARK, sw=5)
        c.go("One slips", miss.animate.set_fill(CLEAR, 1), Create(ring), FadeIn(cnt[3]), rt=0.8)
        c.go("So far", FadeOut(ring), rt=0.6)
        c.end()


class B12_FalseAlarms(Scene):
    def construct(self):
        c = Clock(self, "B12")
        rows = grid_rows()
        sick = sick_marks()
        sick[FN_K].set_fill(CLEAR, 1)
        badge = you_badge()
        cnt = counters_b11()
        self.add(rows, sick, badge, cnt)                          # B11's last frame
        fps = fp_marks()
        more = counters_b12()
        c.at(0.2)
        c.play(FadeIn(more[0]), rt=0.6)
        self.add(fps)                                             # same colour as the row under it: invisible until rows clear
        bar = scan_h(GY0 - PITCH)
        # LaggedStart's Group is re-added on top when played: keep the marks above the rows
        for m in (sick, badge, fps, bar):
            m.set_z_index(1)
        c.go("The test clears", FadeIn(bar), rt=0.3)
        half = ROWS // 2
        c.play(bar.animate.move_to([-1.5, cell_xy((half - 1) * COLS)[1], 0]),
               LaggedStart(*[r.animate.set_fill(CLEAR, 1) for r in rows[:half]], lag_ratio=0.05), rt=1.1)
        c.play(bar.animate.move_to([-1.5, cell_xy((ROWS - 1) * COLS)[1], 0]),
               LaggedStart(*[r.animate.set_fill(CLEAR, 1) for r in rows[half:]], lag_ratio=0.05), rt=1.1)
        c.play(FadeOut(bar), rt=0.2)
        c.go("light up", fps.animate.set_fill(SPARK, 1), rt=0.6)
        c.go("Five percent of", fps.animate.set_fill(DIM, 1), rt=0.8)
        c.go("four hundred", FadeIn(more[1], shift=LEFT * 0.2), rt=0.6)
        c.go("Five times", Indicate(more[1], color=INK, scale_factor=1.1), Indicate(cnt[2], color=INK, scale_factor=1.1), rt=0.9)
        c.end()


class B13_WrongCrowd(Scene):
    def construct(self):
        c = Clock(self, "B13")
        rows, sick, fps, badge, cnt = state_b12_end()
        self.add(rows, sick, fps, badge, cnt)                     # B12's last frame
        rect = sick_box()
        f = frac(str(C["tp"]), str(C["sick"]), 96).move_to([4.5, 0.55, 0])
        lab = label("out of the sick", 36, SOFT).move_to([4.5, -0.95, 0])
        link = sick_link()
        cap = VGroup(label("but all you know", 34, SOFT), label("is: positive", 34, SOFT)
                     ).arrange(DOWN, buff=0.1).move_to([4.5, -2.25, 0])
        c.at(0.2)
        c.play(Create(rect), rt=0.8)
        c.go("ninety-nine of the", ReplacementTransform(VGroup(cnt[2], cnt[1]), f),
             FadeOut(VGroup(cnt[0], cnt[3], cnt[4], cnt[5])), Create(link), FadeIn(lab), rt=1.0)
        c.go("But that fraction", fps.animate.set_fill(SPARK, 1), rt=0.6)
        c.play(fps.animate.set_fill(DIM, 1), rt=0.6)
        c.go("All you know", FadeIn(cap, shift=UP * 0.2), Indicate(badge, color=INK, scale_factor=1.1), rt=0.9)
        c.end()


class B14_OnlyThePositives(Scene):
    def construct(self):
        c = Clock(self, "B14")
        rows, sick, fps, badge, _ = state_b12_end()
        rect = sick_box()
        f = frac(str(C["tp"]), str(C["sick"]), 96).move_to([4.5, 0.55, 0])
        lab = label("out of the sick", 36, SOFT).move_to([4.5, -0.95, 0])
        link = sick_link()
        cap0 = VGroup(label("but all you know", 34, SOFT), label("is: positive", 34, SOFT)
                      ).arrange(DOWN, buff=0.1).move_to([4.5, -2.25, 0])
        self.add(rows, sick, fps, badge, rect, f, lab, link, cap0)  # B13's last frame
        tp_b, fp_b, cap, cnt, _, ask, qm = state_b14_end()
        tp_src = VGroup(*[sick[k] for k in TP_K])
        c.at(0.2)
        c.play(FadeOut(VGroup(rect, f, lab, link, cap0)), rt=0.6)
        c.go("let everyone else", FadeOut(rows), FadeOut(sick[FN_K]), rt=0.9)
        c.go("Here they are", Transform(tp_src, tp_b), Transform(fps, fp_b), FadeIn(cap), rt=0.65)
        c.go("ninety-nine who", FadeIn(cnt[0]), FadeIn(cnt[1]), rt=0.5)
        c.go("four hundred", FadeIn(cnt[2]), rt=0.5)
        c.go("commit", FadeIn(ask), FadeIn(qm, scale=1.2), Create(ask_box(ask, qm)), rt=0.7)
        c.end()                                                   # the hold: nothing moves while the viewer commits


class B15_OneInSix(Scene):
    def construct(self):
        c = Clock(self, "B15")
        tp, fp, cap, cnt, badge, ask, qm = state_b14_end()
        abox = ask_box(ask, qm)
        self.add(tp, fp, cap, cnt, badge, ask, qm, abox)         # B14's last frame
        f = frac(str(C["tp"]), str(C["positives"]), 120).move_to([3.9, 0.35, 0])
        num, bar, den = f
        top = tp.copy()
        alln = VGroup(tp, fp).copy()
        sixth = frac_one_sixth()
        chip = pct_chip()
        c.at(0.2)
        c.play(FadeOut(VGroup(cnt, ask, qm, abox)),
               top.animate.arrange_in_grid(9, 11, buff=0.05).scale(0.55).move_to([3.9, 1.55, 0]), rt=1.0)
        c.go("Five hundred", alln.animate.arrange_in_grid(18, 33, buff=0.03).scale(0.42).move_to([3.9, -0.9, 0]),
             Create(bar), rt=1.0)
        c.go("Watch", ReplacementTransform(top, num), ReplacementTransform(alln, den), rt=1.2)
        c.go("One in six", ReplacementTransform(VGroup(num, bar, den), sixth), Create(sixth_box(sixth)), rt=0.9)
        c.go("Five out of", FadeIn(chip, shift=UP * 0.2), fp.animate.set_fill(CLEAR, 1), rt=0.8)
        c.end()


class B16_BuildBayes(Scene):
    def construct(self):
        c = Clock(self, "B16")
        tp, fp, cap, _, badge, _, _ = state_b14_end()
        fp.set_fill(CLEAR, 1)
        sixth = frac_one_sixth()
        sbox = sixth_box(sixth)
        chip = pct_chip()
        self.add(tp, fp, cap, badge, sixth, chip, sbox)         # B15's last frame
        top = eq_counts()
        f1, e1, f2, e2, f3 = top
        eqD = eq_bayes(False).move_to([0, -0.85, 0])
        lhsD, eqsD, fracD = eqD
        eqA = eq_bayes(True).move_to([0, -0.85, 0])
        name = label("Bayes' theorem", 52, INK).move_to([0, -2.75, 0])
        g1, g2, g3, g4 = ghost(VGroup(e1, f2)), ghost(VGroup(e2, f3)), ghost(eqD), ghost(name)
        c.at(0.2)
        c.play(FadeOut(VGroup(tp, fp, cap, badge, chip, sbox)), ReplacementTransform(sixth, f1), FadeIn(g1), FadeIn(g2), FadeIn(g3), FadeIn(g4), rt=0.85)
        c.go("Divide", FadeOut(g1), FadeIn(e1), FadeIn(f2, shift=LEFT * 0.2), rt=1.0)
        c.go("the counts become", FadeOut(g2), FadeIn(e2), FadeIn(f3, shift=LEFT * 0.2), rt=1.0)
        spot = box(f3[0], min_h=0.4, pad=0.06, color=SOFT)
        c.go("Ninety-nine becomes", Create(spot), FadeIn(fracD[0], shift=UP * 0.2), rt=0.9)
        c.go("Five hundred", Transform(spot, box(f3[2], min_h=0.4, pad=0.06, color=SOFT)), Create(fracD[1]),
             FadeIn(fracD[2], shift=UP * 0.2), rt=0.9)
        c.go("What's left", FadeOut(spot), FadeOut(g3), Write(lhsD), FadeIn(eqsD), rt=0.75)
        c.go("Bayes' theorem", FadeOut(g4), ReplacementTransform(eqD, eqA), FadeIn(name, shift=UP * 0.2),
             Create(theorem_box(eqA)), rt=1.2)
        c.end()


class B17_ReadTheLine(Scene):
    def construct(self):
        c = Clock(self, "B17")
        top, eq0, name, tbox = state_b16_end()
        self.add(top, eq0, name, tbox)                            # B16's last frame
        eq, rows, sent, worked, claim, here = state_b17_parts()
        lhs, eqs, fr = eq
        num, bar, den = fr
        sent2 = sentence(SENT2)
        g_rows, g_worked, g_claim = ghost(rows), ghost(worked), ghost(claim)
        c.at(0.2)
        c.play(FadeOut(top), FadeOut(name), FadeOut(tbox), ReplacementTransform(eq0, eq), FadeIn(g_rows), FadeIn(g_worked), FadeIn(g_claim), rt=0.7)
        spot = box(lhs, min_h=0.6)
        c.go("On the left", Create(spot), FadeIn(sent), FadeIn(rows[0]), FadeIn(rows[1]), rt=0.8)
        c.go("On the right", Transform(spot, box(num[0], min_h=0.6)), ReplacementTransform(sent, sent2),
             FadeIn(rows[2]), rt=0.9)
        c.go("times the base", Transform(spot, box(num[1], min_h=0.6)), FadeIn(rows[3]), rt=0.7)
        c.go("divided by", Transform(spot, box(den, min_h=0.6)), FadeIn(rows[4]), rt=0.7)
        c.go("Zero point nine nine", FadeOut(spot), FadeOut(g_worked), FadeIn(worked, shift=UP * 0.2), rt=1.0)
        c.go("The bar has", FadeOut(g_claim), FadeOut(g_rows), FadeIn(claim), rt=0.9)
        c.go("Swap its sides", Create(box(claim[1], min_w=0.7, min_h=0.8, color=SPARK, sw=6)), FadeIn(here), rt=0.8)
        c.end()


class B18_BackToYou(Scene):
    def construct(self):
        c = Clock(self, "B18")
        eq, rows, _, worked, claim, here = state_b17_parts()
        sent2 = sentence(SENT2)
        spot = box(claim[1], min_w=0.7, min_h=0.8, color=SPARK, sw=6)
        self.add(eq, rows, sent2, worked, claim, here, spot)      # B17's last frame
        tp, fp, you, fr, ratio, rlab = state_b18_end()
        you_sq, you_lab = you
        big = you_big()[0].scale(0.7).move_to([3.9, -1.55, 0])   # the HOOK's square, same factory, enters clear of the block
        c.at(0.2)
        c.play(FadeOut(VGroup(eq, rows, sent2, claim, here, spot)), FadeIn(tp), FadeIn(fp),
               ReplacementTransform(worked, fr[2]), FadeIn(big), rt=0.65)
        c.go("these five", ReplacementTransform(big[0], you_sq), ReplacementTransform(big[1], you_lab), rt=0.9)
        c.go("one in six is", Indicate(tp, color=INK, scale_factor=1.04), rt=0.8)
        c.go("from one in a", FadeIn(fr[0]), GrowArrow(fr[1]), rt=0.9)
        c.go("outnumbered", FadeIn(ratio), FadeIn(rlab), rt=0.8)
        c.go("so a small", Create(box(ratio[0], pad=0.25, color=SPARK, sw=6)), rt=0.6)
        c.end()


class B19_BaseRateDial(Scene):
    def construct(self):
        c = Clock(self, "B19")
        tp, fp, you, fr, ratio, rlab = state_b18_end()
        rbox = box(ratio[0], pad=0.25, color=SPARK, sw=6)
        self.add(tp, fp, you, fr, ratio, rlab, rbox)              # B18's last frame
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 1, 0.5], x_length=7.4, y_length=4.4,
                  axis_config={"color": INK, "stroke_width": 3, "include_ticks": True, "include_tip": False}
                  ).move_to([-1.3, 0.1, 0])

        def P(x, y):
            try:
                p = np.array(ax.c2p(x, y), dtype=float)
                return p if p.shape == (3,) else np.zeros(3)
            except (TypeError, ValueError):
                return np.zeros(3)

        lg = lambda b: float(np.log10(b)) + 3          # 0.1% -> 0 ... 100% -> 3
        curve = VMobject(color=INK, stroke_width=5)
        try:
            curve.set_points_smoothly([P(lg(b), p) for b, p in CURVE])
        except Exception:
            pass
        xt = VGroup(*[label(s, 32, SOFT).move_to(V(P(k, 0)) + DOWN * 0.42) for k, s in
                      zip((0, 1, 2, 3), ("0.1%", "1%", "10%", "100%"))])
        yt = VGroup(*[label(s, 32, SOFT).move_to(V(P(0, v)) + LEFT * 0.62) for v, s in ((0.5, "50%"), (1.0, "100%"))])
        xl = label("base rate: how common the disease is", 34, SOFT).move_to([-1.3, -2.98, 0])
        yl = left_at(label("chance sick, given a positive", 34, SOFT).move_to([-3.0, 2.85, 0]), -5.5)
        pts = {k: (lg(float(SWEEP[k]["base_rate_pct"]) / 100), SWEEP[k]["ppv_pct"] / 100) for k in SWEEP}
        dot = Dot(V(P(*pts["1/100"])), radius=0.13, color=SPARK)

        def path(a, b):
            seg = [P(lg(x), y) for x, y in CURVE if min(a, b) - 1e-9 <= x <= max(a, b) + 1e-9]
            if a > b:
                seg = seg[::-1]
            m = VMobject()
            try:
                m.set_points_smoothly([V(P(lg(a), 0.99 * a / (0.99 * a + 0.05 * (1 - a))))] + seg[1:-1]
                                      + [V(P(lg(b), 0.99 * b / (0.99 * b + 0.05 * (1 - b))))])
            except Exception:
                pass
            return m

        def readout(key):
            d = SWEEP[key]
            return VGroup(label(f"base rate {d['base_rate_pct']:g}%", 36),
                          label(f"→ {d['ppv_pct']:g}% sick", 40)).arrange(DOWN, buff=0.14).move_to([4.45, 1.35, 0])

        r = readout("1/100")
        note = VGroup(label("same test:", 32, SOFT), label("99% sensitive,", 32, SOFT), label("95% specific", 32, SOFT)
                      ).arrange(DOWN, buff=0.08).move_to([4.45, -0.55, 0])
        gap = VGroup(label("not taught here:", 32, SOFT), label("a second positive", 32, SOFT)
                     ).arrange(DOWN, buff=0.08).move_to([4.45, -2.35, 0])
        c.at(0.2)
        c.play(FadeOut(VGroup(tp, fp, you, fr[0], fr[1], ratio, rlab, rbox)), Create(ax), FadeIn(xt), FadeIn(yt),
               FadeIn(yl), fr[2].animate.scale(0.5).move_to(V(P(*pts["1/100"])) + UP * 0.8 + LEFT * 0.45), rt=1.1)
        c.go("the base rate", Create(curve), FadeIn(xl), FadeIn(dot), FadeIn(r), rt=1.2)
        c.go("one in a thousand", MoveAlongPath(dot, path(0.01, 0.001)), Transform(r, readout("1/1000")),
             FadeIn(note), rt=1.4)
        c.go("One in ten", MoveAlongPath(dot, path(0.001, 0.1)), Transform(r, readout("1/10")), rt=1.6)
        c.go("One in two", MoveAlongPath(dot, path(0.1, 0.5)), Transform(r, readout("1/2")), rt=1.2)
        c.go("What this film", FadeIn(gap, shift=UP * 0.2), rt=0.8)
        c.end()
