"""scenes.py — Manim scenes for "From 94.2 Percent to 0.49" (kappa).

Same project as the Week 1–4 reels, so the same visuals: the helper block and clocked Beat base
(`Scene = Beat`) from hai-videos/Week4/progress-proudest-number/scenes.py, Week 1's judge logos
and bar style (Week1/learning-agreement-not-accuracy B02/B03), Week 4's strike → arrow → teal
underline swap rows, outline cards/chips and the type sizes that passed GATE T.

Every number on screen appears in inbox/term2-week05/term2-week5-video-content.md as written.
Only Professor Brown is ever named; the critic is "the reviewer". WORDING LAW: kappa is
agreement corrected for chance, never accuracy.

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
#  B01_ChanceBaseline — 94.2% agreement; the reviewer: what would chance give? 45% approved.
# ─────────────────────────────────────────────────────────────────────────────
class B01_ChanceBaseline(Scene):
    BID = "B01"
    FALLBACK = 16.7

    def construct(self):
        box = card(5.6, 4.0, stroke=SLATE, sw=3).move_to(LEFT * 3.0 + UP * 0.5)
        n = sans("94.2%", 96)
        a = serif("agreement", 40)
        judges = VGroup(*[ink_logo(x, 0.5) for x in ("mistral", "openai", "claude")]).arrange(RIGHT, buff=0.45)
        j_t = serif("three AI judges", 34)
        VGroup(n, a, judges, j_t).arrange(DOWN, buff=0.22).move_to(box)
        who = sans("the reviewer", 32, MUTED).move_to(RIGHT * 3.4 + UP * 2.6)
        q_box = DashedVMobject(RoundedRectangle(width=4.6, height=1.2, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=36)
        q_box.move_to(RIGHT * 3.4 + UP * 1.6)
        q = serif("chance baseline?", 42).move_to(q_box)
        qa = arrow(RIGHT * 1.0 + UP * 1.6, RIGHT * 0.05 + UP * 1.2)
        base = chip("45% approved", 40, stroke=TEAL).move_to(RIGHT * 3.4 + DOWN * 0.4)
        base_t = serif("one tag on 45% of items", 34).move_to(RIGHT * 3.4 + DOWN * 1.25)
        cap = serif("Judges can agree a lot just by chance.", 40).move_to(DOWN * 2.6)

        self.go(Create(box), FadeIn(n), FadeIn(a), rt=0.7)
        self.cue("three", fallback=0.2)
        self.go(LaggedStart(*[FadeIn(j, shift=UP * 0.1) for j in judges], lag_ratio=0.2), FadeIn(j_t), rt=0.7)
        self.cue("reviewer", fallback=0.33)
        self.go(FadeIn(who), rt=0.3)
        self.cue("chance", fallback=0.5)
        self.go(Create(q_box), FadeIn(q), GrowArrow(qa), rt=0.6)
        self.cue("45", fallback=0.63)
        self.go(FadeIn(base), FadeIn(base_t), rt=0.5)
        self.cue("agree", fallback=0.82)
        self.go(FadeIn(cap, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Supabase — individual tags live in the Supabase audit table; paused → restored; 10,049 rows.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Supabase(Scene):
    BID = "B02"
    FALLBACK = 15.3

    def construct(self):
        head = serif("Needed: each model's individual tags", 40).move_to(UP * 2.95)
        l_box = card(4.0, 2.2, stroke=MUTED).move_to(LEFT * 3.9 + UP * 0.6)
        l_t = VGroup(serif("local files", 38), serif("final vote only", 34)).arrange(DOWN, buff=0.15).move_to(l_box)
        a = arrow(LEFT * 1.8 + UP * 0.6, LEFT * 0.75 + UP * 0.6)
        r_box = card(6.3, 3.9, stroke=SLATE, sw=3).move_to(RIGHT * 2.6 + UP * 0.2)
        r_h = VGroup(ink_logo("supabase", 0.55), sans("audit table", 38)).arrange(RIGHT, buff=0.25)
        r_h.move_to(RIGHT * 2.6 + UP * 1.55)
        paused = chip("paused from inactivity", 34, stroke=MUTED).move_to(RIGHT * 2.6 + UP * 0.55)
        restored = chip("restored", 36, stroke=TEAL).move_to(RIGHT * 2.6 + UP * 0.55)
        rows = sans("10,049 rows", 52).move_to(RIGHT * 2.3 + DOWN * 0.65)
        intact = serif("intact", 38, TEAL).next_to(rows, DOWN, buff=0.15)
        ok = tick(s=0.42).next_to(rows, RIGHT, buff=0.3)

        self.go(FadeIn(head), rt=0.4)
        self.cue("final", fallback=0.25)
        self.go(Create(l_box), FadeIn(l_t), rt=0.6)
        self.cue("Supabase", fallback=0.42)
        self.go(GrowArrow(a), Create(r_box), FadeIn(r_h), rt=0.6)
        self.cue("paused", fallback=0.55)
        self.go(FadeIn(paused), rt=0.4)
        self.cue("restored", fallback=0.7)
        self.go(ReplacementTransform(paused, restored), rt=0.5)
        self.cue("10,049", fallback=0.85)
        self.go(FadeIn(rows), FadeIn(intact), Create(ok), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Script — agreement_metrics.py (~800 lines): Fleiss, pairwise Cohen, the dissenter.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Script(Scene):
    BID = "B03"
    FALLBACK = 11.3

    def construct(self):
        box = card(4.8, 2.8, stroke=SLATE, sw=3).move_to(LEFT * 3.5 + UP * 0.2)
        f = serif("agreement_metrics.py", 38)
        ln = sans("~800 lines", 46, TEAL)
        VGroup(f, ln).arrange(DOWN, buff=0.3).move_to(box)
        outs = [chip("Fleiss' kappa · all three judges", 34), chip("Cohen's kappa · each pair", 34),
                chip("dissenter in 2/1 splits", 34)]
        ys = [1.5, 0.2, -1.1]
        for o, y in zip(outs, ys):
            o.move_to(RIGHT * 0.3 + UP * y, aligned_edge=LEFT)
        arrows = [arrow(LEFT * 1.0 + UP * 0.2, RIGHT * 0.2 + UP * y) for y in ys]
        head = serif("Then I built a script", 40).move_to(UP * 2.95)

        self.go(FadeIn(head), Create(box), FadeIn(f), rt=0.6)
        self.cue("800", fallback=0.2)
        self.go(FadeIn(ln), rt=0.4)
        for i, (w, fb) in enumerate([("Fleiss'", 0.38), ("Cohen's", 0.6), ("dissents", 0.82)]):
            self.cue(w, fallback=fb)
            self.go(GrowArrow(arrows[i]), FadeIn(outs[i], shift=RIGHT * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Result — keywords 0.4884 moderate (N = 8,967); acronyms 0.3847 fair (N = 885).
# ─────────────────────────────────────────────────────────────────────────────
class B04_Result(Scene):
    BID = "B04"
    FALLBACK = 11.4

    def result(self, x, name, k, label, n, stroke):
        box = card(5.4, 4.6, stroke=stroke, sw=4).move_to(RIGHT * x + DOWN * 0.2)
        parts = VGroup(sans(name, 40), serif("Fleiss' kappa", 36), sans(k, 84),
                       sans(label, 40, stroke), serif(n, 36)).arrange(DOWN, buff=0.2).move_to(box)
        return VGroup(box, parts)

    def construct(self):
        head = serif("The result", 44).move_to(UP * 3.0)
        kw = self.result(-3.05, "Keywords", "0.4884", "moderate", "N = 8,967 valid", TEAL)
        ac = self.result(3.05, "Acronyms", "0.3847", "fair", "N = 885 valid", SLATE)

        self.go(FadeIn(head), rt=0.4)
        self.cue("8,967", fallback=0.2)
        self.go(Create(kw[0]), FadeIn(kw[1][0]), FadeIn(kw[1][4]), rt=0.6)
        self.cue("Fleiss'", fallback=0.4)
        self.go(FadeIn(kw[1][1]), FadeIn(kw[1][2], scale=0.9), rt=0.5)
        self.cue("moderate", fallback=0.6)
        self.go(FadeIn(kw[1][3]), rt=0.3)
        self.cue("acronyms", fallback=0.72)
        self.go(Create(ac[0]), FadeIn(ac[1][:3]), FadeIn(ac[1][4]), rt=0.6)
        self.cue("fair", fallback=0.92)
        self.go(FadeIn(ac[1][3]), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Pairs — pairwise Cohen's kappa bars; GPT-4o-mini dissents in 55.8% of splits.
#  (Week 1 B03_Calibration bar style, laid on its side.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Pairs(Scene):
    BID = "B05"
    FALLBACK = 18.6
    X0, K = -0.5, 6.0
    PAIRS = [("mistral", "claude", "Mistral – Claude", 0.6559, "0.6559", TEAL),
             ("mistral", "openai", "Mistral – GPT-4o-mini", 0.4251, "0.4251", SLATE),
             ("openai", "claude", "GPT-4o-mini – Claude", 0.4022, "0.4022", SLATE)]
    YS = [1.7, 0.45, -0.8]

    def construct(self):
        head = serif("Pairwise Cohen's kappa", 40).move_to(UP * 2.95)
        base = Line(RIGHT * self.X0 + UP * 2.3, RIGHT * self.X0 + DOWN * 1.4, color=SLATE, stroke_width=3)
        labels, bars, vals = [], [], []
        for (a, b, name, k, ks, col), y in zip(self.PAIRS, self.YS):
            lab = VGroup(ink_logo(a, 0.4), ink_logo(b, 0.4), serif(name, 34)).arrange(RIGHT, buff=0.2)
            lab.move_to(RIGHT * (self.X0 - 0.25) + UP * y, aligned_edge=RIGHT)
            labels.append(lab)
            bar = Rectangle(width=k * self.K, height=0.62, fill_color=col, fill_opacity=1, stroke_opacity=0)
            bar.move_to(RIGHT * self.X0 + UP * y, aligned_edge=LEFT)
            bars.append(bar)
            vals.append(sans(ks, 40).next_to(bar, RIGHT, buff=0.2))
        dis = chip("GPT-4o-mini is the dissenter in 55.8% of 2/1 splits", 36).move_to(DOWN * 2.35)

        self.go(FadeIn(head), Create(base), rt=0.5)
        self.cue("Mistral", fallback=0.12)
        self.go(FadeIn(labels[0]), GrowFromEdge(bars[0], LEFT), rt=0.6)
        self.cue("0.66", fallback=0.3)
        self.go(FadeIn(vals[0]), rt=0.3)
        self.cue("Both", fallback=0.37)
        self.go(*[FadeIn(l) for l in labels[1:]], *[GrowFromEdge(b, LEFT) for b in bars[1:]], rt=0.7)
        self.cue("near", fallback=0.55)
        self.go(*[FadeIn(v) for v in vals[1:]], rt=0.4)
        self.cue("dissenter", fallback=0.85)
        self.go(FadeIn(dis, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Fixes — two of my own errors corrected; one line added to the abstract.
#  (Week 4 B03 swap rows: old struck → arrow → new underlined.)
# ─────────────────────────────────────────────────────────────────────────────
class B06_Fixes(Scene):
    BID = "B06"
    FALLBACK = 26.9
    OX, NX = -3.6, -0.6

    def construct(self):
        head = serif("Two errors in my own paper", 40).move_to(UP * 3.0)
        o1 = sans("5.8%", 46).move_to(RIGHT * self.OX + UP * 1.85)
        o1n = serif("of 10,049", 32).next_to(o1, DOWN, buff=0.12)
        n1 = sans("6.5%", 50, TEAL).move_to(RIGHT * self.NX + UP * 1.85, aligned_edge=LEFT)
        n1n = serif("586 / 8,967 valid items", 36).next_to(n1, RIGHT, buff=0.35)
        o2 = serif("~74% chance", 42).move_to(RIGHT * self.OX + UP * 0.25)
        o2n = serif("the acronym rate", 32).next_to(o2, DOWN, buff=0.12)
        n2 = serif("~67% chance", 42).move_to(RIGHT * self.NX + UP * 0.25, aligned_edge=LEFT)
        n2n = serif("for keywords", 36).next_to(n2, RIGHT, buff=0.35)
        ys = [1.85, 0.25]
        arrows = [arrow(LEFT * 2.05 + UP * y, LEFT * 0.85 + UP * y) for y in ys]
        s1, s2 = strike(o1), strike(o2)
        u1, u2 = under(n1), under(n2)
        a_lab = sans("added to the abstract", 34, TEAL).move_to(DOWN * 1.25)
        a_box = card(11.6, 1.3, stroke=TEAL, sw=3).move_to(DOWN * 2.3)
        a_t = serif("Accuracy against expert ground truth was not measured.", 36).move_to(a_box)

        self.go(FadeIn(head), rt=0.4)
        self.cue("review", fallback=0.12)
        self.go(FadeIn(o1), FadeIn(o1n), rt=0.4)
        self.cue("586", fallback=0.3)
        self.go(Create(s1), GrowArrow(arrows[0]), FadeIn(n1), FadeIn(n1n), rt=0.6)
        self.go(Create(u1), rt=0.3)
        self.cue("acronym", fallback=0.48)
        self.go(FadeIn(o2), FadeIn(o2n), rt=0.4)
        self.cue("right", fallback=0.62)
        self.go(Create(s2), GrowArrow(arrows[1]), FadeIn(n2), FadeIn(n2n), rt=0.6)
        self.go(Create(u2), rt=0.3)
        self.cue("abstract", fallback=0.78)
        self.go(FadeIn(a_lab), Create(a_box), rt=0.5)
        self.cue("accuracy", fallback=0.84)
        self.go(FadeIn(a_t, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_SameData — 94.2% raw → 0.49 after chance: same data, different claim.
# ─────────────────────────────────────────────────────────────────────────────
class B07_SameData(Scene):
    BID = "B07"
    FALLBACK = 6.9

    def construct(self):
        head = serif("The data didn't change. The claim did.", 42).move_to(UP * 2.9)
        l = VGroup(sans("94.2%", 96), serif("raw agreement", 40)).arrange(DOWN, buff=0.2).move_to(LEFT * 3.4 + UP * 0.4)
        r = VGroup(sans("0.49", 96, TEAL), serif("moderate, after chance", 40)).arrange(DOWN, buff=0.2).move_to(RIGHT * 3.4 + UP * 0.4)
        a = arrow(LEFT * 0.9 + UP * 0.6, RIGHT * 0.9 + UP * 0.6)
        cap = sans("same data, different claim", 42).move_to(DOWN * 2.3)
        u = under(cap)

        # GATE T §8.3b: a mid-fade "0.49" read as low contrast, so both numbers land at once
        self.go(FadeIn(head), FadeIn(l), FadeIn(r), rt=0.4)
        self.cue("from", fallback=0.45)
        self.go(GrowArrow(a), rt=0.4)
        self.cue("after", fallback=0.85)
        self.go(FadeIn(cap), Create(u), rt=0.4)
        self.finish()
