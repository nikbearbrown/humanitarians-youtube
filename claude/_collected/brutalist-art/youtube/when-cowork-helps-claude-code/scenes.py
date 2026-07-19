"""scenes.py — Manim scenes for 'When Cowork Can Help Claude Code'

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B01, B03, B05, B06, B07, B08, B10, B11, B13, B14 (hero).
Palette: teardown — flat white GROUND, ink INK, red CRIMSON, teal ACCENT_TEAL.
B14_TheLesson is the hero beat — most care; EB Garamond, teal accent.
B06_WrongNote callbacks to the conductor beat in video 1.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — THE BUILD WAS GOING WELL (15s)
# Progress column: narration ✓, Manim ✓ (9 beats), draft ✓ — all teal.
# Then a red row appears: "6 Remotion terminal beats …" — the stall point.
# ──────────────────────────────────────────────────────────
class B01_GoingWell(Scene):
    def construct(self):
        section = LabelChip("THE INSTALLS BUILD", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        def make_row(label, status, color, width=9.5):
            lbl = Text(label, font=MONO, color=INK, font_size=22)
            st  = Text(status, font=MONO, color=color, font_size=22)
            row = VGroup(lbl, st).arrange(RIGHT, buff=0.35)
            if row.width > width:
                row.scale_to_fit_width(width)
            box = surround_box(row, buff=0.22,
                               fill_color=GROUND,
                               stroke_color=color, stroke_width=2)
            return VGroup(box, row)

        rows = VGroup(
            make_row("narration",              "✓  recorded",       ACCENT_TEAL),
            make_row("B01–B12 Manim concepts", "✓  9 beats done",   ACCENT_TEAL),
            make_row("draft cut",              "✓  on disk",        ACCENT_TEAL),
        )
        rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        rows.move_to(UP * 0.8)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.5)
            self.wait(0.15)
        self.wait(1.2)

        # The blocking row — red, appears last
        blocked = make_row("6 Remotion terminal beats", "… stalled", CRIMSON)
        blocked.next_to(rows, DOWN, buff=0.28, coor_mask=[1, 0, 0])
        # align left edge
        blocked.align_to(rows, LEFT)

        caption = SerifLabel("then it hit the six terminal beats.", accent=CRIMSON, size=22)
        caption.to_edge(DOWN, buff=0.65)

        self.play(FadeIn(blocked, shift=RIGHT * 0.1), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(6.3)


# ──────────────────────────────────────────────────────────
# B03 — THE TELL (17s)
# A figure at the bottom of a deep shaft, digging downward.
# Each stroke: "one more retry", "one more check".
# Caption: "from the inside, every next step looks reasonable."
# ──────────────────────────────────────────────────────────
class B03_TheTell(Scene):
    def construct(self):
        section = LabelChip("THE TELL", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Deep vertical shaft (left side)
        shaft_top    = UP * 3.2
        shaft_bottom = DOWN * 2.6
        shaft_left   = LEFT * 2.2
        shaft_right  = LEFT * 0.2

        wall_l = Line(shaft_top + shaft_left, shaft_bottom + shaft_left,
                      stroke_color=INK, stroke_width=2.5)
        wall_r = Line(shaft_top + shaft_right, shaft_bottom + shaft_right,
                      stroke_color=INK, stroke_width=2.5)
        # horizontal top cap
        top_cap = Line(shaft_top + shaft_left, shaft_top + shaft_right,
                       stroke_color=INK, stroke_width=2.5)
        shaft_grp = VGroup(wall_l, wall_r, top_cap)
        self.play(Create(shaft_grp), run_time=0.7)

        # Figure at bottom of shaft (simple dot + line)
        figure_pos = shaft_bottom + LEFT * 1.2 + UP * 0.4
        figure_head = Dot(radius=0.18, color=INK).move_to(figure_pos + UP * 0.35)
        figure_body = Line(figure_pos + UP * 0.18, figure_pos + DOWN * 0.22,
                           stroke_color=INK, stroke_width=3)
        figure = VGroup(figure_head, figure_body)
        self.play(FadeIn(figure), run_time=0.4)

        # Stroke labels — "one more retry", "one more check"
        stroke_labels = [
            ("one more retry",  UP * 0.5),
            ("one more check",  UP * 1.2),
            ("one more retry",  UP * 1.9),
        ]
        for txt, offset in stroke_labels:
            t = Text(txt, font=SERIF, color=CRIMSON, font_size=17, slant=ITALIC)
            t.move_to(shaft_right + RIGHT * 0.3 + shaft_bottom + offset)
            arr = Arrow(
                shaft_right + shaft_bottom + offset + LEFT * 0.05,
                shaft_right + shaft_bottom + offset + LEFT * 0.05 + LEFT * 0.4,
                stroke_color=CRIMSON, stroke_width=1.5, tip_length=0.14,
                buff=0,
            )
            self.play(FadeIn(t, shift=RIGHT * 0.1), Create(arr), run_time=0.55)
            self.wait(0.15)

        # Main caption (right side)
        cap_lines = VGroup(
            Text("from the inside,", font=SERIF, color=INK, font_size=24),
            Text("every next step looks reasonable.", font=SERIF, color=INK, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        cap_lines.move_to(RIGHT * 3.0 + UP * 0.5)
        self.play(FadeIn(cap_lines, shift=UP * 0.1), run_time=0.8)
        self.wait(0.4)

        # Punchline
        punch = SerifLabel("the optimism is the symptom.", accent=CRIMSON, size=22)
        punch.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(6.3)


# ──────────────────────────────────────────────────────────
# B05 — MORE EFFORT, SAME SEAT (8s)
# Same digging figure; an arrow labelled "try harder" extends the shaft deeper.
# Caption: "more effort from the same vantage doesn't help — it digs."
# Keep stark: one accent (red) on the deepening shaft.
# ──────────────────────────────────────────────────────────
class B05_SameSeat(Scene):
    def construct(self):
        section = LabelChip("SAME SEAT", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Pre-existing shaft (already established from B03 in the viewer's mind)
        shaft_left  = LEFT * 1.4
        shaft_right = RIGHT * 0.4
        shaft_top   = UP * 2.5

        wall_l = Line(shaft_top + shaft_left, DOWN * 1.2 + shaft_left,
                      stroke_color=INK, stroke_width=2.5)
        wall_r = Line(shaft_top + shaft_right, DOWN * 1.2 + shaft_right,
                      stroke_color=INK, stroke_width=2.5)
        top_cap = Line(shaft_top + shaft_left, shaft_top + shaft_right,
                       stroke_color=INK, stroke_width=2.5)
        self.play(Create(VGroup(wall_l, wall_r, top_cap)), run_time=0.5)

        # Figure at bottom
        fig_pos = DOWN * 0.9 + LEFT * 0.5
        fig_head = Dot(radius=0.18, color=INK).move_to(fig_pos + UP * 0.35)
        fig_body = Line(fig_pos + UP * 0.18, fig_pos + DOWN * 0.22,
                        stroke_color=INK, stroke_width=3)
        self.play(FadeIn(VGroup(fig_head, fig_body)), run_time=0.3)

        # Arrow + label: "try harder" pushes the shaft deeper
        deeper_arrow = Arrow(
            DOWN * 1.2 + LEFT * 0.5,
            DOWN * 2.6 + LEFT * 0.5,
            stroke_color=CRIMSON, stroke_width=3, tip_length=0.22, buff=0,
        )
        deeper_lbl = Text("try harder", font=DISPLAY, color=CRIMSON,
                          font_size=20, weight=BOLD)
        deeper_lbl.next_to(deeper_arrow, RIGHT, buff=0.2)

        # Shaft extension (the shaft growing down with the arrow)
        ext_l = Line(DOWN * 1.2 + shaft_left, DOWN * 2.6 + shaft_left,
                     stroke_color=INK, stroke_width=2.5)
        ext_r = Line(DOWN * 1.2 + shaft_right, DOWN * 2.6 + shaft_right,
                     stroke_color=INK, stroke_width=2.5)

        self.play(
            GrowArrow(deeper_arrow),
            FadeIn(deeper_lbl),
            Create(ext_l),
            Create(ext_r),
            run_time=0.8,
        )
        self.wait(0.3)

        # Caption
        caption = SerifLabel("more effort from the same vantage doesn't help — it digs.",
                             accent=CRIMSON, size=20)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(3.3)


# ──────────────────────────────────────────────────────────
# B06 — THE HUMAN HEARS A WRONG NOTE (17s)
# Conductor silhouette (callback to video 1) pausing.
# A single red "?" note rises from the orchestra.
# Caption: "this is taking far too long for a video this simple."
# Restraint — echoes the conductor beat from video 1.
# ──────────────────────────────────────────────────────────
class B06_WrongNote(Scene):
    def construct(self):
        # Slightly warm dark background echoes the V1 conductor hero
        self.camera.background_color = "#FFFFFF"

        section = LabelChip("THE CONDUCTOR", accent=INK, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Baton — the conductor's instrument (minimal: a line)
        baton = Line(LEFT * 2.0, RIGHT * 2.0,
                     stroke_color=INK, stroke_width=5)
        baton.move_to(UP * 1.4)
        self.play(Create(baton), run_time=0.6)
        self.wait(0.2)

        # Conductor silhouette: a rounded stick figure
        head = Circle(radius=0.32, fill_color=INK, fill_opacity=1,
                      stroke_width=0).move_to(UP * 0.5)
        body = Line(UP * 0.18, DOWN * 0.7, stroke_color=INK, stroke_width=4)
        arms = Line(LEFT * 0.55 + DOWN * 0.1, RIGHT * 0.55 + DOWN * 0.1,
                    stroke_color=INK, stroke_width=3)
        conductor = VGroup(head, body, arms)
        conductor.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(conductor, scale=0.9), run_time=0.5)

        # Orchestra "line" (simple horizontal staff)
        staff = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=INK, stroke_width=1.2)
        staff.to_edge(DOWN, buff=1.4)
        self.play(Create(staff), run_time=0.4)

        # Red "?" note rises from the orchestra — wrong note
        note_q = Text("?", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)
        note_q.move_to(staff.get_center() + LEFT * 0.5 + DOWN * 0.1)
        self.play(
            note_q.animate.shift(UP * 1.8),
            FadeIn(note_q),
            run_time=0.9,
        )
        self.wait(0.4)

        # Caption — the human's judgment
        cap1 = Text("this is taking far too long", font=SERIF, color=INK, font_size=24)
        cap2 = Text("for a video this simple.", font=SERIF, color=INK, font_size=24)
        captions = VGroup(cap1, cap2).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        captions.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(captions, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)

        # Subtext — the conductor's role
        sub = SerifLabel("you don't need to know what's wrong to know that something is.",
                         accent=CRIMSON, size=19)
        sub.next_to(captions, UP, buff=0.3)
        self.play(FadeIn(sub), run_time=0.6)
        self.wait(6.5)


# ──────────────────────────────────────────────────────────
# B07 — A DIFFERENT SEAT SEES THE WHOLE BOARD (18s)
# Split frame.
# LEFT: tunnelled agent boxed inside one narrow terminal (can only see its render).
# RIGHT: Cowork positioned outside, looking down at the WHOLE repo tree.
# Teal on the outside view.
# ──────────────────────────────────────────────────────────
class B07_DifferentSeat(Scene):
    def construct(self):
        section = LabelChip("A DIFFERENT SEAT", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # ─── LEFT: stuck agent in a narrow terminal box ───
        left_lbl = SerifLabel("stuck agent", accent=CRIMSON, size=22)
        left_lbl.move_to(LEFT * 3.2 + UP * 2.4)
        self.play(FadeIn(left_lbl), run_time=0.4)

        term_header = Text("$ npx remotion render … &", font=MONO,
                           color=WHITE, font_size=14)
        term_body   = VGroup(
            Text("waiting…", font=MONO, color=SLATE, font_size=14),
            Text("just a couple more minutes.", font=MONO, color=SLATE, font_size=14),
            Text("…", font=MONO, color=SLATE, font_size=14),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        term_content = VGroup(term_header, term_body).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        term_box = surround_box(term_content, buff=0.25,
                                fill_color="#111111", stroke_color=CRIMSON, stroke_width=2)
        term_grp = VGroup(term_box, term_content)
        term_grp.move_to(LEFT * 3.2 + DOWN * 0.4)
        if term_grp.width > 5.2:
            term_grp.scale_to_fit_width(5.2)

        caption_l = Text("can only see its own render", font=SERIF,
                         color=CRIMSON, font_size=17, slant=ITALIC)
        caption_l.next_to(term_grp, DOWN, buff=0.3)
        if caption_l.width > 5.2:
            caption_l.scale_to_fit_width(5.2)

        self.play(FadeIn(term_grp), run_time=0.6)
        self.play(FadeIn(caption_l), run_time=0.4)
        self.wait(0.5)

        # ─── RIGHT: Cowork reading the whole repo tree ───
        right_lbl = SerifLabel("Cowork", accent=ACCENT_TEAL, size=22)
        right_lbl.move_to(RIGHT * 3.2 + UP * 2.4)
        self.play(FadeIn(right_lbl), run_time=0.4)

        # Repo tree showing the full picture
        tree_items = [
            ("mp3/   15 files",    "← narration done",   ACCENT_TEAL),
            ("manim/ 9 files",     "← concept beats done", ACCENT_TEAL),
            ("media/ (empty)",     "← 6 beats stuck",    CRIMSON),
        ]
        tree_rows = VGroup()
        for path, note, color in tree_items:
            p = Text(path, font=MONO, color=INK, font_size=16)
            n = Text(note, font=MONO, color=color, font_size=16)
            row = VGroup(p, n).arrange(RIGHT, buff=0.3)
            if row.width > 5.6:
                row.scale_to_fit_width(5.6)
            tree_rows.add(row)
        tree_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        tree_box = surround_box(tree_rows, buff=0.28,
                                fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2)
        tree_grp = VGroup(tree_box, tree_rows)
        tree_grp.move_to(RIGHT * 3.2 + DOWN * 0.2)
        if tree_grp.width > 5.8:
            tree_grp.scale_to_fit_width(5.8)

        caption_r = Text("sees the whole board in one look", font=SERIF,
                         color=ACCENT_TEAL, font_size=17, slant=ITALIC)
        caption_r.next_to(tree_grp, DOWN, buff=0.3)
        if caption_r.width > 5.8:
            caption_r.scale_to_fit_width(5.8)

        self.play(FadeIn(tree_grp), run_time=0.7)
        self.play(FadeIn(caption_r), run_time=0.4)
        self.wait(8.5)


# ──────────────────────────────────────────────────────────
# B08 — NO SUNK COST (11s)
# Balance/scale: stuck agent clutching "1 hour invested" (heavy, red);
# Cowork holding the failing approach loosely (light, teal).
# Caption: "it hadn't spent an hour on that path, so it could just abandon it."
# ──────────────────────────────────────────────────────────
class B08_NoSunkCost(Scene):
    def construct(self):
        section = LabelChip("NO SUNK COST", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Pivot point of the scale
        pivot = Dot(radius=0.1, color=INK).move_to(ORIGIN + UP * 0.2)
        pivot_stand = Line(ORIGIN + UP * 0.2, ORIGIN + DOWN * 1.0,
                           stroke_color=INK, stroke_width=3)
        base = Line(LEFT * 0.6 + DOWN * 1.0, RIGHT * 0.6 + DOWN * 1.0,
                    stroke_color=INK, stroke_width=3)
        self.play(Create(VGroup(pivot_stand, base, pivot)), run_time=0.5)

        # Balance beam — tilted: left (stuck) is heavier
        beam = Line(LEFT * 3.5 + UP * 0.2 + DOWN * 0.4, RIGHT * 3.5 + UP * 0.2 + UP * 0.3,
                    stroke_color=INK, stroke_width=3)
        beam.move_to(ORIGIN + UP * 0.2)
        self.play(Create(beam), run_time=0.4)

        # LEFT pan — heavy (stuck agent, CRIMSON)
        left_pan_pos = LEFT * 3.5 + DOWN * 0.2
        pan_l = Circle(radius=0.7, stroke_color=CRIMSON, stroke_width=2.5,
                       fill_opacity=0).move_to(left_pan_pos)
        hour_txt = Text("1 hour", font=DISPLAY, color=CRIMSON, font_size=18, weight=BOLD)
        invested_txt = Text("invested", font=SERIF, color=CRIMSON, font_size=16)
        left_label = VGroup(hour_txt, invested_txt).arrange(DOWN, buff=0.08)
        left_label.move_to(left_pan_pos)
        left_agent = SerifLabel("stuck agent", accent=CRIMSON, size=18)
        left_agent.next_to(pan_l, UP, buff=0.28)

        self.play(FadeIn(pan_l), FadeIn(left_label), FadeIn(left_agent), run_time=0.6)

        # RIGHT pan — light (Cowork, teal)
        right_pan_pos = RIGHT * 3.5 + UP * 0.5
        pan_r = Circle(radius=0.55, stroke_color=ACCENT_TEAL, stroke_width=2,
                       fill_opacity=0, stroke_opacity=0.7).move_to(right_pan_pos)
        drop_txt = Text("drop it", font=SERIF, color=ACCENT_TEAL,
                        font_size=17, slant=ITALIC)
        drop_txt.move_to(right_pan_pos)
        right_agent = SerifLabel("Cowork", accent=ACCENT_TEAL, size=18)
        right_agent.next_to(pan_r, UP, buff=0.22)

        self.play(FadeIn(pan_r), FadeIn(drop_txt), FadeIn(right_agent), run_time=0.6)
        self.wait(0.4)

        # Caption
        caption = SerifLabel(
            "no investment → just abandon it.", accent=ACCENT_TEAL, size=20)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.9)


# ──────────────────────────────────────────────────────────
# B10 — PIPELINE WAS NEVER BROKEN (15s)
# Two rows: "video 1 — same Remotion components → ✓ rendered" (teal)
#           "video 2 — same components → stuck" (red)
# Bracket joining them: "so the pipeline was never broken."
# Conclusion stamp: "not a bug to hunt — a wrong approach to drop."
# ──────────────────────────────────────────────────────────
class B10_NeverBroken(Scene):
    def construct(self):
        section = LabelChip("NEVER BROKEN", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        def make_row(vid, status, color):
            vid_t   = Text(vid, font=MONO, color=INK, font_size=21)
            arrow   = Text("→", font=MONO, color=color, font_size=21)
            status_t = Text(status, font=MONO, color=color, font_size=21, weight=BOLD)
            row = VGroup(vid_t, arrow, status_t).arrange(RIGHT, buff=0.3)
            if row.width > 9.5:
                row.scale_to_fit_width(9.5)
            box = surround_box(row, buff=0.22,
                               fill_color=GROUND, stroke_color=color, stroke_width=2)
            return VGroup(box, row)

        row1 = make_row("video 1 — same Remotion components", "✓  rendered",   ACCENT_TEAL)
        row2 = make_row("video 2 — same components",          "stuck",         CRIMSON)

        rows = VGroup(row1, row2).arrange(DOWN, buff=0.35)
        rows.move_to(UP * 0.6)

        self.play(FadeIn(row1, shift=RIGHT * 0.1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(row2, shift=RIGHT * 0.1), run_time=0.6)
        self.wait(0.4)

        # Bracket — the bridge showing same components both times
        brace_txt = Text("so the pipeline was never broken.", font=SERIF,
                         color=INK, font_size=22)
        brace_box = surround_box(brace_txt, buff=0.22,
                                 fill_color=GROUND, stroke_color=INK, stroke_width=1.5)
        brace_grp = VGroup(brace_box, brace_txt)
        brace_grp.next_to(rows, DOWN, buff=0.45)
        self.play(FadeIn(brace_grp, shift=UP * 0.1), run_time=0.6)
        self.wait(0.3)

        # Conclusion stamp
        stamp_txt = Text("not a bug to hunt — a wrong approach to drop.",
                         font=SERIF, color=CRIMSON, font_size=20)
        if stamp_txt.width > 10.5:
            stamp_txt.scale_to_fit_width(10.5)
        stamp_txt.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(stamp_txt), run_time=0.6)
        self.wait(6.5)


# ──────────────────────────────────────────────────────────
# B11 — THE HELPER IT NEVER USED (12s)
# A file sitting in plain sight: "runtime/scripts/remotion_scenes.py"
# A spotlight lands on it.
# The stuck agent's hand-rolled "npx … &" scribble is crossed out beside it.
# Caption: "the tool was right there the whole time."
# ──────────────────────────────────────────────────────────
class B11_HelperRightThere(Scene):
    def construct(self):
        section = LabelChip("THE TOOL WAS RIGHT THERE", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # File box — sitting in the center
        file_name = Text("runtime/scripts/remotion_scenes.py",
                         font=MONO, color=INK, font_size=22, weight=BOLD)
        file_desc = Text("renders each beat · foreground · one at a time",
                         font=MONO, color=ACCENT_TEAL, font_size=18)
        file_content = VGroup(file_name, file_desc).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        if file_content.width > 10.5:
            file_content.scale_to_fit_width(10.5)
        file_box = surround_box(file_content, buff=0.32,
                                fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=3)
        file_grp = VGroup(file_box, file_content)
        file_grp.move_to(UP * 0.8)
        self.play(FadeIn(file_grp, scale=0.9), run_time=0.7)

        # Spotlight: a ring around the file
        spot = SurroundingRectangle(file_grp, buff=0.18,
                                    color=ACCENT_TEAL, stroke_width=4)
        self.play(Create(spot), run_time=0.6)
        self.wait(0.3)

        # The crossed-out improvised command
        wrong_cmd  = Text("npx remotion render … &", font=MONO, color=CRIMSON, font_size=20)
        wrong_box  = auto_box(wrong_cmd, h_pad=0.2, v_pad=0.14,
                              fill_color="#FFF0F0", stroke_color=CRIMSON, stroke_width=2)
        wrong_grp  = VGroup(wrong_box, wrong_cmd)
        wrong_grp.next_to(file_grp, DOWN, buff=0.5)

        strikethrough = Line(
            wrong_grp.get_left() + LEFT * 0.05,
            wrong_grp.get_right() + RIGHT * 0.05,
            stroke_color=CRIMSON, stroke_width=5,
        )
        strikethrough.move_to(wrong_grp)

        self.play(FadeIn(wrong_grp), run_time=0.5)
        self.play(Create(strikethrough), run_time=0.5)
        self.wait(0.3)

        # Caption
        caption = SerifLabel("the tool was right there the whole time.",
                             accent=INK, size=20)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.8)


# ──────────────────────────────────────────────────────────
# B13 — VERIFY BY LOOKING (18s)
# Terminal green "ok ✓" on the LEFT.
# Arrow to a rendered FRAME on the RIGHT with the WRONG text:
#   terminal titled "PHOTOELECTRIC EFFECT", CTA reading "cancer-biology".
# A magnifier over the frame.
# Caption: "the tool said ok; the screen said otherwise. Pull the frame and look."
# ──────────────────────────────────────────────────────────
class B13_VerifyByLooking(Scene):
    def construct(self):
        section = LabelChip("VERIFY BY LOOKING", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Divider
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_color=HAIRLINE, stroke_width=2)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # ── LEFT: terminal showing green "ok" ──
        term_lbl = Text("the tool said:", font=SERIF, color=SLATE,
                        font_size=18, slant=ITALIC)
        term_lbl.move_to(LEFT * 3.2 + UP * 2.3)
        ok_text = Text("ok ✓", font=MONO, color=ACCENT_TEAL,
                       font_size=38, weight=BOLD)
        ok_box = surround_box(ok_text, buff=0.32,
                              fill_color="#F0FAF6", stroke_color=ACCENT_TEAL, stroke_width=3)
        ok_grp = VGroup(ok_box, ok_text)
        ok_grp.move_to(LEFT * 3.2 + UP * 0.5)
        self.play(FadeIn(term_lbl), FadeIn(ok_grp, scale=0.9), run_time=0.6)

        # Arrow pointing right
        mid_arrow = Arrow(
            LEFT * 0.9, RIGHT * 0.9,
            stroke_color=INK, stroke_width=2.5, tip_length=0.2,
        )
        mid_arrow.move_to(ORIGIN + DOWN * 0.0)
        self.play(GrowArrow(mid_arrow), run_time=0.5)

        # ── RIGHT: rendered frame with WRONG text ──
        wrong_lbl = Text("the screen said:", font=SERIF, color=SLATE,
                         font_size=18, slant=ITALIC)
        wrong_lbl.move_to(RIGHT * 3.2 + UP * 2.3)

        frame_title = Text("PHOTOELECTRIC EFFECT", font=MONO,
                           color=CRIMSON, font_size=16, weight=BOLD)
        frame_body  = Text("cancer-biology", font=MONO, color=CRIMSON, font_size=14)
        frame_hint  = Text("(another video's defaults)", font=SERIF, color=SLATE,
                           font_size=13, slant=ITALIC)
        frame_content = VGroup(frame_title, frame_body, frame_hint)
        frame_content.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        frame_box = surround_box(frame_content, buff=0.28,
                                 fill_color="#FFF5F5", stroke_color=CRIMSON, stroke_width=2)
        frame_grp = VGroup(frame_box, frame_content)
        frame_grp.move_to(RIGHT * 3.2 + UP * 0.5)
        if frame_grp.width > 5.2:
            frame_grp.scale_to_fit_width(5.2)

        self.play(FadeIn(wrong_lbl), FadeIn(frame_grp), run_time=0.6)
        self.wait(0.3)

        # Magnifier circle over the wrong frame (emphasizes "look at it")
        magnifier = Circle(radius=0.8, stroke_color=INK, stroke_width=3,
                           fill_opacity=0)
        magnifier.move_to(RIGHT * 3.2 + UP * 0.8)
        mag_handle = Line(magnifier.get_bottom() + DOWN * 0.1,
                          magnifier.get_bottom() + DOWN * 0.6,
                          stroke_color=INK, stroke_width=3)
        mag_handle.shift(RIGHT * 0.5)
        self.play(Create(magnifier), Create(mag_handle), run_time=0.6)
        self.wait(0.5)

        # Caption
        cap_lines = VGroup(
            Text("'ok' from the tool is not the same as correct on the screen.",
                 font=SERIF, color=INK, font_size=20),
            Text("pull the frame and look.", font=SERIF, color=CRIMSON,
                 font_size=20, slant=ITALIC),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        if cap_lines.width > 12.5:
            cap_lines.scale_to_fit_width(12.5)
        cap_lines.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(cap_lines, shift=UP * 0.1), run_time=0.7)
        self.wait(7.5)


# ──────────────────────────────────────────────────────────
# B14 — THE LESSON — HERO BEAT (20s)
# Center title "A SECOND SET OF EYES" in EB Garamond.
# Three plain marks resolving in:
#   "any single agent can tunnel"
#   "a different seat + no sunk cost sees it"
#   "the human calls for it"
# End on the conductor callback — you heard it and asked.
# Teal as the one kept/good accent.
# ──────────────────────────────────────────────────────────
class B14_TheLesson(Scene):
    def construct(self):
        # Dark canvas — hero beats invert
        self.camera.background_color = "#2A1A0E"

        # Central title in EB Garamond — the lesson's name
        title = Text("A SECOND SET OF EYES", font=SERIF, color=WHITE,
                     font_size=52, weight=BOLD)
        title.move_to(UP * 1.8)
        self.play(Write(title), run_time=1.2)

        # Teal accent underline
        underline = Line(
            title.get_corner(DL) + DOWN * 0.1,
            title.get_corner(DR) + DOWN * 0.1,
            stroke_color=ACCENT_TEAL, stroke_width=4,
        )
        self.play(Create(underline), run_time=0.5)
        self.wait(0.4)

        # Three marks — resolving one at a time
        marks_data = [
            ("any single agent can tunnel",          CRIMSON),
            ("a different seat + no sunk cost sees it", WHITE),
            ("the human calls for it",               ACCENT_TEAL),
        ]
        marks = VGroup()
        for text, color in marks_data:
            bullet = Text("·", font=SERIF, color=ACCENT_TEAL, font_size=30)
            line   = Text(text, font=SERIF, color=color, font_size=26)
            row = VGroup(bullet, line).arrange(RIGHT, buff=0.3)
            if row.width > 11.5:
                row.scale_to_fit_width(11.5)
            marks.add(row)
        marks.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        marks.move_to(DOWN * 0.4)

        for mark in marks:
            self.play(FadeIn(mark, shift=UP * 0.12), run_time=0.65)
            self.wait(0.35)

        self.wait(0.5)

        # Conductor callback — the closer
        # Echo of the V1 conductor: a thin horizontal baton line at the bottom
        baton = Line(LEFT * 3.5, RIGHT * 3.5,
                     stroke_color=WHITE, stroke_width=4, stroke_opacity=0.45)
        baton.to_edge(DOWN, buff=0.9)

        coda_text = Text("you heard it · and asked · that is conducting too.",
                         font=SERIF, color=ACCENT_TEAL, font_size=20)
        coda_text.to_edge(DOWN, buff=0.4)
        if coda_text.width > 13.0:
            coda_text.scale_to_fit_width(13.0)

        self.play(Create(baton), FadeIn(coda_text, shift=UP * 0.1), run_time=0.8)
        self.wait(8.5)
