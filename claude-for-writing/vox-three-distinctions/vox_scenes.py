"""vox_scenes.py — Three Questions That Catch Broken Causal Arguments
(vox-three-distinctions, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is own.
B02 and B12 are STILL · ai — no scenes here (they compile as slates).

Color law (teardown palette):
  CRIMSON = the collapsed/wrong reading (bad reasoning)
  TEAL    = the correct distinction / diagnostic pass (good reasoning)
  GOLD    = highlighter fill only, once per graphic, never text
  SLATE   = structural scaffolding

Gate B convention: every zero-width stroke is also zero-opacity.
Font-safe glyphs only: no arrows (->), no check marks, no not-equal (!=).
Use words and ASCII; middle-dot (·) is safe.

Exclusions honored: NO Toulmin, NO analogy, NO other five strategies.
"""
import sys
import json
import pathlib
import numpy as np

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

# ---------------------------------------------------------------- durations
DUR = {
    "B01": 10.0, "B03": 11.0, "B04": 11.0, "B05": 10.0,
    "B06": 13.0, "B07":  9.0, "B08": 13.0, "B09":  9.0,
    "B10": 13.0, "B11":  9.0, "B13": 12.0, "B14": 13.0,
    "B15": 14.0, "B16": 12.0, "B17": 10.0, "B18": 10.0,
}
try:
    _BS = json.load(
        open(pathlib.Path(__file__).with_name("beat_sheet.json"))
    )
    DUR.update({
        b["beat_id"]: float(
            b.get("actual_duration_s") or b.get("estimated_duration_s") or 9.0
        )
        for b in _BS["beats"]
    })
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _box(w, h, fill_color, fill_opacity=1.0, stroke_color=None,
         stroke_width=2.0):
    r = Rectangle(width=w, height=h)
    sc = stroke_color if stroke_color else fill_color
    r.set_fill(fill_color, fill_opacity)
    r.set_stroke(sc, stroke_width)
    return r


def _chain_node(label, accent=SLATE, w=2.4, h=0.7):
    """A single node in a causal chain."""
    box = _box(w, h, accent, fill_opacity=0.15, stroke_color=accent)
    txt = Text(label, font=DISPLAY, color=INK, font_size=22)
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box)
    return VGroup(box, txt)


