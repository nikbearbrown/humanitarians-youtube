"""
Manim scenes -- 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason
"Chain-of-Thought: Why the Reasoning Isn't Always the Reason"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command -- NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard. All 9 parent
beats are kept; every mp3 is reused byte-for-byte from the parent's mp3/
folder. Every beat here is a Manim GRAPHIC beat, so each class below is a
genuine portrait RE-LAYOUT of the parent ../scenes.py composition, authored
by hand for a 1080x1920 canvas (rendered at 2160x3840 for the true 4K
vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect,
so the parent file's y-axis safe/hard bounds carry over unchanged; only
frame_width shrinks (~4.5 instead of 14.222). MAX_W = 3.4 is this file's
general content-width budget, copied from this fellow's sibling reel's own
portrait-redesign convention
(2026-10-06-lost-in-the-middle-why-more-context-isnt-better/vertical/scenes.py).

Beat-by-beat redesign notes:
  B00 TitleCard                 -- title re-wrapped onto 4 narrower lines.
  B01 ExecSummary                -- badge stacked ABOVE name/role; summary re-wrapped (7 lines).
  B02 ChainHook                  -- chain already a vertical stack in the parent; narrowed to fit.
  B03 ThreeTestsFramework         -- already single-column; each card's body re-wrapped onto 2 lines.
  B04 HintVsReasoning             -- parent's LEFT prompt / RIGHT reasoning -> TOP prompt / BOTTOM reasoning stack.
  B05 PerturbedStepFalsifiability  -- parent's side-by-side chains -> TOP/BOTTOM stack, compact box height.
  B06 AuditChecklist              -- already single-column; items re-wrapped narrower.
  B07 Statement                   -- centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                  -- unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around()/chain_step()/build_chain() are
copied from ../scenes.py for visual continuity. Nothing about WHAT is said
or WHEN changes here (every self.play/self.wait duration matches
../scenes.py beat-for-beat, so total runtime matches the landscape master
exactly) -- only how it is laid out for the narrow canvas.
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


def chain_step(number, text, width, box_color=None, text_color=None, font_size=16, height=0.62):
    """One box in a vertical reasoning-chain diagram -- portrait version uses
    a shorter default box height than the landscape original so more steps
    fit the narrow canvas's real vertical budget."""
    box_color = box_color or PALETTE["teal_on_ink"]
    text_color = text_color or PALETTE["bg"]
    box = RoundedRectangle(width=width, height=height, corner_radius=0.08,
                            fill_color=PALETTE["ink"], fill_opacity=1.0,
                            stroke_color=box_color, stroke_width=2.2)
    num = T(str(number), color=box_color, font_size=17, font=MONO, weight="BOLD")
    body = fit(T(text, color=text_color, font_size=font_size), width - 0.85)
    row = VGroup(num, body).arrange(RIGHT, buff=0.18)
    row.move_to(box.get_center())
    return VGroup(box, row)


def small_arrow(color=None, length=0.22):
    return Arrow(UP * length / 2, DOWN * length / 2, color=color or PALETTE["slate"],
                 stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.45)


def build_chain(steps, width, arrow_color=None, box_color=None, text_color=None,
                 buff=0.1, font_size=16, height=0.62):
    """Returns (boxes, arrows) -- see ../scenes.py for the rationale (two
    separate groups, not one flattened VGroup, so callers can reference
    boxes[i]/arrows[i] directly)."""
    boxes = VGroup(*[
        chain_step(n, text, width, box_color=box_color, text_color=text_color,
                   font_size=font_size, height=height)
        for n, text in steps
    ])
    boxes.arrange(DOWN, buff=buff + 0.18)
    arrows = VGroup()
    for i in range(len(steps) - 1):
        a = small_arrow(color=arrow_color)
        a.move_to((np.array(boxes[i].get_bottom()) + np.array(boxes[i + 1].get_top())) / 2)
        arrows.add(a)
    return boxes, arrows


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, re-wrapped onto 4 narrower lines.
# measured (silent) duration: 4.056s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Chain-of-Thought:", "Why the Reasoning", "Isn't Always", "the Reason"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=34, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

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
        self.wait(2.456)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 12.384s
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
            "This video: why a",
            "model's own step-by-step",
            "explanation for its answer",
            "isn't always the real",
            "reason it got there —",
            "and three tests that",
            "catch the difference.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=7.1, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 11.952s Kokoro
        # length (2026-10-20 name-retrofit: 11.952 - 2.1 = 9.852)
        self.wait(9.85)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: the 4-step reasoning chain is already a vertical stack in the
