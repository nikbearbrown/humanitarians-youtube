"""
Manim scenes for 2026-11-13-context-window-limits
"Context Window Limits: The Budget That Doesn't Grow"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Teaches a reusable 3-question test -- Count the Tokens / Share the
Pool / Watch the Edge -- for reasoning about a model's context window: a
hard, fixed-size budget, measured in tokens (not characters or words),
shared by everything that goes into a request -- system instructions,
retrieved/pasted documents, conversation history, and the model's own
output allowance -- all at once, not in separate pools. Distinct from this
fellow's eight earlier videos: not hallucination (fabrication), not
tokenization (how text is chunked -- this video assumes that already
happened and is about what happens once the resulting count exceeds a fixed
ceiling), not lost-in-the-middle (position within content that DOES fit),
not chain-of-thought faithfulness (reasoning traces), not calibration
(confidence vs accuracy), not in-context learning limits (what a prompt can
teach as a MECHANISM -- this video is about the capacity CEILING itself and
what happens at/past it), and not Goodhart's Law (proxy metrics vs real
targets). The worked example (B04) and its falsifiability case (B05) are
both fully generic and hypothetical -- an invented, illustrative token
budget, no real model/vendor/benchmark is named, and no real
context-window size is cited as a universal fact. See FACTCHECK.md and
SOURCES.md.

B00_TitleCard                   -- silent title card (TITLE)
B01_ExecSummary                 -- spoken personal-intro card (EXEC-SUMMARY)
B02_FixedPoolHook               -- the context window is one shared pool -- did it tell you when it filled? (HOOK)
B03_ThreeQuestionsFramework     -- all 3 tests shown together, before any example (FRAMEWORK)
B04_SilentTruncation            -- a fixed budget; the oldest history quietly dropped (WORKED-EXAMPLE)
B05_ExplicitRejectionHolds      -- same overflow, but the system checks first and refuses outright (FALSIFIABILITY)
B06_AuditChecklist              -- the 3 tests as a concrete task to try today (SCAFFOLDED-TASK)
B07_Statement                   -- takeaway statement card (TAKEAWAY)
B08_BrandOutro                  -- @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around(), stat_row(),
metric_panel()) copied from this fellow's sibling reels
(2026-11-04-goodharts-law-proxy-metrics, 2026-10-28-in-context-learning-limits)
for visual consistency across the series. Plain Text (Pango) throughout,
never Integer/DecimalNumber/MathTex -- no LaTeX installed; every string
shown is a plain Text string.

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not a
pre-audio estimate, per the toolkit's audio-first rule:
B00=4.128 (silent, fixed target) B01=16.49 B02=22.61 B03=34.10 B04=31.75
B05=24.79 B06=28.13 B07=14.16 B08=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area).
Framing rules (top_rule/bottom_rule) on structure beats use a 0.5-unit buff
from the frame edge -- computed from final_frame_check.py's own SAFE
constants (a flat 5% margin on an 8-unit frame_height, i.e. a safe
half-height of 3.6), not guessed -- per the sibling reels' documented
edge-bleed fix, applied here from the start rather than re-discovered.

WORKED EXAMPLE CONTENT (B02/B04/B05) -- chosen per the build brief, fully
generic, illustrative, no real model/vendor named, no real context-window
size cited as a universal fact:

B02 (hook) shows a generic "CONTEXT WINDOW (FIXED BUDGET)" panel filling up
row by row, with no real system named, then poses the video's real
question: full -- did it tell you?

B04 (worked example) and B05 (falsifiability case) both use the same
invented, illustrative token budget -- ONE THOUSAND TOKENS, with a FIXED
850 tokens already committed to system instructions + a pasted-in document,
leaving 150 tokens of room, and a growing conversation history that pushes
past that room to 310 tokens -- with the identical numbers and the
identical overflow condition in both beats. The ONLY thing that changes
between B04 and B05 is whether the system checks the running total BEFORE
answering (B05, "CHECKED BEFORE ANSWERING") or not (B04, no check at all)
-- per the house falsifiability-stress-test requirement: change only the
variable the rubric's own test (#3, Watch the Edge) actually names, nothing
else. In B04 the oldest conversation turns are quietly dropped to make room
with nothing said about it (tagged TRUNCATED -- SILENTLY); in B05 the
identical overflow is caught immediately because the system checks the
total and refuses outright with an explicit error (tagged CAUGHT
IMMEDIATELY) -- a concrete illustration of the two documented, generic
classes of overflow behavior (silent truncation vs. explicit rejection),
not a claim that every system that goes over budget behaves either way.
All numbers are invented for teaching clarity, not a disclosed measurement
of any real system (see FACTCHECK.md #4).
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
                          # NEVER used for text/readable content on "bg" per
                          # house palette rule -- only as fill/stroke/accent.
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


def stat_row(label, value, label_color, value_color, font_size=22, value_font_size=None):
    """One 'LABEL : VALUE' budget row -- the core recurring visual idiom for
    this reel (a token count shown as a label + its current value), reused
    across B02/B04/B05."""
    value_font_size = value_font_size or font_size
    label_t = T(label, color=label_color, font_size=font_size - 4, font=MONO, weight="BOLD")
    value_t = T(value, color=value_color, font_size=value_font_size, font=MONO, weight="BOLD")
    return VGroup(label_t, value_t).arrange(RIGHT, buff=0.35)


def metric_panel(label_text, label_color, row_group, fill, stroke, buff=0.3):
    """A bordered panel holding a label ('CONTEXT WINDOW (FIXED BUDGET)' etc.)
    over a stack of stat_row()s -- used by B02/B04/B05. Returns (full_group,
    box, content) so callers can animate label/rows/box separately. content[1]
    is the row_group itself (NOT double-indexed) -- the sibling Goodhart's reel's
    BUILD-LOG documents a real content-correctness bug from an extra index
    into this exact return contract; this file indexes it directly."""
    label = T(label_text, color=label_color, font_size=18, font=MONO, weight="BOLD")
    content = VGroup(label, row_group).arrange(DOWN, buff=0.32)
    box = panel(width=content.width + 0.9, height=content.height + 0.55,
                fill=fill, stroke=stroke, corner_radius=0.15, opacity=1.0)
    box.move_to(content.get_center())
    return VGroup(box, content), box, content


# --------------------------------------------------------------------------- #
# B00 -- TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.128s -- fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Context Window Limits:", color=PALETTE["ink"], font_size=44, weight="BOLD"), 12.0)
        title_line2 = fit(T("The Budget That Doesn't Grow", color=PALETTE["ink"], font_size=32, weight="BOLD"), 12.2)
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
        # sum of plays = 1.6s; remainder tuned to the measured 4.128s silent track
        self.wait(2.528)


# --------------------------------------------------------------------------- #
# B01 -- EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 16.49s
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
            "This video: context window limits —",
            "the fixed budget every prompt",
            "has to fit inside, measured in tokens —",
            "and three tests for what happens when you go over.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=26), 11.4) for l in summary_lines
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
        # sum of plays = 2.1s; remainder tuned to the measured 16.49s Kokoro length (16.49-2.1=14.39)
        self.wait(14.39)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: a generic context-window budget panel filling up row by row --
# then an overlay posing the real question: full -- did it tell you?
# [Source: FACTCHECK.md #1/#2 -- generic/hypothetical, no real system named]
# measured audio: 22.61s
# --------------------------------------------------------------------------- #
class B02_FixedPoolHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("One prompt. One shared pool.", color=PALETTE["bg"], font_size=32), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        rows = VGroup(
            stat_row("INSTRUCTIONS", "150 TOK", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("DOCUMENT", "700 TOK", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("HISTORY", "GROWING", PALETTE["bg"], PALETTE["sage"]),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "CONTEXT WINDOW (FIXED BUDGET)", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.6)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        trend_label = T("MEASURED IN:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        trend_row = T("TOKENS", color=PALETTE["gold"], font_size=24, font=MONO, weight="BOLD")
        trend_block = VGroup(trend_label, trend_row).arrange(RIGHT, buff=0.35)
        trend_block.next_to(panel_group, DOWN, buff=0.55)
        self.play(FadeIn(trend_block), run_time=0.4)
        self.wait(0.5)

        # stacked DOWN, not chained RIGHT -- each line centers independently
        # at x=0 under trend_block, so no accumulated rightward drift can
        # push a later tag off-frame (the exact class of bug this beat hit
        # on the first pass: chaining three short tags RIGHT in one row
        # pushed the last one past the safe/hard frame edge).
        looks_good = T("NOT CHARACTERS", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD")
        looks_good.next_to(trend_block, DOWN, buff=0.3)
        self.play(FadeIn(looks_good), run_time=0.4)
        correct_tag = T("NOT WORDS EITHER", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        correct_tag.next_to(looks_good, DOWN, buff=0.22)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.4)
        same_tag = fit(T("BUT THE POOL ITSELF DOESN'T GROW.", color=PALETTE["sage"], font_size=20, font=MONO), 11.0)
        same_tag.next_to(bottom_rule, DOWN, buff=0.35)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # fluent + plausible, but the hook's whole point: fade content OUT fully
        # before fading the overlay IN (never a dim-behind-overlay trick that
        # leaves underlying Text mobjects at fill_opacity=1) -- a text-on-text
        # overlap bug the sibling reels' GATE B caught the hard way.
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Full.", color=PALETTE["bg"], font_size=48, weight="BOLD"), 10.0)
        overlay_line2 = fit(T("Did it tell you?", color=PALETTE["bg"], font_size=48, weight="BOLD"), 10.0)
        overlay_text = VGroup(overlay_line1, overlay_line2).arrange(DOWN, buff=0.2)
        top_rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule2 = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        overlay = VGroup(top_rule2, qmark, overlay_text, bottom_rule2).arrange(DOWN, buff=1.1).move_to(ORIGIN)

        content_group = VGroup(title, panel_group, trend_block, looks_good, correct_tag, bottom_rule, same_tag)
        self.play(FadeOut(content_group), run_time=0.5)
        self.play(FadeIn(overlay, scale=1.1), run_time=0.6)
        # sum of plays = 0.5+0.4+0.8+0.4+0.4+0.3+0.4+0.5+0.6 = 4.3s
        # waits above = 0.5+0.2+0.8+0.5+0.5+0.3 = 2.8s
        # (waits deliberately front-loaded so the FadeOut/FadeIn transition
        # lands well before GATE V's steady-state sample points -- copied
        # verbatim from the sibling reels' documented B02 timing fix, applied
        # here from the start rather than re-discovered)
        # remainder tuned to the measured 22.61s Kokoro length (22.61-4.3-2.8=15.51)
        self.wait(15.51)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 34.10s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions, before any example:", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.8)
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

        card1 = test_card(1, "Count the Tokens",
                           "Is this budget measured in tokens, not characters or words?")
        card2 = test_card(2, "Share the Pool",
                           "Do instructions, documents, history, and output draw from ONE budget?")
        card3 = test_card(3, "Watch the Edge",
                           "When it's exceeded, does it error loudly, or drop something quietly?")

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 1.6, height=cards.height + 1.1,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(DOWN * 0.15)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.3)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(8.5)

        closing = fit(T("A budget you can't see filling up is a budget you can't manage.",
                        color=PALETTE["gold"], font_size=23, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.8+0.3+8.5+8.5+8.5 = 26.6s
        # remainder tuned to the measured 34.10s Kokoro length (34.10-2.9-26.6=4.6)
        self.wait(4.6)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: a fixed budget, already mostly committed, and a
# growing conversation history that pushes past the room that's left --
# the oldest turns quietly dropped, nothing said about it. Tagged
# TRUNCATED -- SILENTLY.
# [Source: FACTCHECK.md #3/#4 -- generic illustration, no real model named]
# measured audio: 31.75s
# --------------------------------------------------------------------------- #
class B04_SilentTruncation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("A budget, under real pressure.", color=PALETTE["bg"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.68)
        # GATE V canvas-fill: this beat's steady-state frame gets a real
        # framing rule near the top edge (genuine added content mass
        # extending the bounding box toward the frame's hard top edge), not
        # a padding trick -- same idiom as B00/B01/B02's top rules, applied
        # from the start per the sibling reels' documented underfill
        # findings. Folded into the existing title-write play so total beat
        # timing is unchanged. Buff=0.5 computed from final_frame_check.py's
        # own SAFE constants (landscape safe half-height 3.6), not guessed.
        top_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("INSTRUCTIONS + DOCUMENT (FIXED)", "850 TOK", PALETTE["bg"], PALETTE["teal_on_ink"], font_size=22)
        history_row = stat_row("CONVERSATION HISTORY", "150 TOK", PALETTE["bg"], PALETTE["sage"], font_size=22)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "WHAT'S SHARING A 1,000-TOKEN BUDGET", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.move_to([0, 1.55, 0])

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        pressure_label = T("PRESSURE:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        pressure_val = T("CONVERSATION KEEPS GOING", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD")
        pressure_block = VGroup(pressure_label, pressure_val).arrange(RIGHT, buff=0.35)
        pressure_block.next_to(panel_group, DOWN, buff=0.5)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        # the "resolved" step: the fixed allocation never moves (it IS
        # fixed); only the history row's value updates, crossing past the
        # 150-token room that was left -- the exact mechanism the beat's
        # narration describes. No value is hidden or erased without a
        # visible replacement.
        new_history_val = T("310 TOK", color=PALETTE["crimson"], font_size=22, font=MONO, weight="BOLD")
        new_history_val.move_to(history_row[1].get_center())
        self.play(FadeOut(history_row[1]), FadeIn(new_history_val), run_time=0.4)
        self.wait(1.3)

        gap_tag = T("TRUNCATED — SILENTLY", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD")
        gap_tag.next_to(pressure_block, DOWN, buff=0.45)
        gap_box = box_around(gap_tag, buff=0.14, color=PALETTE["crimson"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("The reply still came back. Nobody saw what left.",
                        color=PALETTE["gold"], font_size=20), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.3+0.3+0.5 = 3.5s
        # waits above = 0.8+1.5+1.0+1.3+1.5 = 6.1s
        # remainder tuned to the measured 31.75s Kokoro length (31.75-3.5-6.1=22.15)
        self.wait(22.15)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the identical budget, the identical allocation, the
# identical overflow as B04 -- the ONLY change is that the system now checks
# the running total BEFORE answering. The same overflow happens, but it's
# caught immediately with an explicit error, tagged CAUGHT IMMEDIATELY, a
# visibly different resolution from B04's TRUNCATED -- SILENTLY.
# measured audio: 24.79s
# --------------------------------------------------------------------------- #
class B05_ExplicitRejectionHolds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Same pressure — now it checks first.", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.65)
        # GATE V canvas-fill note: same top/bottom framing-rule idiom as
        # B04, applied from the start (not retrofitted) since this beat's
        # content column is already narrower than B02's -- the sibling
        # Goodhart's reel's BUILD-LOG documents a real underfill regression
        # from skipping this on a narrower beat; pre-applied here instead.
        # Buff=0.5 matches B04's already-confirmed-safe clearance.
        top_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["slate"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("INSTRUCTIONS + DOCUMENT (FIXED)", "850 TOK", PALETTE["ink"], PALETTE["teal"], font_size=22)
        history_row = stat_row("CONVERSATION HISTORY", "150 TOK", PALETTE["ink"], PALETTE["slate"], font_size=22)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "WHAT'S SHARING THE SAME 1,000-TOKEN BUDGET", PALETTE["slate"], rows,
            fill=PALETTE["bg"], stroke=PALETTE["slate"])
        panel_group.next_to(title, DOWN, buff=0.55)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        # mark the checked row after it's on screen: a gold box + tag, not a
        # different row color from the start -- this is the ONE thing
        # different from B04 (the total is being checked), so it should
        # read as a flagged fact, matching this beat's own narration
        # ("checks the total before it answers"). Tag placed BELOW the
        # whole panel, never to the right of a row -- the sibling Goodhart's
        # reel's BUILD-LOG documents a real frame-extraction-only overlap
        # bug from placing an equivalent tag to the right of a row inside a
        # content-fitted panel; applied the safer placement here from the
        # start rather than re-discovering it.
        check_box = Rectangle(width=history_row.width + 0.3, height=history_row.height + 0.18,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        check_box.move_to(history_row.get_center())
        check_tag = T("CHECKED BEFORE ANSWERING", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD")
        check_tag.next_to(panel_group, DOWN, buff=0.3)
        self.play(Create(check_box), FadeIn(check_tag), run_time=0.4)
        self.wait(0.9)

        pressure_label = T("PRESSURE:", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        pressure_val = T("SAME AS BEFORE", color=PALETTE["slate"], font_size=20, font=MONO, weight="BOLD")
        pressure_block = VGroup(pressure_label, pressure_val).arrange(RIGHT, buff=0.35)
        pressure_block.next_to(VGroup(panel_group, check_tag), DOWN, buff=0.55)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.0)

        new_history_val = T("310 TOK", color=PALETTE["crimson"], font_size=22, font=MONO, weight="BOLD")
        new_history_val.move_to(history_row[1].get_center())
        self.play(FadeOut(history_row[1]), FadeIn(new_history_val), run_time=0.4)
        self.wait(0.6)

        caught_tag = T("CAUGHT IMMEDIATELY", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        caught_tag.next_to(pressure_block, DOWN, buff=0.45)
        caught_box = box_around(caught_tag, buff=0.14, color=PALETTE["teal"])
        self.play(FadeIn(caught_tag), run_time=0.3)
        self.play(Create(caught_box), run_time=0.3)
        self.wait(1.5)

        closing = fit(T("Same overflow — this time, it said so.",
                        color=PALETTE["ink"], font_size=22, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.65)
        bottom_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["slate"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.3+0.3+0.5 = 3.9s
        # waits above = 0.8+0.5+0.9+1.0+0.6+1.5 = 5.3s
        # remainder tuned to the measured 24.79s Kokoro length (24.79-3.9-5.3=15.59)
        self.wait(15.59)


# --------------------------------------------------------------------------- #
# B06 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 28.13s
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
            check = fit(T(text, color=PALETTE["ink"], font_size=28), 9.8)
            row = VGroup(box, check).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("Pick a system with a length or size limit.")
        row2, box2 = checklist_item("Go a little over it, on purpose.")
        row3, box3 = checklist_item("See what breaks — loudly, or silently.")

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
        self.wait(6.2)
        self.play(Create(mark2), run_time=0.3)
        self.wait(6.2)
        self.play(Create(mark3), run_time=0.3)
        self.wait(6.2)

        closing1 = fit(T("If something vanished without a word —",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing2 = fit(T("find out exactly what got dropped.",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.15)
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.8+0.8+6.2+6.2+6.2 = 20.2s
        # remainder tuned to the measured 28.13s Kokoro length (28.13-2.8-20.2=5.13)
        self.wait(5.13)


# --------------------------------------------------------------------------- #
# B07 -- TAKEAWAY: statement card.
# measured audio: 14.16s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("A context window isn't elastic —", color=PALETTE["bg"], font_size=36), 12.4)
        line1b = fit(T("it's a fixed budget for everything you put in.", color=PALETTE["bg"], font_size=36, weight="BOLD"), 12.4)
        line2 = fit(T("Going over it was never the real question.", color=PALETTE["gold"], font_size=38), 12.4)
        line2b = fit(T("Whether it told you is the one that matters.", color=PALETTE["gold"], font_size=40, weight="BOLD"), 12.4)

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
        # remainder tuned to the measured 14.16s Kokoro length (14.16-1.8-5.2=7.16)
        self.wait(7.16)


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
