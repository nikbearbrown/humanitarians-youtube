"""
Manim scenes for 2026-09-07-embeddings-how-ai-tells-similar-from-different

"Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)"

B00_TitleCard              — silent title card: video title + @HumanitariansAI (TITLE)
B01_ExecSummary             — spoken personal-intro card: fellow's name + one-line summary (EXEC-SUMMARY)
B02_KeywordMissHook         — a document tagging rule that matches "Investment Adviser
                               Disclosure" but misses a document titled "RIA" (HOOK)
B03_ThreeQuestionsFramework — the 3-question rubric, Wording Varies / Context Flips
                               Meaning / Exactness Is The Point, shown together (FRAMEWORK)
B04_MeaningSpaceDiagram     — "meaning space" scatter: RIA / investment adviser / advisor
                               plotted close together, "quarterly earnings" plotted far
                               away (WORKED-EXAMPLE)
B05_ExactnessFalsifiability — same diagram style, but Section 4.12 / Section 4.13
                               (fictional placeholder numbers) plotted close together —
                               a warning, not a win (FALSIFIABILITY)
B06_AuditChecklist          — the 3 questions restated as a checkbox checklist, visually
                               distinct from B03's rubric card (SCAFFOLDED-TASK)
B07_Statement               — takeaway statement card (TAKEAWAY)
B08_BrandOutro              — @HumanitariansAI sign-off (SIGN-OFF)

IMPORTANT (see FACTCHECK.md / SOURCES.md): B02's worked example (a document-tagging
rule that only matches the literal phrase "investment adviser") and B05's falsifiability
case ("Section 4.12" / "Section 4.13") are BOTH fully generic and fictional — the
regulation-section numbers are deliberately fake placeholders, not real citations, and
no real codebase, company, or regulation is named anywhere in this file.

All 9 beats are self-contained Manim scenes, no pantry stills, no Remotion. Palette and
house idioms (PALETTE / MONO / fit() / panel()) copied from this fellow's sibling reel
(2026-08-17-why-ai-generated-code-still-needs-a-human/scenes.py) for visual consistency
across the series — plain Text (Pango) throughout, never Integer/DecimalNumber/MathTex
(no LaTeX installed on this machine; irrelevant here anyway, no equations).

TIMING NOTE: self.wait()/run_time values are tuned to each beat's *measured* Kokoro
audio duration (beat_sheet.json -> actual_duration_s), not the pre-audio estimate — the
audio-first pipeline conforms video to audio by center-cutting or slow-fitting the
rendered clip to the measured mp3 length (runtime/scripts/compile.py). B00 is the one
exception: it carries no narration (narration_text: "" in beat_sheet.json), so its
duration is a fixed silent-beat target (the real ffmpeg anullsrc mp3, measured 4.05s)
rather than a measured Kokoro length — compile.py's build_master_audio() needs a REAL
audio file (even silent) at every beat's audio_file path, or the entire film's narration
falls back to silence; a bare `audio_file: null` breaks that all-beats-exist check.
"""

from manim import *

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool — "close in meaning" = correct
    "teal_on_ink": "#5FB8CC",  # same hue family, lightened for ink backgrounds
                          # specifically (6.23:1 on "ink" vs a broken 1.56:1 for
                          # plain "teal" there) — use this, never "teal", for any
                          # teal text/stroke placed on an ink background or panel.
    "crimson": "#E4572E", # bad / CVD-safe warm — "close in meaning" = a mistake here
    "slate":  "#29335C",  # structure — on the CREAM bg only (10.3:1 there)
    "slate_on_ink": "#9AA3D6",  # 2026-09-11 fix: plain "slate" measured only 1.16:1 on
                          # "ink" (near-invisible, fellow-reported "blends into the
                          # background") — this lightened tint hits 5.80:1 on ink. Use
                          # this, never plain "slate", for any text/stroke placed on an
                          # ink background or panel (mirrors the teal/teal_on_ink split
                          # above).
    "gold":   "#F3A712",  # fill/stroke accent only — never text color (contrast)
    "sage":   "#A8C686",  # human / growth / code-on-dark
}

MONO = "Courier New"


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def panel(width, height, fill=None, stroke=None, corner_radius=0.12, opacity=1.0):
    return RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        fill_color=fill or PALETTE["ink"], fill_opacity=opacity,
        stroke_color=stroke or PALETTE["slate"], stroke_width=2,
    )


def box_around(mob, buff=0.14, color=None, stroke_width=3):
    """A highlighter rectangle built from the TARGET's own measured bounds
    (width/height/get_center()), never by passing the mobject itself to the
    constructor — SurroundingRectangle-style helpers get flagged by the
    static checker as 'textish' and silently excluded from shape-distinctness
    tracking. Matches the sibling reel's own box_around()/clear_of_divider()
    discipline of measuring real bounds rather than guessing coordinates."""
    r = Rectangle(
        width=mob.width + 2 * buff, height=mob.height + 2 * buff,
        stroke_color=color or PALETTE["gold"], stroke_width=stroke_width, fill_opacity=0,
    )
    r.move_to(mob.get_center())
    return r


