"""
Manim scenes for brutalist-installed/vertical: NATIVE 9:16 layouts (frame 4.5 x 8 units)
for body beats B02-B06 + the @HumanitariansAI outro B09. Same evidence, same audio clock
as the 16:9 cut; long strings WRAP (never shrink below the type floor).

Every artifact on screen is real: folder names, build-state.json contents, the setup guard
message, the Windows python3 message, manim's Requires-Python range (>=3.9,<3.13), the three
commands that were run, and the ./setup readiness rows. The B03 still is a frame the first
attempt actually rendered (images/first-attempt-frame.png).

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only).
"""

import os

import numpy as np
from manim import *

# Portrait scene units: 4.5 wide x 8 tall (Manim otherwise keeps the 14.2 landscape
# width and stretches the height when given a 9:16 pixel resolution).
config.frame_height = 8.0
config.frame_width = 4.5

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.environ.get("ART_HOME") or os.path.join(HERE, "..", "..", "..", "brutalist")

try:  # make the bundled faces resolvable by Pango even if not installed system-wide
    import manimpango
    for _rel in ("runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf",
                 "runtime/fonts/PT_Mono/PTMono-Regular.ttf"):
        _p = os.path.join(_HOME, _rel)
        if os.path.isfile(_p):
            manimpango.register_font(_p)
except Exception:
    pass

PAGE = "#FAF9F5"
CARD = "#F2F0E9"
INK = "#3D3929"
INK_SOFT = "#73705F"
SPARK = "#D97757"
OK = "#5B7F4A"          # muted green for "ready" ticks (shape only)
SERIF = "EB Garamond"
MONO = "PT Mono"


# ── shared helpers ────────────────────────────────────────────────────────────

def serif(s, size=36, color=INK):
    return Text(s, font=SERIF, font_size=size, color=color)


