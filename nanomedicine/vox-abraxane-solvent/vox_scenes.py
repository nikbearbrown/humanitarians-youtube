"""vox_scenes.py — The Cancer Drug Where the Solvent, Not the Drug, Was the Danger
(vox-abraxane-solvent, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 and B10 are STILL (ai media slots) — no scene here.

Color law: TEAL #1F6F5C = albumin / safe / the fix; CRIMSON #BF3339 = Cremophor
/ danger / hypersensitivity. GOLD = editor's pen highlight, once (B06). Two
accents max; never swap mid-film.

Exclusions: NO SPARC uptake, NO liposomes/PLGA, NO three-benefit framework, NO
manufacturing scale-up.

Gate B: every zero-width stroke is also zero-opacity.
"""
import sys, json, os, pathlib
# vox_graphics.py lives in the toolkit at books/vox/aspects/explainer/vox-explainer/manim/
# This reel is at books/cancer-nanomedicine/youtube/vox-abraxane-solvent/
# So resolve 3 parents up (to books/) then into vox/aspects/explainer/vox-explainer/manim
_HERE = pathlib.Path(__file__).resolve().parent
_BOOKS = _HERE.parents[2]   # books/
_GFX_DIR = _BOOKS / "vox" / "aspects" / "explainer" / "vox-explainer" / "manim"
if str(_GFX_DIR) not in sys.path:
    sys.path.insert(0, str(_GFX_DIR))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 16)}

# ---------------------------------------------------------------- B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Cancer Drug Where the Solvent,", font=DISPLAY, color=INK,
                  font_size=26, weight=BOLD)
        t2 = Text("Not the Drug, Was the Danger", font=DISPLAY, color=CRIMSON,
                  font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))

# ---------------------------------------------------------------- B03 Insolubility Problem

class B03_InsolubilityProblem(Scene):
    def construct(self):
        total = DUR["B03"]
        # drug clumps that fail to dissolve — small squares clustering
        clumps = VGroup()
        import numpy as np
        rng = np.random.default_rng(42)
        positions = [
            LEFT * 2.2 + UP * 0.8, LEFT * 1.4 + UP * 0.4, LEFT * 1.8 + DOWN * 0.2,
            LEFT * 0.8 + UP * 1.0, LEFT * 0.5 + DOWN * 0.5, ORIGIN + UP * 0.3,
            RIGHT * 0.6 + UP * 0.7, RIGHT * 1.2 + DOWN * 0.3, RIGHT * 1.8 + UP * 0.5,
            RIGHT * 2.2 + DOWN * 0.8,
        ]
        for pos in positions:
            sq = Square(0.22).set_fill(INK, 0.85).set_stroke(width=0, opacity=0)
            sq.move_to(pos)
            clumps.add(sq)
        # water wave lines (horizontal, light blue-grey)
        wave_color = "#A8C0C8"
        waves = VGroup()
        for y in [-2.0, -1.5, -1.0]:
            w = Line(LEFT * 5.5 + UP * y, RIGHT * 5.5 + UP * y,
                     stroke_width=1.2, color=wave_color)
            waves.add(w)
        label_water = Text("water", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        label_water.to_corner(DL, buff=0.6)
        chip = LabelChip("Nearly Insoluble in Water", accent=CRIMSON, size=22)
        chip.to_edge(DOWN, buff=0.8)
        # animation: waves fade in, clumps appear (scattered, not dissolved)
        self.play(FadeIn(waves), FadeIn(label_water), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(sq) for sq in clumps],
                               lag_ratio=0.08, run_time=1.4))
        # clumps shift slightly toward each other (clumping motion, not dissolving)
        shifts = [RIGHT * 0.18, LEFT * 0.15, UP * 0.12, DOWN * 0.14, RIGHT * 0.10,
                  LEFT * 0.08, UP * 0.16, DOWN * 0.10, LEFT * 0.12, RIGHT * 0.14]
        self.play(AnimationGroup(*[sq.animate.shift(s)
                                   for sq, s in zip(clumps, shifts)],
                                 run_time=1.0))
        self.play(FadeIn(chip, shift=UP * 0.12), run_time=0.6)
        self.wait(max(0.3, total - 3.6))

