"""scenes.py — PORTRAIT (9:16) layouts for 'What is Brutalist?' short.

Kept beats: B00B, B01, B02, B03, B05, B07, B08, B09, B14.
Dropped:    B06, B08B, B11.

Frame: 1080×1920 → Manim units ~4.5 wide × 8.0 tall (x: ±2.25, y: ±4.0).
Strategy: vertical stacks replace left/right splits; font sizes ~0.72× landscape.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *
import numpy as np

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B00B — REVIEW LABEL (portrait, 23s)
# Show the chip; vertical callout list for each field.
# ──────────────────────────────────────────────────────────
class B00B_ReviewLabel(Scene):
    LABEL_STR = "B01  MANIM  FILLED   9.5s  +9.4s"

    def construct(self):
        section = LabelChip("REVIEW LABEL", accent=ACCENT_TEAL, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # The chip itself
        lbl_txt = Text(self.LABEL_STR, font=MONO, font_size=13, color=WHITE)
        lbl_bg = Rectangle(
            width=lbl_txt.width + 0.22,
            height=lbl_txt.height + 0.16,
            fill_color="#000000", fill_opacity=0.70, stroke_width=0,
        )
        lbl_bg.move_to(lbl_txt)
        chip = VGroup(lbl_bg, lbl_txt)
        chip.move_to(UP * 2.8)
        self.play(FadeIn(chip), run_time=0.5)

        ring = SurroundingRectangle(chip, buff=0.18, color=CRIMSON, stroke_width=3)
        self.play(Create(ring), run_time=0.6)
        self.wait(0.3)

        # Five callout rows (vertical list instead of radial)
        callout_data = [
            ("beat id",                        CRIMSON),
            ("engine  (Manim / Remotion / AI)", ACCENT_TEAL),
            ("status",                          INK),
            ("start on timeline",               "#7A5A3A"),
            ("beat duration",                   "#7A5A3A"),
        ]
        rows = VGroup()
        for label, color in callout_data:
            dot = Dot(radius=0.07, color=color)
            t = Text(label, font=SERIF, font_size=18, color=color)
            row = VGroup(dot, t).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        rows.move_to(DOWN * 0.6)
        if rows.width > 3.8:
            rows.scale_to_fit_width(3.8)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.38)
        self.wait(0.5)

        summary = SerifLabel("every beat · labelled · every frame", accent=INK, size=18)
        summary.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(summary), run_time=0.6)
        self.wait(6.5)


# ──────────────────────────────────────────────────────────
# B01 — ONE-CLICK SLOP (portrait, 9s)
# ──────────────────────────────────────────────────────────
class B01_OneClickSlop(Scene):
    def construct(self):
        # Button at top
        btn_box = Rectangle(width=2.6, height=0.9, fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=2.5)
        btn_lbl = Text("MAKE VIDEO", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        btn_lbl.move_to(btn_box)
        button = VGroup(btn_box, btn_lbl).move_to(UP * 2.5)

        # Two-frame filmstrip (fits portrait width)
        frames = []
        for i in range(2):
            f = Rectangle(width=1.3, height=1.8, fill_color="#EEEEEE", fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
            for dy in [0.72, -0.72]:
                hole = Rectangle(width=0.16, height=0.22, fill_color=INK, fill_opacity=1,
                                 stroke_width=0)
                hole.move_to(f.get_center() + np.array([0, dy, 0]))
                f = VGroup(f, hole)
            frames.append(f)
        filmstrip = VGroup(*frames).arrange(RIGHT, buff=0.12).move_to(UP * 0.7)

        # SLOP stamp
        slop_lbl = Text("SLOP", font=DISPLAY, color=CRIMSON, font_size=64, weight=BOLD,
                         slant=ITALIC)
        slop_line = Line(slop_lbl.get_corner(DL) + DOWN * 0.06,
                         slop_lbl.get_corner(DR) + DOWN * 0.06,
                         stroke_width=4, color=CRIMSON)
        slop = VGroup(slop_lbl, slop_line).move_to(DOWN * 0.5).rotate(-0.18)

        self.play(FadeIn(button, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.4)
        self.play(button.animate.scale(0.92), run_time=0.18)
        self.play(button.animate.scale(1.0 / 0.92), run_time=0.14)
        self.play(FadeIn(filmstrip, shift=UP * 0.3), run_time=0.7)
        self.wait(0.6)
        slop.scale(0.01)
        self.play(slop.animate.scale(100), run_time=0.5)
        self.wait(3.5)


# ──────────────────────────────────────────────────────────
# B02 — CANNOT WATCH (portrait, 6s)
# AI circle → dashed gap → screen: natural vertical flow.
# ──────────────────────────────────────────────────────────
class B02_CannotWatch(Scene):
    def construct(self):
        # AI node at top
        ai_circle = Circle(radius=0.65, fill_color=GROUND, fill_opacity=1,
                           stroke_color=INK, stroke_width=2.5).move_to(UP * 2.5)
        ai_lbl = Text("AI", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        ai_lbl.move_to(ai_circle)
        eye_outer = Ellipse(width=0.42, height=0.26, stroke_color=SLATE, stroke_width=2)
        eye_dot = Dot(radius=0.07, color=SLATE)
        eye = VGroup(eye_outer, eye_dot).next_to(ai_circle, UP, buff=0.05)
        cross1 = Line(eye.get_corner(UL), eye.get_corner(DR), stroke_color=CRIMSON, stroke_width=2.5)
        cross2 = Line(eye.get_corner(UR), eye.get_corner(DL), stroke_color=CRIMSON, stroke_width=2.5)
        ai_node = VGroup(ai_circle, ai_lbl, eye, cross1, cross2)

        # Screen below
        screen = Rectangle(width=2.6, height=1.7, fill_color="#1A1A1A", fill_opacity=1,
                            stroke_color=INK, stroke_width=2).move_to(DOWN * 1.2)
        for i, col in enumerate(["#C8102E", "#EEEEEE", "#555555"]):
            bar = Rectangle(width=2.0, height=0.25, fill_color=col, fill_opacity=0.7,
                             stroke_width=0)
            bar.move_to(screen.get_center() + UP * (0.3 - i * 0.3))
            screen.add(bar)
        screen_grp = VGroup(screen)

        # Vertical dashed gap
        gap_start = ai_circle.get_bottom() + DOWN * 0.1
        gap_end = screen.get_top() + UP * 0.1
        dashed = DashedLine(gap_start, gap_end, dash_length=0.18,
                            dashed_ratio=0.5, stroke_color=SLATE, stroke_width=2)

        self.play(FadeIn(ai_node, shift=DOWN * 0.2), run_time=0.7)
        self.play(FadeIn(screen_grp, shift=UP * 0.2), run_time=0.7)
        self.wait(0.4)
        self.play(Create(dashed), run_time=0.9)
        self.wait(2.8)


# ──────────────────────────────────────────────────────────
# B03 — TASTE GAPS (portrait, 12s)
# Three stacked question cards — works naturally in portrait.
# ──────────────────────────────────────────────────────────
class B03_TasteGaps(Scene):
    def construct(self):
        human_lbl = Text("human", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        human_lbl.to_edge(UP, buff=1.0)
        self.play(FadeIn(human_lbl), run_time=0.4)

        questions = ["funny?", "interesting?", "did it land?"]
        cards = VGroup()
        checks = VGroup()
        for q in questions:
            checkbox = Square(side_length=0.30, stroke_color=INK, stroke_width=2, fill_opacity=0)
            label = Text(q, font=SERIF, color=INK, font_size=28, slant=ITALIC)
            row = VGroup(checkbox, label).arrange(RIGHT, buff=0.22)
            box = auto_box(row, h_pad=0.28, v_pad=0.22,
                           fill_color=GROUND, stroke_color=INK, stroke_width=2)
            card = VGroup(box, checkbox, label)
            cards.add(card)
            chk = Text("✓", font=DISPLAY, color=ACCENT_TEAL, font_size=26, weight=BOLD)
            chk.move_to(checkbox.get_center())
            checks.add(chk)

        cards.arrange(DOWN, buff=0.32).move_to(ORIGIN + DOWN * 0.2)
        if cards.width > 3.8:
            cards.scale_to_fit_width(3.8)

        for card, chk in zip(cards, checks):
            self.play(FadeIn(card, shift=RIGHT * 0.25), run_time=0.65)
            self.wait(0.4)
            chk.move_to(card[1].get_center())
            self.play(FadeIn(chk, scale=1.3), run_time=0.45)
            self.wait(0.4)
        self.wait(3.0)


# ──────────────────────────────────────────────────────────
# B05 — TWENTY-HOUR BUG (portrait, 12s)
# Top: human debug side; bottom: machine side. Vertical split.
# ──────────────────────────────────────────────────────────
class B05_TwentyHourBug(Scene):
    def construct(self):
        # Top: human side (CRIMSON)
        clock_lbl = Text("20:00:00", font="PT Mono", color=INK, font_size=42, weight=BOLD)
        clock_sub = Text("human, debugging", font=SERIF, color=SLATE, font_size=18)
        error_text = Text("ERROR: render failed", font="PT Mono", color=CRIMSON, font_size=15)
        h_stack = VGroup(clock_lbl, clock_sub, error_text).arrange(DOWN, buff=0.18)
        h_stack.move_to(UP * 2.0)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(UP * 0.55)

        # Bottom: machine side (TEAL)
        machine_lbl = Text("0:00:03", font="PT Mono", color=INK, font_size=42, weight=BOLD)
        machine_sub = Text("machine, fixed", font=SERIF, color=ACCENT_TEAL, font_size=18)
        ok_chip = LabelChip("OK", accent=ACCENT_TEAL, size=18)
        machine_stack = VGroup(machine_lbl, machine_sub, ok_chip).arrange(DOWN, buff=0.18)
        machine_stack.move_to(DOWN * 1.5)

        # Waste bar
        waste_bar_bg = Rectangle(width=3.0, height=0.20, fill_color=HAIRLINE, fill_opacity=1,
                                  stroke_width=0)
        waste_bar_bg.next_to(h_stack, DOWN, buff=0.28)
        waste_bar = Rectangle(width=3.0, height=0.20, fill_color=CRIMSON, fill_opacity=0.7,
                               stroke_width=0)
        waste_bar.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)

        self.play(FadeIn(h_stack), Create(divider), FadeIn(machine_stack), run_time=0.9)
        self.wait(0.8)
        self.play(FadeIn(waste_bar_bg), FadeIn(waste_bar), run_time=0.5)
        empty = Rectangle(width=0.01, height=0.20, fill_color=CRIMSON, fill_opacity=0.7,
                          stroke_width=0)
        empty.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)
        self.play(Transform(waste_bar, empty), run_time=2.2)
        self.wait(5.5)


# ──────────────────────────────────────────────────────────
# B07 — YOU ARE THE CONDUCTOR (portrait, 5s) ← HERO
# Dark bg, centered title — ideal for portrait.
# ──────────────────────────────────────────────────────────
class B07_YouAreTheConductor(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        # Baton stroke
        baton = Line(LEFT * 1.8, RIGHT * 1.8, stroke_color=WHITE, stroke_width=5)
        baton.shift(UP * 1.2)

        # Title — break to two lines for portrait width
        title_top = Text("YOU ARE THE", font=SERIF, color=WHITE, font_size=40, weight=BOLD)
        title_bot = Text("CONDUCTOR", font=SERIF, color=WHITE, font_size=40, weight=BOLD)
        title = VGroup(title_top, title_bot).arrange(DOWN, buff=0.1)
        title.move_to(ORIGIN + UP * 0.1)
        if title.width > 4.0:
            title.scale_to_fit_width(4.0)

        underline = Line(title.get_corner(DL) + DOWN * 0.08,
                         title.get_corner(DR) + DOWN * 0.08,
                         stroke_color=CRIMSON, stroke_width=4)

        tools = ["Manim", "Remotion", "ffmpeg"]
        tool_row = VGroup(*[
            Text(t, font=DISPLAY, color=WHITE, font_size=17, weight="MEDIUM")
            for t in tools
        ]).arrange(RIGHT, buff=0.9)
        tool_row.shift(DOWN * 1.8).set_opacity(0.35)
        if tool_row.width > 4.0:
            tool_row.scale_to_fit_width(4.0)

        self.play(Create(baton), run_time=0.8)
        self.wait(0.15)
        self.play(Write(title), run_time=0.9)
        self.play(Create(underline), run_time=0.45)
        self.wait(0.2)
        self.play(FadeIn(tool_row, shift=UP * 0.1), run_time=0.6)
        self.wait(1.8)


# ──────────────────────────────────────────────────────────
# B08 — THE SCORE AND THE PLAYING (portrait, 15s)
# Top: score (human). Divider. Bottom: tools playing.
# ──────────────────────────────────────────────────────────
class B08_ScoreAndPlaying(Scene):
    def construct(self):
        # TOP: score section
        score_lbl = SerifLabel("the score is yours", accent=CRIMSON, size=22)
        score_lbl.move_to(UP * 3.0)

        staff_lines = VGroup(*[
            Line(LEFT * 1.8, RIGHT * 1.8,
                 stroke_color=INK, stroke_width=1.2).shift(UP * (2.2 - i * 0.35))
            for i in range(5)
        ])

        wrong_note = Circle(radius=0.20, stroke_color=CRIMSON, stroke_width=2.5,
                            fill_opacity=0).move_to(LEFT * 0.5 + UP * 1.85)
        annotation = Text("✗", font=DISPLAY, color=CRIMSON, font_size=28)
        annotation.next_to(wrong_note, UP, buff=0.28)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(UP * 1.1)

        # BOTTOM: tool-orchestra playing
        play_lbl = SerifLabel("the playing is its", accent=ACCENT_TEAL, size=22)
        play_lbl.move_to(UP * 0.5)

        tools = [("Manim", "animations"), ("Remotion", "graphics"), ("ffmpeg", "cuts")]
        tool_cards = VGroup()
        for tool, role in tools:
            t = Text(tool, font=DISPLAY, color=INK, font_size=18, weight=BOLD)
            r = Text(role, font=SERIF, color=SLATE, font_size=15)
            row = VGroup(t, r).arrange(RIGHT, buff=0.18)
            card = auto_box(row, h_pad=0.22, v_pad=0.14,
                            fill_color="#F5F5F5", stroke_color=INK, stroke_width=1)
            tool_cards.add(VGroup(card, row))
        tool_cards.arrange(DOWN, buff=0.18).move_to(DOWN * 1.4)
        if tool_cards.width > 3.8:
            tool_cards.scale_to_fit_width(3.8)

        baton_arrow = Arrow(UP * 0.85, UP * 0.65, stroke_color=ACCENT_TEAL,
                            stroke_width=3, tip_length=0.22)
        baton_arrow.move_to(divider.get_center() + DOWN * 0.05)

        self.play(Create(divider), run_time=0.35)
        self.play(FadeIn(score_lbl), FadeIn(staff_lines), run_time=0.8)
        self.play(FadeIn(wrong_note), FadeIn(annotation), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(play_lbl), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(tc, shift=UP * 0.15) for tc in tool_cards],
                               lag_ratio=0.25, run_time=1.2))
        self.play(GrowArrow(baton_arrow), run_time=0.6)
        self.wait(8.5)


# ──────────────────────────────────────────────────────────
# B09 — BEAT SHEET HEART (portrait, 8s)
# Center box; arrows pointing up, left, right.
# ──────────────────────────────────────────────────────────
class B09_BeatSheetHeart(Scene):
    def construct(self):
        heart_lbl = Text("beat_sheet.json", font="PT Mono", color=INK, font_size=22, weight=BOLD)
        beat_rows = Text("B01 · B02 · … · B14", font="PT Mono", color=CRIMSON, font_size=15)
        text_stack = VGroup(heart_lbl, beat_rows).arrange(DOWN, buff=0.18)

        # Plain Rectangle (no text children) so the shape checker sees it as non-textish.
        box_w = max(text_stack.width + 0.56, 2.6)
        box_h = text_stack.height + 0.56
        heart_box = Rectangle(width=box_w, height=box_h,
                              fill_color=GROUND, fill_opacity=1,
                              stroke_color=CRIMSON, stroke_width=3)
        heart_box.move_to(UP * 0.3)
        text_stack.move_to(heart_box)
        heart_grp = VGroup(heart_box, text_stack)

        # Portrait: three outputs stacked BELOW the heart
        out_data = [
            ("todo.json",  SLATE),
            ("STATUS.md",  SLATE),
            ("the cut",    ACCENT_TEAL),
        ]
        out_labels = VGroup()
        for label, col in out_data:
            lbl = Text(label, font="PT Mono", color=col, font_size=18)
            out_labels.add(lbl)
        out_labels.arrange(DOWN, buff=0.30).move_to(DOWN * 2.8)
        if out_labels.width > 3.6:
            out_labels.scale_to_fit_width(3.6)

        # Separator line below heart box
        sep = Line(LEFT * 1.6, RIGHT * 1.6, stroke_color=HAIRLINE, stroke_width=2)
        sep.move_to(DOWN * 1.05)

        # Trunk arrow from below heart to above labels (tip clears label block)
        trunk = Arrow(DOWN * 1.15, DOWN * 2.05, stroke_color=SLATE,
                      stroke_width=2.5, tip_length=0.22)

        # Glow ring (Rectangle, not surround_box — keeps it non-textish)
        glow = Rectangle(width=box_w + 0.12, height=box_h + 0.12,
                         fill_opacity=0, stroke_color=CRIMSON, stroke_width=5)
        glow.move_to(heart_box)

        self.play(FadeIn(heart_box), FadeIn(text_stack), run_time=0.7)
        self.play(Create(glow), glow.animate.set_opacity(0), run_time=0.65)
        self.wait(0.2)
        self.play(Create(sep), GrowArrow(trunk), run_time=0.6)
        for lbl in out_labels:
            self.play(FadeIn(lbl, shift=DOWN * 0.1), run_time=0.5)
        self.wait(4.0)


# ──────────────────────────────────────────────────────────
# B14 — THE PLAYLIST (portrait, 16s)
# Title + 3 cards in portrait vertical list.
# ──────────────────────────────────────────────────────────
class B14_ThePlaylist(Scene):
    def construct(self):
        playlist_title = SerifLabel("Brutalist — Claude for Video", accent=CRIMSON, size=20)
        playlist_title.to_edge(UP, buff=0.7)
        if playlist_title.width > 3.8:
            playlist_title.scale_to_fit_width(3.8)

        # Show 3 entries (fits portrait height comfortably)
        entries = [
            ("What is Brutalist?",   "./art explainer-video"),
            ("sketch-explainer",     "./art sketch-explainer"),
            ("explainer",            "./art explainer"),
        ]
        cards = VGroup()
        for title_s, cmd in entries:
            thumb = Rectangle(width=1.6, height=0.9, fill_color="#EEEEEE", fill_opacity=1,
                              stroke_color=INK, stroke_width=1.5)
            tri = Triangle(fill_color=CRIMSON, fill_opacity=0.8, stroke_width=0).scale(0.18)
            tri.move_to(thumb)
            title_txt = Text(title_s, font=DISPLAY, color=INK, font_size=13, weight=BOLD)
            title_txt.next_to(thumb, DOWN, buff=0.06)
            if title_txt.width > thumb.width * 0.98:
                title_txt.scale_to_fit_width(thumb.width * 0.98)
            cmd_txt = Text(cmd, font="PT Mono", color=CRIMSON, font_size=11)
            cmd_txt.next_to(title_txt, DOWN, buff=0.04)
            card = VGroup(thumb, tri, title_txt, cmd_txt)
            cards.add(card)

        cards.arrange(DOWN, buff=0.5).move_to(DOWN * 0.6)
        if cards.width > 3.8:
            cards.scale_to_fit_width(3.8)

        self.play(FadeIn(playlist_title, shift=DOWN * 0.15), run_time=0.6)
        self.wait(0.2)
        self.play(
            LaggedStart(*[FadeIn(card, shift=UP * 0.25) for card in cards],
                         lag_ratio=0.3, run_time=2.8)
        )
        self.wait(10.0)
