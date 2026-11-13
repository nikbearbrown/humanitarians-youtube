"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-13-context-window-limits
"Context Window Limits: The Budget That Doesn't Grow"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command -- NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (built with
--no-endcard --handle "@HumanitariansAI" explicitly, since shorts.py's
default handle is @nikbearbrown and defaults to adding a silent endcard even
under --vertical). All 9 parent beats are kept; every mp3 is reused
byte-for-byte from the parent's mp3/ folder. Every beat here is a Manim
GRAPHIC beat, so each class below is a genuine portrait RE-LAYOUT of the
parent ../scenes.py composition, authored by hand for a narrow portrait
canvas (rendered at 2160x3840 for the true 4K vertical final), not a
mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's y-axis safe/hard bounds carry over unchanged; only
frame_width shrinks (~4.5 instead of 14.222). MAX_W = 3.4 is this file's
general content-width budget, copied from this fellow's sibling reels' own
portrait-redesign convention (2026-11-04-goodharts-law-proxy-metrics/
vertical/scenes.py, 2026-10-28-in-context-learning-limits/vertical/
scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard            -- title re-wrapped onto 3 narrower lines.
  B01 ExecSummary           -- badge stacked ABOVE name/role; summary re-wrapped (5 lines).
  B02 FixedPoolHook          -- budget panel narrowed; trend/tag rows stacked (already DOWN in landscape after its own fix).
  B03 ThreeQuestionsFramework  -- already single-column; each card's body re-wrapped onto 2 lines.
  B04 SilentTruncation           -- budget panel narrowed (smaller fonts, tighter padding), rows stacked.
  B05 ExplicitRejectionHolds      -- same narrowed panel + checked/caught tags stacked, not inline.
  B06 AuditChecklist                -- already single-column; items re-wrapped narrower.
  B07 Statement                       -- centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                        -- unchanged composition; widths trimmed.

Every element within a beat is positioned by chaining `next_to()` off the
block above it (never hand-picked absolute y-coordinates) -- the sibling
reels' BUILD-LOGs document real title/content collisions from absolute
coordinates not accounting for how real rendered heights combine once a
layout is redesigned for a narrow canvas, and this file's own landscape
sibling (`../scenes.py`) hit a real chained-RIGHT drift bug on B02 that
pushed a tag off-frame -- the fix there (stack DOWN, let each line center
independently) is applied by default throughout this portrait file rather
than re-discovered.

Palette/MONO/fit()/T()/panel()/box_around()/stat_row()/metric_panel() are
copied from ../scenes.py for visual continuity. Nothing about WHAT is said
or WHEN changes here -- every self.play/self.wait duration matches
../scenes.py beat-for-beat, so total runtime matches the landscape master
exactly -- only how it is laid out for the narrow canvas.
"""

from manim import *
import numpy as np

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup -- BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait -- every
# coordinate in this file is designed against a ~4.5-wide frame, so without
# this fix everything would render far too small and clustered dead-center.
# Copied verbatim from both sibling reels' vertical/scenes.py, which found
# and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- safe as a STROKE/accent on
                          # ink; avoid as TEXT color on ink (0.28 sep).
    "slate":  "#29335C",  # structure -- 0.04 luminance sep on ink (broken);
                          # use "sage" for any note/tag text on ink.
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as alert TEXT on ink.
    "sage":   "#A8C686",  # human / growth / confirmed; safe secondary text on ink.
}

MONO = "Courier New"
MAX_W = 3.4   # general portrait content-width budget (safe half-width ~1.95)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size -- avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See ../scenes.py for the empirical proof."""
    t = Text(text, font_size=SAFE_TEXT_BASE, **kwargs)
    if font_size != SAFE_TEXT_BASE:
        t.scale(font_size / SAFE_TEXT_BASE)
    return t


def panel(width, height, fill=None, stroke=None, corner_radius=0.12, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def box_around(mob, buff=0.12, color=None):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color or PALETTE["gold"], stroke_width=3, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


def stat_row(label, value, label_color, value_color, font_size=18, value_font_size=None):
    """One 'LABEL : VALUE' budget row, portrait-narrowed: STACKED DOWN (label
    over value), not arranged RIGHT -- the narrow canvas can't fit a long
    label and a value on one line without overflowing MAX_W."""
    value_font_size = value_font_size or font_size
    label_t = fit(T(label, color=label_color, font_size=font_size - 2, font=MONO, weight="BOLD"), MAX_W - 0.3)
    value_t = T(value, color=value_color, font_size=value_font_size, font=MONO, weight="BOLD")
    return VGroup(label_t, value_t).arrange(DOWN, buff=0.1, aligned_edge=LEFT)


def metric_panel(label_text, label_color, row_group, fill, stroke, buff=0.3, label_font=14):
    """A bordered panel holding a label over a stack of stat_row()s --
    narrower padding than the landscape version. Returns (full_group, box,
    content). content[1] is the row_group itself (NOT double-indexed) --
    same return-contract discipline as ../scenes.py."""
    label = fit(T(label_text, color=label_color, font_size=label_font, font=MONO, weight="BOLD"), MAX_W - 0.2)
    content = VGroup(label, row_group).arrange(DOWN, buff=0.28)
    box = panel(width=content.width + 0.5, height=content.height + 0.4,
                fill=fill, stroke=stroke, corner_radius=0.12, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.128s -- fixed target, matches ../scenes.py.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Context Window", color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
        title_line2 = fit(T("Limits:", color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
        title_line3 = fit(T("The Budget That Doesn't Grow", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=22)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=4.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder matches the measured 4.128s silent track
        self.wait(2.528)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 16.49s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.45, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=30, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=16), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        # badge STACKED ABOVE name/role (not side-by-side) -- a narrow canvas
        # can't fit a circular badge and a two-line name block on one row.
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.2)

        summary_lines = [
            "This video: context",
            "window limits — the fixed",
            "budget every prompt has",
            "to fit inside, measured",
            "in tokens — and three",
            "tests for going over it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        frame = panel(width=4.0, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder matches the measured 16.49s Kokoro length (16.49-2.1=14.39)
        self.wait(14.39)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: a generic context-window budget panel filling up row by row --
# then an overlay posing the real question: full -- did it tell you?
# measured audio: 22.61s
# --------------------------------------------------------------------------- #
class B02_FixedPoolHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_l1 = fit(T("One prompt.", color=PALETTE["bg"], font_size=24), MAX_W)
        title_l2 = fit(T("One shared pool.", color=PALETTE["bg"], font_size=24), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        rows = VGroup(
            stat_row("INSTRUCTIONS", "150 TOK", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("DOCUMENT", "700 TOK", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("HISTORY", "GROWING", PALETTE["bg"], PALETTE["sage"]),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "CONTEXT WINDOW (FIXED BUDGET)", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.4)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        trend_label = T("MEASURED IN:", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        trend_row = T("TOKENS", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD")
        trend_block = VGroup(trend_label, trend_row).arrange(DOWN, buff=0.1)
        trend_block.next_to(panel_group, DOWN, buff=0.35)
        self.play(FadeIn(trend_block), run_time=0.4)
        self.wait(0.5)

        # stacked DOWN, each centered independently at x=0 -- the landscape
        # sibling's B02 hit a real off-frame bug chaining these RIGHT; this
        # portrait file never reproduces that chain in the first place.
        looks_good = T("NOT CHARACTERS", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        looks_good.next_to(trend_block, DOWN, buff=0.2)
        self.play(FadeIn(looks_good), run_time=0.4)
        correct_tag = T("NOT WORDS EITHER", color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD")
        correct_tag.next_to(looks_good, DOWN, buff=0.15)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.3)
        same_tag = fit(T("THE POOL DOESN'T GROW.", color=PALETTE["sage"], font_size=15, font=MONO), MAX_W)
        same_tag.next_to(bottom_rule, DOWN, buff=0.25)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # GATE V canvas-fill MAJOR found on the TRUE vertical candidate
        # (underfill, 44% of the safe area at both sample points, min 55%):
        # this overlay was sized for a quick landscape beat and left most of
        # the tall portrait frame empty. Fixed with genuine added content
        # mass -- larger real text, wider real rules (near the portrait
        # safe half-width), and more real spacing between real elements --
        # not an invisible padding rectangle. Zero change to beat timing.
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Full.", color=PALETTE["bg"], font_size=42, weight="BOLD"), MAX_W)
        overlay_line2 = fit(T("Did it tell you?", color=PALETTE["bg"], font_size=36, weight="BOLD"), MAX_W)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.22)
        top_rule2 = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=1.05).move_to(ORIGIN)

        content_group = VGroup(title, panel_group, trend_block, looks_good, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # sum of plays = 0.5+0.4+0.8+0.4+0.4+0.3+0.4+0.5+0.6 = 4.3s
        # waits above = 0.5+0.2+0.8+0.5+0.5+0.3 = 2.8s (front-loaded, same as landscape)
        # remainder matches the measured 22.61s Kokoro length (22.61-4.3-2.8=15.51)
        self.wait(15.51)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 34.10s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions,", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title2 = fit(T("before any example:", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.8)

        # GATE V canvas-fill MAJOR found on the TRUE vertical candidate
        # (underfill, 54% of the safe area, min 55%): this card's original
        # sizing (copied too close to the landscape file's proportions)
        # left the tall portrait frame just barely under the fill floor.
        # Fixed with genuine added content mass -- larger real badges/text
        # and more real spacing between the 3 real cards -- not a padding
        # trick. Zero change to beat timing.
        def test_card(num, head, body_lines):
            badge = Square(side_length=0.48, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=21, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = fit(T(head, color=PALETTE["teal"], font_size=22, weight="BOLD"), MAX_W - 0.5)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.2)
            body_t = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=16), MAX_W - 0.2) for l in body_lines]
                            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            row = VGroup(head_row, body_t).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            body_t.align_to(head_row, LEFT)
            return row

        card1 = test_card(1, "Count the Tokens",
                           ["Measured in tokens,", "not characters or words?"])
        card2 = test_card(2, "Share the Pool",
                           ["Instructions, documents,", "history, output — ONE budget?"])
        card3 = test_card(3, "Watch the Edge",
                           ["Error loudly, or drop", "something quietly?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 0.6, height=cards.height + 0.8,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title_block, DOWN, buff=0.35)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)

        closing1 = fit(T("A budget you can't see", color=PALETTE["gold"], font_size=16, weight="BOLD"), MAX_W)
        closing2 = fit(T("filling up, you can't manage.", color=PALETTE["gold"], font_size=16, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.8+0.3+8.5+8.5+8.5 = 26.6s
        # remainder matches the measured 34.10s Kokoro length (34.10-2.9-26.6=4.6)
        self.wait(4.6)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: a fixed budget, already mostly committed, and a
# growing conversation history that pushes past the room that's left --
# the oldest turns quietly dropped, nothing said about it. Tagged
# TRUNCATED -- SILENTLY.
# measured audio: 31.75s
# --------------------------------------------------------------------------- #
class B04_SilentTruncation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A budget, under", color=PALETTE["bg"], font_size=22, weight="BOLD"), MAX_W)
        title2 = fit(T("real pressure.", color=PALETTE["bg"], font_size=22, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.55)
        self.play(Write(title_block), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("INSTR + DOCUMENT (FIXED)", "850 TOK", PALETTE["bg"], PALETTE["teal_on_ink"], font_size=15)
        history_row = stat_row("CONVERSATION HISTORY", "150 TOK", PALETTE["bg"], PALETTE["sage"], font_size=15)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "SHARING A 1,000-TOKEN BUDGET", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title_block, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        pressure_label = T("PRESSURE:", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        pressure_val = fit(T("CONVERSATION KEEPS GOING", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        pressure_block = VGroup(pressure_label, pressure_val).arrange(DOWN, buff=0.1)
        pressure_block.next_to(panel_group, DOWN, buff=0.4)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        new_history_val = T("310 TOK", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD")
        new_history_val.move_to(history_row[1].get_center())
        self.play(FadeOut(history_row[1]), FadeIn(new_history_val), run_time=0.4)
        self.wait(1.3)

        gap_tag = fit(T("TRUNCATED — SILENTLY", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), MAX_W - 0.1)
        gap_tag.next_to(pressure_block, DOWN, buff=0.35)
        gap_box = box_around(gap_tag, buff=0.12, color=PALETTE["crimson"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing1 = fit(T("The reply still came back.", color=PALETTE["gold"], font_size=15), MAX_W)
        closing2 = fit(T("Nobody saw what left.", color=PALETTE["gold"], font_size=15), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        bottom_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.55)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.3+0.3+0.5 = 3.5s
        # waits above = 0.8+1.5+1.0+1.3+1.5 = 6.1s
        # remainder matches the measured 31.75s Kokoro length (31.75-3.5-6.1=22.15)
        self.wait(22.15)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the identical budget, allocation, and overflow as
# B04 -- the ONLY change is that the system now checks the running total
# BEFORE answering. Tagged CAUGHT IMMEDIATELY.
# measured audio: 24.79s
# --------------------------------------------------------------------------- #
class B05_ExplicitRejectionHolds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Same pressure —", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title2 = fit(T("now it checks first.", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["slate"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.55)
        self.play(Write(title_block), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("INSTR + DOCUMENT (FIXED)", "850 TOK", PALETTE["ink"], PALETTE["teal"], font_size=15)
        history_row = stat_row("CONVERSATION HISTORY", "150 TOK", PALETTE["ink"], PALETTE["slate"], font_size=15)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "SHARING THE SAME 1,000-TOK BUDGET", PALETTE["slate"], rows,
            fill=PALETTE["bg"], stroke=PALETTE["slate"])
        panel_group.next_to(title_block, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        check_box = Rectangle(width=history_row.width + 0.2, height=history_row.height + 0.14,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        check_box.move_to(history_row.get_center())
        check_tag = fit(T("CHECKED BEFORE ANSWERING", color=PALETTE["gold"], font_size=13, font=MONO, weight="BOLD"), MAX_W - 0.1)
        check_tag.next_to(panel_group, DOWN, buff=0.25)
        self.play(Create(check_box), FadeIn(check_tag), run_time=0.4)
        self.wait(0.9)

        pressure_label = T("PRESSURE:", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD")
        pressure_val = T("SAME AS BEFORE", color=PALETTE["slate"], font_size=14, font=MONO, weight="BOLD")
        pressure_block = VGroup(pressure_label, pressure_val).arrange(DOWN, buff=0.1)
        pressure_block.next_to(VGroup(panel_group, check_tag), DOWN, buff=0.4)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        new_history_val = T("310 TOK", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD")
        new_history_val.move_to(history_row[1].get_center())
        self.play(FadeOut(history_row[1]), FadeIn(new_history_val), run_time=0.4)
        self.wait(0.6)

        caught_tag = fit(T("CAUGHT IMMEDIATELY", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD"), MAX_W - 0.1)
        caught_tag.next_to(pressure_block, DOWN, buff=0.35)
        caught_box = box_around(caught_tag, buff=0.12, color=PALETTE["teal"])
        self.play(FadeIn(caught_tag), run_time=0.3)
        self.play(Create(caught_box), run_time=0.3)
        self.wait(1.5)

        closing1 = fit(T("Same overflow — this time,", color=PALETTE["ink"], font_size=17, weight="BOLD"), MAX_W)
        closing2 = fit(T("it said so.", color=PALETTE["ink"], font_size=17, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        bottom_rule = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["slate"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.55)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.3+0.3+0.5 = 3.9s
        # waits above = 0.8+0.5+0.9+1.0+0.6+1.5 = 5.3s
        # remainder matches the measured 24.79s Kokoro length (24.79-3.9-5.3=15.59)
        self.wait(15.59)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 28.13s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=22), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # GATE V canvas-fill MAJOR found on the TRUE vertical candidate
        # (underfill, 47% of the safe area, min 55%): fixed with genuine
        # added content mass -- bigger real checkboxes/text and more real
        # spacing between the 3 real rows -- not a padding trick. Zero
        # change to beat timing.
        def checklist_item(lines):
            box = Square(side_length=0.75, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W - 1.0) for l in lines]
                          ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            row = VGroup(box, check).arrange(RIGHT, buff=0.35)
            return row, box

        row1, box1 = checklist_item(["Pick a system with a", "length or size limit."])
        row2, box2 = checklist_item(["Go a little over it,", "on purpose."])
        row3, box3 = checklist_item(["See what breaks —", "loudly, or silently."])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.75)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.4)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(0.8)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(6.2)
        self.play(Create(mark2), run_time=0.3)
        self.wait(6.2)
        self.play(Create(mark3), run_time=0.3)
        self.wait(6.2)

        closing1 = fit(T("If something vanished", color=PALETTE["ink"], font_size=16), MAX_W)
        closing2 = fit(T("without a word — find out", color=PALETTE["ink"], font_size=16), MAX_W)
        closing3 = fit(T("exactly what got dropped.", color=PALETTE["ink"], font_size=16), MAX_W)
        closing_block = VGroup(closing1, closing2, closing3).arrange(DOWN, buff=0.1)
        closing_block.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.8+0.8+6.2+6.2+6.2 = 20.2s
        # remainder matches the measured 28.13s Kokoro length (28.13-2.8-20.2=5.13)
        self.wait(5.13)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: statement card.
# measured audio: 14.16s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("A context window", color=PALETTE["bg"], font_size=24), MAX_W)
        line1b = fit(T("isn't elastic —", color=PALETTE["bg"], font_size=24), MAX_W)
        line1c = fit(T("it's a fixed budget for", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        line1d = fit(T("everything you put in.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        line2 = fit(T("Going over it was", color=PALETTE["gold"], font_size=26), MAX_W)
        line2b = fit(T("never the real question.", color=PALETTE["gold"], font_size=26), MAX_W)
        line2c = fit(T("Whether it told you is", color=PALETTE["gold"], font_size=27, weight="BOLD"), MAX_W)
        line2d = fit(T("the one that matters.", color=PALETTE["gold"], font_size=27, weight="BOLD"), MAX_W)

        block1 = VGroup(line1, line1b, line1c, line1d).arrange(DOWN, buff=0.18)
        block2 = VGroup(line2, line2b, line2c, line2d).arrange(DOWN, buff=0.2)
        content = VGroup(block1, block2).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=4.0, height=min(content.height + 0.8, 7.2), fill=PALETTE["ink"],
                       stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 0.3+0.6+0.6+0.3 = 1.8s, waits above = 5.2s (3.0+2.2);
        # remainder matches the measured 14.16s Kokoro length (14.16-1.8-5.2=7.16)
        self.wait(7.16)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V canvas-fill MAJOR found on the TRUE vertical candidate
        # (underfill, 34% of the safe area at both sample points, min 55%
        # -- the most severe underfill found in this build): this sign-off
        # card's text was sized for a quick landscape flash and left most
        # of the tall portrait frame empty. Fixed with genuine added
        # content mass -- substantially larger real text, a wider real
        # accent rule, and more real spacing -- not a padding trick. Zero
        # change to beat timing.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=50), MAX_W)
        accent = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=4)
        fixed_line = fit(T("explained with", color=PALETTE["ink"], font_size=30), MAX_W)
        fixed_line2 = fit(T("Claude Code", color=PALETTE["ink"], font_size=30), MAX_W)
        fixed_block = VGroup(fixed_line, fixed_line2).arrange(DOWN, buff=0.12)
        tagline = fit(T("in for", color=PALETTE["ink"], font_size=28), MAX_W)
        tagline2 = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=28), MAX_W)
        tag_block = VGroup(tagline, tagline2).arrange(DOWN, buff=0.12)
        content = VGroup(handle, accent, fixed_block, tag_block).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        # frame capped well inside the portrait safe half-width (1.95) --
        # the first fill-fix pass widened this frame enough to genuinely
        # bleed past the safe left/right margin (a real BLOCKER, caught by
        # GATE V on the true candidate, not a false positive); this cap
        # keeps the frame's own half-width at 1.85, a real 0.1 margin
        # inside the safe bound, while the taller stacked text blocks
        # above (genuine content, not padding) carry the fill ratio.
        frame_w = min(content.width + 0.6, 3.7)
        frame_h = min(content.height + 0.8, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 0.5s; remainder matches the measured 1.51s Kokoro length
        self.wait(1.01)