# ---------------------------------------------------------------- B04 The Question

class B04_Question(Scene):
    def construct(self):
        total = DUR["B04"]
        q1 = Text("Paclitaxel works against cancer.", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        q2 = Text("It also caused severe hypersensitivity", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        q3 = Text("reactions for decades.", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        q4 = Text("The drug didn't change.", font=SERIF, color=INK,
                  font_size=32, slant=ITALIC)
        q5 = Text("What did — and why did the reactions stop?", font=DISPLAY,
                  color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(q1, q2, q3, q4, q5).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        block.move_to(ORIGIN + LEFT * 0.2)
        rule_top = Line(block.get_corner(UL) + LEFT * 0.1 + UP * 0.18,
                        block.get_corner(UR) + RIGHT * 0.1 + UP * 0.18,
                        stroke_width=1.6, color=SLATE)
        rule_bot = Line(block.get_corner(DL) + LEFT * 0.1 + DOWN * 0.18,
                        block.get_corner(DR) + RIGHT * 0.1 + DOWN * 0.18,
                        stroke_width=1.6, color=SLATE)
        self.play(Create(rule_top), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT * 0.1)
                                 for line in block],
                               lag_ratio=0.18, run_time=2.0))
        self.play(Create(rule_bot), run_time=0.4)
        self.wait(max(0.3, total - 2.8))

# ---------------------------------------------------------------- B05 Cremophor Cascade

class B05_CremophorCascade(Scene):
    def construct(self):
        total = DUR["B05"]
        # Cremophor pool label on left
        pool_rect = Rectangle(width=2.8, height=1.0)
        pool_rect.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.2)
        pool_rect.to_edge(LEFT, buff=1.0).shift(UP * 0.5)
        pool_label = Text("Cremophor EL", font=DISPLAY, color=CRIMSON, font_size=20,
                          weight=BOLD)
        pool_label.move_to(pool_rect)
        pool_sub = Text("castor-oil surfactant", font=SERIF, color=CRIMSON,
                        font_size=18, slant=ITALIC)
        pool_sub.next_to(pool_rect, DOWN, buff=0.18)
        # mast cell circle
        mast_circle = Circle(radius=0.7).set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2.5)
        mast_circle.move_to(RIGHT * 0.8 + UP * 0.5)
        mast_label = Text("mast cell", font=SERIF, color=CRIMSON, font_size=20,
                          slant=ITALIC)
        mast_label.next_to(mast_circle, DOWN, buff=0.2)
        # arrow from pool to mast cell
        arrow = Arrow(pool_rect.get_right(), mast_circle.get_left(),
                      color=CRIMSON, stroke_width=3, buff=0.12,
                      max_tip_length_to_length_ratio=0.18)
        arrow.set_stroke(opacity=1)
        # cascade labels below
        broncho = LabelChip("Bronchospasm", accent=CRIMSON, size=20)
        hypoten = LabelChip("Hypotension", accent=CRIMSON, size=20)
        cascade = VGroup(broncho, hypoten).arrange(RIGHT, buff=0.5)
        cascade.to_edge(DOWN, buff=1.0)
        # radiating lines from mast cell
        spike_angs = [30, 60, 90, 120, 150, 210, 240, 270, 300, 330]
        spikes = VGroup()
        for ang in spike_angs:
            import numpy as np
            dx = np.cos(np.radians(ang)) * 1.1
            dy = np.sin(np.radians(ang)) * 1.1
            sp = Line(mast_circle.get_center(),
                      mast_circle.get_center() + RIGHT * dx + UP * dy,
                      stroke_width=2, color=CRIMSON)
            spikes.add(sp)
        # animate
        self.play(FadeIn(pool_rect), FadeIn(pool_label), FadeIn(pool_sub),
                  run_time=0.7)
        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(GrowFromCenter(mast_circle), FadeIn(mast_label), run_time=0.7)
        self.play(LaggedStart(*[Create(sp) for sp in spikes],
                               lag_ratio=0.05, run_time=0.8))
        self.play(FadeIn(cascade, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.6))

