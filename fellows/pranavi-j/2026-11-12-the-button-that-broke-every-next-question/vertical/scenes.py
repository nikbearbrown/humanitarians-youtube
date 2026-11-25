"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-12-the-button-that-broke-every-next-question

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
(B02's 2-tile row, B03's 3-panel stack-of-panels row, B04's App/Chat diff
stack) is re-composed here as a single vertical chain / stacked column
instead — matching this fellow's sibling reels' own portrait-redesign
convention.

This file proactively applies every systemic portrait fix this fellow's
sibling reels' vertical builds already documented finding the hard way (see
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/FRICTIONAL.md
and BUILD-LOG.md), rather than re-discovering them beat by beat:
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
    centered VGroup rather than top-anchored, avoiding the sibling reel's
    own documented B05 underfill defect before ever rendering this aspect.

Beat-by-beat redesign notes:
  B00 TitleCard                  — unchanged 2-line title, narrowed.
  B01 ExecSummary                 — badge stacked ABOVE name/role; summary
                                     re-wrapped across more/narrower lines.
  B02 CapVsNoCapHook              — parent's 2-tile horizontal row ->
                                     stacked column.
  B03 TwoBugsOneClick             — parent's code-panel/fields-panel row ->
                                     stacked column (code, then backend
                                     limit, then error panel below); code
                                     re-wrapped across narrower lines — same
                                     verbatim substrings, height-capped stack.
  B04 CapAndRealReason            — already a single column in the parent;
                                     narrowed, same real line breaks.
  B05 HarnessTable                — parent's row-table panel -> ONE compact
                                     stacked-rows panel (not side by side),
                                     to fit this portrait frame's safe area.
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
# Copied verbatim from this fellow's sibling reels' vertical/scenes.py,
# which found and documented this exact bug.
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

        title_lines = ["The Button", "That Broke", "Every Next", "Question"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=40, weight="BOLD"), 3.5) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), 3.5)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=3.9, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.5)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 14.06s
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

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=34, weight="BOLD"), 3.4)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=19), 3.2)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.22)

        summary_lines = [
            "This video: a button",
            "called 'Select All,'",
            "sitting at the top of",
            "a feed list, that could",
            "silently break every",
            "question you asked",
            "after clicking it — and",
            "an error that never",
            "explained why.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), 3.5) for l in summary_lines
        ]).arrange(DOWN, buff=0.12)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        frame = panel(width=3.9, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 0.3+0.3+0.4+0.5+0.6 = 2.1s; remainder tuned to the
        # measured 14.06s Kokoro length (14.06 - 2.1 = 11.96)
        self.wait(11.96)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 2-tile horizontal row -> stacked column.
# measured audio: 15.34s
# --------------------------------------------------------------------------- #
class B02_CapVsNoCapHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("The chat backend caps context at ten feeds.",
                       color=PALETTE["bg"], font_size=19, line_spacing=1.3), 3.6)

        def tile(heading, value, color, val_fs=50):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=17, line_spacing=1.2), 3.1)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=3.4, height=content.height + 0.8, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_backend = tile("Backend hard limit\n(feed_ids, max_items):", "10", PALETTE["sage"])
        t_selectall = tile("Select All button\n(pre-fix):", "NO CAP", PALETTE["crimson"], val_fs=38)
        tiles = VGroup(t_backend, t_selectall).arrange(DOWN, buff=0.4)
        t_selectall_box = box_around(t_selectall, buff=0.08, color=PALETTE["crimson"])

        zinger = fit(T("The single most obvious button had no limit at all.",
                        color=PALETTE["gold"], font_size=22, weight="BOLD", line_spacing=1.2), 3.5)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        t_selectall_box.move_to(t_selectall.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_backend, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_selectall, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_selectall_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.4+0.3+0.3+0.3+0.5 = 1.8s
        # waits above = 0.8+0.5+0.5 = 1.8s; remainder tuned to the measured
        # 15.34s Kokoro length (15.34 - 1.8 - 1.8 = 11.74)
        self.wait(11.74)


# --------------------------------------------------------------------------- #
# B03 — SETUP: parent's code-panel/fields-panel/error-panel row -> stacked
# column, height-capped so the caption below always has room.
# measured audio: 28.73s
# --------------------------------------------------------------------------- #
class B03_TwoBugsOneClick(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Two bugs,\none click away.",
                       color=PALETTE["ink"], font_size=22, line_spacing=1.2), 3.6)
        title.to_edge(UP, buff=0.68)  # portrait safe-area floor for a 2-line title
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        code_header = T("App.jsx, handleSelectAll\n(pre-fix):", color=PALETTE["gold"],
                         font_size=13, font=MONO, weight="BOLD", line_spacing=1.2)
        select_all_str = "setSelected(new Set("
        select_all_str2 = "  feeds.map(f => f.id)));"
        code_lines = VGroup(
            T(select_all_str, color=PALETTE["bg"], font_size=13, font=MONO),
            T(select_all_str2, color=PALETTE["bg"], font_size=13, font=MONO,
              t2c={"feeds.map": PALETTE["crimson"]}),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.35, height=code_block.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        fields_header = T("backend/app/models.py:", color=PALETTE["gold"], font_size=13,
                           font=MONO, weight="BOLD")
        field_value1 = T("feed_ids: List[int] = Field(", color=PALETTE["sage"], font_size=13,
                          font=MONO)
        field_value2 = T("  min_items=1, max_items=10)", color=PALETTE["sage"], font_size=13,
                          font=MONO)
        fields_lines = VGroup(field_value1, field_value2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, fields_lines).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.35, height=fields_block.height + 0.3,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        error_header = T("ChatInterface.jsx,\ncatch (pre-fix):", color=PALETTE["gold"],
                          font_size=13, font=MONO, weight="BOLD", line_spacing=1.2)
        error_line = T("+ error.message,", color=PALETTE["crimson"], font_size=13, font=MONO,
                        weight="BOLD")
        error_result1 = T('// renders: "Request failed', color=PALETTE["bg"], font_size=12,
                           font=MONO)
        error_result2 = T('//  with status code 422"', color=PALETTE["bg"], font_size=12,
                           font=MONO)
        error_block = VGroup(error_header, error_line, error_result1, error_result2).arrange(
            DOWN, buff=0.15, aligned_edge=LEFT)
        error_panel = panel(width=error_block.width + 0.35, height=error_block.height + 0.3,
                             fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        error_block.move_to(error_panel.get_center())
        error_group = VGroup(error_panel, error_block)

        panels = VGroup(code_group, fields_group, error_group).arrange(DOWN, buff=0.22)
        # height-cap the combined stack so there's always room below it for
        # the caption (next_to, not independent to_edge(DOWN)) — same
        # systemic fix this fellow's sibling reel's vertical B03 documented.
        if panels.height > 5.2:
            panels.scale_to_fit_height(5.2)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        box_cap = box_around(field_value2, buff=0.06, color=PALETTE["sage"])
        box_cap._qc_intentional = True
        box_nocap = box_around(code_lines[1], buff=0.06, color=PALETTE["crimson"])
        box_nocap._qc_intentional = True
        self.play(Create(box_nocap), Create(box_cap), run_time=0.4)
        self.wait(1.0)

        self.play(FadeIn(error_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        caption = fit(T("The real reason was in the\nresponse. The code never read it.",
                        color=PALETTE["crimson"], font_size=16, line_spacing=1.2), 3.6)
        caption.next_to(panels, DOWN, buff=0.3)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.5+0.4+0.4+0.5+0.4 = 3.0s
        # waits above = 1.0+1.0+1.5+1.0+1.5 = 6.0s; remainder tuned to
        # the measured 28.73s Kokoro length (28.73 - 3.0 - 6.0 = 19.73)
        self.wait(19.73)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: already a single column in the parent; narrowed.
# measured audio: 18.38s
# --------------------------------------------------------------------------- #
class B04_CapAndRealReason(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Capped at ten.\nBoth paths.", color=PALETTE["ink"], font_size=26,
                       line_spacing=1.2), 3.6)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- setSelected(new Set(",
            "-  feeds.map(f => f.id)));",
        ]
        plus_strs = [
            "+ const MAX_SELECTABLE_",
            "+  FEEDS = 10;",
            "+ setSelected(new Set(",
            "+  feeds.slice(0, MAX_",
            "+  SELECTABLE_FEEDS)",
            "+  .map(f => f.id)));",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=12, font=MONO, weight="BOLD") for s in minus_strs
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        strikes = VGroup()
        for line in minus_lines:
            s = Line(line.get_left() + LEFT * 0.04, line.get_right() + RIGHT * 0.04,
                      color=PALETTE["crimson"], stroke_width=2.5)
            s.move_to(line.get_center())
            s._qc_intentional = True
            strikes.add(s)
        minus_block = VGroup(minus_lines, strikes)

        plus_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=12, font=MONO, weight="BOLD") for s in plus_strs
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        app_diff = VGroup(minus_block, plus_lines).arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        chat_header = T("ChatInterface.jsx —\nreal reason now:", color=PALETTE["gold"],
                         font_size=12, font=MONO, weight="BOLD", line_spacing=1.2)
        chat_plus_strs = [
            "+ const detail = error.",
            "+  response?.data?.detail;",
            "+ const reason =",
            "+  Array.isArray(detail)",
            "+  ? detail.map(d => d.msg",
            "+    || ...).join('; ') :",
            "+  detail || error.message;",
        ]
        chat_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=12, font=MONO, weight="BOLD") for s in chat_plus_strs
        ]).arrange(DOWN, buff=0.09, aligned_edge=LEFT)
        chat_block = VGroup(chat_header, chat_lines).arrange(DOWN, buff=0.18, aligned_edge=LEFT)

        pairs = VGroup(app_diff, chat_block).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fit(pairs, 3.5)
        # height-cap: the real ChatInterface.jsx reason block is longer once
        # quoted in full (7 narrow lines, not the earlier 4-line paraphrase)
        # — cap the combined panel's height so there's still guaranteed room
        # below it for the footnote AND the caption, same systemic pattern
        # this file's B03 already uses for its own 3-panel stack.
        if pairs.height > 3.95:
            pairs.scale_to_fit_height(3.95)

        diff_panel = panel(width=pairs.width + 0.3, height=pairs.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.2)

        footnote = fit(T("(handleToggle is capped\nthe same way)",
                          color=PALETTE["slate"], font_size=14, line_spacing=1.2), 3.6)
        footnote.next_to(diff_group, DOWN, buff=0.14)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strikes), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(plus_lines, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(chat_block, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        caption = fit(T("Not just the button — both\nselection paths, capped the same way.",
                        color=PALETTE["slate"], font_size=15, line_spacing=1.2), 3.6)
        # next_to(footnote, ...), not an independent to_edge(DOWN): guarantees
        # no overlap with the panel/footnote stack above regardless of its
        # exact height (same systemic fix as B03's caption in this file).
        caption.next_to(footnote, DOWN, buff=0.18)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.4+0.5+0.5+0.4+0.4 = 3.4s
        # waits above = 0.8+1.0+1.0+1.0+0.8 = 4.6s; remainder tuned to
        # the measured 18.38s Kokoro length (18.38 - 3.4 - 4.6 = 10.38)
        self.wait(10.38)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: ONE compact stacked-rows panel, not side-by-side
# tiles, to fit this portrait frame's narrower safe area.
# measured audio: 29.59s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Five checks.\nSeven assertions. All pass.",
                       color=PALETTE["ink"], font_size=24, line_spacing=1.2), 3.6)

        def row(label, result, color):
            lab = fit(T(label, color=PALETTE["bg"], font_size=16, font=MONO, line_spacing=1.2), 3.3)
            res = fit(T(result, color=color, font_size=17, font=MONO, weight="BOLD"), 3.3)
            return VGroup(lab, res).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        rows = VGroup(
            row("1. Select All, 411 feeds", "-> 10", PALETTE["sage"]),
            row("2. 15x handleToggle", "-> stops at 10", PALETTE["sage"]),
            row("3. untoggle, then add", "-> still 10", PALETTE["sage"]),
            row("4. no detail in response", "-> falls back", PALETTE["sage"]),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        rows_panel = panel(width=rows.width + 0.5, height=rows.height + 0.45,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(rows_panel.get_center())
        rows_group = VGroup(rows_panel, rows)

        old_msg = fit(T('OLD: "Request failed\nwith status code 422"',
                         color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD",
                         line_spacing=1.25), 3.4)
        new_msg = fit(T('NEW: "List should have at\nmost 10 items after\nvalidation, not 15"',
                         color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD",
                         line_spacing=1.25), 3.4)
        msg_block = VGroup(old_msg, new_msg).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        msg_panel = panel(width=msg_block.width + 0.5, height=msg_block.height + 0.45,
                           fill=PALETTE["ink"], stroke=PALETTE["gold"])
        msg_block.move_to(msg_panel.get_center())
        msg_group = VGroup(msg_panel, msg_block)

        totals = fit(T("7 / 7 assertions pass", color=PALETTE["slate"], font_size=26, font=MONO,
                       weight="BOLD", line_spacing=1.2), 3.5)

        block = VGroup(title, rows_group, msg_group, totals).arrange(DOWN, buff=0.26)
        # height-cap tightened to 6.6 (from an earlier 7.0): the landscape
        # sibling's identical enlarge-then-cap fix needed the same tighter
        # value to keep both edges inside +/-3.4 — applied here directly
        # rather than re-discovering it via a second GATE B round-trip.
        if block.height > 6.6:
            block.scale_to_fit_height(6.6)
        block.move_to(ORIGIN)

        new_msg_box = box_around(new_msg, buff=0.08, color=PALETTE["sage"])
        new_msg_box.move_to(new_msg.get_center())

        self.play(Write(title), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(rows_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)
        self.play(FadeIn(msg_group, shift=UP * 0.1), run_time=0.4)
        self.wait(0.5)
        self.play(Create(new_msg_box), run_time=0.3)
        self.wait(1.5)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.4+0.3+0.4 = 2.0s
        # waits above = 1.0+1.5+0.5+1.5 = 4.5s; remainder tuned to
        # the measured 29.59s Kokoro length (29.59 - 2.0 - 4.5 = 23.09)
        self.wait(23.09)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-card side-by-side -> stacked column.
# measured audio: 29.14s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=28, weight="BOLD"), 3.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=16, weight="BOLD", line_spacing=1.2), 3.3)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=14, line_spacing=1.2), 3.3) for l in lines
            ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            bg = panel(width=3.6, height=content.height + 0.35, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. No vite build,\nno browser check",
            ["node_modules isn't", "installed. Verified via a", "Node harness, plus the IDE's", "static diagnostics (0 new errors)."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. No UI cap\nindicator added",
            ["Selection silently stops", "growing past 10 — no disabled", "state, no tooltip. A reasonable", "follow-up, not required to ship."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.28)
        cards.next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)

        divider = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.25)
        closing = fit(T("Full weight.\nNeither one softened.", color=PALETTE["gold"], font_size=18,
                        weight="BOLD", line_spacing=1.2), 3.5)
        closing.next_to(divider, DOWN, buff=0.22)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.5+0.5+0.3+0.4 = 2.2s
        # waits above = 1.3+2.2+2.2 = 5.7s; remainder tuned to the measured
        # 29.14s Kokoro length (29.14 - 2.2 - 5.7 = 21.24)
        self.wait(21.24)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 13.49s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "The most obvious",
            "button needs to",
            "respect",
        ]
        line2 = [
            "the system's real limits.",
            "And when something",
            "fails, showing the real",
            "reason is what makes",
            "it fixable.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=27), 3.6) for l in lines
        ]).arrange(DOWN, buff=0.2)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["crimson"], font_size=21, weight="BOLD"), 3.6) for l in line2
        ]).arrange(DOWN, buff=0.16)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        frame_w = max(content.width + 0.6, 3.9)
        frame_h = max(content.height + 0.8, 7.0)
        frame = panel(width=frame_w, height=frame_h,
                      fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        divider = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=2.5)
        divider.move_to(np.array(top.get_bottom()) / 2 + np.array(bottom.get_top()) / 2)

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.wait(1.8)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 1.8s; remainder
        # tuned to the measured 13.49s Kokoro length (13.49 - 1.7 - 1.8 = 9.99)
        self.wait(9.99)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # enlarged from an earlier draft (44/32/27pt, buff=0.5): GATE V on the
        # true final master measured this beat's real bbox at 53% of the safe
        # area (min 55%) — a real, if small, underfill, not a false positive.
        # Bigger type + more generous spacing, same canvas-fill principle as
        # every other beat in this file.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=50), 3.8)
        accent = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with\nClaude Code", color=PALETTE["ink"], font_size=37,
                            line_spacing=1.3), 3.6)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=31), 3.6)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.65).move_to(ORIGIN)

        frame_w = min(content.width + 0.8, 3.95)
        frame_h = min(content.height + 0.7, 7.3)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
