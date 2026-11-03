"""Manim beats for the reel `state-space-models-and-mamba`.

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B01_*(Scene)` and slots the render into manim/B01.mp4).
Run-times match the MEASURED Kokoro am_onyx audio in beat_sheet.json -- audio is
the master clock, never these numbers.

NO LaTeX anywhere: dvisvgm is not installed on this machine, so MathTex/Tex
would fail at render time. The SSM equations are set as plain Text/Pango.

Every claim rendered here is sourced in SOURCES.md / FACTCHECK.md:
  S4       Gu, Goel, Re 2021 -- arXiv:2111.00396
  Mamba    Gu & Dao 2023     -- arXiv:2312.00752
  Copying  Jelassi et al. 2024 -- arXiv:2402.01032

Palette is the Claude fidelity skin -- cream page, warm ink, ONE terracotta
accent. Never retint. Safe area is +/-6.3 x, +/-3.4 y (GATE B); body content
lives between BODY_TOP and BODY_BOTTOM and is SCALED to fit.
"""

import glob
import os

import manimpango
import numpy as np
from manim import (
    DOWN, LEFT, RIGHT, UP, Create, FadeIn, FadeOut, LaggedStart, Line,
    ParametricFunction, RoundedRectangle, Scene, Text, VGroup, Write,
)

_TOOLKIT_FONTS = os.environ.get(
    "ART_FONT_DIR",
    "D:/Projects/brutalist.art/.claude/worktrees/video-creation-setup-4c85fe/runtime/fonts",
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

BODY_TOP = 2.25
BODY_BOTTOM = -2.45
BODY_W = 12.0
BODY_H = BODY_TOP - BODY_BOTTOM


def page(scene):
    scene.camera.background_color = CREAM


def kicker(text, sub=None):
    k = Text(text, font=SANS, font_size=22, color=INK_SOFT).to_edge(UP, buff=0.72)
    k.to_edge(LEFT, buff=0.9)
    rule = Line(k.get_left() + DOWN * 0.28, k.get_left() + RIGHT * 12.0 + DOWN * 0.28,
                stroke_width=1.4, color=INK_SOFT)
    grp = VGroup(k, rule)
    if sub:
        s = Text(sub, font=MONO, font_size=19, color=INK_SOFT)
        s.next_to(rule, DOWN, buff=0.20).align_to(k, LEFT)
        grp.add(s)
    return grp


def spark(text):
    return Text(text, font=SERIF, font_size=38, color=TERRA).to_edge(DOWN, buff=0.62)


def source_line(text):
    """A visible citation. No claim ships without one (no source, no verdict)."""
    return Text(text, font=MONO, font_size=17, color=INK_SOFT).to_edge(DOWN, buff=1.55)


def fit(group, w=BODY_W, h=BODY_H):
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + BODY_BOTTOM) / 2, 0])
    return group


# A citation occupies the strip just under the body, so beats that carry one
# get a SHORTER band — otherwise the body's bottom edge lands on the source
# line and GATE B reads it as label-on-a-line.
SRC_BOTTOM = -1.95


def fit_src(group, w=BODY_W):
    h = BODY_TOP - SRC_BOTTOM
    if group.width > w:
        group.scale_to_fit_width(w)
    if group.height > h:
        group.scale_to_fit_height(h)
    group.move_to([0, (BODY_TOP + SRC_BOTTOM) / 2, 0])
    return group


def card(title, body, accent=INK_SOFT, width=3.6, title_size=27, body_size=21):
    t = Text(title, font=SANS, font_size=title_size, color=INK)
    b = Text(body, font=MONO, font_size=body_size, color=INK_SOFT, line_spacing=0.7)
    inner = VGroup(t, b).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    # never narrower than the content — a fixed width smaller than its text puts
    # the text across the border stroke, which GATE B reads as label-on-a-line
    box = RoundedRectangle(width=max(width, inner.width + 0.7),
                           height=inner.height + 0.8, corner_radius=0.12,
                           stroke_width=1.8, stroke_color=accent, fill_opacity=0)
    box.move_to(inner.get_center())
    return VGroup(box, inner)


