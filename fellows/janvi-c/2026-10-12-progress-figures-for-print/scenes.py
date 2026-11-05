"""scenes.py — Manim scenes for "Figures You Can Read on Paper" (figures-for-print).

Same project as the Week 1–10 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week10/progress-72-comments/scenes.py (Week 9 block + `checkrow`, `stamp`); Week 10 fact cards (B02, B06), Week 9 labelled rows (B03, B05),
Week 8 reference grid (B07), Week 4–10 result cards (B01, B04).

Every number on screen appears in inbox/term2-week11/term2-week11-video-content.md as written.
Only Professor Brown and Professor Gultepe are ever named. Short beats show their key text at once (Week 5 GATE T lesson).

Channel @HumanitariansAI · humanitarians palette (brands/hai.md): cream ground,
warm ink text, petrol teal = kept/good, burnt orange = struck/bad (never text),
navy slate = structure, amber gold = highlighter fill only (never text).
Type: EB Garamond (serif body) + Montserrat (sans headers). Logos in plain ink.
"""
from manim import *
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGOS = HERE / "assets" / "logos"

# ── palette (humanitarians tokens) ──────────────────────────────────────────
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"
CRIMSON = "#E4572E"
SLATE = "#29335C"
GOLD = "#F3A712"
SAGE = "#A8C686"
WHITE = "#FFFFFF"
MUTED = "#6B625A"

SERIF = "EB Garamond"
SANS = "Montserrat"


def beat_seconds(bid, fallback):
    """Measured narration length for a beat (the master clock)."""
    try:
        return float(json.loads((HERE / "mp3" / "timings.json").read_text())[bid])
    except Exception:
        return fallback


def _norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def word_frac(bid, word, nth=1, fallback=0.5):
    """Fraction of the beat at which the nth spoken word starting with `word` begins."""
    try:
        d = json.loads((HERE / "mp3" / "words.json").read_text())
        fps = d.get("fps", 24)
        total = beat_seconds(bid, 0) * fps
        hits = [w for w in d["beats"][bid] if _norm(w["text"]).startswith(_norm(word))]
        return min(0.97, hits[nth - 1]["startFrame"] / total)
    except Exception:
        return fallback


def serif(s, size=36, color=INK, sliceable=False, **kw):
    """sliceable=True disables ligatures so glyph i == char i (needed only for span())."""
    # typeset at 3x and scale down: Pango's glyph positioning rounds badly at small sizes
    return Text(s, font=SERIF, font_size=size * 3, color=color, disable_ligatures=sliceable,
                **kw).scale(1 / 3)


def sans(s, size=28, color=INK, weight="BOLD", **kw):
    return Text(s, font=SANS, font_size=size * 3, color=color, weight=weight, **kw).scale(1 / 3)


def span(t, line, word):
    """Glyphs of `word` inside Text `t` built from `line` (ligatures disabled)."""
    i = line.index(word)
    return t[i:i + len(word)]


def logo(name, height):
    m = SVGMobject(str(LOGOS / f"{name}.svg"))
    m.set(height=height)
    m.set_stroke(opacity=0)
    return m


def strike(mob, color=CRIMSON, width=6):
    ln = Line(mob.get_left() + LEFT * 0.04, mob.get_right() + RIGHT * 0.04,
              color=color, stroke_width=width)
    ln._qc_intentional = True
    return ln


def highlight(mob, color=GOLD, opacity=0.55):
    r = Rectangle(width=mob.width + 0.12, height=mob.height + 0.14,
                  fill_color=color, fill_opacity=opacity, stroke_opacity=0)
    r.move_to(mob)
    return r


