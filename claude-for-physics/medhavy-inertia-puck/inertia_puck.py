"""inertia_puck.py — Chapter 5, Newton's First Law.

A pushed puck slides and stops — intuition says that's what moving things
do. Resolution: friction was acting the whole time; remove it (air hockey)
and the puck glides at constant velocity forever. medhavy palette
(Okabe-Ito), one rotating accent per beat.

Orientation-aware, one file renders either aspect (same doctrine as the
prior 4 videos in this series):
  - Landscape (16:9): no intro/outro card.
  - Portrait (9:16): title card + burned-in captions.

Render (16:9 deep-dive):
  manim -qh inertia_puck.py InertiaPuck
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching inertia_puck.py InertiaPuck
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

PUCK_COLOR = SLATE

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
    TABLE_Y = 0.3
    TABLE_H = 1.2
    PUCK_R = 0.22
    START_X, STOP_X, END_X = -1.4, -0.2, 1.4
    FONT_LABEL, FONT_LAW, FONT_FINAL = 14, 16, 15
else:
    TABLE_Y = -0.2
    TABLE_H = 1.6
    PUCK_R = 0.35
    START_X, STOP_X, END_X = -5.5, -1.5, 5.5
    FONT_LABEL, FONT_LAW, FONT_FINAL = 22, 26, 24

TABLE_TOP = TABLE_Y + TABLE_H / 2


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


def make_table():
    w = 2 * safe_half_w() - 0.4
    h = TABLE_H
    table = Rectangle(width=w, height=h, color=INK, stroke_width=3).move_to([0, TABLE_Y, 0])
    n_lines = 8
    grid = VGroup(*[
        Line([x, TABLE_Y - h / 2, 0], [x, TABLE_Y + h / 2, 0], color=SLATE, stroke_width=1, stroke_opacity=0.4)
        for x in [-w / 2 + i * w / n_lines for i in range(1, n_lines)]
    ])
    return VGroup(table, grid)


def make_puck(x, scale=1.0):
    return Circle(radius=PUCK_R * scale, color=INK, fill_color=PUCK_COLOR, fill_opacity=1).move_to([x, TABLE_Y, 0])


class InertiaPuck(Scene):
    def construct(self):
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_friction()
        self.b02_air_hockey()
        self.b03_the_law()
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

    # ---------------- B00 — Hook: push, decay, stop ----------------
    def b00_hook(self):
        self.table = make_table()
        self.puck = make_puck(START_X)
        push_arrow = Arrow(
            [START_X - 1.0, TABLE_Y, 0], [START_X - 0.1, TABLE_Y, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        push_label = Text("PUSH", font_size=FONT_LABEL, color=CRIMSON).next_to(push_arrow, UP, buff=0.15)
        self.play(Create(self.table), FadeIn(self.puck), GrowArrow(push_arrow), FadeIn(push_label), run_time=1.0)
        self.play(FadeOut(push_arrow), FadeOut(push_label), run_time=0.3)

        decel_time = max(DURS["B00"] - 1.5, 1.0)
        self.play(
            self.puck.animate.move_to([STOP_X, TABLE_Y, 0]),
            rate_func=rate_functions.ease_out_expo,
            run_time=decel_time,
        )
        self.wait(max(DURS["B00"] - 1.5 - decel_time, 0.2))

    # ---------------- B01 — the hidden friction force ----------------
    def b01_friction(self):
        friction_arrow = Arrow(
            [STOP_X + 0.5, TABLE_Y - 0.5, 0], [STOP_X - 0.1, TABLE_Y - 0.5, 0],
            color=TEAL, buff=0, stroke_width=5,
        )
        friction_label = Text("FRICTION", font_size=FONT_LABEL, color=TEAL).next_to(
            friction_arrow, DOWN, buff=0.12
        )
        self.play(GrowArrow(friction_arrow), FadeIn(friction_label), run_time=0.8)
        self.wait(max(DURS["B01"] - 1.6, 0.3))
        self.play(FadeOut(friction_arrow), FadeOut(friction_label), run_time=0.8)

    # ---------------- B02 — turn on the air, glide forever ----------------
    def b02_air_hockey(self):
        self.play(self.puck.animate.move_to([START_X, TABLE_Y, 0]), run_time=0.5)
        jet_y = TABLE_Y - (0.6 if not PORTRAIT else 0.45)
        jet_spacing = 1.2 if not PORTRAIT else 0.5
        jet_xs = [x for x in [START_X + i * jet_spacing for i in range(0, 12)] if x < safe_half_w() - 0.3]
        jets = VGroup(*[
            Arrow([x, jet_y, 0], [x, jet_y + 0.3, 0], color=SLATE, buff=0, stroke_width=3)
            for x in jet_xs
        ])
        push_arrow = Arrow(
            [START_X - 1.0, TABLE_Y, 0], [START_X - 0.1, TABLE_Y, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        flash_friction = Arrow(
            [START_X + 0.4, TABLE_Y - 0.5, 0], [START_X - 0.1, TABLE_Y - 0.5, 0],
            color=TEAL, buff=0, stroke_width=5,
        )
        self.play(FadeIn(jets), GrowArrow(push_arrow), run_time=0.6)
        self.play(FadeIn(flash_friction), run_time=0.1)
        self.play(FadeOut(flash_friction), FadeOut(push_arrow), run_time=0.2)

        glide_time = max(DURS["B02"] - 0.9 - 0.5, 1.5)
        self.play(
            self.puck.animate.move_to([END_X, TABLE_Y, 0]),
            rate_func=linear,
            run_time=glide_time,
        )
        self.jets = jets

    # ---------------- B03 — the law ----------------
    def b03_the_law(self):
        self.play(self.puck.animate.move_to([START_X, TABLE_Y, 0]), FadeOut(self.jets), run_time=0.5)
        law = Text(
            "NET FORCE = 0\nVELOCITY = CONSTANT", font_size=FONT_LAW, color=INK, line_spacing=1.3
        ).move_to([0, TABLE_Y + (1.6 if not PORTRAIT else 1.3), 0])
        law_bg = SurroundingRectangle(law, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.25)
        self.play(FadeIn(law_bg), FadeIn(law), run_time=0.6)

        glide_time = max(DURS["B03"] - 1.1, 1.5)
        self.play(
            self.puck.animate.move_to([END_X, TABLE_Y, 0]),
            rate_func=linear,
            run_time=glide_time,
        )
        self.play(FadeOut(law_bg), FadeOut(law), run_time=0.5)

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        mid_x = 0.0
        self.play(self.puck.animate.move_to([mid_x, TABLE_Y, 0]), run_time=0.6)
        # next_to(self.puck, UP, buff=0.3) put this right on the table's own
        # top border — the puck sits at the table's vertical center, so a
        # small buff above the puck doesn't clear the table's half-height
        # (confirmed bug in the rendered short). Anchor to the table's top
        # edge explicitly instead, with real clearance above it.
        inertia_label = Text("INERTIA", font_size=FONT_LABEL, color=INK).move_to([mid_x, TABLE_TOP + 0.3, 0])
        final_text = Text(
            "\n".join(textwrap.wrap(
                "Nothing stops it, because nothing is pushing it to stop.",
                width=28 if PORTRAIT else 40,
            )),
            font_size=FONT_FINAL, color=INK, line_spacing=1.2,
        ).move_to([0, TABLE_Y - (1.6 if not PORTRAIT else 1.3), 0])
        final_bg = SurroundingRectangle(final_text, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.2)
        self.play(FadeIn(inertia_label), FadeIn(final_bg), FadeIn(final_text), run_time=0.7)
        self.wait(max(DURS["B04"] - 1.3, 0.3))
