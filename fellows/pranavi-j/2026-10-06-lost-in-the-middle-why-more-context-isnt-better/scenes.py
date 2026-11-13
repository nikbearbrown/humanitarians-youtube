"""
Manim scenes for 2026-10-06-lost-in-the-middle-why-more-context-isnt-better
"Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer"

General AI/STEM topic explainer (not a report of the fellow's own engineering
work). Describes the well-documented "lost in the middle" effect in
long-context language models qualitatively — no real model/vendor is named
or benchmarked, no fabricated percentage/statistic is shown. The worked
example (B04/B05, a long onboarding document with one buried fact) is fully
generic/illustrative. See FACTCHECK.md and SOURCES.md.

B00_TitleCard               — silent title card (TITLE)
B01_ExecSummary               — spoken personal-intro card (EXEC-SUMMARY)
B02_TwoDocumentsHook           — short vs long document, same fact (HOOK)
B03_AttentionCurveDiagram      — real U-shaped attention-strength curve (MECHANISM)
B04_BuriedFactMiss             — fact buried in the middle, model misses it (WORKED-EXAMPLE)
B05_RepositionedFactFound      — same fact moved to start/end, model finds it (FALSIFIABILITY)
B06_AuditChecklist             — the 3-question rubric as a task checklist (SCAFFOLDED-TASK)
B07_Statement                  — takeaway statement card (TAKEAWAY)
B08_BrandOutro                 — @HumanitariansAI sign-off (SIGN-OFF)

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion.
Palette + house idioms (fit(), T(), panel(), box_around()) copied from this
fellow's sibling reels (2026-09-22-hallucination-why-sounding-sure-isnt-being-right,
2026-09-29-tokenization-why-ai-cant-count-its-own-letters) for visual
consistency across the series. Plain Text (Pango) throughout, never
Integer/DecimalNumber/MathTex — no LaTeX installed, this reel has no math
typesetting (the attention curve is a plotted ParametricFunction, not MathTex).

CRITICAL HOUSE-STYLE RULE: Manim's Text() has a real empirically-confirmed
Pango/Cairo rendering bug where creating Text() directly at font_size <= ~24
inserts phantom gaps inside words (e.g. "video" -> "v ideo"). Every piece of
on-screen text in this file goes through T() below, never Text() directly.

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured*
Kokoro audio duration (beat_sheet.json -> actual_duration_s), not the
pre-audio estimate, per the toolkit's audio-first rule:
B00=4.06 (silent, fixed target) B01=16.90 B02=16.97 B03=24.00 B04=21.60
B05=15.60 B06=28.27 B07=11.23 B08=1.51.

CANVAS-FILL NOTE: every beat below wraps its real content in a generously
sized, visibly bordered frame/panel sized from the content's OWN measured
bounds (never an oversized invisible rectangle used only to pass a metric),
per this project's canvas-fill requirement (55-80% of the safe area).

MECHANISM VISUALS (B03/B04/B05): the "lost in the middle" curve is a real
plotted U-shape (ParametricFunction over a position axis from 0=start to
1=end, y = low + (high-low)*(2t-1)^2 — high at both ends, low in the
middle), drawn over a horizontal bar representing the context, never just
asserted in narration or shown as a static label. No specific numeric value
is printed on the curve or axis — fully qualitative, per FACTCHECK.md. The
same curve_point()/attention_curve_mobject() helpers build a small reusable
"mini curve" inset in B04 (red marker at the low middle) and B05 (sage
marker at a high end) so the worked example and its resolution visually tie
back to B03's mechanism.
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


def document_stack(num_lines, width, line_color=None):
    """A tall stack of horizontal Lines standing in for dense body text —
    varied widths (every 4th line short) so it reads as paragraph text, not
    a uniform ladder. Returns the VGroup of lines; caller indexes into it to
    find/highlight a specific "buried fact" line."""
    line_color = line_color or PALETTE["slate"]
    lines = VGroup()
    for i in range(num_lines):
        w = width * (0.55 if i % 4 == 3 else 0.92)
        ln = Line(LEFT * w / 2, RIGHT * w / 2, stroke_color=line_color, stroke_width=3)
        lines.add(ln)
    lines.arrange(DOWN, buff=0.1)
    return lines


def curve_y(t, low_y, high_y):
    """The U-shape: high at both ends (t=0, t=1), low in the middle (t=0.5).
    Fully qualitative — no numeric axis is ever drawn or printed."""
    return low_y + (high_y - low_y) * ((2 * t - 1) ** 2)


def attention_curve_mobject(width, low_y, high_y, color, stroke_width=5, y_shift=0.0):
    half = width / 2

    def f(t):
        x = -half + t * width
        y = curve_y(t, low_y, high_y) + y_shift
        return np.array([x, y, 0])

    return ParametricFunction(f, t_range=[0, 1], color=color, stroke_width=stroke_width)


def curve_point(t, width, low_y, high_y, y_shift=0.0):
    half = width / 2
    x = -half + t * width
    y = curve_y(t, low_y, high_y) + y_shift
    return np.array([x, y, 0])


def curve_fill_area(width, low_y, high_y, bar_top_y, color, opacity=0.15, samples=44, y_shift=0.0):
    """A shaded polygon between the curve and the bar's top edge — real
    additional content mass under the curve (a 'terrain' fill), not just a
    bare line, to keep the diagram visually rich."""
    half = width / 2
    top_pts = [curve_point(i / (samples - 1), width, low_y, high_y, y_shift) for i in range(samples)]
    bottom_pts = [np.array([half, bar_top_y, 0]), np.array([-half, bar_top_y, 0])]
    poly = Polygon(*top_pts, *bottom_pts, stroke_width=0, fill_color=color, fill_opacity=opacity)
    return poly


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# measured (silent) duration: 4.06s — fixed target, not measured narration.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_line1 = fit(T("Lost in the Middle:", color=PALETTE["ink"], font_size=48, weight="BOLD"), 12.0)
        title_line2 = fit(T("Why More Context Doesn't", color=PALETTE["ink"], font_size=36, weight="BOLD"), 12.0)
        title_line3 = fit(T("Guarantee a Better Answer", color=PALETTE["ink"], font_size=36, weight="BOLD"), 12.0)
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
        # sum of plays = 1.6s; remainder tuned to the measured 4.06s silent track
        self.wait(2.46)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 16.90s
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
            "This video: a strange, well-documented",
            "habit of AI models reading long documents",
            "— they're much better at using facts near",
            "the start or end than facts buried in the",
            "middle, even when nothing else changes.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=25), 11.0) for l in summary_lines
        ]).arrange(DOWN, buff=0.18)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=11.6, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 16.488s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 16.90s -> wait 14.8)
        self.wait(14.39)


# --------------------------------------------------------------------------- #
# B02 — HOOK: a short paragraph (fact found every time) vs a long document
# (same fact, buried, missed) — both labeled with the same question. Neither
# document names a real model. [Source: FACTCHECK.md — generic/hypothetical]
# measured audio: 16.97s
# --------------------------------------------------------------------------- #
class B02_TwoDocumentsHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same fact. Same question. Different length.", color=PALETTE["bg"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # ---- LEFT: short paragraph, fact near the middle of a short block ----
        left_panel = panel(width=5.2, height=4.6, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        left_panel.move_to([-3.5, -0.5, 0])
        left_label = T("SHORT PARAGRAPH", color=PALETTE["sage"], font_size=16, font=MONO)
        left_lines = document_stack(5, 4.3, line_color=PALETTE["bg"])
        left_hl = left_lines[2]
        left_body = VGroup(left_label, left_lines).arrange(DOWN, buff=0.35)
        left_body.move_to(left_panel.get_center())

        # ---- RIGHT: long document, same fact buried deep inside the stack ----
        right_panel = panel(width=5.2, height=4.6, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        right_panel.move_to([3.5, -0.5, 0])
        right_label = T("LONG DOCUMENT", color=PALETTE["sage"], font_size=16, font=MONO)
        right_lines = document_stack(18, 4.3, line_color=PALETTE["bg"])
        right_hl = right_lines[9]
        right_body = VGroup(right_label, right_lines).arrange(DOWN, buff=0.3)
        right_body.move_to(right_panel.get_center())

        self.play(Create(left_panel), Create(right_panel), run_time=0.5)
        self.play(FadeIn(left_body, shift=UP * 0.1), FadeIn(right_body, shift=UP * 0.1), run_time=0.6)
        self.wait(1.5)

        # the SAME fact in both — a gold highlight box on each one's buried/found line
        left_box = box_around(left_hl, buff=0.1, color=PALETTE["gold"])
        right_box = box_around(right_hl, buff=0.1, color=PALETTE["gold"])
        question = fit(T("“Where does the key fact sit?”", color=PALETTE["gold"], font_size=22), 11.0)
        question.next_to(VGroup(left_panel, right_panel), UP, buff=0.15).move_to([0, 2.6, 0])
        self.play(Create(left_box), Create(right_box), run_time=0.5)
        self.wait(1.5)

        left_tag = T("FOUND", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD")
        left_tag.next_to(left_panel, DOWN, buff=0.3)
        right_tag = T("MISSED?", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
        right_tag.next_to(right_panel, DOWN, buff=0.3)
        self.play(FadeIn(left_tag), FadeIn(right_tag), run_time=0.5)
        self.wait(2.0)

        zinger = fit(T("Only the length changed. Not the fact.", color=PALETTE["gold"], font_size=26), 11.0)
        zinger.to_edge(DOWN, buff=0.65)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.5+0.5+0.6+0.5+0.5+0.5 = 3.1s
        # waits above = 1.0+1.5+1.5+2.0 = 6.0s
        # remainder tuned to the measured 16.97s Kokoro length (16.97-3.1-6.0=7.87)
        self.wait(7.87)


# --------------------------------------------------------------------------- #
# B03 — MECHANISM: a real U-shaped attention-strength curve plotted over a
# horizontal bar representing the context (start...middle...end). High at
# both ends, dipping in the middle — no specific numeric value anywhere.
# [Source: FACTCHECK.md — well-documented, generic qualitative effect]
# measured audio: 24.00s
# --------------------------------------------------------------------------- #
class B03_AttentionCurveDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Attention isn't spread evenly across a long context.", color=PALETTE["ink"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        BAR_W = 10.4
        BAR_Y = -1.3
        LOW_Y = -0.85
        HIGH_Y = 1.75

        # bar fill_opacity 0.18 -> 0.4: GATE V's frame-level QC flagged a real
        # low-contrast MAJOR (0.25-0.29 luminance separation, under the 0.3
        # floor) — a pale, low-opacity slate wash plus a gold curve stroke
        # both sit too close to the cream background's luminance. Verified by
        # computing each color's blended luminance by hand, not a false
        # positive.
        bar = Rectangle(width=BAR_W, height=0.5, fill_color=PALETTE["slate"], fill_opacity=0.4,
                         stroke_color=PALETTE["slate"], stroke_width=2)
        bar.move_to([0, BAR_Y, 0])
        bar_top = BAR_Y + 0.25

        # NOTE: an earlier draft also drew a semi-transparent curve_fill_area()
        # "terrain" shade under the curve — dropped for the same low-contrast
        # reason. Curve stroke color switched gold -> teal (same color used
        # for the "HIGH" labels): teal's luminance separation from the cream
        # background is ~0.67, comfortably over the 0.3 floor, vs gold's
        # ~0.25 (the measured defect). The solid-stroke curve + bar + ticks
        # still satisfy "a real U-shaped curve diagram" on their own.
        curve = attention_curve_mobject(BAR_W, LOW_Y, HIGH_Y, PALETTE["teal"], stroke_width=7)

        start_tick = Line(UP * 0.12, DOWN * 0.12, color=PALETTE["ink"], stroke_width=3).move_to([-BAR_W / 2, BAR_Y, 0])
        mid_tick = Line(UP * 0.12, DOWN * 0.12, color=PALETTE["ink"], stroke_width=3).move_to([0, BAR_Y, 0])
        end_tick = Line(UP * 0.12, DOWN * 0.12, color=PALETTE["ink"], stroke_width=3).move_to([BAR_W / 2, BAR_Y, 0])

        start_label = T("start", color=PALETTE["slate"], font_size=20).next_to(start_tick, DOWN, buff=0.18)
        mid_label = T("middle", color=PALETTE["slate"], font_size=20).next_to(mid_tick, DOWN, buff=0.18)
        end_label = T("end", color=PALETTE["slate"], font_size=20).next_to(end_tick, DOWN, buff=0.18)

        self.play(Create(bar), run_time=0.4)
        self.play(Create(curve), run_time=1.3)
        self.play(Create(start_tick), Create(mid_tick), Create(end_tick),
                  FadeIn(start_label), FadeIn(mid_label), FadeIn(end_label), run_time=0.5)
        self.wait(0.5)

        high_left = T("HIGH", color=PALETTE["teal"], font_size=22, font=MONO, weight="BOLD")
        high_left.move_to(curve_point(0.0, BAR_W, LOW_Y, HIGH_Y) + UP * 0.45 + RIGHT * 0.1)
        high_right = T("HIGH", color=PALETTE["teal"], font_size=22, font=MONO, weight="BOLD")
        high_right.move_to(curve_point(1.0, BAR_W, LOW_Y, HIGH_Y) + UP * 0.45 + LEFT * 0.1)
        self.play(FadeIn(high_left), FadeIn(high_right), run_time=0.5)
        self.wait(3.0)

        # LOW label placed ABOVE the curve's dip (not below it): below would
        # land inside the context bar's own rectangle — a real
        # label-on-shape collision caught by GATE B's post-render layout
        # audit (box overlapping the bar at y in [-1.55,-1.05]). Above the
        # dip clears both the bar and the curve itself (the curve stays
        # near its low value for a wide stretch around the center).
        low_mid = T("LOW", color=PALETTE["crimson"], font_size=22, font=MONO, weight="BOLD")
        low_mid.move_to(curve_point(0.5, BAR_W, LOW_Y, HIGH_Y) + UP * 0.55)
        self.play(FadeIn(low_mid), run_time=0.5)
        self.wait(3.0)

        # notes placed lower and narrower (9.5 vs the title's 11.8): GATE B's
        # post-render layout audit caught a real text-on-text collision
        # between the title (bottom edge ~y=3.05) and a note placed at
        # y=3.0 — moved down to y=2.3/1.9 with a narrower width so they also
        # clear the HIGH labels sitting near the curve's end apexes.
        note1 = fit(T("Not an inability to see that part of the text —", color=PALETTE["slate"], font_size=22), 9.5)
        note1.move_to([0, 2.3, 0])
        self.play(FadeIn(note1, shift=UP * 0.1), run_time=0.5)
        self.wait(2.5)

        note2 = fit(T("just unevenly distributed attention across it.", color=PALETTE["slate"], font_size=22), 9.5)
        note2.move_to([0, 1.85, 0])
        self.play(FadeIn(note2, shift=UP * 0.1), run_time=0.5)
        self.wait(2.5)

        closing = fit(T("The beginning and end get disproportionately more.", color=PALETTE["ink"], font_size=24, weight="BOLD"), 11.6)
        closing.to_edge(DOWN, buff=0.68)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+1.3+0.5+0.5+0.5+0.5+0.5+0.5 = 5.2s
        # waits above = 1.0+0.5+3.0+3.0+2.5+2.5 = 12.5s
        # remainder tuned to the measured 24.00s Kokoro length (24.00-5.2-12.5=6.3)
        self.wait(6.3)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: a long onboarding document, the key fact buried in
# the middle section, the model's answer shown as missed/wrong. A small
# inset reuses B03's curve shape with a red marker at the low middle point.
# [Source: FACTCHECK.md — fully generic/hypothetical onboarding scenario]
# measured audio: 21.60s
# --------------------------------------------------------------------------- #
class B04_BuriedFactMiss(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Buried in the middle.", color=PALETTE["bg"], font_size=32, weight="BOLD"), 11.5)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # ---- left: the document, fact highlighted near the middle ----
        doc_panel = panel(width=5.3, height=5.4, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        doc_panel.move_to([-3.3, -0.2, 0])
        doc_header = T("ONBOARDING DOCUMENT", color=PALETTE["sage"], font_size=15, font=MONO)
        doc_lines = document_stack(16, 4.4, line_color=PALETTE["bg"])
        doc_body = VGroup(doc_header, doc_lines).arrange(DOWN, buff=0.3)
        doc_body.move_to(doc_panel.get_center())

        self.play(Create(doc_panel), run_time=0.4)
        self.play(FadeIn(doc_body, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)

        fact_line = doc_lines[8]
        fact_box = box_around(fact_line, buff=0.09, color=PALETTE["gold"])
        # label placed in the OPEN GAP between the two panels (x in roughly
        # [-0.65, 0.65], clear of both panels' own edges at any y), not
        # next_to the box itself — GATE B's post-render layout audit caught
        # the original next_to(fact_box, RIGHT) placement overflowing past
        # doc_panel's own right edge into its rounded-rectangle stroke (the
        # highlighted line is nearly panel-width wide, leaving no room
        # beside it inside the panel). A narrow (<=1.1) label centered at
        # x=0 stays left of qa_panel's left edge (0.65) regardless of y.
        fact_label = fit(T("fact here", color=PALETTE["gold"], font_size=14, font=MONO), 1.2)
        fact_label.move_to([0, fact_box.get_y(), 0])
        self.play(Create(fact_box), run_time=0.3)
        self.play(FadeIn(fact_label), run_time=0.3)
        self.wait(2.0)

        # ---- right: the question/answer card, answer shown as a miss ----
        qa_panel = panel(width=5.3, height=3.0, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        qa_panel.move_to([3.3, 1.2, 0])
        qa_q = fit(T("“What's the start date?”", color=PALETTE["sage"], font_size=20, font=MONO), 4.8)
        qa_a = fit(T("“Not stated in this document.”", color=PALETTE["bg"], font_size=19), 4.8)
        qa_content = VGroup(qa_q, qa_a).arrange(DOWN, buff=0.3)
        qa_content.move_to(qa_panel.get_center())
        self.play(Create(qa_panel), run_time=0.4)
        self.play(FadeIn(qa_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        miss_tag = T("MISSED", color=PALETTE["gold"], font_size=24, font=MONO, weight="BOLD")
        miss_tag.next_to(qa_panel, DOWN, buff=0.3)
        miss_box = box_around(miss_tag, buff=0.1, color=PALETTE["gold"])
        self.play(FadeIn(miss_tag), run_time=0.3)
        self.play(Create(miss_box), run_time=0.3)
        self.wait(2.0)

        # ---- mini attention-curve inset tying back to B03, red marker at middle ----
        MINI_W, MINI_LOW, MINI_HIGH = 4.0, -0.25, 0.55
        mini_curve = attention_curve_mobject(MINI_W, MINI_LOW, MINI_HIGH, PALETTE["teal_on_ink"], stroke_width=4)
        mini_curve.move_to([3.3, -1.9, 0])
        marker = Dot(point=mini_curve.get_center() + curve_point(0.5, MINI_W, MINI_LOW, MINI_HIGH) - curve_point(0.5, MINI_W, MINI_LOW, MINI_HIGH), radius=0.1, color=PALETTE["crimson"])
        # place the marker exactly at the curve's own middle point (low dip)
        marker.move_to(mini_curve.point_from_proportion(0.5))
        mini_label = fit(T("LOW ATTENTION HERE", color=PALETTE["gold"], font_size=15, font=MONO), 3.8)
        mini_label.next_to(mini_curve, DOWN, buff=0.2)
        self.play(Create(mini_curve), run_time=0.6)
        self.play(FadeIn(marker, scale=1.5), FadeIn(mini_label), run_time=0.4)
        self.wait(1.5)

        closing = fit(T("Right there. Just not where it reliably looked.", color=PALETTE["gold"], font_size=22), 11.2)
        closing.to_edge(DOWN, buff=0.65)
        self.play(Write(closing), run_time=0.5)
        # sum of plays = 0.5+0.4+0.5+0.3+0.3+0.4+0.5+0.3+0.3+0.6+0.4+0.5 = 5.0s
        # waits above = 1.0+1.0+2.0+2.0+2.0+1.5 = 9.5s
        # remainder tuned to the measured 21.60s Kokoro length (21.60-5.0-9.5=7.1)
        self.wait(7.1)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: the same document, same fact, same question, moved
# to the start — the model now finds it. Sage marker at a high end of the
# mini curve, visually distinct from B04's red middle marker.
# measured audio: 15.60s
# --------------------------------------------------------------------------- #
class B05_RepositionedFactFound(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same document. Same fact. Moved.", color=PALETTE["bg"], font_size=30, weight="BOLD"), 11.6)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        doc_panel = panel(width=5.3, height=5.4, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        doc_panel.move_to([-3.3, -0.2, 0])
        doc_header = T("ONBOARDING DOCUMENT", color=PALETTE["sage"], font_size=15, font=MONO)
        doc_lines = document_stack(16, 4.4, line_color=PALETTE["bg"])
        doc_body = VGroup(doc_header, doc_lines).arrange(DOWN, buff=0.3)
        doc_body.move_to(doc_panel.get_center())

        self.play(Create(doc_panel), run_time=0.4)
        self.play(FadeIn(doc_body, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        # the SAME fact, now near the start of the same document. Label
        # placed in the open gap between the two panels (same fix as B04's
        # analogous label — see its comment) rather than next_to the box,
        # which overflowed past doc_panel's own right edge.
        fact_line = doc_lines[1]
        fact_box = box_around(fact_line, buff=0.09, color=PALETTE["sage"])
        fact_label = fit(T("moved here", color=PALETTE["sage"], font_size=14, font=MONO), 1.2)
        fact_label.move_to([0, fact_box.get_y(), 0])
        self.play(Create(fact_box), run_time=0.3)
        self.play(FadeIn(fact_label), run_time=0.3)
        self.wait(1.5)

        qa_panel = panel(width=5.3, height=3.0, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        qa_panel.move_to([3.3, 1.2, 0])
        qa_q = fit(T("“What's the start date?”", color=PALETTE["sage"], font_size=20, font=MONO), 4.8)
        qa_a = fit(T("“Stated on page one: March 2024.”", color=PALETTE["bg"], font_size=18), 4.8)
        qa_content = VGroup(qa_q, qa_a).arrange(DOWN, buff=0.3)
        qa_content.move_to(qa_panel.get_center())
        self.play(Create(qa_panel), run_time=0.4)
        self.play(FadeIn(qa_content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        found_tag = T("FOUND", color=PALETTE["sage"], font_size=24, font=MONO, weight="BOLD")
        found_tag.next_to(qa_panel, DOWN, buff=0.3)
        found_box = box_around(found_tag, buff=0.1, color=PALETTE["sage"])
        self.play(FadeIn(found_tag), run_time=0.3)
        self.play(Create(found_box), run_time=0.2)
        self.wait(1.5)

        MINI_W, MINI_LOW, MINI_HIGH = 4.0, -0.25, 0.55
        mini_curve = attention_curve_mobject(MINI_W, MINI_LOW, MINI_HIGH, PALETTE["teal_on_ink"], stroke_width=4)
        mini_curve.move_to([3.3, -1.9, 0])
        marker = Dot(radius=0.1, color=PALETTE["sage"])
        marker.move_to(mini_curve.point_from_proportion(0.03))
        mini_label = fit(T("HIGH ATTENTION HERE", color=PALETTE["sage"], font_size=15, font=MONO), 3.8)
        mini_label.next_to(mini_curve, DOWN, buff=0.2)
        self.play(Create(mini_curve), run_time=0.5)
        self.play(FadeIn(marker, scale=1.5), FadeIn(mini_label), run_time=0.3)
        self.wait(1.0)

        closing = fit(T("Nothing about the fact changed. Only its position did.", color=PALETTE["sage"], font_size=21), 11.4)
        closing.to_edge(DOWN, buff=0.65)
        self.play(Write(closing), run_time=0.4)
        # sum of plays = 0.5+0.4+0.4+0.3+0.3+0.4+0.5+0.3+0.2+0.5+0.3+0.4 = 4.5s
        # waits above = 1.0+0.8+1.5+1.5+1.5+1.0 = 7.3s
        # remainder tuned to the measured 15.60s Kokoro length (15.60-4.5-7.3=3.8)
        self.wait(3.8)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: the 3-question rubric restated as a concrete
# checklist to run on your own next long-context prompt.
# measured audio: 28.27s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this on your next long prompt:", color=PALETTE["ink"], font_size=28), 11.8)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # box 0.5->0.75, text font 25->34, row/item buffs widened: GATE V's
        # canvas-fill check measured this beat's real candidate export at
        # only 47% of the safe area (min 55%) at the 50% sample (title +
        # panel + first 2 checked rows, before the closing line appears) —
        # a real underfill, confirmed by direct frame inspection (the
        # checklist card was small and centered with large empty margins on
        # all sides). Bigger checkboxes/text and wider gaps between rows is
        # genuine additional content mass.
        def checklist_item(text):
            box = Square(side_length=0.75, color=PALETTE["teal"], stroke_width=4, fill_opacity=0)
            check = T(text, color=PALETTE["ink"], font_size=34)
            row = VGroup(box, fit(check, 11.4)).arrange(RIGHT, buff=0.5)
            return row, box

        row1, box1 = checklist_item("How long is the context?")
        row2, box2 = checklist_item("Where does the key fact actually sit?")
        row3, box3 = checklist_item("Would moving it change whether it's found?")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.9)
        list_panel = panel(width=items.width + 1.4, height=items.height + 1.0,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.1)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(1.0)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["teal"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["teal"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(6.5)
        self.play(Create(mark2), run_time=0.3)
        self.wait(6.5)
        self.play(Create(mark3), run_time=0.3)
        self.wait(5.5)

        closing = fit(T("A real blind spot — not a reason to distrust the model,", color=PALETTE["ink"], font_size=22), 11.6)
        closing2 = fit(T("a reason to put the important part where it's seen.", color=PALETTE["ink"], font_size=22), 11.6)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.15)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # 2-line closing's real bottom edge at y=-3.45, outside the +/-3.4
        # safe-area half-height on the true rendered frame.
        closing_block.to_edge(DOWN, buff=0.68)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.6+0.3+0.3+0.3+0.4 = 2.8s
        # waits above = 1.0+1.0+6.5+6.5+5.5 = 20.5s
        # remainder tuned to the measured 28.27s Kokoro length (28.27-2.8-20.5=4.97)
        self.wait(4.97)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 11.23s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # font sizes bumped (38/38/38/32/32 -> 48/48/48/40/44) and buffs
        # widened: GATE V's canvas-fill check measured this beat's real
        # candidate export at only 49% of the safe area (min 55%) — a real
        # underfill, not a false positive (confirmed by direct frame
        # inspection). Bigger text + wider gaps is genuine additional
        # content mass, not an oversized invisible frame around the same
        # content.
        line1 = fit(T("A model that misses a fact buried", color=PALETTE["bg"], font_size=48), 12.0)
        line1b = fit(T("on page fifty isn't failing to", color=PALETTE["bg"], font_size=48), 12.0)
        line1c = fit(T("understand it.", color=PALETTE["bg"], font_size=48), 12.0)
        line2 = fit(T("It's reading unevenly — and that changes", color=PALETTE["gold"], font_size=40), 12.0)
        line2b = fit(T("where you put what you need it to find.", color=PALETTE["gold"], font_size=44, weight="BOLD"), 12.0)

        block1 = VGroup(line1, line1b, line1c).arrange(DOWN, buff=0.35)
        block2 = VGroup(line2, line2b).arrange(DOWN, buff=0.4)
        content = VGroup(block1, block2).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame = panel(width=content.width + 1.8, height=content.height + 1.2,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.5)

        question_box = box_around(block2, buff=0.16, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        # sum of plays = 0.3+0.6+0.6+0.3 = 1.8s, waits above = 6.5s (4.0+2.5);
        # remainder tuned to the measured 11.23s Kokoro length (11.23-1.8-6.5=2.93)
        self.wait(2.93)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, explained with Claude Code, in for Sai
# Pranavi J. Narration ("Explained with Claude Code.") is short by
# design — the approved beat sheet's exact text — so this card is a brief,
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
