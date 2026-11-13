"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-06-lost-in-the-middle-why-more-context-isnt-better
"Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer"

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the
full-length portrait companion command — NOT a Shorts-style cut: no beats
dropped, no duration cap, no rewritten outro, no added endcard (see
brutalist/docs/PIPELINE-SAFETY.md, "Isolated portrait companions and
Shorts"). All 9 parent beats are kept; every mp3 is reused byte-for-byte
from the parent's mp3/ folder (see vertical/beat_sheet.json, written by
shorts.py). Every beat here is a Manim GRAPHIC beat, so THE REFORMAT RULE's
auto center-cut never applies (generated graphics are never cropped) — each
class below is a genuine portrait RE-LAYOUT of the parent ../scenes.py
composition, authored by hand for a 1080x1920 canvas (rendered at
2160x3840 for the true 4K vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so the parent file's y-axis safe/hard bounds — to_edge(UP/DOWN, buff=...)
— carry over UNCHANGED; only frame_width shrinks). What changes is
frame_width: ~4.5 instead of 14.222 — a hard edge of only +/-2.25 and a
safe half-width of ~1.95. MAX_W = 3.6 is this file's general content-width
budget (leaves real margin on each side), copied from this fellow's sibling
reels' own portrait-redesign convention.

Beat-by-beat redesign notes:
  B00 TitleCard               — title re-wrapped onto 4 narrower lines.
  B01 ExecSummary               — badge stacked ABOVE name/role; summary re-wrapped.
  B02 TwoDocumentsHook           — parent's LEFT/RIGHT documents -> TOP/BOTTOM stack.
  B03 AttentionCurveDiagram      — curve narrowed to MAX_W; labels re-wrapped.
  B04 BuriedFactMiss             — parent's LEFT doc / RIGHT Q&A -> TOP doc / BOTTOM Q&A stack.
  B05 RepositionedFactFound      — same TOP/BOTTOM stack redesign as B04.
  B06 AuditChecklist             — already single-column; items re-wrapped narrower.
  B07 Statement                  — centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                 — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around()/document_stack()/curve helpers
