"""scenes.py — Manim scenes for "Almost Ready to Submit" (ready-to-submit).

Same project as the Week 1–12 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week12/progress-related-work-rebuilt/scenes.py (Week 11 block + `envelope`); Week 9 tick checklist (B01, B06), Week 10 trace table (B02),
Week 11 2×2 panels (B04), Week 4–12 result cards (B03, B05, B07).

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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Clean — clean manuscript checklist; renders at 30 pages; → Professor Gultepe.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Clean(Scene):
    BID = "B01"
    FALLBACK = 15.6
    ROWS = [("tracked changes accepted", "tracked"), ("comment markers removed", "comment"),
            ("2 wording fixes", "two"), ("full verification run", "verification")]

    def construct(self):
        rows = [checkrow(t, None, 2.6 - i * 0.82, xl=-4.6, ls=44) for i, (t, _) in enumerate(self.ROWS)]
        pages = chip("renders at 30 pages", 46, stroke=TEAL).move_to(DOWN * 0.95)
        env = envelope(1.1, 0.72)
        to = serif("to Professor Gultepe for a final review", 44)
        line = VGroup(env, to).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.35)

        for r, (_, w), fb in zip(rows, self.ROWS, (0.1, 0.22, 0.35, 0.45)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), rt=0.35)
        self.cue("30", fallback=0.62)
        self.go(FadeIn(pages), rt=0.4)
        self.cue("Professor", fallback=0.8)
        self.go(Create(env), FadeIn(to), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Requirements — abstract 293 / 300 ✓ · figures and tables 8 / 8 ✓ · body ~7,600 / 6,000 guideline.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Requirements(Scene):
    BID = "B02"
    FALLBACK = 18.3
    X = (-5.5, 0.3, 2.6)

    def construct(self):
        hd = VGroup(*[sans(t, 40, TEAL).move_to(RIGHT * x + UP * 2.5, aligned_edge=LEFT) for t, x in zip(("requirement", "ours", "limit"), self.X)])
        rule = Line(LEFT * 5.7 + UP * 2.1, RIGHT * 5.7 + UP * 2.1, color=SLATE, stroke_width=3)
        spec = [("abstract (words)", "293", "300", True, 1.35, "abstract"), ("figures and tables", "8", "8", True, 0.2, "Eight"),
                ("body (words)", "~7,600", "6,000 guideline", False, -0.95, "body")]
        rows = []
        for lab, ours, lim, ok, y, w in spec:
            g = VGroup(sans(lab, 40).move_to(RIGHT * self.X[0] + UP * y, aligned_edge=LEFT),
                       sans(ours, 46).move_to(RIGHT * self.X[1] + UP * y, aligned_edge=LEFT),
                       serif(lim, 42).move_to(RIGHT * self.X[2] + UP * y, aligned_edge=LEFT))
            if ok:
                g.add(tick(s=0.42).move_to(RIGHT * 5.4 + UP * y))
            rows.append((g, w))
        note = chip("my professor: acceptable", 44, stroke=TEAL).move_to(RIGHT * 1.0 + DOWN * 2.2)

        self.go(FadeIn(hd), Create(rule), rt=0.4)
        for (g, w), fb in zip(rows, (0.12, 0.38, 0.6)):
            self.cue(w, fallback=fb)
            self.go(*[FadeIn(x) for x in g[:3]], *[Create(x) for x in g[3:]], rt=0.4)
        self.cue("acceptable", fallback=0.88)
        self.go(FadeIn(note), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Gaps — three gaps; no fee under Northeastern's agreement.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Gaps(Scene):
    BID = "B03"
    FALLBACK = 12.7
    G = [(("Statement of", "Significance"), "Statement", -4.0), (("graphical", "abstract"), "graphical", 0.0),
         (("generative AI", "declaration"), "declaration", 4.0)]

    def construct(self):
        head = sans("three gaps", 48).move_to(UP * 2.85)
        cards = []
        for k, (lines_, w, x) in enumerate(self.G):
            y = 1.75 - k * 1.15
            b = DashedVMobject(RoundedRectangle(width=9.6, height=0.95, corner_radius=0.16, stroke_color=CRIMSON, stroke_width=4),
                               num_dashes=60).move_to(UP * y)
            t = sans(" ".join(lines_), 44).move_to(UP * y)
            cards.append((VGroup(b, t), w))
        fee = VGroup(serif("no fee under Northeastern's agreement", 44), tick(s=0.42)).arrange(RIGHT, buff=0.35).move_to(DOWN * 2.2)

        self.go(FadeIn(head), rt=0.3)
        for (c, w), fb in zip(cards, (0.08, 0.25, 0.42)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), rt=0.4)
        self.cue("free", fallback=0.75)
        self.go(FadeIn(fee[0]), Create(fee[1]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Drafts — submission materials started (Week 11 2×2 panels).
# ─────────────────────────────────────────────────────────────────────────────
class B04_Drafts(Scene):
    BID = "B04"
    FALLBACK = 11.5
    P = [(("Statement of", "Significance"), "draft", "Statement", -2.95, 1.15), (("graphical abstract",), "outline", "graphical", 2.95, 1.15),
         (("cover letter",), "to the editor", "cover", -2.95, -1.25), (("co-author details",), "ORCIDs, affiliations", "co", 2.95, -1.25)]

    def construct(self):
        cards = []
        for head, sub, w, x, y in self.P:
            b = card(5.75, 2.1, stroke=TEAL, sw=4).move_to(RIGHT * x + UP * y)
            t = VGroup(*[sans(s, 38) for s in head], serif(sub, 44)).arrange(DOWN, buff=0.1).move_to(b)
            cards.append((VGroup(b, t), w))
        for (c, w), fb in zip(cards, (0.1, 0.35, 0.55, 0.72)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Terms — two terminology decisions from standup.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Terms(Scene):
    BID = "B05"
    FALLBACK = 9.9

    def construct(self):
        head = serif("standup: two terminology decisions", 44).move_to(UP * 2.85)
        l = card(5.6, 2.6, stroke=TEAL, sw=4).move_to(LEFT * 2.95 + UP * 0.4)
        lt = VGroup(sans("too_basic", 46), serif("a tag, still ships", 44)).arrange(DOWN, buff=0.25).move_to(l)
        r = card(5.6, 2.6, stroke=TEAL, sw=4).move_to(RIGHT * 2.95 + UP * 0.4)
        rt_ = VGroup(sans("expert review", 44), serif("≠", 52), sans("audit table", 44)).arrange(DOWN, buff=0.12).move_to(r)

        self.go(FadeIn(head), rt=0.4)
        self.cue("too", fallback=0.4)
        self.go(Create(l), FadeIn(lt), rt=0.4)
        self.cue("expert", fallback=0.62)
        self.go(Create(r), FadeIn(rt_), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Record — 13 weeks of reports · GitHub repository · weekly videos; renewal proposed.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Record(Scene):
    BID = "B06"
    FALLBACK = 12.8

    def construct(self):
        r1 = checkrow("reports for all 13 weeks", None, 2.4, xl=-4.6, ls=44)
        r2 = checkrow("repository updated", None, 1.45, xl=-3.7, ls=44)
        gh = ink_logo("github", 0.48).move_to(LEFT * 4.35 + UP * 1.45)
        r2[0].move_to(RIGHT * (-4.6 - 0.55) + UP * 1.45)
        r3 = checkrow("weekly videos", None, 0.5, xl=-4.6, ls=44)
        ren = card(10.4, 1.9, stroke=TEAL, sw=4).move_to(DOWN * 1.65)
        rt_ = VGroup(serif("renewal proposed", 44), sans("Nov 1, 2026 – Feb 20, 2027", 46)).arrange(DOWN, buff=0.18).move_to(ren)

        for r, w, fb, extra in ((r1, "13", 0.15, None), (r2, "GitHub", 0.3, gh), (r3, "videos", 0.45, None)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), *([FadeIn(extra)] if extra else []), rt=0.35)
        self.cue("renewing", fallback=0.7)
        self.go(Create(ren), FadeIn(rt_), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Timeline — Week 1 first draft → Week 13 revised, checked manuscript. (4.8 s: at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B07_Timeline(Scene):
    """Bigger after GATE V underfill (46% < 55%): header + full-width line + larger labels."""
    BID = "B07"
    FALLBACK = 4.8

    def construct(self):
        head = sans("thirteen weeks", 52).move_to(UP * 2.7)
        line = Line(LEFT * 5.0 + UP * 1.0, RIGHT * 5.0 + UP * 1.0, color=SLATE, stroke_width=6)
        d1 = Dot(LEFT * 5.0 + UP * 1.0, radius=0.2, color=SLATE)
        d2 = Dot(RIGHT * 5.0 + UP * 1.0, radius=0.24, color=TEAL)
        a = VGroup(sans("Week 1", 52), serif("first draft", 50)).arrange(DOWN, buff=0.2).move_to(LEFT * 3.7 + DOWN * 0.7)
        b = VGroup(sans("Week 13", 52, TEAL), serif("revised, checked", 50), serif("manuscript", 50)).arrange(DOWN, buff=0.15).move_to(RIGHT * 3.3 + DOWN * 1.0)
        self.go(FadeIn(head), Create(line), FadeIn(d1), FadeIn(d2), FadeIn(a), FadeIn(b), rt=0.5)
        self.cue("revised", fallback=0.6)
        self.go(Create(under(b[2])), rt=0.3)
        self.finish()
