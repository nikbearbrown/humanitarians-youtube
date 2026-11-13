"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-09-22-hallucination-why-sounding-sure-isnt-being-right
"Hallucination: Why Sounding Sure Isn't the Same as Being Right"

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
  B00 TitleCard               — title re-wrapped onto narrower lines.
  B01 ExecSummary              — badge stacked ABOVE name/role; summary re-wrapped.
  B02 SameToneHook              — parent's LEFT/RIGHT bubbles -> TOP/BOTTOM stack.
  B03 ThreeQuestionsFramework   — already a vertical stack; cards narrowed, text re-wrapped.
  B04 FabricatedVsRealCitation  — parent's LEFT/RIGHT citations -> TOP/BOTTOM stack.
  B05 TrueFactFalsifiability    — parent's 3-across tag row -> 3 stacked tag cards.
  B06 AuditChecklist            — already single-column; items re-wrapped narrower.
  B07 Statement                 — centered text, re-wrapped onto narrower lines.
  B08 BrandOutro                — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around() are copied verbatim from
../scenes.py for visual continuity. Nothing about WHAT is said or WHEN
changes here (every self.play/self.wait duration matches ../scenes.py
beat-for-beat, so total runtime matches the landscape master exactly) —
only how it is laid out for the narrow canvas.
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


