"""vox_scenes.py — Why a Perfect AI Model Killed the Doorbell (16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Durations from beat_sheet.json (audio locked 2026-07-05):
B02 5.28 · B05 9.93 · B06 9.46 · B08 9.09 · B09 8.39 · B10 6.50 · B12 7.60
Render:  bash scripts/vox_run.sh reels/vox-doorbell-battery

The cascade (B05 -> B06 -> B09) is the film's spine: one fixed frame, three
budget rows, only the active row animates. Accents: BLUE vs TERRA; GOLD is
the single annotation voice; the HandRing appears once, on B09's overshoot.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403


# ------------------------------------------------ the cascade frame (shared)

ROW_Y = {"MEMORY": 2.0, "LATENCY": 0.1, "POWER": -1.8}
TRACK_X0, TRACK_X1 = -3.4, 5.9        # bar track
BUDGET_X = 4.3                        # the charcoal budget line
BAR_H = 0.5

FINAL_W = {                           # demand-bar end x per row
    "MEMORY": 3.55,                   # under the line — pass
    "LATENCY": 3.85,                  # just under — pass
    "POWER": 5.75,                    # PAST the line — the miss
}


def _row(name):
    """Label + track + budget tick for one budget row."""
    y = ROW_Y[name]
    label = SerifLabel(name, accent=BLUE, size=30)
    label.move_to([-5.1, y + 0.55, 0])
    track = Line([TRACK_X0, y, 0], [TRACK_X1, y, 0], color=INK, stroke_width=2)
    tick = Line([BUDGET_X, y, 0], [BUDGET_X, y + 1.0, 0],
                color=INK, stroke_width=4)
    return VGroup(label, track, tick)


def _bar(name, color):
    """Demand bar seated on the row's track, full final size (grow at play)."""
    y = ROW_Y[name]
    w = FINAL_W[name] - TRACK_X0
    bar = Rectangle(width=w, height=BAR_H).set_fill(color, 1).set_stroke(width=0)
    bar.move_to([TRACK_X0 + w / 2, y + BAR_H / 2, 0])
    return bar


def _budget_caption():
    c = Text("budget", font=SERIF, color=INK, font_size=22, slant=ITALIC)
    c.move_to([BUDGET_X - 0.75, ROW_Y["MEMORY"] + 0.85, 0])   # left of the tick, clear of the stamp
    return c


def _pass_stamp(row):
    """Blue serif PASS stamp beside the budget tick, at the row's height."""
    st = Text("PASS", font=SERIF, color=BLUE, font_size=34, weight=BOLD)
    box = SurroundingRectangle(st, buff=0.12).set_stroke(BLUE, 3).set_fill(opacity=0)
    g = VGroup(box, st).rotate(0.09)
    g.move_to([5.1, ROW_Y[row] + 0.95, 0])
    return g


# ------------------------------------------------------------------ beats

class B02_Title(Scene):            # 5.28s
    def construct(self):
        eye = Text("EMBEDDED AI", font=SERIF, color=BLUE, font_size=24)
        t = Text("WHY A PERFECT MODEL KILLED THE DOORBELL",
                 font=SERIF, color=INK, font_size=50, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=TERRA, stroke_width=2)
        s = Text("the calculation nobody ran", font=SERIF, color=INK,
                 font_size=30)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.5)
        self.wait(3.3)


class B05_CascadeMemory(Scene):    # 9.93s — the spine appears; bar one passes
    def construct(self):
        rows = VGroup(*[_row(n) for n in ROW_Y])
        cap = _budget_caption()
        # "a cascade of three budgets" — the frame builds first
        self.play(FadeIn(rows, lag_ratio=0.25), FadeIn(cap), run_time=1.2)
        self.wait(3.2)
        # "Budget one: memory. This model fit."
        bar = _bar("MEMORY", BLUE)
        self.play(GrowFromEdge(bar, LEFT), run_time=2.2)
        self.wait(1.4)
        # "Pass." — stamp on cue
        stamp = _pass_stamp("MEMORY")
        self.play(FadeIn(stamp, scale=1.35), run_time=0.6)
        self.wait(1.3)


class B06_CascadeLatency(Scene):   # 9.46s — same frame, bar two passes
    def construct(self):
        rows = VGroup(*[_row(n) for n in ROW_Y])
        cap = _budget_caption()
        mem = _bar("MEMORY", BLUE).set_fill(BLUE, 0.35)     # dimmed history
        stamp1 = _pass_stamp("MEMORY").set_opacity(0.45)
        self.add(rows, cap, mem, stamp1)
        self.wait(0.4)
        # "Budget two: time … a couple of seconds per look"
        bar = _bar("LATENCY", BLUE)
        chip = LabelChip("seconds per look", accent=SLATE, size=24)
        chip.move_to([0.4, ROW_Y["LATENCY"] - 0.55, 0])
        self.play(GrowFromEdge(bar, LEFT), run_time=2.0)
        self.play(FadeIn(chip, shift=UP * 0.1), run_time=0.6)
        self.wait(3.2)
        # "Pass."
        stamp2 = _pass_stamp("LATENCY")
        self.play(FadeIn(stamp2, scale=1.35), run_time=0.6)
        self.wait(2.6)


