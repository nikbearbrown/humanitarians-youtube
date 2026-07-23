"""vox_scenes.py — Why Two Checkpoints Fail When One Virus Infects
(vox-hpv-dual-hit, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is STILL (ai media
slot) and has no scene here — it renders as a slate until the plate lands.

Render everything:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-hpv-dual-hit

Color law: TEAL = intact/functional checkpoints; CRIMSON = disabled/hijacked.
GOLD = editor's pen highlight, once only (B10 convergence node).
Exclusions: no HPV taxonomy beyond HPV-16, no CIN grading, no other viral
carcinogens, no vaccine mechanism, no integration/episomal distinction.

Gate B: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 14.0, "B04": 10.0, "B05": 9.0, "B06": 10.0,
    "B07": 4.0, "B08": 11.0, "B09": 12.0, "B10": 12.0, "B11": 11.0,
    "B12": 10.0, "B13": 18.0, "B14": 14.0
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _node(label, color, w=2.2, h=0.7):
    """Rounded rectangle node with white label."""
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
                 max_tip_length_to_length_ratio=0.18,
                 buff=0.08)


def _bar(w, h, color, opacity=1.0):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return b


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """Cold open title card. Eyebrow TEAL, headline INK."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=int(24 * 0.88), weight="MEDIUM")
        t1 = Text("Why Two Checkpoints Fail", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("When One Virus Infects", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Question(Scene):
    """THE QUESTION beat — named on screen AND in narration."""
    def construct(self):
        total = DUR["B03"]
        q_label = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                        font_size=int(20 * 0.88), weight="MEDIUM")
        q_text1 = Text("Why does one infection", font=SERIF, color=INK,
                        font_size=44, weight=BOLD)
        q_text2 = Text("do the work of two mutations?", font=SERIF, color=INK,
                        font_size=44, weight=BOLD)
        block = VGroup(q_text1, q_text2).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        q_label.next_to(block, UP, buff=0.9)
        u = Line(q_text2.get_corner(DL) + DOWN * 0.14,
                 q_text2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(q_label), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


class B04_TwoHitExpectation(Scene):
    """Two-hit mutation expectation: each tumor suppressor falls separately.
    Two CRIMSON mutation arrows hit two TEAL gene nodes, sequentially."""
    def construct(self):
        total = DUR["B04"]
        # Header
        hdr = SerifLabel("normal two-hit logic", SLATE, size=26)
        hdr.to_edge(UP, buff=0.7)
        # Two gene nodes
        gene1 = _node("TP53", TEAL, w=2.0, h=0.65)
        gene1.move_to(LEFT * 3.2 + DOWN * 0.3)
        gene2 = _node("RB1", TEAL, w=2.0, h=0.65)
        gene2.move_to(RIGHT * 3.2 + DOWN * 0.3)
        # Mutation 1 label
        mut1_chip = LabelChip("Mutation 1", accent=CRIMSON, size=22)
        mut1_chip.next_to(gene1, UP, buff=0.55)
        # Mutation 2 label
        mut2_chip = LabelChip("Mutation 2", accent=CRIMSON, size=22)
        mut2_chip.next_to(gene2, UP, buff=0.55)
        # Strike-through lines to show genes disabled
        s1 = Line(gene1.get_left() + LEFT * 0.1,
                  gene1.get_right() + RIGHT * 0.1,
                  color=CRIMSON, stroke_width=4)
        s1._qc_intentional = True
        s2 = Line(gene2.get_left() + LEFT * 0.1,
                  gene2.get_right() + RIGHT * 0.1,
                  color=CRIMSON, stroke_width=4)
        s2._qc_intentional = True
        # "years apart" label
        years = SerifLabel("years apart", INK, size=26)
        years.to_edge(DOWN, buff=0.8)
        sep_line = Line(LEFT * 0.8 + DOWN * 1.0, RIGHT * 0.8 + DOWN * 1.0,
                        color=SLATE, stroke_width=1.5)
        sep_line.set_stroke(width=1.5, opacity=0.5)
        self.play(FadeIn(hdr), run_time=0.5)
        self.play(FadeIn(gene1, shift=RIGHT * 0.4), run_time=0.6)
        self.play(FadeIn(mut1_chip, shift=DOWN * 0.3),
                  Create(s1), run_time=0.8)
        self.play(FadeIn(gene2, shift=LEFT * 0.4), run_time=0.6)
        self.play(FadeIn(mut2_chip, shift=DOWN * 0.3),
                  Create(s2), run_time=0.8)
        self.play(FadeIn(years), run_time=0.5)
        self.wait(max(0.5, total - 3.8))


class B05_P53Circuit(Scene):
    """p53 circuit intact: damage -> p53 -> halt. All TEAL, functional."""
    def construct(self):
        total = DUR["B05"]
        hdr = SerifLabel("p53  ·  the damage guardian", TEAL, size=26)
        hdr.to_edge(UP, buff=0.7)
        # Nodes
        dmg = _node("DNA DAMAGE", SLATE, w=2.4, h=0.65)
        dmg.move_to(LEFT * 4.0 + DOWN * 0.2)
        p53 = _node("p53", TEAL, w=1.8, h=0.65)
        p53.move_to(ORIGIN + DOWN * 0.2)
        halt = _node("CELL HALTS", TEAL, w=2.4, h=0.65)
        halt.move_to(RIGHT * 4.0 + DOWN * 0.2)
        # Arrows
        a1 = _arrow(dmg.get_right(), p53.get_left(), color=TEAL)
        a2 = _arrow(p53.get_right(), halt.get_left(), color=TEAL)
        # Repair label below
        repair = SerifLabel("repair begins", TEAL, size=24)
        repair.next_to(halt, DOWN, buff=0.45)
        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(dmg), run_time=0.6)
        self.play(Create(a1), GrowFromCenter(p53), run_time=0.7)
        self.play(Create(a2), GrowFromCenter(halt), run_time=0.7)
        self.play(FadeIn(repair, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.0))


class B06_RbGate(Scene):
    """Rb/E2F gate intact: Rb holds E2F; cyclin signal -> Rb releases E2F -> S phase."""
    def construct(self):
        total = DUR["B06"]
        hdr = SerifLabel("Rb  ·  the gate to S phase", TEAL, size=26)
        hdr.to_edge(UP, buff=0.7)
        # Rb-E2F complex
        rb_box = _node("Rb", TEAL, w=1.6, h=0.65)
        rb_box.move_to(LEFT * 2.5 + DOWN * 0.2)
        e2f_box = _node("E2F", TEAL, w=1.6, h=0.65)
        e2f_box.move_to(LEFT * 0.5 + DOWN * 0.2)
        bracket = Brace(VGroup(rb_box, e2f_box), DOWN, color=INK)
        b_label = SerifLabel("sequestered", INK, size=22)
        b_label.next_to(bracket, DOWN, buff=0.15)
        # Cyclin signal coming in from left-top
        cyclin_chip = LabelChip("cyclin signal", accent=SLATE, size=22)
        cyclin_chip.move_to(LEFT * 4.5 + UP * 1.0)
        cyclin_arrow = _arrow(cyclin_chip.get_right() + RIGHT * 0.1,
                              rb_box.get_left() + UP * 0.2, color=SLATE)
        # After release: E2F free, S phase node
        s_phase = _node("S PHASE", TEAL, w=2.2, h=0.65)
        s_phase.move_to(RIGHT * 3.8 + DOWN * 0.2)
        s_arrow = _arrow(e2f_box.get_right() + RIGHT * 0.1,
                          s_phase.get_left(), color=TEAL)
        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(rb_box), GrowFromCenter(e2f_box), run_time=0.7)
        self.play(FadeIn(bracket), FadeIn(b_label), run_time=0.6)
        self.play(FadeIn(cyclin_chip, shift=RIGHT * 0.3),
                  Create(cyclin_arrow), run_time=0.7)
        self.play(rb_box.animate.shift(LEFT * 0.4),
                  FadeOut(b_label), FadeOut(bracket), run_time=0.7)
        self.play(Create(s_arrow), GrowFromCenter(s_phase), run_time=0.7)
        self.wait(max(0.5, total - 3.9))


