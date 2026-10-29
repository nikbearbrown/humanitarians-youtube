"""scenes.py — Manim scenes for "When the Best Judge Gets Outvoted" (best-judge-outvoted).

Same project as the Week 1–7 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week7/progress-third-judge/scenes.py (Week 6 block); Week 7 B02 queue bars (B02, B06), Week 7 B01 judge columns (B04), Week 7 B04 verdict card (B05),
Week 4–7 result cards.

Every number on screen appears in inbox/term2-week08/term2-week8-video-content.md as written.
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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Rerun — Claude Code scores all 200 items; strict detection 30.0% → 74.0%; controls 0.0%.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Rerun(Scene):
    BID = "B01"
    FALLBACK = 11.5

    def construct(self):
        top = VGroup(ink_logo("claude-code", 0.55), serif("scores all 200 test items as the third judge", 38)).arrange(RIGHT, buff=0.3).move_to(UP * 2.85)
        head = serif("strict detection", 40).move_to(UP * 1.75)
        lb = card(4.6, 2.2, stroke=SLATE, sw=3).move_to(LEFT * 3.2 + UP * 0.25)
        lt = VGroup(sans("30.0%", 60), serif("2 judges", 36)).arrange(DOWN, buff=0.15).move_to(lb)
        rb = card(4.6, 2.2, stroke=TEAL, sw=4).move_to(RIGHT * 3.2 + UP * 0.25)
        rt_ = VGroup(sans("74.0%", 60, TEAL), serif("3 judges", 36)).arrange(DOWN, buff=0.15).move_to(rb)
        ar = arrow(LEFT * 0.75 + UP * 0.25, RIGHT * 0.75 + UP * 0.25)
        c_t = VGroup(serif("50 controls flagged:", 38), sans("0.0%", 46, TEAL)).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.1)
        ok = tick(s=0.4).next_to(c_t, RIGHT, buff=0.3)

        self.go(FadeIn(top), rt=0.5)
        self.cue("Strict", fallback=0.45)
        self.go(FadeIn(head), Create(lb), FadeIn(lt), rt=0.5)
        self.cue("74", fallback=0.65)
        self.go(GrowArrow(ar), Create(rb), FadeIn(rt_), rt=0.5)
        self.cue("control", fallback=0.85)
        self.go(FadeIn(c_t), Create(ok), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Individual — Claude 98.0% (147/150) · Mistral 68.7% (103/150) · GPT-4o-mini 64.0% (96/150).
# ─────────────────────────────────────────────────────────────────────────────
class B02_Individual(Scene):
    BID = "B02"
    FALLBACK = 13.4
    X0, K = -1.9, 4.6 / 100
    ROWS = [("claude", "Claude", 98.0, "98.0%", "147/150", TEAL, 1.2, "Claude"),
            ("mistral", "Mistral", 68.7, "68.7%", "103/150", SLATE, 0.0, "Mistral"),
            ("openai", "GPT-4o-mini", 64.0, "64.0%", "96/150", SLATE, -1.2, "G")]

    def construct(self):
        head = serif("planted errors caught, each judge alone", 40).move_to(UP * 2.85)
        axis = Line(RIGHT * self.X0 + UP * 1.8, RIGHT * self.X0 + DOWN * 1.8, color=SLATE, stroke_width=3)
        rows = []
        for lg, nm, pct, ps, fr, col, y, _ in self.ROWS:
            lab = VGroup(ink_logo(lg, 0.45), sans(nm, 34)).arrange(RIGHT, buff=0.2)
            lab.move_to(RIGHT * (self.X0 - 0.3) + UP * y, aligned_edge=RIGHT)
            b = vbar(pct, self.K, self.X0, y, col)
            v = VGroup(sans(ps, 40), serif(fr, 32)).arrange(RIGHT, buff=0.25).next_to(b, RIGHT, buff=0.2)
            rows.append(VGroup(lab, b, v))
        cap = serif("of 150 corrupted definitions", 34).move_to(DOWN * 2.6)

        self.go(FadeIn(head), Create(axis), rt=0.4)
        for (lg, nm, pct, ps, fr, col, y, w), r, fb in zip(self.ROWS, rows, (0.08, 0.6, 0.8)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), FadeIn(r[2]), rt=0.5)
            if w == "Claude":
                self.go(FadeIn(cap), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Through — pass-through 18.7% → 20.7%; "why, with a 98% judge?" (7.2 s: numbers at once).
# ─────────────────────────────────────────────────────────────────────────────
class B03_Through(Scene):
    BID = "B03"
    FALLBACK = 7.2

    def construct(self):
        head = serif("corrupted items passed through", 40).move_to(UP * 2.85)
        lb = card(4.6, 2.0, stroke=SLATE, sw=3).move_to(LEFT * 3.2 + UP * 0.9)
        lt = VGroup(sans("18.7%", 56), serif("2 judges", 36)).arrange(DOWN, buff=0.12).move_to(lb)
        rb = card(4.6, 2.0, stroke=CRIMSON, sw=4).move_to(RIGHT * 3.2 + UP * 0.9)
        rt_ = VGroup(sans("20.7%", 56), serif("3 judges", 36)).arrange(DOWN, buff=0.12).move_to(rb)
        ar = arrow(LEFT * 0.75 + UP * 0.9, RIGHT * 0.75 + UP * 0.9)
        q_box = DashedVMobject(RoundedRectangle(width=7.4, height=1.3, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=48).move_to(DOWN * 1.75)
        q = serif("why, with a 98% judge?", 46).move_to(q_box)

        self.go(FadeIn(head), Create(lb), FadeIn(lt), GrowArrow(ar), Create(rb), FadeIn(rt_), rt=0.5)
        self.cue("Why", fallback=0.65)
        self.go(Create(q_box), FadeIn(q), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Outvoted — Claude "flag" vs Mistral "ship" + GPT-4o-mini "ship" → ship; "36 of 39 misses".
# ─────────────────────────────────────────────────────────────────────────────
class B04_Outvoted(Scene):
    BID = "B04"
    FALLBACK = 12.2
    J = [("claude", "Claude", "flag", TEAL, -4.2), ("mistral", "Mistral", "ship", CRIMSON, 0.0),
         ("openai", "GPT-4o-mini", "ship", CRIMSON, 4.2)]

    def construct(self):
        cols = []
        for lg, nm, vote, col, x in self.J:
            head = VGroup(ink_logo(lg, 0.85), sans(nm, 34)).arrange(DOWN, buff=0.2).move_to(RIGHT * x + UP * 1.45)
            v = chip(vote, 40, stroke=col).move_to(RIGHT * x + DOWN * 0.35)
            cols.append((head, v))
        cnt = VGroup(sans("36 of 39 misses", 44)).move_to(UP * 3.0)
        res = card(6.4, 1.2, stroke=CRIMSON, sw=4).move_to(DOWN * 2.3)
        res_t = serif("majority rule → ship", 44).move_to(res)
        a1 = arrow(DOWN * 1.1, DOWN * 1.65)
        bracket = Line(RIGHT * -0.9 + DOWN * 1.1, RIGHT * 5.1 + DOWN * 1.1, color=SLATE, stroke_width=4)

        self.go(FadeIn(cols[0][0]), FadeIn(cols[1][0]), FadeIn(cols[2][0]), FadeIn(cols[0][1]), rt=0.6)
        self.cue("36", fallback=0.2)
        self.go(FadeIn(cnt[0]), Create(under(cnt[0])), rt=0.5)
        self.cue("Mistral", fallback=0.35)
        self.go(FadeIn(cols[1][1]), FadeIn(cols[2][1]), rt=0.5)
        self.cue("majority", fallback=0.6)
        self.go(Create(bracket), GrowArrow(a1), Create(res), FadeIn(res_t), rt=0.6)
        self.cue("even", fallback=0.8)
        self.go(Create(strike(cols[0][1][1])), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Ceiling — "the vote sets the ceiling, not the strongest judge". (4.3 s: shown at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Ceiling(Scene):
    BID = "B05"
    FALLBACK = 4.3

    def construct(self):
        box = card(10.4, 3.4, stroke=TEAL, sw=4).move_to(UP * 0.2)
        a = sans("the vote sets the ceiling,", 52)
        b = serif("not the strongest judge", 50)
        VGroup(a, b).arrange(DOWN, buff=0.35).move_to(box)
        self.go(Create(box), FadeIn(a), FadeIn(b), rt=0.4)
        self.cue("vote", fallback=0.45)
        self.go(Create(under(a)), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_ByType — three judges, caught by corruption type.
# ─────────────────────────────────────────────────────────────────────────────
class B06_ByType(Scene):
    BID = "B06"
    FALLBACK = 11.8
    X0, K = -1.0, 5.0 / 100
    ROWS = [("disambiguation", 96.7, "96.7%", TEAL), ("category swap", 93.3, "93.3%", TEAL),
            ("wrong expansion", 66.7, "66.7%", SLATE), ("conflation", 56.7, "56.7%", CRIMSON),
            ("factual error", 56.7, "56.7%", CRIMSON)]

    def construct(self):
        head = serif("caught by error type, three judges", 40).move_to(UP * 2.95)
        axis = Line(RIGHT * self.X0 + UP * 2.4, RIGHT * self.X0 + DOWN * 2.4, color=SLATE, stroke_width=3)
        rows = []
        for i, (nm, pct, ps, col) in enumerate(self.ROWS):
            y = 1.9 - i * 0.95
            lab = sans(nm, 34).move_to(RIGHT * (self.X0 - 0.3) + UP * y, aligned_edge=RIGHT)
            b = vbar(pct, self.K, self.X0, y, col, h=0.55)
            v = sans(ps, 38).next_to(b, RIGHT, buff=0.2)
            rows.append(VGroup(lab, b, v))

        self.go(FadeIn(head), Create(axis), rt=0.4)
        self.cue("disambiguation", fallback=0.1)
        self.go(*[FadeIn(r[0]) for r in rows[:3]], *[GrowFromEdge(r[1], LEFT) for r in rows[:3]],
                *[FadeIn(r[2]) for r in rows[:3]], rt=0.6)
        self.cue("Conflation", fallback=0.62)
        self.go(*[FadeIn(r[0]) for r in rows[3:]], *[GrowFromEdge(r[1], LEFT) for r in rows[3:]],
                *[FadeIn(r[2]) for r in rows[3:]], rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_References — references [1]–[12] checked: [6] fabricated; [9]–[12] wrong details.
# ─────────────────────────────────────────────────────────────────────────────
class B07_References(Scene):
    BID = "B07"
    FALLBACK = 14.9

    def construct(self):
        srcs = VGroup(*[chip(s, 34) for s in ("Google Scholar", "Crossref", "arXiv")]).arrange(RIGHT, buff=0.4).move_to(UP * 2.95)
        cells = []
        for i in range(12):
            x = -5.0 + (i % 6) * 2.0
            y = 1.45 if i < 6 else 0.25
            box = card(1.7, 0.95, stroke=SLATE, sw=2.5).move_to(RIGHT * x + UP * y)
            t = sans(f"[{i + 1}]", 34).move_to(box)
            cells.append(VGroup(box, t))
        fab = cells[5]
        bad = cells[8:12]
        l1 = VGroup(sans("[6] FABRICATED", 38), serif("the paper does not exist", 36)).arrange(RIGHT, buff=0.4).move_to(DOWN * 1.25)
        l2 = VGroup(sans("[9]–[12] wrong details", 38), serif("authors or venue", 36)).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.3)

        self.go(LaggedStart(*[FadeIn(c) for c in srcs], lag_ratio=0.2), rt=0.8)
        self.cue("first", fallback=0.45)
        self.go(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.06), rt=1.0)
        self.cue("fabricated", fallback=0.6)
        self.go(fab[0].animate.set_stroke(CRIMSON, width=6), Create(strike(fab[1])), FadeIn(l1), rt=0.5)
        self.cue("Four", fallback=0.78)
        self.go(*[c[0].animate.set_stroke(CRIMSON, width=4) for c in bad], FadeIn(l2), rt=0.5)
        self.finish()
