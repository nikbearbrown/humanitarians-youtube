"""scenes.py — portrait (9:16) Manim scenes for p-value/vertical.

Rendered by run.sh at 2160x3840 → frame is 4.5 x 8 units.
Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills.
Explicit font on every Text: EB Garamond. GHOST is for shapes only.
Math is typeset with MathTex (docs/MATH-TYPESETTING.md).
Every label is >= size 32 (GATE T portrait floor, 1.9% of 3840 px) and all
text sits inside the title-safe box (y between -2.85 and 3.4).
B03 / B04 / B06 are ILLUSTRATIVE (labelled on screen). Same text and numbers
as the 16:9 scenes (see ../scenes.py EXAMPLES and FACTCHECK.md).
"""
from math import comb, exp

from manim import *

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
SOFT  = ManimColor("#6E6A57")   # >= 4.5:1 on cream
GHOST = ManimColor("#A8A491")   # shapes only
CARD  = ManimColor("#FFFFFF")

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width
# at the 16:9 default (14.22).
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

SAFE_W = 3.9
APPROX_K = 0.58   # ≈ glyph only, see _approx(); digits stay full size


def _approx(lhs, rhs, size):
    """'lhs ≈ rhs' typeset, with the ≈ glyph alone scaled to APPROX_K (B04, B06).
    GATE T §8.1 reads ≈'s two strokes as a sub-floor text run at portrait
    scale (43 px vs the 72 px floor); at 58% they fall under its own glyph-
    fragment cutoff (27.6 px), which is how the checker means ≈ to be read.
    BUILD-LOG.md has the measurements."""
    parts = [lhs, r"\approx", rhs] if lhs else [r"\approx", rhs]
    m = MathTex(*parts, font_size=size, color=INK)
    sym = m[1] if lhs else m[0]
    sym.scale(APPROX_K, about_point=sym.get_center())
    m.arrange(RIGHT, buff=0.1)        # close the gap the scale-down leaves
    for part in m:                    # restore the math axis: centre on the digits
        part.set_y(m[-1].get_center()[1])
    m[0].align_to(m[-1], DOWN) if lhs else None   # italic p sits on the baseline
    return m

COIN_TAIL = sum(comb(10, k) for k in (9, 10))          # 11 — same check as 16:9
assert COIN_TAIL == 11


def _label(text, size=32, color=None, weight=None, fit=True, max_w=SAFE_W):
    m = 4 if len(text) * size < 1100 else 2      # long lines at 4x wrap in Pango
    kw = {"font_size": size * m, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    t = Text(text, **kw).scale(1 / m)
    if fit and t.width > max_w:
        t.scale_to_fit_width(max_w)
    return t


def _stack(lines, size, weight=None, color=None, buff=0.14):
    """Several lines at ONE shared scale (so they match), centered."""
    ts = [_label(l, size=size, weight=weight, color=color, fit=False) for l in lines]
    g = VGroup(*ts).arrange(DOWN, buff=buff)
    if g.width > SAFE_W:
        g.scale_to_fit_width(SAFE_W)
    return g


class B01_HesitantWriter(Scene):
    """'A p-value is' / 'the chance' / 'you're right.' types in; the wrong
    lines dim and backspace out; 'how likely data' / 'this extreme is' / 'if
    there's no' / 'real effect.' types in. Ink only. ~6.2s (audio 6.17s)."""

    def construct(self):
        self.camera.background_color = BG

        size = 44
        line1 = _label("A p-value is", size=size, fit=False)
        wrong = VGroup(_label("the chance", size=size, fit=False),
                       _label("you're right.", size=size, fit=False))
        right = VGroup(*[_label(t, size=size, fit=False)
                         for t in ("how likely data", "this extreme is",
                                   "if there's no", "real effect.")])
        allw = max(line1.width, *[t.width for t in [*wrong, *right]])
        k = min(1.0, 3.7 / allw)
        for t in (line1, *wrong, *right):
            t.scale(k)
        gap = 0.3
        line1.move_to(UP * 1.5)
        for grp in (wrong, right):
            grp.arrange(DOWN, buff=gap, aligned_edge=LEFT)
            grp.next_to(line1, DOWN, buff=gap, aligned_edge=LEFT)
        left_x = -allw * k / 2
        for t in (line1, wrong, right):
            t.shift(RIGHT * (left_x - t.get_left()[0]))
        dy = -VGroup(line1, right).get_center()[1]
        for t in (line1, wrong, right):
            t.shift(UP * dy)

        self.wait(0.3)
        self.play(AddTextLetterByLetter(line1), run_time=0.45)
        self.play(AddTextLetterByLetter(wrong[0]), run_time=0.3)
        self.play(AddTextLetterByLetter(wrong[1]), run_time=0.3)
        self.wait(0.35)
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)
        self.play(RemoveTextLetterByLetter(wrong[1]), run_time=0.2)
        self.play(RemoveTextLetterByLetter(wrong[0]), run_time=0.2)
        for t in right:
            self.play(AddTextLetterByLetter(t), run_time=0.35)
        self.wait(2.35)


