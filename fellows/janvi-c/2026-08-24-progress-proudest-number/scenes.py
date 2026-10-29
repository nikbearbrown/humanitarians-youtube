"""scenes.py — Manim scenes for "The Number I Was Proudest Of" (proudest-number).

Same project as the Week 1–3 reels, so the same visuals: the helper block and clocked Beat base
(`Scene = Beat`) from hai-videos/Week3/progress-choosing-a-journal/scenes.py, Week 1's
strike/highlight helpers and paper-strip idea (2026-08-07-qa-paper-oversell B08_SelfReview),
outline cards/chips, `cue()` on spoken words and the type sizes that passed GATE T.

Credit rule: the critique came from the professor ("my professor"; only Professor Brown is ever
named); CRITIQ helped make the fixes, it didn't find them; Janvi made the revisions.
WORDING LAW: "verified" appears only as the word being struck out.

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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Sections — JBI's remaining required sections tick; the new Gene Ontology section.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Sections(Scene):
    BID = "B01"
    FALLBACK = 14.6
    SECTIONS = ["Acknowledgments", "Funding", "Author Contributions", "Conflict of Interest", "Data Availability"]
    GO = ["the API", "the category gate", "the silent fallback", "why GO over other ontologies"]

    def construct(self):
        head = sans("required sections", 36, MUTED).move_to(LEFT * 5.4 + UP * 2.85, aligned_edge=LEFT)
        secs = VGroup(*[serif(s, 38) for s in self.SECTIONS]).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        secs.move_to(LEFT * 5.4 + UP * 0.15, aligned_edge=LEFT)
        ticks = [tick().next_to(s, LEFT, buff=0.2) for s in secs]
        box = card(5.9, 4.9, stroke=TEAL, sw=4).move_to(RIGHT * 3.0 + DOWN * 0.1)
        g_new = sans("new section", 32, TEAL)
        g_t = serif("Gene Ontology", 46)
        chips = [chip(c, 32) for c in self.GO]
        col = VGroup(g_new, g_t, *chips).arrange(DOWN, buff=0.2).move_to(box)
        miss = serif("the paper had been missing it", 32, MUTED).next_to(box, UP, buff=0.15)

        self.go(FadeIn(head), FadeIn(secs), rt=0.6)
        self.cue("finished", fallback=0.08)
        self.go(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.2), rt=1.2)
        self.cue("Gene", fallback=0.4)
        self.go(Create(box), FadeIn(g_new), FadeIn(g_t), rt=0.7)
        self.cue("missing", fallback=0.6)
        self.go(FadeIn(miss), rt=0.4)
        for i, (w, fb) in enumerate([("API", 0.7), ("category", 0.8), ("silent", 0.86), ("why", 0.93)]):
            self.cue(w, fallback=fb)
            self.go(FadeIn(chips[i], shift=UP * 0.1), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_TenItems — a ten-item critique sorted into three bins; the first fixed this week.
# ─────────────────────────────────────────────────────────────────────────────
class B02_TenItems(Scene):
    BID = "B02"
    FALLBACK = 14.7
    BINS = ["fixable with existing data", "needs new experiments", "needs a professor's input"]
    YS = [1.75, 0.0, -1.75]

    def construct(self):
        c_box = card(3.5, 3.2, stroke=SLATE, sw=3).move_to(LEFT * 4.2)
        c_n = sans("10", 80)
        c_t = serif("item critique", 38)
        c_f = serif("from my professor", 32, MUTED)
        VGroup(c_n, c_t, c_f).arrange(DOWN, buff=0.15).move_to(c_box)
        bins, arrows = [], []
        for label, y in zip(self.BINS, self.YS):
            b = card(6.9, 1.4, stroke=MUTED).move_to(RIGHT * 2.45 + UP * y)
            t = serif(label, 38).move_to(b)
            bins.append(VGroup(b, t))
            arrows.append(arrow(LEFT * 2.3 + UP * y * 0.5, LEFT * 1.1 + UP * y))
        done = serif("fixed this week, edits with CRITIQ", 32, TEAL)
        ok = tick()

        self.go(Create(c_box), rt=0.5)
        self.cue("ten", fallback=0.1)
        self.go(FadeIn(c_n, scale=0.8), FadeIn(c_t), FadeIn(c_f), rt=0.6)
        for i, (w, fb) in enumerate([("fixable", 0.33), ("new", 0.47), ("professor's", 0.58)]):
            self.cue(w, nth=1, fallback=fb)
            self.go(GrowArrow(arrows[i]), Create(bins[i][0]), FadeIn(bins[i][1]), rt=0.5)
        self.cue("fixed", fallback=0.7)
        b0 = bins[0]
        self.go(b0[0].animate.set_stroke(TEAL, width=5), b0[1].animate.shift(UP * 0.22), rt=0.5)
        done.move_to(b0[0]).shift(DOWN * 0.3)
        ok.next_to(done, LEFT, buff=0.2)
        self.cue("CRITIQ", fallback=0.85)
        self.go(FadeIn(done), Create(ok), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_WordSwaps — three wording fixes: old struck, new highlighted.
# ─────────────────────────────────────────────────────────────────────────────
class B03_WordSwaps(Scene):
    BID = "B03"
    FALLBACK = 16.3
    OX, NX = -3.75, -0.55

    def construct(self):
        head = serif("Some were wording", 40, MUTED).move_to(UP * 3.0)
        olds = [serif("verified", 40), serif("a large language model", 40),
                serif("independently verified", 40)]
        news = [lines(["curated"], 40),
                VGroup(lines(["GPT-4o-mini (OpenAI)"], 40), logo("openai", 0.45).set_fill(INK, opacity=1)).arrange(RIGHT, buff=0.25),
                lines(["internal quality control", "by two co-authors", "with domain expertise"], 36)]
        ys = [1.95, 0.75, -1.35]
        for o, nw, y in zip(olds, news, ys):
            o.move_to(RIGHT * self.OX + UP * y)
            nw.move_to(RIGHT * self.NX + UP * y, aligned_edge=LEFT)
        arrows = [arrow(RIGHT * -1.5 + UP * y, RIGHT * -0.8 + UP * y) for y in ys]
        strikes = [strike(o) for o in olds]
        def under(t):
            return Line(t.get_corner(DL) + DOWN * 0.08, t.get_corner(DR) + DOWN * 0.08, color=TEAL, stroke_width=5)
        # GATE V: gold highlight fills read as low-contrast here, so the new wording is underlined in teal
        hls = [VGroup(*[under(t) for t in news[0]]),
               VGroup(under(news[1][0][0])),
               VGroup(*[under(t) for t in news[2]])]
        where = serif("across the whole paper", 34, TEAL).next_to(news[0], RIGHT, buff=0.5)

        self.go(FadeIn(head), rt=0.4)
        cues = [("Verified", "curated", 0.12, 0.2), ("large", "G", 0.4, 0.5), ("independently", "internal", 0.7, 0.78)]
        for i, (w1, w2, f1, f2) in enumerate(cues):
            self.cue(w1, fallback=f1)
            self.go(FadeIn(olds[i]), rt=0.3)
            self.go(Create(strikes[i]), rt=0.3)
            self.cue(w2, fallback=f2)
            self.go(GrowArrow(arrows[i]), FadeIn(news[i], shift=LEFT * 0.1), rt=0.4)
            self.go(Create(hls[i]), rt=0.3)
            if i == 0:
                self.go(FadeIn(where), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Pattern — one oversold sentence in week one; "verified" was in every section.
#  (Week 1 B08_SelfReview paper strips.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_Pattern(Scene):
    BID = "B04"
    FALLBACK = 16.2
    ROWS = [[1.6, 1.1, 1.9, 0.9], [1.2, 2.0, 1.0, 1.3], [1.8, 0.9, 1.5, 1.2],
            [1.0, 1.7, 1.3, 1.4], [1.5, 1.2, 1.0, 1.8], [1.3, 1.6, 1.8, 0.8]]
    PICK = [2, 1, 3, 0, 2, 1]

    def construct(self):
        head = sans("the paper", 32, MUTED).move_to(LEFT * 5.6 + UP * 3.0, aligned_edge=LEFT)
        rows = []
        for i, ws in enumerate(self.ROWS):
            r = VGroup(*[RoundedRectangle(width=w * 0.8, height=0.34, corner_radius=0.17, fill_color=SLATE,
                                          fill_opacity=0.5, stroke_opacity=0) for w in ws]).arrange(RIGHT, buff=0.22)
            r.move_to(LEFT * 5.6 + UP * (2.4 - i * 0.55), aligned_edge=LEFT)
            rows.append(r)
        one = lines(["week one:", "one oversold sentence"], 36).move_to(RIGHT * 0.5 + UP * 2.05, aligned_edge=LEFT)
        every = serif("“verified” in every section", 36).move_to(RIGHT * 0.5 + UP * 0.75, aligned_edge=LEFT)
        whole = serif("the paper's whole claim", 36, TEAL).move_to(RIGHT * 0.5 + UP * 0.1, aligned_edge=LEFT)
        bracket = Line(LEFT * 0.05 + UP * 2.6, LEFT * 0.05 + DOWN * 0.4, color=SLATE, stroke_width=3)
        saw = serif("My professor saw the pattern I missed from inside.", 36).move_to(DOWN * 1.15)
        l1 = serif("Self-review catches local problems.", 40).move_to(DOWN * 1.95)
        l2 = sans("Outside review catches systemic ones.", 40, TEAL).move_to(DOWN * 2.75)

        self.go(FadeIn(head), LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.1), rt=0.8)
        self.cue("fixed", fallback=0.1)
        self.go(rows[1][self.PICK[1]].animate.set_fill(GOLD, opacity=0.9), FadeIn(one), rt=0.6)
        self.cue("everywhere", fallback=0.33)
        self.go(LaggedStart(*[rows[i][self.PICK[i]].animate.set_fill(GOLD, opacity=0.9)
                              for i in range(6) if i != 1], lag_ratio=0.15), FadeIn(every), Create(bracket), rt=1.0)
        self.cue("whole", fallback=0.45)
        self.go(FadeIn(whole), rt=0.4)
        self.cue("saw", fallback=0.55)
        self.go(FadeIn(saw, shift=UP * 0.1), rt=0.5)
        self.cue("Self-review", fallback=0.7)
        self.go(FadeIn(l1, shift=UP * 0.1), rt=0.5)
        self.cue("outside", fallback=0.85)
        self.go(FadeIn(l2, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Headline — 94.2% agreement demoted to a routing statistic; 5.8% adjudication leads.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Headline(Scene):
    BID = "B05"
    FALLBACK = 17.1

    def construct(self):
        head = sans("the headline", 36, MUTED).move_to(UP * 3.0)
        big = VGroup(sans("94.2%", 120), serif("agreement", 46)).arrange(DOWN, buff=0.2).move_to(UP * 1.0)
        rout = chip("routing statistic", 44).move_to(DOWN * 1.35)
        notq = serif("not a quality metric", 40).move_to(DOWN * 2.3)
        old = VGroup(big, rout, notq)
        lead_h = sans("now the lead", 36, TEAL).move_to(LEFT * 2.1 + UP * 1.6)
        lead_n = sans("5.8%", 110, TEAL).move_to(LEFT * 2.1 + UP * 0.25)
        lead_t = lines(["of items required", "human adjudication"], 44).move_to(LEFT * 2.1 + DOWN * 1.65)
        lead_t.arrange(DOWN, buff=0.08)
        lead_t.move_to(LEFT * 2.1 + DOWN * 1.65)
        rule = Line(RIGHT * 1.5 + UP * 2.6, RIGHT * 1.5 + DOWN * 2.6, color=MUTED, stroke_width=2)

        self.go(FadeIn(head), rt=0.4)
        self.cue("94.2", fallback=0.2)
        self.go(FadeIn(big, scale=0.9), rt=0.7)
        self.cue("routing", fallback=0.45)
        self.go(FadeIn(rout, shift=UP * 0.1), rt=0.4)
        self.cue("not", fallback=0.55)
        self.go(FadeIn(notq), rt=0.4)
        self.cue("leads", fallback=0.72)
        self.go(old.animate.scale(0.6).move_to(RIGHT * 4.1 + UP * 0.2), FadeOut(head), Create(rule), rt=0.8)
        self.go(FadeIn(lead_h), FadeIn(lead_n, scale=0.9), rt=0.6)
        self.cue("required", fallback=0.86)
        self.go(FadeIn(lead_t, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Funnel — a checked funnel (8,053 + 108 = 8,161) and the reproducibility details.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Funnel(Scene):
    BID = "B06"
    FALLBACK = 19.6
    FX = -3.3

    def construct(self):
        head = serif("a funnel, checked at every step", 36, MUTED).move_to(RIGHT * self.FX + UP * 2.95)
        tiers, ticks = [], []
        for i, (top, bot) in enumerate([(5.0, 4.2), (4.0, 3.2), (3.0, 2.2), (2.0, 1.2)]):
            y = 1.95 - i * 0.95
            p = Polygon(RIGHT * (self.FX - top / 2) + UP * (y + 0.38), RIGHT * (self.FX + top / 2) + UP * (y + 0.38),
                        RIGHT * (self.FX + bot / 2) + UP * (y - 0.38), RIGHT * (self.FX - bot / 2) + UP * (y - 0.38),
                        stroke_color=SLATE, stroke_width=3, fill_opacity=0)
            tiers.append(p)
            ticks.append(tick(s=0.28).move_to(RIGHT * (self.FX + top / 2 + 0.35) + UP * y))
        eq = sans("8,053 + 108 = 8,161", 44).move_to(RIGHT * self.FX + DOWN * 2.35)
        eq_ok = tick(s=0.4).next_to(eq, RIGHT, buff=0.3)
        r_head = sans("to reproduce it", 36, TEAL).move_to(RIGHT * 3.6 + UP * 2.95)
        chips = [chip(c, 34) for c in ("Wikipedia dump date", "GO API access date", "model versions", "temperature settings")]
        col = VGroup(*chips).arrange(DOWN, buff=0.3).move_to(RIGHT * 3.6 + UP * 0.55)
        hours = sans("25 hours", 48, TEAL).move_to(RIGHT * 3.4 + DOWN * 2.6)

        self.go(FadeIn(head), LaggedStart(*[Create(t) for t in tiers], lag_ratio=0.2), rt=1.0)
        self.cue("checks", fallback=0.15)
        self.go(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.25), rt=1.0)
        self.cue("8,053", fallback=0.3)
        self.go(FadeIn(eq), rt=0.5)
        self.cue("8,161", fallback=0.45)
        self.go(Create(eq_ok), tiers[2].animate.set_stroke(TEAL, width=5), rt=0.4)
        self.cue("reproduce", fallback=0.65)
        self.go(FadeIn(r_head), rt=0.4)
        for i, (w, fb) in enumerate([("dump", 0.72), ("API", 0.75), ("model", 0.83), ("temperature", 0.88)]):
            self.cue(w, fallback=fb)
            self.go(FadeIn(chips[i], shift=UP * 0.1), rt=0.3)
        self.cue("25", fallback=0.95)
        self.go(FadeIn(hours, shift=UP * 0.1), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Ethics — the ethics gap my professor flagged; who found vs who fixed.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Ethics(Scene):
    BID = "B07"
    FALLBACK = 12.7

    def construct(self):
        flag = sans("flagged by my professor", 34, MUTED).move_to(UP * 3.0)
        q_box = card(11.6, 1.5, stroke=SLATE, sw=3).move_to(UP * 1.85)
        q = serif("Do students know these definitions are AI-generated?", 40).move_to(q_box)
        added = sans("paragraph added to the paper", 38, TEAL).move_to(UP * 0.55)
        ok = tick(s=0.4).next_to(added, LEFT, buff=0.3)
        lb = card(5.4, 2.0, stroke=SLATE).move_to(LEFT * 3.0 + DOWN * 1.75)
        rb = card(5.4, 2.0, stroke=TEAL, sw=4).move_to(RIGHT * 3.0 + DOWN * 1.75)
        lt = VGroup(sans("CRITIQ", 38), serif("helped make the fixes", 38)).arrange(DOWN, buff=0.15).move_to(lb)
        rt_ = VGroup(sans("my professor", 38, TEAL), serif("found them", 38)).arrange(DOWN, buff=0.15).move_to(rb)

        self.go(FadeIn(flag), rt=0.4)
        self.cue("ethics", fallback=0.12)
        self.go(Create(q_box), rt=0.4)
        self.cue("do", fallback=0.3)
        self.go(FadeIn(q, shift=UP * 0.1), rt=0.6)
        self.cue("paragraph", fallback=0.6)
        self.go(Create(ok), FadeIn(added), rt=0.5)
        self.cue("CRITIQ", fallback=0.72)
        self.go(Create(lb), FadeIn(lt), rt=0.5)
        self.cue("didn't", fallback=0.88)
        self.go(Create(rb), FadeIn(rt_), rt=0.5)
        self.finish()