class B07_SectionMechanism(Scene):
    """Section card: THE MECHANISM."""
    def construct(self):
        total = DUR["B07"]
        label = Text("THE MECHANISM", font=DISPLAY, color=SLATE,
                      font_size=int(38 * 0.88), weight="MEDIUM")
        label.move_to(ORIGIN)
        u = Line(label.get_corner(DL) + DOWN * 0.14,
                 label.get_corner(DR) + DOWN * 0.14,
                 color=SLATE, stroke_width=1.5)
        self.play(FadeIn(label), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 0.8))


class B08_E6Degrades(Scene):
    """E6 hijacks E6AP to destroy p53. CRIMSON E6 node; p53 shrinks away."""
    def construct(self):
        total = DUR["B08"]
        hdr = SerifLabel("E6 recruits the cell's own machinery", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)
        # E6 node
        e6 = _node("E6", CRIMSON, w=1.8, h=0.65)
        e6.move_to(LEFT * 3.8 + DOWN * 0.2)
        # E6AP node
        e6ap = _node("E6AP ubiquitin ligase", SLATE, w=2.8, h=0.65)
        e6ap.move_to(LEFT * 0.3 + DOWN * 0.2)
        a_e6_e6ap = _arrow(e6.get_right(), e6ap.get_left(), color=CRIMSON)
        # p53 node
        p53 = _node("p53", TEAL, w=1.8, h=0.65)
        p53.move_to(RIGHT * 3.5 + DOWN * 0.2)
        a_e6ap_p53 = _arrow(e6ap.get_right(), p53.get_left(), color=CRIMSON)
        # "destroyed" chip below p53
        gone_chip = LabelChip("DESTROYED", accent=CRIMSON, size=22)
        gone_chip.next_to(p53, DOWN, buff=0.45)
        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(e6), run_time=0.6)
        self.play(Create(a_e6_e6ap), GrowFromCenter(e6ap), run_time=0.7)
        self.play(Create(a_e6ap_p53), GrowFromCenter(p53), run_time=0.7)
        self.play(p53.animate.scale(0.55),
                  FadeIn(gone_chip, shift=UP * 0.1), run_time=1.0)
        self.wait(max(0.5, total - 3.5))


