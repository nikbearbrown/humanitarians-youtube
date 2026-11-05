"""scenes.py — Manim scenes for "The Outvoting Problem" (outvoting-problem).

Same project as the Week 1–7 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week8/progress-best-judge-outvoted/scenes.py (Week 7 block + `vbar`); its B02 bars (B02), B04 vote layout (B03),
Week 7 learning three-card layout (B05), Week 4–7 result cards (B06).

Every number on screen appears in inbox/term2-week08/term2-week8-video-content.md as written.
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


# ─────────────────────────────────────────────────────────────────────────────
#  B01_Ballots — three equal ballot boxes; "every vote counts the same"; one judge much better.
# ─────────────────────────────────────────────────────────────────────────────
class B01_Ballots(Scene):
    BID = "B01"
    FALLBACK = 8.7
    XS = (-4.0, 0.0, 4.0)

    def construct(self):
        cap = serif("every vote counts the same", 44).move_to(UP * 2.9)
        boxes = []
        for x in self.XS:
            b = card(2.8, 2.2, stroke=SLATE, sw=3).move_to(RIGHT * x + UP * 0.6)
            slot = Line(RIGHT * (x - 0.6) + UP * 1.3, RIGHT * (x + 0.6) + UP * 1.3, color=SLATE, stroke_width=6)
            v = sans("1 vote", 40).move_to(RIGHT * x + UP * 0.35)
            boxes.append(VGroup(b, slot, v))
        better = chip("much better at the task", 36, stroke=TEAL).move_to(LEFT * 4.0 + DOWN * 1.65)
        better.shift(RIGHT * (better.width / 2 - 1.4))
        q = serif("fair when judges are similar", 38).move_to(DOWN * 2.85)

        self.go(*[FadeIn(b) for b in boxes], rt=0.6)
        self.cue("every", fallback=0.15)
        self.go(FadeIn(cap), Create(under(cap)), rt=0.5)
        self.cue("fair", fallback=0.4)
        self.go(FadeIn(q), rt=0.4)
        self.cue("problem", fallback=0.65)
        self.go(boxes[0][0].animate.set_stroke(TEAL, width=6), FadeIn(better), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Gap — 98% · 69% · 64% alone, yet the ensemble 74%.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Gap(Scene):
    BID = "B02"
    FALLBACK = 10.2
    X0, K = -1.4, 5.6 / 100

    def construct(self):
        head = serif("planted errors caught", 40).move_to(UP * 2.95)
        axis = Line(RIGHT * self.X0 + UP * 2.3, RIGHT * self.X0 + DOWN * 2.3, color=SLATE, stroke_width=3)
        spec = [("claude", "judge 1", 98, "98%", TEAL, 1.75), ("mistral", "judge 2", 69, "69%", SLATE, 0.75),
                ("openai", "judge 3", 64, "64%", SLATE, -0.25), (None, "ensemble", 74, "74%", CRIMSON, -1.65)]
        rows = []
        for lg, nm, pct, ps, col, y in spec:
            parts = [ink_logo(lg, 0.42)] if lg else []
            lab = VGroup(*parts, sans(nm, 36)).arrange(RIGHT, buff=0.2)
            lab.move_to(RIGHT * (self.X0 - 0.3) + UP * y, aligned_edge=RIGHT)
            b = vbar(pct, self.K, self.X0, y, col, h=0.6)
            v = sans(ps, 42).next_to(b, RIGHT, buff=0.2)
            rows.append(VGroup(lab, b, v))
        sep = DashedLine(RIGHT * -5.6 + DOWN * 0.95, RIGHT * 5.6 + DOWN * 0.95, color=SLATE, stroke_width=2.5)
        alone = serif("each judge alone", 32).move_to(RIGHT * (self.X0 - 0.3) + UP * 2.4, aligned_edge=RIGHT)

        self.go(FadeIn(head), Create(axis), FadeIn(alone), rt=0.4)
        self.cue("98", fallback=0.25)
        self.go(FadeIn(rows[0][0]), GrowFromEdge(rows[0][1], LEFT), FadeIn(rows[0][2]), rt=0.5)
        self.cue("69", fallback=0.6)
        self.go(*[FadeIn(r[0]) for r in rows[1:3]], *[GrowFromEdge(r[1], LEFT) for r in rows[1:3]],
                *[FadeIn(r[2]) for r in rows[1:3]], rt=0.5)
        self.cue("Yet", fallback=0.78)
        self.go(Create(sep), FadeIn(rows[3][0]), GrowFromEdge(rows[3][1], LEFT), FadeIn(rows[3][2]), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_TwoToOne — 2 "ship" vs 1 "flag" → ship; "36 of 39 misses". (Week 8 progress B04 layout.)
# ─────────────────────────────────────────────────────────────────────────────
class B03_TwoToOne(Scene):
    BID = "B03"
    FALLBACK = 8.6
    J = [("claude", "strong judge", "flag", TEAL, -4.2), ("mistral", "weaker judge", "ship", CRIMSON, 0.0),
         ("openai", "weaker judge", "ship", CRIMSON, 4.2)]

    def construct(self):
        cols = []
        for lg, nm, vote, col, x in self.J:
            head = VGroup(ink_logo(lg, 0.85), sans(nm, 34)).arrange(DOWN, buff=0.2).move_to(RIGHT * x + UP * 1.45)
            v = chip(vote, 40, stroke=col).move_to(RIGHT * x + DOWN * 0.35)
            cols.append((head, v))
        cnt = sans("36 of 39 misses", 44).move_to(UP * 3.0)
        res = card(6.4, 1.2, stroke=CRIMSON, sw=4).move_to(DOWN * 2.3)
        res_t = serif("2 to 1 → ship", 44).move_to(res)
        a1 = arrow(DOWN * 1.1, DOWN * 1.65)
        bracket = Line(RIGHT * -0.9 + DOWN * 1.1, RIGHT * 5.1 + DOWN * 1.1, color=SLATE, stroke_width=4)

        self.go(*[FadeIn(h) for h, _ in cols], *[FadeIn(v) for _, v in cols], rt=0.6)
        self.cue("win", fallback=0.4)
        self.go(Create(bracket), GrowArrow(a1), Create(res), FadeIn(res_t), Create(strike(cols[0][1][1])), rt=0.6)
        self.cue("36", fallback=0.75)
        self.go(FadeIn(cnt), Create(under(cnt)), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Correlated — the two weaker judges' passed sets overlap heavily; the strong judge's sits apart.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Correlated(Scene):
    BID = "B04"
    FALLBACK = 9.5

    def construct(self):
        head = serif("corrupted items each judge let pass", 40).move_to(UP * 2.95)
        c1 = Circle(radius=1.9, stroke_color=SLATE, stroke_width=4).move_to(LEFT * 1.7 + DOWN * 0.1)
        c2 = Circle(radius=1.9, stroke_color=SLATE, stroke_width=4).move_to(LEFT * 0.3 + DOWN * 0.1)
        l1 = ink_logo("mistral", 0.55).move_to(LEFT * 2.95 + DOWN * 0.1)
        l2 = ink_logo("openai", 0.55).move_to(RIGHT * 0.95 + DOWN * 0.1)
        tog = VGroup(serif("passed", 32), serif("together", 32)).arrange(DOWN, buff=0.05).move_to(LEFT * 1.0 + DOWN * 0.1)
        c3 = Circle(radius=0.65, stroke_color=TEAL, stroke_width=4).move_to(RIGHT * 3.9 + DOWN * 0.1)
        l3 = ink_logo("claude", 0.45).move_to(c3)
        l3t = serif("strong judge", 32).next_to(c3, DOWN, buff=0.25)
        cap = serif("mistakes lined up instead of cancelling out", 38).move_to(DOWN * 2.85)

        self.go(FadeIn(head), rt=0.4)
        self.cue("two", fallback=0.3)
        self.go(Create(c1), Create(c2), FadeIn(l1), FadeIn(l2), rt=0.6)
        self.cue("same", fallback=0.45)
        self.go(FadeIn(tog), Create(c3), FadeIn(l3), FadeIn(l3t), rt=0.5)
        self.cue("lined", fallback=0.72)
        self.go(FadeIn(cap), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Options — three untested vote rules; trade-off fewer errors shipped ↔ more human review.
#  (Week 7 learning B05 three-card layout.)
# ─────────────────────────────────────────────────────────────────────────────
class B05_Options(Scene):
    BID = "B05"
    FALLBACK = 16.0
    OPTS = [("weight by|measured skill", "weight", -4.1), ("one strong|judge can send|to review", "let", 0.0),
            ("ship only if|all agree", "ship", 4.1)]

    def construct(self):
        head = serif("options worth testing", 40).move_to(UP * 2.95)
        cards = []
        for txt, w, x in self.OPTS:
            box = card(3.85, 2.6, stroke=SLATE, sw=3).move_to(RIGHT * x + UP * 0.75)
            t = VGroup(*[sans(s, 30) for s in txt.split("|")]).arrange(DOWN, buff=0.1).move_to(box).shift(UP * 0.3)
            tag = DashedVMobject(RoundedRectangle(width=2.7, height=0.5, corner_radius=0.12, stroke_color=SLATE,
                                                  stroke_width=2.5), num_dashes=28).move_to(box.get_bottom() + UP * 0.42)
            tg = serif("not yet tested", 28).move_to(tag)
            cards.append((VGroup(box, t, tag, tg), w))
        da = DoubleArrow(LEFT * 1.4 + DOWN * 1.6, RIGHT * 1.4 + DOWN * 1.6, buff=0, color=SLATE, stroke_width=4)
        lt = serif("fewer errors shipped", 36).move_to(LEFT * 1.6 + DOWN * 1.6, aligned_edge=RIGHT)
        rt_ = serif("more human review", 36).move_to(RIGHT * 1.6 + DOWN * 1.6, aligned_edge=LEFT)
        note = serif("each option trades one for the other", 34).move_to(DOWN * 2.6)

        self.go(FadeIn(head), rt=0.3)
        for (c, w), fb in zip(cards, (0.1, 0.3, 0.5)):
            self.cue(w, fallback=fb)
            self.go(Create(c[0]), FadeIn(c[1]), Create(c[2]), FadeIn(c[3]), rt=0.5)
        self.cue("trades", fallback=0.68)
        self.go(GrowArrow(da), FadeIn(lt), FadeIn(rt_), FadeIn(note), rt=0.6)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_WhenNot — can't measure who is stronger? weighting = another assumption → measure first.
# ─────────────────────────────────────────────────────────────────────────────
class B06_WhenNot(Scene):
    BID = "B06"
    FALLBACK = 10.3

    def construct(self):
        head = serif("when not to change the vote", 40).move_to(UP * 2.95)
        box = card(10.6, 2.1, stroke=CRIMSON, sw=4).move_to(UP * 1.1)
        t = VGroup(sans("can't measure who is stronger?", 36), serif("weighting = another assumption", 36)).arrange(DOWN, buff=0.2).move_to(box)
        ar = arrow(DOWN * 0.15, DOWN * 0.95)
        ok = card(10.6, 1.3, stroke=TEAL, sw=4).move_to(DOWN * 1.75)
        ok_t = sans("measure first, on known errors", 36, TEAL).move_to(ok)

        self.go(FadeIn(head), rt=0.4)
        self.cue("can't", fallback=0.2)
        self.go(Create(box), FadeIn(t[0]), rt=0.5)
        self.cue("weighting", fallback=0.45)
        self.go(FadeIn(t[1]), rt=0.4)
        self.cue("Measure", fallback=0.75)
        self.go(GrowArrow(ar), Create(ok), FadeIn(ok_t), rt=0.5)
        self.finish()
