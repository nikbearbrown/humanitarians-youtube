"""
Manim scenes for 2026-10-20-the-filter-that-didnt-know-its-own-labels
"The Filter That Didn't Know Its Own Labels"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard          — silent title card (TITLE)
B01_ExecSummary         — spoken personal-intro card (EXEC-SUMMARY)
B02_SixthLabelHook      — "5" fixed labels vs "+1" dynamic label (HOOK)
B03_EnumVsClassifier    — the real 5-value enum vs the real identifySource()
                          template string that builds a 6th kind of label (SETUP)
B04_TwoLineDiff         — the real 2-line diff from commit 565e84e (DISCOVERY-FIX)
B05_TestClientTable     — real before/after FastAPI TestClient results (VERIFICATION)
B06_HonestLimits        — 2 honest-limit cards, full weight (HONEST-LIMITS)
B07_Statement           — takeaway statement card (TAKEAWAY)
B08_BrandOutro          — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest sibling,
2026-10-15-the-alert-that-waited-for-a-second-item/scenes.py, for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted enum value (B03), every quoted code line (B03's identifySource()
template, B04's diff) and every status code/result (B05's TestClient table)
is verbatim from the real source files cited in SOURCES.md:
  - Regulatory_QA/backend/app/models.py (SourceFeed enum)
  - scripts/regulatory-intel/workflow.dev.json (identifySource())
  - Regulatory_QA/backend/app/routers/feeds.py, commit 565e84e (the diff)
  - verification/verify_source_feed_output.txt (this session's live TestClient run)
Nothing paraphrased except the B01/B02/B06/B07 on-screen summary/statement
cards, which are intentionally shorter restatements of their own spoken
narration (same convention as every sibling reel).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.05 (silent,
fixed target) B01=15.02 B02=12.24 B03=23.98 B04=22.13 B05=27.12 B06=26.83
B07=9.91 B08=1.51. Every self.play(run_time=...)/self.wait() value in each
scene below was independently re-summed against these measured durations
before rendering (see BUILD-LOG.md / FRICTIONAL.md for the verification
script used).

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
# measured (silent) duration: 4.05s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Filter That", "Didn't Know", "Its Own Labels"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=50, weight="BOLD"), 12.0) for l in title_lines
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
        # sum of plays = 1.6s; remainder tuned to the measured 4.05s silent track
        self.wait(2.45)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 15.02s
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
            "This video: an API filter that rejected",
            "the exact labels our own classifier",
            "builds on the fly — a one-line type fix",
            "that closes a gap I flagged, but didn't",
            "fix, last week.",
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
        # measured 15.02s Kokoro length (15.02 - 2.1 = 12.92)
        self.wait(12.92)


# --------------------------------------------------------------------------- #
# B02 — HOOK: "5" fixed labels vs "+1" dynamic label, built live.
# [Source: BEAT-SHEET.md B02]
# measured audio: 12.24s
# --------------------------------------------------------------------------- #
class B02_SixthLabelHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our source classifier doesn't just pick from a short list anymore.",
                       color=PALETTE["bg"], font_size=27), 12.2)

        def tile(number, label, color, num_fs=72):
            num_txt = T(number, color=color, font_size=num_fs, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["bg"], font_size=19, line_spacing=1.2), 4.3)
            content = VGroup(num_txt, lab_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=4.9, height=content.height + 1.0, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t_fixed = tile("5", "fixed labels\nin the enum", PALETTE["sage"])
        t_dynamic = tile("+1", "dynamic label,\nbuilt live", PALETTE["gold"], num_fs=66)
        tiles = VGroup(t_fixed, t_dynamic).arrange(RIGHT, buff=0.6)
        t_dynamic_box = box_around(t_dynamic, buff=0.1, color=PALETTE["gold"])

        zinger = fit(T("Our filter endpoint never got the memo.", color=PALETTE["gold"],
                        font_size=40, weight="BOLD"), 11.8)

        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.85).move_to(ORIGIN)
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
# B03 — SETUP: the real 5-value SourceFeed enum vs the real identifySource()
# template string that builds a 6th kind of label.
# [Source: models.py SourceFeed; workflow.dev.json identifySource()]
# measured audio: 23.98s
# --------------------------------------------------------------------------- #
class B03_EnumVsClassifier(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Five fixed labels. One classifier that builds a sixth.",
                       color=PALETTE["ink"], font_size=27), 12.2)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # Left: the real 5-value enum, verbatim (models.py)
        enum_header = T("SourceFeed (models.py)", color=PALETTE["gold"], font_size=16,
                         font=MONO, weight="BOLD")
        enum_values = [
            '"SEC Press Releases"',
            '"Federal Register - Securities"',
            '"FINRA Enforcement News"',
            '"CFTC Regulations"',
            '"Investment Advisor Rules"',
        ]
        enum_lines = VGroup(*[
            T(v, color=PALETTE["bg"], font_size=16, font=MONO) for v in enum_values
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        enum_block = VGroup(enum_header, enum_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        enum_panel = panel(width=enum_block.width + 0.6, height=enum_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        enum_block.move_to(enum_panel.get_center())
        enum_group = VGroup(enum_panel, enum_block)

        # Right: the real identifySource() dynamic-label branch, verbatim
        code_header = T("identifySource() (workflow.dev.json)", color=PALETTE["gold"],
                         font_size=16, font=MONO, weight="BOLD")
        line_a_str = "if (creator && creator !== 'Unknown') {"
        line_b_str = "  return `Federal Register - ${creator}`;"
        line_c_str = "}"
        code_lines = VGroup(*[
            T(s, color=PALETTE["bg"], font_size=16, font=MONO)
            for s in (line_a_str, line_b_str, line_c_str)
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        code_block = VGroup(code_header, code_lines).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        code_panel = panel(width=code_block.width + 0.6, height=code_block.height + 0.5,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_block.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_block)

        panels = VGroup(enum_group, code_group).arrange(RIGHT, buff=0.5)
        panels.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(enum_group, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)
        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_block), run_time=0.5)
        self.wait(2.0)

        # Flag the exact real substring "`Federal Register - ${creator}`" within
        # the code line via Text's own character-index slicing (no re-creation,
        # no paraphrase) — colored gold and boxed crimson.
        code_line_b = code_lines[1]
        needle = "`Federal Register - ${creator}`"
        start = line_b_str.index(needle)
        end = start + len(needle)
        highlight = code_line_b[start:end]
        highlight.set_color(PALETTE["gold"])
        flag_box = box_around(highlight, buff=0.08, color=PALETTE["crimson"])
        # intentional annotation: this box's edges necessarily cross the
        # parent code_line_b Text mobject's own centerline (it boxes a
        # SUBSTRING of a larger Text mobject, not a standalone one) —
        # exempted from GATE B's TEXT_ON_CURVE check per
        # manim_layout_audit.py's documented `_qc_intentional` escape hatch.
        flag_box._qc_intentional = True

        self.play(Create(flag_box), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("That label was never in the enum — and never could be.",
                        color=PALETTE["crimson"], font_size=24), 11.8)
        caption.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.5+0.4+0.4 = 2.5s
        # waits above = 1.0+1.0+2.0+1.5 = 5.5s; remainder tuned to
        # the measured 23.98s Kokoro length (23.98 - 2.5 - 5.5 = 15.98)
        self.wait(15.98)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the real 2-line diff from commit 565e84e.
# [Source: feeds.py, commit 565e84e]
# measured audio: 22.13s
# --------------------------------------------------------------------------- #
class B04_TwoLineDiff(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Two lines. The whole fix.", color=PALETTE["ink"], font_size=32), 12.0)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def diff_pair(minus_str, plus_str, fs=20):
            minus_line = T(minus_str, color=PALETTE["crimson"], font_size=fs, font=MONO, weight="BOLD")
            plus_line = T(plus_str, color=PALETTE["sage"], font_size=fs, font=MONO, weight="BOLD")
            pair = VGroup(minus_line, plus_line).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            strike = Line(minus_line.get_left() + LEFT * 0.05, minus_line.get_right() + RIGHT * 0.05,
                          color=PALETTE["crimson"], stroke_width=3)
            strike.move_to(minus_line.get_center())
            # intentional strike-through annotation — exempted from GATE B's
            # TEXT_ON_CURVE check (deliberately crosses minus_line's centerline).
            strike._qc_intentional = True
            return minus_line, plus_line, strike, pair

        m1, p1, s1, pair1 = diff_pair(
            "- source_feed: Optional[SourceFeed] = None,",
            "+ source_feed: Optional[str] = None,",
        )
        m2, p2, s2, pair2 = diff_pair(
            "- source_feed=source_feed.value if source_feed else None,",
            "+ source_feed=source_feed,",
            fs=17,
        )
        pairs = VGroup(pair1, pair2).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        diff_panel = panel(width=pairs.width + 0.8, height=pairs.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        pairs.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, pairs)
        diff_group.next_to(title, DOWN, buff=0.4)
        s1.move_to(m1.get_center())
        s2.move_to(m2.get_center())

        footnote = fit(T("(plus: the now-unused SourceFeed import, dropped)",
                          color=PALETTE["slate"], font_size=16), 10.5)
        footnote.next_to(diff_group, DOWN, buff=0.3)

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

        caption = fit(T("The database column was always just a string underneath.",
                        color=PALETTE["slate"], font_size=21), 11.8)
        # buff 0.55 -> 0.75: GATE B's post-render layout audit found this
        # caption's real bottom edge at y=-3.45, just outside the +/-3.4
        # safe-area half-height — a real overflow, not a false positive.
        caption.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.3+0.4+0.3+0.3+0.4+0.4+0.4 = 3.6s
        # waits above = 0.8+0.7+0.9+0.7+0.9+0.8 = 4.8s; remainder tuned to
        # the measured 22.13s Kokoro length (22.13 - 3.6 - 4.8 = 13.73)
        self.wait(13.73)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: the real before/after FastAPI TestClient results.
# [Source: verification/verify_source_feed_output.txt]
# measured audio: 27.12s
# --------------------------------------------------------------------------- #
class B05_TestClientTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Mounted the real router behind a FastAPI test client:",
                       color=PALETTE["ink"], font_size=25), 12.2)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        header = VGroup(
            fit(T("request", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 4.3),
            fit(T("before fix", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 4.3),
            fit(T("after fix", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 4.3),
        ).arrange(RIGHT, buff=0.7)

        def row_card(scenario, before, after, color):
            s_txt = fit(T(scenario, color=PALETTE["bg"], font_size=18, font=MONO,
                           weight="BOLD", line_spacing=1.2), 4.2)
            before_txt = fit(T(before, color=PALETTE["crimson"] if "422" in before else PALETTE["bg"],
                                font_size=14, font=MONO, line_spacing=1.25), 4.3)
            after_txt = fit(T(after, color=PALETTE["sage"] if "200" in after else PALETTE["bg"],
                               font_size=14, font=MONO, line_spacing=1.25), 4.3)
            content = VGroup(s_txt, before_txt, after_txt).arrange(DOWN, buff=0.16)
            bg = panel(width=4.7, height=content.height + 0.4, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        r_dynamic = row_card(
            "dynamic label\n(Dept. of Labor)",
            "422\nenum validation error\n(bug — label rejected)",
            "200\nCRUD got raw string\n(fixed)",
            PALETTE["gold"],
        )
        r_fixed = row_card(
            "fixed label\n(SEC Press Releases)",
            "200\n(already worked)",
            "200\n(unchanged — no regression)",
            PALETTE["teal"],
        )

        rows = VGroup(r_dynamic, r_fixed).arrange(RIGHT, buff=0.4)
        header.next_to(title, DOWN, buff=0.45)
        rows.next_to(header, DOWN, buff=0.35)
        r_dynamic_box = box_around(r_dynamic, buff=0.08, color=PALETTE["gold"])

        self.play(Create(header), run_time=0.3)
        self.wait(0.8)
        self.play(FadeIn(r_dynamic, shift=UP * 0.1), run_time=0.4)
        self.play(Create(r_dynamic_box), run_time=0.3)
        self.wait(2.2)
        self.play(FadeIn(r_fixed, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        caption1 = fit(T("The dynamic-label row: a real 422 before, a real 200 after.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption1.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption2 = fit(T("The fixed-label row never changed — no regression, either version.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption2.next_to(caption1, DOWN, buff=0.25)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.4+0.3+0.4+0.4+0.4 = 2.7s (incl. the opening
        # title Write(); an earlier pass miscounted this and left the final
        # wait 1.5s too long — caught by independently re-summing every
        # run_time/wait value in this file against the measured audio length
        # before rendering, see FRICTIONAL.md)
        # waits above = 1.0+0.8+2.2+1.5+2.0 = 7.5s; remainder tuned to
        # the measured 27.12s Kokoro length (27.12 - 2.7 - 7.5 = 16.92)
        self.wait(16.92)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: FACTCHECK.md #6, #7]
# measured audio: 26.83s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=34, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=20, weight="BOLD", line_spacing=1.2), 5.4)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=17, line_spacing=1.2), 5.4) for l in lines
            ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            bg = panel(width=5.8, height=content.height + 0.6, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. A latent gap,\nnot an observed incident",
            ["The frontend doesn't currently", "send this parameter at all —", "nothing shows this 422 ever", "reached a real caller."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. The database layer\nwas mocked, not live",
            ["Confirms the API layer accepts", "and forwards the label — not a", "live query against rows that", "actually carry it."],
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
        # 26.83s Kokoro length (26.83 - 2.2 - 5.7 = 18.93)
        self.wait(18.93)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 9.91s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "When a classifier is allowed",
            "to get smarter,",
        ]
        line2 = [
            "every consumer of its output has to",
            "keep up — including the one-line",
            "signature nobody revisits.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34), 11.8) for l in lines
        ]).arrange(DOWN, buff=0.3)
        bottom = VGroup(*[
            # crimson, not gold: GATE V's real luminance check measured gold
            # text directly on the cream page background (no ink panel
            # behind it here, unlike every other gold-text beat) at only
            # 0.29 separation (min 0.3) — a real low-contrast defect, not a
            # false positive. Crimson is already established as legible text
            # on "bg" elsewhere in this file (B03/B04 captions).
            fit(T(l, color=PALETTE["crimson"], font_size=30, weight="BOLD"), 11.8) for l in line2
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
        # tuned to the measured 9.91s Kokoro length (9.91 - 1.7 - 1.8 = 6.41)
        self.wait(6.41)


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
