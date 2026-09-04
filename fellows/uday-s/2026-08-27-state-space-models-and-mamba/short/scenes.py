"""Portrait 9:16 Manim beats for the SHORT cut of `state-space-models-and-mamba`.

Four beats survive the cut: B01 BLUF, B02 FRAMEWORK, B06 MECHANISM (Mamba's
selection), B08 FALSIFIABILITY. The bookends (B00, B11) are Remotion 916
compositions.

These are RE-LAID-OUT, not re-timed. The audio is unchanged from the parent
reel, so every run_time and wait below is copied verbatim from the landscape
scenes.py -- audio is the master clock and the short reuses the parent's mp3s.
Only geometry changes.

THE PORTRAIT FRAME: manim renders 9:16 at 2160x3840, which is a 4.5 x 8 frame
(x +/-2.25, y +/-4.0); GATE B's title-safe box inside that is +/-1.95 x,
+/-3.4 y -- a THIRD of the landscape width. Consequences:

    landscape                      portrait
    3 axis cards in a row (B02) -> 3 cards stacked in one column
    5 tokens across (B06)       -> 4 tokens across, tighter boxes
    SSM | Transformer (B08)     -> SSM ABOVE Transformer

The B08 side-by-side is preserved in substance: the fixed box and the growing
store are on screen TOGETHER and held to the end of the beat, which is what the
PROOF production gate asks for. Only the axis changed.

NO SOURCE, NO VERDICT: B06 and B08 keep their visible arXiv citations, on
screen at the moment of the claim. The citation strip is reserved by fit_src()
so the body never lands on it (GATE B reads that as label-on-a-line).

Palette is the Claude fidelity skin -- cream page, warm ink, ONE terracotta
accent. Never retint. No LaTeX anywhere (dvisvgm absent): Text/Pango only.
"""

import glob
import os

import numpy as np
import manimpango
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, LaggedStart, Line, ParametricFunction,
    RoundedRectangle, Scene, Text, VGroup, Write, config,
)

# THE PORTRAIT FRAME MUST BE DECLARED. Given `-r 2160,3840` alone, manim keeps
# the landscape frame_width (14.22) and stretches the frame anisotropically —
# the authored layout then renders as a squashed band in the middle of the
# canvas. Setting both explicitly gives a true 4.5 x 8 frame at ~477 px/unit
# on both axes, which is what every coordinate below assumes.
config.frame_width = 4.5
config.frame_height = 8.0

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR", "D:/Projects/brutalist.art/runtime/fonts",
)
for _ttf in glob.glob(os.path.join(_TOOLKIT_FONTS, "**", "*.ttf"), recursive=True):
    manimpango.register_font(os.path.abspath(_ttf))

_FAMS = set(manimpango.list_fonts())
SERIF = "EB Garamond" if "EB Garamond" in _FAMS else "Georgia"
SANS = "Inter 28pt" if "Inter 28pt" in _FAMS else "Segoe UI"
MONO = "Consolas" if "Consolas" in _FAMS else "Courier New"

CREAM = "#FAF9F5"
INK = "#3D3929"
INK_SOFT = "#6B6559"
TERRA = "#D97757"

BODY_TOP = 2.35        # clears the kicker subtitle, which bottoms out at 2.55
BODY_BOTTOM = -2.85
BODY_W = 3.8           # GATE B safe half-width is +/-1.95, so 3.9 is the ceiling
BODY_H = BODY_TOP - BODY_BOTTOM

# A citation occupies the strip just under the body, so beats that carry one
# get a SHORTER band — otherwise the body's bottom edge lands on the source
# line and GATE B reads it as label-on-a-line.
SRC_BOTTOM = -2.20     # clears the citation strip, which tops out at -2.35


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=19, color=INK_SOFT)
    # a kicker headline that fits landscape can run clean off a 4.5-wide frame;
    # clamp BEFORE positioning so the rule still starts at the text's left edge
    if k.width > 3.7:
        k.scale_to_fit_width(3.7)
    k.to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.32)
    rule = Line(k.get_left() + DOWN * 0.26, k.get_left() + RIGHT * 3.7 + DOWN * 0.26,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=15, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.18).align_to(k, LEFT)
        if s.width > 3.7:
            s.scale_to_fit_width(3.7)
        grp.add(s)
    return grp


