"""scenes.py — Manim scenes for "Picking the Right Ontology" (picking-an-ontology).

Same helper block as this week's progress reel (hai-videos/Week4/progress-proudest-number), which
carries the Week 1–3 lineage. B04/B05 adapt Week 2's B03_GeneOntology (category gate → GO lookup
→ prompt grounding) from hai-videos/Week2/progress-someone-elses-pipeline/scenes.py.

Credit rule: the GO lookup lives in Thejus's pipeline (stage 05); the approach was a shared design;
Janvi documented the choice. WORDING LAW: grounding is not proof.

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
#  B01_TheJob — thin abbreviation stubs need an authoritative source to ground the rewrite.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TheJob(Scene):
    BID = "B01"
    FALLBACK = 11.0

    def construct(self):
        head = serif("The job", 44).move_to(UP * 2.95)
        a_box = card(5.0, 3.4, stroke=SLATE, sw=3).move_to(LEFT * 3.4 + DOWN * 0.1)
        a_t = sans("abbreviation", 40)
        a_ex = serif("gene and pathway names", 34, MUTED)
        stub = Line(LEFT * 0.9, RIGHT * 0.9, color=MUTED, stroke_width=2)
        stub_t = serif("a thin, one-line definition", 34)
        VGroup(a_t, a_ex, stub, stub_t).arrange(DOWN, buff=0.3).move_to(a_box)
        s_box = DashedVMobject(RoundedRectangle(width=4.6, height=3.4, corner_radius=0.18,
                                                stroke_color=TEAL, stroke_width=3), num_dashes=44)
        s_box.move_to(RIGHT * 3.6 + DOWN * 0.1)
        s_t = VGroup(serif("an authoritative", 38), serif("source", 38)).arrange(DOWN, buff=0.08)
        s_sub = VGroup(serif("to ground the", 32, MUTED), serif("model's rewrite", 32, MUTED)).arrange(DOWN, buff=0.06)
        VGroup(s_t, s_sub).arrange(DOWN, buff=0.3).move_to(s_box)
        a = arrow(LEFT * 0.75 + DOWN * 0.1, RIGHT * 1.15 + DOWN * 0.1, color=TEAL)
        need = sans("needs grounding", 34, TEAL).move_to(RIGHT * 0.2 + DOWN * 2.6)

        self.go(FadeIn(head), rt=0.4)
        self.cue("abbreviations", fallback=0.15)
        self.go(Create(a_box), FadeIn(a_t), FadeIn(a_ex), rt=0.6)
        self.cue("thin", fallback=0.4)
        self.go(Create(stub), FadeIn(stub_t), rt=0.5)
        self.cue("authoritative", fallback=0.65)
        self.go(GrowArrow(a), Create(s_box), FadeIn(s_t), FadeIn(need), rt=0.7)
        self.cue("ground", fallback=0.8)
        self.go(FadeIn(s_sub), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Candidates — NCIt, MeSH, HGNC: what each covers, and what it doesn't.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Candidates(Scene):
    BID = "B02"
    FALLBACK = 17.0
    XS = [-4.15, 0.0, 4.15]
    CANDS = [("NCIt", ["diseases and drugs"], ["not gene functions"]),
             ("MeSH", ["a vocabulary", "built for indexing"], ["not functional", "definitions"]),
             ("HGNC", ["gene names"], ["not broader", "biological processes"])]

    def construct(self):
        head = serif("Several candidates", 44).move_to(UP * 2.95)
        cards = []
        for (name, yes, no), x in zip(self.CANDS, self.XS):
            box = card(3.85, 3.9, stroke=SLATE, sw=3).move_to(RIGHT * x + DOWN * 0.25)
            n = sans(name, 44)
            y = VGroup(*[serif(s, 34) for s in yes]).arrange(DOWN, buff=0.06)
            r = Line(LEFT * 1.3, RIGHT * 1.3, color=MUTED, stroke_width=2)
            nn = VGroup(*[serif(s, 34, MUTED) for s in no]).arrange(DOWN, buff=0.06)
            VGroup(n, y, r, nn).arrange(DOWN, buff=0.25).move_to(box)
            cards.append((box, n, y, r, nn))

        self.go(FadeIn(head), rt=0.4)
        for i, (w, wn, f1, f2) in enumerate([("NCIt", "not", 0.12, 0.25), ("MeSH", "not", 0.35, 0.5),
                                              ("HGNC", "doesn't", 0.75, 0.85)]):
            box, n, y, r, nn = cards[i]
            self.cue(w, fallback=f1)
            self.go(Create(box), FadeIn(n), FadeIn(y), rt=0.6)
            self.cue(wn, nth=i + 1 if wn == "not" else 1, fallback=f2)
            self.go(Create(r), FadeIn(nn), box.animate.set_stroke(MUTED), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_GeneOntology — structured definitions where the stubs were thinnest; public, no login.
# ─────────────────────────────────────────────────────────────────────────────
class B03_GeneOntology(Scene):
    BID = "B03"
    FALLBACK = 12.0

    def construct(self):
        box = card(10.6, 3.3, stroke=TEAL, sw=4).move_to(UP * 1.2)
        t = sans("Gene Ontology", 48, TEAL)
        d = serif("structured definitions for", 38)
        kinds = VGroup(chip("biological processes", 36, stroke=TEAL), chip("molecular functions", 36, stroke=TEAL)).arrange(RIGHT, buff=0.4)
        VGroup(t, d, kinds).arrange(DOWN, buff=0.28).move_to(box)
        where = serif("exactly where our abbreviation stubs were thinnest", 38).move_to(DOWN * 1.15)
        access = VGroup(chip("public API", 36), chip("no login", 36)).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.45)

        self.go(Create(box), FadeIn(t), rt=0.6)
        self.cue("structured", fallback=0.1)
        self.go(FadeIn(d), rt=0.4)
        self.cue("biological", fallback=0.2)
        self.go(FadeIn(kinds[0]), rt=0.3)
        self.cue("molecular", fallback=0.32)
        self.go(FadeIn(kinds[1]), rt=0.3)
        self.cue("exactly", fallback=0.45)
        self.go(FadeIn(where, shift=UP * 0.1), rt=0.5)
        self.cue("public", fallback=0.75)
        self.go(FadeIn(access[0]), rt=0.3)
        self.cue("login", fallback=0.88)
        self.go(FadeIn(access[1]), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Flow — abbreviation → GO autocomplete search → label + definition → prompt,
#  next to textbook sentences. (Adapted from Week 2 B03_GeneOntology.)
# ─────────────────────────────────────────────────────────────────────────────
class B04_Flow(Scene):
    BID = "B04"
    FALLBACK = 13.0

    def construct(self):
        head = serif("In the pipeline", 38, MUTED).move_to(UP * 2.95)
        abbr = chip("abbreviation", 36).move_to(LEFT * 4.55 + UP * 1.2)
        go_b = card(3.9, 1.45, stroke=TEAL, sw=3).move_to(LEFT * 0.55 + UP * 1.2)
        go_t = VGroup(serif("Gene Ontology", 34), serif("autocomplete search", 34)).arrange(DOWN, buff=0.06).move_to(go_b)
        lab = chip("label + definition", 36, stroke=TEAL).move_to(RIGHT * 3.95 + UP * 1.2)
        match = serif("if a match", 32, MUTED).move_to(RIGHT * 1.75 + UP * 2.15)
        pr_b = card(3.2, 1.3, stroke=TEAL, sw=4).move_to(RIGHT * 3.95 + DOWN * 1.3)
        pr_t = sans("prompt", 40, TEAL).move_to(pr_b)
        extra = serif("extra grounding", 32, MUTED).move_to(RIGHT * 3.95 + DOWN * 2.35)
        tb_b = card(3.9, 1.45, stroke=SLATE, sw=3).move_to(LEFT * 0.55 + DOWN * 1.3)
        tb_t = VGroup(serif("sentences from", 34), serif("the textbook", 34)).arrange(DOWN, buff=0.06).move_to(tb_b)
        # fixed coordinates (GATE A stub-safe)
        a1 = arrow(LEFT * 3.2 + UP * 1.2, LEFT * 2.6 + UP * 1.2)
        a2 = arrow(RIGHT * 1.5 + UP * 1.2, RIGHT * 2.05 + UP * 1.2, color=TEAL)
        a3 = arrow(RIGHT * 3.95 + UP * 0.7, RIGHT * 3.95 + DOWN * 0.55, color=TEAL)
        a4 = arrow(RIGHT * 1.5 + DOWN * 1.3, RIGHT * 2.25 + DOWN * 1.3)

        self.go(FadeIn(head), rt=0.4)
        self.cue("abbreviation", fallback=0.1)
        self.go(FadeIn(abbr), rt=0.4)
        self.cue("autocomplete", fallback=0.22)
        self.go(GrowArrow(a1), Create(go_b), FadeIn(go_t), rt=0.6)
        self.cue("match", fallback=0.4)
        self.go(FadeIn(match), rt=0.3)
        self.cue("label", fallback=0.5)
        self.go(GrowArrow(a2), FadeIn(lab), rt=0.5)
        self.cue("prompt", fallback=0.62)
        self.go(GrowArrow(a3), Create(pr_b), FadeIn(pr_t), rt=0.5)
        self.cue("extra", fallback=0.72)
        self.go(FadeIn(extra), rt=0.3)
        self.cue("sentences", fallback=0.85)
        self.go(Create(tb_b), FadeIn(tb_t), GrowArrow(a4), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Gate — only Molecular Biology and Immunology get a lookup; FDA and WHO don't.
#  (Week 2 B03_GeneOntology category gate.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Gate(Scene):
    BID = "B05"
    FALLBACK = 12.0
    GX = -2.6

    def construct(self):
        head = serif("It's gated", 44).move_to(UP * 2.95)
        gate_h = sans("category?", 34).move_to(RIGHT * self.GX + UP * 1.95)
        mb = chip("Molecular Biology", 34, stroke=TEAL).move_to(RIGHT * self.GX + UP * 1.0)
        im = chip("Immunology", 34, stroke=TEAL).move_to(RIGHT * self.GX + UP * 0.05)
        oks = [tick().next_to(mb, RIGHT, buff=0.15), tick().next_to(im, RIGHT, buff=0.15)]
        orgs = VGroup(chip("FDA", 36, stroke=MUTED), chip("WHO", 36, stroke=MUTED)).arrange(RIGHT, buff=0.4)
        orgs.move_to(RIGHT * self.GX + DOWN * 1.35)
        xs = [strike(o[1]) for o in orgs]
        nothing = serif("organizational acronyms: nothing in Gene Ontology", 34, MUTED).move_to(DOWN * 2.5)
        go_b = card(4.0, 1.6, stroke=TEAL, sw=4).move_to(RIGHT * 3.7 + UP * 0.55)
        go_t = VGroup(serif("Gene Ontology", 36), serif("lookup", 36)).arrange(DOWN, buff=0.06).move_to(go_b)
        a = arrow(RIGHT * 0.45 + UP * 0.55, RIGHT * 1.55 + UP * 0.55, color=TEAL)
        no_ask = sans("no lookup", 34).move_to(RIGHT * 3.7 + DOWN * 1.35)

        self.go(FadeIn(head), FadeIn(gate_h), rt=0.5)
        self.cue("molecular", fallback=0.2)
        self.go(FadeIn(mb), Create(oks[0]), rt=0.4)
        self.cue("immunology", fallback=0.3)
        self.go(FadeIn(im), Create(oks[1]), rt=0.4)
        self.cue("lookup", fallback=0.42)
        self.go(GrowArrow(a), Create(go_b), FadeIn(go_t), rt=0.6)
        self.cue("FDA", fallback=0.6)
        self.go(FadeIn(orgs), rt=0.4)
        self.cue("nothing", fallback=0.75)
        self.go(*[Create(x) for x in xs], FadeIn(nothing), rt=0.5)
        self.cue("doesn't", fallback=0.9)
        self.go(FadeIn(no_ask), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — grounding, not proof; the fail path; diseases or drugs need another ontology.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 15.0

    def construct(self):
        head = serif("When not to lean on it", 46).move_to(UP * 2.95)
        rows = [
            VGroup(sans("grounding, not proof", 42, TEAL)),
            VGroup(serif("lookup fails → the definition is still written", 40),
                   serif("and the output still needs review", 36, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(serif("diseases or drugs → a different ontology", 40)),
        ]
        col = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(LEFT * 4.9 + DOWN * 0.15, aligned_edge=LEFT)
        bars = [Line(UP * (r.height / 2 + 0.05), DOWN * (r.height / 2 + 0.05), color=SLATE, stroke_width=6)
                .next_to(r, LEFT, buff=0.3) for r in rows]

        self.go(FadeIn(head), rt=0.4)
        for i, (w, fb) in enumerate([("grounding", 0.12), ("fails", 0.35), ("diseases", 0.78)]):
            self.cue(w, fallback=fb)
            self.go(Create(bars[i]), FadeIn(rows[i][0], shift=RIGHT * 0.1), rt=0.5)
            if i == 1:
                self.cue("review", fallback=0.62)
                self.go(FadeIn(rows[1][1]), rt=0.4)
        self.finish()