def _diagnostic_box(question_text, filled=False, accent=TEAL, w=3.6, h=0.9):
    """A diagnostic question box, optionally pre-filled."""
    box = _box(w, h, accent if filled else SLATE,
               fill_opacity=0.12 if filled else 0.06,
               stroke_color=accent if filled else SLATE)
    if filled:
        txt = Text(question_text, font=SERIF, color=accent, font_size=21,
                   slant=ITALIC)
    else:
        txt = Text(question_text, font=SERIF, color=INK, font_size=21)
    if txt.width > w * 0.90:
        txt.scale_to_fit_width(w * 0.90)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """COLD OPEN — two-fact hook, title card."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("WRITING", font=DISPLAY, color=SLATE, font_size=20,
                   weight="MEDIUM")
        t1 = Text("Two facts. One summer.", font=DISPLAY, color=INK,
                  font_size=48, weight="MEDIUM")
        sub = Text("ice cream sales up  ·  drowning rates up  ·  same spike, same season.",
                   font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
        block = VGroup(t1, sub).arrange(DOWN, buff=0.35).move_to(UP * 0.15)
        u = Line(t1.get_corner(DL) + DOWN * 0.14,
                 t1.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2, color=CRIMSON)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.2))


class B03_QuestionCard(Scene):
    """THE QUESTION — named on screen and in narration."""
    def construct(self):
        total = DUR["B03"]
        q = Text("Three different things", font=DISPLAY, color=INK,
                 font_size=44, weight="MEDIUM")
        dash = Text("or the same thing?", font=SERIF, color=SLATE,
                    font_size=36, slant=ITALIC)
        sub = Text("why public discourse keeps collapsing the distinction",
                   font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        block = VGroup(q, dash).arrange(DOWN, buff=0.3).move_to(UP * 0.3)
        sub.next_to(block, DOWN, buff=0.5)
        u = Line(q.get_corner(DL) + DOWN * 0.12,
                 q.get_corner(DR) + DOWN * 0.12,
                 stroke_width=2, color=CRIMSON)
        self.play(FadeIn(q), Create(u), run_time=1.0)
        self.play(FadeIn(dash, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B04_ChainIntro(Scene):
    """THE PROBLEM — a causal chain builds left to right."""
    def construct(self):
        total = DUR["B04"]
        labels = ["Event A", "Event B", "Event C", "Event D"]
        nodes = [_chain_node(lbl) for lbl in labels]
        arrows = []
        for i in range(len(nodes) - 1):
            arr = Arrow(ORIGIN, RIGHT * 0.6, color=SLATE, stroke_width=3,
                        buff=0.0, max_tip_length_to_length_ratio=0.25)
            arrows.append(arr)

        chain = VGroup()
        for i, node in enumerate(nodes):
            chain.add(node)
            if i < len(arrows):
                chain.add(arrows[i])
        chain.arrange(RIGHT, buff=0.2).move_to(ORIGIN)

        eye = SerifLabel("a cause-and-effect chain", SLATE, size=24)
        eye.to_edge(UP, buff=0.8)

        caption = Text("each item causes the next", font=SERIF, color=SLATE,
                       font_size=22, slant=ITALIC)
        caption.next_to(chain, DOWN, buff=0.5)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(nodes[0], shift=RIGHT * 0.3), run_time=0.6)
        for i in range(len(arrows)):
            self.play(
                GrowArrow(arrows[i]),
                FadeIn(nodes[i + 1], shift=RIGHT * 0.3),
                run_time=0.55,
            )
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - (0.5 + 0.6 + len(arrows) * 0.55 + 0.5)))


class B05_SectionCard(Scene):
    """THE PROBLEM — section card: three checkpoints, three failure modes."""
    def construct(self):
        total = DUR["B05"]
        t1 = Text("Three checkpoints.", font=DISPLAY, color=INK,
                  font_size=46, weight="MEDIUM")
        t2 = Text("Three failure modes.", font=SERIF, color=SLATE,
                  font_size=36, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        u = Line(t1.get_corner(DL) + DOWN * 0.12,
                 t1.get_corner(DR) + DOWN * 0.12,
                 stroke_width=2, color=CRIMSON)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 1.6))


class B06_CorrVsCause(Scene):
    """THE MECHANISM 1 — correlation vs. causation.

    Two trend lines both spike. A direct CRIMSON arrow between them appears,
    then is struck out. Two TEAL arrows point to a shared hidden cause.
    """
    def construct(self):
        total = DUR["B06"]

        # Axes region (sketched, not full axes)
        ax_w, ax_h = 4.2, 2.0
        ax_orig = LEFT * 3.2 + DOWN * 0.4

        # Two trend bars representing rising summer values
        def _bar(x, h, color):
            b = Rectangle(width=0.32, height=h)
            b.set_fill(color, 0.7).set_stroke(width=0, opacity=0)
            b.align_to(ax_orig, DOWN)
            b.shift(RIGHT * x)
            return b

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        # ice cream values (arbitrary illustrative shape — peaks summer)
        ic_vals = [0.3, 0.35, 0.5, 0.7, 1.1, 1.5, 1.8, 1.6, 1.2, 0.7, 0.4, 0.3]
        # drowning values (same shape)
        dr_vals = [0.25, 0.28, 0.45, 0.65, 1.05, 1.45, 1.75, 1.55, 1.15, 0.65, 0.38, 0.28]

        scale = ax_h / 1.8
        gap = ax_w / 13.0
        ic_bars = VGroup(*[
            _bar(gap * (i + 0.4), ic_vals[i] * scale, SLATE)
            for i in range(12)
        ])
        dr_bars = VGroup(*[
            _bar(gap * (i + 0.4) + ax_w + 0.7, dr_vals[i] * scale, SLATE)
            for i in range(12)
        ])

        lbl_ic = SerifLabel("ice cream sales", SLATE, size=22)
        lbl_ic.next_to(ic_bars, UP, buff=0.25)
        lbl_dr = SerifLabel("drowning rate", SLATE, size=22)
        lbl_dr.next_to(dr_bars, UP, buff=0.25)

        eye = SerifLabel("checkpoint 1  ·  correlation vs. causation", SLATE, size=22)
        eye.to_edge(UP, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in ic_bars],
                        lag_ratio=0.04, run_time=1.0),
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in dr_bars],
                        lag_ratio=0.04, run_time=1.0),
        )
        self.play(FadeIn(lbl_ic), FadeIn(lbl_dr), run_time=0.6)
        self.wait(1.0)

        # CRIMSON spurious arrow between the two charts
        arr_bad = Arrow(
            ic_bars.get_right() + RIGHT * 0.1 + UP * 0.4,
            dr_bars.get_left() + LEFT * 0.1 + UP * 0.4,
            color=CRIMSON, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        bad_lbl = LabelChip("causes?", accent=CRIMSON, size=20)
        bad_lbl.next_to(arr_bad, UP, buff=0.1)
        self.play(GrowArrow(arr_bad), FadeIn(bad_lbl), run_time=0.8)
        self.wait(0.8)

        # Strike out the spurious arrow
        strike = Line(
            arr_bad.get_start(), arr_bad.get_end(),
            color=CRIMSON, stroke_width=6,
        )
        strike._qc_intentional = True  # deliberate strike through
        self.play(Create(strike), run_time=0.6)
        self.wait(0.5)

        # Hidden common cause: "summer heat" node above
        heat_node = _chain_node("summer heat", accent=TEAL, w=2.2, h=0.6)
        heat_node.move_to(UP * 2.4)
        arr_ic = Arrow(
            heat_node.get_bottom() + LEFT * 0.5,
            ic_bars.get_top() + RIGHT * 0.5,
            color=TEAL, stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )
        arr_dr = Arrow(
            heat_node.get_bottom() + RIGHT * 0.5,
            dr_bars.get_top() + LEFT * 0.5,
            color=TEAL, stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(FadeIn(heat_node, shift=DOWN * 0.2), run_time=0.7)
        self.play(GrowArrow(arr_ic), GrowArrow(arr_dr), run_time=0.8)
        self.wait(max(0.5, total - (0.5 + 1.0 + 0.6 + 1.0 + 0.8 + 0.8 + 0.5 + 0.6 + 0.5 + 0.7 + 0.8)))


class B07_DiagCard1(Scene):
    """MECHANISM — diagnostic card: what is the mechanism?"""
    def construct(self):
        total = DUR["B07"]
        chip = LabelChip("checkpoint 1", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.8)
        q = Text("What is the mechanism?", font=DISPLAY, color=INK,
                 font_size=46, weight="MEDIUM")
        u = Line(q.get_corner(DL) + DOWN * 0.14,
                 q.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2, color=TEAL)
        sub = Text("correlation vs. causation", font=SERIF, color=SLATE,
                   font_size=26, slant=ITALIC)
        sub.next_to(q, DOWN, buff=0.4)
        q.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(q), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B08_ProximalDistal(Scene):
    """MECHANISM 2 — proximate vs. distal.

    A vertical causal chain builds top to bottom for the Refugio spill.
    Brackets label 'distal' at top and 'proximate' at the rupture node.
    """
    def construct(self):
        total = DUR["B08"]

        steps = [
            ("regulatory failure", SLATE),
            ("aging pipeline", SLATE),
            ("corrosion", SLATE),
            ("rupture", CRIMSON),
            ("oil spill", INK),
            ("wildlife deaths", INK),
        ]
        nodes = [_chain_node(lbl, accent=col, w=2.8, h=0.62)
                 for lbl, col in steps]
        arrows_v = [
            Arrow(ORIGIN, DOWN * 0.35, color=SLATE, stroke_width=3,
                  buff=0.0, max_tip_length_to_length_ratio=0.3)
            for _ in range(len(nodes) - 1)
        ]
        chain = VGroup()
        for i, node in enumerate(nodes):
            chain.add(node)
            if i < len(arrows_v):
                chain.add(arrows_v[i])
        chain.arrange(DOWN, buff=0.08).move_to(ORIGIN + LEFT * 0.5)

        # Brackets
        distal_brace = Brace(VGroup(*nodes[:3]), LEFT, color=SLATE,
                             buff=0.2)
        distal_lbl = Text("distal", font=SERIF, color=SLATE,
                          font_size=22, slant=ITALIC)
        distal_lbl.next_to(distal_brace, LEFT, buff=0.15)

        proximate_brace = Brace(nodes[3], LEFT, color=CRIMSON, buff=0.2)
        proximate_lbl = Text("proximate", font=SERIF, color=CRIMSON,
                             font_size=22, slant=ITALIC)
        proximate_lbl.next_to(proximate_brace, LEFT, buff=0.15)

        eye = SerifLabel(
            "checkpoint 2  ·  proximate vs. distal  ·  Refugio 2015",
            SLATE, size=20,
        )
        eye.to_edge(UP, buff=0.7)

        self.play(FadeIn(eye), run_time=0.5)
        # Build chain top to bottom
        self.play(FadeIn(nodes[0], shift=DOWN * 0.2), run_time=0.5)
        for i in range(len(arrows_v)):
            self.play(
                GrowArrow(arrows_v[i]),
                FadeIn(nodes[i + 1], shift=DOWN * 0.2),
                run_time=0.45,
            )
        self.wait(0.5)
        self.play(FadeIn(distal_brace), FadeIn(distal_lbl), run_time=0.7)
        self.play(FadeIn(proximate_brace), FadeIn(proximate_lbl), run_time=0.7)
        self.wait(max(0.5, total - (0.5 + 0.5 + len(arrows_v) * 0.45 + 0.5 + 0.7 + 0.7)))


class B09_DiagCard2(Scene):
    """MECHANISM — diagnostic card: proximate or distal?"""
    def construct(self):
        total = DUR["B09"]
        chip = LabelChip("checkpoint 2", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.8)
        q = Text("Which cause are you invoking?", font=DISPLAY, color=INK,
                 font_size=40, weight="MEDIUM")
        u = Line(q.get_corner(DL) + DOWN * 0.14,
                 q.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2, color=TEAL)
        sub = Text("proximate vs. distal", font=SERIF, color=SLATE,
                   font_size=26, slant=ITALIC)
        sub.next_to(q, DOWN, buff=0.4)
        q.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(q), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B10_NecVsSuf(Scene):
    """MECHANISM 3 — necessary vs. sufficient.

    Two condition circles: corrosion (necessary) and no monitoring (second
    ingredient). Their intersection labels RUPTURE in CRIMSON.
    An arrow from corrosion-only points to TEAL 'no rupture' outcome.
    """
    def construct(self):
        total = DUR["B10"]

        eye = SerifLabel(
            "checkpoint 3  ·  necessary vs. sufficient",
            SLATE, size=20,
        )
        eye.to_edge(UP, buff=0.7)

        # Two condition ellipses — Venn-style
        c1 = Ellipse(width=3.6, height=2.4)
        c1.set_fill(SLATE, 0.12).set_stroke(SLATE, 2.5)
        c1.move_to(LEFT * 1.5 + DOWN * 0.2)

        c2 = Ellipse(width=3.6, height=2.4)
        c2.set_fill(SLATE, 0.12).set_stroke(SLATE, 2.5)
        c2.move_to(RIGHT * 1.5 + DOWN * 0.2)

        lbl1 = Text("corrosion", font=SERIF, color=INK, font_size=24)
        lbl1.move_to(c1.get_center() + LEFT * 0.8)
        lbl2 = Text("no monitoring", font=SERIF, color=INK, font_size=24)
        lbl2.move_to(c2.get_center() + RIGHT * 0.8)

        intersect_lbl = LabelChip("RUPTURE", accent=CRIMSON, size=24)
        intersect_lbl.move_to(ORIGIN + DOWN * 0.2)

        # Outcome: corrosion alone (left only) -> no rupture (TEAL)
        alone_node = _chain_node("corrosion only", accent=TEAL, w=2.4, h=0.55)
        alone_node.move_to(LEFT * 4.4 + DOWN * 1.8)
        outcome_arr = Arrow(
            LEFT * 1.5 + DOWN * 1.5,
            alone_node.get_right() + RIGHT * 0.1,
            color=TEAL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        outcome_lbl = Text("if inspected + repaired", font=SERIF,
                           color=TEAL, font_size=20, slant=ITALIC)
        outcome_lbl.next_to(alone_node, DOWN, buff=0.2)
        no_rupt = LabelChip("no rupture", accent=TEAL, size=20)
        no_rupt.next_to(outcome_lbl, DOWN, buff=0.15)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(c1), FadeIn(lbl1), run_time=0.7)
        self.play(FadeIn(c2), FadeIn(lbl2), run_time=0.7)
        self.play(FadeIn(intersect_lbl, scale=0.9), run_time=0.7)
        self.wait(0.8)
        self.play(GrowArrow(outcome_arr), FadeIn(alone_node), run_time=0.7)
        self.play(FadeIn(outcome_lbl), FadeIn(no_rupt), run_time=0.6)
        self.wait(max(0.5, total - (0.5 + 0.7 + 0.7 + 0.7 + 0.8 + 0.7 + 0.6)))


class B11_DiagCard3(Scene):
    """MECHANISM — diagnostic card: necessary or sufficient?"""
    def construct(self):
        total = DUR["B11"]
        chip = LabelChip("checkpoint 3", accent=SLATE, size=22)
        chip.to_corner(UL, buff=0.8)
        q = Text("Necessary  --  or sufficient?", font=DISPLAY, color=INK,
                 font_size=40, weight="MEDIUM")
        u = Line(q.get_corner(DL) + DOWN * 0.14,
                 q.get_corner(DR) + DOWN * 0.14,
                 stroke_width=2, color=TEAL)
        sub = Text("necessary vs. sufficient", font=SERIF, color=SLATE,
                   font_size=26, slant=ITALIC)
        sub.next_to(q, DOWN, buff=0.4)
        q.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(chip), run_time=0.4)
        self.play(FadeIn(q), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B13_Matrix(Scene):
    """THE IMPLICATION — the 3x3 matrix, key visual.

    Three distinctions as columns, three rows: (1) what collapses,
    (2) diagnostic question, (3) failure mode produced.
    Cells build in cell by cell, CRIMSON for the failure column header,
    TEAL for the diagnostic and correct-reading cells.
    """
    def construct(self):
        total = DUR["B13"]

        eye = SerifLabel("all three distinctions  ·  one map", SLATE, size=22)
        eye.to_edge(UP, buff=0.7)

        cols = ["Corr vs. Cause", "Prox vs. Distal", "Nec vs. Suf"]
        rows = ["What collapses", "Diagnostic", "Failure mode"]

        col_x = [-3.8, -0.2, 3.4]
        row_y = [1.8, 0.55, -0.65]
        header_y = 2.8
        row_label_x = -6.0

        CELL_W, CELL_H = 3.2, 0.95

        cells_data = [
            # row 0 — what collapses
            [
                ("co-occurrence", CRIMSON),
                ("trigger", CRIMSON),
                ("required ingredient", CRIMSON),
            ],
            # row 1 — diagnostic question
            [
                ("mechanism?", TEAL),
                ("prox or distal?", TEAL),
                ("nec or suf?", TEAL),
            ],
            # row 2 — failure mode
            [
                ("overstates certainty", INK),
                ("shifts blame", INK),
                ("inflates one factor", INK),
            ],
        ]

        # column headers
        col_hdrs = []
        for i, label in enumerate(cols):
            hdr = LabelChip(label, accent=SLATE, size=20)
            hdr.move_to(RIGHT * col_x[i] + UP * header_y)
            col_hdrs.append(hdr)

        # row labels
        row_lbls = []
        for i, label in enumerate(rows):
            lbl = Text(label, font=SERIF, color=SLATE, font_size=20,
                       slant=ITALIC)
            lbl.move_to(RIGHT * row_label_x + UP * row_y[i],
                        aligned_edge=LEFT)
            row_lbls.append(lbl)

        # matrix cells
        cell_groups = []
        for ri in range(3):
            for ci in range(3):
                txt_str, accent = cells_data[ri][ci]
                cell_box = _box(CELL_W, CELL_H, accent, fill_opacity=0.10,
                                stroke_color=accent, stroke_width=1.5)
                cell_box.move_to(RIGHT * col_x[ci] + UP * row_y[ri])
                cell_txt = Text(txt_str, font=SERIF, color=accent,
                                font_size=20)
                if cell_txt.width > CELL_W * 0.86:
                    cell_txt.scale_to_fit_width(CELL_W * 0.86)
                cell_txt.move_to(cell_box)
                cell_groups.append(VGroup(cell_box, cell_txt))

        self.play(FadeIn(eye), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(h, shift=DOWN * 0.15) for h in col_hdrs],
                        lag_ratio=0.2, run_time=0.8),
        )
        self.play(
            LaggedStart(*[FadeIn(rl, shift=RIGHT * 0.15) for rl in row_lbls],
                        lag_ratio=0.2, run_time=0.7),
        )
        # cells build in left-to-right, top-to-bottom
        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.9) for c in cell_groups],
                lag_ratio=0.10,
                run_time=3.2,
            )
        )
        self.wait(max(0.5, total - (0.5 + 0.8 + 0.7 + 3.2)))


class B14_ExampleSetup(Scene):
    """THE EXAMPLE — the claim and three blank diagnostic boxes."""
    def construct(self):
        total = DUR["B14"]

        eye = SerifLabel("worked example  ·  illustrative", SLATE, size=20)
        eye.to_edge(UP, buff=0.7)

        claim_txt = (
            "Teen depression rose sharply after 2012,\n"
            "the same year smartphone ownership\nbecame widespread."
        )
        claim = Text(claim_txt, font=SERIF, color=INK, font_size=28,
                     line_spacing=1.1)
        claim.move_to(UP * 1.5)
        u = Line(claim.get_corner(DL) + DOWN * 0.1,
                 claim.get_corner(DR) + DOWN * 0.1,
                 stroke_width=1.5, color=SLATE)

        q_labels = [
            "1. What is the mechanism?",
            "2. Proximate or distal cause?",
            "3. Necessary or sufficient?",
        ]
        boxes = VGroup(*[_diagnostic_box(q, filled=False) for q in q_labels])
        boxes.arrange(DOWN, buff=0.3)
        boxes.next_to(claim, DOWN, buff=0.6)

        self.play(FadeIn(eye), run_time=0.4)
        self.play(FadeIn(claim), Create(u), run_time=0.9)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in boxes],
                        lag_ratio=0.25, run_time=1.2),
        )
        self.wait(max(0.5, total - (0.4 + 0.9 + 1.2)))


class B15_ExampleFilled(Scene):
    """THE EXAMPLE — diagnostic answers fill in one by one (TEAL)."""
    def construct(self):
        total = DUR["B15"]

        eye = SerifLabel("worked example  ·  illustrative", SLATE, size=20)
        eye.to_edge(UP, buff=0.7)

        claim_txt = (
            "Teen depression rose sharply after 2012,\n"
            "the same year smartphone ownership\nbecame widespread."
        )
        claim = Text(claim_txt, font=SERIF, color=SLATE, font_size=26,
                     line_spacing=1.1)
        claim.move_to(UP * 1.5)

        answers = [
            "1. mechanism unclear  ·  multiple candidates",
            "2. proximate = phone  ·  distal = attention-economy design",
            "3. necessary but not sufficient  ·  one factor among several",
        ]
        filled_boxes = VGroup(
            *[_diagnostic_box(a, filled=True, accent=TEAL) for a in answers]
        )
        filled_boxes.arrange(DOWN, buff=0.3)
        filled_boxes.next_to(claim, DOWN, buff=0.6)

        self.play(FadeIn(eye), FadeIn(claim), run_time=0.6)
        for box in filled_boxes:
            self.play(FadeIn(box, shift=UP * 0.15), run_time=0.8)
            self.wait(1.6)
        self.wait(max(0.5, total - (0.6 + len(filled_boxes) * (0.8 + 1.6))))


class B16_ThreeChecks(Scene):
    """THE PRACTICE — three numbered checklist items appear sequentially."""
    def construct(self):
        total = DUR["B16"]

        eye = SerifLabel("the three-question check", TEAL, size=24)
        eye.to_edge(UP, buff=0.7)

        items = [
            "1  What is the mechanism?",
            "2  Proximate or distal  --  does your argument need the other?",
            "3  Necessary, sufficient, or one factor among several?",
        ]
        item_mobs = []
        for txt in items:
            t = Text(txt, font=SERIF, color=INK, font_size=28)
            if t.width > 11.8:
                t.scale_to_fit_width(11.8)
            bar = Rectangle(width=0.08, height=t.height + 0.2)
            bar.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            bar.align_to(t, LEFT).shift(LEFT * 0.3)
            item_mobs.append(VGroup(bar, t))

        stack = VGroup(*item_mobs).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        stack.move_to(DOWN * 0.2)

        self.play(FadeIn(eye), run_time=0.5)
        for mob in item_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(1.4)
        self.wait(max(0.5, total - (0.5 + len(item_mobs) * (0.7 + 1.4))))


class B17_PracticeCard(Scene):
    """THE PRACTICE — payoff card: three gates, one clean argument."""
    def construct(self):
        total = DUR["B17"]
        t1 = Text("Three gates.", font=DISPLAY, color=INK,
                  font_size=46, weight="MEDIUM")
        t2 = Text("One clean causal claim.", font=SERIF, color=SLATE,
                  font_size=34, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.4).move_to(UP * 0.15)
        u = Line(t1.get_corner(DL) + DOWN * 0.12,
                 t1.get_corner(DR) + DOWN * 0.12,
                 stroke_width=2, color=TEAL)
        sub = Text("pass all three  --  the argument holds",
                   font=SERIF, color=TEAL, font_size=24)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))


class B18_End(Scene):
    """RECAP — endcard: question to answer, WRITING kicker."""
    def construct(self):
        total = DUR["B18"]
        t1 = Text("Three distinctions.", font=DISPLAY, color=INK,
                  font_size=46, weight="MEDIUM")
        t2 = Text("Three diagnostics.", font=SERIF, color=INK,
                  font_size=38)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.3).move_to(UP * 0.3)
        u = Line(t1.get_corner(DL) + DOWN * 0.12,
                 t1.get_corner(DR) + DOWN * 0.12,
                 stroke_width=2, color=CRIMSON)
        kicker = LabelChip("WRITING", accent=SLATE, size=22)
        kicker.next_to(block, DOWN, buff=0.55)
        self.play(FadeIn(t1), Create(u), run_time=0.9)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(kicker, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
