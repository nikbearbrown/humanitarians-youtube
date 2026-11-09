"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-04-goodharts-law-proxy-metrics
"Goodhart's Law: When the Proxy Stops Being the Target"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command -- NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard. All 9 parent
beats are kept; every mp3 is reused byte-for-byte from the parent's mp3/
folder. Every beat here is a Manim GRAPHIC beat, so each class below is a
genuine portrait RE-LAYOUT of the parent ../scenes.py composition, authored
by hand for a narrow portrait canvas (rendered at 2160x3840 for the true 4K
vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's y-axis safe/hard bounds carry over unchanged; only
frame_width shrinks (~4.5 instead of 14.222). MAX_W = 3.4 is this file's
general content-width budget, copied from this fellow's sibling reels' own
portrait-redesign convention (2026-10-21-calibration-why-confidence-isnt-
accuracy/vertical/scenes.py, 2026-10-28-in-context-learning-limits/vertical/
scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard                   -- title re-wrapped onto 4 narrower lines.
  B01 ExecSummary                  -- badge stacked ABOVE name/role; summary re-wrapped (6 lines).
  B02 ProxyUpTargetUpHook            -- metric panel narrowed; trend/tag rows stacked, not inline.
  B03 ThreeQuestionsFramework          -- already single-column; each card's body re-wrapped onto 2 lines.
  B04 HandleTimeDivergence               -- metric panel narrowed (smaller fonts, tighter padding), rows stacked.
  B05 CounterbalancedCheckHolds             -- same narrowed panel + scoreboard/caught tags stacked, not inline.
  B06 AuditChecklist                           -- already single-column; items re-wrapped narrower.
  B07 Statement                                  -- centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                                   -- unchanged composition; widths trimmed.

Every element within a beat is positioned by chaining `next_to()` off the
block above it (never hand-picked absolute y-coordinates) -- both sibling
reels' BUILD-LOGs document real title/content collisions from absolute
coordinates not accounting for how real rendered heights combine once a
layout is redesigned for a narrow canvas; chaining avoids that class of bug
by construction.

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
    """Portrait version of ../scenes.py's stat_row() -- smaller default
    font_size so a stack of these fits MAX_W. Label/value STACKED (DOWN), not
    arranged RIGHT, since this file's narrow canvas can't fit a long label and
    a value on one row without a mechanical shrink."""
    value_font_size = value_font_size or font_size
    label_t = fit(T(label, color=label_color, font_size=font_size - 3, font=MONO, weight="BOLD"), MAX_W - 0.3)
    value_t = T(value, color=value_color, font_size=value_font_size, font=MONO, weight="BOLD")
    return VGroup(label_t, value_t).arrange(DOWN, buff=0.08, aligned_edge=LEFT)


def metric_panel(label_text, label_color, row_group, fill, stroke, buff=0.2, label_font=14):
    """Portrait version of ../scenes.py's metric_panel() -- narrower padding
    and a smaller label font so the whole panel fits MAX_W. content[1] is the
    row_group itself (NOT double-indexed) -- same direct-indexing contract as
    the landscape file."""
    label = fit(T(label_text, color=label_color, font_size=label_font, font=MONO, weight="BOLD"), MAX_W - 0.3)
    content = VGroup(label, row_group).arrange(DOWN, buff=0.22)
    box = panel(width=content.width + 0.5, height=content.height + 0.4,
                fill=fill, stroke=stroke, corner_radius=0.12, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card. measured (silent) duration: 4.128s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Goodhart's", color=PALETTE["ink"], font_size=36, weight="BOLD"), MAX_W)
        title_line2 = fit(T("Law:", color=PALETTE["ink"], font_size=36, weight="BOLD"), MAX_W)
        title_line3 = fit(T("When the Proxy Stops", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_line4 = fit(T("Being the Target", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_line1, title_line2, title_line3, title_line4).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        # GATE V canvas-fill check: safe half-height is 3.6 (frame_height=8,
        # 5% margin). This frame's height stays at 7.0 (half 3.5, real
        # clearance) -- matching both sibling reels' already-confirmed-safe
        # dimension for this beat role, applied from the start.
        frame = panel(width=4.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.528)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: badge stacked above name/role (portrait redesign).
# measured audio: 13.78s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.45, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=32, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.22)

        summary_lines = [
            "This video: Goodhart's",
            "Law — when a measure",
            "becomes a target, it",
            "stops being a good",
            "measure — and three tests",
            "for what a proxy can hide.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        # GATE V edge-bleed guard: frame height fixed at 7.0 (half 3.5, real
        # clearance under the portrait safe half-height of 3.6) -- the exact
        # dimension both sibling reels confirmed safe for this beat role, not
        # the 7.4 that caused a real BLOCKER in the ICL reel's first vertical
        # candidate.
        frame = panel(width=4.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(11.68)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: portrait redesign -- same column order as landscape (title,
# panel, trend, tags, overlay) since the landscape file is already a single
# column; only widths/fonts narrow for MAX_W, and the trend/tag rows stack
# instead of sitting inline.
# measured audio: 20.14s
# --------------------------------------------------------------------------- #
class B02_ProxyUpTargetUpHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_l1 = fit(T("A number on the", color=PALETTE["bg"], font_size=24), MAX_W)
        title_l2 = fit(T("dashboard climbs...", color=PALETTE["bg"], font_size=24), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.12)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        rows = VGroup(
            stat_row("WEEK 1", "100", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("WEEK 2", "118", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("WEEK 3", "139", PALETTE["bg"], PALETTE["sage"]),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "DASHBOARD METRIC (PROXY)", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.45)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        trend_label = T("TREND:", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        trend_row = T("UP", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD")
        trend_block = VGroup(trend_label, trend_row).arrange(RIGHT, buff=0.3)
        trend_block.next_to(panel_group, DOWN, buff=0.4)
        self.play(FadeIn(trend_block), run_time=0.4)
        self.wait(0.5)

        looks_good = T("LOOKS GOOD", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        looks_good.next_to(trend_block, DOWN, buff=0.25)
        self.play(FadeIn(looks_good), run_time=0.4)
        correct_tag = fit(T("EVERYONE'S HAPPY", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        correct_tag.next_to(looks_good, DOWN, buff=0.2)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.35)
        same_tag_l1 = fit(T("BUT NOBODY'S CHECKED", color=PALETTE["sage"], font_size=15, font=MONO), MAX_W)
        same_tag_l2 = fit(T("THE REAL TARGET.", color=PALETTE["sage"], font_size=15, font=MONO), MAX_W)
        same_tag = VGroup(same_tag_l1, same_tag_l2).arrange(DOWN, buff=0.1)
        same_tag.next_to(bottom_rule, DOWN, buff=0.3)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # GATE V overlay-sizing guard: the sibling ICL reel's vertical B02
        # needed a genuinely bigger overlay (qmark/text/rules) to clear a
        # real underfill MAJOR on its TRUE final candidate. Applied those
        # confirmed-safe larger sizes here from the start.
        qmark = T("?", color=PALETTE["gold"], font_size=160, weight="BOLD")
        overlay_line1 = fit(T("Proxy up.", color=PALETTE["bg"], font_size=40, weight="BOLD"), MAX_W)
        overlay_line2 = fit(T("Target up too?", color=PALETTE["bg"], font_size=40, weight="BOLD"), MAX_W)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule2 = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=0.9).move_to(ORIGIN)

        content_group = VGroup(title, panel_group, trend_block, looks_good, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # waits front-loaded (matches ../scenes.py's B02 fix) so the
        # FadeOut/FadeIn transition completes well before GATE V's 50%/85%
        # steady-state sample points.
        self.wait(13.04)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: already single-column; card bodies re-wrapped onto 2
# narrower lines. measured audio: 29.06s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_l1 = fit(T("Three questions,", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title_l2 = fit(T("before any example:", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def test_card(num, head, body_lines):
            badge = Square(side_length=0.38, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = fit(T(head, color=PALETTE["teal"], font_size=18, weight="BOLD"), MAX_W - 0.9)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.18)
            body_t = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=14), MAX_W - 0.4) for l in body_lines]).arrange(
                DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(head_row, body_t).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            body_t.align_to(head_t, LEFT)
            return row

        card1 = test_card(1, "Name the Target",
                           ["What's the real thing this", "number stands in for?"])
        card2 = test_card(2, "Find the Lever",
                           ["Is anything scored, rewarded,", "or optimized on it?"])
        card3 = test_card(3, "Watch the Coupling",
                           ["Has production or incentive", "changed since you trusted it?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 0.3, height=cards.height + 0.6,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.4)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)

        closing_l1 = fit(T("If nothing's watching —", color=PALETTE["gold"], font_size=16, weight="BOLD"), MAX_W)
        closing_l2 = fit(T("it can drift and still look fine.", color=PALETTE["gold"], font_size=16, weight="BOLD"), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        self.wait(4.06)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: narrowed metric panel (same mechanism as landscape),
# rows stacked. measured audio: 27.74s
# --------------------------------------------------------------------------- #
class B04_HandleTimeDivergence(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_l1 = fit(T("A proxy, under", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title_l2 = fit(T("real pressure.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        proxy_row = stat_row("AVG HANDLE TIME (PROXY)", "6.5 MIN", PALETTE["bg"], PALETTE["teal_on_ink"], font_size=16)
        target_row = stat_row("REAL TARGET (OFF SCOREBOARD)", "82%", PALETTE["bg"], PALETTE["sage"], font_size=16)
        rows = VGroup(proxy_row, target_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "WHAT'S TRACKED VS. WHAT'S REAL", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        pressure_label = T("PRESSURE:", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        pressure_val = fit(T("REWARD SHORTER CALLS", color=PALETTE["gold"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        pressure_block = VGroup(pressure_label, pressure_val).arrange(DOWN, buff=0.1)
        pressure_block.next_to(panel_group, DOWN, buff=0.35)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        new_proxy_val = T("4.0 MIN", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        new_proxy_val.move_to(proxy_row[1].get_center())
        new_target_val = T("61%", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        new_target_val.move_to(target_row[1].get_center())
        self.play(FadeOut(proxy_row[1]), FadeOut(target_row[1]),
                  FadeIn(new_proxy_val), FadeIn(new_target_val), run_time=0.4)
        self.wait(1.3)

        gap_tag = fit(T("DIVERGED — NOBODY SAW IT", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        gap_tag.next_to(pressure_block, DOWN, buff=0.3)
        gap_box = box_around(gap_tag, buff=0.1, color=PALETTE["crimson"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing_l1 = fit(T("The tracked number improved.", color=PALETTE["gold"], font_size=15), MAX_W)
        closing_l2 = fit(T("The real target got worse.", color=PALETTE["gold"], font_size=15), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        self.wait(18.14)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: narrowed metric panel, scoreboard/caught tags
# stacked. measured audio: 26.93s
# --------------------------------------------------------------------------- #
class B05_CounterbalancedCheckHolds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_l1 = fit(T("Same pressure —", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_l2 = fit(T("now it's watched.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        proxy_row = stat_row("AVG HANDLE TIME (PROXY)", "6.5 MIN", PALETTE["ink"], PALETTE["teal"], font_size=16)
        check_row = stat_row("FIRST-CALL RESOLUTION (CHECK)", "82%", PALETTE["ink"], PALETTE["slate"], font_size=16)
        rows = VGroup(proxy_row, check_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "WHAT'S TRACKED — BOTH NUMBERS", PALETTE["slate"], rows,
            fill=PALETTE["bg"], stroke=PALETTE["slate"], label_font=12)
        panel_group.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        # GATE B text-on-text guard: the "ON THE SCOREBOARD" tag sits BELOW
        # the whole panel instead of inline next to the check row -- both
        # sibling reels' BUILD-LOGs document a real text-on-text bug from an
        # inline tag landing on the next row's text in a tightly-packed
        # portrait stack; placed below the full panel from the start here.
        check_box = Rectangle(width=check_row.width + 0.2, height=check_row.height + 0.1,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        check_box.move_to(check_row.get_center())
        check_tag = fit(T("ON THE SCOREBOARD", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        check_tag.next_to(panel_group, DOWN, buff=0.22)
        self.play(Create(check_box), run_time=0.2)
        self.play(FadeIn(check_tag), run_time=0.2)
        self.wait(0.9)

        pressure_label = T("PRESSURE:", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD")
        pressure_val = fit(T("SAME AS BEFORE", color=PALETTE["slate"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        pressure_block = VGroup(pressure_label, pressure_val).arrange(DOWN, buff=0.1)
        pressure_block.next_to(VGroup(panel_group, check_tag), DOWN, buff=0.35)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        new_proxy_val = T("4.0 MIN", color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
        new_proxy_val.move_to(proxy_row[1].get_center())
        new_check_val = T("61%", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        new_check_val.move_to(check_row[1].get_center())
        self.play(FadeOut(proxy_row[1]), FadeOut(check_row[1]),
                  FadeIn(new_proxy_val), FadeIn(new_check_val), run_time=0.4)
        self.wait(0.6)

        caught_tag = fit(T("CAUGHT — STAYS HONEST", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD"), MAX_W)
        caught_tag.next_to(pressure_block, DOWN, buff=0.3)
        caught_box = box_around(caught_tag, buff=0.1, color=PALETTE["teal"])
        self.play(FadeIn(caught_tag), run_time=0.3)
        self.play(Create(caught_box), run_time=0.3)
        self.wait(1.5)

        closing_l1 = fit(T("Same shortcut — this time,", color=PALETTE["ink"], font_size=15, weight="BOLD"), MAX_W)
        closing_l2 = fit(T("it shows up immediately.", color=PALETTE["ink"], font_size=15, weight="BOLD"), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        self.wait(17.73)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 28.44s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        def checklist_item(lines):
            box = Square(side_length=0.55, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=17), MAX_W - 0.8) for l in lines]).arrange(
                DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(box, check).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item(["Pick one number you", "already trust."])
        row2, box2 = checklist_item(["Say what it's really", "supposed to measure."])
        row3, box3 = checklist_item(["Check what changed in how", "it's made or scored."])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.5,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.45)
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

        closing1 = fit(T("If no second number would", color=PALETTE["ink"], font_size=15), MAX_W)
        closing2 = fit(T("catch the shortcut, that", color=PALETTE["ink"], font_size=15), MAX_W)
        closing3 = fit(T("proxy's worth a second look.", color=PALETTE["ink"], font_size=15), MAX_W)
        closing_block = VGroup(closing1, closing2, closing3).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(closing_block, shift=UP * 0.1), Create(bottom_rule), run_time=0.4)
        self.wait(5.44)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 17.33s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("Goodhart's Law isn't", color=PALETTE["bg"], font_size=22), MAX_W)
        line1b = fit(T("about bad metrics —", color=PALETTE["bg"], font_size=22), MAX_W)
        line1c = fit(T("it's about good metrics", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        line1d = fit(T("in changed conditions.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        line2 = fit(T("A proxy is correlated", color=PALETTE["gold"], font_size=22), MAX_W)
        line2b = fit(T("with the target only under", color=PALETTE["gold"], font_size=22), MAX_W)
        line2c = fit(T("the conditions it was", color=PALETTE["gold"], font_size=22, weight="BOLD"), MAX_W)
        line2d = fit(T("chosen in.", color=PALETTE["gold"], font_size=22, weight="BOLD"), MAX_W)

        block1 = VGroup(line1, line1b, line1c, line1d).arrange(DOWN, buff=0.14)
        block2 = VGroup(line2, line2b, line2c, line2d).arrange(DOWN, buff=0.14)
        content = VGroup(block1, block2).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        # GATE V canvas-fill guard: a content-fitted frame measured only 53%
        # of the safe area in the sibling ICL reel's equivalent beat. Sized
        # from the portrait safe bounds themselves (4.0 x 7.0) instead of the
        # text's own size, applied here from the start.
        frame = panel(width=4.0, height=7.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(10.33)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: unchanged composition; widths trimmed. measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=46), MAX_W)
        accent = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=26), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=24), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        # GATE V canvas-fill guard: fixed, generously sized, still-visible
        # bordered frame (matching B00/B01's own confirmed-safe dimensions)
        # instead of sizing the frame from this beat's short 4-line content
        # -- the sibling ICL reel's equivalent beat measured only 42% of the
        # safe area when sized from its own content.
        frame = panel(width=4.0, height=7.0,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.01)
