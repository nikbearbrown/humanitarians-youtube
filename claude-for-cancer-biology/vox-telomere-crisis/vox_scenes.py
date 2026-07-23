"""vox_scenes.py — Why Telomere Shortening Is Both a Cancer Brake and a Cancer Accelerator
(vox-telomere-crisis, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 and B07 are STILL
(ai media slots) and have no scene here — they render as slates until plates land.

Render everything:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-telomere-crisis

Color law: TEAL = surviving clone / telomerase active / stable chromosomes;
CRIMSON = chromosomal crisis / fused chromosomes / dying cells.
GOLD = editor's pen highlight, once only (B10 survivor convergence).
Exclusions: no T-loops/shelterin, no ALT pathway, no senescence vs crisis depth,
no telomerase inhibitor drugs.

Gate B: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _node(label, color, w=2.4, h=0.68):
    """Rounded rectangle node with white DISPLAY label."""
    box = RoundedRectangle(width=w, height=h, corner_radius=0.12)
    box.set_fill(color, 1).set_stroke(width=0, opacity=0)
    txt = Text(label, font=DISPLAY, color=WHITE,
               font_size=int(22 * 0.88), weight="MEDIUM")
    if txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(box.get_center())
    return VGroup(box, txt)


def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=3,
                 max_tip_length_to_length_ratio=0.18, buff=0.08)


def _bar(w, h, color, opacity=1.0):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return b


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Telomere Shortening Is", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        t2 = Text("Both Brake and Accelerator", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    """THE QUESTION beat — named on screen AND in narration (gap formula)."""
    def construct(self):
        total = DUR["B03"]
        q_label = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                        font_size=int(20 * 0.88), weight="MEDIUM")
        q1 = Text("Why does exhausting the cancer brake", font=SERIF, color=INK,
                   font_size=36, weight=BOLD)
        q2 = Text("produce the most dangerous cancer cells?", font=SERIF, color=INK,
                   font_size=36, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        q_label.next_to(block, UP, buff=0.85)
        u = Line(q2.get_corner(DL)+DOWN*0.14, q2.get_corner(DR)+DOWN*0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(q_label), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B04_TelomereShortening(Scene):
    """Telomere shortening bar diagram: TEAL bars shrink across divisions to a CRIMSON threshold."""
    def construct(self):
        total = DUR["B04"]
        hdr = SerifLabel("telomere length  ·  division limit", TEAL, size=26)
        hdr.to_edge(UP, buff=0.7)

        # X-axis label
        x_axis = Line(LEFT * 5.0 + DOWN * 1.8, RIGHT * 5.0 + DOWN * 1.8,
                       color=INK, stroke_width=2)
        x_label = Text("cell divisions", font=SERIF, color=INK, font_size=22)
        x_label.next_to(x_axis, DOWN, buff=0.3)

        # Y-axis label
        y_label = Text("telomere length", font=SERIF, color=INK, font_size=22)
        y_label.rotate(PI / 2)
        y_label.move_to(LEFT * 5.2 + DOWN * 0.3)

        # Bars representing telomere length at successive divisions
        heights = [2.8, 2.3, 1.8, 1.3, 0.7, 0.25]
        n = len(heights)
        xs = np.linspace(-3.8, 3.8, n)
        bars = VGroup()
        for x, h in zip(xs, heights):
            b = _bar(0.6, h, TEAL)
            b.move_to(np.array([x, -1.8 + h / 2, 0]))
            bars.add(b)

        # Crisis threshold line
        threshold_y = -1.8 + 0.55
        thresh = DashedLine(LEFT * 4.5 + UP * (threshold_y + 1.8),
                             RIGHT * 4.5 + UP * (threshold_y + 1.8),
                             color=CRIMSON, stroke_width=2, dash_length=0.18)
        thresh.move_to(np.array([0, threshold_y, 0]))
        thresh_label = LabelChip("CRISIS THRESHOLD", accent=CRIMSON, size=20)
        thresh_label.next_to(thresh, RIGHT, buff=0.2)

        self.play(FadeIn(hdr), Create(x_axis), FadeIn(x_label), FadeIn(y_label), run_time=0.8)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                               lag_ratio=0.15), run_time=1.8)
        self.play(Create(thresh), FadeIn(thresh_label), run_time=0.8)
        self.wait(max(0.5, total - 3.4))


class B05_ChromosomeFusion(Scene):
    """Two chromosomes lose caps, fuse, break during division. TEAL -> CRIMSON crisis."""
    def construct(self):
        total = DUR["B05"]
        hdr = SerifLabel("telomere crisis  ·  chromosomes fuse and break", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Chromosome A: rectangle + small cap at top
        chr_a = _bar(0.5, 2.0, TEAL)
        chr_a.move_to(LEFT * 3.5 + DOWN * 0.1)
        cap_a = _bar(0.5, 0.25, TEAL)
        cap_a.move_to(chr_a.get_top() + UP * 0.125)

        # Chromosome B
        chr_b = _bar(0.5, 2.0, TEAL)
        chr_b.move_to(RIGHT * 3.5 + DOWN * 0.1)
        cap_b = _bar(0.5, 0.25, TEAL)
        cap_b.move_to(chr_b.get_top() + UP * 0.125)

        cap_label = SerifLabel("protective caps", TEAL, size=22)
        cap_label.move_to(UP * 1.8)

        # Fusion bridge
        fusion = _bar(7.0, 0.25, CRIMSON)
        fusion.move_to(UP * 1.05)

        no_cap_label = LabelChip("CAPS GONE", accent=CRIMSON, size=20)
        no_cap_label.move_to(UP * 2.5)

        # Break lines (after fusion)
        break_left = Line(LEFT * 0.3 + UP * 0.8, RIGHT * 0.3 + UP * 0.8,
                           color=CRIMSON, stroke_width=5)
        break_right = Line(LEFT * 0.3 + DOWN * 0.2, RIGHT * 0.3 + DOWN * 0.2,
                            color=CRIMSON, stroke_width=5)

        crisis_chip = LabelChip("CRISIS", accent=CRIMSON, size=24)
        crisis_chip.move_to(DOWN * 2.5)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(chr_a), GrowFromCenter(chr_b),
                  GrowFromCenter(cap_a), GrowFromCenter(cap_b),
                  FadeIn(cap_label), run_time=0.9)
        # Caps disappear
        self.play(FadeOut(cap_a), FadeOut(cap_b), FadeOut(cap_label),
                  FadeIn(no_cap_label), run_time=0.7)
        # Fusion forms
        self.play(chr_a.animate.shift(RIGHT * 0.5),
                  chr_b.animate.shift(LEFT * 0.5),
                  GrowFromCenter(fusion), run_time=0.9)
        # Break lines appear showing catastrophic break
        self.play(Create(break_left), Create(break_right), run_time=0.6)
        self.play(FadeIn(crisis_chip, shift=UP * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 4.1))


class B06_SectionMechanism(Scene):
    """Section card: THE MECHANISM."""
    def construct(self):
        total = DUR["B06"]
        label = Text("THE MECHANISM", font=DISPLAY, color=SLATE,
                      font_size=int(38 * 0.88), weight="MEDIUM")
        label.move_to(ORIGIN)
        u = Line(label.get_corner(DL)+DOWN*0.14,
                 label.get_corner(DR)+DOWN*0.14,
                 color=SLATE, stroke_width=1.5)
        self.play(FadeIn(label), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 0.8))


class B08_SurvivorNode(Scene):
    """From field of dying CRIMSON cells, one TEAL cell emerges with TELOMERASE ACTIVE."""
    def construct(self):
        total = DUR["B08"]
        hdr = SerifLabel("the rare survivor  ·  telomerase reactivation", TEAL, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Many dying CRIMSON cells scattered above center
        dying_cells = VGroup()
        rng = np.random.default_rng(42)
        positions = [
            np.array([x, y, 0])
            for x in np.linspace(-5.5, 5.5, 7)
            for y in [1.5, 0.7]
        ]
        for pos in positions:
            c = Circle(radius=0.22)
            c.set_fill(CRIMSON, 0.75).set_stroke(width=0, opacity=0)
            c.move_to(pos + rng.uniform(-0.25, 0.25, 3) * np.array([1, 0.3, 0]))
            dying_cells.add(c)

        # Funnel neck line
        neck_left = Line(LEFT * 0.6 + DOWN * 0.4, LEFT * 0.25 + DOWN * 1.0,
                          color=INK, stroke_width=2)
        neck_left.set_stroke(width=2, opacity=0.4)
        neck_right = Line(RIGHT * 0.6 + DOWN * 0.4, RIGHT * 0.25 + DOWN * 1.0,
                           color=INK, stroke_width=2)
        neck_right.set_stroke(width=2, opacity=0.4)

        # The one TEAL survivor cell
        survivor = Circle(radius=0.32)
        survivor.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        survivor.move_to(DOWN * 2.0)
        survivor_chip = LabelChip("TELOMERASE ACTIVE", accent=TEAL, size=20)
        survivor_chip.next_to(survivor, RIGHT, buff=0.3)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in dying_cells],
                               lag_ratio=0.04), run_time=1.2)
        self.play(LaggedStart(*[FadeOut(c, scale=0.3) for c in dying_cells],
                               lag_ratio=0.06), run_time=1.5)
        self.play(Create(neck_left), Create(neck_right), run_time=0.5)
        self.play(GrowFromCenter(survivor), run_time=0.6)
        self.play(FadeIn(survivor_chip, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 4.3))


class B09_RearrangementAccumulation(Scene):
    """A TEAL chromosome gains multiple CRIMSON rearrangement marks during crisis."""
    def construct(self):
        total = DUR["B09"]
        hdr = SerifLabel("what the survivor carries  ·  rearrangements", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Central chromosome bar
        chrom = _bar(5.5, 0.55, TEAL)
        chrom.move_to(DOWN * 0.2)
        chrom_label = SerifLabel("survivor chromosome", TEAL, size=22)
        chrom_label.next_to(chrom, UP, buff=0.45)

        # Rearrangement marks appearing sequentially
        rearr_xs = [-2.2, -0.7, 0.4, 1.5, 2.3]
        marks = VGroup()
        mark_labels = VGroup()
        for i, x in enumerate(rearr_xs):
            m = Square(side_length=0.32)
            m.set_fill(CRIMSON, 0.9).set_stroke(width=0, opacity=0)
            m.move_to(np.array([x, -0.2, 0]))
            marks.add(m)
            lbl = Text(f"R{i+1}", font=DISPLAY, color=CRIMSON, font_size=16, weight="MEDIUM")
            lbl.next_to(m, DOWN, buff=0.2)
            mark_labels.add(lbl)

        crisis_note = LabelChip("from crisis", accent=CRIMSON, size=20)
        crisis_note.move_to(RIGHT * 4.5 + DOWN * 1.4)

        self.play(FadeIn(hdr), GrowFromCenter(chrom), FadeIn(chrom_label), run_time=0.9)
        for m, lbl in zip(marks, mark_labels):
            self.play(GrowFromCenter(m), FadeIn(lbl), run_time=0.4)
        self.play(FadeIn(crisis_note, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 3.3))


class B10_BottleneckFunnel(Scene):
    """Population bottleneck collapse: many CRIMSON cells enter, nearly all die,
    one TEAL cell with rearrangement marks exits. GOLD highlight on survivor."""
    def construct(self):
        total = DUR["B10"]
        hdr = SerifLabel("the bottleneck selects the hardiest", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Funnel shape: two converging lines (labels overlap the funnel outline by design)
        left_side = Line(LEFT * 6.0 + UP * 1.8, LEFT * 0.45 + DOWN * 1.6,
                          color=INK, stroke_width=2)
        left_side.set_stroke(width=2, opacity=0.5)
        left_side._qc_intentional = True
        right_side = Line(RIGHT * 6.0 + UP * 1.8, RIGHT * 0.45 + DOWN * 1.6,
                           color=INK, stroke_width=2)
        right_side.set_stroke(width=2, opacity=0.5)
        right_side._qc_intentional = True

        # Population of CRIMSON cells entering (top)
        pop_cells = VGroup()
        entry_xs = np.linspace(-5.0, 5.0, 11)
        for i, x in enumerate(entry_xs):
            c = Circle(radius=0.18)
            c.set_fill(CRIMSON, 0.8).set_stroke(width=0, opacity=0)
            c.move_to(np.array([x, 2.4, 0]))
            pop_cells.add(c)

        # All dying label — shown after cells fade, below survivor, clear of lines
        dying_chip = LabelChip("thousands die", accent=CRIMSON, size=20)
        dying_chip.move_to(ORIGIN + DOWN * 1.8)

        # Survivor node at bottom with GOLD highlight
        survivor_bg = Circle(radius=0.42)
        survivor_bg.set_fill(GOLD, 1).set_stroke(width=0, opacity=0)
        survivor_bg.move_to(DOWN * 2.6)
        survivor = Circle(radius=0.32)
        survivor.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        survivor.move_to(DOWN * 2.6)

        # Rearrangement dots on survivor
        r_dots = VGroup()
        for angle in [0.6, 1.8, 3.2]:
            d = Dot(radius=0.07, color=CRIMSON)
            d.move_to(DOWN * 2.6 + RIGHT * 0.22 * np.cos(angle)
                      + UP * 0.22 * np.sin(angle))
            r_dots.add(d)

        survivor_chip = LabelChip("IMMORTALIZED", accent=TEAL, size=20)
        survivor_chip.next_to(survivor_bg, RIGHT, buff=0.25)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(Create(left_side), Create(right_side), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in pop_cells],
                               lag_ratio=0.05), run_time=0.9)
        self.play(FadeIn(dying_chip), run_time=0.4)
        # Cells collapse / shrink away
        self.play(LaggedStart(*[c.animate.scale(0.1) for c in pop_cells],
                               lag_ratio=0.07), run_time=1.5)
        # Survivor emerges
        self.play(GrowFromCenter(survivor_bg), GrowFromCenter(survivor),
                  *[GrowFromCenter(d) for d in r_dots], run_time=0.9)
        self.play(FadeIn(survivor_chip, shift=LEFT * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 5.3))


class B11_ImplicationComparison(Scene):
    """Two-column: brake works (TEAL, 99.9% die) vs survivor (CRIMSON-to-TEAL: immortal, dangerous)."""
    def construct(self):
        total = DUR["B11"]
        hdr = SerifLabel("the brake that builds aggressors", SLATE, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Left column — brake effect
        left_hdr = LabelChip("THE BRAKE WORKED", accent=TEAL, size=20)
        left_hdr.move_to(LEFT * 3.2 + UP * 1.5)

        left_lines = VGroup()
        for i, txt in enumerate(["nearly all cells die", "tumor suppressor function", "intact"]):
            t = Text(txt, font=SERIF, color=INK, font_size=26)
            t.move_to(LEFT * 3.2 + UP * (0.7 - i * 0.6))
            left_lines.add(t)

        # Right column — the dangerous survivor
        right_hdr = LabelChip("THE SURVIVOR", accent=CRIMSON, size=20)
        right_hdr.move_to(RIGHT * 3.2 + UP * 1.5)

        right_items = ["immortalized", "genomically unstable", "death-resistant"]
        right_lines = VGroup()
        for i, txt in enumerate(right_items):
            t = Text(txt, font=SERIF, color=CRIMSON, font_size=26)
            t.move_to(RIGHT * 3.2 + UP * (0.7 - i * 0.6))
            right_lines.add(t)

        # Divider
        div = Line(UP * 2.0, DOWN * 2.2, color=INK, stroke_width=1.5)
        div.set_stroke(width=1.5, opacity=0.3)

        self.play(FadeIn(hdr), Create(div), run_time=0.6)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.2) for t in left_lines],
                               lag_ratio=0.2), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(t, shift=LEFT * 0.2) for t in right_lines],
                               lag_ratio=0.2), run_time=0.9)
        self.wait(max(0.5, total - 3.0))


class B12_TimelineExample(Scene):
    """THE EXAMPLE: illustrative 40-year timeline through crisis. Concrete numbers."""
    def construct(self):
        total = DUR["B12"]
        illus = SerifLabel("illustrative", SLATE, size=22)
        illus.move_to(LEFT * 3.5 + UP * 2.8)

        # Timeline axis
        axis = Line(LEFT * 5.5 + DOWN * 2.0, RIGHT * 5.5 + DOWN * 2.0,
                     color=INK, stroke_width=2)
        axis_label = Text("cell divisions over 40 years", font=SERIF, color=INK, font_size=20)
        axis_label.next_to(axis, DOWN, buff=0.3)

        # Phase labels
        normal_phase = SerifLabel("normal division", TEAL, size=22)
        normal_phase.move_to(LEFT * 3.5 + DOWN * 0.8)

        crisis_chip = LabelChip("TELOMERE CRISIS", accent=CRIMSON, size=20)
        crisis_chip.move_to(ORIGIN + DOWN * 0.8)

        exit_chip = LabelChip("EXIT", accent=TEAL, size=20)
        exit_chip.move_to(RIGHT * 4.0 + DOWN * 0.8)

        # Phase boundary markers on axis
        marker1 = Line(DOWN * 1.85, DOWN * 2.15, color=CRIMSON, stroke_width=2)
        marker1.move_to(LEFT * 1.0 + DOWN * 2.0)
        m1_label = Text("gen. 50\n3 kb threshold", font=DISPLAY, color=CRIMSON,
                         font_size=16, weight="MEDIUM")
        m1_label.next_to(marker1, UP, buff=0.25)

        marker2 = Line(DOWN * 1.85, DOWN * 2.15, color=TEAL, stroke_width=2)
        marker2.move_to(RIGHT * 3.0 + DOWN * 2.0)
        m2_label = Text("TERT active\nstabilized", font=DISPLAY, color=TEAL,
                         font_size=16, weight="MEDIUM")
        m2_label.next_to(marker2, UP, buff=0.25)

        # Death marks in crisis zone (CRIMSON dots)
        death_marks = VGroup()
        for x in np.linspace(-0.9, 2.8, 8):
            d = Dot(radius=0.1, color=CRIMSON)
            d.move_to(np.array([x, -1.3, 0]))
            death_marks.add(d)

        # Survivor cell at exit
        survivor = Circle(radius=0.3)
        survivor.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        survivor.move_to(RIGHT * 4.0 + DOWN * 0.1)

        # Rearrangement marks on survivor
        rmark = LabelChip("15 rearrangements", accent=CRIMSON, size=18)
        rmark.next_to(survivor, UP, buff=0.2)

        self.play(FadeIn(illus), Create(axis), FadeIn(axis_label), run_time=0.8)
        self.play(FadeIn(normal_phase), run_time=0.4)
        self.play(Create(marker1), FadeIn(m1_label), run_time=0.6)
        self.play(FadeIn(crisis_chip), run_time=0.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in death_marks],
                               lag_ratio=0.1), run_time=1.0)
        self.play(Create(marker2), FadeIn(m2_label), run_time=0.6)
        self.play(GrowFromCenter(survivor), FadeIn(exit_chip), run_time=0.6)
        self.play(FadeIn(rmark, shift=DOWN * 0.15), run_time=0.5)
        self.wait(max(0.5, total - 4.9))


class B13_End(Scene):
    """Endcard: question -> answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B13"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=int(22 * 0.88), weight="MEDIUM")
        topic.to_edge(UP, buff=0.7)
        q = SerifLabel("brake -> mass death -> one dangerous survivor", CRIMSON, size=26)
        q.move_to(UP * 0.7)
        a1 = Text("Crisis is a selection gauntlet.", font=SERIF, color=INK,
                   font_size=36, weight=BOLD)
        a2 = Text("The one cell that exits is immortal, rearranged,", font=SERIF,
                   color=INK, font_size=30)
        a3 = Text("and resistant to every death signal that killed its siblings.", font=SERIF,
                   color=INK, font_size=30)
        block = VGroup(a1, a2, a3).arrange(DOWN, buff=0.16).move_to(DOWN * 0.4)
        u = Line(a3.get_corner(DL)+DOWN*0.12, a3.get_corner(DR)+DOWN*0.12,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(a1), run_time=0.7)
        self.play(FadeIn(a2), run_time=0.6)
        self.play(FadeIn(a3), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 3.3))