# ---------------------------------------------------------------- B06 Protocol Document

class B06_Protocol(Scene):
    def construct(self):
        _quote_scene(self,
                     "Premedicate: steroids, antihistamines. "
                     "Keep epinephrine at bedside. "
                     "Infuse over 3 hours through a 0.22-micron filter.",
                     "— standard Taxol infusion protocol",
                     None,
                     "epinephrine",
                     DUR["B06"])

# ---------------------------------------------------------------- B07 Albumin Binding

class B07_AlbuminBinding(Scene):
    def construct(self):
        total = DUR["B07"]
        # albumin protein — simplified folded shape using rounded blobs
        albumin_body = Ellipse(width=2.2, height=1.4)
        albumin_body.set_fill(TEAL, 0.22).set_stroke(TEAL, 2.5)
        albumin_body.move_to(LEFT * 0.5 + UP * 0.2)
        albumin_label = Text("albumin", font=SERIF, color=TEAL, font_size=26,
                             slant=ITALIC, weight=BOLD)
        albumin_label.next_to(albumin_body, UP, buff=0.28)
        sub_label = Text("most abundant blood protein", font=SERIF, color=TEAL,
                         font_size=19, slant=ITALIC)
        sub_label.next_to(albumin_body, DOWN, buff=0.2)
        # drug molecule squares approaching from right
        drug_squares = VGroup()
        approach_positions = [
            RIGHT * 3.5 + UP * 0.6,
            RIGHT * 3.8 + UP * 0.0,
            RIGHT * 3.5 + DOWN * 0.5,
        ]
        for pos in approach_positions:
            sq = Square(0.28).set_fill(INK, 0.85).set_stroke(width=0, opacity=0)
            sq.move_to(pos)
            drug_squares.add(sq)
        # binding pocket positions on albumin surface
        bind_positions = [
            RIGHT * 0.4 + UP * 0.5,
            RIGHT * 0.7 + UP * 0.0,
            RIGHT * 0.4 + DOWN * 0.4,
        ]
        # chip for the nanoparticle
        chip = LabelChip("Albumin Nanoparticle ~130 nm", accent=TEAL, size=20)
        chip.to_edge(DOWN, buff=0.9)
        # animate
        self.play(GrowFromCenter(albumin_body), FadeIn(albumin_label),
                  FadeIn(sub_label), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(sq) for sq in drug_squares],
                               lag_ratio=0.18, run_time=0.7))
        # drug molecules move to bind into albumin
        self.play(AnimationGroup(
            *[sq.animate.move_to(bp)
              for sq, bp in zip(drug_squares, bind_positions)],
            run_time=1.2))
        self.play(FadeIn(chip, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.5))

# ---------------------------------------------------------------- B08 Solvent Drain