class B09_E7Displaces(Scene):
    """E7 wedges Rb-E2F apart. Rb grayed; E2F escapes to S-phase genes."""
    def construct(self):
        total = DUR["B09"]
        hdr = SerifLabel("E7 forces E2F free", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)
        # E7 node
        e7 = _node("E7", CRIMSON, w=1.8, h=0.65)
        e7.move_to(LEFT * 4.0 + DOWN * 0.1)
        # Rb-E2F complex together
        rb = _node("Rb", TEAL, w=1.6, h=0.65)
        rb.move_to(LEFT * 1.0 + DOWN * 0.1)
        e2f = _node("E2F", TEAL, w=1.6, h=0.65)
        e2f.move_to(RIGHT * 0.9 + DOWN * 0.1)
        a_e7 = _arrow(e7.get_right(), rb.get_left(), color=CRIMSON)
        # S-phase destination
        s_phase = _node("S-PHASE GENES ON", CRIMSON, w=3.2, h=0.65)
        s_phase.move_to(RIGHT * 4.0 + UP * 1.2)
        a_e2f_s = _arrow(e2f.get_top(),
                          s_phase.get_left() + LEFT * 0.1, color=CRIMSON)
        # Rb "disabled" chip
        rb_gone = LabelChip("Rb DISABLED", accent=SLATE, size=22)
        rb_gone.next_to(rb, DOWN, buff=0.45)
        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(rb), GrowFromCenter(e2f), run_time=0.6)
        self.play(GrowFromCenter(e7), run_time=0.5)
        self.play(Create(a_e7), run_time=0.6)
        self.play(rb.animate.set_fill(SLATE, 0.5),
                  FadeIn(rb_gone, shift=UP * 0.1),
                  e2f.animate.shift(UP * 0.4 + RIGHT * 0.4),
                  run_time=0.9)
        self.play(Create(a_e2f_s), GrowFromCenter(s_phase), run_time=0.8)
        self.wait(max(0.5, total - 3.9))


