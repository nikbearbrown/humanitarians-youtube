"""vox_scenes.py -- embedded-ai/youtube/cli-battery-life
Reel: Build a Battery-Life Predictor with Claude Code
Palette: teardown (white ground, ink originals, crimson = problem/warning)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  high-freq / danger zone
  SLATE   #545454  structure, neutral chips

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1 (AAA)
  CRIMSON on GROUND -> non-text shape fill only; white-on-CRIMSON chip = OK
  No GOLD text. No chapter references.

Gate A rules (IMPORTANT):
  Each .animate uses a single chained method.
  Every scene has real shape motion (Create / Transform / GrowFromCenter).
  Coords inside +-7.1 x, +-4.0 y; safe area +-6.3 x, +-3.4 y.
"""

import sys, json, pathlib, os, numpy as np
os.environ.setdefault("VOX_PALETTE", "teardown")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass
_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}
def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))


# =============================================================================
# B01_Problem -- title card: duty cycle as the killer; nobody did the math
# =============================================================================
class B01_Problem(Scene):
    """Title card: inference frequency x duty cycle x average current = days."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("BATTERY LIFE PREDICTOR", font=DISPLAY, color=INK, font_size=30)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_dead = LabelChip("DIED IN THE FIELD", accent=CRIMSON, size=22)
        chip_dead.move_to([-2.8, 1.9, 0])

        chip_math = LabelChip("THREE MULTIPLICATIONS", accent=SLATE, size=22)
        chip_math.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_dead), GrowFromCenter(chip_math), run_time=0.5)

        sub = Text("duty = inference_ms x freq_hz / 1000",
                   font=DISPLAY, color=INK, font_size=20)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_avg = LabelChip("AVG CURRENT", accent=SLATE, size=22)
        chip_avg.move_to([-2.8, -0.15, 0])

        chip_days = LabelChip("DAYS OF LIFE", accent=INK, size=22)
        chip_days.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_avg), GrowFromCenter(chip_days), run_time=0.5)

        q = Text("compute this before you build the prototype",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_BatteryLife -- current-vs-time strip at 3 frequencies
# =============================================================================
class B04_BatteryLife(Scene):
    """Show inference pulses at 0.5Hz, 2Hz, 10Hz.
    Each panel: time strip with active pulses, average current line, days label.
    """

    def construct(self):
        dur = _dur("B04")

        hdr = Text("DUTY CYCLE vs FREQUENCY", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # Three panels stacked vertically
        # Each panel: y_center at 1.5, 0.0, -1.5
        PANEL_Y = [1.5, 0.0, -1.5]
        FREQS   = [0.5, 2.0, 10.0]
        DAYS    = [333, 105, 33]
        AVG_MA  = [1.5, 6.0, 30.0]

        # Active pulse current = 30mA, sleep = 0.05mA
        # Time window = 2 seconds shown
        # Pulse width = inf_ms = 100ms = 0.1s
        ACT_MA = 30.0
        INF_S  = 0.1  # seconds

        # Scene: x = time, range 0->2s maps to x -5.5->5.5
        # y within panel: mA range 0->35 maps to 0.8 height units per panel
        T_MAX = 2.0
        X_L, X_R = -5.5, 5.5

        def t_to_x(t):
            return X_L + (t / T_MAX) * (X_R - X_L)

        PANEL_H = 0.8  # half-height of current axis per panel

        elapsed = 0.4

        for pi, (py, freq, days, avg) in enumerate(zip(PANEL_Y, FREQS, DAYS, AVG_MA)):
            # Panel separator line
            if pi > 0:
                psep = Line([X_L, py + PANEL_H + 0.15, 0],
                            [X_R, py + PANEL_H + 0.15, 0],
                            stroke_width=0.6, color=SLATE)
                psep.set_stroke(opacity=0.3)
                self.play(Create(psep), run_time=0.2)
                elapsed += 0.2

            # Frequency label (left)
            freq_str = f"{freq}Hz" if freq != 0.5 else "0.5Hz"
            fl = Text(freq_str, font=DISPLAY, color=INK, font_size=16)
            fl.move_to([X_L + 0.5, py + PANEL_H * 0.5, 0])
            self.play(FadeIn(fl), run_time=0.2)
            elapsed += 0.2

            # Draw pulses as Rectangles
            period_s = 1.0 / freq
            t = 0.0
            pulse_rects = []
            while t + INF_S <= T_MAX:
                px0 = t_to_x(t)
                px1 = t_to_x(t + INF_S)
                pw  = px1 - px0
                pr  = Rectangle(
                    width=pw,
                    height=PANEL_H,
                    fill_color=INK,
                    fill_opacity=0.75,
                    stroke_width=0,
                )
                pr.move_to([(px0 + px1) / 2, py + PANEL_H / 2, 0])
                pulse_rects.append(pr)
                t += period_s

            for pr in pulse_rects:
                self.play(Create(pr), run_time=0.15)
                elapsed += 0.15

            # Average current line (SLATE dashed via short segments)
            avg_y = py + PANEL_H * (avg / ACT_MA)
            avg_line = Line([t_to_x(0), avg_y, 0], [t_to_x(T_MAX), avg_y, 0],
                            stroke_width=1.5, color=SLATE)
            avg_line.set_stroke(opacity=0.8)
            self.play(Create(avg_line), run_time=0.3)
            elapsed += 0.3

            # Days chip (right side)
            days_chip = LabelChip(f"{days} days", accent=INK, size=17)
            days_chip.move_to([X_R - 0.8, py + PANEL_H * 0.6, 0])
            self.play(GrowFromCenter(days_chip), run_time=0.3)
            elapsed += 0.3

        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_RaceToSleep -- two current traces: run slow vs race-to-sleep
# =============================================================================
class B06_RaceToSleep(Scene):
    """Two panels side by side: run slow (SLATE) vs race-to-sleep (INK).
    Race-to-sleep has higher peak but lower average because duty cycle is lower."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("RACE-TO-SLEEP", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # Divider between panels
        div = Line([0, -3.2, 0], [0, 2.9, 0], stroke_width=0.8, color=SLATE)
        div.set_stroke(opacity=0.4)
        self.play(Create(div), run_time=0.3)

        # Left panel: "run slow" -- 1 Hz inference, 100ms pulse at 20mA
        # Right panel: "race-to-sleep" -- 1 Hz inference, 33ms pulse at 50mA (higher clock)
        # Period = 1s for both, T_MAX = 1.5s

        T_MAX = 1.5

        def t_to_x_l(t):
            return -5.5 + (t / T_MAX) * 5.0

        def t_to_x_r(t):
            return 0.3 + (t / T_MAX) * 5.0

        Y_BOT = -2.5
        MA_MAX = 60.0
        PANEL_H = 4.5  # scene height for current axis

        def ma_y(ma):
            return Y_BOT + (ma / MA_MAX) * PANEL_H

        # Left: run slow -- 100ms at 20mA
        RUN_SLOW_INF_S = 0.1   # 100ms
        RUN_SLOW_MA    = 20.0
        RUN_SLOW_FREQ  = 1.0

        # Right: race-to-sleep -- 33ms at 50mA
        RTS_INF_S = 0.033  # 33ms
        RTS_MA    = 50.0
        RTS_FREQ  = 1.0

        # Panel labels
        lbl_l = Text("RUN SLOW", font=DISPLAY, color=SLATE, font_size=20)
        lbl_l.move_to([-3.0, 2.8, 0])
        self.play(FadeIn(lbl_l), run_time=0.3)

        lbl_r = Text("RACE-TO-SLEEP", font=DISPLAY, color=INK, font_size=20)
        lbl_r.move_to([3.0, 2.8, 0])
        self.play(FadeIn(lbl_r), run_time=0.3)

        # X axes
        axl = Line([-5.5, Y_BOT, 0], [-0.3, Y_BOT, 0], stroke_width=1.2, color=INK)
        axr = Line([0.3, Y_BOT, 0], [5.5, Y_BOT, 0], stroke_width=1.2, color=INK)
        self.play(Create(axl), run_time=0.3)
        self.play(Create(axr), run_time=0.3)

        # Left: run slow pulse
        pw_l = (RUN_SLOW_INF_S / T_MAX) * 5.0
        bar_l = Rectangle(width=pw_l, height=ma_y(RUN_SLOW_MA) - Y_BOT,
                          fill_color=SLATE, fill_opacity=0.7, stroke_width=0)
        bar_l.move_to([-5.5 + pw_l / 2,
                       Y_BOT + (ma_y(RUN_SLOW_MA) - Y_BOT) / 2, 0])
        self.play(Create(bar_l), run_time=0.5)

        # Left: average current line
        SLEEP_MA = 0.05
        avg_l = (RUN_SLOW_INF_S * RUN_SLOW_FREQ * RUN_SLOW_MA
                 + (1 - RUN_SLOW_INF_S * RUN_SLOW_FREQ) * SLEEP_MA)
        avg_line_l = Line([-5.5, ma_y(avg_l), 0], [-0.3, ma_y(avg_l), 0],
                          stroke_width=1.5, color=SLATE)
        avg_line_l.set_stroke(opacity=0.9)
        self.play(Create(avg_line_l), run_time=0.4)

        avg_chip_l = LabelChip(f"avg {avg_l:.1f}mA", accent=SLATE, size=16)
        avg_chip_l.move_to([-3.0, ma_y(avg_l) + 0.35, 0])
        self.play(GrowFromCenter(avg_chip_l), run_time=0.3)

        # Right: race-to-sleep pulse (shorter, higher)
        pw_r = (RTS_INF_S / T_MAX) * 5.0
        bar_r = Rectangle(width=pw_r, height=ma_y(RTS_MA) - Y_BOT,
                          fill_color=INK, fill_opacity=0.7, stroke_width=0)
        bar_r.move_to([0.3 + pw_r / 2,
                       Y_BOT + (ma_y(RTS_MA) - Y_BOT) / 2, 0])
        self.play(Create(bar_r), run_time=0.5)

        # Right: average current line
        avg_r = (RTS_INF_S * RTS_FREQ * RTS_MA
                 + (1 - RTS_INF_S * RTS_FREQ) * SLEEP_MA)
        avg_line_r = Line([0.3, ma_y(avg_r), 0], [5.5, ma_y(avg_r), 0],
                          stroke_width=1.5, color=INK)
        avg_line_r.set_stroke(opacity=0.9)
        self.play(Create(avg_line_r), run_time=0.4)

        avg_chip_r = LabelChip(f"avg {avg_r:.1f}mA", accent=INK, size=16)
        avg_chip_r.move_to([3.0, ma_y(avg_r) + 0.35, 0])
        self.play(GrowFromCenter(avg_chip_r), run_time=0.3)

        # Winner chip
        win_chip = LabelChip("RACE-TO-SLEEP WINS", accent=INK, size=20)
        win_chip.move_to([3.0, -3.1, 0])
        self.play(GrowFromCenter(win_chip), run_time=0.4)

        elapsed = 0.4 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.5 + 0.4 + 0.3 + 0.5 + 0.4 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary -- the three-multiplication formula