def token_box(label, color=INK_SOFT, w=0.95, h=0.6, fs=20):
    t = Text(label, font=MONO, font_size=fs, color=color)
    b = RoundedRectangle(width=w, height=h, corner_radius=0.08,
                         stroke_width=1.6, stroke_color=color, fill_opacity=0)
    b.move_to(t.get_center())
    return VGroup(b, t)


class B01_CostCurves(Scene):
    """BLUF: quadratic attention vs linear SSM. 17.69s."""

    def construct(self):
        page(self)
        head = kicker("THE TRADE, IN ONE BREATH", "cost against sequence length")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # Built around a centred origin so every construction coordinate already
        # sits inside the safe box — the static checker reads coords as authored,
        # not after fit() re-centres them.
        o = np.array([-3.3, -1.9, 0.0])
        x_ax = Line(o, o + np.array([6.6, 0, 0]), stroke_width=2.0, color=INK_SOFT)
        y_ax = Line(o, o + np.array([0, 3.5, 0]), stroke_width=2.0, color=INK_SOFT)
        axes = VGroup(x_ax, y_ax)
        xlab = Text("sequence length →", font=SANS, font_size=20, color=INK_SOFT)
        xlab.next_to(x_ax, DOWN, buff=0.22).align_to(x_ax, RIGHT)
        ylab = Text("cost", font=SANS, font_size=20, color=INK_SOFT)
        ylab.next_to(y_ax, UP, buff=0.18)

        quad = ParametricFunction(lambda t: o + np.array([t, 0.078 * t * t, 0]),
                                  t_range=[0, 6.4], color=INK, stroke_width=5)
        lin = ParametricFunction(lambda t: o + np.array([t, 0.30 * t, 0]),
                                 t_range=[0, 6.4], color=INK_SOFT, stroke_width=5)
        qlab = Text("attention  —  grows with the square",
                    font=SANS, font_size=23, color=INK)
        qlab.next_to(quad.get_end(), LEFT, buff=0.25).shift(UP * 0.30)
        llab = Text("state space  —  linear", font=SANS, font_size=23, color=INK_SOFT)
        llab.next_to(lin.get_end(), RIGHT, buff=0.22)

        body = fit(VGroup(axes, xlab, ylab, quad, lin, qlab, llab))

        self.play(Create(axes), FadeIn(VGroup(xlab, ylab)), run_time=1.2)
        self.play(Create(quad), run_time=2.2)
        self.play(FadeIn(qlab, shift=LEFT * 0.2), run_time=0.8)
        self.play(Create(lin), run_time=1.6)
        self.play(FadeIn(llab, shift=RIGHT * 0.2), run_time=0.8)
        self.wait(1.2)

        point = spark("Memory traded for speed")
        self.play(Write(point), run_time=1.8)
        self.wait(7.19)


class B02_ThreeAxes(Scene):
    """FRAMEWORK: the three axes, shown before anything is scored. 17.88s."""

    AXES = [
        ("1", "STATE", "what does the model\ncarry forward?"),
        ("2", "UPDATE", "how does it change\nwhen a token arrives?"),
        ("3", "COST", "what does one more\ntoken cost?"),
    ]

    def construct(self):
        page(self)
        head = kicker("THE THREE QUESTIONS", "ask these of any sequence model")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        cards = VGroup()
        for num, title, body in self.AXES:
            n = Text(num, font=SERIF, font_size=34, color=TERRA)
            t = Text(title, font=SANS, font_size=30, color=INK)
            b = Text(body, font=MONO, font_size=21, color=INK_SOFT, line_spacing=0.7)
            head_row = VGroup(n, t).arrange(RIGHT, buff=0.30)
            inner = VGroup(head_row, b).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
            box = RoundedRectangle(width=3.85, height=inner.height + 0.9,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit(cards.arrange(RIGHT, buff=0.42))

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.15), run_time=1.0)
            self.wait(1.4)

        point = spark("Every sequence model answers these three")
        self.play(Write(point), run_time=1.8)
        self.wait(7.98)