class B10_DualArmSplit(Scene):
    """THE SPLIT: two parallel arms (E6->p53, E7->Rb) converge on one node.
    GOLD highlight on the convergence node (the editor's pen, used once).
    Real shape motion: arms grow and shift into the convergence."""
    def construct(self):
        total = DUR["B10"]
        hdr = SerifLabel("one infection · both circuits dark", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Upper arm: E6 -> p53 destroyed
        e6 = _node("E6", CRIMSON, w=1.5, h=0.58)
        e6.move_to(LEFT * 4.5 + UP * 1.2)
        p53_gone = _node("p53 gone", CRIMSON, w=1.8, h=0.58)
        p53_gone.move_to(LEFT * 1.5 + UP * 1.2)
        a_upper = _arrow(e6.get_right(), p53_gone.get_left(), color=CRIMSON)

        # Lower arm: E7 -> Rb disabled -> E2F free
        e7 = _node("E7", CRIMSON, w=1.5, h=0.58)
        e7.move_to(LEFT * 4.5 + DOWN * 1.2)
        rb_free = _node("Rb disabled", CRIMSON, w=1.8, h=0.58)
        rb_free.move_to(LEFT * 1.5 + DOWN * 1.2)
        a_lower = _arrow(e7.get_right(), rb_free.get_left(), color=CRIMSON)

        # Convergence node with GOLD highlight
        conv_box = RoundedRectangle(width=3.2, height=0.8, corner_radius=0.14)
        conv_box.set_fill(GOLD, 1).set_stroke(width=0, opacity=0)
        conv_box.move_to(RIGHT * 3.5 + ORIGIN)
        conv_txt = Text("CHECKPOINT-FREE CELL", font=DISPLAY, color=INK,
                         font_size=int(20 * 0.88), weight="MEDIUM")
        conv_txt.move_to(conv_box.get_center())
        conv = VGroup(conv_box, conv_txt)

        a_upper_conv = _arrow(p53_gone.get_right() + RIGHT * 0.05,
                               conv.get_left() + UP * 0.18, color=CRIMSON)
        a_lower_conv = _arrow(rb_free.get_right() + RIGHT * 0.05,
                               conv.get_left() + DOWN * 0.18, color=CRIMSON)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(e6), GrowFromCenter(e7), run_time=0.6)
        self.play(Create(a_upper), GrowFromCenter(p53_gone),
                  Create(a_lower), GrowFromCenter(rb_free), run_time=0.9)
        self.play(Create(a_upper_conv), Create(a_lower_conv),
                  GrowFromCenter(conv), run_time=1.0)
        self.wait(max(0.5, total - 3.0))