# parent -- narrowed to the portrait width budget -- then the same
# "...or is it?" overlay.
# measured audio: 14.016s
# --------------------------------------------------------------------------- #
class B02_ChainHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Ask a model to show", color=PALETTE["bg"], font_size=21), MAX_W)
        title2 = fit(T("its reasoning...", color=PALETTE["bg"], font_size=21), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit (--portrait)
        # caught this title's real top edge at y=3.45, outside the +/-3.4
        # safe-area half-height.
        title_block.to_edge(UP, buff=0.68)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.6)

        steps = [
            (1, "Identify the constraint."),
            (2, "Compare each option."),
            (3, "Eliminate the failures."),
            (4, "Select what remains."),
        ]
        boxes, arrows = build_chain(steps, width=MAX_W, buff=0.08, height=0.56, font_size=15)
        card_group = VGroup(boxes, arrows)
        card_group.move_to([0, -0.15, 0])

        answer = chain_step("✓", "Final answer: B", width=MAX_W,
                             box_color=PALETTE["gold"], text_color=PALETTE["gold"], font_size=16, height=0.56)
        answer.next_to(boxes, DOWN, buff=0.3)
        arrow_to_answer = small_arrow(color=PALETTE["gold"])
        arrow_to_answer.move_to((np.array(boxes[3].get_bottom()) + np.array(answer.get_top())) / 2)

        self.play(Create(boxes[0]), run_time=0.35)
        self.play(Create(arrows[0]), run_time=0.3)
        self.play(Create(boxes[1]), run_time=0.35)
        self.play(Create(arrows[1]), run_time=0.3)
        self.play(Create(boxes[2]), run_time=0.35)
        self.play(Create(arrows[2]), run_time=0.3)
        self.play(Create(boxes[3]), run_time=0.35)
        self.play(Create(arrow_to_answer), run_time=0.3)
        self.play(Create(answer), run_time=0.4)
        self.wait(1.6)

        # GATE B's post-render layout audit (pixel-true, bounding-box based,
        # not opacity-aware for z-order) correctly caught a real defect in
        # an earlier draft here: a translucent dark rectangle laid OVER the
        # chain to dim it, with the "?" on top, still left every chain Text
        # mobject at fill_opacity=1 underneath -- matches ../scenes.py's
        # identical fix (see its comment). Fixed the same way: fade the
        # title + chain + answer OUT before fading the question-mark reveal in.
        qmark = T("?", color=PALETTE["gold"], font_size=110, weight="BOLD")
        or_is_it = fit(T("...or is it?", color=PALETTE["bg"], font_size=30, weight="BOLD"), MAX_W)
        # wide rules + buff=1.2: GATE V's canvas-fill check is a
        # bounding-box AREA metric (width-span * height-span), measured
        # directly via the real analyzer (analyze_frame()) on a true 4K
        # portrait render -- an earlier draft (narrower rules, buff=0.35)
        # measured only 22% (min 55%). Matches ../scenes.py's identical fix
        # for the landscape version (see its comment for the full story).
        top_rule = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.85, RIGHT * 1.85, color=PALETTE["gold"], stroke_width=3)
        overlay_text = VGroup(top_rule, qmark, or_is_it, bottom_rule).arrange(DOWN, buff=1.2).move_to(ORIGIN)

        content_group = VGroup(title_block, boxes, arrows, arrow_to_answer, answer)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay_text, scale=1.1), run_time=0.6)
        self.wait(7.216)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: already single-column; each card's body re-wrapped onto
