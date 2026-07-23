import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# brca-parp-synthetic-lethality — Research BRCA x PARP Synthetic Lethality
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_SyntheticLethality(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        title = Text("BRCA x PARP: Synthetic Lethality", font=SERIF, color=INK, font_size=30, weight="BOLD")
        title.move_to(UP * 3.0)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)

        # Column / row headers
        col_hdrs = VGroup(
            Text("PARP active", font=SERIF, color=SLATE, font_size=22),
            Text("PARP inhibited", font=SERIF, color=SLATE, font_size=22),
        ).arrange(RIGHT, buff=2.5)
        col_hdrs.move_to(UP * 1.8)

        row_hdrs = VGroup(
            Text("BRCA wild-type", font=SERIF, color=SLATE, font_size=22),
            Text("BRCA mutant", font=SERIF, color=SLATE, font_size=22),
        ).arrange(DOWN, buff=1.5)
        row_hdrs.move_to(LEFT * 3.8 + DOWN * 0.2)

        self.play(FadeIn(col_hdrs, shift=UP * 0.2), FadeIn(row_hdrs, shift=LEFT * 0.2), run_time=0.5)

        # Four cells
        positions = [
            (RIGHT * 0.5 + UP * 0.9, "Survives", INK),
            (RIGHT * 3.2 + UP * 0.9, "Survives", INK),
            (RIGHT * 0.5 + DOWN * 0.7, "Survives (HR repairs)", INK),
            (RIGHT * 3.2 + DOWN * 0.7, "LETHAL", CRIMSON),
        ]
        cells = VGroup()
        for pos, label, clr in positions:
            box = Rectangle(width=2.4, height=1.0)
            box.set_fill(GOLD if clr == CRIMSON else WHITE, 0.4 if clr == CRIMSON else 0.0)
            box.set_stroke(clr, 2)
            box.move_to(pos)
            txt = Text(label, font=SERIF, color=clr, font_size=20)
            txt.move_to(pos)
            cells.add(VGroup(box, txt))

        for cell in cells:
            self.play(Create(cell[0]), FadeIn(cell[1]), run_time=0.4)

        # Resistance note below last cell
        note = Text("BRCA reversion = resistance", font=SERIF, color=SLATE, font_size=18)
        note.move_to(DOWN * 1.9 + RIGHT * 2.0)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.4)
        self.wait(max(0.1, d - 5.0))


class B06_SyntheticLethality2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("Extension: MTAP-PRMT5", font=SERIF, color=INK, font_size=30, weight="BOLD")
        title.move_to(UP * 3.0)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)

        # BRCA/PARP confirmed pair
        box1 = Rectangle(width=5.0, height=1.0)
        box1.set_fill(WHITE, 0).set_stroke(INK, 2)
        box1.move_to(UP * 1.5)
        lbl1 = Text("BRCA/PARP  |  confirmed  |  FDA-approved", font=SERIF, color=INK, font_size=21)
        lbl1.move_to(UP * 1.5)
        self.play(Create(box1), FadeIn(lbl1), run_time=0.5)

        # MTAP-PRMT5 emerging pair
        box2 = Rectangle(width=5.0, height=1.0)
        box2.set_fill(GOLD, 0.5).set_stroke(CRIMSON, 2)
        box2.move_to(UP * 0.1)
        lbl2 = Text("MTAP-PRMT5  |  Phase 2  |  ORR pending", font=SERIF, color=CRIMSON, font_size=21)
        lbl2.move_to(UP * 0.1)
        self.play(Create(box2), FadeIn(lbl2), run_time=0.6)

        note = Text("Same geometric logic, weaker clinical evidence", font=SERIF, color=SLATE, font_size=20)
        note.move_to(DOWN * 1.2)
        self.play(FadeIn(note, shift=DOWN * 0.3), run_time=0.4)
        self.wait(max(0.1, d - 4.5))