class B08_SolventDrain(Scene):
    def construct(self):
        total = DUR["B08"]
        # crimson pool (Cremophor) and teal albumin nanoparticle side by side
        # crimson pool on left
        pool = Rectangle(width=3.0, height=1.6)
        pool.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2.2)
        pool.to_edge(LEFT, buff=1.2).shift(UP * 0.4)
        pool_label = Text("Cremophor EL", font=DISPLAY, color=CRIMSON,
                          font_size=20, weight=BOLD)
        pool_label.move_to(pool)
        broncho_chip = LabelChip("Bronchospasm", accent=CRIMSON, size=18)
        broncho_chip.next_to(pool, DOWN, buff=0.2)
        # teal nanoparticle on right
        nano = Ellipse(width=1.8, height=1.2)
        nano.set_fill(TEAL, 0.22).set_stroke(TEAL, 2.5)
        nano.to_edge(RIGHT, buff=1.8).shift(UP * 0.4)
        nano_label = Text("albumin", font=SERIF, color=TEAL, font_size=22,
                          slant=ITALIC, weight=BOLD)
        nano_label.move_to(nano)
        # "no hypersensitivity" chip (initially invisible)
        safe_chip = LabelChip("No Hypersensitivity", accent=TEAL, size=20)
        safe_chip.next_to(nano, DOWN, buff=0.2)
        # start with both visible, then drain the crimson
        self.add(pool, pool_label, broncho_chip, nano, nano_label)
        self.wait(0.5)
        # drain: pool falls off bottom of screen — shift only (single-method animate)
        # FadeOut handles opacity; animate handles shift
        self.play(
            pool.animate.shift(DOWN * 5.0),
            pool_label.animate.shift(DOWN * 5.0),
            broncho_chip.animate.shift(DOWN * 5.0),
            FadeOut(pool), FadeOut(pool_label), FadeOut(broncho_chip),
            run_time=1.8
        )
        self.play(FadeIn(safe_chip, shift=UP * 0.12), run_time=0.7)
        # nano scales up slightly to claim the space
        self.play(nano.animate.scale(1.15), nano_label.animate.scale(1.15),
                  run_time=0.8)
        self.wait(max(0.3, total - 3.8))

# ---------------------------------------------------------------- B09 Comparison Bars

class B09_ComparisonBars(Scene):
    def construct(self):
        total = DUR["B09"]
        bar_w = 1.4
        # heights proportional to rates: ~10% vs <1% (scaled for visual clarity)
        taxol_h = 3.2
        abrax_h = 0.35
        base_y = -1.5
        # create bars anchored at bottom (center = base_y + h/2)
        taxol_bar = Rectangle(width=bar_w, height=taxol_h)
        taxol_bar.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        taxol_bar.move_to(LEFT * 2.2 + UP * (base_y + taxol_h / 2))
        abrax_bar = Rectangle(width=bar_w, height=abrax_h)
        abrax_bar.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        abrax_bar.move_to(RIGHT * 2.2 + UP * (base_y + abrax_h / 2))
        # baseline
        baseline = Line(LEFT * 4.0 + UP * base_y, RIGHT * 4.0 + UP * base_y,
                        stroke_width=1.8, color=INK)
        # labels below base
        taxol_lbl = Text("TAXOL", font=DISPLAY, color=CRIMSON, font_size=22,
                         weight=BOLD)
        taxol_lbl.move_to(LEFT * 2.2 + UP * (base_y - 0.42))
        taxol_pct = Text("~10%", font=DISPLAY, color=CRIMSON, font_size=20,
                         weight=BOLD)
        taxol_pct.move_to(LEFT * 2.2 + UP * (base_y - 0.82))
        abrax_lbl = Text("ABRAXANE", font=DISPLAY, color=TEAL, font_size=22,
                         weight=BOLD)
        abrax_lbl.move_to(RIGHT * 2.2 + UP * (base_y - 0.42))
        abrax_pct = Text("<1%", font=DISPLAY, color=TEAL, font_size=20,
                         weight=BOLD)
        abrax_pct.move_to(RIGHT * 2.2 + UP * (base_y - 0.82))
        # title
        title = Text("Hypersensitivity Rate", font=SERIF, color=INK, font_size=28,
                     slant=ITALIC)
        title.to_edge(UP, buff=0.7)
        # illustrative label
        illus = Text("illustrative comparison", font=SERIF, color=SLATE,
                     font_size=18, slant=ITALIC)
        illus.to_edge(DOWN, buff=0.4)
        # animate
        self.play(FadeIn(title), Create(baseline), run_time=0.7)
        self.play(FadeIn(taxol_lbl), FadeIn(taxol_pct), run_time=0.5)
        self.play(GrowFromEdge(taxol_bar, DOWN), run_time=1.0)
        self.play(FadeIn(abrax_lbl), FadeIn(abrax_pct), run_time=0.5)
        self.play(GrowFromEdge(abrax_bar, DOWN), run_time=0.7)
        self.play(FadeIn(illus, shift=UP * 0.08), run_time=0.4)
        self.wait(max(0.3, total - 3.8))

