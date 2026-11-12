"""scenes.py — Manim scenes for "Related Work, Rebuilt" (related-work-rebuilt).

Same project as the Week 1–11 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week11/progress-figures-for-print/scenes.py (Week 10 block); its B01 quote card (B01), Week 9 tick checklist (B06), Week 10 labelled rows (B03),
Week 10 envelope (B07), Week 4–11 result cards (B04, B05).

Every number on screen appears in inbox/term2-week12/term2-week12-video-content.md as written.
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
#  B01_Quote — "Related Work describes your own system instead of prior work." (Week 11 B01.)
# ─────────────────────────────────────────────────────────────────────────────
class B01_Quote(Scene):
    BID = "B01"
    FALLBACK = 6.8

    def construct(self):
        box = card(11.6, 3.2, stroke=SLATE, sw=3).move_to(UP * 0.4)
        q = VGroup(serif("“Related Work describes your own system", 48),
                   serif("instead of prior work.”", 48)).arrange(DOWN, buff=0.15).move_to(box).shift(UP * 0.4)
        who = sans("Professor Gultepe", 42).move_to(box).shift(DOWN * 0.95)
        self.go(Create(box), FadeIn(q), FadeIn(who), rt=0.5)
        self.cue("prior", fallback=0.8)
        self.go(Create(under(q[1])), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Search — five sources → 12 new references, each checked on its publisher's page.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Search(Scene):
    BID = "B02"
    FALLBACK = 18.1

    def construct(self):
        r1 = VGroup(*[chip(s, 42) for s in ("Google Scholar", "ACL Anthology", "PubMed")]).arrange(RIGHT, buff=0.35).move_to(UP * 2.75)
        r2 = VGroup(*[chip(s, 42) for s in ("NeurIPS", "arXiv")]).arrange(RIGHT, buff=0.35).move_to(UP * 1.8)
        ar = arrow(UP * 1.25, UP * 0.65)
        box = card(7.0, 1.2, stroke=TEAL, sw=4).move_to(UP * 0.0)
        bt = sans("12 new references", 50).move_to(box)
        chk = VGroup(serif("each checked on its publisher's page", 44), tick(s=0.42)).arrange(RIGHT, buff=0.35).move_to(DOWN * 1.4)
        rule = sans("no unverified citation goes in", 44).move_to(DOWN * 2.55)

        self.go(LaggedStart(*[FadeIn(c) for c in [*r1, *r2]], lag_ratio=0.2), rt=1.0)
        self.cue("12", fallback=0.35)
        self.go(GrowArrow(ar), Create(box), FadeIn(bt), rt=0.5)
        self.cue("checked", fallback=0.62)
        self.go(FadeIn(chk[0]), Create(chk[1]), rt=0.4)
        self.cue("No", fallback=0.85)
        self.go(FadeIn(rule), Create(under(rule)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Refs — five key new references and what each covers.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Refs(Scene):
    BID = "B03"
    FALLBACK = 12.6
    ROWS = [(["Remy 2023"], "closest prior work", "closest", 2.65),
            (["Panickssery 2024"], "LLM self-evaluation", "self", 1.65),
            (["Ji 2023"], "hallucination", "hallucination", 0.7),
            (["Feinstein &", "Cicchetti 1990"], "kappa interpretation", "kappa", -0.5),
            (["Wilson 1927"], "Wilson interval", "Wilson", -1.75)]

    def construct(self):
        rows = []
        for names, note, w, y in self.ROWS:
            n = VGroup(*[sans(t, 40) for t in names]).arrange(DOWN, buff=0.08, aligned_edge=LEFT).move_to(RIGHT * -5.6 + UP * y, aligned_edge=LEFT)
            t = serif(note, 44).move_to(RIGHT * 1.0 + UP * y, aligned_edge=LEFT)
            rows.append((VGroup(n, t, tick(s=0.34).move_to(RIGHT * 0.2 + UP * y)), w))
        rule = Line(RIGHT * 0.7 + UP * 3.1, RIGHT * 0.7 + DOWN * 2.3, color=SLATE, stroke_width=3)

        self.go(Create(rule), rt=0.3)
        for (r, w), fb in zip(rows, (0.08, 0.5, 0.62, 0.72, 0.85)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[0]), FadeIn(r[1]), Create(r[2]), rt=0.35)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Shows — one line on what each paper shows, so CRITIQ can't overstate it; 36 references.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Shows(Scene):
    BID = "B04"
    FALLBACK = 9.9

    def construct(self):
        ex = card(11.0, 1.9, stroke=SLATE, sw=3).move_to(UP * 2.0)
        et = VGroup(sans("Remy 2023", 42), serif("shows: LLM-generated glossaries", 44)).arrange(DOWN, buff=0.15).move_to(ex)
        why = serif("so CRITIQ can't overstate it", 46).move_to(UP * 0.1)
        tot = card(9.4, 1.5, stroke=TEAL, sw=4).move_to(DOWN * 1.8)
        tt = VGroup(sans("36 references", 50), serif("all checked", 46)).arrange(RIGHT, buff=0.5)
        ok = tick(s=0.45)
        VGroup(tt, ok).arrange(RIGHT, buff=0.35).move_to(tot)

        self.go(Create(ex), FadeIn(et), rt=0.5)
        self.cue("CRITIQ", fallback=0.4)
        self.go(FadeIn(why), rt=0.4)
        self.cue("36", fallback=0.72)
        self.go(Create(tot), FadeIn(tt), Create(ok), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Spelling — old spelling (not shown) → Medhavy, throughout. (4.3 s: shown at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Spelling(Scene):
    """No strike through text (GATE T §8.1 measured the struck run at 35 px): a separate cross instead."""
    BID = "B05"
    FALLBACK = 4.3

    def construct(self):
        old = sans("old spelling", 48).move_to(LEFT * 3.4 + UP * 0.6)
        x = VGroup(Line(UL * 0.3, DR * 0.3, color=CRIMSON, stroke_width=7),
                   Line(DL * 0.3, UR * 0.3, color=CRIMSON, stroke_width=7)).move_to(LEFT * 3.4 + UP * 1.55)
        ar = arrow(LEFT * 1.0 + UP * 0.6, RIGHT * 0.5 + UP * 0.6)
        new = sans("Medhavy", 64, TEAL).move_to(RIGHT * 3.0 + UP * 0.6)
        cap = serif("throughout the paper", 48).move_to(DOWN * 1.4)
        self.go(FadeIn(old), Create(x), GrowArrow(ar), FadeIn(new), FadeIn(cap), rt=0.5)
        self.cue("Medhavy", fallback=0.6)
        self.go(Create(under(new)), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Check — scripted final check, six ticks.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Check(Scene):
    BID = "B06"
    FALLBACK = 15.3
    ROWS = [("72 comments addressed", "72"), ("zero numbers lost", "lost"), ("8 items in order", "eight"),
            ("every reference cited and present", "every"), ("abstract: 293 words", "293"), ("retired values absent", "retired")]

    def construct(self):
        head = sans("scripted final check", 46).move_to(UP * 3.0)
        rows = [checkrow(t, None, 2.0 - i * 0.78, xl=-4.4, ls=42) for i, (t, _) in enumerate(self.ROWS)]
        self.go(FadeIn(head), Create(under(head)), rt=0.4)
        for r, (_, w), fb in zip(rows, self.ROWS, (0.15, 0.3, 0.42, 0.58, 0.75, 0.88)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), rt=0.35)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Sent — 72-row response workbook; sent to all three professors with three attachments.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Sent(Scene):
    BID = "B07"
    FALLBACK = 11.6

    def construct(self):
        wb = card(11.4, 2.0, stroke=SLATE, sw=3).move_to(UP * 1.9)
        wt = VGroup(sans("response workbook · 72 rows", 46), serif("comment · change · location · status", 44)).arrange(DOWN, buff=0.18).move_to(wb)
        env = envelope(1.2, 0.8)
        to = serif("to all three professors", 46)
        line = VGroup(env, to).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.3)
        att = VGroup(*[chip(t, 42) for t in ("paper", "response workbook", "data workbook")]).arrange(RIGHT, buff=0.35).move_to(DOWN * 1.9)

        self.go(Create(wb), FadeIn(wt), rt=0.5)
        self.cue("sent", fallback=0.55)
        self.go(Create(env), FadeIn(to), rt=0.4)
        self.cue("paper", fallback=0.72)
        self.go(LaggedStart(*[FadeIn(a) for a in att], lag_ratio=0.25), rt=0.8)
        self.finish()