# =============================================================================
class B07_Summary(Scene):
    """Recap: the three-multiplication formula; pre-prototype check."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("duty = inf_ms x freq / 1000", font=DISPLAY, color=INK, font_size=22)
        row1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(row1), run_time=0.4)

        row2 = Text("avg_mA = duty x active + (1-duty) x sleep", font=DISPLAY, color=INK, font_size=22)
        row2.move_to([0.0, 0.9, 0])
        self.play(FadeIn(row2), run_time=0.4)

        row3 = Text("days = capacity / (avg_mA x 24)", font=DISPLAY, color=INK, font_size=22)
        row3.move_to([0.0, 0.1, 0])
        self.play(FadeIn(row3), run_time=0.4)

        sep2 = Line([-5.5, -0.45, 0], [5.5, -0.45, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_pre = LabelChip("COMPUTE BEFORE PROTOTYPE", accent=CRIMSON, size=20)
        chip_pre.move_to([0.0, -1.1, 0])
        self.play(GrowFromCenter(chip_pre), run_time=0.4)

        foot = Text("What kills products is almost never accuracy.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -1.95, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps -- action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps card: pull datasheet current, sweep frequency, check duty cycle."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· pull active_mA and sleep_uA from the datasheet",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("or measure with a power monitor on the real hardware",
                    font=SERIF, color=INK, font_size=17)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· sweep freq and check duty cycle",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("duty > 10%  ·  race-to-sleep or lower frequency is the first lever",
                    font=SERIF, color=INK, font_size=17)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
