"""scenes.py — Manim scenes for "Trace Every Number to Its Source" (trace-every-number).

Same project as the Week 1–9 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week10/progress-72-comments/scenes.py (Week 9 block + `checkrow`, `stamp`); its B04 trace table (B02–B04),
its B05 do-not-use card (B05), Week 4–9 result cards (B06).

Every number on screen appears in inbox/term2-week10/term2-week10-video-content.md as written.
Only Professor Brown and Professor Gultepe are ever named. 71,000 is shown only as unsourced/derived. Short beats show their key text at once (Week 5 GATE T lesson).

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


COLS = (-5.4, -1.9, 2.6)   # value · source · status


def sheet_head(y=2.0):
    """Master number sheet header row + rule (Week 10 progress B04 table)."""
    h = VGroup(*[sans(t, 40, TEAL).move_to(RIGHT * x + UP * y, aligned_edge=LEFT)
                 for t, x in zip(("value", "source", "status"), COLS)])
    rule = Line(LEFT * 5.6 + UP * (y - 0.4), RIGHT * 5.6 + UP * (y - 0.4), color=SLATE, stroke_width=3)
    return VGroup(h, rule)


def sheet_row(value, source, status, y, ok=True):
    v = sans(value, 46).move_to(RIGHT * COLS[0] + UP * y, aligned_edge=LEFT)
    s = serif(source, 42).move_to(RIGHT * COLS[1] + UP * y, aligned_edge=LEFT)
    st = tick(s=0.42).move_to(RIGHT * (COLS[2] + 0.3) + UP * y) if ok else serif(status, 42).move_to(RIGHT * COLS[2] + UP * y, aligned_edge=LEFT)
    return VGroup(v, s, st)


def magnifier(r=0.55, color=SLATE):
    c = Circle(radius=r, stroke_color=color, stroke_width=6)
    k = r * 0.7071   # fixed coordinates (static-check stub has no point_at_angle)
    h = Line(RIGHT * k + DOWN * k, RIGHT * (k + r * 0.65) + DOWN * (k + r * 0.65), color=color, stroke_width=9)
    return VGroup(c, h)


def page(w=3.0, h=3.8, n=5):
    """A paper page: outline card + grey text lines."""
    p = card(w, h, stroke=SLATE, sw=3)
    # solid bars, not hairlines: GATE T §8.1 read hairline rows as undersized text
    ls = VGroup(*[Rectangle(width=w - 0.8 - (0.6 if i % 3 == 2 else 0), height=0.2, fill_color=SLATE, fill_opacity=0.35,
                            stroke_opacity=0).move_to(UP * (h / 2 - 0.6 - i * 0.6) + LEFT * (0.3 if i % 3 == 2 else 0))
                  for i in range(n)])
    return VGroup(p, ls)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Floating — numbers float up from a paper page; they all look equally solid.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Floating(Scene):
    """Simplified after two GATE T §8.1 fails: page graphic dropped; numbers + one caption, all ≥ 48."""
    BID = "B01"
    FALLBACK = 9.5
    NUMS = [("~81,000", -3.6, 1.7), ("10,055", 0.4, 2.2), ("10,049", 3.9, 1.4), ("~484", 0.6, 0.2)]

    def construct(self):
        base = Line(LEFT * 5.0 + DOWN * 1.2, RIGHT * 5.0 + DOWN * 1.2, color=SLATE, stroke_width=4)
        nums = [sans(t, 56).move_to(RIGHT * x + UP * y) for t, x, y in self.NUMS]
        cap = sans("they all look equally solid", 48).move_to(DOWN * 2.3)

        self.go(Create(base), rt=0.5)
        self.cue("data", fallback=0.25)
        self.go(*[FadeIn(n, shift=UP * 1.2) for n in nums[:2]], rt=0.6)
        self.cue("calculation", fallback=0.5)
        self.go(*[FadeIn(n, shift=UP * 1.2) for n in nums[2:]], rt=0.6)
        self.cue("solid", fallback=0.85)
        self.go(FadeIn(cap), Create(under(cap)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Sheet — master number sheet: value · source · status.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Sheet(Scene):
    BID = "B02"
    FALLBACK = 8.0

    def construct(self):
        title = sans("master number sheet", 48).move_to(UP * 2.9)
        hd = sheet_head()
        blanks = VGroup(*[Line(LEFT * 5.6 + UP * y, RIGHT * 5.6 + UP * y, color=SLATE, stroke_width=1.5)
                          for y in (0.4, -0.8, -2.0)])
        notes = VGroup(serif("the number", 38).move_to(RIGHT * COLS[0] + UP * 1.0, aligned_edge=LEFT),
                       serif("where it came from", 38).move_to(RIGHT * COLS[1] + UP * 1.0, aligned_edge=LEFT),
                       serif("does it still say so?", 38).move_to(RIGHT * COLS[2] + UP * 1.0, aligned_edge=LEFT))

        self.go(FadeIn(title), Create(under(title)), rt=0.5)
        self.cue("row", fallback=0.35)
        self.go(FadeIn(hd[0]), Create(hd[1]), *[Create(b) for b in blanks], rt=0.5)
        self.cue("value", fallback=0.5)
        self.go(FadeIn(notes[0]), rt=0.3)
        self.cue("where", fallback=0.6)
        self.go(FadeIn(notes[1]), rt=0.3)
        self.cue("whether", fallback=0.8)
        self.go(FadeIn(notes[2]), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Rows — ~81,000 substring run ✓ · 10,055 exact-match run ✓ · 10,049 after 6 duplicates ✓.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Rows(Scene):
    BID = "B03"
    FALLBACK = 12.0
    ROWS = [("~81,000", "substring run", "81,000", 0.9), ("10,055", "exact-match run", "10,055", -0.35),
            ("10,049", "after 6 duplicates", "10,049", -1.6)]

    def construct(self):
        hd = sheet_head()
        rows = [(sheet_row(v, s, None, y), w) for v, s, w, y in self.ROWS]
        self.go(FadeIn(hd[0]), Create(hd[1]), rt=0.4)
        for (r, w), fb in zip(rows, (0.15, 0.45, 0.7)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[0]), FadeIn(r[1]), Create(r[2]), rt=0.45)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Derived — 71,000 · source — · derived: ~81,000 − ~10,000; written down as if measured.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Derived(Scene):
    BID = "B04"
    FALLBACK = 9.6

    def construct(self):
        hd = sheet_head()
        box = card(11.8, 1.3, stroke=CRIMSON, sw=4).move_to(UP * 0.85)
        v = sans("71,000", 46).move_to(RIGHT * COLS[0] + UP * 0.85, aligned_edge=LEFT)
        s = sans("—", 46).move_to(RIGHT * COLS[1] + UP * 0.85, aligned_edge=LEFT)
        st = sans("unsourced", 42).move_to(RIGHT * 2.2 + UP * 0.85, aligned_edge=LEFT)
        der = serif("derived: ~81,000 − ~10,000", 46).move_to(DOWN * 0.75)
        meas = stamp("written down as if measured", 9.2, size=40, angle=-3).move_to(DOWN * 2.2)

        self.go(FadeIn(hd[0]), Create(hd[1]), Create(box), FadeIn(v), FadeIn(s), FadeIn(st), rt=0.5)
        self.cue("subtraction", fallback=0.3)
        self.go(FadeIn(der), rt=0.4)
        self.cue("written", fallback=0.72)
        self.go(Create(meas[0]), FadeIn(meas[1]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_DoNotUse — do-not-use list; search the whole paper before you submit.
# ─────────────────────────────────────────────────────────────────────────────
class B05_DoNotUse(Scene):
    """Simplified after two GATE T §8.1 fails: page and strike dropped; text ≥ 48."""
    BID = "B05"
    FALLBACK = 8.4

    def construct(self):
        dnu = card(5.2, 3.0, stroke=CRIMSON, sw=5).move_to(LEFT * 3.2 + UP * 0.5)
        dh = sans("do not use", 50).move_to(dnu).shift(UP * 0.65)
        dv = sans("71,000", 56).move_to(dnu).shift(DOWN * 0.45)
        mg = magnifier(0.75).move_to(RIGHT * 3.2 + UP * 0.9)
        mt = VGroup(sans("search the", 48), sans("whole paper", 48)).arrange(DOWN, buff=0.15).move_to(RIGHT * 3.0 + DOWN * 0.85)
        cap = sans("before you submit", 48).move_to(DOWN * 2.4)

        self.go(Create(dnu), FadeIn(dh), FadeIn(dv), rt=0.6)
        self.cue("search", fallback=0.7)
        self.go(FadeIn(mg), FadeIn(mt), rt=0.5)
        self.cue("before", fallback=0.82)
        self.go(FadeIn(cap), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — source found ≠ source right; derived is fine if labelled derived.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 9.6

    def construct(self):
        head = serif("what this doesn't do", 44).move_to(UP * 2.9)
        a = card(10.6, 1.6, stroke=CRIMSON, sw=4).move_to(UP * 1.0)
        at = sans("source found ≠ source right", 48).move_to(a)
        b = card(10.6, 1.6, stroke=TEAL, sw=4).move_to(DOWN * 1.2)
        bt = sans("derived is fine if labelled derived", 44, TEAL).move_to(b)

        self.go(FadeIn(head), rt=0.4)
        self.cue("shows", fallback=0.2)
        self.go(Create(a), FadeIn(at), rt=0.5)
        self.cue("derived", fallback=0.6)
        self.go(Create(b), FadeIn(bt), rt=0.5)
        self.finish()
