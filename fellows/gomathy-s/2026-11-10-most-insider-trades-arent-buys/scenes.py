"""scenes.py — Manim scenes for insider-buying-noise (16:9).

Palette: cream #FAF9F5, ink #3D3929. INK ONLY — no terracotta text or fills
(GATE T §8.3; carried over from p-value). Explicit font on every Text: EB
Garamond. GHOST is for shapes only, never text. Math is MathTex.
Every on-screen number is a constant below, copied from the committed Mycroft
audit files (mycroft-work commit fed487c) and cross-checked by asserts; see
SOURCES.md for the file each one comes from. No returns, prices-as-outcomes or
performance numbers appear anywhere (none have been computed).
Clip lengths match mp3/timings.json within the compiler's ±5% retime window.
"""
from manim import *

BG    = ManimColor("#FAF9F5")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — all text and fills
SOFT  = ManimColor("#6E6A57")   # secondary text (>= 4.5:1 on cream)
GHOST = ManimColor("#A8A491")   # shapes only
CARD  = ManimColor("#FFFFFF")

SAFE_W = 12.4                   # usable width inside the 14.22-unit frame

# ---- DATA (Mycroft insider-signals @ fed487c) -------------------------------
# Sum of the 14 data/raw/parsed/<q>_parse_summary.json files, 2023q2–2026q3.
FORM4_ROWS = 999_542
CODES = {"S": 301_979, "A": 217_494, "F": 170_600, "M": 143_930, "P": 82_340}
OTHER = FORM4_ROWS - sum(CODES.values())
assert OTHER == 83_199
QUALIFYING = 78_495                       # code P rows passing every parse check
assert CODES["P"] - QUALIFYING == 3_845
assert 3_296 + 284 + 250 + 11 + 4 == 3_845  # parse-summary failure reasons
# data/verified/conformance-audit.md, "All" row + the note under it.
R2_REPEAT, R1_PLANS, R3_LATE, R4_PENNY = 699, 3_032, 4_028, 5_630
ELIGIBLE = 65_106
assert QUALIFYING - R2_REPEAT - R1_PLANS - R3_LATE - R4_PENNY == ELIGIBLE
ISSUERS, FILINGS = 4_146, 38_320
# Spot-check (conformance-audit.md / status.md): 25 random buys vs filing XML.
SPOT_EXACT, SPOT_ROUND, SPOT_OTHER = 15, 10, 0
assert SPOT_EXACT + SPOT_ROUND + SPOT_OTHER == 25
assert round(100 * ELIGIBLE / FORM4_ROWS, 1) == 6.5
assert round(100 * CODES["P"] / FORM4_ROWS, 1) == 8.2


def pct(n):
    return f"{100 * n / FORM4_ROWS:.1f}%"


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


class B01_HesitantWriter(Scene):
    """Beat 2 BLUF, hesitant writer. 'A Form 4 is' / 'an insider buying.'
    types in; the second line dims and backspaces out; 'any change in an
    insider's holdings,' / 'due within two business days.' types in its place.
    Ink only. ~6.0s (audio 6.02s, incl. 0.8s lead silence)."""

    def construct(self):
        self.camera.background_color = BG

        line1 = _label("A Form 4 is", size=64, fit=False)
        wrong = _label("an insider buying.", size=64, fit=False)
        right = VGroup(_label("any change in an insider's holdings,", size=64, fit=False),
                       _label("due within two business days.", size=64, fit=False))
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
        dy = -VGroup(line1, right).get_center()[1]
        for t in (line1, wrong, right):
            t.shift(UP * dy)

        self.wait(0.3)
        self.play(AddTextLetterByLetter(line1), run_time=0.5)
        self.play(AddTextLetterByLetter(wrong), run_time=0.6)
        self.wait(0.4)
        self.play(wrong.animate.set_color(SOFT), run_time=0.25)
        self.play(RemoveTextLetterByLetter(wrong), run_time=0.4)
        self.play(AddTextLetterByLetter(right[0]), run_time=0.8)
        self.play(AddTextLetterByLetter(right[1]), run_time=0.7)
        self.wait(2.07)


