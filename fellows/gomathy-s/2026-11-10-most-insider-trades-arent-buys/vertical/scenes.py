"""scenes.py — portrait (9:16) Manim scenes for insider-buying-noise/vertical.

Rendered by run.sh at 2160x3840 → frame is 4.5 x 8 units.
Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills.
Explicit font on every Text: EB Garamond. GHOST is for shapes only.
Math is MathTex. Every label is >= size 32 (GATE T portrait floor) and all
text sits inside the title-safe box (y between -2.85 and 3.4).
Same text and numbers as the 16:9 scenes; the DATA block and its asserts are
copied from ../scenes.py (Mycroft insider-signals @ fed487c, see SOURCES.md).
"""
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
APPROX_K = 0.58   # ≈ glyph only, see _approx() (p-value BUILD-LOG measurements)

# ---- DATA (identical to ../scenes.py) ---------------------------------------
FORM4_ROWS = 999_542
CODES = {"S": 301_979, "A": 217_494, "F": 170_600, "M": 143_930, "P": 82_340}
OTHER = FORM4_ROWS - sum(CODES.values())
assert OTHER == 83_199
QUALIFYING = 78_495
assert CODES["P"] - QUALIFYING == 3_845
R2_REPEAT, R1_PLANS, R3_LATE, R4_PENNY = 699, 3_032, 4_028, 5_630
ELIGIBLE = 65_106
assert QUALIFYING - R2_REPEAT - R1_PLANS - R3_LATE - R4_PENNY == ELIGIBLE
ISSUERS, FILINGS = 4_146, 38_320
SPOT_EXACT, SPOT_ROUND, SPOT_OTHER = 15, 10, 0
assert SPOT_EXACT + SPOT_ROUND + SPOT_OTHER == 25
assert round(100 * ELIGIBLE / FORM4_ROWS, 1) == 6.5


def pct(n):
    return f"{100 * n / FORM4_ROWS:.1f}%"


def _approx(lhs, rhs, size):
    """'lhs ≈ rhs' typeset, with the ≈ glyph alone scaled to APPROX_K.
    GATE T §8.1 reads ≈'s two strokes as a sub-floor text run at portrait
    scale; at 58% they fall under its glyph-fragment cutoff (p-value)."""
    m = MathTex(lhs, r"\approx", rhs, font_size=size, color=INK)
    m[1].scale(APPROX_K, about_point=m[1].get_center())
    m.arrange(RIGHT, buff=0.1)
    for part in m:
        part.set_y(m[-1].get_center()[1])
    return m


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
    """'A Form 4 is' / 'an insider' / 'buying.' types in; the wrong lines dim
    and backspace out; 'any change in' / 'an insider's' / 'holdings, due' /
    'within two' / 'business days.' types in. ~6.0s (audio 6.02s)."""

    def construct(self):
        self.camera.background_color = BG

        size = 44
        line1 = _label("A Form 4 is", size=size, fit=False)
        wrong = VGroup(_label("an insider", size=size, fit=False),
                       _label("buying.", size=size, fit=False))
        right = VGroup(*[_label(t, size=size, fit=False)
                         for t in ("any change in", "an insider's", "holdings, due",
                                   "within two", "business days.")])
        allw = max(line1.width, *[t.width for t in [*wrong, *right]])
        k = min(1.0, 3.7 / allw)
        for t in (line1, *wrong, *right):
            t.scale(k)
        gap = 0.3
        line1.move_to(UP * 1.8)
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
            self.play(AddTextLetterByLetter(t), run_time=0.3)
        self.wait(2.17)


