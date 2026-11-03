"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-21-calibration-why-confidence-isnt-accuracy
"Calibration: Why Confidence Isn't Accuracy"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command -- NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard. All 9 parent
beats are kept; every mp3 is reused byte-for-byte from the parent's mp3/
folder. Every beat here is a Manim GRAPHIC beat, so each class below is a
genuine portrait RE-LAYOUT of the parent ../scenes.py composition, authored
by hand for a narrow portrait canvas (rendered at 2160x3840 for the true 4K
vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's y-axis safe/hard bounds carry over unchanged; only
frame_width shrinks (~4.5 instead of 14.222). MAX_W = 3.4 is this file's
general content-width budget, copied from this fellow's sibling reels' own
portrait-redesign convention (2026-10-15-chain-of-thought-why-the-reasoning-
isnt-always-the-reason/vertical/scenes.py,
2026-10-06-lost-in-the-middle-why-more-context-isnt-better/vertical/scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard                       -- title re-wrapped onto 3 narrower lines.
  B01 ExecSummary                      -- badge stacked ABOVE name/role; summary re-wrapped (6 lines).
  B02 SameConfidenceHook                -- parent's SIDE-BY-SIDE cards -> TOP/BOTTOM stack.
  B03 ThreeTestsFramework                -- already single-column; each card's body re-wrapped onto 2 lines.
  B04 OverconfidentBucket                 -- 10-chip single row -> 2 rows of 5; bars narrowed to MAX_W.
  B05 WellCalibratedFalsifiability         -- same 2-row chip grid + narrowed bars as B04.
  B06 AuditChecklist                       -- already single-column; items re-wrapped narrower.
  B07 Statement                            -- centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                           -- unchanged composition; widths trimmed.

Every element within a beat is positioned by chaining `next_to()` off the
block above it (never hand-picked absolute y-coordinates) -- a sibling
reel's BUILD-LOG documents real title/content collisions from absolute
coordinates not accounting for how real rendered heights combine once a
layout is redesigned for a narrow canvas; chaining avoids that class of bug
by construction.

Palette/MONO/fit()/T()/panel()/box_around()/answer_chip()/stat_bar()/
confidence_card() are copied from ../scenes.py for visual continuity.
Nothing about WHAT is said or WHEN changes here -- every self.play/self.wait
duration matches ../scenes.py beat-for-beat, so total runtime matches the
landscape master exactly -- only how it is laid out for the narrow canvas.
"""

from manim import *
import numpy as np

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup -- BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait -- every
# coordinate in this file is designed against a ~4.5-wide frame, so without
# this fix everything would render far too small and clustered dead-center.
# Copied verbatim from this fellow's sibling reels' vertical/scenes.py, which
# found and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- safe as a STROKE/accent on
                          # ink; avoid as TEXT color on ink (0.28 sep).
    "slate":  "#29335C",  # structure -- 0.04 luminance sep on ink (broken);
                          # use "sage" for any note/tag text on ink.
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as alert TEXT on ink.
    "sage":   "#A8C686",  # human / growth / confirmed; safe secondary text on ink.
}

MONO = "Courier New"
MAX_W = 3.4   # general portrait content-width budget (safe half-width ~1.95)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size -- avoids a real Pango/Cairo small-font-size artifact
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


def answer_chip(correct, size=0.26):
    """Portrait version uses a smaller default chip size than the landscape
    original so a 2-row grid fits the narrow canvas's real width budget."""
    color = PALETTE["sage"] if correct else PALETTE["crimson"]
    box = Square(side_length=size, color=color,
                 fill_color=color, fill_opacity=0.85 if correct else 0.12,
                 stroke_width=2.2)
    mark = T("+" if correct else "x", color=PALETTE["ink"] if correct else color,
              font_size=13, weight="BOLD")
    mark.move_to(box.get_center())
    return VGroup(box, mark)


def chip_grid(results, per_row=5, gap=0.14, row_buff=0.18):
    """Portrait redesign of ../scenes.py's chip_row(): the same 10 answer
    chips, wrapped into 2 rows of `per_row` instead of 1 long row, so the
    whole bucket fits MAX_W. Row order preserved left-to-right, top-to-
    bottom, same mixed (not sorted) order as the landscape version."""
    rows = []
    for i in range(0, len(results), per_row):
        chunk = results[i:i + per_row]
        row = VGroup(*[answer_chip(r) for r in chunk]).arrange(RIGHT, buff=gap)
        rows.append(row)
    return VGroup(*rows).arrange(DOWN, buff=row_buff)


def stat_bar(label, pct, width, color, label_color=None):
    """Portrait version -- see ../scenes.py for the rationale (two separate
    references, track/fill, so callers can animate the fill growing in on
    its own). Narrower `width` and smaller fonts for the MAX_W budget.

    width=2.0/font 13+14/buff 0.14 (not the first-guess 2.5/15+16/0.2):
    the real pixel-true portrait layout auditor (--portrait) measured the
    first version's full row at half-width 1.99, just over the ±1.95 safe
    half-width -- queried Manim's own Text/Rectangle widths directly (not
    guessed a second time) before picking these numbers, which land at
    half-width ~1.62, comfortably inside the safe band."""
    label_color = label_color or PALETTE["ink"]
    tag = T(label, color=label_color, font_size=13, font=MONO, weight="BOLD")
    track = Rectangle(width=width, height=0.4, stroke_color=PALETTE["slate"],
                       stroke_width=2.2, fill_opacity=0)
    pct_label = T(f"{pct:.0f}%", color=color, font_size=14, font=MONO, weight="BOLD")
    row = VGroup(tag, track, pct_label).arrange(RIGHT, buff=0.14)
    fill_w = max(width * pct / 100.0, 0.06)
    fill = Rectangle(width=fill_w, height=0.4, stroke_width=0,
                      fill_color=color, fill_opacity=0.9)
    fill.move_to(track.get_center())
    fill.align_to(track, LEFT)
    group = VGroup(tag, track, fill, pct_label)
    return group, track, fill


def confidence_card(pct, correct, width=3.2, height=1.5):
    """Portrait version of ../scenes.py's confidence_card() -- narrower,
    stacked TOP/BOTTOM instead of side by side (see B02 below). width/height
    enlarged (3.1x1.35 -> 3.2x1.5) as part of B02's canvas-fill fix (queried
    real Manim dimensions -- see B02's own comment)."""
    box_color = PALETTE["teal_on_ink"]
    box = RoundedRectangle(width=width, height=height, corner_radius=0.1,
                            fill_color=PALETTE["ink"], fill_opacity=1.0,
                            stroke_color=box_color, stroke_width=2.2)
    conf = T(f"{pct}% confident", color=PALETTE["gold"], font_size=19, font=MONO, weight="BOLD")
    result_color = PALETTE["sage"] if correct else PALETTE["crimson"]
    result = T("Correct" if correct else "Wrong", color=result_color, font_size=18, font=MONO, weight="BOLD")
    body = VGroup(conf, result).arrange(DOWN, buff=0.22)
    body.move_to(box.get_center())
    return VGroup(box, body)


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, re-wrapped onto 3 narrower lines.
# measured (silent) duration: 4.049s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Calibration:", "Why Confidence", "Isn't Accuracy"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.24)

        top_rule = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=24), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=6.6, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.449)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 14.33s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.48, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=17), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.22)

        summary_lines = [
            "This video: whether a",
            "model's confidence in its",
            "own answer matches how",
            "often that answer is right —",
            "and three tests that check",
            "whether it means anything.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.42).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=7.1, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(12.23)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: parent's SIDE-BY-SIDE confidence cards -> TOP/BOTTOM stack.
# measured audio: 15.94s
# --------------------------------------------------------------------------- #
class B02_SameConfidenceHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Ask a model how sure", color=PALETTE["bg"], font_size=22), MAX_W)
        title2 = fit(T("it is...", color=PALETTE["bg"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.1)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.6)

        # card size/buffs enlarged, a bottom rule added: GATE V's canvas-fill
        # check (measured on the TRUE final candidate) found this setup
        # phase at 49% of the safe area (min 55%) -- queried Manim's own
        # real widths/heights for this exact composition (title+cards+tag+
        # rule) and confirmed the new numbers clear the floor (area ~66%)
        # and stay well inside the safe band before re-rendering.
        card1 = confidence_card(95, True)
        card2 = confidence_card(95, False)
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.45)
        cards.next_to(title_block, DOWN, buff=0.55)

        same_tag = T("SAME STATED CONFIDENCE", color=PALETTE["sage"], font_size=14, font=MONO)
        same_tag = fit(same_tag, MAX_W)
        same_tag.next_to(cards, DOWN, buff=0.4)

        setup_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        setup_rule.next_to(same_tag, DOWN, buff=0.4)

        self.play(Create(card1[0]), run_time=0.4)
        self.play(FadeIn(card1[1]), run_time=0.3)
        self.play(Create(card2[0]), run_time=0.4)
        self.play(FadeIn(card2[1]), run_time=0.3)
        self.play(FadeIn(same_tag), Create(setup_rule), run_time=0.3)
        self.wait(5.2)

        qmark = T("?", color=PALETTE["gold"], font_size=110, weight="BOLD")
        overlay_line1 = fit(T("Sounding sure", color=PALETTE["bg"], font_size=32, weight="BOLD"), MAX_W)
        overlay_line2 = fit(T("isn't the same", color=PALETTE["bg"], font_size=32, weight="BOLD"), MAX_W)
        overlay_line3 = fit(T("as being right.", color=PALETTE["bg"], font_size=32, weight="BOLD"), MAX_W)
        overlay_text = VGroup(overlay_line1, overlay_line2, overlay_line3).arrange(DOWN, buff=0.14)
        top_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        # buff=1.2: the analogous sibling-reel GATE V canvas-fill fix (a
        # bounding-box AREA metric) needed genuine vertical spacing, not just
        # wide rules, to clear the 55% floor -- reusing that already-verified
        # magnitude here rather than re-discovering it from scratch.
        overlay = VGroup(top_rule, qmark, overlay_text, bottom_rule).arrange(DOWN, buff=1.2).move_to(ORIGIN)

        content_group = VGroup(title_block, same_tag, cards, setup_rule)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        self.wait(6.84)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: already single-column; each card's body re-wrapped onto
# 2 narrower lines.
# measured audio: 29.35s
# --------------------------------------------------------------------------- #
class B03_ThreeTestsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three tests, before", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title2 = fit(T("any example:", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.8)

        def test_card(num, head, body_lines):
            badge = Square(side_length=0.4, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=18, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = fit(T(head, color=PALETTE["teal"], font_size=20, weight="BOLD"), MAX_W - 0.5)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.2)
            body_rows = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=15), MAX_W) for l in body_lines
            ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            row = VGroup(head_row, body_rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            body_rows.align_to(head_row, LEFT)
            return row

        card1 = test_card(1, "Bucket the Claims",
                           ["Group every answer by confidence —", "how often is each bucket right?"])
        card2 = test_card(2, "Count the Cases",
                           ["One lucky answer proves nothing —", "does it hold across many cases?"])
        card3 = test_card(3, "Spot the Bluff",
                           ["Would a hedged, uncertain answer", "ever get miscounted as confident?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 0.6, height=cards.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.next_to(title_block, DOWN, buff=0.4)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(7.0)

        closing1 = fit(T("If the buckets don't match —", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing2 = fit(T("it's not calibrated.", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        self.play(Write(closing), run_time=0.5)
        self.wait(4.35)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: 10-chip single row -> 2 rows of 5; bars narrowed to
# the MAX_W budget.
# measured audio: 25.63s
# --------------------------------------------------------------------------- #
class B04_OverconfidentBucket(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A documented pattern.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        bucket_label = fit(T("BUCKET: ~90% STATED", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        bucket_label2 = fit(T("CONFIDENCE", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        bucket_label_block = VGroup(bucket_label, bucket_label2).arrange(DOWN, buff=0.05)
        bucket_label_block.next_to(title, DOWN, buff=0.35)

        results = [True, True, False, True, False, True, False, True, False, True]  # 6/10 correct = 60%
        chips = chip_grid(results, per_row=5)
        chips.next_to(bucket_label_block, DOWN, buff=0.3)

        self.play(FadeIn(bucket_label_block), run_time=0.3)
        self.play(FadeIn(chips, lag_ratio=0.08), run_time=0.8)
        self.wait(1.5)

        stated_group, stated_track, stated_fill = stat_bar(
            "STATED", 90, 2.0, PALETTE["gold"], label_color=PALETTE["bg"])
        actual_group, actual_track, actual_fill = stat_bar(
            "ACTUAL", 60, 2.0, PALETTE["teal_on_ink"], label_color=PALETTE["bg"])
        bars = VGroup(stated_group, actual_group).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        bars.next_to(chips, DOWN, buff=0.45)

        self.play(Create(stated_track), FadeIn(stated_group[0]), FadeIn(stated_group[3]), run_time=0.4)
        self.play(FadeIn(stated_fill), run_time=0.4)
        self.wait(1.0)
        self.play(Create(actual_track), FadeIn(actual_group[0]), FadeIn(actual_group[3]), run_time=0.4)
        self.play(FadeIn(actual_fill), run_time=0.4)
        self.wait(1.3)

        gap_tag = fit(T("CONFIDENCE ≠ ACCURACY", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD"), MAX_W)
        gap_tag.next_to(bars, DOWN, buff=0.35)
        gap_box = box_around(gap_tag, buff=0.12, color=PALETTE["gold"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing1 = fit(T("The number sounded confident.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing2 = fit(T("The accuracy didn't follow.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        self.play(Write(closing), run_time=0.5)
        self.wait(15.23)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: same 2-row chip grid + narrowed bars as B04.
# measured audio: 23.66s
# --------------------------------------------------------------------------- #
class B05_WellCalibratedFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Now, a well-calibrated", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title2 = fit(T("bucket.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.7)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.8)

        bucket_label = fit(T("BUCKET: ~90% STATED", color=PALETTE["slate"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        bucket_label2 = fit(T("CONFIDENCE", color=PALETTE["slate"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        bucket_label_block = VGroup(bucket_label, bucket_label2).arrange(DOWN, buff=0.05)
        bucket_label_block.next_to(title_block, DOWN, buff=0.35)

        results = [True, True, True, True, False, True, True, True, True, True]  # 9/10 correct = 90%
        chips = chip_grid(results, per_row=5)
        chips.next_to(bucket_label_block, DOWN, buff=0.3)

        self.play(FadeIn(bucket_label_block), run_time=0.3)
        self.play(FadeIn(chips, lag_ratio=0.08), run_time=0.8)
        self.wait(1.3)

        stated_group, stated_track, stated_fill = stat_bar(
            "STATED", 90, 2.0, PALETTE["gold"], label_color=PALETTE["ink"])
        actual_group, actual_track, actual_fill = stat_bar(
            "ACTUAL", 90, 2.0, PALETTE["teal"], label_color=PALETTE["ink"])
        bars = VGroup(stated_group, actual_group).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        bars.next_to(chips, DOWN, buff=0.45)

        self.play(Create(stated_track), FadeIn(stated_group[0]), FadeIn(stated_group[3]), run_time=0.4)
        self.play(FadeIn(stated_fill), run_time=0.4)
        self.wait(0.6)
        self.play(Create(actual_track), FadeIn(actual_group[0]), FadeIn(actual_group[3]), run_time=0.4)
        self.play(FadeIn(actual_fill), run_time=0.4)
        self.wait(1.0)

        check_tag = fit(T("CONFIDENCE ≈ ACCURACY", color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD"), MAX_W)
        check_tag.next_to(bars, DOWN, buff=0.35)
        check_box = box_around(check_tag, buff=0.12, color=PALETTE["teal"])
        self.play(FadeIn(check_tag), run_time=0.3)
        self.play(Create(check_box), run_time=0.3)
        self.wait(1.5)

        closing1 = fit(T("Same bucket, same test —", color=PALETTE["ink"], font_size=18, weight="BOLD"), MAX_W)
        closing2 = fit(T("this time, it holds up.", color=PALETTE["ink"], font_size=18, weight="BOLD"), MAX_W)
        closing = VGroup(closing1, closing2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.7)
        self.play(Write(closing), run_time=0.5)
        self.wait(14.16)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 21.17s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def checklist_item(lines):
            box = Square(side_length=0.6, color=PALETTE["teal"], stroke_width=3.5, fill_opacity=0)
            check = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W - 0.9) for l in lines
            ]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(box, check).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item(["Ask questions you already", "know the answer to."])
        row2, box2 = checklist_item(["Have it state a confidence", "number each time."])
        row3, box3 = checklist_item(["Group by number — check", "real accuracy."])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.5,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.4)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(0.8)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=3.5)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=3.5)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(4.2)
        self.play(Create(mark2), run_time=0.3)
        self.wait(4.2)
        self.play(Create(mark3), run_time=0.3)
        self.wait(4.2)

        closing1 = fit(T("If a '90% confident' group is", color=PALETTE["ink"], font_size=15), MAX_W)
        closing2 = fit(T("only right half the time —", color=PALETTE["ink"], font_size=15), MAX_W)
        closing3 = fit(T("you've measured a real gap.", color=PALETTE["ink"], font_size=15), MAX_W)
        closing_block = VGroup(closing1, closing2, closing3).arrange(DOWN, buff=0.1)
        closing_block.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        self.wait(4.17)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 11.64s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("Sounding sure", color=PALETTE["bg"], font_size=34), MAX_W)
        line1b = fit(T("isn't the same", color=PALETTE["bg"], font_size=34), MAX_W)
        line1c = fit(T("as being right.", color=PALETTE["bg"], font_size=34), MAX_W)
        line2 = fit(T("Check whether", color=PALETTE["gold"], font_size=28), MAX_W)
        line2b = fit(T("confidence tracks real", color=PALETTE["gold"], font_size=28), MAX_W)
        line2c = fit(T("accuracy, across many cases.", color=PALETTE["gold"], font_size=28, weight="BOLD"), MAX_W)

        block1 = VGroup(line1, line1b, line1c).arrange(DOWN, buff=0.22)
        block2 = VGroup(line2, line2b, line2c).arrange(DOWN, buff=0.24)
        content = VGroup(block1, block2).arrange(DOWN, buff=0.7).move_to(ORIGIN)

        # width padding 0.7 -> 0.25: the real pixel-true GATE V check (on the
        # TRUE final candidate) flagged a genuine edge-bleed BLOCKER here --
        # queried Manim's own widths directly and found the longest line
        # (line2c, fit to MAX_W=3.4 exactly) made the frame 4.1 wide
        # (half=2.05), past the ±1.95 safe half-width by 0.1. Smaller padding
        # keeps the same text at the same size, just a tighter real border.
        frame = panel(width=content.width + 0.25, height=content.height + 0.9,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(4.64)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes and buff enlarged (46/26/24, buff 0.5 -> 52/30/28, buff
        # 1.15): GATE V's canvas-fill check (measured directly on the TRUE
        # final candidate) found this card at only 44% of the safe area (min
        # 55%) -- queried Manim's own real heights/widths to confirm the
        # new numbers clear the floor (area ~74%) before re-rendering.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=52), MAX_W)
        accent = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=30), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=28), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=1.15).move_to(ORIGIN)

        frame_w = min(content.width + 0.4, MAX_W + 0.5)
        frame_h = min(content.height + 0.9, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.01)