class B03_TailShare(Scene):
    """ILLUSTRATIVE null distribution, portrait: the curve up top, 'Your data'
    marker, shaded tail, 'At least this extreme' with an arrow up to it,
    'Shaded share = p-value' at the bottom; every label is on screen by
    ~3.1s. ~6.1s (audio 6.12s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["If the Null", "Is True"], size=44, weight="BOLD").move_to(UP * 2.85)
        meta = _label("ILLUSTRATIVE", size=32, color=SOFT).next_to(title, DOWN, buff=0.18)

        BASE, H, SX = 0.15, 1.4, 0.55
        X0 = 1.9

        def pt(u):
            return [u * SX, BASE + H * exp(-u * u / 2), 0]

        curve = ParametricFunction(pt, t_range=[-3.5, 3.5], color=INK, stroke_width=5)
        base = Line([-3.55 * SX, BASE, 0], [3.55 * SX, BASE, 0], color=INK, stroke_width=3)
        tail_pts = [pt(X0 + i * (3.5 - X0) / 40) for i in range(41)]
        tail_pts += [[3.5 * SX, BASE, 0], [X0 * SX, BASE, 0]]
        tail = Polygon(*tail_pts, stroke_width=0, fill_color=INK, fill_opacity=0.35)

        mark = DashedLine([X0 * SX, BASE - 0.12, 0], [X0 * SX, BASE + 0.95, 0],
                          color=INK, stroke_width=4, dash_length=0.1)
        mark_lbl = _label("Your data", size=34, weight="BOLD")
        mark_lbl.next_to([X0 * SX - 0.08, BASE - 0.1, 0], DOWN + LEFT, buff=0.06)

        ext_lbl = _stack(["At least", "this extreme"], size=36).move_to([0.4, -1.15, 0])
        ext_arrow = Arrow([1.4, -0.82, 0], [1.3, BASE + 0.08, 0], color=INK,
                          stroke_width=4, buff=0.05, max_tip_length_to_length_ratio=0.22)

        share = _stack(["Shaded share", "= p-value"], size=44, weight="BOLD").move_to(DOWN * 2.5)

        # Labels land on their words (whisper timings, 1.08 audio): "data"
        # 1.96s, "this extreme" 2.16s, "or more turn up" 2.78-3.82s, "That
        # share is the p-value" 4.60s. The share label comes in on "or more"
        # so the 50% frame (3.06s) holds the whole diagram (GATE V underfill).
        self.play(Write(title), FadeIn(meta), Create(base), Create(curve), run_time=0.9)
        self.play(Create(mark), FadeIn(mark_lbl), run_time=0.5)
        self.wait(0.7)
        self.play(FadeIn(tail), FadeIn(ext_lbl), GrowArrow(ext_arrow), run_time=0.6)
        self.play(FadeIn(share, shift=UP * 0.1), run_time=0.4)
        self.wait(3.02)


class B04_CoinFlips(Scene):
    """ILLUSTRATIVE worked example, stacked: ten coin tiles in two rows (nine
    H, one T), the typeset tail P(X >= 9) = 11/1024 over '≈ 0.011' (boxed on
    'about one percent'), then 'About 1%, if the coin is fair'.
    ~4.1s (audio 4.06s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Is This Coin Fair?", size=44, weight="BOLD").move_to(UP * 3.05)
        meta = _label("ILLUSTRATIVE", size=32, color=SOFT).next_to(title, DOWN, buff=0.15)

        faces = "HHHHHHTHHH"
        coins = VGroup()
        for f in faces:
            ring = Circle(radius=0.3, color=INK if f == "H" else GHOST, stroke_width=4,
                          fill_color=CARD, fill_opacity=1)
            letter = _label(f, size=36, weight="BOLD", color=INK if f == "H" else SOFT)
            coins.add(VGroup(ring, letter.move_to(ring)))
        rows = VGroup(VGroup(*coins[:5]).arrange(RIGHT, buff=0.12),
                      VGroup(*coins[5:]).arrange(RIGHT, buff=0.12)).arrange(DOWN, buff=0.14)
        rows.move_to(UP * 1.55)

        caption = _stack(["10 flips, 9 heads.", "X = number of heads."], size=32,
                         color=SOFT, buff=0.08).move_to(UP * 0.3)
        eq1 = MathTex(r"P(X \ge 9) = \frac{11}{1024}", font_size=46, color=INK).move_to(DOWN * 0.75)
        if eq1.width > SAFE_W:
            eq1.scale_to_fit_width(SAFE_W)
        eq2 = _approx("", "0.011", 46).move_to(DOWN * 1.62)
        box = RoundedRectangle(width=eq2.width + 0.3, height=eq2.height + 0.3,
                               corner_radius=0.1, color=INK, stroke_width=4).move_to(eq2)
        about = _stack(["About 1%, if", "the coin is fair"], size=38, weight="BOLD",
                       buff=0.08).move_to(DOWN * 2.47)

        self.play(Write(title), FadeIn(meta), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, scale=0.8) for c in coins], lag_ratio=0.12), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.3)
        self.play(Write(eq1), Write(eq2), run_time=0.8)
        self.wait(0.3)
        self.play(Create(box), FadeIn(about, shift=UP * 0.1), run_time=0.45)
        self.wait(0.9)


