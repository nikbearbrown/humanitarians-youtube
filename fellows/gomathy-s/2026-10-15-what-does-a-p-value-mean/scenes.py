"""scenes.py — Manim scenes for p-value (16:9).

Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills
(GATE T §8.3; carried over from knowledge-cutoff and claude-liam-context-window).
Explicit font on every Text: EB Garamond. GHOST is for shapes only, never text.
Math is typeset with MathTex (docs/MATH-TYPESETTING.md), never a Text string.
B03, B04 and B06 are ILLUSTRATIVE (labelled on screen). Their numbers are
computed, not typed in by hand — see EXAMPLES below and FACTCHECK.md.
No slant=ITALIC on multi-word text (Pango collapses spaces).
Clip lengths match the measured audio (mp3/timings.json) within the
compiler's ±5% retime window.
"""
from math import comb, erfc, exp, sqrt

from manim import *

BG    = ManimColor("#FAF9F5")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all text and fills
SOFT  = ManimColor("#6E6A57")   # secondary text (>= 4.5:1 on cream)
GHOST = ManimColor("#A8A491")   # shapes only
CARD  = ManimColor("#FFFFFF")

SAFE_W = 12.4                   # usable width inside the 14.22-unit frame

# ---- EXAMPLES (executable evidence: the on-screen numbers come from here)
# B04: fair coin, 10 flips, one-sided tail P(X >= 9) = (C(10,9) + C(10,10)) / 2^10
COIN_TAIL = sum(comb(10, k) for k in (9, 10))          # 11
assert COIN_TAIL == 11 and abs(COIN_TAIL / 1024 - 0.0107) < 1e-4


def _two_group_p(diff, sd, n):
    """Two-sided normal-approx p for a difference in means, equal groups of n."""
    z = diff / (sd * sqrt(2 / n))
    return erfc(z / sqrt(2))


# B06: SD 10 in both studies. Huge: n=50,000/group, diff 0.2 → p ≈ 0.0016.
# Small: n=10/group, diff 5 → normal approx p ≈ 0.26; the t-test (df 18) gives
# 0.278, which is what the card shows (FACTCHECK.md).
assert abs(_two_group_p(0.2, 10, 50_000) - 0.0016) < 1e-4


def _label(text, size=32, color=None, weight=None, fit=True, max_w=SAFE_W):
    # Lay out at 4x then scale down: Pango kerning at small sizes collapses
    # word spaces; the big layout keeps them. Long lines at 4x wrap, so 2x there.
    m = 4 if len(text) * size < 1100 else 2
    kw = {"font_size": size * m, "color": color or INK, "font": "EB Garamond"}
    if weight:
        kw["weight"] = weight
    t = Text(text, **kw).scale(1 / m)
    if fit and t.width > max_w:
        t.scale_to_fit_width(max_w)
    return t


def _math(tex, size=64):
    return MathTex(tex, font_size=size, color=INK)


class B01_HesitantWriter(Scene):
    """Beat 2 BLUF, hesitant writer in Manim. 'A p-value is' / 'the chance
    you're right.' types in; the second line dims and backspaces out; 'how
    likely data this extreme is' / 'if there's no real effect.' types in its
    place. Ink only. ~6.2s (audio 6.17s, incl. 0.8s lead silence)."""

    def construct(self):
        self.camera.background_color = BG

        line1 = _label("A p-value is", size=64, fit=False)
        wrong = _label("the chance you're right.", size=64, fit=False)
        right = VGroup(_label("how likely data this extreme is", size=64, fit=False),
                       _label("if there's no real effect.", size=64, fit=False))
        allw = max(line1.width, wrong.width, *[t.width for t in right])
        k = min(1.0, 11.6 / allw)
        for t in (line1, wrong, *right):
            t.scale(k)
        gap = 0.45
        line1.move_to(UP * 1.1)
        wrong.next_to(line1, DOWN, buff=gap, aligned_edge=LEFT)
        right.arrange(DOWN, buff=gap, aligned_edge=LEFT)
        right.next_to(line1, DOWN, buff=gap, aligned_edge=LEFT)
        left_x = -allw * k / 2
        for t in (line1, wrong, right):
            t.shift(RIGHT * (left_x - t.get_left()[0]))
        # center the block on its final (three-line) state
        dy = -VGroup(line1, right).get_center()[1]
        for t in (line1, wrong, right):
            t.shift(UP * dy)

        self.wait(0.3)
        self.play(AddTextLetterByLetter(line1), run_time=0.5)
        self.play(AddTextLetterByLetter(wrong), run_time=0.6)
        self.wait(0.4)
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)
        self.play(RemoveTextLetterByLetter(wrong), run_time=0.4)
        self.play(AddTextLetterByLetter(right[0]), run_time=0.7)
        self.play(AddTextLetterByLetter(right[1]), run_time=0.6)
        self.wait(2.4)


