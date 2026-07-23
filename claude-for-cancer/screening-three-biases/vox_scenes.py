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


class B04_ThreeBiasTable(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("THREE BIASES THAT MAKE SCREENING LOOK BETTER",font="Georgia",
                   font_size=21,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        def hdr(txt,cx,cy,clr=None):
            bg=Rectangle(width=3.2,height=0.32,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([cx,cy,0])
            t=Text(txt,font="Georgia",font_size=16,color=ManimColor(clr or INK),weight=BOLD).move_to([cx,cy,0])
            return VGroup(bg,t)
        h_bias=hdr("BIAS",-4.2,2.5)
        h_app=hdr("APPARENT BENEFIT",0.0,2.5)
        h_real=hdr("REALITY",4.2,2.5)
        hdiv=Line([-5.5,2.2,0],[5.5,2.2,0],stroke_width=1.5,color=ManimColor(INK))
        headers=VGroup(h_bias,h_app,h_real,hdiv)
        rows_data=[
            (1.3,"LEAD-TIME",
             "Longer 5-year survival\nafter diagnosis",
             "Diagnosed earlier —\nsame death date"),
            (0.1,"LENGTH-TIME",
             "Screened patients do\nbetter on average",
             "Screen catches slow-\ngrowing tumors first"),
            (-1.1,"OVERDIAGNOSIS",
             "More cancers\ndetected",
             "Some tumors would\nnever have harmed"),
        ]
        row_vgs=[]
        for cy,bias,apparent,reality in rows_data:
            b_bg=Rectangle(width=2.6,height=0.7,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.2,cy,0])
            b_t=Text(bias,font="Georgia",font_size=14,color=ManimColor(CRIMSON),weight=BOLD).move_to([-4.2,cy,0])
            a_bg=Rectangle(width=3.0,height=0.7,fill_color=ManimColor(GOLD),fill_opacity=0.7,stroke_width=0,stroke_opacity=0).move_to([0.0,cy,0])
            a_t=Text(apparent,font="Georgia",font_size=12,color=ManimColor(INK)).move_to([0.0,cy,0])
            r_bg=Rectangle(width=3.0,height=0.7,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.2,cy,0])
            r_t=Text(reality,font="Georgia",font_size=12,color=ManimColor(INK)).move_to([4.2,cy,0])
            div=Line([-5.5,cy-0.4,0],[5.5,cy-0.4,0],stroke_width=0.8,color=ManimColor(SLATE))
            arr=Arrow([1.6,cy,0],[2.5,cy,0],stroke_width=1.5,color=ManimColor(INK),buff=0.05,max_tip_length_to_length_ratio=0.3)
            row_vgs.append(VGroup(b_bg,b_t,a_bg,a_t,r_bg,r_t,div,arr))
        sum_bg=Rectangle(width=5.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.2,0])
        sum_t=Text("Survival time from diagnosis ≠ lifespan. Only mortality endpoints settle it.",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([0,-2.2,0])
        footer=Line([-5.5,-2.9,0],[-4.7,-2.9,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(headers))
        self.play(FadeIn(row_vgs[0]))
        self.play(FadeIn(row_vgs[1]))
        self.play(FadeIn(row_vgs[2]))
        self.play(FadeIn(sum_bg),FadeIn(sum_t))
        self.play(FadeIn(footer))