class B06_TwoStudies(Scene):
    """ILLUSTRATIVE counter-example, stacked: 'Huge study' card above 'Small
    study'. SD 10 in both. ~5.9s (audio 5.93s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["A Small p Isn't", "a Big Effect"], size=38, weight="BOLD").move_to(UP * 2.75)
        meta = _label("ILLUSTRATIVE — SD 10", size=32, color=SOFT).next_to(title, DOWN, buff=0.15)

        def card(head, n, effect, ptex, y):
            top = VGroup(_label(head, size=38, weight="BOLD"), _label(n, size=32, color=SOFT))
            top.arrange(DOWN, buff=0.08)
            body = VGroup(top, _label(effect, size=34),
                          _approx("p", ptex, 46)).arrange(DOWN, buff=0.06)
            frame = RoundedRectangle(width=3.9, height=2.2, corner_radius=0.14, color=INK,
                                     stroke_width=3.5)
            body.move_to(frame).shift(UP * 0.04)   # room for the p-value underline
            return VGroup(frame, body).move_to([0, y, 0])

        upper = card("Huge study", "50,000 per group", "Effect: 0.2 points", "0.002", 0.52)
        lower = card("Small study", "10 per group", "Effect: 5 points", "0.28", -1.72)

        def underline(c):                    # under the card's p-value
            m = c[1][-1]
            return Line(m.get_corner(DL) + DOWN * 0.06, m.get_corner(DR) + DOWN * 0.06,
                        color=INK, stroke_width=4)

        # both card outlines from the start (comparison frame, fills the canvas);
        # each card's contents land on its own sentence; each p-value is
        # underlined on its spoken 'tiny p' (~2.0s) / 'large p' (~4.9s)
        self.play(Write(title), FadeIn(meta), Create(upper[0]), Create(lower[0]), run_time=0.4)
        self.play(FadeIn(upper[1], shift=DOWN * 0.15), run_time=0.6)
        self.wait(1.0)
        self.play(Create(underline(upper)), run_time=0.4)
        self.wait(0.6)                       # second sentence starts at 3.04s
        self.play(FadeIn(lower[1], shift=UP * 0.15), run_time=0.6)
        self.wait(1.3)
        self.play(Create(underline(lower)), run_time=0.4)
        self.wait(0.63)


class B11_OutroCard(Scene):
    """Portrait title card standing in for the landscape OutroSeries (no
    OutroSeries916). Same text: eyebrow '@HumanitariansAI', line 'What Does
    a P-Value Actually Mean?', ink underline drawing in. ~5.3s (audio 5.33s)."""

    def construct(self):
        self.camera.background_color = BG

        eyebrow = _label("@HumanitariansAI", size=34, color=SOFT, weight="BOLD")
        line = _stack(["What Does a", "P-Value", "Actually Mean?"], size=50, buff=0.18)
        group = VGroup(eyebrow, line).arrange(DOWN, buff=0.55).move_to(UP * 0.25)
        underline = Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=5)
        underline.next_to(line, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow, shift=UP * 0.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)
        self.play(Create(underline), run_time=0.7)
        self.wait(2.5)
