"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts

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
(B02's 2-tile row, B03's 2-panel row, B05's 4-tile row, B06's 2-card row) is
re-composed here as a single vertical chain / stacked column instead —
matching this fellow's sibling reels' own portrait-redesign convention.

This file proactively applies every systemic portrait fix this fellow's
sibling reels' vertical builds already documented finding the hard way
(see 2026-10-27-the-correction-that-never-reached-the-email/FRICTIONAL.md
and BUILD-LOG.md), rather than re-discovering them beat by beat:
  - buff=0.68 floor for any 2-line title.to_edge(UP) (portrait safe-area).
  - caption/footer positioned via next_to(panel, DOWN, buff=...), never an
    independently-placed to_edge(DOWN), so it cannot overlap a stack whose
    exact height depends on its own content.
  - generous internal buffs/padding and enlarged type on every beat, so
    real content fills 60-80% of the safe area (canvas-fill requirement) --
    never an invisible spacer used only to pass a metric.

Beat-by-beat redesign notes:
  B00 TitleCard                 — unchanged 3-line title, narrowed.
  B01 ExecSummary                — badge stacked ABOVE name/role; summary
                                    re-wrapped across more/narrower lines.
  B02 DashboardVsEmailHook       — parent's 2-tile horizontal row -> stacked
                                    column.
  B03 OneQueryOneColumn          — parent's code-panel/fields-panel row ->
                                    stacked column (code on top, column-
                                    readers below); code re-wrapped across
                                    narrower lines — same verbatim substrings.
  B04 FourLineDiff                — already a single column in the parent;
                                    narrowed, same real line breaks.
  B05 HarnessTable               — parent's 4 side-by-side tier tiles ->
                                    ONE compact table-style panel (header +
                                    4 text rows + totals), not a literal
                                    vertical stack of 4 bordered tiles, to
                                    fit this portrait frame's safe area.
  B06 HonestLimits               — parent's 2-card side-by-side -> stacked
                                    column.
  B07 Statement                 — unchanged composition; narrower,
                                    re-wrapped.
  B08 BrandOutro                 — unchanged composition; widths trimmed.

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
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- avoid as TEXT on ink
    "slate":  "#29335C",  # structure -- avoid as TEXT on ink (low contrast)
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as TEXT on ink
    "sage":   "#A8C686",  # human / growth; safe secondary text color on ink
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

        title_lines = ["The Dashboard", "That Disagreed", "With Its Own", "Alerts"]
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
# measured audio: 14.28s
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
            "This video: a dashboard",
            "that counts severity",
            "one way, while the real",
            "alert email counts it a",
            "completely different",
            "way — and nobody had",
            "ever checked whether",
            "those numbers agreed.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=22), 3.5) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        frame = panel(width=3.9, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(12.18)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 2-tile horizontal row -> stacked column.
