"""scenes.py — Manim scenes for "Scripted Final Checks" (scripted-final-checks).

Same project as the Week 1–11 reels: the helper block and clocked Beat base (`Scene = Beat`) from
hai-videos/Week12/progress-related-work-rebuilt/scenes.py (Week 11 block); Week 9 learning `step_head` (B02–B05), Week 9 tick checklist (B04),
Week 12 cross mark (B01, B03), Week 4–11 result cards (B05, B06).

Every number on screen appears in inbox/term2-week12/term2-week12-video-content.md as written.
Only Professor Brown and Professor Gultepe are ever named. Short beats show their key text at once (Week 5 GATE T lesson).

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


def stamp(text, w, color=CRIMSON, size=42, angle=-6):
    """Rotated outline stamp (Week 9 learning B01)."""
    s = VGroup(RoundedRectangle(width=w, height=1.0, corner_radius=0.12, stroke_color=color, stroke_width=5),
               sans(text, size))
    s[1].move_to(s[0])
    return s.rotate(angle * DEGREES)


# Week 9–10 GATE T lesson: in dense cards keep serif ≥ 42 and sans ≥ 40; never strike serif text.


def envelope(w=0.95, h=0.62, color=SLATE):
    return VGroup(Rectangle(width=w, height=h, stroke_color=color, stroke_width=3, fill_opacity=0),
                  VMobject(stroke_color=color, stroke_width=3).set_points_as_corners(
                      [LEFT * w / 2 + UP * h / 2, DOWN * h * 0.08, RIGHT * w / 2 + UP * h / 2]))


def step_head(n, title):
    """Numbered teal badge + sans title (Week 9 learning)."""
    badge = VGroup(Circle(radius=0.42, stroke_color=TEAL, stroke_width=5), sans(str(n), 44, TEAL))
    badge[1].move_to(badge[0])
    return VGroup(badge, sans(title, 50)).arrange(RIGHT, buff=0.4).move_to(UP * 2.75)


def cross(s=0.3, color=CRIMSON):
    return VGroup(Line(UL * s, DR * s, color=color, stroke_width=7), Line(DL * s, UR * s, color=color, stroke_width=7))


# ─────────────────────────────────────────────────────────────────────────────
#  B01_EyeScript — dozens of edits; rereading by eye ✗; a script, the same checks every time ✓.
# ─────────────────────────────────────────────────────────────────────────────
class B01_EyeScript(Scene):
    BID = "B01"
    FALLBACK = 10.1

    def construct(self):
        stack = VGroup(*[card(2.6, 1.8, stroke=SLATE, sw=3).move_to(LEFT * (4.3 - i * 0.22) + UP * (1.1 - i * 0.22)) for i in range(4)])
        sl = serif("dozens of edits", 44).move_to(LEFT * 3.7 + DOWN * 1.3)
        x = cross().move_to(LEFT * 0.6 + UP * 1.3)
        eye = sans("rereading by eye", 46).move_to(LEFT * 0.0 + UP * 1.3, aligned_edge=LEFT)
        ok = tick(s=0.45).move_to(LEFT * 0.6 + DOWN * 0.2)
        scr = sans("a script", 46, TEAL).move_to(LEFT * 0.0 + DOWN * 0.2, aligned_edge=LEFT)
        same = serif("the same checks every time", 44).move_to(LEFT * 0.0 + DOWN * 1.0, aligned_edge=LEFT)

        self.go(LaggedStart(*[Create(c) for c in stack], lag_ratio=0.2), FadeIn(sl), rt=0.8)
        self.cue("rereading", fallback=0.2)
        self.go(FadeIn(eye), Create(x), rt=0.4)
        self.cue("script", fallback=0.7)
        self.go(FadeIn(scr), Create(ok), FadeIn(same), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B02_Present — check 1: key figures that must be present.
# ─────────────────────────────────────────────────────────────────────────────
class B02_Present(Scene):
    BID = "B02"
    FALLBACK = 17.9

    def construct(self):
        head = step_head(1, "must be present")
        r1 = VGroup(*[chip(t, 48, stroke=TEAL) for t in ("8,968", "8,053", "915", "10,049")]).arrange(RIGHT, buff=0.4).move_to(UP * 1.0)
        r2 = VGroup(*[chip(t, 48, stroke=TEAL) for t in ("5.8%", "kappa 0.4884", "74.0%")]).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.4)
        cap = serif("the script fails if any is missing", 44).move_to(DOWN * 2.1)

        self.go(FadeIn(head), Create(head[0][0]), rt=0.5)
        self.cue("8,968", fallback=0.3)
        self.go(LaggedStart(*[FadeIn(c) for c in r1], lag_ratio=0.3), rt=1.4)
        self.cue("5.8", fallback=0.65)
        self.go(LaggedStart(*[FadeIn(c) for c in r2], lag_ratio=0.3), rt=1.2)
        self.go(FadeIn(cap), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B03_Absent — check 2: retired values and old wording must be absent; FAIL if found.
# ─────────────────────────────────────────────────────────────────────────────
class B03_Absent(Scene):
    BID = "B03"
    FALLBACK = 7.7

    def construct(self):
        head = step_head(2, "must be absent")
        row = VGroup(*[chip(t, 48, stroke=CRIMSON) for t in ("6.5%", "906", "61,000", "old wording")]).arrange(RIGHT, buff=0.4).move_to(UP * 0.9)
        out = card(6.4, 1.4, stroke=CRIMSON, sw=5).move_to(DOWN * 1.3)
        ot = sans("FAIL if found", 52).move_to(out)

        self.go(FadeIn(head), Create(head[0][0]), FadeIn(row), rt=0.5)
        self.cue("fails", fallback=0.6)
        self.go(Create(out), FadeIn(ot), rt=0.5)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Structure — check 3: references cited and present · figures in order · captions placed.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Structure(Scene):
    BID = "B04"
    FALLBACK = 6.1
    ROWS = [("every reference cited and present", "every"), ("figures in order", "figures"), ("captions in the right place", "captions")]

    def construct(self):
        head = step_head(3, "structure")
        rows = [checkrow(t, None, 1.2 - i * 1.1, xl=-5.0, ls=42) for i, (t, _) in enumerate(self.ROWS)]
        self.go(FadeIn(head), Create(head[0][0]), rt=0.4)
        for r, (_, w), fb in zip(rows, self.ROWS, (0.25, 0.55, 0.75)):
            self.cue(w, fallback=fb)
            self.go(FadeIn(r[1]), Create(r[0]), rt=0.35)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B05_Limits — check 4: abstract under 300 words · 5 highlights under 85 characters.
# ─────────────────────────────────────────────────────────────────────────────
class B05_Limits(Scene):
    BID = "B05"
    FALLBACK = 7.3

    def construct(self):
        head = step_head(4, "journal limits")
        a = card(5.4, 2.2, stroke=TEAL, sw=4).move_to(LEFT * 2.9 + UP * 0.4)
        at = VGroup(sans("abstract", 48), serif("under 300 words", 46)).arrange(DOWN, buff=0.18).move_to(a)
        b = card(5.4, 2.2, stroke=TEAL, sw=4).move_to(RIGHT * 2.9 + UP * 0.4)
        bt = VGroup(sans("5 highlights", 48), serif("under 85 characters", 46)).arrange(DOWN, buff=0.18).move_to(b)

        self.go(FadeIn(head), Create(head[0][0]), rt=0.4)
        self.cue("abstract", fallback=0.25)
        self.go(Create(a), FadeIn(at), rt=0.4)
        self.cue("five", fallback=0.6)
        self.go(Create(b), FadeIn(bt), rt=0.4)
        self.finish()


# ─────────────────────────────────────────────────────────────────────────────
#  B06_Human — what a script can't check → a careful human read.
# ─────────────────────────────────────────────────────────────────────────────
class B06_Human(Scene):
    BID = "B06"
    FALLBACK = 9.0

    def construct(self):
        head = serif("what a script can't check", 46).move_to(UP * 2.9)
        c1 = chip("argument holds?", 46, stroke=CRIMSON).move_to(LEFT * 3.4 + UP * 1.2)
        c2 = chip("claims match evidence?", 46, stroke=CRIMSON).move_to(RIGHT * 2.9 + UP * 1.2)
        a1 = arrow(LEFT * 3.4 + UP * 0.55, LEFT * 1.4 + DOWN * 0.75)
        a2 = arrow(RIGHT * 2.9 + UP * 0.55, RIGHT * 1.4 + DOWN * 0.75)
        hr = card(8.6, 1.4, stroke=TEAL, sw=5).move_to(DOWN * 1.55)
        ht = sans("a careful human read", 50, TEAL).move_to(hr)

        self.go(FadeIn(head), rt=0.4)
        self.cue("argument", fallback=0.25)
        self.go(FadeIn(c1), rt=0.4)
        self.cue("claims", fallback=0.45)
        self.go(FadeIn(c2), rt=0.4)
        self.cue("careful", fallback=0.8)
        self.go(GrowArrow(a1), GrowArrow(a2), Create(hr), FadeIn(ht), rt=0.5)
        self.finish()
