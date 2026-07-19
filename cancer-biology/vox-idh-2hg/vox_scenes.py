"""vox_scenes.py — Why a Metabolic Enzyme Mutation Can Lock Cells
Into an Immature State (vox-idh-2hg, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is own. STILL beats (B02, B10)
have no scene — they compile as slates pending image files in media/.

Render everything:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-idh-2hg

Color law: TEAL #1F6F5C = demethylase active / differentiation possible /
healthy state. CRIMSON #BF3339 = 2HG / blocked / silenced / blast-locked.
GOLD = editor's-pen highlight used ONCE (B08, keyhole). GOLD is FILL ONLY,
NEVER text. SLATE = IDH enzyme box (structural, neutral).

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 11.0, "B03": 13.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 12.0, "B08": 13.0, "B09": 12.0, "B11": 12.0, "B12": 12.0,
    "B13": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _rect(w, h, color, opacity=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return r


def _box(label_text, accent=SLATE, w=2.8, h=1.4, font_size=26):
    """A labeled rectangular box — enzyme or system glyph."""
    box = Rectangle(width=w, height=h)
    box.set_fill(accent, 0.12).set_stroke(accent, 2.2)
    lbl = Text(label_text, font=DISPLAY, color=accent,
               font_size=font_size, weight="MEDIUM")
    if lbl.width > w * 0.88:
        lbl.scale_to_fit_width(w * 0.88)
    lbl.move_to(box)
    return VGroup(box, lbl)


def _molecule(label_text, color, radius=0.28, font_size=20):
    """Small circle glyph for a metabolite."""
    c = Circle(radius=radius)
    c.set_fill(color, 1).set_stroke(width=0, opacity=0)
    lbl = Text(label_text, font=DISPLAY, color=WHITE,
               font_size=font_size, weight="MEDIUM")
    if lbl.width > radius * 1.7:
        lbl.scale_to_fit_width(radius * 1.7)
    lbl.move_to(c)
    return VGroup(c, lbl)


def _arr(start, end, color=INK, stroke_width=3.0):
    """Simple arrow from start to end."""
    a = Arrow(start, end, buff=0.1, color=color,
              stroke_width=stroke_width, max_tip_length_to_length_ratio=0.18)
    return a


def _methyl_dot(pos, color=CRIMSON, r=0.13):
    d = Dot(radius=r, color=color)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    d.move_to(pos)
    return d


def _gene_bar(center, w=2.0, h=0.28, color=TEAL, label="", font_size=18):
    bar = Rectangle(width=w, height=h)
    bar.set_fill(color, 0.18).set_stroke(color, 1.6)
    bar.move_to(center)
    if label:
        lbl = Text(label, font=SERIF, color=color,
                   font_size=font_size, slant=ITALIC)
        lbl.next_to(bar, RIGHT, buff=0.18)
        return VGroup(bar, lbl)
    return VGroup(bar)


def _state_card_simple(title, value, color=CRIMSON, w=2.6, h=1.6):
    """A simple state card: slate background, white title, colored value."""
    bg = Rectangle(width=w, height=h)
    bg.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
    t = Text(title, font=DISPLAY, color=WHITE,
             font_size=16, weight="MEDIUM")
    if t.width > w * 0.86:
        t.scale_to_fit_width(w * 0.86)
    t.move_to(bg.get_top() + DOWN * 0.35)
    v = Text(value, font=DISPLAY, color=color,
             font_size=22, weight="BOLD")
    if v.width > w * 0.86:
        v.scale_to_fit_width(w * 0.86)
    v.next_to(t, DOWN, buff=0.22)
    return VGroup(bg, t, v)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """CARD — title with CANCER BIOLOGY eyebrow (TEAL)."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        t1 = Text("Why a metabolic enzyme mutation", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("can lock cells into an immature state", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.16).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.15, t2.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.75)
        self.play(FadeIn(eye, scale=0.95), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Question(Scene):
    """CARD — THE QUESTION on screen."""
    def construct(self):
        total = DUR["B03"]
        q_label = Text("THE QUESTION", font=DISPLAY, color=CRIMSON,
                       font_size=20, weight="MEDIUM")
        t1 = Text("A metabolic enzyme mutation should", font=SERIF, color=INK,
                  font_size=38, weight=BOLD)
        t2 = Text("change energy production — not", font=SERIF, color=INK,
                  font_size=38, weight=BOLD)
        t3 = Text("freeze development.", font=SERIF, color=CRIMSON,
                  font_size=38, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.14).move_to(UP * 0.3)
        q_label.next_to(block, UP, buff=0.6)
        dek = Text("Why does a single amino acid change in IDH1",
                   font=SERIF, color=INK, font_size=28)
        dek2 = Text("lock cells in an immature, cancer-prone state?",
                    font=SERIF, color=INK, font_size=28)
        dek_block = VGroup(dek, dek2).arrange(DOWN, buff=0.1)
        dek_block.next_to(block, DOWN, buff=0.5)
        # Shape motion: underline grows under t3 (the freeze line)
        u = Line(t3.get_corner(DL) + DOWN * 0.12, t3.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2.5)
        self.play(FadeIn(q_label, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.5)
        self.play(FadeIn(t3), Create(u), run_time=0.6)
        self.play(FadeIn(dek_block, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 3.0))


class B04_TwoSystems(Scene):
    """GRAPHIC — metabolism and differentiation as two separate boxes."""
    def construct(self):
        total = DUR["B04"]
        met_box = _box("METABOLIC\nENZYMES", accent=SLATE, w=3.2, h=1.8, font_size=24)
        met_box.move_to(LEFT * 3.4)
        diff_box = _box("DIFFERENTIATION\nGENES", accent=TEAL, w=3.2, h=1.8, font_size=24)
        diff_box.move_to(RIGHT * 3.4)
        gap_lbl = SerifLabel("no connection expected", INK, size=24)
        gap_lbl.move_to(ORIGIN + UP * 1.6)  # above the barrier, not crossing it
        barrier = DashedLine(ORIGIN + UP * 1.2, ORIGIN + DOWN * 1.2,
                             color=INK, stroke_width=1.5, dash_length=0.18)
        self.play(FadeIn(met_box, shift=RIGHT * 0.5),
                  FadeIn(diff_box, shift=LEFT * 0.5), run_time=1.0)
        self.play(Create(barrier), FadeIn(gap_lbl), run_time=0.9)
        self.wait(max(0.5, total - 1.9))


class B05_CofactorLink(Scene):
    """GRAPHIC — metabolite flows as cofactor to the epigenetic eraser."""
    def construct(self):
        total = DUR["B05"]
        met_box = _box("METABOLIC\nENZYMES", accent=SLATE, w=3.0, h=1.6, font_size=22)
        met_box.move_to(LEFT * 3.6 + UP * 0.4)
        erase_box = _box("EPIGENETIC\nERASERS", accent=TEAL, w=3.0, h=1.6, font_size=22)
        erase_box.move_to(RIGHT * 3.6 + UP * 0.4)
        # Cofactor molecule glyph traveling across
        mol = _molecule("cofactor", TEAL, radius=0.32, font_size=18)
        mol.move_to(met_box.get_right() + RIGHT * 0.5)
        arr = _arr(met_box.get_right() + RIGHT * 0.12,
                   erase_box.get_left() + LEFT * 0.12,
                   color=TEAL, stroke_width=3.0)
        arr_lbl = SerifLabel("feeds demethylases", TEAL, size=22)
        arr_lbl.next_to(arr, UP, buff=0.18)
        gene_chip = LabelChip("gene silencing erased", accent=TEAL, size=22)
        gene_chip.next_to(erase_box, DOWN, buff=0.4)
        self.play(FadeIn(met_box, shift=RIGHT * 0.4),
                  FadeIn(erase_box, shift=LEFT * 0.4), run_time=0.9)
        self.play(GrowArrow(arr), FadeIn(arr_lbl), run_time=0.9)
        self.play(FadeIn(mol), mol.animate.move_to(arr.get_center()), run_time=0.8)
        self.play(FadeIn(gene_chip, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.2))


class B06_NormalIDH(Scene):
    """GRAPHIC — normal IDH: isocitrate → alpha-KG → demethylase → gene ON."""
    def construct(self):
        total = DUR["B06"]
        # IDH enzyme box left
        idh = _box("IDH1\n(normal)", accent=SLATE, w=2.4, h=1.4, font_size=22)
        idh.move_to(LEFT * 4.5 + UP * 0.5)
        # alpha-KG molecule
        akg = _molecule("aKG", TEAL, radius=0.3, font_size=18)
        akg.move_to(LEFT * 1.8 + UP * 0.5)
        arr1 = _arr(idh.get_right() + RIGHT * 0.08,
                    akg.get_left() + LEFT * 0.08, color=TEAL)
        # Demethylase box
        deme = _box("DEME-\nTHYLASE", accent=TEAL, w=2.2, h=1.4, font_size=20)
        deme.move_to(RIGHT * 1.2 + UP * 0.5)
        arr2 = _arr(akg.get_right() + RIGHT * 0.08,
                    deme.get_left() + LEFT * 0.08, color=TEAL)
        akg_lbl = SerifLabel("alpha-KG cofactor", TEAL, size=20)
        akg_lbl.next_to(akg, DOWN, buff=0.25)
        # Gene bar with methyl mark removed
        gene = _gene_bar(RIGHT * 4.5 + UP * 0.5, w=2.0, h=0.32, color=TEAL,
                         label="gene ON")
        arr3 = _arr(deme.get_right() + RIGHT * 0.08,
                    gene[0].get_left() + LEFT * 0.08, color=TEAL)
        # Methyl dot that disappears
        methyl = _methyl_dot(gene[0].get_center() + LEFT * 0.4 + UP * 0.35,
                             color=CRIMSON)
        erase_chip = LabelChip("methyl mark erased", accent=TEAL, size=20)
        erase_chip.move_to(RIGHT * 4.5 + DOWN * 0.6)
        self.play(FadeIn(idh, shift=RIGHT * 0.4), run_time=0.7)
        self.play(GrowArrow(arr1), FadeIn(akg), FadeIn(akg_lbl), run_time=0.8)
        self.play(GrowArrow(arr2), FadeIn(deme), run_time=0.7)
        self.play(GrowArrow(arr3), FadeIn(gene), FadeIn(methyl), run_time=0.7)
        self.play(FadeOut(methyl, scale=0.4), FadeIn(erase_chip), run_time=0.8)
        self.wait(max(0.5, total - 3.7))


class B07_MutantIDH(Scene):
    """GRAPHIC — mutant IDH morphs; alpha-KG diverted to 2HG flood."""
    def construct(self):
        total = DUR["B07"]
        # Start with normal IDH box, then morph to mutant
        idh_normal = _box("IDH1\n(normal)", accent=SLATE, w=2.4, h=1.4, font_size=22)
        idh_normal.move_to(LEFT * 4.2 + UP * 1.0)
        idh_mutant = _box("IDH1\n(mutant)", accent=CRIMSON, w=2.4, h=1.4, font_size=22)
        idh_mutant.move_to(LEFT * 4.2 + UP * 1.0)
        # Old aKG output (crossed out)
        akg_ghost = _molecule("aKG", TEAL, radius=0.28, font_size=17)
        akg_ghost.move_to(LEFT * 1.8 + UP * 1.0).set_opacity(0.3)
        arr_old = _arr(idh_normal.get_right() + RIGHT * 0.08,
                       akg_ghost.get_left() + LEFT * 0.08, color=TEAL)
        arr_old.set_stroke(opacity=0.3)
        cross = Line(arr_old.get_start() + UP * 0.18,
                     arr_old.get_end() + DOWN * 0.18,
                     color=CRIMSON, stroke_width=4)
        cross._qc_intentional = True  # deliberate cross-out line on arrow
        # 2HG molecules flooding right
        hg_positions = [
            RIGHT * 0.2 + UP * 1.8, RIGHT * 1.4 + UP * 2.2,
            RIGHT * 2.6 + UP * 1.5, RIGHT * 3.6 + UP * 2.0,
            RIGHT * 0.8 + DOWN * 0.2, RIGHT * 2.2 + DOWN * 0.4,
            RIGHT * 3.8 + DOWN * 0.1, RIGHT * 4.8 + UP * 1.0,
        ]
        hg_mols = VGroup(*[_molecule("2HG", CRIMSON, radius=0.26, font_size=15)
                           for _ in hg_positions])
        for m, pos in zip(hg_mols, hg_positions):
            m.move_to(pos)
        arr_new = _arr(idh_mutant.get_right() + RIGHT * 0.08,
                       hg_positions[0] + LEFT * 0.3, color=CRIMSON)
        flood_chip = LabelChip("2HG floods the cell", accent=CRIMSON, size=22)
        flood_chip.move_to(RIGHT * 2.5 + DOWN * 1.6)
        mut_lbl = SerifLabel("one amino acid change", CRIMSON, size=22)
        mut_lbl.next_to(idh_mutant, DOWN, buff=0.3)
        self.play(FadeIn(idh_normal), run_time=0.5)
        # Morph: normal IDH to mutant IDH
        self.play(ReplacementTransform(idh_normal, idh_mutant),
                  FadeIn(mut_lbl), run_time=1.0)
        self.play(FadeIn(akg_ghost), FadeIn(arr_old), Create(cross), run_time=0.8)
        self.play(GrowArrow(arr_new), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in hg_mols],
                               lag_ratio=0.08), run_time=1.2)
        self.play(FadeIn(flood_chip, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 4.7))


