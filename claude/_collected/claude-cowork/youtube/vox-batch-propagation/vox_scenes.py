import sys, pathlib, os, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {}
try:
    _data = json.load(open(os.path.join(os.path.dirname(__file__), "beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why 200 Tiny, Reversible Renames", font=SERIF, color=INK, font_size=38, weight=BOLD)
        t2 = Text("Add Up to One You Can't Undo", font=SERIF, color=INK, font_size=38, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Where is your mental map?",
            "— the question this film answers",
            None,
            "map",
            DUR["B03"],
        )


class B04_OneRename(Scene):
    def construct(self):
        total = DUR["B04"]
        old_box = RoundedRectangle(width=2.4, height=0.85, corner_radius=0.1,
                                   color=TEAL, fill_opacity=0.1)
        old_box.set_stroke(color=TEAL, width=2, opacity=1)
        old_txt = Text("scan0012.pdf", font=MONO, color=TEAL, font_size=20)
        old_grp = VGroup(old_box, old_txt).move_to(LEFT * 2.8)
        new_box = RoundedRectangle(width=2.4, height=0.85, corner_radius=0.1,
                                   color=CRIMSON, fill_opacity=0.1)
        new_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        new_txt = Text("consent-001.pdf", font=MONO, color=CRIMSON, font_size=20)
        new_grp = VGroup(new_box, new_txt).move_to(RIGHT * 2.8)
        arrow = Arrow(old_grp.get_right(), new_grp.get_left(), buff=0.1,
                      color=SLATE, stroke_width=2)
        rev_lbl = LabelChip("REVERSIBLE", accent=TEAL, size=18)
        rev_lbl.next_to(arrow, DOWN, buff=0.3)
        self.play(FadeIn(old_grp, shift=UP * 0.1), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(new_grp, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(rev_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 1.6))


class B05_Batch(Scene):
    def construct(self):
        total = DUR["B05"]
        cols, rows = 8, 3
        before_tiles = VGroup()
        after_tiles = VGroup()
        for r in range(rows):
            for c in range(cols):
                b = Rectangle(width=0.55, height=0.38, color=TEAL, fill_opacity=0.15)
                b.set_stroke(color=TEAL, width=1, opacity=1)
                before_tiles.add(b)
                a = Rectangle(width=0.55, height=0.38, color=CRIMSON, fill_opacity=0.15)
                a.set_stroke(color=CRIMSON, width=1, opacity=1)
                after_tiles.add(a)
        before_tiles.arrange_in_grid(rows=rows, cols=cols, buff=0.08).move_to(LEFT * 3.2)
        after_tiles.arrange_in_grid(rows=rows, cols=cols, buff=0.08).move_to(RIGHT * 3.2)
        center_arrow = Arrow(LEFT * 0.8, RIGHT * 0.8, buff=0, color=SLATE, stroke_width=2)
        count_lbl = Text("200 files · 40 minutes", font=MONO, color=CRIMSON, font_size=20)
        count_lbl.next_to(VGroup(before_tiles, after_tiles), DOWN, buff=0.55)
        self.play(FadeIn(before_tiles, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(center_arrow), FadeIn(count_lbl), run_time=0.5)
        self.play(FadeIn(after_tiles, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.7))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("the before-state disappears", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_MentalMap(Scene):
    def construct(self):
        total = DUR["B07"]
        before_col = VGroup(*[
            Text(f"scan{1012 + i:04d}.pdf", font=MONO, color=TEAL, font_size=18)
            for i in range(5)
        ]).arrange(DOWN, buff=0.2).move_to(LEFT * 2.8 + UP * 0.3)
        after_col = VGroup(*[
            Text(f"file-{i+1:03d}.pdf", font=MONO, color=CRIMSON, font_size=18)
            for i in range(5)
        ]).arrange(DOWN, buff=0.2).move_to(RIGHT * 2.8 + UP * 0.3)
        map_lbl = Text("mental map", font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        map_lbl.next_to(before_col, UP, buff=0.3)
        wiped_lbl = Text("wiped", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        wiped_lbl.next_to(before_col, DOWN, buff=0.35)
        arrows = VGroup(*[
            Line(before_col[i].get_right() + RIGHT * 0.05,
                 after_col[i].get_left() + LEFT * 0.05,
                 color=SLATE, stroke_width=1)
            for i in range(5)
        ])
        for a in arrows:
            a.set_stroke(opacity=0.35)
        self.play(FadeIn(before_col, shift=RIGHT * 0.1), FadeIn(map_lbl), run_time=0.5)
        self.play(FadeIn(arrows), FadeIn(after_col, shift=LEFT * 0.1), run_time=0.5)
        self.play(FadeIn(wiped_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.5))


class B08_KeyClaim(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The batch is a single irreversible event, not two hundred small reversible ones.",
            "— the mechanism",
            None,
            "irreversible",
            DUR["B08"],
        )


class B09_Correspondence(Scene):
    def construct(self):
        total = DUR["B09"]
        old_names = ["scan0012.pdf", "scan0013.pdf", "final_v3.docx", "notes.txt"]
        new_names = ["scan-undated-001.pdf", "scan-undated-002.pdf", "???", "???"]
        old_col = VGroup(*[
            Text(n, font=MONO, color=TEAL, font_size=20) for n in old_names
        ]).arrange(DOWN, buff=0.32).move_to(LEFT * 2.6)
        new_col = VGroup(*[
            Text(n, font=MONO, color=CRIMSON, font_size=20) for n in new_names
        ]).arrange(DOWN, buff=0.32).move_to(RIGHT * 2.6)
        broken_arrows = VGroup()
        for i in range(len(old_names)):
            midx = (old_col[i].get_right()[0] + new_col[i].get_left()[0]) / 2
            midy = old_col[i].get_center()[1]
            q = Text("?", font=DISPLAY, color=SLATE, font_size=22)
            q.set_opacity(0.6)
            q.move_to([midx, midy, 0])
            broken_arrows.add(q)
        old_lbl = Text("before", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        old_lbl.next_to(old_col, UP, buff=0.3)
        new_lbl = Text("after", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        new_lbl.next_to(new_col, UP, buff=0.3)
        self.play(FadeIn(old_col, shift=RIGHT * 0.1), FadeIn(old_lbl), run_time=0.5)
        self.play(FadeIn(new_col, shift=LEFT * 0.1), FadeIn(new_lbl), run_time=0.5)
        self.play(FadeIn(broken_arrows, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.5))


class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]
        header = LabelChip("243 files · 40 minutes", accent=CRIMSON, size=20)
        header.move_to(UP * 2.3)
        before_box = RoundedRectangle(width=3.0, height=1.6, corner_radius=0.1,
                                      color=TEAL, fill_opacity=0)
        before_box.set_stroke(color=TEAL, width=2, opacity=1)
        before_lbl = Text("scan0012.pdf", font=MONO, color=TEAL, font_size=18)
        before_range = Text("through scan0019.pdf", font=MONO, color=TEAL, font_size=18)
        before_note = Text("(8 consent forms)", font=SERIF, color=TEAL, font_size=16, slant=ITALIC)
        before_note.set_opacity(0.7)
        before_content = VGroup(before_lbl, before_range, before_note).arrange(DOWN, buff=0.1)
        before_grp = VGroup(before_box, before_content).move_to(LEFT * 3.0 + DOWN * 0.3)
        after_box = RoundedRectangle(width=3.2, height=1.6, corner_radius=0.1,
                                     color=CRIMSON, fill_opacity=0)
        after_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        after_name = Text("scan-undated-001.pdf", font=MONO, color=CRIMSON, font_size=17)
        after_folder = Text("in Uncategorized-Scans/", font=SERIF, color=CRIMSON, font_size=16, slant=ITALIC)
        after_folder.set_opacity(0.8)
        after_content = VGroup(after_name, after_folder).arrange(DOWN, buff=0.12)
        after_grp = VGroup(after_box, after_content).move_to(RIGHT * 3.0 + DOWN * 0.3)
        rename_arrow = Arrow(before_grp.get_right(), after_grp.get_left(), buff=0.1,
                             color=CRIMSON, stroke_width=2.5)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.move_to(DOWN * 2.4)
        self.play(FadeIn(header, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(before_grp, shift=UP * 0.1), run_time=0.5)
        self.play(GrowArrow(rename_arrow), run_time=0.4)
        self.play(FadeIn(after_grp, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 2.1))


class B12_SearchFail(Scene):
    def construct(self):
        total = DUR["B12"]
        search_bar = RoundedRectangle(width=4.0, height=0.7, corner_radius=0.1,
                                      color=SLATE, fill_opacity=0)
        search_bar.set_stroke(color=SLATE, width=1.5, opacity=0.7)
        search_txt = Text("scan0012", font=MONO, color=SLATE, font_size=22)
        search_grp = VGroup(search_bar, search_txt).move_to(UP * 1.3)
        zero_lbl = Text("0 results", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        zero_lbl.next_to(search_grp, DOWN, buff=0.4)
        recovery = Text("2 hours to recover", font=SERIF, color=CRIMSON, font_size=24)
        recovery.next_to(zero_lbl, DOWN, buff=0.35)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.next_to(recovery, DOWN, buff=0.4)
        self.play(FadeIn(search_grp, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(zero_lbl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(recovery, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 1.8))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Two hundred reversible renames become one irreversible batch.",
            "— the example",
            None,
            "irreversible",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("The sum of two hundred reversible steps is not reversible.",
                    font=SERIF, color=INK, font_size=34, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
