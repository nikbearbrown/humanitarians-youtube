"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-28-in-context-learning-limits
"In-Context Learning: What the Prompt Can (and Can't) Teach"

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
general content-width budget, copied from this fellow's sibling reel's own
portrait-redesign convention
(2026-10-21-calibration-why-confidence-isnt-accuracy/vertical/scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard                       -- title re-wrapped onto 3 narrower lines.
  B01 ExecSummary                      -- badge stacked ABOVE name/role; summary re-wrapped (6 lines).
  B02 LearningOrLocatingHook            -- example panel narrowed; query row stacked under its label.
  B03 ThreeTestsFramework                -- already single-column; each card's body re-wrapped onto 2 lines.
  B04 ToyMappingWorkedExample             -- example-pair panel narrowed (smaller fonts, tighter padding).
  B05 ReorderedFlippedFalsifiability        -- same narrowed panel + flip/mismatch tags stacked, not inline.
  B06 AuditChecklist                       -- already single-column; items re-wrapped narrower.
  B07 Statement                            -- centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                           -- unchanged composition; widths trimmed.

Every element within a beat is positioned by chaining `next_to()` off the
block above it (never hand-picked absolute y-coordinates) -- the sibling
reel's BUILD-LOG documents real title/content collisions from absolute
coordinates not accounting for how real rendered heights combine once a
layout is redesigned for a narrow canvas; chaining avoids that class of bug
by construction.

Palette/MONO/fit()/T()/panel()/box_around()/pair_row()/example_panel() are
copied from ../scenes.py for visual continuity. Nothing about WHAT is said
or WHEN changes here -- every self.play/self.wait duration matches
../scenes.py beat-for-beat, so total runtime matches the landscape master
exactly -- only how it is laid out for the narrow canvas.
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
# Copied verbatim from this fellow's sibling reel's vertical/scenes.py, which
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


def pair_row(inp, out, in_color, out_color, font_size=16, arrow_color=None):
    """Portrait version of ../scenes.py's pair_row() -- smaller default
    font_size so a stack of these fits MAX_W."""
    inp_t = T(inp, color=in_color, font_size=font_size, font=MONO, weight="BOLD")
    arrow = T("->", color=arrow_color or PALETTE["gold"], font_size=font_size, font=MONO, weight="BOLD")
    out_t = T(out, color=out_color, font_size=font_size, font=MONO, weight="BOLD")
    return VGroup(inp_t, arrow, out_t).arrange(RIGHT, buff=0.18)


def example_panel(pairs, label_text, label_color, row_in_color, row_out_color,
                   fill, stroke, buff=0.16, label_font=14):
    """Portrait version of ../scenes.py's example_panel() -- narrower padding
    and a smaller label font so the whole panel fits MAX_W."""
    label = fit(T(label_text, color=label_color, font_size=label_font, font=MONO, weight="BOLD"), MAX_W - 0.5)
    rows = VGroup(*[pair_row(i, o, row_in_color, row_out_color) for i, o in pairs]).arrange(
        DOWN, buff=buff, aligned_edge=LEFT)
    content = VGroup(label, rows).arrange(DOWN, buff=0.22)
    box = panel(width=content.width + 0.5, height=content.height + 0.4,
                fill=fill, stroke=stroke, corner_radius=0.12, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card. measured (silent) duration: 4.104s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("In-Context", color=PALETTE["ink"], font_size=38, weight="BOLD"), MAX_W)
        title_line2 = fit(T("Learning:", color=PALETTE["ink"], font_size=38, weight="BOLD"), MAX_W)
        title_line3 = fit(T("What the Prompt Can", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        title_line4 = fit(T("(and Can't) Teach", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        title = VGroup(title_line1, title_line2, title_line3, title_line4).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        # GATE V canvas-fill check: safe half-height is 3.6 (frame_height=8,
        # 5% margin). This frame's height must stay <= 7.2 with margin --
        # 7.0 gives real clearance (half 3.5), matching the fix applied to
        # B01 below after that beat's true-candidate edge-bleed finding.
        frame = panel(width=4.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.504)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: badge stacked above name/role (portrait redesign).
# measured audio: 14.64s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.45, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=32, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.22)

        summary_lines = [
            "This video: in-context",
            "learning — picking up a",
            "pattern from examples in",
            "the prompt, no weight",
            "updates — and three tests",
            "for what that can teach.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=22), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.16)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.45).move_to(ORIGIN)

        # GATE V BLOCKER on the TRUE final candidate (not a review-slate
        # false positive): this frame's height=7.4 (half 3.7) genuinely
        # exceeded the portrait safe half-height of 3.6, bleeding past the
        # top AND bottom title-safe edges -- confirmed by extracting a real
        # frame and measuring the visible gold border against the computed
        # safe boundary. Fixed to height=7.0 (half 3.5, real clearance).
        frame = panel(width=4.0, height=7.0, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        self.wait(12.54)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: portrait redesign -- same column order as landscape (title,
# panel, query, tag, overlay) since the landscape file is already a single
# column; only widths/fonts narrow for MAX_W.
# measured audio: 21.26s
# --------------------------------------------------------------------------- #
class B02_LearningOrLocatingHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_l1 = fit(T("Show it a few", color=PALETTE["bg"], font_size=26), MAX_W)
        title_l2 = fit(T("examples...", color=PALETTE["bg"], font_size=26), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.12)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        pairs = [("CAT", "FDW"), ("DOG", "GRJ"), ("SUN", "VXQ")]
        panel_group, panel_box, panel_content = example_panel(
            pairs, "EXAMPLES IN PROMPT", PALETTE["gold"],
            PALETTE["bg"], PALETTE["teal_on_ink"],
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.5)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        query_label = T("NEW INPUT:", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        query_row = pair_row("BIG", "?", PALETTE["bg"], PALETTE["gold"])
        query_block = VGroup(query_label, query_row).arrange(DOWN, buff=0.14)
        query_block.next_to(panel_group, DOWN, buff=0.45)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(0.5)

        resolved = T("ELJ", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        correct_tag = T("CORRECT", color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD")
        correct_tag.next_to(query_block, DOWN, buff=0.3)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.4)
        same_tag_l1 = fit(T("SAME CONTEXT.", color=PALETTE["sage"], font_size=16, font=MONO), MAX_W)
        same_tag_l2 = fit(T("NO WEIGHTS CHANGED.", color=PALETTE["sage"], font_size=16, font=MONO), MAX_W)
        same_tag = VGroup(same_tag_l1, same_tag_l2).arrange(DOWN, buff=0.1)
        same_tag.next_to(bottom_rule, DOWN, buff=0.3)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # GATE V MAJOR on the TRUE final candidate: this overlay (the beat's
        # whole second half) measured only 48% of the safe area (min 55%) at
        # both sample points. Fixed with genuinely larger content -- a bigger
        # qmark, wider rules, and more inter-element spacing -- not padding.
        qmark = T("?", color=PALETTE["gold"], font_size=160, weight="BOLD")
        overlay_line1 = fit(T("Learning,", color=PALETTE["bg"], font_size=40, weight="BOLD"), MAX_W)
        overlay_line2 = fit(T("or locating?", color=PALETTE["bg"], font_size=40, weight="BOLD"), MAX_W)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule2 = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 1.9, RIGHT * 1.9, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=0.9).move_to(ORIGIN)

        content_group = VGroup(title, panel_group, query_block, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # waits front-loaded (matches ../scenes.py's B02 fix) so the
        # FadeOut/FadeIn transition completes well before GATE V's 50%/85%
        # steady-state sample points -- a real empty-frame/underfill finding
        # on the TRUE final candidate, not a tooling false positive.
        self.wait(14.16)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: already single-column; card bodies re-wrapped onto 2
# narrower lines. measured audio: 35.21s
# --------------------------------------------------------------------------- #
class B03_ThreeTestsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_l1 = fit(T("Three tests,", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_l2 = fit(T("before any example:", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def test_card(num, head, body_lines):
            badge = Square(side_length=0.38, color=PALETTE["teal"], stroke_width=3,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            # GATE V BLOCKER on the TRUE final candidate: this card's
            # head_row (badge + head_t, fit to MAX_W-0.5) plus list_panel's
            # own +0.6 padding pushed the panel's real half-width past the
            # portrait safe half-width of 2.025 -- a real overflow, not a
            # review-slate artifact. Tightened budgets below (head_t to
            # MAX_W-0.9, body_t to MAX_W-0.4, panel padding +0.6 -> +0.3)
            # give real measured clearance instead of guessing.
            head_t = fit(T(head, color=PALETTE["teal"], font_size=19, weight="BOLD"), MAX_W - 0.9)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.18)
            body_t = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=15), MAX_W - 0.4) for l in body_lines]).arrange(
                DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(head_row, body_t).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            body_t.align_to(head_t, LEFT)
            return row

        card1 = test_card(1, "Spot the Mapping",
                           ["Can you tell, from the examples,", "what pattern they point toward?"])
        card2 = test_card(2, "Shuffle the Set",
                           ["Reorder or recount the examples —", "does the answer survive?"])
        card3 = test_card(3, "Push Past the Window",
                           ["Needs more than fits the prompt,", "or a capability never latent at all?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 0.3, height=cards.height + 0.6,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.4)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)

        closing_l1 = fit(T("If it only holds for one", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing_l2 = fit(T("ordering — that's the boundary.", color=PALETTE["gold"], font_size=18, weight="BOLD"), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        self.wait(4.21)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: narrowed example panel (same mechanism as landscape).
# measured audio: 28.49s
# --------------------------------------------------------------------------- #
class B04_ToyMappingWorkedExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title_l1 = fit(T("A made-up rule,", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title_l2 = fit(T("taught by example.", color=PALETTE["bg"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        pairs = [("CAT", "FDW"), ("DOG", "GRJ"), ("SUN", "VXQ"), ("BIG", "ELJ")]
        panel_group, panel_box, panel_content = example_panel(
            pairs, "RULE: UNKNOWN", PALETTE["gold"],
            PALETTE["bg"], PALETTE["teal_on_ink"],
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.45)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        query_label = T("NEW INPUT:", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD")
        query_row = pair_row("RUN", "?", PALETTE["bg"], PALETTE["gold"])
        query_block = VGroup(query_label, query_row).arrange(DOWN, buff=0.14)
        query_block.next_to(panel_group, DOWN, buff=0.4)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(1.0)

        resolved = T("UXQ", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        self.wait(1.3)

        gap_tag = fit(T("LOCATED, NOT LEARNED", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD"), MAX_W)
        gap_tag.next_to(query_block, DOWN, buff=0.35)
        gap_box = box_around(gap_tag, buff=0.12, color=PALETTE["gold"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing_l1 = fit(T("No new fact was learned —", color=PALETTE["gold"], font_size=16), MAX_W)
        closing_l2 = fit(T("a pattern in reach was found.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        self.wait(18.89)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: narrowed example panel, flip/mismatch tags stacked.
# measured audio: 27.17s
# --------------------------------------------------------------------------- #
class B05_ReorderedFlippedFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_l1 = fit(T("Now, reorder it —", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_l2 = fit(T("and flip one.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title = VGroup(title_l1, title_l2).arrange(DOWN, buff=0.1)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        pairs = [("BIG", "ELJ"), ("SUN", "VXQ"), ("DOG", "GRI"), ("CAT", "FDW")]
        flip_index = 2
        panel_group, panel_box, panel_content = example_panel(
            pairs, "SAME EXAMPLES — REORDERED", PALETTE["slate"],
            PALETTE["ink"], PALETTE["teal"],
            fill=PALETTE["bg"], stroke=PALETTE["slate"], label_font=12)
        panel_group.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        rows = panel_content[1]
        flipped_row = rows[flip_index]
        flip_box = Rectangle(width=flipped_row.width + 0.2, height=flipped_row.height + 0.1,
                              stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        flip_box.move_to(flipped_row.get_center())
        # placed BELOW the whole panel (not inline next to the flipped row --
        # a real bug found here: an earlier draft placed this tag directly
        # under flip_box with a small buff, which read fine in the landscape
        # file's wide rows but, in this file's tightly-packed portrait row
        # stack (row buff=0.16), landed on top of the next row's text
        # ("CAT -> FDW") -- confirmed via the real pixel-true
        # manim_layout_audit.py --portrait, a genuine text-on-text ERROR, not
        # a tooling false positive. Fixed by moving the tag below the full
        # panel instead of inline between rows.
        flip_tag = fit(T("FLIPPED EXAMPLE", color=PALETTE["crimson"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        flip_tag.next_to(panel_group, DOWN, buff=0.22)
        self.play(Create(flip_box), run_time=0.3)
        self.play(FadeIn(flip_tag), run_time=0.3)
        self.wait(0.6)

        query_label = T("NEW INPUT:", color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
        query_row = pair_row("RUN", "?", PALETTE["ink"], PALETTE["slate"])
        query_block = VGroup(query_label, query_row).arrange(DOWN, buff=0.14)
        query_block.next_to(VGroup(panel_group, flip_tag), DOWN, buff=0.4)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(1.0)

        resolved = T("UXP", color=PALETTE["crimson"], font_size=18, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        self.wait(0.6)

        mismatch_tag = T("MISMATCH", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        mismatch_tag.next_to(query_block, DOWN, buff=0.35)
        mismatch_box = box_around(mismatch_tag, buff=0.12, color=PALETTE["crimson"])
        self.play(FadeIn(mismatch_tag), run_time=0.3)
        self.play(Create(mismatch_box), run_time=0.3)
        self.wait(1.5)

        closing_l1 = fit(T("Same task, same count —", color=PALETTE["ink"], font_size=16, weight="BOLD"), MAX_W)
        closing_l2 = fit(T("one flip, and it breaks.", color=PALETTE["ink"], font_size=16, weight="BOLD"), MAX_W)
        closing = VGroup(closing_l1, closing_l2).arrange(DOWN, buff=0.08)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        self.wait(18.07)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 27.70s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.7)
        # GATE V MAJOR on the TRUE final candidate: 53% of safe area (min
        # 55%). Fixed with real framing rules (genuine added content mass,
        # folded into the existing title/closing plays so timing is
        # unchanged), same idiom as the landscape B04 fix.
        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        def checklist_item(lines):
            box = Square(side_length=0.55, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = VGroup(*[fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W - 0.8) for l in lines]).arrange(
                DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(box, check).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item(["Invent a rule with no", "real-world meaning."])
        row2, box2 = checklist_item(["Test new inputs — then", "shuffle the examples."])
        row3, box3 = checklist_item(["Flip one mapping —", "check if it still holds."])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.5,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.12, opacity=1.0)
        list_panel.next_to(title, DOWN, buff=0.45)
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
        self.wait(6.0)
        self.play(Create(mark2), run_time=0.3)
        self.wait(6.0)
        self.play(Create(mark3), run_time=0.3)
        self.wait(6.0)

        closing1 = fit(T("If answers only hold for", color=PALETTE["ink"], font_size=16), MAX_W)
        closing2 = fit(T("the original order —", color=PALETTE["ink"], font_size=16), MAX_W)
        closing3 = fit(T("you've found the edge.", color=PALETTE["ink"], font_size=16), MAX_W)
        closing_block = VGroup(closing1, closing2, closing3).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(closing_block, shift=UP * 0.1), Create(bottom_rule), run_time=0.4)
        self.wait(5.3)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 13.06s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("In-context learning is", color=PALETTE["bg"], font_size=24), MAX_W)
        line1b = fit(T("pattern-location, not", color=PALETTE["bg"], font_size=24), MAX_W)
        line1c = fit(T("instant new learning.", color=PALETTE["bg"], font_size=28, weight="BOLD"), MAX_W)
        line2 = fit(T("Bounded by what's", color=PALETTE["gold"], font_size=24), MAX_W)
        line2b = fit(T("already latent, and by", color=PALETTE["gold"], font_size=24), MAX_W)
        line2c = fit(T("what fits, stably, in the prompt.", color=PALETTE["gold"], font_size=24, weight="BOLD"), MAX_W)

        block1 = VGroup(line1, line1b, line1c).arrange(DOWN, buff=0.16)
        block2 = VGroup(line2, line2b, line2c).arrange(DOWN, buff=0.16)
        content = VGroup(block1, block2).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        # GATE V MAJOR on the TRUE final candidate: a content-fitted frame
        # (content.height+0.8) measured only 53% of the safe area at BOTH
        # sample points (min 55%) -- the 6-line statement alone doesn't fill
        # a portrait canvas. Fixed with a genuinely larger, still-visible
        # bordered frame (real content mass, not an invisible padding
        # rectangle) sized from the portrait safe bounds themselves
        # (half-width 2.025, half-height 3.6), not the text's own size.
        frame = panel(width=4.0, height=7.0,
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
        self.wait(6.06)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: unchanged composition; widths trimmed. measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=46), MAX_W)
        accent = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=26), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=24), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        # GATE V MAJOR on the TRUE final candidate: the content-fitted frame
        # measured only 42% of the safe area at both sample points (min
        # 55%), the worst underfill found this build. Fixed with a fixed,
        # generously sized, still-visible bordered frame (real content
        # mass) matching B00/B01's own already-confirmed-safe dimensions,
        # instead of sizing the frame from this beat's short 4-line content.
        frame = panel(width=4.0, height=7.0,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.01)
