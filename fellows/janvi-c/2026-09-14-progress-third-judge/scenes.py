"""scenes.py — Manim scenes for "Is the Third Judge Necessary?" (third-judge).

Same project as the Week 1–6 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week6/progress-self-preference-test/scenes.py (`ink_logo`, `under`), Week 5's
horizontal kappa bars (B02 queue bars), Week 1's segmented triage bar (B06), Week 4–6 result cards.

Every number on screen appears in inbox/term2-week07/term2-week7-video-content.md as written.
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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_DropIt — GPT-4o-mini, the most frequent dissenter: could we keep just Mistral and Claude?
# ─────────────────────────────────────────────────────────────────────────────
class B01_DropIt(Scene):
    BID = "B01"
    FALLBACK = 10.0
    J = [("mistral", "Mistral", -3.8), ("openai", "GPT-4o-mini", 0.0), ("claude", "Claude", 3.8)]

    def construct(self):
        cols = []
        for lg, nm, x in self.J:
            cols.append(VGroup(ink_logo(lg, 1.0), sans(nm, 36)).arrange(DOWN, buff=0.25).move_to(RIGHT * x + UP * 1.2))
        dis = chip("most frequent dissenter", 36).move_to(DOWN * 0.45)
        q_box = DashedVMobject(RoundedRectangle(width=3.6, height=1.2, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=32)
        q_box.move_to(DOWN * 1.9)
        q = serif("drop it?", 46).move_to(q_box)
        keep = [card(3.2, 2.4, stroke=TEAL, sw=4).move_to(RIGHT * x + UP * 1.2) for x in (-3.8, 3.8)]
        k_t = sans("keep just Mistral and Claude?", 36, TEAL).move_to(DOWN * 3.0)

        self.go(*[FadeIn(c) for c in cols], rt=0.6)
        self.cue("most", fallback=0.3)
        self.go(FadeIn(dis), cols[1][0].animate.set_fill(INK, opacity=0.4), rt=0.5)
        self.cue("drop", fallback=0.6)
        self.go(Create(q_box), FadeIn(q), rt=0.5)
        self.cue("keep", fallback=0.75)
        self.go(*[Create(k) for k in keep], FadeIn(k_t), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Ablation — 10,048 rows; Mistral + Claude agree 73.8%; review queue 585 → 2,631 (4.5-fold).
#  (Week 5 B05 horizontal bars.)
# ─────────────────────────────────────────────────────────────────────────────
class B02_Ablation(Scene):
    BID = "B02"
    FALLBACK = 21.1
    X0, K = -2.4, 6.3 / 2631

    def construct(self):
        a_box = card(5.4, 1.7, stroke=SLATE, sw=3).move_to(LEFT * 3.1 + UP * 2.3)
        a_t = VGroup(sans("10,048 valid rows", 38), serif("ablation test, keywords", 32)).arrange(DOWN, buff=0.12).move_to(a_box)
        g_box = card(5.4, 1.7, stroke=TEAL, sw=3).move_to(RIGHT * 3.1 + UP * 2.3)
        g_t = VGroup(VGroup(ink_logo("mistral", 0.4), ink_logo("claude", 0.4), serif("agree on", 34)).arrange(RIGHT, buff=0.2),
                     sans("73.8%", 44, TEAL)).arrange(DOWN, buff=0.12).move_to(g_box)
        head = serif("human review queue", 38).move_to(UP * 0.55)
        axis = Line(RIGHT * self.X0 + UP * 0.05, RIGHT * self.X0 + DOWN * 2.15, color=SLATE, stroke_width=3)
        rows = []
        for lab, n, ns_, col, y in (("3 judges", 585, "585", SLATE, -0.5), ("2 judges", 2631, "2,631", CRIMSON, -1.6)):
            l = serif(lab, 38).move_to(RIGHT * (self.X0 - 0.3) + UP * y, aligned_edge=RIGHT)
            b = Rectangle(width=n * self.K, height=0.62, fill_color=col, fill_opacity=1, stroke_opacity=0)
            b.move_to(RIGHT * self.X0 + UP * y, aligned_edge=LEFT)
            v = sans(ns_, 40).next_to(b, RIGHT, buff=0.2)
            rows.append((l, b, v))
        fold = sans("4.5-fold", 44, TEAL).move_to(LEFT * 4.3 + DOWN * 2.75)

        self.go(Create(a_box), FadeIn(a_t), rt=0.6)
        self.cue("Mistral", fallback=0.22)
        self.go(Create(g_box), FadeIn(g_t), rt=0.6)
        self.cue("two", fallback=0.42)
        self.go(FadeIn(head), Create(axis), rt=0.4)
        self.cue("585", fallback=0.67)
        l, b, v = rows[0]
        self.go(FadeIn(l), GrowFromEdge(b, LEFT), FadeIn(v), rt=0.5)
        self.cue("2,631", fallback=0.8)
        l, b, v = rows[1]
        self.go(FadeIn(l), GrowFromEdge(b, LEFT), FadeIn(v), rt=0.6)
        self.cue("four", fallback=0.88)
        self.go(FadeIn(fold), Create(under(fold)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Changes — 2,046 items (20.4%) change action; GPT-4o-mini broke the tie; 33% cost; 1,799 fewer.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Changes(Scene):
    BID = "B03"
    FALLBACK = 16.7
    POS = [(-3.05, 0.95), (3.05, 0.95), (-3.05, -1.35), (3.05, -1.35)]

    def construct(self):
        head = serif("What changes without it", 40).move_to(UP * 2.95)
        specs = [(sans("2,046 items", 44), serif("change action (20.4%)", 36), SLATE),
                 (VGroup(ink_logo("openai", 0.5), sans("GPT-4o-mini", 38)).arrange(RIGHT, buff=0.2), serif("had broken every tie", 36), SLATE),
                 (sans("33%", 52), serif("API cost saved", 36), SLATE),
                 (sans("1,799", 52), serif("fewer items shipped", 36), CRIMSON)]
        cards = []
        for (a, b, col), (x, y) in zip(specs, self.POS):
            box = card(5.6, 1.95, stroke=col, sw=3 if col == SLATE else 4).move_to(RIGHT * x + UP * y)
            VGroup(a, b).arrange(DOWN, buff=0.15).move_to(box)
            cards.append(VGroup(box, a, b))

        self.go(FadeIn(head), rt=0.3)
        for i, (w, fb) in enumerate([("2,046", 0.05), ("G", 0.37), ("save", 0.6), ("1,799", 0.85)]):
            self.cue(w, fallback=fb)
            self.go(Create(cards[i][0]), FadeIn(cards[i][1:]), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Verdict — not redundant: the tiebreaker. (3.4 s beat: shown at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_Verdict(Scene):
    BID = "B04"
    FALLBACK = 3.4

    def construct(self):
        box = card(9.6, 3.4, stroke=TEAL, sw=4).move_to(UP * 0.2)
        mark = ink_logo("openai", 0.9)
        a = sans("not redundant", 54)
        b = serif("the tiebreaker", 50, TEAL)
        VGroup(mark, a, b).arrange(DOWN, buff=0.25).move_to(box)
        self.go(Create(box), FadeIn(mark), FadeIn(a), FadeIn(b), rt=0.4)
        self.cue("tiebreaker", fallback=0.6)
        self.go(Create(under(b)), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Planted — 200 approved → 150 corrupted (5 types × 30) + 50 controls.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Planted(Scene):
    BID = "B05"
    FALLBACK = 20.8

    def construct(self):
        q = serif("Does the ensemble catch wrong definitions?", 40).move_to(UP * 3.0)
        top = card(7.6, 1.1, stroke=SLATE, sw=3).move_to(UP * 1.85)
        top_t = sans("200 approved definitions", 38).move_to(top)
        lb = card(5.0, 1.6, stroke=CRIMSON, sw=4).move_to(LEFT * 2.9 + UP * 0.05)
        lt = VGroup(sans("150 corrupted", 40), serif("5 types × 30", 34)).arrange(DOWN, buff=0.1).move_to(lb)
        rb = card(4.2, 1.6, stroke=TEAL, sw=4).move_to(RIGHT * 3.4 + UP * 0.05)
        rt_ = VGroup(sans("50 controls", 40), serif("kept untouched", 34)).arrange(DOWN, buff=0.1).move_to(rb)
        al = arrow(LEFT * 1.3 + UP * 1.3, LEFT * 2.0 + UP * 0.9)
        ar = arrow(RIGHT * 1.3 + UP * 1.3, RIGHT * 2.4 + UP * 0.9)
        types = ["conflation", "wrong expansion", "disambiguation", "factual error", "category swap"]
        r1 = VGroup(*[chip(t, 34) for t in types[:3]]).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.55)
        r2 = VGroup(*[chip(t, 34) for t in types[3:]]).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.45)

        self.go(FadeIn(q), rt=0.4)
        self.cue("ground", fallback=0.33)
        self.go(Create(top), FadeIn(top_t), rt=0.5)
        self.cue("150", fallback=0.4)
        self.go(GrowArrow(al), Create(lb), FadeIn(lt), rt=0.6)
        self.cue("five", fallback=0.48)
        self.go(LaggedStart(*[FadeIn(c) for c in [*r1, *r2]], lag_ratio=0.15), rt=1.0)
        self.cue("controls", fallback=0.92)
        self.go(GrowArrow(ar), Create(rb), FadeIn(rt_), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Detection — two judges, blind: caught 30.0% · review 51.3% · through 18.7%; controls 0.0%.
#  (Week 1 B04 segmented triage bar.)
# ─────────────────────────────────────────────────────────────────────────────
class B06_Detection(Scene):
    BID = "B06"
    FALLBACK = 14.2
    W, X0, Y = 11.0, -5.5, 0.6
    SEGS = [(30.0, TEAL), (51.3, SLATE), (18.7, CRIMSON)]

    def construct(self):
        who = VGroup(ink_logo("mistral", 0.45), ink_logo("openai", 0.45),
                     serif("two judges, blind · Claude not in this run", 36)).arrange(RIGHT, buff=0.25).move_to(UP * 2.95)
        segs, x = [], self.X0
        for pct, col in self.SEGS:
            w = self.W * pct / 100
            r = Rectangle(width=w, height=1.0, fill_color=col, fill_opacity=1, stroke_opacity=0)
            r.move_to(RIGHT * x + UP * self.Y, aligned_edge=LEFT)
            segs.append(r)
            x += w
        frame = Rectangle(width=self.W, height=1.0, stroke_color=SLATE, stroke_width=3, fill_opacity=0).move_to(UP * self.Y)
        n_l = serif("150 corrupted", 36).move_to(LEFT * 5.5 + UP * 1.6, aligned_edge=LEFT)
        l_c = serif("caught 30.0%", 36).next_to(segs[0], DOWN, buff=0.25)
        l_r = serif("sent to review 51.3%", 36).next_to(segs[1], DOWN, buff=0.25)
        l_t = serif("passed through 18.7%", 36).move_to(RIGHT * 5.5 + UP * 1.6, aligned_edge=RIGHT)
        c_t = VGroup(serif("50 controls flagged:", 38), sans("0.0%", 46, TEAL)).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.75)
        ok = tick(s=0.4).next_to(c_t, RIGHT, buff=0.3)

        self.go(FadeIn(who), rt=0.5)
        self.cue("strictly", fallback=0.4)
        self.go(Create(frame), FadeIn(n_l), GrowFromEdge(segs[0], LEFT), FadeIn(l_c), rt=0.6)
        self.cue("51.3", fallback=0.55)
        self.go(GrowFromEdge(segs[1], LEFT), FadeIn(l_r), rt=0.5)
        self.cue("18.7", fallback=0.7)
        self.go(GrowFromEdge(segs[2], LEFT), FadeIn(l_t), rt=0.5)
        self.cue("control", fallback=0.85)
        self.go(FadeIn(c_t), Create(ok), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Next — two judges weren't enough: rerun with all three. (5.3 s beat: shown at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B07_Next(Scene):
    BID = "B07"
    FALLBACK = 5.3

    def construct(self):
        box = card(9.6, 3.2, stroke=TEAL, sw=4).move_to(UP * 0.2)
        n = sans("next: rerun with all three", 48)
        logos = VGroup(*[ink_logo(x, 0.7) for x in ("mistral", "openai", "claude")]).arrange(RIGHT, buff=0.7)
        VGroup(n, logos).arrange(DOWN, buff=0.45).move_to(box)
        top = serif("Two judges weren't enough to trust that result.", 38).move_to(UP * 2.75)
        self.go(FadeIn(top), Create(box), FadeIn(n), FadeIn(logos), rt=0.4)
        self.cue("rerun", fallback=0.7)
        self.go(Create(under(n)), rt=0.3)
        self.finish()
