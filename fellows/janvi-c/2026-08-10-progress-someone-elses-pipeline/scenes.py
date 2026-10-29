"""scenes.py — Manim scenes for "Writing Someone Else's Pipeline" (someone-elses-pipeline).

Same project as the Week 1 reels (hai-videos/2026-08-07-qa-paper-oversell,
hai-videos/Week1/learning-agreement-not-accuracy), so the same visuals: the helpers, the clocked
Beat base (`Scene = Beat`), outline cards and chips, the strike/highlight treatment and the
type sizes that passed GATE T. New here: `cue()` places a reveal on a spoken word from
mp3/words.json instead of a hand-measured fraction.

Credit rule: the generation pipeline (stages 00–07) and its design decisions are Thejus's;
Janvi reviewed and documented it. No scene shows Janvi building his stages.

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
#  B01_TwoHalves — Thejus's half generates, Janvi's half reviews; this week: documented his.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TwoHalves(Scene):
    BID = "B01"
    FALLBACK = 15.0
    LX, RX = -3.35, 3.35

    def construct(self):
        head = serif("Medhavy textbook popups: two halves", 46).move_to(UP * 3.0)
        lbox = card(5.6, 3.9).move_to(RIGHT * self.LX + DOWN * 0.2)
        rbox = card(5.6, 3.9).move_to(RIGHT * self.RX + DOWN * 0.2)
        l_name = sans("Thejus", 36).move_to(RIGHT * self.LX + UP * 1.15)
        l_what = serif("generates the definitions", 38).move_to(RIGHT * self.LX + UP * 0.1)
        l_stage = chip("stages 00–07", 32).move_to(RIGHT * self.LX + DOWN * 1.2)
        r_name = sans("Janvi", 36).move_to(RIGHT * self.RX + UP * 1.15)
        r_what = VGroup(serif("reviews them with", 38), serif("three AI judges", 38)).arrange(DOWN, buff=0.1)
        r_what.move_to(RIGHT * self.RX + UP * 0.05)
        judges = VGroup(*[logo(n, 0.5) for n in ("mistral", "openai", "claude")]).arrange(RIGHT, buff=0.5)
        judges.move_to(RIGHT * self.RX + DOWN * 1.0)
        r_stage = sans("stages 10–25", 30, MUTED).move_to(RIGHT * self.RX + DOWN * 1.7)
        flow = Arrow(lbox.get_right(), rbox.get_left(), buff=0.08, color=SLATE, stroke_width=4)
        doc = sans("this week: documented", 32, TEAL).move_to(RIGHT * self.LX + DOWN * 2.75)
        merge = sans("then: two papers → one", 32, TEAL).move_to(RIGHT * self.RX + DOWN * 2.75)

        self.go(FadeIn(head, shift=DOWN * 0.2), rt=0.6)
        self.cue("Thejus", fallback=0.25)
        self.go(Create(lbox), FadeIn(l_name), rt=0.6)
        self.cue("generates", fallback=0.3)
        self.go(FadeIn(l_what, shift=UP * 0.1), FadeIn(l_stage), rt=0.7)
        self.cue("My", fallback=0.45)
        self.go(GrowArrow(flow), Create(rbox), FadeIn(r_name), rt=0.7)
        self.cue("reviews", fallback=0.5)
        self.go(FadeIn(r_what, shift=UP * 0.1), rt=0.6)
        self.cue("three", fallback=0.58)
        self.go(LaggedStart(*[FadeIn(j, shift=UP * 0.15) for j in judges], lag_ratio=0.25),
                FadeIn(r_stage), rt=0.8)
        self.cue("documented", fallback=0.72)
        self.go(lbox.animate.set_stroke(TEAL, width=6), FadeIn(doc, shift=UP * 0.1), rt=0.7)
        self.cue("merged", fallback=0.85)
        self.go(FadeIn(merge, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_EightStages — his repo → Claude Code summary; stages 00–07 light in narration order.
# ─────────────────────────────────────────────────────────────────────────────
class B02_EightStages(Scene):
    BID = "B02"
    FALLBACK = 18.0
    STAGES = [("00", "config"), ("01", "Wikipedia\nextract"), ("02", "clean +\nfilter"),
              ("03", "GPT-4o-mini\nrewrite"), ("04", "abbreviation\nscan"), ("05", "abbreviation\nenrich"),
              ("06", "merge"), ("07", "upload")]
    W, H = 3.0, 1.75

    def stage(self, num, label):
        box = card(self.W, self.H, stroke=MUTED, sw=2.5)
        n = sans(num, 30, MUTED)
        lines = VGroup(*[serif(s, 32) for s in label.split("\n")]).arrange(DOWN, buff=0.12)
        VGroup(n, lines).arrange(DOWN, buff=0.15).move_to(box)
        return VGroup(box, n, lines)

    def construct(self):
        repo = VGroup(logo("github", 0.55), serif("Thejus's repository", 36)).arrange(RIGHT, buff=0.25)
        cc = VGroup(logo("claude-code", 0.45).set_fill(INK, opacity=1), serif("Claude Code summarizes", 36)).arrange(RIGHT, buff=0.25)
        repo.next_to(LEFT * 1.3 + UP * 2.95, LEFT, buff=0.1)       # fixed coordinates (GATE A stub-safe)
        cc.next_to(RIGHT * 0.0 + UP * 2.95, RIGHT, buff=0.1)
        a_top = Arrow(LEFT * 1.2 + UP * 2.95, LEFT * 0.1 + UP * 2.95, buff=0, color=SLATE, stroke_width=4)
        cards = [self.stage(n, l) for n, l in self.STAGES]
        grid = VGroup(*cards).arrange_in_grid(rows=2, cols=4, buff=(0.2, 0.3)).move_to(UP * 0.2)
        words_pos = DOWN * 2.35
        tr = ValueTracker(0)
        cnt = counter(2500, lambda v: f"~{int(round(v / 10) * 10):,} words", 48, TEAL, words_pos, tr)
        cnt_l = serif("written by Janvi about his pipeline", 34, MUTED).move_to(DOWN * 3.05 + LEFT * 0.6)

        def light(*idx):
            anims = []
            for i in idx:
                anims += [cards[i][0].animate.set_stroke(TEAL, width=5), cards[i][1].animate.set_color(TEAL)]
            return anims

        self.go(FadeIn(repo, shift=DOWN * 0.15), rt=0.6)
        self.cue("Claude", fallback=0.12)
        self.go(GrowArrow(a_top), FadeIn(cc), rt=0.7)
        self.cue("eight", fallback=0.25)
        self.go(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.08), rt=1.0)
        self.cue("Wikipedia", fallback=0.36)
        self.go(*light(0, 1), rt=0.5)
        self.cue("filtering", fallback=0.45)
        self.go(*light(2), rt=0.4)
        self.cue("rewrite", fallback=0.6)
        self.go(*light(3), rt=0.4)
        self.cue("abbreviation", fallback=0.66)
        self.go(*light(4, 5), rt=0.5)
        self.cue("merge", fallback=0.74)
        self.go(*light(6), rt=0.3)
        self.cue("upload", fallback=0.78)
        self.go(*light(7), rt=0.3)
        self.cue("wrote", fallback=0.85)
        self.add(cnt)
        self.go(tr.animate.set_value(1), FadeIn(cnt_l), rt=1.2)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_GeneOntology — the category gate, the lookup, the grounding, and the fail path.
# ─────────────────────────────────────────────────────────────────────────────
class B03_GeneOntology(Scene):
    BID = "B03"
    FALLBACK = 22.0

    def construct(self):
        before = serif("earlier draft: how Gene Ontology was used — never explained", 36, MUTED).move_to(UP * 3.05)
        after = sans("traced in the code · tested the API", 36, TEAL).move_to(UP * 3.05)
        stage = serif("stage 05 · abbreviation definitions", 32, MUTED).move_to(UP * 2.3)

        abbr = chip("abbreviation", 34).move_to(LEFT * 5.0 + UP * 0.0)
        gate_h = sans("category?", 32).move_to(LEFT * 1.5 + UP * 1.7)
        cats = [chip("Molecular Biology", 32, stroke=TEAL), chip("Immunology", 32, stroke=TEAL),
                chip("other categories", 32, stroke=MUTED)]
        for c, y in zip(cats, [0.9, 0.0, -0.9]):
            c.move_to(LEFT * 1.5 + UP * y)
        oks = [tick().next_to(cats[0], RIGHT, buff=0.15), tick().next_to(cats[1], RIGHT, buff=0.15)]
        no = strike(cats[2][1])
        go_l = chip("Gene Ontology lookup", 32, stroke=TEAL).move_to(RIGHT * 4.0 + UP * 1.6)
        prompt = chip("prompt grounding", 32).move_to(RIGHT * 4.0 + UP * 0.2)
        out = chip("definition written", 34, stroke=TEAL).move_to(RIGHT * 4.0 + DOWN * 1.3)
        # fixed coordinates (GATE A stub-safe)
        a1 = Arrow(LEFT * 3.65, LEFT * 2.75, buff=0, color=SLATE, stroke_width=4)
        a2 = Arrow(RIGHT * 0.5 + UP * 1.0, RIGHT * 1.95 + UP * 1.55, buff=0, color=TEAL, stroke_width=4)
        a3 = Arrow(RIGHT * 4.0 + UP * 1.25, RIGHT * 4.0 + UP * 0.55, buff=0, color=SLATE, stroke_width=4)
        a4 = Arrow(RIGHT * 4.0 + DOWN * 0.15, RIGHT * 4.0 + DOWN * 0.95, buff=0, color=SLATE, stroke_width=4)
        fail = serif("lookup fails → still written, just without it", 38).move_to(DOWN * 2.6)
        bypass = DashedLine(RIGHT * 0.5 + DOWN * 0.05, RIGHT * 1.95 + DOWN * 1.25,
                            color=SLATE, stroke_width=3, dash_length=0.14)

        self.go(FadeIn(before), rt=0.6)
        self.cue("traced", fallback=0.2)
        self.go(ReplacementTransform(before, after), FadeIn(stage), rt=0.7)
        self.cue("molecular", fallback=0.37)
        self.go(FadeIn(abbr), GrowArrow(a1), FadeIn(gate_h), *[FadeIn(c) for c in cats], rt=0.8)
        self.go(*[Create(o) for o in oks], Create(no), rt=0.5)
        self.cue("fetches", fallback=0.55)
        self.go(GrowArrow(a2), FadeIn(go_l), rt=0.6)
        self.cue("gives", fallback=0.65)
        self.go(GrowArrow(a3), FadeIn(prompt), rt=0.6)
        self.cue("grounding", fallback=0.75)
        self.go(GrowArrow(a4), FadeIn(out), rt=0.6)
        self.cue("fails", fallback=0.83)
        self.go(go_l[0].animate.set_stroke(MUTED), Create(bypass), FadeIn(fail, shift=UP * 0.1), rt=0.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_WikipediaWins — one term in both sets; the merge keeps Wikipedia's; my guess why.
# ─────────────────────────────────────────────────────────────────────────────
class B04_WikipediaWins(Scene):
    BID = "B04"
    FALLBACK = 14.0

    def construct(self):
        head = serif("The hard part: the why", 46).move_to(UP * 3.0)
        cl = Circle(1.55, stroke_color=TEAL, stroke_width=4).move_to(LEFT * 3.55 + DOWN * 0.1)
        cr = Circle(1.55, stroke_color=SLATE, stroke_width=4).move_to(LEFT * 1.65 + DOWN * 0.1)
        wl = VGroup(logo("wikipedia", 0.45), serif("Wikipedia keywords", 32)).arrange(RIGHT, buff=0.15)
        wl.next_to(cl, UP, buff=0.2)
        al = serif("abbreviations", 32).next_to(cr, DOWN, buff=0.2).shift(RIGHT * 0.4)
        term = sans("term", 30).move_to(LEFT * 2.6 + DOWN * 0.1)
        rule_h = sans("stage 06 · merge", 32, MUTED).move_to(RIGHT * 3.5 + UP * 1.5)
        rule = sans("Wikipedia entry wins", 38, TEAL).move_to(RIGHT * 3.3 + UP * 0.8)
        guess_box = DashedVMobject(RoundedRectangle(width=5.2, height=1.9, corner_radius=0.18,
                                                    stroke_color=SLATE, stroke_width=3), num_dashes=40)
        guess_box.move_to(RIGHT * 3.5 + DOWN * 1.2)
        g1 = serif("my guess, from the code:", 32, MUTED)
        g2 = serif("pipeline quality?", 44)
        VGroup(g1, g2).arrange(DOWN, buff=0.15).move_to(guess_box)
        sounded = serif("it sounded right", 34, MUTED).next_to(guess_box, DOWN, buff=0.25)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.cue("both", fallback=0.3)
        self.go(Create(cl), FadeIn(wl), rt=0.6)
        self.cue("abbreviation", fallback=0.42)
        self.go(Create(cr), FadeIn(al), FadeIn(term, scale=0.8), rt=0.6)
        self.cue("wins", fallback=0.55)
        self.go(FadeIn(rule_h), FadeIn(rule, shift=LEFT * 0.2), cl.animate.set_stroke(width=7), rt=0.6)
        self.cue("assumed", fallback=0.7)
        self.go(Create(guess_box), FadeIn(g1), FadeIn(g2), rt=0.8)
        self.cue("sounded", fallback=0.9)
        self.go(FadeIn(sounded), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_RealReason — the guess is struck; the author's reason: definition completeness.
# ─────────────────────────────────────────────────────────────────────────────
class B05_RealReason(Scene):
    BID = "B05"
    FALLBACK = 15.5

    def construct(self):
        g_box = DashedVMobject(RoundedRectangle(width=5.2, height=1.9, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=40)
        g_box.move_to(LEFT * 3.5 + UP * 2.2)
        g1 = serif("my guess, from the code:", 32, MUTED)
        g2 = serif("pipeline quality?", 44, sliceable=True)
        VGroup(g1, g2).arrange(DOWN, buff=0.15).move_to(g_box)
        x = strike(g2, width=7)
        r_box = card(6.2, 1.9, stroke=TEAL, sw=4).move_to(RIGHT * 3.0 + UP * 2.2)
        r1 = sans("definition completeness", 32, TEAL)
        r2 = serif("confirmed with Thejus", 32)
        VGroup(r1, r2).arrange(DOWN, buff=0.18).move_to(r_box)

        lab_w = serif("Wikipedia entry", 34).move_to(LEFT * 4.3 + DOWN * 0.15)
        lab_a = serif("abbreviation entry", 34).move_to(LEFT * 4.3 + DOWN * 1.25)
        x0 = -2.3
        bar_w = Rectangle(width=7.2, height=0.6, fill_color=TEAL, fill_opacity=1, stroke_opacity=0)
        bar_w.move_to(RIGHT * x0 + DOWN * 0.15, aligned_edge=LEFT)
        bar_a = Rectangle(width=3.0, height=0.6, fill_color=SLATE, fill_opacity=1, stroke_opacity=0)
        bar_a.move_to(RIGHT * x0 + DOWN * 1.25, aligned_edge=LEFT)
        t_w = sans("usually a fuller definition", 28, WHITE).move_to(bar_w)
        t_a = serif("from the textbook text", 32).next_to(bar_a, RIGHT, buff=0.25)
        cap = serif("Code shows what was built. It doesn't show why.", 42).move_to(DOWN * 2.7)

        self.add(g_box, g1, g2)
        self.boot()
        self.at(0.02)
        self.go(Create(x), g2.animate.set_color(MUTED), rt=0.6)
        self.cue("checked", fallback=0.15)
        self.go(Create(r_box), FadeIn(r2), rt=0.6)
        self.cue("completeness", fallback=0.3)
        self.go(FadeIn(r1, shift=UP * 0.1), rt=0.5)
        self.cue("Wikipedia", fallback=0.4)
        self.go(FadeIn(lab_w), GrowFromEdge(bar_w, LEFT), rt=0.7)
        self.go(FadeIn(t_w), rt=0.3)
        self.cue("abbreviation", fallback=0.55)
        self.go(FadeIn(lab_a), GrowFromEdge(bar_a, LEFT), FadeIn(t_a), rt=0.7)
        self.cue("Code", fallback=0.78)
        self.go(FadeIn(cap, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_MergedPapers — two papers → one: the four things the merge fixed; 22 hours.
# ─────────────────────────────────────────────────────────────────────────────
class B06_MergedPapers(Scene):
    BID = "B06"
    FALLBACK = 20.5

    def paper(self, w, h, label, stroke=SLATE):
        box = card(w, h, stroke=stroke, sw=3)
        lines = VGroup(*[Line(LEFT * (w / 2 - 0.35), RIGHT * (w / 2 - 0.35), color=MUTED, stroke_width=2)
                         for _ in range(5)]).arrange(DOWN, buff=0.32)
        lines.move_to(box).shift(UP * 0.15)
        t = serif(label, 32).next_to(box, DOWN, buff=0.18)
        return VGroup(box, lines, t)

    def construct(self):
        p1 = self.paper(2.1, 2.8, "generation").move_to(LEFT * 5.0 + UP * 0.4)
        p2 = self.paper(2.1, 2.8, "review").move_to(LEFT * 2.6 + UP * 0.4)
        one = self.paper(2.7, 3.4, "one paper", stroke=TEAL).move_to(LEFT * 3.8 + UP * 0.3)
        items = [
            VGroup(serif("one shared introduction", 38)),
            VGroup(serif("results connect generation to", 38),
                   serif("8,968 popups that reached consensus", 38)).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(serif("consistent terms", 38)),
            VGroup(serif("one stage numbering:", 38),
                   sans("00–07 generation · 10–25 review", 30, TEAL)).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
        ]
        col = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.42).move_to(RIGHT * 2.6 + UP * 0.35)
        col.align_to(LEFT * 1.3, LEFT)
        ticks = [tick().next_to(it[0], LEFT, buff=0.22) for it in items]
        hours = sans("22 hours", 44, TEAL).move_to(LEFT * 3.8 + DOWN * 2.75)

        self.go(FadeIn(p1), FadeIn(p2), rt=0.6)
        self.cue("merged", fallback=0.05)
        self.go(ReplacementTransform(VGroup(p1, p2), one), rt=1.0)
        for i, (w, fb) in enumerate([("shared", 0.18), ("results", 0.3), ("consistent", 0.58), ("numbering", 0.66)]):
            self.cue(w, fallback=fb)
            self.go(Create(ticks[i]), FadeIn(items[i], shift=LEFT * 0.15), rt=0.6)
        self.cue("22", fallback=0.92)
        self.go(FadeIn(hours, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_WhoDidWhat — Claude drafted much of the prose; Janvi decided what it says.
# ─────────────────────────────────────────────────────────────────────────────
class B07_WhoDidWhat(Scene):
    BID = "B07"
    FALLBACK = 6.0
    LX, RX = -3.4, 3.4

    def construct(self):
        head = serif("Who did what", 46).move_to(UP * 2.9)
        div = Line(UP * 1.9, DOWN * 2.3, color=SLATE, stroke_width=2)
        c_h = VGroup(logo("claude", 0.6), sans("Claude", 36)).arrange(RIGHT, buff=0.25)
        c_h.move_to(RIGHT * self.LX + UP * 1.3)
        c_t = VGroup(serif("helped draft much", 40), serif("of the prose", 40)).arrange(DOWN, buff=0.1)
        c_t.move_to(RIGHT * self.LX + DOWN * 0.2)
        j_h = sans("Janvi", 36).move_to(RIGHT * self.RX + UP * 1.3)
        j_t = serif("decided what to say", 40).move_to(RIGHT * self.RX + UP * 0.2)
        j_src = VGroup(chip("from the code", 32), chip("from Thejus", 32, stroke=TEAL)).arrange(RIGHT, buff=0.3)
        j_src.move_to(RIGHT * self.RX + DOWN * 1.1)

        self.go(FadeIn(head), Create(div), FadeIn(c_h), rt=0.5)
        self.go(FadeIn(c_t, shift=UP * 0.1), rt=0.5)
        self.cue("decided", fallback=0.45)
        self.go(FadeIn(j_h), FadeIn(j_t, shift=UP * 0.1), rt=0.5)
        self.cue("code", fallback=0.7)
        self.go(FadeIn(j_src[0]), rt=0.3)
        self.cue("Thejus", fallback=0.85)
        self.go(FadeIn(j_src[1]), rt=0.3)
        self.finish()
