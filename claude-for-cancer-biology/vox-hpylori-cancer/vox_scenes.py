"""vox_scenes.py — Why the Bacteria That Cause Ulcers Also Cause Cancer
(vox-hpylori-cancer, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is STILL (ai media
slot) and has no scene here — it renders as a slate until the plate lands.

Render everything:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-hpylori-cancer

Color law: TEAL = eradicated/inflammation-free/no cancer progression;
           CRIMSON = persistent infection/inflammatory damage/advancing cascade.
GOLD = editor's pen highlight, never text.
Exclusions: no CagA biochemistry; no H. pylori virulence factor taxonomy;
no HPV or other viral carcinogens; no aflatoxin interaction; no Nobel Prize.

Gate B: every zero-width stroke is also zero-opacity.
"""
import sys, json, os
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _node(label, color, w=2.6, h=0.68):
    """Filled rounded rectangle node with white Montserrat label."""
    box = RoundedRectangle(width=w, height=h, corner_radius=0.12)
    box.set_fill(color, 1).set_stroke(width=0, opacity=0)
    txt = Text(label.upper(), font=DISPLAY, color=WHITE,
               font_size=int(22 * 0.88), weight="MEDIUM")
    if txt.width > w * 0.84:
        txt.scale_to_fit_width(w * 0.84)
    txt.move_to(box.get_center())
    return VGroup(box, txt)


def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=3,
                 max_tip_length_to_length_ratio=0.18, buff=0.08)


def _bar_rect(w, h, color, opacity=1.0):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return b