class B11_GenVsProtein(Scene):
    """Gene sequence intact; protein gone. Left column TEAL (DNA), right CRIMSON (protein)."""
    def construct(self):
        total = DUR["B11"]
        hdr = SerifLabel("sequencing finds nothing", SLATE, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Left column header
        dna_hdr = LabelChip("DNA sequence", accent=TEAL, size=22)
        dna_hdr.move_to(LEFT * 3.2 + UP * 1.3)
        # DNA gene bands (intact)
        tp53_band = _bar(2.0, 0.55, TEAL)
        tp53_band.move_to(LEFT * 3.2 + UP * 0.3)
        rb1_band = _bar(2.0, 0.55, TEAL)
        rb1_band.move_to(LEFT * 3.2 + DOWN * 0.55)
        tp53_label = SerifLabel("TP53  intact", TEAL, size=22)
        tp53_label.next_to(tp53_band, RIGHT, buff=0.25)
        rb1_label = SerifLabel("RB1   intact", TEAL, size=22)
        rb1_label.next_to(rb1_band, RIGHT, buff=0.25)

        # Right column header
        prot_hdr = LabelChip("protein level", accent=CRIMSON, size=22)
        prot_hdr.move_to(RIGHT * 3.2 + UP * 1.3)
        # Protein presence bars (tiny = absent)
        p53_prot = _bar(0.28, 0.55, CRIMSON)
        p53_prot.move_to(RIGHT * 3.2 + UP * 0.3)
        rb_prot = _bar(0.28, 0.55, CRIMSON)
        rb_prot.move_to(RIGHT * 3.2 + DOWN * 0.55)
        p53_gone = SerifLabel("p53  absent", CRIMSON, size=22)
        p53_gone.next_to(p53_prot, RIGHT, buff=0.25)
        rb_gone = SerifLabel("Rb   absent", CRIMSON, size=22)
        rb_gone.next_to(rb_prot, RIGHT, buff=0.25)

        # Divider
        div = Line(UP * 1.8 + ORIGIN, DOWN * 1.6 + ORIGIN,
                   color=INK, stroke_width=1.5)
        div.set_stroke(width=1.5, opacity=0.35)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(FadeIn(dna_hdr), FadeIn(prot_hdr), Create(div), run_time=0.6)
        self.play(GrowFromCenter(tp53_band), FadeIn(tp53_label),
                  GrowFromCenter(p53_prot), FadeIn(p53_gone), run_time=0.8)
        self.play(GrowFromCenter(rb1_band), FadeIn(rb1_label),
                  GrowFromCenter(rb_prot), FadeIn(rb_gone), run_time=0.8)
        self.wait(max(0.5, total - 2.7))


class B12_DamageAccumulation(Scene):
    """Damage accumulation over time: small marks appear on a bar, unchecked."""
    def construct(self):
        total = DUR["B12"]
        hdr = SerifLabel("permissive for further mutation", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Timeline axis
        axis = Line(LEFT * 5.5 + DOWN * 0.6, RIGHT * 5.5 + DOWN * 0.6,
                    color=INK, stroke_width=2)
        t_label = SerifLabel("time / cell divisions", INK, size=22)
        t_label.next_to(axis, DOWN, buff=0.3)

        # Build accumulating damage marks (small CRIMSON squares)
        n_marks = 12
        marks = VGroup()
        x_positions = np.linspace(-4.8, 4.8, n_marks)
        for i, x in enumerate(x_positions):
            size = 0.22 + 0.04 * i  # very slight growth to show accumulation
            m = Square(side_length=min(size, 0.38))
            m.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
            y_jitter = 0.22 + (i % 3) * 0.18
            m.move_to(np.array([x, y_jitter, 0]))
            marks.add(m)

        # Label at right
        chip = LabelChip("unchecked", accent=CRIMSON, size=22)
        chip.move_to(RIGHT * 3.8 + UP * 1.3)

        self.play(FadeIn(hdr), Create(axis), FadeIn(t_label), run_time=0.8)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in marks],
                               lag_ratio=0.08), run_time=2.5)
        self.play(FadeIn(chip, shift=DOWN * 0.2), run_time=0.5)
        self.wait(max(0.5, total - 3.8))


