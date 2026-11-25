"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-19-embedding-model-staleness
"Embedding Model Staleness: The Index That Quietly Split in Two"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command -- NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (built with
--no-endcard --handle "@HumanitariansAI" explicitly, since shorts.py's
default handle is @nikbearbrown and defaults to adding a silent endcard even
under --vertical). All 10 parent beats are kept; every mp3 is reused
byte-for-byte from the parent's mp3/ folder. Every beat here is a Manim
GRAPHIC beat, so each class below is a genuine portrait RE-LAYOUT of the
parent ../scenes.py composition, authored by hand for a narrow portrait
canvas (rendered at 2160x3840 for the true 4K vertical final), not a
mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's y-axis safe/hard bounds carry over unchanged; only
frame_width shrinks (~4.5 instead of 14.222). MAX_W = 3.4 is this file's
general content-width budget, copied from this fellow's sibling reels' own
portrait-redesign convention (2026-11-13-context-window-limits/vertical/
scenes.py, 2026-11-04-goodharts-law-proxy-metrics/vertical/scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard              -- title re-wrapped onto 3 narrower lines.
  B01 ExecSummary             -- badge stacked ABOVE name/role; summary re-wrapped (5 lines).
  B02 SplitGeometryHook        -- vector-index panel narrowed; trailing tags stacked (already DOWN in landscape).
  B03 ThreeQuestionsFramework   -- already single-column; each card's body re-wrapped onto 2-3 lines.
  B04 SilentSplit                -- corpus panel narrowed (smaller fonts, tighter padding), rows stacked.
  B05 FullReembedHolds             -- same narrowed panel + re-embed/rank tags stacked, not inline.
  B06 MycroftRealWorldNote           -- code-quote panel narrowed; one quoted line per row, highlight boxes kept.
  B07 AuditChecklist                   -- already single-column; items re-wrapped narrower.
  B08 Statement                          -- centered text, re-wrapped onto narrower lines.
  B09 BrandOutro                           -- unchanged composition; widths trimmed.

Every element within a beat is positioned by chaining `next_to()` off the
block above it (never hand-picked absolute y-coordinates) -- the sibling
reels' BUILD-LOGs document real title/content collisions from absolute
coordinates not accounting for how real rendered heights combine once a
layout is redesigned for a narrow canvas. B02's trailing tags were already
stacked DOWN (not chained RIGHT) in the landscape file from the start, so
that specific bug class does not need re-fixing here, but the same
discipline is applied throughout this portrait file as a precaution.

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
# and documented this exact bug. VERIFIED present and active here (not just
# commented) -- see FRICTIONAL.md for the explicit confirmation step.
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
    created directly at a small font_size."""
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


def box_around(mob, buff=0.1, color=None):
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color or PALETTE["gold"], stroke_width=3, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


def stat_row(label, value, label_color, value_color, font_size=18, value_font_size=None):
    """Portrait variant: label STACKED OVER value (not beside it) -- the
    narrow ~4.5-unit portrait frame can't fit a long label and a value on
    one line the way the landscape file's side-by-side row does."""
    value_font_size = value_font_size or font_size
    label_t = fit(T(label, color=label_color, font_size=font_size - 2, font=MONO, weight="BOLD"), MAX_W)
    value_t = T(value, color=value_color, font_size=value_font_size, font=MONO, weight="BOLD")
    return VGroup(label_t, value_t).arrange(DOWN, buff=0.12, aligned_edge=LEFT)


def metric_panel(label_text, label_color, row_group, fill, stroke, buff=0.25):
    label = fit(T(label_text, color=label_color, font_size=15, font=MONO, weight="BOLD"), MAX_W)
    content = VGroup(label, row_group).arrange(DOWN, buff=0.26)
    box = panel(width=content.width + 0.5, height=content.height + 0.4,
                fill=fill, stroke=stroke, corner_radius=0.12, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent, 3 narrower lines + handle.
# measured (silent) duration: 4.128s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Embedding Model", color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
        title_line2 = fit(T("Staleness: The Index", color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W)
        title_line3 = fit(T("That Quietly Split in Two", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        frame = panel(width=3.7, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.528)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: badge stacked ABOVE name/role; summary re-wrapped 5 lines.
# measured audio: 17.78s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.5, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=26, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=32, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.3)

        summary_lines = [
            "This video: embedding",
            "model staleness — why",
            "swapping the model that",
            "embeds your documents",
            "can silently break search.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=22), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.16)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        frame = panel(width=3.8, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(15.68)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: vector-index panel narrowed; tags stacked (already DOWN).
# measured audio: 24.67s
# --------------------------------------------------------------------------- #
class B02_SplitGeometryHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("One index.", color=PALETTE["bg"], font_size=28), MAX_W)
        title2 = fit(T("Two geometries?", color=PALETTE["bg"], font_size=28), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.1)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.5)

        rows = VGroup(
            stat_row("MODEL A VECTORS", "384-DIM", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("MODEL B VECTORS", "384-DIM", PALETTE["bg"], PALETTE["sage"]),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "VECTOR INDEX (ONE SPACE?)", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title_block, DOWN, buff=0.45)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        trend_label = T("SAME DIMENSION:", color=PALETTE["sage"], font_size=17, font=MONO, weight="BOLD")
        trend_row = T("NOT COMPARABLE", color=PALETTE["gold"], font_size=19, font=MONO, weight="BOLD")
        trend_block = VGroup(trend_label, trend_row).arrange(DOWN, buff=0.12)
        trend_block.next_to(panel_group, DOWN, buff=0.4)
        self.play(FadeIn(trend_block), run_time=0.4)
        self.wait(0.5)

        looks_good = T("NOT THE SAME ORIGIN", color=PALETTE["sage"], font_size=17, font=MONO, weight="BOLD")
        looks_good.next_to(trend_block, DOWN, buff=0.22)
        self.play(FadeIn(looks_good), run_time=0.4)
        correct_tag = T("NOT THE SAME SCALE", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        correct_tag.next_to(looks_good, DOWN, buff=0.16)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.3)
        same_tag = fit(T("BUT NOTHING CHECKS.", color=PALETTE["sage"], font_size=17, font=MONO), MAX_W)
        same_tag.next_to(bottom_rule, DOWN, buff=0.25)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # GATE V real underfill MAJOR, found on the first true vertical
        # candidate (not a burn-in false positive): this overlay's original
        # sizing/spacing (qmark 110, buff=0.7) left too much real negative
        # space in the much taller 9:16 frame (48% of the safe area, min
        # 55%). Fixed with genuine added content mass -- a bigger qmark,
        # bigger text, wider rules closer to the safe edge, and more real
        # spacing between the real elements (never a padding rectangle).
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Two geometries.", color=PALETTE["bg"], font_size=40, weight="BOLD"), MAX_W)
        overlay_line2 = fit(T("Did anything notice?", color=PALETTE["bg"], font_size=36, weight="BOLD"), MAX_W)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule2 = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 1.8, RIGHT * 1.8, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        content_group = VGroup(title_block, panel_group, trend_block, looks_good, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        self.wait(17.57)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: single-column already; bodies re-wrapped narrower.
# measured audio: 29.23s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions,", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        title2 = fit(T("before any example:", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.7)

        def test_card(num, head, body_lines):
            badge = Square(side_length=0.42, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=19, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = fit(T(head, color=PALETTE["teal"], font_size=20, weight="BOLD"), MAX_W - 0.6)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.2)
            body_group = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=15), MAX_W) for l in body_lines
            ]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(head_row, body_group).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            body_group.align_to(head_row, LEFT)
            return row

        card1 = test_card(1, "Check the Checkpoint",
                           ["Is every vector from the", "exact same model/version?"])
        card2 = test_card(2, "Audit the Whole Index",
                           ["Was EVERY vector recomputed,", "or just the new ones?"])
        card3 = test_card(3, "Watch for Silence",
                           ["When geometries mix, does", "it error, or rank worse?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 0.6, height=cards.height + 0.6,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title_block, DOWN, buff=0.4)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.25)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)

        closing1 = fit(T("A split you can't see", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing2 = fit(T("is a split you can't fix.", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        self.play(Write(closing), run_time=0.5)
        self.wait(4.08)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: corpus panel narrowed, rows stacked.
# measured audio: 32.47s
# --------------------------------------------------------------------------- #
class B04_SilentSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title1 = fit(T("An index, under", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title2 = fit(T("a real upgrade.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title1, title2).arrange(DOWN, buff=0.08)
        title.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.next_to(title, UP, buff=0.18)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("MODEL A (OLD)", "820 DOCS", PALETTE["bg"], PALETTE["teal_on_ink"], font_size=17)
        history_row = stat_row("MODEL B (NEW)", "180 DOCS", PALETTE["bg"], PALETTE["sage"], font_size=17)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "1,000-DOC CORPUS", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        pressure_label = T("QUERY ARRIVES:", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        pressure_val = T("MODEL B", color=PALETTE["gold"], font_size=17, font=MONO, weight="BOLD")
        pressure_block = VGroup(pressure_label, pressure_val).arrange(DOWN, buff=0.1)
        pressure_block.next_to(panel_group, DOWN, buff=0.35)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.2)

        rank_label = T("OLD DOC'S RANK:", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        rank_val_before = T("#1", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        rank_row = VGroup(rank_label, rank_val_before).arrange(DOWN, buff=0.1)
        rank_row.next_to(pressure_block, DOWN, buff=0.4)
        self.play(FadeIn(rank_row), run_time=0.4)
        self.wait(1.4)

        rank_val_after = T("#47", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD")
        rank_val_after.move_to(rank_val_before.get_center())
        self.play(FadeOut(rank_val_before), FadeIn(rank_val_after), run_time=0.4)
        self.wait(1.3)

        gap_tag1 = T("SPLIT GEOMETRY", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        gap_tag2 = T("— SILENTLY", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        gap_tag = VGroup(gap_tag1, gap_tag2).arrange(DOWN, buff=0.08)
        gap_tag.next_to(rank_row, DOWN, buff=0.35)
        gap_box = box_around(gap_tag, buff=0.12, color=PALETTE["crimson"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.6)

        closing1 = fit(T("The answer still came back.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing2 = fit(T("Nobody saw the old doc fall.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        self.wait(20.77)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: same narrowed panel; re-embed/rank tags stacked.
# measured audio: 23.11s
# --------------------------------------------------------------------------- #
class B05_FullReembedHolds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title1 = fit(T("Same upgrade —", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title2 = fit(T("re-embedded first.", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title = VGroup(title1, title2).arrange(DOWN, buff=0.08)
        title.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["slate"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.6)

        fixed_row = stat_row("MODEL A (OLD)", "0 DOCS", PALETTE["ink"], PALETTE["teal"], font_size=17)
        history_row = stat_row("MODEL B (NEW)", "1,000 DOCS", PALETTE["ink"], PALETTE["slate"], font_size=17)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "1,000-DOC CORPUS", PALETTE["slate"], rows,
            fill=PALETTE["bg"], stroke=PALETTE["slate"])
        panel_group.next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.4)

        check_box = Rectangle(width=fixed_row.width + 0.25, height=fixed_row.height + 0.15,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        check_box.move_to(fixed_row.get_center())
        check_tag = fit(T("RE-EMBEDDED FIRST", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        check_tag.next_to(panel_group, DOWN, buff=0.25)
        self.play(Create(check_box), FadeIn(check_tag), run_time=0.4)
        self.wait(0.8)

        rank_label = T("OLD DOC'S RANK:", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD")
        rank_val = T("#1", color=PALETTE["slate"], font_size=20, font=MONO, weight="BOLD")
        rank_row = VGroup(rank_label, rank_val).arrange(DOWN, buff=0.1)
        rank_row.next_to(VGroup(panel_group, check_tag), DOWN, buff=0.4)
        self.play(FadeIn(rank_row), run_time=0.4)
        self.wait(0.9)

        rank_val_after = T("#1", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        rank_val_after.move_to(rank_val.get_center())
        self.play(FadeOut(rank_val), FadeIn(rank_val_after), run_time=0.4)
        self.wait(0.5)

        caught_tag1 = T("FULLY RE-EMBEDDED", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD")
        caught_tag2 = T("— NOTHING TO MIX", color=PALETTE["teal"], font_size=15, font=MONO, weight="BOLD")
        caught_tag = VGroup(caught_tag1, caught_tag2).arrange(DOWN, buff=0.08)
        caught_tag.next_to(rank_row, DOWN, buff=0.35)
        caught_box = box_around(caught_tag, buff=0.12, color=PALETTE["teal"])
        self.play(FadeIn(caught_tag), run_time=0.3)
        self.play(Create(caught_box), run_time=0.3)
        self.wait(1.3)

        closing1 = fit(T("Same upgrade — this time,", color=PALETTE["ink"], font_size=17, weight="BOLD"), MAX_W)
        closing2 = fit(T("one geometry held.", color=PALETTE["ink"], font_size=17, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["slate"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        self.wait(14.71)


# --------------------------------------------------------------------------- #
# B06 -- REAL-WORLD-NOTE: code-quote panel narrowed, one line per row.
# Verbatim source quotes unchanged from ../scenes.py (same characters).
# measured audio: 32.02s
# --------------------------------------------------------------------------- #
class B06_MycroftRealWorldNote(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title1 = fit(T("A real design choice", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title2 = fit(T("— not a bug.", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        title = VGroup(title1, title2).arrange(DOWN, buff=0.08)
        title.to_edge(UP, buff=0.7)
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.6)

        file_tag1 = fit(T("rag.py — mycroft /", color=PALETTE["slate"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        file_tag2 = fit(T("Regulatory_QA backend", color=PALETTE["slate"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        file_tag = VGroup(file_tag1, file_tag2).arrange(DOWN, buff=0.05)
        file_tag.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(file_tag), run_time=0.4)
        self.wait(0.6)

        def stmt_block(file_label, code_lines, code_color):
            # see ../scenes.py's matching comment: PALETTE["slate"] on ink is
            # broken contrast (caught by eye, not by GATE V); PALETTE["sage"]
            # is the house-documented safe substitute for note/tag text.
            # ONE real label Text per statement, never an empty Text("") for
            # a continuation line -- a real bug, found only by numerically
            # probing actual rendered coordinates (not visible from the
            # static layout-audit warning alone, and not obvious from a
            # single extracted frame either, since the visual symptom looked
            # like simple box overlap): an earlier version built each
            # continuation line as its own code_row("", code_text, ...),
            # i.e. a Text("") empty-string label paired with the code line.
            # Manim's Text("") has no points at all, so it never
            # participates in arrange()'s positioning the way a normal
            # mobject does, yet VGroup.height/.get_top()/.get_bottom() still
            # fold its degenerate (effectively origin-anchored) bounding box
            # into the group's overall extent -- silently inflating
            # box_around()'s computed box far beyond the statement's real,
            # visible text, enough to visually crowd into the NEXT
            # statement's own box. Fixed by building one label + N code
            # lines in a single VGroup, with no empty-string Text anywhere.
            lbl = T(file_label, color=PALETTE["sage"], font_size=12, font=MONO)
            code_mobs = [fit(T(line, color=code_color, font_size=15, font=MONO, weight="BOLD"), MAX_W - 0.4)
                         for line in code_lines]
            return VGroup(lbl, *code_mobs).arrange(DOWN, buff=0.06, aligned_edge=LEFT)

        stmt1 = stmt_block("rag.py", ["model_name=", "settings.embedding_model"], PALETTE["teal"])
        stmt2 = stmt_block("config.py", ['embedding_model: str =', '"all-MiniLM-L6-v2"'], PALETTE["teal"])
        row3 = stmt_block("rag.py", ["persist_directory=None"], PALETTE["crimson"])
        # Each statement is its own tightly-spaced VGroup (built above);
        # arrange the 3 STATEMENTS with a wide buff between them -- not one
        # flat arrange across every individual line (which would also space
        # a statement's own label apart from its code line by the same wide
        # gap meant to separate DIFFERENT statements).
        code_rows = VGroup(stmt1, stmt2, row3).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        code_panel = panel(width=code_rows.width + 0.4, height=code_rows.height + 0.35,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.12, opacity=1.0)
        code_panel.next_to(file_tag, DOWN, buff=0.3)
        code_rows.move_to(code_panel.get_center())

        self.play(Create(code_panel), run_time=0.4)
        self.play(FadeIn(stmt1, shift=UP * 0.06), run_time=0.5)
        row1_box = box_around(stmt1, buff=0.12, color=PALETTE["teal_on_ink"])
        self.play(Create(row1_box), run_time=0.3)
        # these two waits must match ../scenes.py's B06 beat-for-beat (1.7,
        # not 1.3) -- an earlier draft here used 1.3, a real 0.8s total
        # authoring drift from the landscape file that silently showed up
        # as this beat's raw rendered clip running 0.75s short of its
        # target duration (compile.py's retime-to-exact-duration step then
        # silently absorbed it via a ~2.4% speed-up, rather than erroring),
        # caught only by directly ffprobe-comparing every beat's raw manim
        # clip length between the two aspect folders after a real GATE V
        # duration mismatch (1 frame short) on the first true vertical
        # final. Fixed by restoring the correct, beat-matched value.
        self.wait(1.7)
        self.play(FadeIn(stmt2, shift=UP * 0.06), run_time=0.5)
        row2_box = box_around(stmt2, buff=0.12, color=PALETTE["teal_on_ink"])
        self.play(Create(row2_box), run_time=0.3)
        self.wait(1.7)
        self.play(FadeIn(row3, shift=UP * 0.06), run_time=0.5)
        row3_box = box_around(row3, buff=0.12, color=PALETTE["crimson"])
        self.play(Create(row3_box), run_time=0.3)
        self.wait(1.9)

        tag1 = fit(T("REBUILT FRESH, EVERY", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        tag1b = fit(T("SINGLE CHAT REQUEST", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        tag1_block = VGroup(tag1, tag1b).arrange(DOWN, buff=0.05)
        tag1_block.next_to(code_panel, DOWN, buff=0.3)
        self.play(FadeIn(tag1_block), run_time=0.4)
        self.wait(1.8)

        tag2 = fit(T("NO PERSISTED INDEX =", color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        tag2b = fit(T("NOTHING TO GO STALE", color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        tag2_block = VGroup(tag2, tag2b).arrange(DOWN, buff=0.05)
        tag2_block.next_to(tag1_block, DOWN, buff=0.22)
        self.play(FadeIn(tag2_block), run_time=0.4)
        self.wait(1.6)

        closing1 = fit(T("Trade-off: full re-embed", color=PALETTE["ink"], font_size=15), MAX_W)
        closing2 = fit(T("cost, on every request.", color=PALETTE["ink"], font_size=15), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.06)
        closing.to_edge(DOWN, buff=0.7)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(closing, shift=UP * 0.1), Create(bottom_rule), run_time=0.4)
        self.wait(17.22)


# --------------------------------------------------------------------------- #
# B07 -- SCAFFOLDED-TASK: single-column already; items re-wrapped narrower.
# measured audio: 24.22s
# --------------------------------------------------------------------------- #
class B07_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=26), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.6)

        def checklist_item(lines):
            box = Square(side_length=0.6, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            body = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W - 0.9) for l in lines
            ]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(box, body).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item(["Open any index behind", "search or retrieval."])
        row2, box2 = checklist_item(["Same embedding model", "and version, all of it?"])
        row3, box3 = checklist_item(["If not — full re-embed.", "Appending won't fix it."])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.5,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.4)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(0.7)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(5.4)
        self.play(Create(mark2), run_time=0.3)
        self.wait(5.4)
        self.play(Create(mark3), run_time=0.3)
        self.wait(5.4)

        closing1 = fit(T("No partial migration —", color=PALETTE["ink"], font_size=16), MAX_W)
        closing2 = fit(T("one geometry, or a silent problem.", color=PALETTE["ink"], font_size=16), MAX_W)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.1)
        closing_block.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        self.wait(3.92)


# --------------------------------------------------------------------------- #
# B08 -- TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 13.1s
# --------------------------------------------------------------------------- #
class B08_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # GATE V underfill note: a first fix round capped this beat's frame
        # width to clear the edge-bleed BLOCKER below, which (as a side
        # effect) dropped fill to 53% (just under the 55% floor). Recovered
        # with genuine added content mass -- larger real text and more real
        # spacing between the two real text blocks -- rather than widening
        # the frame back out (which would re-trigger the edge-bleed fix).
        line1 = fit(T("An embedding model's", color=PALETTE["bg"], font_size=27), MAX_W)
        line1b = fit(T("geometry isn't portable —", color=PALETTE["bg"], font_size=27), MAX_W)
        line1c = fit(T("the old vectors don't adapt.", color=PALETTE["bg"], font_size=27, weight="BOLD"), MAX_W)
        line2 = fit(T("The fix was never", color=PALETTE["gold"], font_size=30), MAX_W)
        line2b = fit(T("incremental. It's a full", color=PALETTE["gold"], font_size=30, weight="BOLD"), MAX_W)
        line2c = fit(T("re-embed, every time.", color=PALETTE["gold"], font_size=30, weight="BOLD"), MAX_W)

        block1 = VGroup(line1, line1b, line1c).arrange(DOWN, buff=0.3)
        block2 = VGroup(line2, line2b, line2c).arrange(DOWN, buff=0.32)
        content = VGroup(block1, block2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        # GATE V real edge-bleed BLOCKER, found on the first true vertical
        # candidate (not a burn-in false positive): content.width can reach
        # MAX_W (3.4), so an uncapped width=content.width+0.8 (4.2) exceeds
        # the portrait safe full-width (~3.9, half-width 1.95) -- the frame's
        # own border sat outside the title-safe area. Capped below, matching
        # the house pattern (B09's own frame_w cap) rather than guessed.
        frame_w = min(content.width + 0.8, 3.7)
        frame = panel(width=frame_w, height=content.height + 0.8,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(2.6)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.0)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(6.7)


# --------------------------------------------------------------------------- #
# B09 -- SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B09_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V real underfill MAJOR, found on the first true vertical
        # candidate (not a burn-in false positive): 47% of the safe area
        # (min 55%). Fixed with genuine added content mass -- bigger real
        # text and more real spacing between the real element groups (never
        # a padding rectangle), rather than just enlarging the frame around
        # unchanged content.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=60), MAX_W)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        fixed_line1 = fit(T("explained with", color=PALETTE["ink"], font_size=34), MAX_W)
        fixed_line2 = fit(T("Claude Code", color=PALETTE["ink"], font_size=34), MAX_W)
        fixed_block = VGroup(fixed_line1, fixed_line2).arrange(DOWN, buff=0.12)
        tagline1 = fit(T("in for", color=PALETTE["ink"], font_size=28), MAX_W)
        tagline2 = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=28), MAX_W)
        tagline_block = VGroup(tagline1, tagline2).arrange(DOWN, buff=0.12)
        content = VGroup(handle, accent, fixed_block, tagline_block).arrange(DOWN, buff=0.75).move_to(ORIGIN)

        frame_w = min(content.width + 0.6, 3.7)
        frame_h = min(content.height + 0.6, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.01)