class B03_ScoreIncumbents(Scene):
    """WORKED EXAMPLE: RNN and Transformer scored on the axes. 21.29s."""

    ROWS = ["STATE", "UPDATE", "COST"]
    RNN = ["small, fixed", "same rule each step", "constant per token"]
    TFM = ["the whole context", "attention over all", "grows with the square"]

    def construct(self):
        page(self)
        head = kicker("SCORE THE TWO YOU KNOW", "the rubric, applied")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        row_labels = VGroup(*[Text(r, font=SANS, font_size=25, color=INK_SOFT)
                              for r in self.ROWS])
        row_labels.arrange(DOWN, buff=0.85, aligned_edge=RIGHT)

        def col(title, cells, color):
            h = Text(title, font=SANS, font_size=27, color=INK)
            items = VGroup()
            for c in cells:
                t = Text(c, font=MONO, font_size=21, color=color)
                box = RoundedRectangle(width=4.35, height=0.72, corner_radius=0.09,
                                       stroke_width=1.5, stroke_color=INK_SOFT,
                                       fill_opacity=0).move_to(t.get_center())
                items.add(VGroup(box, t))
            items.arrange(DOWN, buff=0.42)
            g = VGroup(h, items).arrange(DOWN, buff=0.45)
            return g

        rnn = col("RNN", self.RNN, INK)
        tfm = col("TRANSFORMER", self.TFM, INK)
        grid = VGroup(row_labels, rnn, tfm).arrange(RIGHT, buff=0.65, aligned_edge=DOWN)
        fit(grid)

        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in row_labels],
                              lag_ratio=0.3), run_time=1.2)
        self.play(FadeIn(rnn[0], shift=UP * 0.15), run_time=0.7)
        for cell in rnn[1]:
            self.play(Create(cell[0]), FadeIn(cell[1]), run_time=0.8)
        self.wait(1.5)
        self.play(FadeIn(tfm[0], shift=UP * 0.15), run_time=0.7)
        for cell in tfm[1]:
            self.play(Create(cell[0]), FadeIn(cell[1]), run_time=0.8)
        self.wait(1.5)

        point = spark("Forgets nothing — and pays every token")
        self.play(Write(point), run_time=1.7)
        self.wait(8.29)


class B04_SSMRecurrence(Scene):
    """MECHANISM: the SSM equations and the fixed-size state. 19.61s."""

    def construct(self):
        page(self)
        head = kicker("THE STATE SPACE MODEL", "borrowed from control theory")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        eq1 = Text("h'(t)  =  A h(t)  +  B x(t)", font=MONO, font_size=40, color=INK)
        eq2 = Text("y(t)  =  C h(t)", font=MONO, font_size=40, color=INK)
        eqs = VGroup(eq1, eq2).arrange(DOWN, buff=0.42)

        chain = VGroup()
        for i in range(4):
            st = token_box("h", INK, w=1.0, h=0.72, fs=24)
            tok = Text(f"x{i + 1}", font=MONO, font_size=20, color=INK_SOFT)
            tok.next_to(st, DOWN, buff=0.22)
            chain.add(VGroup(st, tok))
        chain.arrange(RIGHT, buff=1.05)
        arrows = VGroup(*[
            Line(chain[i][0].get_right(), chain[i + 1][0].get_left(),
                 stroke_width=2.0, color=INK_SOFT)
            for i in range(3)
        ])
        note = Text("one fixed-size state, stepped per token",
                    font=SANS, font_size=22, color=INK_SOFT)
        note.next_to(chain, DOWN, buff=0.55)

        body = fit(VGroup(eqs, VGroup(chain, arrows, note)).arrange(DOWN, buff=0.75))

        self.play(Write(eq1), run_time=2.0)
        self.play(Write(eq2), run_time=1.6)
        self.wait(1.5)
        self.play(LaggedStart(*[Create(c[0][0]) for c in chain],
                              *[FadeIn(c[0][1]) for c in chain],
                              *[FadeIn(c[1]) for c in chain],
                              lag_ratio=0.18), run_time=1.9)
        self.play(Create(arrows), FadeIn(note), run_time=1.6)
        self.wait(1.0)

        point = spark("Fixed state. Linear cost.")
        self.play(Write(point), run_time=1.7)
        self.wait(7.41)


