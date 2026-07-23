"""vox_scenes.py — Why Your Beautiful Résumé Is Invisible
(vox-invisible-resume, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash scripts/vox_run.sh reels/vox-invisible-resume

Color law: navy #3D5A80 = extracts clean / survives · crimson #BF3339 =
scrambled / vanished / lost. Gold = editor's pen, once. Hero object: a résumé
page under a horizontal read-head that pulls text into one linear strip (scan).
NO OCR tangent, NO vendor names, NO keyword advice (card exclusions).

Gate B / Gate A conventions: zero-width strokes are also zero-opacity; deliberate
line-on-text (strike/ring/read-head) is marked `_qc_intentional = True`; every
`.animate` uses a single method (the static checker's mock rejects chains).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene
import numpy as np

FAINT = "#C9C2B4"          # printed "text line" on the page

DUR = {"B01": 10.0, "B03": 8.0, "B04": 10.0, "B05": 10.5, "B06": 9.0,
       "B07": 9.0, "B08": 9.0, "B09": 10.5, "B10": 9.5, "B11": 8.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------------- geometry
PAGE_X, PAGE_W, PAGE_H = -3.9, 3.0, 4.0
STRIP_X, STRIP_W, STRIP_H = 4.2, 1.6, 4.0
PAGE_TOP = PAGE_H / 2 - 0.3
PAGE_BOT = -PAGE_H / 2 + 0.3


def _panel(x, w, h, fill=WHITE, fo=1.0):
    p = Rectangle(width=w, height=h).set_fill(fill, fo).set_stroke("#D8D2C4", 1.6)
    p.move_to([x, 0, 0])
    return p


def _textbar(w, color=FAINT, x=0.0, y=0.0):
    r = Rectangle(width=w, height=0.13).set_fill(color, 1).set_stroke(width=0, opacity=0)
    r.move_to([x, y, 0])
    return r


def _readhead(y):
    line = Line([PAGE_X - PAGE_W / 2, y, 0], [PAGE_X + PAGE_W / 2, y, 0],
                color=NAVY, stroke_width=3)
    tri = Triangle(color=NAVY).set_fill(NAVY, 1).set_stroke(width=0, opacity=0)
    tri.scale(0.12).rotate(-PI / 2)                    # point right
    tri.move_to([PAGE_X - PAGE_W / 2 - 0.22, y, 0])
    g = VGroup(line, tri)
    g._qc_intentional = True                           # deliberate sweep
    return g


def _strip_bar(color, y, w=1.2, filled=True):
    if filled:
        r = Rectangle(width=w, height=0.16).set_fill(color, 1).set_stroke(width=0, opacity=0)
    else:                                              # an empty slot (a gap)
        r = Rectangle(width=w, height=0.16).set_fill(BLACK, 0).set_stroke(color, 2)
    r.move_to([STRIP_X, y, 0])
    return r


def _strip_ys(n, top=1.5, bot=-1.5):
    return list(np.linspace(top, bot, n))


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("SURVIVING THE FILTER", font=SERIF, color=NAVY, font_size=24)
        t1 = Text("Why your beautiful résumé", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("is invisible", font=SERIF, color=INK, font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Extract(Scene):           # DOCUMENT — the only question the parser asks
    def construct(self):
        _quote_scene(self, "Can I extract the text?",
                     "— the only question the parser asks", None,
                     "extract", DUR["B03"])


class B04_ReadHead(Scene):          # the read-head pulls text into one strip
    def construct(self):
        total = DUR["B04"]
        page = _panel(PAGE_X, PAGE_W, PAGE_H)
        header = _textbar(1.8, INK, PAGE_X, PAGE_TOP - 0.2)
        ys = np.linspace(PAGE_TOP - 0.9, PAGE_BOT + 0.3, 6)
        lines = VGroup(*[_textbar(2.3 - 0.1 * (i % 3), FAINT, PAGE_X, y)
                         for i, y in enumerate(ys)])
        strip = _panel(STRIP_X, STRIP_W, STRIP_H, WHITE, 0.15)
        slabel = SerifLabel("one linear strip", NAVY, size=24).next_to(strip, DOWN, buff=0.3)
        head = _readhead(PAGE_TOP + 0.3)
        self.play(FadeIn(page), FadeIn(header), FadeIn(lines), FadeIn(strip),
                  run_time=0.9)
        self.play(FadeIn(head), run_time=0.4)
        reveals = [FadeIn(_strip_bar(NAVY, y)) for y in _strip_ys(6)]
        self.play(head.animate.shift(DOWN * (PAGE_H - 0.6)),
                  LaggedStart(*reveals, lag_ratio=0.14), run_time=min(3.4, total * 0.4))
        self.play(FadeIn(slabel), run_time=0.5)
        self.wait(max(0.5, total - 0.9 - 0.4 - min(3.4, total * 0.4) - 0.5))


class B05_ColumnInterleave(Scene):  # two columns interleave into nonsense
    def construct(self):
        total = DUR["B05"]
        page = _panel(PAGE_X, PAGE_W, PAGE_H)
        ys = np.linspace(PAGE_TOP - 0.6, PAGE_BOT + 0.3, 3)
        left = VGroup(*[_textbar(1.0, NAVY, PAGE_X - 0.65, y) for y in ys])
        right = VGroup(*[_textbar(1.0, CRIMSON, PAGE_X + 0.65, y) for y in ys])
        strip = _panel(STRIP_X, STRIP_W, STRIP_H, WHITE, 0.15)
        head = _readhead(PAGE_TOP + 0.3)
        self.play(FadeIn(page), FadeIn(left), FadeIn(right), FadeIn(strip),
                  FadeIn(head), run_time=0.9)
        # output alternates L,R,L,R,L,R — the interleave scramble
        colors = [NAVY, CRIMSON, NAVY, CRIMSON, NAVY, CRIMSON]
        reveals = [FadeIn(_strip_bar(c, y)) for c, y in zip(colors, _strip_ys(6))]
        self.play(head.animate.shift(DOWN * (PAGE_H - 0.6)),
                  LaggedStart(*reveals, lag_ratio=0.16), run_time=min(3.6, total * 0.42))
        lab = SerifLabel("interleaved into nonsense", CRIMSON, size=24)
        lab.next_to(strip, DOWN, buff=0.3)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 0.9 - min(3.6, total * 0.42) - 0.6))


class B06_NameVanishes(Scene):      # name in a graphic → absent
    def construct(self):
        total = DUR["B06"]
        page = _panel(PAGE_X, PAGE_W, PAGE_H)
        # the name as a GRAPHIC (a slate banner with text baked in — an image)
        banner = Rectangle(width=2.4, height=0.7).set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        banner.move_to([PAGE_X, PAGE_TOP - 0.3, 0])
        bname = Text("YOUR NAME", font=SERIF, color=WHITE, font_size=26).move_to(banner.get_center())
        tag = LabelChip("image", accent=INK, size=16).next_to(banner, RIGHT, buff=0.1)
        body = VGroup(*[_textbar(2.2, FAINT, PAGE_X, y)
                        for y in np.linspace(PAGE_TOP - 1.3, PAGE_BOT + 0.3, 4)])
        strip = _panel(STRIP_X, STRIP_W, STRIP_H, WHITE, 0.15)
        head = _readhead(PAGE_TOP + 0.5)
        self.play(FadeIn(page), FadeIn(banner), FadeIn(bname), FadeIn(tag),
                  FadeIn(body), FadeIn(strip), FadeIn(head), run_time=1.0)
        blank = _strip_bar(CRIMSON, 1.4, filled=False)     # the empty name slot
        body_bars = [FadeIn(_strip_bar(NAVY, y)) for y in _strip_ys(4, top=0.7, bot=-1.5)]
        self.play(head.animate.shift(DOWN * (PAGE_H - 0.9)),
                  FadeIn(blank), LaggedStart(*body_bars, lag_ratio=0.15),
                  run_time=min(2.6, total * 0.32))
        lab = SerifLabel("name: absent", CRIMSON, size=24)
        lab.next_to(blank, LEFT, buff=0.3)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 1.0 - min(2.6, total * 0.32) - 0.6))


class B07_SkillBarsGap(Scene):      # skill bars → no text, a gap
    def construct(self):
        total = DUR["B07"]
        page = _panel(PAGE_X, PAGE_W, PAGE_H)
        head_lbl = SerifLabel("Skills", INK, size=22).move_to([PAGE_X, PAGE_TOP - 0.2, 0])
        # sidebar skill bars (graphics) — filled tracks
        bars = VGroup()
        for i, y in enumerate(np.linspace(PAGE_TOP - 0.9, PAGE_BOT + 0.5, 4)):
            track = Rectangle(width=2.0, height=0.18).set_fill("#E7E0D1", 1).set_stroke(width=0, opacity=0)
            track.move_to([PAGE_X, y, 0])
            fillw = 2.0 * (0.5 + 0.12 * i)
            fill = Rectangle(width=fillw, height=0.18).set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
            fill.move_to([PAGE_X - (2.0 - fillw) / 2, y, 0])
            bars.add(track, fill)
        strip = _panel(STRIP_X, STRIP_W, STRIP_H, WHITE, 0.15)
        head = _readhead(PAGE_TOP + 0.3)
        self.play(FadeIn(page), FadeIn(head_lbl), FadeIn(bars), FadeIn(strip),
                  FadeIn(head), run_time=1.0)
        gap = _strip_bar(CRIMSON, 0.2, filled=False)
        gap2 = _strip_bar(CRIMSON, -0.15, filled=False)
        self.play(head.animate.shift(DOWN * (PAGE_H - 0.6)),
                  FadeIn(gap), FadeIn(gap2), run_time=min(2.6, total * 0.32))
        lab = SerifLabel("skills: (nothing)", CRIMSON, size=24)
        lab.next_to(VGroup(gap, gap2), LEFT, buff=0.3)
        self.play(FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 1.0 - min(2.6, total * 0.32) - 0.6))


class B08_Unqualified(Scene):       # no title found → unqualified
    def construct(self):
        total = DUR["B08"]
        strip = _panel(0.0, 2.2, 4.2, WHITE, 0.12)
        # the scrambled output: interleaved + blanks
        rows = [(NAVY, True), (CRIMSON, True), (CRIMSON, False), (NAVY, True),
                (CRIMSON, True), (CRIMSON, False)]
        ys = np.linspace(1.5, -1.5, len(rows))
        bars = VGroup()
        for (c, fl), y in zip(rows, ys):
            b = Rectangle(width=1.5, height=0.18)
            if fl:
                b.set_fill(c, 1).set_stroke(width=0, opacity=0)
            else:
                b.set_fill(BLACK, 0).set_stroke(c, 2)
            b.move_to([0.0, y, 0])
            bars.add(b)
        tags = VGroup(
            SerifLabel("name: —", CRIMSON, size=22).move_to([-3.4, 1.4, 0]),
            SerifLabel("dates: drifting", CRIMSON, size=22).move_to([-3.4, 0.0, 0]),
            SerifLabel("skills: —", CRIMSON, size=22).move_to([-3.4, -1.4, 0]),
        )
        self.play(FadeIn(strip), FadeIn(bars), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(t) for t in tags], lag_ratio=0.2), run_time=1.0)
        stamp = LabelChip("UNQUALIFIED", accent=CRIMSON, size=30)
        stamp.rotate(-0.05 * PI).move_to([2.9, 0.2, 0])
        self.play(FadeIn(stamp, scale=0.85), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B09_ForkBeforeHuman(Scene):   # the fork before the human
    def construct(self):
        total = DUR["B09"]
        submit = LabelChip("Submit", accent=NAVY, size=26).move_to([-4.8, 0, 0])
        fork_lbl = SerifLabel("before any human opens it", INK, size=22).to_edge(UP, buff=0.7)
        up_arrow = Arrow([-3.9, 0.2, 0], [0.2, 1.9, 0], color=NAVY, stroke_width=5, buff=0.2)
        dn_arrow = Arrow([-3.9, -0.2, 0], [0.2, -1.9, 0], color=CRIMSON, stroke_width=5, buff=0.2)
        up_lbl = SerifLabel("parses · human · interview", NAVY, size=22)
        up_lbl.move_to([2.7, 1.9, 0])
        dn_lbl = SerifLabel("scrambled · auto-reject", CRIMSON, size=22)
        dn_lbl.move_to([2.7, -1.6, 0])
        dn_lbl2 = Text("no human ever looks", font=SERIF, color=CRIMSON, font_size=20)
        dn_lbl2.move_to([2.7, -2.15, 0])
        self.play(FadeIn(submit), FadeIn(fork_lbl), run_time=0.7)
        self.play(GrowArrow(up_arrow), FadeIn(up_lbl), run_time=0.9)
        self.play(GrowArrow(dn_arrow), FadeIn(dn_lbl), FadeIn(dn_lbl2), run_time=0.9)
        self.wait(max(0.5, total - 3.4))


class B10_SafeVersion(Scene):       # single column → clean strip
    def construct(self):
        total = DUR["B10"]
        page = _panel(PAGE_X, PAGE_W, PAGE_H)
        header = _textbar(1.6, INK, PAGE_X, PAGE_TOP - 0.2)
        ys = np.linspace(PAGE_TOP - 0.9, PAGE_BOT + 0.3, 5)
        lines = VGroup(*[_textbar(2.3, FAINT, PAGE_X, y) for y in ys])
        strip = _panel(STRIP_X, STRIP_W, STRIP_H, WHITE, 0.15)
        head = _readhead(PAGE_TOP + 0.3)
        self.play(FadeIn(page), FadeIn(header), FadeIn(lines), FadeIn(strip),
                  FadeIn(head), run_time=0.9)
        reveals = [FadeIn(_strip_bar(NAVY, y)) for y in _strip_ys(5)]
        self.play(head.animate.shift(DOWN * (PAGE_H - 0.6)),
                  LaggedStart(*reveals, lag_ratio=0.14), run_time=min(3.0, total * 0.4))
        check = LabelChip("name · title · dates: clean", accent=NAVY, size=20)
        check.next_to(strip, DOWN, buff=0.3)
        lab = SerifLabel("one column · real text", INK, size=22).next_to(page, DOWN, buff=0.3)
        self.play(FadeIn(check), FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 0.9 - min(3.0, total * 0.4) - 0.6))


class B11_End(Scene):               # endcard — the 5-second paste test payoff
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Select all, copy, paste —", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("that's what the parser sees.", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 13", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
