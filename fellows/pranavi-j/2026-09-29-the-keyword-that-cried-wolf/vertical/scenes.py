"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-09-29-the-keyword-that-cried-wolf

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
(so the parent file's y-axis safe/hard bounds — to_edge(UP/DOWN, buff=...)
— carry over UNCHANGED; only frame_width shrinks). What changes is
frame_width: ~4.5 instead of 14.222 — a hard edge of only +/-2.25 and a
safe half-width of ~1.95 (vs the parent's +/-6.3). MAX_W = 3.6 is this
file's general content-width budget (leaves ~0.15 margin on each side).
Every side-by-side layout in the parent (B02's two misfire cards, B04's two
word-in-context panels) is re-composed here as a TOP/BOTTOM stack instead
of LEFT/RIGHT columns, and B05's 3-way fan-out / B06's 4-column table / B07's
3-across cards are restacked vertically — matching this fellow's RAG/B3
sibling reels' own portrait-redesign convention.

Beat-by-beat redesign notes:
  B00 TitleCard            — title re-wrapped 2->3 narrow lines.
  B01 ExecSummary          — badge stacked ABOVE name/role; summary re-wrapped.
  B02 TwoMisfiresHook      — parent's LEFT/RIGHT misfire cards -> TOP/BOTTOM stack.
  B03 ScoringRuleVerbatim  — already single-column; narrower code lines,
                             pills kept side-by-side (still fits MAX_W).
  B04 WordInContext        — THE big redesign: parent's LEFT/RIGHT panels ->
                             TOP/BOTTOM stack, both simultaneously visible.
  B05 FailOpenFlowDiagram  — parent's 3-way horizontal fan-out -> a single
                             vertical chain: item -> review -> confirm ->
                             downgrade -> fail-open, each its own stacked card.
  B06 ThreeCaseResultsTable— parent's 4-column table -> 3 stacked case cards,
                             each showing the same 4 fields as short lines.
  B07 HonestLimitsCards    — parent's 3-across row -> 3 stacked cards.
  B08 BrandOutro           — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around()/inline_highlight() are copied
verbatim from ../scenes.py for visual continuity, including the
"sage-not-slate on ink" and "gold-not-crimson for dense stamp/closing text"
contrast fixes already verified on the landscape master — ported here so
the portrait cut never reintroduces either bug. See ../scenes.py for the
full beat-by-beat build history (timing derivations, GATE V findings) —
nothing about WHAT is said or WHEN changes here, only how it is laid out
for the narrow canvas.
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
# Copied verbatim from this fellow's RAG/B3 sibling reels' vertical/scenes.py,
# which found and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- only 0.28 luminance sep on
                          # ink (verified via GATE V on the landscape master);
                          # avoid as TEXT color on ink, fine as a stroke/accent.
    "slate":  "#29335C",  # structure -- 0.04 luminance sep on ink (broken,
                          # same class of bug as "teal on ink"); use "sage"
                          # for any note/tag text on an ink background.
    "gold":   "#F3A712",  # fill/stroke/accent; also used as TEXT on ink
                          # where crimson measured too low (0.51 sep, safe).
    "sage":   "#A8C686",  # human / growth; safe secondary text color on ink
                          # (0.57 sep).
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


def inline_highlight(before, word, after, font_size, base_color, hl_color, font=None):
    """See ../scenes.py's docstring: returns (row, hl); build the tracking
    box via box_around(hl, ...) only AFTER all layout is finished."""
    parts = []
    if before:
        parts.append(T(before + " ", font_size=font_size, color=base_color, font=font))
    hl = T(word, font_size=font_size, color=hl_color, weight="BOLD", font=font)
    parts.append(hl)
    if after:
        parts.append(T(" " + after, font_size=font_size, color=base_color, font=font))
    row = VGroup(*parts).arrange(RIGHT, buff=0.1)
    return row, hl


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Title re-wrapped 2 -> 3 narrow lines.
# measured (silent) duration: 4.049s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Keyword", "That Cried", "Wolf"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=46, weight="BOLD"), MAX_W)
            for l in title_lines
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
        # sum of plays = 1.6s; remainder tuned to the measured 4.049s silent track
        self.wait(2.45)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role (parent's side-by-side
# row would starve the name of width next to a badge in this narrow frame).
# measured audio: 14.904s
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
            "This video: a keyword",
            "scorer that was crying",
            "wolf — marking routine",
            "filings as Critical",
            "because of one word in",
            "the title — and a",
            "second-opinion pass,",
            "running locally, that",
            "catches it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.1)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 14.256s Kokoro
        # length (2026-10-20 name-retrofit: 14.256 - 1.8 = 12.456)
        self.wait(12.46)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's LEFT/RIGHT misfire cards -> TOP/BOTTOM stack.
# measured audio: 13.56s
# --------------------------------------------------------------------------- #
class B02_TwoMisfiresHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two items.\nBoth flagged Critical.", color=PALETTE["bg"],
                          font_size=24, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)

        # ---- TOP: Medicare rule ----
        top_panel = panel(width=3.6, height=2.3, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        top_header = fit(T("MEDICARE PROGRAM RULE", color=PALETTE["sage"], font_size=14, font=MONO), 3.2)
        top_body = fit(T("Hospital Outpatient\nProspective Payment...",
                             color=PALETTE["bg"], font_size=13, line_spacing=1.2), 3.2)
        top_note = fit(T("routine payment rule", color=PALETTE["sage"], font_size=13), 3.2)
        top_stamp = fit(T("10/CRITICAL", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD"), 3.2)
        top_content = VGroup(top_header, top_body, top_note, top_stamp).arrange(DOWN, buff=0.15)

        # ---- BOTTOM: Nasdaq filing ----
        bot_panel = panel(width=3.6, height=2.3, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        bot_header = fit(T("NASDAQ SRO FILING", color=PALETTE["sage"], font_size=14, font=MONO), 3.2)
        bot_body = fit(T("Notice of Filing and\nImmediate Effectiveness",
                             color=PALETTE["bg"], font_size=13, line_spacing=1.2), 3.2)
        bot_note = fit(T("boilerplate cabinet-\nwiring filing", color=PALETTE["sage"],
                             font_size=12, line_spacing=1.15), 3.2)
        bot_stamp = fit(T("9/CRITICAL", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD"), 3.2)
        bot_content = VGroup(bot_header, bot_body, bot_note, bot_stamp).arrange(DOWN, buff=0.15)

        # content centered within its own panel FIRST (so each (panel,
        # content) pair is a correctly laid-out rigid unit before grouping)
        top_content.move_to(top_panel.get_center())
        bot_content.move_to(bot_panel.get_center())

        # the previous draft chained top_panel.next_to(title, ...) then
        # bot_panel.next_to(top_panel, ...) — a static pre-flight run found
        # this chain's real stacked height pushed bot_panel's center well
        # past y=-4 (off the bottom of even the HARD frame, not just the
        # safe area). Capping the two-panel group's total height via
        # scale_to_fit_height (the same pattern already proven clean in
        # this file's B06/B07) guarantees it fits regardless of any single
        # panel's assumed height, while scaling/moving the GROUP (not each
        # piece separately) preserves each panel's own content centering.
        top_group = VGroup(top_panel, top_content)
        bot_group = VGroup(bot_panel, bot_content)
        panels = VGroup(top_group, bot_group).arrange(DOWN, buff=0.3)
        if panels.height > 5.4:
            panels.scale_to_fit_height(5.4)
        panels.next_to(title, DOWN, buff=0.3)

        self.play(Create(top_panel), Create(bot_panel), run_time=0.5)
        self.play(FadeIn(top_content, shift=UP * 0.1), run_time=0.5)
        self.wait(3.9)
        self.play(FadeIn(bot_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        top_stamp_box = box_around(top_stamp, buff=0.1, color=PALETTE["gold"])
        bot_stamp_box = box_around(bot_stamp, buff=0.1, color=PALETTE["gold"])
        self.play(Create(top_stamp_box), Create(bot_stamp_box), run_time=0.3)

        zinger = fit(T("Neither one was\nactually urgent.", color=PALETTE["gold"],
                           font_size=18, line_spacing=1.2), MAX_W)
        zinger.to_edge(DOWN, buff=0.6)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 2.8s; waits above = 5.9s; remainder tuned to the
        # measured 13.56s Kokoro length (13.56 - 2.8 - 5.9 = 4.86)
        self.wait(4.86)


# --------------------------------------------------------------------------- #
# B03 — SETUP: already vertical-friendly (single column); narrower code
# lines, pills kept side-by-side (still fits MAX_W).
# measured audio: 11.472s
# --------------------------------------------------------------------------- #
class B03_ScoringRuleVerbatim(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("The scoring rule\n(verbatim):", color=PALETTE["ink"],
                          font_size=24, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)

        fn_label = fit(T("calculateBasicUrgency()", color=PALETTE["slate"], font_size=14, font=MONO), 3.3)
        fn_label.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(fn_label), run_time=0.3)
        self.wait(1.4)

        code_line1 = fit(T("if (text.includes(", color=PALETTE["bg"], font_size=18, font=MONO), 3.3)
        code_line2 = fit(T("  'immediate') ||", color=PALETTE["bg"], font_size=18, font=MONO), 3.3)
        code_line3 = fit(T("  text.includes(", color=PALETTE["bg"], font_size=18, font=MONO), 3.3)
        code_line4 = fit(T("  'emergency'))", color=PALETTE["bg"], font_size=18, font=MONO), 3.3)
        code_line5 = fit(T("score += 3;", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD"), 3.3)
        code = VGroup(code_line1, code_line2, code_line3, code_line4, code_line5).arrange(
            DOWN, aligned_edge=LEFT, buff=0.18)
        code_panel = panel(width=code.width + 0.5, height=code.height + 0.4,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        code_panel.next_to(fn_label, DOWN, buff=0.3)
        code.move_to(code_panel.get_center())

        self.play(Create(code_panel), run_time=0.35)
        self.play(FadeIn(code, shift=UP * 0.1), run_time=0.6)

        pills_label = fit(T("TRIGGERS ON\nEITHER WORD:", color=PALETTE["slate"],
                                font_size=13, font=MONO, line_spacing=1.2), 3.3)
        pill1_txt = T("immediate", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD")
        pill1 = panel(width=pill1_txt.width + 0.3, height=pill1_txt.height + 0.25,
                       fill=PALETTE["bg"], stroke=PALETTE["crimson"], corner_radius=0.2)
        pill1_txt.move_to(pill1.get_center())
        pill2_txt = T("emergency", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD")
        pill2 = panel(width=pill2_txt.width + 0.3, height=pill2_txt.height + 0.25,
                       fill=PALETTE["bg"], stroke=PALETTE["crimson"], corner_radius=0.2)
        pill2_txt.move_to(pill2.get_center())
        pills_row = VGroup(VGroup(pill1, pill1_txt), VGroup(pill2, pill2_txt)).arrange(RIGHT, buff=0.3)
        if pills_row.width > MAX_W:
            pills_row.scale_to_fit_width(MAX_W)
        pills = VGroup(pills_label, pills_row).arrange(DOWN, buff=0.2)
        pills.next_to(code_panel, DOWN, buff=0.35)
        self.play(FadeIn(pills, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        score_box = box_around(code_line5, buff=0.08, color=PALETTE["crimson"])
        self.play(Create(score_box), run_time=0.3)
        self.wait(1.0)

        caption = fit(T("+3 points — anywhere in the\ntitle, no context understood.",
                            color=PALETTE["crimson"], font_size=15, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 2.85s, waits above = 3.9s; remainder tuned to the
        # measured 11.472s Kokoro length (11.472 - 2.85 - 3.9 = 4.722)
        self.wait(4.722)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY: THE big redesign. Parent's LEFT (Medicare) / RIGHT
# (Nasdaq) panels -> TOP/BOTTOM stack, both simultaneously visible — the
# beat's "word alone vs. word in context, both titles together" requirement
# needs simultaneity, not left-right placement specifically.
# measured audio: 23.208s
# --------------------------------------------------------------------------- #
class B04_WordInContext(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same word.\nDifferent context.", color=PALETTE["bg"],
                          font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # ---- TOP: Medicare rule ----
        top_panel = panel(width=3.8, height=3.1, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        top_hdr = fit(T("MEDICARE RULE — 10/Critical", color=PALETTE["sage"], font_size=12, font=MONO), 3.5)
        top_alone_tag = fit(T("TRIGGER WORD ALONE:", color=PALETTE["sage"], font_size=11, font=MONO), 3.5)
        top_alone_word = T("emergency", color=PALETTE["crimson"], font_size=18, font=MONO, weight="BOLD")
        top_alone_box = box_around(top_alone_word, buff=0.1, color=PALETTE["crimson"])
        top_alone = VGroup(top_alone_box, top_alone_word)
        top_ctx_tag = fit(T("ACTUALLY PART OF:", color=PALETTE["sage"], font_size=11, font=MONO), 3.5)
        top_ctx_row, top_hl = inline_highlight(
            "", "Emergency", "Medical", font_size=11, base_color=PALETTE["bg"],
            hl_color=PALETTE["gold"], font=MONO,
        )
        top_ctx_row2 = fit(T("Treatment and Labor Act", color=PALETTE["bg"], font_size=11, font=MONO), 3.5)
        # buff widened from 0.06 -> 0.16: box_around(top_hl, buff=0.06) built later
        # around the highlighted word in top_ctx_row protrudes ~0.015 world units
        # below its own row at a tight 0.06 gap — real pre-flight found this
        # literally slicing through the ascenders of top_ctx_row2's text
        # ("Treatment and Labor Act"), not a QC-tool false positive.
        top_ctx = VGroup(fit(top_ctx_row, 3.5), top_ctx_row2).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        top_caption = fit(T("a law's name — not an\nactual emergency", color=PALETTE["gold"],
                                font_size=11, line_spacing=1.2), 3.5)
        top_content = VGroup(
            top_hdr, top_alone_tag, top_alone, top_ctx_tag, top_ctx, top_caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        top_content.move_to(top_panel.get_center())

        # ---- BOTTOM: Nasdaq filing ----
        bot_panel = panel(width=3.8, height=3.1, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        bot_hdr = fit(T("NASDAQ FILING — 9/Critical", color=PALETTE["sage"], font_size=12, font=MONO), 3.5)
        bot_alone_tag = fit(T("TRIGGER WORD ALONE:", color=PALETTE["sage"], font_size=11, font=MONO), 3.5)
        bot_alone_word = T("immediate", color=PALETTE["crimson"], font_size=18, font=MONO, weight="BOLD")
        bot_alone_box = box_around(bot_alone_word, buff=0.1, color=PALETTE["crimson"])
        bot_alone = VGroup(bot_alone_box, bot_alone_word)
        bot_ctx_tag = fit(T("ACTUALLY PART OF:", color=PALETTE["sage"], font_size=11, font=MONO), 3.5)
        bot_ctx_row, bot_hl = inline_highlight(
            "Notice of Filing", "and", "", font_size=11, base_color=PALETTE["bg"],
            hl_color=PALETTE["bg"], font=MONO,
        )
        bot_ctx_row2, bot_hl2 = inline_highlight(
            "", "Immediate", "Effectiveness", font_size=11, base_color=PALETTE["bg"],
            hl_color=PALETTE["gold"], font=MONO,
        )
        bot_ctx = VGroup(fit(bot_ctx_row, 3.5), fit(bot_ctx_row2, 3.5)).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        bot_caption = fit(T("standard boilerplate —\nevery routine filing", color=PALETTE["gold"],
                                font_size=11, line_spacing=1.2), 3.5)
        bot_content = VGroup(
            bot_hdr, bot_alone_tag, bot_alone, bot_ctx_tag, bot_ctx, bot_caption,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

        bot_content.move_to(bot_panel.get_center())

        # content centered within its own panel FIRST, THEN the two panels
        # are grouped, height-capped and positioned as rigid units — same
        # fix as B02's panels (a next_to chain here pushed bot_panel well
        # past the bottom of the frame on the real static pre-flight run).
        # The highlight boxes around top_hl/bot_hl2 are built ONLY after
        # this final scale+position step (see inline_highlight's docstring
        # for why building them earlier would go stale).
        top_group = VGroup(top_panel, top_content)
        bot_group = VGroup(bot_panel, bot_content)
        panels = VGroup(top_group, bot_group).arrange(DOWN, buff=0.22)
        if panels.height > 4.8:
            panels.scale_to_fit_height(4.8)
        panels.next_to(title, DOWN, buff=0.3)

        top_ctx_box = box_around(top_hl, buff=0.06, color=PALETTE["gold"])
        bot_ctx_box = box_around(bot_hl2, buff=0.06, color=PALETTE["gold"])

        self.play(Create(top_panel), Create(bot_panel), run_time=0.5)
        self.play(FadeIn(top_hdr), FadeIn(bot_hdr), run_time=0.3)
        self.wait(0.8)
        self.play(
            FadeIn(top_alone_tag), FadeIn(top_alone),
            FadeIn(bot_alone_tag), FadeIn(bot_alone),
            run_time=0.5,
        )
        self.wait(4.5)
        self.play(
            FadeIn(top_ctx_tag), FadeIn(top_ctx), Create(top_ctx_box),
            FadeIn(bot_ctx_tag), FadeIn(bot_ctx), Create(bot_ctx_box),
            run_time=0.6,
        )
        self.wait(5.5)
        self.play(FadeIn(top_caption), FadeIn(bot_caption), run_time=0.4)
        self.wait(3.2)

        closing = fit(T("The scorer can't see\nthe difference.", color=PALETTE["gold"],
                            font_size=15, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 3.2s, waits above = 14.8s; remainder tuned to the
        # measured 23.208s Kokoro length (23.208 - 3.2 - 14.8 = 5.208)
        self.wait(5.208)


# --------------------------------------------------------------------------- #
# B05 — FIX: parent's 3-way horizontal fan-out -> a single vertical chain:
# item -> review -> confirm -> downgrade -> fail-open, each its own stacked
# card. The fail-open branch is still its OWN explicit reveal, not bundled
# with the happy-path cards — same safety-critical requirement as the parent.
# measured audio: 25.608s
# --------------------------------------------------------------------------- #
class B05_FailOpenFlowDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("A second opinion,\nnot a rewrite:", color=PALETTE["ink"],
                          font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.2)

        item_box = panel(width=3.3, height=0.55, fill=PALETTE["ink"], stroke=PALETTE["slate"])
        item_txt = fit(T("ITEM (score > 6)", color=PALETTE["bg"], font_size=14, font=MONO), 3.0)
        item_txt.move_to(item_box.get_center())

        review_box = panel(width=3.7, height=0.8, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        review_txt = VGroup(
            fit(T("LOCAL MODEL REVIEW", color=PALETTE["bg"], font_size=13, font=MONO), 3.4),
            fit(T("(Ollama, this machine)", color=PALETTE["bg"], font_size=12, font=MONO), 3.4),
        ).arrange(DOWN, buff=0.06)
        review_txt.move_to(review_box.get_center())

        outcomes_label = fit(T("3 possible outcomes:", color=PALETTE["slate"], font_size=14, weight="BOLD"), 3.4)

        confirm_card = panel(width=3.7, height=0.7, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        confirm_txt = VGroup(
            fit(T("CONFIRM", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD"), 3.3),
            fit(T("goes through", color=PALETTE["bg"], font_size=12), 3.3),
        ).arrange(DOWN, buff=0.06)
        confirm_txt.move_to(confirm_card.get_center())

        downgrade_card = panel(width=3.7, height=0.7, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        downgrade_txt = VGroup(
            fit(T("DOWNGRADE", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), 3.3),
            fit(T("held back", color=PALETTE["bg"], font_size=12), 3.3),
        ).arrange(DOWN, buff=0.06)
        downgrade_txt.move_to(downgrade_card.get_center())

        failopen_card = panel(width=3.9, height=0.95, fill=PALETTE["ink"], stroke=PALETTE["gold"])
        failopen_txt = VGroup(
            fit(T("MODEL FAILS", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), 3.5),
            fit(T("goes through anyway", color=PALETTE["bg"], font_size=11), 3.5),
            fit(T("(FAIL-OPEN)", color=PALETTE["gold"], font_size=12, font=MONO, weight="BOLD"), 3.5),
        ).arrange(DOWN, buff=0.07)
        failopen_txt.move_to(failopen_card.get_center())

        # The previous draft chained 6 next_to() calls (item -> review ->
        # outcomes_label -> confirm -> downgrade -> fail-open) — a static
        # pre-flight run found 3 explicit coordinates landing well past
        # y=-4 (off the bottom of even the HARD frame). Building every
        # piece as a (box, text) unit FIRST, then arranging the whole chain
        # as one VGroup and capping its total height via scale_to_fit_height
        # (same proven pattern as B02/B04 above) guarantees the chain fits
        # regardless of any single element's assumed height. Arrows are
        # built AFTER this final layout, from each box's real get_top()/
        # get_bottom() — exactly like the landscape parent's B05.
        item_group = VGroup(item_box, item_txt)
        review_group = VGroup(review_box, review_txt)
        confirm_group = VGroup(confirm_card, confirm_txt)
        downgrade_group = VGroup(downgrade_card, downgrade_txt)
        failopen_group = VGroup(failopen_card, failopen_txt)

        chain = VGroup(item_group, review_group, outcomes_label,
                        confirm_group, downgrade_group, failopen_group)
        chain.arrange(DOWN, buff=0.22)
        if chain.height > 4.8:
            chain.scale_to_fit_height(4.8)
        chain.next_to(title, DOWN, buff=0.25)

        arrow1 = Arrow(item_box.get_bottom(), review_box.get_top(), buff=0.05,
                       color=PALETTE["slate"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        arrow2 = Arrow(review_box.get_bottom(), outcomes_label.get_top(), buff=0.05,
                       color=PALETTE["slate"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        self.play(Create(item_box), FadeIn(item_txt), run_time=0.4)
        self.play(Create(arrow1), run_time=0.2)
        self.play(Create(review_box), FadeIn(review_txt), run_time=0.4)
        self.wait(3.0)

        self.play(Create(arrow2), FadeIn(outcomes_label), run_time=0.3)

        self.play(Create(confirm_card), Create(downgrade_card), run_time=0.4)
        self.play(FadeIn(confirm_txt), FadeIn(downgrade_txt), run_time=0.4)
        self.wait(4.0)

        # the fail-open branch is revealed as its own explicit beat, not
        # bundled silently with the happy-path cards — this is this reel's
        # single most safety-critical visual element.
        self.play(Create(failopen_card), run_time=0.3)
        self.play(FadeIn(failopen_txt, shift=UP * 0.08), run_time=0.5)
        self.wait(5.0)

        closing = fit(T("A broken re-score never\nblocks the pipeline.", color=PALETTE["slate"],
                            font_size=14, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 4.1s, waits above = 13.2s; remainder tuned to the
        # measured 25.608s Kokoro length (25.608 - 4.1 - 13.2 = 8.308)
        self.wait(8.308)


# --------------------------------------------------------------------------- #
# B06 — PROOF: parent's 4-column table -> 3 stacked case cards, each
# showing the same 4 fields (case/score/review/verdict) as short lines —
# all 3 cards visible together satisfies "not sequential reveals that hide
# the comparison" without needing literal table columns in this narrow
# canvas.
# measured audio: 18.48s
# --------------------------------------------------------------------------- #
class B06_ThreeCaseResultsTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("All 3 test cases,\ntogether:", color=PALETTE["ink"],
                          font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        cards_data = [
            ("Medicare rule (id 4)", "10/Critical", "reviewed", "DOWNGRADE -> High", PALETTE["gold"], PALETTE["crimson"]),
            ("Nasdaq filing (id 966/967)", "9/Critical", "reviewed", "DOWNGRADE -> High", PALETTE["gold"], PALETTE["crimson"]),
            ("SEC insider-trading (id 153)", "5/Critical", "not sent to model", "UNTOUCHED", PALETTE["sage"], PALETTE["sage"]),
        ]

        cards = VGroup()
        extra_labels = []
        for case, score, review, verdict, vcolor, stroke_color in cards_data:
            case_txt = fit(T(case, color=PALETTE["bg"], font_size=14), 3.3)
            score_txt = fit(T(f"Keyword score: {score}", color=PALETTE["bg"], font_size=12, font=MONO), 3.3)
            review_txt = fit(T(f"LLM review: {review}", color=PALETTE["bg"], font_size=12), 3.3)
            verdict_txt = fit(T(verdict, color=vcolor, font_size=14, font=MONO, weight="BOLD"), 3.3)
            card_content = VGroup(case_txt, score_txt, review_txt, verdict_txt).arrange(
                DOWN, aligned_edge=LEFT, buff=0.1)
            card_bg = panel(width=3.7, height=card_content.height + 0.4,
                             fill=PALETTE["ink"], stroke=stroke_color)
            card_content.move_to(card_bg.get_center())
            cards.add(VGroup(card_bg, card_content))

        cards.arrange(DOWN, buff=0.18)
        cards.next_to(title, DOWN, buff=0.35)

        self.play(Create(cards[0][0]), run_time=0.3)
        self.play(FadeIn(cards[0][1]), run_time=0.3)
        self.wait(3.2)
        self.play(Create(cards[1][0]), run_time=0.3)
        self.play(FadeIn(cards[1][1]), run_time=0.3)
        self.wait(3.2)
        self.play(Create(cards[2][0]), run_time=0.3)
        self.play(FadeIn(cards[2][1]), run_time=0.3)
        self.wait(1.2)

        sec_label = fit(T("not reviewed — below\nalert threshold", color=PALETTE["sage"],
                              font_size=13, weight="BOLD", line_spacing=1.2), 3.4)
        sec_label.next_to(cards[2], DOWN, buff=0.2)
        self.play(FadeIn(sec_label, shift=UP * 0.06), run_time=0.3)
        self.wait(1.0)

        sec_verdict_box = box_around(cards[2][1][3], buff=0.08, color=PALETTE["sage"])
        self.play(Create(sec_verdict_box), run_time=0.3)
        # sum of plays = 3.0s, waits above = 8.6s; remainder tuned to the
        # measured 18.48s Kokoro length (18.48 - 3.0 - 8.6 = 6.88)
        self.wait(6.88)


# --------------------------------------------------------------------------- #
# B07 — HONEST-LIMITS: parent's 3-across row -> 3 stacked cards.
# measured audio: 18.528s
# --------------------------------------------------------------------------- #
class B07_HonestLimitsCards(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Three things this\ndoesn't claim:", color=PALETTE["bg"],
                          font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.9)

        cards_data = [
            ("1", "Conservative, not precise", "The correction lands on\n\"High,\" not Medium/Low."),
            ("2", "Small sample", "Tested against 2 known\nfalse-positive patterns."),
            ("3", "Real added latency", "Could add several minutes\nto a single run at scale."),
        ]

        cards = VGroup()
        for num, label, body in cards_data:
            num_badge = Circle(radius=0.26, color=PALETTE["crimson"], fill_opacity=0, stroke_width=2.2)
            num_txt = T(num, color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD")
            num_txt.move_to(num_badge.get_center())
            num_group = VGroup(num_badge, num_txt)

            label_txt = fit(T(label, color=PALETTE["gold"], font_size=15, weight="BOLD"), 3.3)
            body_txt = fit(T(body, color=PALETTE["bg"], font_size=12, line_spacing=1.25), 3.3)
            text_col = VGroup(label_txt, body_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            card_content = VGroup(num_group, text_col).arrange(RIGHT, buff=0.2, aligned_edge=UP)

            card_bg = panel(width=3.7, height=card_content.height + 0.35,
                             fill=PALETTE["ink"], stroke=PALETTE["crimson"])
            card_content.move_to(card_bg.get_center())
            cards.add(VGroup(card_bg, card_content))

        cards.arrange(DOWN, buff=0.16)
        cards.next_to(title, DOWN, buff=0.35)

        self.play(Create(VGroup(*[c[0] for c in cards])), run_time=0.5)
        holds = [3.5, 3.5, 3.5]
        for card, hold in zip(cards, holds):
            self.play(FadeIn(card[1], shift=UP * 0.08), run_time=0.4)
            self.wait(hold)

        closing = fit(T("Not softened.\nNot overclaimed.", color=PALETTE["gold"],
                            font_size=16, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.3)
        # sum of plays = 3.0s, waits above = 11.4s; remainder tuned to the
        # measured 18.528s Kokoro length (18.528 - 3.0 - 11.4 = 4.128)
        self.wait(4.128)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 5.544s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=38), MAX_W)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("fixed with Claude Code", color=PALETTE["ink"], font_size=24), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"],
                            font_size=22, line_spacing=1.25), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.95).move_to(ORIGIN)

        frame_w = min(content.width + 1.0, 3.95)
        frame_h = min(content.height + 1.0, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.55)
        self.wait(4.994)
