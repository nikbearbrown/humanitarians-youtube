"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-27-the-correction-that-never-reached-the-email

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
(B02's 2-tile row, B03's fields/code panel row, B05's 3-row-card row,
B06's 2-card row) is re-composed here as a single vertical chain / stacked
column instead — matching this fellow's sibling reels' own portrait-
redesign convention. Because frame_HEIGHT stays the same 8 units as the
parent but content that was side-by-side is now stacked, vertical space is
at a premium here in a way it wasn't in the parent — B05 in particular is
redesigned as one compact table-style panel (text rows, not 3 separate
bordered cards) rather than a literal stack of the parent's 3 cards, to fit
the same measured beat duration's worth of real content inside the
narrower, equally-tall safe area.

Beat-by-beat redesign notes:
  B00 TitleCard                 — unchanged 3-line title, narrowed.
  B01 ExecSummary                — badge stacked ABOVE name/role; summary
                                    re-wrapped across more/narrower lines.
  B02 IgnoredCorrectionHook      — parent's 2-tile horizontal row -> stacked
                                    column.
  B03 FieldWrittenFieldIgnored   — parent's fields-panel/code-panel row ->
                                    stacked column (fields on top, code
                                    below); code re-wrapped across narrower
                                    lines — same verbatim substrings.
  B04 EffectiveImpactDiff        — already a single column in the parent;
                                    narrowed, same real line breaks.
  B05 HarnessTable               — parent's 3 side-by-side row-cards ->
                                    ONE compact table-style panel (header +
                                    3 text rows + totals), not a literal
                                    vertical stack of 3 bordered cards, to
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

        title_lines = ["The Correction", "That Never", "Reached", "The Email"]
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
# measured audio: 17.14s
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
            "This video: a severity",
            "correction an LLM review",
            "step computes and writes",
            "down, that the email",
            "generator never actually",
            "reads — so the old,",
            "wrong label keeps",
            "shipping, every time.",
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
        self.wait(15.04)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's 2-tile horizontal row -> stacked column.
# measured audio: 19.54s
# --------------------------------------------------------------------------- #
class B02_IgnoredCorrectionHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our pipeline added a second opinion: an LLM that can correct a wrong label.",
                       color=PALETTE["bg"], font_size=20, line_spacing=1.3), 3.6)

        def tile(heading, value, color, val_fs=54):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=18, line_spacing=1.2), 3.1)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.35)
            bg = panel(width=3.4, height=content.height + 0.9, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_llm = tile("LLM correction writes:", "High", PALETTE["sage"])
        t_email = tile("Email still shows:", "Critical", PALETTE["crimson"], val_fs=48)
        tiles = VGroup(t_llm, t_email).arrange(DOWN, buff=0.5)
        t_email_box = box_around(t_email, buff=0.08, color=PALETTE["crimson"])

        zinger = fit(T("The correction never reached the email.", color=PALETTE["gold"],
                        font_size=26, weight="BOLD", line_spacing=1.2), 3.5)

        # GATE V found this beat's real content covering only 51% of the safe
        # area (min 55%, real underfill) — widened every internal buff above
        # and the top-level arrange below (0.45 -> 0.7) rather than padding
        # with an invisible spacer, per the canvas-fill requirement.
        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        t_email_box.move_to(t_email.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_llm, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_email, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_email_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        self.wait(15.94)


# --------------------------------------------------------------------------- #
# B03 — SETUP: parent's fields/code panel row -> stacked column.
# measured audio: 27.07s
# --------------------------------------------------------------------------- #
class B03_FieldWrittenFieldIgnored(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Four fields written.\nOne field read.",
                       color=PALETTE["ink"], font_size=24, line_spacing=1.2), 3.6)
        # buff 0.5 -> 0.68: this portrait frame's safe-area floor for any
        # 2-line title.to_edge(UP) — GATE B measured this exact title's real
        # top edge at y=3.5 against the +/-3.4 safe half-height at buff=0.5
        # (see BUILD-LOG.md/FRICTIONAL.md; same systemic finding documented
        # in this fellow's sibling reels' vertical builds).
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        fields_header = T("Layer 2 writes:", color=PALETTE["gold"], font_size=14,
                           font=MONO, weight="BOLD")
        field_values = [
            "llm_reviewed",
            "llm_verdict",
            "llm_corrected_",
            "  impact_level",
            "llm_downgrade",
        ]
        field_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=14, font=MONO) for v in field_values
        ]).arrange(DOWN, buff=0.13, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, field_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.4, height=fields_block.height + 0.35,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        code_header = T("Generate Email reads\n(pre-fix):", color=PALETTE["gold"],
                         font_size=14, font=MONO, weight="BOLD", line_spacing=1.2)
        line_a_str = "criticalItems ="
        line_a2_str = "  filter(i =>"
        line_a3_str = "  impact_level"
        line_a4_str = "  === 'Critical');"
        line_b_str = "highItems ="
        line_b2_str = "  filter(i =>"
        line_b3_str = "  impact_level"
        line_b4_str = "  === 'High');"
        code_lines = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=14, font=MONO)
            for s in (line_a_str, line_a2_str, line_a3_str, line_a4_str,
                      line_b_str, line_b2_str, line_b3_str, line_b4_str)
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.4, height=code_block.height + 0.35,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        panels = VGroup(fields_group, code_group).arrange(DOWN, buff=0.3)
        fit(panels, 3.7)
        # GATE B found the un-capped panel stack tall enough to push the
        # closing caption below it off the bottom safe edge AND overlap the
        # code panel's own last line (real measured defects, not false
        # positives) — cap the combined stack's height so there's always
        # room below it for the caption, same pattern as this fellow's
        # sibling reels' vertical B03 fix.
        # GATE V found the capped stack too small for this beat's own
        # canvas-fill floor (measured 50% of the safe area, min 55%) —
        # raised the cap from 3.5 to 4.3 (still leaves clear room below for
        # the caption via next_to(), confirmed by re-running GATE B/V).
        if panels.height > 4.3:
            panels.scale_to_fit_height(4.3)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(2.0)

        # "impact_level" is isolated on its own sub-line in this narrower
        # layout (line_a3_str / line_b3_str), so the whole sub-line is boxed
        # rather than a character-index slice of a longer line.
        hl_a = code_lines[2]
        hl_a.set_color(PALETTE["gold"])
        box_a = box_around(hl_a, buff=0.05, color=PALETTE["crimson"])
        box_a._qc_intentional = True

        hl_b = code_lines[6]
        hl_b.set_color(PALETTE["gold"])
        box_b = box_around(hl_b, buff=0.05, color=PALETTE["crimson"])
        box_b._qc_intentional = True

        self.play(Create(box_a), Create(box_b), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("Computed, written down,\nnever looked at again.",
                        color=PALETTE["crimson"], font_size=18, line_spacing=1.2), 3.6)
        # next_to(panels, ...), not to_edge(DOWN): guarantees no overlap with
        # the (now height-capped) panel stack regardless of its exact size,
        # rather than two independently-positioned blocks that can collide.
        caption.next_to(panels, DOWN, buff=0.35)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(19.07)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: already a single column in the parent; narrowed.
