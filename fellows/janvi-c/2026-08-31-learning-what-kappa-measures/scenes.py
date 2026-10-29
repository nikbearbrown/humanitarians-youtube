"""scenes.py — Manim scenes for "What Kappa Actually Measures" (what-kappa-measures).

Same helper block as this week's progress reel (hai-videos/Week5/progress-kappa), Week 1–4 lineage.
B03's segmented bar follows Week 1 B04_Triage; B05's table follows Week 3 B02_FiveOptions.
The formula is plain text (no LaTeX/MathTex). Every number on screen appears in
inbox/term2-week05/term2-week5-video-content.md as written (B01 is an unnumbered illustration).
WORDING LAW: kappa is agreement corrected for chance, never accuracy.

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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_BlindJudges — two judges tag without reading; most items share one tag; they still agree.
# ─────────────────────────────────────────────────────────────────────────────
class B01_BlindJudges(Scene):
    BID = "B01"
    FALLBACK = 12.0
    A = [1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
    B = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]

    def judge(self, name, x):
        box = card(4.6, 1.35, stroke=SLATE, sw=3).move_to(RIGHT * x + UP * 2.2)
        t = VGroup(sans(name, 36), serif("tags without reading", 32)).arrange(DOWN, buff=0.1).move_to(box)
        return VGroup(box, t)

    def row(self, marks, y):
        sq = VGroup(*[RoundedRectangle(width=0.62, height=0.62, corner_radius=0.1,
                                       fill_color=TEAL if m else SLATE, fill_opacity=1, stroke_opacity=0)
                      for m in marks]).arrange(RIGHT, buff=0.22)
        return sq.move_to(RIGHT * 0.6 + UP * y)

    def construct(self):
        ja, jb = self.judge("judge A", -3.1), self.judge("judge B", 3.1)
        ra, rb = self.row(self.A, 0.75), self.row(self.B, -0.05)
        la = sans("A", 34).next_to(ra, LEFT, buff=0.35)
        lb = sans("B", 34).next_to(rb, LEFT, buff=0.35)
        frame = Rectangle(width=9.0, height=0.6, stroke_color=SLATE, stroke_width=3, fill_opacity=0).move_to(DOWN * 1.85)
        fill = Rectangle(width=9.0 * 0.8, height=0.6, fill_color=TEAL, fill_opacity=1, stroke_opacity=0)
        fill.move_to(frame.get_left(), aligned_edge=LEFT)
        f_lab = serif("raw agreement (illustration)", 34).next_to(frame, LEFT, buff=0.3).shift(UP * 0.0)
        f_lab.next_to(frame, UP, buff=0.12).align_to(frame, LEFT)
        cap = serif("Raw agreement can't tell this apart from real agreement.", 38).move_to(DOWN * 2.85)

        self.go(Create(ja[0]), FadeIn(ja[1]), Create(jb[0]), FadeIn(jb[1]), rt=0.7)
        self.cue("most", fallback=0.3)
        self.go(FadeIn(la), LaggedStart(*[FadeIn(s) for s in ra], lag_ratio=0.08), rt=0.8)
        self.go(FadeIn(lb), LaggedStart(*[FadeIn(s) for s in rb], lag_ratio=0.08), rt=0.8)
        self.cue("agree", fallback=0.55)
        self.go(Create(frame), FadeIn(f_lab), rt=0.4)
        self.go(GrowFromEdge(fill, LEFT), rt=0.9)
        self.cue("Raw", fallback=0.75)
        self.go(FadeIn(cap, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Formula — kappa = (observed − chance) ÷ (1 − chance), plain text; 0 = chance, 1 = perfect.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Formula(Scene):
    BID = "B02"
    FALLBACK = 15.0

    def construct(self):
        head = serif("Kappa fixes this", 44).move_to(UP * 2.95)
        parts = [serif("kappa =", 50), serif("(observed", 50), serif("− chance)", 50), serif("÷", 50), serif("(1 − chance)", 50)]
        f = VGroup(*parts).arrange(RIGHT, buff=0.3).move_to(UP * 1.45)
        box = card(f.width + 0.8, 1.5, stroke=SLATE, sw=3).move_to(f)
        gain = serif("the most you could gain over chance", 34).move_to(RIGHT * 2.5 + UP * 0.3)
        scale = Line(LEFT * 3.8 + DOWN * 1.35, RIGHT * 3.8 + DOWN * 1.35, color=SLATE, stroke_width=4)
        t0 = Line(LEFT * 3.8 + DOWN * 1.15, LEFT * 3.8 + DOWN * 1.55, color=SLATE, stroke_width=4)
        t1 = Line(RIGHT * 3.8 + DOWN * 1.15, RIGHT * 3.8 + DOWN * 1.55, color=SLATE, stroke_width=4)
        z = VGroup(sans("0", 44), serif("no better than chance", 36)).arrange(DOWN, buff=0.12).next_to(t0, DOWN, buff=0.15)
        o = VGroup(sans("1", 44, TEAL), serif("perfect agreement", 36)).arrange(DOWN, buff=0.12).next_to(t1, DOWN, buff=0.15)

        self.go(FadeIn(head), Create(box), FadeIn(parts[0]), rt=0.6)
        self.cue("observed", fallback=0.15)
        self.go(FadeIn(parts[1]), rt=0.3)
        self.cue("subtract", fallback=0.25)
        self.go(FadeIn(parts[2]), rt=0.3)
        self.cue("divide", fallback=0.45)
        self.go(FadeIn(parts[3]), FadeIn(parts[4]), rt=0.4)
        self.cue("most", fallback=0.5)
        self.go(FadeIn(gain), rt=0.4)
        self.cue("Zero", fallback=0.72)
        self.go(Create(scale), Create(t0), Create(t1), FadeIn(z), rt=0.6)
        self.cue("One", fallback=0.88)
        self.go(FadeIn(o), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_BaseRates — keyword base rates 45.0 / 33.0 / 11.9 / 10.2%; chance agreement about 67%.
#  (Week 1 B04_Triage segmented bar.)
# ─────────────────────────────────────────────────────────────────────────────
class B03_BaseRates(Scene):
    BID = "B03"
    FALLBACK = 13.0
    W, X0, Y = 11.0, -5.5, 0.55
    SEGS = [("approved", 45.0, TEAL), ("supplementary", 33.0, SLATE), ("too_basic", 11.9, MUTED), ("junk", 10.2, GOLD)]

    def construct(self):
        head = serif("Keyword base rates · 26,901 tag assignments", 38).move_to(UP * 2.95)
        segs, x = [], self.X0
        for name, pct, col in self.SEGS:
            w = self.W * pct / 100.1
            r = Rectangle(width=w, height=1.1, fill_color=col, fill_opacity=1, stroke_opacity=0)
            r.move_to(RIGHT * x + UP * self.Y, aligned_edge=LEFT)
            segs.append(r)
            x += w
        frame = Rectangle(width=self.W, height=1.1, stroke_color=SLATE, stroke_width=3, fill_opacity=0)
        frame.move_to(RIGHT * (self.X0 + self.W / 2) + UP * self.Y)
        lab = [serif("approved 45.0%", 36).next_to(segs[0], DOWN, buff=0.25),
               serif("supplementary 33.0%", 36).next_to(segs[1], DOWN, buff=0.25),
               serif("too_basic 11.9%", 34).next_to(segs[2], UP, buff=0.25),
               serif("junk 10.2%", 34).next_to(segs[3], DOWN, buff=0.25).shift(RIGHT * 0.1)]
        lab[3].align_to(frame, RIGHT)
        chance = chip("chance agreement: about 67%", 42, stroke=TEAL).move_to(DOWN * 2.2)

        self.go(FadeIn(head), Create(frame), rt=0.5)
        self.cue("45", fallback=0.3)
        self.go(GrowFromEdge(segs[0], LEFT), FadeIn(lab[0]), rt=0.6)
        self.cue("33", fallback=0.45)
        self.go(GrowFromEdge(segs[1], LEFT), FadeIn(lab[1]), rt=0.6)
        self.go(GrowFromEdge(segs[2], LEFT), FadeIn(lab[2]), GrowFromEdge(segs[3], LEFT), FadeIn(lab[3]), rt=0.6)
        self.cue("chance", nth=2, fallback=0.8)
        self.go(FadeIn(chance, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_FleissCohen — 94.2% raw → Fleiss' kappa 0.49; Fleiss = 3+ raters, Cohen = one pair.
# ─────────────────────────────────────────────────────────────────────────────
class B04_FleissCohen(Scene):
    BID = "B04"
    FALLBACK = 11.0

    def construct(self):
        l = VGroup(sans("94.2%", 90), serif("raw agreement", 38)).arrange(DOWN, buff=0.15).move_to(LEFT * 3.4 + UP * 1.3)
        r = VGroup(sans("0.49", 90, TEAL), serif("Fleiss' kappa", 38)).arrange(DOWN, buff=0.15).move_to(RIGHT * 3.4 + UP * 1.3)
        a = arrow(LEFT * 0.9 + UP * 1.5, RIGHT * 0.9 + UP * 1.5)
        fb = card(5.6, 1.9, stroke=TEAL, sw=3).move_to(LEFT * 3.05 + DOWN * 1.6)
        ft = VGroup(sans("Fleiss' kappa", 36), serif("three or more raters at once", 34)).arrange(DOWN, buff=0.15).move_to(fb)
        cb = card(5.6, 1.9, stroke=SLATE, sw=3).move_to(RIGHT * 3.05 + DOWN * 1.6)
        ct = VGroup(sans("Cohen's kappa", 36), serif("one pair at a time", 34)).arrange(DOWN, buff=0.15).move_to(cb)

        self.go(FadeIn(l), rt=0.5)
        self.cue("became", fallback=0.25)
        self.go(GrowArrow(a), FadeIn(r, shift=LEFT * 0.1), rt=0.6)
        self.cue("handles", fallback=0.55)
        self.go(Create(fb), FadeIn(ft), rt=0.5)
        self.cue("Cohen's", fallback=0.78)
        self.go(Create(cb), FadeIn(ct), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Pairwise — who agrees with whom (exact source values). (Week 3 B02 table rows.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Pairwise(Scene):
    BID = "B05"
    FALLBACK = 10.0
    ROWS = [("mistral", "claude", "Mistral – Claude", "0.6559", TEAL),
            ("mistral", "openai", "Mistral – GPT-4o-mini", "0.4251", INK),
            ("openai", "claude", "GPT-4o-mini – Claude", "0.4022", INK)]
    YS = [1.35, 0.2, -0.95]

    def construct(self):
        head = serif("Who agrees with whom", 44).move_to(UP * 3.0)
        h1 = sans("pair", 34).move_to(LEFT * 5.6 + UP * 2.2, aligned_edge=LEFT)
        h2 = sans("Cohen's kappa", 34).move_to(RIGHT * 3.6 + UP * 2.2)
        top = Line(LEFT * 5.8 + UP * 1.85, RIGHT * 5.8 + UP * 1.85, color=SLATE, stroke_width=2)
        rows, seps = [], []
        for (a, b, name, v, col), y in zip(self.ROWS, self.YS):
            lab = VGroup(ink_logo(a, 0.45), ink_logo(b, 0.45), serif(name, 38)).arrange(RIGHT, buff=0.22)
            lab.move_to(LEFT * 5.6 + UP * y, aligned_edge=LEFT)
            val = sans(v, 46, col).move_to(RIGHT * 3.6 + UP * y)
            rows.append(VGroup(lab, val))
            seps.append(Line(LEFT * 5.8 + UP * (y - 0.57), RIGHT * 5.8 + UP * (y - 0.57), color=MUTED, stroke_width=1.5))
        foot = serif("each pair with GPT-4o-mini: near 0.4", 38).move_to(DOWN * 2.35)

        self.go(FadeIn(head), FadeIn(h1), FadeIn(h2), Create(top), rt=0.5)
        self.cue("Mistral", fallback=0.4)
        self.go(FadeIn(rows[0]), Create(seps[0]), rt=0.5)
        self.cue("each", fallback=0.65)
        self.go(FadeIn(rows[1]), Create(seps[1]), FadeIn(rows[2]), Create(seps[2]), rt=0.6)
        self.cue("near", fallback=0.88)
        self.go(FadeIn(foot), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — kappa is agreement, not accuracy; a shared mistake still scores high.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 15.0

    def construct(self):
        l1 = sans("kappa: agreement, corrected for chance", 40).move_to(UP * 2.7)
        l2 = serif("It doesn't tell you whether anyone is right.", 40).move_to(UP * 1.8)
        ys = [0.75, 0.0, -0.75]
        judges = [ink_logo(n, 0.5).move_to(LEFT * 4.9 + UP * y) for n, y in zip(("mistral", "openai", "claude"), ys)]
        arrows = [arrow(LEFT * 4.4 + UP * y, LEFT * 1.9 + UP * y * 0.3) for y in ys]
        m_box = card(3.4, 1.3, stroke=CRIMSON, sw=4).move_to(LEFT * 0.0)
        m_t = serif("the same mistake", 38).move_to(m_box)
        a2 = arrow(RIGHT * 1.8, RIGHT * 2.6)
        hi = VGroup(sans("kappa:", 38), sans("still high", 38)).arrange(DOWN, buff=0.1).move_to(RIGHT * 4.1)
        cap = serif("moderate, substantial: conventions, not laws", 38).move_to(DOWN * 2.4)
        u = under(cap)

        self.go(FadeIn(l1), rt=0.5)
        self.cue("right", fallback=0.12)
        self.go(FadeIn(l2), rt=0.4)
        self.cue("Three", fallback=0.42)
        self.go(*[FadeIn(j) for j in judges], *[GrowArrow(a) for a in arrows], Create(m_box), FadeIn(m_t), rt=0.7)
        self.cue("high", fallback=0.62)
        self.go(GrowArrow(a2), FadeIn(hi), rt=0.4)
        self.cue("labels", fallback=0.75)
        self.go(FadeIn(cap), Create(u), rt=0.5)
        self.finish()
