"""
Manim scenes for brutalist-installed  (body beats B02-B06 + the @HumanitariansAI outro B09)

Every artifact on screen is real: folder names, build-state.json contents, the setup guard
message, the Windows python3 message, manim's Requires-Python range (>=3.9,<3.13), the three
commands that were run, and the ./setup readiness rows. The B03 still is a frame the first
attempt actually rendered (images/first-attempt-frame.png).

Claude palette: cream ground, warm ink, terracotta as the one accent (shapes only -
terracotta never carries text; it fails AA contrast on cream).
Run times are fitted to the measured Kokoro audio (af_bella, speed 1.0).
"""

import os

import numpy as np
from manim import *

HERE = os.path.dirname(os.path.abspath(__file__))
_HOME = os.environ.get("ART_HOME") or os.path.join(HERE, "..", "..", "brutalist")

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


def mono(s, size=30, color=INK):
    return Text(s, font=MONO, font_size=size, color=color)


def fit(m, width):
    if m.width > width:
        m.scale_to_fit_width(width)
    return m


def spark_line(words):
    """The spark + one short serif line, top-left (SPARK-LINE LAW)."""
    c = np.array([-5.85, 2.95, 0])
    arms = VGroup(*[
        Line(c + 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             c - 0.2 * np.array([np.cos(a), np.sin(a), 0]),
             color=SPARK, stroke_width=6)
        for a in (0, np.pi / 3, 2 * np.pi / 3)])
    label = serif(words, 44).next_to(arms, RIGHT, buff=0.3)
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
    bug = wordmark(0.22)
    bug.set_fill(INK, opacity=0.4)
    return bug.move_to(np.array([4.95, -3.2, 0]))


def tick(color=OK, s=0.32):
    return VMobject(stroke_color=color, stroke_width=8).set_points_as_corners(
        [[-0.5 * s, 0, 0], [-0.1 * s, -0.4 * s, 0], [0.6 * s, 0.45 * s, 0]])


def cross(color=SPARK, s=0.3):
    return VGroup(Line([-s / 2, -s / 2, 0], [s / 2, s / 2, 0], color=color, stroke_width=8),
                  Line([-s / 2, s / 2, 0], [s / 2, -s / 2, 0], color=color, stroke_width=8))


def card(w, h, fill=CARD):
    return RoundedRectangle(corner_radius=0.18, width=w, height=h).set_fill(
        fill, opacity=1).set_stroke(INK, width=2.5)


def chip(label, mark, size=26):
    t = mono(label, size)
    g = VGroup(t, mark.copy().scale(0.8)).arrange(RIGHT, buff=0.18)
    box = RoundedRectangle(corner_radius=0.15, width=g.width + 0.4, height=g.height + 0.25)
    box.set_fill(PAGE, opacity=1).set_stroke(INK_SOFT, width=2)
    return VGroup(box, g.move_to(box))


def terminal_line(text, size=28, width=12.0):
    """One line of real terminal output on a soft card."""
    t = fit(mono(text, size), width - 0.6)
    box = RoundedRectangle(corner_radius=0.15, width=width, height=t.height + 0.5)
    box.set_fill(CARD, opacity=1).set_stroke(INK_SOFT, width=2)
    return VGroup(box, t.move_to(box).align_to(box, LEFT).shift(RIGHT * 0.3))


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

