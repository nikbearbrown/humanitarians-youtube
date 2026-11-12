"""scenes.py — Manim scenes for "My Paper Had Fake Citations" (fake-citations).

Same project as the Week 1–8 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week8/progress-best-judge-outvoted/scenes.py (Week 7 block + `vbar`); its B07 reference grid (B01), Week 7 learning B03 labelled rows (B02),
Week 4–8 result cards (B03, B04, B07), Week 6–8 tick checklists (B05, B06).

Every number on screen appears in inbox/term2-week09/term2-week9-video-content.md as written.
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


def checkrow(label, value, y, xl=-5.0, xv=-1.4, ls=34, vs=34):
    """Tick + sans label + serif value on one row (consistency checklist)."""
    t = tick(s=0.34).move_to(RIGHT * (xl - 0.55) + UP * y)
    l = sans(label, ls).move_to(RIGHT * xl + UP * y, aligned_edge=LEFT)
    v = serif(value, vs).move_to(RIGHT * xv + UP * y, aligned_edge=LEFT) if value else VGroup()
    return VGroup(t, l, v)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Remaining — [1]–[12] checked last week ([6] fabricated); [13]–[24] this week; four sources.
#  (Week 8 B07 reference grid, 4 rows.)
# ─────────────────────────────────────────────────────────────────────────────
class B01_Remaining(Scene):
    BID = "B01"
    FALLBACK = 13.1

    def construct(self):
        srcs = VGroup(*[chip(s, 32) for s in ("Google Scholar", "Crossref", "arXiv", "proceedings")]).arrange(RIGHT, buff=0.35).move_to(UP * 2.95)
        cells = []
        for i in range(24):
            x = -5.0 + (i % 6) * 2.0
            y = 1.75 - (i // 6) * 0.95
            box = card(1.7, 0.75, stroke=SLATE, sw=2.5).move_to(RIGHT * x + UP * y)
            t = sans(f"[{i + 1}]", 30).move_to(box)
            cells.append(VGroup(box, t))
        old, new = cells[:12], cells[12:]
        l_old = serif("[1]–[12] checked last week", 34).move_to(LEFT * 3.0 + DOWN * 2.45)
        l_new = sans("[13]–[24] this week", 34, TEAL).move_to(RIGHT * 3.0 + DOWN * 2.45)

        self.go(LaggedStart(*[FadeIn(c) for c in old], lag_ratio=0.05), rt=0.8)
        self.go(old[5][0].animate.set_stroke(CRIMSON, width=5), Create(strike(old[5][1])), FadeIn(l_old), rt=0.5)
        self.cue("remaining", fallback=0.4)
        self.go(LaggedStart(*[FadeIn(c) for c in new], lag_ratio=0.05), FadeIn(l_new), rt=0.8)
        self.go(*[c[0].animate.set_stroke(TEAL, width=4) for c in new], rt=0.4)
        self.cue("Google", fallback=0.6)
        self.go(LaggedStart(*[FadeIn(c) for c in srcs[:3]], lag_ratio=0.2), rt=0.6)
        self.cue("conference", fallback=0.85)
        self.go(FadeIn(srcs[3]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Found — [14] fabricated (0 matches, BEA 2023 on the ACL Anthology); [13], [15], [19] wrong details.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Found(Scene):
    BID = "B02"
    FALLBACK = 16.7

    def construct(self):
        fb = card(11.4, 1.7, stroke=CRIMSON, sw=4).move_to(UP * 2.05)
        f1 = sans("[14] FABRICATED", 44).move_to(fb).shift(UP * 0.35)
        f2 = serif("0 matches in the BEA 2023 proceedings, ACL Anthology", 36).move_to(fb).shift(DOWN * 0.35)
        rows = []
        for y, ref, txt in ((0.35, "[13]", "wrong author initial and title"), (-0.75, "[15]", "wrong third author")):
            rows.append(VGroup(sans(ref, 38).move_to(RIGHT * -5.4 + UP * y, aligned_edge=LEFT),
                               serif(txt, 38).move_to(RIGHT * -4.1 + UP * y, aligned_edge=LEFT)))
        y = -1.85
        r19 = sans("[19]", 38).move_to(RIGHT * -5.4 + UP * y, aligned_edge=LEFT)
        p0 = serif("wrong pages:", 36).move_to(RIGHT * -4.1 + UP * y, aligned_edge=LEFT)
        old = serif("D1009-D1014", 36).next_to(p0, RIGHT, buff=0.3)
        ar = serif("→", 36).next_to(old, RIGHT, buff=0.25)
        new = sans("D940-D946", 36, TEAL).next_to(ar, RIGHT, buff=0.25)

        self.go(Create(fb), FadeIn(f1), rt=0.5)
        self.cue("searched", fallback=0.2)
        self.go(FadeIn(f2), rt=0.5)
        self.cue("Others", fallback=0.6)
        self.go(FadeIn(rows[0]), rt=0.4)
        self.cue("third", fallback=0.75)
        self.go(FadeIn(rows[1]), rt=0.4)
        self.cue("page", fallback=0.88)
        self.go(FadeIn(r19), FadeIn(p0), FadeIn(old), FadeIn(ar), FadeIn(new), Create(strike(old)), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Total — 24 references · 2 fabricated · 7 incorrect details · 37.5%. (8.1 s: shown at once.)
# ─────────────────────────────────────────────────────────────────────────────
class B03_Total(Scene):
    BID = "B03"
    FALLBACK = 8.1

    def construct(self):
        top = sans("24 references", 48).move_to(UP * 2.6)
        a = card(4.8, 1.6, stroke=CRIMSON, sw=4).move_to(LEFT * 2.9 + UP * 0.8)
        at = VGroup(sans("2", 56), serif("fabricated", 36)).arrange(DOWN, buff=0.1).move_to(a)
        b = card(4.8, 1.6, stroke=SLATE, sw=3).move_to(RIGHT * 2.9 + UP * 0.8)
        bt = VGroup(sans("7", 56), serif("incorrect details", 36)).arrange(DOWN, buff=0.1).move_to(b)
        tot = card(6.0, 1.9, stroke=CRIMSON, sw=4).move_to(DOWN * 1.6)
        tt = VGroup(sans("37.5%", 64), serif("had an error", 34)).arrange(DOWN, buff=0.28).move_to(tot)

        self.go(FadeIn(top), Create(a), FadeIn(at), Create(b), FadeIn(bt), Create(tot), FadeIn(tt), rt=0.5)
        self.cue("That's", fallback=0.75)
        self.go(Create(under(tt[0])), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Replace — [6] → Mendes et al. "DBpedia Spotlight" (I-Semantics 2011);
#  [14] → Sarsa et al. "Automatic generation of programming exercises" (ICER 2022).
# ─────────────────────────────────────────────────────────────────────────────
class B04_Replace(Scene):
    """Simplified after two GATE T §8.1 fails: four text runs, all ≥ 46."""
    BID = "B04"
    FALLBACK = 16.5

    def construct(self):
        r6 = sans("[6]", 50).move_to(LEFT * 5.0 + UP * 1.75)
        c6 = card(9.0, 1.9, stroke=TEAL, sw=4).move_to(RIGHT * 1.45 + UP * 1.75)
        t6 = VGroup(sans("DBpedia Spotlight", 48), serif("Mendes et al. · I-Semantics 2011", 48)).arrange(DOWN, buff=0.15).move_to(c6)
        a6 = arrow(LEFT * 4.3 + UP * 1.75, LEFT * 3.1 + UP * 1.75)
        r14 = sans("[14]", 50).move_to(LEFT * 5.0 + DOWN * 0.65)
        c14 = card(9.0, 2.6, stroke=TEAL, sw=4).move_to(RIGHT * 1.45 + DOWN * 0.65)
        t14 = VGroup(sans("Automatic generation of", 46), sans("programming exercises", 46),
                     serif("Sarsa et al. · ICER 2022", 48)).arrange(DOWN, buff=0.12).move_to(c14)
        a14 = arrow(LEFT * 4.3 + DOWN * 0.65, LEFT * 3.1 + DOWN * 0.65)
        tag = chip("several searches", 48).move_to(DOWN * 2.75)

        self.go(FadeIn(r6), FadeIn(r14), Create(strike(r6)), Create(strike(r14)), rt=0.6)
        self.cue("DBpedia", fallback=0.4)
        self.go(GrowArrow(a6), Create(c6), FadeIn(t6), rt=0.5)
        self.cue("2022", fallback=0.6)
        self.go(GrowArrow(a14), Create(c14), FadeIn(t14), rt=0.5)
        self.cue("several", fallback=0.85)
        self.go(FadeIn(tag), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Fixes — 7 corrected · DOI on all 24 · in-text citations re-read.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Fixes(Scene):
    BID = "B05"
    FALLBACK = 7.6

    def construct(self):
        box = card(9.0, 4.2, stroke=SLATE, sw=3).move_to(UP * 0.1)
        rows = [checkrow(l, None, y, xl=-3.4, ls=44) for l, y in
                (("7 corrected", 1.3), ("DOI on all 24", 0.1), ("in-text citations re-read", -1.1))]
        for r in rows:
            r[0].scale(1.2)
        self.go(Create(box), rt=0.4)
        for r, w, fb in zip(rows, ("corrected", "DOI", "checked"), (0.1, 0.35, 0.6)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Consistency — final consistency pass, then a summary of every change to all three professors.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Consistency(Scene):
    BID = "B06"
    FALLBACK = 16.7
    ROWS = [("sensitivity", "74.0% · 20.7% · 79.3%", "sensitivity"), ("ablation", "2,046 · 1,799 · 4.5-fold", "ablation"),
            ("kappa", "0.4884 · 0.3847", "kappa"), ("pipeline funnel", "10,049 → 8,161 → 8,053", "funnel"),
            ("wording", "“curated”, not “verified”", "curated"), ("abstract", "under 300 words", "abstract")]

    def construct(self):
        rows = [checkrow(l, v, 2.7 - i * 0.72, xv=-0.8) for i, (l, v, _) in enumerate(self.ROWS)]
        env = VGroup(Rectangle(width=0.95, height=0.62, stroke_color=SLATE, stroke_width=3, fill_opacity=0),
                     VMobject(stroke_color=SLATE, stroke_width=3).set_points_as_corners([LEFT * 0.475 + UP * 0.31, DOWN * 0.05, RIGHT * 0.475 + UP * 0.31]))
        msg = serif("summary of every change → all three professors", 36)
        mail = VGroup(env, msg).arrange(RIGHT, buff=0.35).move_to(DOWN * 2.35)

        for r, (_, _, w), fb in zip(rows, self.ROWS, (0.12, 0.2, 0.28, 0.38, 0.5, 0.65)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), FadeIn(r[2]), Create(r[0]), rt=0.4)
        self.cue("sent", fallback=0.8)
        self.go(Create(env), FadeIn(msg), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Irony — a pipeline to check AI-generated definitions; a paper with AI-fabricated citations.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Irony(Scene):
    BID = "B07"
    FALLBACK = 11.6

    def construct(self):
        head = sans("the irony", 44).move_to(UP * 2.9)
        l = card(5.7, 2.4, stroke=TEAL, sw=4).move_to(LEFT * 3.0 + UP * 0.6)
        lt = VGroup(serif("a pipeline to check", 38), sans("AI-generated definitions", 30)).arrange(DOWN, buff=0.2).move_to(l)
        r = card(5.7, 2.4, stroke=CRIMSON, sw=4).move_to(RIGHT * 3.0 + UP * 0.6)
        rt_ = VGroup(serif("a paper with", 38), sans("AI-fabricated citations", 30)).arrange(DOWN, buff=0.2).move_to(r)
        bot = serif("most were fine; a real minority weren't", 40).move_to(DOWN * 1.85)

        self.go(FadeIn(head), rt=0.4)
        self.cue("pipeline", fallback=0.15)
        self.go(Create(l), FadeIn(lt), rt=0.5)
        self.cue("own", fallback=0.45)
        self.go(Create(r), FadeIn(rt_), rt=0.5)
        self.cue("Most", fallback=0.75)
        self.go(FadeIn(bot), Create(under(bot)), rt=0.4)
        self.finish()
