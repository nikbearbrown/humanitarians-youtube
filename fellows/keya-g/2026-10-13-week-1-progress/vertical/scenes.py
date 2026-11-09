"""Native 9:16 layouts for "Week 1 Progress" (Keya G.).

Same scene names, content, colours and go() cues as ../scenes.py, rearranged for a tall
frame (4.5 x 8 Manim units at 2160x3840). Nothing here is a crop of the landscape film.


B01_Background    degree card, then an automation developer's tools as generic icons
B02_StateMachine  a generic five-state review lifecycle: step through, undo, self-approval blocked
B03_WeekOne       a week strip: joined, Monday and Thursday meetups, fellows website, film as code
B04_Workflow      this film's own beat-sheet lines, narration waveform, animation bars, three checks
B05_FirstVideo    key drawings and in-betweens, then the week's issues worked through
B06_Bridge        a bridge between two banks; footsteps crossing; keep learning

Simple drawn shapes only: no photos, no person icons, no company or tool logos.
Each scene's length comes from actual_duration_s in beat_sheet.json. The times passed
to go() are word timings measured from the beat's narration audio (faster-whisper), so
re-check them if that audio is regenerated.
"""
import json
import math
import subprocess
from pathlib import Path

import numpy as np
from manim import *

# Portrait sync: Manim CE takes pixel dims from -r W,H but leaves frame_width at the
# 16:9 default (14.22); make it 4.5 so the frame is 4.5 x 8 units.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

HERE = Path(__file__).resolve().parent
# beat_sheet.json is the master clock. The fallback is its measured values, for run.sh's
# Gate A, which checks a copy of this file in a folder without the sheet.
DUR = {"B01": 13.97, "B02": 15.96, "B03": 11.16, "B04": 14.4, "B05": 15.38, "B06": 7.81}
SHEET = {}
if (HERE / "beat_sheet.json").is_file():
    SHEET = json.loads((HERE / "beat_sheet.json").read_text())
    DUR = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}

# humanitarians palette: runtime/remotion/src/tokens/humanitarians.ts
CREAM = "#F3EBDD"
INK = "#2F2A26"
TEAL = "#1F4E5F"     # good / done / kept
CRIMSON = "#E4572E"  # problem / blocked
SLATE = "#29335C"    # structure
GOLD = "#F3A712"     # fill only, never text or fine marks
SAGE = "#A8C686"     # fill only

# Just inside the portrait safe band Gate B enforces (1.95 x 3.4). Gate T also keeps the
# bottom 14% of a phone frame clear, so nothing sits below FLOOR.
SAFE_X, SAFE_Y = 1.85, 3.3
FLOOR = -2.85
WIDE = SAFE_X * 2


def T(text, size=48, color=INK, **kw):
    return Text(text, font="EB Garamond", font_size=size, color=color, **kw)


def fit(mob, max_w):
    """Shrink (never grow) a label so it is at most max_w units wide."""
    if mob.width > max_w:
        mob.scale(max_w / mob.width)
    return mob


def M(text, size=30, color=INK):
    return Text(text, font="Menlo", font_size=size, color=color)


def centred(lines, size, color=INK, buff=.28):
    return VGroup(*[T(line, size, color) for line in lines]).arrange(DOWN, buff=buff)


