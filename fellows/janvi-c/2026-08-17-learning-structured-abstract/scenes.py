"""scenes.py — Manim scenes for "Writing a Structured Abstract" (structured-abstract).

Same project as the Week 1 and Week 2 reels (hai-videos/Week1/*, hai-videos/Week2/*), so the same
visuals: helpers, the clocked Beat base (`Scene = Beat`), outline cards and chips, strike/highlight
treatment, `cue()` on spoken words (mp3/words.json) and the type sizes that passed GATE T.

Same helper block as this week's progress reel (hai-videos/Week3/progress-choosing-a-journal).
The worked example is Janvi's own JBI abstract (345 → 285 words). The original long sentence is
not quoted (not in the source); B04 shows only what it contained.

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


def counter(target, fmt, size, color, pos, tracker, start=0):
    """Text counter that runs start → target as `tracker` goes 0 → 1."""
    def build():
        v = start + tracker.get_value() * (target - start)
        return sans(fmt(v), size, color).move_to(pos)
    return always_redraw(build)


def arrow(a, b, color=SLATE):
    """Fixed-coordinate arrow (GATE A stub-safe)."""
    return Arrow(a, b, buff=0, color=color, stroke_width=4)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_FiveParts — five labelled parts, one job each, all in 300 words.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FiveParts(Scene):
    BID = "B01"
    FALLBACK = 16.0
    PARTS = [("Objective",), ("Materials and", "Methods"), ("Results",), ("Discussion",), ("Conclusion",)]
    CUES = ["Objective", "Materials", "Results", "Discussion", "Conclusion"]

    def construct(self):
        head = serif("A structured abstract: labelled parts, one job each", 42).move_to(UP * 2.95)
        sub = serif("the Journal of Biomedical Informatics requires five", 36, MUTED).move_to(UP * 2.1)
        boxes = []
        for p in self.PARTS:
            t = VGroup(*[serif(s, 34) for s in p]).arrange(DOWN, buff=0.08)
            b = card(t.width + 0.4, 1.7, stroke=MUTED)
            t.move_to(b)
            boxes.append(VGroup(b, t))
        VGroup(*boxes).arrange(RIGHT, buff=0.18).move_to(UP * 0.2)
        span_l = Line(LEFT * 5.9 + DOWN * 1.3, RIGHT * 5.9 + DOWN * 1.3, color=TEAL, stroke_width=4)
        ends = VGroup(Line(LEFT * 5.9 + DOWN * 1.1, LEFT * 5.9 + DOWN * 1.5, color=TEAL, stroke_width=4),
                      Line(RIGHT * 5.9 + DOWN * 1.1, RIGHT * 5.9 + DOWN * 1.5, color=TEAL, stroke_width=4))
        total = sans("all five: 300 words total", 44, TEAL).move_to(DOWN * 2.3)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.cue("labelled", fallback=0.12)
        self.go(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.1), rt=0.8)
        self.cue("requires", fallback=0.4)
        self.go(FadeIn(sub), rt=0.4)
        for i, w in enumerate(self.CUES):
            self.cue(w, fallback=0.5 + 0.06 * i)
            self.go(boxes[i][0].animate.set_stroke(TEAL, width=5), boxes[i][1].animate.set_color(TEAL), rt=0.3)
        self.cue("fit", fallback=0.88)
        self.go(Create(span_l), Create(ends), FadeIn(total, shift=UP * 0.1), rt=0.6)
        self.finish()


def word_bar(x0, y, scale, tr, start, end, limit=300):
    """Bar for a word count that runs start → end; burnt orange while over the limit."""
    def build():
        n = start + tr.get_value() * (end - start)
        return Rectangle(width=n * scale, height=0.6, fill_color=CRIMSON if n > limit else TEAL,
                         fill_opacity=1, stroke_opacity=0).move_to(RIGHT * x0 + UP * y, aligned_edge=LEFT)
    return always_redraw(build)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_WhatItHolds — two phases + the numbers; first draft 345 words.
# ─────────────────────────────────────────────────────────────────────────────
class B02_WhatItHolds(Scene):
    BID = "B02"
    FALLBACK = 16.0

    def construct(self):
        head = serif("Mine had to hold", 40, MUTED).move_to(LEFT * 5.6 + UP * 3.0, aligned_edge=LEFT)
        items = [
            VGroup(sans("two phases", 36), serif("generation → review", 38)).arrange(RIGHT, buff=0.35),
            VGroup(sans("10,049 → 8,053", 36), serif("keywords", 38)).arrange(RIGHT, buff=0.35),
            VGroup(sans("927 → 915", 36), serif("acronyms", 38)).arrange(RIGHT, buff=0.35),
            VGroup(sans("5", 36), serif("tags", 38), sans("·  3", 36), serif("models", 38)).arrange(RIGHT, buff=0.25),
        ]
        col = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.42).move_to(LEFT * 5.6 + UP * 0.85, aligned_edge=LEFT)
        X0, SC, by = -5.6, 10.5 / 360, -2.0
        tr = ValueTracker(0)
        bar = word_bar(X0, by, SC, tr, 0, 345)
        lim_x = X0 + 300 * SC
        lim = DashedLine(RIGHT * lim_x + UP * (by + 0.6), RIGHT * lim_x + UP * (by - 0.6),
                         color=INK, stroke_width=4, dash_length=0.12)
        lim_t = sans("300-word limit", 34).move_to(RIGHT * (lim_x - 1.6) + UP * (by - 0.95))
        draft = serif("first draft", 36, MUTED).move_to(RIGHT * 3.9 + UP * 1.3)
        cnt = counter(345, lambda v: f"{int(round(v))} words", 52, INK, RIGHT * 3.9 + UP * 0.5, tr)

        self.go(FadeIn(head), rt=0.4)
        for i, (w, fb) in enumerate([("two", 0.05), ("10,049", 0.3), ("927", 0.5), ("five", 0.65)]):
            self.cue(w, fallback=fb)
            self.go(FadeIn(items[i], shift=RIGHT * 0.15), rt=0.5)
        self.cue("first", fallback=0.82)
        self.add(bar, cnt)
        self.go(FadeIn(draft), Create(lim), FadeIn(lim_t), tr.animate.set_value(1), rt=1.2)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_TheRule — did + found → abstract; why → methods.
# ─────────────────────────────────────────────────────────────────────────────
class B03_TheRule(Scene):
    BID = "B03"
    FALLBACK = 9.0

    def tagged(self, tag, text, stroke):
        c = chip(text, 36, stroke=stroke)
        t = sans(tag, 32, stroke)
        return VGroup(t, c).arrange(DOWN, buff=0.15)

    def construct(self):
        head = serif("The rule I used", 44).move_to(UP * 2.95)
        did = self.tagged("DID", "what you did", TEAL).move_to(LEFT * 4.6 + UP * 0.95)
        plus = sans("+", 44).move_to(LEFT * 2.75 + UP * 0.75)
        found = self.tagged("FOUND", "what you found", TEAL).move_to(LEFT * 0.75 + UP * 0.95)
        a1 = arrow(RIGHT * 1.35 + UP * 0.75, RIGHT * 2.45 + UP * 0.75, color=TEAL)
        abs_box = card(3.3, 1.2, stroke=TEAL, sw=4).move_to(RIGHT * 4.3 + UP * 0.75)
        abs_t = sans("abstract", 40, TEAL).move_to(abs_box)
        why = self.tagged("WHY", "why you made each design choice", SLATE).move_to(LEFT * 2.2 + DOWN * 1.65)
        a2 = arrow(RIGHT * 1.35 + DOWN * 1.85, RIGHT * 2.45 + DOWN * 1.85)
        m_box = card(3.3, 1.2, stroke=SLATE, sw=4).move_to(RIGHT * 4.3 + DOWN * 1.85)
        m_t = sans("methods", 40, SLATE).move_to(m_box)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.5)
        self.cue("done", fallback=0.3)
        self.go(FadeIn(did), rt=0.4)
        self.cue("found", fallback=0.42)
        self.go(FadeIn(plus), FadeIn(found), GrowArrow(a1), Create(abs_box), FadeIn(abs_t), rt=0.6)
        self.cue("Why", fallback=0.55)
        self.go(FadeIn(why), rt=0.5)
        self.cue("methods", fallback=0.85)
        self.go(GrowArrow(a2), Create(m_box), FadeIn(m_t), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_OneCut — a ~25-word sentence (models, providers, why mixed) → a few words.
# ─────────────────────────────────────────────────────────────────────────────
class B04_OneCut(Scene):
    BID = "B04"
    FALLBACK = 13.0

    def construct(self):
        head = serif("One example", 40, MUTED).move_to(UP * 3.0)
        box = card(11.0, 2.6, stroke=SLATE, sw=3).move_to(UP * 1.25)
        lab = serif("one full sentence, about 25 words, naming", 36, MUTED)
        parts = VGroup(chip("all three models", 34), chip("their providers", 34),
                       chip("why I mixed providers", 34, stroke=SLATE)).arrange(RIGHT, buff=0.3)
        VGroup(lab, parts).arrange(DOWN, buff=0.3).move_to(box)
        x = Line(LEFT * 5.6 + UP * 1.2, RIGHT * 5.6 + UP * 1.2, color=CRIMSON, stroke_width=7)
        x._qc_intentional = True
        new = serif("a three-model cross-provider ensemble", 50).move_to(DOWN * 1.15)
        hl = highlight(new)
        cnt = sans("about 25 words → a few", 40, TEAL).move_to(DOWN * 2.5)

        self.go(FadeIn(head), rt=0.4)
        self.cue("full", fallback=0.15)
        self.go(Create(box), FadeIn(lab), rt=0.5)
        self.cue("three", fallback=0.25)
        self.go(FadeIn(parts[0]), rt=0.3)
        self.cue("providers", fallback=0.35)
        self.go(FadeIn(parts[1]), rt=0.3)
        self.cue("mixed", fallback=0.45)
        self.go(FadeIn(parts[2]), rt=0.3)
        self.cue("cut", fallback=0.65)
        self.go(Create(x), VGroup(lab, parts).animate.set_opacity(0.45), rt=0.6)
        self.cue("ensemble", nth=1, fallback=0.85)
        self.add(hl)
        self.go(FadeIn(hl), FadeIn(new, shift=UP * 0.1), FadeIn(cnt), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_TheCount — 345 → 285 under the 300 line.
# ─────────────────────────────────────────────────────────────────────────────
class B05_TheCount(Scene):
    BID = "B05"
    FALLBACK = 5.0

    def construct(self):
        head = serif("Cuts like that", 40, MUTED).move_to(UP * 2.9)
        X0, SC, by = -5.6, 11.0 / 360, -0.9
        tr = ValueTracker(0)
        bar = word_bar(X0, by, SC, tr, 345, 285)
        lim_x = X0 + 300 * SC
        lim = DashedLine(RIGHT * lim_x + UP * (by + 0.6), RIGHT * lim_x + UP * (by - 0.6),
                         color=INK, stroke_width=4, dash_length=0.12)
        lim_t = sans("300-word limit", 34).move_to(RIGHT * (lim_x - 1.6) + UP * (by - 0.95))
        cnt = counter(285, lambda v: f"{int(round(v))} words", 64, INK, UP * 1.3, tr, start=345)
        ok = sans("under the limit", 40, TEAL).move_to(DOWN * 2.8)
        ok_t = tick(s=0.4).next_to(ok, LEFT, buff=0.3)

        self.add(bar, cnt)
        self.go(FadeIn(head), Create(lim), FadeIn(lim_t), rt=0.5)
        self.cue("345", fallback=0.3)
        self.go(tr.animate.set_value(1), rt=1.6)
        self.cue("under", fallback=0.75)
        self.go(FadeIn(ok, shift=UP * 0.1), Create(ok_t), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — keep findings and numbers; cut rationale instead.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 15.0

    def construct(self):
        head = serif("What not to cut", 46).move_to(UP * 2.95)
        keep = [chip("findings", 40, stroke=TEAL), chip("the numbers behind them", 40, stroke=TEAL)]
        cut = chip("rationale", 40, stroke=MUTED)
        row = VGroup(*keep, cut).arrange(RIGHT, buff=0.9).move_to(UP * 1.45)
        k_t = [tick().next_to(k, DOWN, buff=0.2) for k in keep]
        k_l = [sans("keep", 34, TEAL).next_to(t, RIGHT, buff=0.12) for t in k_t]
        c_l = sans("cut", 34, MUTED).next_to(cut, DOWN, buff=0.25)
        reader = VGroup(serif("A reader who sees only the abstract", 38),
                        serif("should still know what you did and what you got.", 38)).arrange(DOWN, buff=0.1)
        reader.move_to(DOWN * 0.75)
        rule = VGroup(serif("If a cut removes a result:", 36, MUTED),
                      sans("put it back, cut rationale instead", 38, TEAL)).arrange(DOWN, buff=0.12).move_to(DOWN * 2.45)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.5)
        self.cue("findings", fallback=0.12)
        self.go(FadeIn(keep[0]), Create(k_t[0]), FadeIn(k_l[0]), rt=0.5)
        self.cue("numbers", fallback=0.2)
        self.go(FadeIn(keep[1]), Create(k_t[1]), FadeIn(k_l[1]), rt=0.5)
        self.cue("reader", fallback=0.32)
        self.go(FadeIn(reader, shift=UP * 0.1), rt=0.6)
        self.cue("removes", fallback=0.72)
        self.go(FadeIn(cut), rt=0.4)
        self.cue("rationale", fallback=0.88)
        self.go(Create(strike(cut[1])), FadeIn(c_l), FadeIn(rule, shift=UP * 0.1), rt=0.6)
        self.finish()