class B05_S4Fixed(Scene):
    """MECHANISM: S4 — the SAME matrices for every token. 22.21s."""

    def construct(self):
        page(self)
        head = kicker("S4 — STRUCTURE MADE IT TRAINABLE",
                      "first non-trivial result on Path-X")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        toks = VGroup(*[token_box(f"x{i + 1}", INK_SOFT) for i in range(5)])
        toks.arrange(RIGHT, buff=0.75)

        blocks = VGroup()
        for t in toks:
            b = token_box("A B C", INK, w=1.45, h=0.62, fs=19)
            b.next_to(t, UP, buff=0.75)
            blocks.add(b)
        links = VGroup(*[Line(toks[i].get_top(), blocks[i].get_bottom(),
                              stroke_width=1.6, color=INK_SOFT) for i in range(5)])

        same = Text("identical for every token", font=SANS, font_size=24, color=TERRA)
        same.next_to(blocks, UP, buff=0.45)

        body = fit(VGroup(blocks, links, toks, same))
        src = source_line("Gu, Goel & Ré 2021 · arXiv:2111.00396")

        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.15) for t in toks],
                              lag_ratio=0.25), run_time=1.4)
        for i in range(5):
            self.play(Create(blocks[i][0]), FadeIn(blocks[i][1]), Create(links[i]),
                      run_time=0.9)
        self.play(FadeIn(same, shift=DOWN * 0.15), run_time=1.5)
        self.wait(1.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.2)

        point = spark("It could not choose what mattered")
        self.play(Write(point), run_time=1.8)
        self.wait(8.51)


class B06_MambaSelection(Scene):
    """MECHANISM: Mamba — parameters become functions of the input. 22.10s."""

    PARAMS = ["Δ₁ B₁ C₁", "Δ₂ B₂ C₂", "Δ₃ B₃ C₃", "Δ₄ B₄ C₄", "Δ₅ B₅ C₅"]

    def construct(self):
        page(self)
        head = kicker("MAMBA — SELECTION",
                      "the parameters become functions of the input")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        toks = VGroup(*[token_box(f"x{i + 1}", INK_SOFT) for i in range(5)])
        toks.arrange(RIGHT, buff=0.75)

        # the token that gets kept, and the one that gets forgotten
        accents = [INK_SOFT, TERRA, INK_SOFT, INK_SOFT, INK_SOFT]
        blocks = VGroup()
        for t, p, a in zip(toks, self.PARAMS, accents):
            b = token_box(p, a, w=1.75, h=0.62, fs=18)
            b.next_to(t, UP, buff=0.75)
            blocks.add(b)
        links = VGroup(*[Line(toks[i].get_top(), blocks[i].get_bottom(),
                             stroke_width=1.6, color=accents[i]) for i in range(5)])

        keep = Text("propagate", font=SANS, font_size=21, color=TERRA)
        keep.next_to(blocks[1], UP, buff=0.32)
        drop = Text("forget", font=SANS, font_size=21, color=INK_SOFT)
        drop.next_to(blocks[3], UP, buff=0.32)
        # "forget" has to be VISIBLE, not just labelled. Cut the LINK, not the
        # block: a cross through the connection reads as "this token's
        # information does not propagate", and — unlike a strikethrough over the
        # label — it crosses no text, stays above the ~40% opacity floor, and
        # leaves terracotta reserved for "propagate".
        _m = links[3].get_center()
        _d = 0.15
        strike = VGroup(
            Line(_m + np.array([-_d, -_d, 0]), _m + np.array([_d, _d, 0]),
                 stroke_width=2.6, color=INK_SOFT),
            Line(_m + np.array([-_d, _d, 0]), _m + np.array([_d, -_d, 0]),
                 stroke_width=2.6, color=INK_SOFT),
        )

        body = fit(VGroup(blocks, links, toks, keep, drop, strike))
        src = source_line("Gu & Dao 2023 · arXiv:2312.00752")

        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.15) for t in toks],
                              lag_ratio=0.25), run_time=1.5)
        for i in range(5):
            self.play(Create(blocks[i][0]), FadeIn(blocks[i][1]), Create(links[i]),
                      run_time=0.8)
        self.play(FadeIn(keep, shift=DOWN * 0.12), FadeIn(drop, shift=DOWN * 0.12),
                  Create(strike), run_time=1.8)
        self.wait(1.4)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.2)

        point = spark("Selectively propagate or forget")
        self.play(Write(point), run_time=1.8)
        self.wait(8.5)


