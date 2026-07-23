"""vox_scenes.py — Why a Broken Oxygen Sensor Causes a Cancer to Act Permanently Starved
(vox-vhl-hif, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B02 and B12 are STILL (ai) slots — no scene here; they compile as slates.

Color law:
  TEAL   = working degradation pathway / HIF destroyed / normal cell
  CRIMSON = VHL absent / HIF accumulating / cancer cell outcome
  GOLD   = single editor highlight per scene (fill only, NEVER text)
  Two accents max. Never swapped mid-film.

Exclusions honored: no prolyl hydroxylase biochemistry detail, no HIF-1a vs HIF-2a
distinction, no oncogenic pseudohypoxia routes (SDH/KRAS/MYC), no VEGF mechanism detail.

Run from books/ root:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-vhl-hif
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ---------------------------------------------------------------- DUR dict
DUR = {
    "B01": 10.0, "B03": 12.0, "B04": 13.0, "B05": 13.0,
    "B06": 11.0, "B07": 16.0, "B08": 14.0, "B09": 14.0,
    "B10": 13.0, "B11": 11.0, "B13": 12.0, "B14": 16.0, "B15": 13.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _chip(label, accent=TEAL, size=24):
    return LabelChip(label, accent=accent, size=size)


def _arrow(start, end, color=TEAL):
    return Arrow(start, end, color=color, stroke_width=3,
                 buff=0.15, tip_length=0.22)


def _panel_rect(center, w, h, color=TEAL):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 0.06).set_stroke(color, 2.2)
    r.move_to(center)
    return r


def _dashed_rect(center, w, h, color=CRIMSON):
    """A dashed-border rectangle for the 'absent' node."""
    r = DashedVMobject(Rectangle(width=w, height=h).move_to(center),
                       num_dashes=22, dashed_ratio=0.55)
    r.set_stroke(color, 2.5)
    return r


def _gold_bar(center, w=2.6, h=0.45):
    """A translucent GOLD highlight bar at a fixed position (fill only, never text)."""
    bar = Rectangle(width=w, height=h)
    bar.set_fill(GOLD, 0.45).set_stroke(width=0, opacity=0)
    bar.move_to(center)
    return bar


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    """Title card — COLD OPEN — 'CANCER BIOLOGY' TEAL eyebrow, INK title."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why a broken oxygen sensor", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("causes a cancer to act", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t3 = Text("permanently starved", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.65)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_HIFRole(Scene):
    """HIF-1alpha as hub: three output arrows to GLUT1, glycolytic enzymes, VEGF."""
    def construct(self):
        total = DUR["B03"]
        hub = _chip("HIF-1alpha", accent=TEAL, size=28)
        hub.move_to(LEFT * 3.2)
        eye = Text("hypoxic response master switch", font=SERIF, color=TEAL,
                   font_size=22).next_to(hub, UP, buff=0.45)
        out1 = _chip("GLUT1", accent=TEAL, size=24).move_to(RIGHT * 3.2 + UP * 1.4)
        out2 = _chip("glycolytic enzymes", accent=TEAL, size=24).move_to(RIGHT * 3.2)
        out3 = _chip("VEGF", accent=TEAL, size=24).move_to(RIGHT * 3.2 + DOWN * 1.4)
        arr1 = _arrow(hub.get_right() + RIGHT * 0.05, out1.get_left() + LEFT * 0.05,
                      color=TEAL)
        arr2 = _arrow(hub.get_right() + RIGHT * 0.05, out2.get_left() + LEFT * 0.05,
                      color=TEAL)
        arr3 = _arrow(hub.get_right() + RIGHT * 0.05, out3.get_left() + LEFT * 0.05,
                      color=TEAL)
        self.play(FadeIn(hub), FadeIn(eye), run_time=0.8)
        self.play(GrowArrow(arr1), FadeIn(out1), run_time=0.7)
        self.play(GrowArrow(arr2), FadeIn(out2), run_time=0.7)
        self.play(GrowArrow(arr3), FadeIn(out3), run_time=0.7)
        self.wait(max(0.5, total - 2.9))


class B04_QuestionCard(Scene):
    """THE QUESTION — named on screen and in narration."""
    def construct(self):
        total = DUR["B04"]
        label = Text("THE QUESTION", font=DISPLAY, color=SLATE, font_size=20)
        facts = VGroup(
            Text("HIF-1alpha gene:  intact", font=SERIF, color=INK, font_size=28),
            Text("Prolyl hydroxylases:  intact", font=SERIF, color=INK, font_size=28),
            Text("Oxygen:  adequate", font=SERIF, color=INK, font_size=28),
            Text("HIF-1alpha activity:  constitutively on", font=SERIF,
                 color=CRIMSON, font_size=28, weight=BOLD),
        )
        facts.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        facts.move_to(UP * 0.3)
        label.next_to(facts, UP, buff=0.55)
        q = Text(
            "Why does a cell with normal oxygen-sensing",
            font=SERIF, color=INK, font_size=26, slant=ITALIC,
        )
        q2 = Text(
            "fire the hypoxic program anyway?",
            font=SERIF, color=INK, font_size=26, slant=ITALIC,
        )
        qblock = VGroup(q, q2).arrange(DOWN, buff=0.12)
        qblock.next_to(facts, DOWN, buff=0.45)
        self.play(FadeIn(label), run_time=0.5)
        for line in facts:
            self.play(FadeIn(line, shift=RIGHT * 0.15), run_time=0.55)
        self.play(FadeIn(qblock, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 0.5 - len(facts) * 0.55 - 0.8))


class B05_NaiveExpectation(Scene):
    """THE PROBLEM — expected normoxic chain: O2 -> PHD -> HIF destroyed."""
    def construct(self):
        total = DUR["B05"]
        panel = _panel_rect(ORIGIN + DOWN * 0.15, 12.5, 3.4, TEAL)
        plabel = Text("expected in a normoxic cell", font=SERIF, color=TEAL,
                      font_size=20).next_to(panel, UP, buff=0.2)
        n1 = _chip("O2  adequate", accent=TEAL, size=24).move_to(LEFT * 4.8 + DOWN * 0.15)
        n2 = _chip("PHD  hydroxylates HIF-1a", accent=TEAL, size=22).move_to(LEFT * 1.4 + DOWN * 0.15)
        n3 = _chip("HIF-1a  destroyed", accent=TEAL, size=24).move_to(RIGHT * 3.4 + DOWN * 0.15)
        a1 = _arrow(n1.get_right() + RIGHT * 0.08, n2.get_left() + LEFT * 0.08, TEAL)
        a2 = _arrow(n2.get_right() + RIGHT * 0.08, n3.get_left() + LEFT * 0.08, TEAL)
        self.play(FadeIn(panel), FadeIn(plabel), run_time=0.7)
        self.play(FadeIn(n1), run_time=0.5)
        self.play(GrowArrow(a1), FadeIn(n2), run_time=0.8)
        self.play(GrowArrow(a2), FadeIn(n3), run_time=0.8)
        self.wait(max(0.5, total - 2.8))


class B06_MechanismCard(Scene):
    """Section card — THE MECHANISM."""
    def construct(self):
        total = DUR["B06"]
        card = _panel_rect(ORIGIN, 8.0, 3.0, SLATE)
        t1 = Text("THE MECHANISM", font=DISPLAY, color=WHITE, font_size=52, weight=BOLD)
        t2 = Text("what VHL actually does", font=SERIF, color=WHITE, font_size=26,
                  slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(card), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B07_NormalDegradation(Scene):
    """Normal pathway: PHD hydroxylates -> VHL binds -> proteasome destroys."""
    def construct(self):
        total = DUR["B07"]
        # four nodes in a horizontal chain
        n1 = _chip("PHD", accent=TEAL, size=26).move_to(LEFT * 5.2 + UP * 0.4)
        n2_label = Text("HIF-1a + OH", font=SERIF, color=INK, font_size=22)
        n2_box = Rectangle(width=2.0, height=0.65).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        n2 = VGroup(n2_box, n2_label).move_to(LEFT * 1.8 + UP * 0.4)
        n3 = _chip("VHL binds", accent=TEAL, size=26).move_to(RIGHT * 1.8 + UP * 0.4)
        n4 = _chip("proteasome", accent=TEAL, size=26).move_to(RIGHT * 5.2 + UP * 0.4)
        a1 = _arrow(n1.get_right() + RIGHT * 0.08, n2.get_left() + LEFT * 0.08, TEAL)
        a2 = _arrow(n2.get_right() + RIGHT * 0.08, n3.get_left() + LEFT * 0.08, TEAL)
        a3 = _arrow(n3.get_right() + RIGHT * 0.08, n4.get_left() + LEFT * 0.08, TEAL)
        gone = Text("HIF-1a: gone", font=SERIF, color=TEAL, font_size=22, weight=BOLD)
        gone.next_to(n4, DOWN, buff=0.4)
        hl = SerifLabel("half-life ~5 min", TEAL, size=22).move_to(DOWN * 1.5)
        self.play(FadeIn(n1), run_time=0.5)
        self.play(GrowArrow(a1), FadeIn(n2), run_time=0.8)
        self.play(GrowArrow(a2), FadeIn(n3), run_time=0.8)
        self.play(GrowArrow(a3), FadeIn(n4), run_time=0.8)
        self.play(FadeIn(gone), FadeIn(hl, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 3.6))


class B08_VHLAbsent(Scene):
    """THE MECHANISM reveal: PHD works (TEAL), VHL missing (CRIMSON dashed + GOLD), HIF piles up."""
    def construct(self):
        total = DUR["B08"]
        n1 = _chip("PHD", accent=TEAL, size=26).move_to(LEFT * 5.2 + UP * 0.6)
        n2_label = Text("HIF-1a + OH", font=SERIF, color=INK, font_size=22)
        n2_box = Rectangle(width=2.0, height=0.65).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        n2 = VGroup(n2_box, n2_label).move_to(LEFT * 1.8 + UP * 0.6)
        a1 = _arrow(n1.get_right() + RIGHT * 0.08, n2.get_left() + LEFT * 0.08, TEAL)
        # VHL node — dashed CRIMSON box
        vhl_dashed = _dashed_rect(RIGHT * 1.8 + UP * 0.6, 2.2, 0.75, CRIMSON)
        vhl_text = Text("VHL absent", font=SERIF, color=CRIMSON, font_size=22, weight=BOLD)
        vhl_text.move_to(RIGHT * 1.8 + UP * 0.6)
        # GOLD highlight bar on the missing VHL node (fill only, behind the label)
        _vhl_center = np.array([1.8, 0.6, 0.0])
        gold = _gold_bar(_vhl_center, w=2.3, h=0.48)
        # accumulating HIF-1a pile
        hif_stack = VGroup(*[
            Rectangle(width=2.0, height=0.3)
            .set_fill(CRIMSON, 0.18 + i * 0.06)
            .set_stroke(CRIMSON, 1.2)
            for i in range(4)
        ]).arrange(UP, buff=0.05).move_to(RIGHT * 5.2 + DOWN * 0.1)
        pile_label = SerifLabel("HIF-1a accumulates", CRIMSON, size=22)
        pile_label.next_to(hif_stack, DOWN, buff=0.3)
        a2_dashed = DashedLine(n2.get_right() + RIGHT * 0.1, vhl_dashed.get_left() + LEFT * 0.1,
                               color=INK, stroke_width=2, dash_length=0.18)
        self.play(FadeIn(n1), run_time=0.5)
        self.play(GrowArrow(a1), FadeIn(n2), run_time=0.8)
        self.play(Create(a2_dashed), run_time=0.6)
        self.play(Create(vhl_dashed), FadeIn(vhl_text), run_time=0.8)
        self.play(FadeIn(gold), run_time=0.5)
        for bar in hif_stack:
            self.play(FadeIn(bar, shift=UP * 0.08), run_time=0.3)
        self.play(FadeIn(pile_label), run_time=0.6)
        self.wait(max(0.5, total - 4.0))


class B09_ConstitutiveHIF(Scene):
    """Constitutive HIF program: HIF floods nucleus, three CRIMSON outputs in normoxic cell."""
    def construct(self):
        total = DUR["B09"]
        nucleus = Circle(radius=1.1).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 2.5)
        nucleus.move_to(LEFT * 3.0)
        nuc_label = Text("nucleus", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        nuc_label.move_to(nucleus.get_center())
        hif_chip = _chip("HIF-1a", accent=CRIMSON, size=24).move_to(LEFT * 3.0)
        context = SerifLabel("well-oxygenated cell", INK, size=21).move_to(LEFT * 3.0 + DOWN * 1.8)
        out1 = _chip("GLUT1", accent=CRIMSON, size=24).move_to(RIGHT * 3.5 + UP * 1.4)
        out2 = _chip("glycolytic enzymes", accent=CRIMSON, size=24).move_to(RIGHT * 3.5)
        out3 = _chip("VEGF", accent=CRIMSON, size=24).move_to(RIGHT * 3.5 + DOWN * 1.4)
        arr1 = _arrow(nucleus.get_right() + RIGHT * 0.05, out1.get_left() + LEFT * 0.08, CRIMSON)
        arr2 = _arrow(nucleus.get_right() + RIGHT * 0.05, out2.get_left() + LEFT * 0.08, CRIMSON)
        arr3 = _arrow(nucleus.get_right() + RIGHT * 0.05, out3.get_left() + LEFT * 0.08, CRIMSON)
        self.play(Create(nucleus), FadeIn(nuc_label), run_time=0.8)
        self.play(ReplacementTransform(nuc_label, hif_chip), run_time=0.5)
        self.play(FadeIn(context), run_time=0.5)
        self.play(GrowArrow(arr1), FadeIn(out1), run_time=0.6)
        self.play(GrowArrow(arr2), FadeIn(out2), run_time=0.6)
        self.play(GrowArrow(arr3), FadeIn(out3), run_time=0.6)
        self.wait(max(0.5, total - 3.6))


class B10_SideBySide(Scene):
    """THE COMPARE: left panel TEAL (normal), right panel CRIMSON (VHL-null RCC)."""
    def construct(self):
        total = DUR["B10"]
        # left panel — normal cell
        lp = _panel_rect(LEFT * 3.3 + DOWN * 0.1, 5.8, 5.5, TEAL)
        ltitle = Text("normal cell", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        ltitle.next_to(lp, UP, buff=0.18)
        ln1 = _chip("PHD works", accent=TEAL, size=20).move_to(LEFT * 4.3 + UP * 1.2)
        ln2 = _chip("VHL binds", accent=TEAL, size=20).move_to(LEFT * 4.3 + UP * 0.2)
        ln3 = _chip("HIF-1a destroyed", accent=TEAL, size=20).move_to(LEFT * 4.3 + DOWN * 0.8)
        la1 = Arrow(ln1.get_bottom(), ln2.get_top(), color=TEAL, stroke_width=2.5,
                    buff=0.08, tip_length=0.18)
        la2 = Arrow(ln2.get_bottom(), ln3.get_top(), color=TEAL, stroke_width=2.5,
                    buff=0.08, tip_length=0.18)
        lgone = Text("HIF: absent", font=SERIF, color=TEAL, font_size=19, weight=BOLD)
        lgone.next_to(ln3, DOWN, buff=0.35)
        # right panel — VHL-null RCC
        rp = _panel_rect(RIGHT * 3.3 + DOWN * 0.1, 5.8, 5.5, CRIMSON)
        rtitle = Text("clear cell RCC", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        rtitle.next_to(rp, UP, buff=0.18)
        rn1 = _chip("PHD works", accent=TEAL, size=20).move_to(RIGHT * 2.3 + UP * 1.2)
        # VHL absent — dashed
        rvhl = _dashed_rect(RIGHT * 2.3 + UP * 0.2, 2.0, 0.6, CRIMSON)
        rvhl_t = Text("VHL absent", font=SERIF, color=CRIMSON, font_size=18, weight=BOLD)
        rvhl_t.move_to(RIGHT * 2.3 + UP * 0.2)
        # HIF piles up
        rstack = VGroup(*[
            Rectangle(width=1.8, height=0.25)
            .set_fill(CRIMSON, 0.15 + i * 0.07)
            .set_stroke(CRIMSON, 1.0)
            for i in range(3)
        ]).arrange(UP, buff=0.04).move_to(RIGHT * 2.3 + DOWN * 0.9)
        raccu = Text("HIF: accumulating", font=SERIF, color=CRIMSON, font_size=19, weight=BOLD)
        raccu.next_to(rstack, DOWN, buff=0.3)
        ra1 = Arrow(rn1.get_bottom(), rvhl.get_top(), color=TEAL, stroke_width=2.5,
                    buff=0.08, tip_length=0.18)
        # dividing line
        div = Line(UP * 3.0, DOWN * 3.0, color=INK, stroke_width=1.5)
        div.move_to(ORIGIN)
        # animate
        self.play(FadeIn(lp), FadeIn(rp), FadeIn(div), run_time=0.8)
        self.play(FadeIn(ltitle), FadeIn(rtitle), run_time=0.6)
        self.play(FadeIn(ln1), FadeIn(rn1), run_time=0.6)
        self.play(Create(la1), GrowArrow(ra1), run_time=0.7)
        self.play(FadeIn(ln2), Create(rvhl), FadeIn(rvhl_t), run_time=0.8)
        self.play(Create(la2), run_time=0.6)
        self.play(FadeIn(ln3), run_time=0.5)
        self.play(FadeIn(lgone), run_time=0.5)
        for bar in rstack:
            self.play(FadeIn(bar, shift=UP * 0.06), run_time=0.25)
        self.play(FadeIn(raccu), run_time=0.5)
        self.wait(max(0.5, total - 5.4))


class B11_ImplicationCard(Scene):
    """Section card — THE IMPLICATION."""
    def construct(self):
        total = DUR["B11"]
        card = _panel_rect(ORIGIN, 8.0, 3.0, SLATE)
        t1 = Text("THE IMPLICATION", font=DISPLAY, color=WHITE, font_size=52, weight=BOLD)
        t2 = Text("what VHL loss means for the tumor", font=SERIF, color=WHITE,
                  font_size=26, slant=ITALIC)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(FadeIn(card), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), run_time=0.6)
        self.wait(max(0.5, total - 1.9))


class B13_NormalTimeline(Scene):
    """THE EXAMPLE — normal cell: synthesis -> PHD 45s -> VHL 10s -> destroyed, half-life ~5 min."""
    def construct(self):
        total = DUR["B13"]
        eye = Text("normal kidney cell (illustrative)", font=SERIF, color=TEAL,
                   font_size=21).to_edge(UP, buff=0.6)
        # timeline nodes
        s0 = _chip("synthesis", accent=TEAL, size=22).move_to(LEFT * 5.4 + DOWN * 0.2)
        s1_box = Rectangle(width=2.0, height=0.6).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        s1_t = Text("PHD tags", font=SERIF, color=INK, font_size=20)
        s1_t45 = Text("~45 sec", font=MONO, color=TEAL, font_size=18)
        s1 = VGroup(s1_box, VGroup(s1_t, s1_t45).arrange(DOWN, buff=0.05)).move_to(LEFT * 2.1 + DOWN * 0.2)
        s2 = _chip("VHL binds", accent=TEAL, size=22).move_to(RIGHT * 1.3 + DOWN * 0.2)
        s2_t = Text("~10 sec", font=MONO, color=TEAL, font_size=18)
        s2_t.next_to(s2, DOWN, buff=0.15)
        s3 = _chip("destroyed", accent=TEAL, size=22).move_to(RIGHT * 4.8 + DOWN * 0.2)
        a0 = _arrow(s0.get_right() + RIGHT * 0.08, s1.get_left() + LEFT * 0.08, TEAL)
        a1 = _arrow(s1.get_right() + RIGHT * 0.08, s2.get_left() + LEFT * 0.08, TEAL)
        a2 = _arrow(s2.get_right() + RIGHT * 0.08, s3.get_left() + LEFT * 0.08, TEAL)
        hl_text = Text("half-life ~5 min", font=SERIF, color=TEAL, font_size=22)
        hl_text.move_to(DOWN * 1.7)
        undet = SerifLabel("steady state: undetectable", TEAL, size=21).move_to(DOWN * 2.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(s0), run_time=0.4)
        self.play(GrowArrow(a0), FadeIn(s1), run_time=0.7)
        self.play(GrowArrow(a1), FadeIn(s2), FadeIn(s2_t), run_time=0.7)
        self.play(GrowArrow(a2), FadeIn(s3), run_time=0.7)
        self.play(FadeIn(hl_text), FadeIn(undet), run_time=0.7)
        self.wait(max(0.5, total - 3.7))


class B14_VHLNullTimeline(Scene):
    """THE EXAMPLE — VHL-null RCC: PHD works (TEAL), VHL absent (CRIMSON), 40x accumulation + GOLD."""
    def construct(self):
        total = DUR["B14"]
        eye = Text("VHL-null clear cell RCC (illustrative)", font=SERIF, color=CRIMSON,
                   font_size=21).to_edge(UP, buff=0.6)
        # same layout as B13 but divergent at VHL
        s0 = _chip("synthesis", accent=TEAL, size=22).move_to(LEFT * 5.4 + UP * 0.7)
        s1_box = Rectangle(width=2.0, height=0.6).set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        s1_t = Text("PHD tags", font=SERIF, color=INK, font_size=20)
        s1_t45 = Text("~45 sec", font=MONO, color=TEAL, font_size=18)
        s1 = VGroup(s1_box, VGroup(s1_t, s1_t45).arrange(DOWN, buff=0.05)).move_to(LEFT * 2.1 + UP * 0.7)
        a0 = _arrow(s0.get_right() + RIGHT * 0.08, s1.get_left() + LEFT * 0.08, TEAL)
        # VHL absent
        vhl_d = _dashed_rect(RIGHT * 1.3 + UP * 0.7, 2.1, 0.65, CRIMSON)
        vhl_t = Text("VHL absent", font=SERIF, color=CRIMSON, font_size=20, weight=BOLD)
        vhl_t.move_to(RIGHT * 1.3 + UP * 0.7)
        a1 = DashedLine(s1.get_right() + RIGHT * 0.1, vhl_d.get_left() + LEFT * 0.1,
                        color=INK, stroke_width=2, dash_length=0.18)
        # accumulation pile
        stack = VGroup(*[
            Rectangle(width=1.9, height=0.28)
            .set_fill(CRIMSON, 0.14 + i * 0.06)
            .set_stroke(CRIMSON, 1.2)
            for i in range(5)
        ]).arrange(UP, buff=0.04).move_to(RIGHT * 4.8 + UP * 0.2)
        fold_text = Text("~40x normal", font=SERIF, color=CRIMSON, font_size=22, weight=BOLD)
        fold_text.next_to(stack, DOWN, buff=0.2)
        # GOLD highlight bar on the fold number (fill only, fixed coord)
        _fold_center = np.array([4.8, -0.1, 0.0])
        gold = _gold_bar(_fold_center, w=2.4, h=0.48)
        illu = SerifLabel("after 4 hours  (illustrative)", CRIMSON, size=19)
        illu.next_to(fold_text, DOWN, buff=0.25)
        # output chips
        out1 = _chip("GLUT1 up", accent=CRIMSON, size=19).move_to(LEFT * 4.5 + DOWN * 2.2)
        out2 = _chip("VEGF secreted", accent=CRIMSON, size=19).move_to(ORIGIN + DOWN * 2.2)
        out3 = _chip("glycolytic enzymes up", accent=CRIMSON, size=19).move_to(RIGHT * 4.5 + DOWN * 2.2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(s0), run_time=0.4)
        self.play(GrowArrow(a0), FadeIn(s1), run_time=0.7)
        self.play(Create(a1), Create(vhl_d), FadeIn(vhl_t), run_time=0.9)
        for bar in stack:
            self.play(FadeIn(bar, shift=UP * 0.06), run_time=0.22)
        self.play(FadeIn(gold), FadeIn(fold_text), run_time=0.6)
        self.play(FadeIn(illu), run_time=0.5)
        self.play(LaggedStart(FadeIn(out1), FadeIn(out2), FadeIn(out3), lag_ratio=0.25),
                  run_time=0.9)
        self.wait(max(0.5, total - 5.5))


class B15_End(Scene):
    """RECAP endcard — question answered, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B15"]
        kicker = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("VHL reads the hydroxylation tag", font=DISPLAY, color=INK,
                  font_size=38, weight=BOLD)
        t2 = Text("and commits HIF-1alpha to destruction.", font=DISPLAY, color=INK,
                  font_size=38, weight=BOLD)
        t3 = Text("Lose VHL and HIF-1alpha accumulates", font=SERIF, color=CRIMSON,
                  font_size=28)
        t4 = Text("regardless of oxygen.", font=SERIF, color=CRIMSON, font_size=28)
        block1 = VGroup(t1, t2).arrange(DOWN, buff=0.15)
        block2 = VGroup(t3, t4).arrange(DOWN, buff=0.12)
        stack = VGroup(block1, block2).arrange(DOWN, buff=0.4).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2)
        kicker.next_to(stack, UP, buff=0.6)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(block1), Create(u), run_time=1.0)
        self.play(FadeIn(block2, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.5, total - 2.3))
