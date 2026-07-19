"""vox_scenes.py — Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten
(vox-format-credibility, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT beat whose source is 'own'.
B02 and B10 are STILL (ai) slots — compiled as slates.

Color law: TEAL #1F6F5C = correctly read / verified value
           CRIMSON #BF3339 = wrong extraction / silent error
           GOLD #F5D061 = editor's-pen highlight fill only, once in B08
Two accents max — never swapped mid-film.

Exclusions honored: NO OCR/vision-model architecture, NO schema walkthrough,
NO verification-checklist, NO invoices, NO hallucination taxonomy.

Gate B: every zero-width stroke is also zero-opacity.
"""
import json
import os
import sys
import pathlib

# ---- beat durations (populated after audio lock) ----
_bs_path = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs_path))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np


# ---------------------------------------------------------------- helpers

CELL_W, CELL_H = 2.8, 0.7

def _cell(value, border_color=INK, bg_alpha=0.0):
    """A single spreadsheet cell rectangle with a text value inside."""
    rect = Rectangle(width=CELL_W, height=CELL_H)
    rect.set_fill(WHITE, bg_alpha).set_stroke(border_color, 1.6)
    label = Text(value, font="Montserrat", color=INK, font_size=28)
    if label.width > CELL_W * 0.85:
        label.scale_to_fit_width(CELL_W * 0.85)
    label.move_to(rect)
    return VGroup(rect, label)


def _box(label_text, color=INK, w=3.2, h=1.0):
    """A labeled process box for the pipeline diagrams."""
    rect = Rectangle(width=w, height=h)
    rect.set_fill(color, 0.10).set_stroke(color, 2.0)
    txt = Text(label_text, font="Montserrat", color=color, font_size=22)
    if txt.width > w * 0.88:
        txt.scale_to_fit_width(w * 0.88)
    txt.move_to(rect)
    return VGroup(rect, txt)


def _row_bar(color=INK, w=4.0, h=0.22):
    """A single spreadsheet-row bar."""
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1.0).set_stroke(width=0, opacity=0)
    return r


# ============================================================ scenes

