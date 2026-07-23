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


class B04_TheranosticLoop(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("PSMA THERANOSTICS: IMAGE-THEN-TREAT",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # 4 boxes in a row at y=0.8, then return arrow below
        BOX_W=2.0; BOX_H=0.7
        boxes_data=[
            (-4.3,0.8,"Ga-68 PSMA\nPET IMAGING",SLATE),
            (-1.4,0.8,"SELECT\nELIGIBLE",SLATE),
            ( 1.4,0.8,"Lu-177\nTHERAPY",CRIMSON),
            ( 4.3,0.8,"ASSESS\nRESPONSE",SLATE),
        ]
        box_vgs=[]
        for bx,by,btxt,bclr in boxes_data:
            rect=Rectangle(width=BOX_W,height=BOX_H,fill_color=ManimColor(bclr),
                            fill_opacity=0.5,stroke_width=1.5,stroke_color=ManimColor(INK),stroke_opacity=1.0)
            rect.move_to([bx,by,0])
            t=Text(btxt,font="Georgia",font_size=14,color=ManimColor(CREAM if bclr==CRIMSON else INK)).move_to([bx,by,0])
            box_vgs.append(VGroup(rect,t))
        # Arrows between boxes (left to right)
        arrows_lr=VGroup(*[
            Arrow([boxes_data[i][0]+BOX_W/2,0.8,0],[boxes_data[i+1][0]-BOX_W/2,0.8,0],
                   stroke_width=2,color=ManimColor(INK),buff=0.05,max_tip_length_to_length_ratio=0.25)
            for i in range(3)
        ])
        # Return arrow (below the boxes): from rightmost box bottom to leftmost box bottom
        ret_line1=Line([4.3,0.8-BOX_H/2,0],[4.3,-0.5,0],stroke_width=2,color=ManimColor(GOLD))
        ret_line2=Line([4.3,-0.5,0],[-4.3,-0.5,0],stroke_width=2,color=ManimColor(GOLD))
        ret_arr=Arrow([-4.3,-0.5,0],[-4.3,0.8-BOX_H/2,0],stroke_width=2,color=ManimColor(GOLD),
                       buff=0.05,max_tip_length_to_length_ratio=0.2)
        ret_bg=Rectangle(width=2.0,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-0.82,0])
        ret_t=Text("or escalate to Ac-225",font="Georgia",font_size=13,color=ManimColor(GOLD)).move_to([0,-0.82,0])
        return_loop=VGroup(ret_line1,ret_line2,ret_arr,ret_bg,ret_t)
        # VISION trial result
        vis_bg=Rectangle(width=5.0,height=0.52,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.0,0])
        vis_t=Text("VISION trial (NEJM 2021): Lu-177-PSMA-617\nimproves OS in PSMA-positive mCRPC",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,-2.0,0])
        # Alpha vs beta callout
        ab_bg=Rectangle(width=5.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.7,0])
        ab_t=Text("Ac-225 (alpha): 50 µm range, high LET  |  Lu-177 (beta): 1-2 mm range",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([0,-2.7,0])
        footer=Line([-5.0,-3.2,0],[-4.2,-3.2,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title))                                                           # 1
        self.play(FadeIn(VGroup(*box_vgs)))                                                # 2
        self.play(FadeIn(arrows_lr))                                                       # 3
        self.play(FadeIn(return_loop))                                                     # 4
        self.play(FadeIn(vis_bg),FadeIn(vis_t))                                           # 5
        self.play(FadeIn(ab_bg),FadeIn(ab_t))                                             # 6
        self.play(FadeIn(footer))                                                          # 7
