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


class B04_TumorTrajectories(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("TUMOR RESPONSE: EGFR vs KRAS G12C vs NON-RESPONSE",font="Georgia",
                   font_size=19,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        def pt(weeks,burden):
            x=-5.0+weeks/60*9.5
            y=-2.5+(burden/200)*5.0
            return [x,y,0]
        x_axis=Line([-5.2,-2.5,0],[4.8,-2.5,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-5.2,-2.5,0],[-5.2,2.5,0],stroke_width=2,color=ManimColor(INK))
        baseline=Line([-5.0,-2.5+100/200*5.0,0],[4.5,-2.5+100/200*5.0,0],
                       stroke_width=1,color=ManimColor(SLATE))
        xl_bg=Rectangle(width=1.5,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-3.1,0])
        xl=Text("TIME (weeks)",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([0,-3.1,0])
        yl_bg=Rectangle(width=1.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.5,0.5,0])
        yl=Text("TUMOR BURDEN",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([-4.5,0.5,0])
        egfr_pts=[pt(0,100),pt(8,70),pt(16,40),pt(24,20),pt(40,15),pt(60,10)]
        egfr_segs=VGroup(*[Line(egfr_pts[i],egfr_pts[i+1],stroke_width=3,color=ManimColor(GOLD))
                            for i in range(len(egfr_pts)-1)])
        egfr_bg=Rectangle(width=2.0,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,pt(60,10)[1]+0.35,0])
        egfr_t=Text("EGFR (osimertinib)\n>60% ORR, durable",font="Georgia",font_size=13,color=ManimColor(GOLD)).move_to([3.0,pt(60,10)[1]+0.35,0])
        kras_pts=[pt(0,100),pt(8,75),pt(16,55),pt(24,50),pt(32,60),pt(44,90),pt(60,140)]
        kras_segs=VGroup(*[Line(kras_pts[i],kras_pts[i+1],stroke_width=3,color=ManimColor(SLATE))
                            for i in range(len(kras_pts)-1)])
        kras_bg=Rectangle(width=2.2,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.5,-1.5,0])
        kras_t=Text("KRAS G12C (sotorasib)\n35-40% ORR, transient",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([2.5,-1.5,0])
        nr_pts=[pt(0,100),pt(8,105),pt(16,110),pt(24,120),pt(40,140),pt(60,160)]
        nr_segs=VGroup(*[Line(nr_pts[i],nr_pts[i+1],stroke_width=3,color=ManimColor(CRIMSON))
                          for i in range(len(nr_pts)-1)])
        nr_bg=Rectangle(width=1.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,pt(60,160)[1]+0.22,0])
        nr_t=Text("Non-responder",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([3.0,pt(60,160)[1]+0.22,0])
        footer=Line([-5.2,-3.1,0],[-4.4,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis),FadeIn(y_axis),FadeIn(baseline),FadeIn(xl_bg),FadeIn(xl),FadeIn(yl_bg),FadeIn(yl))
        self.play(FadeIn(egfr_segs),FadeIn(egfr_bg),FadeIn(egfr_t))
        self.play(FadeIn(kras_segs),FadeIn(kras_bg),FadeIn(kras_t))
        self.play(FadeIn(nr_segs),FadeIn(nr_bg),FadeIn(nr_t))
        self.play(FadeIn(footer))
