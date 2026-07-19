"""vox_scenes.py — Why Cancer Cannot Read Its Own Death Instructions
(vox-p53-circuit, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is own. STILL beats (B02, B08)
have no scene here — they compile as slates until the human drops media.

Color law: TEAL #1F6F5C = p53 wild-type / damage sensed / death executed (good
path). CRIMSON #BF3339 = p53 mutant / hub removed / damage ignored (bad path).
GOLD = editor's-pen fill once per graphic only (B07). Two accents max, never swap.

Exclusions (card): NO extrinsic pathway, NO necroptosis/ferroptosis/pyroptosis,
NO venetoclax or BH3 mimetics, NO p53 tetramer detail.

Gate B convention: every zero-width stroke is also zero-opacity.
Single-method .animate chains only — no chained attribute calls on _Anim objects.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 10.0, "B03": 12.0, "B04": 11.0, "B05": 10.0, "B06": 13.0,
    "B07": 13.0, "B09": 12.0, "B10": 13.0, "B11": 11.0, "B12": 10.0,
    "B13": 14.0, "B14": 14.0, "B15": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _box(color, w, h, fill_opacity=0.10, stroke_color=None, stroke_width=2.5):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, fill_opacity)
    r.set_stroke(stroke_color or color, stroke_width)
    return r


def _solid_box(color, w, h):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1.0)
    r.set_stroke(width=0, opacity=0)
    return r


def _chip(text, accent):
    return LabelChip(text, accent=accent, size=24)


def _label(text, accent, size=28):
    return SerifLabel(text, accent=accent, size=size)


def _arrow(start, end, color=INK):
    a = Arrow(start, end, color=color, stroke_width=3,
              tip_length=0.22, buff=0.12)
    a.set_stroke(color, 3)
    return a


def _node_circle(color, radius=0.38):
    c = Circle(radius=radius)
    c.set_fill(color, 1.0)
    c.set_stroke(width=0, opacity=0)
    return c


def _x_mark(center, color=CRIMSON, size=0.28):
    l1 = Line(center + UP * size + LEFT * size,
              center + DOWN * size + RIGHT * size,
              color=color, stroke_width=4)
    l2 = Line(center + UP * size + RIGHT * size,
              center + DOWN * size + LEFT * size,
              color=color, stroke_width=4)
    return VGroup(l1, l2)


def _dashed_line(start, end, color=CRIMSON, n=8):
    """Approximate dashed line as small rectangles."""
    pts = [start + (end - start) * i / (n * 2 - 1) for i in range(0, n * 2, 2)]
    pts2 = [start + (end - start) * (i + 1) / (n * 2 - 1) for i in range(0, n * 2, 2)]
    segs = VGroup(*[Line(p, q, color=color, stroke_width=2.5)
                    for p, q in zip(pts, pts2)])
    return segs


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """COLD OPEN — title card. Eyebrow CANCER BIOLOGY in TEAL."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=26, weight="MEDIUM")
        t1 = Text("Why cancer cannot read", font=DISPLAY, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("its own death instructions", font=DISPLAY, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        sub = Text("the p53 circuit", font=SERIF, color=INK, font_size=28,
                   slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.4)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.08), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B03_QuestionCard(Scene):
    """THE QUESTION — gap formula on screen AND in narration."""
    def construct(self):
        total = DUR["B03"]
        q = Text("The same damage.", font=DISPLAY, color=INK,
                 font_size=44, weight=BOLD)
        a1 = Text("One cell dies. One cell divides.", font=DISPLAY, color=INK,
                  font_size=38)
        a2 = Text("Why?", font=DISPLAY, color=CRIMSON,
                  font_size=52, weight=BOLD)
        block = VGroup(q, a1, a2).arrange(DOWN, buff=0.28).move_to(UP * 0.2)
        sub = Text("irreparable DNA damage should trigger apoptosis", font=SERIF,
                   color=INK, font_size=26, slant=ITALIC)
        sub.next_to(block, DOWN, buff=0.5)
        u_sub = Line(sub.get_corner(DL) + DOWN * 0.1, sub.get_corner(DR) + DOWN * 0.1,
                     color=CRIMSON, stroke_width=1.4)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(a1), run_time=0.6)
        self.play(FadeIn(a2, scale=0.9), run_time=0.7)
        self.play(FadeIn(sub), Create(u_sub), run_time=0.8)
        self.wait(max(0.5, total - 2.8))


