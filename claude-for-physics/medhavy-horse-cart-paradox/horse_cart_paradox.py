"""horse_cart_paradox.py — Chapter 5, Newton's Third Law.

The horse pulls the cart forward (500 N); the cart pulls back on the horse
(500 N) by Newton's third law. Naive sum = zero, so why does anything move?
Resolution: third-law pairs act on DIFFERENT objects and never share a
free-body diagram — each object's own net force is what matters, and both
nets point forward. medhavy palette (Okabe-Ito), one rotating accent/beat.

Orientation-aware, one file renders either aspect (same doctrine as
ball_and_feather.py / car_turning.py / rain_relative_motion.py):
  - Landscape (16:9): no intro/outro card. B02-B03 split is SIDE BY SIDE.
  - Portrait (9:16): title card + burned-in captions. B02-B03 split is
    TOP/BOTTOM stacked (narrow safe width can't fit two side panels).

Render (16:9 deep-dive):
  manim -qh horse_cart_paradox.py HorseCartParadox
Render (9:16 short — NOT -qh: it forces 1920x1080 and overrides -r):
  manim -r 1080,1920 --fps 60 --disable_caching horse_cart_paradox.py HorseCartParadox
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

# config.frame_width does not auto-recompute from -r's aspect ratio in this
# Manim version (confirmed across ball_and_feather.py/car_turning.py/
# rain_relative_motion.py) — detect orientation from pixel dims instead.
PORTRAIT = config.pixel_width < config.pixel_height
if PORTRAIT:
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

CREAM = "#FFFFFF"
INK = "#000000"
TEAL = "#009E73"
CRIMSON = "#D55E00"
SLATE = "#4D4D4D"
GOLD = "#F0E442"

HORSE_COLOR = SLATE
CART_COLOR = CREAM  # outline-only (hollow), distinguishes it from the solid horse

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
    HORSE_X, CART_X = -0.7, 0.7
    GROUND_Y = -0.6
    ICON_SCALE = 0.6
    FONT_LABEL, FONT_EQ, FONT_FINAL = 14, 18, 16
    PANEL_GROUND_Y = 0.0
    LEFT_X = RIGHT_X = 0.0
    TOP_PANEL_Y = 1.5  # title_y = TOP_PANEL_Y + 1.95*ICON_SCALE(0.6) = 2.67, clear of TOP_Y=2.8
    BOTTOM_PANEL_Y = -0.85
    DIVIDER_Y = 0.5
    FINAL_Y = -1.55  # was -1.85 — 4-line wrapped text there overlapped the caption band (confirmed bug)
    ARROW_LEN = 0.55
else:
    HORSE_X, CART_X = -1.8, 1.8
    GROUND_Y = -1.0
    ICON_SCALE = 1.0
    FONT_LABEL, FONT_EQ, FONT_FINAL = 24, 32, 26
    PANEL_GROUND_Y = -1.0
    LEFT_X, RIGHT_X = -3.3, 3.3
    TOP_PANEL_Y = None
    BOTTOM_PANEL_Y = None
    DIVIDER_Y = None
    FINAL_Y = -2.3
    ARROW_LEN = 1.0


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


def make_horse(x, ground_y, scale=1.0):
    s = scale
    body = Ellipse(width=0.9 * s, height=0.45 * s, color=INK, fill_color=HORSE_COLOR, fill_opacity=1)
    body.move_to([x, ground_y + 0.42 * s, 0])
    head = Circle(radius=0.16 * s, color=INK, fill_color=HORSE_COLOR, fill_opacity=1)
    head.move_to([x - 0.5 * s, ground_y + 0.55 * s, 0])
    leg1 = Line([x - 0.3 * s, ground_y + 0.2 * s, 0], [x - 0.3 * s, ground_y, 0], color=INK, stroke_width=3)
    leg2 = Line([x + 0.3 * s, ground_y + 0.2 * s, 0], [x + 0.3 * s, ground_y, 0], color=INK, stroke_width=3)
    return VGroup(body, head, leg1, leg2)


def make_cart(x, ground_y, scale=1.0):
    s = scale
    box = Rectangle(width=0.7 * s, height=0.45 * s, color=INK, fill_color=CART_COLOR, fill_opacity=1)
    box.move_to([x, ground_y + 0.35 * s, 0])
    wheel1 = Circle(radius=0.12 * s, color=INK, fill_color=CREAM, fill_opacity=1).move_to(
        [x - 0.2 * s, ground_y + 0.1 * s, 0]
    )
    wheel2 = Circle(radius=0.12 * s, color=INK, fill_color=CREAM, fill_opacity=1).move_to(
        [x + 0.2 * s, ground_y + 0.1 * s, 0]
    )
    return VGroup(box, wheel1, wheel2)


class HorseCartParadox(Scene):
    def construct(self):
        if PORTRAIT:
            self._init_captions()
            self.question_card()
        self.b00_hook()
        self.b01_naive_cancellation()
        self.b02_split()
        self.b03_net_force()
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

    # ---------------- B00 — Hook ----------------
    def b00_hook(self):
        self.horse = make_horse(HORSE_X, GROUND_Y, ICON_SCALE)
        self.cart = make_cart(CART_X, GROUND_Y, ICON_SCALE)
        self.rope = Line(
            [HORSE_X + 0.45 * ICON_SCALE, GROUND_Y + 0.3 * ICON_SCALE, 0],
            [CART_X - 0.35 * ICON_SCALE, GROUND_Y + 0.3 * ICON_SCALE, 0],
            color=INK, stroke_width=2,
        )
        mid_y = GROUND_Y + 0.8 * ICON_SCALE
        arrow_hc = Arrow(
            [HORSE_X + 0.5 * ICON_SCALE, mid_y, 0], [CART_X - 0.5 * ICON_SCALE, mid_y, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        # 0.5*ICON_SCALE between the two arrows wasn't enough clearance for
        # both "500 N" labels above them — they landed on top of each other
        # (confirmed bug in the rendered short). 0.9 gives enough room that
        # label_hc's top clears label_ch's bottom.
        label_hc = Text("500 N", font_size=FONT_LABEL, color=CRIMSON).next_to(arrow_hc, UP, buff=0.1)
        mid_y2 = mid_y + 0.9 * ICON_SCALE
        arrow_ch = Arrow(
            [CART_X - 0.5 * ICON_SCALE, mid_y2, 0], [HORSE_X + 0.5 * ICON_SCALE, mid_y2, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        label_ch = Text("500 N", font_size=FONT_LABEL, color=CRIMSON).next_to(arrow_ch, UP, buff=0.1)

        self.play(
            FadeIn(self.horse), FadeIn(self.cart), Create(self.rope),
            GrowArrow(arrow_hc), FadeIn(label_hc),
            GrowArrow(arrow_ch), FadeIn(label_ch),
            run_time=1.4,
        )
        self.arrow_hc, self.label_hc, self.arrow_ch, self.label_ch = arrow_hc, label_hc, arrow_ch, label_ch
        self.wait(max(DURS["B00"] - 1.4, 0.3))

    # ---------------- B01 — naive cancellation ----------------
    def b01_naive_cancellation(self):
        mid_x = (HORSE_X + CART_X) / 2
        mid_y = (self.arrow_hc.get_start()[1] + self.arrow_ch.get_start()[1]) / 2
        target1 = Arrow(
            [mid_x - 0.3, mid_y, 0], [mid_x, mid_y, 0], color=CRIMSON, buff=0, stroke_width=6
        ).set_opacity(0.5)
        target2 = Arrow(
            [mid_x, mid_y, 0], [mid_x - 0.3, mid_y, 0], color=CRIMSON, buff=0, stroke_width=6
        ).set_opacity(0.5)
        self.play(
            FadeOut(self.label_hc), FadeOut(self.label_ch),
            Transform(self.arrow_hc, target1), Transform(self.arrow_ch, target2),
            run_time=1.0,
        )
        # MathTex, not Text — Open Sans renders "0" with a slash that reads
        # as the empty-set symbol (confirmed bug in the contact-sheet scan)
        zero = MathTex("0", font_size=FONT_EQ * 1.6, color=SLATE).move_to([mid_x, mid_y, 0])
        strike = Line(
            zero.get_corner(DOWN + LEFT) + LEFT * 0.05, zero.get_corner(UP + RIGHT) + RIGHT * 0.05,
            color=SLATE, stroke_width=4,
        )
        self.play(
            FadeOut(self.arrow_hc), FadeOut(self.arrow_ch),
            FadeIn(zero), Create(strike),
            run_time=0.8,
        )
        self.wait(max(DURS["B01"] - 1.8, 0.3))
        self.play(FadeOut(zero), FadeOut(strike), run_time=0.5)

    # ---------------- B02 — split into free-body diagrams ----------------
    def b02_split(self):
        self.play(FadeOut(self.horse), FadeOut(self.cart), FadeOut(self.rope), run_time=0.5)

        if PORTRAIT:
            horse_panel_y, cart_panel_y = TOP_PANEL_Y, BOTTOM_PANEL_Y
            divider = Line(
                [-safe_half_w() + 0.2, DIVIDER_Y, 0], [safe_half_w() - 0.2, DIVIDER_Y, 0],
                color=SLATE, stroke_width=2,
            )
            horse_x, cart_x = 0.0, 0.0
        else:
            horse_panel_y = cart_panel_y = PANEL_GROUND_Y
            divider = Line([0, -safe_half_h() + 0.3, 0], [0, TOP_Y, 0], color=SLATE, stroke_width=2)
            horse_x, cart_x = LEFT_X, RIGHT_X

        self.play(Create(divider), run_time=0.4)

        self.horse2 = make_horse(horse_x, horse_panel_y, ICON_SCALE * 0.8)
        self.cart2 = make_cart(cart_x, cart_panel_y, ICON_SCALE * 0.8)

        # explicit fixed height, not next_to(icon) — the panel title needs to
        # clear the "above" force arrow + its label too, not just the icon
        title_y = horse_panel_y + 1.95 * ICON_SCALE
        horse_label = Text("FREE-BODY: HORSE", font_size=FONT_LABEL - 2, color=INK).move_to(
            [horse_x, title_y, 0]
        )
        title_y_c = cart_panel_y + 1.95 * ICON_SCALE
        cart_label = Text("FREE-BODY: CART", font_size=FONT_LABEL - 2, color=INK).move_to(
            [cart_x, title_y_c, 0]
        )

        # One arrow ABOVE the icon, one BELOW — the earlier version put both
        # ~0.35 apart at similar height with overlapping horizontal spans,
        # so the two arrows visually merged and both labels collided
        # (confirmed bug in the contact-sheet scan). Labels point further
        # away from the icon (UP for the top arrow, DOWN for the bottom),
        # so neither label can ever land on the icon either.
        above_y = horse_panel_y + 1.15 * ICON_SCALE
        below_y = horse_panel_y - 0.35 * ICON_SCALE
        self.h_pull = Arrow(
            [horse_x + ARROW_LEN / 2, above_y, 0], [horse_x - ARROW_LEN / 2, above_y, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        h_pull_label = Text("500 N", font_size=FONT_LABEL, color=CRIMSON).next_to(self.h_pull, UP, buff=0.12)
        self.h_ground = Arrow(
            [horse_x - ARROW_LEN / 2, below_y, 0], [horse_x + ARROW_LEN / 2, below_y, 0],
            color=TEAL, buff=0, stroke_width=6,
        )
        h_ground_label = Text("600 N", font_size=FONT_LABEL, color=TEAL).next_to(self.h_ground, DOWN, buff=0.12)

        above_y_c = cart_panel_y + 1.15 * ICON_SCALE
        below_y_c = cart_panel_y - 0.35 * ICON_SCALE
        self.c_pull = Arrow(
            [cart_x - ARROW_LEN / 2, above_y_c, 0], [cart_x + ARROW_LEN / 2, above_y_c, 0],
            color=CRIMSON, buff=0, stroke_width=6,
        )
        c_pull_label = Text("500 N", font_size=FONT_LABEL, color=CRIMSON).next_to(self.c_pull, UP, buff=0.12)
        self.c_fric = Arrow(
            [cart_x + ARROW_LEN / 2, below_y_c, 0], [cart_x - ARROW_LEN / 2, below_y_c, 0],
            color=TEAL, buff=0, stroke_width=6,
        )
        c_fric_label = Text("200 N", font_size=FONT_LABEL, color=TEAL).next_to(self.c_fric, DOWN, buff=0.12)

        self.play(
            FadeIn(self.horse2), FadeIn(self.cart2), FadeIn(horse_label), FadeIn(cart_label),
            GrowArrow(self.h_pull), FadeIn(h_pull_label),
            GrowArrow(self.h_ground), FadeIn(h_ground_label),
            GrowArrow(self.c_pull), FadeIn(c_pull_label),
            GrowArrow(self.c_fric), FadeIn(c_fric_label),
            run_time=1.4,
        )
        (self.h_pull_label, self.h_ground_label, self.c_pull_label, self.c_fric_label) = (
            h_pull_label, h_ground_label, c_pull_label, c_fric_label
        )
        self.divider = divider
        self.horse_panel_y, self.cart_panel_y = horse_panel_y, cart_panel_y
        self.horse_x, self.cart_x = horse_x, cart_x
        self.horse_label, self.cart_label = horse_label, cart_label
        self.wait(max(DURS["B02"] - 1.9, 0.3))

    # ---------------- B03 — net force resolves the paradox ----------------
    def b03_net_force(self):
        # net arrow sits at the same "above the icon" height the pull arrow
        # used — that's the position already proven clear of the icon and
        # the panel title (fixed in b02_split's overlap bugfix)
        h_mid_y = self.horse_panel_y + 1.15 * ICON_SCALE
        c_mid_y = self.cart_panel_y + 1.15 * ICON_SCALE

        h_net_target = Arrow(
            [self.horse_x - ARROW_LEN * 0.2, h_mid_y, 0],
            [self.horse_x - ARROW_LEN * 0.2 + ARROW_LEN * 0.4, h_mid_y, 0],
            color=GOLD, buff=0, stroke_width=8,
        ).set_opacity(1)
        c_net_target = Arrow(
            [self.cart_x - ARROW_LEN * 0.35, c_mid_y, 0],
            [self.cart_x - ARROW_LEN * 0.35 + ARROW_LEN * 0.7, c_mid_y, 0],
            color=GOLD, buff=0, stroke_width=8,
        ).set_opacity(1)

        self.play(
            FadeOut(self.h_pull_label), FadeOut(self.h_ground_label),
            FadeOut(self.c_pull_label), FadeOut(self.c_fric_label),
            run_time=0.4,
        )
        self.play(
            ReplacementTransform(VGroup(self.h_pull, self.h_ground), h_net_target),
            ReplacementTransform(VGroup(self.c_pull, self.c_fric), c_net_target),
            run_time=1.0,
        )
        h_net_label = Text("Net: 100 N", font_size=FONT_LABEL, color=GOLD).next_to(h_net_target, UP, buff=0.15)
        # gold text is unreadable directly on white — outline it in ink so
        # the "highlighter fill only, never text" rule doesn't leave it blank
        h_net_label.set_stroke(color=INK, width=1)
        c_net_label = Text("Net: 300 N", font_size=FONT_LABEL, color=GOLD).next_to(c_net_target, UP, buff=0.15)
        c_net_label.set_stroke(color=INK, width=1)
        self.play(FadeIn(h_net_label), FadeIn(c_net_label), run_time=0.6)
        self.h_net_label, self.c_net_label = h_net_label, c_net_label
        # the arrows themselves (not just their labels) need to be faded in
        # b04_outro too — confirmed bug: they were local vars, never stored,
        # so ReplacementTransform's own added mobjects lingered as ghosts
        self.h_net_target, self.c_net_target = h_net_target, c_net_target
        self.wait(max(DURS["B03"] - 2.0, 0.3))

    # ---------------- B04 — Outro (plain, held frame) ----------------
    def b04_outro(self):
        # horse_label/cart_label ("FREE-BODY: HORSE/CART") were never faded
        # out here — confirmed bug via the portrait contact-sheet scan: they
        # persisted through B03 and B04, ending up under the gold punchline
        self.play(
            FadeOut(self.divider), FadeOut(self.h_net_label), FadeOut(self.c_net_label),
            FadeOut(self.horse_label), FadeOut(self.cart_label),
            FadeOut(self.h_net_target), FadeOut(self.c_net_target),
            run_time=0.5,
        )
        target_ground_y = GROUND_Y if not PORTRAIT else 0.3
        target_horse_x, target_cart_x = HORSE_X, CART_X
        rope = Line(
            [target_horse_x + 0.45 * ICON_SCALE, target_ground_y + 0.3 * ICON_SCALE, 0],
            [target_cart_x - 0.35 * ICON_SCALE, target_ground_y + 0.3 * ICON_SCALE, 0],
            color=INK, stroke_width=2,
        )
        horse_final = make_horse(target_horse_x, target_ground_y, ICON_SCALE)
        cart_final = make_cart(target_cart_x, target_ground_y, ICON_SCALE)
        self.play(
            ReplacementTransform(self.horse2, horse_final),
            ReplacementTransform(self.cart2, cart_final),
            Create(rope),
            run_time=1.0,
        )

        final_text = Text(
            "\n".join(textwrap.wrap(
                "Action-reaction pairs act on different objects, so they never cancel.",
                width=30 if PORTRAIT else 40,
            )),
            font_size=FONT_FINAL, color=INK, line_spacing=1.2,
        ).move_to([0, FINAL_Y, 0])
        final_bg = SurroundingRectangle(
            final_text, color=GOLD, fill_color=GOLD, fill_opacity=0.6, buff=0.2,
        )
        self.play(FadeIn(final_bg), FadeIn(final_text), run_time=0.6)
        self.wait(max(DURS["B04"] - 2.1, 0.3))