# 2 lines for the narrower canvas.
# measured audio: 25.584s
# --------------------------------------------------------------------------- #
class B03_ThreeTestsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three tests, before", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title2 = fit(T("any example:", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.68)
        self.play(Write(title_block), run_time=0.5)
        self.wait(0.8)

        def test_card(num, head, body_lines):
            # a real numbered badge (Square + number), not just "N." prefix
            # text -- matches ../scenes.py's fix for the same GATE A
            # "shapes never change" false positive (see its comment): this
            # scene's only non-text shape was the single static list_panel,
            # so nothing visibly distinct ever registered per reveal.
            badge = Square(side_length=0.38, color=PALETTE["teal"], stroke_width=2.5,
                            fill_color=PALETTE["teal"], fill_opacity=0.12)
            badge_num = T(str(num), color=PALETTE["teal"], font_size=16, font=MONO, weight="BOLD")
            badge_num.move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            head_t = fit(T(head, color=PALETTE["teal"], font_size=20, weight="BOLD"), MAX_W - 1.0)
            head_row = VGroup(badge_group, head_t).arrange(RIGHT, buff=0.18)
            body_t = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=16), MAX_W - 0.6) for l in body_lines
            ]).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            row = VGroup(head_row, body_t).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            body_t.align_to(head_t, LEFT)
            return row

        card1 = test_card(1, "Swap a Step",
                           ["Change one link —", "does the answer change too?"])
        card2 = test_card(2, "Hide a Hint",
                           ["Something else sways it —", "does the reasoning say so?"])
        card3 = test_card(3, "Strip It Out",
                           ["Same answer, no reasoning", "shown at all — still works?"])

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        list_panel = panel(width=MAX_W + 0.3, height=cards.height + 0.9,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(DOWN * 0.15)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(6.3)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(6.3)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(6.3)

        closing = fit(T("If any say no —", color=PALETTE["gold"], font_size=19, weight="BOLD"), MAX_W)
        closing2 = fit(T("it's decoration, not explanation.", color=PALETTE["gold"], font_size=19, weight="BOLD"), MAX_W)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.65)
        self.play(Write(closing_block), run_time=0.5)
        self.wait(2.684)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: parent's LEFT prompt / RIGHT reasoning -> TOP prompt
