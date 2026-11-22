"""
Manim scenes for 2026-11-19-the-dashboard-that-forgot-what-day-it-was
"The Dashboard That Forgot What Day It Was"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                 — spoken personal-intro card (EXEC-SUMMARY)
B02_StaleWindowHook             — fixture date range vs. today, vs. the
                                   7-day window: the arithmetic that
                                   guarantees zero rows (HOOK)
B03_TwoPanelsDisagree           — the real pre-fix WHERE clause, the real
                                   Stats.jsx labels, and the real unwindowed
                                   list_feeds/App.jsx limit:100 (SETUP)
B04_OneLineFix                  — the real one-line diff removing the
                                   WHERE clause; what was deliberately left
                                   alone (DISCOVERY-FIX)
B05_LiveQueryTable               — this session's real before/after live
                                   Postgres query results (VERIFICATION)
B06_HonestLimits                 — 2 honest-limit cards, full weight
                                   (HONEST-LIMITS)
B07_Statement                    — takeaway statement card (TAKEAWAY)
B08_BrandOutro                   — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest siblings,
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/scenes.py and
2026-11-12-the-button-that-broke-every-next-question/scenes.py, for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted code line (B02/B03's dates, pre-fix WHERE clause, Stats.jsx
labels; B04's diff) and every count/result (B05's live-query table) is
verbatim from the real source cited in SOURCES.md:
  - Regulatory_QA/backend/app/crud.py ("FeedCRUD.get_stats()", read-only,
    not modified by this build — the fix is already committed, a7e1628)
  - Regulatory_QA/frontend/src/components/Stats.jsx (card labels,
    read-only)
  - Regulatory_QA/frontend/src/App.jsx (feedsAPI.listFeeds limit, read-only)
  - scripts/regulatory-intel/F1-VERIFICATION.md (the diff, the verification
    table)
  - verification/verify_stale_stats_window_output.txt (this session's own
    live-DB harness run)
Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement
cards, which are intentionally shorter restatements of their own spoken
narration (same convention as every sibling reel).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.10 B01=16.51
B02=17.64 B03=24.17 B04=24.84 B05=25.37 B06=25.49 B07=10.06 B08=1.51. Every
self.play(run_time=...)/self.wait() value in each scene below was summed
against these measured durations before rendering (see BUILD-LOG.md /
FRICTIONAL.md). compile.py time-stretches the rendered clip a small amount
to match render_duration_s exactly (frame-ceil of the measured audio), so
exact-to-the-millisecond scene timing is not required, but close timing
keeps that stretch negligible.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric)
per this project's canvas-fill requirement (60-80% of the safe area), and
builds its whole visible block as one centered VGroup (title through
closing caption) rather than top-anchoring, per the sibling reels'
documented B05 underfill lesson — applied proactively here rather than
re-discovered.
"""

from manim import *
import numpy as np

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1) --
                          # use this, never "teal", for teal text/strokes on
                          # any ink-background scene or ink-filled panel.
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure
    "gold":   "#F3A712",  # fill only — never text color
    "sage":   "#A8C686",  # human / growth
}