def spark(text):
    t = Text(text, font=SERIF, font_size=31, color=TERRA).to_edge(DOWN, buff=0.62)
    if t.width > BODY_W:
        t.scale_to_fit_width(BODY_W)
    return t


def source_line(text):
    """A visible citation. No claim ships without one (no source, no verdict)."""
    t = Text(text, font=MONO, font_size=14, color=INK_SOFT).to_edge(DOWN, buff=1.50)
    if t.width > BODY_W:
        t.scale_to_fit_width(BODY_W)
    return t


def fit(group, w=BODY_W, h=BODY_H):
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + BODY_BOTTOM) / 2, 0])
    return group


def fit_src(group, w=BODY_W):
    h = BODY_TOP - SRC_BOTTOM
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + SRC_BOTTOM) / 2, 0])
    return group


def token_box(label, color=INK_SOFT, w=0.78, h=0.52, fs=17):
    t = Text(label, font=MONO, font_size=fs, color=color)
    b = RoundedRectangle(width=max(w, t.width + 0.18), height=h, corner_radius=0.08,
                         stroke_width=1.6, stroke_color=color, fill_opacity=0)
    b.move_to(t.get_center())
    return VGroup(b, t)


class B01_CostCurves(Scene):
    """BLUF: quadratic attention vs linear SSM. 17.69s."""

    def construct(self):
        page(self)
        head = kicker("IN ONE BREATH", "cost against sequence length")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Built around a centred origin so every construction coordinate already
        # sits inside the safe box — the static checker reads coords as authored,
        # not after fit() re-centres them. Portrait: a narrower, taller plot, and
        # the curve labels move BELOW the axes because there is no side room.
        o = np.array([-1.7, -1.4, 0.0])
        x_ax = Line(o, o + np.array([3.4, 0, 0]), stroke_width=2.0, color=INK_SOFT)
        y_ax = Line(o, o + np.array([0, 3.2, 0]), stroke_width=2.0, color=INK_SOFT)
        axes = VGroup(x_ax, y_ax)
        xlab = Text("sequence length →", font=SANS, font_size=16, color=INK_SOFT)
        xlab.next_to(x_ax, DOWN, buff=0.18).align_to(x_ax, RIGHT)
        ylab = Text("cost", font=SANS, font_size=16, color=INK_SOFT)
        ylab.next_to(y_ax, UP, buff=0.16)

        quad = ParametricFunction(lambda t: o + np.array([t, 0.28 * t * t, 0]),
                                  t_range=[0, 3.3], color=INK, stroke_width=5)
        lin = ParametricFunction(lambda t: o + np.array([t, 0.30 * t, 0]),
                                 t_range=[0, 3.3], color=INK_SOFT, stroke_width=5)

        # legend under the plot, not beside the curve ends
        qkey = Line(np.array([0, 0, 0]), np.array([0.42, 0, 0]),
                    stroke_width=5, color=INK)
        qlab = Text("attention — grows with the square",
                    font=SANS, font_size=17, color=INK)
        qlab.next_to(qkey, RIGHT, buff=0.20)
        qrow = VGroup(qkey, qlab)

        lkey = Line(np.array([0, 0, 0]), np.array([0.42, 0, 0]),
                    stroke_width=5, color=INK_SOFT)
        llab = Text("state space — linear", font=SANS, font_size=17, color=INK_SOFT)
        llab.next_to(lkey, RIGHT, buff=0.20)
        lrow = VGroup(lkey, llab)

        legend = VGroup(qrow, lrow).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        plot = VGroup(axes, xlab, ylab, quad, lin)
        fit(VGroup(plot, legend).arrange(DOWN, buff=0.45))

        self.play(Create(axes), FadeIn(VGroup(xlab, ylab)), run_time=1.2)
        self.play(Create(quad), run_time=2.2)
        self.play(FadeIn(qrow, shift=LEFT * 0.08), run_time=0.8)
        self.play(Create(lin), run_time=1.6)
        self.play(FadeIn(lrow, shift=RIGHT * 0.08), run_time=0.8)
        self.wait(1.2)

        point = spark("Memory traded for speed")
        self.play(Write(point), run_time=1.8)
        self.wait(7.19)


