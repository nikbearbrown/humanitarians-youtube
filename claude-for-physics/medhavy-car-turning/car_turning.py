"""car_turning.py — Chapter 4, Acceleration Vector.

A car rounds a curve at constant speed. The speedometer never moves, but the
velocity *vector* does — direction changes even though magnitude doesn't —
so the car is accelerating, and that acceleration points toward the inside
of the curve. medhavy palette (Okabe-Ito), one rotating accent per beat.

Orientation-aware, one file renders either aspect (same doctrine as
ball_and_feather.py): frame_height stays 8 in both, only frame_width changes.
  - Landscape (16:9, deep-dive/book): no intro card, no outro card.
  - Portrait (9:16, short-form): title card + burned-in captions.

Render (16:9 deep-dive):
  manim -qh car_turning.py CarTurning
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching car_turning.py CarTurning
"""
import json
import textwrap
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).parent
SHEET = json.loads((HERE / "beat_sheet.json").read_text())
DURS = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}
NARR = {b["beat_id"]: b["narration_text"] for b in SHEET["beats"]}
TITLE = SHEET["metadata"]["title"]


# config.frame_width does NOT auto-recompute from -r's aspect ratio in this
# Manim version — it silently stays at the 16:9 default even though
# pixel_width/pixel_height/aspect_ratio all update correctly (verified
# directly: setting config.pixel_width/pixel_height alone leaves frame_width
# unchanged). Detect orientation from pixel dimensions instead, and force
# frame_width to the correct value ourselves — same fix as ball_and_feather.py.
PORTRAIT = config.pixel_width < config.pixel_height
if PORTRAIT:
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

# ---- medhavy palette (Okabe-Ito, colorblind-safe) ----
# Background overridden to pure white per professor feedback (same override
# applied in ball_and_feather.py) — accent colors unchanged.
CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

CAR_COLOR = TEAL
V_COLOR = CRIMSON
A_COLOR = SLATE

config.background_color = CREAM

SAFE_MARGIN = 0.6


def safe_half_w():
    return config.frame_width / 2 - SAFE_MARGIN


def safe_half_h():
    return config.frame_height / 2 - SAFE_MARGIN


TOP_Y = safe_half_h() - 0.6
CAPTION_Y = -safe_half_h() + 0.5   # only used when PORTRAIT

# The road is a dome-shaped arc (start_angle 20 deg, sweep 140 deg, passing
# through 90 deg at the top) confined to the UPPER part of the frame, with
# its geometry computed explicitly below rather than guessed — the road's
# own bounding box (peak = center_y + radius, endpoints = center_y +
# radius*sin(20deg)) is checked against TOP_Y and safe_half_w before use.
START_ANGLE = 20 * DEGREES
SWEEP_ANGLE = 140 * DEGREES

if PORTRAIT:
    ROAD_RADIUS = 1.5
    ROAD_CENTER_Y = 0.6
    CAR_SIZE = 0.24
    V_LEN, A_LEN = 0.6, 0.5
    FONT_LABEL, FONT_EQ, FONT_FINAL = 16, 22, 18
    WORKSPACE_Y = -1.1   # B02 delta-v construction — clear of road min (~1.11)
    FINAL_Y = -1.5        # B04 punchline — pushed up for clearance from the caption band (was -1.8, shadowed it)
else:
    ROAD_RADIUS = 1.8
    ROAD_CENTER_Y = 0.8
    CAR_SIZE = 0.4
    V_LEN, A_LEN = 1.1, 0.9
    FONT_LABEL, FONT_EQ, FONT_FINAL = 24, 40, 30
    WORKSPACE_Y = -0.6    # B02 delta-v construction — clear of road min (~1.42)
    FINAL_Y = -2.3         # B04 punchline

ROAD_CENTER = np.array([0.0, ROAD_CENTER_Y, 0.0])
# sanity-checked bounds (peak must stay under TOP_Y, span under safe_half_w):
#   peak_y = ROAD_CENTER_Y + ROAD_RADIUS ; min_y = ROAD_CENTER_Y + ROAD_RADIUS*sin(20deg)
#   half_span_x = ROAD_RADIUS*cos(20deg)