class B02_FirstAttempt(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("The first attempt.")), rt=0.4)

        def reel(name, chips):
            c = card(6.0, 4.9).set_fill(PAGE)
            title = fit(mono(name, 28), 5.4)
            title.move_to(c.get_top() + DOWN * 0.45)
            rule = Line(c.get_left() + RIGHT * 0.25, c.get_right() + LEFT * 0.25,
                        color=INK_SOFT, stroke_width=2).next_to(title, DOWN, buff=0.25)
            ch = VGroup(*chips).arrange(RIGHT, buff=0.25).next_to(rule, DOWN, buff=0.3)
            js = VGroup(
                mono("build-state.json", 22, INK_SOFT),
                mono('"status": "failed",', 26),
                mono('"error": "Review pipeline', 26),
                mono('  failed (exit 2)"', 26),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            fit(js, 5.4)
            js.next_to(ch, DOWN, buff=0.4).align_to(c, LEFT).shift(RIGHT * 0.35)
            under = Line(js[1].get_left() + RIGHT * 1.75 + DOWN * 0.24,
                         js[1].get_right() + LEFT * 0.12 + DOWN * 0.24,
                         color=SPARK, stroke_width=6)
            return VGroup(c, title, rule), ch, js, under

        a_frame, a_chips, a_js, a_u = reel("binary-search-test", [chip("mp3/", tick())])
        b_frame, b_chips, b_js, b_u = reel("claude-liam-ribosomes-read-mrna",
                                           [chip("mp3/", tick()), chip("manim/", tick())])
        left = VGroup(a_frame, a_chips, a_js, a_u).move_to([-3.2, -0.25, 0])
        right = VGroup(b_frame, b_chips, b_js, b_u).move_to([3.2, -0.25, 0])

        self.at(4.6)   # "I built two test videos."
        self.run(FadeIn(a_frame, shift=UP * 0.3), FadeIn(b_frame, shift=UP * 0.3), rt=0.7)
        self.at(6.6)   # "The narration was generated."
        self.run(FadeIn(a_chips[0]), FadeIn(b_chips[0]), rt=0.5)
        self.at(8.4)   # "Some animations even rendered."
        self.run(FadeIn(b_chips[1]), rt=0.5)
        self.at(12.4)  # "the build-state file says failed..."
        self.run(FadeIn(a_js, lag_ratio=0.15), FadeIn(b_js, lag_ratio=0.15), rt=0.9)
        self.run(Create(a_u), Create(b_u), rt=0.5)

        none = VGroup(serif("finished cut:", 38), serif("none", 38, INK_SOFT)).arrange(RIGHT, buff=0.25)
        slot = DashedVMobject(RoundedRectangle(corner_radius=0.15, width=none.width + 0.8,
                                               height=none.height + 0.4).set_stroke(INK, width=3),
                              num_dashes=40)
        end = VGroup(slot, none.move_to(slot))
        self.at(16.6)  # "Neither video made it to a finished cut."
        self.run(left.animate.shift(UP * 0.35), right.animate.shift(UP * 0.35), rt=0.4)
        end.move_to([0, -3.15, 0])
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
        img.scale_to_fit_width(6.0)
        frame = SurroundingRectangle(img, buff=0, color=INK, stroke_width=2.5)
        cap = serif("a frame the first attempt rendered", 30, INK_SOFT).next_to(img, DOWN, buff=0.25)
        shot = Group(img, frame, cap).move_to([-3.25, -0.2, 0])

        def stage(name, mark):
            b = card(1.9, 1.3).set_fill(PAGE).set_stroke(INK_SOFT, width=2)
            t = serif(name, 30).move_to(b.get_center() + UP * 0.3)
            m = mark.copy().move_to(b.get_center() + DOWN * 0.33)
            return VGroup(b, t, m)

        s1, s2, s3 = stage("audio", tick()), stage("animation", tick()), stage("review", cross())
        fit(s2[1], 1.6)
        row = VGroup(s1, s2, s3).arrange(RIGHT, buff=0.26).move_to([3.15, 1.65, 0])
        arrows = VGroup(*[Arrow(a.get_right(), b.get_left(), buff=0.04, color=INK_SOFT,
                                stroke_width=3, max_tip_length_to_length_ratio=0.35)
                          for a, b in ((s1, s2), (s2, s3))])
        s3[0].set_stroke(SPARK, width=4)

        def problem(text):
            t = fit(serif(text, 36), 5.0)
            bar = Line(UP * 0.3, DOWN * 0.3, color=SPARK, stroke_width=8)
            return VGroup(bar, t).arrange(RIGHT, buff=0.3)

        p1 = problem("packages wanting an older Python").move_to([3.15, -0.05, 0]).align_to(row, LEFT)
        p2 = problem("gate checks halting the build").move_to([3.15, -1.2, 0]).align_to(row, LEFT)
        link = VGroup(Line(s3.get_bottom(), [s3.get_x(), p1.get_top()[1], 0], color=SPARK, stroke_width=4))

        self.run(FadeIn(shot), FadeIn(row), FadeIn(arrows), rt=0.8)
        self.at(2.6)   # "Some packages needed an older Python..."
        self.run(Create(link), FadeIn(p1, shift=DOWN * 0.3), rt=0.6)
        self.at(7.3)   # "...stopping at its gates"
        self.run(FadeIn(p2, shift=DOWN * 0.3), rt=0.6)

        hours = serif("hours of patching symptoms", 32, INK_SOFT).move_to([3.15, -2.4, 0])
        self.at(12.6)  # "I spent hours patching symptoms."
        self.run(FadeIn(hours), rt=0.5)
        self.at(15.0)  # "Eventually I deleted the old install..."
        everything = Group(shot, row, arrows, link, p1, p2, hours)
        self.run(FadeOut(everything), rt=1.2)
        restart = serif("start over.", 64).move_to(ORIGIN)
        self.run(FadeIn(restart), rt=0.5)
        self.at(18.20)


# ── B04 — second attempt: the false alarm (18.24 s) ─────────────────────────

class B04_FalseAlarm(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("Second attempt.")), rt=0.4)

        clone = terminal_line("$ git clone https://github.com/nikbearbrown/brutalist.art.git", 30)
        clone.move_to([0, 2.05, 0])
        self.at(1.0)   # "a clean copy"
        self.run(FadeIn(clone, shift=DOWN * 0.2), rt=0.6)

        guard = terminal_line("$ ./setup → ElevenLabs reference found — this toolkit is Kokoro-only", 28, 11.4)
        x = cross().next_to(guard, RIGHT, buff=0.25)
        VGroup(guard, x).move_to([0, 0.85, 0])
        self.at(7.6)   # "The setup check stopped at once"
        self.run(FadeIn(guard), Create(x), rt=0.6)

        box = card(5.2, 2.5).set_fill(PAGE).move_to([-3.0, -2.0, 0])
        blabel = mono("brutalist/", 30).move_to(box.get_top() + DOWN * 0.4).align_to(box, LEFT).shift(RIGHT * 0.3)
        subs = VGroup(mono("runtime/", 26, INK_SOFT), mono("skills/", 26, INK_SOFT),
                      mono("youtube/brutalist/", 26)).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        subs.next_to(blabel, DOWN, buff=0.25).align_to(blabel, LEFT).shift(RIGHT * 0.35)
        hl = SurroundingRectangle(subs[2], buff=0.1, color=SPARK, stroke_width=4)
        note = serif("videos about the check itself", 34, INK_SOFT).next_to(box, RIGHT, buff=0.6)

        self.at(11.0)  # "It was a false alarm"
        self.run(FadeIn(box), FadeIn(blabel), FadeIn(subs), rt=0.6)
        self.run(Create(hl), FadeIn(note), rt=0.5)

        dest = card(4.2, 1.0).set_fill(PAGE).move_to([3.4, -2.75, 0])
        dlabel = mono("brutalist-vids/", 28, INK_SOFT).move_to(dest)
        ok = VGroup(serif("check:", 36), serif("clean", 36), tick()).arrange(RIGHT, buff=0.2)
        ok.next_to(guard, DOWN, buff=0.25).align_to(guard, RIGHT)

        self.at(15.9)  # "Moved out, the check passed."
        self.run(FadeOut(note), FadeIn(dest), FadeIn(dlabel), rt=0.4)
        moving = VGroup(subs[2], hl)
        self.run(moving.animate.move_to(dest.get_center() + UP * 0.95), rt=0.8)
        self.run(FadeOut(x), guard.animate.set_opacity(0.4), FadeIn(ok), rt=0.5)
        self.at(18.24)


