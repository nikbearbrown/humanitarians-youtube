"""weight_vs_mass.py — Chapter 5, Mass and Weight.

Same astronaut, Earth vs Moon: weighs 180 lb on Earth, 30 lb on the Moon.
Weight (W = mg) is a force that depends on local gravity; mass is inertia,
identical on both worlds (same push, same slide distance). medhavy palette
(Okabe-Ito), one rotating accent per beat.

Orientation-aware, one file renders either aspect (same doctrine as the
prior 5 videos in this series):
  - Landscape (16:9): no intro/outro card. Panels SIDE BY SIDE.
  - Portrait (9:16): title card + burned-in captions. Panels TOP/BOTTOM.

Render (16:9 deep-dive):
  manim -qh weight_vs_mass.py WeightVsMass
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching weight_vs_mass.py WeightVsMass
"""
import json
import textwrap
from pathlib import Path

from manim import *

HERE = Path(__file__).parent
SHEET = json.loads((HERE / "beat_sheet.json").read_text())
DURS = {b["beat_id"]: b["actual_duration_s"] for b in SHEET["beats"]}
NARR = {b["beat_id"]: b["narration_text"] for b in SHEET["beats"]}
TITLE = SHEET["metadata"]["title"]

PORTRAIT = config.pixel_width < config.pixel_height
if PORTRAIT:
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

FIGURE_COLOR = SLATE

config.background_color = CREAM
SAFE_MARGIN = 0.6


def safe_half_w():
    return config.frame_width / 2 - SAFE_MARGIN


def safe_half_h():
    return config.frame_height / 2 - SAFE_MARGIN


TOP_Y = safe_half_h() - 0.6
CAPTION_Y = -safe_half_h() + 0.5
CAPTION_FONT = 15
CAPTION_STYLE = "PT Sans"  # switched from Open Sans — Open Sans exhibited mid-word gap artifacts when rendered by Manim/Pango at this size (confirmed on ball_and_feather.py)
CAPTION_WRAP = 30
TITLE_DURATION = 0.0  # no separate title card anymore: question_card() is the sole
# opening card and starts at t=0, so the caption schedule (which is keyed to
# B00Q's narration) needs no offset before it begins
CAPTION_WORDS_PER_CHUNK = 7

if PORTRAIT:
    LEFT_X = RIGHT_X = 0.0
    TOP_PANEL_Y, BOTTOM_PANEL_Y = 1.6, -0.7
    DIVIDER_Y = 0.45
    FIG_SCALE = 0.55
    SLIDE_DX = 0.5
    FONT_LABEL, FONT_TITLE, FONT_FINAL = 13, 15, 14
    FINAL_Y = -1.7
else:
    LEFT_X, RIGHT_X = -3.3, 3.3
    TOP_PANEL_Y = BOTTOM_PANEL_Y = -0.6
    DIVIDER_Y = None
    FIG_SCALE = 1.0
    SLIDE_DX = 1.1
    FONT_LABEL, FONT_TITLE, FONT_FINAL = 20, 24, 22
    FINAL_Y = -2.3


def build_caption_schedule():
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


def make_figure(x, ground_y, scale=1.0):
    s = scale
    head = Circle(radius=0.16 * s, color=INK, fill_color=FIGURE_COLOR, fill_opacity=1).move_to(
        [x, ground_y + 0.85 * s, 0]
    )
    body = Line([x, ground_y + 0.68 * s, 0], [x, ground_y + 0.35 * s, 0], color=INK, stroke_width=3)
    leg_l = Line([x, ground_y + 0.35 * s, 0], [x - 0.15 * s, ground_y, 0], color=INK, stroke_width=3)
    leg_r = Line([x, ground_y + 0.35 * s, 0], [x + 0.15 * s, ground_y, 0], color=INK, stroke_width=3)
    arm_l = Line([x, ground_y + 0.58 * s, 0], [x - 0.18 * s, ground_y + 0.42 * s, 0], color=INK, stroke_width=3)
    arm_r = Line([x, ground_y + 0.58 * s, 0], [x + 0.18 * s, ground_y + 0.42 * s, 0], color=INK, stroke_width=3)
    return VGroup(head, body, leg_l, leg_r, arm_l, arm_r)


def make_scale(x, ground_y, scale=1.0):
    return Rectangle(width=0.6 * scale, height=0.15 * scale, color=INK, fill_color=CREAM, fill_opacity=1).move_to(
        [x, ground_y - 0.07 * scale, 0]
    )