class B02_ThreeAxes(Scene):
    """FRAMEWORK: the three axes, shown before anything is scored. 17.88s.

    The hero beat of the short. In portrait the row of three cards becomes a
    single column, which also matches the order the narration names them.
    """

    AXES = [
        ("1", "STATE", "what does the model carry forward?"),
        ("2", "UPDATE", "how does it change when a token arrives?"),
        ("3", "COST", "what does one more token cost?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE THREE QUESTIONS", "ask these of any sequence model")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.AXES:
            n = Text(num, font=SERIF, font_size=27, color=TERRA)
            t = Text(title, font=SANS, font_size=23, color=INK)
            b = Text(body, font=MONO, font_size=15, color=INK_SOFT, line_spacing=0.7)
            if b.width > 3.05:
                b.scale_to_fit_width(3.05)
            head_row = VGroup(n, t).arrange(RIGHT, buff=0.26)
            inner = VGroup(head_row, b).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
            box = RoundedRectangle(width=max(3.55, inner.width + 0.5),
                                   height=inner.height + 0.60,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(DOWN, buff=0.38))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.0)
            self.wait(1.4)

        point = spark("Every sequence model answers these three")
        self.play(Write(point), run_time=1.8)
        self.wait(7.98)


class B06_MambaSelection(Scene):
    """MECHANISM: Mamba — parameters become functions of the input. 22.10s.

    Portrait drops the token run from five to FOUR: five 1.75-wide parameter
    boxes cannot sit in a 4.5 frame without scaling the labels below legibility.
    Four still carries the claim (per-token parameters, one propagated, one
    forgotten) and keeps the boxes readable on a phone.
    """

    PARAMS = ["Δ₁ B₁ C₁", "Δ₂ B₂ C₂", "Δ₃ B₃ C₃", "Δ₄ B₄ C₄"]

    def construct(self):
        page(self)
        head = kicker("MAMBA — SELECTION",
                      "parameters become functions of the input")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        n = len(self.PARAMS)
        toks = VGroup(*[token_box(f"x{i + 1}", INK_SOFT, w=0.62, h=0.46, fs=16)
                        for i in range(n)])
        toks.arrange(RIGHT, buff=0.30)

        # the token that gets kept, and the one that gets forgotten
        accents = [INK_SOFT, TERRA, INK_SOFT, INK_SOFT]
        blocks = VGroup()
        for t, p, a in zip(toks, self.PARAMS, accents):
            b = token_box(p, a, w=0.86, h=0.50, fs=14)
            b.next_to(t, UP, buff=0.85)
            blocks.add(b)
        links = VGroup(*[Line(toks[i].get_top(), blocks[i].get_bottom(),
                              stroke_width=1.6, color=accents[i]) for i in range(n)])

        keep = Text("propagate", font=SANS, font_size=17, color=TERRA)
        keep.next_to(blocks[1], UP, buff=0.28)
        drop = Text("forget", font=SANS, font_size=17, color=INK_SOFT)
        drop.next_to(blocks[3], UP, buff=0.28)
        # "forget" has to be VISIBLE, not just labelled. Cut the LINK, not the
        # block: a cross through the connection reads as "this token's
        # information does not propagate", crosses no text, stays above the
        # ~40% opacity floor, and leaves terracotta reserved for "propagate".
        _m = links[3].get_center()
        _d = 0.13
        strike = VGroup(
            Line(_m + np.array([-_d, -_d, 0]), _m + np.array([_d, _d, 0]),
                 stroke_width=2.6, color=INK_SOFT),
            Line(_m + np.array([-_d, _d, 0]), _m + np.array([_d, -_d, 0]),
                 stroke_width=2.6, color=INK_SOFT),
        )

        fit_src(VGroup(blocks, links, toks, keep, drop, strike))
        src = source_line("Gu & Dao 2023 · arXiv:2312.00752")

        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.15) for t in toks],
                              lag_ratio=0.25), run_time=1.5)
        for i in range(n):
            self.play(Create(blocks[i][0]), FadeIn(blocks[i][1]), Create(links[i]),
                      run_time=1.0)
        self.play(FadeIn(keep, shift=DOWN * 0.12), FadeIn(drop, shift=DOWN * 0.12),
                  Create(strike), run_time=1.8)
        self.wait(1.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.2)

        point = spark("Selectively propagate or forget")
        self.play(Write(point), run_time=1.8)
        self.wait(8.5)