class B01_Title(Scene):
    """COLD OPEN — title card with CLAUDE COWORK eyebrow."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why a Perfect-Looking Spreadsheet", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("Can Be Off by a Factor of Ten", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14,
                 t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    """THE QUESTION — gap formula on screen."""
    def construct(self):
        _quote_scene(
            self,
            "A pristine spreadsheet should mean correct data. "
            "This one is spotless and row 23 is wrong by ten times. Why?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_TwoCells(Scene):
    """THE PROBLEM — two identically formatted cells, different values."""
    def construct(self):
        total = DUR["B04"]

        src_cell = _cell("$34.20", border_color=TEAL)
        ext_cell = _cell("$342.00", border_color=CRIMSON)
        pair = VGroup(src_cell, ext_cell).arrange(RIGHT, buff=0.9)
        pair.move_to(UP * 0.3)

        src_lbl = LabelChip("SOURCE", accent=TEAL, size=22)
        src_lbl.next_to(src_cell, UP, buff=0.25)
        ext_lbl = LabelChip("EXTRACTED", accent=CRIMSON, size=22)
        ext_lbl.next_to(ext_cell, UP, buff=0.25)

        note = SerifLabel("same format · different value", accent=INK, size=26)
        note.next_to(pair, DOWN, buff=0.45)

        self.play(
            FadeIn(src_cell, shift=RIGHT * 0.4),
            FadeIn(ext_cell, shift=LEFT * 0.4),
            run_time=0.9,
        )
        self.play(FadeIn(src_lbl, shift=DOWN * 0.1),
                  FadeIn(ext_lbl, shift=DOWN * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.1))


class B05_TwoSteps(Scene):
    """THE PROBLEM — two-step pipeline: READ then FORMAT."""
    def construct(self):
        total = DUR["B05"]

        read_box = _box("READ THE\nDOCUMENT", INK, w=2.9, h=1.2)
        fmt_box = _box("WRITE THE\nTABLE", TEAL, w=2.9, h=1.2)
        pipeline = VGroup(read_box, fmt_box).arrange(RIGHT, buff=1.4)
        pipeline.move_to(UP * 0.2)

        arrow = Arrow(
            read_box.get_right(), fmt_box.get_left(),
            color=INK, buff=0.15, stroke_width=3,
        )

        check = Text("always", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        check.next_to(fmt_box, DOWN, buff=0.35)

        self.play(FadeIn(read_box, shift=RIGHT * 0.3), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(fmt_box, shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(check, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.2))


class B06_SectionMechanism(Scene):
    """SECTION CARD — THE MECHANISM."""
    def construct(self):
        total = DUR["B06"]
        head = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48)
        sub = Text("two separate steps", font=SERIF, color=TEAL, font_size=28,
                   slant=ITALIC)
        block = VGroup(head, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(block, scale=0.95), run_time=0.7)
        self.wait(max(0.3, total - 0.7))


class B07_StepFails(Scene):
    """THE MECHANISM — read step fails, format step still runs."""
    def construct(self):
        total = DUR["B07"]

        read_box = _box("READ THE\nDOCUMENT", CRIMSON, w=2.9, h=1.2)
        fmt_box = _box("WRITE THE\nTABLE", TEAL, w=2.9, h=1.2)
        pipeline = VGroup(read_box, fmt_box).arrange(RIGHT, buff=1.4)
        pipeline.move_to(UP * 0.4)

        arrow = Arrow(
            read_box.get_right(), fmt_box.get_left(),
            color=INK, buff=0.15, stroke_width=3,
        )

        fail_lbl = Text("X", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)
        fail_lbl.next_to(read_box, DOWN, buff=0.3)

        ok_lbl = Text("always", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        ok_lbl.next_to(fmt_box, DOWN, buff=0.3)

        out_cell = _cell("$342.00", border_color=CRIMSON)
        out_cell.next_to(fmt_box, RIGHT, buff=1.0)

        out_note = SerifLabel("clean cell", accent=CRIMSON, size=24)
        out_note.next_to(out_cell, DOWN, buff=0.3)

        self.play(
            FadeIn(read_box), FadeIn(fmt_box),
            GrowArrow(arrow), run_time=0.8,
        )
        self.play(FadeIn(fail_lbl, scale=0.7), run_time=0.5)
        self.play(FadeIn(ok_lbl), run_time=0.4)
        self.play(FadeIn(out_cell, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(out_note, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.6))


class B08_MerchantClone(Scene):
    """THE MECHANISM — Unknown Merchant cloned to 4 rows, GOLD sweep."""
    def construct(self):
        total = DUR["B08"]

        rows = VGroup(*[
            VGroup(
                Rectangle(width=4.2, height=0.38)
                .set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.0),
                Text("Unknown Merchant", font=DISPLAY, color=CRIMSON,
                     font_size=20),
            ).arrange(ORIGIN)
            for _ in range(4)
        ])
        rows.arrange(DOWN, buff=0.14).move_to(UP * 0.3)
        for g in rows:
            g[1].move_to(g[0])

        no_flag = SerifLabel("no flag · no asterisk", accent=INK, size=24)
        no_flag.next_to(rows, DOWN, buff=0.4)

        gold_bar = Rectangle(width=4.5, height=rows.height + 0.3)
        gold_bar.set_fill(GOLD, 0.0).set_stroke(width=0, opacity=0)
        gold_bar.move_to(rows.get_center())

        self.play(FadeIn(rows[0], shift=DOWN * 0.15), run_time=0.4)
        self.play(
            FadeIn(rows[1], shift=DOWN * 0.1),
            FadeIn(rows[2], shift=DOWN * 0.1),
            FadeIn(rows[3], shift=DOWN * 0.1),
            run_time=0.7,
        )
        self.add(gold_bar)
        self.play(gold_bar.animate.set_fill(GOLD, 0.28), run_time=0.7)
        self.play(FadeIn(no_flag, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.3))


class B09_KeyClaim(Scene):
    """THE MECHANISM — key claim quote."""
    def construct(self):
        _quote_scene(
            self,
            "Structure confers credibility the numbers have not earned.",
            "— the mechanism",
            None,
            "credibility",
            DUR["B09"],
        )


class B11_Example(Scene):
    """THE EXAMPLE — mini spreadsheet, row 23 error (illustrative)."""
    def construct(self):
        total = DUR["B11"]

        # 5 visible rows to represent the spreadsheet
        row_labels = ["Row 21", "Row 22", "Row 23", "Row 24", "Row 25"]
        row_values = ["$89.50", "$212.00", "$342.00", "$156.75", "$44.00"]
        row_colors = [INK, INK, CRIMSON, INK, INK]

        table = VGroup()
        for rl, rv, rc in zip(row_labels, row_values, row_colors):
            lbl = Text(rl, font=SERIF, color=INK, font_size=22)
            val = Text(rv, font="PT Mono", color=rc, font_size=26,
                       weight="BOLD" if rc == CRIMSON else "NORMAL")
            row_g = VGroup(lbl, val).arrange(RIGHT, buff=1.2)
            table.add(row_g)
        table.arrange(DOWN, buff=0.22).move_to(LEFT * 1.5 + UP * 0.2)

        # Align columns
        for row_g in table:
            row_g[0].align_to(table, LEFT)
            row_g[1].align_to(table[0][1], LEFT)

        # Highlight row 23 (index 2)
        highlight = Rectangle(width=4.5, height=0.42)
        highlight.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.2)
        highlight.move_to(table[2].get_center())

        # Source arrow
        source_val = Text("$34.20", font="PT Mono", color=TEAL, font_size=28,
                          weight="BOLD")
        source_val.move_to(RIGHT * 3.5 + table[2].get_center()[1] * UP)
        src_arrow = Arrow(
            table[2][1].get_right() + RIGHT * 0.15,
            source_val.get_left() + LEFT * 0.1,
            color=TEAL, buff=0.0, stroke_width=2.5,
        )
        src_lbl = Text("source", font=SERIF, color=TEAL, font_size=18,
                       slant=ITALIC)
        src_lbl.next_to(source_val, DOWN, buff=0.12)

        illus = SerifLabel("illustrative numbers", accent=INK, size=20)
        illus.to_corner(DL, buff=0.55)

        self.play(FadeIn(table, shift=UP * 0.1), run_time=0.8)
        self.play(FadeIn(highlight, scale=0.92), run_time=0.5)
        self.play(GrowArrow(src_arrow), FadeIn(source_val, shift=LEFT * 0.2),
                  run_time=0.6)
        self.play(FadeIn(src_lbl, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.5, total - 2.7))


class B12_SpotCheck(Scene):
    """THE EXAMPLE — 47 row-marks, 5 checked, 2 error, 42 unchecked."""
    def construct(self):
        total = DUR["B12"]

        # 47 small squares in a grid (7 cols x 7 rows = 49, trim to 47)
        n_total = 47
        n_checked = 5
        n_error = 2  # of the 5 checked, 2 are errors
        per_row = 7
        sq_size = 0.28
        sq_gap = 0.14

        squares = VGroup()
        for i in range(n_total):
            sq = Square(sq_size)
            sq.set_fill(INK, 0.15).set_stroke(INK, 1.0)
            sq.move_to(
                RIGHT * (i % per_row) * (sq_size + sq_gap)
                + DOWN * (i // per_row) * (sq_size + sq_gap)
            )
            squares.add(sq)
        squares.move_to(UP * 0.4)

        # Legend
        ok_sq = Square(sq_size).set_fill(TEAL, 0.7).set_stroke(TEAL, 1.0)
        ok_lbl = Text("checked (3)", font=SERIF, color=INK, font_size=22)
        err_sq = Square(sq_size).set_fill(CRIMSON, 0.8).set_stroke(CRIMSON, 1.0)
        err_lbl = Text("error (2)", font=SERIF, color=CRIMSON, font_size=22)
        ok_g = VGroup(ok_sq, ok_lbl).arrange(RIGHT, buff=0.2)
        err_g = VGroup(err_sq, err_lbl).arrange(RIGHT, buff=0.2)
        legend = VGroup(ok_g, err_g).arrange(RIGHT, buff=0.7)
        legend.next_to(squares, DOWN, buff=0.5)

        illus = SerifLabel("illustrative", accent=INK, size=20)
        illus.to_corner(DL, buff=0.55)

        self.play(lrows := squares.animate.scale(1.0), run_time=0.01)
        self.play(FadeIn(squares), run_time=0.5)

        # Tick 5 checked squares (indices 0-4): 2 error, 3 ok
        for idx in range(n_checked):
            color = CRIMSON if idx < n_error else TEAL
            self.play(squares[idx].animate.set_fill(color, 0.8),
                      run_time=0.18)

        self.play(FadeIn(legend, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - (0.5 + n_checked * 0.18 + 1.3)))


class B13_Endcard(Scene):
    """RECAP — endcard: Clean format does not mean correct data. CLAUDE COWORK."""
    def construct(self):
        total = DUR["B13"]
        topic = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        main = Text("Clean format does not mean correct data.",
                    font=SERIF, color=INK, font_size=42, weight=BOLD)
        if main.width > 11.0:
            main.scale_to_fit_width(11.0)
        u = Line(main.get_corner(DL) + DOWN * 0.14,
                 main.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(main, u).move_to(ORIGIN)
        topic.next_to(block, UP, buff=0.6)
        self.play(FadeIn(topic, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(main, shift=UP * 0.1), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 1.5))