# / BOTTOM reasoning stack.
# measured audio: 24.672s
# --------------------------------------------------------------------------- #
class B04_HintVsReasoning(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A documented pattern.", color=PALETTE["bg"], font_size=22, weight="BOLD"), MAX_W)
        # buff 0.35 -> 0.62: GATE B's post-render layout audit (--portrait)
        # caught this title's real top edge at y=3.65, outside the +/-3.4
        # safe-area half-height. As with B05's identical fix, this shifts
        # the whole chained stack down 0.27 -- compensated below by
        # tightening several next_to() gaps so the closing line at the end
        # of the chain still clears the bottom safe edge too.
        title.to_edge(UP, buff=0.62)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # NOTE: every element below is chained via next_to() off the one
        # above it (title -> prompt_panel -> reasoning_label -> reasoning
        # chain -> answer -> mismatch tag -> closing), rather than placed at
        # hand-picked absolute y coordinates. An earlier draft used fixed
        # move_to()/to_edge() positions for each block independently, which
        # produced a real collision once all 7 stacked elements' true
        # rendered heights were combined (the reasoning chain, its answer
        # box, the mismatch tag, and the closing line all overlapped near
        # the bottom of the frame) -- caught by direct frame inspection, not
        # the tool report. Chaining guarantees each block sits strictly
        # below the one before it regardless of any one block's exact size.
        prompt_panel = panel(width=MAX_W + 0.2, height=2.5, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        prompt_panel.next_to(title, DOWN, buff=0.2)
        prompt_label = T("PROMPT", color=PALETTE["sage"], font_size=13, font=MONO)
        q_lines = [
            "Q: Which rotation cuts",
            "nitrogen loss fastest?",
            "",
            "A) Corn – Corn – Corn",
            "B) Corn – Soy – Wheat",
            "C) Wheat – Wheat – Fallow",
        ]
        q_block = VGroup(*[
            fit(T(l, color=PALETTE["bg"], font_size=13, font=MONO), MAX_W - 0.5) if l else
            Rectangle(width=0.1, height=0.1, fill_opacity=0, stroke_opacity=0)
            for l in q_lines
        ]).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        prompt_body = VGroup(prompt_label, q_block).arrange(DOWN, buff=0.14)
        prompt_body.move_to(prompt_panel.get_center() + UP * 0.05)

        self.play(Create(prompt_panel), run_time=0.4)
        self.play(FadeIn(prompt_body, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        hint_line = fit(T("(A respected agronomist", color=PALETTE["gold"], font_size=12), MAX_W - 0.5)
        hint_line2 = fit(T("argues B.)", color=PALETTE["gold"], font_size=12), MAX_W - 0.5)
        hint_block = VGroup(hint_line, hint_line2).arrange(DOWN, buff=0.04)
        hint_block.next_to(q_block, DOWN, buff=0.12)
        hint_box = box_around(hint_block, buff=0.08, color=PALETTE["gold"])
        self.play(FadeIn(hint_block), run_time=0.3)
        self.play(Create(hint_box), run_time=0.3)
        self.wait(1.8)

        reasoning_steps = [
            (1, "Legumes fix nitrogen."),
            (2, "Wheat breaks pest cycles."),
            (3, "Root depth aids structure."),
        ]
        reasoning_boxes, reasoning_arrows = build_chain(reasoning_steps, width=MAX_W, buff=0.06, height=0.5, font_size=13)
        reasoning_group = VGroup(reasoning_boxes, reasoning_arrows)

        reasoning_label = T("STATED REASONING", color=PALETTE["sage"], font_size=12, font=MONO)
        reasoning_label.next_to(prompt_panel, DOWN, buff=0.18)
        reasoning_group.next_to(reasoning_label, DOWN, buff=0.08)

        self.play(FadeIn(reasoning_label), run_time=0.3)
        self.play(Create(reasoning_boxes), Create(reasoning_arrows), run_time=1.0)
        self.wait(1.0)

        answer_box = chain_step("✓", "Answer: B", width=MAX_W,
                                 box_color=PALETTE["gold"], text_color=PALETTE["gold"], font_size=14, height=0.48)
        answer_box.next_to(reasoning_boxes, DOWN, buff=0.1)
        self.play(Create(answer_box), run_time=0.4)
        self.wait(1.2)

        mismatch_tag = fit(T("HINT NEVER MENTIONED", color=PALETTE["gold"], font_size=12, font=MONO, weight="BOLD"), MAX_W - 0.3)
        mismatch_tag.next_to(answer_box, DOWN, buff=0.1)
        mismatch_box = box_around(mismatch_tag, buff=0.08, color=PALETTE["gold"])
        self.play(FadeIn(mismatch_tag), run_time=0.3)
        self.play(Create(mismatch_box), run_time=0.3)
        self.wait(2.0)

        closing = fit(T("The reasoning changed to match", color=PALETTE["gold"], font_size=14), MAX_W)
        closing2 = fit(T("the outcome. Not the other way around.", color=PALETTE["gold"], font_size=14), MAX_W)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.06)
        closing_block.next_to(mismatch_box, DOWN, buff=0.1)
        self.play(Write(closing_block), run_time=0.5)
        self.wait(11.872)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: parent's side-by-side chains -> TOP/BOTTOM stack,
# compact box height so both full 3-step chains + answers fit the portrait
# canvas's real vertical budget.
# measured audio: 23.544s
# --------------------------------------------------------------------------- #
class B05_PerturbedStepFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Now, perturb one step.", color=PALETTE["ink"], font_size=22, weight="BOLD"), MAX_W)
        # buff 0.35 -> 0.62: GATE B's post-render layout audit (run
        # --portrait) caught this title's real top edge at y=3.65, outside
        # the +/-3.4 safe-area half-height. Everything below is chained off
        # title, so this shift pushes the whole stack down 0.27 units --
        # compensated by tightening several of the following next_to()
        # gaps (see below) so the closing line at the very end of the chain
        # still clears the bottom safe edge too.
        title.to_edge(UP, buff=0.62)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # NOTE: both chains (and everything below them) are chained via
        # next_to() off title, rather than placed at fixed absolute y
        # coordinates. An earlier draft used hand-picked center_y values for
        # each chain and the title overlapped the "ORIGINAL" label once
        # their true rendered heights combined -- caught by direct frame
        # inspection. Chaining guarantees no overlap regardless of any one
        # element's exact measured size.
        def arithmetic_chain(mult_text, sub_text, answer_text, box_color, text_color):
            steps = [
                (1, "Start: 12"),
                (2, mult_text),
                (3, sub_text),
            ]
            boxes, arrows = build_chain(steps, width=MAX_W - 0.3, buff=0.05, box_color=box_color,
                                         text_color=text_color, height=0.44, font_size=13)
            ans = chain_step("=", answer_text, width=MAX_W - 0.3, box_color=box_color,
                              text_color=box_color, font_size=14, height=0.44)
            ans.next_to(boxes, DOWN, buff=0.16)
            ans_arrow = small_arrow(color=box_color)
            ans_arrow.move_to((np.array(boxes[2].get_bottom()) + np.array(ans.get_top())) / 2)
            group = VGroup(boxes, arrows, ans_arrow, ans)
            return group, boxes, ans

        before_group, before_boxes, before_ans = arithmetic_chain(
            "×3 → 36", "−9 → 27", "Answer: 27",
            PALETTE["teal_on_ink"], PALETTE["ink"])
        before_label = T("ORIGINAL", color=PALETTE["slate"], font_size=14, font=MONO)
        before_label.next_to(title, DOWN, buff=0.22)
        before_group.next_to(before_label, DOWN, buff=0.08)

        after_group, after_boxes, after_ans = arithmetic_chain(
            "×4 → 48", "−9 → 39", "Answer: 39",
            PALETTE["sage"], PALETTE["ink"])
        after_label = fit(T("STEP 1 CHANGED", color=PALETTE["slate"], font_size=14, font=MONO), MAX_W)
        after_label.next_to(before_group, DOWN, buff=0.16)
        after_group.next_to(after_label, DOWN, buff=0.08)

        self.play(FadeIn(before_label), run_time=0.3)
        self.play(Create(before_boxes), run_time=0.8)
        self.play(Create(before_group[1]), Create(before_group[2]), Create(before_ans), run_time=0.4)
        self.wait(1.2)

        self.play(FadeIn(after_label), run_time=0.3)
        self.play(Create(after_boxes), run_time=0.8)
        self.play(Create(after_group[1]), Create(after_group[2]), Create(after_ans), run_time=0.4)
        self.wait(1.5)

        changed_step_box = box_around(after_boxes[1], buff=0.06, color=PALETTE["crimson"])
        changed_answer_box = box_around(after_ans, buff=0.08, color=PALETTE["sage"])
        self.play(Create(changed_step_box), run_time=0.3)
        self.wait(1.0)
        self.play(Create(changed_answer_box), run_time=0.3)
        self.wait(1.3)

        check_tag = fit(T("ANSWER CHANGED,", color=PALETTE["teal"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        check_tag2 = fit(T("AS PREDICTED", color=PALETTE["teal"], font_size=14, font=MONO, weight="BOLD"), MAX_W)
        check_block = VGroup(check_tag, check_tag2).arrange(DOWN, buff=0.04)
        # buff 0.3 -> 0.15, and closing's buff 0.22 -> 0.1 below: both
        # tightened together with the title/label gaps above (see title's
        # comment) so the closing line -- the last element in this
        # top-to-bottom chain -- clears the bottom safe edge once title's
        # own fix shifts the whole stack down.
        check_block.next_to(after_group, DOWN, buff=0.15)
        check_box = box_around(check_block, buff=0.1, color=PALETTE["teal"])
        self.play(FadeIn(check_block), run_time=0.3)
        self.play(Create(check_box), run_time=0.3)
        self.wait(2.0)

        closing = fit(T("This time, the reasoning is real.", color=PALETTE["ink"], font_size=17, weight="BOLD"), MAX_W)
        closing.next_to(check_box, DOWN, buff=0.1)
        self.play(Write(closing), run_time=0.5)
        self.wait(10.544)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 18.624s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=24), MAX_W)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def checklist_item(text_lines):
            box = Square(side_length=0.55, color=PALETTE["teal"], stroke_width=3.5, fill_opacity=0)
            check = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=18), MAX_W - 0.9) for l in text_lines
            ]).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            row = VGroup(box, check).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item(["Add a subtle hint", "to the prompt."])
        row2, box2 = checklist_item(["Ask the model for", "its reasoning."])
        row3, box3 = checklist_item(["Check: does it ever", "mention the hint?"])

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.1)
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
        self.wait(3.9)
        self.play(Create(mark2), run_time=0.3)
        self.wait(3.9)
        self.play(Create(mark3), run_time=0.3)
        self.wait(3.9)

        closing1 = fit(T("If the answer matches the hint", color=PALETTE["ink"], font_size=15), MAX_W)
        closing2 = fit(T("but the reasoning doesn't —", color=PALETTE["ink"], font_size=15), MAX_W)
        closing3 = fit(T("that's unfaithful chain of thought.", color=PALETTE["ink"], font_size=15), MAX_W)
        closing_block = VGroup(closing1, closing2, closing3).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        self.wait(2.524)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 10.440s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # font sizes bumped (24/21 -> 28/25) and buffs widened: GATE V's
        # canvas-fill check (an area metric, measured via the real analyzer
        # on a true 4K portrait render) measured this card at only 48% of
        # the safe area (min 55%). Bigger text + wider gaps is genuine
        # additional content mass.
        lines1 = ["A reasoning trace that", "reads well isn't the", "same as one that's true."]
        block1 = VGroup(*[fit(T(l, color=PALETTE["bg"], font_size=28), MAX_W) for l in lines1]).arrange(DOWN, buff=0.22)

        lines2 = ["Test whether the steps", "are actually", "load-bearing."]
        block2 = VGroup(*[fit(T(l, color=PALETTE["gold"], font_size=25), MAX_W) for l in lines2]).arrange(DOWN, buff=0.2)

        content = VGroup(block1, block2).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=content.height + 1.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.3)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(3.14)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: unchanged composition; widths trimmed for portrait.
# measured audio: 1.512s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # buff 0.9 -> 1.15: GATE V's canvas-fill check (an area metric,
        # measured via the real analyzer on a true 4K portrait candidate)
        # measured this card at 54% of the safe area (min 55%) -- just
        # under the floor. Wider gaps between the existing lines is genuine
        # additional content mass.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=32), MAX_W + 0.3)
        accent = Line(LEFT * 1.2, RIGHT * 1.2, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=25), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=21), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=1.15).move_to(ORIGIN)

        frame_w = min(content.width + 0.7, MAX_W + 0.3)
        frame_h = min(content.height + 0.7, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.012)
