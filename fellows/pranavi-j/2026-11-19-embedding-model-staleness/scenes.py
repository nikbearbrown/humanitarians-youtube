"""
Manim scenes for 2026-11-19-embedding-model-staleness
"Embedding Model Staleness: The Index That Quietly Split in Two"

General AI/STEM topic explainer (not a report of a live bug). Teaches a
reusable 3-question test -- Check the Checkpoint / Audit the Whole Index /
Watch for Silence -- for reasoning about embedding model staleness: an
embedding model maps text into a vector space shaped entirely by its own
training, so two different models (or two checkpoints of "the same" model)
place the same text in geometrically incompatible spaces, even when both
produce valid, same-dimensionality unit vectors. Distinct from this fellow's
nine earlier videos -- not hallucination, not tokenization, not
lost-in-the-middle, not chain-of-thought faithfulness, not calibration, not
in-context learning limits, not Goodhart's Law, not context window limits
(a request-time token-budget capacity question, not a stored-index geometry
question), and not the earlier general embeddings video (what similarity
means WITHIN one space -- this video is about a single index silently
containing vectors from more than one incompatible space). See FACTCHECK.md
and SOURCES.md. The ONE quantified claim in this video (B04/B05's mechanism)
is backed by a real, reproducible local demo in verification/ using two
real, named, open sentence-transformer models -- reported as one real run,
not a general benchmark. B06 names a real project (mycroft's rag.py) as an
honest design-choice illustration, confirmed by direct source read -- NOT a
bug report; there is no bug there, by construction (see FACTCHECK.md #6).

B00_TitleCard                   -- silent title card (TITLE)
B01_ExecSummary                 -- spoken personal-intro card (EXEC-SUMMARY)
B02_SplitGeometryHook           -- one index, two geometries -- did anything notice? (HOOK)
B03_ThreeQuestionsFramework     -- all 3 tests shown together, before any example (FRAMEWORK)
B04_SilentSplit                 -- an index silently splits after a model swap (WORKED-EXAMPLE)
B05_FullReembedHolds            -- same swap, but a full re-embed holds the line (FALSIFIABILITY)
B06_MycroftRealWorldNote        -- rag.py's real design choice, verbatim-quoted (REAL-WORLD-NOTE)
B07_AuditChecklist              -- the 3 tests as a concrete task to try today (SCAFFOLDED-TASK)
B08_Statement                   -- takeaway statement card (TAKEAWAY)
B09_BrandOutro                  -- @HumanitariansAI sign-off (SIGN-OFF)

All 10 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around(), stat_row(),
metric_panel()) copied from this fellow's sibling reels
(2026-11-13-context-window-limits, 2026-11-04-goodharts-law-proxy-metrics)
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
B00=4.128 (silent, fixed target) B01=17.78 B02=24.67 B03=29.23 B04=32.47
B05=23.11 B06=32.02 B07=24.22 B08=13.1 B09=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area).
Framing rules (top_rule/bottom_rule) on structure beats use a 0.5-unit buff
from the frame edge -- computed from final_frame_check.py's own SAFE
constants (a flat 5% margin on an 8-unit frame_height, i.e. a safe
half-height of 3.6), not guessed -- per the sibling reels' documented
edge-bleed fix, applied here from the start rather than re-discovered.

B06 ON-SCREEN CODE QUOTE NOTE: every quoted line is copied verbatim from the
real source files (mycroft's Core_Components/Regulatory_QA/backend/app/
rag.py and app/config.py and app/routers/chat.py), confirmed by direct read
immediately before writing this scene -- see FACTCHECK.md's "Verbatim
accuracy check" section. mycroft is read-only reference; nothing inside it
was modified.
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
    """One 'LABEL : VALUE' row -- the core recurring visual idiom for this
    reel (a model/dimension/rank fact shown as a label + its current
    value), reused across B02/B04/B05."""
    value_font_size = value_font_size or font_size
    label_t = T(label, color=label_color, font_size=font_size - 4, font=MONO, weight="BOLD")
    value_t = T(value, color=value_color, font_size=value_font_size, font=MONO, weight="BOLD")
    return VGroup(label_t, value_t).arrange(RIGHT, buff=0.35)


def metric_panel(label_text, label_color, row_group, fill, stroke, buff=0.3):
    """A bordered panel holding a label over a stack of stat_row()s -- used
    by B02/B04/B05. Returns (full_group, box, content) so callers can
    animate label/rows/box separately. content[1] is the row_group itself
    (NOT double-indexed) -- the sibling Goodhart's/CWL reels' BUILD-LOGs
    document a real content-correctness bug from an extra index into this
    exact return contract; this file indexes it directly."""
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

        title_line1 = fit(T("Embedding Model Staleness:", color=PALETTE["ink"], font_size=40, weight="BOLD"), 12.2)
        title_line2 = fit(T("The Index That Quietly Split in Two", color=PALETTE["ink"], font_size=30, weight="BOLD"), 12.2)
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
# measured audio: 17.78s
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
            "This video: embedding model staleness —",
            "why swapping the model that turns your",
            "documents into vectors can silently break",
            "similarity search — and three tests for it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=26), 11.6) for l in summary_lines
        ]).arrange(DOWN, buff=0.2)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=11.8, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 17.78s Kokoro length (17.78-2.1=15.68)
        self.wait(15.68)


# --------------------------------------------------------------------------- #
# B02 -- HOOK: a generic vector-index panel showing docs embedded by two
# different models at the same dimensionality, then an overlay posing the
# real question: two geometries -- did anything notice?
# [Source: FACTCHECK.md #1/#2 -- generic/hypothetical, no real model named]
# measured audio: 24.67s
# --------------------------------------------------------------------------- #
class B02_SplitGeometryHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("One index. Two geometries?", color=PALETTE["bg"], font_size=32), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.5)

        rows = VGroup(
            stat_row("MODEL A VECTORS", "384-DIM", PALETTE["bg"], PALETTE["teal_on_ink"]),
            stat_row("MODEL B VECTORS", "384-DIM", PALETTE["bg"], PALETTE["sage"]),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "VECTOR INDEX (ONE SPACE?)", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.next_to(title, DOWN, buff=0.6)

        self.play(Create(panel_box), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(panel_content, lag_ratio=0.12), run_time=0.8)
        self.wait(0.8)

        trend_label = T("SAME DIMENSION:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        trend_row = T("NOT COMPARABLE", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
        trend_block = VGroup(trend_label, trend_row).arrange(RIGHT, buff=0.35)
        trend_block.next_to(panel_group, DOWN, buff=0.55)
        self.play(FadeIn(trend_block), run_time=0.4)
        self.wait(0.5)

        # stacked DOWN, not chained RIGHT -- each line centers independently
        # at x=0 under trend_block, so no accumulated rightward drift can
        # push a later tag off-frame -- the exact bug class this idiom (used
        # verbatim from the CWL reel's own fixed B02) was already fixed to
        # avoid, applied here from the start.
        looks_good = T("NOT THE SAME ORIGIN", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD")
        looks_good.next_to(trend_block, DOWN, buff=0.3)
        self.play(FadeIn(looks_good), run_time=0.4)
        correct_tag = T("NOT THE SAME SCALE", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD")
        correct_tag.next_to(looks_good, DOWN, buff=0.22)
        self.play(FadeIn(correct_tag), run_time=0.3)
        self.wait(0.5)

        bottom_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.next_to(correct_tag, DOWN, buff=0.4)
        same_tag = fit(T("BUT NOTHING IN THE SEARCH CHECKS.", color=PALETTE["sage"], font_size=20, font=MONO), 11.0)
        same_tag.next_to(bottom_rule, DOWN, buff=0.35)
        self.play(Create(bottom_rule), FadeIn(same_tag), run_time=0.4)
        self.wait(0.3)

        # fluent + plausible, but the hook's whole point: fade content OUT fully
        # before fading the overlay IN (never a dim-behind-overlay trick that
        # leaves underlying Text mobjects at fill_opacity=1) -- a text-on-text
        # overlap bug the sibling reels' GATE B caught the hard way.
        qmark = T("?", color=PALETTE["gold"], font_size=150, weight="BOLD")
        overlay_line1 = fit(T("Two geometries.", color=PALETTE["bg"], font_size=44, weight="BOLD"), 10.5)
        overlay_line2 = fit(T("Did anything notice?", color=PALETTE["bg"], font_size=44, weight="BOLD"), 10.5)
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
        # verbatim from the sibling reels' documented B02 timing fix)
        # remainder tuned to the measured 24.67s Kokoro length (24.67-4.3-2.8=17.57)
        self.wait(17.57)


# --------------------------------------------------------------------------- #
# B03 -- FRAMEWORK: all 3 tests shown together, before any example.
# measured audio: 29.23s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions, before any example:", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.7)

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

        card1 = test_card(1, "Check the Checkpoint",
                           "Is every vector from the exact same model and version?")
        card2 = test_card(2, "Audit the Whole Index",
                           "Was EVERY existing vector recomputed, or just new ones?")
        card3 = test_card(3, "Watch for Silence",
                           "When geometries mix, does it error, or just rank worse?")

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        list_panel = panel(width=cards.width + 1.6, height=cards.height + 1.1,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(DOWN * 0.15)
        cards.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.wait(0.25)

        self.play(FadeIn(card1, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)
        self.play(FadeIn(card2, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)
        self.play(FadeIn(card3, shift=UP * 0.1), run_time=0.5)
        self.wait(7.1)

        closing = fit(T("A split you can't see is a split you can't fix.",
                        color=PALETTE["gold"], font_size=23, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.5+0.5+0.5 = 2.9s
        # waits above = 0.7+0.25+7.1+7.1+7.1 = 22.25s
        # remainder tuned to the measured 29.23s Kokoro length (29.23-2.9-22.25=4.08)
        self.wait(4.08)


# --------------------------------------------------------------------------- #
# B04 -- WORKED-EXAMPLE: a document store fully indexed with one embedding
# model, later switched to a newer model for new documents only -- the old
# vectors stay in the old geometry, and a query against the whole index at
# once quietly ranks them worse, with no error anywhere. Tagged
# SPLIT GEOMETRY -- SILENTLY.
# [Source: FACTCHECK.md #3/#4 -- generic illustration backed by this
# build's own real demo, see verification/demo_output.txt]
# measured audio: 32.47s
# --------------------------------------------------------------------------- #
class B04_SilentSplit(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("An index, under a real upgrade.", color=PALETTE["bg"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.68)
        # GATE V canvas-fill: a real framing rule near the top edge (genuine
        # added content mass extending the bounding box toward the frame's
        # hard top edge), not a padding trick -- same idiom as B00/B01/B02's
        # top rules, applied from the start. Buff=0.5 computed from
        # final_frame_check.py's own SAFE constants (landscape safe
        # half-height 3.6), not guessed.
        top_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.8)

        fixed_row = stat_row("EMBEDDED WITH MODEL A (OLD)", "820 DOCS", PALETTE["bg"], PALETTE["teal_on_ink"], font_size=22)
        history_row = stat_row("EMBEDDED WITH MODEL B (NEW)", "180 DOCS", PALETTE["bg"], PALETTE["sage"], font_size=22)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "ONE CORPUS, 1,000 DOCUMENTS", PALETTE["gold"], rows,
            fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        panel_group.move_to([0, 1.55, 0])

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(1.5)

        pressure_label = T("QUERY ARRIVES:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        pressure_val = T("EMBEDDED WITH MODEL B", color=PALETTE["gold"], font_size=20, font=MONO, weight="BOLD")
        pressure_block = VGroup(pressure_label, pressure_val).arrange(RIGHT, buff=0.35)
        pressure_block.next_to(panel_group, DOWN, buff=0.5)
        self.play(FadeIn(pressure_block), run_time=0.4)
        self.wait(1.2)

        # the "resolved" step: the fixed 820-doc allocation never moves (it
        # IS fixed, un-migrated); only the OLD document's search rank
        # updates, falling from #1 to #47 -- the exact mechanism the beat's
        # narration describes. No value is hidden or erased without a
        # visible replacement.
        rank_label = T("OLD DOC'S SEARCH RANK:", color=PALETTE["sage"], font_size=20, font=MONO, weight="BOLD")
        rank_val_before = T("#1", color=PALETTE["sage"], font_size=24, font=MONO, weight="BOLD")
        rank_row = VGroup(rank_label, rank_val_before).arrange(RIGHT, buff=0.35)
        rank_row.next_to(pressure_block, DOWN, buff=0.55)
        self.play(FadeIn(rank_row), run_time=0.4)
        self.wait(1.4)

        rank_val_after = T("#47", color=PALETTE["crimson"], font_size=24, font=MONO, weight="BOLD")
        rank_val_after.move_to(rank_val_before.get_center())
        self.play(FadeOut(rank_val_before), FadeIn(rank_val_after), run_time=0.4)
        self.wait(1.3)

        gap_tag = T("SPLIT GEOMETRY — SILENTLY", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD")
        gap_tag.next_to(rank_row, DOWN, buff=0.45)
        gap_box = box_around(gap_tag, buff=0.14, color=PALETTE["crimson"])
        self.play(FadeIn(gap_tag), run_time=0.3)
        self.play(Create(gap_box), run_time=0.3)
        self.wait(1.6)

        closing = fit(T("The answer still came back. Nobody saw the old doc fall.",
                        color=PALETTE["gold"], font_size=20), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.3+0.3+0.5 = 3.9s
        # waits above = 0.8+1.5+1.2+1.4+1.3+1.6 = 7.8s
        # remainder tuned to the measured 32.47s Kokoro length (32.47-3.9-7.8=20.77)
        self.wait(20.77)


# --------------------------------------------------------------------------- #
# B05 -- FALSIFIABILITY: the identical corpus and the identical switch event
# as B04 -- the ONLY change is that the team fully re-embeds every old
# document with the new model and rebuilds the index from scratch before
# serving a single query. No split ever exists, tagged
# FULLY RE-EMBEDDED -- NOTHING TO MIX, visibly different from B04's
# resolution.
# measured audio: 23.11s
# --------------------------------------------------------------------------- #
class B05_FullReembedHolds(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Same upgrade — fully re-embedded first.", color=PALETTE["ink"], font_size=28, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.65)
        # GATE V canvas-fill note: same top/bottom framing-rule idiom as
        # B04, applied from the start. Buff=0.5 matches B04's already-safe
        # clearance.
        top_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["slate"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.6)

        fixed_row = stat_row("EMBEDDED WITH MODEL A (OLD)", "0 DOCS", PALETTE["ink"], PALETTE["teal"], font_size=22)
        history_row = stat_row("EMBEDDED WITH MODEL B (NEW)", "1,000 DOCS", PALETTE["ink"], PALETTE["slate"], font_size=22)
        rows = VGroup(fixed_row, history_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        panel_group, panel_box, panel_content = metric_panel(
            "ONE CORPUS, 1,000 DOCUMENTS", PALETTE["slate"], rows,
            fill=PALETTE["bg"], stroke=PALETTE["slate"])
        panel_group.next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(panel_content[0]), run_time=0.3)
        self.play(Create(panel_box), FadeIn(panel_content[1], lag_ratio=0.1), run_time=0.8)
        self.wait(0.4)

        # mark the re-embed step after it's on screen: a gold box + tag, not
        # a different row color from the start -- this is the ONE thing
        # different from B04 (every old doc was re-embedded), so it should
        # read as a flagged fact, matching this beat's own narration. Tag
        # placed BELOW the whole panel, never beside a row -- the sibling
        # reels' BUILD-LOGs document a real frame-extraction-only overlap
        # bug from placing an equivalent tag beside a row inside a
        # content-fitted panel; applied the safer placement here from the
        # start.
        check_box = Rectangle(width=fixed_row.width + 0.3, height=fixed_row.height + 0.18,
                               stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0)
        check_box.move_to(fixed_row.get_center())
        check_tag = T("RE-EMBEDDED BEFORE SERVING", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD")
        check_tag.next_to(panel_group, DOWN, buff=0.3)
        self.play(Create(check_box), FadeIn(check_tag), run_time=0.4)
        self.wait(0.8)

        rank_label = T("OLD DOC'S SEARCH RANK:", color=PALETTE["teal"], font_size=20, font=MONO, weight="BOLD")
        rank_val = T("#1", color=PALETTE["slate"], font_size=24, font=MONO, weight="BOLD")
        rank_row = VGroup(rank_label, rank_val).arrange(RIGHT, buff=0.35)
        rank_row.next_to(VGroup(panel_group, check_tag), DOWN, buff=0.5)
        self.play(FadeIn(rank_row), run_time=0.4)
        self.wait(0.9)

        rank_val_after = T("#1", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        rank_val_after.move_to(rank_val.get_center())
        self.play(FadeOut(rank_val), FadeIn(rank_val_after), run_time=0.4)
        self.wait(0.5)

        caught_tag = T("FULLY RE-EMBEDDED — NOTHING TO MIX", color=PALETTE["teal"], font_size=18, font=MONO, weight="BOLD")
        caught_tag.next_to(rank_row, DOWN, buff=0.45)
        caught_box = box_around(caught_tag, buff=0.14, color=PALETTE["teal"])
        self.play(FadeIn(caught_tag), run_time=0.3)
        self.play(Create(caught_box), run_time=0.3)
        self.wait(1.3)

        closing = fit(T("Same upgrade — this time, one geometry held.",
                        color=PALETTE["ink"], font_size=22, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.65)
        bottom_rule = Line(LEFT * 5.7, RIGHT * 5.7, color=PALETTE["slate"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(Write(closing), Create(bottom_rule), run_time=0.5)
        # sum of plays = 0.5+0.3+0.8+0.4+0.4+0.4+0.3+0.3+0.5 = 3.9s
        # waits above = 0.6+0.4+0.8+0.9+0.5+1.3 = 4.5s
        # remainder tuned to the measured 23.11s Kokoro length (23.11-3.9-4.5=14.71)
        self.wait(14.71)


# --------------------------------------------------------------------------- #
# B06 -- REAL-WORLD-NOTE: a real, honest illustration (NOT a bug report) --
# mycroft's own rag.py sidesteps this entire bug class by rebuilding its
# vector store fresh on every chat request, so there's never a persisted
# index to go stale. Every quoted line is verbatim from the real source,
# confirmed by direct read (see FACTCHECK.md's verbatim accuracy check).
# measured audio: 32.02s
# --------------------------------------------------------------------------- #
class B06_MycroftRealWorldNote(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("A real design choice — not a bug.", color=PALETTE["ink"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.6)
        # GATE A static-distinctness note: this beat is otherwise all Text
        # (code quotes, tags), which the static pre-flight checker's
        # shape-distinctness pass flags as "shapes never change" if the
        # ONLY non-text shape in the whole scene is one panel created once
        # and never joined by another real shape -- the exact false-trigger
        # class B03's own module docstring documents from an earlier draft.
        # Fix applied here (not discovered via a failed render): a real top
        # rule line, matching B04/B05's own framing idiom, plus a real
        # per-row highlight box around each code quote as it's revealed
        # (mirroring B05's check_box), so the shape set actually changes
        # snapshot to snapshot.
        top_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["gold"], stroke_width=2.5)
        top_rule.to_edge(UP, buff=0.5)
        self.play(Write(title), Create(top_rule), run_time=0.5)
        self.wait(0.6)

        file_tag = T("rag.py — mycroft / Regulatory_QA backend", color=PALETTE["slate"], font_size=20, font=MONO, weight="BOLD")
        file_tag.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(file_tag), run_time=0.4)
        self.wait(0.6)

        def code_row(file_label, code_text, code_color):
            # PALETTE["slate"] is documented as broken contrast on an ink
            # background (0.04 luminance sep) -- caught by eye on a real
            # extracted frame (file labels "rag.py"/"config.py" were nearly
            # invisible), NOT by GATE V itself (whole-panel contrast sampling
            # didn't trip on this small a text region). PALETTE["sage"] is
            # the house-documented safe substitute for note/tag text on ink.
            lbl = T(file_label, color=PALETTE["sage"], font_size=16, font=MONO)
            code = T(code_text, color=code_color, font_size=22, font=MONO, weight="BOLD")
            return VGroup(lbl, code).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        row1 = code_row("rag.py", "model_name=settings.embedding_model", PALETTE["teal"])
        row2 = code_row("config.py", 'embedding_model: str = "all-MiniLM-L6-v2"', PALETTE["teal"])
        row3 = code_row("rag.py", "persist_directory=None", PALETTE["crimson"])
        code_rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        code_panel = panel(width=code_rows.width + 1.0, height=code_rows.height + 0.7,
                            fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.15, opacity=1.0)
        code_panel.next_to(file_tag, DOWN, buff=0.45)
        code_rows.move_to(code_panel.get_center())

        self.play(Create(code_panel), run_time=0.4)
        self.play(FadeIn(row1, shift=UP * 0.08), run_time=0.5)
        row1_box = box_around(row1, buff=0.1, color=PALETTE["teal_on_ink"])
        self.play(Create(row1_box), run_time=0.3)
        self.wait(1.7)
        self.play(FadeIn(row2, shift=UP * 0.08), run_time=0.5)
        row2_box = box_around(row2, buff=0.1, color=PALETTE["teal_on_ink"])
        self.play(Create(row2_box), run_time=0.3)
        self.wait(1.7)
        self.play(FadeIn(row3, shift=UP * 0.08), run_time=0.5)
        row3_box = box_around(row3, buff=0.1, color=PALETTE["crimson"])
        self.play(Create(row3_box), run_time=0.3)
        self.wait(1.9)

        tag1 = fit(T("REBUILT FRESH, EVERY SINGLE CHAT REQUEST", color=PALETTE["gold"], font_size=18, font=MONO, weight="BOLD"), 11.4)
        tag1.next_to(code_panel, DOWN, buff=0.4)
        self.play(FadeIn(tag1), run_time=0.4)
        self.wait(1.8)

        tag2 = fit(T("NO PERSISTED INDEX = NOTHING TO GO STALE", color=PALETTE["sage"], font_size=18, font=MONO, weight="BOLD"), 11.4)
        tag2.next_to(tag1, DOWN, buff=0.28)
        self.play(FadeIn(tag2), run_time=0.4)
        self.wait(1.6)

        closing = fit(T("Trade-off: full re-embed cost, on every single request.",
                        color=PALETTE["ink"], font_size=20), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        bottom_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["gold"], stroke_width=2.5)
        bottom_rule.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(closing, shift=UP * 0.1), Create(bottom_rule), run_time=0.4)
        # sum of plays = 0.5+0.4+0.4+0.5+0.3+0.5+0.3+0.5+0.3+0.4+0.4+0.4 = 4.9s
        # waits above = 0.6+0.6+1.7+1.7+1.9+1.8+1.6 = 9.9s
        # remainder tuned to the measured 32.02s Kokoro length (32.02-4.9-9.9=17.22)
        self.wait(17.22)


# --------------------------------------------------------------------------- #
# B07 -- SCAFFOLDED-TASK: the 3 tests restated as a concrete, actionable
# checklist (not a second copy of B03's framework card) to try today.
# measured audio: 24.22s
# --------------------------------------------------------------------------- #
class B07_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this today:", color=PALETTE["ink"], font_size=30), 11.8)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.6)

        def checklist_item(text):
            box = Square(side_length=0.85, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = fit(T(text, color=PALETTE["ink"], font_size=26), 9.8)
            row = VGroup(box, check).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("Open any index behind search or retrieval.")
        row2, box2 = checklist_item("Check: same embedding model and version, all of it?")
        row3, box3 = checklist_item("If not — full re-embed. Appending won't fix it.")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.9)
        list_panel = panel(width=items.width + 1.8, height=items.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.05)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(0.7)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(5.4)
        self.play(Create(mark2), run_time=0.3)
        self.wait(5.4)
        self.play(Create(mark3), run_time=0.3)
        self.wait(5.4)

        closing1 = fit(T("No partial migration exists for this —",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing2 = fit(T("one geometry, or a silent problem.",
                         color=PALETTE["ink"], font_size=20), 11.6)
        closing_block = VGroup(closing1, closing2).arrange(DOWN, buff=0.15)
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 0.6+0.7+5.4+5.4+5.4 = 17.5s
        # remainder tuned to the measured 24.22s Kokoro length (24.22-2.8-17.5=3.92)
        self.wait(3.92)


# --------------------------------------------------------------------------- #
# B08 -- TAKEAWAY: statement card.
# measured audio: 13.1s
# --------------------------------------------------------------------------- #
class B08_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("An embedding model's geometry isn't portable —", color=PALETTE["bg"], font_size=32), 12.4)
        line1b = fit(T("swap it, and the old vectors don't adapt.", color=PALETTE["bg"], font_size=32, weight="BOLD"), 12.4)
        line2 = fit(T("The fix was never incremental.", color=PALETTE["gold"], font_size=38), 12.4)
        line2b = fit(T("It's a full re-embed, every single time.", color=PALETTE["gold"], font_size=40, weight="BOLD"), 12.4)

        block1 = VGroup(line1, line1b).arrange(DOWN, buff=0.4)
        block2 = VGroup(line2, line2b).arrange(DOWN, buff=0.45)
        content = VGroup(block1, block2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=content.width + 1.8, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(2.6)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.0)

        question_box = box_around(block2, buff=0.16, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 0.3+0.6+0.6+0.3 = 1.8s, waits above = 4.6s (2.6+2.0);
        # remainder tuned to the measured 13.1s Kokoro length (13.1-1.8-4.6=6.7)
        self.wait(6.7)


# --------------------------------------------------------------------------- #
# B09 -- SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Narration ("Explained with Claude Code.") is short by
# design -- the approved beat sheet's exact text -- so this card is a brief,
# clean flash, not an extended hold.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B09_BrandOutro(Scene):
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