class B08_CopyingCeiling(Scene):
    """FALSIFIABILITY: the fixed state has a proven ceiling. 27.11s.

    Both halves are on screen together and held, so the comparison is visible
    at the moment it is asserted (PROOF production gate). Portrait stacks the
    two models vertically instead of placing them side by side.
    """

    def construct(self):
        page(self)
        head = kicker("THE FRAMEWORK PREDICTS",
                      "axis 1 is fixed size — so what breaks?")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # TOP — one fixed state box against a growing input
        l_title = Text("STATE SPACE MODEL", font=SANS, font_size=18, color=INK)
        l_state = RoundedRectangle(width=1.05, height=1.05, corner_radius=0.12,
                                   stroke_width=2.2, stroke_color=TERRA, fill_opacity=0)
        l_cap = Text("one fixed box", font=MONO, font_size=15, color=INK_SOFT)
        left = VGroup(l_title, l_state, l_cap).arrange(DOWN, buff=0.22)

        # BOTTOM — a store that grows with the input
        r_title = Text("TRANSFORMER", font=SANS, font_size=18, color=INK)
        r_boxes = VGroup(*[RoundedRectangle(width=0.40, height=0.40, corner_radius=0.07,
                                            stroke_width=1.8, stroke_color=INK_SOFT,
                                            fill_opacity=0) for _ in range(6)])
        r_boxes.arrange(RIGHT, buff=0.12)
        r_cap = Text("grows with the input", font=MONO, font_size=15, color=INK_SOFT)
        right = VGroup(r_title, r_boxes, r_cap).arrange(DOWN, buff=0.22)

        pair = VGroup(left, right).arrange(DOWN, buff=0.45)

        stream = VGroup(*[token_box(f"t{i + 1}", INK_SOFT, w=0.46, h=0.36, fs=13)
                          for i in range(6)]).arrange(RIGHT, buff=0.12)
        stream_lab = Text("copy this input →", font=SANS, font_size=16, color=INK_SOFT)
        stream_row = VGroup(stream_lab, stream).arrange(DOWN, buff=0.18)

        # the verdict is composed INTO the fitted body, not positioned after it —
        # anything placed relative to a group post-fit can land on the citation
        verdict = Text("cannot copy unless the state\ngrows with the sequence",
                       font=SANS, font_size=19, color=TERRA, line_spacing=0.8)
        fit_src(VGroup(stream_row, pair, verdict).arrange(DOWN, buff=0.40))
        src = source_line("Jelassi et al. 2024 · arXiv:2402.01032")

        self.play(FadeIn(stream_lab), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.06) for t in stream],
                              lag_ratio=0.3), run_time=2.6)
        self.play(FadeIn(l_title), Create(l_state), FadeIn(l_cap), run_time=1.5)
        self.play(FadeIn(r_title), FadeIn(r_cap),
                  LaggedStart(*[Create(b) for b in r_boxes], lag_ratio=0.3),
                  run_time=2.5)
        self.wait(1.5)

        self.play(Write(verdict), run_time=2.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.2)

        point = spark("Fixed memory, fixed ceiling")
        self.play(Write(point), run_time=1.8)
        self.wait(9.81)