def card(w, h, stroke=SLATE, sw=2.5):
    """Outline card on the cream ground (no fill: keeps the frame's ink dark, GATE V)."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_opacity=0,
                            stroke_color=stroke, stroke_width=sw)


def chip(label, size=30, stroke=SLATE):
    t = serif(label, size)
    box = RoundedRectangle(width=t.width + 0.45, height=t.height + 0.32,
                           corner_radius=0.16, fill_opacity=0,
                           stroke_color=stroke, stroke_width=2.5)
    t.move_to(box)
    return VGroup(box, t)


def tick(color=TEAL, s=0.32):
    """A drawn check mark (no glyph, so no font fallback)."""
    return VMobject(stroke_color=color, stroke_width=6).set_points_as_corners(
        [LEFT * s * 0.5 + UP * s * 0.05, DOWN * s * 0.4 + LEFT * s * 0.1, RIGHT * s * 0.6 + UP * s * 0.5])


class Beat(Scene):
    """Clocked scene: events land at fractions of the measured beat length."""
    BID = "B00"
    FALLBACK = 20.0

    def boot(self):
        """Clock + ground + HAI corner bug (LOGO LAW). Lazy: runs on first use."""
        if getattr(self, "_booted", False):
            return
        self._booted = True
        self.camera.background_color = CREAM
        self.D = beat_seconds(self.BID, self.FALLBACK)
        self.t = 0.0
        bug = logo("humanitarians", 0.32)
        bug.set_fill(INK, opacity=0.45)
        bug.move_to(RIGHT * 6.0 + DOWN * 3.18)
        self.add(bug)

    def at(self, frac):
        self.boot()
        target = frac * self.D
        if target - self.t > 1 / 24:
            self.wait(target - self.t)
            self.t = target

    def cue(self, word, nth=1, fallback=0.5):
        """Wait until the nth spoken word starting with `word`."""
        self.at(word_frac(self.BID, word, nth, fallback))

    def go(self, *anims, rt=0.8):
        self.boot()
        self.play(*anims, run_time=rt)
        self.t += rt

    def finish(self):
        self.boot()
        if self.D - self.t > 1 / 24:
            self.wait(self.D - self.t)
            self.t = self.D


# run.sh discovers scenes only when declared with the literal base "Scene", so every beat
# scene below is declared `(Scene)`; the name is rebound to the clocked Beat base here.
Scene = Beat


def counter(target, fmt, size, color, pos, tracker, start=0):
    """Text counter that runs start → target as `tracker` goes 0 → 1."""
    def build():
        v = start + tracker.get_value() * (target - start)
        return sans(fmt(v), size, color).move_to(pos)
    return always_redraw(build)


def arrow(a, b, color=SLATE):
    """Fixed-coordinate arrow (GATE A stub-safe)."""
    return Arrow(a, b, buff=0, color=color, stroke_width=4)


def lines(texts, size=36, color=INK, buff=0.08):
    return VGroup(*[serif(t, size, color) for t in texts]).arrange(DOWN, aligned_edge=LEFT, buff=buff)


def ink_logo(name, h):
    return logo(name, h).set_fill(INK, opacity=1)


def under(t):
    """Teal underline (Week 4: replaces multi-line gold highlights, GATE V contrast)."""
    return Line(t.get_corner(DL) + DOWN * 0.08, t.get_corner(DR) + DOWN * 0.08, color=TEAL, stroke_width=5)




def vbar(pct, K, x0, y, color, h=0.6):
    """Horizontal bar from the axis at x0 (Week 7 B02 queue bars)."""
    b = Rectangle(width=max(pct * K, 0.02), height=h, fill_color=color, fill_opacity=1, stroke_opacity=0)
    return b.move_to(RIGHT * x0 + UP * y, aligned_edge=LEFT)


def checkrow(label, value, y, xl=-5.0, xv=-1.4, ls=34, vs=34):
    """Tick + sans label + serif value on one row (consistency checklist)."""
    t = tick(s=0.34).move_to(RIGHT * (xl - 0.55) + UP * y)
    l = sans(label, ls).move_to(RIGHT * xl + UP * y, aligned_edge=LEFT)
    v = serif(value, vs).move_to(RIGHT * xv + UP * y, aligned_edge=LEFT) if value else VGroup()
    return VGroup(t, l, v)


def stamp(text, w, color=CRIMSON, size=42, angle=-6):
    """Rotated outline stamp (Week 9 learning B01)."""
    s = VGroup(RoundedRectangle(width=w, height=1.0, corner_radius=0.12, stroke_color=color, stroke_width=5),
               sans(text, size))
    s[1].move_to(s[0])
    return s.rotate(angle * DEGREES)


# Week 9–10 GATE T lesson: in dense cards keep serif ≥ 42 and sans ≥ 40; never strike serif text.


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Quote — "I cannot read the figures when printed." — Professor Gultepe.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Quote(Scene):
    BID = "B01"
    FALLBACK = 7.4

    def construct(self):
        box = card(11.6, 2.6, stroke=SLATE, sw=3).move_to(UP * 1.0)
        q = serif("“I cannot read the figures when printed.”", 50).move_to(box).shift(UP * 0.35)
        who = sans("Professor Gultepe", 42).move_to(box).shift(DOWN * 0.6)
        rules = chip("rules for every figure", 46, stroke=TEAL).move_to(DOWN * 1.9)

        self.go(Create(box), FadeIn(q), FadeIn(who), rt=0.5)
        self.cue("rules", fallback=0.75)
        self.go(FadeIn(rules), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Rules — ≥ 16px text on a 1000px canvas · no titles inside images · paper terms only.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Rules(Scene):
    BID = "B02"
    FALLBACK = 12.8

    def construct(self):
        specs = [(VGroup(sans("≥ 16px text on a 1000px canvas", 44)), 1.2, 2.2, "16"),
                 (VGroup(sans("no titles inside images", 44), serif("captions go below", 42)).arrange(DOWN, buff=0.12), 1.6, 0.55, "titles"),
                 (VGroup(sans("paper terms only", 44), serif("old labels removed", 42)).arrange(DOWN, buff=0.12), 1.6, -1.45, "terms")]
        cards = []
        for t, h, y, w in specs:
            b = card(11.4, h, stroke=TEAL, sw=4).move_to(UP * y)
            t.move_to(b)
            cards.append((VGroup(b, t), w))
        for (c, w), fb in zip(cards, (0.05, 0.35, 0.7)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Figures — Figs 1, 2, S1 rebuilt; Figs 3, 4 in matplotlib at 300 dpi; two check rounds.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Figures(Scene):
    BID = "B03"
    FALLBACK = 15.8
    FIGS = [("Fig 1", "architecture"), ("Fig 2", "decision logic"), ("Fig S1", "funnel"),
            ("Fig 3", "kappa heatmap"), ("Fig 4", "sensitivity by judge")]

    def construct(self):
        rows = []
        for i, (f, nm) in enumerate(self.FIGS):
            y = 2.7 - i * 0.82
            rows.append(VGroup(tick(s=0.36).move_to(RIGHT * -5.6 + UP * y),
                               sans(f, 42).move_to(RIGHT * -5.1 + UP * y, aligned_edge=LEFT),
                               serif(nm, 44).move_to(RIGHT * -2.9 + UP * y, aligned_edge=LEFT)))
        mp = chip("Figs 3 and 4: matplotlib · 300 dpi", 42).move_to(DOWN * 1.45)
        r1 = chip("round 1: 3 issues", 44, stroke=CRIMSON)
        r2 = chip("round 2: all fixed", 44, stroke=TEAL)
        ar = serif("→", 46)
        rr = VGroup(r1, ar, r2).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.45)

        self.cue("architecture", fallback=0.08)
        self.go(*[FadeIn(r[1:]) for r in rows[:3]], *[Create(r[0]) for r in rows[:3]], rt=0.6)
        self.cue("kappa", fallback=0.35)
        self.go(*[FadeIn(r[1:]) for r in rows[3:]], *[Create(r[0]) for r in rows[3:]], rt=0.5)
        self.cue("matplotlib", fallback=0.5)
        self.go(FadeIn(mp), rt=0.4)
        self.cue("Two", fallback=0.72)
        self.go(FadeIn(r1), rt=0.4)
        self.cue("confirmed", fallback=0.88)
        self.go(FadeIn(ar), FadeIn(r2), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Panels — Playwright screenshots → four panels (a)–(d).
# ─────────────────────────────────────────────────────────────────────────────
class B04_Panels(Scene):
    BID = "B04"
    FALLBACK = 12.8
    P = [("(a) approved", "Apoptosis", TEAL, -2.95, 1.15, "approved"), ("(b) junk", "Prolactin list", CRIMSON, 2.95, 1.15, "junk"),
         ("(c) fix_definition", "CTL", SLATE, -2.95, -1.05, "fixed"), ("(d) REVIEW", "Iron metabolism", SLATE, 2.95, -1.05, "review")]

    def construct(self):
        tool = chip("Playwright, headless Chromium", 44).move_to(UP * 2.95)
        panels = []
        for a, b, col, x, y, w in self.P:
            box = card(5.6, 1.9, stroke=col, sw=4).move_to(RIGHT * x + UP * y)
            t = VGroup(sans(a, 40), serif(b, 44)).arrange(DOWN, buff=0.15).move_to(box)
            panels.append((VGroup(box, t), w))
        cap = serif("one dashboard figure, four labelled panels", 42).move_to(DOWN * 2.6)

        self.go(FadeIn(tool), rt=0.5)
        for (p, w), fb in zip(panels, (0.4, 0.5, 0.6, 0.75)):
            self.cue(w, fallback=fb)
            self.go(Create(p[0]), FadeIn(p[1]), rt=0.4)
        self.cue("assembled", fallback=0.85)
        self.go(FadeIn(cap), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Funnel — Table 2 disposition walk-through, 10,055 → 8,053 shipped.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Funnel(Scene):
    BID = "B05"
    FALLBACK = 17.4
    ROWS = [("10,055", "matched articles", "10,055"), ("- 6", "duplicates = 10,049", "six"),
            ("- 1,302", "junk", "junk"), ("- 586", "REVIEW", "review"), ("- 338", "fix_definition", "fix"),
            ("+ 230", "returned from regeneration", "230"), ("= 8,053", "shipped keywords", "8,053")]

    def construct(self):
        tag = chip("Table 2", 44).move_to(RIGHT * 4.6 + UP * 2.75)
        rows = []
        for i, (v, l, w) in enumerate(self.ROWS):
            y = 2.75 - i * 0.8
            col = TEAL if i == 6 else INK
            rows.append((VGroup(sans(v, 44, col).move_to(RIGHT * -2.9 + UP * y, aligned_edge=RIGHT),
                                serif(l, 44).move_to(RIGHT * -2.4 + UP * y, aligned_edge=LEFT)), w))
        fin = card(9.6, 0.8, stroke=TEAL, sw=4).move_to(RIGHT * -0.9 + UP * (2.75 - 6 * 0.8))

        self.go(FadeIn(tag), rt=0.4)
        for (r, w), fb in zip(rows, (0.12, 0.3, 0.42, 0.48, 0.55, 0.72, 0.88)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r), rt=0.35)
        self.go(Create(fin), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Workbook — Table 3: all experiments, one table; 4 new Wilson 95% intervals; the workbook.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Workbook(Scene):
    BID = "B06"
    FALLBACK = 14.2

    def construct(self):
        t3 = card(10.4, 1.7, stroke=SLATE, sw=3).move_to(UP * 2.2)
        t3t = VGroup(sans("Table 3", 46), serif("all experiments, one table", 44)).arrange(RIGHT, buff=0.5).move_to(t3)
        wil = chip("4 new Wilson 95% intervals", 46, stroke=TEAL).move_to(UP * 0.55)
        wb = card(10.4, 2.7, stroke=SLATE, sw=3).move_to(DOWN * 1.75)
        wh = serif("data workbook", 42).move_to(wb).shift(UP * 0.85)
        stats = [sans("7 sheets · ~87 live formulas", 42), sans("zero errors", 42)]
        stats[0].move_to(wb)
        ok = tick(s=0.42)
        VGroup(stats[1], ok).arrange(RIGHT, buff=0.3).move_to(wb).shift(DOWN * 0.8)

        self.go(Create(t3), FadeIn(t3t), rt=0.5)
        self.cue("four", fallback=0.3)
        self.go(FadeIn(wil), rt=0.4)
        self.cue("seven", fallback=0.55)
        self.go(Create(wb), FadeIn(wh), FadeIn(stats[0]), rt=0.5)
        self.cue("zero", fallback=0.85)
        self.go(FadeIn(stats[1]), Create(ok), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Swap — image swaps matched by content, not filename; 8 items in order.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Swap(Scene):
    BID = "B07"
    FALLBACK = 10.2

    def construct(self):
        head = serif("the riskiest step: swapping images in", 44).move_to(UP * 2.9)
        cells = []
        for i in range(8):
            x = -4.9 + i * 1.4
            b = card(1.2, 1.0, stroke=SLATE, sw=3).move_to(RIGHT * x + UP * 1.35)
            cells.append(VGroup(b, sans(str(i + 1), 44).move_to(b), tick(s=0.34).move_to(RIGHT * x + UP * 0.35)))
        m = chip("matched by content, not filename", 44, stroke=TEAL).move_to(DOWN * 1.1)
        n = sans("8 items in order", 44).move_to(DOWN * 2.4)

        self.go(FadeIn(head), *[Create(c[0]) for c in cells], *[FadeIn(c[1]) for c in cells], rt=0.6)
        self.cue("identified", fallback=0.35)
        self.go(FadeIn(m), rt=0.4)
        self.cue("eight", fallback=0.75)
        self.go(LaggedStart(*[Create(c[2]) for c in cells], lag_ratio=0.1), FadeIn(n), rt=0.7)
        self.finish()