FONT_MASS = 24  # unused here, kept for parity — speed readout font instead
CAPTION_FONT = 15
CAPTION_STYLE = "PT Sans"  # switched from Open Sans — Open Sans exhibited mid-word gap artifacts when rendered by Manim/Pango at this size (confirmed on ball_and_feather.py)
CAPTION_WRAP = 30

TITLE_DURATION = 0.0  # no separate title card anymore: question_card() is the sole
# opening card and starts at t=0, so the caption schedule (which is keyed to
# B00Q's narration) needs no offset before it begins
CAPTION_WORDS_PER_CHUNK = 7  # short subtitle-style phrases, not the whole beat's narration


def build_caption_schedule():
    """(start_s, end_s, text) for every short caption chunk across the whole
    video, in absolute self.time coordinates — a whole beat's narration is far
    too long to show as one on-screen block (confirmed: it overflowed the
    frame in rain_relative_motion.py's first cut); real captions are short
    phrases that cycle, timed proportionally to each chunk's share of that
    beat's measured duration. (Ported from ball_and_feather.py.)"""
    schedule = []
    t = TITLE_DURATION
    for b in SHEET["beats"]:
        bid = b["beat_id"]
        dur = DURS[bid]
        words = NARR[bid].split()
        chunks = [
            " ".join(words[i:i + CAPTION_WORDS_PER_CHUNK])
            for i in range(0, len(words), CAPTION_WORDS_PER_CHUNK)
        ] or [""]
        chunk_dur = dur / len(chunks)
        for c in chunks:
            schedule.append((t, t + chunk_dur, c))
            t += chunk_dur
    return schedule


def make_road():
    return Arc(
        radius=ROAD_RADIUS, start_angle=START_ANGLE, angle=SWEEP_ANGLE,
        arc_center=ROAD_CENTER, color=INK, stroke_width=5,
    )


def point_on_road(road, alpha):
    return road.point_from_proportion(alpha)


def tangent_on_road(road, alpha, eps=0.002):
    a2, a1 = min(alpha + eps, 1.0), max(alpha - eps, 0.0)
    d = road.point_from_proportion(a2) - road.point_from_proportion(a1)
    n = np.linalg.norm(d)
    return d / n if n > 0 else np.array([1.0, 0.0, 0.0])


def inward_on_road(road, alpha):
    p = point_on_road(road, alpha)
    d = ROAD_CENTER - p
    n = np.linalg.norm(d)
    return d / n if n > 0 else np.array([0.0, 1.0, 0.0])


def make_car():
    return Square(side_length=CAR_SIZE, color=INK, fill_color=CAR_COLOR, fill_opacity=1)


