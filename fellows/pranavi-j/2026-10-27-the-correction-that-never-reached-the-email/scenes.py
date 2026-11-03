"""
Manim scenes for 2026-10-27-the-correction-that-never-reached-the-email
"The Correction That Never Reached The Email"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                 — spoken personal-intro card (EXEC-SUMMARY)
B02_IgnoredCorrectionHook       — LLM correction vs. what the email actually
                                   showed (HOOK)
B03_FieldWrittenFieldIgnored    — the real fields Layer 2 writes vs. the
                                   real pre-fix bucketing that never reads
                                   them (SETUP)
B04_EffectiveImpactDiff         — the real diff: effectiveImpact() added
                                   (DISCOVERY-FIX)
B05_HarnessTable                — this session's real before/after Node.js
                                   harness results (VERIFICATION)
B06_HonestLimits                — 2 honest-limit cards, full weight
                                   (HONEST-LIMITS)
B07_Statement                  — takeaway statement card (TAKEAWAY)
B08_BrandOutro                  — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest siblings,
2026-10-20-the-filter-that-didnt-know-its-own-labels/scenes.py and
2026-10-21-calibration-why-confidence-isnt-accuracy/scenes.py, for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted field name (B03's Layer 2 fields), every quoted code line
(B03's pre-fix bucketing, B04's diff — both minus and plus sides) and every
count/result (B05's harness table) is verbatim from the real source cited
in SOURCES.md:
  - scripts/regulatory-intel/workflow.dev.json ("Layer 2 - LLM Re-Score"
    and "Generate Email" nodes, read-only, not modified by this build)
  - scripts/regulatory-intel/C3-VERIFICATION.md (the diff, the verification
    table)
  - verification/verify_effective_severity_output.txt (this session's own
    live Node.js harness run)
Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement
cards, which are intentionally shorter restatements of their own spoken
narration (same convention as every sibling reel).

Long verbatim code lines (B03, B04) are composed as a VGroup and fit() to a
width budget as a WHOLE BLOCK (not per-line), so relative sizing across a
multi-line statement stays consistent — a deliberate choice for this reel's
longer real lines (the effectiveImpact() ternary is a genuinely long real
line), documented in BUILD-LOG.md / FRICTIONAL.md.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.10 (silent,
fixed target) B01=17.14 B02=19.54 B03=27.07 B04=19.82 B05=29.42 B06=29.83
B07=11.18 B08=1.51. Every self.play(run_time=...)/self.wait() value in each
scene below was independently re-summed against these measured durations
via a standalone checker before rendering (see BUILD-LOG.md / FRICTIONAL.md).

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric)
per this project's canvas-fill requirement (60-80% of the safe area).
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

        title_lines = ["The Correction That", "Never Reached", "The Email"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=46, weight="BOLD"), 12.0) for l in title_lines
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
# measured audio: 17.14s
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
            "This video: a severity correction an",
            "LLM review step computes and writes",
            "down, that the email generator never",
            "actually reads — so the old, wrong",
            "label keeps shipping, every time.",
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
        # measured 17.14s Kokoro length (17.14 - 2.1 = 15.04)
        self.wait(15.04)


# --------------------------------------------------------------------------- #
# B02 — HOOK: LLM correction vs. what the email actually showed.
# [Source: BEAT-SHEET.md B02]
# measured audio: 19.54s
# --------------------------------------------------------------------------- #
class B02_IgnoredCorrectionHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our pipeline added a second opinion: an LLM that can correct a wrong label.",
                       color=PALETTE["bg"], font_size=25), 12.2)

        def tile(heading, value, color, val_fs=58):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=18, line_spacing=1.2), 4.3)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=5.2, height=content.height + 1.0, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_llm = tile("LLM correction\nwrites:", "High", PALETTE["sage"])
        t_email = tile("Email still\nshows:", "Critical", PALETTE["crimson"], val_fs=50)
        tiles = VGroup(t_llm, t_email).arrange(RIGHT, buff=0.6)
        t_email_box = box_around(t_email, buff=0.1, color=PALETTE["crimson"])

        zinger = fit(T("The correction never reached the email.", color=PALETTE["gold"],
                        font_size=36, weight="BOLD"), 11.8)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.85).move_to(ORIGIN)
        t_email_box.move_to(t_email.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_llm, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_email, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_email_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.4+0.3+0.3+0.3+0.5 = 1.8s
        # waits above = 0.8+0.5+0.5 = 1.8s; remainder tuned to the measured
        # 19.54s Kokoro length (19.54 - 1.8 - 1.8 = 15.94)
        self.wait(15.94)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the real fields Layer 2 writes vs. the real pre-fix bucketing
# in Generate Email that never reads them.
# [Source: workflow.dev.json, "Layer 2 - LLM Re-Score" / "Generate Email"]
# measured audio: 27.07s
# --------------------------------------------------------------------------- #
class B03_FieldWrittenFieldIgnored(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Four fields written. One field read.",
                       color=PALETTE["ink"], font_size=28), 12.2)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # Left: the real fields Layer 2 writes back, verbatim (workflow.dev.json)
        fields_header = T("Layer 2 - LLM Re-Score writes:", color=PALETTE["gold"], font_size=16,
                           font=MONO, weight="BOLD")
        field_values = [
            "llm_reviewed",
            "llm_verdict",
            "llm_corrected_impact_level",
            "llm_downgrade",
        ]
        field_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=16, font=MONO) for v in field_values
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, field_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.6, height=fields_block.height + 0.5,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        # Right: the real pre-fix bucketing from Generate Email, verbatim
        code_header = T("Generate Email reads (pre-fix):", color=PALETTE["gold"],
                         font_size=16, font=MONO, weight="BOLD")
        line_a_str = "criticalItems = newItems.filter(i =>"
        line_a2_str = "  i.json.impact_level === 'Critical');"
        line_b_str = "highItems = newItems.filter(i =>"
        line_b2_str = "  i.json.impact_level === 'High');"
        code_lines = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=16, font=MONO)
            for s in (line_a_str, line_a2_str, line_b_str, line_b2_str)
        ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.6, height=code_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        panels = VGroup(fields_group, code_group).arrange(RIGHT, buff=0.5)
        panels.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(2.0)

        # Flag the exact real substring "impact_level" within both filter
        # lines via Text's own character-index slicing (no re-creation, no
        # paraphrase) — colored gold and boxed crimson, to show the field
        # Generate Email actually reads.
        needle = "impact_level"
        line_a2 = code_lines[1]
        start_a = line_a2_str.index(needle)
        end_a = start_a + len(needle)
        hl_a = line_a2[start_a:end_a]
        hl_a.set_color(PALETTE["gold"])
        box_a = box_around(hl_a, buff=0.06, color=PALETTE["crimson"])
        box_a._qc_intentional = True

        line_b2 = code_lines[3]
        start_b = line_b2_str.index(needle)
        end_b = start_b + len(needle)
        hl_b = line_b2[start_b:end_b]
        hl_b.set_color(PALETTE["gold"])
        box_b = box_around(hl_b, buff=0.06, color=PALETTE["crimson"])
        box_b._qc_intentional = True

        self.play(Create(box_a), Create(box_b), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("The correction was computed, written down, and never looked at again.",
                        color=PALETTE["crimson"], font_size=22), 11.8)
        caption.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.5+0.4+0.4 = 2.5s
        # waits above = 1.0+1.0+2.0+1.5 = 5.5s; remainder tuned to
        # the measured 27.07s Kokoro length (27.07 - 2.5 - 5.5 = 19.07)
        self.wait(19.07)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the real diff — effectiveImpact() added.
# [Source: C3-VERIFICATION.md, "The fix"]
# measured audio: 19.82s
# --------------------------------------------------------------------------- #
class B04_EffectiveImpactDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One helper. The whole fix.", color=PALETTE["ink"], font_size=32), 12.0)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- const criticalItems = newItems.filter(i => i.json.impact_level === 'Critical');",
            "- const highItems = newItems.filter(i => i.json.impact_level === 'High');",
        ]
        plus_strs = [
            "+ const effectiveImpact = (item) => (item.json.llm_reviewed &&",
            "+   item.json.llm_corrected_impact_level)",
            "+   ? item.json.llm_corrected_impact_level : item.json.impact_level;",
            "+ const criticalItems = newItems.filter(i => effectiveImpact(i) === 'Critical');",
            "+ const highItems = newItems.filter(i => effectiveImpact(i) === 'High');",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD") for s in minus_strs
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
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
        # they must already be nested inside the thing being scaled).
        minus_block = VGroup(minus_lines, strikes)

        plus_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=17, font=MONO, weight="BOLD") for s in plus_strs
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        pairs = VGroup(minus_block, plus_lines).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        fit(pairs, 11.6)

        diff_panel = panel(width=pairs.width + 0.8, height=pairs.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.35)

        footnote = fit(T("(items the LLM never touched: unaffected, no regression)",
                          color=PALETTE["slate"], font_size=16), 10.5)
        footnote.next_to(diff_group, DOWN, buff=0.3)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strikes), run_time=0.4)
        self.wait(1.2)
        self.play(FadeIn(plus_lines, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.9)

        caption = fit(T("An item the LLM never touched behaves exactly as before.",
                        color=PALETTE["slate"], font_size=21), 11.8)
        caption.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.4+0.6+0.4+0.4 = 3.0s
        # waits above = 0.8+1.2+1.5+0.9 = 4.4s; remainder tuned to
        # the measured 19.82s Kokoro length (19.82 - 3.0 - 4.4 = 12.42)
        self.wait(12.42)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: this session's real before/after Node.js harness.
# [Source: verification/verify_effective_severity_output.txt]
# measured audio: 29.42s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real code in a live Node.js harness:",
                       color=PALETTE["ink"], font_size=25), 12.2)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        def row_card(scenario, before, after, color):
            s_txt = fit(T(scenario, color=PALETTE["bg"], font_size=17, font=MONO,
                           weight="BOLD", line_spacing=1.2), 3.9)
            before_txt = fit(T(before, color=PALETTE["crimson"] if "bug" in before else PALETTE["bg"],
                                font_size=14, font=MONO, line_spacing=1.25), 3.9)
            after_txt = fit(T(after, color=PALETTE["sage"] if "fixed" in after else PALETTE["bg"],
                               font_size=14, font=MONO, line_spacing=1.25), 3.9)
            content = VGroup(s_txt, before_txt, after_txt).arrange(DOWN, buff=0.16)
            bg = panel(width=4.3, height=content.height + 0.4, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        r1 = row_card(
            "item-1\nconfirmed, recategorized",
            "Critical\n(bug — still Critical)",
            "High\n(fixed)",
            PALETTE["gold"],
        )
        r2 = row_card(
            "item-2\nconfirmed, unchanged",
            "High",
            "High\n(unchanged)",
            PALETTE["teal"],
        )
        r3 = row_card(
            "item-3\nnever reviewed",
            "Critical",
            "Critical\n(unchanged)",
            PALETTE["teal"],
        )

        rows = VGroup(r1, r2, r3).arrange(RIGHT, buff=0.35)
        # GATE B found the un-fit row group 13.6 wide against a 12.6-wide safe
        # area (3 cards @4.3 + 2 gaps @0.35) — r1's scenario label spilled past
        # the left safe edge (box=[-6.35, ...], half-width 6.3). fit() as a
        # whole block before positioning, same pattern used for B04's diff.
        fit(rows, 12.2)
        rows.next_to(title, DOWN, buff=0.5)
        r1_box = box_around(r1, buff=0.08, color=PALETTE["gold"])
        r1_box.move_to(r1.get_center())

        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.4)
        self.play(Create(r1_box), run_time=0.3)
        self.wait(1.3)
        self.play(FadeIn(r2, shift=UP * 0.1), FadeIn(r3, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        totals = fit(T("critical_count: 2 -> 1      high_count: 1 -> 2",
                       color=PALETTE["slate"], font_size=20, font=MONO, weight="BOLD"), 11.6)
        totals.next_to(rows, DOWN, buff=0.45)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption1 = fit(T("The recategorized item: counted Critical before, High after.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption1.next_to(totals, DOWN, buff=0.3)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.2)

        caption2 = fit(T("The other two items: unchanged in both versions — no regression.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption2.next_to(caption1, DOWN, buff=0.22)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.5+0.4+0.4+0.4 = 2.9s
        # waits above = 1.0+1.3+1.5+2.0+2.2 = 8.0s; remainder tuned to
        # the measured 29.42s Kokoro length (29.42 - 2.9 - 8.0 = 18.52)
        self.wait(18.52)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: C3-VERIFICATION.md "What's NOT touched"; RUN_LOG.md 2026-10-27]
# measured audio: 29.83s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=34, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=19, weight="BOLD", line_spacing=1.2), 5.5)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=16, line_spacing=1.2), 5.5) for l in lines
            ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            bg = panel(width=5.9, height=content.height + 0.6, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. Only this node's\nbucketing changed",
            ["Layer 2's own review logic, the", "High Priority Filter's downgrade", "gate, and the two earlier fixes", "in this node are untouched."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. A separate defect found,\nnot fixed, this week",
            ["Dashboard stats re-bucket by raw", "urgency score — cutoffs disagree", "with impact level on 57 of 411", "real rows. Flagged for later."],
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
        # 29.83s Kokoro length (29.83 - 2.2 - 5.7 = 21.93)
        self.wait(21.93)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 11.18s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A correction that's computed",
            "but never read",
        ]
        line2 = [
            "isn't a correction. Every consumer",
            "of a label has to check whether",
            "it actually changed.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34), 11.8) for l in lines
        ]).arrange(DOWN, buff=0.3)
        bottom = VGroup(*[
            # crimson, not gold: gold is this file's PALETTE fill-only color
            # and a direct gold-on-cream text line is a known low-contrast
            # defect in this fellow's sibling reels (GATE V measured 0.29
            # separation against a 0.3 floor there) — using crimson from the
            # start here, already proven legible as text on "bg" elsewhere
            # in this file (B03/B04 captions).
            fit(T(l, color=PALETTE["crimson"], font_size=28, weight="BOLD"), 11.8) for l in line2
        ]).arrange(DOWN, buff=0.28)

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
        # tuned to the measured 11.18s Kokoro length (11.18 - 1.7 - 1.8 = 7.68)
        self.wait(7.68)


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
