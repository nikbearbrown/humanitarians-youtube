"""scenes.py — PORTRAIT (9:16) layouts for 'Posting to YouTube' short.

Kept GENERATED beats: B01, B02, B09, B10, B11, B12.
Dropped:             B03, B04, B04A, B07, B08.

Frame: 1080×1920 → Manim units ~4.5 wide × 8.0 tall (x: ±2.25, y: ±4.0).
Strategy: vertical stacks replace left/right splits; font sizes ~0.72× landscape.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — THE GAP (portrait, 18s)
# mp4 box → dashed gap → YouTube box (vertical).
# Manual pain items below.
# ──────────────────────────────────────────────────────────
class B01_TheGap(Scene):
    def construct(self):
        section = LabelChip("THE GAP", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # TOP: finished cut
        disk_lbl = Text("finished cut", font=MONO, color=INK, font_size=18)
        disk_file = Text("video.mp4", font=MONO, color=INK, font_size=20, weight=BOLD)
        disk_stack = VGroup(disk_lbl, disk_file).arrange(DOWN, buff=0.16)
        disk_box = surround_box(disk_stack, buff=0.28, fill_color=GROUND,
                                stroke_color=SLATE, stroke_width=2)
        disk_grp = VGroup(disk_box, disk_stack).move_to(UP * 2.4)
        if disk_grp.width > 3.8:
            disk_grp.scale_to_fit_width(3.8)
        self.play(FadeIn(disk_grp, scale=0.9), run_time=0.55)

        # Dashed vertical gap
        gap_line = DashedLine(
            disk_grp.get_bottom() + DOWN * 0.12,
            disk_grp.get_bottom() + DOWN * 1.0,
            dash_length=0.18, dashed_ratio=0.55,
            stroke_color=CRIMSON, stroke_width=3,
        )
        self.play(Create(gap_line), run_time=0.65)

        # BOTTOM of gap: YouTube
        yt_lbl = Text("YouTube", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        yt_url = Text("youtu.be/…", font=MONO, color=SLATE, font_size=16)
        yt_stack = VGroup(yt_lbl, yt_url).arrange(DOWN, buff=0.16)
        yt_box = surround_box(yt_stack, buff=0.28, fill_color=GROUND,
                              stroke_color=ACCENT_TEAL, stroke_width=2)
        yt_grp = VGroup(yt_box, yt_stack)
        yt_grp.next_to(gap_line, DOWN, buff=0.12)
        if yt_grp.width > 3.8:
            yt_grp.scale_to_fit_width(3.8)
        self.play(FadeIn(yt_grp, scale=0.9), run_time=0.55)
        self.wait(0.25)

        caption = SerifLabel("a finished cut on disk is not on YouTube.", accent=CRIMSON, size=20)
        caption.to_edge(DOWN, buff=1.4)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)
        self.play(FadeIn(caption), run_time=0.55)

        pain_items = [
            "retype title · paste description",
            "re-enter tags · find playlist",
            "drag into order — every time",
        ]
        pain_grp = VGroup(*[
            Text(t, font=SERIF, color=CRIMSON, font_size=16, slant=ITALIC)
            for t in pain_items
        ]).arrange(DOWN, buff=0.14)
        pain_grp.to_edge(DOWN, buff=0.45)
        if pain_grp.width > 3.8:
            pain_grp.scale_to_fit_width(3.8)
        self.play(FadeIn(pain_grp, shift=UP * 0.1), run_time=0.65)
        self.wait(8.5)


# ──────────────────────────────────────────────────────────
# B02 — API NOT STUDIO (portrait, 19s)
# Top: Studio drag-and-drop items. Bottom: API one-shot.
# ──────────────────────────────────────────────────────────
class B02_ApiNotStudio(Scene):
    def construct(self):
        section = LabelChip("API NOT STUDIO", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # TOP: manual Studio items
        left_lbl = SerifLabel("Studio drag-and-drop", accent=CRIMSON, size=18)
        left_lbl.move_to(UP * 3.0)
        if left_lbl.width > 3.8:
            left_lbl.scale_to_fit_width(3.8)
        self.play(FadeIn(left_lbl), run_time=0.35)

        manual_items = ["title", "description", "tags", "category", "find playlist"]
        manual_grp = VGroup()
        for item in manual_items:
            t = Text(item, font=MONO, color=CRIMSON, font_size=16)
            b = auto_box(t, h_pad=0.14, v_pad=0.09, fill_color="#FFF5F5",
                         stroke_color=CRIMSON, stroke_width=1.5)
            manual_grp.add(VGroup(b, t))
        manual_grp.arrange(DOWN, buff=0.09).move_to(UP * 1.8)
        if manual_grp.width > 3.8:
            manual_grp.scale_to_fit_width(3.8)
        every_time = Text("every time.", font=SERIF, color=CRIMSON, font_size=15, slant=ITALIC)
        every_time.next_to(manual_grp, DOWN, buff=0.16)

        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in manual_grp],
                              lag_ratio=0.10), run_time=0.8)
        self.play(FadeIn(every_time), run_time=0.35)
        self.wait(0.25)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(UP * 0.3)
        self.play(Create(divider), run_time=0.28)

        # BOTTOM: API
        right_lbl = SerifLabel("the API", accent=ACCENT_TEAL, size=18)
        right_lbl.move_to(UP * 0.0)
        self.play(FadeIn(right_lbl), run_time=0.35)

        source_t = Text("beat_sheet.json", font=MONO, color=INK, font_size=16, weight=BOLD)
        source_b = surround_box(source_t, buff=0.20, fill_color=GROUND,
                                stroke_color=ACCENT_TEAL, stroke_width=2)
        source_grp = VGroup(source_b, source_t).move_to(DOWN * 0.6)

        auto_arrow = Arrow(source_grp.get_bottom(), source_grp.get_bottom() + DOWN * 0.65,
                           stroke_color=ACCENT_TEAL, stroke_width=2.5, tip_length=0.18, buff=0)

        auto_fields = VGroup(*[
            Text(f, font=MONO, color=ACCENT_TEAL, font_size=14)
            for f in ["title · description · tags", "category · playlist · order"]
        ]).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
        auto_fields.next_to(auto_arrow, DOWN, buff=0.10)
        if auto_fields.width > 3.8:
            auto_fields.scale_to_fit_width(3.8)

        once_lbl = Text("once.", font=SERIF, color=ACCENT_TEAL, font_size=15, slant=ITALIC)
        once_lbl.next_to(auto_fields, DOWN, buff=0.15)

        self.play(FadeIn(source_grp, scale=0.9), run_time=0.45)
        self.play(GrowArrow(auto_arrow), FadeIn(auto_fields), run_time=0.55)
        self.play(FadeIn(once_lbl), run_time=0.35)
        self.wait(8.0)


# ──────────────────────────────────────────────────────────
# B09 — QUOTA (portrait, 15s)
# Narrow quota bar + labels stacked vertically.
# ──────────────────────────────────────────────────────────
class B09_Quota(Scene):
    def construct(self):
        section = LabelChip("QUOTA", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # Quota bar — narrower for portrait
        bar_total_w = 3.6
        bar_h = 0.48
        bar_bg = Rectangle(width=bar_total_w, height=bar_h,
                           fill_color="#E8E8E8", fill_opacity=1, stroke_width=0)
        bar_bg.move_to(UP * 1.5)

        used_frac = (3 * 1600) / 10000
        bar_used = Rectangle(width=bar_total_w * used_frac, height=bar_h,
                             fill_color=ACCENT_TEAL, fill_opacity=1, stroke_width=0)
        bar_used.align_to(bar_bg, LEFT).align_to(bar_bg, DOWN)

        ticks = VGroup()
        for i in range(1, 7):
            frac = (i * 1600) / 10000
            tick = Line(DOWN * 0.07, UP * 0.07, stroke_color=WHITE, stroke_width=2)
            tick.move_to(bar_bg.get_left() + RIGHT * frac * bar_total_w + UP * 1.5)
            ticks.add(tick)

        self.play(FadeIn(bar_bg), run_time=0.28)
        self.play(FadeIn(bar_used, shift=RIGHT * 0.25), run_time=0.55)
        self.play(FadeIn(ticks), run_time=0.28)
        self.wait(0.18)

        total_lbl = Text("10,000 units / day", font=MONO, color=INK, font_size=18)
        total_lbl.next_to(bar_bg, UP, buff=0.28)
        used_lbl = Text("1,600 per upload", font=MONO, color=ACCENT_TEAL, font_size=16)
        used_lbl.next_to(bar_bg, DOWN, buff=0.22)
        approx_lbl = Text("→ ~6 uploads a day", font=MONO, color=INK,
                          font_size=18, weight=BOLD)
        approx_lbl.next_to(used_lbl, DOWN, buff=0.18)
        if approx_lbl.width > 3.8:
            approx_lbl.scale_to_fit_width(3.8)

        self.play(FadeIn(total_lbl), FadeIn(used_lbl), run_time=0.45)
        self.play(FadeIn(approx_lbl), run_time=0.45)
        self.wait(0.25)

        used_note = Text("▲ 3 used this run", font=MONO, color=ACCENT_TEAL, font_size=15)
        used_note.next_to(approx_lbl, DOWN, buff=0.30)
        self.play(FadeIn(used_note, shift=UP * 0.1), run_time=0.35)

        ledger_n = SerifLabel("ledger tracks the boundary across days.", accent=INK, size=17)
        ledger_n.to_edge(DOWN, buff=0.50)
        if ledger_n.width > 3.8:
            ledger_n.scale_to_fit_width(3.8)
        self.play(FadeIn(ledger_n), run_time=0.45)
        self.wait(7.0)


# ──────────────────────────────────────────────────────────
# B10 — THE FUNNEL (portrait, 13s)
# Shorts column → intro video. Longs column → series playlist.
# Both stacked vertically.
# ──────────────────────────────────────────────────────────
class B10_Funnel(Scene):
    def construct(self):
        section = LabelChip("THE FUNNEL", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # Shorts → intro video
        short_lbl = Text("Shorts", font=DISPLAY, color=SLATE, font_size=20, weight=BOLD)
        short_lbl.move_to(UP * 3.0)

        short_chips = VGroup()
        for label in ["Short A", "Short B", "Short C"]:
            t = Text(label, font=MONO, color=INK, font_size=15)
            b = auto_box(t, h_pad=0.14, v_pad=0.10, fill_color=GROUND,
                         stroke_color=SLATE, stroke_width=1.5)
            short_chips.add(VGroup(b, t))
        short_chips.arrange(RIGHT, buff=0.22).move_to(UP * 2.4)
        if short_chips.width > 3.8:
            short_chips.scale_to_fit_width(3.8)

        intro_t = Text("What is Brutalist?", font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        intro_sub = Text("intro VIDEO", font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
        intro_stack = VGroup(intro_t, intro_sub).arrange(DOWN, buff=0.08)
        intro_box = surround_box(intro_stack, buff=0.22, fill_color=GROUND,
                                 stroke_color=ACCENT_TEAL, stroke_width=2)
        intro_grp = VGroup(intro_box, intro_stack).move_to(UP * 1.2)
        if intro_grp.width > 3.8:
            intro_grp.scale_to_fit_width(3.8)

        short_arr = Arrow(short_chips.get_bottom(), intro_grp.get_top(),
                          stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.16, buff=0.06)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=HAIRLINE, stroke_width=1.5)
        divider.move_to(UP * 0.2)

        # Longs → series playlist
        long_lbl = Text("Longs", font=DISPLAY, color=SLATE, font_size=20, weight=BOLD)
        long_lbl.move_to(DOWN * 0.2)

        long_chips = VGroup()
        for label in ["Long A", "Long B", "Long C"]:
            t = Text(label, font=MONO, color=INK, font_size=15)
            b = auto_box(t, h_pad=0.14, v_pad=0.10, fill_color=GROUND,
                         stroke_color=SLATE, stroke_width=1.5)
            long_chips.add(VGroup(b, t))
        long_chips.arrange(RIGHT, buff=0.22).move_to(DOWN * 0.8)
        if long_chips.width > 3.8:
            long_chips.scale_to_fit_width(3.8)

        playlist_t = Text('"Brutalist"', font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        playlist_sub = Text("series PLAYLIST", font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
        playlist_stack = VGroup(playlist_t, playlist_sub).arrange(DOWN, buff=0.08)
        playlist_box = surround_box(playlist_stack, buff=0.22, fill_color=GROUND,
                                    stroke_color=ACCENT_TEAL, stroke_width=2)
        playlist_grp = VGroup(playlist_box, playlist_stack).move_to(DOWN * 1.9)
        if playlist_grp.width > 3.8:
            playlist_grp.scale_to_fit_width(3.8)

        long_arr = Arrow(long_chips.get_bottom(), playlist_grp.get_top(),
                         stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.16, buff=0.06)

        self.play(FadeIn(short_lbl), FadeIn(short_chips), run_time=0.5)
        self.play(GrowArrow(short_arr), FadeIn(intro_grp, scale=0.9), run_time=0.5)
        self.wait(0.2)
        self.play(Create(divider), run_time=0.25)
        self.play(FadeIn(long_lbl), FadeIn(long_chips), run_time=0.5)
        self.play(GrowArrow(long_arr), FadeIn(playlist_grp, scale=0.9), run_time=0.5)
        self.wait(0.3)

        caption = SerifLabel("appended to every description automatically.", accent=ACCENT_TEAL, size=17)
        caption.to_edge(DOWN, buff=0.45)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)
        self.play(FadeIn(caption), run_time=0.45)
        self.wait(6.0)


# ──────────────────────────────────────────────────────────
# B11 — THE THREE, LIVE (portrait, 14s)
# Three stacked video cards — portrait-natural.
# ──────────────────────────────────────────────────────────
class B11_TheThree(Scene):
    def construct(self):
        section = LabelChip("THE THREE, LIVE", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        pl_label = LabelChip("Brutalist playlist", accent=ACCENT_TEAL, size=16)
        pl_label.to_edge(UP, buff=0.55)
        self.play(FadeIn(pl_label), run_time=0.35)

        videos = [
            ("ch1", "What is Brutalist?",             "xXKgCXc1nm4"),
            ("ch2", "Installs, .env & Credentials",   "7rUcwkFOhvM"),
            ("ch3", "When Cowork Can Help Claude Code","AhdmP75PBY0"),
        ]
        cards = VGroup()
        for ch, title_s, vid_id in videos:
            ch_t = Text(ch, font=DISPLAY, color=ACCENT_TEAL, font_size=14, weight=BOLD)
            title_t = Text(title_s, font=DISPLAY, color=INK, font_size=15, weight=BOLD)
            id_t = Text(f"youtu.be/{vid_id}", font=MONO, color=SLATE, font_size=12)
            unlisted_t = Text("unlisted", font=MONO, color=ACCENT_TEAL, font_size=12)
            row_top = VGroup(ch_t, title_t).arrange(RIGHT, buff=0.22)
            row_bot = VGroup(id_t, unlisted_t).arrange(RIGHT, buff=0.28)
            card_content = VGroup(row_top, row_bot).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            card_box = surround_box(card_content, buff=0.20, fill_color=GROUND,
                                    stroke_color=ACCENT_TEAL, stroke_width=2)
            card = VGroup(card_box, card_content)
            if card.width > 3.8:
                card.scale_to_fit_width(3.8)
            cards.add(card)

        cards.arrange(DOWN, buff=0.26).move_to(DOWN * 0.4)
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.1), run_time=0.45)
            self.wait(0.12)
        self.wait(8.0)


# ──────────────────────────────────────────────────────────
# B12 — THE SPLIT — HERO BEAT (portrait, 21s)
# Dark bg. Title stacked. Machine list (left→center). Switch below.
# ──────────────────────────────────────────────────────────
class B12_TheSplit(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        title = Text("THE MACHINE POSTS.", font=SERIF, color=WHITE,
                     font_size=32, weight=BOLD)
        title.move_to(UP * 3.2)
        if title.width > 3.8:
            title.scale_to_fit_width(3.8)
        self.play(Write(title), run_time=0.8)

        subtitle = Text("YOU OWN WHAT SHIPS.", font=SERIF, color=ACCENT_TEAL,
                        font_size=28, weight=BOLD)
        subtitle.next_to(title, DOWN, buff=0.18)
        if subtitle.width > 3.8:
            subtitle.scale_to_fit_width(3.8)
        underline = Line(subtitle.get_corner(DL) + DOWN * 0.06,
                         subtitle.get_corner(DR) + DOWN * 0.06,
                         stroke_color=ACCENT_TEAL, stroke_width=2.5)
        self.play(FadeIn(subtitle, shift=DOWN * 0.1), Create(underline), run_time=0.65)
        self.wait(0.35)

        # Machine items — centered vertical list
        machine_lbl = SerifLabel("the machine", accent=ACCENT_TEAL, size=20)
        machine_lbl.move_to(UP * 1.5)
        machine_items = ["description", "chapters", "tags", "playlist order", "ledger"]
        machine_grp = VGroup(*[
            Text(item, font=MONO, color=ACCENT_TEAL, font_size=17)
            for item in machine_items
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        machine_grp.move_to(UP * 0.4)

        self.play(FadeIn(machine_lbl), run_time=0.35)
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in machine_grp],
                              lag_ratio=0.12), run_time=0.75)
        self.wait(0.25)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0,
                       stroke_color=WHITE, stroke_width=1, stroke_opacity=0.3)
        divider.move_to(DOWN * 0.7)
        self.play(Create(divider), run_time=0.3)

        # Human switch (still off)
        human_lbl = SerifLabel("you", accent=WHITE, size=20)
        human_lbl.move_to(DOWN * 0.80)

        switch_bg = Rectangle(width=1.6, height=0.65,
                              fill_color="#333333", fill_opacity=1,
                              stroke_color=WHITE, stroke_width=1.5, stroke_opacity=0.5)
        switch_dot = Circle(radius=0.24, fill_color=SLATE, fill_opacity=1, stroke_width=0)
        switch_dot.move_to(switch_bg.get_left() + RIGHT * 0.35)
        switch_grp = VGroup(switch_bg, switch_dot).move_to(DOWN * 1.7)

        public_lbl = Text("PUBLIC", font=DISPLAY, color=SLATE, font_size=16, weight=BOLD)
        public_lbl.next_to(switch_grp, UP, buff=0.16)
        public_lbl.set_opacity(0.5)

        waiting_lbl = Text("unlisted · waiting", font=SERIF, color=SLATE,
                           font_size=14, slant=ITALIC)
        waiting_lbl.next_to(switch_grp, DOWN, buff=0.18)

        self.play(FadeIn(human_lbl), run_time=0.35)
        self.play(FadeIn(switch_grp), FadeIn(public_lbl), FadeIn(waiting_lbl), run_time=0.55)
        self.wait(0.4)

        # Coda
        baton = Line(LEFT * 1.8, RIGHT * 1.8,
                     stroke_color=WHITE, stroke_width=3, stroke_opacity=0.35)
        baton.to_edge(DOWN, buff=1.0)
        coda = Text("it plays every part — you own what ships.", font=SERIF,
                    color=ACCENT_TEAL, font_size=17)
        if coda.width > 3.8:
            coda.scale_to_fit_width(3.8)
        coda.to_edge(DOWN, buff=0.42)
        self.play(Create(baton), FadeIn(coda, shift=UP * 0.1), run_time=0.75)
        self.wait(10.5)