class B07_PaperNumbers(Scene):
    """EVIDENCE: the paper's own headline numbers, with the citation. 20.78s."""

    CLAIMS = [
        ("5×", "inference throughput vs\na similar-size Transformer"),
        ("linear", "scaling in\nsequence length"),
        ("1M", "sequence length —\nstill improving"),
        ("3B", "matches Transformers\ntwice its size"),
    ]

    def construct(self):
        page(self)
        head = kicker("WHAT SELECTION BOUGHT", "the paper's own numbers")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # 2x2, and the box is sized to its OWN content: a fixed width narrower
        # than the text pushed the body across the border stroke (GATE B caught
        # it as label-on-a-line). Never hard-code a box narrower than its text.
        cards = VGroup()
        for big, body in self.CLAIMS:
            n = Text(big, font=SERIF, font_size=52, color=TERRA)
            b = Text(body, font=MONO, font_size=19, color=INK_SOFT, line_spacing=0.7)
            inner = VGroup(n, b).arrange(DOWN, buff=0.28)
            box = RoundedRectangle(width=inner.width + 0.9, height=inner.height + 0.85,
                                   corner_radius=0.12, stroke_width=1.8,
                                   stroke_color=INK_SOFT, fill_opacity=0)
            box.move_to(inner.get_center())
            cards.add(VGroup(box, inner))
        fit_src(VGroup(*cards).arrange_in_grid(rows=2, cols=2, buff=(0.5, 0.45)))
        src = source_line("Gu & Dao 2023 · arXiv:2312.00752 — abstract")

        for c in cards:
            self.play(Create(c[0]), FadeIn(c[1], shift=UP * 0.12), run_time=0.9)
            self.wait(1.2)
        self.play(FadeIn(src), run_time=1.0)
        self.wait(1.0)

        point = spark("No attention. No MLP blocks.")
        self.play(Write(point), run_time=1.7)
        self.wait(7.78)


