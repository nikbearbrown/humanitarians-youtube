"""scenes.py — Manim scenes for "Keep Your Terms Distinct" (keep-terms-distinct).

Same project as the Week 1–12 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week13/progress-ready-to-submit/scenes.py (Week 12 block); its B05 split term cards (B03, B04),
Week 13 dashed rows (B04), Week 4–13 result cards (B02, B05, B06).

Every number on screen appears in inbox/term2-week13/term2-week13-video-content.md as written.
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


def envelope(w=0.95, h=0.62, color=SLATE):
    return VGroup(Rectangle(width=w, height=h, stroke_color=color, stroke_width=3, fill_opacity=0),
                  VMobject(stroke_color=color, stroke_width=3).set_points_as_corners(
                      [LEFT * w / 2 + UP * h / 2, DOWN * h * 0.08, RIGHT * w / 2 + UP * h / 2]))


def link(a, b, color=SLATE):
    """Fixed-coordinate connector between two points."""
    return Line(a, b, color=color, stroke_width=3)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Names — one idea, three names; two ideas, one name.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Names(Scene):
    """Simplified after two GATE T fails (contrast, then label overlap): two large text cards."""
    BID = "B01"
    FALLBACK = 9.7

    def construct(self):
        a = card(10.0, 1.5, stroke=SLATE, sw=3).move_to(UP * 1.6)
        at = VGroup(sans("one idea", 50), serif("→ many names", 48)).arrange(RIGHT, buff=0.5).move_to(a)
        b = card(10.0, 1.5, stroke=SLATE, sw=3).move_to(DOWN * 0.3)
        bt = VGroup(sans("two ideas", 50), serif("→ one name", 48)).arrange(RIGHT, buff=0.5).move_to(b)
        cap = serif("readers notice, and reviewers do too", 46).move_to(DOWN * 2.3)

        self.cue("same", fallback=0.1)
        self.go(Create(a), FadeIn(at), rt=0.5)
        self.cue("ideas", fallback=0.4)
        self.go(Create(b), FadeIn(bt), rt=0.5)
        self.cue("Readers", fallback=0.75)
        self.go(FadeIn(cap), Create(under(cap)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Paragraph — a terminology paragraph: 13 terms, defined up front.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Paragraph(Scene):
    BID = "B02"
    FALLBACK = 8.3

    def construct(self):
        box = card(10.4, 1.9, stroke=TEAL, sw=4).move_to(UP * 2.0)
        bt = VGroup(sans("terminology paragraph", 46), serif("13 terms, defined up front", 46)).arrange(DOWN, buff=0.15).move_to(box)
        sq = VGroup(*[Square(side_length=0.6, stroke_color=SLATE, stroke_width=3) for _ in range(13)]).arrange(RIGHT, buff=0.18).move_to(DOWN * 0.1)
        same = VGroup(tick(s=0.45), sans("each used the same way everywhere", 44)).arrange(RIGHT, buff=0.35).move_to(DOWN * 1.8)

        self.go(Create(box), FadeIn(bt[0]), rt=0.5)
        self.cue("13", fallback=0.35)
        self.go(FadeIn(bt[1]), LaggedStart(*[Create(s) for s in sq], lag_ratio=0.08), rt=0.9)
        self.cue("same", fallback=0.75)
        self.go(Create(same[0]), FadeIn(same[1]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Basic — too_basic: the tag (a judgment) vs shipping anyway (a policy).
# ─────────────────────────────────────────────────────────────────────────────
class B03_Basic(Scene):
    BID = "B03"
    FALLBACK = 15.8

    def construct(self):
        head = sans("too_basic", 52).move_to(UP * 2.8)
        l = card(5.3, 2.6, stroke=TEAL, sw=4).move_to(LEFT * 3.15 + UP * 0.5)
        lt = VGroup(sans("a tag", 48), serif("a judgment", 46)).arrange(DOWN, buff=0.2).move_to(l)
        r = card(5.3, 2.6, stroke=SLATE, sw=4).move_to(RIGHT * 3.15 + UP * 0.5)
        rt_ = VGroup(sans("still ships", 48), serif("a policy", 46), serif("for undergraduates", 42)).arrange(DOWN, buff=0.15).move_to(r)
        neq = sans("≠", 60).move_to(UP * 0.5)
        cap = serif("the paper keeps the two apart", 46).move_to(DOWN * 2.2)

        self.go(FadeIn(head), Create(under(head)), rt=0.4)
        self.cue("tag", fallback=0.2)
        self.go(Create(l), FadeIn(lt[0]), rt=0.4)
        self.cue("ship", fallback=0.35)
        self.go(Create(r), FadeIn(rt_[0]), FadeIn(rt_[2]), rt=0.4)
        self.cue("separates", fallback=0.6)
        self.go(FadeIn(lt[1]), FadeIn(rt_[1]), FadeIn(neq), FadeIn(cap), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Review — expert review = people with domain expertise; audit table = automated scores.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Review(Scene):
    BID = "B04"
    FALLBACK = 15.6

    def construct(self):
        l = card(5.3, 2.6, stroke=TEAL, sw=4).move_to(LEFT * 3.15 + UP * 1.2)
        lt = VGroup(sans("expert review", 46), serif("people with", 44), serif("domain expertise", 44)).arrange(DOWN, buff=0.12).move_to(l)
        r = card(5.3, 2.6, stroke=SLATE, sw=4).move_to(RIGHT * 3.15 + UP * 1.2)
        rt_ = VGroup(sans("audit table", 46), serif("automated scores", 44)).arrange(DOWN, buff=0.2).move_to(r)
        neq = sans("≠", 60).move_to(UP * 1.2)
        warn = DashedVMobject(RoundedRectangle(width=11.4, height=1.3, corner_radius=0.16, stroke_color=CRIMSON, stroke_width=4),
                              num_dashes=60).move_to(DOWN * 1.6)
        wt = serif("mixed up, scoring sounds like human judgment", 44).move_to(warn)

        self.cue("Expert", nth=2, fallback=0.2)
        self.go(Create(l), FadeIn(lt), rt=0.5)
        self.cue("audit", nth=2, fallback=0.5)
        self.go(Create(r), FadeIn(rt_), FadeIn(neq), rt=0.5)
        self.cue("Mixing", fallback=0.72)
        self.go(Create(warn), FadeIn(wt), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Rule — one name per idea · one idea per name.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Rule(Scene):
    BID = "B05"
    FALLBACK = 7.9

    def construct(self):
        box = card(10.6, 2.8, stroke=TEAL, sw=5).move_to(UP * 1.0)
        t = VGroup(sans("one name per idea", 54), sans("one idea per name", 54)).arrange(DOWN, buff=0.3).move_to(box)
        cap = serif("close? define both and say how they differ", 44).move_to(DOWN * 1.8)
        self.go(Create(box), FadeIn(t[0]), rt=0.5)
        self.cue("one", nth=2, fallback=0.25)
        self.go(FadeIn(t[1]), rt=0.4)
        self.cue("close", fallback=0.55)
        self.go(FadeIn(cap), Create(under(cap)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — standard term → use it; renaming mid-project → update every mention.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 10.8

    def construct(self):
        head = serif("when not to force it", 46).move_to(UP * 2.95)
        a = card(11.0, 1.8, stroke=SLATE, sw=3).move_to(UP * 1.1)
        at = VGroup(serif("your field already has a standard term", 44), sans("use it", 46, TEAL)).arrange(DOWN, buff=0.15).move_to(a)
        b = card(11.0, 1.8, stroke=SLATE, sw=3).move_to(DOWN * 1.1)
        bt = VGroup(serif("renaming mid-project", 44), sans("update every mention", 46, TEAL)).arrange(DOWN, buff=0.15).move_to(b)

        self.go(FadeIn(head), rt=0.4)
        self.cue("standard", fallback=0.25)
        self.go(Create(a), FadeIn(at), rt=0.5)
        self.cue("rename", fallback=0.65)
        self.go(Create(b), FadeIn(bt), rt=0.5)
        self.finish()
