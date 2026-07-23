"""scenes.py — PORTRAIT (9:16) layouts for 'When Cowork Can Help Claude Code' short.

Kept GENERATED beats: B01, B05, B06, B07, B08, B10, B11, B14.
Dropped:             B03, B04, B13.

Frame: 1080×1920 → Manim units ~4.5 wide × 8.0 tall (x: ±2.25, y: ±4.0).
Strategy: vertical stacks replace left/right splits; font sizes ~0.72× landscape.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — THE BUILD WAS GOING WELL (portrait, 15s)
# Progress column then blocked row — works naturally vertical.
# ──────────────────────────────────────────────────────────
class B01_GoingWell(Scene):
    def construct(self):
        section = LabelChip("THE INSTALLS BUILD", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        def make_row(label, status, color):
            lbl = Text(label, font=MONO, color=INK, font_size=18)
            st  = Text(status, font=MONO, color=color, font_size=18)
            row = VGroup(lbl, st).arrange(RIGHT, buff=0.28)
            if row.width > 3.6:
                row.scale_to_fit_width(3.6)
            box = surround_box(row, buff=0.20, fill_color=GROUND,
                               stroke_color=color, stroke_width=2)
            return VGroup(box, row)

        rows = VGroup(
            make_row("narration",         "✓  recorded",     ACCENT_TEAL),
            make_row("B01–B12 Manim",     "✓  9 beats done", ACCENT_TEAL),
            make_row("draft cut",         "✓  on disk",      ACCENT_TEAL),
        )
        rows.arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        rows.move_to(UP * 1.5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.45)
            self.wait(0.12)
        self.wait(1.0)

        blocked = make_row("6 Remotion beats", "… stalled", CRIMSON)
        blocked.next_to(rows, DOWN, buff=0.26)
        blocked.align_to(rows, LEFT)

        caption = SerifLabel("then it hit the six terminal beats.", accent=CRIMSON, size=20)
        caption.to_edge(DOWN, buff=0.55)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)

        self.play(FadeIn(blocked, shift=RIGHT * 0.1), run_time=0.55)
        self.play(FadeIn(caption), run_time=0.45)
        self.wait(7.0)


# ──────────────────────────────────────────────────────────
# B05 — MORE EFFORT, SAME SEAT (portrait, 5s)
# Shaft + figure + downward arrow. Fits well vertically.
# ──────────────────────────────────────────────────────────
class B05_SameSeat(Scene):
    def construct(self):
        section = LabelChip("SAME SEAT", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # Narrow vertical shaft
        shaft_left  = LEFT * 0.8
        shaft_right = RIGHT * 0.8
        shaft_top   = UP * 3.2

        wall_l = Line(shaft_top + shaft_left,  DOWN * 0.8 + shaft_left,
                      stroke_color=INK, stroke_width=2.5)
        wall_r = Line(shaft_top + shaft_right, DOWN * 0.8 + shaft_right,
                      stroke_color=INK, stroke_width=2.5)
        top_cap = Line(shaft_top + shaft_left, shaft_top + shaft_right,
                       stroke_color=INK, stroke_width=2.5)
        self.play(Create(VGroup(wall_l, wall_r, top_cap)), run_time=0.45)

        # Figure at bottom of shaft
        fig_pos = DOWN * 0.5
        fig_head = Dot(radius=0.16, color=INK).move_to(fig_pos + UP * 0.32)
        fig_body = Line(fig_pos + UP * 0.16, fig_pos + DOWN * 0.20,
                        stroke_color=INK, stroke_width=3)
        self.play(FadeIn(VGroup(fig_head, fig_body)), run_time=0.28)

        # Downward arrow + label
        deeper_arrow = Arrow(
            DOWN * 0.8, DOWN * 2.4,
            stroke_color=CRIMSON, stroke_width=3, tip_length=0.20, buff=0,
        )
        deeper_lbl = Text("try harder", font=DISPLAY, color=CRIMSON,
                          font_size=19, weight=BOLD)
        deeper_lbl.move_to(DOWN * 2.65)

        ext_l = Line(DOWN * 0.8 + shaft_left, DOWN * 2.4 + shaft_left,
                     stroke_color=INK, stroke_width=2.5)
        ext_r = Line(DOWN * 0.8 + shaft_right, DOWN * 2.4 + shaft_right,
                     stroke_color=INK, stroke_width=2.5)

        self.play(GrowArrow(deeper_arrow), FadeIn(deeper_lbl),
                  Create(ext_l), Create(ext_r), run_time=0.7)
        self.wait(0.25)

        caption = SerifLabel("more effort from the same vantage doesn't help.", accent=CRIMSON, size=18)
        caption.to_edge(DOWN, buff=0.55)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)
        self.play(FadeIn(caption), run_time=0.55)
        self.wait(1.5)


# ──────────────────────────────────────────────────────────
# B06 — THE WRONG NOTE (portrait, 18s)
# Conductor figure + baton; red "?" rises from staff.
# ──────────────────────────────────────────────────────────
class B06_WrongNote(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        section = LabelChip("THE CONDUCTOR", accent=INK, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # Baton — horizontal, narrower for portrait
        baton = Line(LEFT * 1.6, RIGHT * 1.6, stroke_color=INK, stroke_width=5)
        baton.move_to(UP * 2.0)
        self.play(Create(baton), run_time=0.55)
        self.wait(0.18)

        # Conductor silhouette
        head = Circle(radius=0.28, fill_color=INK, fill_opacity=1, stroke_width=0)
        head.move_to(UP * 1.3)
        body = Line(UP * 1.02, UP * 0.3, stroke_color=INK, stroke_width=4)
        arms = Line(LEFT * 0.48 + UP * 0.7, RIGHT * 0.48 + UP * 0.7,
                    stroke_color=INK, stroke_width=3)
        conductor = VGroup(head, body, arms)
        self.play(FadeIn(conductor, scale=0.9), run_time=0.45)

        # Orchestra staff
        staff = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=INK, stroke_width=1.2)
        staff.move_to(DOWN * 0.5)
        self.play(Create(staff), run_time=0.35)

        # Red "?" note rises — offset right so it clears the conductor body (x=0)
        note_q = Text("?", font=DISPLAY, color=CRIMSON, font_size=48, weight=BOLD)
        note_q.move_to(RIGHT * 0.65 + DOWN * 0.5)
        self.play(FadeIn(note_q), note_q.animate.shift(UP * 1.6), run_time=0.8)
        self.wait(0.35)

        # Caption
        cap1 = Text("this is taking far too long", font=SERIF, color=INK, font_size=20)
        cap2 = Text("for a video this simple.", font=SERIF, color=INK, font_size=20)
        captions = VGroup(cap1, cap2).arrange(DOWN, buff=0.16)
        captions.to_edge(DOWN, buff=1.3)
        if captions.width > 3.8:
            captions.scale_to_fit_width(3.8)
        self.play(FadeIn(captions, shift=UP * 0.1), run_time=0.65)
        self.wait(0.35)

        sub = SerifLabel("you don't need to know what's wrong to know something is.",
                         accent=CRIMSON, size=17)
        sub.to_edge(DOWN, buff=0.45)
        if sub.width > 3.8:
            sub.scale_to_fit_width(3.8)
        self.play(FadeIn(sub), run_time=0.55)
        self.wait(8.0)


# ──────────────────────────────────────────────────────────
# B07 — A DIFFERENT SEAT (portrait, 18s)
# Top: stuck agent in narrow terminal box.
# Bottom: Cowork with repo tree.
# ──────────────────────────────────────────────────────────
class B07_DifferentSeat(Scene):
    def construct(self):
        section = LabelChip("A DIFFERENT SEAT", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # TOP: stuck agent
        top_lbl = SerifLabel("stuck agent", accent=CRIMSON, size=20)
        top_lbl.move_to(UP * 3.0)
        self.play(FadeIn(top_lbl), run_time=0.35)

        term_header = Text("$ npx remotion render … &", font=MONO, color=WHITE, font_size=13)
        term_body = VGroup(
            Text("waiting…", font=MONO, color=SLATE, font_size=13),
            Text("just a couple more minutes.", font=MONO, color=SLATE, font_size=13),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10)
        term_content = VGroup(term_header, term_body).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        term_box = surround_box(term_content, buff=0.22,
                                fill_color="#111111", stroke_color=CRIMSON, stroke_width=2)
        term_grp = VGroup(term_box, term_content).move_to(UP * 1.8)
        if term_grp.width > 3.8:
            term_grp.scale_to_fit_width(3.8)

        caption_t = Text("can only see its own render", font=SERIF,
                         color=CRIMSON, font_size=15, slant=ITALIC)
        caption_t.next_to(term_grp, DOWN, buff=0.22)

        self.play(FadeIn(term_grp), run_time=0.55)
        self.play(FadeIn(caption_t), run_time=0.35)
        self.wait(0.5)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(UP * 0.4)
        self.play(Create(divider), run_time=0.3)

        # BOTTOM: Cowork
        bot_lbl = SerifLabel("Cowork", accent=ACCENT_TEAL, size=20)
        bot_lbl.move_to(UP * 0.0)
        self.play(FadeIn(bot_lbl), run_time=0.35)

        tree_items = [
            ("mp3/   15 files",  "← narration done",   ACCENT_TEAL),
            ("manim/ 9 files",   "← concept beats done", ACCENT_TEAL),
            ("media/ (empty)",   "← 6 beats stuck",    CRIMSON),
        ]
        tree_rows = VGroup()
        for path, note, color in tree_items:
            p = Text(path, font=MONO, color=INK, font_size=14)
            n = Text(note, font=MONO, color=color, font_size=14)
            row = VGroup(p, n).arrange(RIGHT, buff=0.22)
            if row.width > 3.6:
                row.scale_to_fit_width(3.6)
            tree_rows.add(row)
        tree_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        tree_box = surround_box(tree_rows, buff=0.22,
                                fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2)
        tree_grp = VGroup(tree_box, tree_rows).move_to(DOWN * 1.5)
        if tree_grp.width > 3.8:
            tree_grp.scale_to_fit_width(3.8)

        caption_b = Text("sees the whole board in one look", font=SERIF,
                         color=ACCENT_TEAL, font_size=15, slant=ITALIC)
        caption_b.to_edge(DOWN, buff=0.45)
        if caption_b.width > 3.8:
            caption_b.scale_to_fit_width(3.8)

        self.play(FadeIn(tree_grp), run_time=0.65)
        self.play(FadeIn(caption_b), run_time=0.35)
        self.wait(8.5)


# ──────────────────────────────────────────────────────────
# B08 — NO SUNK COST (portrait, 9s)
# Balance scale — tilt toward the stuck agent (top).
# Cowork "drop it" (bottom).
# ──────────────────────────────────────────────────────────
class B08_NoSunkCost(Scene):
    def construct(self):
        section = LabelChip("NO SUNK COST", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # Simple tilted beam scale — scaled to ±1.5 to stay within portrait safe area
        pivot_stand = Line(UP * 0.2, DOWN * 0.8, stroke_color=INK, stroke_width=3)
        base = Line(LEFT * 0.5 + DOWN * 0.8, RIGHT * 0.5 + DOWN * 0.8,
                    stroke_color=INK, stroke_width=3)
        pivot = Dot(radius=0.09, color=INK).move_to(UP * 0.2)
        beam = Line(LEFT * 1.5 + DOWN * 0.3, RIGHT * 1.5 + UP * 0.2,
                    stroke_color=INK, stroke_width=3).move_to(UP * 0.2)
        self.play(Create(VGroup(pivot_stand, base, pivot, beam)), run_time=0.5)

        # LEFT pan — heavy (stuck agent)
        pan_l = Circle(radius=0.45, stroke_color=CRIMSON, stroke_width=2.5,
                       fill_opacity=0).move_to(LEFT * 1.5 + DOWN * 0.4)
        left_lbl = VGroup(
            Text("1 hour", font=DISPLAY, color=CRIMSON, font_size=14, weight=BOLD),
            Text("invested", font=SERIF, color=CRIMSON, font_size=12),
        ).arrange(DOWN, buff=0.06)
        left_lbl.move_to(pan_l)
        stuck = SerifLabel("stuck agent", accent=CRIMSON, size=13)
        stuck.next_to(pan_l, UP, buff=0.18)
        self.play(FadeIn(pan_l), FadeIn(left_lbl), FadeIn(stuck), run_time=0.55)

        # RIGHT pan — light (Cowork)
        pan_r = Circle(radius=0.40, stroke_color=ACCENT_TEAL, stroke_width=2,
                       fill_opacity=0, stroke_opacity=0.7).move_to(RIGHT * 1.5 + UP * 0.4)
        drop_txt = Text("drop it", font=SERIF, color=ACCENT_TEAL, font_size=14, slant=ITALIC)
        drop_txt.move_to(pan_r)
        cowork_lbl = SerifLabel("Cowork", accent=ACCENT_TEAL, size=13)
        cowork_lbl.next_to(pan_r, UP, buff=0.15)
        self.play(FadeIn(pan_r), FadeIn(drop_txt), FadeIn(cowork_lbl), run_time=0.55)
        self.wait(0.35)

        caption = SerifLabel("no investment → just abandon it.", accent=ACCENT_TEAL, size=19)
        caption.to_edge(DOWN, buff=0.55)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)
        self.play(FadeIn(caption), run_time=0.45)
        self.wait(5.5)


# ──────────────────────────────────────────────────────────
# B10 — NEVER BROKEN (portrait, 13s)
# Two stacked row cards; conclusion below.
# ──────────────────────────────────────────────────────────
class B10_NeverBroken(Scene):
    def construct(self):
        section = LabelChip("NEVER BROKEN", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        def make_row(vid, status, color):
            vid_t = Text(vid, font=MONO, color=INK, font_size=16)
            arrow = Text("→", font=MONO, color=color, font_size=16)
            status_t = Text(status, font=MONO, color=color, font_size=16, weight=BOLD)
            row = VGroup(vid_t, arrow, status_t).arrange(RIGHT, buff=0.22)
            if row.width > 3.6:
                row.scale_to_fit_width(3.6)
            box = surround_box(row, buff=0.20, fill_color=GROUND,
                               stroke_color=color, stroke_width=2)
            return VGroup(box, row)

        row1 = make_row("video 1 — same Remotion", "✓  rendered", ACCENT_TEAL)
        row2 = make_row("video 2 — same components", "stuck",       CRIMSON)

        rows = VGroup(row1, row2).arrange(DOWN, buff=0.30)
        rows.move_to(UP * 1.8)

        self.play(FadeIn(row1, shift=RIGHT * 0.1), run_time=0.55)
        self.wait(0.25)
        self.play(FadeIn(row2, shift=RIGHT * 0.1), run_time=0.55)
        self.wait(0.35)

        brace_txt = Text("so the pipeline was never broken.", font=SERIF, color=INK, font_size=20)
        if brace_txt.width > 3.8:
            brace_txt.scale_to_fit_width(3.8)
        brace_box = surround_box(brace_txt, buff=0.20, fill_color=GROUND,
                                 stroke_color=INK, stroke_width=1.5)
        brace_grp = VGroup(brace_box, brace_txt)
        brace_grp.next_to(rows, DOWN, buff=0.40)
        self.play(FadeIn(brace_grp, shift=UP * 0.1), run_time=0.55)
        self.wait(0.25)

        stamp_txt = Text("not a bug to hunt — a wrong approach to drop.",
                         font=SERIF, color=CRIMSON, font_size=18)
        if stamp_txt.width > 3.8:
            stamp_txt.scale_to_fit_width(3.8)
        stamp_txt.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(stamp_txt), run_time=0.55)
        self.wait(6.5)


# ──────────────────────────────────────────────────────────
# B11 — THE HELPER RIGHT THERE (portrait, 10s)
# File box centered + spotlight + crossed-out command below.
# ──────────────────────────────────────────────────────────
class B11_HelperRightThere(Scene):
    def construct(self):
        section = LabelChip("THE TOOL WAS RIGHT THERE", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # File box
        file_name = Text("runtime/scripts/remotion_scenes.py",
                         font=MONO, color=INK, font_size=16, weight=BOLD)
        if file_name.width > 3.6:
            file_name.scale_to_fit_width(3.6)
        file_desc = Text("renders each beat · foreground · one at a time",
                         font=MONO, color=ACCENT_TEAL, font_size=14)
        if file_desc.width > 3.6:
            file_desc.scale_to_fit_width(3.6)
        file_content = VGroup(file_name, file_desc).arrange(DOWN, buff=0.20, aligned_edge=LEFT)
        file_box = surround_box(file_content, buff=0.28,
                                fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=3)
        file_grp = VGroup(file_box, file_content).move_to(UP * 1.5)
        self.play(FadeIn(file_grp, scale=0.9), run_time=0.65)

        spot = SurroundingRectangle(file_grp, buff=0.16, color=ACCENT_TEAL, stroke_width=4)
        self.play(Create(spot), run_time=0.55)
        self.wait(0.25)

        # Crossed-out improvised command
        wrong_cmd = Text("npx remotion render … &", font=MONO, color=CRIMSON, font_size=18)
        if wrong_cmd.width > 3.6:
            wrong_cmd.scale_to_fit_width(3.6)
        wrong_box = auto_box(wrong_cmd, h_pad=0.18, v_pad=0.13,
                             fill_color="#FFF0F0", stroke_color=CRIMSON, stroke_width=2)
        wrong_grp = VGroup(wrong_box, wrong_cmd).next_to(file_grp, DOWN, buff=0.45)
        strikethrough = Line(wrong_grp.get_left() + LEFT * 0.05,
                             wrong_grp.get_right() + RIGHT * 0.05,
                             stroke_color=CRIMSON, stroke_width=5)
        strikethrough.move_to(wrong_grp)
        strikethrough._qc_intentional = True   # intentional strike-through crossing text

        self.play(FadeIn(wrong_grp), run_time=0.45)
        self.play(Create(strikethrough), run_time=0.45)
        self.wait(0.25)

        caption = SerifLabel("the tool was right there the whole time.", accent=INK, size=19)
        caption.to_edge(DOWN, buff=0.55)
        if caption.width > 3.8:
            caption.scale_to_fit_width(3.8)
        self.play(FadeIn(caption), run_time=0.45)
        self.wait(5.5)


# ──────────────────────────────────────────────────────────
# B14 — THE LESSON — HERO BEAT (portrait, 21s)
# Dark bg. Title + three marks + conductor baton coda.
# ──────────────────────────────────────────────────────────
class B14_TheLesson(Scene):
    def construct(self):
        self.camera.background_color = "#2A1A0E"

        title = Text("A SECOND SET", font=SERIF, color=WHITE, font_size=40, weight=BOLD)
        title2 = Text("OF EYES", font=SERIF, color=WHITE, font_size=40, weight=BOLD)
        title_grp = VGroup(title, title2).arrange(DOWN, buff=0.06)
        title_grp.move_to(UP * 2.8)
        if title_grp.width > 3.8:
            title_grp.scale_to_fit_width(3.8)
        self.play(Write(title_grp), run_time=1.0)

        underline = Line(
            title_grp.get_corner(DL) + DOWN * 0.08,
            title_grp.get_corner(DR) + DOWN * 0.08,
            stroke_color=ACCENT_TEAL, stroke_width=3,
        )
        self.play(Create(underline), run_time=0.45)
        self.wait(0.35)

        marks_data = [
            ("any single agent can tunnel",           CRIMSON),
            ("a different seat sees it",              WHITE),
            ("the human calls for it",                ACCENT_TEAL),
        ]
        marks = VGroup()
        for text, color in marks_data:
            bullet = Text("·", font=SERIF, color=ACCENT_TEAL, font_size=28)
            line   = Text(text, font=SERIF, color=color, font_size=21)
            row = VGroup(bullet, line).arrange(RIGHT, buff=0.25)
            if row.width > 3.8:
                row.scale_to_fit_width(3.8)
            marks.add(row)
        marks.arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        marks.move_to(UP * 0.5)

        for mark in marks:
            self.play(FadeIn(mark, shift=UP * 0.10), run_time=0.58)
            self.wait(0.28)

        self.wait(0.4)

        baton = Line(LEFT * 1.6, RIGHT * 1.6,
                     stroke_color=WHITE, stroke_width=3, stroke_opacity=0.4)
        baton.move_to(DOWN * 2.4)

        coda_text = Text("you heard it · and asked · that is conducting too.",
                         font=SERIF, color=ACCENT_TEAL, font_size=17)
        if coda_text.width > 3.8:
            coda_text.scale_to_fit_width(3.8)
        coda_text.to_edge(DOWN, buff=0.45)

        self.play(Create(baton), FadeIn(coda_text, shift=UP * 0.1), run_time=0.7)
        self.wait(9.5)