class B08_CopyingCeiling(Scene):
    """FALSIFIABILITY: the fixed state has a proven ceiling. 27.11s.

    Both halves are on screen together and held, so the comparison is visible
    at the moment it is asserted (PROOF production gate).
    """

    def construct(self):
        page(self)
        head = kicker("WHAT THE FRAMEWORK PREDICTS",
                      "axis 1 is fixed size — so what breaks?")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        # LEFT — one fixed state box against a growing input
        l_title = Text("STATE SPACE MODEL", font=SANS, font_size=23, color=INK)
        l_state = RoundedRectangle(width=1.6, height=1.6, corner_radius=0.12,
                                   stroke_width=2.2, stroke_color=TERRA, fill_opacity=0)
        l_cap = Text("one fixed box", font=MONO, font_size=19, color=INK_SOFT)
        l_cap.next_to(l_state, DOWN, buff=0.25)
        left = VGroup(l_title, l_state, l_cap).arrange(DOWN, buff=0.35)

        # RIGHT — a store that grows with the input
        r_title = Text("TRANSFORMER", font=SANS, font_size=23, color=INK)
        r_boxes = VGroup(*[RoundedRectangle(width=0.5, height=0.5, corner_radius=0.07,
                                            stroke_width=1.8, stroke_color=INK_SOFT,
                                            fill_opacity=0) for _ in range(6)])
        r_boxes.arrange(RIGHT, buff=0.14)
        r_cap = Text("grows with the input", font=MONO, font_size=19, color=INK_SOFT)
        r_cap.next_to(r_boxes, DOWN, buff=0.25)
        right = VGroup(r_title, r_boxes, r_cap).arrange(DOWN, buff=0.35)

        pair = VGroup(left, right).arrange(RIGHT, buff=1.5, aligned_edge=UP)

        stream = VGroup(*[token_box(f"t{i + 1}", INK_SOFT, w=0.62, h=0.44, fs=17)
                          for i in range(8)]).arrange(RIGHT, buff=0.16)
        stream_lab = Text("copy this input →", font=SANS, font_size=21, color=INK_SOFT)
        stream_row = VGroup(stream_lab, stream).arrange(RIGHT, buff=0.35)

        # the verdict is composed INTO the fitted body, not positioned after it —
        # anything placed relative to a group post-fit can land on the citation
        verdict = Text("cannot copy unless the state grows with the sequence",
                       font=SANS, font_size=25, color=TERRA)
        body = fit_src(VGroup(stream_row, pair, verdict).arrange(DOWN, buff=0.55))
        src = source_line("Jelassi et al. 2024 · arXiv:2402.01032")

        self.play(FadeIn(stream_lab), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.15) for t in stream],
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


class B09_Verdict(Scene):
    """VERDICT: Mamba scored on the same axes, plus when NOT to use it. 18.39s."""

    ROWS = ["STATE", "UPDATE", "COST"]
    MAMBA = ["fixed and small", "input-dependent", "linear per token"]

    def construct(self):
        page(self)
        head = kicker("MAMBA, SCORED", "the same three axes")
        self.play(FadeIn(head, shift=UP * 0.2), run_time=0.9)

        rows = VGroup()
        for label, val in zip(self.ROWS, self.MAMBA):
            l = Text(label, font=SANS, font_size=25, color=INK_SOFT)
            t = Text(val, font=MONO, font_size=23, color=INK)
            box = RoundedRectangle(width=4.6, height=0.72, corner_radius=0.09,
                                   stroke_width=1.5, stroke_color=INK_SOFT,
                                   fill_opacity=0).move_to(t.get_center())
            rows.add(VGroup(l, VGroup(box, t)))
        lw = max(r[0].width for r in rows)
        for r in rows:
            r[1].next_to(r[0], RIGHT, buff=0.5 + (lw - r[0].width))
        rows.arrange(DOWN, buff=0.34, aligned_edge=LEFT)

        use = card("USE IT", "long sequences\ncompression\naudio · genomics", INK_SOFT,
                   width=4.3, title_size=25, body_size=20)
        careful = card("BE CAREFUL", "retrieval\nliteral recall\nfrom the context", TERRA,
                       width=4.3, title_size=25, body_size=20)
        advice = VGroup(use, careful).arrange(RIGHT, buff=0.55)

        fit(VGroup(rows, advice).arrange(DOWN, buff=0.55))

        for r in rows:
            self.play(FadeIn(r[0], shift=RIGHT * 0.18), Create(r[1][0]),
                      FadeIn(r[1][1]), run_time=0.8)
        self.wait(1.2)
        self.play(Create(use[0]), FadeIn(use[1], shift=UP * 0.12), run_time=1.5)
        self.play(Create(careful[0]), FadeIn(careful[1], shift=UP * 0.12), run_time=1.5)
        self.wait(1.0)

        point = spark("Cheap because it forgets")
        self.play(Write(point), run_time=1.7)
        self.wait(6.19)
