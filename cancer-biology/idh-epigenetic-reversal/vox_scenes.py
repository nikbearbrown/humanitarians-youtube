import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# idh-epigenetic-reversal — Research IDH Mutations and Epigenetic Reprogramming
# CANCER BIOLOGY · CLI video · 10 beats
# Color law: INK = neutral/normal; CRIMSON = key finding/vulnerability/risk

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_IDHCausalChain(Scene):
    def construct(self):
        d = DUR.get('B04', 14)
        title = Text("IDH Mutation Causal Chain", font=SERIF, color=INK, font_size=26, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        nodes = [
            ("mutant IDH", CRIMSON),
            ("2HG\noncometabolite", CRIMSON),
            ("TET2/KDM\nblocked", CRIMSON),
            ("hyper-\nmethylation", CRIMSON),
            ("diff. locked", CRIMSON),
        ]
        box_w, box_h = 1.8, 0.85
        spacing = 2.3
        total_w = (len(nodes) - 1) * spacing
        start_x = -total_w / 2
        node_grps = []

        for i, (label, clr) in enumerate(nodes):
            x = start_x + i * spacing
            box = Rectangle(width=box_w, height=box_h)
            box.set_fill(GOLD, 0.5).set_stroke(clr, 2)
            box.move_to([x, 0.5, 0])
            txt = Text(label, font=SERIF, color=clr, font_size=17)
            txt.move_to([x, 0.5, 0])
            grp = VGroup(box, txt)
            node_grps.append(grp)
            self.play(Create(box), FadeIn(txt), run_time=0.35)
            if i < len(nodes) - 1:
                arr = Arrow([x + box_w/2, 0.5, 0], [x + spacing - box_w/2, 0.5, 0],
                            color=CRIMSON, stroke_width=2.5, buff=0.05)
                self.play(Create(arr), run_time=0.2)

        note = Text("drug removes 2HG -> chain reverses", font=SERIF, color=SLATE, font_size=19)
        note.move_to(DOWN * 1.4)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.4)
        self.wait(max(0.1, d - 7.0))


class B06_IDHCausalChain2(Scene):
    def construct(self):
        d = DUR.get('B06', 12)
        title = Text("Other Oncometabolites", font=SERIF, color=INK, font_size=26, weight="BOLD")
        title.move_to(UP * 3.2)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.4)

        row_data = [
            ("IDH1/2   2HG   ivosidenib / enasidenib   FDA approved", CRIMSON, GOLD, 0.5, UP * 1.8),
            ("SDH   succinate   no approved inhibitor   Phase 1 only", SLATE, WHITE, 0.0, UP * 0.7),
            ("FH   fumarate   no approved inhibitor   preclinical", SLATE, WHITE, 0.0, DOWN * 0.4),
        ]
        for label, stroke_c, fill_c, fill_op, pos in row_data:
            box = Rectangle(width=11.0, height=0.68)
            box.set_fill(fill_c, fill_op).set_stroke(stroke_c, 2)
            box.move_to(pos)
            txt = Text(label, font=SERIF, color=stroke_c, font_size=16)
            txt.move_to(pos)
            self.play(Create(box), run_time=0.3)
            self.play(FadeIn(txt), run_time=0.3)

        note = Text("Same logic, earlier in the pipeline", font=SERIF, color=SLATE, font_size=19)
        note.move_to(DOWN * 1.6)
        self.play(FadeIn(note, shift=DOWN * 0.2), run_time=0.3)
        self.wait(max(0.1, d - 5.5))
