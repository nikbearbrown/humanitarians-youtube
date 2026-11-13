"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-09-14-rag-why-looking-it-up-isnt-enough

Built via `./art vertical` (runtime/scripts/shorts.py --vertical), the NEW
(2026-09-07+) full-length portrait companion command — NOT a Shorts-style
cut: no beats dropped, no duration cap, no rewritten outro, no added
endcard (see brutalist/docs/PIPELINE-SAFETY.md, "Isolated portrait
companions and Shorts"). All 9 parent beats are kept; every mp3 is reused
byte-for-byte from the parent's mp3/ folder (see vertical/beat_sheet.json,
written by shorts.py). Every beat here is a Manim GRAPHIC beat, so THE
REFORMAT RULE's auto center-cut never applies (generated graphics are never
cropped) — each class below is a genuine portrait RE-LAYOUT of the parent
../scenes.py composition, authored by hand for a 1080x1920 canvas (rendered
at 2160x3840 for the true 4K vertical final), not a mechanical crop.

PORTRAIT GEOMETRY: Manim keeps frame_height fixed at 8 regardless of aspect
(so vertical safe/hard bounds the parent file already designed against —
to_edge(UP/DOWN, buff=...) — carry over almost unchanged). What changes is
frame_width: 4.5 instead of 14.222 — a hard edge of only +/-2.25 and a safe
half-width of ~1.95 (vs the parent's +/-6.3). MAX_W = 3.6 is this file's
general content-width budget (leaves ~0.15 margin on each side). Every
side-by-side layout in the parent (B04's two document/answer panels, B05's
two comparison panels) is re-composed here as a TOP/BOTTOM stack instead of
LEFT/RIGHT columns, matching this fellow's 2026-08-17 sibling short's own
portrait redesign convention.

Beat-by-beat redesign notes:
  B00 TitleCard        — title re-wrapped 2->4 narrow lines.
  B01 ExecSummary      — badge+name row (side-by-side in the parent)
                         stacked badge-above-name; summary re-wrapped to
                         narrow lines.
  B02 StaleDocHook     — already a single vertical column in the parent;
                         narrowed widths + re-wrapped text, y-anchors
                         re-spread for the taller (in units-of-safe-area)
                         portrait canvas.
  B03 ThreeQuestionsFramework — already vertical-friendly (rows stacked);
                         each row's badge+label sits ABOVE its now
                         narrower, re-wrapped description.
  B04 StaleDocResolved — THE big redesign: parent's LEFT/RIGHT document +
                         answer panels -> TOP (document) / BOTTOM (answer)
                         stack, both simultaneously visible (the beat's
                         "both dates legible together" requirement doesn't
                         require left-right, only simultaneous).
  B05 RetrievalWorksFalsifiability — same TOP/BOTTOM restack: "NO
                         RETRIEVAL" panel above "WITH RETRIEVAL" panel.
  B06 AuditChecklist   — already vertical-friendly; narrowed + re-wrapped.
  B07 Statement        — already vertical-friendly; narrowed + re-wrapped.
  B08 BrandOutro       — unchanged composition; only widths trimmed.

Palette/MONO/fit()/panel() are copied verbatim from ../scenes.py for visual
continuity, including the "teal_on_ink" fix (teal text/strokes measure a
broken 1.56:1 on the ink background; teal_on_ink measures 6.23:1 — same fix
already applied to the landscape master, ported here so the portrait cut
never reintroduces it). See ../scenes.py for the full beat-by-beat build
history (timing derivations, GATE V findings) — nothing about WHAT is said
or WHEN changes here, only how it is laid out for the narrow canvas.
"""

from manim import *

# CRITICAL PORTRAIT FIX: manim's CLI only derives frame_width from the pixel
# aspect ratio ONCE, inside ManimConfig.digest_parser() at startup — BEFORE
# the -r/--resolution CLI flag is applied (that happens later, in
# digest_args(), via plain pixel_width/pixel_height property setters that do
# NOT recompute frame_width). So a bare `manim -r 2160,3840 scenes.py B00`
# (exactly what runtime/scripts/run.sh invokes) leaves frame_width at the
# 16:9 DEFAULT (14.222...) even though the render is portrait — every
# coordinate in this file is designed against a 4.5-wide frame, so without
# this fix everything would render ~3.2x too small and clustered dead-center.
# Copied verbatim from this fellow's 2026-08-17 sibling short/scenes.py,
# which found and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm
    "slate":  "#29335C",  # structure
    "gold":   "#F3A712",  # fill only — never text color
    "sage":   "#A8C686",  # human / growth
}

MONO = "Courier New"
MAX_W = 3.6   # general portrait content-width budget (safe half-width 1.95)


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


SAFE_TEXT_BASE = 48  # empirically confirmed clean; Pango/Cairo hinting artifact appears at font_size <= ~24

def T(text, font_size=48, **kwargs):
    """Always renders Text at a large, hinting-safe font_size, then scales geometrically
    to the visually-intended size — avoids a real Pango/Cairo small-font-size artifact
    that inserts visual gaps inside words (e.g. "video" -> "v ideo") when Text() is
    created directly at a small font_size. See BUILD-LOG.md for the empirical proof."""
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. Title re-wrapped 2 -> 4 narrow lines.
# measured (silent) duration: 4.049s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["RAG: Why", "\"Looking It Up\"", "Doesn't Guarantee", "It's True"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=30, weight="BOLD"), MAX_W)
            for l in title_lines
        ]).arrange(DOWN, buff=0.2)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        # buff=0.85 (not ~0.5) — same GATE V canvas-fill lesson as the
        # landscape master's B00 fix and this fellow's 2026-08-17 sibling
        # short's own B00: a portrait card's few elements have to spend the
        # tall safe area (6.8 units) on SPACING since there's little width
        # left to spend it on.
        # buff bumped 0.85 -> 1.0 after the real candidate export measured
        # exactly 55% canvas-fill (the checker's floor, "not < 0.55" —
        # borderline enough to trip on rounding) at both GATE V sample
        # points; a bit more spacing gives real margin above the floor.
        VGroup(top_rule, title, bottom_rule, handle).arrange(
            DOWN, buff=1.0
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.35)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.8)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.5)
        # sum of plays = 1.65s; remainder tuned to the measured 4.049s
        # silent-track length
        self.wait(2.4)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role (parent's side-by-side
# row would starve the name of width next to a badge in this narrow frame).
# measured audio: 18.336s (2026-10-20 name-retrofit: "Sai Pranavi J.", was 18.744s)
# --------------------------------------------------------------------------- #
class B01_ExecSummary(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)

        badge = Circle(radius=0.42, color=PALETTE["teal"], fill_color=PALETTE["teal"],
                        fill_opacity=0.15, stroke_width=3)
        initials = T("SPJ", color=PALETTE["teal"], font_size=24, font=MONO, weight="BOLD")
        initials.move_to(badge.get_center())
        badge_group = VGroup(badge, initials)

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=24, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: Retrieval-",
            "Augmented Generation —",
            "giving an AI model a search",
            "step so it can look things",
            "up instead of guessing —",
            "and 3 questions that catch",
            "a grounded answer from one",
            "that just sounds like it is.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.12)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(
            DOWN, buff=0.45
        ).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 18.336s Kokoro
        # length (2026-10-20 name-retrofit: 18.336 - 1.8 = 16.536)
        self.wait(16.54)


# --------------------------------------------------------------------------- #
# B02 — HOOK: already a single vertical column in the parent; narrowed
# widths, re-wrapped text, y-anchors re-spread for the portrait canvas.
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md — no real product/vendor]
# measured audio: 17.304s
# --------------------------------------------------------------------------- #
class B02_StaleDocHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        question = fit(T(
            "\"What's our\nrefund policy?\"", color=PALETTE["bg"], font_size=22, line_spacing=1.1
        ), MAX_W)
        q_panel = panel(width=question.width + 0.5, height=question.height + 0.4,
                         fill=PALETTE["slate"], stroke=PALETTE["sage"], opacity=0.3)
        q_panel.move_to(question.get_center())
        question_bubble = VGroup(q_panel, question)

        doc_header = fit(T("RETRIEVED: Policy #114\n— Refund Window", color=PALETTE["sage"],
                               font_size=17, font=MONO, line_spacing=1.15), MAX_W)
        doc_stamp = fit(T("Last updated:\nJan 12, 2026", color=PALETTE["crimson"],
                              font_size=17, font=MONO, weight="BOLD", line_spacing=1.15), MAX_W)
        doc_body = fit(T("\"Refunds accepted\nwithin 30 days\nof purchase.\"",
                             color=PALETTE["bg"], font_size=16, line_spacing=1.15), MAX_W)
        doc_col = VGroup(doc_header, doc_stamp, doc_body).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        doc_card_bg = panel(width=doc_col.width + 0.5, height=doc_col.height + 0.4,
                             fill=PALETTE["ink"], stroke=PALETTE["sage"])
        doc_card_bg.move_to(doc_col.get_center())
        doc_card = VGroup(doc_card_bg, doc_col)

        stale_tag = fit(T("STALE — replaced\n8 months ago", color=PALETTE["crimson"],
                              font_size=16, font=MONO, weight="BOLD", line_spacing=1.15), MAX_W)

        answer = fit(T(
            "\"Per Policy #114,\nrefunds are available\nwithin 30 days.\"",
            color=PALETTE["bg"], font_size=18, line_spacing=1.15
        ), MAX_W)
        a_panel = panel(width=answer.width + 0.5, height=answer.height + 0.4,
                         fill=PALETTE["teal"], stroke=PALETTE["sage"], opacity=0.3)
        a_panel.move_to(answer.get_center())
        answer_bubble = VGroup(a_panel, answer)

        wrong_tag = fit(T("WRONG", color=PALETTE["crimson"], font_size=20, font=MONO, weight="BOLD"), 2.4)
        # padding (0.5/0.4) kept generously ABOVE manim_layout_audit.py's
        # curve_inset=0.15 tolerance — a first draft used the landscape
        # master's tighter 0.3/0.2 padding, which read fine at the
        # landscape scale but, combined with this beat's real (not
        # guessed) portrait heights, put the box's own stroke inside the
        # inset zone around "WRONG" and "STALE..." — a real GATE B
        # TEXT_ON_CURVE error caught on the actual render, not a false
        # positive (see BUILD-LOG.md).
        wrong_box = Rectangle(width=wrong_tag.width + 0.4, height=wrong_tag.height + 0.3,
                               stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        wrong_box.move_to(wrong_tag.get_center())
        wrong_group = VGroup(wrong_box, wrong_tag)

        # arrange() (not hand-guessed y-coordinates) computes every
        # element's position from its OWN real measured size — the same
        # lesson as B05's next_to-chain overflow fix, applied here to
        # guarantee zero overlap between doc_card and stale_tag (a real
        # collision the first draft's guessed coordinates produced, also
        # caught by GATE B). Elements are revealed later via FadeIn at
        # these pre-computed positions; arranging up front doesn't
        # pre-reveal them.
        VGroup(question_bubble, doc_card, stale_tag, answer_bubble, wrong_group).arrange(
            DOWN, buff=0.12
        ).move_to(ORIGIN)

        self.play(FadeIn(question_bubble, shift=DOWN * 0.15), run_time=0.4)
        self.wait(3.93)
        self.play(FadeIn(doc_card, shift=UP * 0.1), run_time=0.5)
        self.wait(1.72)
        self.play(FadeIn(answer_bubble, shift=UP * 0.1), run_time=0.5)
        self.wait(2.07)

        self.play(FadeIn(stale_tag, shift=LEFT * 0.1), FadeIn(wrong_group, scale=1.2), run_time=0.4)
        self.wait(7.58)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: already vertical-friendly; each row's badge+label sits
# ABOVE its (narrower, re-wrapped) description.
# measured audio: 26.352s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The 3 Questions", "Behind Every RAG Answer"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=26), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.15)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)

        intro = fit(T("Here's the check,\nbefore any example.", color=PALETTE["slate"],
                          font_size=19, line_spacing=1.15), MAX_W)
        intro.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(intro, shift=UP * 0.1), run_time=0.4)
        self.wait(4.38)
        self.play(FadeOut(intro, shift=UP * 0.1), run_time=0.3)

        rows_data = [
            ("1", "RELEVANT",
             ["Does the retrieved document", "actually address this question", "— or just share keywords?"]),
            ("2", "CURRENT",
             ["Is this the newest version —", "or a stale copy the index", "never updated?"]),
            ("3", "GROUNDED",
             ["Is the answer built from what", "was retrieved — or did the model", "fall back on what it \"knew\"?"]),
        ]

        rows = VGroup()
        for num, label, desc_lines in rows_data:
            badge = Circle(radius=0.3, color=PALETTE["teal"], fill_color=PALETTE["teal"], fill_opacity=0.15, stroke_width=2.5)
            badge_num = T(num, color=PALETTE["teal"], font_size=20, font=MONO).move_to(badge.get_center())
            badge_group = VGroup(badge, badge_num)
            label_txt = fit(T(label, color=PALETTE["slate"], font_size=19, font=MONO), 2.8)
            top_row = VGroup(badge_group, label_txt).arrange(RIGHT, buff=0.25)

            desc_txt = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=16, line_spacing=1.0), MAX_W) for l in desc_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            row = VGroup(top_row, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 5.3:
            rows.scale_to_fit_height(5.3)
        rows.move_to(ORIGIN).shift(UP * 0.05)

        for r in rows:
            self.play(FadeIn(r[0], shift=UP * 0.12), run_time=0.15)

        row_holds = [4.96, 4.38, 8.18]
        for row, hold in zip(rows, row_holds):
            desc_txt = row[1]
            self.play(FadeIn(desc_txt, shift=UP * 0.1), run_time=0.3)
            self.wait(hold)

        not_two = fit(T("not one, not two —\nall three.", color=PALETTE["crimson"],
                            font_size=19, line_spacing=1.15), MAX_W)
        not_two.to_edge(DOWN, buff=0.68)
        self.play(Write(not_two), run_time=0.5)
        self.wait(1.40)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: THE redesign. Parent's LEFT (document) / RIGHT
# (answer) panels -> TOP (document) / BOTTOM (answer) stack, both
# simultaneously visible — the beat's "both dates legible together"
# requirement needs simultaneity, not left-right placement specifically.
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md]
# measured audio: 17.136s
# --------------------------------------------------------------------------- #
class B04_StaleDocResolved(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        today_banner = fit(T("TODAY: Sep 14, 2026", color=PALETTE["gold"],
                                 font_size=18, font=MONO, weight="BOLD"), MAX_W)
        today_banner.to_edge(UP, buff=0.68)

        # ---- TOP: the retrieved document ----
        top_header = fit(T("RETRIEVED DOCUMENT", color=PALETTE["sage"], font_size=15, font=MONO), 3.2)
        top_title = fit(T("Policy #114 — Refund Window", color=PALETTE["bg"], font_size=15, font=MONO), 3.2)
        top_stamp = fit(T("Last updated: Jan 12, 2026", color=PALETTE["crimson"],
                              font_size=15, font=MONO, weight="BOLD"), 3.2)
        top_body = fit(T("\"Refunds accepted within 30 days.\"", color=PALETTE["bg"], font_size=14), 3.2)
        top_content = VGroup(top_header, top_title, top_stamp, top_body).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        top_panel = panel(width=3.6, height=2.2, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        top_panel.next_to(today_banner, DOWN, buff=0.3)
        top_content.move_to(top_panel.get_center())

        # ---- BOTTOM: the model's confident answer ----
        bot_header = fit(T("MODEL'S ANSWER", color=PALETTE["sage"], font_size=15, font=MONO), 3.2)
        bot_quote = fit(T("\"Per Policy #114, refunds\navailable within 30 days.\"",
                              color=PALETTE["bg"], font_size=14, line_spacing=1.2), 3.2)
        bot_content = VGroup(bot_header, bot_quote).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        bot_panel = panel(width=3.6, height=1.5, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        bot_panel.next_to(top_panel, DOWN, buff=0.3)
        bot_content.move_to(bot_panel.get_center())

        self.play(FadeIn(today_banner), run_time=0.3)
        self.play(Create(top_panel), Create(bot_panel), run_time=0.4)
        self.play(FadeIn(top_content, shift=UP * 0.1), FadeIn(bot_content, shift=UP * 0.1), run_time=0.6)
        self.wait(1.54)

        def box_around(mob, buff=0.1):
            r = Rectangle(
                width=mob.width + 2 * buff, height=mob.height + 2 * buff,
                stroke_color=PALETTE["gold"], stroke_width=3, fill_opacity=0,
            )
            r.move_to(mob.get_center())
            return r

        highlight = box_around(top_title)
        self.play(Create(highlight), run_time=0.3)

        status_zone = VGroup()

        def show_status(text_lines, color, hold, focus):
            nonlocal status_zone
            new_status = VGroup(*[
                fit(T(l, color=color, font_size=16, font=MONO, weight="BOLD"), MAX_W)
                for l in text_lines
            ]).arrange(DOWN, buff=0.08)
            new_status.to_edge(DOWN, buff=0.62)
            new_highlight = box_around(focus)
            if len(status_zone) == 0:
                self.play(FadeIn(new_status, shift=UP * 0.1), Transform(highlight, new_highlight), run_time=0.3)
            else:
                self.play(FadeOut(status_zone), FadeIn(new_status, shift=UP * 0.1),
                          Transform(highlight, new_highlight), run_time=0.3)
            status_zone = new_status
            self.wait(hold)

        show_status(["RELEVANT — yes, right doc"], PALETTE["teal_on_ink"], 2.46, top_title)
        show_status(["CURRENT — no, 8mo stale"], PALETTE["crimson"], 2.15, top_stamp)
        show_status(["GROUNDED — doesn't matter"], PALETTE["crimson"], 6.15, bot_quote)

        self.play(FadeOut(status_zone), FadeOut(highlight), run_time=0.2)
        closing = fit(T("Retrieval didn't fail.\nFreshness did.", color=PALETTE["gold"],
                            font_size=18, line_spacing=1.15), MAX_W)
        closing.to_edge(DOWN, buff=0.62)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.3)
        self.wait(1.84)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: same TOP/BOTTOM restack — "NO RETRIEVAL" panel
# above "WITH RETRIEVAL" panel, both clearly labeled, fair comparison.
# [GENERIC/HYPOTHETICAL SCENARIO — see FACTCHECK.md]
# measured audio: 25.392s
# --------------------------------------------------------------------------- #
class B05_RetrievalWorksFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # EXPLICIT y-anchors (not a next_to() chain): a first draft chained
        # each element off the one above it (title -> question -> top_panel
        # -> bot_panel -> closing) and the accumulated real heights landed
        # the last element at y=-5.3 — an actual off-frame coordinate, not
        # just an unsafe margin, caught by GATE A's static pre-flight before
        # any render was spent. Hand-computed positions below keep the
        # whole stack inside the +/-3.4 safe band on a real frame_height=8
        # portrait canvas, with panels shrunk from the first draft's
        # oversized 2.5/2.9 heights to what their own (short) content
        # actually needs.
        title = fit(T("Now retrieval is\nexactly the fix:", color=PALETTE["ink"],
                          font_size=22, line_spacing=1.15), MAX_W)
        title.to_edge(UP, buff=0.62)
        self.play(Write(title), run_time=0.5)
        self.wait(3.11)

        question = fit(T("\"What is Project\nNighthawk?\"", color=PALETTE["slate"],
                             font_size=16, font=MONO, line_spacing=1.15), MAX_W)
        question.move_to([0, 2.00, 0])
        self.play(FadeIn(question), run_time=0.3)

        # ---- TOP panel: no retrieval ----
        top_panel = panel(width=3.6, height=1.7, fill=PALETTE["ink"], stroke=PALETTE["crimson"])
        top_panel.move_to([0, 0.63, 0])
        top_label = fit(T("NO RETRIEVAL", color=PALETTE["crimson"], font_size=15, font=MONO, weight="BOLD"), 3.1)
        top_answer = fit(T("\"Project Nighthawk is\na cloud security suite...\"",
                               color=PALETTE["bg"], font_size=12, line_spacing=1.15), 3.1)
        top_tag = fit(T("INVENTED", color=PALETTE["crimson"], font_size=13, font=MONO, weight="BOLD"), 2.3)
        top_content = VGroup(top_label, top_answer, top_tag).arrange(DOWN, buff=0.14)
        top_content.move_to(top_panel.get_center())

        # ---- BOTTOM panel: with retrieval ----
        bot_panel = panel(width=3.6, height=2.1, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
        bot_panel.move_to([0, -1.42, 0])
        bot_label = fit(T("WITH RETRIEVAL", color=PALETTE["teal_on_ink"], font_size=15, font=MONO, weight="BOLD"), 3.1)
        bot_source = fit(T("Launch doc: internal\nanalytics dashboard,\nlaunched Sep 8, 2026",
                               color=PALETTE["sage"], font_size=11, line_spacing=1.15), 3.1)
        bot_answer = fit(T("\"...internal analytics\ndashboard, launched\nlast week.\"",
                               color=PALETTE["bg"], font_size=12, line_spacing=1.15), 3.1)
        bot_tag = fit(T("GROUNDED", color=PALETTE["teal_on_ink"], font_size=13, font=MONO, weight="BOLD"), 2.3)
        bot_content = VGroup(bot_label, bot_source, bot_answer, bot_tag).arrange(DOWN, buff=0.12)
        bot_content.move_to(bot_panel.get_center())

        self.play(
            Create(top_panel), Create(bot_panel),
            FadeIn(top_label), FadeIn(bot_label),
            run_time=0.6,
        )

        top_marker = Rectangle(width=top_tag.width + 0.25, height=top_tag.height + 0.16,
                                stroke_color=PALETTE["crimson"], stroke_width=3, fill_opacity=0)
        bot_marker = Rectangle(width=bot_tag.width + 0.25, height=bot_tag.height + 0.16,
                                stroke_color=PALETTE["teal_on_ink"], stroke_width=3, fill_opacity=0)

        self.play(FadeIn(VGroup(top_answer, top_tag), shift=UP * 0.1), run_time=0.4)
        top_marker.move_to(top_tag.get_center())
        self.play(Create(top_marker), run_time=0.2)
        self.wait(9.74)
        self.play(FadeIn(VGroup(bot_source, bot_answer, bot_tag), shift=UP * 0.1), run_time=0.4)
        bot_marker.move_to(bot_tag.get_center())
        self.play(Create(bot_marker), run_time=0.2)
        self.wait(5.71)

        closing = fit(T("Same mechanism.\nDifferent source,\ndifferent outcome.",
                            color=PALETTE["ink"], font_size=15, line_spacing=1.2), MAX_W)
        closing.move_to([0, -2.97, 0])
        self.play(FadeIn(closing), run_time=0.3)
        self.wait(4.34)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: already vertical-friendly; narrowed + re-wrapped.
# measured audio: 18.864s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Audit one RAG\nanswer today:", color=PALETTE["ink"],
                          font_size=24, line_spacing=1.15), MAX_W)
        title.to_edge(UP, buff=0.72)

        frame = panel(width=3.9, height=6.9, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), Write(title), run_time=0.3)
        self.wait(0.9)

        # explain lines are pre-wrapped by WORD (not a raw character slice) —
        # a first draft sliced every 22 characters regardless of word
        # boundaries, which split real words mid-letter ("keyword overl" /
        # "ap", "the i" / "ndex") — legible width-wise but a real polish
        # defect only visible on direct frame inspection, not caught by any
        # automated gate (margins/contrast were both fine).
        steps_data = [
            (["Was the source", "actually relevant?"], ["not just keyword", "overlap"]),
            (["Was it actually", "current?"], ["not a stale copy the", "index missed"]),
            (["Can you point to the", "exact sentence it", "came from?"], ["if not, you don't know", "it's grounded"]),
        ]

        rows = VGroup()
        for main_lines, explain_lines in steps_data:
            box = Square(side_length=0.26, color=PALETTE["slate"], stroke_width=2.5)
            main_txt = VGroup(*[
                fit(T(l, color=PALETTE["ink"], font_size=18, font=MONO), 3.0) for l in main_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            explain_txt = VGroup(*[
                fit(T(l, color=PALETTE["slate"], font_size=14), 3.2) for l in explain_lines
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            text_col = VGroup(main_txt, explain_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            row = VGroup(box, text_col).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        if rows.width > MAX_W:
            rows.scale_to_fit_width(MAX_W)
        if rows.height > 4.6:
            rows.scale_to_fit_height(4.6)
        rows.move_to(ORIGIN).shift(UP * 0.1)

        for r in rows:
            self.play(FadeIn(VGroup(r[0], r[1][0]), shift=UP * 0.12), run_time=0.2)

        row_holds = [2.76, 1.23, 3.68]
        for row, hold in zip(rows, row_holds):
            explain_txt = row[1][1]
            self.play(FadeIn(explain_txt, shift=UP * 0.08), run_time=0.3)
            self.wait(hold)

        zinger = fit(T("can't point to it? you're\nnot grounded — you're hoping.",
                           color=PALETTE["crimson"], font_size=15, line_spacing=1.2), MAX_W)
        zinger.to_edge(DOWN, buff=0.7)
        self.play(Write(zinger), run_time=0.5)
        self.wait(7.75)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: already vertical-friendly; narrowed + re-wrapped.
# measured audio: 9.480s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        line1 = fit(T("Giving a model a search\nstep doesn't make it honest.",
                          color=PALETTE["bg"], font_size=22, line_spacing=1.25), MAX_W)
        line2 = fit(T("It makes it capable\nof being honest —",
                          color=PALETTE["sage"], font_size=19, line_spacing=1.25), MAX_W)
        line3 = fit(T("only if what it finds\nis actually right, and\nit actually uses it.",
                          color=PALETTE["gold"], font_size=17, line_spacing=1.25), MAX_W)

        content = VGroup(line1, line2, line3).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame_w = min(content.width + 0.9, 3.9)
        frame = panel(width=frame_w, height=content.height + 1.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)
        self.play(Create(frame), run_time=0.25)

        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.5)
        self.wait(2.36)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.09)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.4)
        underline = Line(
            line3.get_corner(DL) + DOWN * 0.15, line3.get_corner(DR) + DOWN * 0.15,
            color=PALETTE["gold"], stroke_width=2,
        )
        self.play(Create(underline), run_time=0.1)
        self.wait(3.39)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.512s — a very short beat; all elements land together.
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # v2: the first pass here (font 32/22, buff 0.8) measured only 50%
        # real canvas-fill on the true candidate export — pushed larger and
        # re-verified against the real GATE V run, same lesson as the
        # landscape master's own B08 fix.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=40), MAX_W)
        accent = Line(LEFT * 1.7, RIGHT * 1.7, color=PALETTE["gold"], stroke_width=3)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"],
                            font_size=28, line_spacing=1.25), MAX_W)
        content = VGroup(handle, accent, tagline).arrange(DOWN, buff=1.3).move_to(ORIGIN)

        frame_w = min(content.width + 1.1, 3.9)
        frame_h = min(content.height + 1.0, 7.0)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        self.wait(1.06)