class B13_UVExample(Scene):
    """THE EXAMPLE: UV in normal vs HPV-infected cell. Side by side.
    Left = TEAL (p53 rises, halts). Right = CRIMSON (no p53, S phase proceeds).
    Label: illustrative."""
    def construct(self):
        total = DUR["B13"]
        hdr = SerifLabel("illustrative", SLATE, size=22)
        hdr.move_to(LEFT * 3.5 + UP * 3.25)   # top-left, clear of center divider

        # Column headers
        normal_hdr = LabelChip("normal cell", accent=TEAL, size=22)
        normal_hdr.move_to(LEFT * 3.5 + UP * 2.6)
        hpv_hdr = LabelChip("HPV-infected cell", accent=CRIMSON, size=22)
        hpv_hdr.move_to(RIGHT * 3.0 + UP * 2.6)

        # Divider — faint separator; illustrative label deliberately crosses it
        div = Line(UP * 3.0, DOWN * 2.8,
                   color=INK, stroke_width=1.5)
        div.set_stroke(width=1.5, opacity=0.3)
        div._qc_intentional = True   # "illustrative" hdr crosses this faint rule: deliberate

        # Shared: UV arrow (same in both)
        uv_left = LabelChip("UV damage", accent=SLATE, size=20)
        uv_left.move_to(LEFT * 3.5 + UP * 1.6)
        uv_right = LabelChip("UV damage", accent=SLATE, size=20)
        uv_right.move_to(RIGHT * 3.0 + UP * 1.6)

        # Left (normal): p53 bar rises -> HALT
        p53_bar_left = _bar(0.55, 0.65, TEAL)
        p53_bar_left.move_to(LEFT * 3.5 + UP * 0.5)
        p53_label_left = SerifLabel("p53 rises", TEAL, size=20)
        p53_label_left.next_to(p53_bar_left, RIGHT, buff=0.2)
        halt_left = _node("HALT", TEAL, w=1.6, h=0.55)
        halt_left.move_to(LEFT * 3.5 + DOWN * 0.65)
        a_left = _arrow(p53_bar_left.get_bottom(),
                         halt_left.get_top(), color=TEAL)

        # Right (HPV): flat p53 (absent) -> no halt -> S phase
        p53_bar_right = _bar(0.08, 0.65, CRIMSON)
        p53_bar_right.move_to(RIGHT * 3.0 + UP * 0.5)
        p53_label_right = SerifLabel("no p53 response", CRIMSON, size=20)
        p53_label_right.next_to(p53_bar_right, RIGHT, buff=0.2)
        s_phase_right = _node("S PHASE", CRIMSON, w=1.8, h=0.55)
        s_phase_right.move_to(RIGHT * 3.0 + DOWN * 0.65)
        a_right = _arrow(p53_bar_right.get_bottom(),
                          s_phase_right.get_top(), color=CRIMSON)

        # Damage carries forward label
        damage_fwd = SerifLabel("damage passes through", CRIMSON, size=20)
        damage_fwd.move_to(RIGHT * 3.0 + DOWN * 1.8)

        self.play(FadeIn(hdr), run_time=0.4)
        self.play(FadeIn(normal_hdr), FadeIn(hpv_hdr), Create(div), run_time=0.6)
        self.play(FadeIn(uv_left), FadeIn(uv_right), run_time=0.5)
        self.play(GrowFromCenter(p53_bar_left), FadeIn(p53_label_left),
                  GrowFromCenter(p53_bar_right), FadeIn(p53_label_right),
                  run_time=0.9)
        self.play(Create(a_left), GrowFromCenter(halt_left),
                  Create(a_right), GrowFromCenter(s_phase_right), run_time=0.9)
        self.play(FadeIn(damage_fwd, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.5, total - 3.9))


class B14_End(Scene):
    """Endcard: question -> answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B14"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=int(22 * 0.88), weight="MEDIUM")
        topic.to_edge(UP, buff=0.7)
        q = SerifLabel("one infection  ->  two checkpoints lost", CRIMSON, size=28)
        q.move_to(UP * 0.6)
        a1 = Text("E6 and E7 commandeer the cell's own machinery", font=SERIF,
                   color=INK, font_size=38, weight=BOLD)
        a2 = Text("to eliminate p53 and Rb — no DNA letter changed.", font=SERIF,
                   color=INK, font_size=38, weight=BOLD)
        block = VGroup(a1, a2).arrange(DOWN, buff=0.16).move_to(DOWN * 0.5)
        u = Line(a2.get_corner(DL) + DOWN * 0.14,
                 a2.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), run_time=0.7)
        self.play(FadeIn(a1), run_time=0.8)
        self.play(FadeIn(a2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.9))