# --------------------------------------------------------------------------- #
# B00 — TITLE: silent opening card. measured (silent) duration: 4.06s.
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["Hallucination:", "Why Sounding Sure", "Isn't the Same", "as Being Right"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=40, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=6.6, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        self.wait(2.46)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked above name/role; summary re-wrapped.
# measured audio: 13.10s
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

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.12)
        header = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: why a",
            "confident-sounding answer",
            "from an AI model isn't",
            "the same thing as a",
            "correct one — and three",
            "questions that catch the",
            "difference before you",
            "act on it.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.14)

        VGroup(top_rule, header, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=7.2, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 2.1s; remainder tuned to the measured 12.648s Kokoro length
        # (2026-10-20 name-retrofit: "Sai Pranavi J.", was 13.10s -> wait 11.0)
        self.wait(10.55)


# --------------------------------------------------------------------------- #
# B02 — HOOK: parent's LEFT/RIGHT bubbles -> TOP/BOTTOM stack.
# measured audio: 12.50s
# --------------------------------------------------------------------------- #
class B02_SameToneHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Two answers.", color=PALETTE["bg"], font_size=26), MAX_W)
        title2 = fit(T("Same confident tone.", color=PALETTE["bg"], font_size=26), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.1)
        # buff 0.5 -> 0.75: GATE B's post-render layout audit caught this
        # 2-line title's real top edge at y=3.5, outside the +/-3.4
        # safe-area half-height on the true rendered portrait frame.
        title_block.to_edge(UP, buff=0.75)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        def bubble():
            p = panel(width=3.7, height=2.3, fill=PALETTE["ink"], stroke=PALETTE["teal_on_ink"])
            q = fit(T("“When did this happen?”", color=PALETTE["sage"], font_size=14), 3.3)
            a = fit(T(
                "“Yes — this is well\nestablished, and I'm\nconfident in the answer.”",
                color=PALETTE["bg"], font_size=14, line_spacing=1.15,
            ), 3.3)
            tag = T("?", color=PALETTE["gold"], font_size=26, font=MONO, weight="BOLD")
            content = VGroup(q, a, tag).arrange(DOWN, buff=0.16)
            content.move_to(p.get_center())
            return VGroup(p, content), tag

        top_group, top_tag = bubble()
        bot_group, bot_tag = bubble()
        # stack height trimmed (panel 2.6->2.3, gap 0.35->0.25) and centered
        # (no longer shifted down): GATE B's post-render layout audit caught
        # the closing zinger's real bounding box overlapping this stack's own
        # bottom panel's rounded-corner curve — real clearance needed on both
        # sides (title above, zinger below), not a guessed margin.
        stack = VGroup(top_group, bot_group).arrange(DOWN, buff=0.25)
        stack.move_to(ORIGIN)

        self.play(Create(top_group[0]), Create(bot_group[0]), run_time=0.5)
        self.play(FadeIn(top_group[1], shift=UP * 0.08), FadeIn(bot_group[1], shift=UP * 0.08), run_time=0.5)
        self.wait(4.5)

        top_label = T("REAL", color=PALETTE["sage"], font_size=22, font=MONO, weight="BOLD")
        top_label.move_to(top_tag.get_center())
        bot_label = T("FABRICATED", color=PALETTE["gold"], font_size=16, font=MONO, weight="BOLD")
        bot_label.move_to(bot_tag.get_center())
        self.play(
            FadeOut(top_tag), FadeOut(bot_tag),
            FadeIn(top_label), FadeIn(bot_label),
            run_time=0.5,
        )
        self.wait(2.0)

        top_box = box_around(top_label, buff=0.1, color=PALETTE["sage"])
        bot_box = box_around(bot_label, buff=0.1, color=PALETTE["gold"])
        self.play(Create(top_box), Create(bot_box), run_time=0.3)
        self.wait(0.7)

        zinger = fit(T("Nothing in the tone told\nyou which was which.", color=PALETTE["gold"], font_size=16, line_spacing=1.15), MAX_W)
        # buff 0.55 -> 0.65 (not higher): GATE B's post-render layout audit
        # caught this 2-line closing's real bounding box overlapping the
        # stack's bottom panel curve when buff was pushed too high (0.75) —
        # the smallest buff that still clears the -3.4 safe-area floor keeps
        # the most real clearance from the stack above.
        zinger.to_edge(DOWN, buff=0.65)
        self.play(Write(zinger), run_time=0.5)
        self.wait(1.5)


# --------------------------------------------------------------------------- #
# B03 — FRAMEWORK: already a vertical stack of 3 cards; narrowed for portrait.
# measured audio: 25.75s
# --------------------------------------------------------------------------- #
class B03_ThreeQuestionsFramework(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Three questions,", color=PALETTE["ink"], font_size=24), MAX_W)
        title2 = fit(T("before any example:", color=PALETTE["ink"], font_size=24), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.65)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        def make_card(num, label, body, accent):
            num_badge = Circle(radius=0.26, color=accent, fill_opacity=0, stroke_width=2.5)
            num_txt = T(num, color=accent, font_size=18, font=MONO, weight="BOLD")
            num_txt.move_to(num_badge.get_center())
            label_txt = fit(T(label, color=PALETTE["ink"], font_size=19, weight="BOLD"), MAX_W - 0.9)
            body_txt = fit(T(body, color=PALETTE["slate"], font_size=14, line_spacing=1.2), MAX_W - 0.9)
            text_col = VGroup(label_txt, body_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            # the badge + its number must travel together with the text as one
            # unit when `row` is later shifted — group them explicitly.
            row = VGroup(VGroup(num_badge, num_txt), text_col).arrange(RIGHT, buff=0.25)
            bg = panel(width=MAX_W + 0.3, height=row.height + 0.4, fill=PALETTE["bg"], stroke=accent, corner_radius=0.12)
            row.move_to(bg.get_center())
            return VGroup(bg, row)

        q1 = make_card("1", "Checkable?", "Is there something\nspecific you could verify?", PALETTE["teal"])
        q2 = make_card("2", "Would it hedge?", "Would it admit\nuncertainty if asked?", PALETTE["teal"])
        q3 = make_card("3", "Confidence tracks\ndifficulty?", "As sure about the hard\npart as the easy part?", PALETTE["crimson"])

        cards = VGroup(q1, q2, q3).arrange(DOWN, buff=0.28).move_to(ORIGIN).shift(DOWN * 0.3)

        self.play(FadeIn(cards, shift=UP * 0.1), run_time=0.6)
        self.wait(1.0)

        self.play(Indicate(q1[0], color=PALETTE["teal"], scale_factor=1.03), run_time=0.6)
        self.wait(4.9)
        self.play(Indicate(q2[0], color=PALETTE["teal"], scale_factor=1.03), run_time=0.6)
        self.wait(5.9)
        self.play(Indicate(q3[0], color=PALETTE["crimson"], scale_factor=1.03), run_time=0.6)
        self.wait(5.4)

        tell_box = box_around(q3, buff=0.05, color=PALETTE["crimson"])
        self.play(Create(tell_box), run_time=0.3)
        tell_caption = fit(T("That's the tell.", color=PALETTE["crimson"], font_size=20, weight="BOLD"), MAX_W)
        tell_caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(tell_caption, shift=UP * 0.1), run_time=0.4)
        self.wait(3.95)


# --------------------------------------------------------------------------- #
# B04 — WORKED-EXAMPLE: parent's LEFT/RIGHT citations -> TOP/BOTTOM stack.
# measured audio: 25.58s
# --------------------------------------------------------------------------- #
class B04_FabricatedVsRealCitation(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same fluent tone.", color=PALETTE["bg"], font_size=23), MAX_W)
        title2 = fit(T("One of these isn't real.", color=PALETTE["bg"], font_size=23), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.65)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        # Portrait has no spare width beside the cards (unlike the parent's
        # side-by-side layout), so the "CHECKABLE?" callout is built as a
        # real line INSIDE each card's own content column from the start
        # (not positioned beside the card), then swapped in place for the
        # VERIFIED / DOESN'T EXIST verdict — same tag-swap idiom as B02's
        # "?" -> REAL/FABRICATED reveal.
        def citation_card(header, cite_title, cite_meta, stroke):
            hdr = fit(T(header, color=PALETTE["sage"], font_size=14, font=MONO), MAX_W - 0.6)
            ct = fit(T(cite_title, color=PALETTE["bg"], font_size=15, line_spacing=1.2, weight="BOLD"), MAX_W - 0.6)
            meta = fit(T(cite_meta, color=PALETTE["bg"], font_size=13, line_spacing=1.2), MAX_W - 0.6)
            tag = T("CHECKABLE?", color=PALETTE["gold"], font_size=14, font=MONO, weight="BOLD")
            content = VGroup(hdr, ct, meta, tag).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            bg = panel(width=MAX_W, height=content.height + 0.7, fill=PALETTE["ink"], stroke=stroke)
            content.move_to(bg.get_center())
            return VGroup(bg, content), content, tag

        top_card, top_content, top_tag = citation_card(
            "CITATION A",
            "“Sparse Attention for\nLong-Context Transformers”",
            "Castillo, D. & Ng, P. (2021)\nJ. of Machine Learning Research",
            PALETTE["teal_on_ink"],
        )
        bot_card, bot_content, bot_tag = citation_card(
            "CITATION B",
            "“Recursive Calibration of\nLatent Confidence Vectors”",
            "Harrow, J. & Delacroix, M. (2022)\nJ. of Applied Neural Computation",
            PALETTE["teal_on_ink"],
        )
        stack = VGroup(top_card, bot_card).arrange(DOWN, buff=0.3)
        stack.move_to(ORIGIN).shift(DOWN * 0.15)

        self.play(Create(top_card[0]), Create(bot_card[0]), run_time=0.5)
        self.play(FadeIn(top_content, shift=UP * 0.1), FadeIn(bot_content, shift=UP * 0.1), run_time=0.6)
        # wait 8.4 = parent's 5.0 (hold on unresolved tags) + 3.0 (hold on
        # "CHECKABLE?") + 0.4 (parent's separate tag-FadeIn play, folded in
        # here since this layout's tag is already part of the first FadeIn).
        self.wait(8.4)

        verified = T("VERIFIED", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        verified.move_to(top_tag.get_center()).align_to(top_tag, LEFT)
        doesnt_exist = T("DOESN'T EXIST", color=PALETTE["gold"], font_size=15, font=MONO, weight="BOLD")
        doesnt_exist.move_to(bot_tag.get_center()).align_to(bot_tag, LEFT)
        self.play(
            FadeOut(top_tag), FadeOut(bot_tag),
            FadeIn(verified), FadeIn(doesnt_exist),
            run_time=0.5,
        )
        self.wait(4.5)

        alert_box = box_around(doesnt_exist, buff=0.1, color=PALETTE["gold"])
        self.play(Create(alert_box), run_time=0.3)
        closing = fit(T("The tone never told you.", color=PALETTE["gold"], font_size=18), MAX_W)
        closing.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        self.wait(8.88)


# --------------------------------------------------------------------------- #
# B05 — FALSIFIABILITY: parent's 3-across tag row -> 3 stacked tag cards.
# measured audio: 25.42s
# --------------------------------------------------------------------------- #
class B05_TrueFactFalsifiability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("Same tone. Genuinely", color=PALETTE["bg"], font_size=22), MAX_W)
        title2 = fit(T("true this time.", color=PALETTE["bg"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.65)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.5)

        fact_panel = panel(width=MAX_W + 0.2, height=1.9, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        fact_panel.move_to([0, 1.5, 0])
        fact_q = fit(T("“Boiling point of water\nat sea level?”", color=PALETTE["sage"], font_size=15, font=MONO, line_spacing=1.2), MAX_W - 0.3)
        fact_a = fit(T("“Yes — 100°C / 212°F.\nI'm confident in this.”", color=PALETTE["bg"], font_size=15, weight="BOLD", line_spacing=1.2), MAX_W - 0.3)
        fact_content = VGroup(fact_q, fact_a).arrange(DOWN, buff=0.2)
        fact_content.move_to(fact_panel.get_center())

        self.play(Create(fact_panel), run_time=0.5)
        self.play(FadeIn(fact_content, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)

        def check_tag(label, verdict):
            lbl = fit(T(label, color=PALETTE["bg"], font_size=14, font=MONO), MAX_W - 1.0)
            vd = fit(T(verdict, color=PALETTE["sage"], font_size=16, font=MONO, weight="BOLD"), MAX_W - 1.0)
            row = VGroup(lbl, vd).arrange(RIGHT, buff=0.3)
            bg = panel(width=MAX_W, height=row.height + 0.3, fill=PALETTE["ink"], stroke=PALETTE["sage"])
            row.move_to(bg.get_center())
            return VGroup(bg, row)

        t1 = check_tag("CHECKABLE?", "CONFIRMED")
        t2 = check_tag("WOULD IT HEDGE?", "NO NEED")
        t3 = check_tag("TRACKS DIFFICULTY?", "YES — EASY")
        tags = VGroup(t1, t2, t3).arrange(DOWN, buff=0.18)
        tags.move_to([0, -1.3, 0])

        self.play(FadeIn(tags, shift=UP * 0.1), run_time=0.6)
        self.wait(6.0)

        tags_box = box_around(tags, buff=0.12, color=PALETTE["sage"])
        self.play(Create(tags_box), run_time=0.3)
        self.wait(3.0)

        closing = fit(T("Same fluent tone.\nCompletely different,\ncorrect answer.", color=PALETTE["sage"], font_size=15, line_spacing=1.15), MAX_W)
        closing.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        self.wait(8.02)


# --------------------------------------------------------------------------- #
# B06 — SCAFFOLDED-TASK: already single-column; items re-wrapped narrower.
# measured audio: 23.16s
# --------------------------------------------------------------------------- #
class B06_AuditChecklist(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Try this on the next", color=PALETTE["ink"], font_size=22), MAX_W)
        title2 = fit(T("answer you get:", color=PALETTE["ink"], font_size=22), MAX_W)
        title_block = VGroup(title, title2).arrange(DOWN, buff=0.08)
        title_block.to_edge(UP, buff=0.65)
        self.play(Write(title_block), run_time=0.5)
        self.wait(1.0)

        def checklist_item(text):
            box = Square(side_length=0.4, color=PALETTE["teal"], stroke_width=3, fill_opacity=0)
            check = fit(T(text, color=PALETTE["ink"], font_size=17, line_spacing=1.2), MAX_W - 0.7)
            row = VGroup(box, check).arrange(RIGHT, buff=0.25)
            return row, box

        row1, box1 = checklist_item("Is it checkable —\nand did you check it?")
        row2, box2 = checklist_item("Would it hedge if\nyou pushed on it?")
        row3, box3 = checklist_item("Does its confidence\nchange with difficulty?")

        items = VGroup(row1, row2, row3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        list_panel = panel(width=items.width + 0.6, height=items.height + 0.7,
                            fill=PALETTE["bg"], stroke=PALETTE["slate"], corner_radius=0.15, opacity=1.0)
        list_panel.move_to(ORIGIN).shift(UP * 0.1)
        items.move_to(list_panel.get_center())

        self.play(Create(list_panel), run_time=0.4)
        self.play(FadeIn(items), run_time=0.6)
        self.wait(1.0)

        def make_check(box):
            c1 = Line(box.get_corner(DL), box.get_center(), color=PALETTE["crimson"], stroke_width=4)
            c2 = Line(box.get_center(), box.get_corner(UR), color=PALETTE["crimson"], stroke_width=4)
            return VGroup(c1, c2)

        mark1, mark2, mark3 = make_check(box1), make_check(box2), make_check(box3)

        self.play(Create(mark1), run_time=0.3)
        self.wait(5.3)
        self.play(Create(mark2), run_time=0.3)
        self.wait(5.3)
        self.play(Create(mark3), run_time=0.3)
        self.wait(4.0)

        closing = fit(T("No wavering confidence?\nThat's not certainty —\nthat's tone.", color=PALETTE["crimson"], font_size=17, line_spacing=1.2), MAX_W)
        closing.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        self.wait(3.76)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: centered text, re-wrapped onto narrower lines.
# measured audio: 11.14s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        lines1 = ["A model's tone is", "generated the same way", "whether it's right", "or wrong."]
        block1 = VGroup(*[fit(T(l, color=PALETTE["bg"], font_size=26), MAX_W) for l in lines1]).arrange(DOWN, buff=0.18)

        lines2a = ["The only question", "that matters:"]
        block2a = VGroup(*[fit(T(l, color=PALETTE["gold"], font_size=22), MAX_W) for l in lines2a]).arrange(DOWN, buff=0.12)
        quote = fit(T("“Can this actually\nbe checked?”", color=PALETTE["gold"], font_size=27, weight="BOLD", line_spacing=1.25), MAX_W)
        block2 = VGroup(block2a, quote).arrange(DOWN, buff=0.25)

        content = VGroup(block1, block2).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        frame = panel(width=MAX_W + 0.3, height=content.height + 1.0,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)
        frame.move_to(content.get_center())

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(block1, shift=UP * 0.1), run_time=0.6)
        self.wait(4.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.6)
        self.wait(2.5)

        question_box = box_around(quote, buff=0.12, color=PALETTE["gold"])
        self.play(Create(question_box), run_time=0.3)
        self.wait(2.84)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed for portrait.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # font sizes and buff bumped up: GATE V's canvas-fill check measured
        # this beat's real candidate export at only 39% of the safe area
        # (min 55%) — a real underfill. "handle" is already width-clamped at
        # MAX_W+0.3 (increasing its font_size alone doesn't add real size
        # once clamped), so the real fix is more buff (genuine added height)
        # plus bigger fixed_line/tagline text (not yet width-clamped at
        # MAX_W, so they gain real size).
        # buff bumped again (0.7 -> 1.0): GATE V's canvas-fill check still
        # measured only 50% of the safe area after the first round of fixes
        # (min 55%) — real added vertical mass, not a guessed margin.
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