class B08_WrongKey(Scene):
    """GRAPHIC — 2HG (wrong key) blocks the demethylase active site."""
    def construct(self):
        total = DUR["B08"]

        def _keyhole(center, fill_color=GOLD, h=2.0, w=1.0):
            """Simplified keyhole: circle on top, trapezoid below."""
            circ = Circle(radius=w * 0.42)
            circ.set_fill(fill_color, 0.22).set_stroke(INK, 2.5)
            slot = Rectangle(width=w * 0.38, height=h * 0.55)
            slot.set_fill(fill_color, 0.22).set_stroke(width=0, opacity=0)
            slot.next_to(circ, DOWN, buff=-0.06)
            kh = VGroup(circ, slot)
            kh.move_to(center)
            return kh

        def _key(label, color, center, angle=0):
            """Simple key glyph. Label in INK so it has contrast on any fill."""
            shaft = Rectangle(width=0.9, height=0.22)
            shaft.set_fill(color, 1).set_stroke(width=0, opacity=0)
            head = Circle(radius=0.22)
            head.set_fill(color, 1).set_stroke(width=0, opacity=0)
            head.next_to(shaft, LEFT, buff=0)
            k = VGroup(shaft, head)
            lbl = Text(label, font=DISPLAY, color=INK,
                       font_size=16, weight="BOLD")
            lbl.move_to(shaft)
            k.add(lbl)
            k.rotate(angle)
            k.move_to(center)
            return k

        # Demethylase enzyme as a rectangle with a keyhole cutout label
        deme_box = _box("DEME-\nTHYLASE", accent=TEAL, w=2.8, h=2.2, font_size=20)
        deme_box.move_to(ORIGIN + UP * 0.2)
        active_site_lbl = SerifLabel("active site", INK, size=20)
        active_site_lbl.next_to(deme_box, DOWN, buff=0.2)
        # GOLD highlight keyhole circle (the active site pocket)
        hole = Circle(radius=0.38)
        hole.set_fill(GOLD, 0.45).set_stroke(INK, 2)
        hole.move_to(deme_box[0].get_center() + UP * 0.25)
        # teal key (alpha-KG) — fits and turns
        akg_key = _key("aKG", TEAL, LEFT * 4.8 + UP * 1.0)
        akg_lbl = SerifLabel("alpha-KG (real key)", TEAL, size=20)
        akg_lbl.next_to(akg_key, UP, buff=0.18)
        # crimson key (2HG) — fits but does not turn
        hg_key = _key("2HG", CRIMSON, LEFT * 4.8 + DOWN * 1.2)
        hg_lbl = SerifLabel("2HG (mimic — blocks)", CRIMSON, size=20)
        hg_lbl.next_to(hg_key, DOWN, buff=0.18)
        # Result chips
        good_chip = LabelChip("methyl mark erased", accent=TEAL, size=20)
        good_chip.move_to(RIGHT * 4.2 + UP * 1.0)
        block_chip = LabelChip("mark persists — gene silenced", accent=CRIMSON, size=20)
        block_chip.move_to(RIGHT * 4.2 + DOWN * 2.1)  # well below the arrow
        block_arr = Arrow(RIGHT * 0.2 + DOWN * 1.2, RIGHT * 3.0 + DOWN * 1.2,
                          color=CRIMSON, buff=0.1, stroke_width=3)
        self.play(FadeIn(deme_box), FadeIn(hole), FadeIn(active_site_lbl), run_time=0.8)
        # Phase 1: alpha-KG key enters → gene unsilenced
        self.play(FadeIn(akg_key), FadeIn(akg_lbl), run_time=0.6)
        self.play(akg_key.animate.move_to(hole.get_center()), run_time=0.7)
        self.play(FadeIn(good_chip, shift=LEFT * 0.3), run_time=0.6)
        # Phase 2: 2HG key enters — does not turn
        self.play(FadeOut(akg_key), FadeOut(good_chip), run_time=0.5)
        self.play(FadeIn(hg_key), FadeIn(hg_lbl), run_time=0.6)
        self.play(hg_key.animate.move_to(hole.get_center()), run_time=0.7)
        self.play(GrowArrow(block_arr), FadeIn(block_chip), run_time=0.8)
        self.wait(max(0.5, total - 5.3))


