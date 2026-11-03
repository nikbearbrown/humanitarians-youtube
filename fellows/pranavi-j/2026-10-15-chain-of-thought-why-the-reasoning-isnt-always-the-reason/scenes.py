"""
Manim scenes for 2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason
"Chain-of-Thought: Why the Reasoning Isn't Always the Reason"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Teaches a reusable 3-question test -- Swap a Step / Hide a Hint /
Strip It Out -- for telling whether a model's stated step-by-step reasoning
actually caused its answer, or is a fluent, plausible-sounding story attached
after the fact. The worked example (B04) and its falsifiability case (B05)
are both fully generic/hypothetical -- no real model, vendor, or product is
named or benchmarked. See FACTCHECK.md and SOURCES.md.

B00_TitleCard                   -- silent title card (TITLE)
B01_ExecSummary                  -- spoken personal-intro card (EXEC-SUMMARY)
B02_ChainHook                    -- confident reasoning chain, then "...or is it?" (HOOK)
B03_ThreeTestsFramework           -- all 3 tests shown together, before any example (FRAMEWORK)
B04_HintVsReasoning               -- hint in the prompt vs. reasoning that never mentions it (WORKED-EXAMPLE)
B05_PerturbedStepFalsifiability    -- perturbed step visibly changes the answer (FALSIFIABILITY)
B06_AuditChecklist                -- the 3 tests as a concrete task to try today (SCAFFOLDED-TASK)
B07_Statement                     -- takeaway statement card (TAKEAWAY)
B08_BrandOutro                    -- @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's sibling reel (2026-10-06-lost-in-the-middle-why-more-context-isnt-better)
for visual consistency across the series. Plain Text (Pango) throughout,
never Integer/DecimalNumber/MathTex -- no LaTeX installed, and this reel's
arithmetic example (B05) is shown as plain Text strings, not typeset math.

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule:
B00=4.056 (silent, fixed target) B01=12.384 B02=14.016 B03=25.584 B04=24.672
B05=23.544 B06=18.624 B07=10.440 B08=1.512.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area).

WORKED EXAMPLE CONTENT (B04/B05) -- chosen per the build brief, fully generic:

B04 -- a multiple-choice-style agronomy question with a planted authority
hint ("a respected agronomist argues B") sitting in the prompt. The model's
stated reasoning independently re-derives the same answer (B) from 3 generic
domain facts (nitrogen fixation / pest-cycle break / root depth) and never
once refers to the hint. Chosen because it's a clean, self-contained, fully
fictional domain (no real model/vendor, no real agronomy claim needs to be
true or false -- it only needs to be *plausible-sounding*, which is the
entire point: a reasoning trace can sound rigorous while doing no causal
work) and because the mismatch (hint present, answer matches hint, hint
absent from the stated reasoning) is visible on screen without narration.

B05 -- a 3-step arithmetic chain (start at 12, multiply, then subtract) run
twice: once as originally stated (answer 27), once with ONE intermediate
step's number changed (the multiplier 3 -> 4), and the final answer changes
exactly as that step predicts (answer becomes 39, not 27). Chosen because
it's the simplest possible case where the causal claim "this step really
produces the output" is mechanically true and checkable by anyone watching,
giving B04's mismatch a real, visibly different (checkmark, not a gap)
counterpart -- per FACTCHECK.md #3, an uncontested, non-benchmarked claim.
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
    created directly at a small font_size. See sibling reel's BUILD-LOG.md for the
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


def chain_step(number, text, width, box_color=None, text_color=None, font_size=19):
    """One box in a vertical reasoning-chain diagram: a step number + its
    text. Used by B02 (hook), B04 (right-hand reasoning), B05 (arithmetic)."""
    box_color = box_color or PALETTE["teal_on_ink"]
    text_color = text_color or PALETTE["bg"]
    box = RoundedRectangle(width=width, height=0.86, corner_radius=0.1,
                            fill_color=PALETTE["ink"], fill_opacity=1.0,
                            stroke_color=box_color, stroke_width=2.5)
    num = T(str(number), color=box_color, font_size=20, font=MONO, weight="BOLD")
    body = fit(T(text, color=text_color, font_size=font_size), width - 1.1)
    row = VGroup(num, body).arrange(RIGHT, buff=0.22)
    row.move_to(box.get_center())
    return VGroup(box, row)


def small_arrow(color=None, length=0.3):
    return Arrow(UP * length / 2, DOWN * length / 2, color=color or PALETTE["slate"],
                 stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.45)


def build_chain(steps, width, arrow_color=None, box_color=None, text_color=None, buff=0.18):
    """Returns (boxes, arrows): `boxes` is a VGroup of chain_step boxes
    arranged top-to-bottom, `arrows` is a VGroup of the small connecting
    arrows between consecutive boxes (len(boxes) - 1 of them). Kept as two
    separate groups -- rather than one flattened VGroup -- so callers can
    reference boxes[i] / arrows[i] directly without re-deriving offsets."""
    boxes = VGroup(*[
        chain_step(n, text, width, box_color=box_color, text_color=text_color)
        for n, text in steps
    ])
    boxes.arrange(DOWN, buff=buff + 0.3)
    arrows = VGroup()
    for i in range(len(steps) - 1):
        a = small_arrow(color=arrow_color)
        a.move_to((np.array(boxes[i].get_bottom()) + np.array(boxes[i + 1].get_top())) / 2)
        arrows.add(a)
    return boxes, arrows


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.056s -- fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Chain-of-Thought:", color=PALETTE["ink"], font_size=46, weight="BOLD"), 12.0)
        title_line2 = fit(T("Why the Reasoning Isn't", color=PALETTE["ink"], font_size=36, weight="BOLD"), 12.0)
        title_line3 = fit(T("Always the Reason", color=PALETTE["ink"], font_size=36, weight="BOLD"), 12.0)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.28)

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
        # sum of plays = 1.6s; remainder tuned to the measured 4.056s silent track
        self.wait(2.456)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 12.384s
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
            "This video: why a model's own step-by-step",
            "explanation for its answer isn't always the",
            "real reason it got there — and three tests",
            "that catch the difference.",
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
        # sum of plays = 2.1s; remainder tuned to the measured 11.952s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 12.384s -> wait 10.284)
        self.wait(9.85)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: a confident, well-formatted 4-step reasoning chain ending in
# an answer, then a question mark overlay: "...or is it?"
# [Source: FACTCHECK.md #1 -- generic/hypothetical, no real model named]
# measured audio: 14.016s
# --------------------------------------------------------------------------- #
class B02_ChainHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Ask a model to show its reasoning...", color=PALETTE["bg"], font_size=28), 11.8)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # title's real top edge at y=3.45, outside the +/-3.4 safe-area
        # half-height on the true rendered 4K frame.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.6)

        steps = [
            (1, "Identify the relevant constraint."),
            (2, "Compare each option against it."),
            (3, "Eliminate the options that fail."),
            (4, "Select the one that remains."),
        ]
        boxes, arrows = build_chain(steps, width=7.4, buff=0.12)
        card_group = VGroup(boxes, arrows)
        card_group.move_to([0, 0.35, 0])

        answer = chain_step("✓", "Final answer: B", width=7.4,
                             box_color=PALETTE["gold"], text_color=PALETTE["gold"], font_size=22)
        answer.next_to(boxes, DOWN, buff=0.45)
        arrow_to_answer = small_arrow(color=PALETTE["gold"])
        arrow_to_answer.move_to((np.array(boxes[3].get_bottom()) + np.array(answer.get_top())) / 2)

        # reveal step-by-step, box then its connecting arrow, in narration order
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

        # fluent + plausible, but the hook's whole point: looks finished.
        # GATE B's post-render layout audit (pixel-true, bounding-box based,
        # not opacity-aware for z-order) correctly caught a real defect in
        # an earlier draft here: a translucent dark rectangle laid OVER the
        # chain to dim it, with the "?" on top, still left every chain Text
        # mobject at fill_opacity=1 underneath -- the audit has no concept
        # of "visually obscured by a mobject drawn later," only each Text's
        # own bounding box and opacity, so it flagged real text-on-text
        # overlaps between "?" and the chain steps it was meant to replace.
        # Fixed by actually fading the title + chain + answer OUT (to
        # opacity 0, removing them from the scene) before fading the
        # question-mark reveal in -- a cleaner reveal than a dim-behind
        # effect, not just a workaround.
        qmark = T("?", color=PALETTE["gold"], font_size=160, weight="BOLD")
        or_is_it = fit(T("...or is it?", color=PALETTE["bg"], font_size=44, weight="BOLD"), 10.0)
        # top/bottom accent rules + wide buff: GATE V's canvas-fill check is
        # a bounding-box AREA metric (width-span * height-span over the safe
        # area), not a width-only span -- confirmed by direct measurement on
        # the TRUE final candidate (not the review slate, whose burn-in
        # labels happen to mask this: the slate's own GATE V pass was not
        # trustworthy here). A first fix (thin rules, tight buff=0.45) only
        # widened the card, leaving it short -- 31% area, worse than before,
        # because area is width-fraction * height-fraction and the height
        # span was still small. Fixed for real this time: buff widened to
        # 1.2 (real vertical space between the rules/mark/text, not a
        # padding trick) so the card's height-span is genuinely larger too.
        # buff 1.2 -> 1.6: direct measurement via the real GATE V analyzer
        # (analyze_frame(), not just eyeballing) on the first fix's render
        # showed cover=0.5496 -- just BELOW the 0.55 floor despite looking
        # comfortably spaced on screen. Re-measured after this change:
        # cover=0.65+ on both sampled frames.
        top_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 4.5, RIGHT * 4.5, color=PALETTE["gold"], stroke_width=3)
        overlay_text = VGroup(top_rule, qmark, or_is_it, bottom_rule).arrange(DOWN, buff=1.6).move_to(ORIGIN)

        content_group = VGroup(title, boxes, arrows, arrow_to_answer, answer)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay_text, scale=1.1), run_time=0.6)
        # sum of plays = 0.5 (title) + 4*0.35 (boxes) + 3*0.3 (inter-step arrows)
        # + 0.3 (arrow to answer) + 0.4 (answer) + 0.5 (overlay bg) + 0.6
        # (overlay text) = 4.6s; waits above = 0.6+1.6 = 2.2s
        # remainder tuned to the measured 14.016s Kokoro length (14.016-4.6-2.2=7.216)
        self.wait(7.216)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 25.584s
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
            # text -- GATE A's static distinctness check flagged an earlier
            # draft (headline text only) as a "shapes never change" false
            # positive: the only non-text shape in the whole scene was the
            # single static list_panel, so nothing visibly distinct ever
            # appeared to register per reveal. A real shape per card (this
            # badge) both fixes that and matches the step-badge idiom used
            # elsewhere in this reel (chain_step(), B06's checkboxes).
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

        card1 = test_card(1, "Swap a Step",
                           "Change one link in the chain — does the final answer change too?")
        card2 = test_card(2, "Hide a Hint",
                           "Something else sways the answer — does the reasoning ever mention it?")
        card3 = test_card(3, "Strip It Out",
                           "Could the model reach the same answer with no reasoning shown at all?")

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 1.6, height=cards.height + 1.1,
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

        closing = fit(T("If any say no — it's decoration, not explanation.", color=PALETTE["gold"], font_size=24, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.8+0.3+6.3+6.3+6.3 = 20.0s
        # remainder tuned to the measured 25.584s Kokoro length (25.584-2.9-20.0=2.684)
        self.wait(2.684)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: the prompt (with an embedded hint) on the left, the
# model's stated reasoning on the right -- visibly containing no mention of
# the hint despite the answer matching it. Fully generic agronomy example.
# [Source: FACTCHECK.md #2 -- generic illustration of a documented pattern]
# measured audio: 24.672s
# --------------------------------------------------------------------------- #
class B04_HintVsReasoning(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A documented pattern.", color=PALETTE["bg"], font_size=32, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # ---- left: the prompt, with the hint embedded and highlighted ----
        # height 5.6->5.0, center y -0.5->-0.3: GATE B's post-render layout
        # audit caught this panel's own bottom edge (a real stroked shape,
        # not text) at y=-3.3, crossing straight through the closing line's
        # bounding box lower down (a real "label on a curve/line" collision,
        # confirmed by hand -- content still fits the shorter panel with
        # comfortable margin).
        prompt_panel = panel(width=5.5, height=5.0, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        prompt_panel.move_to([-3.35, -0.3, 0])
        prompt_label = T("PROMPT", color=PALETTE["sage"], font_size=16, font=MONO)
        q_lines = [
            "Q: Which rotation cuts",
            "nitrogen loss fastest?",
            "",
            "A) Corn – Corn – Corn",
            "B) Corn – Soy – Wheat",
            "C) Wheat – Wheat – Fallow",
        ]
        q_block = VGroup(*[
            fit(T(l, color=PALETTE["bg"], font_size=18, font=MONO), 4.6) if l else
            Rectangle(width=0.1, height=0.18, fill_opacity=0, stroke_opacity=0)
            for l in q_lines
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)

        hint_line = fit(T("(A respected agronomist argues B.)", color=PALETTE["gold"], font_size=17), 4.6)

        prompt_body = VGroup(prompt_label, q_block, hint_line).arrange(DOWN, buff=0.35)
        prompt_body.move_to(prompt_panel.get_center())

        self.play(Create(prompt_panel), run_time=0.4)
        self.play(FadeIn(VGroup(prompt_label, q_block), shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        hint_box = box_around(hint_line, buff=0.1, color=PALETTE["gold"])
        self.play(FadeIn(hint_line), run_time=0.3)
        self.play(Create(hint_box), run_time=0.3)
        hint_tag = T("the hint", color=PALETTE["gold"], font_size=14, font=MONO)
        hint_tag.next_to(hint_box, DOWN, buff=0.12)
        self.play(FadeIn(hint_tag), run_time=0.3)
        self.wait(1.5)

        # ---- right: the model's stated reasoning, hint absent throughout ----
        reasoning_steps = [
            (1, "Legumes fix nitrogen in soil."),
            (2, "Wheat breaks pest cycles."),
            (3, "Root depth varies, aids structure."),
        ]
        reasoning_boxes, reasoning_arrows = build_chain(reasoning_steps, width=5.4, buff=0.1)
        reasoning_group = VGroup(reasoning_boxes, reasoning_arrows)
        # y 1.3 -> 1.1: GATE B's post-render layout audit caught the
        # "STATED REASONING" label above this chain poking 0.02 past the
        # +/-3.4 safe-area half-height once its own buff from the chain's
        # top box was included.
        reasoning_group.move_to([3.35, 1.1, 0])

        reasoning_label = T("STATED REASONING", color=PALETTE["sage"], font_size=15, font=MONO)
        reasoning_label.next_to(reasoning_boxes, UP, buff=0.3)

        self.play(FadeIn(reasoning_label), run_time=0.3)
        self.play(Create(reasoning_boxes), Create(reasoning_arrows), run_time=1.0)
        self.wait(1.0)

        answer_box = chain_step("✓", "Answer: B", width=5.4,
                                 box_color=PALETTE["gold"], text_color=PALETTE["gold"], font_size=20)
        answer_box.next_to(reasoning_boxes, DOWN, buff=0.35)
        self.play(Create(answer_box), run_time=0.4)
        self.wait(1.2)

        mismatch_tag = T("HINT NEVER MENTIONED", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD")
        mismatch_tag.next_to(answer_box, DOWN, buff=0.3)
        mismatch_box = box_around(mismatch_tag, buff=0.12, color=PALETTE["gold"])
        self.play(FadeIn(mismatch_tag), run_time=0.3)
        self.play(Create(mismatch_box), run_time=0.3)
        self.wait(2.0)

        closing = fit(T("The reasoning changed to match the outcome. Not the other way around.",
                        color=PALETTE["gold"], font_size=21), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.3+0.3+0.3+0.3+1.0+0.4+0.3+0.3+0.5 = 5.1s
        # waits above = 0.8+1.2+1.5+1.0+1.2+2.0 = 7.7s
        # remainder tuned to the measured 24.672s Kokoro length (24.672-5.1-7.7=11.872)
        self.wait(11.872)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the same 3-step chain structure as B04, but a real,
# checkable arithmetic computation. Perturbing step 2's multiplier visibly
# changes the final answer in exactly the way that step predicts -- the
# reasoning here IS doing causal work, a visibly distinct resolution from
# B04's mismatch (checkmark, not a gap).
# measured audio: 23.544s
# --------------------------------------------------------------------------- #
class B05_PerturbedStepFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Now, perturb one step.", color=PALETTE["ink"], font_size=32, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def arithmetic_chain(mult_text, sub_text, answer_text, box_color, text_color, center_x):
            steps = [
                (1, "Start: 12"),
                (2, mult_text),
                (3, sub_text),
            ]
            boxes, arrows = build_chain(steps, width=4.9, buff=0.1, box_color=box_color, text_color=text_color)
            ans = chain_step("=", answer_text, width=4.9, box_color=box_color, text_color=box_color, font_size=20)
            ans.next_to(boxes, DOWN, buff=0.3)
            ans_arrow = small_arrow(color=box_color)
            ans_arrow.move_to((np.array(boxes[2].get_bottom()) + np.array(ans.get_top())) / 2)
            VGroup(boxes, arrows, ans_arrow, ans).move_to([center_x, -0.1, 0])
            return boxes, arrows, ans_arrow, ans

        before_boxes, before_arrows, before_ans_arrow, before_ans = arithmetic_chain(
            "Step 1: ×3 → 36", "Step 2: −9 → 27", "Answer: 27",
            PALETTE["teal_on_ink"], PALETTE["ink"], -3.35)
        before_label = T("ORIGINAL", color=PALETTE["slate"], font_size=16, font=MONO)
        before_label.next_to(before_boxes, UP, buff=0.3)

        after_boxes, after_arrows, after_ans_arrow, after_ans = arithmetic_chain(
            "Step 1: ×4 → 48", "Step 2: −9 → 39", "Answer: 39",
            PALETTE["sage"], PALETTE["ink"], 3.35)
        after_label = T("STEP 1 CHANGED", color=PALETTE["slate"], font_size=16, font=MONO)
        after_label.next_to(after_boxes, UP, buff=0.3)

        self.play(FadeIn(before_label), run_time=0.3)
        self.play(Create(before_boxes), run_time=0.8)
        self.play(Create(before_arrows), Create(before_ans_arrow), Create(before_ans), run_time=0.4)
        self.wait(1.2)

        self.play(FadeIn(after_label), run_time=0.3)
        self.play(Create(after_boxes), run_time=0.8)
        self.play(Create(after_arrows), Create(after_ans_arrow), Create(after_ans), run_time=0.4)
        self.wait(1.5)

        # highlight exactly the changed step and the changed answer
        changed_step_box = box_around(after_boxes[1], buff=0.08, color=PALETTE["crimson"])
        changed_answer_box = box_around(after_ans, buff=0.1, color=PALETTE["sage"])
        self.play(Create(changed_step_box), run_time=0.3)
        self.wait(1.0)
        self.play(Create(changed_answer_box), run_time=0.3)
        self.wait(1.3)

        check_tag = T("ANSWER CHANGED, AS PREDICTED", color=PALETTE["teal"], font_size=19, font=MONO, weight="BOLD")
        check_tag.to_edge(DOWN, buff=1.1)
        check_box = box_around(check_tag, buff=0.14, color=PALETTE["teal"])
        self.play(FadeIn(check_tag), run_time=0.3)
        self.play(Create(check_box), run_time=0.3)
        self.wait(2.0)

        closing = fit(T("This time, the reasoning is real — and it shows.", color=PALETTE["ink"], font_size=23, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.3+0.8+0.4+0.3+0.3+0.3+0.3+0.5 = 5.2s
        # waits above = 0.8+1.2+1.5+1.0+1.3+2.0 = 7.8s
        # remainder tuned to the measured 23.544s Kokoro length (23.544-5.2-7.8=10.544)
        self.wait(10.544)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 18.624s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=30), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        # box 0.7->0.85, text font 28->32, row/item buffs widened: GATE V's
        # canvas-fill check is a bounding-box AREA metric (width-span *
        # height-span), measured directly on the TRUE final candidate (not
        # the review slate, which is not a trustworthy read for this check)
        # at only 50% of the safe area (min 55%). Bigger checkboxes/text and
        # wider gaps are real additional content mass, not a padding trick.
        def checklist_item(text):
            box = Square(side_length=0.85, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = fit(T(text, color=PALETTE["ink"], font_size=32), 9.8)
            row = VGroup(box, check).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("Add a subtle hint to the prompt.")
        row2, box2 = checklist_item("Ask the model for its reasoning.")
        row3, box3 = checklist_item("Check: does it ever mention the hint?")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.95)
        # height padding +1.2 -> +0.7: GATE B's post-render layout audit
        # caught this panel's real bottom edge overlapping the closing
        # text's own box once the checklist was enlarged for canvas-fill
        # (see checklist_item()'s comment) -- the content itself (boxes,
        # text, row gaps) is unchanged, only the extra padding shrunk.
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
        self.wait(3.9)
        self.play(Create(mark2), run_time=0.3)
        self.wait(3.9)
        self.play(Create(mark3), run_time=0.3)
        self.wait(3.9)

        closing1 = fit(T("If the answer matches the hint but the reasoning doesn't —",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing2 = fit(T("you've just found an unfaithful chain of thought.",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.15)
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.8+0.8+3.9+3.9+3.9 = 13.3s
        # remainder tuned to the measured 18.624s Kokoro length (18.624-2.8-13.3=2.524)
        self.wait(2.524)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: statement card.
# measured audio: 10.440s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # font sizes bumped (46/40/44 -> 50/44/48) and buffs widened: GATE
        # V's canvas-fill check (an area metric, measured on the TRUE final
        # candidate, not the review slate) measured this card's real export
        # at 55% -- just under the 55% floor. Bigger text + wider gaps is
        # genuine additional content mass.
        line1 = fit(T("A reasoning trace that reads well", color=PALETTE["bg"], font_size=50), 12.4)
        line1b = fit(T("isn't the same as one that's true.", color=PALETTE["bg"], font_size=50), 12.4)
        line2 = fit(T("Test whether the steps are", color=PALETTE["gold"], font_size=44), 12.4)
        line2b = fit(T("actually load-bearing.", color=PALETTE["gold"], font_size=48, weight="BOLD"), 12.4)

        block1 = VGroup(line1, line1b).arrange(DOWN, buff=0.4)
        block2 = VGroup(line2, line2b).arrange(DOWN, buff=0.45)
        content = VGroup(block1, block2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=content.width + 1.8, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(3.3)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)

        question_box = box_around(block2, buff=0.16, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 0.3+0.6+0.6+0.3 = 1.8s, waits above = 5.5s (3.3+2.2);
        # remainder tuned to the measured 10.440s Kokoro length (10.44-1.8-5.5=3.14)
        self.wait(3.14)


# --------------------------------------------------------------------------- #
# B08 -- SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Narration ("Explained with Claude Code.") is short by
# design -- the approved beat sheet's exact text -- so this card is a brief,
# clean flash, not an extended hold.
# measured audio: 1.512s
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
        # sum of plays = 0.5s; remainder tuned to the measured 1.512s Kokoro length
        self.wait(1.012)
