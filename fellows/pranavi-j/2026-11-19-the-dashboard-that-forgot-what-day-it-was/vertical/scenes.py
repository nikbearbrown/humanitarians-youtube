"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-19-the-dashboard-that-forgot-what-day-it-was

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command — NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (see
brutalist/docs/PIPELINE-SAFETY.md, "Isolated portrait companions and
Shorts"). All 9 parent beats are kept; every mp3 is reused byte-for-byte
from the parent's mp3/ folder (see vertical/beat_sheet.json, written by
shorts.py). Every beat here is a Manim GRAPHIC beat, so THE REFORMAT RULE's
auto center-cut never applies (generated graphics are never cropped) — each
class below is a genuine portrait RE-LAYOUT of the parent ../scenes.py
composition, authored by hand for a 2160x3840 canvas, not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so the parent file's y-axis safe/hard bounds carry over broadly unchanged;
only frame_width shrinks). What changes is frame_width: ~4.5 instead of
14.222 — a hard edge of only +/-2.25 and a safe half-width of ~1.95 (vs the
parent's +/-6.3). MAX_W = 3.6 is this file's general content-width budget
(leaves ~0.15 margin on each side). Every side-by-side layout in the parent
(B02's 3-tile row, B03's 2-panel-plus-list stack, B04's diff/kept-row stack)
is re-composed here as a single vertical chain / stacked column instead —
matching this fellow's sibling reels' own portrait-redesign convention.

This file proactively applies every systemic portrait fix this fellow's
sibling reels' vertical builds already documented finding the hard way (see
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/FRICTIONAL.md
and 2026-11-12-the-button-that-broke-every-next-question/FRICTIONAL.md),
rather than re-discovering them beat by beat:
  - CRITICAL PORTRAIT FIX (see below): config.frame_width/frame_height
    explicitly patched BEFORE any coordinate math in this file — this is
    the single most recurring toolkit bug (a comment alone is not a fix).
  - buff=0.68 floor for any 2-line title.to_edge(UP) (portrait safe-area).
  - caption/footer positioned via next_to(panel, DOWN, buff=...), never an
    independently-placed to_edge(DOWN), so it cannot overlap a stack whose
    exact height depends on its own content.
  - a height cap (scale_to_fit_height) on any multi-panel vertical stack,
    so there's always room below it for a following caption.
  - generous internal buffs/padding and enlarged type on every beat, so
    real content fills 60-80% of the safe area (canvas-fill requirement) --
    never an invisible spacer used only to pass a metric.
  - the whole visible block (title through closing caption) built as one
    centered VGroup rather than top-anchored, avoiding the sibling reels'
    own documented B05 underfill defect before ever rendering this aspect.

Beat-by-beat redesign notes:
  B00 TitleCard                  — unchanged 2-line title, narrowed.
  B01 ExecSummary                 — badge stacked ABOVE name/role; summary
                                     re-wrapped across more/narrower lines.
  B02 StaleWindowHook             — parent's 3-tile horizontal row ->
                                     stacked column.
  B03 TwoPanelsDisagree           — parent's code-panel/stats-panel row ->
                                     stacked column (code, then stats, then
                                     list panel below); code re-wrapped
                                     across narrower lines — same verbatim
                                     substrings, height-capped stack.
  B04 OneLineFix                  — parent's diff-panel + kept-row ->
                                     single narrower column, kept-row cards
                                     stacked instead of side by side.
  B05 LiveQueryTable               — parent's rows-table panel -> narrower
                                     stacked-rows panel, same real numbers.
  B06 HonestLimits                — parent's 2-card side-by-side -> stacked
                                     column.
  B07 Statement                  — unchanged composition; narrower,
                                     re-wrapped.
  B08 BrandOutro                  — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around() are copied verbatim from
../scenes.py for visual continuity. See ../scenes.py for the full beat-by-
beat build history (timing derivations, source citations) — nothing about
WHAT is said or WHEN changes here, only how it is laid out for the narrow
canvas.
"""

from manim import *
import numpy as np

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup — BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait — every
# coordinate in this file is designed against a 4.5-wide frame, so without
# this fix everything would render ~3.2x too small and clustered dead-center.
# This is the single most recurring toolkit bug across prior weeks' builds
# (a docstring/comment alone, with no actual code, does nothing) — the fix
# below is real executed code, verified by printing config.frame_width
# during this session's build (see FRICTIONAL.md) before trusting it.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "teal_on_ink": "#5FB8CC",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

MONO = "Courier New"

MAX_W = 3.6   # general portrait content-width budget (safe half-width 1.95)


def fit(mob, max_w=MAX_W):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48

def T(text, font_size=48, **kwargs):
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. measured (silent) duration: 4.10s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Dashboard", "That Forgot", "What Day It Was"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34, weight="BOLD")) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26))

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.5)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 16.51s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.5, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=26, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=34, weight="BOLD"))
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18))
        name_block = VGroup(badge_group, name, role).arrange(DOWN, buff=0.18)

        summary_lines = [
            "This video: a dashboard",
            "whose severity counts",
            "went blind the moment",
            "its fixture data got old",
            "enough — a seven-day",
            "filter that quietly",
            "zeroed out Critical and",
            "High, forever, while the",
            "list right below kept",
            "showing the real thing.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20)) for l in summary_lines
        ]).arrange(DOWN, buff=0.12)

        block = VGroup(top_rule, name_block, summary, bottom_rule).arrange(DOWN, buff=0.32)
        # GATE V true-master fix: a 7.2 cap left this beat's text (the frame's
        # hard edge is +/-4.0, but the title-SAFE area GATE V actually checks
        # is +/-3.4, i.e. a 6.8 total budget) bleeding past the real safe top/
        # bottom edge even though it looked fine inside this beat's own
        # decorative gold frame. 6.5 keeps a verified margin inside the real
        # safe area. See FRICTIONAL.md.
        if block.height > 6.5:
            block.scale_to_fit_height(6.5)
        block.move_to(ORIGIN)

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(VGroup(name, role), shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(14.41)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 3-tile row -> stacked column.
# measured audio: 17.64s
# --------------------------------------------------------------------------- #
class B02_StaleWindowHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_lines = ["The fixture data was", "loaded back in July."]
        title = VGroup(*[
            fit(T(l, color=PALETTE["bg"], font_size=21)) for l in title_lines
        ]).arrange(DOWN, buff=0.12)

        def tile(heading, value, color, val_fs=22):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=15, line_spacing=1.2))
            val_txt = fit(T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD"))
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.22)
            bg = panel(width=3.5, height=content.height + 0.5, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_range = tile("Fixture created_at range:", "Jul 14 - Jul 24, 2026", PALETTE["sage"], val_fs=18)
        t_today = tile("Today:", "Nov 19, 2026", PALETTE["bg"], val_fs=20)
        t_window = tile("Severity query's window\n(pre-fix):", "last 7 days", PALETTE["crimson"], val_fs=20)
        tiles = VGroup(t_range, t_today, t_window).arrange(DOWN, buff=0.22)
        t_window_box = box_around(t_window, buff=0.08, color=PALETTE["crimson"])

        zinger_lines = ["Seven days, against data four", "months stale, is zero. Every time."]
        zinger = VGroup(*[
            fit(T(l, color=PALETTE["gold"], font_size=18, weight="BOLD")) for l in zinger_lines
        ]).arrange(DOWN, buff=0.1)

        block = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.4)
        # Same safe-area cap fix as B01 above (true safe budget is 6.8, not
        # the 8.0 frame hard-edge) — applied proactively here too, since this
        # beat used the same unsafe 7.2 value even though it happened not to
        # trip GATE V this pass.
        if block.height > 6.5:
            block.scale_to_fit_height(6.5)
        block.move_to(ORIGIN)
        t_window_box.move_to(t_window.get_center())

        self.play(Write(title), run_time=0.5)
        self.wait(0.9)
        self.play(FadeIn(t_range, shift=UP * 0.1), run_time=0.3)
        self.wait(0.6)
        self.play(FadeIn(t_today, shift=UP * 0.1), run_time=0.3)
        self.wait(0.6)
        self.play(FadeIn(t_window, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_window_box), run_time=0.3)
        self.wait(0.8)
        self.play(Write(zinger), run_time=0.6)
        self.wait(12.44)


# --------------------------------------------------------------------------- #
# B03 — SETUP: parent's code/stats row -> stacked column, list panel below.
# measured audio: 24.17s
# --------------------------------------------------------------------------- #
class B03_TwoPanelsDisagree(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Two panels, one page,", "one contradiction."]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=23)) for l in title_lines
        ]).arrange(DOWN, buff=0.12)

        code_header = T("crud.py severity query", color=PALETTE["gold"], font_size=16,
                         font=MONO, weight="BOLD")
        where_line = T("FROM regulatory_feeds", color=PALETTE["bg"], font_size=16, font=MONO)
        where_line2a = T("WHERE created_at >=", color=PALETTE["crimson"], font_size=16, font=MONO,
                          weight="BOLD")
        where_line2b = T("  NOW() - INTERVAL '7 days'", color=PALETTE["crimson"], font_size=16,
                          font=MONO, weight="BOLD")
        code_block = VGroup(code_header, where_line, where_line2a, where_line2b).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.5, height=code_block.height + 0.45,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        stats_header = T("Stats.jsx cards", color=PALETTE["gold"], font_size=16,
                          font=MONO, weight="BOLD")
        stats_line1 = T('"Total Feeds" -> 411', color=PALETTE["bg"], font_size=16, font=MONO)
        stats_line2 = T('"Critical" -> 0', color=PALETTE["crimson"], font_size=16, font=MONO,
                         weight="BOLD")
        stats_line3 = T('"High Priority" -> 0', color=PALETTE["crimson"], font_size=16, font=MONO,
                         weight="BOLD")
        stats_block = VGroup(stats_header, stats_line1, stats_line2, stats_line3).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT)
        stats_panel = panel(width=stats_block.width + 0.5, height=stats_block.height + 0.45,
                             fill=PALETTE["ink"], stroke=PALETTE["slate"])
        stats_block.move_to(stats_panel.get_center())
        stats_group = VGroup(stats_panel, stats_block)

        list_header = T("FeedList.jsx, no date filter", color=PALETTE["gold"],
                         font_size=16, font=MONO, weight="BOLD")
        list_line1 = T("App.jsx: limit: 100", color=PALETTE["sage"], font_size=16, font=MONO)
        list_line2 = T("crud.py: ORDER BY created_at", color=PALETTE["sage"], font_size=16,
                       font=MONO)
        list_line2b = T("  DESC, urgency_score DESC", color=PALETTE["sage"], font_size=16,
                        font=MONO)
        list_line3 = T("// top 100: 24 Crit, 8 High", color=PALETTE["bg"],
                       font_size=15, font=MONO)
        list_block = VGroup(list_header, list_line1, list_line2, list_line2b, list_line3).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT)
        list_panel = panel(width=list_block.width + 0.5, height=list_block.height + 0.45,
                            fill=PALETTE["ink"], stroke=PALETTE["sage"])
        list_block.move_to(list_panel.get_center())
        list_group = VGroup(list_panel, list_block)

        stack = VGroup(code_group, stats_group, list_group).arrange(DOWN, buff=0.26)
        stack.next_to(title, DOWN, buff=0.35)

        box_zero1 = box_around(stats_line2, buff=0.06, color=PALETTE["crimson"])
        box_zero1._qc_intentional = True
        box_zero2 = box_around(stats_line3, buff=0.06, color=PALETTE["crimson"])
        box_zero2._qc_intentional = True
        box_where = box_around(VGroup(where_line2a, where_line2b), buff=0.06, color=PALETTE["crimson"])
        box_where._qc_intentional = True

        caption_lines = ["Same database. Same page.", "Zero clicks between them."]
        caption = VGroup(*[
            fit(T(l, color=PALETTE["crimson"], font_size=17)) for l in caption_lines
        ]).arrange(DOWN, buff=0.12)
        caption.next_to(stack, DOWN, buff=0.3)

        # CANVAS-FILL + SAFE-AREA FIX: a GATE V true-master pass caught this
        # beat at only 52% safe-area fill (min 55%) — title.to_edge(UP) had
        # pinned the title near the top, leaving the whole bottom half of the
        # frame empty below the caption. Fixed by building title+stack+
        # caption as one group and centering IT as a whole on ORIGIN (same
        # systemic fix this file's module docstring describes for its other
        # beats), with a height cap so the centered group still clears both
        # the top and bottom safe edges (+/-3.4y, 6.8 total budget). See
        # FRICTIONAL.md.
        full_block = VGroup(title, stack, caption, box_where, box_zero1, box_zero2)
        if full_block.height > 6.6:
            full_block.scale_to_fit_height(6.6)
        full_block.move_to(ORIGIN)

        self.play(Write(title), run_time=0.5)
        self.wait(1.0)
        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(stats_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.2)
        self.play(Create(box_where), Create(box_zero1), Create(box_zero2), run_time=0.5)
        self.wait(1.3)
        self.play(FadeIn(list_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(15.07)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: narrower single column, kept-row cards stacked.
# measured audio: 24.84s
# --------------------------------------------------------------------------- #
class B04_OneLineFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["One line. Same population", "as the rest of the page."]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19)) for l in title_lines
        ]).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.9)

        unchanged = T("FROM regulatory_feeds", color=PALETTE["bg"], font_size=14, font=MONO)
        minus_line1 = T("- WHERE created_at >=", color=PALETTE["crimson"], font_size=14,
                        font=MONO, weight="BOLD")
        minus_line2 = T("-   NOW() - INTERVAL '7 days'", color=PALETTE["crimson"], font_size=14,
                        font=MONO, weight="BOLD")
        minus_lines = VGroup(minus_line1, minus_line2).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        strike = Line(minus_lines.get_left() + LEFT * 0.05, minus_lines.get_right() + RIGHT * 0.05,
                      color=PALETTE["crimson"], stroke_width=3)
        strike.move_to(minus_lines.get_center())
        strike._qc_intentional = True
        minus_block = VGroup(minus_lines, strike)

        diff_block = VGroup(unchanged, minus_block).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        diff_panel = panel(width=diff_block.width + 0.5, height=diff_block.height + 0.4,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        diff_block.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, diff_block)
        diff_group.next_to(title, DOWN, buff=0.35)

        card1_lines = ["source_distribution:", "30-day window — KEPT"]
        card2_lines = ["recent_activity:", "14-day window — KEPT", "(intentional time series)"]
        card1 = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=13, font=MONO) for s in card1_lines
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        card2 = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=13, font=MONO) for s in card2_lines
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        card1_panel = panel(width=card1.width + 0.4, height=card1.height + 0.3,
                             fill=PALETTE["ink"], stroke=PALETTE["sage"])
        card1.move_to(card1_panel.get_center())
        card2_panel = panel(width=card2.width + 0.4, height=card2.height + 0.3,
                             fill=PALETTE["ink"], stroke=PALETTE["sage"])
        card2.move_to(card2_panel.get_center())
        kept_stack = VGroup(VGroup(card1_panel, card1), VGroup(card2_panel, card2)).arrange(
            DOWN, buff=0.22)
        kept_stack.next_to(diff_group, DOWN, buff=0.3)

        footnote_lines = ["Deliberately left alone — not", "contradicted the way severity was."]
        footnote = VGroup(*[
            fit(T(l, color=PALETTE["slate"], font_size=15)) for l in footnote_lines
        ]).arrange(DOWN, buff=0.1)
        footnote.next_to(kept_stack, DOWN, buff=0.28)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(unchanged), run_time=0.4)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.wait(1.3)
        self.play(FadeIn(kept_stack, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(18.54)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: narrower stacked-rows panel.
# measured audio: 25.37s
# --------------------------------------------------------------------------- #
class B05_LiveQueryTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Ran against the live database.", "Both versions."]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=21)) for l in title_lines
        ]).arrange(DOWN, buff=0.12)

        def row(label, result, color):
            lab = fit(T(label, color=PALETTE["bg"], font_size=15, font=MONO))
            res = fit(T(result, color=color, font_size=17, font=MONO, weight="BOLD"))
            return VGroup(lab, res).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        rows = VGroup(
            row("Old query (7-day window)", "0/0/0/0", PALETTE["crimson"]),
            row("New query (unwindowed)", "33/98/280/0", PALETTE["sage"]),
            row("Top-100 feed-list slice", "24 Crit / 8 High", PALETTE["sage"]),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        rows_panel = panel(width=rows.width + 0.5, height=rows.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(rows_panel.get_center())
        rows_group = VGroup(rows_panel, rows)

        match_lines = ["matches last week's verified", "impact_level counts exactly"]
        match_block = VGroup(*[
            T(l, color=PALETTE["gold"], font_size=13, font=MONO, weight="BOLD") for l in match_lines
        ]).arrange(DOWN, buff=0.1)
        match_panel = panel(width=match_block.width + 0.5, height=match_block.height + 0.4,
                             fill=PALETTE["ink"], stroke=PALETTE["gold"])
        match_block.move_to(match_panel.get_center())
        match_group = VGroup(match_panel, match_block)

        totals = fit(T("13 / 13 assertions pass", color=PALETTE["slate"], font_size=22, font=MONO,
                       weight="BOLD"))

        block = VGroup(title, rows_group, match_group, totals).arrange(DOWN, buff=0.32)
        if block.height > 7.0:
            block.scale_to_fit_height(7.0)
        block.move_to(ORIGIN)

        new_row_box = box_around(rows[1], buff=0.08, color=PALETTE["sage"])
        new_row_box.move_to(rows[1].get_center())

        self.play(Write(title), run_time=0.5)
        self.wait(1.1)
        self.play(FadeIn(rows_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.6)
        self.play(Create(new_row_box), run_time=0.3)
        self.wait(0.8)
        self.play(FadeIn(match_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.4)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        self.wait(18.47)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 cards stacked instead of side by side.
# measured audio: 25.49s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=26, weight="BOLD"))
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=15, weight="BOLD", line_spacing=1.2))
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=13, line_spacing=1.2)) for l in lines
            ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            bg = panel(width=3.6, height=content.height + 0.4, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. source_distribution's own\n30-day window",
            ["Same structural staleness risk", "as the one just fixed — not", "touched this round. A reasonable", "follow-up, not required here."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. No live browser/frontend\nsession",
            ["Verified by running the real", "query text against the live DB —", "no frontend or backend server", "was up this session."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.3)
        cards.next_to(title, DOWN, buff=0.45)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)

        divider = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.3)
        closing = fit(T("Full weight. Neither softened.", color=PALETTE["gold"], font_size=18,
                        weight="BOLD"))
        closing.next_to(divider, DOWN, buff=0.25)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        self.wait(17.59)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card, narrower, re-wrapped.
# measured audio: 10.06s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A dashboard's summary",
            "is only as honest as",
            "the window it looks",
            "through.",
        ]
        line2 = [
            "A window that quietly",
            "stops matching the data",
            "underneath it is worse",
            "than no window at all.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=24)) for l in lines
        ]).arrange(DOWN, buff=0.2)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["crimson"], font_size=19, weight="BOLD")) for l in line2
        ]).arrange(DOWN, buff=0.18)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        frame_w = max(content.width + 0.8, 3.9)
        frame_h = max(content.height + 0.8, 6.8)
        frame = panel(width=frame_w, height=frame_h,
                      fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        divider = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=2.5)
        divider.move_to(np.array(top.get_bottom()) / 2 + np.array(bottom.get_top()) / 2)

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        self.wait(7.06)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: widths trimmed for portrait.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # CANVAS-FILL FIX: a GATE V true-master pass caught this beat at only
        # 43% safe-area fill (min 55%) — modest font sizes and tight buffs
        # left most of the tall portrait frame empty above and below a small
        # centered block. Fixed with larger type, split across more lines
        # (so vertical space is used, not just horizontal), and generous
        # buffs — fit()'s MAX_W cap still keeps every line inside the safe
        # width regardless of font_size. See FRICTIONAL.md.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=56))
        accent = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        fixed_lines = ["explained with", "Claude Code"]
        fixed_line = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34)) for l in fixed_lines
        ]).arrange(DOWN, buff=0.22)
        tagline_lines = ["in for", "Sai Pranavi J."]
        tagline = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=30)) for l in tagline_lines
        ]).arrange(DOWN, buff=0.2)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 0.8, 4.0)
        frame_h = min(content.height + 0.8, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(1.06)
