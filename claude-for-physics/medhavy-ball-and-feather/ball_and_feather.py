"""ball_and_feather.py — Chapter 3, Free Fall.

A 10 kg ball and a 0.01 kg feather released simultaneously in vacuum hit the
ground at the same instant. medhavy palette (Okabe-Ito), one rotating accent
per beat. Audio durations are ground truth, read from beat_sheet.json
(generate_audio_kokoro.py already measured them).

Orientation-aware, one file renders either aspect (matches the sketch-explainer
doctrine): frame_height stays 8 in both, only frame_width changes via -r.
  - Landscape (16:9, deep-dive / book): no intro card — B00 is the first
    frame on screen; no outro card — B04 is a plain held final frame.
  - Portrait (9:16, short-form/Reels/TikTok): adds a title card at the very
    start and burned-in captions (one per beat, from the same narration_text
    as the audio) — the two things a short needs that the book cut doesn't.

Render (16:9 deep-dive):
  manim -qh ball_and_feather.py BallAndFeather
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching --flush_cache ball_and_feather.py BallAndFeather
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


# Manim does NOT auto-derive frame_width from -r's pixel_width/pixel_height —
# verified directly: setting config.pixel_width/pixel_height alone leaves
# frame_width at its landscape default (14.22). Detect orientation from the
# actual output resolution instead, and set frame_width explicitly so world
# units stay isotropic (otherwise circles render as ellipses).
PORTRAIT = config.pixel_width < config.pixel_height
if PORTRAIT:
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

# ---- medhavy palette (Okabe-Ito, colorblind-safe) ----
# Background overridden to pure white per professor feedback (medhavy's stock
# cream #F0EAD6 read as "dirty brown" on screen) — accent colors unchanged.
CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

# object fill colors — professor feedback: objects should be colored, not gray
BALL_COLOR = TEAL
FEATHER_COLOR = GOLD

config.background_color = CREAM

SAFE_MARGIN = 0.6  # ~8% inset on a 14.22 x 8 frame


def safe_half_w():
    return config.frame_width / 2 - SAFE_MARGIN


def safe_half_h():
    return config.frame_height / 2 - SAFE_MARGIN


# frame_height is 8 in both orientations (only frame_width changes), so
# TOP_Y/GROUND_Y are identical in landscape and portrait — only the
# horizontal spread and font/object sizes need to shrink for the narrow
# 9:16 frame_width (4.5 vs 14.22).
if PORTRAIT:
    LEFT_X, RIGHT_X = -1.0, 1.0
    BALL_RADIUS = 0.32
    FEATHER_H, FEATHER_W = 0.5, 0.24
    FONT_MASS = 20
    FONT_ARROW = 15
    ARROW_GAP = 0.45
    FONT_EQ, FONT_DERIV, FONT_AG, FONT_MERGED, FONT_AG_TAG, FONT_FINAL = 30, 22, 26, 20, 16, 20
else:
    LEFT_X, RIGHT_X = -3.2, 3.2
    BALL_RADIUS = 0.45
    FEATHER_H, FEATHER_W = 0.7, 0.34
    FONT_MASS = 28
    FONT_ARROW = 22
    ARROW_GAP = 0.9
    FONT_EQ, FONT_DERIV, FONT_AG, FONT_MERGED, FONT_AG_TAG, FONT_FINAL = 52, 36, 40, 28, 24, 30

TOP_Y = safe_half_h() - 0.6
# portrait reserves a caption band at the very bottom of the frame, so the
# "ground" the objects fall to sits higher than in landscape (which has no
# captions and uses the full vertical safe area)
CAPTION_BAND = 1.1 if PORTRAIT else 0.0
GROUND_Y = -safe_half_h() + 0.5 + CAPTION_BAND
# positioned 0.80-0.85 down the frame per feedback (was 0.8625 — nudged up
# slightly into the requested band); only meaningful when PORTRAIT
CAPTION_FRAC = 0.925
CAPTION_Y = config.frame_height / 2 - CAPTION_FRAC * config.frame_height

LABEL_BUFF = 0.35   # generous clearance between an object and its own label

CAPTION_FONT = 15   # smaller still, per feedback (was 22, then 18)
CAPTION_STYLE = "PT Sans"  # switched from Open Sans per feedback — Open Sans exhibited mid-word gap artifacts when rendered by Manim/Pango at this size
CAPTION_WRAP = 30   # chars per line — tuned for the 4.5-wide portrait frame at the smaller font


def tagged(text_mobj):
    """Wrap a small on-screen label in an opaque CREAM backing so it never
    visually overlaps the dashed guide lines (or anything else) behind it —
    confirmed bug: bare Text has no fill between glyphs/words, so a guide
    line's dash shows through the gap (e.g. between "10" and "kg", or across
    the "=" in "F = mg" / "a = g") whenever the label sits over the line's
    vertical extent, which happens constantly since labels track their
    falling object via next_to() updaters."""
    bg = BackgroundRectangle(text_mobj, color=CREAM, fill_opacity=1, buff=0.05)
    return VGroup(bg, text_mobj)


def make_feather(height=FEATHER_H, width=FEATHER_W, fill_color=FEATHER_COLOR, stroke_color=INK):
    """A stylized feather silhouette: pointed tip, notched quill base, center
    quill line, a few angled barb strokes. Returns a VGroup positioned with
    its own center at the origin, so .move_to()/.get_center() behave exactly
    like the Circle it replaces."""
    h, w = height, width
    body = Polygon(
        [0, h / 2, 0],
        [w * 0.5, h * 0.15, 0],
        [w * 0.35, -h * 0.25, 0],
        [w * 0.12, -h * 0.42, 0],
        [0, -h * 0.30, 0],
        [-w * 0.12, -h * 0.42, 0],
        [-w * 0.35, -h * 0.25, 0],
        [-w * 0.5, h * 0.15, 0],
        color=stroke_color, fill_color=fill_color, fill_opacity=1, stroke_width=2.5,
    ).round_corners(radius=0.05)
    quill = Line([0, h / 2, 0], [0, -h * 0.30, 0], color=stroke_color, stroke_width=2)
    # a few simple angled barb strokes off the quill, both sides, tip-ward
    barbs = VGroup(*[
        Line([0, y, 0], [side * w * 0.3, y + h * 0.12, 0], color=stroke_color, stroke_width=1.5)
        for y in (h * 0.18, -h * 0.05, -h * 0.20)
        for side in (1, -1)
    ])
    return VGroup(body, barbs, quill)


TITLE_DURATION = 0.0  # no separate title card anymore: question_card() is the sole
# opening card and starts at t=0, so the caption schedule (which is keyed to
# B00Q's narration) needs no offset before it begins
CAPTION_WORDS_PER_CHUNK = 7  # short subtitle-style phrases, not the whole beat's narration


def build_caption_schedule():
    """(start_s, end_s, text) for every short caption chunk across the whole
    video, in absolute self.time coordinates. A whole beat's narration is far
    too long to show as one on-screen block (it overflowed the entire frame
    in the first cut) — real captions are short phrases that cycle, timed
    proportionally to each chunk's share of that beat's measured duration."""
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


class BallAndFeather(Scene):
    def construct(self):
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_naive_expectation()
        self.b02_force_arrows()
        self.b03_collapse()
        self.b04_outro()

    def wait(self, duration=1.0, stop_condition=None, frozen_frame=None):
        # Manim's "frozen frame" optimization renders ONE frame and repeats
        # it for the whole wait when it thinks nothing is animating — which
        # skips per-frame updater calls entirely. That silently froze the
        # caption updater for a wait's full duration (e.g. B01's 12.9s wait),
        # producing exactly the "captions pause, then jump" behavior seen in
        # the short. Force real per-frame ticking whenever captions are live.
        if PORTRAIT and frozen_frame is None:
            frozen_frame = False
        return super().wait(duration, stop_condition=stop_condition, frozen_frame=frozen_frame)

    # ---------------- Portrait-only: title card ----------------
    def title_card(self):
        wrapped = "\n".join(textwrap.wrap(TITLE, width=15))
        title = Text(wrapped, font_size=26, color=INK, line_spacing=1.25).move_to(ORIGIN)
        max_w = 2 * safe_half_w()
        if title.width > max_w:
            title.scale_to_fit_width(max_w)
        underline = Line(
            title.get_corner(DOWN + LEFT) + DOWN * 0.25,
            title.get_corner(DOWN + RIGHT) + DOWN * 0.25,
            color=BALL_COLOR, stroke_width=5,
        )
        self.play(Write(title), Create(underline), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(underline), run_time=0.5)

    # ---------------- Portrait-only: driving question / title card ------
    # Sole opening card for the short: the driving question IS the title —
    # no separate concept-title screen precedes it. Poses the video's
    # question, in both on-screen text and narration (beat B00Q, its own
    # Kokoro line), before any physics explanation begins. Not one of the
    # shared beats the landscape render walks — landscape's construct()
    # never calls this, so the long-form deep-dive is untouched. Styled
    # larger and less italic than the original question-card treatment so
    # it reads as a proper title, not a mid-video caption.
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
    # Driven by an updater keyed on self.time (Manim's running scene clock,
    # advanced automatically by every self.play/self.wait regardless of what
    # they animate) — this runs the whole caption track independently of the
    # beats' own choreography, so no per-beat wiring or timing math is needed
    # anywhere else in the file.
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
        dur = DURS["B00"]
        self.left_guide = DashedLine(
            [LEFT_X, TOP_Y, 0], [LEFT_X, GROUND_Y, 0], color=SLATE, dash_length=0.15
        )
        self.right_guide = DashedLine(
            [RIGHT_X, TOP_Y, 0], [RIGHT_X, GROUND_Y, 0], color=SLATE, dash_length=0.15
        )
        self.ground = Line(
            [-safe_half_w(), GROUND_Y, 0], [safe_half_w(), GROUND_Y, 0], color=INK
        )

        self.ball = Circle(
            radius=BALL_RADIUS, color=INK, fill_color=BALL_COLOR, fill_opacity=1
        ).move_to([LEFT_X, TOP_Y, 0])
        self.ball_label = tagged(Text("10 kg", font_size=FONT_MASS, color=INK)).next_to(
            self.ball, UP, buff=LABEL_BUFF
        )

        self.feather = make_feather().move_to([RIGHT_X, TOP_Y, 0])
        self.feather_label = tagged(Text("0.01 kg", font_size=FONT_MASS, color=INK)).next_to(
            self.feather, UP, buff=LABEL_BUFF
        )

        self.play(
            Create(self.left_guide), Create(self.right_guide), Create(self.ground),
            FadeIn(self.ball), FadeIn(self.ball_label),
            FadeIn(self.feather), FadeIn(self.feather_label),
            run_time=1.2,
        )

        fall_time = max(dur - 2.4, 1.5)
        # updaters keep each label pinned to its own object's actual
        # (radius-aware) top edge every frame — next_to() on a bare
        # coordinate was the earlier bug: it ignores the circle's radius
        self.ball_label.add_updater(lambda m: m.next_to(self.ball, UP, buff=LABEL_BUFF))
        self.feather_label.add_updater(lambda m: m.next_to(self.feather, UP, buff=LABEL_BUFF))
        self.play(
            self.ball.animate.move_to([LEFT_X, GROUND_Y, 0]),
            self.feather.animate.move_to([RIGHT_X, GROUND_Y, 0]),
            rate_func=rate_functions.ease_in_quad,
            run_time=fall_time,
        )
        self.ball_label.clear_updaters()
        self.feather_label.clear_updaters()

        pulse_l = Circle(radius=0.1, color=SLATE).move_to([LEFT_X, GROUND_Y, 0])
        pulse_r = Circle(radius=0.1, color=SLATE).move_to([RIGHT_X, GROUND_Y, 0])
        self.play(
            pulse_l.animate.scale(4).set_opacity(0),
            pulse_r.animate.scale(4).set_opacity(0),
            run_time=0.6,
        )

    # ---------------- B01 — Naive expectation ----------------
    def b01_naive_expectation(self):
        # nothing is falling in this beat — the guide lines add no meaning
        # here and the thought-bubble sits squarely on the left guide's axis,
        # so hide both guides for the duration (same pattern as B03)
        self.play(FadeOut(self.left_guide), FadeOut(self.right_guide), run_time=0.4)

        if PORTRAIT:
            # the landscape bubble (width 3.6, centered over the ball) is
            # wider than the whole portrait safe area (3.3) — center it on
            # the frame instead and stack the cross below rather than beside
            thought = RoundedRectangle(
                width=2.6, height=0.8, corner_radius=0.16, color=CRIMSON
            ).move_to([0, GROUND_Y + 2.7, 0])
            thought_text = Text(
                "SHOULD FALL FASTER?", font_size=16, color=CRIMSON
            ).move_to(thought.get_center())
            cross = Cross(scale_factor=0.22, color=CRIMSON).move_to(
                [0, GROUND_Y + 1.7, 0]
            )
        else:
            thought = RoundedRectangle(
                width=3.6, height=1.0, corner_radius=0.2, color=CRIMSON
            ).move_to([LEFT_X, GROUND_Y + 2.6, 0])
            thought_text = Text(
                "SHOULD FALL FASTER?", font_size=22, color=CRIMSON
            ).move_to(thought.get_center())
            cross = Cross(scale_factor=0.3, color=CRIMSON).move_to(
                [RIGHT_X, GROUND_Y + 2.6, 0]
            )

        self.play(Create(thought), Write(thought_text), Create(cross), run_time=1.0)
        self.wait(max(DURS["B01"] - 2.4, 0.3))
        self.play(FadeOut(thought), FadeOut(thought_text), FadeOut(cross), run_time=0.6)
        self.play(FadeIn(self.left_guide), FadeIn(self.right_guide), run_time=0.4)

    # ---------------- B02 — Force arrows ----------------
    def b02_force_arrows(self):
        # hide the mass tags first so the new force-arrow labels never share
        # the space directly above each object
        self.play(FadeOut(self.ball_label), FadeOut(self.feather_label), run_time=0.4)

        big_arrow = Arrow(
            start=[LEFT_X, GROUND_Y + 2.4, 0], end=[LEFT_X, GROUND_Y + 0.55, 0],
            color=TEAL, buff=0, stroke_width=10,
        )
        small_arrow = Arrow(
            start=[RIGHT_X, GROUND_Y + 1.3, 0], end=[RIGHT_X, GROUND_Y + 0.24, 0],
            color=TEAL, buff=0, stroke_width=4,
        )
        if PORTRAIT:
            # LEFT/RIGHT placement (landscape) would push these past the
            # narrow frame's safe edge — shorter text, stacked above each
            # arrow instead, same x as the arrow so nothing runs off-frame
            big_label = tagged(Text("F = mg", font_size=FONT_ARROW, color=TEAL)).next_to(
                big_arrow, UP, buff=0.15
            )
            small_label = tagged(Text("F = mg", font_size=FONT_ARROW, color=TEAL)).next_to(
                small_arrow, UP, buff=0.15
            )
        else:
            big_label = Text("F = mg (large)", font_size=FONT_ARROW, color=TEAL).next_to(
                big_arrow, LEFT, buff=ARROW_GAP
            )
            small_label = Text("F = mg (small)", font_size=FONT_ARROW, color=TEAL).next_to(
                small_arrow, RIGHT, buff=ARROW_GAP
            )

        self.play(
            GrowArrow(big_arrow), FadeIn(big_label),
            GrowArrow(small_arrow), FadeIn(small_label),
            run_time=1.2,
        )
        self.wait(max(DURS["B02"] - 2.2, 0.3))

        self.play(
            FadeOut(big_arrow), FadeOut(big_label),
            FadeOut(small_arrow), FadeOut(small_label),
            run_time=0.6,
        )
        # restore the mass tags for B01/B02's continuity before the collapse beat
        self.play(FadeIn(self.ball_label), FadeIn(self.feather_label), run_time=0.4)

    # ---------------- B03 — Collapse: mass cancels ----------------
    def b03_collapse(self):
        # the guide lines run straight through the derivation text's column —
        # hide them (and the mass tags) while the equations are on screen
        self.play(
            FadeOut(self.ball_label), FadeOut(self.feather_label),
            FadeOut(self.left_guide), FadeOut(self.right_guide),
            run_time=0.4,
        )

        eq = MathTex("a = \\frac{F}{m}", color=INK, font_size=FONT_EQ).move_to(
            [0, GROUND_Y + (3.7 if PORTRAIT else 3.1), 0]
        )
        if PORTRAIT:
            # two side-by-side fractions don't fit the narrow frame at any
            # readable font size (±1.0 apart, safe half-width only 1.65) —
            # stack them vertically on the center line instead. Gap must be
            # wide (1.8, not the original 1.0): ReplacementTransform between
            # mismatched glyph counts interpolates sub-paths that can swing
            # through the space between two closely-stacked targets — at
            # gap 1.0 this produced a visibly garbled blob mid-transform.
            left_deriv = MathTex(
                "a = \\frac{10\\,\\text{kg} \\cdot g}{10\\,\\text{kg}}", color=INK, font_size=FONT_DERIV
            ).move_to([0, GROUND_Y + 3.0, 0])
            right_deriv = MathTex(
                "a = \\frac{0.01\\,\\text{kg} \\cdot g}{0.01\\,\\text{kg}}", color=INK, font_size=FONT_DERIV
            ).move_to([0, GROUND_Y + 1.2, 0])
        else:
            left_deriv = MathTex(
                "a = \\frac{10\\,\\text{kg} \\cdot g}{10\\,\\text{kg}}", color=INK, font_size=FONT_DERIV
            ).move_to([LEFT_X, GROUND_Y + 1.7, 0])
            right_deriv = MathTex(
                "a = \\frac{0.01\\,\\text{kg} \\cdot g}{0.01\\,\\text{kg}}", color=INK, font_size=FONT_DERIV
            ).move_to([RIGHT_X, GROUND_Y + 1.7, 0])

        self.play(Write(eq), run_time=0.8)
        self.play(FadeIn(left_deriv), FadeIn(right_deriv), run_time=0.8)
        self.wait(max(DURS["B03"] - 4.6, 0.3))

        left_g = MathTex("a = g", color=INK, font_size=FONT_AG).move_to(left_deriv.get_center())
        right_g = MathTex("a = g", color=INK, font_size=FONT_AG).move_to(right_deriv.get_center())
        self.play(
            ReplacementTransform(left_deriv, left_g),
            ReplacementTransform(right_deriv, right_g),
            run_time=1.0,
        )
        self.wait(0.5)

        merged = Text(
            "g = 9.8 m/s², same for both", font_size=FONT_MERGED, color=INK
        ).move_to([0, GROUND_Y + (2.2 if PORTRAIT else 1.7), 0])
        merged_bg = SurroundingRectangle(
            merged, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.25
        )

        self.play(
            ReplacementTransform(VGroup(left_g, right_g), VGroup(merged_bg, merged)),
            FadeOut(eq),
            run_time=1.0,
        )
        self.wait(0.5)

        self.ag_label = tagged(Text("a = g", font_size=FONT_AG_TAG, color=INK))
        ag_left = self.ag_label.copy().next_to(self.ball, UP, buff=LABEL_BUFF)
        ag_right = self.ag_label.copy().next_to(self.feather, UP, buff=LABEL_BUFF)
        self.play(
            FadeOut(merged), FadeOut(merged_bg),
            FadeIn(ag_left), FadeIn(ag_right),
            run_time=0.6,
        )
        self.ball_label, self.feather_label = ag_left, ag_right

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        self.play(FadeIn(self.left_guide), FadeIn(self.right_guide), run_time=0.4)
        fall_time = max(DURS["B04"] - 2.0, 1.0)

        self.ball_label.add_updater(lambda m: m.next_to(self.ball, UP, buff=LABEL_BUFF))
        self.feather_label.add_updater(lambda m: m.next_to(self.feather, UP, buff=LABEL_BUFF))

        self.play(
            self.ball.animate.move_to([LEFT_X, TOP_Y, 0]),
            self.feather.animate.move_to([RIGHT_X, TOP_Y, 0]),
            run_time=0.8,
        )
        self.play(
            self.ball.animate.move_to([LEFT_X, GROUND_Y, 0]),
            self.feather.animate.move_to([RIGHT_X, GROUND_Y, 0]),
            rate_func=rate_functions.ease_in_quad,
            run_time=fall_time,
        )
        self.ball_label.clear_updaters()
        self.feather_label.clear_updaters()

        # in portrait, must clear the ball's own bottom edge (GROUND_Y - 0.32)
        # above and the caption band (now at frac 0.925) below — 0.8 sits
        # safely between both
        final_label = Text("SAME g. NO AIR.", font_size=FONT_FINAL, color=INK).move_to(
            [0, GROUND_Y - (0.8 if PORTRAIT else 1.3), 0]
        )
        self.play(FadeIn(final_label), run_time=0.5)
        self.wait(0.5)