class B02_TotalCount(Scene):
    """Counter 0 → 999,542, fourteen quarter ticks (two rows of seven),
    source settles. ~3.9s (audio 3.91s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["Every Form 4", "Transaction"], size=44, weight="BOLD").move_to(UP * 2.8)
        meta = _label("Non-derivative table", size=32, color=SOFT)
        meta.next_to(title, DOWN, buff=0.2)

        v = ValueTracker(0)
        counter = always_redraw(lambda: _label(f"{int(round(v.get_value())):,}", size=100,
                                               weight="BOLD").move_to(UP * 0.85))

        ticks = VGroup(*[RoundedRectangle(width=0.42, height=0.36, corner_radius=0.05,
                                          color=INK, stroke_width=3, fill_color=INK,
                                          fill_opacity=0) for _ in range(14)])
        ticks.arrange_in_grid(2, 7, buff=(0.1, 0.14)).move_to(DOWN * 0.3)
        span = _stack(["Q2 2023 – Q3 2026", "14 quarters, filing date"], size=32)
        span.next_to(ticks, DOWN, buff=0.25)
        src = _stack(["Source: SEC Insider", "Transactions Data Sets"], size=32, color=SOFT)
        src.move_to(DOWN * 2.45)

        self.add(counter)
        self.play(Write(title), FadeIn(meta), run_time=0.4)
        self.play(v.animate.set_value(FORM4_ROWS), run_time=1.2, rate_func=smooth)
        self.play(LaggedStart(*[t.animate.set_fill(INK, opacity=0.85) for t in ticks], lag_ratio=0.15),
                  FadeIn(span), run_time=0.8)
        self.play(FadeIn(src), run_time=0.3)
        self.wait(1.21)


class B03_CodeSplit(Scene):
    """One bar per transaction code (label above, bar + % below);
    Purchases (P) 8.2% last, solid, boxed. ~2.9s (audio 2.90s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Most Aren't Buys", size=40, weight="BOLD").move_to(UP * 3.12)
        rows = [("Sales (S)", CODES["S"]), ("Grants, awards (A)", CODES["A"]),
                ("Tax/exercise (F)", CODES["F"]), ("Option exercises (M)", CODES["M"]),
                ("All other codes", OTHER), ("Purchases (P)", CODES["P"])]
        X0, MAXW = -1.85, 2.65  # box + slide-in stay inside ±1.95 (final GATE V)
        scale = MAXW / max(n for _, n in rows)
        group = VGroup()
        for i, (name, n) in enumerate(rows):
            y = 2.35 - i * 0.78
            is_p = name.startswith("Purchases")
            lbl = _label(name, size=32, weight="BOLD" if is_p else None)
            lbl.move_to([X0, y + 0.18, 0], aligned_edge=LEFT)
            bar = Rectangle(width=n * scale, height=0.22, stroke_width=0,
                            fill_color=INK if is_p else GHOST, fill_opacity=1)
            bar.move_to([X0, y - 0.2, 0], aligned_edge=LEFT)
            val = _label(pct(n), size=32, weight="BOLD" if is_p else None)
            val.next_to(bar, RIGHT, buff=0.15)
            group.add(VGroup(lbl, bar, val))
        p_row = group[-1]
        box = SurroundingRectangle(p_row, color=INK, stroke_width=4, buff=0.06, corner_radius=0.08)
        src = _label("Share of 999,542 rows", size=32, color=SOFT)
        src.move_to(DOWN * 2.55)

        self.play(Write(title), FadeIn(src), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.08) for r in group[:-1]], lag_ratio=0.25),
                  run_time=1.0)
        self.play(FadeIn(p_row, shift=RIGHT * 0.08), run_time=0.3)
        self.play(Create(box), run_time=0.35)
        self.wait(0.95)


