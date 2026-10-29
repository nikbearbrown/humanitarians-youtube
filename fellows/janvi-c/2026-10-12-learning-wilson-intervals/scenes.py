"""scenes.py — Manim scenes for "Confidence Intervals for Small Tests" (wilson-intervals).

Same project as the Week 1–10 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week11/progress-figures-for-print/scenes.py (Week 10 block); Week 8 `vbar` bars (B01, B02), new interval brackets (B02–B05),
Week 9 struck-row/chip layout (B06).

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


def bracket(x1, x2, y, color=TEAL, h=0.3, sw=6):
    """Interval bracket |———| from x1 to x2 (fixed coordinates)."""
    return VGroup(Line(RIGHT * x1 + UP * y, RIGHT * x2 + UP * y, color=color, stroke_width=sw),
                  Line(RIGHT * x1 + UP * (y - h / 2), RIGHT * x1 + UP * (y + h / 2), color=color, stroke_width=sw),
                  Line(RIGHT * x2 + UP * (y - h / 2), RIGHT * x2 + UP * (y + h / 2), color=color, stroke_width=sw))


def cross(at, s=0.28, color=CRIMSON):
    c = VGroup(Line(at + (UL * s), at + (DR * s), color=color, stroke_width=6),
               Line(at + (DL * s), at + (UR * s), color=color, stroke_width=6))
    for l in c:
        l._qc_intentional = True
    return c


X0, K = -5.0, 10.0 / 100     # 0% at x −5, 100% at x +5


def px(p):
    return X0 + p * K


# ─────────────────────────────────────────────────────────────────────────────
#  B01_OneBar — 150 planted errors; one bar, 74.0%; how much could it move?
# ─────────────────────────────────────────────────────────────────────────────
class B01_OneBar(Scene):
    BID = "B01"
    FALLBACK = 9.3

    def construct(self):
        top = sans("150 planted errors", 48).move_to(UP * 2.6)
        axis = Line(RIGHT * px(0) + DOWN * 0.1, RIGHT * px(100) + DOWN * 0.1, color=SLATE, stroke_width=3)
        b = vbar(74.0, K, X0, 0.55, TEAL, h=0.9)
        v = sans("74.0%", 52).next_to(b, RIGHT, buff=0.25)
        q = serif("how much could it move?", 48).move_to(DOWN * 1.9)

        self.go(FadeIn(top), Create(axis), rt=0.5)
        self.cue("small", fallback=0.4)
        self.go(GrowFromEdge(b, LEFT), FadeIn(v), rt=0.6)
        self.cue("hides", fallback=0.7)
        self.go(FadeIn(q), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Range — the bar gains a range bracket; wider = less certain. (Bracket is illustrative.)
# ─────────────────────────────────────────────────────────────────────────────
class B02_Range(Scene):
    BID = "B02"
    FALLBACK = 7.7

    def construct(self):
        axis = Line(RIGHT * px(0) + DOWN * 0.1, RIGHT * px(100) + DOWN * 0.1, color=SLATE, stroke_width=3)
        b = vbar(74.0, K, X0, 0.55, TEAL, h=0.9)
        v = sans("74.0%", 52).move_to(RIGHT * px(74) + UP * 2.55)
        br = bracket(px(66), px(81), 1.45, color=INK)
        lab = serif("values consistent with the data", 44).move_to(DOWN * 1.2)
        cap = sans("wider = less certain", 48).move_to(DOWN * 2.4)

        self.add(axis, b)
        self.go(FadeIn(v), rt=0.3)
        self.cue("range", fallback=0.2)
        self.go(Create(br), FadeIn(lab), rt=0.5)
        self.cue("Wider", fallback=0.75)
        self.go(FadeIn(cap), Create(under(cap)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Edge — near 100%: the simple interval runs past it (✗); Wilson stays inside (✓).
# ─────────────────────────────────────────────────────────────────────────────
class B03_Edge(Scene):
    BID = "B03"
    FALLBACK = 14.6
    E = 4.4   # x of the 100% wall

    def construct(self):
        axis = Line(LEFT * 5.0 + DOWN * 0.15, RIGHT * self.E + DOWN * 0.15, color=SLATE, stroke_width=4)
        wall = DashedLine(RIGHT * self.E + UP * 2.3, RIGHT * self.E + DOWN * 2.6, color=SLATE, stroke_width=3)
        l0 = sans("0%", 42).move_to(LEFT * 5.0 + DOWN * 0.7)
        l100 = sans("100%", 42).move_to(RIGHT * self.E + DOWN * 0.7)
        simple = bracket(2.6, 5.7, 1.5, color=CRIMSON)
        s_lab = serif("simple interval", 46).move_to(RIGHT * 2.2 + UP * 1.5, aligned_edge=RIGHT)
        x = cross(LEFT * 4.6 + UP * 1.5)
        past = serif("runs past 100%", 42).move_to(RIGHT * 2.2 + UP * 2.4, aligned_edge=RIGHT)
        wil = bracket(2.2, 4.25, -1.7, color=TEAL)
        w_lab = sans("Wilson", 46).move_to(RIGHT * 1.8 + DOWN * 1.7, aligned_edge=RIGHT)
        ok = tick(s=0.42).move_to(LEFT * 4.6 + DOWN * 1.7)
        inside = serif("stays inside 0–100%", 42).move_to(RIGHT * 1.8 + DOWN * 2.6, aligned_edge=RIGHT)

        self.go(Create(axis), FadeIn(l0), FadeIn(l100), Create(wall), rt=0.6)
        self.cue("breaks", fallback=0.2)
        self.go(Create(simple), FadeIn(s_lab), rt=0.5)
        self.cue("past", fallback=0.38)
        self.go(FadeIn(past), Create(x), rt=0.4)
        self.cue("Wilson", fallback=0.55)
        self.go(Create(wil), FadeIn(w_lab), rt=0.5)
        self.cue("possible", fallback=0.7)
        self.go(FadeIn(inside), Create(ok), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Claude — Claude detection 98.0%; Wilson 94.3% – 99.3%. (Zoomed scale; only source values labelled.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_Claude(Scene):
    BID = "B04"
    FALLBACK = 9.6

    @staticmethod
    def zx(p):
        return -5.0 + (p - 90.0) * 1.0

    def construct(self):
        head = VGroup(ink_logo("claude", 0.6), sans("Claude detection", 48)).arrange(RIGHT, buff=0.3).move_to(UP * 2.7)
        axis = Line(RIGHT * self.zx(90) + DOWN * 0.3, RIGHT * self.zx(100) + DOWN * 0.3, color=SLATE, stroke_width=3)
        dot = Dot(RIGHT * self.zx(98.0) + DOWN * 0.3, radius=0.16, color=TEAL)
        dv = sans("98.0%", 52).move_to(RIGHT * self.zx(98.0) + UP * 1.1)
        br = bracket(self.zx(94.3), self.zx(99.3), -1.1, color=TEAL)
        lo = sans("94.3%", 46).move_to(RIGHT * self.zx(94.3) + DOWN * 1.85)
        hi = sans("99.3%", 46).move_to(RIGHT * self.zx(99.3) + DOWN * 1.85)
        lab = serif("Wilson 95% interval", 42).move_to(LEFT * 5.6 + DOWN * 1.1, aligned_edge=LEFT)

        self.go(FadeIn(head), Create(axis), rt=0.5)
        self.cue("98", fallback=0.3)
        self.go(FadeIn(dot), FadeIn(dv), rt=0.4)
        self.cue("Wilson", fallback=0.55)
        self.go(Create(br), FadeIn(lab), FadeIn(lo), FadeIn(hi), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Others — Mistral 60.9–75.5% · GPT-4o-mini 56.1–71.2% · pass-through 15.0–27.8%.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Others(Scene):
    BID = "B05"
    FALLBACK = 13.6
    S0, SK = -0.9, 0.083   # 10% at x −0.9

    def sx(self, p):
        return self.S0 + (p - 10.0) * self.SK

    def construct(self):
        rows = [("mistral", "Mistral", 60.9, 75.5, "60.9% – 75.5%", SLATE, 1.6, "about", "above"),
                ("openai", "GPT-4o-mini", 56.1, 71.2, "56.1% – 71.2%", SLATE, 0.0, "56", "above"),
                (None, "pass-through", 15.0, 27.8, "15.0% – 27.8%", CRIMSON, -1.9, "share", "right")]
        out = []
        for lg, nm, lo, hi, txt, col, y, w, where in rows:
            parts = [ink_logo(lg, 0.45)] if lg else []
            lab = VGroup(*parts, sans(nm, 42)).arrange(RIGHT, buff=0.2).move_to(RIGHT * -1.3 + UP * y, aligned_edge=RIGHT)
            br = bracket(self.sx(lo), self.sx(hi), y, color=col)
            v = sans(txt, 42)
            if where == "above":
                v.move_to(RIGHT * (self.sx(lo) + self.sx(hi)) / 2 + UP * (y + 0.6))
            else:
                v.move_to(RIGHT * (self.sx(hi) + 0.35) + UP * y, aligned_edge=LEFT)
            out.append((VGroup(lab, br, v), w))
        axis = Line(RIGHT * self.sx(10) + DOWN * 2.7, RIGHT * self.sx(80) + DOWN * 2.7, color=SLATE, stroke_width=3)

        self.go(Create(axis), rt=0.3)
        for (g, w), fb in zip(out, (0.12, 0.35, 0.6)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(g[0]), Create(g[1]), FadeIn(g[2]), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Limits — what an interval doesn't fix.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Limits(Scene):
    BID = "B06"
    FALLBACK = 12.4
    L = [("assumes a fair sample", "fair", 1.5), ("only the errors you planted", "nothing", 0.0), ("size, not bias", "uncertainty", -1.5)]

    def construct(self):
        head = serif("what an interval doesn't fix", 46).move_to(UP * 2.9)
        cs = [(chip(t, 48, stroke=CRIMSON).move_to(UP * y), w) for t, w, y in self.L]
        self.go(FadeIn(head), rt=0.4)
        for (c, w), fb in zip(cs, (0.25, 0.5, 0.72)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), rt=0.4)
        self.finish()