# ── B05 — the Python fix (17.96 s) ──────────────────────────────────────────

class B05_PythonFix(Scene):
    setup = _setup
    at = _at
    run = _run

    def construct(self):
        self.run(FadeIn(spark_line("One fix for both.")), rt=0.4)

        versions = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]
        x0, dx, y = -4.6, 1.84, 1.75
        axis = Line([x0 - 0.4, y, 0], [x0 + dx * 5 + 0.4, y, 0], color=INK, stroke_width=3)
        ticks = VGroup(*[Line([x0 + dx * i, y - 0.12, 0], [x0 + dx * i, y + 0.12, 0],
                              color=INK, stroke_width=3) for i in range(6)])
        labels = VGroup(*[mono(v, 28).move_to([x0 + dx * i, y - 0.45, 0]) for i, v in enumerate(versions)])
        band = Rectangle(width=dx * 3 + 0.5, height=0.42).set_fill(OK, opacity=0.18).set_stroke(width=0)
        band.move_to([x0 + dx * 1.5, y, 0])
        blabel = mono("manim 0.18 requires Python >=3.9, <3.13", 26, INK_SOFT).next_to(labels, DOWN, buff=0.22)
        blabel.align_to(band, LEFT)

        def marker(i, color, text):
            p = Triangle(fill_color=color, fill_opacity=1, stroke_width=0).scale(0.2).rotate(PI)
            p.move_to([x0 + dx * i, y + 0.42, 0])
            return VGroup(p, serif(text, 30).next_to(p, UP, buff=0.12))

        m314 = marker(5, SPARK, "mine")
        m312 = marker(3, OK, "the fix")

        self.at(1.2)   # "...came back. My Python was too new"
        self.run(Create(axis), FadeIn(ticks), FadeIn(labels), FadeIn(band), FadeIn(blabel), rt=0.8)
        self.at(3.4)
        self.run(FadeIn(m314, shift=DOWN * 0.3), rt=0.5)

        msg = terminal_line("$ python3   Python was not found; run without arguments to install from the Microsoft Store…", 25)
        msg.move_to([0, -0.05, 0])
        self.at(6.4)   # "...couldn't even find it by name"
        self.run(FadeIn(msg), rt=0.5)

        cmds = VGroup(
            terminal_line("$ py -3.12 -m venv .venv", 28, 9.4),
            terminal_line("$ cp .venv/Scripts/python.exe .venv/Scripts/python3.exe", 28, 9.4),
            terminal_line("$ ./setup --install", 28, 9.4),
        ).arrange(DOWN, buff=0.15).move_to([-0.6, -2.0, 0])
        for c in cmds:
            c.set_opacity(0)

        self.at(10.4)  # "One fix covered both"
        self.run(msg.animate.set_opacity(0.4), rt=0.3)
        self.at(11.6)  # "a separate Python three point twelve environment"
        self.run(FadeIn(m312, shift=DOWN * 0.3), cmds[0].animate.set_opacity(1), rt=0.6)
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
            "audio (Kokoro Bella/Onyx)",
            "captions + word clock",
            "Manim beats",
            "Manim equation beats",
            "Remotion beats + bookends",
            "slates / previz / compile",
            "fonts (EB Garamond + Oswald)",
        ]
        top, step, xl, xr = 2.3, 0.64, -5.4, 2.2
        head = VGroup(mono("FEATURE", 28, INK_SOFT).move_to([xl, top, 0], aligned_edge=LEFT),
                      mono("STATUS", 28, INK_SOFT).move_to([xr, top, 0], aligned_edge=LEFT))
        rule = Line([xl, top - 0.32, 0], [5.6, top - 0.32, 0], color=INK_SOFT, stroke_width=2)
        names = VGroup(*[mono(r, 32).move_to([xl, top - step * (i + 1), 0], aligned_edge=LEFT)
                         for i, r in enumerate(rows)])
        status = []
        for i, r in enumerate(rows):
            yy = top - step * (i + 1)
            if i == 3:
                g = VGroup(cross(s=0.26), mono("blocked", 32)).arrange(RIGHT, buff=0.25)
            else:
                g = VGroup(tick(s=0.28), mono("ready", 32)).arrange(RIGHT, buff=0.25)
            status.append(g.move_to([xr, yy, 0], aligned_edge=LEFT))

        self.at(0.6)   # "Then the check that matters."
        self.run(FadeIn(head), Create(rule), FadeIn(names, lag_ratio=0.08), rt=0.9)
        self.at(2.4)   # "Voice: ready."
        self.run(FadeIn(status[0]), rt=0.4)
        for i, t in zip((1, 2, 4, 5, 6), (3.4, 4.1, 4.8, 5.6, 6.3)):
            self.at(t)  # "Captions, animation, scenes, compiling: ready."
            self.run(FadeIn(status[i]), rt=0.35)
        self.at(7.9)   # "One row stays blocked: equations need LaTeX."
        hl = SurroundingRectangle(VGroup(names[3], status[3]), buff=0.12, color=SPARK, stroke_width=4)
        self.run(FadeIn(status[3]), Create(hl), rt=0.5)
        tag = serif("needs LaTeX · not needed for this video", 30, INK_SOFT)
        tag.next_to(names[-1], DOWN, buff=0.4).align_to(names, LEFT)
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
        title = serif("Brutalist, Installed", 120)
        dot = Dot(radius=0.11, color=SPARK)
        grp = VGroup(title, dot).arrange(RIGHT, buff=0.06, aligned_edge=DOWN).move_to([0, 0.75, 0])
        dot.shift(UP * 0.12)
        sub = serif("Made with this install.", 44, INK_SOFT).next_to(grp, UP, buff=0.6)
        self.run(Write(title), FadeIn(sub), rt=1.0)
        self.run(FadeIn(dot, scale=1.6), rt=0.3)
        rule = Line(title.get_left() + DOWN * 0.95, title.get_right() + DOWN * 0.95,
                    color=SPARK, stroke_width=4).shift(UP * 0.2)
        self.run(Create(rule), rt=0.5)

        mark = wordmark(0.6).move_to([0, -1.55, 0])
        handle = serif("@HumanitariansAI", 50).next_to(mark, DOWN, buff=0.35)
        self.at(3.4)   # "...works as expected." — the mark is up before the title is read
        self.run(FadeIn(mark), FadeIn(handle), rt=0.6)
        self.at(8.06)
