"""scenes.py — Manim scenes for "One Word That Oversold My Paper" (qa-paper-oversell).

Channel @HumanitariansAI · humanitarians palette (brands/hai.md): cream ground,
warm ink text, petrol teal = kept/good, burnt orange = struck/bad (never text),
navy slate = structure, amber gold = highlighter fill only (never text).
Type: EB Garamond (serif body) + Montserrat (sans headers).

Every number on screen comes from SOURCE-LOCKED-FACTS.md. Every scene runs to its
beat's measured narration length (mp3/timings.json), so compile never retimes it.
B06's sentences use disable_ligatures (sliceable=True) so glyph i == character i (word spans for
strikes and highlights). Strike lines are flagged _qc_intentional for GATE B.
"""
from manim import *
import json
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


def serif(s, size=36, color=INK, sliceable=False, **kw):
    """sliceable=True disables ligatures so glyph i == char i (needed only for span());
    elsewhere ligatures stay on, because disabling them breaks Pango's kerning at small sizes."""
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


def chip(label, size=26, stroke=SLATE):
    t = serif(label, size)
    box = RoundedRectangle(width=t.width + 0.45, height=t.height + 0.32,
                           corner_radius=0.16, fill_opacity=0,
                           stroke_color=stroke, stroke_width=2.5)
    t.move_to(box)
    return VGroup(box, t)


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
        return serif(fmt(v), size, color).move_to(pos)
    return always_redraw(build)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ThreeJudges — three providers, five tags, 2-of-3 majority, all-differ → REVIEW.