class B04_DamageToDeathExpected(Scene):
    """THE PROBLEM — naive expectation: damage flows through to death."""
    def construct(self):
        total = DUR["B04"]
        # Three nodes: DAMAGE -> [sensor] -> DEATH
        cx = [-4.2, 0.0, 4.2]
        cy = 0.2

        dmg_box = _box(CRIMSON, 2.4, 0.9)
        dmg_box.move_to([cx[0], cy, 0])
        dmg_lbl = Text("DAMAGE", font=DISPLAY, color=CRIMSON,
                       font_size=28, weight="MEDIUM")
        dmg_lbl.move_to(dmg_box.get_center())

        sens_circle = _node_circle(TEAL, 0.55)
        sens_circle.move_to([cx[1], cy, 0])
        sens_lbl = Text("sensor", font=SERIF, color=WHITE,
                        font_size=24, slant=ITALIC)
        sens_lbl.move_to(sens_circle.get_center())

        death_box = _box(TEAL, 2.4, 0.9)
        death_box.move_to([cx[2], cy, 0])
        death_lbl = Text("DEATH", font=DISPLAY, color=TEAL,
                         font_size=28, weight="MEDIUM")
        death_lbl.move_to(death_box.get_center())

        # Arrows between them
        arr1 = _arrow(np.array([cx[0] + 1.3, cy, 0]),
                      np.array([cx[1] - 0.6, cy, 0]), TEAL)
        arr2 = _arrow(np.array([cx[1] + 0.6, cy, 0]),
                      np.array([cx[2] - 1.3, cy, 0]), TEAL)

        eye = _label("expected: damage triggers death", TEAL, 24)
        eye.next_to(VGroup(dmg_box, death_box), DOWN, buff=0.6)

        self.play(FadeIn(dmg_box), FadeIn(dmg_lbl), run_time=0.7)
        self.play(GrowArrow(arr1), run_time=0.6)
        self.play(FadeIn(sens_circle), FadeIn(sens_lbl), run_time=0.6)
        self.play(GrowArrow(arr2), run_time=0.6)
        self.play(FadeIn(death_box), FadeIn(death_lbl), run_time=0.6)
        self.play(FadeIn(eye, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B05_BrokenLink(Scene):
    """THE PROBLEM — sensors fire but link to death is cut."""
    def construct(self):
        total = DUR["B05"]
        cx = [-4.2, 0.0, 4.2]
        cy = 0.2

        dmg_box = _box(CRIMSON, 2.4, 0.9)
        dmg_box.move_to([cx[0], cy, 0])
        dmg_lbl = Text("DAMAGE", font=DISPLAY, color=CRIMSON,
                       font_size=28, weight="MEDIUM")
        dmg_lbl.move_to(dmg_box.get_center())

        sens_circle = _node_circle(TEAL, 0.55)
        sens_circle.move_to([cx[1], cy, 0])
        sens_lbl = Text("sensor", font=SERIF, color=WHITE,
                        font_size=24, slant=ITALIC)
        sens_lbl.move_to(sens_circle.get_center())

        # Death box grayed out
        death_box = _box(SLATE, 2.4, 0.9, fill_opacity=0.05, stroke_width=1.5)
        death_box.move_to([cx[2], cy, 0])
        death_lbl = Text("DEATH", font=DISPLAY, color=SLATE,
                         font_size=28, weight="MEDIUM")
        death_lbl.set_opacity(0.35)
        death_lbl.move_to(death_box.get_center())

        arr1 = _arrow(np.array([cx[0] + 1.3, cy, 0]),
                      np.array([cx[1] - 0.6, cy, 0]), TEAL)

        # Broken/dashed segment + X between sensor and death
        break_start = np.array([cx[1] + 0.65, cy, 0])
        break_end = np.array([cx[2] - 1.35, cy, 0])
        dashed = _dashed_line(break_start, break_end, CRIMSON, 6)
        x_center = (break_start + break_end) / 2
        x_mark = _x_mark(x_center, CRIMSON, 0.24)

        q_lbl = _label("sensors fire — but then what?", CRIMSON, 24)
        q_lbl.next_to(VGroup(dmg_box, death_box), DOWN, buff=0.6)

        self.play(FadeIn(dmg_box), FadeIn(dmg_lbl),
                  FadeIn(sens_circle), FadeIn(sens_lbl), run_time=0.8)
        self.play(GrowArrow(arr1), run_time=0.5)
        # The broken link appears
        self.play(FadeIn(dashed), run_time=0.6)
        self.play(FadeIn(x_mark, scale=0.8), run_time=0.5)
        self.play(FadeIn(death_box), FadeIn(death_lbl), run_time=0.5)
        self.play(FadeIn(q_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.5))


class B06_P53Hub(Scene):
    """THE MECHANISM — p53 hub stabilizes between sensor and death."""
    def construct(self):
        total = DUR["B06"]
        cx = [-4.8, -1.8, 1.2, 4.8]
        cy = 0.2

        dmg_box = _box(CRIMSON, 2.0, 0.8)
        dmg_box.move_to([cx[0], cy, 0])
        dmg_lbl = Text("DAMAGE", font=DISPLAY, color=CRIMSON,
                       font_size=24, weight="MEDIUM")
        dmg_lbl.move_to(dmg_box.get_center())

        sens_chip = _chip("ATR / ATM", TEAL)
        sens_chip.move_to([cx[1], cy, 0])

        p53_circle = _node_circle(TEAL, 0.6)
        p53_circle.move_to([cx[2], cy, 0])
        p53_lbl = Text("p53", font=DISPLAY, color=WHITE,
                       font_size=30, weight=BOLD)
        p53_lbl.move_to(p53_circle.get_center())

        arrow_hint_box = _box(TEAL, 2.0, 0.8, fill_opacity=0.06)
        arrow_hint_box.move_to([cx[3], cy, 0])
        arrow_hint_lbl = Text("DEATH", font=DISPLAY, color=TEAL,
                              font_size=24, weight="MEDIUM")
        arrow_hint_lbl.set_opacity(0.5)
        arrow_hint_lbl.move_to(arrow_hint_box.get_center())

        arr1 = _arrow(np.array([cx[0] + 1.1, cy, 0]),
                      np.array([cx[1] - 0.75, cy, 0]), TEAL)
        arr2 = _arrow(np.array([cx[1] + 0.75, cy, 0]),
                      np.array([cx[2] - 0.65, cy, 0]), TEAL)
        arr3 = _arrow(np.array([cx[2] + 0.65, cy, 0]),
                      np.array([cx[3] - 1.1, cy, 0]), TEAL)

        stabilize_lbl = _label("stabilizes", TEAL, 26)
        stabilize_lbl.next_to(p53_circle, DOWN, buff=0.45)

        eye = _label("p53: the missing hub", TEAL, 24)
        eye.to_edge(UP, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(dmg_box), FadeIn(dmg_lbl), run_time=0.6)
        self.play(GrowArrow(arr1), FadeIn(sens_chip), run_time=0.7)
        self.play(GrowArrow(arr2), run_time=0.5)
        # p53 hub grows in
        self.play(GrowFromCenter(p53_circle), FadeIn(p53_lbl), run_time=0.9)
        self.play(FadeIn(stabilize_lbl, shift=UP * 0.08), run_time=0.5)
        self.play(GrowArrow(arr3), FadeIn(arrow_hint_box),
                  FadeIn(arrow_hint_lbl), run_time=0.7)
        self.wait(max(0.5, total - 4.4))


class B07_P53Transcribes(Scene):
    """THE MECHANISM — p53 fans into PUMA, NOXA, BAX."""
    def construct(self):
        total = DUR["B07"]
        # p53 hub on the left, three fan branches to the right
        hub_center = np.array([-2.8, 0.0, 0])
        p53_circle = _node_circle(TEAL, 0.6)
        p53_circle.move_to(hub_center)
        p53_lbl = Text("p53", font=DISPLAY, color=WHITE,
                       font_size=30, weight=BOLD)
        p53_lbl.move_to(hub_center)

        targets = [
            ("PUMA", np.array([1.8, 1.6, 0])),
            ("NOXA", np.array([1.8, 0.0, 0])),
            ("BAX",  np.array([1.8, -1.6, 0])),
        ]

        chips = []
        arrows = []
        for name, pos in targets:
            chip = _chip(name, TEAL)
            chip.move_to(pos)
            chips.append(chip)
            arr = _arrow(hub_center + RIGHT * 0.65, pos + LEFT * 0.8, TEAL)
            arrows.append(arr)

        # BCL-2 balance label at far right
        bcl_box = _box(TEAL, 3.2, 0.85)
        bcl_box.move_to(np.array([5.2, 0.0, 0]))
        bcl_lbl = Text("BCL-2 balance tips", font=DISPLAY, color=TEAL,
                       font_size=22, weight="MEDIUM")
        bcl_lbl.move_to(bcl_box.get_center())

        # Gold highlight bar behind the BCL-2 label (editor's pen, once)
        gold_bar = _solid_box(GOLD, 3.2, 0.85)
        gold_bar.set_opacity(0.30)
        gold_bar.move_to(bcl_box.get_center())

        arr_to_bcl = _arrow(np.array([2.85, 0.0, 0]),
                            np.array([3.55, 0.0, 0]), TEAL)

        transcribes_lbl = _label("transcribes", TEAL, 26)
        transcribes_lbl.next_to(p53_circle, DOWN, buff=0.5)

        self.play(FadeIn(p53_circle), FadeIn(p53_lbl), run_time=0.6)
        self.play(FadeIn(transcribes_lbl, shift=UP * 0.08), run_time=0.5)
        # Fan chips appear in sequence
        for chip, arr in zip(chips, arrows):
            self.play(GrowArrow(arr), FadeIn(chip, scale=0.9), run_time=0.55)
        # BCL-2 endpoint with gold accent
        self.play(GrowArrow(arr_to_bcl), FadeIn(gold_bar),
                  FadeIn(bcl_box), FadeIn(bcl_lbl), run_time=0.9)
        self.wait(max(0.5, total - 4.2))


class B09_FullCircuit(Scene):
    """THE MECHANISM — full intact circuit, p53 at center."""
    def construct(self):
        total = DUR["B09"]
        # Horizontal chain: DAMAGE -> ATR/ATM -> p53 -> PUMA/NOXA/BAX -> MOMP -> CASPASES
        positions = [-5.8, -3.5, -0.8, 1.8, 4.0, 6.2]
        labels_text = ["DAMAGE", "ATR/ATM", "p53", "PUMA\nNOXA\nBAX",
                       "MOMP", "CASPASES"]
        colors_list = [CRIMSON, TEAL, TEAL, TEAL, TEAL, TEAL]
        widths = [1.8, 1.8, 0.0, 2.0, 1.8, 2.0]
        # p53 is a circle (width=0 means circle node)

        nodes = []
        for i, (x, txt, col, w) in enumerate(zip(positions, labels_text,
                                                  colors_list, widths)):
            if w == 0.0:
                # circle node
                circ = _node_circle(col, 0.5)
                circ.move_to([x, 0.0, 0])
                lbl = Text(txt, font=DISPLAY, color=WHITE,
                           font_size=22, weight=BOLD)
                lbl.move_to([x, 0.0, 0])
                node = VGroup(circ, lbl)
            else:
                box = _box(col, w, 0.75 if "\n" not in txt else 0.9)
                box.move_to([x, 0.0, 0])
                if "\n" in txt:
                    lines = txt.split("\n")
                    txts = VGroup(*[Text(l, font=DISPLAY, color=col,
                                        font_size=18, weight="MEDIUM")
                                    for l in lines])
                    txts.arrange(DOWN, buff=0.04)
                    txts.move_to([x, 0.0, 0])
                    node = VGroup(box, txts)
                else:
                    lbl = Text(txt, font=DISPLAY, color=col,
                               font_size=20, weight="MEDIUM")
                    lbl.move_to([x, 0.0, 0])
                    node = VGroup(box, lbl)
            nodes.append(node)

        # Arrows between successive nodes
        arrows = []
        gaps = [
            (positions[0] + 0.95, positions[1] - 0.95),
            (positions[1] + 0.95, positions[2] - 0.55),
            (positions[2] + 0.55, positions[3] - 1.05),
            (positions[3] + 1.05, positions[4] - 0.95),
            (positions[4] + 0.95, positions[5] - 1.05),
        ]
        for start_x, end_x in gaps:
            arr = _arrow(np.array([start_x, 0.0, 0]),
                         np.array([end_x, 0.0, 0]), TEAL)
            arrows.append(arr)

        hinge_lbl = _label("p53 is the hinge", TEAL, 26)
        hinge_lbl.next_to(nodes[2], DOWN, buff=0.55)

        self.play(FadeIn(nodes[0]), run_time=0.5)
        for i in range(len(arrows)):
            self.play(GrowArrow(arrows[i]), FadeIn(nodes[i + 1]), run_time=0.5)
        self.play(FadeIn(hinge_lbl, shift=UP * 0.08), run_time=0.6)
        self.wait(max(0.5, total - 4.1))


class B10_CircuitCollapse(Scene):
    """THE MECHANISM — COLLAPSE: p53 hub removed, downstream goes dark."""
    def construct(self):
        total = DUR["B10"]
        positions = [-5.8, -3.5, -0.8, 1.8, 4.0, 6.2]
        labels_text = ["DAMAGE", "ATR/ATM", "p53", "PUMA\nNOXA\nBAX",
                       "MOMP", "CASPASES"]
        colors_list = [CRIMSON, TEAL, TEAL, TEAL, TEAL, TEAL]
        widths = [1.8, 1.8, 0.0, 2.0, 1.8, 2.0]

        # Build full circuit (same as B09)
        nodes = []
        for i, (x, txt, col, w) in enumerate(zip(positions, labels_text,
                                                  colors_list, widths)):
            if w == 0.0:
                circ = _node_circle(col, 0.5)
                circ.move_to([x, 0.0, 0])
                lbl = Text(txt, font=DISPLAY, color=WHITE,
                           font_size=22, weight=BOLD)
                lbl.move_to([x, 0.0, 0])
                node = VGroup(circ, lbl)
            else:
                box = _box(col, w, 0.75 if "\n" not in txt else 0.9)
                box.move_to([x, 0.0, 0])
                if "\n" in txt:
                    lines = txt.split("\n")
                    txts = VGroup(*[Text(l, font=DISPLAY, color=col,
                                        font_size=18, weight="MEDIUM")
                                    for l in lines])
                    txts.arrange(DOWN, buff=0.04)
                    txts.move_to([x, 0.0, 0])
                    node = VGroup(box, txts)
                else:
                    lbl = Text(txt, font=DISPLAY, color=col,
                               font_size=20, weight="MEDIUM")
                    lbl.move_to([x, 0.0, 0])
                    node = VGroup(box, lbl)
            nodes.append(node)

        arrows = []
        gaps = [
            (positions[0] + 0.95, positions[1] - 0.95),
            (positions[1] + 0.95, positions[2] - 0.55),
            (positions[2] + 0.55, positions[3] - 1.05),
            (positions[3] + 1.05, positions[4] - 0.95),
            (positions[4] + 0.95, positions[5] - 1.05),
        ]
        for start_x, end_x in gaps:
            arr = _arrow(np.array([start_x, 0.0, 0]),
                         np.array([end_x, 0.0, 0]), TEAL)
            arrows.append(arr)

        # Start with full circuit visible
        self.add(*nodes, *arrows)
        self.wait(0.6)

        # COLLAPSE: fade out p53 hub, downstream dims and grays
        downstream = VGroup(nodes[3], nodes[4], nodes[5],
                            arrows[2], arrows[3], arrows[4])
        p53_hub = nodes[2]
        arr_to_p53 = arrows[1]   # arrow from ATR/ATM to p53

        # First: p53 shrinks out
        self.play(ShrinkToCenter(p53_hub), run_time=0.9)

        # Crimson X at p53 position
        x_center = np.array([positions[2], 0.0, 0])
        x_mark = _x_mark(x_center, CRIMSON, 0.32)
        self.play(FadeIn(x_mark, scale=0.7), run_time=0.5)

        # arr_to_p53 fades (nothing to point to)
        self.play(FadeOut(arr_to_p53), run_time=0.4)

        # Downstream fades to gray
        self.play(downstream.animate.set_opacity(0.18), run_time=0.9)

        lbl = _label("message dead-ends", CRIMSON, 26)
        lbl.next_to(x_mark, DOWN, buff=0.55)
        self.play(FadeIn(lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.3))


class B11_P53FrequencyBar(Scene):
    """THE IMPLICATION — TP53 lost in ~50% of cancers (IsotypeGrid 100 squares)."""
    def construct(self):
        total = DUR["B11"]
        eye = Text("TP53 — the most frequently mutated gene in human cancer",
                   font=SERIF, color=INK, font_size=26, slant=ITALIC)
        eye.to_edge(UP, buff=0.65)

        # IsotypeGrid: 100 squares — 50 crimson (mutant), 50 teal (intact)
        grid = IsotypeGrid([50, 50], [CRIMSON, TEAL], per_row=10,
                           size=0.22, gap=0.12, mark="square")
        grid.move_to(ORIGIN + DOWN * 0.2)

        mut_chip = _chip("TP53 MUTANT", CRIMSON)
        intact_chip = _chip("TP53 INTACT", TEAL)
        chips = VGroup(mut_chip, intact_chip).arrange(RIGHT, buff=1.2)
        chips.next_to(grid, DOWN, buff=0.5)

        approx = Text("approximately half of all human cancers",
                      font=SERIF, color=INK, font_size=24, slant=ITALIC)
        approx.next_to(chips, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.6)
        self.play(grid.count_up(run_time=2.5, lag_ratio=0.012), run_time=2.5)
        self.play(FadeIn(mut_chip), FadeIn(intact_chip), run_time=0.7)
        self.play(FadeIn(approx, shift=UP * 0.08), run_time=0.6)
        self.wait(max(0.5, total - 4.4))


class B12_LineageDrift(Scene):
    """THE IMPLICATION — lineage without p53 drifts, errors accumulate."""
    def construct(self):
        total = DUR["B12"]
        # Left: p53-intact tree (terminates at damage)
        # Right: p53-mutant tree (fans out, errors accumulate)

        left_lbl = _chip("p53 INTACT", TEAL)
        right_lbl = _chip("p53 MUTANT", CRIMSON)
        left_lbl.move_to(LEFT * 3.8 + UP * 3.0)
        right_lbl.move_to(RIGHT * 3.8 + UP * 3.0)

        # LEFT: root -> 2 daughters; one gets damage and stops (X)
        lroot = _node_circle(TEAL, 0.25)
        lroot.move_to(LEFT * 3.8 + UP * 1.8)
        ld1 = _node_circle(TEAL, 0.22)
        ld1.move_to(LEFT * 4.6 + UP * 0.6)
        ld2 = _node_circle(CRIMSON, 0.22)
        ld2.move_to(LEFT * 3.0 + UP * 0.6)
        larr1 = Line(lroot.get_bottom(), ld1.get_top(),
                     color=TEAL, stroke_width=2)
        larr2 = Line(lroot.get_bottom(), ld2.get_top(),
                     color=TEAL, stroke_width=2)
        # damage cell terminates: X mark
        lx = _x_mark(ld2.get_center() + DOWN * 0.5, CRIMSON, 0.2)
        l_term = Text("terminates", font=SERIF, color=CRIMSON,
                      font_size=20, slant=ITALIC)
        l_term.next_to(lx, DOWN, buff=0.2)

        # RIGHT: root -> 2 -> 4, all carry crimson errors
        rroot = _node_circle(CRIMSON, 0.25)
        rroot.move_to(RIGHT * 3.8 + UP * 1.8)
        rd1 = _node_circle(CRIMSON, 0.22)
        rd1.move_to(RIGHT * 3.1 + UP * 0.6)
        rd2 = _node_circle(CRIMSON, 0.22)
        rd2.move_to(RIGHT * 4.5 + UP * 0.6)
        rarr1 = Line(rroot.get_bottom(), rd1.get_top(),
                     color=CRIMSON, stroke_width=2)
        rarr2 = Line(rroot.get_bottom(), rd2.get_top(),
                     color=CRIMSON, stroke_width=2)
        # grandchildren
        rg1 = _node_circle(CRIMSON, 0.19)
        rg1.move_to(RIGHT * 2.7 + DOWN * 0.55)
        rg2 = _node_circle(CRIMSON, 0.19)
        rg2.move_to(RIGHT * 3.5 + DOWN * 0.55)
        rg3 = _node_circle(CRIMSON, 0.19)
        rg3.move_to(RIGHT * 4.1 + DOWN * 0.55)
        rg4 = _node_circle(CRIMSON, 0.19)
        rg4.move_to(RIGHT * 4.9 + DOWN * 0.55)
        rgarr1 = Line(rd1.get_bottom(), rg1.get_top(),
                      color=CRIMSON, stroke_width=2)
        rgarr2 = Line(rd1.get_bottom(), rg2.get_top(),
                      color=CRIMSON, stroke_width=2)
        rgarr3 = Line(rd2.get_bottom(), rg3.get_top(),
                      color=CRIMSON, stroke_width=2)
        rgarr4 = Line(rd2.get_bottom(), rg4.get_top(),
                      color=CRIMSON, stroke_width=2)

        r_drift = Text("errors accumulate", font=SERIF, color=CRIMSON,
                       font_size=20, slant=ITALIC)
        r_drift.next_to(VGroup(rg1, rg2, rg3, rg4), DOWN, buff=0.3)

        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.6)
        # Left lineage
        self.play(FadeIn(lroot), run_time=0.4)
        self.play(Create(larr1), Create(larr2),
                  FadeIn(ld1), FadeIn(ld2), run_time=0.7)
        self.play(FadeIn(lx), FadeIn(l_term), run_time=0.6)
        # Right lineage
        self.play(FadeIn(rroot), run_time=0.4)
        self.play(Create(rarr1), Create(rarr2),
                  FadeIn(rd1), FadeIn(rd2), run_time=0.7)
        self.play(Create(rgarr1), Create(rgarr2), Create(rgarr3), Create(rgarr4),
                  FadeIn(rg1), FadeIn(rg2), FadeIn(rg3), FadeIn(rg4), run_time=0.8)
        self.play(FadeIn(r_drift, shift=UP * 0.08), run_time=0.6)
        self.wait(max(0.5, total - 4.8))


class B13_TwoCellsLeft(Scene):
    """THE EXAMPLE — left cell (p53 WT) executes death in ~60 min."""
    def construct(self):
        total = DUR["B13"]

        # Divider
        divider = Line(UP * 3.2, DOWN * 3.2, color=SLATE, stroke_width=1.2)
        divider.set_stroke(SLATE, 1.2)
        divider.move_to(ORIGIN)

        # Panel headers
        l_head = _chip("p53 WILD-TYPE", TEAL)
        l_head.move_to(LEFT * 3.5 + UP * 3.0)
        r_head = _chip("p53 MUTANT", CRIMSON)
        r_head.move_to(RIGHT * 3.5 + UP * 3.0)
        r_head.set_opacity(0.28)

        # Left panel — cascade cascade cascade -> cell dies
        uv_lbl = Text("UV", font=DISPLAY, color=CRIMSON,
                      font_size=22, weight=BOLD)
        uv_lbl.move_to(LEFT * 5.5 + UP * 1.8)

        # Vertical cascade: UV -> p53 rises -> PUMA/NOXA -> BCL-2 tips -> caspases -> GONE
        cascade_items = [
            ("p53 rises", TEAL),
            ("PUMA / NOXA", TEAL),
            ("BCL-2 tips", TEAL),
            ("caspases fire", TEAL),
        ]
        cascade_y = [1.0, 0.1, -0.8, -1.7]
        cascade_x = -3.5

        prev_center = np.array([cascade_x, 1.8, 0])
        uv_box = _box(CRIMSON, 1.6, 0.55)
        uv_box.move_to([cascade_x, 1.9, 0])
        uv_t = Text("UV", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        uv_t.move_to(uv_box.get_center())
        prev_center = uv_box.get_center()

        cascade_nodes = []
        cascade_arrows = []
        for (txt, col), y in zip(cascade_items, cascade_y):
            box = _box(col, 2.4, 0.55)
            box.move_to([cascade_x, y, 0])
            lbl = Text(txt, font=DISPLAY, color=col, font_size=20, weight="MEDIUM")
            lbl.move_to([cascade_x, y, 0])
            node = VGroup(box, lbl)
            cascade_nodes.append(node)
            arr = _arrow(prev_center + DOWN * 0.3,
                         np.array([cascade_x, y + 0.3, 0]), TEAL)
            cascade_arrows.append(arr)
            prev_center = np.array([cascade_x, y, 0])

        # Cell gone — teal circle shrinks to nothing
        cell_circle = Circle(radius=0.45)
        cell_circle.set_fill(TEAL, 0.8)
        cell_circle.set_stroke(width=0, opacity=0)
        cell_circle.move_to([cascade_x, -2.65, 0])
        gone_lbl = Text("GONE", font=DISPLAY, color=TEAL,
                        font_size=24, weight=BOLD)
        gone_lbl.move_to([cascade_x, -2.65, 0])

        timer_lbl = Text("~60 min (illustrative)", font=SERIF, color=TEAL,
                         font_size=22, slant=ITALIC)
        timer_lbl.next_to(cell_circle, DOWN, buff=0.28)

        arr_to_gone = _arrow(
            prev_center + DOWN * 0.3,
            np.array([cascade_x, -2.35, 0]), TEAL)

        self.play(FadeIn(divider), FadeIn(l_head), FadeIn(r_head), run_time=0.6)
        self.play(FadeIn(uv_box), FadeIn(uv_t), run_time=0.5)
        for i, (node, arr) in enumerate(zip(cascade_nodes, cascade_arrows)):
            self.play(GrowArrow(arr), FadeIn(node, scale=0.9), run_time=0.55)
        self.play(GrowArrow(arr_to_gone), run_time=0.4)
        self.play(FadeIn(cell_circle), run_time=0.4)
        # Cell shrinks to nothing
        self.play(ShrinkToCenter(cell_circle), FadeIn(gone_lbl, scale=0.7),
                  run_time=0.7)
        self.play(FadeIn(timer_lbl, shift=UP * 0.08), run_time=0.5)
        self.wait(max(0.5, total - 5.9))


class B14_TwoCellsRight(Scene):
    """THE EXAMPLE — right cell (p53 mutant) divides into 2 daughters."""
    def construct(self):
        total = DUR["B14"]

        # Divider
        divider = Line(UP * 3.2, DOWN * 3.2, color=SLATE, stroke_width=1.2)
        divider.set_stroke(SLATE, 1.2)
        divider.move_to(ORIGIN)

        l_head = _chip("p53 WILD-TYPE", TEAL)
        l_head.move_to(LEFT * 3.5 + UP * 3.0)
        l_head.set_opacity(0.28)
        r_head = _chip("p53 MUTANT", CRIMSON)
        r_head.move_to(RIGHT * 3.5 + UP * 3.0)

        # Left panel — grayed-out "GONE" result from B13
        gone_lbl = Text("GONE", font=DISPLAY, color=TEAL,
                        font_size=24, weight=BOLD)
        gone_lbl.move_to([-3.5, 0.0, 0])
        gone_lbl.set_opacity(0.28)

        # Right panel cascade — p53 flatlines, PUMA/NOXA crossed out, BCL-2 holds
        cascade_x = 3.5
        uv_box = _box(CRIMSON, 1.6, 0.55)
        uv_box.move_to([cascade_x, 1.9, 0])
        uv_t = Text("UV", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        uv_t.move_to(uv_box.get_center())

        # p53 does not rise — flat/absent label
        p53_flat_box = _box(CRIMSON, 2.6, 0.55, fill_opacity=0.05)
        p53_flat_box.move_to([cascade_x, 1.0, 0])
        p53_flat_t = Text("p53: absent", font=DISPLAY, color=CRIMSON,
                          font_size=20, weight="MEDIUM")
        p53_flat_t.move_to(p53_flat_box.get_center())

        # PUMA/NOXA with X
        puma_box = _box(SLATE, 2.6, 0.55, fill_opacity=0.04)
        puma_box.move_to([cascade_x, 0.1, 0])
        puma_t = Text("PUMA / NOXA", font=DISPLAY, color=SLATE,
                      font_size=20, weight="MEDIUM")
        puma_t.set_opacity(0.30)
        puma_t.move_to(puma_box.get_center())
        puma_x = _x_mark(puma_box.get_center(), CRIMSON, 0.22)

        # BCL-2 holds
        bcl_box = _box(SLATE, 2.6, 0.55, fill_opacity=0.06)
        bcl_box.move_to([cascade_x, -0.8, 0])
        bcl_t = Text("BCL-2 holds", font=DISPLAY, color=SLATE,
                     font_size=20, weight="MEDIUM")
        bcl_t.set_opacity(0.40)
        bcl_t.move_to(bcl_box.get_center())

        # Arrow from UV -> p53 flat
        arr1 = _arrow(np.array([cascade_x, 1.62, 0]),
                      np.array([cascade_x, 1.3, 0]), CRIMSON)

        # Cell enters S phase -> divides into 2 daughters
        cell_center = np.array([cascade_x, -1.85, 0])
        cell = Circle(radius=0.4)
        cell.set_fill(CRIMSON, 0.7)
        cell.set_stroke(width=0, opacity=0)
        cell.move_to(cell_center)

        s_phase_arr = _arrow(np.array([cascade_x, -1.15, 0]),
                             np.array([cascade_x, -1.42, 0]), CRIMSON)
        s_phase_lbl = Text("S phase", font=DISPLAY, color=CRIMSON,
                           font_size=20, weight="MEDIUM")
        s_phase_lbl.next_to(s_phase_arr, RIGHT, buff=0.1)

        # Two daughter circles
        d1 = Circle(radius=0.3)
        d1.set_fill(CRIMSON, 0.7)
        d1.set_stroke(width=0, opacity=0)
        d1.move_to(np.array([cascade_x - 0.85, -3.0, 0]))
        d2 = Circle(radius=0.3)
        d2.set_fill(CRIMSON, 0.7)
        d2.set_stroke(width=0, opacity=0)
        d2.move_to(np.array([cascade_x + 0.85, -3.0, 0]))

        dimer_note = Text("500 dimers (illustrative)", font=SERIF,
                          color=CRIMSON, font_size=20, slant=ITALIC)
        dimer_note.next_to(VGroup(d1, d2), DOWN, buff=0.22)

        self.play(FadeIn(divider), FadeIn(l_head), FadeIn(r_head),
                  FadeIn(gone_lbl), run_time=0.6)
        self.play(FadeIn(uv_box), FadeIn(uv_t), run_time=0.5)
        self.play(GrowArrow(arr1), FadeIn(p53_flat_box), FadeIn(p53_flat_t),
                  run_time=0.6)
        self.play(FadeIn(puma_box), FadeIn(puma_t),
                  FadeIn(puma_x, scale=0.7), run_time=0.6)
        self.play(FadeIn(bcl_box), FadeIn(bcl_t), run_time=0.5)
        # Cell enters S phase
        self.play(FadeIn(cell), GrowArrow(s_phase_arr),
                  FadeIn(s_phase_lbl), run_time=0.6)
        # Divides into 2
        self.play(ReplacementTransform(cell, VGroup(d1, d2)), run_time=0.7)
        self.play(FadeIn(dimer_note, shift=UP * 0.08), run_time=0.5)
        self.wait(max(0.5, total - 5.6))


class B15_Endcard(Scene):
    """RECAP — endcard: question -> answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B15"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                     font_size=26, weight="MEDIUM")
        q = Text("Same damage.", font=DISPLAY, color=INK,
                 font_size=38, weight=BOLD)
        a1 = Text("p53 intact: cell dies.", font=DISPLAY, color=TEAL,
                  font_size=34, weight=BOLD)
        a2 = Text("p53 lost: lineage drifts.", font=DISPLAY, color=CRIMSON,
                  font_size=34, weight=BOLD)
        block = VGroup(q, a1, a2).arrange(DOWN, buff=0.22).move_to(UP * 0.15)
        u = Line(a2.get_corner(DL) + DOWN * 0.16, a2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        topic.next_to(block, UP, buff=0.7)
        hinge = Text("p53 is the hinge between damage detected and death executed",
                     font=SERIF, color=INK, font_size=24, slant=ITALIC)
        hinge.next_to(u, DOWN, buff=0.45)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), run_time=0.6)
        self.play(FadeIn(a1), run_time=0.6)
        self.play(FadeIn(a2), Create(u), run_time=0.7)
        self.play(FadeIn(hinge, shift=UP * 0.08), run_time=0.6)
        self.wait(max(0.5, total - 3.0))