def _stage_block(label, color, w=2.0, h=0.82):
    """A Correa cascade stratum block."""
    box = Rectangle(width=w, height=h)
    box.set_fill(color, 1).set_stroke(width=0, opacity=0)
    txt = Text(label, font=DISPLAY, color=WHITE,
               font_size=int(19 * 0.88), weight="MEDIUM")
    if txt.width > w * 0.84:
        txt.scale_to_fit_width(w * 0.84)
    txt.move_to(box.get_center())
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """Cold open title card."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Ulcer Bacteria Also Cause Cancer", font=DISPLAY, color=INK,
                  font_size=24, weight=BOLD)
        t2 = Text("Through Decades of Inflammation", font=DISPLAY, color=CRIMSON,
                  font_size=24, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    """THE QUESTION beat — named on screen AND in narration."""
    def construct(self):
        total = DUR["B03"]
        q_label = LabelChip("THE QUESTION", accent=SLATE, size=22)
        q_text1 = Text("Why does a curable bacterial infection", font=SERIF,
                       color=INK, font_size=38, weight=BOLD)
        q_text2 = Text("cause cancer after 30-50 years?", font=SERIF,
                       color=INK, font_size=38, weight=BOLD)
        block = VGroup(q_text1, q_text2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        q_label.next_to(block, UP, buff=0.7)
        u = Line(q_text2.get_corner(DL) + DOWN * 0.14,
                 q_text2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q_label), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B04_NaiveExpectation(Scene):
    """THE PROBLEM — direct oncogene model vs H. pylori reality."""
    def construct(self):
        total = DUR["B04"]

        # Left column: DIRECT ONCOGENE (TEAL) — simple one-step model
        l_head = LabelChip("DIRECT ONCOGENE", accent=TEAL, size=20)
        pathogen_l = _node("Pathogen", TEAL, w=2.2)
        onco_l = _node("Oncogene", TEAL, w=2.2)
        cancer_l = _node("Cancer Driver", TEAL, w=2.2)
        l_col = VGroup(pathogen_l, onco_l, cancer_l).arrange(DOWN, buff=0.5)
        l_col.move_to(LEFT * 3.2 + DOWN * 0.2)
        l_head.next_to(l_col, UP, buff=0.35)
        arr_l1 = _arrow(pathogen_l.get_bottom(), onco_l.get_top(), TEAL)
        arr_l2 = _arrow(onco_l.get_bottom(), cancer_l.get_top(), TEAL)

        # Right column: H. PYLORI (CRIMSON) — CagA doesn't close
        r_head = LabelChip("H. PYLORI", accent=CRIMSON, size=20)
        pathogen_r = _node("H. pylori", CRIMSON, w=2.2)
        caga_r = _node("CagA", CRIMSON, w=2.2)
        no_driver = _node("No driver", SLATE, w=2.2)
        r_col = VGroup(pathogen_r, caga_r, no_driver).arrange(DOWN, buff=0.5)
        r_col.move_to(RIGHT * 3.2 + DOWN * 0.2)
        r_head.next_to(r_col, UP, buff=0.35)
        arr_r1 = _arrow(pathogen_r.get_bottom(), caga_r.get_top(), CRIMSON)
        arr_r2 = _arrow(caga_r.get_bottom(), no_driver.get_top(), CRIMSON)

        # Cross mark on right bottom node
        cx = no_driver.get_center()
        cross_h = Line(cx + LEFT * 0.6, cx + RIGHT * 0.6,
                       color=CRIMSON, stroke_width=5)
        cross_v = Line(cx + UP * 0.25, cx + DOWN * 0.25,
                       color=CRIMSON, stroke_width=5)

        self.play(
            FadeIn(l_head), FadeIn(l_col),
            FadeIn(r_head), FadeIn(r_col),
            run_time=1.0
        )
        self.play(
            Create(arr_l1), Create(arr_l2),
            Create(arr_r1), Create(arr_r2),
            run_time=1.0
        )
        self.play(Create(cross_h), Create(cross_v), run_time=0.7)
        self.wait(max(0.3, total - 2.7))


class B05_MostNeverGetCancer(Scene):
    """THE PROBLEM — rarity: isotype grid of 100 carriers."""
    def construct(self):
        total = DUR["B05"]

        # 100 dots: ~95 TEAL, 5 CRIMSON (illustrative proportion)
        teal_count = 95
        crimson_count = 5
        colors = [TEAL] * teal_count + [CRIMSON] * crimson_count
        per_row = 10
        dot_size = 0.22
        gap = 0.15
        dots = VGroup()
        for i, c in enumerate(colors):
            d = Circle(radius=dot_size / 2)
            d.set_fill(c, 1).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * (i % per_row) * (dot_size + gap)
                      + DOWN * (i // per_row) * (dot_size + gap))
            dots.add(d)
        dots.move_to(ORIGIN + DOWN * 0.2)

        headline = Text("100 H. pylori carriers", font=DISPLAY, color=INK,
                        font_size=22)
        headline.next_to(dots, UP, buff=0.45)

        teal_label = SerifLabel("no gastric cancer (95)", accent=TEAL, size=24)
        crimson_label = SerifLabel("cancer risk (5)", accent=CRIMSON, size=24)
        legend = VGroup(teal_label, crimson_label).arrange(RIGHT, buff=0.8)
        legend.next_to(dots, DOWN, buff=0.45)

        self.play(FadeIn(headline), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in dots], lag_ratio=0.008),
            run_time=1.8
        )
        self.play(FadeIn(teal_label), FadeIn(crimson_label), run_time=0.7)
        self.wait(max(0.3, total - 3.0))


class B06_SectionCard(Scene):
    """Section card — THE MECHANISM."""
    def construct(self):
        total = DUR["B06"]
        chip = LabelChip("THE MECHANISM", accent=SLATE, size=30)
        chip.move_to(ORIGIN)
        self.play(FadeIn(chip, scale=0.9), run_time=0.6)
        self.play(chip.animate.scale(1.05), run_time=0.4)
        self.wait(max(0.3, total - 1.0))


class B07_PersistentEngine(Scene):
    """THE MECHANISM — persistent colonization drives immune response and ROS."""
    def construct(self):
        total = DUR["B07"]

        # Bacterium at center-left
        bact = _node("H. pylori", CRIMSON, w=2.4)
        bact.move_to(LEFT * 4.5 + UP * 0.2)
        bact_label = SerifLabel("persists indefinitely", CRIMSON, size=22)
        bact_label.next_to(bact, DOWN, buff=0.2)

        # Immune cells
        immune = _node("Neutrophils / Macrophages", CRIMSON, w=3.2)
        immune.move_to(ORIGIN + UP * 0.2)

        # DNA damage node
        dna = _node("DNA Damage", CRIMSON, w=2.4)
        dna.move_to(RIGHT * 4.2 + UP * 0.2)

        # ROS label
        ros_label = SerifLabel("reactive oxygen + nitrogen species", CRIMSON, size=21)
        ros_label.next_to(immune, DOWN, buff=0.35)

        arr1 = _arrow(bact.get_right(), immune.get_left(), CRIMSON)
        arr2 = _arrow(immune.get_right(), dna.get_left(), CRIMSON)

        # Loop arrow from dna back to immune (cycle)
        loop_start = dna.get_bottom() + DOWN * 0.15
        loop_end = immune.get_bottom() + DOWN * 0.15
        loop_mid = (loop_start + loop_end) / 2 + DOWN * 0.6
        loop = CubicBezier(loop_start, loop_start + DOWN * 0.5,
                           loop_end + DOWN * 0.5, loop_end,
                           color=CRIMSON, stroke_width=2)

        self.play(FadeIn(bact), FadeIn(bact_label), run_time=0.7)
        self.play(Create(arr1), FadeIn(immune), run_time=0.8)
        self.play(FadeIn(ros_label), run_time=0.5)
        self.play(Create(arr2), FadeIn(dna), run_time=0.8)
        self.play(Create(loop), run_time=0.7)
        self.wait(max(0.3, total - 3.5))


class B08_CompensatoryRegeneration(Scene):
    """THE MECHANISM — DNA damage -> cell division -> mutation accumulation."""
    def construct(self):
        total = DUR["B08"]

        # Timeline bar
        bar_bg = Rectangle(width=11.0, height=0.5)
        bar_bg.set_fill(SLATE, 0.18).set_stroke(SLATE, 1.2)
        bar_bg.move_to(ORIGIN + DOWN * 0.3)

        bar_label = SerifLabel("gastric epithelium over time", SLATE, size=23)
        bar_label.next_to(bar_bg, UP, buff=0.35)

        # Accumulating mutation marks (small CRIMSON squares)
        mark_positions = [
            -4.8, -3.9, -2.8, -1.7, -0.6, 0.5, 1.5, 2.5, 3.4, 4.3
        ]
        marks = VGroup()
        for x in mark_positions:
            m = Rectangle(width=0.18, height=0.42)
            m.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            m.move_to(RIGHT * x + DOWN * 0.3)
            marks.add(m)

        div_label = LabelChip("elevated cell division", accent=CRIMSON, size=22)
        div_label.next_to(bar_bg, DOWN, buff=0.4)

        self.play(FadeIn(bar_bg), FadeIn(bar_label), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(m, scale=0.7) for m in marks], lag_ratio=0.1),
            run_time=1.5
        )
        self.play(FadeIn(div_label), run_time=0.6)
        self.wait(max(0.3, total - 2.8))


class B09_CorreaCascade(Scene):
    """THE MECHANISM — the Correa cascade as geological strata."""
    def construct(self):
        total = DUR["B09"]

        decades_label = SerifLabel("decades of inflammatory pressure", CRIMSON, size=22)
        decades_label.move_to(UP * 3.1)

        # Five stage blocks accumulating left to right
        stage_names = ["Gastritis", "Atrophy", "Metaplasia", "Dysplasia", "Adenocarcinoma"]
        # Color gradient from light CRIMSON to deep CRIMSON: use opacity for staging
        stage_colors = [
            "#D4737A",  # lightest — gastritis
            "#CC5C63",  # atrophy
            "#BF3339",  # metaplasia (CRIMSON proper)
            "#A02B30",  # dysplasia
            "#7A1F24",  # adenocarcinoma — deepest
        ]

        stage_blocks = VGroup()
        block_w = 2.05
        block_h = 1.4
        for i, (name, col) in enumerate(zip(stage_names, stage_colors)):
            blk = _stage_block(name, col, w=block_w, h=block_h)
            blk.move_to(RIGHT * (i * (block_w + 0.12) - 4.2) + UP * 0.3)
            stage_blocks.add(blk)

        # Bacterium engine label at far left
        engine_label = LabelChip("H. pylori engine", accent=CRIMSON, size=19)
        engine_label.next_to(stage_blocks[0], DOWN, buff=0.45)

        # Arrows between stages
        arrows = VGroup()
        for i in range(len(stage_blocks) - 1):
            a = _arrow(
                stage_blocks[i].get_right(),
                stage_blocks[i + 1].get_left(),
                CRIMSON
            )
            arrows.add(a)

        self.play(FadeIn(decades_label), run_time=0.5)
        for i, blk in enumerate(stage_blocks):
            self.play(FadeIn(blk, shift=UP * 0.15), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)
        self.play(FadeIn(engine_label), run_time=0.5)
        self.wait(max(0.3, total - (0.5 + 5 * 0.5 + 4 * 0.3 + 0.5)))


class B10_EradicationVsNoEradication(Scene):
    """THE IMPLICATION — two-arm comparison: eradication stops cascade."""
    def construct(self):
        total = DUR["B10"]

        # --- Left arm: TEAL — eradication
        l_head = LabelChip("ERADICATED", accent=TEAL, size=20)
        l_bact = _node("H. pylori", TEAL, w=2.2)
        l_erase = _node("Eradicated Y1", TEAL, w=2.2)
        l_out = _node("Low cancer risk", TEAL, w=2.2)
        l_col = VGroup(l_bact, l_erase, l_out).arrange(DOWN, buff=0.45)
        l_col.move_to(LEFT * 3.2 + DOWN * 0.1)
        l_head.next_to(l_col, UP, buff=0.3)

        l_arr1 = _arrow(l_bact.get_bottom(), l_erase.get_top(), TEAL)
        l_arr2 = _arrow(l_erase.get_bottom(), l_out.get_top(), TEAL)

        reduction = SerifLabel("~35% less gastric cancer", TEAL, size=23)
        reduction.next_to(l_col, DOWN, buff=0.32)

        # --- Right arm: CRIMSON — no eradication
        r_head = LabelChip("NOT ERADICATED", accent=CRIMSON, size=20)
        r_bact = _node("H. pylori", CRIMSON, w=2.2)
        r_cascade = _node("Correa cascade", CRIMSON, w=2.2)
        r_out = _node("Adenocarcinoma", CRIMSON, w=2.2)
        r_col = VGroup(r_bact, r_cascade, r_out).arrange(DOWN, buff=0.45)
        r_col.move_to(RIGHT * 3.2 + DOWN * 0.1)
        r_head.next_to(r_col, UP, buff=0.3)

        r_arr1 = _arrow(r_bact.get_bottom(), r_cascade.get_top(), CRIMSON)
        r_arr2 = _arrow(r_cascade.get_bottom(), r_out.get_top(), CRIMSON)

        self.play(
            FadeIn(l_head), FadeIn(l_col),
            FadeIn(r_head), FadeIn(r_col),
            run_time=1.0
        )
        self.play(
            Create(l_arr1), Create(l_arr2),
            Create(r_arr1), Create(r_arr2),
            run_time=1.0
        )
        self.play(FadeIn(reduction), run_time=0.7)
        self.wait(max(0.3, total - 2.7))


class B11_ProbabilisticThreshold(Scene):
    """THE IMPLICATION — why only some infected people develop cancer."""
    def construct(self):
        total = DUR["B11"]

        headline = Text("H. pylori carriers: probabilistic risk", font=DISPLAY,
                        color=INK, font_size=20)
        headline.move_to(UP * 3.2)

        # Threshold line
        thresh = Line(LEFT * 5.5 + UP * 0.5, RIGHT * 5.5 + UP * 0.5,
                      color=INK, stroke_width=2.5)
        thresh_label = SerifLabel("cancer threshold", INK, size=22)
        thresh_label.next_to(headline, DOWN, buff=0.25)

        # Below threshold: TEAL dots (no cancer)
        below_positions = [
            (-4.5, -0.5), (-3.2, -0.9), (-2.0, -0.3), (-1.0, -1.0),
            (0.2, -0.7), (1.3, -0.4), (2.5, -0.8), (3.6, -0.2),
            (-3.8, -1.5), (-0.5, -1.4), (1.8, -1.3), (4.0, -1.1),
        ]
        # Above threshold: CRIMSON dots (cancer)
        above_positions = [
            (-1.5, 1.0), (0.8, 1.3), (3.0, 0.9),
        ]

        below_dots = VGroup()
        for x, y in below_positions:
            d = Circle(radius=0.19)
            d.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x + UP * y + DOWN * 0.4)
            below_dots.add(d)

        above_dots = VGroup()
        for x, y in above_positions:
            d = Circle(radius=0.19)
            d.set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * x + UP * y + DOWN * 0.4)
            above_dots.add(d)

        teal_leg = SerifLabel("no cancer", TEAL, size=22)
        crim_leg = SerifLabel("cancer", CRIMSON, size=22)
        legend = VGroup(teal_leg, crim_leg).arrange(RIGHT, buff=1.0)
        legend.move_to(DOWN * 2.9)

        self.play(FadeIn(headline), run_time=0.5)
        self.play(Create(thresh), FadeIn(thresh_label), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in below_dots], lag_ratio=0.05),
            run_time=0.9
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.85) for d in above_dots], lag_ratio=0.1),
            run_time=0.6
        )
        self.play(FadeIn(teal_leg), FadeIn(crim_leg), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


class B12_TwoVillages(Scene):
    """THE EXAMPLE — two villages, Japan: eradication vs no eradication. Illustrative."""
    def construct(self):
        total = DUR["B12"]

        headline = Text("Two villages, rural Japan (illustrative)", font=DISPLAY,
                        color=INK, font_size=20)
        headline.move_to(UP * 3.2)

        year_labels = ["1990", "2000", "2010", "2020"]

        # Village A (TEAL) — eradicated in ~2000, cancer falls
        va_head = LabelChip("Village A — eradicated", accent=TEAL, size=20)
        va_vals = [1.0, 0.55, 0.35, 0.25]   # relative cancer incidence
        va_bars = VGroup()
        bar_w = 0.55
        for i, v in enumerate(va_vals):
            b = _bar_rect(bar_w, v * 2.5, TEAL)
            b.move_to(LEFT * 3.5 + RIGHT * i * 0.85 + DOWN * (3.0 - v * 2.5) / 2)
            va_bars.add(b)
        va_head.next_to(va_bars, UP, buff=0.4)

        # Village B (CRIMSON) — no eradication, stays high
        vb_head = LabelChip("Village B — no eradication", accent=CRIMSON, size=20)
        vb_vals = [1.0, 0.95, 0.98, 1.0]   # stays elevated
        vb_bars = VGroup()
        for i, v in enumerate(vb_vals):
            b = _bar_rect(bar_w, v * 2.5, CRIMSON)
            b.move_to(RIGHT * 1.5 + RIGHT * i * 0.85 + DOWN * (3.0 - v * 2.5) / 2)
            vb_bars.add(b)
        vb_head.next_to(vb_bars, UP, buff=0.4)

        # 40% label
        reduction_label = SerifLabel("40% lower by 2020", TEAL, size=23)
        reduction_label.next_to(va_bars, DOWN, buff=0.35)

        self.play(FadeIn(headline), run_time=0.5)
        self.play(FadeIn(va_head), FadeIn(vb_head), run_time=0.6)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in va_bars], lag_ratio=0.12),
            LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in vb_bars], lag_ratio=0.12),
            run_time=1.4
        )
        self.play(FadeIn(reduction_label), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


class B13_Endcard(Scene):
    """RECAP endcard — question, answer, topic."""
    def construct(self):
        total = DUR["B13"]

        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=17)
        q = Text("Why a curable bacterial infection", font=SERIF,
                 color=INK, font_size=28, weight=BOLD)
        q2 = Text("causes cancer after decades:", font=SERIF,
                  color=INK, font_size=28, weight=BOLD)
        a = Text("Chronic inflammation — not a cancer gene —", font=SERIF,
                 color=CRIMSON, font_size=26)
        a2 = Text("assembles the driver mutations over 30-50 years.", font=SERIF,
                  color=CRIMSON, font_size=26)
        block = VGroup(q, q2, a, a2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(a2.get_corner(DL) + DOWN * 0.12, a2.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.55)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), FadeIn(q2), run_time=0.8)
        self.play(FadeIn(a), FadeIn(a2), Create(u), run_time=1.0)
        self.wait(max(0.3, total - 2.3))