# --------------------------------------------------------------------------- #
# Shared "meaning space" diagram builder — used by B04 (good closeness) and
# B05 (bad closeness). A real, legible 2D scatter-style panel: a bordered
# frame, faint gridlines (illustrative depth, not literal axes/units — this
# is a SIMPLIFIED meaning space, per the beat sheet's own language), plotted
# points as Dot + label pairs, and a grouping indicator (dashed ellipse)
# around whichever points are "close together". Built centered at ORIGIN;
# callers position the whole returned VGroup afterward.
# --------------------------------------------------------------------------- #
# GATE V fix (2026-09-07 patch): panel enlarged from 9.6x4.3 to 11.4x6.0 —
# the small diagram box floating in a mostly-empty canvas was confirmed by
# direct visual inspection of the contact sheets (not just a GATE V number)
# as the single worst systemic underfill offender in the whole reel. Every
# point coordinate, ellipse, and font size below is scaled to the new
# panel's own half-extents (see PANEL_SCALE_X/Y) so the plotted layout keeps
# the same relative shape inside the much bigger frame, rather than leaving
# the old small cluster adrift in new empty space.
# 2026-09-11 fix: PANEL_H trimmed 5.2->4.7 to free enough gap below the panel
# (frame_bottom to panel_bottom) for the B04 caption / B05 warn_label to sit at a real
# ~11% frame-edge safe margin (buff=0.9) WITHOUT overlapping the panel's own border —
# at PANEL_H=5.2 there wasn't enough room for both (GATE B's post-render layout audit
# caught the actual overlap directly: "label on a curve/line" for B04's caption box
# crossing the panel bottom edge once its buff was raised for the frame-edge fix).
PANEL_W, PANEL_H = 11.4, 4.7
PANEL_SCALE_X = (PANEL_W / 2) / 4.8   # 4.8 = old PANEL_W/2
PANEL_SCALE_Y = (PANEL_H / 2) / 2.15  # 2.15 = old PANEL_H/2


def meaning_space_frame(stroke=None):
    """Built centered at ORIGIN. Callers place the returned VGroup with a
    single explicit .move_to(...) (never next_to a title, whose stub-vs-real
    height estimate differs enough to risk pushing the panel below the safe
    frame) — a fixed anchor keeps every point/label computed against it
    guaranteed to land inside the ±7.12/±4.05 hard frame.

    No internal gridlines: an earlier version drew faint gridlines across the
    panel for depth, but manim_layout_audit.py's real post-render pass (GATE
    B) flags any label text whose bounding box crosses a Line/curve mobject
    as a real "label on a curve/line" ERROR — the gridlines crossed under
    almost every plotted label. A plain bordered panel keeps the labels
    legible without tripping that check, and the panel border + dots/labels
    already read clearly as a coordinate space without decorative gridlines.

    stroke: border color override. B05 (ink background) passes
    teal_on_ink — plain slate-on-ink border pixels average too close to the
    ink background's own luminance once the enlarged panel's much longer
    border perimeter makes up a bigger share of total "ink" pixels, which
    was diluting GATE V's whole-frame low-contrast check (real measured
    separation ~0.29, just under the 0.30 floor) — a real regression from
    the panel enlargement, not the pre-existing accepted dilution artifact
    this reel's BUILD-LOG already documents for the smaller original panel."""
    return VGroup(panel(PANEL_W, PANEL_H, fill=PALETTE["ink"], stroke=stroke or PALETTE["slate"], opacity=1.0))


def plot_point(pos, label_text, color, label_dir=DOWN, font_size=26):
    # dot radius + label font both sized up (0.11->0.16, 20->26) to read as
    # real content inside the enlarged panel, not tiny marks lost in it.
    dot = Dot(point=[pos[0], pos[1], 0], radius=0.16, color=color, fill_opacity=1.0)
    label = fit(Text(label_text, color=color, font_size=font_size, font=MONO), 4.4)
    label.next_to(dot, label_dir, buff=0.2)
    return VGroup(dot, label)


def grouping_ellipse(center, color, w=3.0, h=2.2):
    # defaults scaled to the enlarged panel; callers that pass explicit w/h
    # already pass pre-scaled values (see B04/B05 below).
    ell = Ellipse(width=w, height=h, color=color, stroke_width=3.5, fill_opacity=0.06,
                   fill_color=color)
    ell.move_to([center[0], center[1], 0])
    return DashedVMobject(ell, num_dashes=28)