class B03_TailShare(Scene):
    """ILLUSTRATIVE null distribution: a bell curve ('If the Null Is True'),
    'Your data' marked on its right side, the tail beyond it shaded ('At least
    this extreme'), and 'Shaded share = p-value'. No real data. ~6.1s
    (audio 6.12s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("If the Null Is True", size=44, weight="BOLD").move_to(UP * 2.9)
        meta = _label("ILLUSTRATIVE — a sketch, not real data", size=30, color=SOFT)
        meta.next_to(title, DOWN, buff=0.2)

        BASE, H, SX = -1.9, 3.0, 1.6           # baseline y, peak height, x scale
        X0 = 1.9                                 # observed statistic (in SD units)

        def pt(u):
            return [u * SX, BASE + H * exp(-u * u / 2), 0]

        curve = ParametricFunction(pt, t_range=[-3.5, 3.5], color=INK, stroke_width=5)
        base = Line([-3.6 * SX, BASE, 0], [3.6 * SX, BASE, 0], color=INK, stroke_width=3)

        tail_pts = [pt(X0 + i * (3.5 - X0) / 40) for i in range(41)]
        tail_pts += [[3.5 * SX, BASE, 0], [X0 * SX, BASE, 0]]
        tail = Polygon(*tail_pts, stroke_width=0, fill_color=INK, fill_opacity=0.35)

        mark = DashedLine([X0 * SX, BASE - 0.15, 0], [X0 * SX, BASE + 1.45, 0],
                          color=INK, stroke_width=4, dash_length=0.12)
        mark_lbl = _label("Your data", size=34, weight="BOLD").next_to(mark, DOWN, buff=0.15)

        ext_lbl = VGroup(_label("At least", size=34), _label("this extreme", size=34))
        ext_lbl.arrange(DOWN, buff=0.08).move_to([4.85, 0.05, 0])
        ext_arrow = Arrow(ext_lbl.get_bottom() + DOWN * 0.05, [4.0, BASE + 0.2, 0],
                          color=INK, stroke_width=4, buff=0.05,
                          max_tip_length_to_length_ratio=0.18)

        share = _label("Shaded share = p-value", size=42, weight="BOLD").move_to(DOWN * 2.95)

        self.play(Write(title), FadeIn(meta), run_time=0.6)
        self.play(Create(base), Create(curve), run_time=0.9)
        self.play(Create(mark), FadeIn(mark_lbl), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(tail), run_time=0.7)
        self.play(FadeIn(ext_lbl), GrowArrow(ext_arrow), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(share, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)


class B04_CoinFlips(Scene):
    """ILLUSTRATIVE worked example: ten coin tiles (nine H, one T), then the
    typeset one-sided tail P(X >= 9) = 11/1024 ≈ 0.011 and 'About 1%, if the
    coin is fair'. ~4.1s (audio 4.06s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Is This Coin Fair?", size=44, weight="BOLD").move_to(UP * 2.9)
        meta = _label("ILLUSTRATIVE", size=30, color=SOFT).next_to(title, DOWN, buff=0.2)

        faces = "HHHHHHTHHH"
        coins = VGroup()
        for f in faces:
            ring = Circle(radius=0.45, color=INK if f == "H" else GHOST, stroke_width=4,
                          fill_color=CARD, fill_opacity=1)
            letter = _label(f, size=40, weight="BOLD", color=INK if f == "H" else SOFT)
            coins.add(VGroup(ring, letter.move_to(ring)))
        coins.arrange(RIGHT, buff=0.18).move_to(UP * 0.95)

        caption = _label("10 flips, 9 heads.  X = number of heads.", size=32, color=SOFT)
        caption.move_to(DOWN * 0.15)
        eq = MathTex(r"P(X \ge 9) =", r"\frac{11}{1024}", r"\approx 0.011",
                     font_size=68, color=INK).move_to(DOWN * 1.45)
        ring = RoundedRectangle(width=eq[2].width + 0.32, height=eq[2].height + 0.32,
                                corner_radius=0.1, color=INK, stroke_width=4).move_to(eq[2])
        about = _label("About 1%, if the coin is fair", size=40, weight="BOLD").move_to(DOWN * 2.85)

        self.play(Write(title), FadeIn(meta), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, scale=0.8) for c in coins], lag_ratio=0.12), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.3)
        self.play(Write(eq), run_time=0.8)
        self.wait(0.3)
        self.play(Create(ring), FadeIn(about, shift=UP * 0.1), run_time=0.45)
        self.wait(0.9)