class CarTurning(Scene):
    def construct(self):
        self.road = make_road()
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_velocity_rotates()
        self.b02_delta_v()
        self.b03_acceleration_inward()
        self.b04_outro()

    def wait(self, duration=1.0, stop_condition=None, frozen_frame=None):
        # Manim's "frozen frame" optimization skips per-frame updater calls
        # during a wait when it thinks nothing is animating, which silently
        # freezes the caption updater for the wait's full duration (confirmed
        # bug, ball_and_feather.py). Force real per-frame ticking whenever
        # captions are live.
        if PORTRAIT and frozen_frame is None:
            frozen_frame = False
        return super().wait(duration, stop_condition=stop_condition, frozen_frame=frozen_frame)

    # ---------------- Portrait-only: driving question / title card ------
    # Sole opening card for the short: the driving question IS the title —
    # no separate concept-title screen precedes it. Ported from
    # ball_and_feather.py: poses the video's question, in both on-screen
    # text and narration (beat B00Q, its own Kokoro line), before any
    # physics explanation begins. Landscape's construct() never calls this.
    def question_card(self):
        dur = DURS.get("B00Q", 4.0)
        q_text = NARR.get("B00Q", "")
        wrapped = "\n".join(textwrap.wrap(q_text, width=22))
        question = Text(
            wrapped, font_size=30, color=INK, line_spacing=1.3
        ).move_to(ORIGIN)
        max_w = 2 * safe_half_w()
        if question.width > max_w:
            question.scale_to_fit_width(max_w)
        underline = Line(
            question.get_corner(DOWN + LEFT) + DOWN * 0.25,
            question.get_corner(DOWN + RIGHT) + DOWN * 0.25,
            color=CRIMSON, stroke_width=5,
        )
        self.play(Write(question), Create(underline), run_time=1.0)
        self.wait(max(dur - 1.6, 0.5))
        self.play(FadeOut(question), FadeOut(underline), run_time=0.6)

    # ---------------- Portrait-only: burned-in captions ----------------
    # Ported from ball_and_feather.py: a global updater keyed on self.time
    # cycles short 7-word caption chunks, independent of each beat's own
    # choreography — no per-beat wiring needed.
    def _init_captions(self):
        self.caption_schedule = build_caption_schedule()
        self.caption_idx = -1
        caption_mobj = VGroup()

        def updater(m):
            t = self.renderer.time
            idx = self.caption_idx
            for i, (start, end, _text) in enumerate(self.caption_schedule):
                if start <= t < end:
                    idx = i
                    break
            if idx == self.caption_idx or idx >= len(self.caption_schedule):
                return
            self.caption_idx = idx
            _, _, chunk_text = self.caption_schedule[idx]
            if not chunk_text:
                m.become(VGroup())
                return
            wrapped = "\n".join(textwrap.wrap(chunk_text, width=CAPTION_WRAP))
            text = Text(
                wrapped, font_size=CAPTION_FONT, color=INK, line_spacing=1.15, font=CAPTION_STYLE
            ).move_to([0, CAPTION_Y, 0])
            backing = SurroundingRectangle(
                text, color=SLATE, fill_color=CREAM, fill_opacity=0.92, buff=0.2, corner_radius=0.08,
            )
            m.become(VGroup(backing, text))

        caption_mobj.add_updater(updater)
        self.add(caption_mobj)

    # ---------------- B00 — Hook ----------------
    def b00_hook(self):
        self.car = make_car().move_to(point_on_road(self.road, 0.0))
        readout = Text("60 km/h", font_size=FONT_LABEL, color=INK)
        readout_box = SurroundingRectangle(readout, color=SLATE, buff=0.18, corner_radius=0.06)
        readout_group = VGroup(readout_box, readout).to_corner(UR, buff=0.5)

        self.play(Create(self.road), FadeIn(self.car), FadeIn(readout_group), run_time=1.2)
        self.readout_group = readout_group
        self.wait(max(DURS["B00"] - 1.2, 0.3), frozen_frame=False)

    # ---------------- B01 — velocity vector rotates ----------------
    def b01_velocity_rotates(self):
        snap_alphas = [0.12, 0.28, 0.44]
        snaps = VGroup()
        for a in snap_alphas:
            p = point_on_road(self.road, a)
            t = tangent_on_road(self.road, a)
            arrow = Arrow(p, p + t * V_LEN, color=V_COLOR, buff=0, stroke_width=6)
            arrow.set_opacity(0.3)
            snaps.add(arrow)
        self.snaps = snaps
        self.play(FadeIn(snaps), run_time=0.5)

        v_arrow = Arrow(
            point_on_road(self.road, 0.0),
            point_on_road(self.road, 0.0) + tangent_on_road(self.road, 0.0) * V_LEN,
            color=V_COLOR, buff=0, stroke_width=8,
        )
        v_label = Text("v", font_size=FONT_LABEL, color=V_COLOR)
        v_label.add_updater(lambda m: m.next_to(v_arrow.get_end(), UP, buff=0.1))
        self.add(v_label)

        def updater(mob, alpha):
            a = 0.05 + alpha * 0.50
            p = point_on_road(self.road, a)
            t = tangent_on_road(self.road, a)
            self.car.move_to(p)
            v_arrow.put_start_and_end_on(p, p + t * V_LEN)

        self.v_arrow = v_arrow
        self.add(v_arrow)
        run_time = max(DURS["B01"] - 1.0, 1.5)
        self.play(UpdateFromAlphaFunc(self.car, updater), rate_func=linear, run_time=run_time)
        v_label.clear_updaters()
        self.v_label = v_label

    # ---------------- B02 — delta v ----------------
    def b02_delta_v(self):
        self.play(FadeOut(self.v_label), run_time=0.3)

        # snaps[0] (alpha 0.12) and snaps[2] (alpha 0.44) — wider angular
        # separation than the adjacent 0.12/0.28 pair, so the two vectors
        # and the delta-v triangle between them are legible rather than a
        # cramped near-parallel pair
        v1, v2 = self.snaps[0], self.snaps[2]
        origin = np.array([0.0, WORKSPACE_Y, 0.0])
        # opacity is baked into the TARGET mobjects rather than animated
        # separately via .animate on the same v1/v2 — combining a Transform
        # with an .animate call on the same mobject in one self.play() is a
        # known Manim conflict where one animation's interpolation silently
        # wins over the other (this was why v1/v2 never actually relocated
        # to `origin` — the Transform's own position update was clobbered)
        v1_target = Arrow(
            origin, origin + tangent_on_road(self.road, 0.12) * V_LEN,
            color=V_COLOR, buff=0, stroke_width=6,
        ).set_opacity(1)
        v2_target = Arrow(
            origin, origin + tangent_on_road(self.road, 0.44) * V_LEN,
            color=V_COLOR, buff=0, stroke_width=6,
        ).set_opacity(1)
        self.play(
            Transform(v1, v1_target), Transform(v2, v2_target),
            run_time=1.0,
        )

        delta_v = Arrow(v1.get_end(), v2.get_end(), color=V_COLOR, buff=0, stroke_width=6)
        delta_v_label = Text(
            "Δv", font_size=FONT_LABEL, color=V_COLOR
        ).next_to(delta_v, UR, buff=0.2)
        eq = MathTex(
            r"a = \frac{\Delta v}{\Delta t}", color=INK, font_size=FONT_EQ
        ).next_to(VGroup(v1, v2, delta_v), DOWN, buff=0.4)

        self.play(GrowArrow(delta_v), FadeIn(delta_v_label), run_time=0.8)
        self.play(Write(eq), run_time=0.8)
        self.wait(max(DURS["B02"] - 2.6, 0.3), frozen_frame=False)

        self.play(
            FadeOut(v1), FadeOut(v2), FadeOut(delta_v), FadeOut(delta_v_label), FadeOut(eq),
            FadeOut(self.snaps[1]),  # the unused middle snapshot (alpha 0.28), still faded on the road
            run_time=0.5,
        )

    # ---------------- B03 — acceleration points inward ----------------
    def b03_acceleration_inward(self):
        v_label = Text("v", font_size=FONT_LABEL, color=V_COLOR)
        v_label.add_updater(lambda m: m.next_to(self.v_arrow.get_end(), UP, buff=0.1))
        a_arrow = Arrow(
            point_on_road(self.road, 0.55),
            point_on_road(self.road, 0.55) + inward_on_road(self.road, 0.55) * A_LEN,
            color=A_COLOR, buff=0, stroke_width=8,
        )
        a_label = Text("a", font_size=FONT_LABEL, color=A_COLOR)
        a_label.add_updater(lambda m: m.next_to(a_arrow.get_end(), a_arrow.get_unit_vector(), buff=0.1))
        self.add(v_label, a_arrow, a_label)
        self.play(FadeIn(v_label), GrowArrow(a_arrow), FadeIn(a_label), run_time=0.8)

        def updater(mob, alpha):
            a = 0.55 + alpha * 0.40
            p = point_on_road(self.road, a)
            t = tangent_on_road(self.road, a)
            n = inward_on_road(self.road, a)
            self.car.move_to(p)
            self.v_arrow.put_start_and_end_on(p, p + t * V_LEN)
            a_arrow.put_start_and_end_on(p, p + n * A_LEN)

        run_time = max(DURS["B03"] - 1.6, 1.5)
        self.play(UpdateFromAlphaFunc(self.car, updater), rate_func=linear, run_time=run_time)
        v_label.clear_updaters()
        a_label.clear_updaters()
        self.v_label, self.a_arrow, self.a_label = v_label, a_arrow, a_label

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        final = Text(
            "Constant speed. Changing direction. Still accelerating.",
            font_size=FONT_FINAL, color=INK,
        )
        if PORTRAIT:
            final = Text(
                "\n".join(textwrap.wrap(
                    "Constant speed. Changing direction. Still accelerating.", width=22
                )),
                font_size=FONT_FINAL, color=INK, line_spacing=1.2,
            )
        final.move_to([0, FINAL_Y, 0])
        final_bg = SurroundingRectangle(
            final, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.2,
        )
        self.play(FadeIn(final_bg), FadeIn(final), run_time=0.6)
        self.wait(max(DURS["B04"] - 0.6, 0.3), frozen_frame=False)
