"""scenes.py — Manim scenes for "How to Audit a Reference List" (auditing-references).

Same project as the Week 1–8 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week9/progress-fake-citations/scenes.py (Week 8 block + `checkrow`); one step-card layout for B02–B05,
Week 6 learning strike rows (B06), Week 4–9 result cards.

Every number on screen appears in inbox/term2-week09/term2-week9-video-content.md as written.
Only Professor Brown is ever named. Short beats show their key text at once (Week 5 GATE T lesson).

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


def step_head(n, title):
    """Step header: numbered badge + sans title, top of frame."""
    badge = VGroup(Circle(radius=0.42, stroke_color=TEAL, stroke_width=5), sans(str(n), 44, TEAL))
    badge[1].move_to(badge[0])
    return VGroup(badge, sans(title, 48)).arrange(RIGHT, buff=0.4).move_to(UP * 2.75)


def chips(labels, size=40, stroke=SLATE, buff=0.3):
    return VGroup(*[chip(l, size, stroke=stroke) for l in labels]).arrange(RIGHT, buff=buff)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Looks — a perfect-looking citation (our fabricated [14]); "does it exist?"; ours: 2 of 24, 7.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Looks(Scene):
    BID = "B01"
    FALLBACK = 10.5

    def construct(self):
        box = card(8.6, 2.2, stroke=SLATE, sw=3).move_to(UP * 1.3)
        t = VGroup(sans("[14]  Elkins & Kochmar", 46), serif("BEA 2023", 46)).arrange(DOWN, buff=0.2).move_to(box)
        stamp = VGroup(RoundedRectangle(width=5.0, height=1.05, corner_radius=0.12, stroke_color=CRIMSON, stroke_width=5),
                       sans("does it exist?", 44))
        stamp[1].move_to(stamp[0])
        stamp.rotate(-6 * DEGREES).move_to(RIGHT * 3.2 + DOWN * 0.85)
        ours = chip("ours: 2 of 24 fabricated, 7 wrong details", 42).move_to(DOWN * 2.2)

        self.go(Create(box), FadeIn(t), rt=0.6)
        self.cue("don't", fallback=0.3)
        self.go(Create(stamp[0]), FadeIn(stamp[1]), rt=0.4)
        self.cue("24", fallback=0.55)
        self.go(FadeIn(ours), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Exists — step 1: exact title → Scholar · Crossref · arXiv; named venue → its own proceedings.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Exists(Scene):
    BID = "B02"
    FALLBACK = 10.0

    def construct(self):
        head = step_head(1, "Does it exist?")
        l1 = sans("search the exact title in", 44).move_to(UP * 1.4)
        c1 = chips(["Google Scholar", "Crossref", "arXiv"], 40).move_to(UP * 0.4)
        l2 = sans("a venue is named? search", 44).move_to(DOWN * 1.0)
        c2 = chip("its own proceedings", 40).move_to(DOWN * 2.0)

        self.go(FadeIn(head), Create(head[0][0]), rt=0.5)
        self.cue("exact", fallback=0.3)
        self.go(FadeIn(l1), FadeIn(c1), rt=0.5)
        self.cue("venue", fallback=0.65)
        self.go(FadeIn(l2), FadeIn(c2), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Details — step 2: authors and initials · title · venue · year · pages; our errors.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Details(Scene):
    BID = "B03"
    FALLBACK = 13.9

    def construct(self):
        head = step_head(2, "Do the details match?")
        r1 = chips(["authors and initials", "title", "venue"], 40).move_to(UP * 1.45)
        r2 = chips(["year", "pages"], 40).move_to(UP * 0.4)
        lab = serif("our errors hid there:", 42).move_to(DOWN * 0.75)
        e1 = chips(["wrong authors", "wrong pages"], 40, stroke=CRIMSON, buff=0.5).move_to(DOWN * 1.75)
        e2 = chip("preprint listed as a conference paper", 40, stroke=CRIMSON).move_to(DOWN * 2.75)

        self.go(FadeIn(head), Create(head[0][0]), rt=0.5)
        self.cue("author", fallback=0.25)
        self.go(LaggedStart(*[FadeIn(c) for c in [*r1, *r2]], lag_ratio=0.25), rt=1.2)
        self.cue("Our", fallback=0.6)
        self.go(FadeIn(lab), FadeIn(e1[0]), rt=0.5)
        self.cue("preprint", fallback=0.72)
        self.go(FadeIn(e2), rt=0.4)
        self.cue("pages", nth=2, fallback=0.9)
        self.go(FadeIn(e1[1]), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_DOI — step 3: add a DOI (our replacement [6]'s); no DOI found → look harder. (5.3 s: at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_DOI(Scene):
    BID = "B04"
    FALLBACK = 5.3

    def construct(self):
        head = step_head(3, "Add a DOI")
        box = card(10.0, 1.6, stroke=TEAL, sw=4).move_to(UP * 0.7)
        d = sans("DOI: 10.1145/2063518.2063519", 46).move_to(box)
        ok = tick(s=0.45).next_to(box, RIGHT, buff=0.2)
        warn = DashedVMobject(RoundedRectangle(width=8.4, height=1.25, corner_radius=0.16, stroke_color=CRIMSON,
                                               stroke_width=4), num_dashes=48).move_to(DOWN * 1.6)
        w = serif("no DOI found → look harder", 46).move_to(warn)

        self.go(FadeIn(head), Create(head[0][0]), Create(box), FadeIn(d), Create(ok), rt=0.5)
        self.cue("can't", fallback=0.5)
        self.go(Create(warn), FadeIn(w), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Claim — step 4: your sentence ↔ the paper; replaced a citation → re-read its sentence.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Claim(Scene):
    BID = "B05"
    FALLBACK = 10.4

    def construct(self):
        head = step_head(4, "Does it support the claim?")
        l = card(5.0, 1.6, stroke=SLATE, sw=3).move_to(LEFT * 3.3 + UP * 0.8)
        lt = sans("your sentence", 42).move_to(l)
        r = card(5.0, 1.6, stroke=SLATE, sw=3).move_to(RIGHT * 3.3 + UP * 0.8)
        rt_ = sans("the paper", 42).move_to(r)
        da = DoubleArrow(LEFT * 0.7 + UP * 0.8, RIGHT * 0.7 + UP * 0.8, buff=0, color=TEAL, stroke_width=5)
        same = serif("says the same?", 42).move_to(DOWN * 0.45)
        rb = card(10.6, 1.3, stroke=TEAL, sw=4).move_to(DOWN * 2.05)
        rbt = serif("replaced a citation → re-read its sentence", 44).move_to(rb)

        self.go(FadeIn(head), Create(head[0][0]), rt=0.5)
        self.cue("Read", fallback=0.25)
        self.go(Create(l), FadeIn(lt), Create(r), FadeIn(rt_), GrowArrow(da), FadeIn(same), rt=0.6)
        self.cue("replace", fallback=0.65)
        self.go(Create(rb), FadeIn(rbt), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Trust — struck: sounds right · an AI tool says it exists · similar title in search; kept: the record.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Trust(Scene):
    BID = "B06"
    FALLBACK = 11.5
    ROWS = [("sounds right", "sounds", 1.6), ("an AI tool says it exists", "AI", 0.55), ("similar title in search", "similar", -0.5)]

    def construct(self):
        head = sans("what not to trust", 48).move_to(UP * 2.75)
        rows = [serif(t, 46).move_to(LEFT * 4.6 + UP * y, aligned_edge=LEFT) for t, _, y in self.ROWS]
        keep = card(7.4, 1.3, stroke=TEAL, sw=5).move_to(DOWN * 2.0)
        kt = sans("the record itself", 48, TEAL).move_to(keep)
        ok = tick(s=0.5).next_to(keep, RIGHT, buff=0.3)

        self.go(FadeIn(head), rt=0.4)
        for r, (_, w, _), fb in zip(rows, self.ROWS, (0.2, 0.4, 0.62)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r), rt=0.3)
            self.go(Create(strike(r)), rt=0.3)
        self.cue("Only", fallback=0.85)
        self.go(Create(keep), FadeIn(kt), Create(ok), rt=0.4)
        self.finish()
