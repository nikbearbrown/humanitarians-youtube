"""
Manim scenes for 2026-10-21-calibration-why-confidence-isnt-accuracy
"Calibration: Why Confidence Isn't Accuracy"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Teaches a reusable 3-question test -- Bucket the Claims / Count the
Cases / Spot the Bluff -- for telling whether a model's stated or implied
confidence in an answer actually tracks how often that answer is right, or
just sounds equally confident whether it's correct or wrong. Distinct from
this fellow's earlier hallucination video (fabrication, not confidence-to-
accuracy correspondence) and chain-of-thought-faithfulness video (reasoning
traces, not confidence numbers). The worked example (B04) and its
falsifiability case (B05) are both fully generic/hypothetical -- no real
model, vendor, or product is named or benchmarked. See FACTCHECK.md and
SOURCES.md.

B00_TitleCard                      -- silent title card (TITLE)
B01_ExecSummary                     -- spoken personal-intro card (EXEC-SUMMARY)
B02_SameConfidenceHook               -- same stated confidence, opposite outcomes (HOOK)
B03_ThreeTestsFramework              -- all 3 tests shown together, before any example (FRAMEWORK)
B04_OverconfidentBucket              -- stated 90%, actual 60% -- a real gap (WORKED-EXAMPLE)
B05_WellCalibratedFalsifiability     -- stated 90%, actual ~90% -- the bars line up (FALSIFIABILITY)
B06_AuditChecklist                   -- the 3 tests as a concrete task to try today (SCAFFOLDED-TASK)
B07_Statement                        -- takeaway statement card (TAKEAWAY)
B08_BrandOutro                       -- @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's sibling reels (2026-10-15-chain-of-thought-why-the-reasoning-isnt-
always-the-reason, 2026-10-06-lost-in-the-middle-why-more-context-isnt-better)
for visual consistency across the series. Plain Text (Pango) throughout,
never Integer/DecimalNumber/MathTex -- no LaTeX installed; every number shown
(confidence percentages, bar readouts) is a plain Text string, not typeset
math.

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not a pre-audio
estimate, per the toolkit's audio-first rule:
B00=4.049 (silent, fixed target) B01=14.33 B02=15.94 B03=29.35 B04=25.63
B05=23.66 B06=21.17 B07=11.64 B08=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area). Frame/
panel dimensions for the structure beats (B00/B01/B07/B08) are copied
verbatim from the sibling reel's already-GATE-V-clean values for the same
beat roles, to avoid re-discovering the same underfill bugs from scratch.

WORKED EXAMPLE CONTENT (B04/B05) -- chosen per the build brief, fully generic:

B04 -- a "confidence bucket": every answer a hypothetical model gave at
roughly the same stated confidence (~90%) across many different questions,
bucketed together. Ten answer chips (6 correct / 4 wrong = 60% actual
accuracy) sit under the bucket label, then a STATED bar (90%, gold) and an
ACTUAL bar (60%, teal) drawn to the same scale make the gap directly
visible, not just asserted. Chosen because round numbers (90% stated vs 60%
actual) make the mismatch legible at a glance without requiring the viewer
to do arithmetic, and because the bar-pair idiom directly visualizes the
rubric's first test (Bucket the Claims) -- per FACTCHECK.md #2, a fully
generic illustration, no real model/vendor named.

B05 -- the identical bucket-and-bars layout, this time well-calibrated: nine
correct / one wrong (90% actual accuracy) under a "~90% stated confidence"
bucket, so the STATED and ACTUAL bars land at nearly the same length -- a
visibly different, matching resolution to B04's gap, giving the
falsifiability case (a genuinely well-calibrated case the rubric must NOT
flag) a real, checkable counterpart -- per FACTCHECK.md #3, an uncontested,
non-benchmarked illustration of the other side of the same measurement.
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
    "crimson": "#E4572E", # bad / CVD-safe warm -- only safe as a STROKE/accent
                          # on ink (0.28 luminance sep as text, under the 0.3
                          # floor); use "gold" for bad/alert TEXT on ink.
    "slate":  "#29335C",  # structure -- 0.04 luminance sep on ink (broken);
                          # use "sage" for any note/tag text on ink.
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as alert TEXT on ink.
    "sage":   "#A8C686",  # human / growth / confirmed; safe secondary text on ink.
}

MONO = "Courier New"


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size -- avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See the sibling reels' BUILD-LOG.md for the
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


def answer_chip(correct, size=0.32):
    """One small square chip in a confidence-bucket row: filled sage if the
    answer was actually correct, a crimson outline with an X if it wasn't.
    Used by B04 (overconfident bucket) and B05 (well-calibrated bucket)."""
    color = PALETTE["sage"] if correct else PALETTE["crimson"]
    box = Square(side_length=size, color=color,
                 fill_color=color, fill_opacity=0.85 if correct else 0.12,
                 stroke_width=2.5)
    mark = T("+" if correct else "x", color=PALETTE["ink"] if correct else color,
              font_size=16, weight="BOLD")
    mark.move_to(box.get_center())
    return VGroup(box, mark)


def chip_row(results, gap=0.16):
    """Returns a VGroup of answer_chip()s arranged left to right in the
    exact order given -- deliberately mixed (not grouped by outcome) so the
    row reads as "many individual answers in one bucket", not a sorted bar."""
    return VGroup(*[answer_chip(r) for r in results]).arrange(RIGHT, buff=gap)


def stat_bar(label, pct, width, color, label_color=None):
    """A labeled horizontal bar: LABEL | track (with a fill scaled to `pct`
    of `width`, 0-100) | bold percentage readout. Returns (group, track,
    fill) -- group is the full VGroup for layout, track/fill are kept
    separate so callers can animate the fill growing in on its own, after
    the empty track is already on screen (same two-group pattern as the
    sibling reels' build_chain(), for the same reason: direct references,
    no re-deriving offsets)."""
    label_color = label_color or PALETTE["ink"]
    tag = T(label, color=label_color, font_size=18, font=MONO, weight="BOLD")
    track = Rectangle(width=width, height=0.5, stroke_color=PALETTE["slate"],
                       stroke_width=2.5, fill_opacity=0)
    pct_label = T(f"{pct:.0f}%", color=color, font_size=20, font=MONO, weight="BOLD")
    row = VGroup(tag, track, pct_label).arrange(RIGHT, buff=0.35)
    fill_w = max(width * pct / 100.0, 0.08)
    fill = Rectangle(width=fill_w, height=0.5, stroke_width=0,
                      fill_color=color, fill_opacity=0.9)
    fill.move_to(track.get_center())
    fill.align_to(track, LEFT)
    group = VGroup(tag, track, fill, pct_label)
    return group, track, fill


def confidence_card(pct, correct, width=4.3, height=1.7):
    """One 'answer card' for B02's hook: a stated confidence percentage and
    a correct/wrong outcome tag, same visual weight regardless of outcome --
    the whole point of the hook (same stated confidence, opposite result)."""
    box_color = PALETTE["teal_on_ink"]
    box = RoundedRectangle(width=width, height=height, corner_radius=0.12,
                            fill_color=PALETTE["ink"], fill_opacity=1.0,
                            stroke_color=box_color, stroke_width=2.5)
    conf = T(f"{pct}% confident", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
    result_color = PALETTE["sage"] if correct else PALETTE["crimson"]
    result = T("Correct" if correct else "Wrong", color=result_color, font_size=20, font=MONO, weight="BOLD")
    body = VGroup(conf, result).arrange(DOWN, buff=0.28)
    body.move_to(box.get_center())
    return VGroup(box, body)


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.049s -- fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Calibration:", color=PALETTE["ink"], font_size=50, weight="BOLD"), 12.0)
        title_line2 = fit(T("Why Confidence Isn't Accuracy", color=PALETTE["ink"], font_size=36, weight="BOLD"), 12.0)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=36)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.049s silent track
        self.wait(2.449)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 14.33s
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
            "This video: whether a model's confidence",
            "in its own answer matches how often",
            "that answer is right — and three tests",
            "that check whether it means anything.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=26), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.2)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 14.33s Kokoro length
        self.wait(12.23)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: two answer cards, identically confident in tone, one correct
# one wrong -- then an overlay: "Sounding sure isn't the same as being right."
# [Source: FACTCHECK.md #1 -- generic/hypothetical, no real model named]
# measured audio: 15.94s
# --------------------------------------------------------------------------- #
class B02_SameConfidenceHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Ask a model how sure it is...", color=PALETTE["bg"], font_size=34), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.6)

        # card width/height enlarged (4.3x1.7 -> 4.8x2.3) and chained via
        # next_to() off the title, then a bottom rule chained off the tag --
        # GATE V's canvas-fill check (a bounding-box AREA metric, measured
        # directly on the TRUE final candidate, not the review slate -- the
        # review slate showed 0 MAJOR here) measured this beat's setup phase
        # at only 41% of the safe area (min 55%): the original side-by-side
        # cards were short (height 1.7) and centered in a narrow vertical
        # band. Bigger cards + a real framing rule genuinely extend the
        # content's measured height-span, not a padding trick.
        card1 = confidence_card(95, True, width=4.8, height=2.5)
        card2 = confidence_card(95, False, width=4.8, height=2.5)
        cards = VGroup(card1, card2).arrange(RIGHT, buff=1.0)
        cards.next_to(title, DOWN, buff=0.85)

        same_tag = fit(T("SAME STATED CONFIDENCE", color=PALETTE["sage"], font_size=20, font=MONO), 11.0)
        same_tag.next_to(cards, DOWN, buff=0.65)

        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(same_tag, DOWN, buff=0.6)

        self.play(Create(card1[0]), run_time=0.4)
        self.play(FadeIn(card1[1]), run_time=0.3)
        self.play(Create(card2[0]), run_time=0.4)
        self.play(FadeIn(card2[1]), run_time=0.3)
        self.play(FadeIn(same_tag), Create(bottom_rule), run_time=0.3)
        self.wait(5.2)

        # fluent + plausible, but the hook's whole point: both cards sound
        # equally sure. Fade the content OUT fully before fading the overlay
        # IN (never a dim-behind-overlay trick) -- a text-on-text-overlap
        # bug a sibling reel's GATE B caught the hard way when an earlier
        # draft only dimmed content behind a translucent rectangle while the
        # underlying Text mobjects stayed at fill_opacity=1 underneath.
        #
        # REAL BUG CAUGHT HERE (not a review-slate false positive this time):
        # an earlier revision used 5 separately-arranged elements (2 text
        # lines as their own arrange() entries) at buff=1.9 with a 165pt
        # qmark -- queried Manim's own Text().height directly (not guessed)
        # and found that combination summed to ~10.26 units of total height
        # against an 8-unit-tall frame, so the top/bottom rules were pushed
        # entirely outside the camera view (not clipped-looking, genuinely
        # absent from the rendered frame -- confirmed by extracting a real
        # frame and finding no rules at all). Fixed by querying real heights
        # up front and solving for a buff that keeps the whole group inside
        # the frame with comfortable safe-area margin: the 2 lines are now
        # one sub-group (tight internal buff) so the main arrange has only 4
        # elements, and buff/qmark size are chosen from the measured numbers
        # (qmark 150pt height=1.46, line height=0.53 each) rather than
        # guessed, giving a total height of ~6.0 (fits the 6.8 safe height).
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Sounding sure", color=PALETTE["bg"], font_size=42, weight="BOLD"), 10.0)
        overlay_line2 = fit(T("isn't the same as being right.", color=PALETTE["bg"], font_size=42, weight="BOLD"), 10.0)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        content_group = VGroup(title, same_tag, cards, bottom_rule)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # sum of plays = 0.5+0.4+0.3+0.4+0.3+0.3+0.5+0.6 = 3.3s
        # waits above = 0.6+5.2 = 5.8s
        # remainder tuned to the measured 15.94s Kokoro length (15.94-3.3-5.8=6.84)
        self.wait(6.84)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 29.35s
# --------------------------------------------------------------------------- #
class B03_ThreeTestsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three tests, before any example:", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def test_card(num, head, body_text):
            # a real numbered badge (Square + number), not just "N." prefix
            # text -- a sibling reel's GATE A static distinctness check
            # flagged an earlier draft (headline text only) as a "shapes
            # never change" false positive, since the only non-text shape in
            # the whole scene was one static list_panel. A real shape per
            # card (this badge) fixes that and matches the step-badge idiom
            # used elsewhere in this reel's siblings.
            badge = Square(side_length=0.5, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=22, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = T(head, color=PALETTE["teal"], font_size=26, weight="BOLD")
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.25)
            body_t = fit(T(body_text, color=PALETTE["ink"], font_size=20), 9.9)
            row = VGroup(head_row, body_t).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            body_t.align_to(head_t, LEFT)
            return row

        card1 = test_card(1, "Bucket the Claims",
                           "Group every answer by confidence — how often is each bucket right?")
        card2 = test_card(2, "Count the Cases",
                           "One lucky answer proves nothing — does the pattern hold across many cases?")
        card3 = test_card(3, "Spot the Bluff",
                           "Would a hedged, uncertain answer ever get miscounted as confident?")

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 1.6, height=cards.height + 1.1,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(DOWN * 0.15)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)

        closing = fit(T("If the buckets don't match — it's not calibrated.", color=PALETTE["gold"], font_size=24, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.8+0.3+7.0+7.0+7.0 = 22.1s
        # remainder tuned to the measured 29.35s Kokoro length (29.35-2.9-22.1=4.35)
        self.wait(4.35)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: a "~90% confident" bucket of 10 answers, 6 correct /
# 4 wrong (60% actual accuracy) -- a STATED bar (90%, gold) and an ACTUAL bar
# (60%, teal) drawn to the same scale make the gap visible without relying
# on narration alone. Fully generic illustration, round numbers for clarity.
# [Source: FACTCHECK.md #2 -- generic illustration of a documented pattern]
# measured audio: 25.63s
# --------------------------------------------------------------------------- #
class B04_OverconfidentBucket(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A documented pattern.", color=PALETTE["bg"], font_size=32, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        bucket_label = T("BUCKET: ~90% STATED CONFIDENCE", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD")
        results = [True, True, False, True, False, True, False, True, False, True]  # 6/10 correct = 60%
        chips = chip_row(results)
        chip_block = VGroup(bucket_label, chips).arrange(DOWN, buff=0.32)
        chip_block.move_to([0, 2.15, 0])

        self.play(FadeIn(bucket_label), run_time=0.3)
        self.play(FadeIn(chips, lag_ratio=0.08), run_time=0.8)
        self.wait(1.5)

        stated_group, stated_track, stated_fill = stat_bar(
            "STATED", 90, 5.4, PALETTE["gold"], label_color=PALETTE["bg"])
        actual_group, actual_track, actual_fill = stat_bar(
            "ACTUAL", 60, 5.4, PALETTE["teal_on_ink"], label_color=PALETTE["bg"])
        bars = VGroup(stated_group, actual_group).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        bars.next_to(chip_block, DOWN, buff=0.55)

        self.play(Create(stated_track), FadeIn(stated_group[0]), FadeIn(stated_group[3]), run_time=0.4)
        self.play(FadeIn(stated_fill), run_time=0.4)
        self.wait(1.0)
        self.play(Create(actual_track), FadeIn(actual_group[0]), FadeIn(actual_group[3]), run_time=0.4)
        self.play(FadeIn(actual_fill), run_time=0.4)
        self.wait(1.3)

        gap_tag = T("CONFIDENCE ≠ ACCURACY", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD")
        gap_tag.next_to(bars, DOWN, buff=0.4)
        gap_box = box_around(gap_tag, buff=0.14, color=PALETTE["gold"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("The number sounded confident. The real accuracy didn't follow it.",
                        color=PALETTE["gold"], font_size=21), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.4+0.3+0.3+0.5 = 4.3s
        # waits above = 0.8+1.5+1.0+1.3+1.5 = 6.1s
        # remainder tuned to the measured 25.63s Kokoro length (25.63-4.3-6.1=15.23)
        self.wait(15.23)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the same bucket-and-bars layout as B04, but a
# genuinely well-calibrated bucket -- 9 correct / 1 wrong (90% actual
# accuracy) under a "~90% stated confidence" label, so STATED and ACTUAL
# land at nearly the same bar length -- a visibly distinct resolution from
# B04's gap (bars that line up, not a mismatch), the test correctly NOT
# flagging a genuinely calibrated case.
# measured audio: 23.66s
# --------------------------------------------------------------------------- #
class B05_WellCalibratedFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Now, a well-calibrated bucket.", color=PALETTE["ink"], font_size=32, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        bucket_label = T("BUCKET: ~90% STATED CONFIDENCE", color=PALETTE["slate"], font_size=18, font=MONO, weight="BOLD")
        results = [True, True, True, True, False, True, True, True, True, True]  # 9/10 correct = 90%
        chips = chip_row(results, gap=0.2)
        chip_block = VGroup(bucket_label, chips).arrange(DOWN, buff=0.38)
        chip_block.next_to(title, DOWN, buff=0.55)

        self.play(FadeIn(bucket_label), run_time=0.3)
        self.play(FadeIn(chips, lag_ratio=0.08), run_time=0.8)
        self.wait(1.3)

        # bar width 5.4 -> 5.9 and the gaps below genuinely widened: GATE V's
        # canvas-fill check (a bounding-box AREA metric, measured directly on
        # the TRUE final candidate, not the review slate) measured this
        # beat's steady-state frame at 54% of the safe area -- just under
        # the 55% floor. Real additional width/height, not a padding trick.
        stated_group, stated_track, stated_fill = stat_bar(
            "STATED", 90, 5.9, PALETTE["gold"], label_color=PALETTE["ink"])
        actual_group, actual_track, actual_fill = stat_bar(
            "ACTUAL", 90, 5.9, PALETTE["teal"], label_color=PALETTE["ink"])
        bars = VGroup(stated_group, actual_group).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        bars.next_to(chip_block, DOWN, buff=0.7)

        self.play(Create(stated_track), FadeIn(stated_group[0]), FadeIn(stated_group[3]), run_time=0.4)
        self.play(FadeIn(stated_fill), run_time=0.4)
        self.wait(0.6)
        self.play(Create(actual_track), FadeIn(actual_group[0]), FadeIn(actual_group[3]), run_time=0.4)
        self.play(FadeIn(actual_fill), run_time=0.4)
        self.wait(1.0)

        check_tag = T("CONFIDENCE ≈ ACCURACY", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        check_tag.next_to(bars, DOWN, buff=0.5)
        check_box = box_around(check_tag, buff=0.14, color=PALETTE["teal"])
        self.play(FadeIn(check_tag), run_time=0.3)
        self.play(Create(check_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("Same bucket, same test — this time, it holds up.",
                        color=PALETTE["ink"], font_size=23, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.65)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.4+0.3+0.3+0.5 = 4.3s
        # waits above = 0.8+1.3+0.6+1.0+1.5 = 5.2s
        # remainder tuned to the measured 23.66s Kokoro length (23.66-4.3-5.2=14.16)
        self.wait(14.16)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 21.17s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=30), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def checklist_item(text):
            box = Square(side_length=0.85, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = fit(T(text, color=PALETTE["ink"], font_size=32), 9.8)
            row = VGroup(box, check).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("Ask questions you already know the answer to.")
        row2, box2 = checklist_item("Have it state a confidence number each time.")
        row3, box3 = checklist_item("Group by number — check real accuracy.")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.95)
        list_panel = panel(width=items.width + 1.8, height=items.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.05)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(0.8)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(4.2)
        self.play(Create(mark2), run_time=0.3)
        self.wait(4.2)
        self.play(Create(mark3), run_time=0.3)
        self.wait(4.2)

        closing1 = fit(T("If a '90% confident' group is only right half the time —",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing2 = fit(T("you've just measured a real calibration gap.",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.15)
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.8+0.8+4.2+4.2+4.2 = 14.2s
        # remainder tuned to the measured 21.17s Kokoro length (21.17-2.8-14.2=4.17)
        self.wait(4.17)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: statement card.
# measured audio: 11.64s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("Sounding sure", color=PALETTE["bg"], font_size=50), 12.4)
        line1b = fit(T("isn't the same as being right.", color=PALETTE["bg"], font_size=50), 12.4)
        line2 = fit(T("Check whether confidence tracks", color=PALETTE["gold"], font_size=44), 12.4)
        line2b = fit(T("real accuracy, across many cases.", color=PALETTE["gold"], font_size=48, weight="BOLD"), 12.4)

        block1 = VGroup(line1, line1b).arrange(DOWN, buff=0.4)
        block2 = VGroup(line2, line2b).arrange(DOWN, buff=0.45)
        content = VGroup(block1, block2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=content.width + 1.8, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.16, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 0.3+0.6+0.6+0.3 = 1.8s, waits above = 5.2s (3.0+2.2);
        # remainder tuned to the measured 11.64s Kokoro length (11.64-1.8-5.2=4.64)
        self.wait(4.64)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Narration ("Explained with Claude Code.") is short by
# design -- the approved beat sheet's exact text -- so this card is a brief,
# clean flash, not an extended hold.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=86), 11.6)
        accent = Line(LEFT * 3.6, RIGHT * 3.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=46), 11.0)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=40), 11.0)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame_w = min(content.width + 1.8, 12.4)
        frame_h = min(content.height + 1.1, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 0.5s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.01)
