"""vox_scenes.py — Why the Application Counter Is Lying to You
(vox-application-counter, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback) —
the compile ladder retimes ±5%. Render everything:
  bash scripts/vox_run.sh reels/vox-application-counter

Color law (FACTCHECK.md / beat_sheet color_semantics):
  terracotta #D35F43 = the counter / cold channel / feedback
  dusty blue #5B7B9C = connections channel / return
  gold = the single editor's-pen voice. Never swap mid-film.
Two-number cap: only ~0.2% (B06) and 54% (B07) may appear on screen.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

# Fallback estimates — used when checked from an isolated copy (Gate A).
DUR = {"B01": 8.4, "B03": 9.2, "B05": 10.4, "B06": 6.0, "B07": 8.0,
       "B08": 10.4, "B09": 10.4, "B10": 7.2, "B11": 8.0}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _counter_group(value="41", scale=1.0):
    """The odometer: mono digits in terracotta on a hairline frame."""
    digits = Text(value, font=MONO, color=TERRA, font_size=int(96 * scale),
                  weight=BOLD)
    frame = SurroundingRectangle(digits, buff=0.25)
    frame.set_stroke(INK, 2).set_fill(WHITE, 0.0)
    lab = SerifLabel("applications sent", TERRA, size=int(26 * scale))
    lab.next_to(frame, DOWN, buff=0.35)
    return VGroup(frame, digits, lab)


class B01_Title(Scene):            # title card
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION PRINCIPLE", font=SERIF, color=BLUE,
                   font_size=24)
        t1 = Text("Why the application counter", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("is lying to you", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Counter(Scene):          # the odometer ticks — dressing, not data
    def construct(self):
        total = DUR["B03"]
        group = _counter_group("28")
        group.move_to(UP * 0.3)
        self.play(FadeIn(group), run_time=0.8)
        stamps = VGroup()
        for i, v in enumerate(("33", "37", "41")):
            nxt = _counter_group(v)
            nxt.move_to(UP * 0.3)
            stamp = Square(0.28)
            stamp.set_fill(TERRA, 0.85).set_stroke(width=0)
            stamp.move_to(DOWN * 2.4 + LEFT * 1.2 + RIGHT * i * 1.2)
            stamps.add(stamp)
            self.play(Transform(group, nxt),
                      FadeIn(stamp, shift=DOWN * 0.2), run_time=0.9)
        self.wait(max(0.5, total - 0.8 - 3 * 0.9))


class B05_Deletions(Scene):        # three named waves — NO rates on screen
    def construct(self):
        total = DUR["B05"]
        grid = IsotypeGrid([60], [INK], per_row=12, size=0.3, gap=0.14)
        grid.move_to(RIGHT * 1.8 + UP * 0.2)
        title = SerifLabel("what the machine deletes", NAVY, size=28)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title), run_time=0.6)
        self.play(grid.count_up(1.4))
        waves = (("never real", list(range(0, 20))),
                 ("no sponsorship", list(range(20, 38))),
                 ("auto-rejected", list(range(38, 52))))
        y = 1.1
        for name, idx in waves:
            chip = LabelChip(name, accent=TERRA, size=24)
            chip.move_to(LEFT * 4.3 + UP * y)
            y -= 1.1
            self.play(FadeIn(chip, shift=RIGHT * 0.2),
                      LaggedStart(*[grid.marks[i].animate.set_opacity(0.18)
                                    for i in idx],
                                  lag_ratio=0.02, run_time=1.2))
        self.wait(max(0.5, total - 0.6 - 1.4 - 3 * 1.2))


class B06_OneInFiveHundred(Scene):  # number 1 of 2 — the arithmetic is drawn
    def construct(self):
        total = DUR["B06"]
        grid = IsotypeGrid([500], ["#B9B2A4"], per_row=32, size=0.11, gap=0.05)
        grid.move_to(UP * 0.5)
        lab = SerifLabel("~0.2% — one in five hundred", TERRA, size=30)
        lab.next_to(grid, DOWN, buff=0.5)
        self.play(grid.count_up(2.0, lag_ratio=0.003))
        one = grid.marks[271]
        self.play(one.animate.set_fill(INK, 1), FadeIn(lab), run_time=0.9)
        ring = HandRing(one, color=TERRA)
        self.play(Create(ring), run_time=0.7)
        self.wait(max(0.5, total - 3.6))


class B07_FiftyFour(Scene):        # number 2 of 2 — the 54% claim card
    def construct(self):
        total = DUR["B07"]
        num = Text("54%", font=SERIF, color=INK, font_size=140, weight=BOLD)
        num.move_to(UP * 1.2)
        c1 = Text("of hires came through a personal", font=SERIF, color=INK,
                  font_size=34)
        c2 = Text("or professional connection", font=SERIF, color=INK,
                  font_size=34)
        claim = VGroup(c1, c2).arrange(DOWN, buff=0.15)
        claim.next_to(num, DOWN, buff=0.5)
        att = Text("MyPerfectResume survey of 1,000 U.S. workers, 2025",
                   font=SERIF, color=INK, font_size=20)
        att.to_corner(DL, buff=0.6)
        self.play(FadeIn(num, scale=0.95), run_time=0.9)
        self.play(FadeIn(claim), run_time=0.7)
        bar = Rectangle(width=0.1, height=c2.height + 0.2)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0)
        bar.align_to(c2, LEFT).align_to(c2, DOWN)
        bar._qc_intentional = True
        bar_full = Rectangle(width=c2.width + 0.2, height=c2.height + 0.2)
        bar_full.set_fill(GOLD, 0.55).set_stroke(width=0)
        bar_full.move_to(c2)
        bar_full._qc_intentional = True
        self.add(bar)
        c2.set_z_index(1)
        self.play(Transform(bar, bar_full), run_time=0.9)
        self.play(FadeIn(att), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


class B08_TwoClocks(Scene):        # instant feedback vs delayed return
    def construct(self):
        total = DUR["B08"]
        top_lab = SerifLabel("the counter", TERRA, size=26)
        top_lab.move_to(LEFT * 4.4 + UP * 2.1)
        top = Line(LEFT * 4.6, RIGHT * 4.6, color=TERRA, stroke_width=3)
        top.shift(UP * 1.4)
        bot_lab = SerifLabel("connections", BLUE, size=26)
        bot_lab.move_to(LEFT * 4.4 + DOWN * 0.5)
        bot = Line(LEFT * 4.6, RIGHT * 4.6, color=BLUE, stroke_width=3)
        bot.shift(DOWN * 1.2)
        self.play(FadeIn(top_lab), Create(top), run_time=0.9)
        ticks = VGroup(*[Line(UP * 0.16, DOWN * 0.16, color=TERRA,
                              stroke_width=3)
                         .move_to(np.array([-4.2 + i * 0.73, 1.4, 0]))
                         for i in range(12)])
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.1) for t in ticks],
                              lag_ratio=0.12, run_time=1.8))
        self.play(FadeIn(bot_lab), Create(bot), run_time=1.4)  # the long quiet
        marks = (("conversation", 1.4, 0.10), ("referral", 2.9, 0.14),
                 ("offer", 4.3, 0.18))
        for name, x, r in marks:
            dot = Dot(np.array([x, -1.2, 0]), radius=r, color=BLUE)
            lab = Text(name, font=SERIF, color=INK, font_size=20)
            if lab.width > 1.25:
                lab.scale_to_fit_width(1.25)
            lab.next_to(dot, DOWN, buff=0.22)
            self.play(GrowFromCenter(dot), FadeIn(lab), run_time=0.6)
        self.wait(max(0.5, total - 5.9))


class B09_InstinctRing(Scene):     # hours drift to the loudest feedback
    def construct(self):
        total = DUR["B09"]
        counter = _counter_group("41", scale=0.7)
        counter.move_to(RIGHT * 3.2 + UP * 0.6)
        quiet = Line(LEFT * 5.2, LEFT * 1.6, color=BLUE, stroke_width=3)
        quiet.shift(DOWN * 1.6)
        quiet_lab = SerifLabel("connections", BLUE, size=22)
        quiet_lab.next_to(quiet, DOWN, buff=0.25)
        self.add(counter, quiet, quiet_lab)
        blocks = VGroup(*[Square(0.42).set_fill(INK, 0.8).set_stroke(width=0)
                          .move_to(LEFT * 4.6 + RIGHT * (i % 3) * 0.6
                                   + UP * (0.9 - (i // 3) * 0.6))
                          for i in range(6)])
        self.play(FadeIn(blocks), run_time=0.7)
        for i, b in enumerate(blocks):
            self.play(b.animate.move_to(counter.get_bottom()
                                        + DOWN * 0.7 + LEFT * 1.0
                                        + RIGHT * (i % 3) * 0.6
                                        + DOWN * (i // 3) * 0.6),
                      run_time=0.55)
        ring = HandRing(counter, color=TERRA)
        self.play(Create(ring), run_time=0.9)
        self.wait(max(0.5, total - 0.7 - 6 * 0.55 - 0.9))


class B10_Reallocate(Scene):       # conservation: same blocks, other column
    def construct(self):
        total = DUR["B10"]
        left_lab = SerifLabel("where the feedback is", TERRA, size=24)
        if left_lab.width > 3.6:
            left_lab.scale_to_fit_width(3.6)
        left_lab.move_to(LEFT * 2.9 + UP * 2.2)
        right_lab = SerifLabel("where the return is", BLUE, size=24)
        if right_lab.width > 3.6:
            right_lab.scale_to_fit_width(3.6)
        right_lab.move_to(RIGHT * 2.9 + UP * 2.2)
        blocks = VGroup(*[Square(0.55).set_fill(TERRA, 0.9).set_stroke(width=0)
                          .move_to(LEFT * 2.9 + DOWN * 2.0
                                   + UP * (i % 4) * 0.75
                                   + RIGHT * (i // 4) * 0.75 + LEFT * 0.37)
                          for i in range(8)])
        self.play(FadeIn(left_lab), FadeIn(right_lab), FadeIn(blocks),
                  run_time=0.9)
        for i, b in enumerate(blocks):
            tgt = Square(0.55).set_fill(BLUE, 0.9).set_stroke(width=0)
            tgt.move_to(RIGHT * 2.9 + DOWN * 2.0 + UP * (i % 4) * 0.75
                        + RIGHT * (i // 4) * 0.75 + LEFT * 0.37)
            self.play(Transform(b, tgt), run_time=0.5)
        self.wait(max(0.5, total - 0.9 - 8 * 0.5))


class B11_End(Scene):              # endcard (outro law owns the beat's tail)
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Spend effort where the return is —", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("not where the feedback is.", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from The Reallocation Engine — chapter 2", font=SERIF,
                 color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