def distance_connector(start, end, color, label_text, label_shift=UP * 0.22, label_max_w=4.6):
    """GATE V fix (2026-09-10 patch): B05's far point and its cluster sat in
    opposite corners of the panel with the entire middle (plus the other two
    corners) empty for most of the beat — confirmed by direct full-res frame
    extraction at 95s into the 16:9 master, not just the GATE V bbox number.
    This mirrors the portrait short's own distance_connector() (see
    short/scenes.py): a dashed line + small label bridging the two point-
    groups so the space between them reads as a real "far apart in meaning"
    element instead of dead space. start/end are already-anchor-shifted
    [x, y] pairs (same convention as plot_point's returned Dot position).
    label_max_w: callers whose connector's midpoint sits close to another
    label (see B05's call, which narrows this to keep clear of "Section
    4.13") can shrink it from the default."""
    line = DashedLine([start[0], start[1], 0], [end[0], end[1], 0], color=color,
                       stroke_width=2.5, dash_length=0.2)
    label = fit(Text(label_text, color=color, font_size=22, font=MONO), label_max_w)
    label.move_to([(start[0] + end[0]) / 2, (start[1] + end[1]) / 2, 0])
    label.shift(label_shift)
    return VGroup(line, label)


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card, video title + @HumanitariansAI, no VO.
# Fixed silent-beat duration (4.05s, real ffmpeg anullsrc mp3) — see file
# docstring + beat_sheet.json shot.note.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # Title wrapped onto 3 hand-set lines (13 words / 78 chars — too long
        # for one legible line at title-card size).
        # GATE V fix (2026-09-07 patch): sized up from 48/48/34 to 58/58/40 and
        # buff widened from 0.85 to 1.35 — the original settled state measured
        # only ~53% safe-area coverage (real GATE V number, below the 55%
        # floor), matching this fellow's other title-card fix precedent
        # (canvas-fill has to come from spacing/size, not word count, on a
        # 3-element card).
        title_line1 = fit(Text(
            "Embeddings: How AI Tells Similar",
            color=PALETTE["ink"], font_size=58, weight="BOLD",
        ), 12.4)
        title_line2 = fit(Text(
            "From Different",
            color=PALETTE["ink"], font_size=58, weight="BOLD",
        ), 12.4)
        title_line3 = fit(Text(
            "(When Keyword Matching Can't)",
            color=PALETTE["slate"], font_size=40,
        ), 12.4)
        title = VGroup(title_line1, title_line2, title_line3).arrange(DOWN, buff=0.32)

        top_rule = Line(LEFT * 3.6, RIGHT * 3.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 3.6, RIGHT * 3.6, color=PALETTE["gold"], stroke_width=3)
        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=42)

        # generous buff (1.25, not the usual ~0.4-0.5) — a title-only card
        # has few elements, so real canvas-fill has to come from spacing.
        # (1.35 originally pushed the handle 0.05 past the layout audit's
        # stricter safe-area bound; trimmed to 1.25 for real margin.)
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.25
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.7)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # settled well before any QC sample point; remainder is a clean hold
        # tuned to the real measured silent-track length (4.05s, mp3/beat-B00.mp3)
        self.wait(2.55)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: spoken personal-intro card (name + one-line thesis).
