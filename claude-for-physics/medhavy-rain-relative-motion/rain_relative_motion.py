"""rain_relative_motion.py — Chapter 4, Relative Motion.

Rain falls straight down in the ground frame. In a walker's own frame, that
same rain appears to slant forward into their face — not because the rain
changed, but because relative velocity is vector subtraction: v_rain' =
v_rain - v_walk. medhavy palette (Okabe-Ito), one rotating accent per beat.

Orientation-aware, one file renders either aspect (same doctrine as
ball_and_feather.py / car_turning.py): frame_height stays 8 in both, only
frame_width changes.
  - Landscape (16:9, deep-dive/book): no intro card, no outro card. The
    ground-frame/walker-frame split in B02-B03 is SIDE BY SIDE.
  - Portrait (9:16, short-form): title card + burned-in captions. The split
    becomes a TOP/BOTTOM stack — side-by-side panels don't fit the narrow
    safe width (matches the sketch-explainer portrait-reflow doctrine).

Render (16:9 deep-dive):
  manim -qh rain_relative_motion.py RainRelativeMotion
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching rain_relative_motion.py RainRelativeMotion
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
# Manim version — same fix as ball_and_feather.py / car_turning.py: detect
# orientation from pixel dimensions (which DO update correctly) and force
# frame_width ourselves.
PORTRAIT = config.pixel_width < config.pixel_height
if PORTRAIT:
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

# ---- medhavy palette (Okabe-Ito, colorblind-safe) ----
CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

config.background_color = CREAM

SAFE_MARGIN = 0.6


def safe_half_w():
    return config.frame_width / 2 - SAFE_MARGIN


def safe_half_h():
    return config.frame_height / 2 - SAFE_MARGIN


TOP_Y = safe_half_h() - 0.6
CAPTION_Y = -safe_half_h() + 0.5   # only used when PORTRAIT

CAPTION_FONT = 15
CAPTION_STYLE = "PT Sans"  # switched from Open Sans — Open Sans exhibited mid-word gap artifacts when rendered by Manim/Pango at this size (confirmed on ball_and_feather.py)
CAPTION_WRAP = 30

TITLE_DURATION = 0.0  # no separate title card anymore: question_card() is the sole
# opening card and starts at t=0, so the caption schedule (which is keyed to
# B00Q's narration) needs no offset before it begins
CAPTION_WORDS_PER_CHUNK = 7  # short subtitle-style phrases, not the whole beat's narration

# ---- geometry, explicitly derived (not guessed) and orientation-specific ----
# FIG_SCALE actually scales make_stick_figure/head_pos (an earlier version
# defined FIG_H but never passed it through as a scale factor, so the figure
# silently rendered full-size regardless — confirmed bug, this fixes it).
if PORTRAIT:
    GROUND_Y = 1.6           # single-panel stage (B00/B01), well above the divider
    FIG_SCALE = 0.75
    RAIN_LEN = 0.85
    WALK_LEN = 0.5
    FONT_LABEL, FONT_EQ, FONT_FINAL = 14, 18, 16
    # B02+ stacked layout (top/bottom, not side by side — narrow safe width)
    DIVIDER_Y = 0.9
    PANEL_LABEL_Y = 0.55
    LEFT_TARGET_Y = 2.0
    RIGHT_GROUND_Y = -1.3
    RIGHT_FIG_SCALE = 0.55
    WORKSPACE_GAP = 0.25    # clearance between the figure's head and the vector construction above it
    L_WALK_MAX = 0.35
    L_RAIN = 0.45
    FINAL_Y = -1.85
else:
    GROUND_Y = -0.3
    FIG_SCALE = 1.0
    RAIN_LEN = 1.9
    WALK_LEN = 0.9
    FONT_LABEL, FONT_EQ, FONT_FINAL = 24, 34, 28
    RIGHT_GROUND_Y = GROUND_Y
    RIGHT_FIG_SCALE = 1.0
    WORKSPACE_GAP = 0.25
    L_WALK_MAX = 1.1
    L_RAIN = 0.9
    FINAL_Y = None  # computed relative to right_ground_y in b04_outro

RAIN_DX = 0.55 * FIG_SCALE  # rain arrow offset to the side of the head, scaled with figure size


def build_caption_schedule():
    """(start_s, end_s, text) for every short caption chunk across the whole
    video, in absolute self.time coordinates — ported from ball_and_feather.py
    after a whole-beat caption overflowed the frame here (confirmed bug)."""
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


def make_stick_figure(x, ground_y, scale=1.0):
    s = scale
    head = Circle(radius=0.15 * s, color=INK, stroke_width=3).move_to([x, ground_y + 0.85 * s, 0])
    body = Line([x, ground_y + 0.7 * s, 0], [x, ground_y + 0.35 * s, 0], color=INK, stroke_width=3)
    leg_l = Line([x, ground_y + 0.35 * s, 0], [x - 0.15 * s, ground_y, 0], color=INK, stroke_width=3)
    leg_r = Line([x, ground_y + 0.35 * s, 0], [x + 0.15 * s, ground_y, 0], color=INK, stroke_width=3)
    arm_l = Line([x, ground_y + 0.6 * s, 0], [x - 0.15 * s, ground_y + 0.45 * s, 0], color=INK, stroke_width=3)
    arm_r = Line([x, ground_y + 0.6 * s, 0], [x + 0.15 * s, ground_y + 0.45 * s, 0], color=INK, stroke_width=3)
    return VGroup(head, body, leg_l, leg_r, arm_l, arm_r)


def head_pos(x, ground_y, scale=1.0):
    return np.array([x, ground_y + 0.85 * scale, 0.0])


class RainRelativeMotion(Scene):
    def construct(self):
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_walker_starts()
        self.b02_reframe()
        self.b03_speed_comparison()
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
        self.fig_x = 0.0
        self.figure = make_stick_figure(self.fig_x, GROUND_Y, scale=FIG_SCALE)
        self.ground_line = Line(
            [-safe_half_w(), GROUND_Y, 0], [safe_half_w(), GROUND_Y, 0], color=INK
        )
        rain_x = self.fig_x + RAIN_DX
        head_top = GROUND_Y + 0.85 * FIG_SCALE
        rain_top = min(head_top + RAIN_LEN, TOP_Y)
        self.rain = Arrow(
            [rain_x, rain_top, 0], [rain_x, head_top + 0.05, 0],
            color=SLATE, buff=0, stroke_width=6,
        )
        self.rain_label = Text("v_rain", font_size=FONT_LABEL, color=SLATE).next_to(
            self.rain, RIGHT, buff=0.2
        )
        self.play(
            Create(self.ground_line), FadeIn(self.figure),
            GrowArrow(self.rain), FadeIn(self.rain_label),
            run_time=1.2,
        )
        self.wait(max(DURS["B00"] - 1.2, 0.3), frozen_frame=False)

    # ---------------- B01 — walker starts moving ----------------
    def b01_walker_starts(self):
        walk_arrow = Arrow(
            [self.fig_x - 0.1, GROUND_Y - 0.05, 0], [self.fig_x - 0.1 + WALK_LEN, GROUND_Y - 0.05, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        walk_label = Text("v_walk", font_size=FONT_LABEL, color=CRIMSON).next_to(
            walk_arrow, DOWN, buff=0.15
        )
        self.play(GrowArrow(walk_arrow), FadeIn(walk_label), run_time=0.8)
        self.wait(max(DURS["B01"] - 0.8, 0.3), frozen_frame=False)
        self.walk_arrow, self.walk_label = walk_arrow, walk_label

    # ---------------- B02 — reframe into the walker's view ----------------
    def b02_reframe(self):
        left_group = VGroup(self.figure, self.ground_line, self.rain, self.rain_label,
                             self.walk_arrow, self.walk_label)

        if PORTRAIT:
            # stacked top/bottom (not side by side — the narrow safe width
            # can't fit two panels across); shrink+lift the ground-frame
            # panel to sit clearly ABOVE the divider, well under TOP_Y
            self.play(left_group.animate.scale(0.55).move_to([0, LEFT_TARGET_Y, 0]), run_time=1.0)
            right_ground_y = RIGHT_GROUND_Y
            right_x = 0.0
            divider = Line([-safe_half_w() + 0.2, DIVIDER_Y, 0], [safe_half_w() - 0.2, DIVIDER_Y, 0],
                           color=SLATE, stroke_width=2)
        else:
            left_target_x = -3.3
            # scale 0.75 wasn't small enough: the ground line spans the FULL
            # original safe width (±6.51), so even scaled it reached past
            # x=0 and crossed the vertical divider (confirmed bug — visible
            # as the ground line and divider intersecting). 0.42 keeps the
            # scaled line's right edge at -3.3+6.51*0.42=-0.57, clear of x=0.
            self.play(left_group.animate.scale(0.42).move_to([left_target_x, GROUND_Y * 0.75, 0]),
                      run_time=1.0)
            right_ground_y = RIGHT_GROUND_Y
            right_x = 3.3
            divider = Line([0, -safe_half_h() + 0.3, 0], [0, TOP_Y, 0], color=SLATE, stroke_width=2)

        self.play(Create(divider), run_time=0.4)

        right_figure = make_stick_figure(right_x, right_ground_y, scale=RIGHT_FIG_SCALE)
        right_ground_line = Line(
            [right_x - 1.6, right_ground_y, 0], [right_x + 1.6, right_ground_y, 0], color=INK
        )
        panel_label = Text("WALKER'S FRAME", font_size=FONT_LABEL, color=INK)
        if PORTRAIT:
            panel_label.move_to([right_x, PANEL_LABEL_Y, 0])
        else:
            # fixed near TOP_Y rather than next_to(right_figure, UP, ...) —
            # that placed it only ~1 unit above the figure, which collided
            # with the resultant's label once the vector construction (which
            # sits WORKSPACE_GAP+L_RAIN above the head) was added (confirmed
            # bug); anchoring to the frame's own ceiling guarantees clearance
            # from content whose height depends on L_RAIN/L_WALK_MAX
            panel_label.move_to([right_x, TOP_Y - 0.25, 0])
        self.play(Create(right_ground_line), FadeIn(right_figure), FadeIn(panel_label), run_time=0.6)

        # the vector construction lives in its own workspace strictly ABOVE
        # the head (with WORKSPACE_GAP clearance) rather than converging
        # exactly on it — confirmed bug: terminating the resultant AT the
        # head crowded the arrowheads/labels directly into the figure
        head = head_pos(right_x, right_ground_y, scale=RIGHT_FIG_SCALE)
        base = head + UP * WORKSPACE_GAP
        p0 = base + np.array([L_WALK_MAX, L_RAIN, 0.0])
        rain_v = Arrow(p0, p0 + DOWN * L_RAIN, color=SLATE, buff=0, stroke_width=6)
        self.play(GrowArrow(rain_v), run_time=0.6)

        neg_walk = Arrow(
            rain_v.get_end(), rain_v.get_end() + LEFT * 0.15,
            color=CRIMSON, buff=0, stroke_width=6,
        )
        # the label must NOT be positioned via next_to() until AFTER the
        # arrow finishes growing — confirmed bug: computing it against the
        # short 0.15-long starting stub left the label stranded over the
        # middle of the arrow once put_start_and_end_on grew it to full length
        self.play(
            neg_walk.animate.put_start_and_end_on(rain_v.get_end(), rain_v.get_end() + LEFT * L_WALK_MAX),
            run_time=1.0,
        )
        neg_walk_label = Text("-v_walk", font_size=FONT_LABEL, color=CRIMSON).next_to(
            neg_walk, LEFT, buff=0.2
        )
        self.play(FadeIn(neg_walk_label), run_time=0.3)

        resultant = Arrow(p0, neg_walk.get_end(), color=TEAL, buff=0, stroke_width=7)
        resultant_label = Text(
            "v_rain (walker's frame)", font_size=FONT_LABEL, color=TEAL
        ).next_to(resultant, UP, buff=0.2)
        self.play(GrowArrow(resultant), FadeIn(resultant_label), run_time=0.8)
        self.wait(max(DURS["B02"] - 4.4, 0.3))

        self.right_x, self.right_ground_y = right_x, right_ground_y
        self.right_figure, self.right_ground_line = right_figure, right_ground_line
        self.p0, self.rain_v = p0, rain_v
        self.neg_walk, self.neg_walk_label = neg_walk, neg_walk_label
        self.resultant, self.resultant_label = resultant, resultant_label
        self.left_group, self.divider, self.panel_label = left_group, divider, panel_label

    # ---------------- B03 — speed comparison ----------------
    def b03_speed_comparison(self):
        for frac in (0.35, 0.7, 1.0):
            l_walk = L_WALK_MAX * frac
            new_neg_walk = Arrow(
                self.rain_v.get_end(), self.rain_v.get_end() + LEFT * l_walk,
                color=CRIMSON, buff=0, stroke_width=6,
            )
            new_resultant = Arrow(self.p0, new_neg_walk.get_end(), color=TEAL, buff=0, stroke_width=7)
            new_resultant_label = Text(
                "v_rain (walker's frame)", font_size=FONT_LABEL, color=TEAL
            ).next_to(new_resultant, UP, buff=0.2)
            self.play(
                ReplacementTransform(self.neg_walk, new_neg_walk),
                ReplacementTransform(self.resultant, new_resultant),
                ReplacementTransform(self.resultant_label, new_resultant_label),
                FadeOut(self.neg_walk_label),
                run_time=1.1,
            )
            self.neg_walk, self.resultant, self.resultant_label = (
                new_neg_walk, new_resultant, new_resultant_label
            )
            self.neg_walk_label = Text("-v_walk", font_size=FONT_LABEL, color=CRIMSON).next_to(
                self.neg_walk, LEFT, buff=0.2
            )
            self.play(FadeIn(self.neg_walk_label), run_time=0.3)
        self.wait(max(DURS["B03"] - 1.4 * 3, 0.3))

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        final_y = FINAL_Y if PORTRAIT else self.right_ground_y - 0.6
        final = Text("It's just vector addition.", font_size=FONT_FINAL, color=INK).move_to(
            [self.right_x, final_y, 0]
        )
        final_bg = SurroundingRectangle(
            final, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.2,
        )
        self.play(FadeIn(final_bg), FadeIn(final), run_time=0.6)
        self.wait(max(DURS["B04"] - 0.6, 0.3), frozen_frame=False)