class B09_MethylAccumulate(Scene):
    """GRAPHIC — methyl marks pile up on differentiation gene promoters."""
    def construct(self):
        total = DUR["B09"]
        n_genes = 5
        gene_centers = [LEFT * 3.5 + UP * (1.6 - i * 0.8) for i in range(n_genes)]
        genes = VGroup(*[_gene_bar(c, w=3.0, h=0.28, color=TEAL) for c in gene_centers])
        gene_labels = VGroup(*[Text(f"diff gene {i+1}", font=SERIF, color=TEAL,
                                    font_size=18, slant=ITALIC)
                                .next_to(genes[i][0], RIGHT, buff=0.2)
                                for i in range(n_genes)])
        header = SerifLabel("differentiation gene promoters", TEAL, size=24)
        header.move_to(LEFT * 3.5 + UP * 2.3)
        self.play(FadeIn(genes), FadeIn(gene_labels), FadeIn(header), run_time=0.8)
        # Methyl dots accumulate one by one
        dots = VGroup()
        dot_positions_per_gene = []
        for i, center in enumerate(gene_centers):
            row_dots = [center + LEFT * (0.5 - j * 0.32) + UP * 0.35
                        for j in range(3)]
            dot_positions_per_gene.append(row_dots)
        anims = []
        for row in dot_positions_per_gene:
            for pos in row:
                d = _methyl_dot(pos, color=CRIMSON)
                dots.add(d)
                anims.append(FadeIn(d, scale=0.5))
        self.play(LaggedStart(*anims, lag_ratio=0.07), run_time=1.8)
        # Gene labels turn to SILENCED
        silenced_labels = VGroup(*[Text("SILENCED", font=DISPLAY, color=CRIMSON,
                                        font_size=17, weight="BOLD")
                                   .next_to(genes[i][0], RIGHT, buff=0.2)
                                   for i in range(n_genes)])
        self.play(ReplacementTransform(gene_labels, silenced_labels), run_time=0.9)
        # 2HG annotation
        hg_chip = LabelChip("2HG blocks demethylases", accent=CRIMSON, size=22)
        hg_chip.move_to(RIGHT * 3.0 + DOWN * 0.2)
        self.play(FadeIn(hg_chip, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 4.2))


