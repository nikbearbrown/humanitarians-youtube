"""scenes.py — Manim scenes for "Agreement Is Not Accuracy" (agreement-not-accuracy).

Same project as Video 1 (hai-videos/2026-08-07-qa-paper-oversell), so the same visuals:
the helpers, the clocked Beat base, B02_ThreeJudges (Video 1 B04_ThreeJudges) and
B05_Limitations (Video 1 B07_Limitations) are reused; B06_SayAvoid reuses Video 1's
B06_BeforeAfter strike/highlight treatment. New: B01_AllApproved, B03_Calibration, B04_Triage.

Channel @HumanitariansAI · humanitarians palette (brands/hai.md): cream ground,
warm ink text, petrol teal = kept/good, burnt orange = struck/bad (never text),
navy slate = structure, amber gold = highlighter fill only (never text).
Type: EB Garamond (serif body) + Montserrat (sans headers).

Every number on screen comes from SOURCE-LOCKED-FACTS.md / the primary inbox file. Every scene
runs to its beat's measured narration length (mp3/timings.json), so compile never retimes it.
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
#  B01_AllApproved — the trap: three judges agree, which is not the same as right.
# ─────────────────────────────────────────────────────────────────────────────
class B01_AllApproved(Scene):
    BID = "B01"
    FALLBACK = 13.0
    JUDGES = [("mistral", "Mistral Small"), ("openai", "GPT-4o-mini"), ("claude", "Claude 3.5 Sonnet")]
    XS = [-4.3, 0.0, 4.3]

    def construct(self):
        defn_t = serif("the same definition, read by three AI judges", 34).move_to(UP * 3.05)
        defn = VGroup(defn_t, Line(defn_t.get_corner(DL) + DOWN * 0.12, defn_t.get_corner(DR) + DOWN * 0.12,
                                   color=SLATE, stroke_width=3))
        cols = [VGroup(logo(lg, 0.5).move_to(RIGHT * x + UP * 1.45),   # 0.5 as in B03 (GATE T §8.3)
                       sans(name, 28).move_to(RIGHT * x + UP * 0.7))
                for (lg, name), x in zip(self.JUDGES, self.XS)]
        chips = VGroup(*[chip("approved", 36, stroke=TEAL).move_to(RIGHT * x + DOWN * 0.4) for x in self.XS])
        proof = serif("feels like proof…", 44, MUTED).move_to(DOWN * 1.9)
        brace = Brace(chips, DOWN, color=SLATE, buff=0.25)
        agreed = sans("all you learned: they agreed", 36, TEAL).next_to(brace, DOWN, buff=0.2)
        cap = serif("agreed ≠ right", 56).move_to(DOWN * 2.8)

        self.go(FadeIn(defn, shift=DOWN * 0.2), rt=0.6)
        self.at(0.11)                                   # "Three AI models read the same definition"
        self.go(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cols], lag_ratio=0.3), rt=1.2)
        self.at(0.33)                                   # "all three say it's fine"
        self.go(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in chips], lag_ratio=0.3), rt=1.0)
        self.at(0.50)                                   # "That feels like proof"
        self.go(FadeIn(proof), rt=0.5)
        self.at(0.63)                                   # "all you've learned is that they agreed"
        self.go(FadeOut(proof), GrowFromCenter(brace), FadeIn(agreed, shift=UP * 0.1), rt=0.8)
        self.at(0.83)                                   # "Whether they're right is a separate question"
        self.go(FadeIn(cap, shift=UP * 0.15), rt=0.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_ThreeJudges — Video 1 B04_ThreeJudges, re-cued; ends on the all-differ case (no count).
# ─────────────────────────────────────────────────────────────────────────────
class B02_ThreeJudges(Scene):
    BID = "B02"
    FALLBACK = 18.0
    JUDGES = [("mistral", "Mistral Small", "Mistral AI"),
              ("openai", "GPT-4o-mini", "OpenAI"),
              ("claude", "Claude 3.5 Sonnet", "Anthropic")]
    XS = [-4.3, 0.0, 4.3]
    TAGS = ["approved", "supplementary", "too_basic", "fix_definition", "junk"]

    def construct(self):
        defn_t = serif("a keyword popup · Medhavy cancer biology textbook", 32).move_to(UP * 3.05)
        defn = VGroup(defn_t, Line(defn_t.get_corner(DL) + DOWN * 0.12, defn_t.get_corner(DR) + DOWN * 0.12,
                                   color=SLATE, stroke_width=3))
        prov_t = serif("three different providers", 32, MUTED).move_to(UP * 2.35)
        cols = []
        for (lg, name, prov), x in zip(self.JUDGES, self.XS):
            mark = logo(lg, 0.95).move_to(RIGHT * x + UP * 1.4)
            n = sans(name, 28).move_to(RIGHT * x + UP * 0.6)
            p = serif(prov, 26, MUTED).move_to(RIGHT * x + UP * 0.15)
            cols.append(VGroup(mark, n, p))
        tag_row = VGroup(*[chip(t, 28) for t in self.TAGS]).arrange(RIGHT, buff=0.22)
        tag_row.move_to(DOWN * 3.0)
        tag_head = serif("five tags, one action each", 28, MUTED).next_to(tag_row, UP, buff=0.22)

        votes1 = ["approved", "approved", "supplementary"]
        v1 = VGroup(*[chip(v, 30).move_to(RIGHT * x + DOWN * 0.65) for v, x in zip(votes1, self.XS)])
        win = sans("2 of 3 agree  →  approved", 34, TEAL).move_to(DOWN * 1.6)
        votes2 = ["approved", "too_basic", "junk"]
        v2 = VGroup(*[chip(v, 30).move_to(RIGHT * x + DOWN * 0.65) for v, x in zip(votes2, self.XS)])
        rev = chip("all 3 differ  →  flagged for human REVIEW", 34, stroke=SLATE)
        rev.move_to(DOWN * 1.6)

        self.go(FadeIn(defn, shift=DOWN * 0.2), rt=0.6)
        self.at(0.09)                                   # "different providers"
        self.go(FadeIn(prov_t), rt=0.5)
        for c, cue in zip(cols, [0.32, 0.37, 0.49]):    # on each model's name
            self.at(cue)
            self.go(FadeIn(c, shift=UP * 0.15), rt=0.6)
        self.at(0.60)                                   # "Each picks one of five tags"
        self.go(FadeIn(tag_head), LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in tag_row],
                                                lag_ratio=0.15), rt=1.2)
        self.at(0.72)                                   # "Two of three agree"
        self.go(LaggedStart(*[FadeIn(v, shift=DOWN * 0.3) for v in v1], lag_ratio=0.25), rt=0.9)
        self.go(v1[0][0].animate.set_stroke(TEAL, width=5),
                v1[1][0].animate.set_stroke(TEAL, width=5), FadeIn(win), rt=0.7)
        self.at(0.85)                                   # "All three differ"
        self.go(FadeOut(v1), FadeOut(win), rt=0.4)
        self.go(LaggedStart(*[FadeIn(v, shift=DOWN * 0.3) for v in v2], lag_ratio=0.25), rt=0.8)
        self.go(FadeIn(rev, shift=UP * 0.15), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Calibration — average scores ~65 / ~76 / ~56; a 70 cutoff punishes the strictest judge.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Calibration(Scene):
    BID = "B03"
    FALLBACK = 16.0
    JUDGES = [("mistral", "Mistral Small", 65), ("openai", "GPT-4o-mini", 76), ("claude", "Claude 3.5 Sonnet", 56)]
    XS = [-3.8, 0.0, 3.8]
    BASE = -1.9
    K = 0.05          # scene units per score point

    def construct(self):
        title = sans("average score per judge", 34).move_to(UP * 3.15)
        title2 = sans("a tag means the same from every judge", 34, TEAL).move_to(UP * 3.15)
        base = Line(LEFT * 5.9 + UP * self.BASE, RIGHT * 5.9 + UP * self.BASE, color=SLATE, stroke_width=3)
        names, bars, vals, tags = [], [], [], []
        for (lg, name, v), x in zip(self.JUDGES, self.XS):
            names.append(VGroup(logo(lg, 0.5), sans(name, 28)).arrange(DOWN, buff=0.15)
                         .next_to(RIGHT * x + UP * self.BASE, DOWN, buff=0.2))
            bar = Rectangle(width=1.7, height=v * self.K, fill_color=SLATE, fill_opacity=1, stroke_opacity=0)
            bar.move_to(RIGHT * x + UP * (self.BASE + v * self.K / 2))
            bars.append(bar)
            vals.append(sans(f"~{v}", 40).next_to(bar, UP, buff=0.18))
            tags.append(chip("approved", 32, stroke=TEAL).next_to(bar, UP, buff=0.18))
        y70 = self.BASE + 70 * self.K
        cut = DashedLine(LEFT * 5.9 + UP * y70, RIGHT * 5.9 + UP * y70, color=CRIMSON, stroke_width=5,
                         dash_length=0.2)
        cut._qc_intentional = True
        cut_l = serif("cutoff 70", 32).next_to(cut, UP, buff=0.12).align_to(cut, RIGHT)
        below = serif("below 70", 32, WHITE).move_to(bars[2]).shift(DOWN * 0.6)

        self.go(FadeIn(title, shift=DOWN * 0.15), rt=0.6)
        self.at(0.20)                                   # "My judges scored on different scales"
        self.go(Create(base), *[FadeIn(n) for n in names], rt=0.8)
        for i, cue in enumerate([0.40, 0.47, 0.53]):    # "65", "76", "56"
            self.at(cue)
            self.go(GrowFromEdge(bars[i], DOWN), FadeIn(vals[i], shift=UP * 0.1), rt=0.6)
        self.at(0.62)                                   # "A cutoff of 70"
        self.go(Create(cut), FadeIn(cut_l), rt=0.7)
        self.at(0.72)                                   # "would punish the strictest judge"
        self.go(bars[2].animate.set_fill(CRIMSON), FadeIn(below), rt=0.5)
        self.at(0.83)                                   # "A tag means the same thing from every judge"
        self.go(FadeOut(cut), FadeOut(cut_l), FadeOut(below), *[FadeOut(v) for v in vals],
                bars[2].animate.set_fill(SLATE), rt=0.4)
        self.go(ReplacementTransform(title, title2),
                LaggedStart(*[FadeIn(t, shift=DOWN * 0.15) for t in tags], lag_ratio=0.2), rt=0.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Triage — 10,049 rows: 94.2% resolved by majority, 5.8% flagged for human review.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Triage(Scene):
    BID = "B04"
    FALLBACK = 12.0
    W = 11.0

    def construct(self):
        head = serif("What the vote is good for: triage at scale", 44).move_to(UP * 2.7)
        rows = sans("10,049 audit rows", 36).move_to(UP * 1.4)
        frame = Rectangle(width=self.W, height=1.1, stroke_color=SLATE, stroke_width=3, fill_opacity=0)
        left = frame.get_left()
        maj = Rectangle(width=self.W * 0.942, height=1.1, fill_color=TEAL, fill_opacity=1, stroke_opacity=0)
        maj.move_to(left, aligned_edge=LEFT)
        rev = Rectangle(width=self.W * 0.058, height=1.1, fill_color=GOLD, fill_opacity=1, stroke_opacity=0)
        rev.next_to(maj, RIGHT, buff=0)
        maj_l = sans("94.2%  resolved by majority", 40, WHITE).move_to(maj)
        rev_l = serif("5.8%  flagged for human review", 38).move_to(DOWN * 1.75).align_to(frame, RIGHT)
        rx = -self.W / 2 + self.W * (0.942 + 0.029)     # centre of the 5.8% segment
        ptr = Line(RIGHT * rx + DOWN * 0.55, RIGHT * rx + DOWN * 1.4, color=SLATE, stroke_width=3)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.at(0.21)                                   # "Across 10,049 rows"
        self.go(FadeIn(rows), Create(frame), rt=0.6)
        self.at(0.43)                                   # "94.2 percent were resolved by majority"
        self.go(GrowFromEdge(maj, LEFT), rt=1.0)
        self.go(FadeIn(maj_l), rt=0.5)
        self.at(0.76)                                   # "and 5.8 percent were flagged for human review"
        self.go(GrowFromEdge(rev, LEFT), Create(ptr), FadeIn(rev_l, shift=UP * 0.1), rt=0.8)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Limitations — Video 1 B07_Limitations, re-cued: when not to trust the vote.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Limitations(Scene):
    BID = "B05"
    FALLBACK = 18.0
    XS = [-4.2, 0.0, 4.2]

    def panel(self, x, title):
        box = card(3.9, 5.5).move_to(RIGHT * x + DOWN * 0.2)
        t = sans(title, 25).move_to(RIGHT * x + UP * 2.15)
        return box, t

    def construct(self):
        head = serif("When not to trust the vote", 40).move_to(UP * 3.1)

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
        c1 = VGroup(serif("agreement alone", 30), serif("says nothing", 30),
                    serif("about accuracy", 30)).arrange(DOWN, buff=0.12).move_to(RIGHT * self.XS[0] + DOWN * 1.6)

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
        c2 = VGroup(serif("an error all three", 30), serif("share, the vote", 30),
                    serif("can't see", 30)).arrange(DOWN, buff=0.12).move_to(RIGHT * self.XS[1] + DOWN * 1.6)

        # 3 — self-preference
        b3, t3 = self.panel(self.XS[2], "Self-preference risk")
        oa = logo("openai", 0.75).move_to(RIGHT * self.XS[2] + UP * 1.3)
        gen = chip("writes", 28).move_to(RIGHT * (self.XS[2] - 0.9) + UP * 0.05)
        jud = chip("judges", 28, stroke=CRIMSON).move_to(RIGHT * (self.XS[2] + 0.9) + UP * 0.05)
        a_gen = Arrow(oa.get_bottom(), gen.get_top(), buff=0.1, color=SLATE, stroke_width=3)
        a_jud = Arrow(oa.get_bottom(), jud.get_top(), buff=0.1, color=CRIMSON, stroke_width=3)
        c3 = VGroup(serif("GPT-4o-mini helped", 28), serif("generate some", 28),
                    serif("definitions, and", 28), serif("also judged them", 28)
                    ).arrange(DOWN, buff=0.1).move_to(RIGHT * self.XS[2] + DOWN * 1.65)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.at(0.09)                                   # "There's no gold standard"
        self.go(FadeIn(b1), FadeIn(t1), rt=0.5)
        self.go(FadeIn(votes), FadeIn(vote_l), FadeIn(vs), Create(key), FadeIn(keyq), FadeIn(key_l), rt=0.9)
        self.at(0.19)                                   # "agreement alone says nothing about accuracy"
        self.go(FadeIn(c1, shift=UP * 0.15), rt=0.6)
        self.at(0.36)                                   # "If all three judges share a blind spot"
        self.go(FadeIn(b2), FadeIn(t2), rt=0.5)
        self.go(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.3), rt=1.0)
        self.at(0.51)                                   # "the vote can't see it"
        self.go(GrowFromCenter(blind), FadeIn(c2, shift=UP * 0.15), rt=0.7)
        self.at(0.61)                                   # "And G P T four o mini"
        self.go(FadeIn(b3), FadeIn(t3), FadeIn(oa), rt=0.6)
        self.at(0.70)                                   # "helped generate some definitions"
        self.go(GrowArrow(a_gen), FadeIn(gen), rt=0.6)
        self.at(0.82)                                   # "and also judged them"
        self.go(GrowArrow(a_jud), FadeIn(jud), rt=0.6)
        self.go(FadeIn(c3, shift=UP * 0.15), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_SayAvoid — report what you measured (Video 1 B06 strike/highlight treatment).
# ─────────────────────────────────────────────────────────────────────────────
class B06_SayAvoid(Scene):
    BID = "B06"
    FALLBACK = 10.0
    LX, RX = -3.1, 3.4

    def construct(self):
        head = serif("Report what you measured", 44).move_to(UP * 2.85)
        div = Line(UP * 2.0, DOWN * 1.9, color=SLATE, stroke_width=2)
        say_h = sans("SAY", 36, TEAL).move_to(RIGHT * self.LX + UP * 1.85)
        avoid_h = sans("AVOID", 36).move_to(RIGHT * self.RX + UP * 1.85)
        say = [serif(w, 46).move_to(RIGHT * self.LX + UP * y) for w, y in
               [("inter-model agreement", 0.75), ("consensus", -0.45)]]
        hls = [highlight(w, opacity=0) for w in say]
        avoid = [serif(w, 50).move_to(RIGHT * self.RX + UP * y) for w, y in
                 [("verified", 0.85), ("accurate", -0.1), ("reliable", -1.05)]]
        strikes = [strike(w) for w in avoid]
        foot = serif("unless you checked against expert answers", 40, MUTED).move_to(DOWN * 2.75)

        self.go(FadeIn(head, shift=DOWN * 0.15), Create(div), FadeIn(say_h), rt=0.6)
        self.add(*hls)    # transparent highlights, under the words
        for i, cue in enumerate([0.19, 0.32]):          # "inter-model agreement", "consensus"
            self.at(cue)
            self.go(FadeIn(say[i]), hls[i].animate.set_fill(GOLD, opacity=0.55), rt=0.6)
        self.at(0.43)                                   # "Not verified, accurate or reliable"
        self.go(FadeIn(avoid_h), *[FadeIn(w) for w in avoid], rt=0.5)
        for i, cue in enumerate([0.49, 0.60, 0.67]):
            self.at(cue)
            self.go(Create(strikes[i]), rt=0.3)
        self.at(0.72)                                   # "unless you checked against expert answers"
        self.go(FadeIn(foot, shift=UP * 0.1), rt=0.6)
        self.finish()