are copied from ../scenes.py for visual continuity. Nothing about WHAT is
said or WHEN changes here (every self.play/self.wait duration matches
../scenes.py beat-for-beat, so total runtime matches the landscape master
exactly) — only how it is laid out for the narrow canvas.
"""

from manim import *
import numpy as np

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup — BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait — every
# coordinate in this file is designed against a 4.5-wide frame, so without
# this fix everything would render ~3.2x too small and clustered dead-center.
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
MAX_W = 3.6   # general portrait content-width budget (safe half-width ~1.95)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
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


def document_stack(num_lines, width, line_color=None):
    line_color = line_color or PALETTE["slate"]
    lines = VGroup()
    for i in range(num_lines):
        w = width * (0.55 if i % 4 == 3 else 0.92)
        ln = Line(LEFT * w / 2, RIGHT * w / 2, stroke_color=line_color, stroke_width=3)
        lines.add(ln)
    lines.arrange(DOWN, buff=0.08)
    return lines


def curve_y(t, low_y, high_y):
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


def curve_fill_area(width, low_y, high_y, bar_top_y, color, opacity=0.15, samples=36, y_shift=0.0):
    half = width / 2
    top_pts = [curve_point(i / (samples - 1), width, low_y, high_y, y_shift) for i in range(samples)]
    bottom_pts = [np.array([half, bar_top_y, 0]), np.array([-half, bar_top_y, 0])]
    return Polygon(*top_pts, *bottom_pts, stroke_width=0, fill_color=color, fill_opacity=opacity)


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, re-wrapped onto 4 narrower lines.
# measured (silent) duration: 4.06s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Lost in the Middle:", "Why More Context", "Doesn't Guarantee", "a Better Answer"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=36, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.46)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 16.90s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.5, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=26, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=25, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: a strange,",
            "well-documented habit of",
            "AI models reading long",
            "documents — they're much",
            "better at using facts near",
            "the start or end than facts",
            "buried in the middle, even",
            "when nothing else changes.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.13)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        # height 7.3 -> 7.1: GATE V's frame-level check caught this frame's
        # real top/bottom edges at y=+/-3.65, outside the portrait safe
        # area's +/-3.6 half-height (the frame's own stroke, not the text,
        # was the content crossing the line — confirmed by direct pixel
        # inspection of the ink bounding box).
        frame = panel(width=MAX_W + 0.3, height=7.1, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 16.488s Kokoro
        # length (2026-10-20 name-retrofit: 16.488 - 2.1 = 14.388)
        self.wait(14.39)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's LEFT/RIGHT documents -> TOP/BOTTOM stack.
# measured audio: 16.97s
# --------------------------------------------------------------------------- #
class B02_TwoDocumentsHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same fact. Same question.", color=PALETTE["bg"], font_size=22), MAX_W)
        title2 = fit(T("Different length.", color=PALETTE["bg"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.6)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        def doc_block(label_text, n_lines, hl_idx, panel_h):
            p = panel(width=MAX_W + 0.1, height=panel_h, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
            lbl = T(label_text, color=PALETTE["sage"], font_size=13, font=MONO)
            lines = document_stack(n_lines, MAX_W - 0.5, line_color=PALETTE["bg"])
            body = VGroup(lbl, lines).arrange(DOWN, buff=0.18)
            body.move_to(p.get_center())
            return VGroup(p, body), lines[hl_idx], lbl

        # labels shortened (SHORT PARAGRAPH/LONG DOCUMENT -> SHORT DOC/LONG
        # DOC) to leave real room beside them for the FOUND/MISSED? tag —
        # see below.
        top_group, top_hl, top_lbl = doc_block("SHORT DOC", 5, 2, 1.85)
        bot_group, bot_hl, bot_lbl = doc_block("LONG DOC", 13, 7, 2.55)
        stack = VGroup(top_group, bot_group).arrange(DOWN, buff=0.25)
        stack.move_to(ORIGIN).shift(DOWN * 0.25)

        self.play(Create(top_group[0]), Create(bot_group[0]), run_time=0.5)
        self.play(FadeIn(top_group[1], shift=UP * 0.08), FadeIn(bot_group[1], shift=UP * 0.08), run_time=0.6)
        self.wait(1.5)

        top_box = box_around(top_hl, buff=0.08, color=PALETTE["gold"])
        bot_box = box_around(bot_hl, buff=0.08, color=PALETTE["gold"])
        self.play(Create(top_box), Create(bot_box), run_time=0.5)
        self.wait(1.5)

        # tags placed next to each panel's OWN header label (inside the
        # panel's own safe bounds), not next_to the whole panel group — GATE
        # B's post-render layout audit caught the original next_to(...,
        # RIGHT) placement landing off-frame (box starting at x=2.0, outside
        # the +/-1.95 safe half-width — portrait has no spare width beside a
        # panel that already spans most of the safe width).
        top_tag = fit(T("FOUND", color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD"), 0.85)
        top_tag.next_to(top_lbl, RIGHT, buff=0.12)
        bot_tag = fit(T("MISSED?", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD"), 0.85)
        bot_tag.next_to(bot_lbl, RIGHT, buff=0.12)
        self.play(FadeIn(top_tag), FadeIn(bot_tag), run_time=0.5)
        self.wait(2.0)

        zinger = fit(T("Only the length changed.\nNot the fact.", color=PALETTE["gold"], font_size=18, line_spacing=1.15), MAX_W)
        zinger.to_edge(DOWN, buff=0.65)
        self.play(Write(zinger), run_time=0.5)
        self.wait(7.87)


# --------------------------------------------------------------------------- #
# B03 — MECHANISM: curve narrowed to MAX_W; labels re-wrapped.
# measured audio: 24.00s
# --------------------------------------------------------------------------- #
class B03_AttentionCurveDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Attention isn't spread", color=PALETTE["ink"], font_size=22), MAX_W)
        title2 = fit(T("evenly across a long context.", color=PALETTE["ink"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # title's real top edge at y=3.45, outside the +/-3.4 safe-area
        # half-height on the true rendered portrait frame.
        title_block.to_edge(UP, buff=0.68)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        # BAR_W narrowed MAX_W(3.6) -> 3.2: GATE B's post-render layout audit
        # caught the start/end tick labels' real bounding boxes landing just
        # outside the +/-1.95 safe half-width (e.g. box=[-1.98,...]) — the
        # bar's own half-width (1.8) left no margin once "start"/"end" text
        # extended past the tick mark. A narrower bar leaves real clearance.
        # BAR_Y/LOW_Y/HIGH_Y all shifted down by 1.0 (same curve shape/height,
        # just lower in the frame): GATE V's canvas-fill check measured this
        # beat's real 50%-sample candidate at only 53% of the safe area (min
        # 55%) — confirmed by direct frame inspection: at that sample point
        # (title + curve + HIGH/LOW + note1 only; note2/closing appear later,
        # synced to narration) everything was clustered in the top half,
        # leaving the whole bottom half empty. Moving the diagram down uses
        # real additional vertical space without changing its shape or any
        # play/wait timing.
        BAR_W = 3.2
        BAR_Y = -1.1
        LOW_Y = -1.55
        HIGH_Y = -0.1

        # bar fill_opacity 0.18 -> 0.4 and curve gold -> teal: see
        # ../scenes.py's B03 for the GATE V low-contrast MAJOR this fixes
        # (0.25-0.29 luminance separation on the landscape master, under the
        # 0.3 floor) — same fix applied here pre-emptively.
        bar = Rectangle(width=BAR_W, height=0.4, fill_color=PALETTE["slate"], fill_opacity=0.4,
                         stroke_color=PALETTE["slate"], stroke_width=2)
        bar.move_to([0, BAR_Y, 0])
        bar_top = BAR_Y + 0.2

        curve = attention_curve_mobject(BAR_W, LOW_Y, HIGH_Y, PALETTE["teal"], stroke_width=6)

        start_tick = Line(UP * 0.1, DOWN * 0.1, color=PALETTE["ink"], stroke_width=3).move_to([-BAR_W / 2, BAR_Y, 0])
        mid_tick = Line(UP * 0.1, DOWN * 0.1, color=PALETTE["ink"], stroke_width=3).move_to([0, BAR_Y, 0])
        end_tick = Line(UP * 0.1, DOWN * 0.1, color=PALETTE["ink"], stroke_width=3).move_to([BAR_W / 2, BAR_Y, 0])

        start_label = T("start", color=PALETTE["slate"], font_size=16).next_to(start_tick, DOWN, buff=0.15)
        mid_label = T("middle", color=PALETTE["slate"], font_size=16).next_to(mid_tick, DOWN, buff=0.15)
        end_label = T("end", color=PALETTE["slate"], font_size=16).next_to(end_tick, DOWN, buff=0.15)

        self.play(Create(bar), run_time=0.4)
        self.play(Create(curve), run_time=1.3)
        self.play(Create(start_tick), Create(mid_tick), Create(end_tick),
                  FadeIn(start_label), FadeIn(mid_label), FadeIn(end_label), run_time=0.5)
        self.wait(0.5)

        high_left = T("HIGH", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD")
        high_left.move_to(curve_point(0.0, BAR_W, LOW_Y, HIGH_Y) + UP * 0.35 + RIGHT * 0.25)
        high_right = T("HIGH", color=PALETTE["teal"], font_size=17, font=MONO, weight="BOLD")
        high_right.move_to(curve_point(1.0, BAR_W, LOW_Y, HIGH_Y) + UP * 0.35 + LEFT * 0.25)
        self.play(FadeIn(high_left), FadeIn(high_right), run_time=0.5)
        self.wait(3.0)

        low_mid = T("LOW", color=PALETTE["crimson"], font_size=17, font=MONO, weight="BOLD")
        low_mid.move_to(curve_point(0.5, BAR_W, LOW_Y, HIGH_Y) + DOWN * 0.4)
        self.play(FadeIn(low_mid), run_time=0.5)
        self.wait(3.0)

        # y 2.9 -> 1.9 AND width MAX_W(3.6) -> 2.4: GATE B's post-render
        # layout audit caught two real collisions — this note's original
        # y=2.9 overlapped the title (bottom edge ~y=2.7 once its own buff
        # was corrected above), and at full MAX_W width it also reached out
        # to x~1.8, overlapping the "HIGH" labels sitting near the curve's
        # end apexes (x~1.3-1.8). Narrower + lower clears both: at this
        # width (+/-1.2) the curve directly underneath only reaches ~0.27,
        # well below y=1.9's note block.
        note1 = fit(T("Not an inability to see", color=PALETTE["slate"], font_size=17), 2.4)
        note1b = fit(T("that part of the text —", color=PALETTE["slate"], font_size=17), 2.4)
        note1_block = VGroup(note1, note1b).arrange(DOWN, buff=0.08)
        note1_block.move_to([0, 1.9, 0])
        self.play(FadeIn(note1_block, shift=UP * 0.1), run_time=0.5)
        self.wait(2.5)

        note2 = fit(T("just unevenly distributed", color=PALETTE["slate"], font_size=17), 2.4)
        note2b = fit(T("attention across it.", color=PALETTE["slate"], font_size=17), 2.4)
        note2_block = VGroup(note2, note2b).arrange(DOWN, buff=0.08)
        note2_block.next_to(note1_block, DOWN, buff=0.18)
        self.play(FadeIn(note2_block, shift=UP * 0.1), run_time=0.5)
        self.wait(2.5)

        closing = fit(T("The beginning and end get", color=PALETTE["ink"], font_size=19, weight="BOLD"), MAX_W)
        closing2 = fit(T("disproportionately more.", color=PALETTE["ink"], font_size=19, weight="BOLD"), MAX_W)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.65)
        self.play(Write(closing_block), run_time=0.5)
        self.wait(6.3)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: parent's LEFT doc / RIGHT Q&A -> TOP doc / BOTTOM Q&A.
# measured audio: 21.60s
# --------------------------------------------------------------------------- #
class B04_BuriedFactMiss(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # title's real top edge at y=3.45, outside the +/-3.4 safe-area
        # half-height. That alone then pushed the title's (now-lower) bottom
        # edge into doc_panel's own top edge (a second real collision, "label
        # on a curve/line") — the single-line title and the 3.3-tall panel
        # directly below it left only ~0.2 units of clearance between the
        # +/-3.4 safe ceiling and the panel's top, not enough for either.
        # Fixed on BOTH sides: panel shrunk+shifted down (3.3->3.0 tall,
        # center 1.55->1.4) to free real room above it, title kept at a safe
        # buff that clears the ceiling.
        title = fit(T("Buried in the middle.", color=PALETTE["bg"], font_size=26, weight="BOLD"), MAX_W)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        # height/center tightened again (3.0/1.4 -> 2.7/1.25): GATE B's
        # post-render layout audit caught B05's 2-line title's own SECOND
        # line ("Moved.") still overlapping this panel's top edge even
        # after the first round-trip fix — a 2-line title needs more
        # clearance above the panel than a 1-line one. Applied to both
        # B04 and B05 for visual consistency (same document, same size).
        doc_panel = panel(width=MAX_W + 0.1, height=2.7, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        doc_panel.move_to([0, 1.25, 0])
        doc_header = T("ONBOARDING DOCUMENT", color=PALETTE["sage"], font_size=12, font=MONO)
        doc_lines = document_stack(13, MAX_W - 0.5, line_color=PALETTE["bg"])
        doc_body = VGroup(doc_header, doc_lines).arrange(DOWN, buff=0.18)
        doc_body.move_to(doc_panel.get_center())

        self.play(Create(doc_panel), run_time=0.4)
        self.play(FadeIn(doc_body, shift=UP * 0.1), run_time=0.5)
        self.wait(1.0)

        # the small "fact is here" text label (present in ../scenes.py,
        # placed in the open gap between side-by-side panels) is DROPPED
        # here: portrait has no side-by-side gap, only a single full-width
        # column, so any inline label beside/below a packed document line
        # collides with a neighboring line (GATE B's post-render layout
        # audit: "label on a curve/line"). The gold highlight box alone is
        # still a real, visually obvious position marker.
        fact_line = doc_lines[6]
        fact_box = box_around(fact_line, buff=0.07, color=PALETTE["gold"])
        self.play(Create(fact_box), run_time=0.3)
        self.wait(2.0)

        qa_panel = panel(width=MAX_W + 0.1, height=1.9, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        qa_panel.move_to([0, -1.3, 0])
        qa_q = fit(T("“What's the start date?”", color=PALETTE["sage"], font_size=15, font=MONO), MAX_W - 0.4)
        qa_a = fit(T("“Not stated in this document.”", color=PALETTE["bg"], font_size=14), MAX_W - 0.4)
        qa_content = VGroup(qa_q, qa_a).arrange(DOWN, buff=0.2)
        qa_content.move_to(qa_panel.get_center())
        self.play(Create(qa_panel), run_time=0.4)
        self.play(FadeIn(qa_content, shift=UP * 0.1), run_time=0.5)
        self.wait(2.0)

        miss_tag = T("MISSED", color=PALETTE["gold"], font_size=19, font=MONO, weight="BOLD")
        miss_tag.next_to(qa_panel, DOWN, buff=0.18)
        miss_box = box_around(miss_tag, buff=0.08, color=PALETTE["gold"])
        self.play(FadeIn(miss_tag), run_time=0.3)
        self.play(Create(miss_box), run_time=0.3)
        # the mini attention-curve inset (present in ../scenes.py, tying
        # back to B03) is DROPPED here: there is not enough real vertical
        # budget left below qa_panel/miss_tag, inside the safe area, for
        # both the inset AND the closing line without a real overlap (GATE
        # B caught the inset's own label overlapping the closing text at
        # 90% — confirmed by hand-computing both elements' y-ranges, not a
        # false positive). The gold "MISSED" tag plus the doc highlight
        # above already make the position/outcome visually obvious; the
        # full attention-curve tie-back is taught once, clearly, in B03.
        self.wait(4.8)

        # buff 0.35 -> 0.75: GATE B's post-render layout audit caught this
        # closing's real bottom edge at y=-3.65, outside the +/-3.4
        # safe-area half-height.
        closing = fit(T("Right there. Just not where", color=PALETTE["gold"], font_size=16), MAX_W)
        closing2 = fit(T("it reliably looked.", color=PALETTE["gold"], font_size=16), MAX_W)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.75)
        self.play(Write(closing_block), run_time=0.5)
        self.wait(7.1)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: same TOP/BOTTOM stack redesign as B04.
# measured audio: 15.60s
# --------------------------------------------------------------------------- #
class B05_RepositionedFactFound(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # buff 0.55 -> 0.68, AND doc_panel shrunk+shifted down (same as
        # B04's fix, see its comment): GATE B's post-render layout audit
        # caught the title's first line's own bottom edge at y=3.1
        # overlapping doc_panel's top edge at y=3.2 (a real collision — at
        # 3.3-tall/center-1.55 the panel's top left only 0.2 units of
        # clearance below the +/-3.4 safe ceiling, less than the first
        # line's own ~0.22 height, so no buff value could clear both at
        # once; the panel had to move, not just the title).
        title = fit(T("Same document. Same fact.", color=PALETTE["bg"], font_size=23, weight="BOLD"), MAX_W)
        title2 = fit(T("Moved.", color=PALETTE["bg"], font_size=23, weight="BOLD"), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.68)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        # height/center tightened again (3.0/1.4 -> 2.7/1.25): GATE B's
        # post-render layout audit caught B05's 2-line title's own SECOND
        # line ("Moved.") still overlapping this panel's top edge even
        # after the first round-trip fix — a 2-line title needs more
        # clearance above the panel than a 1-line one. Applied to both
        # B04 and B05 for visual consistency (same document, same size).
        doc_panel = panel(width=MAX_W + 0.1, height=2.7, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        doc_panel.move_to([0, 1.25, 0])
        doc_header = T("ONBOARDING DOCUMENT", color=PALETTE["sage"], font_size=12, font=MONO)
        doc_lines = document_stack(13, MAX_W - 0.5, line_color=PALETTE["bg"])
        doc_body = VGroup(doc_header, doc_lines).arrange(DOWN, buff=0.18)
        doc_body.move_to(doc_panel.get_center())

        self.play(Create(doc_panel), run_time=0.4)
        self.play(FadeIn(doc_body, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)

        # "same fact, moved" inline label dropped — same reasoning as B04's
        # "fact is here" (see its comment): no side-by-side gap in portrait
        # to place it in without colliding with a neighboring document line.
        fact_line = doc_lines[1]
        fact_box = box_around(fact_line, buff=0.07, color=PALETTE["sage"])
        self.play(Create(fact_box), run_time=0.3)
        self.wait(1.5)

        qa_panel = panel(width=MAX_W + 0.1, height=1.9, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        qa_panel.move_to([0, -1.3, 0])
        qa_q = fit(T("“What's the start date?”", color=PALETTE["sage"], font_size=15, font=MONO), MAX_W - 0.4)
        qa_a = fit(T("“Stated on page one: March 2024.”", color=PALETTE["bg"], font_size=13), MAX_W - 0.4)
        qa_content = VGroup(qa_q, qa_a).arrange(DOWN, buff=0.2)
        qa_content.move_to(qa_panel.get_center())
        self.play(Create(qa_panel), run_time=0.4)
        self.play(FadeIn(qa_content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        found_tag = T("FOUND", color=PALETTE["sage"], font_size=19, font=MONO, weight="BOLD")
        found_tag.next_to(qa_panel, DOWN, buff=0.18)
        found_box = box_around(found_tag, buff=0.08, color=PALETTE["sage"])
        self.play(FadeIn(found_tag), run_time=0.3)
        self.play(Create(found_box), run_time=0.2)
        # mini attention-curve inset dropped — same reasoning as B04's (see
        # its comment): not enough real vertical budget below
        # qa_panel/found_tag, inside the safe area, for both the inset and
        # the closing line without a real overlap.
        self.wait(3.6)

        # buff 0.35 -> 0.75: same preemptive safe-area fix as B04's closing
        # (see its comment).
        closing = fit(T("Nothing about the fact changed.", color=PALETTE["sage"], font_size=15), MAX_W)
        closing2 = fit(T("Only its position did.", color=PALETTE["sage"], font_size=15), MAX_W)
        closing_block = VGroup(closing, closing2).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.75)
        self.play(Write(closing_block), run_time=0.4)
        self.wait(3.8)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 28.27s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # buff 0.55 -> 0.68: GATE B's post-render layout audit caught this
        # title's real top edge at y=3.45, outside the +/-3.4 safe-area
        # half-height.
        title = fit(T("Try this on your", color=PALETTE["ink"], font_size=22), MAX_W)
        title2 = fit(T("next long prompt:", color=PALETTE["ink"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.68)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        # box 0.4->0.55, font 17->20, row/item buffs widened: GATE V's
        # canvas-fill check measured this beat's real 50%-sample candidate
        # at only 54% of the safe area (min 55%) — confirmed by direct
        # frame inspection (checklist card small and centered, with large
        # empty margins). Bigger checkboxes/text and wider gaps is genuine
        # additional content mass.
        def checklist_item(text):
            box = Square(side_length=0.55, color=PALETTE["teal"], stroke_width=3, fill_opacity=0)
            check = fit(T(text, color=PALETTE["ink"], font_size=20, line_spacing=1.2), MAX_W - 0.7)
            row = VGroup(box, check).arrange(RIGHT, buff=0.3)
            return row, box

        row1, box1 = checklist_item("How long is\nthe context?")
        row2, box2 = checklist_item("Where does the key\nfact actually sit?")
        row3, box3 = checklist_item("Would moving it\nchange whether\nit's found?")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.7,
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

        # buff 0.35 -> 0.75: GATE B's post-render layout audit caught this
        # 3-line closing's real bottom edge at y=-3.65, outside the +/-3.4
        # safe-area half-height.
        closing = fit(T("A real blind spot — not a reason", color=PALETTE["ink"], font_size=15), MAX_W)
        closing2 = fit(T("to distrust the model, a reason to", color=PALETTE["ink"], font_size=15), MAX_W)
        closing3 = fit(T("put the key part where it's seen.", color=PALETTE["ink"], font_size=15), MAX_W)
        closing_block = VGroup(closing, closing2, closing3).arrange(DOWN, buff=0.08)
        closing_block.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(closing_block, shift=UP * 0.1), run_time=0.4)
        self.wait(4.97)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 11.23s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        lines1 = ["A model that misses", "a fact buried on page", "fifty isn't failing to", "understand it."]
        block1 = VGroup(*[fit(T(l, color=PALETTE["bg"], font_size=24), MAX_W) for l in lines1]).arrange(DOWN, buff=0.16)

        lines2 = ["It's reading unevenly —", "and that changes where", "you put what you need", "it to find."]
        block2 = VGroup(*[fit(T(l, color=PALETTE["gold"], font_size=21), MAX_W) for l in lines2]).arrange(DOWN, buff=0.14)

        content = VGroup(block1, block2).arrange(DOWN, buff=0.55).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=content.height + 1.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.5)

        question_box = box_around(block2, buff=0.14, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(2.93)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed for portrait.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=34), MAX_W + 0.3)
        accent = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=27), MAX_W)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"], font_size=23), MAX_W)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=1.0).move_to(ORIGIN)

        frame_w = min(content.width + 0.7, MAX_W + 0.3)
        frame_h = min(content.height + 0.7, 7.2)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.5)
        self.wait(1.01)
