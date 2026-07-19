"""vox_scenes.py — embedded-ai/youtube/cli-brownout
Reel: A Battery Can Be Full and Still Crash Your Device
Palette: teardown (white ground, ink originals, crimson = damage/problem)

teardown token mapping (from vox_graphics.py):
  GROUND  #FFFFFF  background
  INK     #2A1A0E  originals, axes, all text
  CRIMSON #C8102E  sag / reset event / error
  SLATE   #545454  structure, neutral chips

Gate W colour rules (teardown on GROUND #FFFFFF):
  INK on GROUND -> contrast ~21:1 (AAA)
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
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

_DEFAULTS = {"B01": 14.0, "B04": 17.0, "B06": 12.0, "B07": 11.0, "B08": 10.0}
def _dur(bid):
    return DUR.get(bid, _DEFAULTS.get(bid, 10.0))

# ── voltage model parameters ───────────────────────────────────────────────────
V_OC     = 3.0    # open-circuit voltage (V)
R_INT    = 1000   # internal resistance (ohm)
I_IDLE   = 0.001  # idle current (A)
I_PULSE  = 0.008  # inference pulse current (A)
V_RESET  = 2.0    # brownout reset threshold (V)

# Pulse window: t in [0.3, 0.55] (fraction of 200ms total)
# i.e. 60ms to 110ms

# ── coordinate mapping ─────────────────────────────────────────────────────────
# t in [0, 1] = 0 to 200ms, mapped to x in [-5.5, 5.5]
# V in [1.5, 3.3] mapped to y in [-2.5, 2.8]
T_TOTAL  = 0.200  # seconds
V_PLOT_LO, V_PLOT_HI = 1.5, 3.3

X0, X1 = -5.5, 5.5
Y0, Y1 = -2.5, 2.8

def _tx(t_frac):
    return X0 + t_frac * (X1 - X0)

def _vy(v):
    return Y0 + (v - V_PLOT_LO) / (V_PLOT_HI - V_PLOT_LO) * (Y1 - Y0)

def _v_no_cap(t_frac):
    """Voltage without capacitor."""
    i = I_PULSE if 0.30 <= t_frac <= 0.55 else I_IDLE
    return V_OC - i * R_INT

def _v_with_cap(t_frac, C=100e-6, dt=0.001/0.200):
    """Voltage with 100uF bulk cap -- simplified RC discharge model.
    During pulse: cap discharges to supply extra current beyond 3mA.
    Outside pulse: cap recharges from cell.
    We pre-compute the trace as a parametric so Manim can use it.
    """
    return _v_cap_array[min(int(t_frac / 0.005), len(_v_cap_array) - 1)]

# Pre-compute cap trace at 200 steps
_DT = 0.001   # 1ms time step
_N  = int(T_TOTAL / _DT)  # 200 steps
_t_arr = np.linspace(0, 1, _N)

C = 100e-6   # 100uF
V_cap = V_OC  # initial cap voltage
_v_cap_arr = []
for _k in range(_N):
    tf = _t_arr[_k]
    i_demand = I_PULSE if 0.30 <= tf <= 0.55 else I_IDLE
    i_cell = min(i_demand, 3e-3)  # cell limited to ~3mA
    i_cap  = max(0, i_demand - i_cell)
    V_cap  = V_cap - i_cap * _DT / C  # cap discharge
    # V from cell accounting for cell's own drop
    V_supply = V_OC - i_cell * R_INT + (V_cap - (V_OC - i_cell * R_INT)) * np.exp(-_DT / (R_INT * C))
    _v_cap_arr.append(float(np.clip(V_supply, V_PLOT_LO, V_PLOT_HI)))

_v_cap_array = _v_cap_arr


def _trace_no_cap_pt(t):
    v = _v_no_cap(t)
    return np.array([_tx(t), _vy(v), 0.0])

def _trace_cap_pt(t):
    idx = min(int(t / 0.005), len(_v_cap_array) - 1)
    v = _v_cap_array[idx]
    return np.array([_tx(t), _vy(v), 0.0])


# =============================================================================
# B01_Problem — title card: CR2032 internal resistance, inference burst, reset
# =============================================================================
class B01_Problem(Scene):
    """Title card: coin cell + internal resistance + inference burst -> brownout."""

    def construct(self):
        dur = _dur("B01")

        hdr = Text("BROWNOUT: FULL BATTERY, DEAD DEVICE", font=DISPLAY, color=INK, font_size=28)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.5)

        chip_cell = LabelChip("CR2032  3V NOMINAL", accent=SLATE, size=22)
        chip_cell.move_to([-2.8, 1.9, 0])

        chip_limit = LabelChip("3mA SUSTAINED LIMIT", accent=CRIMSON, size=22)
        chip_limit.move_to([2.8, 1.9, 0])

        self.play(GrowFromCenter(chip_cell), GrowFromCenter(chip_limit), run_time=0.5)

        sub = Text("8mA inference burst -> supply sags below 2V reset threshold",
                   font=DISPLAY, color=INK, font_size=18)
        sub.move_to([0.0, 1.1, 0])
        self.play(FadeIn(sub), run_time=0.4)

        sep2 = Line([-5.5, 0.5, 0], [5.5, 0.5, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        chip_energy = LabelChip("ENERGY: how long", accent=SLATE, size=22)
        chip_energy.move_to([-2.8, -0.15, 0])

        chip_instant = LabelChip("DELIVERY: whether at all", accent=CRIMSON, size=22)
        chip_instant.move_to([2.8, -0.15, 0])

        self.play(GrowFromCenter(chip_energy), GrowFromCenter(chip_instant), run_time=0.5)

        q = Text("the battery was full -- the reset line saw the sag",
                 font=SERIF, color=INK, font_size=22)
        q.move_to([0.0, -1.2, 0])
        self.play(FadeIn(q), run_time=0.5)

        elapsed = 0.4 + 0.5 + 0.5 + 0.4 + 0.4 + 0.5 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B04_Brownout — voltage trace with sag crossing reset line
# =============================================================================
class B04_Brownout(Scene):
    """Voltage trace: idle -> inference pulse -> sag below V_RESET (CRIMSON)."""

    def construct(self):
        dur = _dur("B04")

        hdr = Text("BROWNOUT SIMULATION", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X0, Y0, 0], [X1 + 0.2, Y0, 0], stroke_width=1.5, color=INK)
        ax_y = Line([X0, Y0, 0], [X0, Y1 + 0.2, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.4)
        self.play(Create(ax_y), run_time=0.4)

        x_lbl = Text("time (200ms total)", font=DISPLAY, color=INK, font_size=15)
        x_lbl.move_to([0.0, -3.0, 0])
        y_lbl = Text("Supply V", font=DISPLAY, color=INK, font_size=15)
        y_lbl.rotate(PI / 2)
        y_lbl.move_to([-5.8, 0.3, 0])
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── brownout reset line (SLATE dashed) ────────────────────────────────
        reset_y = _vy(V_RESET)
        reset_line = DashedLine([X0, reset_y, 0], [X1, reset_y, 0],
                                stroke_width=1.5, color=SLATE, dash_length=0.2)
        self.play(Create(reset_line), run_time=0.5)

        reset_lbl = Text("V_reset = 2.0V", font=DISPLAY, color=SLATE, font_size=16)
        reset_lbl.move_to([X1 - 1.2, reset_y + 0.3, 0])
        self.play(FadeIn(reset_lbl), run_time=0.3)

        # ── nominal trace: pre-pulse (INK) ────────────────────────────────────
        # Draw the pre-pulse portion (t=0 to 0.30)
        def _pre_pulse(t):
            t_frac = t * 0.30
            return _trace_no_cap_pt(t_frac)

        pre_trace = ParametricFunction(_pre_pulse, t_range=[0.0, 1.0, 0.01],
                                       color=INK, stroke_width=2.5)
        self.play(Create(pre_trace), run_time=0.5)

        # ── sag portion (CRIMSON: below V_RESET during pulse) ─────────────────
        def _pulse_sag(t):
            t_frac = 0.30 + t * 0.25
            return _trace_no_cap_pt(t_frac)

        sag_trace = ParametricFunction(_pulse_sag, t_range=[0.0, 1.0, 0.01],
                                       color=CRIMSON, stroke_width=3.0)
        self.play(Create(sag_trace), run_time=0.7)

        # ── post-pulse recovery (INK) ─────────────────────────────────────────
        def _post_pulse(t):
            t_frac = 0.55 + t * 0.45
            return _trace_no_cap_pt(t_frac)

        post_trace = ParametricFunction(_post_pulse, t_range=[0.0, 1.0, 0.01],
                                        color=INK, stroke_width=2.5)
        self.play(Create(post_trace), run_time=0.4)

        # ── reset chip ────────────────────────────────────────────────────────
        reset_chip = LabelChip("RESET TRIGGERED", accent=CRIMSON, size=20)
        reset_chip.move_to([0.0, -2.0, 0])
        self.play(GrowFromCenter(reset_chip), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.3 + 0.5 + 0.3 + 0.5 + 0.7 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B06_BrownoutCap — same trace with 100uF cap: sag blunted
# =============================================================================
class B06_BrownoutCap(Scene):
    """Original trace (SLATE, faint, sags) and capped trace (INK, stays above)."""

    def construct(self):
        dur = _dur("B06")

        hdr = Text("100uF CAP  --  SAG BLUNTED", font=DISPLAY, color=INK, font_size=26)
        hdr.move_to([0.0, 3.2, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        # ── axes ──────────────────────────────────────────────────────────────
        ax_x = Line([X0, Y0, 0], [X1 + 0.2, Y0, 0], stroke_width=1.5, color=INK)
        ax_y = Line([X0, Y0, 0], [X0, Y1 + 0.2, 0], stroke_width=1.5, color=INK)
        self.play(Create(ax_x), run_time=0.3)
        self.play(Create(ax_y), run_time=0.3)

        # ── reset line ────────────────────────────────────────────────────────
        reset_y = _vy(V_RESET)
        reset_line = DashedLine([X0, reset_y, 0], [X1, reset_y, 0],
                                stroke_width=1.5, color=SLATE, dash_length=0.2)
        self.play(Create(reset_line), run_time=0.4)

        reset_lbl = Text("V_reset = 2.0V", font=DISPLAY, color=SLATE, font_size=16)
        reset_lbl.move_to([X1 - 1.2, reset_y + 0.3, 0])
        self.play(FadeIn(reset_lbl), run_time=0.3)

        # ── original trace (SLATE, faint) ─────────────────────────────────────
        orig_trace = ParametricFunction(_trace_no_cap_pt, t_range=[0.0, 1.0, 0.005],
                                        color=SLATE, stroke_width=1.5)
        orig_trace.set_stroke(opacity=0.5)
        self.play(Create(orig_trace), run_time=0.8)

        orig_lbl = Text("no cap  (resets)", font=DISPLAY, color=SLATE, font_size=16)
        orig_lbl.move_to([-2.5, -2.2, 0])
        self.play(FadeIn(orig_lbl), run_time=0.3)

        # ── capped trace (INK, full opacity) ─────────────────────────────────
        cap_trace = ParametricFunction(_trace_cap_pt, t_range=[0.0, 1.0, 0.005],
                                       color=INK, stroke_width=2.5)
        self.play(Create(cap_trace), run_time=0.9)

        cap_lbl = Text("100uF cap  (safe)", font=DISPLAY, color=INK, font_size=16)
        cap_lbl.move_to([2.5, -2.2, 0])
        self.play(FadeIn(cap_lbl), run_time=0.3)

        # ── verdict chip ──────────────────────────────────────────────────────
        verdict_chip = LabelChip("SAG BLUNTED  CAP SAVES IT", accent=INK, size=20)
        verdict_chip.move_to([0.0, -3.0, 0])
        self.play(GrowFromCenter(verdict_chip), run_time=0.4)

        elapsed = 0.4 + 0.3 + 0.3 + 0.4 + 0.3 + 0.8 + 0.3 + 0.9 + 0.3 + 0.4
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B07_Summary — two power questions, one word
# =============================================================================
class B07_Summary(Scene):
    """Recap: energy (how long) vs instantaneous delivery (whether at all)."""

    def construct(self):
        dur = _dur("B07")

        hdr = Text("THE LESSON", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        row1 = Text("energy", font=DISPLAY, color=INK, font_size=24)
        row1.move_to([-3.0, 1.6, 0])
        chip1 = LabelChip("HOW LONG", accent=SLATE, size=22)
        chip1.move_to([2.5, 1.6, 0])
        self.play(FadeIn(row1), run_time=0.4)
        self.play(GrowFromCenter(chip1), run_time=0.4)

        row2 = Text("instantaneous delivery", font=DISPLAY, color=INK, font_size=24)
        row2.move_to([-2.2, 0.6, 0])
        chip2 = LabelChip("WHETHER AT ALL", accent=CRIMSON, size=22)
        chip2.move_to([3.0, 0.6, 0])
        self.play(FadeIn(row2), run_time=0.4)
        self.play(GrowFromCenter(chip2), run_time=0.4)

        sep2 = Line([-5.5, 0.0, 0], [5.5, 0.0, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        foot = Text("Datasheets quote the first. The field punishes the second.",
                    font=SERIF, color=INK, font_size=21)
        foot.move_to([0.0, -0.75, 0])
        self.play(FadeIn(foot), run_time=0.5)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.5
        self.wait(max(0.5, dur - elapsed))


# =============================================================================
# B08_NextSteps — action items for the viewer
# =============================================================================
class B08_NextSteps(Scene):
    """Next-steps: find reset threshold, measure burst, size a cap."""

    def construct(self):
        dur = _dur("B08")

        hdr = Text("YOUR MOVE", font=DISPLAY, color=INK, font_size=32)
        hdr.move_to([0.0, 3.0, 0])
        self.play(FadeIn(hdr), run_time=0.4)

        sep = Line([-5.5, 2.55, 0], [5.5, 2.55, 0], stroke_width=1.2, color=SLATE)
        sep.set_stroke(opacity=0.6)
        self.play(Create(sep), run_time=0.4)

        step1 = Text("· find brownout reset threshold in the datasheet",
                     font=DISPLAY, color=INK, font_size=20)
        step1.move_to([0.0, 1.7, 0])
        self.play(FadeIn(step1), run_time=0.4)

        sub1 = Text("usually 1.8V to 2.5V depending on regulator",
                    font=SERIF, color=INK, font_size=18)
        sub1.move_to([0.0, 1.05, 0])
        self.play(FadeIn(sub1), run_time=0.4)

        step2 = Text("· estimate or measure inference burst current",
                     font=DISPLAY, color=INK, font_size=20)
        step2.move_to([0.0, 0.1, 0])
        self.play(FadeIn(step2), run_time=0.4)

        sub2 = Text("size a bulk cap  ·  the simulation runs today",
                    font=SERIF, color=INK, font_size=18)
        sub2.move_to([0.0, -0.55, 0])
        self.play(FadeIn(sub2), run_time=0.4)

        sep2 = Line([-5.5, -1.2, 0], [5.5, -1.2, 0], stroke_width=0.8, color=SLATE)
        sep2.set_stroke(opacity=0.4)
        self.play(Create(sep2), run_time=0.4)

        elapsed = 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4 + 0.4
        self.wait(max(0.5, dur - elapsed))