# measured audio: 17.95s
# --------------------------------------------------------------------------- #
class B02_DashboardVsEmailHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Every item gets a severity label everything downstream trusts.",
                       color=PALETTE["bg"], font_size=20, line_spacing=1.3), 3.6)

        def tile(heading, value, color, val_fs=54):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=18, line_spacing=1.2), 3.1)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.35)
            bg = panel(width=3.4, height=content.height + 0.9, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_email = tile("Email reads\nimpact_level:", "Medium", PALETTE["sage"])
        t_dash = tile("Dashboard counts it\nas (urgency_score):", "High", PALETTE["crimson"], val_fs=48)
        tiles = VGroup(t_email, t_dash).arrange(DOWN, buff=0.5)
        t_dash_box = box_around(t_dash, buff=0.08, color=PALETTE["crimson"])

        zinger = fit(T("The dashboard never reads the label the email reads.", color=PALETTE["gold"],
                        font_size=24, weight="BOLD", line_spacing=1.2), 3.5)

        # canvas-fill: widened internal buffs/padding proactively, per this
        # project's canvas-fill requirement. GATE B measured the resulting
        # block at buff=0.7 slightly overflowing BOTH the top safe edge
        # (title top at y=3.48 against +/-3.4) and the bottom safe edge
        # (zinger bottom at y=-3.48) once centered — a real, if small,
        # overflow, not a false positive. Tightened the top-level buff to
        # 0.55 (saves 0.3 of total block height across the 2 gaps) rather
        # than shrinking the tiles/type that canvas-fill needs to stay big.
        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        t_dash_box.move_to(t_dash.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_email, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_dash, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_dash_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        self.wait(14.35)


# --------------------------------------------------------------------------- #
# B03 — SETUP: parent's code-panel/fields-panel row -> stacked column.
# measured audio: 24.12s
# --------------------------------------------------------------------------- #
class B03_OneQueryOneColumn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One query re-derives\nits own answer.",
                       color=PALETTE["ink"], font_size=24, line_spacing=1.2), 3.6)
        # buff 0.5 -> 0.68: this portrait frame's safe-area floor for any
        # 2-line title.to_edge(UP) — documented systemic fix in this
        # fellow's sibling reels' vertical builds; applied here proactively.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        code_header = T("get_stats() read\n(pre-fix):", color=PALETTE["gold"], font_size=14,
                         font=MONO, weight="BOLD", line_spacing=1.2)
        line1_str = "urgency_score >= 8"
        line1b_str = "  -> critical"
        line2_str = "urgency_score 6-7"
        line2b_str = "  -> high"
        line3_str = "urgency_score 4-5"
        line3b_str = "  -> medium"
        line4_str = "urgency_score <= 3"
        line4b_str = "  -> low"
        code_lines = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=14, font=MONO)
            for s in (line1_str, line1b_str, line2_str, line2b_str,
                      line3_str, line3b_str, line4_str, line4b_str)
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.4, height=code_block.height + 0.35,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        fields_header = T("Everyone else reads:", color=PALETTE["gold"], font_size=14,
                           font=MONO, weight="BOLD")
        field_values = [
            "impact_level",
            "-> Generate Email",
            "-> feed list UI",
            "-> RAG chat context",
        ]
        field_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=14, font=MONO) for v in field_values
        ]).arrange(DOWN, buff=0.13, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, field_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.4, height=fields_block.height + 0.35,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        panels = VGroup(code_group, fields_group).arrange(DOWN, buff=0.3)
        # height-cap the combined stack so there's always room below it for
        # the caption (next_to, not independent to_edge(DOWN)) — same
        # systemic fix this fellow's sibling reels' vertical B03 documented;
        # 4.3 is the value that fix converged on after GATE V found 3.5 too
        # small for canvas-fill, applied here directly rather than
        # re-discovering it.
        if panels.height > 4.3:
            panels.scale_to_fit_height(4.3)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        hl_1 = code_lines[0]
        hl_1.set_color(PALETTE["crimson"])
        box_1 = box_around(hl_1, buff=0.05, color=PALETTE["crimson"])
        box_1._qc_intentional = True

        hl_2 = code_lines[2]
        hl_2.set_color(PALETTE["crimson"])
        box_2 = box_around(hl_2, buff=0.05, color=PALETTE["crimson"])
        box_2._qc_intentional = True

        column_line = field_lines[0]
        column_line.set_color(PALETTE["sage"])
        box_col = box_around(column_line, buff=0.05, color=PALETTE["sage"])
        box_col._qc_intentional = True

        self.play(Create(box_1), Create(box_2), run_time=0.3)
        self.play(Create(box_col), run_time=0.3)
        self.wait(1.5)

        caption = fit(T("Set together at first.\nThey can drift apart.",
                        color=PALETTE["crimson"], font_size=18, line_spacing=1.2), 3.6)
        # next_to(panels, ...), not to_edge(DOWN): guarantees no overlap with
        # the (now height-capped) panel stack regardless of its exact size.
        caption.next_to(panels, DOWN, buff=0.35)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(15.92)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: already a single column in the parent; narrowed.
# measured audio: 17.88s
# --------------------------------------------------------------------------- #
class B04_FourLineDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Four lines.\nThe whole fix.", color=PALETTE["ink"], font_size=26,
                       line_spacing=1.2), 3.6)
        title.to_edge(UP, buff=0.68)  # see B03's note: 0.68 is this file's safe floor
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- FILTER (WHERE",
            "-  urgency_score >= 8)",
            "-  as critical,",
            "- FILTER (WHERE urgency_",
            "-  score BETWEEN 6 AND 7)",
            "-  as high, ...",
        ]
        plus_strs = [
            "+ FILTER (WHERE impact_",
            "+  level = 'Critical')",
            "+  as critical,",
            "+ FILTER (WHERE impact_",
            "+  level = 'High')",
            "+  as high, ...",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=13, font=MONO, weight="BOLD") for s in minus_strs
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
            T(s, color=PALETTE["sage"], font_size=13, font=MONO, weight="BOLD") for s in plus_strs
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        pairs = VGroup(minus_block, plus_lines).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        fit(pairs, 3.5)

        diff_panel = panel(width=pairs.width + 0.3, height=pairs.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.3)

        footnote = fit(T("(same response shape —\nStats.jsx unchanged)",
                          color=PALETTE["slate"], font_size=14, line_spacing=1.2), 3.6)
        footnote.next_to(diff_group, DOWN, buff=0.22)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strikes), run_time=0.4)
        self.wait(1.1)
        self.play(FadeIn(plus_lines, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        caption = fit(T("Same windowing.\nJust a different column.",
                        color=PALETTE["slate"], font_size=17, line_spacing=1.2), 3.6)
        caption.to_edge(DOWN, buff=0.68)  # same safe-area floor as the UP edge
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(10.88)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: ONE compact table-style panel (header + 4 rows +
# totals), not a literal stack of the parent's 4 bordered tiles — chosen to
# fit this portrait frame's equally-tall-but-narrower safe area.
# measured audio: 24.55s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real query\nagainst the real data:",
                       color=PALETTE["ink"], font_size=21, line_spacing=1.2), 3.6)

        header_row = VGroup(
            fit(T("tier", color=PALETTE["slate"], font_size=16, font=MONO, weight="BOLD"), 1.25),
            fit(T("old", color=PALETTE["slate"], font_size=16, font=MONO, weight="BOLD"), 1.05),
            fit(T("new", color=PALETTE["slate"], font_size=16, font=MONO, weight="BOLD"), 1.05),
        ).arrange(RIGHT, buff=0.22)

        def table_row(tier, old, new, color):
            l_txt = fit(T(tier, color=PALETTE["bg"], font_size=16, font=MONO, weight="BOLD"), 1.25)
            o_txt = fit(T(str(old), color=PALETTE["bg"], font_size=16, font=MONO), 1.05)
            n_txt = fit(T(str(new), color=color, font_size=16, font=MONO, weight="BOLD"), 1.05)
            row = VGroup(l_txt, o_txt, n_txt).arrange(RIGHT, buff=0.22, aligned_edge=UP)
            return row

        r1 = table_row("Critical", 32, 33, PALETTE["teal_on_ink"])
        r2 = table_row("High", 139, 98, PALETTE["crimson"])
        r3 = table_row("Medium", 240, 280, PALETTE["gold"])
        r4 = table_row("Low", 0, 0, PALETTE["teal_on_ink"])

        rows = VGroup(header_row, r1, r2, r3, r4).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        table_panel = panel(width=rows.width + 0.5, height=rows.height + 0.5,
                             fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(table_panel.get_center())
        table_group = VGroup(table_panel, rows)

        totals = fit(T("62/411 rows (15%)\nland in a different tier",
                       color=PALETTE["slate"], font_size=18, font=MONO, weight="BOLD",
                       line_spacing=1.2), 3.5)

        caption1 = fit(T("High overcounted by 41\nitems — 30% inflated.",
                         color=PALETTE["crimson"], font_size=17, weight="BOLD", line_spacing=1.2), 3.6)

        caption2 = fit(T("Matches D1-VERIFICATION.md's\nlive-DB table exactly.",
                         color=PALETTE["slate"], font_size=17, line_spacing=1.2), 3.6)

        # canvas-fill: arrange the WHOLE block as one centered column with
        # generous buffs, rather than pinning the title to the top edge — same
        # fix the parent (landscape) scenes.py's B05 needed after GATE V
        # measured its top-anchored layout at only 50% of the safe area.
        # Applied here proactively rather than waiting for a second GATE V
        # round-trip on this aspect.
        block = VGroup(title, table_group, totals, caption1, caption2).arrange(DOWN, buff=0.4)
        block.move_to(ORIGIN)

        r2_box = box_around(r2, buff=0.07, color=PALETTE["crimson"])
        r2_box.move_to(r2.get_center())

        self.play(Write(title), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(header_row, shift=UP * 0.1), run_time=0.3)
        self.wait(0.3)
        self.play(Create(table_panel), run_time=0.3)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.3)
        self.play(Create(r2_box), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(r3, shift=UP * 0.1), FadeIn(r4, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        self.wait(16.65)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-card side-by-side -> stacked column.
# measured audio: 29.11s
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
            "1. Only this one\nquery changed",
            ["total_feeds, source_", "distribution, recent_activity,", "the route, and Stats.jsx", "are all untouched."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. Verified unwindowed,\nnot live",
            ["Checked against the full", "411-row table. Real 7/30-day", "windows weren't re-checked", "against live data — stale fixture."],
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
        self.wait(21.21)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 11.28s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A dashboard that",
            "re-derives its",
            "own answer",
        ]
        line2 = [
            "from a different number",
            "isn't measuring the",
            "same thing. Two",
            "consumers must read",
            "the same column.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=27), 3.6) for l in lines
        ]).arrange(DOWN, buff=0.2)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["crimson"], font_size=22, weight="BOLD"), 3.6) for l in line2
        ]).arrange(DOWN, buff=0.18)

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
        self.wait(7.78)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=44), 3.7)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with\nClaude Code", color=PALETTE["ink"], font_size=32,
                            line_spacing=1.3), 3.5)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=27), 3.5)
        # canvas-fill: enlarged type and widened the top-level buff
        # (0.45 -> 0.85) proactively, per this project's canvas-fill
        # requirement (sibling reels found 45% underfill at the smaller
        # defaults and fixed it exactly this way).
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 0.6, 3.9)
        frame_h = min(content.height + 0.6, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(1.06)