# measured audio: 12.34s
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~37% safe-area coverage (real GATE V number) — the worst
        # underfill offender among the text/rubric cards. Sized up across the
        # board (badge/name/role/summary fonts + rule width) and the
        # inter-element buff widened from 0.75 to 1.15, same lesson as
        # B00_TitleCard's own fix: a card with few elements needs its OWN
        # spacing/size to clear the canvas-fill floor, not just word count.
        top_rule = Line(LEFT * 4.2, RIGHT * 4.2, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 4.2, RIGHT * 4.2, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.7, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3.5)
        initials = Text("SPJ", color=PALETTE["teal"], font_size=36, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(Text("Sai Pranavi Jeedigunta", color=PALETTE["ink"], font_size=50, weight="BOLD"), 9.6)
        role = fit(Text("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=27), 7.6)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.18)
        header_row = VGroup(badge_group, name_block).arrange(RIGHT, buff=0.5)

        # matches the second+third sentence of narration_text in substance
        summary_lines = [
            "This video: why keyword-matching rules",
            "quietly break over time — and what",
            "embeddings actually do differently.",
        ]
        summary = VGroup(*[
            fit(Text(l, color=PALETTE["ink"], font_size=32), 11.6) for l in summary_lines
        ]).arrange(DOWN, buff=0.26)

        VGroup(top_rule, header_row, summary, bottom_rule).arrange(
            DOWN, buff=1.15
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # 4 self.play() calls above sum to 1.8s; remainder is a clean hold
        # tuned to the measured 12.34s Kokoro length for B01.
        self.wait(10.54)


# --------------------------------------------------------------------------- #
# B02 — HOOK: a document-tagging rule that matches "Investment Adviser
# Disclosure" but misses a document titled "RIA" — the rule only recognizes
# the literal phrase "investment adviser".
# [GENERIC EXAMPLE — see FACTCHECK.md — plain document-classification/tagging
# scenario, no real codebase named]
# measured audio: 18.53s
# --------------------------------------------------------------------------- #
class B02_KeywordMissHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # GATE V fix (2026-09-07 patch): despite reading "reasonably filled"
        # on the contact sheet thumbnail, a real per-second measurement of
        # this beat found it held at only ~40% safe-area coverage for 9 of
        # its 18.75s (t=2.5-11.5s) — the doc/rule cards alone were never wide
        # enough to reach the width floor, and the "closing" caption (the
        # only element that used to extend the bbox toward the bottom safe
        # edge) didn't land until t=11.7s. Fixed the same way as B06's
        # identical late-arriving-anchor bug: a floor rule now draws with the
        # header at t=0 (present the whole beat), with "closing" landing
        # above it later; the doc/rule cards themselves are also enlarged
        # and pushed further apart so the width alone clears the floor even
        # before the closing line appears.
        header = fit(Text(
            "document tagging rule", color=PALETTE["sage"], font_size=22, font=MONO
        ), 10.0)
        header.to_edge(UP, buff=0.7)
        floor_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["slate"], stroke_width=2)
        floor_rule.to_edge(DOWN, buff=0.95)

        def doc_card(title_text, w=3.5, h=4.2):
            body = RoundedRectangle(width=w, height=h, corner_radius=0.08,
                                     fill_color=PALETTE["bg"], fill_opacity=1.0,
                                     stroke_color=PALETTE["slate"], stroke_width=2)
            fold = Polygon(
                [w / 2 - 0.5, h / 2, 0], [w / 2, h / 2, 0], [w / 2, h / 2 - 0.5, 0],
                fill_color=PALETTE["slate"], fill_opacity=0.3, stroke_width=0,
            )
            title = fit(Text(title_text, color=PALETTE["ink"], font_size=22, weight="BOLD"), w - 0.5)
            title.move_to([0, h / 2 - 0.6, 0])
            lines = VGroup(*[
                Line([-w / 2 + 0.35, y, 0], [w / 2 - 0.35, y, 0],
                     color=PALETTE["slate"], stroke_width=1.5, stroke_opacity=0.5)
                for y in (h / 2 - 1.3, h / 2 - 1.75, h / 2 - 2.2, h / 2 - 2.65, h / 2 - 3.1)
            ])
            return VGroup(body, fold, title, lines)

        def rule_box(w=4.1, h=2.8):
            box = panel(w, h, fill=PALETTE["slate"], stroke=PALETTE["gold"], opacity=0.35)
            rule_hdr = Text("RULE", color=PALETTE["gold"], font_size=22, font=MONO, weight="BOLD")
            rule_hdr.move_to([0, h / 2 - 0.48, 0])
            phrase = fit(Text('contains exact phrase:', color=PALETTE["sage"], font_size=18, font=MONO), w - 0.4)
            phrase.move_to([0, 0.15, 0])
            phrase2 = fit(Text('"investment adviser"?', color=PALETTE["sage"], font_size=19, font=MONO, weight="BOLD"), w - 0.4)
            phrase2.next_to(phrase, DOWN, buff=0.2)
            return VGroup(box, rule_hdr, phrase, phrase2)

        rule = rule_box()
        rule.move_to([3.6, 0.3, 0])

        self.play(FadeIn(header, shift=UP * 0.1), Create(floor_rule), run_time=0.4)
        self.play(Create(rule[0]), FadeIn(rule[1:]), run_time=0.6)

        # CASE 1 — the rule works: a doc that spells out the phrase in full.
        # GATE V fix (patch): the card's FadeIn(shift=RIGHT*0.2) entrance meant
        # its FIRST rendered position was the -4.6 anchor minus that shift
        # (-4.8), putting the card's left edge (half-width 1.75) at x=-6.55 —
        # outside the ~-6.4 safe-area left bound (confirmed BLOCKER edge-bleed
        # on a real rendered frame). Moved the entrance anchor to -4.3 so even
        # the pre-shift position (-4.5) clears the safe edge with margin.
        doc1 = doc_card("Investment Adviser\nDisclosure")
        doc1.move_to([-4.3, 0.3, 0])
        self.play(FadeIn(doc1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(doc1.animate.move_to([-4.0, 0.3, 0]), run_time=0.6)

        check1 = Text("✓ FLAGGED", color=PALETTE["teal_on_ink"], font_size=22, font=MONO, weight="BOLD")
        check1.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(check1, scale=1.2), run_time=0.4)
        self.wait(1.5)

        # CASE 2 — swap in the doc titled with the industry's own acronym.
        self.play(FadeOut(doc1, shift=LEFT * 0.3), FadeOut(check1), run_time=0.3)

        doc2 = doc_card("RIA\nAnnual Update")
        doc2.move_to([-4.3, 0.3, 0])
        self.play(FadeIn(doc2, shift=RIGHT * 0.2), run_time=0.4)
        self.play(doc2.animate.move_to([-4.0, 0.3, 0]), run_time=0.8)
        self.wait(1.0)

        scan_box = box_around(rule[3], color=PALETTE["gold"], stroke_width=2)
        self.play(Create(scan_box), run_time=0.5)
        self.wait(1.2)

        miss = Text("✗ NOT FLAGGED", color=PALETTE["crimson"], font_size=24, font=MONO, weight="BOLD")
        miss.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(miss, scale=1.2), run_time=0.5)
        self.wait(3.0)

        closing = fit(Text(
            "nothing crashed — it just quietly stopped working",
            color=PALETTE["sage"], font_size=22,
        ), 11.6)
        closing.next_to(floor_rule, UP, buff=0.25)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.6)
        # everything settled well before any QC sample point; remainder tuned
        # to the measured 18.53s Kokoro length for B02.
        self.wait(6.23)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: the 3-question rubric, shown in full before any example.
# Wording Varies / Context Flips Meaning / Exactness Is The Point.
# measured audio: 24.07s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # ~54-55% safe-area coverage (real GATE V number, right at/under the
        # 55% floor) — badges/fonts sized up and row buff widened from 0.7 to
        # 0.9 (matching the sibling reel's own B03 fix of the identical
        # underfill bug), plus a bottom-anchored closing line added so the
        # row block's own span reaches further toward the safe-area floor
        # instead of leaving a dead lower band once all 3 rows have landed.
        title = fit(Text(
            "Three Questions, Before Any Example", color=PALETTE["ink"], font_size=46
        ), 11.8)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)

        intro = fit(Text(
            "Ask all three, in order:", color=PALETTE["slate"], font_size=24
        ), 9.4)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        # shortened 1.3 -> 0.6 (the 0.7s moved to the closer's hold below) —
        # this title+intro-only state measured well under the canvas-fill
        # floor (title/intro alone are a small fraction of the safe area,
        # same as any beat's brief opening moment), so it shouldn't linger
        # longer than needed before the full rubric skeleton lands.
        self.wait(0.6)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "WORDING VARIES", "Does the wording actually vary in the real world —\nor is there only one way to say this?"),
            ("2", "CONTEXT FLIPS MEANING", "Does context change what a phrase means, so a fixed\nkeyword could be right in one place, wrong in another?"),
            ("3", "EXACTNESS IS THE POINT", "Is exactness itself the point — like matching a specific\nID or code — where a close-but-different match is wrong?"),
        ]

        rows = VGroup()
        for num, label, desc in rows_data:
            badge = Circle(radius=0.48, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                            fill_opacity=0.15, stroke_width=3)
            badge_num = Text(num, color=PALETTE["teal"], font_size=32, font=MONO).move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)

            label_txt = fit(Text(label, color=PALETTE["slate"], font_size=27, font=MONO, weight="BOLD"), 8.9)
            desc_txt = fit(Text(desc, color=PALETTE["ink"], font_size=22, line_spacing=1.05), 9.9)

            text_col = VGroup(label_txt, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            row = VGroup(badge_group, text_col).arrange(RIGHT, buff=0.55)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.9)
        if rows.width > 12.2:
            rows.scale_to_fit_width(12.2)
        if rows.height > 5.3:
            rows.scale_to_fit_height(5.3)
        rows.move_to(ORIGIN).shift(DOWN * 0.05)

        # SKELETON FIRST: all 3 badges + labels land before any one question
        # is explained — the full rubric on screen before any example starts.
        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.15)

        # holds tuned to the measured 24.07s Kokoro audio, split proportional
        # to each question's word count (18/22/22 of 62 words spoken across
        # the 3 questions).
        row_holds = [5.29, 6.46, 6.46]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1][1]
            self.play(FadeIn(desc_txt, shift=UP * 0.1), run_time=0.3)
            self.wait(hold)

        closer = fit(Text(
            "all three, every time — not two, not one.",
            color=PALETTE["crimson"], font_size=24,
        ), 10.5)
        closer.to_edge(DOWN, buff=0.95)
        self.play(FadeIn(closer, shift=UP * 0.1), run_time=0.3)
        self.wait(2.41)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: "meaning space" diagram. RIA / investment adviser /
