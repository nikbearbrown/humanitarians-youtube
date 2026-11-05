"""scenes.py — Manim scenes for "Planting Errors to Test a Checker" (planted-errors).

Same helper block as this week's progress reel (hai-videos/Week7/progress-third-judge), Week 1–6
lineage. B04 adapts that reel's B05_Planted; B05 uses the Week 6 three-card layout.
Every data number on screen appears in inbox/term2-week07/term2-week7-video-content.md as written.

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


def lines(texts, size=36, color=INK, buff=0.08):
    return VGroup(*[serif(t, size, color) for t in texts]).arrange(DOWN, aligned_edge=LEFT, buff=buff)


def ink_logo(name, h):
    return logo(name, h).set_fill(INK, opacity=1)


def under(t):
    """Teal underline (Week 4: replaces multi-line gold highlights, GATE V contrast)."""
    return Line(t.get_corner(DL) + DOWN * 0.08, t.get_corner(DR) + DOWN * 0.08, color=TEAL, stroke_width=5)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_NoKey — to measure a checker you need an answer key; nobody has one; so you make it.
# ─────────────────────────────────────────────────────────────────────────────
class B01_NoKey(Scene):
    BID = "B01"
    FALLBACK = 9.0

    def construct(self):
        c_box = card(5.4, 2.8, stroke=SLATE, sw=3).move_to(LEFT * 3.1 + UP * 0.7)
        c_t = VGroup(sans("the checker", 40), serif("how many mistakes", 36), serif("does it catch?", 36)).arrange(DOWN, buff=0.15).move_to(c_box)
        k_box = DashedVMobject(RoundedRectangle(width=4.6, height=2.8, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=44)
        k_box.move_to(RIGHT * 3.3 + UP * 0.7)
        k_t = VGroup(sans("answer key", 38), serif("nobody has one", 36)).arrange(DOWN, buff=0.2).move_to(k_box)
        a = arrow(LEFT * 0.3 + UP * 0.7, RIGHT * 0.9 + UP * 0.7)
        make = sans("so you make it", 44, TEAL).move_to(DOWN * 2.2)

        self.go(Create(c_box), FadeIn(c_t), rt=0.6)
        self.cue("already", fallback=0.35)
        self.go(GrowArrow(a), Create(k_box), FadeIn(k_t[0]), rt=0.6)
        self.cue("nobody", fallback=0.65)
        self.go(FadeIn(k_t[1]), rt=0.4)
        self.cue("make", fallback=0.85)
        self.go(FadeIn(make), Create(under(make)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Recipe — good items → corrupted on purpose + kept as controls → the checker, blind.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Recipe(Scene):
    BID = "B02"
    FALLBACK = 9.0

    def construct(self):
        g = card(3.4, 1.4, stroke=SLATE, sw=3).move_to(LEFT * 4.6 + UP * 0.2)
        g_t = VGroup(serif("items you", 36), serif("believe are good", 36)).arrange(DOWN, buff=0.06).move_to(g)
        c = card(3.8, 1.3, stroke=CRIMSON, sw=4).move_to(LEFT * 0.2 + UP * 1.4)
        c_t = VGroup(serif("some corrupted", 36), serif("on purpose", 36)).arrange(DOWN, buff=0.06).move_to(c)
        k = card(3.8, 1.3, stroke=TEAL, sw=4).move_to(LEFT * 0.2 + DOWN * 1.0)
        k_t = VGroup(serif("the rest kept", 36), serif("as controls", 36)).arrange(DOWN, buff=0.06).move_to(k)
        ch = card(3.0, 1.6, stroke=SLATE, sw=3).move_to(RIGHT * 4.5 + UP * 0.2)
        ch_t = VGroup(sans("checker", 38), serif("blind", 36)).arrange(DOWN, buff=0.1).move_to(ch)
        a1 = arrow(LEFT * 2.85 + UP * 0.5, LEFT * 2.15 + UP * 1.2)
        a2 = arrow(LEFT * 2.85 + DOWN * 0.1, LEFT * 2.15 + DOWN * 0.8)
        a3 = arrow(RIGHT * 1.75 + UP * 1.2, RIGHT * 2.95 + UP * 0.5)
        a4 = arrow(RIGHT * 1.75 + DOWN * 0.8, RIGHT * 2.95 + DOWN * 0.1)
        all_t = serif("everything goes through, blind", 38).move_to(DOWN * 2.6)

        self.go(Create(g), FadeIn(g_t), rt=0.5)
        self.cue("Corrupt", fallback=0.3)
        self.go(GrowArrow(a1), Create(c), FadeIn(c_t), rt=0.5)
        self.cue("controls", fallback=0.5)
        self.go(GrowArrow(a2), Create(k), FadeIn(k_t), rt=0.5)
        self.cue("run", fallback=0.65)
        self.go(GrowArrow(a3), GrowArrow(a4), Create(ch), FadeIn(ch_t), FadeIn(all_t), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_FiveTypes — conflation · wrong expansion · disambiguation list · factual error · wrong field.
# ─────────────────────────────────────────────────────────────────────────────
class B03_FiveTypes(Scene):
    BID = "B03"
    FALLBACK = 18.0
    ROWS = [("conflation", "BRCA1 as a growth promoter,|not a tumor suppressor"),
            ("wrong expansion", "ER as endoplasmic reticulum,|not estrogen receptor"),
            ("disambiguation", "a disambiguation-page style list"),
            ("factual error", "a wrong drug target, a wrong organ"),
            ("wrong field", "an industrial or engineering definition")]
    YS = [1.9, 0.9, -0.1, -1.1, -2.1]

    def construct(self):
        head = serif("Five kinds of corruption", 40).move_to(UP * 2.95)
        rows = []
        for (nm, ex), y in zip(self.ROWS, self.YS):
            bar = Line(UP * 0.3, DOWN * 0.3, color=CRIMSON, stroke_width=6).move_to(LEFT * 5.8 + UP * y)
            n = sans(nm, 34).move_to(LEFT * 5.5 + UP * y, aligned_edge=LEFT)
            e = VGroup(*[serif(t, 32) for t in ex.split("|")]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
            e.move_to(LEFT * 0.8 + UP * y, aligned_edge=LEFT)
            rows.append(VGroup(bar, n, e))

        self.go(FadeIn(head), rt=0.3)
        for i, (w, fb) in enumerate([("conflation", 0.1), ("wrong", 0.55), ("disambiguation-style", 0.68), ("factual", 0.8), ("field", 0.92)]):
            self.cue(w, fallback=fb)
            self.go(Create(rows[i][0]), FadeIn(rows[i][1:]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Sample — 200 approved → 150 corrupted (30 of each type) + 50 controls.
#  (Progress reel B05_Planted.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_Sample(Scene):
    BID = "B04"
    FALLBACK = 7.0

    def construct(self):
        top = card(7.6, 1.1, stroke=SLATE, sw=3).move_to(UP * 2.3)
        top_t = sans("200 approved definitions", 38).move_to(top)
        lb = card(5.6, 1.5, stroke=CRIMSON, sw=4).move_to(LEFT * 2.7 + UP * 0.4)
        lt = VGroup(sans("150 corrupted", 40), serif("30 of each type", 34)).arrange(DOWN, buff=0.1).move_to(lb)
        rb = card(4.2, 1.5, stroke=TEAL, sw=4).move_to(RIGHT * 3.4 + UP * 0.4)
        rt_ = VGroup(sans("50 controls", 40), serif("kept untouched", 34)).arrange(DOWN, buff=0.1).move_to(rb)
        al = arrow(LEFT * 1.3 + UP * 1.75, LEFT * 2.0 + UP * 1.2)
        ar = arrow(RIGHT * 1.3 + UP * 1.75, RIGHT * 2.4 + UP * 1.2)
        fives = VGroup(*[VGroup(RoundedRectangle(width=1.0, height=0.8, corner_radius=0.1, stroke_color=CRIMSON,
                                                 stroke_width=3, fill_opacity=0), sans("30", 36)) for _ in range(5)])
        for f in fives:
            f[1].move_to(f[0])
        fives.arrange(RIGHT, buff=0.15).move_to(LEFT * 2.7 + DOWN * 1.2)

        self.go(Create(top), FadeIn(top_t), rt=0.5)
        self.cue("150", fallback=0.35)
        self.go(GrowArrow(al), Create(lb), FadeIn(lt), rt=0.5)
        self.cue("30", fallback=0.5)
        self.go(LaggedStart(*[Create(f[0]) for f in fives], lag_ratio=0.1), *[FadeIn(f[1]) for f in fives], rt=0.6)
        self.cue("kept", fallback=0.7)
        self.go(GrowArrow(ar), Create(rb), FadeIn(rt_), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Measures — caught · slipped through · controls wrongly flagged (= false positive rate).
#  (Week 6 three-card layout.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Measures(Scene):
    BID = "B05"
    FALLBACK = 11.0
    XS = [-4.15, 0.0, 4.15]
    M = [("caught", ["corrupted items", "the checker flags"], "30.0%", SLATE),
         ("slipped|through", ["corrupted items", "that pass"], "18.7%", SLATE),
         ("wrongly|flagged", ["good controls", "it flags"], "0.0%", TEAL)]

    def construct(self):
        head = serif("Measure three things", 42).move_to(UP * 2.95)
        cards = []
        for (nm, lines_, v, col), x in zip(self.M, self.XS):
            box = card(3.85, 3.3, stroke=col, sw=4 if col == TEAL else 3).move_to(RIGHT * x + UP * 0.35)
            n = VGroup(*[sans(w, 36, TEAL if col == TEAL else INK) for w in nm.split("|")]).arrange(DOWN, buff=0.06)
            t = VGroup(*[serif(s, 34) for s in lines_]).arrange(DOWN, buff=0.06)
            VGroup(n, t).arrange(DOWN, buff=0.3).move_to(box)
            ours = serif(f"our run: {v}", 32).next_to(box, DOWN, buff=0.2)
            cards.append(VGroup(box, n, t, ours))
        fpr = sans("= your false positive rate", 40, TEAL).move_to(DOWN * 2.75)

        self.go(FadeIn(head), rt=0.3)
        for i, (w, fb) in enumerate([("caught", 0.2), ("slip", 0.35), ("flagged", 0.55)]):
            self.cue(w, fallback=fb)
            self.go(Create(cards[i][0]), FadeIn(cards[i][1:]), rt=0.5)
        self.cue("false", fallback=0.85)
        self.go(FadeIn(fpr), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Limit — you only learn about the errors you planted; a sixth kind can slip by.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Limit(Scene):
    BID = "B06"
    FALLBACK = 10.0

    def construct(self):
        l1 = serif("You only learn about the errors you planted.", 42).move_to(UP * 2.7)
        types = ["conflation", "wrong expansion", "disambiguation", "factual error", "wrong field"]
        chips = [chip(t, 34, stroke=TEAL) for t in types]
        r1 = VGroup(*chips[:3]).arrange(RIGHT, buff=0.55).move_to(UP * 1.2)
        r2 = VGroup(*chips[3:]).arrange(RIGHT, buff=0.55)
        six_box = DashedVMobject(RoundedRectangle(width=2.6, height=0.85, corner_radius=0.16,
                                                  stroke_color=SLATE, stroke_width=3), num_dashes=24)
        six = VGroup(six_box, serif("a sixth kind?", 34).move_to(six_box))
        row2 = VGroup(r2, six).arrange(RIGHT, buff=0.55).move_to(DOWN * 0.1)
        ticks = [tick(s=0.3).next_to(c, RIGHT, buff=0.08) for c in chips]
        l2 = serif("Real mistakes can look different.", 40).move_to(DOWN * 1.7)

        self.go(FadeIn(l1), rt=0.4)
        self.go(*[FadeIn(c) for c in chips], Create(six_box), FadeIn(six[1]), rt=0.5)
        self.cue("Real", fallback=0.4)
        self.go(FadeIn(l2), rt=0.4)
        self.cue("well", fallback=0.65)
        self.go(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.1), rt=0.6)
        self.finish()
