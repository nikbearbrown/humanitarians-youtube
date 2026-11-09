"""
Manim scenes for 2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts
"The Dashboard That Disagreed With Its Own Alerts"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard                  — silent title card (TITLE)
B01_ExecSummary                 — spoken personal-intro card (EXEC-SUMMARY)
B02_DashboardVsEmailHook        — the dashboard's own invented tier vs. what
                                   the real alert email reads (HOOK)
B03_OneQueryOneColumn           — the real pre-fix urgency_score cutoff SQL
                                   vs. the real impact_level column every
                                   other consumer already reads (SETUP)
B04_FourLineDiff                 — the real diff: 4 FILTER lines changed
                                   (DISCOVERY-FIX)
B05_HarnessTable                — this session's real before/after SQL
                                   harness results (VERIFICATION)
B06_HonestLimits                — 2 honest-limit cards, full weight
                                   (HONEST-LIMITS)
B07_Statement                  — takeaway statement card (TAKEAWAY)
B08_BrandOutro                  — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest sibling,
2026-10-27-the-correction-that-never-reached-the-email/scenes.py, for
visual consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted SQL line (B03's pre-fix cutoffs, B04's diff — both minus and
plus sides) and every count/result (B05's harness table) is verbatim from
the real source cited in SOURCES.md:
  - Regulatory_QA/backend/app/crud.py ("FeedCRUD.get_stats()", read-only,
    not modified by this build)
  - scripts/regulatory-intel/D1-VERIFICATION.md (the diff, the verification
    table)
  - verification/verify_dashboard_stats_output.txt (this session's own
    harness run)
Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement
cards, which are intentionally shorter restatements of their own spoken
narration (same convention as every sibling reel).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.10 (silent,
fixed target) B01=14.28 B02=17.95 B03=24.12 B04=17.88 B05=24.55 B06=29.11
B07=11.28 B08=1.51. Every self.play(run_time=...)/self.wait() value in each
scene below was independently re-summed against these measured durations
before rendering (see BUILD-LOG.md / FRICTIONAL.md).

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

        title_lines = ["The Dashboard That", "Disagreed With", "Its Own Alerts"]
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
# measured audio: 14.28s
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
            "This video: a dashboard that counts",
            "severity one way, while the real alert",
            "email counts it a completely different",
            "way — and nobody had ever checked",
            "whether those two numbers agreed.",
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
        # measured 14.28s Kokoro length (14.28 - 2.1 = 12.18)
        self.wait(12.18)


# --------------------------------------------------------------------------- #
# B02 — HOOK: the dashboard's own invented tier vs. what the real alert
# email reads. [Source: BEAT-SHEET.md B02]
# measured audio: 17.95s
# --------------------------------------------------------------------------- #
class B02_DashboardVsEmailHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Every item gets a severity label everything downstream trusts.",
                       color=PALETTE["bg"], font_size=25), 12.2)

        def tile(heading, value, color, val_fs=58):
            head_txt = fit(T(heading, color=PALETTE["bg"], font_size=18, line_spacing=1.2), 4.3)
            val_txt = T(value, color=color, font_size=val_fs, font=MONO, weight="BOLD")
            content = VGroup(head_txt, val_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=5.2, height=content.height + 1.0, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_email = tile("Email reads\nimpact_level:", "Medium", PALETTE["sage"])
        t_dash = tile("Dashboard counts it\nas (urgency_score):", "High", PALETTE["crimson"], val_fs=58)
        tiles = VGroup(t_email, t_dash).arrange(RIGHT, buff=0.6)
        t_dash_box = box_around(t_dash, buff=0.1, color=PALETTE["crimson"])

        zinger = fit(T("The dashboard never reads the label the email reads.", color=PALETTE["gold"],
                        font_size=32, weight="BOLD"), 11.8)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.85).move_to(ORIGIN)
        t_dash_box.move_to(t_dash.get_center())

        self.play(Write(title), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(t_email, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(t_dash, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_dash_box), run_time=0.3)
        self.wait(0.5)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.4+0.3+0.3+0.3+0.5 = 1.8s
        # waits above = 0.8+0.5+0.5 = 1.8s; remainder tuned to the measured
        # 17.95s Kokoro length (17.95 - 1.8 - 1.8 = 14.35)
        self.wait(14.35)


# --------------------------------------------------------------------------- #
# B03 — SETUP: the real pre-fix urgency_score cutoff SQL vs. the real
# impact_level column every other consumer already reads.
# [Source: Regulatory_QA/backend/app/crud.py, get_stats(); D1-VERIFICATION.md]
# measured audio: 24.12s
# --------------------------------------------------------------------------- #
class B03_OneQueryOneColumn(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One query re-derives its own answer.",
                       color=PALETTE["ink"], font_size=28), 12.2)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # Left: the real pre-fix urgency_score cutoff SQL, verbatim
        # (D1-VERIFICATION.md's "The fix" diff, "-" lines; crud.py pre-fix).
        code_header = T("get_stats() read (pre-fix):", color=PALETTE["gold"], font_size=16,
                         font=MONO, weight="BOLD")
        line1_str = "FILTER (WHERE urgency_score >= 8) as critical,"
        line2_str = "FILTER (WHERE urgency_score BETWEEN 6 AND 7) as high,"
        line3_str = "FILTER (WHERE urgency_score BETWEEN 4 AND 5) as medium,"
        line4_str = "FILTER (WHERE urgency_score <= 3) as low"

        # Highlight "urgency_score" within each line using Manim's own `t2c`
        # constructor param (the house-correct way to color a substring —
        # Manim resolves the real Pango glyph indices for it internally, so
        # this is the only one of three approaches tried this build that
        # neither mis-locates the highlight nor collapses real whitespace).
        # Two earlier attempts both failed for documented, real reasons (see
        # FRICTIONAL.md): (1) slicing the Text mobject directly by python
        # string index (`line[start:end]`) landed 1-2 characters late,
        # because Manim's Text gives whitespace no submobject of its own, so
        # plain string offsets silently drift once any space precedes the
        # slice -- confirmed by a rendered-frame inspection ("rgency_score
        # >=" boxed instead of "urgency_score"); (2) manually splitting each
        # line into separate prefix/needle/suffix Text() pieces fixed the
        # highlight boundary but collapsed the real spaces around the needle
        # (each piece's own leading/trailing whitespace is trimmed from its
        # layout box) -- confirmed by a second rendered-frame inspection
        # ("WHEREurgency_score>=" ran together with no gap). This toolkit's
        # render-free GATE A stub (static_scene_check.py) also does not
        # implement the real Text's `.chars` property used by attempt (1)'s
        # fix, which independently rules it out (hard GATE A error, nothing
        # rendered) even once the highlight itself was correct. `t2c` is
        # simple enough that the stub silently no-ops it, so GATE A passes
        # too. The box below wraps the WHOLE line (not just the substring)
        # for the same reason -- no sub-mobject handle is needed at all.
        needle = "urgency_score"
        line1 = T(line1_str, color=PALETTE["bg"], font_size=16, font=MONO,
                  t2c={needle: PALETTE["crimson"]})
        line2 = T(line2_str, color=PALETTE["bg"], font_size=16, font=MONO,
                  t2c={needle: PALETTE["crimson"]})
        line3 = T(line3_str, color=PALETTE["bg"], font_size=16, font=MONO)
        line4 = T(line4_str, color=PALETTE["bg"], font_size=16, font=MONO)
        code_lines = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.6, height=code_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        # Right: the real column every other consumer reads, verbatim
        fields_header = T("Everyone else reads:", color=PALETTE["gold"], font_size=16,
                           font=MONO, weight="BOLD")
        field_values = [
            "impact_level",
            "  -> Generate Email (alert)",
            "  -> feed list UI",
            "  -> RAG chat context",
        ]
        field_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=16, font=MONO) for v in field_values
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        fields_block = VGroup(fields_header, field_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fields_panel = panel(width=fields_block.width + 0.6, height=fields_block.height + 0.5,
                              fill=PALETTE["ink"], stroke=PALETTE["slate"])
        fields_block.move_to(fields_panel.get_center())
        fields_group = VGroup(fields_panel, fields_block)

        panels = VGroup(code_group, fields_group).arrange(RIGHT, buff=0.5)
        panels.next_to(title, DOWN, buff=0.5)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(fields_group, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        # Box the two already-colored "urgency_score" needle mobjects built
        # above by split_line() — the real field get_stats() actually read,
        # flagged crimson; "impact_level" on the right is boxed the same way
        # (a whole line, no slicing needed), to show the field it should
        # have read instead.
        box_1 = box_around(line1, buff=0.08, color=PALETTE["crimson"])
        box_1._qc_intentional = True
        box_2 = box_around(line2, buff=0.08, color=PALETTE["crimson"])
        box_2._qc_intentional = True

        column_line = field_lines[0]
        column_line.set_color(PALETTE["sage"])
        box_col = box_around(column_line, buff=0.06, color=PALETTE["sage"])
        box_col._qc_intentional = True

        self.play(Create(box_1), Create(box_2), run_time=0.3)
        self.play(Create(box_col), run_time=0.3)
        self.wait(1.5)

        caption = fit(T("Set together at first. They can drift apart.",
                        color=PALETTE["crimson"], font_size=22), 11.8)
        caption.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.5+0.4+0.3+0.3+0.4 = 2.7s
        # waits above = 1.0+1.0+2.0+1.5 = 5.5s; remainder tuned to
        # the measured 24.12s Kokoro length (24.12 - 2.7 - 5.5 = 15.92)
        self.wait(15.92)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the real diff — 4 FILTER lines changed.
# [Source: D1-VERIFICATION.md, "The fix"]
# measured audio: 17.88s
# --------------------------------------------------------------------------- #
class B04_FourLineDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Four lines. The whole fix.", color=PALETTE["ink"], font_size=32), 12.0)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_strs = [
            "- COUNT(*) FILTER (WHERE urgency_score >= 8) as critical,",
            "- COUNT(*) FILTER (WHERE urgency_score BETWEEN 6 AND 7) as high,",
            "- COUNT(*) FILTER (WHERE urgency_score BETWEEN 4 AND 5) as medium,",
            "- COUNT(*) FILTER (WHERE urgency_score <= 3) as low",
        ]
        plus_strs = [
            "+ COUNT(*) FILTER (WHERE impact_level = 'Critical') as critical,",
            "+ COUNT(*) FILTER (WHERE impact_level = 'High') as high,",
            "+ COUNT(*) FILTER (WHERE impact_level = 'Medium') as medium,",
            "+ COUNT(*) FILTER (WHERE impact_level = 'Low') as low",
        ]

        minus_lines = VGroup(*[
            T(s, color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD") for s in minus_strs
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
        # lesson this fellow's 2026-10-27 report's BUILD-LOG.md/FRICTIONAL.md
        # documented catching for its own B04 the hard way — applied proactively
        # here instead of re-discovering it.
        minus_block = VGroup(minus_lines, strikes)

        plus_lines = VGroup(*[
            T(s, color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD") for s in plus_strs
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)

        pairs = VGroup(minus_block, plus_lines).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        fit(pairs, 11.6)

        diff_panel = panel(width=pairs.width + 0.8, height=pairs.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.35)

        footnote = fit(T("(same response shape — Stats.jsx needs no change)",
                          color=PALETTE["slate"], font_size=16), 10.5)
        footnote.next_to(diff_group, DOWN, buff=0.3)

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_lines), run_time=0.4)
        self.play(Create(strikes), run_time=0.4)
        self.wait(1.1)
        self.play(FadeIn(plus_lines, shift=UP * 0.1), run_time=0.6)
        self.wait(1.3)
        self.play(FadeIn(footnote, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        caption = fit(T("Same windowing. Just a different column.",
                        color=PALETTE["slate"], font_size=21), 11.8)
        caption.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.4+0.6+0.4+0.4 = 3.0s
        # waits above = 0.8+1.1+1.3+0.8 = 4.0s; remainder tuned to
        # the measured 17.88s Kokoro length (17.88 - 3.0 - 4.0 = 10.88)
        self.wait(10.88)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: this session's real before/after SQL harness.
# [Source: verification/verify_dashboard_stats_output.txt]
# measured audio: 24.55s
# --------------------------------------------------------------------------- #
class B05_HarnessTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real query against the real distribution:",
                       color=PALETTE["ink"], font_size=26), 12.4)

        def tier_tile(tier, old, new, color):
            head = T(tier, color=PALETTE["bg"], font_size=22, font=MONO, weight="BOLD")
            vals = T(f"{old} -> {new}", color=color, font_size=32, font=MONO, weight="BOLD")
            content = VGroup(head, vals).arrange(DOWN, buff=0.3)
            bg = panel(width=2.95, height=content.height + 0.9, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_crit = tier_tile("Critical", 32, 33, PALETTE["teal_on_ink"])
        t_high = tier_tile("High", 139, 98, PALETTE["crimson"])
        t_med = tier_tile("Medium", 240, 280, PALETTE["gold"])
        t_low = tier_tile("Low", 0, 0, PALETTE["teal_on_ink"])

        tiles = VGroup(t_crit, t_high, t_med, t_low).arrange(RIGHT, buff=0.35)
        fit(tiles, 12.4)

        totals = fit(T("62 / 411 rows (15%) land in a different tier",
                       color=PALETTE["slate"], font_size=26, font=MONO, weight="BOLD"), 11.8)

        caption1 = fit(T("The old method overcounted High by 41 items — 30% inflated.",
                         color=PALETTE["crimson"], font_size=23, weight="BOLD"), 12.0)

        caption2 = fit(T("Matches D1-VERIFICATION.md's live-DB table exactly.",
                         color=PALETTE["slate"], font_size=23), 12.0)

        # canvas-fill: arrange the WHOLE block (title through caption2) as one
        # centered group with generous vertical buffs, rather than pinning the
        # title to the top edge — GATE V measured the top-anchored layout at
        # only 50% of the safe area (min 55%): a real underfill, with content
        # clustered near the top and the bottom half of the frame empty.
        # Bigger tiles/type plus a vertically centered block, not an invisible
        # spacer, per this project's canvas-fill requirement.
        block = VGroup(title, tiles, totals, caption1, caption2).arrange(DOWN, buff=0.7)
        block.move_to(ORIGIN)

        t_high_box = box_around(t_high, buff=0.09, color=PALETTE["crimson"])
        t_high_box.move_to(t_high.get_center())

        self.play(Write(title), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(t_crit, shift=UP * 0.1), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(t_high, shift=UP * 0.1), run_time=0.3)
        self.play(Create(t_high_box), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(t_med, shift=UP * 0.1), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(t_low, shift=UP * 0.1), run_time=0.3)
        self.wait(0.5)
        self.play(FadeIn(totals, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.3+0.3+0.3+0.4+0.4+0.4 = 3.2s
        # waits above = 1.0+0.3+0.3+0.3+0.5+1.0+1.0 = 4.4s; remainder tuned to
        # the measured 24.55s Kokoro length (24.55 - 3.2 - 4.4 = 16.95)
        self.wait(16.95)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: D1-VERIFICATION.md "What's NOT touched"/"Verification"; RUN_LOG.md 2026-11-03]
# measured audio: 29.11s
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
            "1. Only this one\nquery changed",
            ["total_feeds, source_distribution,", "recent_activity, the route, and", "Stats.jsx are untouched. How", "impact_level is set is untouched too."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. Verified unwindowed,\nnot live",
            ["Checked against the full 411-row", "table. The real 7/30-day rolling", "windows weren't re-checked against", "live data — this fixture is stale."],
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
        # 29.11s Kokoro length (29.11 - 2.2 - 5.7 = 21.21)
        self.wait(21.21)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 11.28s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "A dashboard that re-derives",
            "its own answer",
        ]
        line2 = [
            "from a different number isn't",
            "measuring the same thing. Two",
            "consumers have to read the",
            "same column.",
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
        # tuned to the measured 11.28s Kokoro length (11.28 - 1.7 - 1.8 = 7.78)
        self.wait(7.78)


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