# measured audio: 19.82s
# --------------------------------------------------------------------------- #
class B04_EffectiveImpactDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One helper.\nThe whole fix.", color=PALETTE["ink"], font_size=26,
                       line_spacing=1.2), 3.6)
        title.to_edge(UP, buff=0.68)  # see B03's note: 0.68 is this file's safe floor
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- criticalItems = newItems.filter(i =>",
            "-   i.json.impact_level === 'Critical');",
            "- highItems = newItems.filter(i =>",
            "-   i.json.impact_level === 'High');",
        ]
        plus_strs = [
            "+ const effectiveImpact = (item) =>",
            "+   (item.json.llm_reviewed &&",
            "+   item.json.llm_corrected_impact_level)",
            "+   ? item.json.llm_corrected_impact_level",
            "+   : item.json.impact_level;",
            "+ criticalItems = newItems.filter(i =>",
            "+   effectiveImpact(i) === 'Critical');",
            "+ highItems = newItems.filter(i =>",
            "+   effectiveImpact(i) === 'High');",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=13, font=MONO, weight="BOLD") for s in minus_strs
        ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
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

        footnote = fit(T("(items the LLM never touched:\nunaffected, no regression)",
                          color=PALETTE["slate"], font_size=14, line_spacing=1.2), 3.6)
        footnote.next_to(diff_group, DOWN, buff=0.22)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strikes), run_time=0.4)
        self.wait(1.2)
        self.play(FadeIn(plus_lines, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.9)

        caption = fit(T("Untouched items behave\nexactly as before.",
                        color=PALETTE["slate"], font_size=17, line_spacing=1.2), 3.6)
        caption.to_edge(DOWN, buff=0.68)  # same safe-area floor as the UP edge
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        self.wait(12.42)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: ONE compact table-style panel (header + 3 rows +
# totals), not a literal stack of the parent's 3 bordered cards — chosen to
# fit this portrait frame's equally-tall-but-narrower safe area.
# measured audio: 29.42s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real code in a\nlive Node.js harness:",
                       color=PALETTE["ink"], font_size=19, line_spacing=1.2), 3.6)
        title.to_edge(UP, buff=0.68)  # safe-area floor, see B03 note
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def table_row(label, before, after, color, fs=14):
            l_txt = fit(T(label, color=PALETTE["bg"], font_size=fs, font=MONO, weight="BOLD"), 1.15)
            b_txt = fit(T(before, color=PALETTE["crimson"] if "bug" in before else PALETTE["bg"],
                          font_size=fs, font=MONO), 1.25)
            a_txt = fit(T(after, color=PALETTE["sage"] if "fixed" in after else PALETTE["bg"],
                          font_size=fs, font=MONO), 1.25)
            row = VGroup(l_txt, b_txt, a_txt).arrange(RIGHT, buff=0.12, aligned_edge=UP)
            return row, color

        header_row = VGroup(
            fit(T("item", color=PALETTE["slate"], font_size=13, font=MONO, weight="BOLD"), 1.15),
            fit(T("before", color=PALETTE["slate"], font_size=13, font=MONO, weight="BOLD"), 1.25),
            fit(T("after", color=PALETTE["slate"], font_size=13, font=MONO, weight="BOLD"), 1.25),
        ).arrange(RIGHT, buff=0.12)

        r1, c1 = table_row("1 (recat.)", "Critical\n(bug)", "High\n(fixed)", PALETTE["gold"])
        r2, c2 = table_row("2 (unchg.)", "High", "High", PALETTE["teal"])
        r3, c3 = table_row("3 (never)", "Critical", "Critical", PALETTE["teal"])

        rows = VGroup(header_row, r1, r2, r3).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        row1_box = box_around(r1, buff=0.07, color=PALETTE["gold"])
        row1_box.move_to(r1.get_center())

        table_panel = panel(width=rows.width + 0.4, height=rows.height + 0.4,
                             fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(table_panel.get_center())
        row1_box.move_to(r1.get_center())
        table_group = VGroup(table_panel, rows)
        table_group.next_to(title, DOWN, buff=0.35)
        row1_box.move_to(r1.get_center())

        self.play(FadeIn(header_row, shift=UP * 0.1), run_time=0.3)
        self.wait(0.6)
        self.play(Create(table_panel), run_time=0.3)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.4)
        self.play(Create(row1_box), run_time=0.3)
        self.wait(1.3)
        self.play(FadeIn(r2, shift=UP * 0.1), FadeIn(r3, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        totals = fit(T("critical: 2->1\nhigh: 1->2",
                       color=PALETTE["slate"], font_size=18, font=MONO, weight="BOLD",
                       line_spacing=1.2), 3.5)
        totals.next_to(table_group, DOWN, buff=0.3)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption1 = fit(T("Item 1: counted Critical\nbefore, High after.",
                         color=PALETTE["slate"], font_size=16, line_spacing=1.2), 3.6)
        caption1.next_to(totals, DOWN, buff=0.25)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.2)

        caption2 = fit(T("Items 2/3: unchanged —\nno regression.",
                         color=PALETTE["slate"], font_size=16, line_spacing=1.2), 3.6)
        caption2.next_to(caption1, DOWN, buff=0.18)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        self.wait(17.62)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-card side-by-side -> stacked column.
# measured audio: 29.83s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=28, weight="BOLD"), 3.5)
        title.to_edge(UP, buff=0.68)  # safe-area floor, see B03 note
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
            "1. Only this node's\nbucketing changed",
            ["Layer 2's own logic, the", "downgrade gate, and the", "two earlier fixes in this", "node are untouched."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. A separate defect\nfound, not fixed",
            ["Dashboard stats re-bucket", "by raw urgency score —", "disagrees with impact level", "on 57/411 real rows."],
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
        self.wait(21.93)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 11.18s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A correction",
            "that's computed",
            "but never read",
        ]
        line2 = [
            "isn't a correction.",
            "Every consumer of a",
            "label has to check",
            "whether it changed.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=28), 3.6) for l in lines
        ]).arrange(DOWN, buff=0.2)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["crimson"], font_size=24, weight="BOLD"), 3.6) for l in line2
        ]).arrange(DOWN, buff=0.2)

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
        self.wait(7.68)


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
        # GATE V found this beat's real content covering only 45% of the safe
        # area (min 55%) — enlarged the type and widened the top-level buff
        # (0.45 -> 0.85) rather than adding an invisible spacer.
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 0.6, 3.9)
        frame_h = min(content.height + 0.6, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(1.06)
