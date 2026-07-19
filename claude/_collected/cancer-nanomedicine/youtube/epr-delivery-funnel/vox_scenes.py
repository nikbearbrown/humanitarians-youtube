import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_DeliveryFunnel(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("EPR EFFECT: 0.7% ACTUALLY DELIVERED",font="Georgia",
                   font_size=24,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # 5 funnel stages (visual, not to scale)
        stages=[
            ("INJECTED DOSE",     "100%",        5.6, 2.0,  SLATE,  0.5),
            ("BLOOD CIRCULATION", "~60% remain", 4.2, 1.1,  SLATE,  0.45),
            ("TUMOR VASCULATURE", "~10% reach",  2.8, 0.2,  SLATE,  0.4),
            ("INTERSTITIAL SPACE","~3% via EPR", 1.5,-0.7,  SLATE,  0.35),
            ("CELLULAR UPTAKE",   "0.7% MEDIAN", 0.65,-1.6, CRIMSON,0.9),
        ]
        BOX_H=0.45
        boxes=[]; stage_labels=[]; pct_labels=[]; connectors=[]
        for label,pct,width,cy,clr,op in stages:
            box=Rectangle(width=width,height=BOX_H,fill_color=ManimColor(clr),
                          fill_opacity=op,stroke_width=0,stroke_opacity=0)
            box.move_to([0,cy,0])
            boxes.append(box)
            lbl_bg=Rectangle(width=len(label)*0.11+0.3,height=0.28,fill_color=ManimColor(CREAM),
                              fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-0.5,cy,0])
            lbl_t=Text(label,font="Georgia",font_size=14,color=ManimColor(INK)).move_to([-0.5,cy,0])
            stage_labels.append(VGroup(lbl_bg,lbl_t))
            pct_bg=Rectangle(width=1.4,height=0.28,fill_color=ManimColor(CREAM),
                              fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.5,cy,0])
            pct_t=Text(pct,font="Georgia",font_size=14,
                       color=ManimColor(CRIMSON if clr==CRIMSON else INK)).move_to([3.5,cy,0])
            pct_labels.append(VGroup(pct_bg,pct_t))
        # Connectors between stages (tapered lines on sides)
        for i in range(len(stages)-1):
            w1=stages[i][2]/2; w2=stages[i+1][2]/2
            y1=stages[i][3]-BOX_H/2; y2=stages[i+1][3]+BOX_H/2
            l_conn=Line([-w1,y1,0],[-w2,y2,0],stroke_width=1.5,color=ManimColor(SLATE))
            r_conn=Line([ w1,y1,0],[ w2,y2,0],stroke_width=1.5,color=ManimColor(SLATE))
            connectors.append(VGroup(l_conn,r_conn))
        # 0.7% annotation arrow
        ann_arr=Arrow([2.5,-1.6,0],[0.5,-1.6,0],stroke_width=2,color=ManimColor(CRIMSON),
                       buff=0.05,max_tip_length_to_length_ratio=0.25)
        ann_bg=Rectangle(width=3.2,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.5,-1.95,0])
        ann_t=Text("Wilhelm 2016 meta-analysis (117 studies)",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([3.5,-1.95,0])
        footer=Line([-5.0,-3.0,0],[-4.2,-3.0,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title))                                                           # 1
        self.play(FadeIn(boxes[0]),FadeIn(stage_labels[0]),FadeIn(pct_labels[0]))         # 2
        self.play(FadeIn(connectors[0]),FadeIn(boxes[1]),FadeIn(stage_labels[1]),FadeIn(pct_labels[1]),
                  FadeIn(connectors[1]),FadeIn(boxes[2]),FadeIn(stage_labels[2]),FadeIn(pct_labels[2]))  # 3
        self.play(FadeIn(connectors[2]),FadeIn(boxes[3]),FadeIn(stage_labels[3]),FadeIn(pct_labels[3]))  # 4
        self.play(FadeIn(connectors[3]),FadeIn(boxes[4]),FadeIn(stage_labels[4]),FadeIn(pct_labels[4]))  # 5
        self.play(FadeIn(ann_arr),FadeIn(ann_bg),FadeIn(ann_t))                           # 6
        self.play(FadeIn(footer))                                                           # 7