# ─────────────────────────────────────────────────────────────────────────────
class B04_ThreeJudges(Scene):
    BID = "B04"
    FALLBACK = 25.0
    JUDGES = [("mistral", "Mistral Small", "Mistral AI"),
              ("openai", "GPT-4o-mini", "OpenAI"),
              ("claude", "Claude 3.5 Sonnet", "Anthropic")]
    XS = [-4.3, 0.0, 4.3]
    TAGS = ["approved", "supplementary", "too_basic", "fix_definition", "junk"]

    def construct(self):
        # plain label over a thin rule (a boxed label reads to GATE T as one text run over its interior)
        defn_t = serif("a keyword popup · Medhavy cancer biology textbook", 32).move_to(UP * 3.05)
        defn = VGroup(defn_t, Line(defn_t.get_corner(DL) + DOWN * 0.12, defn_t.get_corner(DR) + DOWN * 0.12,
                                   color=SLATE, stroke_width=3))
        cols = []
        for (lg, name, prov), x in zip(self.JUDGES, self.XS):
            mark = logo(lg, 0.95).move_to(RIGHT * x + UP * 1.75)
            n = sans(name, 28).move_to(RIGHT * x + UP * 0.85)
            p = serif(prov, 26, MUTED).move_to(RIGHT * x + UP * 0.4)
            cols.append(VGroup(mark, n, p))
        # side judges: arrows angle out from the card's edges; the centre judge sits right under it
        arrows = [Arrow(defn.get_corner(DL if x < 0 else DR) + RIGHT * (0.6 if x < 0 else -0.6),
                        RIGHT * x + UP * 2.3, buff=0.08, color=SLATE, stroke_width=3,
                        max_tip_length_to_length_ratio=0.12) if x else None
                  for x in self.XS]
        tag_row = VGroup(*[chip(t, 28) for t in self.TAGS]).arrange(RIGHT, buff=0.22)
        tag_row.move_to(DOWN * 3.0)
        tag_head = serif("five tags, one action each", 28, MUTED).next_to(tag_row, UP, buff=0.22)

        votes1 = ["approved", "approved", "supplementary"]
        v1 = VGroup(*[chip(v, 30).move_to(RIGHT * x + DOWN * 0.45) for v, x in zip(votes1, self.XS)])
        win = sans("2 of 3 agree  →  approved", 34, TEAL).move_to(DOWN * 1.45)
        votes2 = ["approved", "too_basic", "junk"]
        v2 = VGroup(*[chip(v, 30).move_to(RIGHT * x + DOWN * 0.45) for v, x in zip(votes2, self.XS)])
        rev = chip("all 3 differ  →  flagged for human REVIEW", 34, stroke=SLATE)
        rev.move_to(DOWN * 1.45)
        rows = serif("10,049 audit rows", 34).move_to(DOWN * 0.45)
        split = sans("94.2% resolved by majority  ·  5.8% flagged", 38, TEAL).move_to(DOWN * 1.35)

        self.go(FadeIn(defn, shift=DOWN * 0.2), rt=0.6)
        for c, a, cue in zip(cols, arrows, [0.30, 0.34, 0.41]):   # on each model's name
            self.at(cue)
            self.go(*([GrowArrow(a)] if a is not None else []), FadeIn(c, shift=UP * 0.15), rt=0.6)
        self.at(0.49)                                   # "each pick one of five tags"
        self.go(FadeIn(tag_head), LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in tag_row],
                                                lag_ratio=0.15), rt=1.2)
        self.at(0.56)                                   # "If two agree"
        self.go(LaggedStart(*[FadeIn(v, shift=DOWN * 0.3) for v in v1], lag_ratio=0.25), rt=0.9)
        self.go(v1[0][0].animate.set_stroke(TEAL, width=5),
                v1[1][0].animate.set_stroke(TEAL, width=5), FadeIn(win), rt=0.7)
        self.at(0.65)                                   # "If all three differ"
        self.go(FadeOut(v1), FadeOut(win), rt=0.4)
        self.go(LaggedStart(*[FadeIn(v, shift=DOWN * 0.3) for v in v2], lag_ratio=0.25), rt=0.8)
        self.go(FadeIn(rev, shift=UP * 0.15), rt=0.6)
        self.at(0.79)                                   # "Across 10,049 rows, 94.2 percent resolved by majority"
        self.go(FadeOut(v2), FadeOut(rev), rt=0.4)
        self.go(FadeIn(rows, shift=UP * 0.15), rt=0.5)
        self.go(FadeIn(split, shift=UP * 0.15), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_BeforeAfter — the oversell catch, both sentences verbatim.
# ─────────────────────────────────────────────────────────────────────────────
BEFORE = ["The ensemble verified 8,053 keywords with",
          "94.2% agreement across three independent",
          "models, demonstrating high reliability of",
          "the verification process."]
AFTER = ["The ensemble achieved 94.2% inter-model",
         "agreement, with 8,053 keywords reaching",
         "consensus for inclusion in the",
         "production set."]


class B06_BeforeAfter(Scene):
    BID = "B06"
    FALLBACK = 24.0

    def sentence(self, lines, size=40):
        ts = VGroup(*[serif(l, size, sliceable=True) for l in lines]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        return ts

    def construct(self):
        b_card = card(11.9, 2.75, stroke=CRIMSON).move_to(LEFT * 0.15 + UP * 1.35)
        b_lab = sans("BEFORE · first draft", 32, INK).move_to(UP * 3.08).align_to(b_card, LEFT).shift(RIGHT * 0.1)
        b_txt = self.sentence(BEFORE).move_to(b_card)
        s_ver = strike(span(b_txt[0], BEFORE[0], "verified"))
        s_dem = strike(span(b_txt[2], BEFORE[2], "demonstrating high reliability of"))
        s_rel = strike(span(b_txt[3], BEFORE[3], "the verification process"))

        a_card = card(11.9, 2.75, stroke=TEAL).move_to(LEFT * 0.15 + DOWN * 2.0)
        a_lab = sans("AFTER · the rewrite", 32, INK).move_to(DOWN * 0.42).align_to(a_card, LEFT).shift(RIGHT * 0.1)
        a_txt = self.sentence(AFTER).move_to(a_card)
        h1 = VGroup(highlight(span(a_txt[0], AFTER[0], "inter-model"), opacity=0),
                    highlight(span(a_txt[1], AFTER[1], "agreement"), opacity=0))
        h2 = VGroup(highlight(span(a_txt[1], AFTER[1], "reaching"), opacity=0),
                    highlight(span(a_txt[2], AFTER[2], "consensus for inclusion"), opacity=0))

        self.go(FadeIn(b_card), FadeIn(b_lab), FadeIn(b_txt), rt=0.8)
        self.at(0.11)                                   # "'Verified' implies…"
        self.go(Create(s_ver), rt=0.5)
        self.at(0.26)                                   # "'Demonstrating high reliability' implies…"
        self.go(Create(s_dem), rt=0.4)
        self.go(Create(s_rel), rt=0.6)
        self.at(0.51)                                   # "It shows that three models agreed"
        self.go(FadeIn(a_card), FadeIn(a_lab), rt=0.5)
        self.add(h1, h2)   # transparent highlights, layered above the card, under the text
        self.at(0.63)                                   # "So the rewrite says exactly that"
        for line in a_txt:
            self.go(AddTextLetterByLetter(line), rt=0.55)
        self.at(0.77)                                   # "inter-model agreement"
        self.go(*[h.animate.set_fill(GOLD, opacity=0.55) for h in h1], rt=0.5)
        self.at(0.90)                                   # "reaching consensus for inclusion"
        self.go(*[h.animate.set_fill(GOLD, opacity=0.55) for h in h2], rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Limitations — what the overselling sentence was hiding.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Limitations(Scene):
    BID = "B07"
    FALLBACK = 22.0
    XS = [-4.2, 0.0, 4.2]

    def panel(self, x, title):
        box = card(3.9, 5.5).move_to(RIGHT * x + DOWN * 0.2)
        t = sans(title, 25).move_to(RIGHT * x + UP * 2.15)
        return box, t

    def construct(self):
        head = serif("What that sentence was hiding", 40).move_to(UP * 3.1)

        # 1 — no gold standard
        b1, t1 = self.panel(self.XS[0], "No gold standard")
        votes = VGroup(*[Circle(0.22, fill_color=TEAL, fill_opacity=1, stroke_opacity=0)
                         for _ in range(3)]).arrange(RIGHT, buff=0.18)
        votes.move_to(RIGHT * (self.XS[0] - 0.95) + UP * 0.8)
        vs = serif("vs", 30, MUTED).move_to(RIGHT * (self.XS[0] + 0.2) + UP * 0.8)
        key = DashedVMobject(RoundedRectangle(width=1.0, height=1.0, corner_radius=0.12,
                                              stroke_color=SLATE, stroke_width=3), num_dashes=18)
        key.move_to(RIGHT * (self.XS[0] + 1.0) + UP * 0.8)
        keyq = serif("?", 48, SLATE).move_to(key)
        vote_l = serif("the vote", 30, MUTED).move_to(RIGHT * (self.XS[0] - 0.95) + DOWN * 0.05)
        key_l = serif("answer key", 30, MUTED).move_to(RIGHT * (self.XS[0] + 1.0) + DOWN * 0.05)
        c1 = VGroup(serif("agreement, not", 30), serif("expert-checked", 30),
                    serif("accuracy", 30)).arrange(DOWN, buff=0.12).move_to(RIGHT * self.XS[0] + DOWN * 1.6)

        # 2 — shared blind spots
        b2, t2 = self.panel(self.XS[1], "Shared blind spots")
        r = 0.78
        cx, cy = self.XS[1], 0.65
        circles = VGroup(
            Circle(r, stroke_color=TEAL, stroke_width=4).move_to(RIGHT * (cx - 0.42) + UP * (cy + 0.25)),
            Circle(r, stroke_color=SLATE, stroke_width=4).move_to(RIGHT * (cx + 0.42) + UP * (cy + 0.25)),
            Circle(r, stroke_color=INK, stroke_width=4).move_to(RIGHT * cx + UP * (cy - 0.45)),
        )
        blind = Circle(0.26, fill_color=CRIMSON, fill_opacity=0.85, stroke_opacity=0)
        blind.move_to(RIGHT * cx + UP * (cy + 0.02))
        c2 = VGroup(serif("an error all three", 30), serif("miss goes undetected", 30)).arrange(DOWN, buff=0.12).move_to(RIGHT * self.XS[1] + DOWN * 1.6)

        # 3 — self-preference
        b3, t3 = self.panel(self.XS[2], "Self-preference risk")
        oa = logo("openai", 0.75).move_to(RIGHT * self.XS[2] + UP * 1.3)
        gen = chip("writes", 28).move_to(RIGHT * (self.XS[2] - 0.9) + UP * 0.05)
        jud = chip("judges", 28, stroke=CRIMSON).move_to(RIGHT * (self.XS[2] + 0.9) + UP * 0.05)
        a_gen = Arrow(oa.get_bottom(), gen.get_top(), buff=0.1, color=SLATE, stroke_width=3)
        a_jud = Arrow(oa.get_bottom(), jud.get_top(), buff=0.1, color=CRIMSON, stroke_width=3)
        c3 = VGroup(serif("GPT-4o-mini helped", 28), serif("generate some", 28),
                    serif("definitions, and", 28), serif("also judges them", 28)
                    ).arrange(DOWN, buff=0.1).move_to(RIGHT * self.XS[2] + DOWN * 1.65)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.at(0.22)                                   # "There is no gold standard"
        self.go(FadeIn(b1), FadeIn(t1), rt=0.5)
        self.go(FadeIn(votes), FadeIn(vote_l), FadeIn(vs), Create(key), FadeIn(keyq), FadeIn(key_l), rt=0.9)
        self.at(0.31)                                   # "I measured agreement, not expert-checked accuracy"
        self.go(FadeIn(c1, shift=UP * 0.15), rt=0.6)
        self.at(0.47)                                   # "If all three judges share a blind spot"
        self.go(FadeIn(b2), FadeIn(t2), rt=0.5)
        self.go(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.3), rt=1.0)
        self.at(0.60)                                   # "the vote cannot see it"
        self.go(GrowFromCenter(blind), FadeIn(c2, shift=UP * 0.15), rt=0.7)
        self.at(0.70)                                   # "And G P T four o mini"
        self.go(FadeIn(b3), FadeIn(t3), FadeIn(oa), rt=0.6)
        self.at(0.76)                                   # "helped generate some definitions"
        self.go(GrowArrow(a_gen), FadeIn(gen), rt=0.6)
        self.at(0.85)                                   # "and also judged them"
        self.go(GrowArrow(a_jud), FadeIn(jud), rt=0.6)
        self.go(FadeIn(c3, shift=UP * 0.15), rt=0.6)
        self.finish()




# ─────────────────────────────────────────────────────────────────────────────
#  B08_SelfReview — I caught this sentence in my own review; who did what in the paper.
# ─────────────────────────────────────────────────────────────────────────────
class B08_SelfReview(Scene):
    BID = "B08"
    FALLBACK = 15.0

    def construct(self):
        strips = VGroup(*[RoundedRectangle(width=w, height=0.5, corner_radius=0.25,
                                           fill_color=MUTED, fill_opacity=0.35, stroke_opacity=0)
                          for w in [2.2, 1.6, 2.6, 1.4, 2.0]])
        strips.arrange(RIGHT, buff=0.3).move_to(UP * 2.55)
        caught = 2               # this sentence
        lens = VGroup(Circle(0.6, stroke_color=TEAL, stroke_width=6),
                      Line(ORIGIN, DR * 0.5, color=TEAL, stroke_width=8))
        lens[1].move_to(lens[0].get_corner(DR) + DR * 0.14)
        lens.move_to(strips[0].get_center())
        me1 = serif("I caught this sentence in my own review.", 44).move_to(UP * 1.25)
        me2 = serif("Self-review catches some framing, not all.", 44, TEAL).move_to(UP * 0.3)

        band_t = sans("Who did what in the paper", 28, SLATE).move_to(LEFT * 2.9 + DOWN * 0.9)
        cl = VGroup(logo("claude", 0.55), serif("Claude: helped draft and refine the prose", 36))
        cl.arrange(RIGHT, buff=0.3).move_to(DOWN * 1.75).align_to(band_t, LEFT)
        me = VGroup(serif("Janvi: the content, the design reasoning,", 36),
                    serif("the Supabase queries, and what the paper claims", 36))
        me.arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(DOWN * 2.8).align_to(band_t, LEFT)

        self.go(FadeIn(strips), FadeIn(lens), rt=0.5)
        for i in range(1, caught + 1):
            self.go(lens.animate.move_to(strips[i].get_center()), rt=0.4)
        self.go(strips[caught].animate.set_fill(GOLD, opacity=0.9), FadeIn(me1, shift=UP * 0.15), rt=0.6)
        self.at(0.17)                                   # "Self-review catches some framing, not all"
        for i in range(caught + 1, 5):
            self.go(lens.animate.move_to(strips[i].get_center()), rt=0.4)
        self.go(FadeOut(lens), FadeIn(me2, shift=UP * 0.15), rt=0.6)
        self.at(0.39)                                   # "Claude helped me draft and refine the prose"
        self.go(FadeIn(band_t), FadeIn(cl, shift=UP * 0.15), rt=0.7)
        self.at(0.57)                                   # "I supplied the content and design reasoning…"
        self.go(FadeIn(me, shift=UP * 0.15), rt=0.7)
        self.finish()
