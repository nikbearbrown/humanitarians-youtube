"""scenes.py — Manim scenes for "Blind Testing an AI Judge" (blind-ab-test).

Same helper block as this week's progress reel (hai-videos/Week6/progress-self-preference-test),
Week 1–5 lineage. B03 and B05 adapt that reel's B03_Blind and B05_Tests; B04 uses the Week 4
three-candidate card layout. Every number on screen appears in
inbox/term2-week06/term2-week6-video-content.md as written. The judge is a labelled card,
never a person (rule 9).

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
#  B01_Question — does the judge favor its own writing, or is its writing just better?
# ─────────────────────────────────────────────────────────────────────────────
class B01_Question(Scene):
    BID = "B01"
    FALLBACK = 10.0

    def construct(self):
        q_box = card(11.4, 1.7, stroke=SLATE, sw=3).move_to(UP * 1.7)
        q = serif("Does the judge favor its own writing?", 48).move_to(q_box)
        alone = sans("its scores alone can't tell", 40).move_to(UP * 0.0)
        c_box = DashedVMobject(RoundedRectangle(width=8.4, height=1.4, corner_radius=0.18,
                                                stroke_color=SLATE, stroke_width=3), num_dashes=48)
        c_box.move_to(DOWN * 1.7)
        c = serif("or is its writing just better?", 44).move_to(c_box)

        self.go(Create(q_box), FadeIn(q), rt=0.7)
        self.cue("scores", fallback=0.5)
        self.go(FadeIn(alone), Create(under(alone)), rt=0.5)
        self.cue("because", fallback=0.7)
        self.go(Create(c_box), FadeIn(c), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Paired — same items, two authors: 200 keywords, own model vs other model, same format.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Paired(Scene):
    BID = "B02"
    FALLBACK = 13.0
    XL, XR = -1.4, 3.4
    YS = [1.05, -0.05, -1.15]

    def version(self, x, y):
        box = card(4.2, 0.85, stroke=SLATE, sw=2.5).move_to(RIGHT * x + UP * y)
        ln = VGroup(Line(LEFT * 1.7, RIGHT * 1.7, color=SLATE, stroke_width=3),
                    Line(LEFT * 1.7, RIGHT * 1.0, color=SLATE, stroke_width=3)).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ln.move_to(box)
        return VGroup(box, ln)

    def construct(self):
        head = sans("same items, two authors", 40).move_to(UP * 2.95)
        h_l = VGroup(ink_logo("openai", 0.42), serif("own model", 36)).arrange(RIGHT, buff=0.2).move_to(RIGHT * self.XL + UP * 2.05)
        h_r = VGroup(ink_logo("mistral", 0.42), serif("other model", 36)).arrange(RIGHT, buff=0.2).move_to(RIGHT * self.XR + UP * 2.05)
        rows = []
        for y in self.YS:
            lab = serif("keyword", 36).move_to(LEFT * 5.9 + UP * y, aligned_edge=LEFT)
            rows.append(VGroup(lab, self.version(self.XL, y), self.version(self.XR, y)))
        n = sans("200 keywords", 40, TEAL).move_to(LEFT * 3.4 + DOWN * 2.4)
        fmt = chip("same format", 38).move_to(RIGHT * 2.6 + DOWN * 2.4)

        self.go(FadeIn(head), rt=0.4)
        self.cue("200", fallback=0.35)
        self.go(LaggedStart(*[FadeIn(r[0]) for r in rows], lag_ratio=0.15), FadeIn(n), rt=0.6)
        self.cue("own", fallback=0.55)
        self.go(FadeIn(h_l), LaggedStart(*[Create(r[1]) for r in rows], lag_ratio=0.15), rt=0.6)
        self.cue("different", fallback=0.75)
        self.go(FadeIn(h_r), LaggedStart(*[Create(r[2]) for r in rows], lag_ratio=0.15), rt=0.6)
        self.cue("format", fallback=0.92)
        self.go(FadeIn(fmt), rt=0.3)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Blind — separate passes, same rubric, never told who wrote what.
#  (Progress reel B03_Blind.)
# ─────────────────────────────────────────────────────────────────────────────
class B03_Blind(Scene):
    BID = "B03"
    FALLBACK = 8.0

    def construct(self):
        j_box = card(4.2, 2.6, stroke=SLATE, sw=3).move_to(LEFT * 3.9 + UP * 0.45)
        j = VGroup(sans("the judge", 40), serif("kept blind", 36)).arrange(DOWN, buff=0.2).move_to(j_box)
        p1 = card(4.6, 1.3, stroke=SLATE, sw=3).move_to(RIGHT * 3.0 + UP * 1.3)
        p1t = VGroup(sans("pass 1", 36), serif("one set", 34)).arrange(RIGHT, buff=0.35).move_to(p1)
        p2 = card(4.6, 1.3, stroke=SLATE, sw=3).move_to(RIGHT * 3.0 + DOWN * 0.5)
        p2t = VGroup(sans("pass 2", 36), serif("the other set", 34)).arrange(RIGHT, buff=0.35).move_to(p2)
        a1 = arrow(LEFT * 1.7 + UP * 0.8, RIGHT * 0.6 + UP * 1.3)
        a2 = arrow(LEFT * 1.7 + UP * 0.1, RIGHT * 0.6 + DOWN * 0.5)
        rub = chip("the same rubric", 40, stroke=TEAL).move_to(DOWN * 2.0)
        hid = sans("never told who wrote what", 38).move_to(DOWN * 2.9)

        self.go(Create(j_box), FadeIn(j), rt=0.5)
        self.cue("separate", fallback=0.3)
        self.go(GrowArrow(a1), Create(p1), FadeIn(p1t), GrowArrow(a2), Create(p2), FadeIn(p2t), rt=0.7)
        self.cue("rubric", fallback=0.55)
        self.go(FadeIn(rub), rt=0.4)
        self.cue("never", fallback=0.72)
        self.go(FadeIn(hid), Create(under(hid)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_PickTests — chi-square, Welch's t-test, McNemar: what each one compares.
# ─────────────────────────────────────────────────────────────────────────────
class B04_PickTests(Scene):
    BID = "B04"
    FALLBACK = 16.0
    XS = [-4.15, 0.0, 4.15]
    TESTS = [("chi-square", ["compares", "approval rates"], SLATE),
             ("Welch's|t-test", ["compares", "mean scores"], SLATE),
             ("McNemar", ["uses the pairing:", "only items whose", "verdicts differ"], TEAL)]

    def construct(self):
        head = serif("Pick tests that match your data", 42).move_to(UP * 2.95)
        cards = []
        for (nm, lines_, col), x in zip(self.TESTS, self.XS):
            box = card(3.85, 3.6, stroke=col, sw=4 if col == TEAL else 3).move_to(RIGHT * x + DOWN * 0.2)
            n = VGroup(*[sans(w, 36, col if col == TEAL else INK) for w in nm.split("|")]).arrange(DOWN, buff=0.08)
            t = VGroup(*[serif(s, 34) for s in lines_]).arrange(DOWN, buff=0.08)
            VGroup(n, t).arrange(DOWN, buff=0.35).move_to(box)
            cards.append(VGroup(box, n, t))

        self.go(FadeIn(head), rt=0.4)
        for i, (w, fb) in enumerate([("Chi-square", 0.15), ("Welch's", 0.38), ("McNemar's", 0.6)]):
            self.cue(w, fallback=fb)
            self.go(Create(cards[i][0]), FadeIn(cards[i][1]), FadeIn(cards[i][2]), rt=0.6)
        self.cue("different", fallback=0.88)
        self.go(Create(under(cards[2][2][2])), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Disagree — in our test: chi-square and t-test nothing; McNemar significant, other model.
#  (Progress reel B05_Tests.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Disagree(Scene):
    BID = "B05"
    FALLBACK = 11.0
    ROWS = [("chi-square", "p = 0.1547", ["not significant"], SLATE),
            ("Welch's t-test", "p = 0.1154", ["not significant"], SLATE),
            ("McNemar", "p = 0.0196", ["significant, favors", "the other model"], TEAL)]
    YS = [1.4, -0.1, -1.6]

    def construct(self):
        head = serif("In our test", 40).move_to(UP * 2.95)
        rows = []
        for (nm, p, verdict, col), y in zip(self.ROWS, self.YS):
            box = card(11.8, 1.3, stroke=col, sw=4 if col == TEAL else 3).move_to(UP * y)
            n = sans(nm, 36).move_to(LEFT * 5.5 + UP * y, aligned_edge=LEFT)
            pv = sans(p, 40).move_to(RIGHT * 0.0 + UP * y)
            v = VGroup(*[serif(s, 36, TEAL if col == TEAL else INK) for s in verdict]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
            v.move_to(RIGHT * 2.4 + UP * y, aligned_edge=LEFT)
            rows.append(VGroup(box, n, pv, v))

        self.go(FadeIn(head), rt=0.3)
        self.cue("chi-square", fallback=0.3)
        self.go(*[Create(r[0]) for r in rows[:2]], *[FadeIn(r[1:]) for r in rows[:2]], rt=0.7)
        self.cue("McNemar", fallback=0.6)
        self.go(Create(rows[2][0]), FadeIn(rows[2][1]), FadeIn(rows[2][2]), rt=0.5)
        self.cue("favor", fallback=0.8)
        self.go(FadeIn(rows[2][3]), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — one sample, one other model, one rubric; no self-bias is not correctness.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 14.0

    def construct(self):
        head = serif("When not to over-read it", 44).move_to(UP * 2.95)
        chips = VGroup(chip("one sample of 200", 36), chip("one other model", 36), chip("one rubric", 36)).arrange(RIGHT, buff=0.4)
        chips.move_to(UP * 1.6)
        n_box = card(11.2, 1.4, stroke=SLATE, sw=3).move_to(DOWN * 0.2)
        n_t = serif("No bias toward itself is not the same as correct.", 40).move_to(n_box)
        len_t = sans("it may just be lenient on everything", 38, TEAL).move_to(DOWN * 2.0)

        self.go(FadeIn(head), rt=0.4)
        for i, (w, fb) in enumerate([("sample", 0.15), ("other", 0.25), ("rubric", 0.33)]):
            self.cue(w, fallback=fb)
            self.go(FadeIn(chips[i], shift=UP * 0.1), rt=0.3)
        self.cue("bias", fallback=0.45)
        self.go(Create(n_box), FadeIn(n_t), rt=0.6)
        self.cue("lenient", fallback=0.85)
        self.go(FadeIn(len_t), Create(under(len_t)), rt=0.4)
        self.finish()
