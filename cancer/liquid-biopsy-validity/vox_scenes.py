import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_ValidityFunnel(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"
        title=Text("THREE-VALIDITY FRAMEWORK: LIQUID BIOPSY",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        gates=["ANALYTIC\nVALIDITY","CLINICAL\nVALIDITY","CLINICAL\nUTILITY"]
        gate_xs=[-3.0,0.0,3.0]
        gate_hdrs=VGroup(*[
            VGroup(
                Rectangle(width=2.2,height=0.7,fill_color=ManimColor(SLATE),fill_opacity=0.3,stroke_width=0,stroke_opacity=0).move_to([gx,2.2,0]),
                Text(gt,font="Georgia",font_size=14,color=ManimColor(INK),weight=BOLD).move_to([gx,2.2,0])
            ) for gx,gt in zip(gate_xs,gates)
        ])
        tests=["EGFR T790M\n(osimertinib)","DYNAMIC MRD\n(stage II CRC)","MCED\n(asymptomatic)"]
        test_ys=[0.8,-0.4,-1.6]
        test_lbls=VGroup(*[
            VGroup(
                Rectangle(width=2.4,height=0.7,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-5.0,ty,0]),
                Text(tt,font="Georgia",font_size=13,color=ManimColor(INK)).move_to([-5.0,ty,0])
            ) for tt,ty in zip(tests,test_ys)
        ])
        results=[
            [True,True,True],
            [True,True,True],
            [True,True,False],
        ]
        g1_marks=VGroup(*[
            VGroup(
                Rectangle(width=0.5,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([gate_xs[0],test_ys[i],0]),
                Text("V" if results[i][0] else "X",font="Georgia",font_size=24,
                     color=ManimColor(PASS_CLR if results[i][0] else CRIMSON),weight=BOLD).move_to([gate_xs[0],test_ys[i],0])
            ) for i in range(3)
        ])
        g2_marks=VGroup(*[
            VGroup(
                Rectangle(width=0.5,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([gate_xs[1],test_ys[i],0]),
                Text("V" if results[i][1] else "X",font="Georgia",font_size=24,
                     color=ManimColor(PASS_CLR if results[i][1] else CRIMSON),weight=BOLD).move_to([gate_xs[1],test_ys[i],0])
            ) for i in range(3)
        ])
        g3_marks=VGroup(*[
            VGroup(
                Rectangle(width=0.5,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([gate_xs[2],test_ys[i],0]),
                Text("V" if results[i][2] else "X",font="Georgia",font_size=24,
                     color=ManimColor(PASS_CLR if results[i][2] else CRIMSON),weight=BOLD).move_to([gate_xs[2],test_ys[i],0])
            ) for i in range(3)
        ])
        mced_bg=Rectangle(width=4.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.0,-2.5,0])
        mced_t=Text("MCED: detection improved — mortality endpoint pending",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([1.0,-2.5,0])
        footer=Line([-5.5,-3.1,0],[-4.7,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(gate_hdrs),FadeIn(test_lbls))
        self.play(FadeIn(g1_marks))
        self.play(FadeIn(g2_marks))
        self.play(FadeIn(g3_marks))
        self.play(FadeIn(mced_bg),FadeIn(mced_t))
        self.play(FadeIn(footer))