def mono(s, size=26, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def fit(m, width):
    if m.width > width:
        m.scale_to_fit_width(width)
    return m


def spark_line(words):
    """The spark + one short serif line, top-left (SPARK-LINE LAW)."""
    c = np.array([-1.75, 3.05, 0])
    arms = VGroup(*[
        Line(c + 0.15 * np.array([np.cos(a), np.sin(a), 0]),
             c - 0.15 * np.array([np.cos(a), np.sin(a), 0]),
             color=SPARK, stroke_width=6)
        for a in (0, np.pi / 3, 2 * np.pi / 3)])
    label = fit(serif(words, 34), 3.25).next_to(arms, RIGHT, buff=0.22)
    return VGroup(arms, label)


def wordmark(height):
    try:
        m = SVGMobject(os.path.join(HERE, "hai-wordmark.svg"))
        m.set_fill(INK, opacity=1).set_stroke(width=0)
        m.height = height
        return m
    except Exception:
        return serif("Humanitarians AI", int(height * 60))


def logo_bug():
    """HAI mark, small and low-opacity, lower-right inside title-safe (LOGO LAW)."""
    bug = wordmark(0.13)
    bug.set_fill(INK, opacity=0.4)
    return bug.move_to(np.array([1.2, -3.42, 0]))


def tick(color=OK, s=0.26):
    return VMobject(stroke_color=color, stroke_width=7).set_points_as_corners(
        [[-0.5 * s, 0, 0], [-0.1 * s, -0.4 * s, 0], [0.6 * s, 0.45 * s, 0]])


def cross(color=SPARK, s=0.24):
    return VGroup(Line([-s / 2, -s / 2, 0], [s / 2, s / 2, 0], color=color, stroke_width=7),
                  Line([-s / 2, s / 2, 0], [s / 2, -s / 2, 0], color=color, stroke_width=7))


def box(w, h, fill=PAGE, stroke=INK_SOFT):
    return RoundedRectangle(corner_radius=0.1, width=w, height=h).set_fill(
        fill, opacity=1).set_stroke(stroke, width=2)


def chip(label, mark, size=26):
    g = VGroup(mono(label, size), mark.copy().scale(0.7)).arrange(RIGHT, buff=0.12)
    b = box(g.width + 0.25, g.height + 0.16)
    return VGroup(b, g.move_to(b))


def terminal_line(text, size=26, width=3.95):
    """Real terminal output on a soft card; newlines wrap (portrait: wrap, never shrink)."""
    lines = VGroup(*[mono(l, size) for l in text.split("\n")]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
    fit(lines, width - 0.3)
    b = box(width, lines.height + 0.3, fill=CARD)
    return VGroup(b, lines.move_to(b).align_to(b, LEFT).shift(RIGHT * 0.15))


def _setup(self):
    self.camera.background_color = PAGE
    self.add(logo_bug())
    self.t = 0.0


def _at(self, target):
    """Wait until `target` seconds into the beat (audio clock)."""
    now = getattr(self, "t", 0.0)
    if target > now:
        self.wait(target - now)
    self.t = max(now, target)


def _run(self, *anims, rt=0.6):
    self.play(*anims, run_time=rt)
    self.t = getattr(self, "t", 0.0) + rt


# ── B02 — the first attempt (18.97 s) ────────────────────────────────────────
# Portrait: wrap, never shrink. Mono >= 26, <= ~22 chars per line (gate T floor).

class B02_FirstAttempt(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The first attempt.")), rt=0.4)

        r1 = VGroup(mono("binary-search-test"), chip("mp3/", tick())).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        r2 = VGroup(mono("claude-liam-"), mono("  ribosomes-read-mrna"),
                    VGroup(chip("mp3/", tick()), chip("manim/", tick())).arrange(RIGHT, buff=0.15)
                    ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        folders = VGroup(r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, 1.55, 0]).align_to([-1.9, 0, 0], LEFT)

        js = VGroup(
            mono("both build-state.json:", 24, INK_SOFT),
            mono('"status": "failed",'),
            mono('"error": "Review'),
            mono('  pipeline failed'),
            mono('  (exit 2)"'),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        fit(js, 3.6)
        jbox = box(3.95, js.height + 0.35, fill=CARD).move_to([0, -1.25, 0])
        js.move_to(jbox).align_to(jbox, LEFT).shift(RIGHT * 0.18)
        word = js[1]
        under = Line(word.get_right() + LEFT * 1.12 + DOWN * 0.19,
                     word.get_right() + LEFT * 0.1 + DOWN * 0.19, color=SPARK, stroke_width=5)

        self.at(4.6)   # "I built two test videos."
        self.run(FadeIn(r1[0], shift=UP * 0.15), FadeIn(r2[0:2], shift=UP * 0.15), rt=0.7)
        self.at(6.6)   # "The narration was generated."
        self.run(FadeIn(r1[1]), FadeIn(r2[2][0]), rt=0.5)
        self.at(8.4)   # "Some animations even rendered."
        self.run(FadeIn(r2[2][1]), rt=0.5)
        self.at(12.4)  # "the build-state file says failed..."
        self.run(FadeIn(jbox), FadeIn(js, lag_ratio=0.15), rt=0.9)
        self.run(Create(under), rt=0.5)

        none = VGroup(serif("finished cut:", 32), serif("none", 32, INK_SOFT)).arrange(RIGHT, buff=0.18)
        slot = DashedVMobject(RoundedRectangle(corner_radius=0.1, width=none.width + 0.5,
                                               height=none.height + 0.3).set_stroke(INK, width=3),
                              num_dashes=36)
        end = VGroup(slot, none.move_to(slot)).move_to([0, -2.95, 0])
        self.at(16.6)  # "Neither video made it to a finished cut."
        self.run(FadeIn(end), rt=0.5)
        self.at(18.97)


# ── B03 — what went wrong (18.20 s) ──────────────────────────────────────────

class B03_Causes(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("What went wrong.")), rt=0.4)

        img = ImageMobject(os.path.join(HERE, "images", "first-attempt-frame.png"))
        img.scale_to_fit_width(3.1)
        frame = SurroundingRectangle(img, buff=0, color=INK_SOFT, stroke_width=1.5).set_stroke(opacity=0.5)
        cap = VGroup(serif("a frame the first", 38, INK_SOFT), serif("attempt rendered", 38, INK_SOFT)
                     ).arrange(DOWN, buff=0.02).next_to(img, DOWN, buff=0.12)
        shot = Group(img, frame, cap).move_to([0, 1.42, 0])

        def problem(*lines):
            t = VGroup(*[serif(l, 37) for l in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.02)
            bar = Line(UP * 0.3, DOWN * 0.3, color=SPARK, stroke_width=8)
            return VGroup(bar, t).arrange(RIGHT, buff=0.2)

        p1 = problem("packages wanting", "an older Python").move_to([0, -0.55, 0]).align_to([-1.88, 0, 0], LEFT)
        p2 = problem("gate checks", "halting the build").move_to([0, -1.62, 0]).align_to([-1.88, 0, 0], LEFT)

        self.run(FadeIn(shot), rt=0.8)
        self.at(2.6)   # "Some packages needed an older Python..."
        self.run(FadeIn(p1, shift=DOWN * 0.2), rt=0.6)
        self.at(7.3)   # "...stopping at its gates"
        self.run(FadeIn(p2, shift=DOWN * 0.2), rt=0.6)

        hours = VGroup(serif("hours of patching", 38, INK_SOFT), serif("symptoms", 38, INK_SOFT)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.02).move_to([0, -2.75, 0]).align_to([-1.88, 0, 0], LEFT)
        self.at(12.6)  # "I spent hours patching symptoms."
        self.run(FadeIn(hours), rt=0.5)
        self.at(15.0)  # "Eventually I deleted the old install..."
        everything = Group(shot, p1, p2, hours)
        self.run(FadeOut(everything), rt=1.2)
        restart = serif("start over.", 60).move_to(ORIGIN)
        self.run(FadeIn(restart), rt=0.5)
        self.at(18.20)


# ── B04 — second attempt: the false alarm (18.24 s) ─────────────────────────

class B04_FalseAlarm(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Second attempt.")), rt=0.4)

        clone = terminal_line("$ git clone\n  https://github.com/\n  nikbearbrown/\n  brutalist.art.git")
        clone.move_to([0, 1.95, 0])
        self.at(1.0)   # "a clean copy"
        self.run(FadeIn(clone, shift=DOWN * 0.15), rt=0.6)

        guard = terminal_line("$ ./setup\n  ElevenLabs reference\n  found — this toolkit\n  is Kokoro-only")
        guard.next_to(clone, DOWN, buff=0.12)
        x = cross().move_to(guard[0].get_corner(UR) + DOWN * 0.25 + LEFT * 0.3)
        self.at(7.6)   # "The setup check stopped at once"
        self.run(FadeIn(guard), Create(x), rt=0.6)

        folder = box(3.85, 1.5).move_to([0, -1.72, 0])
        blabel = mono("brutalist/").move_to(folder.get_top() + DOWN * 0.24).align_to(folder, LEFT).shift(RIGHT * 0.12)
        subs = VGroup(mono("runtime/", 26, INK_SOFT), mono("skills/", 26, INK_SOFT),
                      mono("youtube/brutalist/")).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        subs.next_to(blabel, DOWN, buff=0.06).align_to(blabel, LEFT).shift(RIGHT * 0.1)
        hl = SurroundingRectangle(subs[2], buff=0.05, color=SPARK, stroke_width=4)
        note = serif("videos about the check itself", 30, INK_SOFT)
        fit(note, 3.9).move_to([0, -2.85, 0])

        self.at(11.0)  # "It was a false alarm"
        self.run(FadeIn(folder), FadeIn(blabel), FadeIn(subs), rt=0.6)
        self.run(Create(hl), FadeIn(note), rt=0.5)

        dlabel = mono("brutalist-vids/", 26, INK_SOFT)
        dest = box(dlabel.width + 0.3, 0.45).move_to([0, -3.1, 0]).align_to([-1.8, 0, 0], LEFT)
        dlabel.move_to(dest)
        ok = VGroup(serif("check: clean", 32), tick()).arrange(RIGHT, buff=0.14)
        ok.move_to(guard).align_to(guard, RIGHT).shift(LEFT * 0.15)

        self.at(15.9)  # "Moved out, the check passed."
        self.run(FadeOut(note), FadeIn(dest), FadeIn(dlabel), rt=0.4)
        moving = VGroup(subs[2], hl)
        self.run(moving.animate.next_to(dest, UP, buff=0.04).align_to(dest, LEFT).shift(RIGHT * 0.06), rt=0.8)
        self.run(FadeOut(x), FadeOut(guard), FadeIn(ok), rt=0.5)
        self.at(18.24)


# ── B05 — the Python fix (17.96 s) ──────────────────────────────────────────

class B05_PythonFix(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("One fix for both.")), rt=0.4)

        versions = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]
        x0, dx, y = -1.5, 0.6, 1.95
        axis = Line([x0 - 0.2, y, 0], [x0 + dx * 5 + 0.2, y, 0], color=INK, stroke_width=3)
        ticks = VGroup(*[Line([x0 + dx * i, y - 0.08, 0], [x0 + dx * i, y + 0.08, 0],
                              color=INK, stroke_width=3) for i in range(6)])
        labels = VGroup(*[mono(v, 26).move_to([x0 + dx * i, y - 0.3, 0])
                          for i, v in enumerate(versions) if v in ("3.9", "3.12", "3.14")])
        band = Rectangle(width=dx * 3 + 0.3, height=0.26).set_fill(OK, opacity=0.18).set_stroke(width=0)
        band.move_to([x0 + dx * 1.5, y, 0])
        blabel = VGroup(mono("manim 0.18 requires", 26, INK_SOFT), mono("Python >=3.9, <3.13", 26, INK_SOFT))
        blabel.arrange(DOWN, aligned_edge=LEFT, buff=0.08).next_to(labels, DOWN, buff=0.2).align_to([-1.9, 0, 0], LEFT)

        def marker(i, color, text):
            p = Triangle(fill_color=color, fill_opacity=1, stroke_width=0).scale(0.13).rotate(PI)
            p.move_to([x0 + dx * i, y + 0.3, 0])
            return VGroup(p, serif(text, 30).next_to(p, UP, buff=0.08))

        m314 = marker(5, SPARK, "mine")
        m312 = marker(3, OK, "the fix")

        self.at(1.2)   # "...came back. My Python was too new"
        self.run(Create(axis), FadeIn(ticks), FadeIn(labels), FadeIn(band), FadeIn(blabel), rt=0.8)
        self.at(3.4)
        self.run(FadeIn(m314, shift=DOWN * 0.2), rt=0.5)

        msg = terminal_line("$ python3\n  Python was not found;\n  run without arguments\n  to install from the\n  Microsoft Store…")
        msg.move_to([0, -0.85, 0])
        self.at(6.4)   # "...couldn't even find it by name"
        self.run(FadeIn(msg), rt=0.5)

        cmds = VGroup(
            terminal_line("$ py -3.12 -m venv\n    .venv"),
            terminal_line("$ cp .venv/Scripts/\n    python.exe\n  .venv/Scripts/\n    python3.exe"),
            terminal_line("$ ./setup --install"),
        ).arrange(DOWN, buff=0.1).move_to([0, -1.45, 0])
        for c in cmds:
            c.set_opacity(0)

        self.at(10.4)  # "One fix covered both"
        self.run(FadeOut(msg), rt=0.4)
        self.at(11.6)  # "a separate Python three point twelve environment"
        self.run(FadeIn(m312, shift=DOWN * 0.2), cmds[0].animate.set_opacity(1), rt=0.6)
        self.at(14.2)  # "a python three command inside it"
        self.run(cmds[1].animate.set_opacity(1), rt=0.5)
        self.at(16.3)  # "then the toolkit's own installer"
        self.run(cmds[2].animate.set_opacity(1), rt=0.5)
        self.at(17.96)


# ── B06 — the readiness table (13.65 s) ─────────────────────────────────────

class B06_Readiness(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Ready.")), rt=0.4)

        rows = [
            ("audio", "(Kokoro Bella/Onyx)"),
            ("captions +", "word clock"),
            ("Manim beats", None),
            ("Manim equation", "beats"),
            ("Remotion beats", "+ bookends"),
            ("slates / previz /", "compile"),
            ("fonts (EB Garamond", "+ Oswald)"),
        ]
        xl, xr = -1.9, 1.62
        head = VGroup(mono("FEATURE", 24, INK_SOFT).move_to([xl, 2.5, 0], aligned_edge=LEFT),
                      mono("STATUS", 24, INK_SOFT).move_to([1.9, 2.5, 0], aligned_edge=RIGHT))
        rule = Line([xl, 2.3, 0], [1.9, 2.3, 0], color=INK_SOFT, stroke_width=2)
        names, status = VGroup(), []
        y = 2.12
        for i, (a, b) in enumerate(rows):
            g = VGroup(mono(a)) if b is None else VGroup(mono(a), mono(b, 26, INK_SOFT)).arrange(
                DOWN, aligned_edge=LEFT, buff=0.04)
            fit(g, 3.1)
            g.move_to([xl, y - g.height / 2, 0], aligned_edge=LEFT)
            names.add(g)
            s = cross() if i == 3 else tick()
            status.append(s.move_to([xr, g.get_center()[1], 0]))
            y -= g.height + 0.07

        self.at(0.6)   # "Then the check that matters."
        self.run(FadeIn(head), Create(rule), FadeIn(names, lag_ratio=0.08), rt=0.9)
        self.at(2.4)   # "Voice: ready."
        self.run(FadeIn(status[0]), rt=0.4)
        for i, t in zip((1, 2, 4, 5, 6), (3.4, 4.1, 4.8, 5.6, 6.3)):
            self.at(t)  # "Captions, animation, scenes, compiling: ready."
            self.run(FadeIn(status[i]), rt=0.35)
        self.at(7.9)   # "One row stays blocked: equations need LaTeX."
        hl = SurroundingRectangle(VGroup(names[3], status[3]), buff=0.07, color=SPARK, stroke_width=4)
        self.run(FadeIn(status[3]), Create(hl), rt=0.5)
        tag = VGroup(serif("blocked: needs LaTeX,", 30, INK_SOFT), serif("not needed for this video", 30, INK_SOFT))
        tag.arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        fit(tag, 3.75).next_to(names[-1], DOWN, buff=0.16).align_to(names, LEFT)
        self.at(10.4)  # "This video has no equations, so that one can wait."
        self.run(FadeIn(tag), rt=0.5)
        self.at(13.65)


# ── B09 — @HumanitariansAI title outro (8.06 s) ─────────────────────────────

class B09_Outro(Scene):
    at = _at
    run = _run

    def setup(self):
        # Outro card carries the mark full size instead of the corner bug.
        self.camera.background_color = PAGE
        self.t = 0.0

    def construct(self):
        l1, l2 = serif("Brutalist,", 72), serif("Installed", 72)
        dot = Dot(radius=0.06, color=SPARK)
        line2 = VGroup(l2, dot).arrange(RIGHT, buff=0.03, aligned_edge=DOWN)
        dot.shift(UP * 0.07)
        title = VGroup(l1, line2).arrange(DOWN, buff=0.15).move_to([0, 1.0, 0])
        fit(title, 3.8)
        sub = serif("Made with this install.", 32, INK_SOFT).next_to(title, UP, buff=0.45)
        fit(sub, 3.8)
        self.run(Write(l1), Write(l2), FadeIn(sub), rt=1.0)
        self.run(FadeIn(dot, scale=1.6), rt=0.3)
        rule = Line(title.get_left(), title.get_right(), color=SPARK, stroke_width=4)
        rule.next_to(title, DOWN, buff=0.18)
        self.run(Create(rule), rt=0.5)

        mark = wordmark(0.26).move_to([0, -1.2, 0])
        handle = serif("@HumanitariansAI", 34).next_to(mark, DOWN, buff=0.25)
        fit(handle, 3.6)
        self.at(3.4)   # "...works as expected." — the mark is up before the title is read
        self.run(FadeIn(mark), FadeIn(handle), rt=0.6)
        self.at(8.06)


# ── B07 — verdict: what I learned (16.19 s) ──────────────────────────────────
# Portrait replacement for ClaudeVerdictArtifact916 (fixed small card -> gate V
# underfill at 29%). Same artifact-page pattern: label, heading, numbered lines.

class B07_Verdict(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        card = box(3.9, 6.25, fill=CARD).move_to([0, -0.08, 0])
        label = mono("Verdict", 24, INK_SOFT).move_to(card.get_corner(UL) + RIGHT * 0.25 + DOWN * 0.3, aligned_edge=UL)
        rule = Line(card.get_left() + RIGHT * 0.2, card.get_right() + LEFT * 0.2, color=INK_SOFT, stroke_width=2)
        rule.next_to(label, DOWN, buff=0.15).set_x(0)
        heading = serif("What I learned", 44).next_to(rule, DOWN, buff=0.35).align_to(label, LEFT)

        def item(n, *lines):
            num = serif(f"{n}.", 38)
            t = VGroup(*[serif(l, 38) for l in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
            return VGroup(num, t).arrange(RIGHT, buff=0.22, aligned_edge=UP)

        items = VGroup(item(1, "Read the", "error first"),
                       item(2, "Gates are", "checks,", "not bugs"),
                       item(3, "Isolate your", "Python")).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        items.next_to(heading, DOWN, buff=0.35).align_to(heading, LEFT).shift(RIGHT * 0.22)
        marks = VGroup(*[Line(UP * 0.22, DOWN * 0.22, color=SPARK, stroke_width=7).next_to(it, LEFT, buff=0.12).align_to(it, UP).shift(DOWN * 0.08) for it in items])
        for it in items:
            it.set_opacity(0)

        self.run(FadeIn(card), FadeIn(label), Create(rule), FadeIn(heading), rt=0.6)
        self.at(0.8)   # "Read the error before fixing anything"
        self.run(items[0].animate.set_opacity(1), FadeIn(marks[0]), rt=0.5)
        self.at(6.3)   # "Gates are checks, not bugs"
        self.run(items[1].animate.set_opacity(1), FadeIn(marks[1]), rt=0.5)
        self.at(11.8)  # "And isolate your Python."
        self.run(items[2].animate.set_opacity(1), FadeIn(marks[2]), rt=0.5)
        self.at(16.19)
