"""scenes.py — Manim scenes for "Why Substring Matching Fails" (substring-vs-exact).

Same project as the Week 1 reels and Week 2's "Writing Someone Else's Pipeline" (hai-videos/2026-08-07-qa-paper-oversell,
hai-videos/Week1/learning-agreement-not-accuracy), so the same visuals: the helpers, the clocked
Beat base (`Scene = Beat`), outline cards and chips, the strike/highlight treatment and the
type sizes that passed GATE T, and Week 2's `cue()` (a reveal lands on a spoken word from
mp3/words.json).

Credit rule: the Wikipedia filter and the substring → exact decision are Thejus's; Janvi documented it.
Every number on screen comes from inbox/week-01/PROJECT_PIPELINE_REPORT.md §4.1 or Janvi's narration.

Channel @HumanitariansAI · humanitarians palette (brands/hai.md): cream ground,
warm ink text, petrol teal = kept/good, burnt orange = struck/bad (never text),
navy slate = structure, amber gold = highlighter fill only (never text).
Type: EB Garamond (serif body) + Montserrat (sans headers).
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


def counter(target, fmt, size, color, pos, tracker):
    """Text counter that runs to `target` as `tracker` goes 0 → 1."""
    def build():
        v = tracker.get_value() * target
        return sans(fmt(v), size, color).move_to(pos)
    return always_redraw(build)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TheTask — ~7 million Wikipedia articles → a list of 468 oncology category terms.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TheTask(Scene):
    BID = "B01"
    FALLBACK = 13.0

    def construct(self):
        pages = VGroup(*[card(2.4, 3.0, stroke=SLATE, sw=2.5).shift(RIGHT * 0.16 * i + UP * 0.16 * i)
                         for i in range(4)])
        pages.move_to(LEFT * 4.25 + UP * 0.4)
        wl = logo("wikipedia", 0.9).move_to(pages[-1])
        p_l1 = sans("English Wikipedia", 30).move_to(LEFT * 4.2 + DOWN * 1.75)
        p_l2 = serif("about 7 million articles", 34).move_to(LEFT * 4.2 + DOWN * 2.45)
        a1 = Arrow(LEFT * 2.75 + UP * 0.4, LEFT * 1.65 + UP * 0.4, buff=0, color=SLATE, stroke_width=4)
        f_box = card(4.4, 3.6, stroke=TEAL, sw=4).move_to(RIGHT * 0.6 + UP * 0.4)
        f_h = sans("468", 54, TEAL).move_to(RIGHT * 0.6 + UP * 1.65)
        f_t = serif("oncology category terms", 34).move_to(RIGHT * 0.6 + UP * 0.95)
        samples = VGroup(chip("cancer", 30), chip("oncology", 30), chip("carcinoma", 30),
                         chip("chemotherapy", 30)).arrange_in_grid(rows=2, cols=2, buff=(0.2, 0.2))
        samples.move_to(RIGHT * 0.6 + DOWN * 0.35)
        a2 = Arrow(RIGHT * 2.9 + UP * 0.4, RIGHT * 3.5 + UP * 0.4, buff=0, color=TEAL, stroke_width=4)
        keep = VGroup(serif("a page stays", 36), serif("if its categories", 36),
                      serif("match the list", 36)).arrange(DOWN, buff=0.1).move_to(RIGHT * 4.8 + UP * 0.4)
        head = serif("The task: pull cancer-related pages out of Wikipedia", 42).move_to(UP * 3.05)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.cue("English", fallback=0.2)
        self.go(LaggedStart(*[FadeIn(p) for p in pages], lag_ratio=0.15), FadeIn(wl), FadeIn(p_l1), rt=0.8)
        self.cue("seven", fallback=0.35)
        self.go(FadeIn(p_l2, shift=UP * 0.1), rt=0.5)
        self.cue("filter", fallback=0.48)
        self.go(GrowArrow(a1), Create(f_box), rt=0.6)
        self.cue("468", fallback=0.58)
        self.go(FadeIn(f_h), FadeIn(f_t), LaggedStart(*[FadeIn(c) for c in samples], lag_ratio=0.2), rt=0.9)
        self.cue("stays", fallback=0.8)
        self.go(GrowArrow(a2), FadeIn(keep, shift=LEFT * 0.15), rt=0.7)
        self.finish()


def rule_card(title, line1, line2, stroke):
    h = sans(title, 32, stroke)
    t = VGroup(serif(line1, 40), serif(line2, 40)).arrange(RIGHT, buff=0.3)
    box = card(min(12.4, max(8.0, t.width + 0.9)), 1.9, stroke=stroke, sw=4)
    VGroup(h, t).arrange(DOWN, buff=0.2).move_to(box)
    return VGroup(box, h, t)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Substring — keep if a term appears anywhere inside a category name → ~81,000.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Substring(Scene):
    BID = "B02"
    FALLBACK = 10.0
    W = 11.0

    def construct(self):
        rule = rule_card("version 1 · substring matching", "term appears anywhere inside a category name",
                         "→ keep", SLATE).move_to(UP * 2.3)
        frame = Rectangle(width=self.W, height=1.0, stroke_color=SLATE, stroke_width=3, fill_opacity=0)
        frame.move_to(DOWN * 0.6)
        bar = Rectangle(width=self.W, height=1.0, fill_color=SLATE, fill_opacity=1, stroke_opacity=0)
        bar.move_to(DOWN * 0.6)
        tr = ValueTracker(0)
        cnt = counter(81000, lambda v: f"~{int(round(v / 1000) * 1000):,}", 64, INK, DOWN * 2.3 + LEFT * 1.6, tr)
        cnt_l = serif("articles kept", 40).move_to(DOWN * 2.3 + RIGHT * 2.6)

        self.go(FadeIn(rule, shift=DOWN * 0.15), rt=0.7)
        self.cue("anywhere", fallback=0.4)
        self.go(rule[2].animate.set_color(SLATE), rt=0.3)
        self.cue("kept", fallback=0.75)
        self.add(cnt)
        self.go(Create(frame), GrowFromEdge(bar, LEFT), tr.animate.set_value(1), FadeIn(cnt_l), rt=1.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Composers — SERS is on the list; the letters s-e-r-s sit inside "Composers".
# ─────────────────────────────────────────────────────────────────────────────
class B03_Composers(Scene):
    BID = "B03"
    FALLBACK = 14.0

    def construct(self):
        term = chip("SERS", 48, stroke=TEAL).move_to(LEFT * 4.2 + UP * 2.3)
        t1 = serif("surface-enhanced Raman spectroscopy", 36).move_to(RIGHT * 1.9 + UP * 2.55)
        t2 = serif("a nanotechnology term on the list", 36, MUTED).move_to(RIGHT * 1.9 + UP * 1.95)
        word = "Composers"
        big = serif(word, 120, sliceable=True).move_to(DOWN * 0.15)
        sub = span(big, word, "sers")
        hl = highlight(sub, opacity=0)
        lab = sans("category name", 30, MUTED).next_to(big, UP, buff=0.25)
        res = serif("pages about composers passed a cancer filter", 42).move_to(DOWN * 2.45)
        res_box = card(res.width + 0.6, res.height + 0.5, stroke=CRIMSON, sw=4).move_to(res)

        self.add(hl)
        self.go(FadeIn(term, scale=0.9), rt=0.6)
        self.cue("surface", fallback=0.15)
        self.go(FadeIn(t1, shift=LEFT * 0.15), rt=0.6)
        self.cue("nanotechnology", fallback=0.33)
        self.go(FadeIn(t2), rt=0.5)
        self.cue("letters", fallback=0.5)
        self.go(FadeIn(lab), FadeIn(big), rt=0.7)
        self.cue("Composers", fallback=0.68)
        self.go(hl.animate.set_fill(GOLD, opacity=0.55), sub.animate.set_color(TEAL), rt=0.6)
        self.cue("pages", fallback=0.8)
        self.go(FadeIn(res, shift=UP * 0.1), Create(res_box), rt=0.7)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Exact — keep only when a category name equals a term → ~81,000 falls to ~10,000.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Exact(Scene):
    BID = "B04"
    FALLBACK = 12.0
    W = 11.0

    def construct(self):
        rule = rule_card("version 2 · exact matching", "category name equals a term on the list",
                         "→ keep", TEAL).move_to(UP * 2.3)
        frame = Rectangle(width=self.W, height=1.0, stroke_color=SLATE, stroke_width=3, fill_opacity=0)
        frame.move_to(DOWN * 0.6)
        old = Rectangle(width=self.W, height=1.0, fill_color=SLATE, fill_opacity=0.45, stroke_opacity=0)
        old.move_to(DOWN * 0.6)
        new = Rectangle(width=self.W * 10 / 81, height=1.0, fill_color=TEAL, fill_opacity=1, stroke_opacity=0)
        new.move_to(frame.get_left(), aligned_edge=LEFT)
        old_l = serif("~81,000 with substring", 34, MUTED).move_to(DOWN * 1.55 + RIGHT * 3.2)
        tr = ValueTracker(0)
        cnt = counter(1, lambda v: f"~{int(round((81000 - v * 71000) / 1000) * 1000):,}", 64, INK,
                      DOWN * 2.45 + LEFT * 3.0, tr)
        cnt_l = serif("articles kept", 40).move_to(DOWN * 2.45 + RIGHT * 0.6)
        fewer = sans("far fewer false matches", 34, TEAL).move_to(DOWN * 3.15 + LEFT * 1.0)

        self.add(frame, old, old_l)
        self.go(FadeIn(rule, shift=DOWN * 0.15), rt=0.7)
        self.cue("cut", fallback=0.5)
        self.add(cnt)
        self.go(FadeIn(cnt_l), GrowFromEdge(new, LEFT), tr.animate.set_value(1), rt=1.4)
        self.cue("fewer", fallback=0.82)
        self.go(FadeIn(fewer, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Trade — catching more vs catching right: wide net vs narrow net (illustration).
# ─────────────────────────────────────────────────────────────────────────────
class B05_Trade(Scene):
    BID = "B05"
    FALLBACK = 13.0
    XS = [-3.4, 3.4]
    # (x, y, real match?) — the same field of pages in both panels; illustrative, not data
    DOTS = [(-1.6, 0.9, 1), (-0.7, 1.2, 0), (0.3, 1.0, 1), (1.3, 0.8, 0), (-1.3, 0.0, 0), (-0.4, 0.25, 1),
            (0.5, 0.1, 1), (1.4, -0.1, 0), (-1.5, -0.9, 1), (-0.5, -0.7, 0), (0.4, -0.9, 0), (1.3, -1.0, 1),
            (0.0, -0.3, 1), (-0.9, 0.6, 0)]

    def field(self, cx):
        dots = VGroup()
        for x, y, ok in self.DOTS:
            d = Circle(0.17, fill_color=TEAL if ok else CRIMSON, fill_opacity=1, stroke_opacity=0)
            d.move_to(RIGHT * (cx + x) + UP * (y + 0.2))
            dots.add(d)
        return dots

    def construct(self):
        head = serif("catching more  vs  catching right", 44).move_to(UP * 3.05)
        f1, f2 = self.field(self.XS[0]), self.field(self.XS[1])
        wide = Ellipse(width=4.6, height=3.3, stroke_color=SLATE, stroke_width=4).move_to(RIGHT * self.XS[0] + UP * 0.2)
        narrow = Ellipse(width=1.7, height=1.25, stroke_color=TEAL, stroke_width=4)
        narrow.move_to(RIGHT * (self.XS[1] + 0.25) + UP * 0.25)
        s_h = sans("Substring", 34).move_to(RIGHT * self.XS[0] + DOWN * 1.95)
        s_t = serif("wide net · many false matches", 36).move_to(RIGHT * self.XS[0] + DOWN * 2.6)
        e_h = sans("Exact", 34, TEAL).move_to(RIGHT * self.XS[1] + DOWN * 1.95)
        e_t = serif("narrow net · few false matches", 36).move_to(RIGHT * self.XS[1] + DOWN * 2.6)
        key = VGroup(Circle(0.12, fill_color=TEAL, fill_opacity=1, stroke_opacity=0), serif("real match", 30),
                     Circle(0.12, fill_color=CRIMSON, fill_opacity=1, stroke_opacity=0), serif("false match", 30),
                     serif("· illustration", 30, MUTED)).arrange(RIGHT, buff=0.2).move_to(UP * 2.35)
        div = Line(UP * 1.9, DOWN * 2.9, color=SLATE, stroke_width=2)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.go(FadeIn(key), Create(div), FadeIn(f1), FadeIn(f2), rt=0.8)
        self.cue("Substring", fallback=0.35)
        self.go(FadeIn(s_h), Create(wide), rt=0.8)
        self.cue("including", fallback=0.6)
        self.go(FadeIn(s_t, shift=UP * 0.1), rt=0.5)
        self.cue("Exact", fallback=0.8)
        self.go(FadeIn(e_h), Create(narrow), FadeIn(e_t, shift=UP * 0.1), rt=0.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — exact matching misses plurals and reworded names; add variants, check drops.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 17.0

    def row(self, y, term, cat, kind):
        t = chip(term, 40, stroke=TEAL).move_to(LEFT * 4.4 + UP * y)
        ne = serif("≠", 52, MUTED).move_to(LEFT * 2.5 + UP * y)
        c = serif(cat, 40).move_to(LEFT * 0.4 + UP * y)
        k = serif(kind, 40, MUTED).move_to(RIGHT * 2.4 + UP * y)
        m = sans("missed", 40, INK).move_to(RIGHT * 4.6 + UP * y)
        x = strike(m, width=5)
        return VGroup(t, ne, c, k), VGroup(m, x)

    def construct(self):
        head = serif("When not to rely on exact matching alone", 44).move_to(UP * 3.05)
        h_l = sans("on the list", 34, MUTED).move_to(LEFT * 4.4 + UP * 2.25)
        h_c = sans("category name", 34, MUTED).move_to(LEFT * 0.4 + UP * 2.25)
        r1, m1 = self.row(1.45, "cancer", "cancers", "a plural")
        r2, m2 = self.row(0.4, "cancer", "Lung cancer", "reworded")
        fix_h = serif("if missing an item is costly:", 40, MUTED).move_to(DOWN * 0.75)
        fixes = VGroup(chip("add the variants you need", 40, stroke=TEAL),
                       chip("check a sample of what was dropped", 40, stroke=TEAL)).arrange(DOWN, buff=0.25)
        fixes.move_to(DOWN * 2.15)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.cue("misses", fallback=0.25)
        self.go(FadeIn(r1), rt=0.7)
        self.cue("plurals", fallback=0.4)
        self.go(FadeIn(m1), Create(m1[1]), rt=0.5)
        self.cue("reworded", fallback=0.5)
        self.go(FadeIn(r2), FadeIn(m2), Create(m2[1]), rt=0.7)
        self.cue("costly", fallback=0.65)
        self.go(FadeIn(fix_h), rt=0.4)
        self.cue("add", fallback=0.72)
        self.go(FadeIn(fixes[0], shift=UP * 0.1), rt=0.5)
        self.cue("check", fallback=0.85)
        self.go(FadeIn(fixes[1], shift=UP * 0.1), rt=0.5)
        self.finish()
