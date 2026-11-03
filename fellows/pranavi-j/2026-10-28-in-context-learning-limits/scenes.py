"""
Manim scenes for 2026-10-28-in-context-learning-limits
"In-Context Learning: What the Prompt Can (and Can't) Teach"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Teaches a reusable 3-question test -- Spot the Mapping / Shuffle the
Set / Push Past the Window -- for telling what in-context learning (ICL: a
model conditioning on examples/instructions given in its prompt at inference
time, with NO weight updates) can actually do versus what it only looks like
it's doing. Distinct from this fellow's earlier hallucination (fabrication),
tokenization (how text is chunked), lost-in-the-middle (position in a long
context), chain-of-thought-faithfulness (reasoning traces), and calibration
(stated confidence vs accuracy) videos. The worked example (B04) and its
falsifiability case (B05) are both fully generic/hypothetical -- a toy,
invented Caesar-shift substitution rule, no real model, vendor, or benchmark
is named. See FACTCHECK.md and SOURCES.md.

B00_TitleCard                        -- silent title card (TITLE)
B01_ExecSummary                      -- spoken personal-intro card (EXEC-SUMMARY)
B02_LearningOrLocatingHook           -- examples complete a new case -- learning, or locating? (HOOK)
B03_ThreeTestsFramework              -- all 3 tests shown together, before any example (FRAMEWORK)
B04_ToyMappingWorkedExample          -- a made-up rule, taught purely by example pairs (WORKED-EXAMPLE)
B05_ReorderedFlippedFalsifiability   -- same task, reordered + one mapping flipped -- it breaks (FALSIFIABILITY)
B06_AuditChecklist                   -- the 3 tests as a concrete task to try today (SCAFFOLDED-TASK)
B07_Statement                        -- takeaway statement card (TAKEAWAY)
B08_BrandOutro                       -- @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's sibling reel 2026-10-21-calibration-why-confidence-isnt-accuracy for
visual consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex -- no LaTeX installed; every string shown is a
plain Text string, not typeset math.

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not a pre-audio
estimate, per the toolkit's audio-first rule:
B00=4.104 (silent, fixed target) B01=14.64 B02=21.26 B03=35.21 B04=28.49
B05=27.17 B06=27.70 B07=13.06 B08=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area). Frame/
panel dimensions for the structure beats (B00/B01/B07/B08) are copied
verbatim from the sibling reel's already-GATE-V-clean values for the same
beat roles, to avoid re-discovering the same underfill bugs from scratch.

WORKED EXAMPLE CONTENT (B02/B04/B05) -- chosen per the build brief, fully
generic, textbook-level, no real model/vendor named:

A toy, invented rule -- a simple Caesar-shift-by-3 substitution (A->D,
B->E, ... each letter shifted 3 places forward in the alphabet) -- is shown
ONLY as a handful of input/output example pairs in a "prompt," never named
or explained on screen. B02 (hook) and B04 (worked example) use the same
running set of 4 examples (CAT->FDW, DOG->GRJ, SUN->VXQ, BIG->ELJ) and the
same new, unseen query (RUN), which resolves correctly to UXQ -- chosen
because a letter-shift cipher is a well-established, textbook-level
illustrative device (not a real named benchmark) whose correctness is
mechanically checkable on screen without narration. B05 (falsifiability)
reorders the identical 4 examples and flips ONE mapping (DOG -> GRI instead
of the consistent GRJ) -- contradicting the otherwise-consistent rule the
other 3 examples still demonstrate -- then asks the identical new query
(RUN) again; this time the resolved output is shown as UXP (wrong,
inconsistent with the true shift-by-3 rule), tagged MISMATCH. This is a
fully generic, hypothetical illustration of two well-documented, broadly-
discussed ICL findings: (1) in-context learning is naturally framed as
pattern-location rather than new parameter learning (FACTCHECK.md #2), and
(2) few-shot performance can be sensitive to example order and to whether a
demonstration agrees with what the model's pretraining would otherwise favor
(FACTCHECK.md #4) -- no real model, vendor, or disclosed benchmark is named
or resembled anywhere in this file.
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
    created directly at a small font_size. See the sibling reel's BUILD-LOG.md for the
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


def pair_row(inp, out, in_color, out_color, font_size=24, arrow_color=None):
    """One 'INPUT -> OUTPUT' example-pair row for the prompt/example panels
    in B02/B04/B05 -- the core recurring visual idiom for this reel (a toy
    rule shown ONLY as example pairs, never named/explained on screen)."""
    inp_t = T(inp, color=in_color, font_size=font_size, font=MONO, weight="BOLD")
    arrow = T("->", color=arrow_color or PALETTE["gold"], font_size=font_size, font=MONO, weight="BOLD")
    out_t = T(out, color=out_color, font_size=font_size, font=MONO, weight="BOLD")
    return VGroup(inp_t, arrow, out_t).arrange(RIGHT, buff=0.3)


def example_panel(pairs, label_text, label_color, row_in_color, row_out_color,
                   fill, stroke, buff=0.26):
    """A bordered panel holding a label ('EXAMPLES IN THE PROMPT' etc.) over a
    stack of pair_row()s -- used by B02/B04/B05. Returns (full_group, box,
    content_block) so callers can animate label/rows/box separately (same
    two/three-group return pattern as the sibling reel's stat_bar(), kept for
    the same reason: direct references, no re-deriving offsets)."""
    label = T(label_text, color=label_color, font_size=18, font=MONO, weight="BOLD")
    rows = VGroup(*[pair_row(i, o, row_in_color, row_out_color) for i, o in pairs]).arrange(
        DOWN, buff=buff, aligned_edge=LEFT)
    content = VGroup(label, rows).arrange(DOWN, buff=0.32)
    box = panel(width=content.width + 0.9, height=content.height + 0.55,
                fill=fill, stroke=stroke, corner_radius=0.15, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.104s -- fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("In-Context Learning:", color=PALETTE["ink"], font_size=46, weight="BOLD"), 12.0)
        title_line2 = fit(T("What the Prompt Can (and Can't) Teach", color=PALETTE["ink"], font_size=32, weight="BOLD"), 12.2)
        title = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=PALETTE["gold"], stroke_width=3)
        handle = T("@HumanitariansAI", color=PALETTE["slate"], font_size=36)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=11.8, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.104s silent track
        self.wait(2.504)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 14.64s
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
            "This video: in-context learning —",
            "picking up a pattern from examples",
            "in the prompt, no weight updates —",
            "and three tests for what that can teach.",
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
        # sum of plays = 2.1s; remainder tuned to the measured 14.64s Kokoro length
        self.wait(12.54)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: a prompt window with a few example pairs, a new query resolving
# to a correct answer -- then an overlay posing the real question: is this
# learning, or is this locating?
# [Source: FACTCHECK.md #1/#3 -- generic/hypothetical, no real model named]
# measured audio: 21.26s
# --------------------------------------------------------------------------- #
class B02_LearningOrLocatingHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Show it a few examples...", color=PALETTE["bg"], font_size=34), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        pairs = [("CAT", "FDW"), ("DOG", "GRJ"), ("SUN", "VXQ")]
        panel_group, panel_box, panel_content = example_panel(
            pairs, "EXAMPLES IN THE PROMPT", PALETTE["gold"],
            PALETTE["bg"], PALETTE["teal_on_ink"],
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.6)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        query_label = T("NEW INPUT:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        query_row = pair_row("BIG", "?", PALETTE["bg"], PALETTE["gold"])
        query_block = VGroup(query_label, query_row).arrange(RIGHT, buff=0.35)
        query_block.next_to(panel_group, DOWN, buff=0.55)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(0.5)

        resolved = T("ELJ", color=PALETTE["sage"], font_size=24, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        correct_tag = T("CORRECT", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        correct_tag.next_to(query_block, RIGHT, buff=0.4)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(query_block, DOWN, buff=0.55)
        same_tag = fit(T("SAME CONTEXT. NO WEIGHTS CHANGED.", color=PALETTE["sage"], font_size=20, font=MONO), 11.0)
        same_tag.next_to(bottom_rule, DOWN, buff=0.35)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # fluent + plausible, but the hook's whole point: fade content OUT fully
        # before fading the overlay IN (never a dim-behind-overlay trick that
        # leaves underlying Text mobjects at fill_opacity=1) -- a text-on-text
        # overlap bug the sibling reel's GATE B caught the hard way.
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Learning,", color=PALETTE["bg"], font_size=48, weight="BOLD"), 10.0)
        overlay_line2 = fit(T("or locating?", color=PALETTE["bg"], font_size=48, weight="BOLD"), 10.0)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        content_group = VGroup(title, panel_group, query_block, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # sum of plays = 0.5+0.4+0.8+0.4+0.4+0.3+0.4+0.5+0.6 = 4.3s
        # waits above = 0.5+0.2+0.8+0.5+0.5+0.3 = 2.8s
        # (waits deliberately front-loaded so the FadeOut/FadeIn transition
        # lands by ~t=7.1s, well before GATE V's steady-state sample points --
        # an earlier draft held content until t=10.0s, putting the 50% sample
        # a few frames into the overlay's own FadeIn at near-zero opacity,
        # which GATE V correctly flagged as an empty-frame MAJOR on direct
        # measurement, not a review-slate false positive this time)
        # remainder tuned to the measured 21.26s Kokoro length (21.26-4.3-2.8=14.16)
        self.wait(14.16)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 35.21s
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
            # never change" false positive. A real shape per card (this
            # badge) fixes that.
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

        card1 = test_card(1, "Spot the Mapping",
                           "Can you tell, from the examples, what pattern they point toward?")
        card2 = test_card(2, "Shuffle the Set",
                           "Reorder, recount, or reselect the examples — does the answer survive?")
        card3 = test_card(3, "Push Past the Window",
                           "Does it need more than fits the prompt, or a capability never latent at all?")

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 1.6, height=cards.height + 1.1,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(DOWN * 0.15)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(9.0)

        closing = fit(T("If the pattern only holds for one ordering — that's the boundary.",
                        color=PALETTE["gold"], font_size=23, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.8+0.3+9.0+9.0+9.0 = 28.1s
        # remainder tuned to the measured 35.21s Kokoro length (35.21-2.9-28.1=4.21)
        self.wait(4.21)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: a made-up rule, shown only as example pairs in a
# prompt, correctly applied to a brand-new input -- "located, not learned."
# [Source: FACTCHECK.md #2/#3 -- generic illustration, no real model named]
# measured audio: 28.49s
# --------------------------------------------------------------------------- #
class B04_ToyMappingWorkedExample(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A made-up rule, taught by example.", color=PALETTE["bg"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.68)
        # GATE V canvas-fill MAJOR on the TRUE final candidate (not the review
        # slate, which showed 0 MAJOR here): this beat's steady-state frame
        # measured 53% of the safe area (min 55%). Fixed with a real framing
        # rule near the top edge (genuine added content mass extending the
        # bounding box toward the frame's hard top edge), not a padding trick
        # -- same idiom as B00/B01/B02's top rules. Folded into the existing
        # title-write play so total beat timing is unchanged.
        top_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        pairs = [("CAT", "FDW"), ("DOG", "GRJ"), ("SUN", "VXQ"), ("BIG", "ELJ")]
        panel_group, panel_box, panel_content = example_panel(
            pairs, "RULE: UNKNOWN — SHOWN ONLY AS EXAMPLES", PALETTE["gold"],
            PALETTE["bg"], PALETTE["teal_on_ink"],
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.move_to([0, 1.65, 0])

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        query_label = T("NEW INPUT:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        query_row = pair_row("RUN", "?", PALETTE["bg"], PALETTE["gold"])
        query_block = VGroup(query_label, query_row).arrange(RIGHT, buff=0.35)
        query_block.next_to(panel_group, DOWN, buff=0.55)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(1.0)

        resolved = T("UXQ", color=PALETTE["sage"], font_size=24, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        self.wait(1.3)

        gap_tag = T("LOCATED, NOT LEARNED", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD")
        gap_tag.next_to(query_block, DOWN, buff=0.45)
        gap_box = box_around(gap_tag, buff=0.14, color=PALETTE["gold"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("No new fact was learned — a pattern already in reach was found.",
                        color=PALETTE["gold"], font_size=20), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.3+0.3+0.5 = 3.5s
        # waits above = 0.8+1.5+1.0+1.3+1.5 = 6.1s
        # remainder tuned to the measured 28.49s Kokoro length (28.49-3.5-6.1=18.89)
        self.wait(18.89)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the identical task, reordered, with one mapping
# flipped against the otherwise-consistent rule -- the same new query now
# resolves inconsistently (MISMATCH), a visibly different resolution from
# B04's clean LOCATED tag.
# measured audio: 27.17s
# --------------------------------------------------------------------------- #
class B05_ReorderedFlippedFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Now, reorder it — and flip one.", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        pairs = [("BIG", "ELJ"), ("SUN", "VXQ"), ("DOG", "GRI"), ("CAT", "FDW")]
        flip_index = 2  # DOG -> GRI is the flipped mapping (true rule gives GRJ)
        panel_group, panel_box, panel_content = example_panel(
            pairs, "SAME EXAMPLES — REORDERED", PALETTE["slate"],
            PALETTE["ink"], PALETTE["teal"],
            fill=PALETTE["bg"], stroke=PALETTE["slate"])
        panel_group.next_to(title, DOWN, buff=0.55)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        # mark the flipped row after it's on screen: a crimson box + tag, not
        # a different row color from the start -- the flip should read as an
        # event, matching this beat's own narration ("flip just one").
        rows = panel_content[1]
        flipped_row = rows[flip_index]
        flip_box = Rectangle(width=flipped_row.width + 0.3, height=flipped_row.height + 0.18,
                              stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        flip_box.move_to(flipped_row.get_center())
        flip_tag = T("FLIPPED", color=PALETTE["crimson"], font_size=16, font=MONO, weight="BOLD")
        flip_tag.next_to(flip_box, RIGHT, buff=0.3)
        self.play(Create(flip_box), FadeIn(flip_tag), run_time=0.4)
        self.wait(0.9)

        query_label = T("NEW INPUT:", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        query_row = pair_row("RUN", "?", PALETTE["ink"], PALETTE["slate"])
        query_block = VGroup(query_label, query_row).arrange(RIGHT, buff=0.35)
        query_block.next_to(VGroup(panel_group, flip_tag), DOWN, buff=0.55)
        self.play(FadeIn(query_block), run_time=0.4)
        self.wait(1.0)

        resolved = T("UXP", color=PALETTE["crimson"], font_size=24, font=MONO, weight="BOLD")
        resolved.move_to(query_row[2].get_center())
        self.play(FadeOut(query_row[2]), FadeIn(resolved), run_time=0.4)
        self.wait(0.6)

        mismatch_tag = T("MISMATCH", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD")
        mismatch_tag.next_to(query_block, DOWN, buff=0.45)
        mismatch_box = box_around(mismatch_tag, buff=0.14, color=PALETTE["crimson"])
        self.play(FadeIn(mismatch_tag), run_time=0.3)
        self.play(Create(mismatch_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("Same task, same count — one flipped example, and it breaks.",
                        color=PALETTE["ink"], font_size=22, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.65)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.3+0.3+0.5 = 3.9s
        # waits above = 0.8+0.5+0.9+1.0+0.6+1.5 = 5.3s
        # remainder tuned to the measured 27.17s Kokoro length (27.17-3.9-5.3=17.97)
        self.wait(17.97)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 27.70s
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
            check = fit(T(text, color=PALETTE["ink"], font_size=30), 9.8)
            row = VGroup(box, check).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("Invent a rule with no real-world meaning.")
        row2, box2 = checklist_item("Test new inputs — then shuffle the examples.")
        row3, box3 = checklist_item("Flip one mapping — check if it still holds.")

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
        self.wait(6.0)
        self.play(Create(mark2), run_time=0.3)
        self.wait(6.0)
        self.play(Create(mark3), run_time=0.3)
        self.wait(6.0)

        closing1 = fit(T("If the answers only hold for the original order —",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing2 = fit(T("you've found the edge of what the prompt can teach.",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.15)
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.8+0.8+6.0+6.0+6.0 = 19.6s
        # remainder tuned to the measured 27.70s Kokoro length (27.70-2.8-19.6=5.3)
        self.wait(5.3)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: statement card.
# measured audio: 13.06s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("In-context learning is pattern-location,", color=PALETTE["bg"], font_size=38), 12.4)
        line1b = fit(T("not instant new learning.", color=PALETTE["bg"], font_size=44, weight="BOLD"), 12.4)
        line2 = fit(T("Bounded by what's already latent,", color=PALETTE["gold"], font_size=38), 12.4)
        line2b = fit(T("and by what fits, stably, in the prompt.", color=PALETTE["gold"], font_size=40, weight="BOLD"), 12.4)

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
        # remainder tuned to the measured 13.06s Kokoro length (13.06-1.8-5.2=6.06)
        self.wait(6.06)


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