class Timed:
    """Narration-clock helpers: go(t, ...) starts animations at t seconds."""

    def setup(self):
        self.camera.background_color = CREAM
        self._reported = set()

    @property
    def now(self):
        return self.renderer.time

    def go(self, t, *anims, rt=0.5):
        """rt=None lets each animation keep its own run_time."""
        gap = t - self.now
        if gap > 1e-3:
            self.wait(gap)
        elif gap < -0.05:
            print(f"QC {self.BEAT}: cue {t}s is late by {-gap:.2f}s")
        self._audit(t)
        if anims:
            self.play(*anims, **({} if rt is None else {"run_time": rt}))

    def finish(self):
        self._audit(self.now)
        gap = DUR[self.BEAT] - self.now
        if gap > 1e-3:
            self.wait(gap)

    def _audit(self, t):
        """Log text outside the safe area or colliding with other text."""
        if not hasattr(self, "get_mobject_family_members"):  # Gate A's stand-in for Manim
            return
        texts = [m for m in self.get_mobject_family_members()
                 if isinstance(m, Text) and m.get_fill_opacity() > 0.05]
        for m in texts:
            box = (m.get_left()[0], m.get_right()[0], m.get_bottom()[1], m.get_top()[1])
            if box[0] < -SAFE_X - .01 or box[1] > SAFE_X + .01 or box[2] < FLOOR - .01 or box[3] > SAFE_Y + .01:
                self._say(f"t={t}: '{m.text}' leaves the safe area {tuple(round(v, 2) for v in box)}")
        for i, a in enumerate(texts):
            for b in texts[i + 1:]:
                if (a.get_left()[0] < b.get_right()[0] and b.get_left()[0] < a.get_right()[0]
                        and a.get_bottom()[1] < b.get_top()[1] and b.get_bottom()[1] < a.get_top()[1]):
                    self._say(f"t={t}: '{a.text}' overlaps '{b.text}'")

    def _say(self, msg):
        if msg not in self._reported:
            self._reported.add(msg)
            print(f"QC {self.BEAT}: {msg}")


def timed(beat):
    """Give a scene the Timed helpers. Each scene stays `class Name(Scene)` because
    run.sh finds scenes by that exact text, so it would miss a Scene subclass."""
    def wrap(cls):
        for name, value in vars(Timed).items():
            if not name.startswith("__"):
                setattr(cls, name, value)
        cls.BEAT = beat
        return cls
    return wrap


# ---- generic drawn icons (never a company or tool logo) ---------------------------

def box(x, y, w, h, stroke=INK, width=3, fill=CREAM, fill_opacity=1):
    return RoundedRectangle(corner_radius=.14, width=w, height=h, stroke_color=stroke,
                            stroke_width=width, fill_color=fill,
                            fill_opacity=fill_opacity).move_to([x, y, 0])


def check(at, size=.5, color=TEAL):
    at = np.array(at, dtype=float)
    pts = [at + np.array([-.5, 0, 0]) * size, at + np.array([-.1, -.45, 0]) * size,
           at + np.array([.6, .55, 0]) * size]
    return VMobject(stroke_color=color, stroke_width=10).set_points_as_corners(pts)


def cross(at, size=.5, color=CRIMSON):
    at = np.array(at, dtype=float)
    d = size * .5
    return VGroup(Line(at + [-d, -d, 0], at + [d, d, 0], stroke_color=color, stroke_width=12),
                  Line(at + [-d, d, 0], at + [d, -d, 0], stroke_color=color, stroke_width=12))


def code_icon(x, y, s=1.0, color=SLATE):
    """< / > drawn as strokes."""
    w = 8 * s
    left = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[-.25, .4, 0], [-.65, 0, 0], [-.25, -.4, 0]])
    right = VMobject(stroke_color=color, stroke_width=w).set_points_as_corners(
        [[.25, .4, 0], [.65, 0, 0], [.25, -.4, 0]])
    slash = Line([.12, .45, 0], [-.12, -.45, 0], stroke_color=color, stroke_width=w)
    return VGroup(left, slash, right).scale(s).move_to([x, y, 0])


def cloud_icon(x, y, s=1.0, color=SLATE):
    parts = [Circle(radius=r, fill_color=color, fill_opacity=1, stroke_width=0).move_to(p)
             for r, p in ((.32, [-.38, -.05, 0]), (.42, [.05, .12, 0]), (.3, [.45, -.08, 0]))]
    base = RoundedRectangle(corner_radius=.18, width=1.3, height=.42, fill_color=color,
                            fill_opacity=1, stroke_width=0).move_to([.03, -.2, 0])
    return VGroup(*parts, base).scale(s).move_to([x, y, 0])