class B02_TotalCount(Scene):
    """'Every Form 4 Transaction': a counter rolls 0 → 999,542, fourteen
    quarter ticks light (filed Apr 2023 – Sep 2026), source line settles.
    ~3.9s (audio 3.91s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Every Form 4 Transaction", size=44, weight="BOLD").move_to(UP * 2.9)
        meta = _label("Non-derivative table · Form 4 only", size=32, color=SOFT)
        meta.next_to(title, DOWN, buff=0.2)

        v = ValueTracker(0)
        counter = always_redraw(lambda: _label(f"{int(round(v.get_value())):,}", size=140,
                                               weight="BOLD").move_to(UP * 0.55))

        ticks = VGroup(*[RoundedRectangle(width=0.62, height=0.42, corner_radius=0.06,
                                          color=INK, stroke_width=3, fill_color=INK,
                                          fill_opacity=0) for _ in range(14)])
        ticks.arrange(RIGHT, buff=0.14).move_to(DOWN * 1.25)
        t_left = _label("Q2 2023", size=32, color=SOFT).next_to(ticks[0], DOWN, buff=0.18)
        t_right = _label("Q3 2026", size=32, color=SOFT).next_to(ticks[-1], DOWN, buff=0.18)
        span = _label("14 quarters, by filing date", size=32).next_to(ticks, DOWN, buff=0.22)
        src = _label("Source: SEC Insider Transactions Data Sets", size=32, color=SOFT)
        src.move_to(DOWN * 3.05)

        self.add(counter)
        self.play(Write(title), FadeIn(meta), run_time=0.4)
        self.play(v.animate.set_value(FORM4_ROWS), run_time=1.2, rate_func=smooth)
        self.play(LaggedStart(*[t.animate.set_fill(INK, opacity=0.85) for t in ticks], lag_ratio=0.15),
                  FadeIn(t_left), FadeIn(t_right), FadeIn(span), run_time=0.8)
        self.play(FadeIn(src), run_time=0.3)
        self.wait(1.21)


class B03_CodeSplit(Scene):
    """'Most Aren't Buys': one bar per transaction code, as a share of the
    999,542 Form 4 rows. Purchases (P) 8.2% lands last and is boxed.
    ~2.9s (audio 2.90s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Most Aren't Buys", size=44, weight="BOLD").move_to(UP * 3.0)
        rows = [("Sales (S)", CODES["S"]), ("Grants, awards (A)", CODES["A"]),
                ("Tax/exercise payments (F)", CODES["F"]), ("Option exercises (M)", CODES["M"]),
                ("All other codes", OTHER), ("Purchases (P)", CODES["P"])]
        X0, MAXW = -0.9, 5.6
        scale = MAXW / max(n for _, n in rows)
        group = VGroup()
        bars = []
        for i, (name, n) in enumerate(rows):
            y = 1.95 - i * 0.78
            is_p = name.startswith("Purchases")
            lbl = _label(name, size=34, weight="BOLD" if is_p else None)
            lbl.move_to([X0 - 0.3, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(width=n * scale, height=0.5, stroke_width=0,
                            fill_color=INK if is_p else GHOST, fill_opacity=1)
            bar.move_to([X0 + n * scale / 2, y, 0])
            val = _label(pct(n), size=34, weight="BOLD" if is_p else None)
            val.next_to(bar, RIGHT, buff=0.2)
            group.add(VGroup(lbl, bar, val))
            bars.append(bar)
        p_row = group[-1]
        box = SurroundingRectangle(p_row, color=INK, stroke_width=4, buff=0.14, corner_radius=0.08)
        src = _label("Share of all 999,542 Form 4 rows, by transaction code", size=30, color=SOFT)
        src.move_to(DOWN * 2.95)

        self.play(Write(title), FadeIn(src), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in group[:-1]], lag_ratio=0.25),
                  run_time=1.0)
        self.play(FadeIn(p_row, shift=RIGHT * 0.2), run_time=0.3)
        self.play(Create(box), run_time=0.35)
        self.wait(0.95)


class B05_Filters(Scene):
    """'Pre-Registered Filters' waterfall: 78,495 qualifying buys, then
    Rule 2 repeat amendments −699, Rule 1 private deals/ESPP/DRIP −3,032,
    Rule 3 filed >30 days after trade −4,028, Rule 4 price under $1 −5,630,
    = 65,106 eligible. Footer: 10b5-1 plan buys kept and flagged.
    ~5.9s (audio 5.93s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Pre-Registered Filters", size=44, weight="BOLD").move_to(UP * 3.0)
        X0, W = -0.6, 5.2
        k = W / QUALIFYING
        LX = -0.9                                # right edge of the label column
        NX = 6.2                                 # right edge of the number column

        def row(i, name, lo, hi, number, solid, bold=False):
            y = 2.0 - i * 0.74
            lbl = _label(name, size=32, weight="BOLD" if bold else None, max_w=5.2)
            lbl.move_to([LX - lbl.width / 2, y, 0])
            w = max((hi - lo) * k, 0.04)
            if solid:
                bar = Rectangle(width=w, height=0.46, stroke_width=0, fill_color=INK, fill_opacity=1)
            else:
                bar = Rectangle(width=w, height=0.46, stroke_color=INK, stroke_width=2.5,
                                fill_color=GHOST, fill_opacity=1)
            bar.move_to([X0 + (lo + hi) / 2 * k, y, 0])
            num = _label(number, size=32, weight="BOLD" if bold else None)
            num.move_to([NX - num.width / 2, y, 0])
            return VGroup(lbl, bar, num)

        start = row(0, "Qualifying buys", 0, QUALIFYING, f"{QUALIFYING:,}", True, bold=True)
        steps = []
        level = QUALIFYING
        for i, (name, n) in enumerate([("Repeat amendments", R2_REPEAT),
                                       ("Private deals, ESPP, DRIP", R1_PLANS),
                                       ("Filed >30 days after trade", R3_LATE),
                                       ("Price under $1", R4_PENNY)], start=1):
            steps.append(row(i, name, level - n, level, f"−{n:,}", False))
            level -= n
        assert level == ELIGIBLE
        end = row(5, "Eligible buys", 0, ELIGIBLE, f"{ELIGIBLE:,}", True, bold=True)
        rule = Line([X0 - 0.05, 2.35, 0], [X0 - 0.05, 2.0 - 5 * 0.74 - 0.35, 0],
                    color=GHOST, stroke_width=2)
        foot = _label("10b5-1 plan buys: kept, flagged · joint filing = one insider",
                      size=30, color=SOFT).move_to(DOWN * 2.95)

        self.play(Write(title), Create(rule), FadeIn(start), run_time=0.6)
        for s in steps:
            self.play(FadeIn(s, shift=DOWN * 0.15), run_time=0.5)
            self.wait(0.38)
        self.play(FadeIn(end, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(foot), run_time=0.4)
        self.wait(0.91)


class B06_Eligible(Scene):
    """'65,106 eligible buys' (left) and typeset 65,106 / 999,542 ≈ 6.5%
    (right, 6.5% boxed); a full-width bar of all 999,542 Form 4 rows with the
    65,106 eligible share filled; '4,146 issuers · 38,320 filings'.
    ~5.4s (audio 5.40s)."""

    def construct(self):
        self.camera.background_color = BG

        big = _label(f"{ELIGIBLE:,}", size=130, weight="BOLD")
        cap = _label("eligible buys", size=44)
        left = VGroup(big, cap).arrange(DOWN, buff=0.2).move_to([-3.4, 1.55, 0])
        eq = MathTex(r"\frac{65{,}106}{999{,}542}", r"\approx", r"6.5\%",
                     font_size=60, color=INK)
        of_all = _label("of all Form 4 transactions", size=34, color=SOFT)
        right = VGroup(eq, of_all).arrange(DOWN, buff=0.3).move_to([3.3, 1.55, 0])
        ring = SurroundingRectangle(eq[2], color=INK, stroke_width=4, buff=0.16, corner_radius=0.08)

        BW = 12.0
        frame = Rectangle(width=BW, height=0.62, color=INK, stroke_width=3).move_to(DOWN * 0.95)
        share = BW * ELIGIBLE / FORM4_ROWS
        fill = Rectangle(width=share, height=0.62, stroke_width=0, fill_color=INK, fill_opacity=1)
        fill.move_to(frame.get_left() + RIGHT * share / 2)
        tag_l = _label("Eligible: 6.5%", size=32, weight="BOLD").next_to(fill, DOWN, buff=0.2)
        tag_l.align_to(frame, LEFT)
        tag_r = _label(f"All {FORM4_ROWS:,} Form 4 rows", size=32, color=SOFT)
        tag_r.next_to(frame, DOWN, buff=0.2).align_to(frame, RIGHT)
        meta = _label(f"{ISSUERS:,} issuers · {FILINGS:,} filings", size=34).move_to(DOWN * 2.95)

        self.play(FadeIn(left, scale=0.95), Create(frame), FadeIn(tag_r), run_time=0.6)
        self.wait(0.9)
        self.play(Write(eq), FadeIn(fill), FadeIn(tag_l), run_time=0.9)
        self.play(Create(ring), FadeIn(of_all), run_time=0.45)
        self.wait(0.5)
        self.play(FadeIn(meta, shift=UP * 0.1), run_time=0.4)
        self.wait(1.65)


class B07_SpotCheck(Scene):
    """'Spot-Check vs. Original Filings': 25 tiles in a 5x5 grid; 15 fill
    solid with a check (exact), 10 fill hatched (rounding only), legend
    '0 other errors'; Equifax example filed $166.1941 vs data set $166.19.
    ~5.6s (audio 5.59s)."""

    def construct(self):
        self.camera.background_color = BG

        title = _label("Spot-Check vs. Original Filings", size=44, weight="BOLD").move_to(UP * 3.0)
        meta = _label("25 random buys, each compared with its filing", size=32, color=SOFT)
        meta.next_to(title, DOWN, buff=0.2)

        S = 0.66
        tiles = VGroup(*[Square(S, color=INK, stroke_width=3) for _ in range(25)])
        tiles.arrange_in_grid(5, 5, buff=0.13).move_to([-3.7, -0.55, 0])

        def check(sq):
            c = sq.get_center()
            return VMobject(stroke_color=BG, stroke_width=7).set_points_as_corners(
                [c + [-0.17, 0.0, 0], c + [-0.04, -0.14, 0], c + [0.19, 0.16, 0]])

        def hatch(sq):
            c, h = sq.get_center(), S / 2
            lines = VGroup()
            for d in (-0.33, 0.0, 0.33):
                # diagonal y = x + d, clipped to the square
                x0, x1 = max(-h, -h - d), min(h, h - d)
                lines.add(Line(c + [x0, x0 + d, 0], c + [x1, x1 + d, 0], color=INK, stroke_width=3))
            return lines

        exact = [tiles[i] for i in range(SPOT_EXACT)]
        rnd = [tiles[i] for i in range(SPOT_EXACT, SPOT_EXACT + SPOT_ROUND)]
        fills = [sq.copy().set_fill(INK, opacity=1) for sq in exact]
        checks = [check(sq) for sq in exact]
        hatches = [hatch(sq) for sq in rnd]

        def legend_row(swatch, text, y):
            t = _label(text, size=36)
            g = VGroup(swatch, t).arrange(RIGHT, buff=0.3)
            g.move_to([0.0 + g.width / 2, y, 0])
            return g

        sw1 = VGroup(Square(0.42, color=INK, stroke_width=3).set_fill(INK, 1))
        sq2 = Square(0.42, color=INK, stroke_width=3)
        sw2 = VGroup(sq2, Line(sq2.get_corner(DL), sq2.get_corner(UR), color=INK, stroke_width=3))
        sw3 = Square(0.42, color=GHOST, stroke_width=3)
        l1 = legend_row(sw1, f"{SPOT_EXACT} exact match", 0.95)
        l2 = legend_row(sw2, f"{SPOT_ROUND} rounding only", 0.15)
        l3 = legend_row(sw3, f"{SPOT_OTHER} other errors", -0.65)
        ex = VGroup(_label("Example, Equifax price:", size=32, color=SOFT),
                    _label("filed $166.1941 · data set $166.19", size=32))
        ex.arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to([0.0, -2.05, 0], aligned_edge=LEFT)

        self.play(Write(title), FadeIn(meta), Create(tiles), run_time=0.6)
        self.play(LaggedStart(*[AnimationGroup(FadeIn(f), Create(c)) for f, c in zip(fills, checks)],
                              lag_ratio=0.12), FadeIn(l1), run_time=1.0)
        self.wait(0.3)
        self.play(LaggedStart(*[Create(h) for h in hatches], lag_ratio=0.15), FadeIn(l2), run_time=0.9)
        self.play(FadeIn(ex), run_time=0.5)
        self.play(FadeIn(l3), run_time=0.4)
        self.wait(1.89)