# ---------------------------------------------------------------- B11 Two Bag Comparison

class B11_TwoBagComparison(Scene):
    def construct(self):
        total = DUR["B11"]
        # two columns: left = Taxol (crimson), right = Abraxane (teal)
        col_gap = 0.6
        # left column
        taxol_head = Text("TAXOL", font=DISPLAY, color=CRIMSON, font_size=26,
                          weight=BOLD)
        taxol_items = VGroup(
            Text("Cremophor EL solvent", font=SERIF, color=CRIMSON, font_size=21),
            Text("Steroid premedication", font=SERIF, color=CRIMSON, font_size=21),
            Text("Epinephrine at bedside", font=SERIF, color=CRIMSON, font_size=21),
            Text("Filter required", font=SERIF, color=CRIMSON, font_size=21),
            Text("3-hour infusion", font=SERIF, color=CRIMSON, font_size=21),
        )
        taxol_items.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        taxol_col = VGroup(taxol_head, taxol_items).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        taxol_col.to_edge(LEFT, buff=1.0).shift(UP * 0.2)
        # right column
        abrax_head = Text("ABRAXANE", font=DISPLAY, color=TEAL, font_size=26,
                          weight=BOLD)
        abrax_items = VGroup(
            Text("Albumin nanoparticle", font=SERIF, color=TEAL, font_size=21),
            Text("No premedication", font=SERIF, color=TEAL, font_size=21),
            Text("No epinephrine needed", font=SERIF, color=TEAL, font_size=21),
            Text("No filter", font=SERIF, color=TEAL, font_size=21),
            Text("30-minute infusion", font=SERIF, color=TEAL, font_size=21),
        )
        abrax_items.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        abrax_col = VGroup(abrax_head, abrax_items).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        abrax_col.to_edge(RIGHT, buff=1.0).shift(UP * 0.2)
        # divider line
        divider = Line(UP * 2.8, DOWN * 2.2, stroke_width=1.2, color=SLATE)
        divider.move_to(ORIGIN)
        # bottom label: SAME DRUG
        same_drug = Text("SAME DRUG", font=DISPLAY, color=INK, font_size=30,
                         weight=BOLD)
        same_drug.to_edge(DOWN, buff=0.5)
        # animate
        self.play(FadeIn(taxol_head), FadeIn(abrax_head), Create(divider), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.08)
                                 for item in taxol_items],
                               lag_ratio=0.12, run_time=1.2))
        self.play(LaggedStart(*[FadeIn(item, shift=LEFT * 0.08)
                                 for item in abrax_items],
                               lag_ratio=0.12, run_time=1.2))
        self.play(FadeIn(same_drug, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.7))

# ---------------------------------------------------------------- B12 Section Card

class B12_SectionCard(Scene):
    def construct(self):
        total = DUR["B12"]
        label = Text("A formulation fix", font=DISPLAY, color=INK, font_size=34,
                     weight=BOLD)
        sub = Text("not a tumor-targeting story", font=SERIF, color=SLATE,
                   font_size=26, slant=ITALIC)
        block = VGroup(label, sub).arrange(DOWN, buff=0.32)
        block.move_to(ORIGIN)
        rule = Line(block.get_corner(DL) + DOWN * 0.18,
                    block.get_corner(DR) + DOWN * 0.18,
                    stroke_width=1.8, color=TEAL)
        self.play(FadeIn(label), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.08), Create(rule), run_time=0.8)
        self.wait(max(0.3, total - 1.5))

# ---------------------------------------------------------------- B13 Timeline Summary

