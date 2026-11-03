"""
Manim scenes — 9:16 PORTRAIT VERTICAL COMPANION derived from
2026-10-06-the-classifier-that-learned-when-not-to-guess

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
(so the parent file's y-axis safe/hard bounds carry over broadly unchanged;
only frame_width shrinks). What changes is frame_width: ~4.5 instead of
14.222 — a hard edge of only +/-2.25 and a safe half-width of ~1.95 (vs the
parent's +/-6.3). MAX_W = 3.6 is this file's general content-width budget
(leaves ~0.15 margin on each side). Every side-by-side layout in the parent
(B04's two branch cards, B05's 4-tile row) is re-composed here as a single
vertical chain / stacked column instead — matching this fellow's
2026-09-29 sibling reel's own portrait-redesign convention.

Beat-by-beat redesign notes:
  B00 TitleCard         — unchanged 3-line title, narrowed.
  B01 ExecSummary       — badge stacked ABOVE name/role; summary re-wrapped.
  B02 CounterHook       — each row's number stacked ABOVE its label (was
                          side-by-side) to fit the narrow width; same 3
                          persistent rows + zinger, one centered column.
  B03 ResidualHeadlines — already near-single-column; narrower cards.
  B04 PipelineDiagram   — THE big redesign: parent's side-by-side YES/NO
                          branch cards -> a single vertical chain: Normalize
                          -> gate -> NEW node -> bypass node -> merge, each
                          its own full-width stacked card.
  B05 ProofNumbers      — parent's 4-tile horizontal row -> 2x2 grid.
  B06 HonestLimits      — parent's 2-column declined list -> single column.
  B07 Statement         — unchanged composition; narrower, re-wrapped.
  B08 BrandOutro        — unchanged composition; widths trimmed.

Palette/MONO/fit()/T()/panel()/box_around() are copied verbatim from
../scenes.py for visual continuity. See ../scenes.py for the full beat-by-
beat build history (timing derivations, GATE V findings) — nothing about
WHAT is said or WHEN changes here, only how it is laid out for the narrow
canvas.
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
# Copied verbatim from this fellow's sibling reels' vertical/scenes.py,
# which found and documented this exact bug.
if config.pixel_height > config.pixel_width:
    config.frame_height = 8.0
    config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

PALETTE = {
    "bg":     "#F3EBDD",  # CREAM
    "ink":    "#2F2A26",  # INK
    "teal":   "#1F4E5F",  # good / CVD-safe cool -- only ever legible on "bg"
    "teal_on_ink": "#5FB8CC",  # lightened teal for ink backgrounds (6.23:1)
    "crimson": "#E4572E", # bad / CVD-safe warm -- avoid as TEXT on ink
    "slate":  "#29335C",  # structure -- avoid as TEXT on ink (low contrast)
    "gold":   "#F3A712",  # fill/stroke/accent; also safe as TEXT on ink
    "sage":   "#A8C686",  # human / growth; safe secondary text color on ink
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
# B00 — TITLE: silent opening card. Same 3-line title, narrowed.
# measured (silent) duration: 4.05s
# --------------------------------------------------------------------------- #
class B00_TitleCard(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title_lines = ["The Classifier", "That Learned", "When Not to Guess"]
        title = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=42, weight="BOLD"), MAX_W) for l in title_lines
        ]).arrange(DOWN, buff=0.22)

        top_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        bottom_rule = Line(LEFT * 1.5, RIGHT * 1.5, color=PALETTE["gold"], stroke_width=3)
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=26), MAX_W)

        VGroup(top_rule, title, bottom_rule, handle).arrange(DOWN, buff=0.85).move_to(ORIGIN)

        frame = panel(width=3.9, height=6.8, fill=PALETTE["bg"], stroke=PALETTE["gold"],
                       corner_radius=0.2, opacity=0.0)
        frame.set_stroke(width=2.5)

        self.play(Create(frame), run_time=0.3)
        self.play(Create(top_rule), run_time=0.3)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.6)
        self.play(Create(bottom_rule), FadeIn(handle, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 1.6s; remainder tuned to the measured 4.05s silent track
        self.wait(2.45)


# --------------------------------------------------------------------------- #
# B01 — EXEC-SUMMARY: badge stacked ABOVE name/role (parent's side-by-side
# row would starve the name of width next to a badge in this narrow frame).
# measured audio: 17.59s
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

        name = fit(T("Sai Pranavi J.", color=PALETTE["ink"], font_size=26, weight="BOLD"), MAX_W)
        role = fit(T("Humanitarians AI Fellow", color=PALETTE["slate"], font_size=18), MAX_W)
        name_block = VGroup(name, role).arrange(DOWN, buff=0.15)
        header_col = VGroup(badge_group, name_block).arrange(DOWN, buff=0.25)

        summary_lines = [
            "This video: teaching our",
            "regulatory pipeline to ask",
            "a local AI model for help",
            "on headlines it couldn't",
            "classify — and why the",
            "honest answer was",
            "“I don't know,” most",
            "of the time.",
        ]
        summary = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=19), MAX_W) for l in summary_lines
        ]).arrange(DOWN, buff=0.1)

        VGroup(top_rule, header_col, summary, bottom_rule).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(Create(top_rule), run_time=0.3)
        self.play(Create(badge), FadeIn(initials), run_time=0.4)
        self.play(FadeIn(name_block, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.1), Create(bottom_rule), run_time=0.6)
        # sum of plays = 1.8s; remainder tuned to the measured 16.896s Kokoro
        # length (2026-10-20 name-retrofit: 16.896 - 1.8 = 15.096)
        self.wait(15.1)


# --------------------------------------------------------------------------- #
# B02 — HOOK: each row's number stacked ABOVE its label (parent's
# number-beside-label row is too wide for this frame); same 3 persistent
# rows + zinger, one centered column spanning most of the safe height.
# measured audio: 14.86s
# --------------------------------------------------------------------------- #
class B02_CounterHook(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("21 headlines.\nUnknown Source.", color=PALETTE["bg"],
                       font_size=24, line_spacing=1.2), MAX_W)
        divider = Line(LEFT * 1.4, RIGHT * 1.4, color=PALETTE["gold"], stroke_width=3)

        def row(number, label, color, num_fs):
            num_txt = T(number, color=color, font_size=num_fs, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["bg"], font_size=18, line_spacing=1.15), MAX_W)
            return VGroup(num_txt, lab_txt).arrange(DOWN, buff=0.12)

        r1 = row("21", "fell through to\nUnknown Source", PALETTE["bg"], 44)
        r2 = row("13", "resolved by fixes\nalready shipped", PALETTE["sage"], 44)
        r3 = row("8", "remain, genuinely\nunresolved", PALETTE["gold"], 50)
        rows = VGroup(r1, r2, r3).arrange(DOWN, buff=0.3)
        r3_box = box_around(r3[0], buff=0.14, color=PALETTE["gold"])

        zinger = fit(T("This week: hand those 8\nto a local AI model.", color=PALETTE["gold"],
                        font_size=20, line_spacing=1.2), MAX_W)

        VGroup(title, divider, rows, zinger).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(Write(title), run_time=0.3)
        self.play(Create(divider), run_time=0.2)
        self.wait(0.6)
        self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.4)
        self.play(Create(r3_box), run_time=0.3)
        self.wait(1.2)
        self.play(Write(zinger), run_time=0.5)
        # sum of plays = 0.3+0.2+0.4+0.4+0.4+0.3+0.5 = 2.5s
        # waits above = 0.6+0.6+0.8+1.2 = 3.2s; remainder tuned to the
        # measured 14.86s Kokoro length (14.86 - 2.5 - 3.2 = 9.16)
        self.wait(9.16)


# --------------------------------------------------------------------------- #
# B03 — SETUP: already near-single-column; narrower cards.
# measured audio: 30.41s
# --------------------------------------------------------------------------- #
class B03_ResidualHeadlines(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Re-ran the classifier\nagainst all 21 rows:", color=PALETTE["ink"],
                       font_size=20, line_spacing=1.2), MAX_W)
        # buff 0.55 -> 0.68: GATE B's post-render layout audit found this
        # title's real top edge landing outside the +/-3.4 safe-area
        # half-height on the true rendered frame.
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(1.2)

        pill1_txt = T("13 resolved", color=PALETTE["sage"], font_size=15, font=MONO, weight="BOLD")
        pill1 = panel(width=pill1_txt.width + 0.3, height=pill1_txt.height + 0.22,
                       fill=PALETTE["ink"], stroke=PALETTE["sage"], corner_radius=0.2)
        pill1_txt.move_to(pill1.get_center())
        pill2_txt = T("8 residual", color=PALETTE["gold"], font_size=15, font=MONO, weight="BOLD")
        pill2 = panel(width=pill2_txt.width + 0.3, height=pill2_txt.height + 0.22,
                       fill=PALETTE["ink"], stroke=PALETTE["gold"], corner_radius=0.2)
        pill2_txt.move_to(pill2.get_center())
        pills_row = VGroup(VGroup(pill1, pill1_txt), VGroup(pill2, pill2_txt)).arrange(RIGHT, buff=0.25)

        headlines = [
            "“Understanding the\nRegulations of\n24-Hour Trading”",
            "“Know Your Client\n(KYC): Key Requirements\nand Compliance”",
            "“What Are Regulatory\nAssets Under\nManagement (RAUM)?”",
        ]
        sources = ["Investopedia", "Investopedia", "SmartAsset"]

        def make_card(text, source):
            body_txt = fit(T(text, color=PALETTE["bg"], font_size=14, line_spacing=1.2), 3.3)
            src_txt = fit(T(source, color=PALETTE["sage"], font_size=11, font=MONO), 3.3)
            body = VGroup(body_txt, src_txt).arrange(DOWN, buff=0.1)
            bg = panel(width=3.7, height=body.height + 0.3, fill=PALETTE["ink"], stroke=PALETTE["gold"])
            body.move_to(bg.get_center())
            return VGroup(bg, body)

        cards = VGroup(*[make_card(h, s) for h, s in zip(headlines, sources)])
        cards.arrange(DOWN, buff=0.16)

        more_tag = fit(T("+ 5 more, same shape", color=PALETTE["slate"], font_size=15, weight="BOLD"), MAX_W)
        caption = fit(T("No fixed keyword list\nresolves these safely.", color=PALETTE["crimson"],
                         font_size=15, line_spacing=1.2), MAX_W)

        # Every piece built FIRST (above), then the WHOLE rest-of-beat chain
        # (pills through caption) is arranged as one VGroup and height-capped
        # via scale_to_fit_height, guaranteeing it fits below the title
        # regardless of any single card's assumed height — a first draft
        # here positioned cards/more_tag/caption via independent next_to()/
        # to_edge() calls, and GATE B's post-render layout audit found real
        # text-on-text overlap (the caption pinned to the bottom edge while
        # the cards+more_tag, positioned independently, grew past it) plus
        # a real out-of-safe-area box — same proven cap-and-chain pattern as
        # this file's B04 below.
        rest = VGroup(pills_row, cards, more_tag, caption).arrange(DOWN, buff=0.22)
        # cap 5.9 -> 5.5: GATE B's post-render layout audit still found the
        # caption's real bottom edge just outside the +/-3.4 safe-area floor
        # at the 5.9 cap — a tighter cap leaves real clearance.
        if rest.height > 5.5:
            rest.scale_to_fit_height(5.5)
        rest.next_to(title, DOWN, buff=0.3)

        self.play(FadeIn(pills_row, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)

        for c, hold in zip(cards, [3.4, 3.4, 2.6]):
            self.play(Create(c[0]), run_time=0.3)
            self.play(FadeIn(c[1]), run_time=0.3)
            self.wait(hold)

        self.play(FadeIn(more_tag, shift=UP * 0.08), run_time=0.4)
        self.wait(1.8)

        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+3x(0.3+0.3)+0.4+0.4 = 3.5s
        # waits above = 1.2+1.8+3.4+3.4+2.6+1.8 = 14.2s; remainder tuned to
        # the measured 30.41s Kokoro length (30.41 - 3.5 - 14.2 = 12.71)
        self.wait(12.71)


# --------------------------------------------------------------------------- #
# B04 — DISCOVERY/FIX: THE big redesign. Parent's side-by-side YES/NO branch
# cards -> a single vertical chain: Normalize -> gate -> NEW node -> bypass
# node -> merge, each its own full-width stacked card. The conditional gate
# and the untouched-bypass path are still each their own explicit card, not
# narrated alone — same legibility requirement as the parent.
# measured audio: 26.5s
# --------------------------------------------------------------------------- #
class B04_PipelineDiagram(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("A new node — only\nfor the holdouts:", color=PALETTE["ink"],
                       font_size=20, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.68)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        norm_box = panel(width=3.8, height=0.7, fill=PALETTE["ink"], stroke=PALETTE["slate"])
        norm_txt = fit(T("Normalize Data\n(keyword rules)", color=PALETTE["bg"],
                          font_size=13, font=MONO, line_spacing=1.15), 3.5)
        norm_txt.move_to(norm_box.get_center())
        norm_group = VGroup(norm_box, norm_txt)

        gate_box = panel(width=3.8, height=0.9, fill=PALETTE["ink"], stroke=PALETTE["gold"])
        gate_txt = fit(T("ONLY IF source_feed\n== 'Unknown Source'", color=PALETTE["gold"],
                          font_size=13, font=MONO, weight="BOLD", line_spacing=1.2), 3.5)
        gate_txt.move_to(gate_box.get_center())
        gate_group = VGroup(gate_box, gate_txt)

        new_box = panel(width=3.9, height=1.5, fill=PALETTE["ink"], stroke=PALETTE["teal"])
        new_label = fit(T("NEW: Layer 2 - LLM\nSource Classification", color=PALETTE["teal"],
                           font_size=13, font=MONO, weight="BOLD", line_spacing=1.2), 3.6)
        new_sub = fit(T("(Ollama, local) — picks 1 of\n4 categories, or none",
                         color=PALETTE["bg"], font_size=11, font=MONO, line_spacing=1.2), 3.6)
        new_failopen = fit(T("invalid/failed -> keeps\noriginal label", color=PALETTE["crimson"],
                              font_size=11, font=MONO, line_spacing=1.2), 3.6)
        new_content = VGroup(new_label, new_sub, new_failopen).arrange(DOWN, buff=0.1)
        new_content.move_to(new_box.get_center())
        new_group = VGroup(new_box, new_content)

        bypass_box = panel(width=3.8, height=0.85, fill=PALETTE["ink"], stroke=PALETTE["sage"])
        bypass_label = fit(T("every other item", color=PALETTE["sage"], font_size=14, font=MONO, weight="BOLD"), 3.5)
        bypass_sub = fit(T("never touched", color=PALETTE["bg"], font_size=12), 3.5)
        bypass_content = VGroup(bypass_label, bypass_sub).arrange(DOWN, buff=0.1)
        bypass_content.move_to(bypass_box.get_center())
        bypass_group = VGroup(bypass_box, bypass_content)

        merge_box = panel(width=3.8, height=0.7, fill=PALETTE["ink"], stroke=PALETTE["slate"])
        merge_txt = fit(T("Filter Valid\nContent", color=PALETTE["bg"], font_size=14, font=MONO, line_spacing=1.15), 3.5)
        merge_txt.move_to(merge_box.get_center())
        merge_group = VGroup(merge_box, merge_txt)

        yes_tag = T("YES", color=PALETTE["teal"], font_size=13, font=MONO, weight="BOLD")
        no_tag = T("NO", color=PALETTE["sage"], font_size=13, font=MONO, weight="BOLD")

        # Every box built as a (panel, text) unit FIRST, then the whole
        # chain arranged as one VGroup and height-capped — same proven
        # pattern as ../scenes.py's B04 (a first draft here with manual
        # y-coordinates risked exactly the kind of safe-area overflow that
        # bit the landscape parent twice before it adopted this pattern).
        chain = VGroup(norm_group, gate_group, new_group, bypass_group, merge_group)
        chain.arrange(DOWN, buff=0.28)
        # cap 5.6 -> 4.9: GATE B's post-render layout audit found the real
        # closing caption (positioned independently via to_edge(DOWN))
        # overlapping this chain's own merge_box text by 67% — the chain at
        # the larger cap left no real room below it. A tighter cap
        # guarantees clearance regardless of the caption's own height.
        if chain.height > 4.9:
            chain.scale_to_fit_height(4.9)
        chain.next_to(title, DOWN, buff=0.3)

        yes_tag.next_to(gate_box, DOWN, buff=0.03).shift(LEFT * 1.3)
        no_tag.next_to(gate_box, DOWN, buff=0.03).shift(RIGHT * 1.3)

        arrow1 = Arrow(norm_box.get_bottom(), gate_box.get_top(), buff=0.05,
                       color=PALETTE["slate"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        arrow2 = Arrow(gate_box.get_bottom(), new_box.get_top(), buff=0.05,
                       color=PALETTE["teal"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        arrow3 = Arrow(new_box.get_bottom(), bypass_box.get_top(), buff=0.05,
                       color=PALETTE["sage"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
        arrow4 = Arrow(bypass_box.get_bottom(), merge_box.get_top(), buff=0.05,
                       color=PALETTE["slate"], stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        self.play(Create(norm_box), FadeIn(norm_txt), run_time=0.4)
        self.wait(0.8)
        self.play(Create(arrow1), run_time=0.2)
        self.play(Create(gate_box), FadeIn(gate_txt), run_time=0.4)
        self.wait(1.6)
        self.play(Create(arrow2), FadeIn(yes_tag), run_time=0.3)
        self.play(Create(new_box), FadeIn(new_content), run_time=0.5)
        self.wait(2.2)
        self.play(Create(arrow3), FadeIn(no_tag), run_time=0.3)
        self.play(Create(bypass_box), FadeIn(bypass_content), run_time=0.4)
        self.wait(2.2)
        self.play(Create(arrow4), run_time=0.3)
        self.play(Create(merge_box), FadeIn(merge_txt), run_time=0.4)
        self.wait(2.0)

        caption = fit(T("Nothing gets silently\nmislabeled.", color=PALETTE["slate"],
                         font_size=16, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.2+0.4+0.3+0.5+0.3+0.4+0.3+0.4+0.4 = 4.1s
        # waits above = 0.8+1.6+2.2+2.2+2.0 = 8.8s; remainder tuned to
        # the measured 26.5s Kokoro length (26.5 - 4.1 - 8.8 = 13.6)
        self.wait(13.6)


# --------------------------------------------------------------------------- #
# B05 — PROOF: parent's 4-tile horizontal row -> 2x2 grid.
# measured audio: 27.12s
# --------------------------------------------------------------------------- #
class B05_ProofNumbers(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        title = fit(T("Tested against the real 8\n— not a simulation:", color=PALETTE["ink"],
                       font_size=19, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(0.8)

        def tile(number, label, color):
            num_txt = T(number, color=color, font_size=32, font=MONO, weight="BOLD")
            lab_txt = fit(T(label, color=PALETTE["ink"], font_size=13), 1.55)
            content = VGroup(num_txt, lab_txt).arrange(DOWN, buff=0.12)
            bg = panel(width=1.7, height=content.height + 0.35, fill=PALETTE["ink"], stroke=color)
            content.move_to(bg.get_center())
            return VGroup(bg, content)

        t1 = tile("0", "mutated", PALETTE["sage"])
        t2 = tile("1", "resolved", PALETTE["gold"])
        t3 = tile("7", "declined", PALETTE["teal"])
        t4 = tile("0", "errors", PALETTE["sage"])
        top_row = VGroup(t1, t2).arrange(RIGHT, buff=0.25)
        bot_row = VGroup(t3, t4).arrange(RIGHT, buff=0.25)
        tiles = VGroup(top_row, bot_row).arrange(DOWN, buff=0.25)
        tiles.next_to(title, DOWN, buff=0.4)

        self.play(Create(t1[0]), FadeIn(t1[1]), run_time=0.3)
        self.wait(1.0)
        self.play(Create(t2[0]), FadeIn(t2[1]), run_time=0.3)
        self.wait(1.0)
        self.play(Create(t3[0]), FadeIn(t3[1]), run_time=0.3)
        self.wait(1.0)
        self.play(Create(t4[0]), FadeIn(t4[1]), run_time=0.3)
        self.wait(1.8)

        resolved_title = fit(T("The 1 resolved:", color=PALETTE["slate"], font_size=16, weight="BOLD"), MAX_W)
        headline = fit(T(
            "“Recent Enforcement Actions\nDefine the ‘Person’ that\nParticipates in a Partial\nTender” — JD Supra",
            color=PALETTE["ink"], font_size=14, line_spacing=1.25,
        ), 3.3)
        arrow_txt = T("→", color=PALETTE["slate"], font_size=18)
        new_label = fit(T("FINRA Enforcement\nNews", color=PALETTE["gold"], font_size=16,
                           font=MONO, weight="BOLD", line_spacing=1.15), 3.3)
        label_row = VGroup(arrow_txt, new_label).arrange(RIGHT, buff=0.2)

        headline_block = VGroup(resolved_title, headline, label_row).arrange(DOWN, buff=0.16)
        hl_panel = panel(width=3.8, height=headline_block.height + 0.4, fill=PALETTE["ink"], stroke=PALETTE["gold"])
        headline_block.move_to(hl_panel.get_center())
        headline_group = VGroup(hl_panel, headline_block)
        headline_group.next_to(tiles, DOWN, buff=0.3)

        self.play(Create(hl_panel), run_time=0.3)
        self.play(FadeIn(headline_block, shift=UP * 0.1), run_time=0.5)
        self.wait(3.0)

        caption = fit(T("Killed the Ollama connection\ntoo — nothing broke.",
                         color=PALETTE["slate"], font_size=15, line_spacing=1.2), MAX_W)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.3*4+0.3+0.5+0.4 = 2.9s
        # waits above = 0.8+1.0+1.0+1.0+1.8+3.0 = 8.6s; remainder tuned to
        # the measured 27.12s Kokoro length (27.12 - 2.9 - 8.6 = 15.62)
        self.wait(15.62)


# --------------------------------------------------------------------------- #
# B06 — HONEST-LIMITS: parent's 2-column declined list -> single column.
# measured audio: 24.34s
# --------------------------------------------------------------------------- #
class B06_HonestLimits(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["ink"]

        title = fit(T("1 of 8 is not\na big number.", color=PALETTE["bg"],
                       font_size=22, line_spacing=1.2), MAX_W)
        title.to_edge(UP, buff=0.65)
        self.play(Write(title), run_time=0.5)
        self.wait(1.0)

        statement = fit(T("And that's the\ncorrect number.", color=PALETTE["gold"],
                           font_size=24, weight="BOLD", line_spacing=1.2), MAX_W)
        statement.next_to(title, DOWN, buff=0.3)
        stmt_box = box_around(statement, buff=0.18, color=PALETTE["gold"])
        self.play(FadeIn(statement, shift=UP * 0.1), run_time=0.4)
        self.play(Create(stmt_box), run_time=0.3)
        self.wait(1.2)

        # Each declined headline condensed to ONE short line (not the
        # parent's full wrapped titles): GATE B's post-render layout audit
        # found the original 7-entry, 2-line-each list (14 text lines) real
        # bottom edge overlapping the closing line by 44% — genuinely too
        # tall for this narrow frame's safe height alongside the title,
        # statement and closing above/below it.
        declined = [
            "24-Hour Trading explainer",
            "Regulators & text messages",
            "Ropes & Gray update, Jan–Feb",
            "Regulatory AUM (RAUM)?",
            "Capital Markets Insights",
            "Know Your Client (KYC)",
            "Operational integration",
        ]
        dimmed_label = fit(T("declined — 7 of 8:", color=PALETTE["sage"], font_size=16, font=MONO), MAX_W)
        dimmed_lines = VGroup(*[
            fit(T(l, color=PALETTE["bg"], font_size=15), 3.4) for l in declined
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        dimmed_lines.set_opacity(0.45)
        dimmed_block = VGroup(dimmed_label, dimmed_lines).arrange(DOWN, buff=0.28)

        closing = fit(T(
            "A model that forced a label onto\nall 8 would have looked more\nimpressive and been more wrong.",
            color=PALETTE["bg"], font_size=16, line_spacing=1.3,
        ), MAX_W)

        # dimmed_block + closing capped as ONE group below stmt_box — same
        # proven cap-and-chain pattern as this file's B03/B04 (independent
        # next_to()/to_edge() positioning is exactly what let the two
        # overlap in the first place). Line/font spacing (not a blanket
        # scale_to_fit_height) bumped to close a real 51% canvas-fill
        # underfill GATE V's real final-cut frame extraction found at this
        # cap — a uniform group-wide scale-up would also have widened the
        # declined-list lines toward the unsafe x-edge, so height-only
        # spacing increases are used here instead.
        rest = VGroup(dimmed_block, closing).arrange(DOWN, buff=0.5)
        # cap 5.4 -> 5.0: GATE B's post-render layout audit found the real
        # closing line's bottom edge just outside the +/-3.4 safe-area
        # floor at the 5.4 cap.
        if rest.height > 5.0:
            rest.scale_to_fit_height(5.0)
        rest.next_to(stmt_box, DOWN, buff=0.3)

        dimmed_panel = panel(width=dimmed_block.width + 0.4, height=dimmed_block.height + 0.3,
                              fill=PALETTE["ink"], stroke=PALETTE["sage"], opacity=0.0)
        dimmed_panel.move_to(dimmed_block.get_center())
        self.play(Create(dimmed_panel), run_time=0.3)
        self.play(FadeIn(dimmed_block, shift=UP * 0.1), run_time=0.5)
        self.wait(1.5)

        self.play(FadeIn(closing, shift=UP * 0.1), run_time=0.4)
        # sum of plays = 0.5+0.4+0.3+0.3+0.5+0.4 = 2.4s
        # waits above = 1.0+1.2+1.5 = 3.7s; remainder tuned to the measured
        # 24.34s Kokoro length (24.34 - 2.4 - 3.7 = 18.24)
        self.wait(18.24)


# --------------------------------------------------------------------------- #
# B07 — TAKEAWAY: unchanged composition; narrower, re-wrapped.
# measured audio: 13.3s
# --------------------------------------------------------------------------- #
class B07_Statement(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        lines = [
            "When you add an AI model",
            "to a pipeline, the win isn't",
            "always a bigger number.",
        ]
        line2 = [
            "Sometimes the win is a",
            "system that knows the",
            "difference between",
            "“I can classify this” and",
            "“I shouldn't guess” — and",
            "does the second one",
            "on purpose.",
        ]
        top = VGroup(*[
            fit(T(l, color=PALETTE["ink"], font_size=20), MAX_W) for l in lines
        ]).arrange(DOWN, buff=0.16)
        bottom = VGroup(*[
            fit(T(l, color=PALETTE["gold"], font_size=20, weight="BOLD"), MAX_W) for l in line2
        ]).arrange(DOWN, buff=0.16)

        content = VGroup(top, bottom).arrange(DOWN, buff=0.45).move_to(ORIGIN)
        frame_w = max(content.width + 0.8, 3.9)
        frame_h = max(content.height + 0.7, 6.8)
        frame = panel(width=frame_w, height=frame_h,
                      fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        divider = Line(LEFT * 1.3, RIGHT * 1.3, color=PALETTE["gold"], stroke_width=2.5)
        divider.move_to(np.array(top.get_bottom()) / 2 + np.array(bottom.get_top()) / 2)

        self.play(Create(frame), run_time=0.3)
        self.play(FadeIn(top, shift=UP * 0.1), run_time=0.6)
        self.wait(1.6)
        self.play(Create(divider), run_time=0.2)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.6)
        # sum of plays = 0.3+0.6+0.2+0.6 = 1.7s; waits above = 1.6s; remainder
        # tuned to the measured 13.3s Kokoro length (13.3 - 1.7 - 1.6 = 10.0)
        self.wait(10.0)


# --------------------------------------------------------------------------- #
# B08 — SIGN-OFF: unchanged composition; widths trimmed.
# measured audio: 1.51s
# --------------------------------------------------------------------------- #
class B08_BrandOutro(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]

        # fit cap 3.6 (MAX_W) -> 3.3 for the handle: at the full MAX_W this
        # single wide word already uses nearly the entire safe width on its
        # own, leaving no room for ANY frame padding around it — GATE V's
        # real final-cut frame extraction found the frame (built at
        # content.width + 1.0) crossing the safe left/right edge outright.
        handle = fit(T("@HumanitariansAI", color=PALETTE["slate"], font_size=38), 3.3)
        accent = Line(LEFT * 1.6, RIGHT * 1.6, color=PALETTE["gold"], stroke_width=3)
        fixed_line = fit(T("explained with Claude Code", color=PALETTE["ink"], font_size=22), 3.3)
        tagline = fit(T("in for Sai Pranavi J.", color=PALETTE["ink"],
                         font_size=20, line_spacing=1.25), 3.3)
        content = VGroup(handle, accent, fixed_line, tagline).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        # Modest fixed padding (0.3), not content.width + 1.0 (which, at
        # this card's naturally wide handle text, previously pushed the
        # frame itself past the safe x-edge — a real edge-bleed BLOCKER).
        # Height still uses a generous fixed floor since this card's total
        # text is short and GATE V separately measured a real 52% vertical
        # underfill at the old content-derived height.
        frame_w = content.width + 0.3
        frame_h = max(content.height + 1.0, 6.4)
        frame = panel(width=frame_w, height=frame_h,
                       fill=PALETTE["bg"], stroke=PALETTE["gold"], corner_radius=0.2, opacity=0.0)
        frame.move_to(content.get_center())
        frame.set_stroke(width=2.5)

        self.play(Create(frame), FadeIn(content, shift=UP * 0.1), run_time=0.45)
        # sum of plays = 0.45s; remainder tuned to the measured 1.51s Kokoro length
        self.wait(1.06)