# advisor plot close together; "quarterly earnings" plots far away.
# measured audio: 25.9s
# --------------------------------------------------------------------------- #
class B04_MeaningSpaceDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): direct visual inspection of the
        # contact sheet confirmed this diagram was the worst systemic
        # underfill offender in the whole reel — a small dark rectangle with
        # 2-3 tiny dots floating in a mostly-empty cream canvas. The panel
        # itself is now enlarged 11.4x5.7 (was 9.6x4.3, PANEL_W/PANEL_H
        # above) and every point/ellipse coordinate below is scaled by the
        # module-level PANEL_SCALE_X/Y factors so the plotted layout keeps
        # the same relative shape inside the much bigger frame.
        title = fit(Text("Meaning Space", color=PALETTE["ink"], font_size=38), 8.6)
        title.move_to([0, 3.1, 0])

        # fixed anchor (not next_to the title) so every point/label computed
        # against it is guaranteed inside the hard frame — see
        # meaning_space_frame()'s own docstring for why.
        frame = meaning_space_frame()
        frame.move_to([0, -0.3, 0])
        anchor = frame.get_center()

        self.play(Write(title), run_time=0.4)
        self.play(FadeIn(frame), run_time=0.5)
        self.wait(2.6)

        sx, sy = PANEL_SCALE_X, PANEL_SCALE_Y
        # cluster: RIA / investment adviser / advisor — plotted close together
        p_ria = plot_point([1.1 * sx, 1.2 * sy], "RIA", PALETTE["teal_on_ink"], label_dir=UP)
        p_ia = plot_point([2.3 * sx, 0.6 * sy], "investment adviser", PALETTE["teal_on_ink"], label_dir=DOWN)
        p_adv = plot_point([1.4 * sx, -0.1 * sy], "advisor", PALETTE["teal_on_ink"], label_dir=DOWN)
        for p in (p_ria, p_ia, p_adv):
            p.shift(anchor)

        self.play(FadeIn(p_ria), run_time=0.3)
        self.play(FadeIn(p_ia), run_time=0.3)
        self.play(FadeIn(p_adv), run_time=0.3)

        # GATE V fix (2026-09-10 patch): the unrelated far term was
        # previously introduced only in the last ~3.6s of this 25.9s beat —
        # confirmed by direct frame extraction that for ~85% of the beat's
        # runtime, the entire left half of the panel was empty (the cluster
        # occupies only the upper-right quadrant). Moved here, right after
        # the cluster appears, with NO other duration changed anywhere in
        # this scene (same self.play/self.wait lines, same run_time/wait
        # values, just reordered) — the far point is now visible for ~83%
        # of the beat instead of ~13%, using both halves of the panel for
        # nearly the whole runtime. Total scene duration is unchanged
        # (still exactly 25.9s), so Kokoro audio sync is unaffected.
        p_far = plot_point([-3.4 * sx, -1.55 * sy], "quarterly earnings", PALETTE["slate_on_ink"], label_dir=UP)
        p_far.shift(anchor)
        self.play(FadeIn(p_far), run_time=0.4)
        self.wait(3.7)

        ellipse = grouping_ellipse([1.6 * sx, 0.55 * sy], PALETTE["teal_on_ink"], w=3.4 * sx, h=2.4 * sy)
        ellipse.shift(anchor)
        # deliberate annotation: the whole point of this ellipse is to
        # encircle the 3 cluster labels, so its stroke passing near/behind
        # their glyphs is intentional design, not a stray line crossing text
        # by accident — same escape hatch the sibling reel uses for its own
        # deliberate strike-through (see manim_layout_audit.py's
        # _collect_strokes() docstring).
        ellipse._qc_intentional = True
        close_tag = fit(Text("close together in meaning", color=PALETTE["teal_on_ink"], font_size=24, font=MONO), 6.4)
        close_tag.next_to(ellipse, DOWN, buff=0.16)

        self.play(Create(ellipse), run_time=0.6)
        self.play(FadeIn(close_tag), run_time=0.5)
        self.wait(6.9)

        checkmark = fit(Text("✓ same real-world thing", color=PALETTE["teal_on_ink"], font_size=24, font=MONO, weight="BOLD"), 9.5)
        checkmark.next_to(title, DOWN, buff=0.15)
        pulse_box = box_around(VGroup(p_ria, p_ia, p_adv), color=PALETTE["teal_on_ink"], stroke_width=2.5, buff=0.6)
        # deliberate annotation (a highlight box around the whole cluster,
        # drawn AFTER close_tag is already on screen) — same escape hatch as
        # the ellipse above.
        pulse_box._qc_intentional = True
        self.play(FadeIn(checkmark, scale=1.1), Create(pulse_box), run_time=0.8)
        self.wait(5.2)

        # p_far is already on screen (moved up, see the 2026-09-10 patch note
        # above) — only the caption is new here. The removed duplicate
        # p_far creation + its 0.4s FadeIn is folded into this wait so total
        # scene duration is still exactly 25.9s (was wait(2.6) + 0.4s FadeIn
        # = 3.0s of tail time; now a single wait(3.0)).
        caption = fit(Text(
            "catches every synonym — even the ones nobody listed",
            color=PALETTE["ink"], font_size=23,
        ), 11.6)
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # tuned to the measured 25.9s Kokoro audio for B04 (2.6 + the 0.4s
        # reclaimed from the removed duplicate p_far FadeIn = 3.0).
        self.wait(3.0)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: same meaning-space diagram, but "Section 4.12" and