class B13_TimelineSummary(Scene):
    def construct(self):
        total = DUR["B13"]
        # horizontal timeline bar
        timeline = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=3.0, color=SLATE)
        timeline.move_to(ORIGIN)
        # dividing tick
        tick = Line(DOWN * 0.25, UP * 0.25, stroke_width=2.5, color=INK)
        tick.move_to(ORIGIN)
        # left zone (Taxol era) — crimson
        taxol_zone = Rectangle(width=5.2, height=2.8)
        taxol_zone.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.5)
        taxol_zone.to_edge(LEFT, buff=0.7).shift(UP * 0.8)
        taxol_era = Text("TAXOL ERA", font=DISPLAY, color=CRIMSON, font_size=22,
                         weight=BOLD)
        taxol_era.to_corner(UL, buff=1.0)
        taxol_desc1 = Text("Cremophor EL solvent", font=SERIF, color=CRIMSON,
                           font_size=20)
        taxol_desc2 = Text("hypersensitivity risk", font=SERIF, color=CRIMSON,
                           font_size=20)
        taxol_descs = VGroup(taxol_desc1, taxol_desc2).arrange(DOWN, buff=0.2,
                                                                aligned_edge=LEFT)
        taxol_descs.next_to(taxol_era, DOWN, buff=0.3, aligned_edge=LEFT)
        # right zone (Abraxane era) — teal
        abrax_zone = Rectangle(width=5.2, height=2.8)
        abrax_zone.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
        abrax_zone.to_edge(RIGHT, buff=0.7).shift(UP * 0.8)
        abrax_era = Text("ABRAXANE ERA", font=DISPLAY, color=TEAL, font_size=22,
                         weight=BOLD)
        abrax_era.to_corner(UR, buff=1.0)
        abrax_desc1 = Text("albumin carrier", font=SERIF, color=TEAL, font_size=20)
        abrax_desc2 = Text("solvent gone", font=SERIF, color=TEAL, font_size=20)
        abrax_descs = VGroup(abrax_desc1, abrax_desc2).arrange(DOWN, buff=0.2,
                                                                aligned_edge=LEFT)
        abrax_descs.next_to(abrax_era, DOWN, buff=0.3, aligned_edge=LEFT)
        # same drug icon across both zones
        same_label = Text("SAME DRUG", font=DISPLAY, color=INK, font_size=20,
                          weight=BOLD)
        same_label.to_edge(DOWN, buff=0.6)
        # animate
        self.play(Create(timeline), run_time=0.5)
        self.play(FadeIn(taxol_zone), FadeIn(taxol_era), run_time=0.6)
        self.play(FadeIn(taxol_descs), run_time=0.6)
        self.play(FadeIn(abrax_zone), FadeIn(abrax_era), Create(tick), run_time=0.6)
        self.play(FadeIn(abrax_descs), run_time=0.6)
        self.play(FadeIn(same_label, shift=UP * 0.08), run_time=0.4)
        self.wait(max(0.3, total - 3.3))

# ---------------------------------------------------------------- B14 The Example