class B06_TwoStudies(Scene):
    """ILLUSTRATIVE counter-example, side by side: 'Huge study' (50,000 per
    group, effect 0.2 points, p ≈ 0.002) vs 'Small study' (10 per group,
    effect 5 points, p ≈ 0.28). SD 10 in both. ~5.9s (audio 5.93s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("A Small p Isn't a Big Effect", size=44, weight="BOLD").move_to(UP * 2.9)
        meta = _label("ILLUSTRATIVE — two groups compared, SD 10", size=34, color=SOFT)
        meta.next_to(title, DOWN, buff=0.2)

        def card(head, n, effect, ptex, x):
            body = VGroup(
                _label(head, size=44, weight="BOLD"),
                _label(n, size=34, color=SOFT),
                _label(effect, size=38),
                _math(ptex, size=64),
            ).arrange(DOWN, buff=0.28)
            frame = RoundedRectangle(width=5.6, height=4.0, corner_radius=0.18, color=INK,
                                     stroke_width=3.5)
            return VGroup(frame, body.move_to(frame)).move_to([x, -0.8, 0])

        left = card("Huge study", "50,000 per group", "Effect: 0.2 points", r"p \approx 0.002", -3.15)
        right = card("Small study", "10 per group", "Effect: 5 points", r"p \approx 0.28", 3.15)

        def underline(c):                    # under the card's p-value
            m = c[1][-1]
            return Line(m.get_corner(DL) + DOWN * 0.06, m.get_corner(DR) + DOWN * 0.06,
                        color=INK, stroke_width=4)

        # both card outlines from the start (comparison frame, fills the canvas);
        # each card's contents land on its own sentence; each p-value is
        # underlined on its spoken 'tiny p' (~2.0s) / 'large p' (~4.9s)
        self.play(Write(title), FadeIn(meta), Create(left[0]), Create(right[0]), run_time=0.4)
        self.play(FadeIn(left[1], shift=UP * 0.15), run_time=0.6)
        self.wait(1.0)
        self.play(Create(underline(left)), run_time=0.4)
        self.wait(0.6)                       # second sentence starts at 3.04s
        self.play(FadeIn(right[1], shift=UP * 0.15), run_time=0.6)
        self.wait(1.3)
        self.play(Create(underline(right)), run_time=0.4)
        self.wait(0.63)