class B08_CurrentArithmetic(Scene):  # 9.09s — sliver vs column, then the average
    def construct(self):
        y0 = -2.6
        base = Line([-4.6, y0, 0], [4.6, y0, 0], color=INK, stroke_width=2)
        # asleep — a sliver you can barely see
        sliver = Rectangle(width=0.9, height=0.07).set_fill(BLUE, 1).set_stroke(width=0)
        sliver.move_to([-2.5, y0 + 0.035, 0])
        lab_s = SerifLabel("asleep · microamps", accent=BLUE, size=26)
        lab_s.next_to(sliver, DOWN, buff=0.35)
        self.play(Create(base), FadeIn(sliver), FadeIn(lab_s), run_time=0.9)
        self.wait(1.2)
        # awake — thousands of times taller (axis-break tildes keep it honest)
        col = Rectangle(width=0.9, height=4.6).set_fill(TERRA, 1).set_stroke(width=0)
        col.move_to([2.5, y0 + 2.3, 0])
        lab_a = SerifLabel("awake · milliamps", accent=TERRA, size=26)
        lab_a.next_to(col, DOWN, buff=0.35).shift(DOWN * 0.0)
        brk = VGroup(
            Line([2.0, y0 + 2.1, 0], [3.0, y0 + 2.35, 0], color=GROUND, stroke_width=10),
            Line([2.0, y0 + 1.9, 0], [3.0, y0 + 2.15, 0], color=INK, stroke_width=2),
            Line([2.0, y0 + 2.3, 0], [3.0, y0 + 2.55, 0], color=INK, stroke_width=2),
        )
        self.play(GrowFromEdge(col, DOWN), FadeIn(lab_a), run_time=1.6)
        self.play(FadeIn(brk), run_time=0.3)
        self.wait(1.6)
        # "the average draw jumps from microamps to milliamps"
        avg = DashedLine([-4.4, y0 + 1.15, 0], [4.4, y0 + 1.15, 0],
                         color=INK, stroke_width=3)
        tag = SerifLabel("average draw", accent=GOLD, size=28)
        tag.move_to([-0.2, y0 + 1.75, 0])
        self.play(Create(avg), run_time=0.8)
        self.play(FadeIn(tag, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)


class B09_CascadeFail(Scene):      # 8.39s — bar three misses; the film's image
    def construct(self):
        rows = VGroup(*[_row(n) for n in ROW_Y])
        cap = _budget_caption()
        mem = _bar("MEMORY", BLUE).set_fill(BLUE, 0.35)
        lat = _bar("LATENCY", BLUE).set_fill(BLUE, 0.35)
        self.add(rows, cap, mem, lat)
        # "That's the murder weapon." — the bar blows through the line
        bar = _bar("POWER", TERRA)
        self.play(GrowFromEdge(bar, LEFT), run_time=1.6)
        over = Rectangle(width=FINAL_W["POWER"] - BUDGET_X, height=BAR_H * 1.7)
        over.move_to([(BUDGET_X + FINAL_W["POWER"]) / 2,
                      ROW_Y["POWER"] + BAR_H / 2, 0])
        ring = HandRing(over, color=TERRA)          # the editor's pen — once
        self.play(Create(ring), run_time=1.0)
        self.wait(1.2)
        # "Six months becomes two days."
        six = Text("SIX MONTHS", font=SERIF, color=INK, font_size=36, weight=BOLD)
        six.move_to([-1.8, -2.95, 0])
        strike = Line(six.get_left() + LEFT * 0.15, six.get_right() + RIGHT * 0.15,
                      color=TERRA, stroke_width=5)
        strike._qc_intentional = True      # the editor's strike-through touches text on purpose
        two = Text("TWO DAYS", font=SERIF, color=TERRA, font_size=40, weight=BOLD)
        two.next_to(six, RIGHT, buff=1.1)  # side by side — nothing below the safe line
        self.play(FadeIn(six), run_time=0.5)
        self.play(Create(strike), run_time=0.5)
        self.play(FadeIn(two, scale=1.25), run_time=0.7)
        self.wait(2.9)


class B10_ReturnsIsotype(Scene):   # 6.50s — 24 squares × 500 = 12,000 returns
    def construct(self):
        grid = IsotypeGrid([24], [INK], per_row=8, size=0.34, gap=0.16)
        grid.move_to([0, 0.6, 0])
        cap = Text("one square = 500 returned units", font=SERIF, color=INK,
                   font_size=24, slant=ITALIC)
        cap.next_to(grid, DOWN, buff=0.5)
        # count-up fills the beat's first phrase
        self.play(grid.count_up(2.4))
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.0)
        # "rolled back. Deleted." — the ink X
        chip = LabelChip("PERSON DETECTION", accent=SLATE, size=26)
        chip.move_to([0, -2.7, 0])
        x1 = Line(chip.get_corner(DL) + DL * 0.08, chip.get_corner(UR) + UR * 0.08,
                  color=TERRA, stroke_width=6)
        x2 = Line(chip.get_corner(UL) + UL * 0.08, chip.get_corner(DR) + DR * 0.08,
                  color=TERRA, stroke_width=6)
        x1._qc_intentional = True          # the ink X strikes the chip on purpose
        x2._qc_intentional = True
        self.play(FadeIn(chip), run_time=0.5)
        self.play(Create(x1), Create(x2), run_time=0.7)
        self.wait(1.4)


class B12_End(Scene):              # 7.60s — the kicker
    def construct(self):
        eye = Text("EMBEDDED AI", font=SERIF, color=BLUE, font_size=24)
        t = Text("THE THIRD BUDGET", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=TERRA, stroke_width=2)
        eye.to_edge(UP, buff=1.2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        # "memory, latency, power" — the third word is the one that kills
        words = VGroup(
            SerifLabel("memory", accent=BLUE, size=36),
            SerifLabel("latency", accent=BLUE, size=36),
            SerifLabel("power", accent=TERRA, size=36),
        ).arrange(RIGHT, buff=1.1)
        words.next_to(u, DOWN, buff=0.7)
        for w in words:
            self.play(FadeIn(w, shift=UP * 0.12), run_time=0.5)
        self.wait(0.6)
        ring = HandRing(words[2], color=TERRA)
        self.play(Create(ring), run_time=0.9)
        self.wait(2.7)