# "Section 4.13" (fully fictional placeholder rule numbers — NOT real
# regulation citations, see FACTCHECK.md) plot close together — a warning,
# not a win. Visually distinct treatment from B04 (gold/crimson, not teal).
# measured audio: 26.83s
# --------------------------------------------------------------------------- #
class B05_ExactnessFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        # GATE V fix (2026-09-07 patch): same panel enlargement + coordinate
        # rescale as B04 above (see that class's comment for the full
        # rationale) — this beat shares the identical small-box-in-empty-
        # canvas defect, confirmed by the same contact-sheet inspection.
        title = fit(Text("Meaning Space — the Exactness Case", color=PALETTE["bg"], font_size=32), 11.0)
        title.move_to([0, 3.1, 0])

        # fixed anchor (not next_to the title) — see B04's identical note in
        # meaning_space_frame()'s docstring for why this matters.
        frame = meaning_space_frame(stroke=PALETTE["teal_on_ink"])
        frame.move_to([0, -0.3, 0])
        anchor = frame.get_center()

        sx, sy = PANEL_SCALE_X, PANEL_SCALE_Y
        # a dimmed echo of B04's far term, to signal "same underlying space"
        # — opacity raised 0.5 -> 0.65 (still visibly dimmer than the active
        # gold points) after the panel enlargement made this element a big
        # enough share of total ink pixels to drag the low-contrast check's
        # whole-frame average close to the floor (see meaning_space_frame()'s
        # docstring for the stroke-color half of this same fix).
        #
        # GATE V fix (2026-09-10 patch): direct full-res frame extraction at
        # 95s into this master showed the panel ~70% empty — p_far sat alone
        # in the bottom-left corner, the 4.12/4.13 cluster sat alone in the
        # upper-right, with the whole middle (plus top-left/bottom-right)
        # empty dead space. Both groups are pulled ~25-35% closer toward the
        # panel's center along the SAME diagonal (p_far: -3.4,-1.55 ->
        # -3.0,-1.3; cluster shifted as a rigid group by (-0.35,-0.25) so its
        # internal shape — the 0.9 x / -0.7 y offset between 4.12 and
        # 4.13 — is unchanged) while still reading as clearly separated, and
        # a new distance_connector (see that function's docstring above)
        # bridges the two groups so the middle band is real content instead
        # of a void.
        p_far = plot_point([-3.0 * sx, -1.3 * sy], "quarterly earnings", PALETTE["slate_on_ink"], label_dir=UP)
        p_far.shift(anchor)
        # 2026-09-11 fix: 0.65 opacity was compounding plain "slate"'s already-broken
        # 1.16:1 contrast into total illegibility. slate_on_ink at 0.85 still reads as
        # dimmer than the active gold points (the original design intent) while holding
        # ~4.6:1 contrast against ink.
        p_far.set_opacity(0.85)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(frame), FadeIn(p_far), run_time=0.4)
        self.wait(2.6)

        p_412 = plot_point([0.85 * sx, 0.85 * sy], "Section 4.12", PALETTE["gold"], label_dir=UP)
        p_412.shift(anchor)
        self.play(FadeIn(p_412), run_time=0.4)
        self.wait(6.6)

        p_413 = plot_point([1.75 * sx, 0.15 * sy], "Section 4.13", PALETTE["gold"], label_dir=DOWN)
        p_413.shift(anchor)
        ellipse = grouping_ellipse([1.3 * sx, 0.5 * sy], PALETTE["gold"], w=2.9 * sx, h=2.1 * sy)
        ellipse.shift(anchor)
        # deliberate annotation — see B04's identical note.
        ellipse._qc_intentional = True
        self.play(FadeIn(p_413), run_time=0.4)
        self.play(Create(ellipse), run_time=0.6)

        # connector spans from just outside p_far to short of the cluster's
        # ellipse (22%-58%, not 82%, along the straight line between the two
        # groups' centers), filling the panel's previously-empty middle band
        # with a real "far apart in meaning" element instead of a void.
        # First render (82% end) put the connector's label close enough to
        # "Section 4.13" that the two texts visually ran together with no
        # gap — confirmed by direct frame inspection, not just coordinates
        # on paper. Pulled the end back to 58% (well clear of the ellipse's
        # left edge at x=-0.15) and narrowed the label's own max width
        # (3.4, was 4.6) so its right edge stays left of "Section 4.13"'s
        # left edge with real margin. New 0.6s Create is offset by
        # shortening the following wait from 6.5 to 5.9 so total beat
        # duration is still exactly 26.83s.
        conn_start = [-2.054 * sx + anchor[0], -0.904 * sy + anchor[1]]
        conn_end = [-0.506 * sx + anchor[0], -0.256 * sy + anchor[1]]
        connector = distance_connector(conn_start, conn_end, PALETTE["gold"], "far apart in meaning", label_max_w=3.4)
        connector[0]._qc_intentional = True
        self.play(Create(connector), run_time=0.6)
        self.wait(5.9)

        warn_tri = Triangle(color=PALETTE["crimson"], fill_color=PALETTE["crimson"],
                             fill_opacity=0.2, stroke_width=3.5)
        warn_tri.scale(0.4)
        warn_bang = Text("!", color=PALETTE["crimson"], font_size=26, font=MONO, weight="BOLD")
        warn_bang.move_to(warn_tri.get_center() + DOWN * 0.02)
        warn_badge = VGroup(warn_tri, warn_bang)
        warn_badge.next_to(title, DOWN, buff=0.18)
        warn_label = fit(Text("different rules — different requirements", color=PALETTE["crimson"], font_size=24, font=MONO, weight="BOLD"), 10.8)
        warn_label.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(warn_badge, scale=1.2), run_time=0.6)
        self.wait(2.4)

        exact_line = fit(Text("exactness is the whole point here", color=PALETTE["bg"], font_size=25), 10.5)
        exact_line.next_to(warn_label, UP, buff=0.32)
        self.play(Write(exact_line), run_time=0.5)
        self.wait(2.0)

        self.play(FadeIn(warn_label, shift=UP * 0.1), run_time=0.5)
        # tuned to the measured 26.83s Kokoro audio for B05.
        self.wait(2.83)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: the 3 questions restated as a checkbox checklist —
