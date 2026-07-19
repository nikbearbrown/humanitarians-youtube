"""vox_scenes.py — medhavy-vol4-gate-bloch/short (9:16 portrait)
Reel: Quantum Gates — H and S on Bloch sphere (portrait)
Palette: medhavy (Okabe-Ito)

Physics:
  H|0> = |+>   (north pole to equator, xz rotation)
  S|+> = |i>   (equator, 90° phi rotation in xy plane)
  H*H = I      (self-inverse)

Portrait layout:
  Safe area: ±1.95x / ±3.4y
  Single large Bloch circle, center at (0, 0.3), radius R=1.6
  xz cross-section showing H gate

  State vectors (in scene units from circle center):
    |0> at north: (0, +1.6) → scene (0, 1.9)
    |+> at equator right: (+1.6, 0) → scene (1.6, 0.3)
    S gate arc: equatorial plane shown as smaller circle below

  Chips at y=-2.65 and y=-3.1
"""

import sys, json, pathlib, os
os.environ.setdefault("VOX_PALETTE", "medhavy")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np

DUR: dict = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

_DEFAULTS = {"B03": 22.0}

def _dur(bid): return DUR.get(bid, _DEFAULTS.get(bid, 10.0))
def _ink_text(copy: str, font_size: int = 24, font: str = SERIF, **kw) -> "Text":
    return Text(copy, font=font, color=INK, font_size=font_size, **kw)


class B03_GateBlochRun(Scene):
    """Portrait Bloch circle schematic showing H and S gates.

    Single xz cross-section panel; S gate shown as equatorial arc annotation.
    All label positions as pure floats, Gate A safe.
    """

    def construct(self):
        dur = _dur("B03")

        R = 1.55   # circle radius; center at (cx, cy)
        cx, cy = 0.0, 0.3

        # State positions (from circle center + offset to scene coords)
        def state_pos(theta_deg, phi_scene_offset_x=0.0, phi_scene_offset_y=0.0):
            """theta_deg: 0=north, 90=equator(+x), 180=south."""
            rad = np.radians(theta_deg)
            x = cx + R * np.sin(rad) + phi_scene_offset_x
            y = cy + R * np.cos(rad) + phi_scene_offset_y
            return [x, y, 0]

        north = state_pos(0)    # |0>: (0.0, 1.85)
        east  = state_pos(90)   # |+>: (1.55, 0.3)
        south = state_pos(180)  # (0.0, -1.25)

        # Header
        header = _ink_text("H and S Gates", font_size=18, font=DISPLAY)
        header.move_to([0, 3.15, 0])
        self.play(FadeIn(header), run_time=0.4)

        # Bloch circle: xz cross-section
        bloch_circle = Circle(radius=R, color=SLATE, stroke_width=1.5, fill_opacity=0)
        bloch_circle.move_to([cx, cy, 0])
        self.play(Create(bloch_circle), run_time=0.5)

        # Axes inside circle
        z_axis = Line(start=[cx, cy - R - 0.15, 0], end=[cx, cy + R + 0.15, 0],
                      stroke_width=1.0, color=SLATE)
        x_axis = Line(start=[cx - R - 0.15, cy, 0], end=[cx + R + 0.15, cy, 0],
                      stroke_width=1.0, color=SLATE)
        z_lbl = _ink_text("z", font_size=14)
        z_lbl.move_to([cx + 0.18, cy + R + 0.25, 0])
        x_lbl = _ink_text("x", font_size=14)
        x_lbl.move_to([cx + R + 0.30, cy, 0])
        self.play(FadeIn(z_axis), FadeIn(x_axis), FadeIn(z_lbl), FadeIn(x_lbl), run_time=0.3)

        # |0> at north pole: TEAL arrow
        arrow0 = Arrow(start=[cx, cy, 0], end=north, color=TEAL,
                       buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.15)
        self.play(Create(arrow0), run_time=0.4)
        lbl0 = _ink_text("|0>", font_size=16)
        lbl0.move_to([north[0] - 0.35, north[1] + 0.22, 0])
        self.play(FadeIn(lbl0), run_time=0.25)

        # H gate arc: from north to east (90° rotation), Arc from 90° to 0° in standard coords
        # In Manim: Arc with start_angle and angle; north is at angle 90° (pi/2), east is at 0°
        h_arc = Arc(radius=R * 0.8, start_angle=PI / 2, angle=-PI / 2,
                    color=TEAL, stroke_width=2.0)
        h_arc.move_arc_center_to([cx, cy, 0])
        h_label = _ink_text("H", font_size=16)
        h_label.move_to([cx + R * 0.5, cy + R * 0.5, 0])
        self.play(Create(h_arc), FadeIn(h_label), run_time=0.5)

        # |+> at east: TEAL arrow
        arrowP = Arrow(start=[cx, cy, 0], end=east, color=TEAL,
                       buff=0, stroke_width=2.5, max_tip_length_to_length_ratio=0.15)
        self.play(Create(arrowP), run_time=0.4)
        lblP = _ink_text("|+>", font_size=16)
        lblP.move_to([east[0] + 0.32, east[1], 0])
        self.play(FadeIn(lblP), run_time=0.25)

        # S gate: shown as annotation (equatorial plane rotation)
        # Small circle at bottom of diagram to represent xy view
        s_note = _ink_text("S gate: +90 deg in phi", font_size=13)
        s_note.move_to([cx, south[1] - 0.45, 0])
        self.play(FadeIn(s_note), run_time=0.3)

        # |i> position in xy plane (behind the xz section, annotate only)
        i_note = _ink_text("|i>", font_size=16)
        i_note.move_to([cx - 0.70, south[1] - 0.80, 0])
        self.play(FadeIn(i_note), run_time=0.25)

        # H*H = I annotation
        hh_note = _ink_text("H x H = I", font_size=14)
        hh_note.move_to([cx - 0.90, cy - 0.35, 0])
        self.play(FadeIn(hh_note), run_time=0.25)

        # --- Chips ---
        h_chip = LabelChip("H: pole to equator", accent=TEAL, size=16)
        h_chip.move_to([-0.50, -2.65, 0])
        self.play(GrowFromCenter(h_chip), run_time=0.4)

        s_chip = LabelChip("S: +90 deg phi", accent=CRIMSON, size=16)
        s_chip.move_to([0.55, -3.08, 0])
        self.play(GrowFromCenter(s_chip), run_time=0.35)

        elapsed = (0.4 + 0.5 + 0.3 + 0.4 + 0.25 + 0.5 + 0.4 + 0.25 + 0.3 + 0.25 + 0.25 + 0.4 + 0.35)
        self.wait(max(0.5, dur - elapsed))
