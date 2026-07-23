"""scenes.py — Manim scenes for 'Posting to YouTube'

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B01, B02, B04, B04A, B07, B08, B09, B10, B11, B12 (hero).
Palette: teardown — flat white GROUND, ink INK, red CRIMSON, teal ACCENT_TEAL.
B12_TheSplit is the hero beat — most care; EB Garamond, conductor split.
REV 2: B04A_CaptionsRight added (captions ship with the post).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — THE GAP (16s)
# Finished .mp4 on disk (left), YouTube destination (right),
# gap between them with a red dashed line.
# Caption: "a finished cut on disk is not on YouTube."
# ──────────────────────────────────────────────────────────
class B01_TheGap(Scene):
    def construct(self):
        section = LabelChip("THE GAP", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # LEFT: disk with .mp4 file
        disk_lbl = Text("finished cut", font=MONO, color=INK, font_size=20)
        disk_file = Text("video.mp4", font=MONO, color=INK, font_size=22, weight=BOLD)
        disk_stack = VGroup(disk_lbl, disk_file).arrange(DOWN, buff=0.18)
        disk_box = surround_box(disk_stack, buff=0.32, fill_color=GROUND,
                                stroke_color=SLATE, stroke_width=2)
        disk_grp = VGroup(disk_box, disk_stack).move_to(LEFT * 4.0)
        self.play(FadeIn(disk_grp, scale=0.9), run_time=0.6)

        # RIGHT: YouTube destination
        yt_lbl = Text("YouTube", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        yt_url = Text("youtu.be/…", font=MONO, color=SLATE, font_size=18)
        yt_stack = VGroup(yt_lbl, yt_url).arrange(DOWN, buff=0.18)
        yt_box = surround_box(yt_stack, buff=0.32, fill_color=GROUND,
                              stroke_color=ACCENT_TEAL, stroke_width=2)
        yt_grp = VGroup(yt_box, yt_stack).move_to(RIGHT * 4.0)
        self.play(FadeIn(yt_grp, scale=0.9), run_time=0.6)

        # GAP — red dashed line between them
        gap_line = DashedLine(
            disk_box.get_right() + RIGHT * 0.12,
            yt_box.get_left() + LEFT * 0.12,
            dash_length=0.22, dashed_ratio=0.55,
            stroke_color=CRIMSON, stroke_width=3,
        )
        self.play(Create(gap_line), run_time=0.7)
        self.wait(0.3)

        # Caption
        caption = SerifLabel("a finished cut on disk is not on YouTube.",
                             accent=CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.6)

        # Sub-note: the manual pain
        pain_items = [
            "retype title · paste description",
            "re-enter tags · find playlist",
            "drag into order — every time",
        ]
        pain_grp = VGroup(*[
            Text(t, font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
            for t in pain_items
        ]).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        pain_grp.next_to(gap_line, DOWN, buff=0.45)
        self.play(FadeIn(pain_grp, shift=UP * 0.1), run_time=0.7)
        self.wait(6.8)


# ──────────────────────────────────────────────────────────
# B02 — API NOT STUDIO (16s)
# Two columns.
# LEFT "Studio drag-and-drop": repeated red items.
# RIGHT "the API": fields flowing from beat_sheet.json (teal, one arrow).
# ──────────────────────────────────────────────────────────
class B02_ApiNotStudio(Scene):
    def construct(self):
        section = LabelChip("API NOT STUDIO", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # LEFT: manual repeated items
        left_lbl = SerifLabel("Studio drag-and-drop", accent=CRIMSON, size=20)
        left_lbl.move_to(LEFT * 3.2 + UP * 2.5)
        self.play(FadeIn(left_lbl), run_time=0.4)

        manual_items = [
            "title", "description", "tags",
            "category", "find playlist", "drag into order",
        ]
        manual_grp = VGroup()
        for item in manual_items:
            t = Text(item, font=MONO, color=CRIMSON, font_size=17)
            b = auto_box(t, h_pad=0.16, v_pad=0.1, fill_color="#FFF5F5",
                         stroke_color=CRIMSON, stroke_width=1.5)
            manual_grp.add(VGroup(b, t))
        manual_grp.arrange(DOWN, buff=0.1)
        manual_grp.move_to(LEFT * 3.2 + DOWN * 0.3)
        if manual_grp.width > 5.0:
            manual_grp.scale_to_fit_width(5.0)

        every_time = Text("every time.", font=SERIF, color=CRIMSON,
                          font_size=16, slant=ITALIC)
        every_time.next_to(manual_grp, DOWN, buff=0.2)

        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in manual_grp],
                              lag_ratio=0.12), run_time=0.9)
        self.play(FadeIn(every_time), run_time=0.4)
        self.wait(0.3)

        # RIGHT: the API — fields from beat_sheet.json
        right_lbl = SerifLabel("the API", accent=ACCENT_TEAL, size=20)
        right_lbl.move_to(RIGHT * 3.2 + UP * 2.5)
        self.play(FadeIn(right_lbl), run_time=0.4)

        source_t = Text("beat_sheet.json", font=MONO, color=INK, font_size=17, weight=BOLD)
        source_b = surround_box(source_t, buff=0.22, fill_color=GROUND,
                                stroke_color=ACCENT_TEAL, stroke_width=2)
        source_grp = VGroup(source_b, source_t).move_to(RIGHT * 3.2 + UP * 0.9)

        auto_arrow = Arrow(source_grp.get_bottom(), source_grp.get_bottom() + DOWN * 1.0,
                           stroke_color=ACCENT_TEAL, stroke_width=2.5, tip_length=0.2, buff=0)

        auto_fields = VGroup(*[
            Text(f, font=MONO, color=ACCENT_TEAL, font_size=15)
            for f in ["title · description · tags", "category · playlist · order"]
        ]).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        auto_fields.next_to(auto_arrow, DOWN, buff=0.1)

        once_lbl = Text("once.", font=SERIF, color=ACCENT_TEAL, font_size=16, slant=ITALIC)
        once_lbl.next_to(auto_fields, DOWN, buff=0.18)

        self.play(FadeIn(source_grp, scale=0.9), run_time=0.5)
        self.play(GrowArrow(auto_arrow), FadeIn(auto_fields), run_time=0.6)
        self.play(FadeIn(once_lbl), run_time=0.4)
        self.wait(5.8)


# ──────────────────────────────────────────────────────────
# B04 — WHAT THE PUBLISHER DOES (17s)
# Three-step flow: find/create playlist → upload → add to playlist.
# Ledger chip below.
# ──────────────────────────────────────────────────────────
class B04_WhatPublisherDoes(Scene):
    def construct(self):
        section = LabelChip("THE PUBLISHER", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        steps = [
            ("1. find / create", "'Brutalist' playlist",    ACCENT_TEAL),
            ("2. upload master",  "resumable videos.insert", INK),
            ("3. add to playlist", "at chapter position",    ACCENT_TEAL),
        ]
        step_grps = VGroup()
        for num_s, detail_s, color in steps:
            num = Text(num_s, font=DISPLAY, color=color, font_size=21, weight=BOLD)
            detail = Text(detail_s, font=SERIF, color=INK, font_size=18, slant=ITALIC)
            row = VGroup(num, detail).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            box = surround_box(row, buff=0.26, fill_color=GROUND,
                               stroke_color=color, stroke_width=2)
            step_grps.add(VGroup(box, row))

        step_grps.arrange(DOWN, buff=0.35)
        step_grps.move_to(UP * 0.5)
        if step_grps.width > 8.0:
            step_grps.scale_to_fit_width(8.0)

        # Arrows between steps
        for i in range(len(step_grps) - 1):
            arr = Arrow(step_grps[i].get_bottom(),
                        step_grps[i + 1].get_top(),
                        stroke_color=SLATE, stroke_width=1.5, tip_length=0.16, buff=0.08)
            self.play(FadeIn(step_grps[i], shift=RIGHT * 0.1), GrowArrow(arr), run_time=0.55)
        self.play(FadeIn(step_grps[-1], shift=RIGHT * 0.1), run_time=0.55)
        self.wait(0.4)

        # Ledger chip
        ledger_t = Text("ledger: records each ID → re-runs skip what's already up.",
                        font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        if ledger_t.width > 11.0:
            ledger_t.scale_to_fit_width(11.0)
        ledger_box = auto_box(ledger_t, h_pad=0.25, v_pad=0.16, fill_color=GROUND,
                              stroke_color=SLATE, stroke_width=1.5)
        ledger_grp = VGroup(ledger_box, ledger_t)
        ledger_grp.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(ledger_grp), run_time=0.5)
        self.wait(7.0)


# ──────────────────────────────────────────────────────────
# B04A — CAPTIONS RIGHT (18s)  REV 2
# An .srt cue card with a teal arrow FROM beat_sheet.json
# ('source text · measured timing'). Beside it, faded, an
# 'auto-generated' caption with a misheard phrase crossed
# out in red: voice says 'h nu', auto writes 'h new', source
# has 'E = hν'. Bottom: 'captions.insert — CC track travels
# with the upload.'
# ──────────────────────────────────────────────────────────
class B04A_CaptionsRight(Scene):
    def construct(self):
        section = LabelChip("CAPTIONS", accent=ACCENT_TEAL, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # LEFT — source .srt cue card
        srt_num   = Text("1",                        font=MONO, color=SLATE,      font_size=14)
        srt_tc    = Text("00:00:46,000 --> 00:01:02,000", font=MONO, color=SLATE, font_size=13)
        srt_l1    = Text("E = hν — the energy of a photon.", font=MONO, color=INK, font_size=15, weight=BOLD)
        srt_l2    = Text("(Planck, 1900.)",          font=MONO, color=INK,        font_size=15)
        srt_content = VGroup(srt_num, srt_tc, srt_l1, srt_l2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        srt_box = surround_box(srt_content, buff=0.28, fill_color=GROUND,
                               stroke_color=ACCENT_TEAL, stroke_width=2)
        srt_grp = VGroup(srt_box, srt_content).move_to(LEFT * 3.2 + UP * 0.3)
        if srt_grp.width > 5.5:
            srt_grp.scale_to_fit_width(5.5)

        # Source label + arrow INTO srt card FROM beat_sheet.json chip
        src_t = Text("beat_sheet.json", font=MONO, color=INK, font_size=15, weight=BOLD)
        src_b = auto_box(src_t, h_pad=0.16, v_pad=0.1, fill_color=GROUND,
                         stroke_color=ACCENT_TEAL, stroke_width=1.5)
        src_grp = VGroup(src_b, src_t).next_to(srt_grp, UP, buff=0.45)

        src_arrow = Arrow(src_grp.get_bottom(),
                          srt_grp.get_top(),
                          stroke_color=ACCENT_TEAL, stroke_width=2.5,
                          tip_length=0.18, buff=0.06)
        src_lbl = Text("source text · measured timing",
                       font=SERIF, color=ACCENT_TEAL, font_size=14, slant=ITALIC)
        src_lbl.next_to(src_arrow, RIGHT, buff=0.15)
        if src_lbl.width > 3.2:
            src_lbl.scale_to_fit_width(3.2)

        self.play(FadeIn(src_grp, scale=0.9), run_time=0.5)
        self.play(GrowArrow(src_arrow), FadeIn(src_lbl), run_time=0.5)
        self.play(FadeIn(srt_grp), run_time=0.6)
        self.wait(0.3)

        # RIGHT — auto-generated caption (faded) with misheard phrase
        auto_hdr = Text("auto-generated:", font=SERIF, color=SLATE, font_size=15, slant=ITALIC)
        auto_wrong = Text('"h new — the energy of a photon"',
                          font=MONO, color=SLATE, font_size=15)
        auto_stack = VGroup(auto_hdr, auto_wrong).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        auto_box_obj = auto_box(auto_wrong, h_pad=0.18, v_pad=0.12,
                                fill_color="#F9F9F9", stroke_color=SLATE, stroke_width=1)
        auto_grp = VGroup(auto_box_obj, auto_stack).move_to(RIGHT * 3.0 + UP * 0.9)
        if auto_grp.width > 5.0:
            auto_grp.scale_to_fit_width(5.0)
        auto_grp.set_opacity(0.55)

        # Strikethrough on the misheard text
        strike = Line(auto_wrong.get_left() + LEFT * 0.05,
                      auto_wrong.get_right() + RIGHT * 0.05,
                      stroke_color=CRIMSON, stroke_width=3.5)
        strike.move_to(auto_wrong.get_center())

        # Correction chip
        fix_t = Text("E = hν", font=MONO, color=INK, font_size=16, weight=BOLD)
        fix_b = auto_box(fix_t, h_pad=0.18, v_pad=0.12,
                         fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2)
        fix_grp = VGroup(fix_b, fix_t)
        fix_grp.next_to(auto_grp, DOWN, buff=0.3)
        fix_grp.set_x(auto_grp.get_x())

        fix_lbl = Text("the source text has it right",
                       font=SERIF, color=ACCENT_TEAL, font_size=14, slant=ITALIC)
        fix_lbl.next_to(fix_grp, DOWN, buff=0.15)
        fix_lbl.set_x(fix_grp.get_x())

        self.play(FadeIn(auto_grp, scale=0.9), run_time=0.5)
        self.play(Create(strike), run_time=0.4)
        self.play(FadeIn(fix_grp, scale=1.05), FadeIn(fix_lbl), run_time=0.5)
        self.wait(0.4)

        # Bottom caption
        caption = SerifLabel("captions.insert — the CC track travels with the upload.",
                             accent=ACCENT_TEAL, size=19)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(7.5)


# ──────────────────────────────────────────────────────────
# B07 — THE BUG (18s)
# Error card: "playlistItems.insert → 400 manualSortRequired"
# position= token crossed out (red) → clean insert (teal).
# Real from PUBLISH-LOG.md.
# ──────────────────────────────────────────────────────────
class B07_TheBug(Scene):
    def construct(self):
        section = LabelChip("ONE REAL BUG", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Error card
        err_hdr = Text("playlistItems.insert", font=MONO, color=WHITE, font_size=18, weight=BOLD)
        err_code = Text("→ 400  manualSortRequired", font=MONO, color=CRIMSON, font_size=18)
        err_msg = Text('"Playlist should use manual sorting to support position."',
                       font=SERIF, color=SLATE, font_size=15, slant=ITALIC)
        err_content = VGroup(err_hdr, err_code, err_msg).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        err_box = surround_box(err_content, buff=0.3,
                               fill_color="#111111", stroke_color=CRIMSON, stroke_width=2)
        err_grp = VGroup(err_box, err_content).move_to(UP * 1.3)
        if err_grp.width > 11.0:
            err_grp.scale_to_fit_width(11.0)
        self.play(FadeIn(err_grp), run_time=0.7)
        self.wait(0.4)

        # Cause: position= sent but playlist is auto-sort
        cause_txt = Text("cause: playlist auto-sorts; script sent  position=N",
                         font=MONO, color=INK, font_size=18)
        if cause_txt.width > 11.0:
            cause_txt.scale_to_fit_width(11.0)
        cause_box = auto_box(cause_txt, h_pad=0.22, v_pad=0.16, fill_color=GROUND,
                             stroke_color=SLATE, stroke_width=1.5)
        cause_grp = VGroup(cause_box, cause_txt).next_to(err_grp, DOWN, buff=0.35)
        self.play(FadeIn(cause_grp, shift=UP * 0.1), run_time=0.5)
        self.wait(0.3)

        # Fix: crossed out → clean
        wrong_t = Text('"position": pos,', font=MONO, color=CRIMSON, font_size=18)
        wrong_b = auto_box(wrong_t, h_pad=0.18, v_pad=0.12, fill_color="#FFF5F5",
                           stroke_color=CRIMSON, stroke_width=2)
        wrong_grp = VGroup(wrong_b, wrong_t).move_to(LEFT * 2.8 + DOWN * 1.0)

        strike = Line(wrong_grp.get_left() + LEFT * 0.05,
                      wrong_grp.get_right() + RIGHT * 0.05,
                      stroke_color=CRIMSON, stroke_width=4)
        strike.move_to(wrong_grp)

        arrow_fix = Arrow(wrong_grp.get_right() + RIGHT * 0.1,
                          wrong_grp.get_right() + RIGHT * 1.4,
                          stroke_color=ACCENT_TEAL, stroke_width=2.5, tip_length=0.18, buff=0)

        clean_t = Text("(removed)", font=MONO, color=ACCENT_TEAL, font_size=18)
        clean_b = auto_box(clean_t, h_pad=0.18, v_pad=0.12, fill_color="#F0FAF6",
                           stroke_color=ACCENT_TEAL, stroke_width=2)
        clean_grp = VGroup(clean_b, clean_t)
        clean_grp.next_to(arrow_fix, RIGHT, buff=0.1)

        self.play(FadeIn(wrong_grp), run_time=0.4)
        self.play(Create(strike), run_time=0.4)
        self.play(GrowArrow(arrow_fix), FadeIn(clean_grp), run_time=0.5)
        self.wait(0.4)

        ledger_note = SerifLabel("ledger: re-run skipped the already-uploaded video.",
                                 accent=ACCENT_TEAL, size=19)
        ledger_note.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(ledger_note), run_time=0.5)
        self.wait(7.5)


# ──────────────────────────────────────────────────────────
# B08 — PRIVACY AUDIT (17s)
# Three chips: PRIVATE, UNLISTED (teal ✓), PUBLIC (red, locked).
# Arrow UNLISTED → PUBLIC labelled "a manual flip in Studio — you decide."
# ──────────────────────────────────────────────────────────
class B08_PrivacyAudit(Scene):
    def construct(self):
        section = LabelChip("PRIVACY + AUDIT", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        def make_chip(label, note, color, fill_col=None):
            fill_col = fill_col or GROUND
            lbl_t = Text(label, font=DISPLAY, color=color, font_size=22, weight=BOLD)
            note_t = Text(note, font=SERIF, color=INK, font_size=16, slant=ITALIC)
            stack = VGroup(lbl_t, note_t).arrange(DOWN, buff=0.14)
            box = surround_box(stack, buff=0.3, fill_color=fill_col,
                               stroke_color=color, stroke_width=2.5)
            return VGroup(box, stack)

        chip_p  = make_chip("PRIVATE",  "not posted",          SLATE)
        chip_u  = make_chip("UNLISTED", "✓ no audit needed",   ACCENT_TEAL, fill_col="#F0FAF6")
        chip_pub= make_chip("PUBLIC",   "⚠ needs API audit",   CRIMSON,     fill_col="#FFF5F5")

        chips = VGroup(chip_p, chip_u, chip_pub).arrange(RIGHT, buff=0.5)
        chips.move_to(UP * 0.5)
        if chips.width > 12.0:
            chips.scale_to_fit_width(12.0)

        self.play(FadeIn(chip_p, scale=0.9), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(chip_u, scale=1.05), run_time=0.5)  # teal pops
        self.wait(0.3)
        self.play(FadeIn(chip_pub, scale=0.9), run_time=0.5)
        self.wait(0.4)

        # Arrow UNLISTED → PUBLIC
        flip_arrow = Arrow(
            chip_u.get_bottom() + DOWN * 0.05,
            chip_pub.get_bottom() + DOWN * 0.05,
            stroke_color=INK, stroke_width=2, tip_length=0.18,
            path_arc=-0.8,
        )
        flip_lbl = Text("a manual flip in Studio — you decide.",
                        font=SERIF, color=INK, font_size=18, slant=ITALIC)
        if flip_lbl.width > 8.0:
            flip_lbl.scale_to_fit_width(8.0)
        flip_lbl.next_to(flip_arrow, DOWN, buff=0.25)

        self.play(Create(flip_arrow), FadeIn(flip_lbl, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)

        caption = SerifLabel("the machine posts; you decide what the world sees.",
                             accent=ACCENT_TEAL, size=20)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(7.5)


# ──────────────────────────────────────────────────────────
# B09 — QUOTA (14s)
# Meter: 10,000 units/day, each upload 1,600 → ~6/day.
# Three ticks used (teal), plenty left.
# ──────────────────────────────────────────────────────────
class B09_Quota(Scene):
    def construct(self):
        section = LabelChip("QUOTA", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Quota meter bar
        bar_total_w = 10.0
        bar_h = 0.55
        bar_bg = Rectangle(width=bar_total_w, height=bar_h,
                           fill_color="#E8E8E8", fill_opacity=1, stroke_width=0)
        bar_bg.move_to(UP * 0.8)

        # 3 uploads × 1600 = 4800 units used; 10000 total
        used_frac = (3 * 1600) / 10000  # 0.48
        bar_used = Rectangle(width=bar_total_w * used_frac, height=bar_h,
                             fill_color=ACCENT_TEAL, fill_opacity=1, stroke_width=0)
        bar_used.align_to(bar_bg, LEFT).align_to(bar_bg, DOWN)

        # Tick marks at 1600-unit intervals
        ticks = VGroup()
        for i in range(1, 7):
            frac = (i * 1600) / 10000
            tick = Line(DOWN * 0.08, UP * 0.08,
                        stroke_color=WHITE, stroke_width=2)
            tick.move_to(bar_bg.get_left() + RIGHT * frac * bar_total_w + UP * 0.8)
            ticks.add(tick)

        self.play(FadeIn(bar_bg), run_time=0.3)
        self.play(FadeIn(bar_used, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(ticks), run_time=0.3)
        self.wait(0.2)

        # Labels
        total_lbl = Text("10,000 units / day", font=MONO, color=INK, font_size=20)
        total_lbl.next_to(bar_bg, UP, buff=0.3)
        used_lbl = Text("1,600 per upload", font=MONO, color=ACCENT_TEAL, font_size=18)
        used_lbl.next_to(bar_bg, DOWN, buff=0.25)
        approx_lbl = Text("→ ~6 uploads a day", font=MONO, color=INK,
                          font_size=20, weight=BOLD)
        approx_lbl.next_to(used_lbl, DOWN, buff=0.2)

        self.play(FadeIn(total_lbl), FadeIn(used_lbl), run_time=0.5)
        self.play(FadeIn(approx_lbl), run_time=0.5)
        self.wait(0.3)

        # Three upload ticks used
        used_note = Text("▲ 3 used this run", font=MONO, color=ACCENT_TEAL, font_size=16)
        used_note.next_to(bar_used, DOWN, buff=0.6)
        self.play(FadeIn(used_note, shift=UP * 0.1), run_time=0.4)

        # Ledger note
        ledger_n = SerifLabel("longer runs batch across days; ledger tracks the boundary.",
                              accent=INK, size=18)
        ledger_n.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(ledger_n), run_time=0.5)
        self.wait(5.5)


# ──────────────────────────────────────────────────────────
# B10 — THE FUNNEL (14s)
# SHORTS → intro VIDEO "What is Brutalist?"; LONGS → series PLAYLIST "Brutalist".
# Caption: appended automatically.
# ──────────────────────────────────────────────────────────
class B10_Funnel(Scene):
    def construct(self):
        section = LabelChip("THE FUNNEL", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # TOP: three SHORTS chips
        short_chips = VGroup(*[
            VGroup(
                surround_box(Text(f"Short {i}", font=MONO, color=INK, font_size=16),
                             buff=0.14, fill_color=GROUND, stroke_color=SLATE, stroke_width=1.5),
                Text(f"Short {i}", font=MONO, color=INK, font_size=16),
            )
            for i in range(1, 4)
        ])
        # actually simpler: build them properly
        short_chips = VGroup()
        for label in ["Short A", "Short B", "Short C"]:
            t = Text(label, font=MONO, color=INK, font_size=16)
            b = auto_box(t, h_pad=0.16, v_pad=0.12, fill_color=GROUND,
                         stroke_color=SLATE, stroke_width=1.5)
            short_chips.add(VGroup(b, t))
        short_chips.arrange(RIGHT, buff=0.4).move_to(UP * 2.4 + LEFT * 1.8)

        long_chips = VGroup()
        for label in ["Long A", "Long B", "Long C"]:
            t = Text(label, font=MONO, color=INK, font_size=16)
            b = auto_box(t, h_pad=0.16, v_pad=0.12, fill_color=GROUND,
                         stroke_color=SLATE, stroke_width=1.5)
            long_chips.add(VGroup(b, t))
        long_chips.arrange(RIGHT, buff=0.4).move_to(UP * 2.4 + RIGHT * 3.8)

        self.play(FadeIn(short_chips), FadeIn(long_chips), run_time=0.6)

        # Destination: intro VIDEO (left) and series PLAYLIST (right)
        intro_t = Text("What is Brutalist?", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        intro_sub = Text("intro VIDEO", font=SERIF, color=SLATE, font_size=15, slant=ITALIC)
        intro_stack = VGroup(intro_t, intro_sub).arrange(DOWN, buff=0.1)
        intro_box = surround_box(intro_stack, buff=0.26, fill_color=GROUND,
                                 stroke_color=ACCENT_TEAL, stroke_width=2)
        intro_grp = VGroup(intro_box, intro_stack).move_to(DOWN * 0.5 + LEFT * 1.8)
        if intro_grp.width > 4.5:
            intro_grp.scale_to_fit_width(4.5)

        playlist_t = Text('"Brutalist"', font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        playlist_sub = Text("series PLAYLIST", font=SERIF, color=SLATE, font_size=15, slant=ITALIC)
        playlist_stack = VGroup(playlist_t, playlist_sub).arrange(DOWN, buff=0.1)
        playlist_box = surround_box(playlist_stack, buff=0.26, fill_color=GROUND,
                                    stroke_color=ACCENT_TEAL, stroke_width=2)
        playlist_grp = VGroup(playlist_box, playlist_stack).move_to(DOWN * 0.5 + RIGHT * 3.8)
        if playlist_grp.width > 4.5:
            playlist_grp.scale_to_fit_width(4.5)

        # Funnel arrows
        short_arrows = VGroup(*[
            Arrow(chip.get_bottom(), intro_grp.get_top() + UP * 0.05,
                  stroke_color=ACCENT_TEAL, stroke_width=1.5, tip_length=0.14, buff=0.06)
            for chip in short_chips
        ])
        long_arrows = VGroup(*[
            Arrow(chip.get_bottom(), playlist_grp.get_top() + UP * 0.05,
                  stroke_color=ACCENT_TEAL, stroke_width=1.5, tip_length=0.14, buff=0.06)
            for chip in long_chips
        ])

        self.play(FadeIn(intro_grp, scale=0.9), FadeIn(playlist_grp, scale=0.9), run_time=0.5)
        self.play(FadeIn(short_arrows), FadeIn(long_arrows), run_time=0.6)
        self.wait(0.4)

        caption = SerifLabel("appended to every description automatically.",
                             accent=ACCENT_TEAL, size=19)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(6.2)


# ──────────────────────────────────────────────────────────
# B11 — THE THREE, LIVE (15s)
# Three stacked cards: ch1, ch2, ch3, all "unlisted",
# inside a "Brutalist" playlist frame.
# ──────────────────────────────────────────────────────────
class B11_TheThree(Scene):
    def construct(self):
        section = LabelChip("THE THREE, LIVE", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Playlist container frame
        pl_label = LabelChip("Brutalist playlist", accent=ACCENT_TEAL, size=18)
        pl_label.to_edge(UP, buff=0.55)
        self.play(FadeIn(pl_label), run_time=0.4)

        # Three video cards
        videos = [
            ("ch1", "What is Brutalist?",          "review cut · on purpose", "xXKgCXc1nm4"),
            ("ch2", "Installs, .env & Credentials", None,                      "7rUcwkFOhvM"),
            ("ch3", "When Cowork Can Help Claude Code", None,                  "AhdmP75PBY0"),
        ]
        cards = VGroup()
        for ch, title, note, vid_id in videos:
            ch_t = Text(ch, font=DISPLAY, color=ACCENT_TEAL, font_size=16, weight=BOLD)
            title_t = Text(title, font=DISPLAY, color=INK, font_size=18, weight=BOLD)
            id_t = Text(f"youtu.be/{vid_id}", font=MONO, color=SLATE, font_size=14)
            unlisted_t = Text("unlisted", font=MONO, color=ACCENT_TEAL, font_size=14)
            row_top = VGroup(ch_t, title_t).arrange(RIGHT, buff=0.3)
            row_bot_items = [id_t, unlisted_t]
            if note:
                note_t = Text(note, font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
                row_bot_items.append(note_t)
            row_bot = VGroup(*row_bot_items).arrange(RIGHT, buff=0.35)
            card_content = VGroup(row_top, row_bot).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            card_box = surround_box(card_content, buff=0.22, fill_color=GROUND,
                                    stroke_color=ACCENT_TEAL, stroke_width=2)
            card = VGroup(card_box, card_content)
            if card.width > 11.5:
                card.scale_to_fit_width(11.5)
            cards.add(card)

        cards.arrange(DOWN, buff=0.28)
        cards.move_to(DOWN * 0.2)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.1), run_time=0.5)
            self.wait(0.15)
        self.wait(7.5)


# ──────────────────────────────────────────────────────────
# B12 — THE SPLIT — HERO BEAT (20s)
# Center title in EB Garamond on dark background.
# LEFT (teal): machine's mechanical publish.
# RIGHT: human hand on PUBLIC switch, still off.
# Caption: "it plays every part; you own what ships."
# Conductor split — one more time.
# ──────────────────────────────────────────────────────────
class B12_TheSplit(Scene):
    def construct(self):
        # Dark canvas — hero
        self.camera.background_color = "#2A1A0E"

        # Central title — EB Garamond
        title = Text("THE MACHINE POSTS.", font=SERIF, color=WHITE,
                     font_size=42, weight=BOLD)
        title.move_to(UP * 2.5)
        self.play(Write(title), run_time=0.9)

        subtitle = Text("YOU OWN WHAT SHIPS.", font=SERIF, color=ACCENT_TEAL,
                        font_size=38, weight=BOLD)
        subtitle.next_to(title, DOWN, buff=0.22)
        underline = Line(subtitle.get_corner(DL) + DOWN * 0.08,
                         subtitle.get_corner(DR) + DOWN * 0.08,
                         stroke_color=ACCENT_TEAL, stroke_width=3)
        self.play(FadeIn(subtitle, shift=DOWN * 0.1), Create(underline), run_time=0.7)
        self.wait(0.4)

        # Vertical divider
        divider = Line(UP * 1.5, DOWN * 2.0,
                       stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.3)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # LEFT — machine's part (teal)
        machine_items = [
            "description", "chapters", "tags",
            "playlist order", "ledger",
        ]
        machine_lbl = SerifLabel("the machine", accent=ACCENT_TEAL, size=22)
        machine_lbl.move_to(LEFT * 3.2 + UP * 1.2)
        machine_grp = VGroup(*[
            Text(item, font=MONO, color=ACCENT_TEAL, font_size=18)
            for item in machine_items
        ]).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        machine_grp.move_to(LEFT * 3.2 + DOWN * 0.4)
        self.play(FadeIn(machine_lbl), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in machine_grp],
                              lag_ratio=0.15), run_time=0.8)
        self.wait(0.3)

        # RIGHT — human switch (still off, waiting)
        human_lbl = SerifLabel("you", accent=WHITE, size=22)
        human_lbl.move_to(RIGHT * 3.2 + UP * 1.2)

        switch_bg = Rectangle(width=1.8, height=0.75,
                              fill_color="#333333", fill_opacity=1,
                              stroke_color=WHITE, stroke_width=2, stroke_opacity=0.5)
        switch_dot = Circle(radius=0.28, fill_color=SLATE, fill_opacity=1, stroke_width=0)
        switch_dot.move_to(switch_bg.get_left() + RIGHT * 0.4)
        switch_grp = VGroup(switch_bg, switch_dot).move_to(RIGHT * 3.2 + DOWN * 0.1)

        public_lbl = Text("PUBLIC", font=DISPLAY, color=SLATE, font_size=18, weight=BOLD)
        public_lbl.next_to(switch_grp, UP, buff=0.2)
        public_lbl.set_opacity(0.5)

        waiting_lbl = Text("unlisted · waiting", font=SERIF, color=SLATE,
                           font_size=16, slant=ITALIC)
        waiting_lbl.next_to(switch_grp, DOWN, buff=0.22)

        self.play(FadeIn(human_lbl), run_time=0.4)
        self.play(FadeIn(switch_grp), FadeIn(public_lbl), FadeIn(waiting_lbl), run_time=0.6)
        self.wait(0.5)

        # Conductor baton coda (echoes videos 1–3)
        baton = Line(LEFT * 3.8, RIGHT * 3.8,
                     stroke_color=WHITE, stroke_width=4, stroke_opacity=0.4)
        baton.to_edge(DOWN, buff=1.0)
        coda = Text("it plays every part — you own what ships.",
                    font=SERIF, color=ACCENT_TEAL, font_size=20)
        if coda.width > 13.0:
            coda.scale_to_fit_width(13.0)
        coda.to_edge(DOWN, buff=0.4)
        self.play(Create(baton), FadeIn(coda, shift=UP * 0.1), run_time=0.8)
        self.wait(9.5)
