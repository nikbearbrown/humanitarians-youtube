"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-15-the-alert-that-waited-for-a-second-item

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
(B02's 3-tile row, B04's fails/dead-end chain stays vertical already, B05's
3 table cards, B06's 2 honest-limit cards) is re-composed here as a single
vertical chain / stacked column instead — matching this fellow's sibling
reels' own portrait-redesign convention.

Beat-by-beat redesign notes:
  B00 TitleCard         — unchanged 3-line title, narrowed.
  B01 ExecSummary       — badge stacked ABOVE name/role; summary re-wrapped.
  B02 CounterHook       — parent's 3-tile horizontal row -> single stacked
                          column, same 3 persistent tiles + zinger.
  B03 BuggyLineOfCode   — the real hasData line re-wrapped across more
                          (narrower) lines — same verbatim substrings,
                          nothing reworded; same gold/crimson flag box.
  B04 DeadEndAndFix     — same vertical diff->fails->dead-end chain as the
                          parent (already a single column), narrowed.
  B05 BeforeAfterTable  — parent's 3-card horizontal row -> stacked column.
  B06 HonestLimits      — parent's 2-card side-by-side -> stacked column.
  B07 Statement         — unchanged composition; narrower, re-wrapped.
  B08 BrandOutro        — unchanged composition; widths trimmed.

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

        title_lines = ["The Alert That", "Waited for a", "Second Item"]
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
# measured audio: 15.94s
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
            "This video: a one-",
            "character bug in our",
            "regulatory pipeline",
            "meant a single urgent",
            "filing — the exact case",
            "our alert system exists",
            "for — could silently",
            "generate no alert at all.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.1)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 15.456s Kokoro
        # length (2026-10-20 name-retrofit: 15.456 - 1.8 = 13.656)
        self.wait(13.66)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 3-tile horizontal row -> a single stacked column (the
# narrow frame can't hold 3 side-by-side tiles); same 3 persistent tiles +
# zinger.
# measured audio: 12.5s
# --------------------------------------------------------------------------- #
class B02_CounterHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our alert only fires\nwhen there's something\nurgent.",
                       color=PALETTE["bg"], font_size=20, line_spacing=1.2), MAX_W)

        def tile(number, label, color, num_fs=46):
            num_txt = T(number, color=color, font_size=num_fs, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["bg"], font_size=15, line_spacing=1.15), 3.0)
            content = VGroup(num_txt, lab_txt).arrange(RIGHT, buff=0.3)
            bg = panel(width=3.5, height=content.height + 0.35, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t0 = tile("0", "no items\ncorrectly silent", PALETTE["sage"])
        t1 = tile("1", "one urgent item", PALETTE["gold"], num_fs=52)
        t2 = tile("2", "two items\nalready worked", PALETTE["teal_on_ink"])
        tiles = VGroup(t0, t1, t2).arrange(DOWN, buff=0.22)
        t1_box = box_around(t1, buff=0.08, color=PALETTE["gold"])

        zinger = fit(T("Not zero.\nNot two. One.", color=PALETTE["gold"],
                        font_size=24, weight="BOLD", line_spacing=1.2), MAX_W)

        VGroup(title, tiles, zinger).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        t1_box.move_to(t1.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t0, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t1, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t1_box), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.4+0.3+0.3+0.3+0.3+0.5 = 2.1s
        # waits above = 0.8+0.5+0.5+0.5 = 2.3s; remainder tuned to the
        # measured 12.5s Kokoro length (12.5 - 2.1 - 2.3 = 8.1)
        self.wait(8.1)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the real hasData guard line, re-wrapped across more (narrower)
# lines — same verbatim substrings, nothing reworded.
# measured audio: 16.54s
# --------------------------------------------------------------------------- #
class B03_BuggyLineOfCode(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("The real gate,\nstraight from the workflow:",
                       color=PALETTE["ink"], font_size=18, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        node_txt = T("Generate Email\nhasData guard", color=PALETTE["gold"], font_size=13,
                      font=MONO, weight="BOLD", line_spacing=1.2)
        node_pill = panel(width=node_txt.width + 0.35, height=node_txt.height + 0.25,
                           fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2)
        node_txt.move_to(node_pill.get_center())
        node_group = VGroup(node_pill, node_txt)
        node_group.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(node_group, shift=UP * 0.1), run_time=0.3)
        self.wait(0.8)

        # Same verbatim code, re-wrapped across more/narrower lines than the
        # landscape parent — concatenated, this is the exact same string.
        l1_str = "const hasData ="
        l2_str = "newItems &&"
        l3_str = "newItems.length > 1 &&"
        l4_str = "newItems[0].json &&"
        l5_str = "Object.keys(newItems[0]"
        l6_str = "  .json).length > 1;"

        l1 = T(l1_str, color=PALETTE["bg"], font_size=16, font=MONO)
        l2 = T(l2_str, color=PALETTE["bg"], font_size=16, font=MONO)
        l3 = T(l3_str, color=PALETTE["bg"], font_size=16, font=MONO)
        l4 = T(l4_str, color=PALETTE["bg"], font_size=16, font=MONO)
        l5 = T(l5_str, color=PALETTE["bg"], font_size=16, font=MONO)
        l6 = T(l6_str, color=PALETTE["bg"], font_size=16, font=MONO)
        code_lines = VGroup(l1, l2, l3, l4, l5, l6).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        code_panel = panel(width=code_lines.width + 0.5, height=code_lines.height + 0.4,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_lines.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_lines)
        code_group.next_to(node_group, DOWN, buff=0.35)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_lines), run_time=0.5)
        self.wait(2.0)

        # Flag the exact real substring "newItems.length > 1" — it is l3 in
        # its entirety here (the narrow re-wrap put it on its own line).
        needle = "newItems.length > 1"
        start = l3_str.index(needle)
        end = start + len(needle)
        highlight = l3[start:end]
        highlight.set_color(PALETTE["gold"])
        flag_box = box_around(highlight, buff=0.08, color=PALETTE["crimson"])
        # intentional annotation — see ../scenes.py's B03 for the full
        # explanation (box around a SUBSTRING of a larger Text mobject
        # necessarily crosses that mobject's own centerline).
        flag_box._qc_intentional = True

        self.play(Create(flag_box), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("Greater than —\nnot greater than or equal.",
                        color=PALETTE["crimson"], font_size=17, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.5+0.4+0.4 = 2.4s
        # waits above = 1.0+0.8+2.0+1.5 = 5.3s; remainder tuned to
        # the measured 16.54s Kokoro length (16.54 - 2.4 - 5.3 = 8.84)
        self.wait(8.84)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: same vertical diff -> fails -> dead-end chain as the
# parent (already a single column there), narrowed for portrait.
# measured audio: 16.49s
# --------------------------------------------------------------------------- #
class B04_DeadEndAndFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One character.\nThe whole bug.", color=PALETTE["ink"],
                       font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_line = T("- newItems.length > 1", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        plus_line = T("+ newItems.length > 0", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        diff_lines = VGroup(minus_line, plus_line).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fit(diff_lines, MAX_W - 0.6)
        strike = Line(minus_line.get_left() + LEFT * 0.04, minus_line.get_right() + RIGHT * 0.04,
                      color=PALETTE["crimson"], stroke_width=2.5)
        strike.move_to(minus_line.get_center())
        strike._qc_intentional = True

        diff_panel = panel(width=diff_lines.width + 0.5, height=diff_lines.height + 0.4,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        diff_lines.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, diff_lines)
        diff_group.next_to(title, DOWN, buff=0.3)
        strike.move_to(minus_line.get_center())

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_line), run_time=0.3)
        self.play(Create(strike), run_time=0.3)
        self.wait(1.0)
        self.play(FadeIn(plus_line, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)

        fails_box = panel(width=3.6, height=1.05, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        fails_txt = fit(T("fails the check ->\nhas_items: false", color=PALETTE["crimson"],
                           font_size=14, font=MONO, weight="BOLD", line_spacing=1.2), 3.3)
        fails_txt.move_to(fails_box.get_center())
        fails_group = VGroup(fails_box, fails_txt)

        deadend_box = panel(width=3.6, height=1.05, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        deadend_txt = fit(T("If-node TRUE: [ ]\nnowhere to go", color=PALETTE["crimson"],
                             font_size=14, font=MONO, weight="BOLD", line_spacing=1.2), 3.3)
        deadend_txt.move_to(deadend_box.get_center())
        deadend_group = VGroup(deadend_box, deadend_txt)

        lower_chain = VGroup(fails_group, deadend_group).arrange(DOWN, buff=0.35)
        lower_chain.next_to(diff_group, DOWN, buff=0.3)

        arrow1 = Arrow(diff_panel.get_bottom(), fails_box.get_top(), buff=0.05,
                       color=PALETTE["crimson"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        arrow2 = Arrow(fails_box.get_bottom(), deadend_box.get_top(), buff=0.05,
                       color=PALETTE["crimson"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        self.play(Create(arrow1), run_time=0.25)
        self.play(Create(fails_box), FadeIn(fails_txt), run_time=0.4)
        self.wait(0.8)
        self.play(Create(arrow2), run_time=0.25)
        self.play(Create(deadend_box), FadeIn(deadend_txt), run_time=0.4)
        # wait 1.5 -> 0.8: same real GATE V fix as ../scenes.py's B04 — the
        # closing caption needs to land before the 50% sample timestamp.
        self.wait(0.8)

        caption = fit(T("No error. No log line.\nJust an alert that never arrives.",
                        color=PALETTE["slate"], font_size=15, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.3+0.4+0.25+0.4+0.25+0.4+0.4 = 3.5s
        # waits above = 0.8+1.0+1.0+0.8+0.8 = 4.4s; remainder tuned to
        # the measured 16.49s Kokoro length (16.49 - 3.5 - 4.4 = 8.59)
        self.wait(8.59)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: parent's 3-card horizontal row -> stacked column.
# measured audio: 22.9s
# --------------------------------------------------------------------------- #
class B05_BeforeAfterTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real extracted code\n— not a rewritten copy:",
                       color=PALETTE["ink"], font_size=16, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def row_card(batch, before, after, color):
            b_txt = fit(T(batch, color=PALETTE["bg"], font_size=16, font=MONO, weight="BOLD"), 3.3)
            before_txt = fit(T(before, color=PALETTE["crimson"] if "bug" in before else PALETTE["bg"],
                                font_size=12, font=MONO, line_spacing=1.2), 3.3)
            after_txt = fit(T(after, color=PALETTE["sage"] if "fixed" in after else PALETTE["bg"],
                               font_size=12, font=MONO, line_spacing=1.2), 3.3)
            content = VGroup(b_txt, before_txt, after_txt).arrange(DOWN, buff=0.1)
            bg = panel(width=3.7, height=content.height + 0.3, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        r0 = row_card("0 items", "before: has_items: false\n(correct)",
                      "after: has_items: false\n(unchanged — correct)", PALETTE["sage"])
        r1 = row_card("1 item", "before: has_items: false\n(bug — email skipped)",
                      "after: has_items: true\n(fixed — email built)", PALETTE["gold"])
        r2 = row_card("2 items", "before: has_items: true\n(already worked)",
                      "after: has_items: true\n(unchanged)", PALETTE["teal"])

        rows = VGroup(r0, r1, r2).arrange(DOWN, buff=0.2)
        # cap 4.6 -> 4.3: GATE B's post-render layout audit found caption2's
        # real bottom edge at y=-3.46, just outside the +/-3.4 safe-area
        # half-height — the rows cap left no real room for the two
        # independently-chained captions below it. A tighter cap leaves
        # real clearance.
        if rows.height > 4.3:
            rows.scale_to_fit_height(4.3)
        rows.next_to(title, DOWN, buff=0.3)
        r1_box = box_around(r1, buff=0.06, color=PALETTE["gold"])

        self.play(FadeIn(r0, shift=UP * 0.1), run_time=0.35)
        self.wait(1.2)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.35)
        self.play(Create(r1_box), run_time=0.3)
        self.wait(2.0)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.35)
        self.wait(1.3)

        caption1 = fit(T("The 1-item row: silently skipped\nbefore, a real email after.",
                         color=PALETTE["slate"], font_size=14, line_spacing=1.2), MAX_W)
        caption1.next_to(rows, DOWN, buff=0.25)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption2 = fit(T("Re-run against the real patched\nfile on disk: same result.",
                         color=PALETTE["slate"], font_size=14, line_spacing=1.2), MAX_W)
        caption2.next_to(caption1, DOWN, buff=0.2)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.35+0.35+0.3+0.35+0.4+0.4 = 2.65s
        # waits above = 1.0+1.2+2.0+1.3+2.0 = 7.5s; remainder tuned to
        # the measured 22.9s Kokoro length (22.9 - 2.65 - 7.5 = 12.75)
        self.wait(12.75)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-card side-by-side -> stacked column.
# measured audio: 23.38s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=16, weight="BOLD", line_spacing=1.2), 3.3)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=13, line_spacing=1.2), 3.3) for l in lines
            ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            bg = panel(width=3.7, height=content.height + 0.4, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. Caught by code review,\nnot a live incident",
            ["No evidence this exact case", "ever occurred on a real run —", "not instrumented at that", "granularity."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. A related gap,\nflagged, not fixed",
            ["A downstream service's", "source list doesn't yet cover", "a newer classification —", "flagged, not resolved yet."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.25)
        cards.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        divider = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.25)
        closing = fit(T("Full weight.\nNeither one softened.", color=PALETTE["gold"],
                        font_size=18, weight="BOLD", line_spacing=1.2), MAX_W)
        closing.next_to(divider, DOWN, buff=0.22)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.5+0.5+0.3+0.4 = 2.2s
        # waits above = 1.3+2.0+2.0 = 5.3s; remainder tuned to the measured
        # 23.38s Kokoro length (23.38 - 2.2 - 5.3 = 15.88)
        self.wait(15.88)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 10.03s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "An alert system is only",
            "as good as the cases it",
            "was actually built to handle.",
        ]
        line2 = [
            "The scariest bugs aren't",
            "the ones that crash —",
            "they're the ones that quietly",
            "do nothing at all.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in lines
        ]).arrange(DOWN, buff=0.16)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["gold"], font_size=20, weight="BOLD"), MAX_W) for l in line2
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
        self.wait(2.0)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 2.0s; remainder
        # tuned to the measured 10.03s Kokoro length (10.03 - 1.7 - 2.0 = 6.33)
        self.wait(6.33)


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