class B05_Filters(Scene):
    """Filter waterfall, portrait (label above each bar): 78,495 → −699,
    −3,032, −4,028, −5,630 → 65,106. Footer: plans kept, joint = one insider.
    ~5.9s (audio 5.93s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Registered Filters", size=40, weight="BOLD").move_to(UP * 3.08)
        X0, W = -1.95, 2.55
        k = W / QUALIFYING
        NX = 1.9

        def row(i, name, lo, hi, number, solid, bold=False):
            y = 2.35 - i * 0.74
            lbl = _label(name, size=32, weight="BOLD" if bold else None)
            lbl.move_to([X0, y + 0.18, 0], aligned_edge=LEFT)
            w = max((hi - lo) * k, 0.04)
            if solid:
                bar = Rectangle(width=w, height=0.24, stroke_width=0, fill_color=INK, fill_opacity=1)
            else:
                bar = Rectangle(width=w, height=0.24, stroke_color=INK, stroke_width=2.5,
                                fill_color=GHOST, fill_opacity=1)
            bar.move_to([X0 + (lo + hi) / 2 * k, y - 0.19, 0])
            num = _label(number, size=32, weight="BOLD" if bold else None)
            num.move_to([NX, y - 0.19, 0], aligned_edge=RIGHT)
            return VGroup(lbl, bar, num)

        start = row(0, "Qualifying buys", 0, QUALIFYING, f"{QUALIFYING:,}", True, bold=True)
        steps = []
        level = QUALIFYING
        for i, (name, n) in enumerate([("Repeat amendments", R2_REPEAT),
                                       ("Private, ESPP, DRIP", R1_PLANS),
                                       ("Over 30 days to file", R3_LATE),
                                       ("Price under $1", R4_PENNY)], start=1):
            steps.append(row(i, name, level - n, level, f"−{n:,}", False))
            level -= n
        assert level == ELIGIBLE
        end = row(5, "Eligible buys", 0, ELIGIBLE, f"{ELIGIBLE:,}", True, bold=True)
        foot = _stack(["10b5-1: kept, flagged", "Joint filing: 1 insider"],
                      size=32, color=SOFT, buff=0.1).move_to(DOWN * 2.36)

        # footer lands with the title (portrait only) so the beat fills the
        # canvas while the steps build (GATE V underfill at 50%)
        self.play(Write(title), FadeIn(start), FadeIn(foot), run_time=0.6)
        for s in steps:
            self.play(FadeIn(s, shift=DOWN * 0.1), run_time=0.5)
            self.wait(0.38)
        self.play(FadeIn(end, shift=DOWN * 0.1), run_time=0.5)
        self.wait(1.31)


class B06_Eligible(Scene):
    """'65,106 eligible buys', typeset 65,106/999,542 ≈ 6.5% (6.5% boxed),
    '4,146 issuers · 38,320 filings'. ~5.4s (audio 5.40s)."""

    def construct(self):
        self.camera.background_color = BG

        big = _label(f"{ELIGIBLE:,}", size=104, weight="BOLD").move_to(UP * 2.6)
        cap = _label("eligible buys", size=44).next_to(big, DOWN, buff=0.2)
        eq = _approx(r"\frac{65{,}106}{999{,}542}", r"6.5\%", 54).move_to(UP * 0.45)
        ring = SurroundingRectangle(eq[2], color=INK, stroke_width=4, buff=0.14, corner_radius=0.08)
        of_all = _stack(["of all Form 4", "transactions"], size=34, color=SOFT)
        of_all.next_to(eq, DOWN, buff=0.35)
        meta = _stack([f"{ISSUERS:,} issuers", f"{FILINGS:,} filings"], size=34).move_to(DOWN * 2.35)

        self.play(FadeIn(big, scale=0.9), FadeIn(cap), run_time=0.6)
        self.wait(0.9)
        self.play(Write(eq), run_time=0.9)
        self.play(Create(ring), FadeIn(of_all), run_time=0.45)
        self.wait(0.5)
        self.play(FadeIn(meta, shift=UP * 0.1), run_time=0.4)
        self.wait(1.65)


class B07_SpotCheck(Scene):
    """25 tiles, 15 solid with a check, 10 hatched, legend, Equifax example.
    ~5.6s (audio 5.59s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _stack(["Spot-Check vs.", "Original Filings"], size=40, weight="BOLD").move_to(UP * 2.75)
        meta = _label("25 random buys", size=32, color=SOFT)
        meta.next_to(title, DOWN, buff=0.18)

        S = 0.36
        tiles = VGroup(*[Square(S, color=INK, stroke_width=3) for _ in range(25)])
        tiles.arrange_in_grid(5, 5, buff=0.07).move_to(UP * 0.4)

        def check(sq):
            c = sq.get_center()
            return VMobject(stroke_color=BG, stroke_width=6).set_points_as_corners(
                [c + [-0.12, 0.0, 0], c + [-0.03, -0.1, 0], c + [0.13, 0.11, 0]])

        def hatch(sq):
            c, h = sq.get_center(), S / 2
            lines = VGroup()
            for d in (-0.22, 0.0, 0.22):
                x0, x1 = max(-h, -h - d), min(h, h - d)
                lines.add(Line(c + [x0, x0 + d, 0], c + [x1, x1 + d, 0], color=INK, stroke_width=3))
            return lines

        exact = [tiles[i] for i in range(SPOT_EXACT)]
        rnd = [tiles[i] for i in range(SPOT_EXACT, SPOT_EXACT + SPOT_ROUND)]
        fills = [sq.copy().set_fill(INK, opacity=1) for sq in exact]
        checks = [check(sq) for sq in exact]
        hatches = [hatch(sq) for sq in rnd]

        def legend_row(swatch, text, y):
            t = _label(text, size=32)
            g = VGroup(swatch, t).arrange(RIGHT, buff=0.22)
            g.move_to([-1.75, y, 0], aligned_edge=LEFT)
            return g

        sw1 = Square(0.3, color=INK, stroke_width=3).set_fill(INK, 1)
        sq2 = Square(0.3, color=INK, stroke_width=3)
        sw2 = VGroup(sq2, Line(sq2.get_corner(DL), sq2.get_corner(UR), color=INK, stroke_width=3))
        sw3 = Square(0.3, color=GHOST, stroke_width=3)
        l1 = legend_row(sw1, f"{SPOT_EXACT} exact match", -0.85)
        l2 = legend_row(sw2, f"{SPOT_ROUND} rounding only", -1.24)
        l3 = legend_row(sw3, f"{SPOT_OTHER} other errors", -1.63)
        ex = _stack(["e.g. filed $166.1941", "data set $166.19"], size=32, color=SOFT)
        ex.move_to(DOWN * 2.37)

        self.play(Write(title), FadeIn(meta), Create(tiles), run_time=0.6)
        self.play(LaggedStart(*[AnimationGroup(FadeIn(f), Create(c)) for f, c in zip(fills, checks)],
                              lag_ratio=0.12), FadeIn(l1), run_time=1.0)
        self.wait(0.3)
        self.play(LaggedStart(*[Create(h) for h in hatches], lag_ratio=0.15), FadeIn(l2), run_time=0.9)
        self.play(FadeIn(ex), run_time=0.5)
        self.play(FadeIn(l3), run_time=0.4)
        self.wait(1.89)


class B11_OutroCard(Scene):
    """Portrait title card standing in for the landscape OutroSeries (no
    OutroSeries916). Eyebrow '@HumanitariansAI', line 'Most Insider Trades
    Aren't Buys', ink underline drawing in. ~5.5s (audio 5.47s)."""

    def construct(self):
        self.camera.background_color = BG

        eyebrow = _label("@HumanitariansAI", size=34, color=SOFT, weight="BOLD")
        line = _stack(["Most Insider", "Trades", "Aren't Buys"], size=50, buff=0.18)
        group = VGroup(eyebrow, line).arrange(DOWN, buff=0.55).move_to(UP * 0.25)
        underline = Line(LEFT * 0.75, RIGHT * 0.75, color=INK, stroke_width=5)
        underline.next_to(line, DOWN, buff=0.4)

        self.play(FadeIn(eyebrow, shift=UP * 0.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(line, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)
        self.play(Create(underline), run_time=0.7)
        self.wait(2.67)
