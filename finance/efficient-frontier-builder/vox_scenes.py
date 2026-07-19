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


class B04_EfficientFrontier(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("EFFICIENT FRONTIER: WHERE VGLT GETS ZERO",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Map vol%∈[5,30]→x∈[-4.5,4.5], return%∈[3,18]→y∈[-2.5,2.5]
        def pnt(vol,ret):
            x=-4.5+(vol-5)/25*9.0
            y=-2.5+(ret-3)/15*5.0
            return [x,y,0]
        # Axes
        x_axis=Line([-4.8,-2.8,0],[5.0,-2.8,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-4.8,-2.8,0],[-4.8,2.8,0],stroke_width=2,color=ManimColor(INK))
        xl_bg=Rectangle(width=3.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0.0,-3.2,0])
        xl=Text("VOLATILITY (annualized)",font="Georgia",font_size=16,color=ManimColor(SLATE)).move_to([0.0,-3.2,0])
        yl_bg=Rectangle(width=2.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.0,0.0,0])
        yl=Text("RETURN",font="Georgia",font_size=15,color=ManimColor(SLATE)).move_to([-4.0,0.0,0])
        # Frontier pts (convex curve, min-var at vol=10%,ret=6%; tangency at 14%,10%)
        fp=[(10,6),(11,7.0),(12,8.0),(13,9.0),(14,10.0),(16,11.5),(18,12.5),(20,13.5),(23,14.5),(26,15.5),(29,16.0)]
        segs=VGroup(*[Line(pnt(*fp[i]),pnt(*fp[i+1]),stroke_width=3,color=ManimColor(INK))
                      for i in range(len(fp)-1)])
        # Asset dots
        assets=[("VTI",(16,9.5)),("VB",(21,10.5)),("VEA",(18,8.0)),("BND",(7,4.5)),("VGLT",(12,5.0))]
        adots=VGroup(*[Dot(pnt(*p),radius=0.12,color=ManimColor(SLATE)) for _,p in assets])
        def albl(name,pos,dx,dy):
            bg=Rectangle(width=len(name)*0.12+0.2,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([pnt(*pos)[0]+dx,pnt(*pos)[1]+dy,0])
            t=Text(name,font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([pnt(*pos)[0]+dx,pnt(*pos)[1]+dy,0])
            return VGroup(bg,t)
        albls=VGroup(albl("VTI",(16,9.5),0.4,0.25),albl("VB",(21,10.5),0.35,0.25),
                     albl("VEA",(18,8.0),0.4,-0.25),albl("BND",(7,4.5),0.4,0.25),
                     albl("VGLT",(12,5.0),0.55,-0.28))
        # Tangency dot (14%,10%)
        tp=pnt(14,10)
        tan_dot=Dot(tp,radius=0.18,color=ManimColor(CRIMSON))
        tan_bg=Rectangle(width=2.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([tp[0]+1.3,tp[1]+0.35,0])
        tan_lbl=Text("MAX SHARPE",font="Georgia",font_size=15,color=ManimColor(CRIMSON)).move_to([tp[0]+1.3,tp[1]+0.35,0])
        # VGLT "dominated" callout
        vp=pnt(12,5.0)
        vg_bg=Rectangle(width=2.2,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([vp[0]+1.8,vp[1]-0.5,0])
        vg_lbl=Text("0% weight\non frontier",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([vp[0]+1.8,vp[1]-0.5,0])
        vg_arr=Arrow([vp[0]+0.7,vp[1]-0.3,0],vp,stroke_width=1.5,color=ManimColor(CRIMSON),buff=0.1,max_tip_length_to_length_ratio=0.25)
        vglt_ann=VGroup(vg_bg,vg_lbl,vg_arr)
        footer=Line([-4.8,-3.3,0],[-4.0,-3.3,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis),FadeIn(y_axis),FadeIn(xl_bg),FadeIn(xl),FadeIn(yl_bg),FadeIn(yl))  # 1
        self.play(FadeIn(segs))                                                            # 2
        self.play(FadeIn(adots),FadeIn(albls))                                             # 3
        self.play(FadeIn(tan_dot),FadeIn(tan_bg),FadeIn(tan_lbl))                         # 4
        self.play(FadeIn(vglt_ann))                                                        # 5
        self.play(FadeIn(footer))                                                          # 6
