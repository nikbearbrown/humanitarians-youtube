"""vox_scenes.py — Why More Context Can Make the Output Worse
(vox-context-priority-weight, slate cut, 16:9)

Color law (teardown):
  INK     = labeled / correctly weighted documents
  CRIMSON = unlabeled / incorrectly weighted documents
  SLATE   = neutral structure

Exclusions: no RAG, no token limits, no chunking, no context-window literature.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 9.0, "B04": 12.0, "B05": 11.0, "B06": 11.0,
    "B07": 10.0, "B08": 12.0, "B09": 11.0, "B10": 10.0, "B11": 13.0,
    "B12": 12.0, "B13": 11.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


def _label(text, color=INK, size=26):
    return Text(text, font=SERIF, color=color, font_size=size)


def _chip(text, accent=SLATE, size=20):
    return LabelChip(text, accent=accent, size=size)


def _doc_rect(width, height, color=INK, opacity=0.15):
    r = Rectangle(width=width, height=height)
    r.set_fill(color, opacity).set_stroke(color, 1.5)
    return r


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("PROMPT ENGINEERING", font=DISPLAY, color=CRIMSON,
                   font_size=22, weight=BOLD)
        t1 = Text("Why more context can", font=SERIF, color=INK, font_size=54, weight=BOLD)
        t2 = Text("make the output worse", font=SERIF, color=INK, font_size=54, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        sub = _label("unlabeled documents create false priority orders", SLATE, 26)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


class B03_Question(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("Why did more context", font=SERIF, color=INK, font_size=50, weight=BOLD)
        q2 = Text("produce worse output?", font=SERIF, color=INK, font_size=50, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.14, q2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.6)
        self.play(FadeIn(q2), Create(u), run_time=0.8)
        self.wait(max(0.5, total - 1.4))


class B04_DocumentStack(Scene):
    """Three unlabeled documents stacked — shown as undifferentiated block."""
    def construct(self):
        total = DUR["B04"]
        title = _label("Without labels: one undifferentiated block", INK, 28)
        title.to_edge(UP, buff=0.6)
        # three docs stacked (biggest at bottom, smallest at top)
        doc_big = _doc_rect(4.0, 2.0, CRIMSON, 0.12)
        doc_big.move_to(DOWN * 0.8)
        lbl_big = _label("brand guide (15 pages)", CRIMSON, 22)
        lbl_big.next_to(doc_big, RIGHT, buff=0.3)
        doc_med = _doc_rect(4.0, 0.9, CRIMSON, 0.15)
        doc_med.move_to(DOWN * 0.0)
        lbl_med = _label("competitor analysis (6 pages)", CRIMSON, 22)
        lbl_med.next_to(doc_med, RIGHT, buff=0.3)
        doc_small = _doc_rect(4.0, 0.35, CRIMSON, 0.18)
        doc_small.move_to(UP * 0.6)
        lbl_small = _label("brief (1 page)", CRIMSON, 22)
        lbl_small.next_to(doc_small, RIGHT, buff=0.3)
        note = SerifLabel("Claude sees one block — no labels, no hierarchy", CRIMSON, size=26)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(doc_big), FadeIn(lbl_big), run_time=0.6)
        self.play(FadeIn(doc_med), FadeIn(lbl_med), run_time=0.6)
        self.play(FadeIn(doc_small), FadeIn(lbl_small), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.9))


class B05_WeightByLength(Scene):
    """Documents with weight bars proportional to length."""
    def construct(self):
        total = DUR["B05"]
        title = _label("Length and formality predict attention weight", INK, 28)
        title.to_edge(UP, buff=0.6)
        docs = [
            ("BRAND GUIDE", 15, "long + formal"),
            ("COMPETITOR ANALYSIS", 6, "medium + formal"),
            ("CLIENT BRIEF (FYI)", 1, "short + informal"),
        ]
        rows = VGroup()
        for name, pages, desc in docs:
            chip = _chip(name, accent=CRIMSON, size=18)
            bar_w = pages / 15 * 4.5
            bar = Rectangle(width=bar_w, height=0.35)
            bar.set_fill(CRIMSON, 0.7 - pages * 0.01).set_stroke(width=0, opacity=0)
            page_lbl = _label(f"{pages}p — {desc}", CRIMSON, 20)
            row = VGroup(chip, bar, page_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(DOWN * 0.1)
        note = SerifLabel("more pages = more influence (without your label)", CRIMSON, size=26)
        note.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B06_PriorityOrder(Scene):
    """Proportional weight bars: brief gets 1/15 the influence."""
    def construct(self):
        total = DUR["B06"]
        title = _label("The brief's hard constraint gets proportional weight", INK, 28)
        title.to_edge(UP, buff=0.6)
        # weight visualization: three bars
        bar_brand = Rectangle(width=5.5, height=0.55)
        bar_brand.set_fill(CRIMSON, 0.7).set_stroke(width=0, opacity=0)
        bar_brand.move_to(LEFT * 0.5 + UP * 1.0)
        lbl_brand = _label("brand guide — 15/22 weight", CRIMSON, 22)
        lbl_brand.next_to(bar_brand, RIGHT, buff=0.3)
        bar_comp = Rectangle(width=2.2, height=0.55)
        bar_comp.set_fill(CRIMSON, 0.55).set_stroke(width=0, opacity=0)
        bar_comp.move_to(LEFT * 1.9 + DOWN * 0.0)
        lbl_comp = _label("competitor — 6/22", CRIMSON, 22)
        lbl_comp.next_to(bar_comp, RIGHT, buff=0.3)
        bar_brief = Rectangle(width=0.37, height=0.55)
        bar_brief.set_fill(CRIMSON, 0.4).set_stroke(CRIMSON, 1.5)
        bar_brief.move_to(LEFT * 2.7 + DOWN * 1.0)
        lbl_brief = _label("brief — 1/22", CRIMSON, 22)
        lbl_brief.next_to(bar_brief, RIGHT, buff=0.3)
        ring = HandRing(bar_brief, color=CRIMSON)
        note = SerifLabel("'nothing blue' constraint gets 1/22 of the attention", CRIMSON, size=24)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(bar_brand), FadeIn(lbl_brand), run_time=0.6)
        self.play(FadeIn(bar_comp), FadeIn(lbl_comp), run_time=0.6)
        self.play(FadeIn(bar_brief), FadeIn(lbl_brief), run_time=0.6)
        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.7))


class B07_SectionCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("More unlabeled context =", font=DISPLAY, color=INK,
                  font_size=46, weight=BOLD)
        t2 = Text("more false priority", font=DISPLAY, color=CRIMSON,
                  font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2, scale=0.95), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B08_LabeledSources(Scene):
    """Same three documents, now labeled with priority tiers."""
    def construct(self):
        total = DUR["B08"]
        title = _label("Label each source before it appears", INK, 28)
        title.to_edge(UP, buff=0.6)
        labels_data = [
            ("BINDING CONSTRAINT", "client brief — nothing blue", INK),
            ("BACKGROUND", "competitor analysis — context only", SLATE),
            ("BACKGROUND", "brand guide — do not override the brief", SLATE),
        ]
        rows = VGroup()
        for label, doc, color in labels_data:
            label_chip = _chip(label, accent=color, size=18)
            doc_lbl = _label(doc, color, 24)
            row = VGroup(label_chip, doc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(DOWN * 0.1)
        note = SerifLabel("you assign the priority order — not document length", INK, size=26)
        note.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.25),
                  run_time=1.2)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B09_CorrectPriority(Scene):
    """Correct weight distribution: brief at full weight."""
    def construct(self):
        total = DUR["B09"]
        title = _label("Labeled: brief gets full weight as binding constraint", INK, 28)
        title.to_edge(UP, buff=0.6)
        # brief now at full
        bar_brief = Rectangle(width=5.5, height=0.55)
        bar_brief.set_fill(INK, 0.7).set_stroke(width=0, opacity=0)
        bar_brief.move_to(LEFT * 0.5 + UP * 1.0)
        lbl_brief = _label("client brief — BINDING", INK, 22)
        lbl_brief.next_to(bar_brief, RIGHT, buff=0.3)
        # others at low weight
        bar_bg = Rectangle(width=1.8, height=0.55)
        bar_bg.set_fill(SLATE, 0.4).set_stroke(width=0, opacity=0)
        bar_bg.move_to(LEFT * 2.4 + DOWN * 0.2)
        lbl_bg = _label("brand guide + analysis — background", SLATE, 22)
        lbl_bg.next_to(bar_bg, RIGHT, buff=0.3)
        result = SerifLabel("output: nothing blue honored as a hard constraint", INK, size=26)
        result.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(bar_brief), FadeIn(lbl_brief), run_time=0.7)
        self.play(FadeIn(bar_bg), FadeIn(lbl_bg), run_time=0.6)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.4))


class B10_AnyMultiDoc(Scene):
    """Pattern applies to any multi-document paste."""
    def construct(self):
        total = DUR["B10"]
        title = _label("Any multi-document paste has this problem", INK, 28)
        title.to_edge(UP, buff=0.6)
        examples = [
            ("POLICY DOC", "long", CRIMSON),
            ("MEETING NOTES", "medium", CRIMSON),
            ("EMAIL OVERRIDE", "short — most current", INK),
        ]
        rows = VGroup()
        for doc, size, color in examples:
            chip = _chip(doc, accent=color, size=18)
            sz = _label(size, color, 22)
            row = VGroup(chip, sz).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).move_to(UP * 0.3)
        label_note = _label("label 'email overrides policy on timeline'", INK, 24)
        arrow = Arrow(UP * 0.5, DOWN * 0.1, color=INK, stroke_width=3, buff=0.1)
        arrow.move_to(DOWN * 0.6)
        result = SerifLabel("Claude reflects what you actually intended", INK, size=26)
        result.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.2), run_time=0.9)
        self.play(FadeIn(label_note), GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.7))


class B11_SchoolExample(Scene):
    """School admin: handbook dominates; override email invisible."""
    def construct(self):
        total = DUR["B11"]
        title = _label("Handbook (20p) drowns out override email (2 sentences)", INK, 26)
        title.to_edge(UP, buff=0.6)
        doc1 = _doc_rect(3.5, 2.2, CRIMSON, 0.12)
        doc1.move_to(LEFT * 3.5 + DOWN * 0.2)
        lbl1 = _label("district handbook\n20 pages", CRIMSON, 22)
        lbl1.move_to(LEFT * 3.5 + DOWN * 0.2)
        doc2 = _doc_rect(3.5, 0.8, CRIMSON, 0.15)
        doc2.move_to(LEFT * 0.5 + UP * 0.3)
        lbl2 = _label("teacher memo, 3 pages", CRIMSON, 22)
        lbl2.next_to(doc2, RIGHT, buff=0.3)
        doc3 = _doc_rect(3.5, 0.22, CRIMSON, 0.2)
        doc3.move_to(LEFT * 0.5 + DOWN * 0.4)
        lbl3 = _label("override email — 2 sentences", CRIMSON, 22)
        lbl3.next_to(doc3, RIGHT, buff=0.3)
        out = _chip("OUTPUT: summarizes handbook", accent=CRIMSON, size=22)
        out.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(doc1), FadeIn(lbl1), run_time=0.6)
        self.play(FadeIn(doc2), FadeIn(lbl2), run_time=0.5)
        self.play(FadeIn(doc3), FadeIn(lbl3), run_time=0.5)
        self.play(FadeIn(out), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


class B12_SchoolFixed(Scene):
    """Two labels reverse the priority order."""
    def construct(self):
        total = DUR["B12"]
        title = _label("Two labels — three words each — fix the priority", INK, 28)
        title.to_edge(UP, buff=0.6)
        labels_data = [
            ("BINDING OVERRIDE", "override email — takes priority on section 4", INK),
            ("BACKGROUND", "district handbook — background only", SLATE),
        ]
        rows = VGroup()
        for lbl, doc, color in labels_data:
            chip = _chip(lbl, accent=color, size=18)
            doc_lbl = _label(doc, color, 24)
            row = VGroup(chip, doc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(UP * 0.2)
        result = SerifLabel("output: reflects the override — correct policy summary", INK, size=26)
        result.next_to(rows, DOWN, buff=0.5)
        note = _label("three words of labeling reversed the priority order", INK, 26)
        note.next_to(result, DOWN, buff=0.3)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.3),
                  run_time=0.9)
        self.play(FadeIn(result, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.6))


class B13_Practice(Scene):
    """Three label categories before any multi-doc paste."""
    def construct(self):
        total = DUR["B13"]
        title = _label("Before pasting multiple documents:", INK, 28)
        title.to_edge(UP, buff=0.6)
        categories = [
            ("PRIMARY", "binding source — use this first", INK),
            ("BACKGROUND", "context only — do not quote directly", SLATE),
            ("OVERRIDE", "takes priority over conflicting information above", CRIMSON),
        ]
        rows = VGroup()
        for name, desc, color in categories:
            chip = _chip(name, accent=color, size=20)
            desc_lbl = _label(desc, color, 24)
            row = VGroup(chip, desc_lbl).arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4).move_to(DOWN * 0.1)
        note = SerifLabel("then prune each to what the task actually needs", INK, size=26)
        note.next_to(rows, DOWN, buff=0.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2),
                  run_time=1.0)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.1))


class B14_End(Scene):
    def construct(self):
        total = DUR["B14"]
        t1 = Text("Unlabeled context creates false priority orders.", font=SERIF,
                  color=INK, font_size=38, weight=BOLD)
        t2 = Text("Label your sources. Assign the weight yourself.", font=SERIF,
                  color=INK, font_size=38, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        topic = Text("PROMPT ENGINEERING", font=DISPLAY, color=SLATE,
                     font_size=22, weight=BOLD)
        topic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(topic, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.1))
