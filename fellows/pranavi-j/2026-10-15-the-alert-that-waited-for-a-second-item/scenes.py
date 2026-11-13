"""
Manim scenes for 2026-10-15-the-alert-that-waited-for-a-second-item
"The Alert That Waited for a Second Item"

Built under the toolkit's submission spec (effective 2026-09-07): see
brutalist/docs/FELLOWS-SUBMISSION.md and PIPELINE-SAFETY.md. B00 is a
declared-silent beat (audio_policy: "silence" in beat_sheet.json, real
silent mp3 generated via ffmpeg anullsrc) per build_safety.py's gate that
hard-fails any undeclared silent required-audio beat.

B00_TitleCard          — silent title card (TITLE)
B01_ExecSummary         — spoken personal-intro card (EXEC-SUMMARY)
B02_CounterHook         — 0 / 1 (flagged) / 2 item counter (HOOK)
B03_BuggyLineOfCode     — the real hasData guard line, newItems.length > 1 (SETUP)
B04_DeadEndAndFix       — before/after diff + the dead-end branch (DISCOVERY-FIX)
B05_BeforeAfterTable    — real 0/1/2-item before/after harness table (VERIFICATION)
B06_HonestLimits        — 2 honest-limit cards, full weight (HONEST-LIMITS)
B07_Statement           — takeaway statement card (TAKEAWAY)
B08_BrandOutro          — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's closest sibling, 2026-10-06-the-classifier-that-learned-when-not-to-guess/scenes.py,
for visual consistency across the series. Plain Text (Pango) throughout,
never Integer/DecimalNumber/MathTex — no LaTeX installed.

Every quoted code line (B03's hasData guard, B04's diff and dead-end
output) and every number (B05's before/after table) is verbatim from
/Users/pranavijs/mycroft/scripts/regulatory-intel/B6-VERIFICATION.md — see
SOURCES.md's claim -> source mapping. Nothing paraphrased except the
B01/B02/B06/B07 on-screen summary/statement cards, which are intentionally
shorter restatements of their own spoken narration (same convention as every
sibling reel's exec-summary/hook/statement beats).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule: B00=4.05 (silent,
fixed target) B01=15.94 B02=12.5 B03=16.54 B04=16.49 B05=22.9 B06=23.38
B07=10.03 B08=1.51.

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

        title_lines = ["The Alert That", "Waited for a", "Second Item"]
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
# measured audio: 15.94s
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
            "This video: a one-character bug in our",
            "regulatory pipeline meant a single urgent",
            "filing — the exact case our alert system",
            "exists for — could silently generate",
            "no alert at all.",
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
        # sum of plays = 2.1s; remainder tuned to the measured 15.456s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 15.94s -> wait 13.84)
        self.wait(13.36)


# --------------------------------------------------------------------------- #
# B02 — HOOK: 0 / 1 (flagged) / 2 item counter — the exactly-one-item case.
# [Source: BEAT-SHEET.md B02]
# measured audio: 12.5s
# --------------------------------------------------------------------------- #
class B02_CounterHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Our alert only fires when there's something urgent.",
                       color=PALETTE["bg"], font_size=30), 12.2)

        def tile(number, label, color, num_fs=72):
            num_txt = T(number, color=color, font_size=num_fs, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["bg"], font_size=20), 3.3)
            content = VGroup(num_txt, lab_txt).arrange(DOWN, buff=0.3)
            bg = panel(width=3.6, height=content.height + 1.0, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t0 = tile("0", "no items — correctly silent", PALETTE["sage"])
        t1 = tile("1", "one urgent item", PALETTE["gold"], num_fs=86)
        t2 = tile("2", "two items — already worked", PALETTE["teal_on_ink"])
        tiles = VGroup(t0, t1, t2).arrange(RIGHT, buff=0.35)
        t1_box = box_around(t1, buff=0.08, color=PALETTE["gold"])

        zinger = fit(T("Not zero. Not two. One.", color=PALETTE["gold"], font_size=44, weight="BOLD"), 11.8)

        # buff 0.55 -> 0.9: GATE V's real final-cut frame extraction measured
        # this beat's content bounding box at only 45% of the safe area (min
        # 55%) — genuine vertical underfill, not a false positive (width was
        # already ~91% but height only ~51%). Taller tiles + more inter-group
        # spacing closes the real gap.
        content = VGroup(title, tiles, zinger).arrange(DOWN, buff=0.9).move_to(ORIGIN)
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
# B03 — SETUP: the real hasData guard line, newItems.length > 1, flagged.
# [Source: B6-VERIFICATION.md, workflow.dev.json "Generate Email" node]
# measured audio: 16.54s
# --------------------------------------------------------------------------- #
class B03_BuggyLineOfCode(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("The real gate, straight from the workflow:", color=PALETTE["ink"], font_size=28), 12.0)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        node_txt = T("Generate Email — hasData guard", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD")
        node_pill = panel(width=node_txt.width + 0.5, height=node_txt.height + 0.3,
                           fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.25)
        node_txt.move_to(node_pill.get_center())
        node_group = VGroup(node_pill, node_txt)
        node_group.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(node_group, shift=UP * 0.1), run_time=0.3)
        self.wait(0.8)

        line_a_str = "const hasData = newItems && newItems.length > 1 &&"
        line_b_str = "  newItems[0].json &&"
        line_c_str = "  Object.keys(newItems[0].json).length > 1;"

        line_a = T(line_a_str, color=PALETTE["bg"], font_size=22, font=MONO)
        line_b = T(line_b_str, color=PALETTE["bg"], font_size=22, font=MONO)
        line_c = T(line_c_str, color=PALETTE["bg"], font_size=22, font=MONO)
        code_lines = VGroup(line_a, line_b, line_c).arrange(DOWN, buff=0.22, aligned_edge=LEFT)

        code_panel = panel(width=code_lines.width + 0.8, height=code_lines.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["slate"])
        code_lines.move_to(code_panel.get_center())
        code_group = VGroup(code_panel, code_lines)
        code_group.next_to(node_group, DOWN, buff=0.4)

        self.play(Create(code_panel), run_time=0.3)
        self.play(FadeIn(code_lines), run_time=0.5)
        self.wait(2.0)

        # Flag the exact real substring "newItems.length > 1" within line_a
        # via Text's own character-index slicing (no re-creation, no
        # paraphrase) — colored gold and boxed crimson.
        needle = "newItems.length > 1"
        start = line_a_str.index(needle)
        end = start + len(needle)
        highlight = line_a[start:end]
        highlight.set_color(PALETTE["gold"])
        flag_box = box_around(highlight, buff=0.1, color=PALETTE["crimson"])
        # intentional annotation: this box's edges necessarily cross the
        # parent line_a text's own centerline (it boxes a SUBSTRING of a
        # larger Text mobject, not a standalone one) — exempted from GATE B's
        # TEXT_ON_CURVE check per manim_layout_audit.py's documented
        # `_qc_intentional` escape hatch for deliberate strike-through/ring
        # annotations.
        flag_box._qc_intentional = True

        self.play(Create(flag_box), run_time=0.4)
        self.wait(1.5)

        caption = fit(T("Greater than — not greater than or equal.", color=PALETTE["crimson"], font_size=24), 11.5)
        caption.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.5+0.4+0.4 = 2.4s
        # waits above = 1.0+0.8+2.0+1.5 = 5.3s; remainder tuned to
        # the measured 16.54s Kokoro length (16.54 - 2.4 - 5.3 = 8.84)
        self.wait(8.84)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: the one-character diff, and the dead-end it leaves.
# [Source: B6-VERIFICATION.md "The fix" + "The bug" sections]
# measured audio: 16.49s
# --------------------------------------------------------------------------- #
class B04_DeadEndAndFix(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("One character. The whole bug.", color=PALETTE["ink"], font_size=30), 12.0)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        minus_line = T("- newItems.length > 1", color=PALETTE["crimson"], font_size=26, font=MONO, weight="BOLD")
        plus_line = T("+ newItems.length > 0", color=PALETTE["sage"], font_size=26, font=MONO, weight="BOLD")
        diff_lines = VGroup(minus_line, plus_line).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        strike = Line(minus_line.get_left() + LEFT * 0.05, minus_line.get_right() + RIGHT * 0.05,
                      color=PALETTE["crimson"], stroke_width=3)
        strike.move_to(minus_line.get_center())
        # intentional strike-through annotation — exempted from GATE B's
        # TEXT_ON_CURVE check (it deliberately crosses minus_line's centerline).
        strike._qc_intentional = True

        diff_panel = panel(width=diff_lines.width + 0.8, height=diff_lines.height + 0.6,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"])
        diff_lines.move_to(diff_panel.get_center())
        diff_group = VGroup(diff_panel, diff_lines)
        diff_group.next_to(title, DOWN, buff=0.35)
        strike.move_to(minus_line.get_center())

        self.play(Create(diff_panel), run_time=0.3)
        self.play(FadeIn(minus_line), run_time=0.3)
        self.play(Create(strike), run_time=0.3)
        self.wait(1.0)
        self.play(FadeIn(plus_line, shift=UP * 0.1), run_time=0.4)
        self.wait(1.0)

        fails_box = panel(width=7.6, height=0.9, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        fails_txt = fit(T("fails the check -> has_items: false", color=PALETTE["crimson"],
                           font_size=19, font=MONO, weight="BOLD"), 7.2)
        fails_txt.move_to(fails_box.get_center())
        fails_group = VGroup(fails_box, fails_txt)

        deadend_box = panel(width=7.6, height=0.9, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        deadend_txt = fit(T("If-node TRUE branch: [ ]  — nowhere to go", color=PALETTE["crimson"],
                             font_size=19, font=MONO, weight="BOLD"), 7.2)
        deadend_txt.move_to(deadend_box.get_center())
        deadend_group = VGroup(deadend_box, deadend_txt)

        lower_chain = VGroup(fails_group, deadend_group).arrange(DOWN, buff=0.45)
        lower_chain.next_to(diff_group, DOWN, buff=0.4)

        arrow1 = Arrow(diff_panel.get_bottom(), fails_box.get_top(), buff=0.06,
                       color=PALETTE["crimson"], stroke_width=3, max_tip_length_to_length_ratio=0.18)
        arrow2 = Arrow(fails_box.get_bottom(), deadend_box.get_top(), buff=0.06,
                       color=PALETTE["crimson"], stroke_width=3, max_tip_length_to_length_ratio=0.18)

        self.play(Create(arrow1), run_time=0.25)
        self.play(Create(fails_box), FadeIn(fails_txt), run_time=0.4)
        self.wait(0.8)
        self.play(Create(arrow2), run_time=0.25)
        self.play(Create(deadend_box), FadeIn(deadend_txt), run_time=0.4)
        # wait 1.5 -> 0.8: GATE V's real final-cut frame extraction sampled
        # this beat at its 50% timestamp (t≈8.25s) and found the closing
        # caption not yet on screen (it previously landed at t≈9.3s) — only
        # 41% of the safe area (min 55%), missing the caption's own width/
        # height. Bringing the caption in earlier means both the 50% and 85%
        # samples see the complete composition.
        self.wait(0.8)

        caption = fit(T("No error. No log line. Just an alert that never arrives.",
                        color=PALETTE["slate"], font_size=21), 11.8)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.3+0.3+0.4+0.25+0.4+0.25+0.4+0.4 = 3.5s
        # waits above = 0.8+1.0+1.0+0.8+0.8 = 4.4s; remainder tuned to
        # the measured 16.49s Kokoro length (16.49 - 3.5 - 4.4 = 8.59)
        self.wait(8.59)


# --------------------------------------------------------------------------- #
# B05 — VERIFICATION: the real before/after harness table (0/1/2 items), the
# 1-item row highlighted as the one that changed.
# [Source: B6-VERIFICATION.md "Verification" table]
# measured audio: 22.9s
# --------------------------------------------------------------------------- #
class B05_BeforeAfterTable(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Ran the real extracted code — not a rewritten copy:",
                       color=PALETTE["ink"], font_size=26), 12.2)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        header = VGroup(
            fit(T("batch", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 3.5),
            fit(T("before fix", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 3.5),
            fit(T("after fix", color=PALETTE["slate"], font_size=17, font=MONO, weight="BOLD"), 3.5),
        ).arrange(RIGHT, buff=0.55)

        def row_card(batch, before, after, color):
            b_txt = fit(T(batch, color=PALETTE["bg"], font_size=20, font=MONO, weight="BOLD"), 3.4)
            before_txt = fit(T(before, color=PALETTE["crimson"] if "bug" in before else PALETTE["bg"],
                                font_size=15, font=MONO, line_spacing=1.2), 3.5)
            after_txt = fit(T(after, color=PALETTE["sage"] if "fixed" in after else PALETTE["bg"],
                               font_size=15, font=MONO, line_spacing=1.2), 3.5)
            content = VGroup(b_txt, before_txt, after_txt).arrange(DOWN, buff=0.14)
            bg = panel(width=3.9, height=content.height + 0.4, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        r0 = row_card("0 items", "has_items: false\n(correct)", "has_items: false\n(unchanged — correct)", PALETTE["sage"])
        r1 = row_card("1 item", "has_items: false\n(bug — email skipped)", "has_items: true\n(fixed — email built)", PALETTE["gold"])
        r2 = row_card("2 items", "has_items: true\n(already worked)", "has_items: true\n(unchanged)", PALETTE["teal"])

        rows = VGroup(r0, r1, r2).arrange(RIGHT, buff=0.3)
        header.next_to(title, DOWN, buff=0.45)
        rows.next_to(header, DOWN, buff=0.3)
        r1_box = box_around(r1, buff=0.08, color=PALETTE["gold"])

        self.play(Create(header), run_time=0.3)
        self.wait(0.7)
        self.play(FadeIn(r0, shift=UP * 0.1), run_time=0.35)
        self.wait(1.2)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.35)
        self.play(Create(r1_box), run_time=0.3)
        self.wait(2.0)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.35)
        self.wait(1.3)

        caption1 = fit(T("The 1-item row: silently skipped before, a real email after.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption1.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(caption1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)

        caption2 = fit(T("Re-run against the real patched file on disk: same result.",
                         color=PALETTE["slate"], font_size=19), 11.8)
        caption2.next_to(caption1, DOWN, buff=0.25)
        self.play(FadeIn(caption2, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3+0.35+0.35+0.3+0.35+0.4+0.4 = 2.95s
        # waits above = 1.0+0.7+1.2+2.0+1.3+2.0 = 8.2s; remainder tuned to
        # the measured 22.9s Kokoro length (22.9 - 2.95 - 8.2 = 11.75)
        self.wait(11.75)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: 2 honest-limit cards, side by side, full weight.
# [Source: FACTCHECK.md #5, #6]
# measured audio: 23.38s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two honest limits.", color=PALETTE["bg"], font_size=34, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.3)

        def limit_card(heading, lines, color):
            head = fit(T(heading, color=color, font_size=21, weight="BOLD"), 5.4)
            body = VGroup(*[
                fit(T(l, color=PALETTE["bg"], font_size=17, line_spacing=1.2), 5.4) for l in lines
            ]).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content = VGroup(head, body).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            bg = panel(width=5.8, height=content.height + 0.6, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        card1 = limit_card(
            "1. Caught by code review,\nnot a live incident",
            ["No evidence this exact case", "ever occurred on a real run —", "this pipeline isn't", "instrumented at that", "granularity."],
            PALETTE["gold"],
        )
        card2 = limit_card(
            "2. A related gap,\nflagged, not fixed",
            ["A downstream service's", "source list doesn't yet", "cover a newer classification", "— flagged for a future", "week, not resolved yet."],
            PALETTE["crimson"],
        )
        cards = VGroup(card1, card2).arrange(RIGHT, buff=0.5)
        cards.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        divider = Line(LEFT * 3.0, RIGHT * 3.0, color=PALETTE["gold"], stroke_width=2.5)
        divider.next_to(cards, DOWN, buff=0.35)
        closing = fit(T("Full weight. Neither one softened.", color=PALETTE["gold"], font_size=22, weight="BOLD"), 11.5)
        closing.next_to(divider, DOWN, buff=0.3)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.5+0.5+0.3+0.4 = 2.2s
        # waits above = 1.3+2.0+2.0 = 5.3s; remainder tuned to the measured
        # 23.38s Kokoro length (23.38 - 2.2 - 5.3 = 15.88)
        self.wait(15.88)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 10.03s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "An alert system is only as good as",
            "the cases it was actually built to handle.",
        ]
        line2 = [
            "The scariest bugs aren't the ones that crash —",
            "they're the ones that quietly do nothing at all.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34), 11.8) for l in lines
        ]).arrange(DOWN, buff=0.3)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["gold"], font_size=34, weight="BOLD"), 11.8) for l in line2
        ]).arrange(DOWN, buff=0.3)

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
        self.wait(2.0)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 2.0s; remainder
        # tuned to the measured 10.03s Kokoro length (10.03 - 1.7 - 2.0 = 6.33)
        self.wait(6.33)


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
