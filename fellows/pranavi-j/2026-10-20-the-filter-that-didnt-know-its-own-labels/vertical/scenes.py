"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-20-the-filter-that-didnt-know-its-own-labels

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command — NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (see
brutalist/docs/PIPELINE-SAFETY.md, "Isolated portrait companions and
Shorts"). All 9 parent beats are kept; every mp3 is reused byte-for-byte
from the parent's mp3/ folder (see vertical/beat_sheet.json, written by
shorts.py). Every beat here is a Manim GRAPHIC beat, so THE REFORMAT RULE's
auto center-cut never applies (generated graphics are never cropped) — each
class below is a genuine portrait RE-LAYOUT of the parent ../scenes.py
composition, authored by hand for a 1080x1920 canvas (rendered at
2160x3840 for the true 4K vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so the parent file's y-axis safe/hard bounds carry over broadly unchanged;
only frame_width shrinks). What changes is frame_width: ~4.5 instead of
14.222 — a hard edge of only +/-2.25 and a safe half-width of ~1.95 (vs the
parent's +/-6.3). MAX_W = 3.6 is this file's general content-width budget
(leaves ~0.15 margin on each side). Every side-by-side layout in the parent
(B02's 2-tile row, B03's enum/code panel row, B05's 2-card row, B06's
2-card row) is re-composed here as a single vertical chain / stacked column
instead — matching this fellow's sibling reels' own portrait-redesign
convention.

Beat-by-beat redesign notes:
  B00 TitleCard          — unchanged 3-line title, narrowed.
  B01 ExecSummary        — badge stacked ABOVE name/role; summary re-wrapped.
  B02 SixthLabelHook     — parent's 2-tile horizontal row -> stacked column.
  B03 EnumVsClassifier   — parent's enum-panel/code-panel row -> stacked
                           column (enum on top, code below); code re-wrapped
                           across narrower lines — same verbatim substrings.
  B04 TwoLineDiff        — already a single column in the parent; narrowed,
                           diff lines re-wrapped across more lines.
  B05 TestClientTable    — parent's 2-card horizontal row -> stacked column.
  B06 HonestLimits       — parent's 2-card side-by-side -> stacked column.
  B07 Statement          — unchanged composition; narrower, re-wrapped.
  B08 BrandOutro         — unchanged composition; widths trimmed.

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


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Same 3-line title, narrowed.
# measured (silent) duration: 4.05s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Filter That", "Didn't Know", "Its Own Labels"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=42, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=3.9, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.05s silent track
        self.wait(2.45)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role.
# measured audio: 15.02s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: an API filter",
            "that rejected the exact",
            "labels our own classifier",
            "builds on the fly — a",
            "one-line type fix that",
            "closes a gap I flagged,",
            "but didn't fix, last week.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.18)

        # buff 0.4 -> 0.7: GATE V's real final-cut frame extraction measured
        # this beat's content bounding box at only 52% of the safe area (min
        # 55%) — genuine vertical underfill, not a false positive. More
        # inter-group spacing (plus the summary's own wider internal buff
        # above) closes the real gap without changing any text.
        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 15.02s Kokoro
        # length (15.02 - 1.8 = 13.22)
        self.wait(13.22)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 2-tile horizontal row -> stacked column.
# measured audio: 12.24s
# --------------------------------------------------------------------------- #
class B02_SixthLabelHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our source classifier\ndoesn't just pick from a\nshort list anymore.",
                       color=PALETTE["bg"], font_size=19, line_spacing=1.2), MAX_W)

        def tile(number, label, color, num_fs=46):
            num_txt = T(number, color=color, font_size=num_fs, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["bg"], font_size=15, line_spacing=1.15), 3.0)
            content = VGroup(num_txt, lab_txt).arrange(RIGHT, buff=0.3)
            bg = panel(width=3.5, height=content.height + 0.35, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_fixed = tile("5", "fixed labels\nin the enum", PALETTE["sage"])
        t_dynamic = tile("+1", "dynamic label,\nbuilt live", PALETTE["gold"], num_fs=50)
        tiles = VGroup(t_fixed, t_dynamic).arrange(DOWN, buff=0.3)
        t_dynamic_box = box_around(t_dynamic, buff=0.08, color=PALETTE["gold"])

        zinger = fit(T("Our filter endpoint\nnever got the memo.", color=PALETTE["gold"],
                        font_size=22, weight="BOLD", line_spacing=1.2), MAX_W)

        VGroup(title, tiles, zinger).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        t_dynamic_box.move_to(t_dynamic.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_fixed, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_dynamic, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_dynamic_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.4+0.3+0.3+0.3+0.5 = 1.8s
        # waits above = 0.8+0.5+0.5 = 1.8s; remainder tuned to the measured
        # 12.24s Kokoro length (12.24 - 1.8 - 1.8 = 8.64)
        self.wait(8.64)


# --------------------------------------------------------------------------- #
# B03 — SETUP: parent's enum-panel/code-panel row -> stacked column; code
# re-wrapped across narrower lines — same verbatim substrings.
# measured audio: 23.98s
# --------------------------------------------------------------------------- #
class B03_EnumVsClassifier(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Five fixed labels.\nOne classifier that\nbuilds a sixth.",
                       color=PALETTE["ink"], font_size=19, line_spacing=1.2), MAX_W)
        # buff 0.5 -> 0.68: GATE B's post-render layout audit found this
        # title's real top edge at y=3.5, just outside the +/-3.4 safe-area
        # half-height — a real overflow, not a false positive.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        enum_header = T("SourceFeed\n(models.py)", color=PALETTE["gold"], font_size=13,
                         font=MONO, weight="BOLD", line_spacing=1.2)
        enum_values = [
            '"SEC Press',
            ' Releases"',
            '"Federal Register',
            ' - Securities"',
            '"FINRA Enforcement',
            ' News"',
            '"CFTC Regulations"',
            '"Investment Advisor',
            ' Rules"',
        ]
        enum_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=12, font=MONO) for v in enum_values
        ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        enum_block = VGroup(enum_header, enum_lines).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        enum_panel = panel(width=enum_block.width + 0.35, height=enum_block.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        enum_block.move_to(enum_panel.get_center())
        enum_group = VGroup(enum_panel, enum_block)
        enum_group.next_to(title, DOWN, buff=0.3)

        code_header = T("identifySource()\n(workflow.dev.json)", color=PALETTE["gold"],
                         font_size=12, font=MONO, weight="BOLD", line_spacing=1.2)
        l1_str = "if (creator &&"
        l2_str = "  creator !== 'Unknown') {"
        l3_str = "  return `Federal"
        l4_str = "    Register -"
        l5_str = "    ${creator}`;"
        l6_str = "}"
        code_lines = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=14, font=MONO)
            for s in (l1_str, l2_str, l3_str, l4_str, l5_str, l6_str)
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.4, height=code_block.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)
        code_group.next_to(enum_group, DOWN, buff=0.3)

        # GATE B also found the closing caption crossing the code panel's own
        # stroked border (TEXT_ON_CURVE) and the whole stack running past the
        # bottom safe edge — real overlap from two tall panels plus a caption
        # in a frame only 6.8 tall net of safe margins. Cap the combined
        # enum+code stack so there's always real clearance below it.
        panels = VGroup(enum_group, code_group)
        if panels.height > 4.0:
            panels.scale_to_fit_height(4.0)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(enum_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(2.0)

        # Flag the exact real template literal, now split across l4/l5 by the
        # narrow re-wrap — box both lines together (still the same verbatim
        # substring, concatenated: "Federal Register - ${creator}`").
        highlight_group = VGroup(code_lines[3], code_lines[4])
        for ln in highlight_group:
            ln.set_color(PALETTE["gold"])
        flag_box = box_around(highlight_group, buff=0.06, color=PALETTE["crimson"])
        flag_box._qc_intentional = True

        self.play(Create(flag_box), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("That label was never in\nthe enum — and never could be.",
                        color=PALETTE["crimson"], font_size=16, line_spacing=1.2), MAX_W)
        # buff 0.55 -> 0.85: paired with the panels height cap above, gives
        # real clearance below the code panel's border (was flagged
        # TEXT_ON_CURVE against the panel's own stroke) and the safe-area
        # floor (was at y=-3.45).
        caption.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.5+0.4+0.4 = 2.5s
        # waits above = 1.0+1.0+2.0+1.5 = 5.5s; remainder tuned to
        # the measured 23.98s Kokoro length (23.98 - 2.5 - 5.5 = 15.98)
        self.wait(15.98)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: already a single column in the parent; narrowed, diff
# lines re-wrapped across more lines.
# measured audio: 22.13s
# --------------------------------------------------------------------------- #
class B04_TwoLineDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Two lines.\nThe whole fix.", color=PALETTE["ink"],
                       font_size=24, line_spacing=1.2), MAX_W)
        # buff 0.5 -> 0.68: same real GATE B safe-area fix as B03's title
        # (real top edge was at y=3.5, just past +/-3.4).
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def diff_pair(minus_lines, plus_lines, fs=13):
            minus_grp = VGroup(*[T(s, color=PALETTE["crimson"], font_size=fs, font=MONO, weight="BOLD")
                                  for s in minus_lines]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            plus_grp = VGroup(*[T(s, color=PALETTE["sage"], font_size=fs, font=MONO, weight="BOLD")
                                 for s in plus_lines]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            pair = VGroup(minus_grp, plus_grp).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            strike = Line(minus_grp.get_left() + LEFT * 0.04, minus_grp.get_right() + RIGHT * 0.04,
                          color=PALETTE["crimson"], stroke_width=2.5)
            strike.move_to(minus_grp.get_center())
            strike._qc_intentional = True
            return minus_grp, plus_grp, strike, pair

        m1, p1, s1, pair1 = diff_pair(
            ["- source_feed: Optional", "  [SourceFeed] = None,"],
            ["+ source_feed: Optional", "  [str] = None,"],
        )
        m2, p2, s2, pair2 = diff_pair(
            ["- source_feed=source_feed", "  .value if source_feed", "  else None,"],
            ["+ source_feed=source_feed,"],
            fs=12,
        )
        pairs = VGroup(pair1, pair2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fit(pairs, MAX_W - 0.5)
        diff_panel = panel(width=pairs.width + 0.4, height=pairs.height + 0.3,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.3)
        s1.move_to(m1.get_center())
        s2.move_to(m2.get_center())

        footnote = fit(T("(plus: the now-unused\nSourceFeed import, dropped)",
                          color=PALETTE["slate"], font_size=12, line_spacing=1.2), MAX_W)
        footnote.next_to(diff_group, DOWN, buff=0.25)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(m1), run_time=0.3)
        self.play(Create(s1), run_time=0.3)
        self.wait(0.7)
        self.play(FadeIn(p1, shift=UP * 0.1), run_time=0.4)
        self.wait(0.9)
        self.play(FadeIn(m2), run_time=0.3)
        self.play(Create(s2), run_time=0.3)
        self.wait(0.7)
        self.play(FadeIn(p2, shift=UP * 0.1), run_time=0.4)
        self.wait(0.9)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        caption = fit(T("The database column was\nalways just a string underneath.",
                        color=PALETTE["slate"], font_size=15, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.3+0.4+0.3+0.3+0.4+0.4+0.4 = 3.6s
        # waits above = 0.8+0.7+0.9+0.7+0.9+0.8 = 4.8s; remainder tuned to
        # the measured 22.13s Kokoro length (22.13 - 3.6 - 4.8 = 13.73)
        self.wait(13.73)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: parent's 2-card horizontal row -> stacked column.
# measured audio: 27.12s
# --------------------------------------------------------------------------- #
class B05_TestClientTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Mounted the real router\nbehind a FastAPI test client:",
                       color=PALETTE["ink"], font_size=16, line_spacing=1.2), MAX_W)
        # buff 0.5 -> 0.68: same systemic real GATE B safe-area fix applied
        # to every 2-line title.to_edge(UP) in this file (B03/B04) — a
        # two-line title at buff=0.5 consistently lands its real top edge at
        # y=3.5, just past the +/-3.4 safe half-height.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def row_card(scenario, before, after, color):
            s_txt = fit(T(scenario, color=PALETTE["bg"], font_size=15, font=MONO,
                           weight="BOLD", line_spacing=1.2), 3.3)
            before_txt = fit(T(before, color=PALETTE["crimson"] if "422" in before else PALETTE["bg"],
                                font_size=12, font=MONO, line_spacing=1.2), 3.3)
            after_txt = fit(T(after, color=PALETTE["sage"] if "200" in after else PALETTE["bg"],
                               font_size=12, font=MONO, line_spacing=1.2), 3.3)
            content = VGroup(s_txt, before_txt, after_txt).arrange(DOWN, buff=0.12)
            bg = panel(width=3.7, height=content.height + 0.3, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        r_dynamic = row_card(
            "dynamic label\n(Dept. of Labor)",
            "before: 422\nenum validation error\n(bug — rejected)",
            "after: 200\nCRUD got raw string\n(fixed)",
            PALETTE["gold"],
        )
        r_fixed = row_card(
            "fixed label\n(SEC Press Releases)",
            "before: 200\n(already worked)",
            "after: 200\n(unchanged)",
            PALETTE["teal"],
        )

        rows = VGroup(r_dynamic, r_fixed).arrange(DOWN, buff=0.22)
        if rows.height > 4.2:
            rows.scale_to_fit_height(4.2)
        rows.next_to(title, DOWN, buff=0.3)
        r_dynamic_box = box_around(r_dynamic, buff=0.06, color=PALETTE["gold"])

        self.play(FadeIn(r_dynamic, shift=UP * 0.1), run_time=0.4)
        self.play(Create(r_dynamic_box), run_time=0.3)
        self.wait(2.2)
        self.play(FadeIn(r_fixed, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        caption1 = fit(T("The dynamic-label row:\na real 422 before, a real 200 after.",
                         color=PALETTE["slate"], font_size=14, line_spacing=1.2), MAX_W)
        caption1.next_to(rows, DOWN, buff=0.22)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption2 = fit(T("The fixed-label row never\nchanged — no regression, either version.",
                         color=PALETTE["slate"], font_size=14, line_spacing=1.2), MAX_W)
        caption2.next_to(caption1, DOWN, buff=0.18)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.4+0.4+0.4 = 2.4s
        # waits above = 1.0+2.2+1.5+2.0 = 6.7s; remainder tuned to
        # the measured 27.12s Kokoro length (27.12 - 2.4 - 6.7 = 18.02)
        self.wait(18.02)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-card side-by-side -> stacked column.
# measured audio: 26.83s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        # buff 0.5 -> 0.68: turns out even this single-line, larger-font
        # title hits the same real safe-area overflow (top edge at y=3.5) as
        # the 2-line titles elsewhere in this file — same fix.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=15, weight="BOLD", line_spacing=1.2), 3.3)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=12, line_spacing=1.2), 3.3) for l in lines
            ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            bg = panel(width=3.7, height=content.height + 0.35, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. A latent gap, not\nan observed incident",
            ["The frontend doesn't", "currently send this", "parameter at all — nothing", "shows this 422 ever", "reached a real caller."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. The database layer\nwas mocked, not live",
            ["Confirms the API layer", "accepts and forwards the", "label — not a live query", "against rows that", "actually carry it."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.25)
        cards.next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.2)

        divider = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.22)
        closing = fit(T("Full weight.\nNeither one softened.", color=PALETTE["gold"],
                        font_size=18, weight="BOLD", line_spacing=1.2), MAX_W)
        closing.next_to(divider, DOWN, buff=0.2)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.5+0.5+0.3+0.4 = 2.2s
        # waits above = 1.3+2.2+2.2 = 5.7s; remainder tuned to the measured
        # 26.83s Kokoro length (26.83 - 2.2 - 5.7 = 18.93)
        self.wait(18.93)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 9.91s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "When a classifier is",
            "allowed to get smarter,",
        ]
        line2 = [
            "every consumer of its",
            "output has to keep up —",
            "including the one-line",
            "signature nobody revisits.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in lines
        ]).arrange(DOWN, buff=0.16)
        bottom = VGroup(*[
            # crimson, not gold — same real GATE V low-contrast fix as
            # ../scenes.py's B07 (gold directly on the cream page background,
            # not an ink panel, measured 0.29 separation against a 0.3 floor).
            fit(T(l, color=PALETTE["crimson"], font_size=19, weight="BOLD"), MAX_W) for l in line2
        ]).arrange(DOWN, buff=0.16)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        frame_w = max(content.width + 0.8, 3.9)
        frame_h = max(content.height + 0.7, 6.8)
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
        # tuned to the measured 9.91s Kokoro length (9.91 - 1.7 - 1.8 = 6.41)
        self.wait(6.41)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=38), 3.3)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=22), 3.3)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"],
                         font_size=20, line_spacing=1.25), 3.3)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        frame_w = content.width + 0.3
        frame_h = max(content.height + 1.0, 6.4)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