MONO = "Courier New"


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See sibling reels' BUILD-LOG.md for the
    empirical proof."""
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.10s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Dashboard That", "Forgot What Day It Was"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=44, weight="BOLD"), 12.0) for l in title_lines
        ]).arrange(DOWN, buff=0.28)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=38)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.8).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.10s silent track
        self.wait(2.5)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 16.51s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 3.4, RIGHT * 3.4, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.55, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=30, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=42, weight="BOLD"), 9.0)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=22), 7.0)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_row = VGroup(badge_group, name_block).arrange(RIGHT, buff=0.4)

        summary_lines = [
            "This video: a dashboard whose severity",
            "counts went blind the moment its fixture",
            "data got old enough — a seven-day filter",
            "that quietly zeroed out Critical and High,",
            "forever, while the list right below kept",
            "showing the real thing.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=24), 11.4) for l in summary_lines
        ]).arrange(DOWN, buff=0.16)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 0.3+0.3+0.4+0.5+0.6 = 2.1s; remainder tuned to the
        # measured 16.51s Kokoro length (16.51 - 2.1 = 14.41)
        self.wait(14.41)


# --------------------------------------------------------------------------- #
# B02 — HOOK: fixture date range vs. today, vs. the 7-day window — the
# arithmetic that guarantees zero rows. [Source: F1-VERIFICATION.md;
# verification/verify_stale_stats_window_output.txt]
# measured audio: 17.64s
# --------------------------------------------------------------------------- #
class B02_StaleWindowHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("The fixture data was loaded back in July.",
                       color=PALETTE["bg"], font_size=26), 12.2)

        def tile(heading, value, color, val_fs=30):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=15, line_spacing=1.2), 3.7)
            val_txt = fit(T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD"), 3.7)
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.28)
            bg = panel(width=3.9, height=content.height + 0.9, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_range = tile("Fixture created_at\nrange:", "Jul 14 - Jul 24,\n2026", PALETTE["sage"], val_fs=21)
        t_today = tile("Today:", "Nov 19, 2026", PALETTE["bg"], val_fs=23)
        t_window = tile("Severity query's\nwindow (pre-fix):", "last 7 days", PALETTE["crimson"], val_fs=23)
        tiles = VGroup(t_range, t_today, t_window).arrange(RIGHT, buff=0.3)
        fit(tiles, 12.0)
        t_window_box = box_around(t_window, buff=0.1, color=PALETTE["crimson"])

        zinger = fit(T("Seven days, against data four months stale, is zero. Every time.",
                        color=PALETTE["gold"], font_size=27, weight="BOLD"), 12.0)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.8).move_to(ORIGIN)
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
        # sum of plays = 0.5+0.3+0.3+0.3+0.3+0.6 = 2.3s
        # waits above = 0.9+0.6+0.6+0.8 = 2.9s; remainder tuned to the
        # measured 17.64s Kokoro length (17.64 - 2.3 - 2.9 = 12.44)
        self.wait(12.44)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the real pre-fix WHERE clause, the real Stats.jsx labels, and
# the real unwindowed list_feeds/App.jsx limit:100.
# [Source: Regulatory_QA/backend/app/crud.py (pre-fix), Stats.jsx, App.jsx;
# F1-VERIFICATION.md]
# measured audio: 24.17s
# --------------------------------------------------------------------------- #
class B03_TwoPanelsDisagree(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Two panels, one page, one contradiction.",
                       color=PALETTE["ink"], font_size=29), 12.4)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # Top-left: the real pre-fix severity query WHERE clause.
        code_header = T("crud.py, get_stats() severity query (pre-fix):",
                         color=PALETTE["gold"], font_size=15, font=MONO, weight="BOLD")
        where_line = T("FROM regulatory_feeds", color=PALETTE["bg"], font_size=15, font=MONO)
        where_line2 = T("WHERE created_at >= NOW() - INTERVAL '7 days'",
                         color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD")
        code_block = VGroup(code_header, where_line, where_line2).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.6, height=code_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        # Top-right: the real Stats.jsx card labels, with the real values that
        # result from the pre-fix query.
        stats_header = T("Stats.jsx (dashboard cards):", color=PALETTE["gold"], font_size=15,
                          font=MONO, weight="BOLD")
        stats_line1 = T('"Total Feeds"  ->  411', color=PALETTE["bg"], font_size=15, font=MONO)
        stats_line2 = T('"Critical"     ->  0', color=PALETTE["crimson"], font_size=15, font=MONO,
                         weight="BOLD")
        stats_line3 = T('"High Priority"->  0', color=PALETTE["crimson"], font_size=15, font=MONO,
                         weight="BOLD")
        stats_block = VGroup(stats_header, stats_line1, stats_line2, stats_line3).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT)
        stats_panel = panel(width=stats_block.width + 0.6, height=stats_block.height + 0.5,
                             fill=PALETTE["ink"], stroke=PALETTE["slate"])
        stats_block.move_to(stats_panel.get_center())
        stats_group = VGroup(stats_panel, stats_block)

        top_row = VGroup(code_group, stats_group).arrange(RIGHT, buff=0.5)

        # Bottom: the real, unwindowed list_feeds/App.jsx fetch sitting right
        # below the stats cards, no date filter.
        list_header = T("FeedList.jsx, same page, no date filter:", color=PALETTE["gold"],
                         font_size=15, font=MONO, weight="BOLD")
        list_line1 = T("App.jsx: feedsAPI.listFeeds({ limit: 100 })",
                       color=PALETTE["sage"], font_size=15, font=MONO)
        list_line2 = T("crud.py: ORDER BY created_at DESC, urgency_score DESC",
                       color=PALETTE["sage"], font_size=15, font=MONO)
        list_line3 = T("// top 100 real rows: 24 Critical, 8 High", color=PALETTE["bg"],
                       font_size=14, font=MONO)
        list_block = VGroup(list_header, list_line1, list_line2, list_line3).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT)
        list_panel = panel(width=list_block.width + 0.6, height=list_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["sage"])
        list_block.move_to(list_panel.get_center())
        list_group = VGroup(list_panel, list_block)

        block = VGroup(top_row, list_group).arrange(DOWN, buff=0.4)
        block.next_to(title, DOWN, buff=0.4)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(stats_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.2)

        box_zero1 = box_around(stats_line2, buff=0.07, color=PALETTE["crimson"])
        box_zero1._qc_intentional = True
        box_zero2 = box_around(stats_line3, buff=0.07, color=PALETTE["crimson"])
        box_zero2._qc_intentional = True
        box_where = box_around(where_line2, buff=0.07, color=PALETTE["crimson"])
        box_where._qc_intentional = True
        self.play(Create(box_where), Create(box_zero1), Create(box_zero2), run_time=0.5)
        self.wait(1.3)

        self.play(FadeIn(list_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        caption = fit(T("Same database. Same page. Zero clicks between them.",
                        color=PALETTE["crimson"], font_size=21), 12.0)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.5+0.4+0.5+0.5+0.4 = 3.1s
        # waits above = 1.0+1.0+1.2+1.3+1.5 = 6.0s; remainder tuned to
        # the measured 24.17s Kokoro length (24.17 - 3.1 - 6.0 = 15.07)
        self.wait(15.07)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the real one-line diff removing the WHERE clause.
# [Source: F1-VERIFICATION.md, "The fix"]
# measured audio: 24.84s
# --------------------------------------------------------------------------- #
class B04_OneLineFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One line. Same population as the rest of the page.",
                       color=PALETTE["ink"], font_size=27), 12.4)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.9)

        diff_lines = [
            "                FROM regulatory_feeds",
        ]
        minus_str = "-                WHERE created_at >= NOW() - INTERVAL '7 days'"

        unchanged = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=22, font=MONO) for s in diff_lines
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        minus_line = T(minus_str, color=PALETTE["crimson"], font_size=22, font=MONO, weight="BOLD")
        strike = Line(minus_line.get_left() + LEFT * 0.05, minus_line.get_right() + RIGHT * 0.05,
                      color=PALETTE["crimson"], stroke_width=4)
        strike.move_to(minus_line.get_center())
        strike._qc_intentional = True  # deliberately crosses its own line's centerline
        minus_block = VGroup(minus_line, strike)
        # group minus text + its strike-through BEFORE the whole-block fit()
        # below, so scaling/repositioning carries both in lockstep (Line has
        # no settable .width, so a strike can't be recomputed after a scale —
        # it must already be nested inside the thing being scaled). Same
        # lesson this fellow's sibling reels' BUILD-LOG.md/FRICTIONAL.md
        # documented catching the hard way for their own diff beats — applied
        # proactively here instead of re-discovering it.

        diff_block = VGroup(unchanged, minus_block).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        # CANVAS-FILL FIX: a GATE V true-master pass caught this beat at only
        # 41% safe-area fill (min 55%) — the diff/kept-row content was
        # correctly centered but every panel was sized too narrow/modestly
        # relative to the 12.6-wide safe area. Fixed the same way B05's
        # sibling underfill was fixed: a minimum panel width floor (11.4,
        # not just content-width + padding) plus larger fonts throughout, not
        # an invisible spacer used only to pass the metric. See FRICTIONAL.md.
        diff_panel = panel(width=max(diff_block.width + 1.0, 11.4), height=diff_block.height + 0.8,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        diff_block.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, diff_block)
        diff_group.next_to(title, DOWN, buff=0.5)

        left_card_lines = [
            "source_distribution:",
            "30-day window — KEPT",
        ]
        right_card_lines = [
            "recent_activity:",
            "14-day window — KEPT",
            "(intentional time series)",
        ]
        left_card = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=19, font=MONO) for s in left_card_lines
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        right_card = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=19, font=MONO) for s in right_card_lines
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        left_panel = panel(width=max(left_card.width + 0.7, 5.4), height=left_card.height + 0.55,
                            fill=PALETTE["ink"], stroke=PALETTE["sage"])
        left_card.move_to(left_panel.get_center())
        right_panel = panel(width=max(right_card.width + 0.7, 5.4), height=right_card.height + 0.55,
                             fill=PALETTE["ink"], stroke=PALETTE["sage"])
        right_card.move_to(right_panel.get_center())
        kept_row = VGroup(VGroup(left_panel, left_card), VGroup(right_panel, right_card)).arrange(
            RIGHT, buff=0.5)
        kept_row.next_to(diff_group, DOWN, buff=0.45)

        footnote = fit(T("Deliberately left alone — not directly contradicted the way severity was.",
                          color=PALETTE["slate"], font_size=20), 12.2)
        footnote.next_to(kept_row, DOWN, buff=0.4)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(unchanged), run_time=0.4)
        self.play(FadeIn(minus_line), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.wait(1.3)
        self.play(FadeIn(kept_row, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.4+0.4+0.5+0.4 = 2.9s
        # waits above = 0.9+1.3+1.2 = 3.4s; remainder tuned to
        # the measured 24.84s Kokoro length (24.84 - 2.9 - 3.4 = 18.54)
        self.wait(18.54)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: this session's real before/after live Postgres query.
# [Source: verification/verify_stale_stats_window_output.txt]
# measured audio: 25.37s
# --------------------------------------------------------------------------- #
class B05_LiveQueryTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran against the live database. Both versions.",
                       color=PALETTE["ink"], font_size=29), 12.6)

        def row(label, result, color):
            lab = fit(T(label, color=PALETTE["bg"], font_size=20, font=MONO), 7.8)
            res = fit(T(result, color=color, font_size=22, font=MONO, weight="BOLD"), 4.2)
            line = VGroup(lab, res).arrange(RIGHT, buff=0.5)
            return line

        rows = VGroup(
            row("Old query (7-day window)", "0/0/0/0", PALETTE["crimson"]),
            row("New query (unwindowed)", "33/98/280/0", PALETTE["sage"]),
            row("Top-100 feed-list slice", "24 Crit / 8 High", PALETTE["sage"]),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        rows_panel = panel(width=max(rows.width + 0.9, 11.2), height=rows.height + 0.75,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(rows_panel.get_center())
        rows_group = VGroup(rows_panel, rows)

        match_line = T("matches last week's verified impact_level counts exactly",
                        color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD")
        match_panel = panel(width=max(match_line.width + 0.9, 11.0), height=match_line.height + 0.6,
                             fill=PALETTE["ink"], stroke=PALETTE["gold"])
        match_line.move_to(match_panel.get_center())
        match_group = VGroup(match_panel, match_line)

        totals = fit(T("13 / 13 assertions pass", color=PALETTE["slate"], font_size=32, font=MONO,
                       weight="BOLD"), 11.8)

        block = VGroup(title, rows_group, match_group, totals).arrange(DOWN, buff=0.4)
        if block.height > 6.6:
            block.scale_to_fit_height(6.6)
        block.move_to(ORIGIN)

        new_row_box = box_around(rows[1], buff=0.1, color=PALETTE["sage"])
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
        # sum of plays = 0.5+0.4+0.3+0.4+0.4 = 2.0s
        # waits above = 1.1+1.6+0.8+1.4 = 4.9s; remainder tuned to
        # the measured 25.37s Kokoro length (25.37 - 2.0 - 4.9 = 18.47)
        self.wait(18.47)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: F1-VERIFICATION.md "What's NOT touched"; RUN_LOG.md 2026-11-19
# "Open issues"]
# measured audio: 25.49s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=34, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=18, weight="BOLD", line_spacing=1.2), 5.6)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=16, line_spacing=1.2), 5.6) for l in lines
            ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            bg = panel(width=6.0, height=content.height + 0.6, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. source_distribution's\nown 30-day window",
            ["Same structural staleness risk", "as the one just fixed — not", "touched this round. A reasonable", "follow-up, not required here."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. No live browser/\nfrontend session",
            ["Verified by running the real", "query text against the live DB —", "no frontend or backend server", "was up this session."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(RIGHT, buff=0.5)
        cards.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)

        divider = Line(LEFT * 3.0, RIGHT * 3.0, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.35)
        closing = fit(T("Full weight. Neither one softened.", color=PALETTE["gold"], font_size=22, weight="BOLD"), 11.5)
        closing.next_to(divider, DOWN, buff=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.5+0.5+0.3+0.4 = 2.2s
        # waits above = 1.3+2.2+2.2 = 5.7s; remainder tuned to the measured
        # 25.49s Kokoro length (25.49 - 2.2 - 5.7 = 17.59)
        self.wait(17.59)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 10.06s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A dashboard's summary is",
            "only as honest as the",
            "window it looks through.",
        ]
        line2 = [
            "A window that quietly stops",
            "matching the data underneath",
            "it is worse than no window",
            "at all.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=32), 11.8) for l in lines
        ]).arrange(DOWN, buff=0.28)
        bottom = VGroup(*[
            # crimson, not gold: gold is this file's PALETTE fill-only color
            # and a direct gold-on-cream text line is a known low-contrast
            # defect in this fellow's sibling reels — crimson is already
            # proven legible as text on "bg" elsewhere in this file (B03/B04
            # captions).
            fit(T(l, color=PALETTE["crimson"], font_size=25, weight="BOLD"), 11.8) for l in line2
        ]).arrange(DOWN, buff=0.24)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.65).move_to(ORIGIN)
        frame_w = max(content.width + 1.4, 11.8)
        frame_h = max(content.height + 1.1, 6.2)
        frame = panel(width=frame_w, height=frame_h,
                      fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        divider = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=2.5)
        divider.move_to(np.array(top.get_bottom()) / 2 + np.array(bottom.get_top()) / 2)

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 1.3s; remainder
        # tuned to the measured 10.06s Kokoro length (10.06 - 1.7 - 1.3 = 7.06)
        self.wait(7.06)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Very short beat (1.51s measured) — narration is just
# "Explained with Claude Code."
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=86), 11.6)
        accent = Line(LEFT * 3.6, RIGHT * 3.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=46), 11.0)
        tagline = fit(T(
            "in for Sai Pranavi J.", color=PALETTE["ink"], font_size=40
        ), 11.0)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 1.8, 12.4)
        frame_h = min(content.height + 1.1, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
