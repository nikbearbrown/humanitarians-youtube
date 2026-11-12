"""scenes.py — Manim scenes for "Choosing a Journal That Will Say Yes" (choosing-a-journal).

Same project as the Week 1 and Week 2 reels (hai-videos/Week1/*, hai-videos/Week2/*), so the same
visuals: helpers, the clocked Beat base (`Scene = Beat`), outline cards and chips, strike/highlight
treatment, `cue()` on spoken words (mp3/words.json) and the type sizes that passed GATE T.

Credit rule: the journal research and the reformatting are Janvi's; the journal decision was the
professor's. Only Professor Brown is named; the other professor is "my professor".
No impact factors are shown (Janvi's beat brief).

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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_FreeToPublish — Professor Brown's rule; agreements checked with CRITIQ, confirmed in SciFree.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FreeToPublish(Scene):
    BID = "B01"
    FALLBACK = 17.6

    def tool(self, name, what, x):
        box = card(4.4, 1.7).move_to(RIGHT * x + DOWN * 2.0)
        n = sans(name, 38)
        w = serif(what, 34, MUTED)
        VGroup(n, w).arrange(DOWN, buff=0.15).move_to(box)
        return VGroup(box, n, w)

    def construct(self):
        who = serif("The first rule, from Professor Brown", 38, MUTED).move_to(UP * 3.0)
        rule_box = card(9.6, 1.9, stroke=TEAL, sw=4).move_to(UP * 1.55)
        r1 = sans("Free to publish", 46, TEAL)
        r2 = serif("no article processing charge out of our pocket", 36)
        VGroup(r1, r2).arrange(DOWN, buff=0.18).move_to(rule_box)
        q = serif("Which journals do Northeastern's open access agreements cover?", 36).move_to(DOWN * 0.25)
        critiq = self.tool("CRITIQ", "research", -3.1)
        scifree = self.tool("SciFree", "confirm coverage", 3.1)
        a = arrow(LEFT * 0.75 + DOWN * 2.0, RIGHT * 0.75 + DOWN * 2.0)

        self.go(FadeIn(who, shift=DOWN * 0.15), rt=0.6)
        self.cue("publication", fallback=0.15)
        self.go(Create(rule_box), FadeIn(r1, shift=UP * 0.1), rt=0.7)
        self.cue("article", fallback=0.27)
        self.go(FadeIn(r2), rt=0.5)
        self.cue("checked", fallback=0.47)
        self.go(FadeIn(q, shift=UP * 0.1), rt=0.6)
        self.cue("CRITIQ", fallback=0.74)
        self.go(Create(critiq[0]), FadeIn(critiq[1:]), rt=0.6)
        self.cue("SciFree", fallback=0.89)
        self.go(GrowArrow(a), Create(scifree[0]), FadeIn(scifree[1:]), rt=0.6)
        self.go(scifree[0].animate.set_stroke(TEAL, width=5), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_FiveOptions — five options by fit and fee coverage (no impact factors).
# ─────────────────────────────────────────────────────────────────────────────
class B02_FiveOptions(Scene):
    BID = "B02"
    FALLBACK = 15.2
    X0, X1, X2 = -6.0, -0.6, 3.0
    ROWS = [
        (["JAMIA"], "health", "yes", "JAMIA"),
        (["Journal of Biomedical", "Informatics"], "biomedical", "yes · limited pool", "Journal"),
        (["Education and", "Information Technologies"], "education", "—", "Education"),
        (["ACM conferences"], "shorter format", "yes", "ACM"),
        (["an AI-in-education journal"], "AI in education", "—", "AI-in-education"),
    ]

    def construct(self):
        head = serif("Five options", 44).move_to(UP * 3.1)
        hy = 2.4
        hdr = VGroup(sans("option", 34, MUTED).move_to(RIGHT * self.X0 + UP * hy, aligned_edge=LEFT),
                     sans("fit", 34, MUTED).move_to(RIGHT * self.X1 + UP * hy, aligned_edge=LEFT),
                     sans("fee covered", 34, MUTED).move_to(RIGHT * self.X2 + UP * hy, aligned_edge=LEFT))
        rule = Line(LEFT * 6.0 + UP * 2.0, RIGHT * 6.0 + UP * 2.0, color=SLATE, stroke_width=2)
        ys = [1.5, 0.55, -0.55, -1.55, -2.35]
        names, fits, fees = [], [], []
        for (nm, fit, fee, _), y in zip(self.ROWS, ys):
            n = VGroup(*[serif(s, 34) for s in nm]).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
            n.move_to(RIGHT * self.X0 + UP * y, aligned_edge=LEFT)
            names.append(n)
            fits.append(serif(fit, 34).move_to(RIGHT * self.X1 + UP * y, aligned_edge=LEFT))
            fees.append(serif(fee, 34, TEAL if fee.startswith("yes") else MUTED)
                        .move_to(RIGHT * self.X2 + UP * y, aligned_edge=LEFT))
        seps = [Line(LEFT * 6.0 + UP * (y - 0.47), RIGHT * 6.0 + UP * (y - 0.47), color=MUTED, stroke_width=1.5)
                for y in ys[:-1]] + [Line(LEFT * 6.0 + DOWN * 2.75, RIGHT * 6.0 + DOWN * 2.75, color=MUTED, stroke_width=1.5)]
        note = serif("— : not recorded in my notes", 32, MUTED).move_to(RIGHT * 1.6 + DOWN * 3.1)

        self.go(FadeIn(head), FadeIn(hdr), Create(rule), rt=0.6)
        for i, row in enumerate(self.ROWS):
            self.cue(row[3], fallback=0.15 + 0.15 * i)
            self.go(FadeIn(names[i], shift=RIGHT * 0.15), Create(seps[i]), rt=0.4)
        self.cue("fit", fallback=0.83)
        self.go(hdr[1].animate.set_color(TEAL), LaggedStart(*[FadeIn(f) for f in fits], lag_ratio=0.1), rt=0.6)
        self.cue("fee", fallback=0.9)
        self.go(hdr[2].animate.set_color(TEAL), LaggedStart(*[FadeIn(f) for f in fees], lag_ratio=0.1),
                FadeIn(note), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ThreeRounds — CS methodology → bioinformatics → the dedicated journals weren't free.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ThreeRounds(Scene):
    BID = "B03"
    FALLBACK = 14.9
    XS = [-4.25, 0.0, 4.25]

    def round_card(self, i, lines, sub, stroke):
        box = card(3.8, 3.3, stroke=stroke, sw=3).move_to(RIGHT * self.XS[i] + DOWN * 0.1)
        n = sans(f"round {i + 1}", 34, MUTED)
        body = VGroup(*[serif(s, 38) for s in lines]).arrange(DOWN, buff=0.08)
        parts = [n, body]
        if sub:
            parts.append(VGroup(*[serif(s, 32, MUTED) for s in sub]).arrange(DOWN, buff=0.06))
        VGroup(*parts).arrange(DOWN, buff=0.25).move_to(box)
        return VGroup(box, *parts)

    def construct(self):
        head = serif("The framing changed three times", 46).move_to(UP * 2.95)
        r1 = self.round_card(0, ["computer science", "methodology"], None, SLATE)
        r2 = self.round_card(1, ["bioinformatics"], ["the CS angle wasn't", "novel enough"], SLATE)
        r3 = self.round_card(2, ["dedicated", "bioinformatics", "journals"], None, CRIMSON)
        verdict = sans("not free under our agreements", 40).move_to(DOWN * 2.6 + RIGHT * 1.6)
        a1 = arrow(LEFT * 2.3 + DOWN * 0.1, LEFT * 1.95 + DOWN * 0.1)
        a2 = arrow(RIGHT * 1.95 + DOWN * 0.1, RIGHT * 2.3 + DOWN * 0.1)

        self.go(FadeIn(head, shift=DOWN * 0.15), rt=0.6)
        self.cue("First", fallback=0.18)
        self.go(Create(r1[0]), FadeIn(r1[1:]), rt=0.7)
        self.cue("bioinformatics", fallback=0.4)
        self.go(GrowArrow(a1), Create(r2[0]), FadeIn(r2[1:3]), rt=0.7)
        self.cue("because", fallback=0.48)
        self.go(FadeIn(r2[3]), r1[0].animate.set_stroke(MUTED), rt=0.5)
        self.cue("dedicated", fallback=0.7)
        self.go(GrowArrow(a2), Create(r3[0]), FadeIn(r3[1:]), rt=0.7)
        self.cue("free", fallback=0.86)
        self.go(FadeIn(verdict, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_TheDecision — on a standup call, my professor chose JBI: "We just want to get it published."
# ─────────────────────────────────────────────────────────────────────────────
class B04_TheDecision(Scene):
    BID = "B04"
    FALLBACK = 14.4

    def construct(self):
        top = serif("On a standup call, my professor chose", 38, MUTED).move_to(UP * 3.0)
        jbi_box = card(10.0, 1.4, stroke=SLATE, sw=3).move_to(UP * 1.75)
        jbi = serif("Journal of Biomedical Informatics", 48).move_to(jbi_box).shift(LEFT * 0.3)
        ok = tick(s=0.45).next_to(jbi, RIGHT, buff=0.4)
        q_box = card(10.0, 2.3, stroke=SLATE, sw=2.5).move_to(DOWN * 0.6)
        q1 = serif("“We just want to get it published.”", 46)
        q2 = serif("“find something that will give you an answer quickly”", 34, MUTED)
        VGroup(q1, q2).arrange(DOWN, buff=0.25).move_to(q_box)
        foot = sans("a practical choice over an aspirational one", 40, TEAL).move_to(DOWN * 2.75)

        self.go(FadeIn(top, shift=DOWN * 0.15), rt=0.6)
        self.cue("Journal", fallback=0.17)
        self.go(Create(jbi_box), FadeIn(jbi), rt=0.7)
        self.go(jbi_box.animate.set_stroke(TEAL, width=6), Create(ok), rt=0.5)
        self.cue("we", fallback=0.47)
        self.go(Create(q_box), FadeIn(q1, shift=UP * 0.1), rt=0.6)
        self.cue("somewhere", fallback=0.6)
        self.go(FadeIn(q2), rt=0.5)
        self.cue("practical", fallback=0.82)
        self.go(FadeIn(foot, shift=UP * 0.1), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Reformat — JBI section order; structured abstract, five parts, 345 → 285 under 300.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Reformat(Scene):
    BID = "B05"
    FALLBACK = 14.6
    SECTIONS = ["Introduction", "Background", "Materials and Methods", "Results",
                "Discussion", "Limitations", "Conclusion"]
    PARTS = ["Objective", "Materials and Methods", "Results", "Discussion", "Conclusion"]
    BX, SCALE = -1.0, 7.0 / 360

    def construct(self):
        l_head = sans("JBI section order", 36, TEAL).move_to(LEFT * 6.0 + UP * 2.95, aligned_edge=LEFT)
        secs = VGroup(*[serif(f"{i + 1}  {s}", 34) for i, s in enumerate(self.SECTIONS)])
        secs.arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to(LEFT * 6.0 + UP * 0.45, aligned_edge=LEFT)
        more = serif("+ statements, references", 32, MUTED).next_to(secs, DOWN, aligned_edge=LEFT, buff=0.22)
        r_head = sans("structured abstract · 5 parts", 36, TEAL).move_to(RIGHT * self.BX + UP * 2.95, aligned_edge=LEFT)
        chips = [chip(p, 32) for p in self.PARTS]
        row1 = VGroup(*chips[:2]).arrange(RIGHT, buff=0.25)
        row2 = VGroup(*chips[2:]).arrange(RIGHT, buff=0.25)
        grid = VGroup(row1, row2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        grid.move_to(RIGHT * self.BX + UP * 1.45, aligned_edge=LEFT)

        by = -1.25
        lim_x = self.BX + 300 * self.SCALE
        tr = ValueTracker(0)

        def bar():
            w = (345 + tr.get_value() * (285 - 345)) * self.SCALE
            col = CRIMSON if w > 300 * self.SCALE else TEAL
            return Rectangle(width=w, height=0.6, fill_color=col, fill_opacity=1, stroke_opacity=0) \
                .move_to(RIGHT * self.BX + UP * by, aligned_edge=LEFT)
        b = always_redraw(bar)
        cnt = counter(285, lambda v: f"{int(round(v))} words", 44, INK, RIGHT * 1.6 + DOWN * 0.2, tr, start=345)
        lim = DashedLine(RIGHT * lim_x + UP * (by + 0.6), RIGHT * lim_x + UP * (by - 0.6),
                         color=INK, stroke_width=4, dash_length=0.12)
        lim_t = sans("300-word limit", 34).move_to(RIGHT * (lim_x - 0.9) + UP * (by - 1.0))

        self.go(FadeIn(l_head), rt=0.5)
        self.cue("section", fallback=0.25)
        self.go(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.1) for s in secs], lag_ratio=0.12), FadeIn(more), rt=1.0)
        self.cue("structured", fallback=0.36)
        self.go(FadeIn(r_head), rt=0.4)
        self.cue("five", fallback=0.45)
        self.go(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.15), rt=0.8)
        self.cue("cut", fallback=0.56)
        self.add(b, cnt)
        self.go(Create(lim), FadeIn(lim_t), rt=0.5)
        self.cue("285", fallback=0.75)
        self.go(tr.animate.set_value(1), rt=1.2)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Details — highlights, MeSH keywords, Vancouver [1]–[22] with no gaps; 23 hours.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Details(Scene):
    BID = "B06"
    FALLBACK = 15.5

    def construct(self):
        items = [
            VGroup(serif("5 highlights, each under 85 characters", 40)),
            VGroup(serif("MeSH keywords", 40),
                   serif("Neoplasms · Vocabulary, Controlled · Natural Language Processing", 32, MUTED))
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(serif("numbered Vancouver citations", 40),
                   sans("[1]  [2]  [3]  …  [21]  [22]", 34, SLATE)).arrange(DOWN, aligned_edge=LEFT, buff=0.12),
            VGroup(serif("numbering checked: no gaps", 40)),
            VGroup(serif("body: about 3,900 words", 40)),
        ]
        col = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.36)
        col.move_to(LEFT * 5.3 + UP * 0.45, aligned_edge=LEFT)
        ticks = [tick().next_to(it[0], LEFT, buff=0.25) for it in items]
        hours = sans("23 hours", 48, TEAL).move_to(RIGHT * 3.6 + DOWN * 2.85)

        cues = [("highlights", 0.08), ("MeSH", 0.27), ("Vancouver", 0.48), ("gaps", 0.78)]
        for i, (w, fb) in enumerate(cues):
            self.cue(w, fallback=fb)
            self.go(Create(ticks[i]), FadeIn(items[i], shift=LEFT * 0.15), rt=0.6)
        self.go(Create(ticks[4]), FadeIn(items[4], shift=LEFT * 0.15), rt=0.5)
        self.cue("23", fallback=0.9)
        self.go(FadeIn(hours, shift=UP * 0.1), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B07_Lesson — journal choice isn't only topical fit: fees, agreements, realistic odds.
# ─────────────────────────────────────────────────────────────────────────────
class B07_Lesson(Scene):
    BID = "B07"
    FALLBACK = 6.6

    def construct(self):
        head = serif("What I learned", 40, MUTED).move_to(UP * 2.6)
        line = serif("Journal choice isn't only topical fit.", 50).move_to(UP * 1.2)
        fit = chip("topical fit", 38, stroke=MUTED)
        plus = sans("+", 44)
        more = [chip(s, 38, stroke=TEAL) for s in ("fees", "agreements", "realistic odds")]
        row = VGroup(fit, plus, *more).arrange(RIGHT, buff=0.35).move_to(DOWN * 0.8)

        self.go(FadeIn(head), rt=0.4)
        self.cue("journal", fallback=0.2)
        self.go(FadeIn(line, shift=UP * 0.1), FadeIn(fit), rt=0.6)
        self.cue("fees", fallback=0.6)
        self.go(FadeIn(plus), FadeIn(more[0]), rt=0.3)
        self.cue("agreements", fallback=0.7)
        self.go(FadeIn(more[1]), rt=0.3)
        self.cue("realistic", fallback=0.82)
        self.go(FadeIn(more[2]), rt=0.3)
        self.finish()
