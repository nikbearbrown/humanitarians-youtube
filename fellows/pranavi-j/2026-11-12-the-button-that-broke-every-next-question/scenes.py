"""
Manim scenes for 2026-11-12-the-button-that-broke-every-next-question
"The Button That Broke Every Next Question"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                 — spoken personal-intro card (EXEC-SUMMARY)
B02_CapVsNoCapHook              — the backend's real 10-feed cap vs. Select
                                   All's real pre-fix "no cap" code (HOOK)
B03_TwoBugsOneClick             — the real pre-fix handleSelectAll/
                                   handleToggle, the real backend max_items
                                   field, and the real pre-fix generic error
                                   line (SETUP)
B04_CapAndRealReason            — the real diff: MAX_SELECTABLE_FEEDS added
                                   to App.jsx, detail-extraction added to
                                   ChatInterface.jsx (DISCOVERY-FIX)
B05_HarnessTable                — this session's real before/after Node
                                   harness results (VERIFICATION)
B06_HonestLimits                — 2 honest-limit cards, full weight
                                   (HONEST-LIMITS)
B07_Statement                   — takeaway statement card (TAKEAWAY)
B08_BrandOutro                  — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest sibling,
2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/scenes.py, for
visual consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted code line (B02/B03's pre-fix selection/error logic, B04's diff
— both minus and plus sides) and every count/result (B05's harness table) is
verbatim from the real source cited in SOURCES.md:
  - Regulatory_QA/frontend/src/App.jsx ("handleToggle"/"handleSelectAll",
    read-only, not modified by this build)
  - Regulatory_QA/frontend/src/components/ChatInterface.jsx (error-reason
    extraction, read-only, not modified by this build)
  - scripts/regulatory-intel/E1-VERIFICATION.md (the diff, the verification
    table)
  - verification/verify_feed_cap_output.txt (this session's own harness run)
Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement
cards, which are intentionally shorter restatements of their own spoken
narration (same convention as every sibling reel).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.10 B01=14.06
B02=15.34 B03=28.73 B04=18.38 B05=29.59 B06=29.14 B07=13.49 B08=1.51. Every
self.play(run_time=...)/self.wait() value in each scene below was
independently re-summed against these measured durations before rendering
(see BUILD-LOG.md / FRICTIONAL.md).

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric)
per this project's canvas-fill requirement (60-80% of the safe area), and
builds its whole visible block as one centered VGroup (title through
closing caption) rather than top-anchoring, per the sibling reel's
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

        title_lines = ["The Button That Broke", "Every Next Question"]
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
# measured audio: 14.06s
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
            "This video: a button called 'Select All,'",
            "sitting at the top of a feed list, that",
            "could silently break every question you",
            "asked after clicking it — and an error",
            "message that never explained why.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=25), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.18)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
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
# B02 — HOOK: the backend's real 10-feed cap vs. Select All's real pre-fix
# "no cap" code. [Source: BEAT-SHEET.md B02]
# measured audio: 15.34s
# --------------------------------------------------------------------------- #
class B02_CapVsNoCapHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("The chat backend caps context at ten feeds.",
                       color=PALETTE["bg"], font_size=25), 12.2)

        def tile(heading, value, color, val_fs=58):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=18, line_spacing=1.2), 4.5)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=5.4, height=content.height + 1.0, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_backend = tile("Backend hard limit\n(feed_ids, max_items):", "10", PALETTE["sage"])
        t_selectall = tile("Select All button\n(pre-fix):", "NO CAP", PALETTE["crimson"], val_fs=46)
        tiles = VGroup(t_backend, t_selectall).arrange(RIGHT, buff=0.6)
        t_selectall_box = box_around(t_selectall, buff=0.1, color=PALETTE["crimson"])

        zinger = fit(T("The single most obvious button had no limit at all.", color=PALETTE["gold"],
                        font_size=30, weight="BOLD"), 11.8)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.85).move_to(ORIGIN)
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
# B03 — SETUP: the real pre-fix handleSelectAll/handleToggle, the real
# backend max_items field, and the real pre-fix generic error line.
# [Source: Regulatory_QA/frontend/src/App.jsx, src/components/ChatInterface.jsx
# (pre-fix); E1-VERIFICATION.md]
# measured audio: 28.73s
# --------------------------------------------------------------------------- #
class B03_TwoBugsOneClick(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Two bugs, one click away.",
                       color=PALETTE["ink"], font_size=30), 12.2)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # Top-left: the real pre-fix handleSelectAll, verbatim.
        code_header = T("App.jsx, handleSelectAll (pre-fix):", color=PALETTE["gold"], font_size=15,
                         font=MONO, weight="BOLD")
        select_all_str = "setSelected(new Set(feeds.map(f => f.id)));"
        select_all_line = T(select_all_str, color=PALETTE["bg"], font_size=15, font=MONO,
                             t2c={"feeds.map": PALETTE["crimson"]})
        code_block = VGroup(code_header, select_all_line).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.6, height=code_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        # Top-right: the real backend limit every selection should respect.
        fields_header = T("backend/app/models.py:", color=PALETTE["gold"], font_size=15,
                           font=MONO, weight="BOLD")
        # split across 2 lines (real parens-wrap) so the panel stays inside
        # the safe x-width — a single-line version pushed this panel's right
        # edge to x=6.54, past the +/-6.3 safe half-width, and shoved the
        # left code panel off the left edge too, once both were re-centered.
        field_value1 = T("feed_ids: List[int] = Field(", color=PALETTE["sage"], font_size=15,
                          font=MONO)
        field_value2 = T("  min_items=1, max_items=10)", color=PALETTE["sage"], font_size=15,
                          font=MONO)
        field_lines = VGroup(field_value1, field_value2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, field_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.6, height=fields_block.height + 0.5,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        top_row = VGroup(code_group, fields_group).arrange(RIGHT, buff=0.5)

        # Bottom: the real pre-fix generic error line.
        error_header = T("ChatInterface.jsx, catch block (pre-fix):", color=PALETTE["gold"],
                          font_size=15, font=MONO, weight="BOLD")
        error_line_str = "content: 'Failed to get response: ' + error.message,"
        error_line = T(error_line_str, color=PALETTE["crimson"], font_size=15, font=MONO,
                        weight="BOLD")
        error_result = T('// renders: "Request failed with status code 422"',
                          color=PALETTE["bg"], font_size=14, font=MONO)
        error_block = VGroup(error_header, error_line, error_result).arrange(
            DOWN, buff=0.22, aligned_edge=LEFT)
        error_panel = panel(width=error_block.width + 0.6, height=error_block.height + 0.5,
                             fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        error_block.move_to(error_panel.get_center())
        error_group = VGroup(error_panel, error_block)

        block = VGroup(top_row, error_group).arrange(DOWN, buff=0.45)
        block.next_to(title, DOWN, buff=0.45)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        box_cap = box_around(field_value2, buff=0.08, color=PALETTE["sage"])
        box_cap._qc_intentional = True
        box_nocap = box_around(select_all_line, buff=0.08, color=PALETTE["crimson"])
        box_nocap._qc_intentional = True
        self.play(Create(box_nocap), Create(box_cap), run_time=0.4)
        self.wait(1.0)

        self.play(FadeIn(error_group, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        caption = fit(T("The real reason was in the response. The code never read it.",
                        color=PALETTE["crimson"], font_size=20), 11.8)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.5+0.4+0.4+0.5+0.4 = 3.0s
        # waits above = 1.0+1.0+1.5+1.0+1.5 = 6.0s; remainder tuned to
        # the measured 28.73s Kokoro length (28.73 - 3.0 - 6.0 = 19.73)
        self.wait(19.73)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the real diff — MAX_SELECTABLE_FEEDS added to
# App.jsx, detail-extraction added to ChatInterface.jsx.
# [Source: E1-VERIFICATION.md, "The fix"]
# measured audio: 18.38s
# --------------------------------------------------------------------------- #
class B04_CapAndRealReason(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Capped at ten. Both paths.", color=PALETTE["ink"], font_size=32), 12.0)
        title.to_edge(UP, buff=0.75)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- setSelected(new Set(feeds.map(f => f.id)));",
        ]
        plus_strs = [
            "+ const MAX_SELECTABLE_FEEDS = 10;",
            "+ setSelected(new Set(",
            "+   feeds.slice(0, MAX_SELECTABLE_FEEDS).map(f => f.id)));",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD") for s in minus_strs
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        strikes = VGroup()
        for line in minus_lines:
            s = Line(line.get_left() + LEFT * 0.05, line.get_right() + RIGHT * 0.05,
                      color=PALETTE["crimson"], stroke_width=3)
            s.move_to(line.get_center())
            s._qc_intentional = True  # deliberately crosses its own line's centerline
            strikes.add(s)
        # group minus text + its strike-throughs together BEFORE the whole-block
        # fit() below, so scaling/repositioning carries both in lockstep (Line
        # has no settable .width, so strikes can't be recomputed after a scale —
        # they must already be nested inside the thing being scaled). Same
        # lesson this fellow's sibling reels' BUILD-LOG.md/FRICTIONAL.md
        # documented catching for their own diff beats the hard way — applied
        # proactively here instead of re-discovering it.
        minus_block = VGroup(minus_lines, strikes)

        plus_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD") for s in plus_strs
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)

        app_diff = VGroup(minus_block, plus_lines).arrange(DOWN, buff=0.35, aligned_edge=LEFT)

        chat_header = T("ChatInterface.jsx — catch block now reads the real reason:",
                         color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD")
        chat_plus_strs = [
            "+ const detail = error.response?.data?.detail;",
            "+ const reason = Array.isArray(detail)",
            "+   ? detail.map(d => d.msg || JSON.stringify(d)).join('; ')",
            "+   : detail || error.message;",
        ]
        chat_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD") for s in chat_plus_strs
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        chat_block = VGroup(chat_header, chat_lines).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        pairs = VGroup(app_diff, chat_block).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        fit(pairs, 11.8)

        diff_panel = panel(width=pairs.width + 0.8, height=pairs.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.35)

        footnote = fit(T("(handleToggle is capped the same way — both paths, not just the button)",
                          color=PALETTE["slate"], font_size=15), 11.0)
        footnote.next_to(diff_group, DOWN, buff=0.3)

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

        caption = fit(T("Not just the button — both selection paths, capped the same way.",
                        color=PALETTE["slate"], font_size=19), 11.8)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.4+0.5+0.5+0.4+0.4 = 3.4s
        # waits above = 0.8+1.0+1.0+1.0+0.8 = 4.6s; remainder tuned to
        # the measured 18.38s Kokoro length (18.38 - 3.4 - 4.6 = 10.38)
        self.wait(10.38)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: this session's real before/after Node harness.
# [Source: verification/verify_feed_cap_output.txt]
# measured audio: 29.59s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Five checks. Seven assertions. All pass.",
                       color=PALETTE["ink"], font_size=32), 12.6)

        def row(label, result, color):
            lab = fit(T(label, color=PALETTE["bg"], font_size=21, font=MONO), 7.4)
            res = fit(T(result, color=color, font_size=23, font=MONO, weight="BOLD"), 3.8)
            line = VGroup(lab, res).arrange(RIGHT, buff=0.5)
            return line

        rows = VGroup(
            row("1. Select All, 411 feeds", "-> 10", PALETTE["sage"]),
            row("2. 15x handleToggle", "-> stops at 10", PALETTE["sage"]),
            row("3. untoggle, then add", "-> still 10", PALETTE["sage"]),
            row("4. no detail in response", "-> falls back", PALETTE["sage"]),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rows_panel = panel(width=max(rows.width + 0.9, 11.0), height=rows.height + 0.75,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        rows.move_to(rows_panel.get_center())
        rows_group = VGroup(rows_panel, rows)

        old_msg = T('OLD: "Request failed with status code 422"',
                     color=PALETTE["crimson"], font_size=21, font=MONO, weight="BOLD")
        new_msg = T('NEW: "List should have at most 10 items', color=PALETTE["sage"], font_size=21,
                     font=MONO, weight="BOLD")
        new_msg2 = T('       after validation, not 15"', color=PALETTE["sage"], font_size=21,
                      font=MONO, weight="BOLD")
        msg_block = VGroup(old_msg, new_msg, new_msg2).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        msg_panel = panel(width=max(msg_block.width + 0.9, 11.0), height=msg_block.height + 0.7,
                           fill=PALETTE["ink"], stroke=PALETTE["gold"])
        msg_block.move_to(msg_panel.get_center())
        msg_group = VGroup(msg_panel, msg_block)

        totals = fit(T("7 / 7 assertions pass", color=PALETTE["slate"], font_size=34, font=MONO,
                       weight="BOLD"), 11.8)

        block = VGroup(title, rows_group, msg_group, totals).arrange(DOWN, buff=0.38)
        # height-cap so the block's top/bottom edges stay inside the safe
        # area (+/-3.4y) regardless of how large the individual rows/panels
        # grew to satisfy canvas-fill — same systemic guard this file's
        # vertical companion already uses for its own tallest beats.
        if block.height > 6.6:
            block.scale_to_fit_height(6.6)
        block.move_to(ORIGIN)

        new_msg_box = box_around(VGroup(new_msg, new_msg2), buff=0.1, color=PALETTE["sage"])
        new_msg_box.move_to(VGroup(new_msg, new_msg2).get_center())

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
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: E1-VERIFICATION.md "Verification"/"What's NOT touched"; RUN_LOG.md 2026-11-12]
# measured audio: 29.14s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=34, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=18, weight="BOLD", line_spacing=1.2), 5.5)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=16, line_spacing=1.2), 5.5) for l in lines
            ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            bg = panel(width=5.9, height=content.height + 0.6, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. No vite build,\nno browser check",
            ["node_modules isn't installed.", "Verified via a Node harness on", "extracted logic, plus the IDE's", "static diagnostics (0 new errors)."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. No UI cap\nindicator added",
            ["Selection silently stops growing", "past 10 — no disabled state, no", "tooltip. A reasonable follow-up,", "not required to close the bug."],
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
        # 29.14s Kokoro length (29.14 - 2.2 - 5.7 = 21.24)
        self.wait(21.24)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 13.49s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "The most obvious button",
            "needs to respect",
        ]
        line2 = [
            "the system's real limits. And",
            "when something fails, showing",
            "the real reason is what makes",
            "it fixable.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34), 11.8) for l in lines
        ]).arrange(DOWN, buff=0.3)
        bottom = VGroup(*[
            # crimson, not gold: gold is this file's PALETTE fill-only color
            # and a direct gold-on-cream text line is a known low-contrast
            # defect in this fellow's sibling reels — crimson is already
            # proven legible as text on "bg" elsewhere in this file (B03/B04
            # captions).
            fit(T(l, color=PALETTE["crimson"], font_size=27, weight="BOLD"), 11.8) for l in line2
        ]).arrange(DOWN, buff=0.26)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.7).move_to(ORIGIN)
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
        self.wait(1.8)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 1.8s; remainder
        # tuned to the measured 13.49s Kokoro length (13.49 - 1.7 - 1.8 = 9.99)
        self.wait(9.99)


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