class B14_ExampleSideBySide(Scene):
    def construct(self):
        total = DUR["B14"]
        # illustrative banner at top
        banner = Text("ILLUSTRATIVE EXAMPLE", font=DISPLAY, color=SLATE,
                      font_size=18, weight=BOLD)
        banner.to_edge(UP, buff=0.35)
        # patient context
        patient = Text("Ovarian cancer patient. Same paclitaxel dose.", font=SERIF,
                       color=INK, font_size=22, slant=ITALIC)
        patient.next_to(banner, DOWN, buff=0.25)
        # divider
        divider = Line(UP * 2.0, DOWN * 2.8, stroke_width=1.2, color=SLATE)
        divider.move_to(ORIGIN)
        # left panel — Bag A (Taxol)
        bag_a_head = Text("BAG A: TAXOL", font=DISPLAY, color=CRIMSON, font_size=22,
                          weight=BOLD)
        bag_a_head.move_to(LEFT * 3.2 + UP * 1.6)
        bag_a_items = VGroup(
            Text("6 Cremophor EL vials", font=SERIF, color=CRIMSON, font_size=19),
            Text("Steroid premedication", font=SERIF, color=CRIMSON, font_size=19),
            Text("Epinephrine on table", font=SERIF, color=CRIMSON, font_size=19),
            Text("3-hour filtered infusion", font=SERIF, color=CRIMSON, font_size=19),
        )
        bag_a_items.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        bag_a_items.next_to(bag_a_head, DOWN, buff=0.28, aligned_edge=LEFT)
        bag_a_chip = LabelChip("~10% hypersensitivity", accent=CRIMSON, size=18)
        bag_a_chip.next_to(bag_a_items, DOWN, buff=0.3)
        # right panel — Bag B (Abraxane)
        bag_b_head = Text("BAG B: ABRAXANE", font=DISPLAY, color=TEAL, font_size=22,
                          weight=BOLD)
        bag_b_head.move_to(RIGHT * 3.2 + UP * 1.6)
        bag_b_items = VGroup(
            Text("Albumin nanoparticle", font=SERIF, color=TEAL, font_size=19),
            Text("No premedication", font=SERIF, color=TEAL, font_size=19),
            Text("No epinephrine", font=SERIF, color=TEAL, font_size=19),
            Text("30-minute infusion", font=SERIF, color=TEAL, font_size=19),
        )
        bag_b_items.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        bag_b_items.next_to(bag_b_head, DOWN, buff=0.28, aligned_edge=LEFT)
        bag_b_chip = LabelChip("<1% hypersensitivity", accent=TEAL, size=18)
        bag_b_chip.next_to(bag_b_items, DOWN, buff=0.3)
        # bottom: SAME DRUG
        same = Text("SAME DRUG", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        same.to_edge(DOWN, buff=0.4)
        # animate
        self.play(FadeIn(banner), FadeIn(patient), Create(divider), run_time=0.8)
        self.play(FadeIn(bag_a_head), FadeIn(bag_b_head), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(item) for item in bag_a_items],
                               lag_ratio=0.1, run_time=1.0))
        self.play(LaggedStart(*[FadeIn(item) for item in bag_b_items],
                               lag_ratio=0.1, run_time=1.0))
        self.play(FadeIn(bag_a_chip), FadeIn(bag_b_chip), run_time=0.6)
        self.play(FadeIn(same, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.5))

# ---------------------------------------------------------------- B15 Endcard

class B15_Endcard(Scene):
    def construct(self):
        total = DUR["B15"]
        eye = Text("CANCER NANOMEDICINE", font=DISPLAY, color=TEAL, font_size=18)
        headline = Text("The drug never changed.", font=DISPLAY, color=INK,
                        font_size=30, weight=BOLD)
        headline2 = Text("The solvent did.", font=DISPLAY, color=CRIMSON,
                         font_size=34, weight=BOLD)
        sub = Text(
            "Abraxane's benefit: albumin dissolved paclitaxel without Cremophor",
            font=SERIF, color=INK, font_size=22, slant=ITALIC
        )
        sub2 = Text(
            "— the hypersensitivity disappeared.",
            font=SERIF, color=INK, font_size=22, slant=ITALIC
        )
        block = VGroup(headline, headline2).arrange(DOWN, buff=0.18)
        subs = VGroup(sub, sub2).arrange(DOWN, buff=0.12)
        eye.next_to(block, UP, buff=0.55)
        subs.next_to(block, DOWN, buff=0.4)
        rule = Line(block.get_corner(DL) + DOWN * 0.16,
                    block.get_corner(DR) + DOWN * 0.16,
                    stroke_width=1.6, color=GOLD)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(rule), run_time=1.0)
        self.play(FadeIn(subs, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.3, total - 2.3))