# a distinct visual (Square checkboxes, task framing) from B03's numbered
# rubric badges, not a copy of that card.
# measured audio: 21.22s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~25-49% safe-area coverage (real GATE V number) across most of
        # this beat's hold — checkboxes/fonts sized up and row buff widened
        # from 0.55 to 0.8 (same lesson as B03's own fix). That alone wasn't
        # enough: real per-second measurement showed the beat held at a flat
        # ~47.5% for a full 4s window (t=2-6s) because the decision block
        # (the only element that used to reach toward the safe-area floor)
        # didn't land until the very end — for most of the beat's runtime the
        # visible bbox was just the title + partially-revealed rows, well
        # short of the floor. Fixed by drawing the decision's own floor rule
        # up front (with the title, present the whole beat, same bracket
        # idiom as B00/B01/B07's rules) so the bbox reaches the safe-area
        # floor from frame 1 — the decision TEXT still lands late, above
        # this already-present rule, preserving the original reveal pacing.
        title = fit(Text("Audit One Rule Today", color=PALETTE["ink"], font_size=40), 11.0)
        title.to_edge(UP, buff=0.65)
        floor_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["gold"], stroke_width=2.5)
        floor_rule.to_edge(DOWN, buff=0.9)
        self.play(Write(title), Create(floor_rule), run_time=0.3)
        self.wait(1.0)

        steps_data = [
            ("Does the wording actually vary?", "not just one way to say it"),
            ("Does context flip the meaning?", "right here, wrong somewhere else"),
            ("Is exactness the whole point?", "a close match would be wrong"),
        ]

        rows = VGroup()
        for main, explain in steps_data:
            box = Square(side_length=0.46, color=PALETTE["slate"], stroke_width=3)
            main_txt = fit(Text(main, color=PALETTE["ink"], font_size=29, font=MONO), 11.2)
            explain_txt = fit(Text(explain, color=PALETTE["slate"], font_size=21), 11.2)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.5, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        if rows.width > 12.2:
            rows.scale_to_fit_width(12.2)
        if rows.height > 4.6:
            rows.scale_to_fit_height(4.6)
        rows.move_to(ORIGIN).shift(UP * 0.05)

        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.2)

        row_holds = [1.7, 1.7, 1.7]
        for row, hold in zip(rows, row_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        decision = VGroup(
            fit(Text("2 YES + 1 NO", color=PALETTE["teal"], font_size=30, font=MONO, weight="BOLD"), 9.6),
            fit(Text("-> move that rule to similarity matching", color=PALETTE["ink"], font_size=24), 11.8),
        ).arrange(DOWN, buff=0.22)
        decision.next_to(floor_rule, UP, buff=0.22)
        self.play(FadeIn(decision, shift=UP * 0.1), run_time=0.5)
        # tuned to the measured 21.22s Kokoro audio for B06.
        self.wait(12.82)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: statement card.
# measured audio: 9.41s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # GATE V fix (2026-09-07 patch): the original settled state measured
        # only ~20% safe-area coverage (real GATE V number) — the worst
        # underfill offender in the whole reel: just 2 short lines adrift in
        # a huge empty card. Fixed with BOTH levers the task calls for:
        # substantially bigger typography (28/26/22 -> 38/34/28) AND a
        # supporting visual treatment — a bordered card. First attempt
        # anchored the top/bottom rules to the TEXT (next_to), which still
        # measured only ~48% (real number) because the rules sat close to
        # the text with ~118px of unused safe margin above/below on each
        # side. Fixed by anchoring the rules to the SAFE FRAME itself
        # (to_edge, same convention as B00's title card) so the card reaches
        # close to the safe-area top/bottom regardless of how tall the text
        # block underneath happens to be.
        statement1 = fit(Text(
            "A keyword list only knows the words you thought of.",
            color=PALETTE["ink"], font_size=38
        ), 11.6)
        statement2 = fit(Text(
            "Embeddings measure the meaning you didn't have to spell out —",
            color=PALETTE["ink"], font_size=34
        ), 11.9)
        statement = VGroup(statement1, statement2).arrange(DOWN, buff=0.45)

        gap_line = fit(Text(
            "but only where closeness is actually what you want.",
            color=PALETTE["ink"], font_size=28
        ), 11.4)

        content = VGroup(statement, gap_line).arrange(DOWN, buff=0.85)
        content.move_to(ORIGIN)

        # card framing: top/bottom accent rules bracketing the whole card,
        # anchored to the safe frame (not the text) — same bracket idiom as
        # B00/B01's title cards — so the card reaches the safe-area floor
        # even though this beat has only 2-3 lines of text to work with.
        top_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["gold"], stroke_width=3)
        top_rule.to_edge(UP, buff=0.7)
        bottom_rule = Line(LEFT * 5.6, RIGHT * 5.6, color=PALETTE["gold"], stroke_width=3)
        bottom_rule.to_edge(DOWN, buff=1.0)

        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(statement), run_time=0.5)
        self.wait(0.2)

        highlight = Rectangle(
            width=gap_line.width + 0.5, height=gap_line.height + 0.3,
            fill_color=PALETTE["gold"], fill_opacity=0.15, stroke_width=0,
        ).move_to(gap_line.get_center())
        self.play(FadeIn(highlight), FadeIn(gap_line), Create(bottom_rule), run_time=0.5)
        # tuned to the measured 9.41s Kokoro audio for B07.
        self.wait(7.91)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: @HumanitariansAI, in for Sai Pranavi Jeedigunta.
# measured audio: 1.51s — a very short narration line ("Explained with
# Claude Code."), so this beat builds fast: nothing spends time mid-`Write()`
# past the QC sample points.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        handle = Text("@HumanitariansAI", color=PALETTE["slate"], font_size=32)
        accent = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(Text(
            "explained with Claude Code — in for Sai Pranavi Jeedigunta",
            color=PALETTE["ink"], font_size=17
        ), 9.5)
        VGroup(handle, accent, tagline).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        tagline_underline = Line(color=PALETTE["sage"], stroke_width=1)
        tagline_underline.put_start_and_end_on(
            tagline.get_corner(DL) + DOWN * 0.1, tagline.get_corner(DR) + DOWN * 0.1
        )

        self.play(FadeIn(handle, shift=UP * 0.1), Create(accent), run_time=0.4)
        self.play(FadeIn(tagline), run_time=0.3)
        self.play(Create(tagline_underline), run_time=0.2)
        # everything is a fully-formed static frame from here — tuned to the
        # measured 1.51s Kokoro audio for B08.
        self.wait(0.61)