class WeightVsMass(Scene):
    def construct(self):
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_weight()
        self.b02_push()
        self.b03_same_resistance()
        self.b04_outro()

    def wait(self, duration=1.0, stop_condition=None, frozen_frame=None):
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

    # ---------------- B00 — Hook: Earth vs Moon scale ----------------
    def b00_hook(self):
        if PORTRAIT:
            earth_x, moon_x = 0.0, 0.0
            earth_y, moon_y = TOP_PANEL_Y, BOTTOM_PANEL_Y
            self.divider = Line(
                [-safe_half_w() + 0.2, DIVIDER_Y, 0], [safe_half_w() - 0.2, DIVIDER_Y, 0],
                color=SLATE, stroke_width=2,
            )
        else:
            earth_x, moon_x = LEFT_X, RIGHT_X
            earth_y = moon_y = TOP_PANEL_Y
            self.divider = Line([0, -safe_half_h() + 0.3, 0], [0, TOP_Y, 0], color=SLATE, stroke_width=2)

        self.earth_x, self.moon_x, self.earth_y, self.moon_y = earth_x, moon_x, earth_y, moon_y

        earth_title = Text("EARTH", font_size=FONT_TITLE, color=INK).move_to(
            [earth_x, earth_y + 1.6 * FIG_SCALE, 0]
        )
        moon_title = Text("MOON", font_size=FONT_TITLE, color=INK).move_to(
            [moon_x, moon_y + 1.6 * FIG_SCALE, 0]
        )
        self.earth_fig = make_figure(earth_x, earth_y, FIG_SCALE)
        self.moon_fig = make_figure(moon_x, moon_y, FIG_SCALE)
        earth_scale = make_scale(earth_x, earth_y, FIG_SCALE)
        moon_scale = make_scale(moon_x, moon_y, FIG_SCALE)
        earth_readout = Text("180 lb", font_size=FONT_LABEL, color=INK).next_to(earth_scale, DOWN, buff=0.15)
        moon_readout = Text("30 lb", font_size=FONT_LABEL, color=INK).next_to(moon_scale, DOWN, buff=0.15)

        self.play(Create(self.divider), run_time=0.4)
        self.play(
            FadeIn(earth_title), FadeIn(moon_title),
            FadeIn(self.earth_fig), FadeIn(self.moon_fig),
            Create(earth_scale), Create(moon_scale),
            FadeIn(earth_readout), FadeIn(moon_readout),
            run_time=1.2,
        )
        self.earth_title, self.moon_title = earth_title, moon_title
        self.earth_scale, self.moon_scale = earth_scale, moon_scale
        self.earth_readout, self.moon_readout = earth_readout, moon_readout
        self.wait(max(DURS["B00"] - 1.6, 0.3))

    # ---------------- B01 — weight is a force, changes with g ----------------
    def b01_weight(self):
        # offset to the side of the figure (x + 0.4*scale) — starting the
        # arrow directly above the head sent it piercing straight through
        # the head and body on its way down (confirmed bug via zoomed frame)
        off = 0.4 * FIG_SCALE
        earth_arrow = Arrow(
            [self.earth_x + off, self.earth_y + 0.9 * FIG_SCALE, 0],
            [self.earth_x + off, self.earth_y + 0.9 * FIG_SCALE - 0.85 * FIG_SCALE, 0],
            color=CRIMSON, buff=0, stroke_width=7,
        )
        earth_w_label = Text("W = mg,  g = 9.8", font_size=FONT_LABEL - 2, color=CRIMSON).next_to(
            earth_arrow, RIGHT if not PORTRAIT else UP, buff=0.15
        )
        moon_arrow = Arrow(
            [self.moon_x + off, self.moon_y + 0.9 * FIG_SCALE, 0],
            [self.moon_x + off, self.moon_y + 0.9 * FIG_SCALE - 0.3 * FIG_SCALE, 0],
            color=CRIMSON, buff=0, stroke_width=7,
        )
        moon_w_label = Text("g = 1.6", font_size=FONT_LABEL - 2, color=CRIMSON).next_to(
            moon_arrow, RIGHT if not PORTRAIT else UP, buff=0.15
        )
        self.play(
            GrowArrow(earth_arrow), FadeIn(earth_w_label),
            GrowArrow(moon_arrow), FadeIn(moon_w_label),
            run_time=1.2,
        )
        self.earth_w_arrow, self.moon_w_arrow = earth_arrow, moon_arrow
        self.earth_w_label, self.moon_w_label = earth_w_label, moon_w_label
        self.wait(max(DURS["B01"] - 1.2, 0.3))

    # ---------------- B02 — push sideways, mass resists equally ----------------
    def b02_push(self):
        self.play(
            FadeOut(self.earth_w_arrow), FadeOut(self.earth_w_label),
            FadeOut(self.moon_w_arrow), FadeOut(self.moon_w_label),
            FadeOut(self.earth_scale), FadeOut(self.moon_scale),
            FadeOut(self.earth_readout), FadeOut(self.moon_readout),
            run_time=0.5,
        )
        below_y_e = self.earth_y - 0.35 * FIG_SCALE
        below_y_m = self.moon_y - 0.35 * FIG_SCALE
        earth_push = Arrow(
            [self.earth_x - 0.6, below_y_e, 0], [self.earth_x - 0.1, below_y_e, 0],
            color=TEAL, buff=0, stroke_width=6,
        )
        moon_push = Arrow(
            [self.moon_x - 0.6, below_y_m, 0], [self.moon_x - 0.1, below_y_m, 0],
            color=TEAL, buff=0, stroke_width=6,
        )
        self.play(GrowArrow(earth_push), GrowArrow(moon_push), run_time=0.6)

        earth_trail = DashedLine(
            [self.earth_x, self.earth_y, 0], [self.earth_x + SLIDE_DX, self.earth_y, 0],
            color=SLATE, stroke_width=2,
        )
        moon_trail = DashedLine(
            [self.moon_x, self.moon_y, 0], [self.moon_x + SLIDE_DX, self.moon_y, 0],
            color=SLATE, stroke_width=2,
        )
        self.play(
            self.earth_fig.animate.shift(RIGHT * SLIDE_DX),
            self.moon_fig.animate.shift(RIGHT * SLIDE_DX),
            Create(earth_trail), Create(moon_trail),
            FadeOut(earth_push), FadeOut(moon_push),
            run_time=1.0,
        )
        self.earth_trail, self.moon_trail = earth_trail, moon_trail
        self.wait(max(DURS["B02"] - 2.1, 0.3))

    # ---------------- B03 — same resistance ----------------
    def b03_same_resistance(self):
        self.play(
            self.earth_trail.animate.set_color(GOLD).set_stroke(width=5),
            self.moon_trail.animate.set_color(GOLD).set_stroke(width=5),
            run_time=0.6,
        )
        check_e = Text("✓", font_size=FONT_TITLE + 6, color=GOLD).set_stroke(color=INK, width=1).move_to(
            [self.earth_x, self.earth_y + 1.6 * FIG_SCALE, 0]
        )
        check_m = Text("✓", font_size=FONT_TITLE + 6, color=GOLD).set_stroke(color=INK, width=1).move_to(
            [self.moon_x, self.moon_y + 1.6 * FIG_SCALE, 0]
        )
        same_label = Text("SAME RESISTANCE", font_size=FONT_LABEL, color=INK).move_to([0, FINAL_Y, 0])
        self.play(
            ReplacementTransform(self.earth_title, check_e),
            ReplacementTransform(self.moon_title, check_m),
            FadeIn(same_label),
            run_time=0.8,
        )
        self.check_e, self.check_m, self.same_label = check_e, check_m, same_label
        self.wait(max(DURS["B03"] - 1.4, 0.3))

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        self.play(
            FadeOut(self.divider), FadeOut(self.check_e), FadeOut(self.check_m), FadeOut(self.same_label),
            FadeOut(self.earth_fig), FadeOut(self.moon_fig),
            FadeOut(self.earth_trail), FadeOut(self.moon_trail),
            run_time=0.6,
        )
        title = Text("PROPORTIONAL, NOT THE SAME", font_size=FONT_TITLE, color=INK).move_to(
            [0, 1.3 if not PORTRAIT else 1.0, 0]
        )
        weight_line = Text(
            "WEIGHT — a force, W = mg, changes with gravity", font_size=FONT_FINAL, color=INK
        ).move_to([0, 0.3, 0])
        mass_line = Text(
            "MASS — inertia, constant everywhere", font_size=FONT_FINAL, color=INK
        ).move_to([0, -0.3, 0])
        box = SurroundingRectangle(
            VGroup(weight_line, mass_line), color=GOLD, fill_color=GOLD, fill_opacity=0.5, buff=0.3,
        )
        self.play(FadeIn(title), FadeIn(box), FadeIn(weight_line), FadeIn(mass_line), run_time=0.8)
        self.wait(max(DURS["B04"] - 1.4, 0.3))