def database_icon(x, y, s=1.0, color=SLATE):
    body = Rectangle(width=1.0, height=.9, fill_color=color, fill_opacity=1, stroke_width=0)
    bottom = Ellipse(width=1.0, height=.32, fill_color=color, fill_opacity=1,
                     stroke_width=0).move_to([0, -.45, 0])
    top = Ellipse(width=1.0, height=.32, fill_color=SAGE, fill_opacity=1, stroke_color=color,
                  stroke_width=4).move_to([0, .45, 0])
    bands = VGroup(*[Arc(radius=.5, start_angle=PI, angle=PI, stroke_color=CREAM, stroke_width=4)
                     .stretch(.32, 1).move_to([0, yy - .08, 0]) for yy in (.15, -.15)])
    return VGroup(body, bottom, bands, top).scale(s).move_to([x, y, 0])


def browser_icon(x, y, w=1.3, h=1.0, color=SLATE, cursor=True):
    frame = RoundedRectangle(corner_radius=.08, width=w, height=h, stroke_color=color,
                             stroke_width=5, fill_color=CREAM, fill_opacity=1)
    bar = Rectangle(width=w, height=h * .2, fill_color=color, fill_opacity=1,
                    stroke_width=0).move_to([0, h / 2 - h * .1, 0])
    dots = VGroup(*[Dot(radius=h * .035, color=CREAM).move_to([-w / 2 + h * .1 + i * h * .1, h / 2 - h * .1, 0])
                    for i in range(3)])
    lines = VGroup(*[Line([-w * .36, yy, 0], [w * (.36 - .12 * i), yy, 0], stroke_color=SAGE,
                          stroke_width=6) for i, yy in enumerate([h * .12, -h * .08, -h * .28])])
    g = VGroup(frame, bar, dots, lines)
    if cursor:
        g.add(Polygon([0, 0, 0], [0, -h * .3, 0], [h * .09, -h * .22, 0], [h * .2, -h * .2, 0],
                      fill_color=INK, fill_opacity=1, stroke_color=CREAM, stroke_width=2)
              .move_to([w * .25, -h * .2, 0]))
    return g.move_to([x, y, 0])


def checklist_icon(x, y, s=1.0, color=SLATE):
    page = RoundedRectangle(corner_radius=.08, width=1.0, height=1.2, stroke_color=color,
                            stroke_width=5, fill_color=CREAM, fill_opacity=1)
    rows = VGroup()
    for i, yy in enumerate((.3, 0, -.3)):
        rows.add(check([-.25, yy, 0], .28, TEAL),
                 Line([0, yy, 0], [.32, yy, 0], stroke_color=color, stroke_width=6))
    return VGroup(page, rows).scale(s).move_to([x, y, 0])


def film_icon(x, y, w=2.6, h=1.4, color=SLATE):
    strip = Rectangle(width=w, height=h, fill_color=color, fill_opacity=1, stroke_width=0)
    holes = VGroup(*[RoundedRectangle(corner_radius=.03, width=.14, height=.12, fill_color=CREAM,
                                      fill_opacity=1, stroke_width=0).move_to([-w / 2 + .2 + i * (w - .4) / 7, yy, 0])
                     for i in range(8) for yy in (h / 2 - .14, -h / 2 + .14)])
    frames = VGroup(*[Rectangle(width=(w - .5) / 3 - .1, height=h - .65, fill_color=SAGE, fill_opacity=1,
                                stroke_width=0).move_to([-w / 2 + .25 + (w - .5) / 6 + i * (w - .5) / 3, 0, 0])
                      for i in range(3)])
    return VGroup(strip, holes, frames).move_to([x, y, 0])


