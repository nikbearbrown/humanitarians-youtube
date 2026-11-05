"""scenes.py — Manim scenes for "72 Comments, One Plan" (72-comments).

Same project as the Week 1–9 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week9/progress-fake-citations/scenes.py (Week 8 block + `checkrow`); Week 9 labelled rows (B04, B06), Week 7 sort arrows (B02),
Week 4–9 result cards (B01, B05, B07), Week 9 stamp (B05).

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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Review — Professor Gultepe's second review: 6 big-picture points + 72 comments, every section.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Review(Scene):
    BID = "B01"
    FALLBACK = 12.6
    SECS = ["Introduction", "Methods", "Results", "Discussion"]

    def construct(self):
        top = sans("Professor Gultepe, second review", 46).move_to(UP * 2.8)
        big = chip("6 big-picture points", 44).move_to(LEFT * 3.0 + UP * 1.5)
        com = chip("72 comments", 44).move_to(RIGHT * 3.0 + UP * 1.5)
        secs, fan = [], []
        for i, nm in enumerate(self.SECS):
            x = -4.5 + i * 3.0
            b = card(2.9, 1.0, stroke=SLATE, sw=3).move_to(RIGHT * x + DOWN * 0.45)
            secs.append(VGroup(b, serif(nm, 38).move_to(b)))
            fan.append(Line(RIGHT * 3.0 + UP * 1.0, RIGHT * x + UP * 0.05, color=SLATE, stroke_width=3))
        risk = DashedVMobject(RoundedRectangle(width=11.6, height=1.15, corner_radius=0.16, stroke_color=CRIMSON,
                                               stroke_width=4), num_dashes=60).move_to(DOWN * 2.3)
        rt_ = serif("one pass risks lost content and broken numbers", 44).move_to(risk)

        self.go(FadeIn(top), rt=0.5)
        self.cue("six", fallback=0.25)
        self.go(FadeIn(big), rt=0.4)
        self.cue("72", fallback=0.4)
        self.go(FadeIn(com), *[Create(f) for f in fan], *[FadeIn(s) for s in secs], rt=0.7)
        self.cue("Applying", fallback=0.6)
        self.go(Create(risk), FadeIn(rt_), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Sort — a script extracts 72 comments (anchor text + section) → four types.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Sort(Scene):
    BID = "B02"
    FALLBACK = 13.6
    BINS = [("paper-only edits", "paper"), ("facts to check in the repository", "facts"),
            ("figure work", "figure"), ("tables to build", "tables")]

    def construct(self):
        src = card(4.7, 2.8, stroke=SLATE, sw=3).move_to(LEFT * 3.55 + UP * 0.1)
        st = VGroup(sans("script", 40, TEAL), sans("72 comments", 40), serif("anchor text", 42), serif("+ section", 42)).arrange(DOWN, buff=0.12).move_to(src)
        bins = []
        for i, (t, w) in enumerate(self.BINS):
            y = 1.95 - i * 1.25
            b = card(6.8, 1.0, stroke=TEAL, sw=3).move_to(RIGHT * 2.55 + UP * y)
            a = arrow(LEFT * 1.2 + UP * 0.1, LEFT * 0.85 + UP * y)
            bins.append((VGroup(b, serif(t, 40).move_to(b)), a, w))

        self.go(Create(src), FadeIn(st[0]), rt=0.4)
        self.cue("72", fallback=0.2)
        self.go(FadeIn(st[1:]), rt=0.5)
        for (b, a, w), fb in zip(bins, (0.55, 0.65, 0.78, 0.88)):
            self.cue(w, fallback=fb)
            self.go(GrowArrow(a), Create(b[0]), FadeIn(b[1]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Rules — 6 batched CRITIQ prompts under one shared set of hard rules.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Rules(Scene):
    BID = "B03"
    FALLBACK = 14.9
    RULES = [("no number change without a source", "number"), ("no invented facts", "invented"), ("no em dashes", "em"),
             ("keep every comment", "keep"), ("report OLD text → NEW text", "report")]

    def construct(self):
        head = sans("one shared set of rules", 44).move_to(UP * 3.1)
        box = card(11.6, 3.7, stroke=TEAL, sw=4).move_to(UP * 0.7)
        rows = [checkrow(t, None, 2.0 - i * 0.66, xl=-4.7, ls=38) for i, (t, _) in enumerate(self.RULES)]
        lab = VGroup(sans("6 batched", 38), sans("CRITIQ prompts", 38)).arrange(DOWN, buff=0.08, aligned_edge=LEFT).move_to(LEFT * 5.8 + DOWN * 2.3, aligned_edge=LEFT)
        bat = VGroup(*[VGroup(card(0.8, 0.8, stroke=SLATE, sw=3), sans(str(i + 1), 40)) for i in range(6)])
        for b in bat:
            b[1].move_to(b[0])
        bat.arrange(RIGHT, buff=0.2).move_to(RIGHT * 1.85 + DOWN * 2.3)

        self.go(FadeIn(lab), LaggedStart(*[FadeIn(b) for b in bat], lag_ratio=0.12), rt=0.8)
        self.cue("shared", fallback=0.22)
        self.go(FadeIn(head), Create(box), rt=0.5)
        for r, (_, w), fb in zip(rows, self.RULES, (0.35, 0.5, 0.6, 0.68, 0.78)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), rt=0.35)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Trace — every article count traced to its origin; 71,000 shown only as "no source".
# ─────────────────────────────────────────────────────────────────────────────
class B04_Trace(Scene):
    BID = "B04"
    FALLBACK = 18.9
    ROWS = [("~81,000", "substring matches", "81,000", 0.95), ("10,055", "exact matches", "10,055", -0.25),
            ("10,049", "after 6 duplicates removed", "10,049", -1.45)]

    def construct(self):
        q1 = serif("the step from", 42)
        q2 = sans("71,000", 44)
        q3 = serif("(no source) to 10,000?", 42)
        q = VGroup(q1, q2, q3).arrange(RIGHT, buff=0.25).move_to(UP * 2.8)
        tag = Line(q2.get_corner(DL) + DOWN * 0.1, q2.get_corner(DR) + DOWN * 0.1, color=CRIMSON, stroke_width=5)
        hd = VGroup(serif("count", 38).move_to(LEFT * 5.4 + UP * 1.85, aligned_edge=LEFT),
                    serif("origin", 38).move_to(LEFT * 1.8 + UP * 1.85, aligned_edge=LEFT))
        rule = Line(LEFT * 5.6 + UP * 1.5, RIGHT * 5.6 + UP * 1.5, color=SLATE, stroke_width=3)
        rows = []
        for v, s, w, y in self.ROWS:
            rows.append((VGroup(sans(v, 46).move_to(LEFT * 5.4 + UP * y, aligned_edge=LEFT),
                                serif(s, 42).move_to(LEFT * 1.8 + UP * y, aligned_edge=LEFT),
                                tick(s=0.42).move_to(RIGHT * 5.3 + UP * y)), w))

        self.go(FadeIn(q), Create(tag), rt=0.5)
        self.cue("traced", fallback=0.3)
        self.go(FadeIn(hd), Create(rule), rt=0.4)
        for (r, w), fb in zip(rows, (0.45, 0.62, 0.78)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[0]), FadeIn(r[1]), Create(r[2]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Unsourced — 71,000: only in the manuscript, no data source; derived; → do-not-use list.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Unsourced(Scene):
    BID = "B05"
    FALLBACK = 14.8

    def construct(self):
        box = card(11.2, 1.3, stroke=CRIMSON, sw=4).move_to(UP * 2.5)
        bt = VGroup(sans("71,000", 50), serif("only in the manuscript", 44)).arrange(RIGHT, buff=0.6).move_to(box)
        st = stamp("no data source", 5.0).move_to(RIGHT * 3.2 + UP * 0.95)
        der = serif("derived: ~81,000 minus ~10,000", 42).move_to(LEFT * 5.5 + DOWN * 0.05, aligned_edge=LEFT)
        s0 = serif("status:", 42).move_to(LEFT * 5.5 + DOWN * 1.05, aligned_edge=LEFT)
        s1 = serif("Verified", 42).next_to(s0, RIGHT, buff=0.3)
        s2 = serif("→", 42).next_to(s1, RIGHT, buff=0.3)
        s3 = sans("Unsourced", 42).next_to(s2, RIGHT, buff=0.3)
        dnu = card(8.2, 1.25, stroke=SLATE, sw=3).move_to(DOWN * 2.4)
        dt = VGroup(sans("do not use", 42), serif("71,000", 44)).arrange(RIGHT, buff=0.6).move_to(dnu)

        self.go(Create(box), FadeIn(bt), rt=0.5)
        self.go(Create(st[0]), FadeIn(st[1]), rt=0.4)
        self.cue("subtraction", fallback=0.25)
        self.go(FadeIn(der), rt=0.4)
        self.cue("verified", fallback=0.52)
        self.go(FadeIn(s0), FadeIn(s1), rt=0.3)
        self.go(Create(strike(s1)), FadeIn(s2), FadeIn(s3), rt=0.4)
        self.cue("do", fallback=0.75)
        self.go(Create(dnu), FadeIn(dt), Create(strike(dt[1])), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Repo — answers only the code could give.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Repo(Scene):
    BID = "B06"
    FALLBACK = 17.3
    FACTS = [("artifact checker", "rule-based, up to 2 retries", "artifact", 1.55),
             ("generation model", "GPT-4o-mini", "generation", 0.0),
             ("GO gate", "3 categories set, 2 reachable", "Gene", -1.55)]

    def construct(self):
        head = serif("answers only the code could give", 42).move_to(UP * 2.95)
        cards = []
        for lab, val, w, y in self.FACTS:
            b = card(11.7, 1.25, stroke=SLATE, sw=3).move_to(UP * y)
            l = sans(lab, 38).move_to(LEFT * 5.5 + UP * y, aligned_edge=LEFT)
            v = serif(val, 40).move_to(LEFT * 0.2 + UP * y, aligned_edge=LEFT)
            if w == "generation":
                v = VGroup(ink_logo("openai", 0.5), sans(val, 42)).arrange(RIGHT, buff=0.25).move_to(LEFT * 0.2 + UP * y, aligned_edge=LEFT)
            cards.append((VGroup(b, l, v), w))

        self.go(FadeIn(head), rt=0.4)
        for (c, w), fb in zip(cards, (0.25, 0.5, 0.7)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), FadeIn(c[2]), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Batches — batches 1 terminology · 2 structure · 3 line-level fixes; 2 CRITIQ errors caught.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Batches(Scene):
    BID = "B07"
    FALLBACK = 10.7
    B = [("1", "terminology", "terminology", -4.0), ("2", "structure", "structure", 0.0), ("3", "line-level fixes", "line", 4.0)]

    def construct(self):
        head = serif("the first three batches", 42).move_to(UP * 2.9)
        cards = []
        for n, t, w, x in self.B:
            b = card(3.8, 2.0, stroke=TEAL, sw=4).move_to(RIGHT * x + UP * 1.0)
            tt = VGroup(sans(n, 56, TEAL), serif(t, 42)).arrange(DOWN, buff=0.15).move_to(b)
            cards.append((VGroup(b, tt), w))
        err = card(11.0, 1.3, stroke=CRIMSON, sw=4).move_to(DOWN * 1.6)
        et = VGroup(sans("2 errors CRITIQ introduced:", 40), serif("caught", 44)).arrange(RIGHT, buff=0.35)
        ok = tick(s=0.45)
        VGroup(et, ok).arrange(RIGHT, buff=0.4).move_to(err)

        self.go(FadeIn(head), rt=0.4)
        for (c, w), fb in zip(cards, (0.25, 0.32, 0.42)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), rt=0.4)
        self.cue("two", fallback=0.75)
        self.go(Create(err), FadeIn(et), Create(ok), rt=0.5)
        self.finish()