class B11_DayZero(Scene):
    """GRAPHIC — Day 0 state: three state cards, all red."""
    def construct(self):
        total = DUR["B11"]
        day_lbl = Text("DAY 0", font=DISPLAY, color=INK,
                       font_size=30, weight="BOLD")
        day_lbl.move_to(UP * 2.8)
        card1 = _state_card_simple("2HG LEVEL", "1000x normal", color=CRIMSON,
                                    w=2.8, h=1.8)
        card2 = _state_card_simple("DEMETHYLASES", "10% active", color=CRIMSON,
                                    w=2.8, h=1.8)
        card3 = _state_card_simple("BLAST COUNT", "high", color=CRIMSON,
                                    w=2.8, h=1.8)
        cards = VGroup(card1, card2, card3).arrange(RIGHT, buff=0.5)
        cards.move_to(UP * 0.3)
        illustr = SerifLabel("illustrative", INK, size=20)
        illustr.move_to(DOWN * 2.0)
        self.play(FadeIn(day_lbl), run_time=0.4)
        self.play(FadeIn(card1, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(card2, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(card3, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(illustr), run_time=0.4)
        self.wait(max(0.5, total - 2.3))


class B12_DayTimeline(Scene):
    """GRAPHIC — Day 14 and Day 28 columns: crimson to teal recovery arc."""
    def construct(self):
        total = DUR["B12"]
        # Column headers
        headers = ["DAY 0", "DAY 14", "DAY 28"]
        header_colors = [CRIMSON, INK, TEAL]
        header_texts = VGroup(*[
            Text(h, font=DISPLAY, color=c, font_size=22, weight="BOLD")
            for h, c in zip(headers, header_colors)
        ])
        col_xs = [-3.8, 0.0, 3.8]
        for txt, x in zip(header_texts, col_xs):
            txt.move_to(UP * 2.6 + RIGHT * x)

        row_labels = ["2HG LEVEL", "DEMETHYLASES", "BLASTS"]
        row_values_0   = ["1000x", "10% active", "high"]
        row_values_14  = ["500x", "50% active", "high"]
        row_values_28  = ["near normal", "90% active", "maturing"]
        row_colors_0   = [CRIMSON, CRIMSON, CRIMSON]
        row_colors_14  = [CRIMSON, TEAL, CRIMSON]
        row_colors_28  = [TEAL, TEAL, TEAL]

        # Build a 3-column table
        row_ys = [1.1, 0.0, -1.1]
        all_cells = VGroup()
        for row_i, (rl, y) in enumerate(zip(row_labels, row_ys)):
            row_lbl = Text(rl, font=DISPLAY, color=INK,
                           font_size=16, weight="MEDIUM")
            row_lbl.move_to(LEFT * 5.8 + UP * y)
            all_cells.add(row_lbl)
            for col_i, (vals, colors, x) in enumerate(zip(
                    [row_values_0, row_values_14, row_values_28],
                    [row_colors_0, row_colors_14, row_colors_28],
                    col_xs)):
                cell = Text(vals[row_i], font=DISPLAY,
                            color=colors[row_i], font_size=18, weight="BOLD")
                cell.move_to(UP * y + RIGHT * x)
                all_cells.add(cell)

        illustr = SerifLabel("illustrative", INK, size=20)
        illustr.move_to(DOWN * 2.1)

        self.play(FadeIn(header_texts[0]), run_time=0.4)
        # Day 0 column
        day0_cells = VGroup(*[all_cells[1 + i * 4] for i in range(3)])
        for i in range(3):
            self.add(all_cells[i * 4])  # row labels
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2)
                                 for c in day0_cells], lag_ratio=0.12), run_time=0.8)
        # Day 14 column
        self.play(FadeIn(header_texts[1]), run_time=0.4)
        day14_cells = VGroup(*[all_cells[2 + i * 4] for i in range(3)])
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2)
                                 for c in day14_cells], lag_ratio=0.12), run_time=0.8)
        # Day 28 column
        self.play(FadeIn(header_texts[2]), run_time=0.4)
        day28_cells = VGroup(*[all_cells[3 + i * 4] for i in range(3)])
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2)
                                 for c in day28_cells], lag_ratio=0.12), run_time=0.8)
        self.play(FadeIn(illustr), run_time=0.4)
        self.wait(max(0.5, total - 4.0))


class B13_End(Scene):
    """CARD — endcard: question -> answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B13"]
        kicker = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        t1 = Text("2HG mimics alpha-KG —", font=SERIF, color=INK,
                  font_size=44, weight=BOLD)
        t2 = Text("fits the demethylase but blocks it,", font=SERIF, color=INK,
                  font_size=40, weight=BOLD)
        t3 = Text("locking cells in an immature state.", font=SERIF, color=CRIMSON,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.16).move_to(UP * 0.15)
        u = Line(t3.get_corner(DL) + DOWN * 0.15, t3.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        kicker.next_to(block, UP, buff=0.65)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), run_time=0.6)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.4))
