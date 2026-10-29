"""scenes.py — Manim scenes for "Testing My Judge for Bias" (self-preference-test).

Same project as the Week 1–5 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week5/progress-kappa/scenes.py (with `ink_logo`, `under`), Week 3/5 table rows and
result cards, outline cards/chips, `cue()` on spoken words and the type sizes that passed GATE T.

Every number on screen appears in inbox/term2-week06/term2-week6-video-content.md as written.
Only Professor Brown is ever named; the critic is "the reviewer". The judge is shown by its
logo and a "blind" label, never as a person (rule 9).

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
#  B01_Conflict — GPT-4o-mini writes the definitions and judges them: conflict of interest?
# ─────────────────────────────────────────────────────────────────────────────
class B01_Conflict(Scene):
    BID = "B01"
    FALLBACK = 12.6

    def construct(self):
        mark = ink_logo("openai", 1.3).move_to(UP * 1.0)
        name = sans("GPT-4o-mini", 40).next_to(mark, DOWN, buff=0.25)
        lb = card(4.0, 1.4, stroke=SLATE, sw=3).move_to(LEFT * 4.2 + UP * 0.6)
        lt = serif("writes definitions", 38).move_to(lb)
        rb = card(4.0, 1.4, stroke=SLATE, sw=3).move_to(RIGHT * 4.2 + UP * 0.6)
        rt_ = serif("judges definitions", 38).move_to(rb)
        al = arrow(LEFT * 0.95 + UP * 0.6, LEFT * 2.1 + UP * 0.6)
        ar = arrow(RIGHT * 0.95 + UP * 0.6, RIGHT * 2.1 + UP * 0.6)
        who = sans("the reviewer", 34).move_to(DOWN * 1.15)
        flag = chip("conflict of interest?", 42, stroke=CRIMSON).move_to(DOWN * 1.95)
        cap = serif("maybe it scores its own writing more kindly", 38).move_to(DOWN * 2.85)

        self.go(FadeIn(mark), FadeIn(name), rt=0.6)
        self.cue("wrote", fallback=0.15)
        self.go(GrowArrow(al), Create(lb), FadeIn(lt), rt=0.6)
        self.cue("judges", fallback=0.4)
        self.go(GrowArrow(ar), Create(rb), FadeIn(rt_), rt=0.6)
        self.cue("reviewer", fallback=0.53)
        self.go(FadeIn(who), rt=0.3)
        self.cue("conflict", fallback=0.62)
        self.go(FadeIn(flag, shift=UP * 0.1), rt=0.5)
        self.cue("maybe", fallback=0.78)
        self.go(FadeIn(cap), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Design — 200 keywords, seed 42; a Mistral alternative for each, same format.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Design(Scene):
    BID = "B02"
    FALLBACK = 12.6

    def construct(self):
        s_box = card(5.0, 1.55, stroke=TEAL, sw=4).move_to(UP * 2.3)
        s_t = VGroup(sans("200 keywords", 42), serif("sampled with seed 42", 34)).arrange(DOWN, buff=0.12).move_to(s_box)
        lb = card(5.2, 2.3, stroke=SLATE, sw=3).move_to(LEFT * 3.1 + DOWN * 0.55)
        lh = VGroup(ink_logo("openai", 0.5), serif("own definition", 38)).arrange(RIGHT, buff=0.25)
        ls = serif("GPT-4o-mini", 34)
        VGroup(lh, ls).arrange(DOWN, buff=0.25).move_to(lb)
        rb = card(5.2, 2.3, stroke=SLATE, sw=3).move_to(RIGHT * 3.1 + DOWN * 0.55)
        rh = VGroup(ink_logo("mistral", 0.5), serif("Mistral definition", 38)).arrange(RIGHT, buff=0.25)
        rs = serif("ministral-8b-latest", 34)
        VGroup(rh, rs).arrange(DOWN, buff=0.25).move_to(rb)
        al = arrow(LEFT * 1.0 + UP * 1.45, LEFT * 2.2 + UP * 0.7)
        ar = arrow(RIGHT * 1.0 + UP * 1.45, RIGHT * 2.2 + UP * 0.7)
        fmt = chip("same 2-sentence popup format", 38).move_to(DOWN * 2.55)

        self.go(Create(s_box), rt=0.4)
        self.cue("200", fallback=0.2)
        self.go(FadeIn(s_t), rt=0.5)
        self.cue("each", fallback=0.5)
        self.go(GrowArrow(al), Create(lb), FadeIn(lh), FadeIn(ls), rt=0.6)
        self.cue("Mistral", fallback=0.6)
        self.go(GrowArrow(ar), Create(rb), FadeIn(rh), FadeIn(rs), rt=0.6)
        self.cue("same", fallback=0.85)
        self.go(FadeIn(fmt, shift=UP * 0.1), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Blind — one rubric, separate passes, author hidden.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Blind(Scene):
    BID = "B03"
    FALLBACK = 9.3

    def construct(self):
        j_box = card(4.2, 3.0, stroke=SLATE, sw=3).move_to(LEFT * 3.9 + UP * 0.4)
        j = VGroup(ink_logo("openai", 0.8), sans("GPT-4o-mini", 36), serif("the judge", 34)).arrange(DOWN, buff=0.2).move_to(j_box)
        p1 = card(4.6, 1.3, stroke=SLATE, sw=3).move_to(RIGHT * 3.0 + UP * 1.3)
        p1t = VGroup(sans("pass 1", 36), serif("one set", 34)).arrange(RIGHT, buff=0.35).move_to(p1)
        p2 = card(4.6, 1.3, stroke=SLATE, sw=3).move_to(RIGHT * 3.0 + DOWN * 0.5)
        p2t = VGroup(sans("pass 2", 36), serif("the other set", 34)).arrange(RIGHT, buff=0.35).move_to(p2)
        a1 = arrow(LEFT * 1.7 + UP * 0.8, RIGHT * 0.6 + UP * 1.3)
        a2 = arrow(LEFT * 1.7 + UP * 0.0, RIGHT * 0.6 + DOWN * 0.5)
        rub = chip("same 5-tag rubric", 40, stroke=TEAL).move_to(DOWN * 2.0)
        hid = sans("author hidden", 38).move_to(DOWN * 2.9)

        self.go(Create(j_box), FadeIn(j), rt=0.6)
        self.cue("same", fallback=0.3)
        self.go(FadeIn(rub), rt=0.4)
        self.cue("separate", fallback=0.55)
        self.go(GrowArrow(a1), Create(p1), FadeIn(p1t), GrowArrow(a2), Create(p2), FadeIn(p2t), rt=0.7)
        self.cue("without", fallback=0.72)
        self.go(FadeIn(hid), Create(under(hid)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Results — approval 55.5% (111/200) vs 62.5% (125/200); mean 82.77 vs 85.00.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Results(Scene):
    BID = "B04"
    FALLBACK = 14.7
    XO, XM = 0.8, 4.3

    def construct(self):
        head = serif("The result surprised me", 40).move_to(UP * 3.0)
        h_own = VGroup(ink_logo("openai", 0.45), sans("own", 36)).arrange(RIGHT, buff=0.2).move_to(RIGHT * self.XO + UP * 1.9)
        h_mis = VGroup(ink_logo("mistral", 0.45), sans("Mistral", 36)).arrange(RIGHT, buff=0.2).move_to(RIGHT * self.XM + UP * 1.9)
        top = Line(LEFT * 5.9 + UP * 1.4, RIGHT * 5.9 + UP * 1.4, color=SLATE, stroke_width=2)
        r1 = serif("approval rate", 40).move_to(LEFT * 5.7 + UP * 0.5, aligned_edge=LEFT)
        o1 = VGroup(sans("55.5%", 52), serif("111/200", 34)).arrange(DOWN, buff=0.1).move_to(RIGHT * self.XO + UP * 0.5)
        m1 = VGroup(sans("62.5%", 52), serif("125/200", 34)).arrange(DOWN, buff=0.1).move_to(RIGHT * self.XM + UP * 0.5)
        sep = Line(LEFT * 5.9 + DOWN * 0.55, RIGHT * 5.9 + DOWN * 0.55, color=MUTED, stroke_width=1.5)
        r2 = serif("mean score", 40).move_to(LEFT * 5.7 + DOWN * 1.4, aligned_edge=LEFT)
        o2 = sans("82.77", 52).move_to(RIGHT * self.XO + DOWN * 1.4)
        m2 = sans("85.00", 52).move_to(RIGHT * self.XM + DOWN * 1.4)
        bot = Line(LEFT * 5.9 + DOWN * 2.2, RIGHT * 5.9 + DOWN * 2.2, color=MUTED, stroke_width=1.5)
        u1, u2 = under(m1[0]), under(m2)

        self.go(FadeIn(head), FadeIn(h_own), FadeIn(h_mis), Create(top), rt=0.6)
        self.cue("approved", fallback=0.15)
        self.go(FadeIn(r1), rt=0.3)
        self.cue("55.5", fallback=0.25)
        self.go(FadeIn(o1), rt=0.4)
        self.cue("62.5", fallback=0.45)
        self.go(FadeIn(m1), Create(u1), Create(sep), rt=0.5)
        self.cue("Mean", fallback=0.6)
        self.go(FadeIn(r2), rt=0.3)
        self.cue("82.8", fallback=0.72)
        self.go(FadeIn(o2), rt=0.4)
        self.cue("85.0", fallback=0.88)
        self.go(FadeIn(m2), Create(u2), Create(bot), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Tests — chi-square and Welch's t-test not significant; McNemar significant, favors Mistral.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Tests(Scene):
    BID = "B05"
    FALLBACK = 15.8
    ROWS = [("chi-square", "approval rates", "p = 0.1547", ["not significant"], SLATE),
            ("Welch's t-test", "mean scores", "p = 0.1154", ["not significant"], SLATE),
            ("McNemar", "paired", "p = 0.0196", ["significant,", "favors Mistral"], TEAL)]
    YS = [1.75, 0.0, -1.75]

    def construct(self):
        rows = []
        for (nm, what, p, verdict, col), y in zip(self.ROWS, self.YS):
            box = card(11.8, 1.5, stroke=col, sw=4 if col == TEAL else 3).move_to(UP * y)
            n = VGroup(sans(nm, 36), serif(what, 32)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            n.move_to(LEFT * 5.5 + UP * y, aligned_edge=LEFT)
            pv = sans(p, 42).move_to(RIGHT * 0.2 + UP * y)
            v = VGroup(*[serif(s, 36, TEAL if col == TEAL else INK) for s in verdict]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
            v.move_to(RIGHT * 2.9 + UP * y, aligned_edge=LEFT)
            rows.append(VGroup(box, n, pv, v))

        for i, (w, fb) in enumerate([("chi-square", 0.05), ("t-test", 0.18), ("McNemar", 0.38)]):
            self.cue(w, fallback=fb)
            self.go(Create(rows[i][0]), FadeIn(rows[i][1]), FadeIn(rows[i][2]), rt=0.5)
            if i == 1:
                self.cue("significant", fallback=0.26)
                self.go(FadeIn(rows[0][3]), FadeIn(rows[1][3]), rt=0.4)
        self.cue("opposite", fallback=0.72)
        self.go(FadeIn(rows[2][3]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Finding — no evidence of self-preference; general leniency; Section 5.4 rewritten.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Finding(Scene):
    BID = "B06"
    FALLBACK = 16.8

    def construct(self):
        v_box = card(10.4, 1.4, stroke=TEAL, sw=4).move_to(UP * 2.45)
        v = sans("no evidence of self-preference", 44, TEAL).move_to(v_box)
        g = VGroup(serif("general leniency", 46),
                   serif("GPT-4o-mini is easy on everyone's writing", 36)).arrange(DOWN, buff=0.15).move_to(UP * 0.85)
        avg_l = serif("Term 1 average scores", 34).move_to(DOWN * 0.45)
        avgs = VGroup(*[VGroup(ink_logo(lg, 0.5), sans(n, 44)).arrange(RIGHT, buff=0.2)
                        for lg, n in (("openai", "76"), ("mistral", "65"), ("claude", "56"))]).arrange(RIGHT, buff=1.0)
        avgs.move_to(DOWN * 1.2)
        u = under(avgs[0][1])
        sec = chip("paper Section 5.4 rewritten with these results", 36).move_to(DOWN * 2.5)

        self.go(Create(v_box), FadeIn(v), rt=0.6)
        self.cue("general", fallback=0.25)
        self.go(FadeIn(g[0]), rt=0.4)
        self.cue("easy", fallback=0.4)
        self.go(FadeIn(g[1]), rt=0.4)
        self.cue("higher", fallback=0.6)
        self.go(FadeIn(avg_l), FadeIn(avgs), rt=0.5)
        self.go(Create(u), rt=0.3)
        self.cue("replaced", fallback=0.82)
        self.go(FadeIn(sec, shift=UP * 0.1), rt=0.4)
        self.finish()
