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


class B04_PPVGrid(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"
        title=Text("PPV DEPENDS ON PREVALENCE, NOT JUST SPECIFICITY",font="Georgia",
                   font_size=20,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        BASE_Y=-2.5; SCALE=0.03; BAR_W=1.2
        scenarios=[(-3.0,31,"0.5%\nprevalence","PPV = 31%"),
                   (0.0, 65,"2%\nprevalence", "PPV = 65%"),
                   (3.0, 91,"10%\nprevalence","PPV = 91%")]
        x_axis=Line([-4.5,BASE_Y,0],[4.5,BASE_Y,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-4.5,BASE_Y,0],[-4.5,1.5,0],stroke_width=2,color=ManimColor(INK))
        yl_bg=Rectangle(width=0.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.0,0.0,0])
        yl_t=Text("PPV %",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([-4.0,0.0,0])
        bar_vgs=[]
        for bx,ppv_val,prev_txt,ppv_txt in scenarios:
            h=ppv_val*SCALE
            clr=CRIMSON if ppv_val<50 else (SLATE if ppv_val<80 else PASS_CLR)
            bar=Rectangle(width=BAR_W,height=h,fill_color=ManimColor(clr),
                          fill_opacity=0.8,stroke_width=0,stroke_opacity=0)
            bar.move_to([bx,BASE_Y+h/2,0])
            prev_bg=Rectangle(width=1.5,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([bx,BASE_Y-0.45,0])
            prev_t=Text(prev_txt,font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([bx,BASE_Y-0.45,0])
            ppv_bg=Rectangle(width=1.2,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([bx,BASE_Y+h+0.22,0])
            ppv_t=Text(ppv_txt,font="Georgia",font_size=15,color=ManimColor(clr),weight=BOLD).move_to([bx,BASE_Y+h+0.22,0])
            bar_vgs.append(VGroup(bar,prev_bg,prev_t,ppv_bg,ppv_t))
        fp_data=[("FP: 995\nTP: 450",-3.0),("FP: 980\nTP: 1800",0.0),("FP: 900\nTP: 9000",3.0)]
        fp_vgs=VGroup(*[
            VGroup(
                Rectangle(width=1.4,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([fx,-1.6,0]),
                Text(ft,font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to([fx,-1.6,0])
            ) for ft,fx in fp_data
        ])
        ins_bg=Rectangle(width=5.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,2.5,0])
        ins_t=Text("Same test (99% specific) — prevalence changes everything",font="Georgia",font_size=15,color=ManimColor(INK)).move_to([0,2.5,0])
        footer=Line([-4.5,-3.1,0],[-3.7,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis),FadeIn(y_axis),FadeIn(yl_bg),FadeIn(yl_t))
        self.play(FadeIn(bar_vgs[0]))
        self.play(FadeIn(bar_vgs[1]))
        self.play(FadeIn(bar_vgs[2]))
        self.play(FadeIn(fp_vgs))
        self.play(FadeIn(ins_bg),FadeIn(ins_t))
        self.play(FadeIn(footer))