def play_icon(x, y, s=1.0, color=TEAL):
    return Triangle(fill_color=color, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(.45 * s).move_to([x, y, 0])


def star(color=SLATE, scale=1.0, opacity=1.0):
    """The first video's abstract 'drawing': a plain star, so it can never read as a person."""
    return Star(n=5, outer_radius=.5, inner_radius=.22, fill_color=color, fill_opacity=opacity,
                stroke_width=0).scale(scale)


# ---- scenes (portrait) -------------------------------------------------------------

@timed("B01")
class B01_Background(Scene):
    def construct(self):
        # A degree card, drawn: Master's in Software Engineering Systems.
        card = box(0, 1.2, 3.7, 2.7, stroke=SLATE, width=5)
        seal = VGroup(Circle(radius=.26, fill_color=GOLD, fill_opacity=1, stroke_width=0),
                      Circle(radius=.18, stroke_color=CREAM, stroke_width=4)).move_to([1.47, .0, 0])
        masters = T("Master's", 70, SLATE).move_to([0, 2.05, 0])
        # Three short lines, so the type stays above Gate T's phone floor once the card shrinks.
        field = centred(["Software", "Engineering", "Systems"], 46, buff=.06).move_to([0, .8, 0])
        self.go(.1, FadeIn(card), rt=.4)
        self.go(1.4, FadeIn(masters, shift=UP * .1), FadeIn(seal, scale=.6), rt=.5)
        self.go(2.08, FadeIn(field, shift=UP * .1), rt=.6)
        degree = VGroup(card, seal, masters, field)

        # Work: an automation developer, and the tools as generic icons, one per row.
        ys = [.3, -.42, -1.14, -1.86, -2.5]
        slots = VGroup(*[DashedVMobject(box(0, y, 3.65, .62, stroke=INK, width=3, fill_opacity=0), num_dashes=36)
                         for y in ys])
        self.go(4.38, degree.animate.scale(.72).move_to([0, 2.31, 0]), Create(slots), rt=.7)
        role = fit(T("automation developer", 50), 3.6).move_to([0, 1.02, 0])
        self.go(6.94, FadeIn(role, shift=UP * .1), rt=.5)
        ix, lx = -1.2, -.55
        icons = [code_icon(ix, ys[0], .7), cloud_icon(ix, ys[1], .68), database_icon(ix, ys[2], .55),
                 browser_icon(ix, ys[3], .82, .5), checklist_icon(ix, ys[4], .44)]
        names = ["code", "cloud", "database", "browser tests", "unit tests"]
        labels = []
        for n, y in zip(names, ys):
            lbl = fit(T(n, 38), 2.4)
            labels.append(lbl.move_to([lx + lbl.width / 2, y, 0]))
        # Java, Python, AWS, SQL, Selenium, JUnit: each icon lands on its spoken name.
        self.go(8.54, FadeIn(icons[0], scale=.7), FadeIn(labels[0]), slots[0].animate.set_stroke(SLATE), rt=.45)
        self.go(9.42, Indicate(icons[0], color=TEAL, scale_factor=1.12), rt=.5)
        for i, t in enumerate([10.3, 11.48, 12.38, 13.2], start=1):
            self.go(t, FadeIn(icons[i], scale=.7), FadeIn(labels[i]), slots[i].animate.set_stroke(SLATE), rt=.45)
        self.finish()


@timed("B02")
class B02_StateMachine(Scene):
    def construct(self):
        title = T("VeriCode", 62, SLATE).move_to([0, 2.92, 0])
        sub = fit(centred(["collaborative", "code review"], 40, buff=.06), 3.6).move_to([0, 2.05, 0])
        self.go(1.8, FadeIn(title, shift=UP * .1))
        self.go(3.14, FadeIn(sub))

        # Five generic states, numbered, top to bottom: the real names are not shown.
        sub2 = fit(centred(["the review", "lifecycle"], 40, TEAL, buff=.06), 3.6).move_to([0, 2.05, 0])
        cx = -1.3
        ys = [.95, .2, -.55, -1.3, -2.05]
        rings = VGroup(*[Circle(radius=.3, stroke_color=SLATE, stroke_width=5, fill_color=CREAM,
                                fill_opacity=1).move_to([cx, y, 0]) for y in ys])
        nums = VGroup(*[T(str(i + 1), 40, SLATE).move_to([cx, y, 0]) for i, y in enumerate(ys)])
        links = VGroup(*[Arrow([cx, ys[i] - .3, 0], [cx, ys[i + 1] + .3, 0], buff=0, stroke_width=5,
                               color=INK, max_tip_length_to_length_ratio=.35) for i in range(4)])
        self.go(6.3, FadeOut(sub), FadeIn(sub2),
                LaggedStart(*[GrowFromCenter(r) for r in rings], lag_ratio=.15), FadeIn(nums), rt=.8)
        self.go(7.88, Create(links), rt=.6)

        tag = centred(["pull", "request"], 34, TEAL, buff=.0)

        def tag_at(i):
            return [cx + .45 + tag.width / 2, ys[i], 0]
        tag.move_to(tag_at(0))
        self.go(9.24, rings[0].animate.set_fill(TEAL, 1), nums[0].animate.set_color(CREAM),
                FadeIn(tag), rt=.4)
        for i, t in zip(range(1, 5), (10.0, 10.4, 10.8, 11.2)):
            self.go(t, rings[i - 1].animate.set_fill(CREAM, 1), nums[i - 1].animate.set_color(SLATE),
                    rings[i].animate.set_fill(TEAL, 1), nums[i].animate.set_color(CREAM),
                    tag.animate.move_to(tag_at(i)), rt=.3)

        # Undo: one state back (the arrow runs up the left side).
        undo = CurvedArrow([cx - .3, ys[4], 0], [cx - .3, ys[3], 0], angle=-TAU / 4,
                           color=TEAL, stroke_width=5)
        undo_lbl = T("undo", 34, TEAL)
        undo_lbl.move_to([SAFE_X - .05 - undo_lbl.width / 2, (ys[3] + ys[4]) / 2, 0])
        self.go(11.68, Create(undo), FadeIn(undo_lbl), rt=.4)
        self.go(12.1, rings[4].animate.set_fill(CREAM, 1), nums[4].animate.set_color(SLATE),
                rings[3].animate.set_fill(TEAL, 1), nums[3].animate.set_color(CREAM),
                tag.animate.move_to(tag_at(3)), rt=.4)

        # The rule: an author can't approve their own code (beside the column).
        sub3 = fit(centred(["a rule: authors can't", "approve their own code"], 40, CRIMSON, buff=.06), 3.6).move_to([0, 2.05, 0])
        bx = .75
        author = VGroup(box(bx, .95, 2.1, .62, stroke=SLATE, width=5), T("author", 40).move_to([bx, .95, 0]))
        approve = VGroup(box(bx, -.35, 2.1, .62, stroke=SLATE, width=5), T("approve", 40).move_to([bx, -.35, 0]))
        self.go(12.9, FadeOut(sub2), FadeIn(sub3), FadeIn(author), FadeIn(approve), rt=.45)
        reach = Arrow([bx, .63, 0], [bx, -.03, 0], buff=0, stroke_width=6, color=INK)
        self.go(13.86, GrowArrow(reach), rt=.4)
        self.go(14.32, reach.animate.set_color(CRIMSON), FadeIn(cross([bx, .3, 0], .34), scale=1.3), rt=.35)
        self.finish()


@timed("B03")
class B03_WeekOne(Scene):
    def construct(self):
        title = T("Week 1", 68, SLATE).move_to([0, 2.9, 0])
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        cx, step, top = -1.4, .44, 2.1
        ys = [top - i * step for i in range(7)]
        cells = VGroup(*[box(cx, y, .88, .38, stroke=SLATE, width=4) for y in ys])
        names = VGroup(*[T(d, 30, SLATE).move_to([cx, y, 0]) for d, y in zip(days, ys)])
        self.go(.1, FadeIn(title), FadeIn(cells), FadeIn(names), rt=.45)

        # Joined, at the start of the week.
        lx = -.72
        joined = T("joined", 34, TEAL)
        joined.move_to([lx + joined.width / 2, ys[0], 0])
        flag = Triangle(fill_color=GOLD, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(.12) \
            .move_to([lx - .12, ys[0], 0])
        self.go(.56, FadeIn(flag), FadeIn(joined), rt=.4)

        # The Monday and Thursday meetups.
        # Too narrow on a phone for two labels side by side: Monday's label grows instead.
        m1 = fit(T("joined, meetup", 34, TEAL), SAFE_X - lx - .05)
        m1.move_to([lx + m1.width / 2, ys[0], 0])
        m2 = T("meetup", 34, TEAL)
        m2.move_to([lx + m2.width / 2, ys[3], 0])
        self.go(3.0, cells[0].animate.set_fill(TEAL, 1), names[0].animate.set_color(CREAM), FadeOut(joined), FadeIn(m1), rt=.35)
        self.go(3.56, cells[3].animate.set_fill(TEAL, 1), names[3].animate.set_color(CREAM), FadeIn(m2), rt=.35)

        # The fellows website.
        site = browser_icon(-1.05, -1.35, 1.45, .9, cursor=False)
        site_lbl = centred(["fellows", "website"], 38, buff=.06).move_to([-1.05, -2.35, 0])
        self.go(4.96, FadeIn(site, scale=.8), FadeIn(site_lbl), rt=.5)

        # AI coding, with Brutalist: film as code.
        film = film_icon(.58, -1.35, .85, .7)
        code = code_icon(1.45, -1.35, .5, TEAL)
        ai_lbl = centred(["AI", "coding"], 38, buff=.06).move_to([1.0, -2.35, 0])
        self.go(7.26, FadeIn(code, scale=.7), FadeIn(ai_lbl), rt=.45)
        fac_lbl = centred(["film as", "code"], 38, TEAL, buff=.06).move_to([1.0, -2.35, 0])
        self.go(8.98, FadeIn(film, shift=RIGHT * .2), rt=.5)
        self.go(9.56, FadeOut(ai_lbl), FadeIn(fac_lbl), rt=.45)
        self.finish()


def _b04_excerpt():
    """Real lines from this film's beat_sheet.json (B04's own entry), short enough for a phone."""
    b = next((b for b in SHEET.get("beats", []) if b["beat_id"] == "B04"), None)
    bid = b["beat_id"] if b else "B04"
    first = b["narration_text"].split()[0] if b else "Brutalist"
    dur = b["actual_duration_s"] if b else DUR["B04"]
    return [f'"beat_id": "{bid}",', '"narration_text":', f'  "{first}…",', '"actual_duration_s":', f'  {dur}']


def _envelope(n=60):
    """RMS envelope of this beat's real narration MP3 (empty if the file is absent)."""
    mp3 = HERE / "mp3" / "beat-B04.mp3"
    if not mp3.is_file():
        return np.zeros(n)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(mp3), "-f", "f32le", "-ac", "1",
                          "-ar", "8000", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32)
    chunks = np.array_split(x, n)
    env = np.array([math.sqrt(float(np.mean(c ** 2))) if len(c) else 0 for c in chunks])
    return env / (env.max() or 1)


@timed("B04")
class B04_Workflow(Scene):
    def construct(self):
        # Code becomes video.
        code = code_icon(-1.0, 3.0, .6, SLATE)
        to = Arrow([-.45, 3.0, 0], [.45, 3.0, 0], buff=0, stroke_width=6, color=INK)
        play = VGroup(Circle(radius=.28, stroke_color=TEAL, stroke_width=6), play_icon(.04, 0, .42)).move_to([1.0, 3.0, 0])
        self.go(.1, FadeIn(code, scale=.7), rt=.4)
        self.go(1.02, GrowArrow(to), FadeIn(play, scale=.7), rt=.45)

        # A beat sheet: real lines from this film's beat_sheet.json.
        head = T("beat_sheet.json", 42, SLATE).move_to([0, 2.38, 0])
        card = box(0, 1.25, 3.7, 1.75, stroke=SLATE, width=5)
        lines = VGroup(*[M(s, 30) for s in _b04_excerpt()]).arrange(DOWN, aligned_edge=LEFT, buff=.1)
        fit(lines, 3.35).move_to([0, 1.25, 0])
        self.go(2.62, FadeIn(card), FadeIn(head), rt=.4)
        self.go(3.0, LaggedStart(*[FadeIn(l, shift=RIGHT * .1) for l in lines], lag_ratio=.25), rt=1.0)

        # The narration first: its real waveform and measured length.
        x0, x1, wy = -1.75, 1.75, -.85
        env = _envelope()
        n = len(env)
        bars = VGroup(*[Line([x0 + (x1 - x0) * (i + .5) / n, wy - .05 - .35 * v, 0],
                             [x0 + (x1 - x0) * (i + .5) / n, wy + .05 + .35 * v, 0],
                             stroke_color=TEAL, stroke_width=5) for i, v in enumerate(env)])
        wlabel = fit(T(f"narration · {DUR['B04']:g} s", 38, TEAL), 3.5).move_to([0, -.25, 0])
        self.go(5.18, FadeIn(wlabel), Create(bars, lag_ratio=.02), rt=1.0)

        # Its timing drives every animation: the bars stretch to the narration's end.
        end = DashedLine([x1, wy + .4, 0], [x1, -1.86, 0], stroke_color=INK, stroke_width=4)
        anims = VGroup(*[RoundedRectangle(corner_radius=.07, width=x1 - x0, height=.16, fill_color=c,
                                          fill_opacity=1, stroke_width=0).move_to([(x0 + x1) / 2, y, 0])
                         for c, y in ((SLATE, -1.38), (SAGE, -1.58), (GOLD, -1.78))])
        starts = [a.copy().stretch(.25, 0).align_to(a, LEFT) for a in anims]
        self.go(7.3, Create(end), *[FadeIn(s) for s in starts], rt=.4)
        self.go(7.8, *[Transform(s, a) for s, a in zip(starts, anims)], rt=.9)

        # Quality checks: layout, text, facts, then final (two rows on a phone).
        items = [("layout", -1.15, -2.14, 11.02), ("text", .95, -2.14, 11.96), ("facts", -1.15, -2.64, 12.5)]
        ticks, rows = [], VGroup()
        for word, x, y, _ in items:
            sq = Square(side_length=.32, stroke_color=SLATE, stroke_width=5).move_to([x - .45, y, 0])
            lbl = T(word, 36).next_to(sq, RIGHT, buff=.14)
            rows.add(sq, lbl)
            ticks.append(check(np.array(sq.get_center(), dtype=float) + [.04, .02, 0], .34))
        self.go(10.0, FadeIn(rows), rt=.4)
        for tick, (_, _, _, t) in zip(ticks, items):
            self.go(t, Create(tick), rt=.3)
        final = VGroup(box(1.05, -2.64, 1.4, .44, stroke=TEAL, width=0, fill=TEAL), T("final", 38, CREAM).move_to([1.05, -2.64, 0]))
        self.go(13.84, FadeIn(final, scale=.8), rt=.4)
        self.finish()


@timed("B05")
class B05_FirstVideo(Scene):
    def construct(self):
        title = fit(centred(["How AI Draws", "Anime Frames"], 52, SLATE, buff=.04), 3.6).move_to([0, 2.75, 0])
        self.go(.14, FadeIn(title), rt=.45)
        w, gap, sy = .64, .1, .55
        xs = [(i - 2) * (w + gap) for i in range(5)]
        slots = VGroup(*[DashedVMobject(box(x, sy, w, 1.9, stroke=INK, width=3, fill_opacity=0), num_dashes=22)
                         for x in xs])
        keys = VGroup(star(SLATE, .66).move_to([xs[0], sy, 0]), star(SLATE, .66).move_to([xs[-1], sy, 0]))
        self.go(1.22, Create(slots), FadeIn(keys), rt=.7)
        fills = VGroup(*[star(TEAL, .66).move_to([x, sy, 0]) for x in xs[1:-1]])
        self.go(3.22, LaggedStart(*[FadeIn(f, scale=.7) for f in fills], lag_ratio=.4), rt=1.1)

        # Why anime is hard for it: one in-between ghosts.
        hard = fit(centred(["and why anime", "is hard for AI"], 48, CRIMSON, buff=.06), 3.55).move_to([0, -1.35, 0])
        # Two offset solid stars read as a doubled frame; a pale ghost fails Gate T contrast at phone size.
        ghost = VGroup(star(CRIMSON, .66).move_to([xs[2] - .07, sy + .05, 0]),
                       star(CRIMSON, .66).move_to([xs[2] + .07, sy - .05, 0]))
        self.go(5.48, FadeIn(hard), FadeOut(fills[1]), FadeIn(ghost), rt=.5)

        # "I was completely new...": the first video moves up to make room for the week's issues.
        first = VGroup(title, slots, keys, fills, ghost, hard)
        self.go(7.92, first.animate.scale(.7).move_to([0, 1.4, 0]), rt=.6)
        new = fit(T("new to AI coding", 50), 3.6).move_to([0, -.82, 0])
        self.go(8.6, FadeIn(new, shift=UP * .1), rt=.45)
        issues = ["pronunciation", "quality gates", "portrait layout"]
        ys = [-1.42, -1.99, -2.56]
        cards = []
        for t, y, s in zip((10.64, 11.3, 11.86), ys, issues):
            c = VGroup(box(-.2, y, 3.05, .5, stroke=CRIMSON, width=5), fit(T(s, 40), 2.7).move_to([-.2, y, 0]))
            cards.append(c)
            self.go(t, FadeIn(c, shift=UP * .15), rt=.35)
        for t, c, y in zip((14.08, 14.5, 14.86), cards, ys):
            self.go(t, c[0].animate.set_stroke(TEAL), Create(check([1.62, y, 0], .36)), rt=.3)
        self.finish()


@timed("B06")
class B06_Bridge(Scene):
    def construct(self):
        # Portrait: one bank low on the left, the other high on the right.
        lo = Polygon([-SAFE_X, -1.75, 0], [-.95, -1.75, 0], [-1.2, -2.25, 0], [-SAFE_X, -2.25, 0],
                     fill_color=SLATE, fill_opacity=1, stroke_width=0)
        hi = Polygon([SAFE_X, 1.45, 0], [.95, 1.45, 0], [1.2, .95, 0], [SAFE_X, .95, 0],
                     fill_color=TEAL, fill_opacity=1, stroke_width=0)
        l_lbl = fit(T("software engineering", 42), 3.6)
        l_lbl.move_to([-SAFE_X + .05 + l_lbl.width / 2, -2.55, 0])
        r_lbl = fit(T("coding with AI", 42), 3.6)
        r_lbl.move_to([SAFE_X - .05 - r_lbl.width / 2, 1.85, 0])
        self.go(.1, FadeIn(lo), FadeIn(l_lbl), rt=.4)
        self.go(.64, FadeIn(hi), FadeIn(r_lbl), rt=.4)

        p0, p1, p2 = np.array([-.95, -1.75, 0]), np.array([-.55, 1.1, 0]), np.array([.95, 1.45, 0])

        def arc(a):
            return (1 - a) ** 2 * p0 + 2 * a * (1 - a) * p1 + a ** 2 * p2

        deck = VMobject(stroke_color=INK, stroke_width=9).set_points_smoothly([arc(a / 40) for a in range(41)])
        heading = fit(T("a new bridge", 54, SLATE), 3.6).move_to([0, 2.85, 0])
        self.go(2.0, Create(deck), FadeIn(heading), rt=.7)

        # Footsteps cross the bridge: no figure, just the steps.
        steps = []
        for k in range(12):
            a = .05 + k * .062
            p, q = arc(a), arc(a + .01)
            ang = math.atan2(q[1] - p[1], q[0] - p[0])
            off = np.array([-math.sin(ang), math.cos(ang), 0]) * (.07 if k % 2 else .15)
            steps.append(Ellipse(width=.17, height=.09, fill_color=GOLD, fill_opacity=1, stroke_width=0)
                         .rotate(ang).move_to(p + off))
        times = np.linspace(3.12, 7.3, len(steps))
        learn = fit(T("keep learning", 46, TEAL), 2.3)
        learn.move_to([SAFE_X - .05 - learn.width / 2, -.9, 0])
        at_keep = int(np.argmin(np.abs(times - 5.18)))  # "keep learning" lands on the spoken words
        for i, (t, s) in enumerate(zip(times, steps)):
            extra = [FadeIn(learn, shift=UP * .1)] if i == at_keep else []
            self.go(float(t), FadeIn(s, scale=.6), *extra, rt=.2)
        self.finish()
