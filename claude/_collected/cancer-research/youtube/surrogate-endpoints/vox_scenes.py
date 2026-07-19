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


class B04_EndpointHierarchy(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"
        title=Text("SURROGATE vs HARD ENDPOINTS: THE TRANSLATION GAP",font="Georgia",
                   font_size=20,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        BOX_W=4.5; BOX_H=0.65
        os_box=Rectangle(width=BOX_W,height=BOX_H,fill_color=ManimColor(GOLD),fill_opacity=0.9,stroke_width=0,stroke_opacity=0)
        os_box.move_to([0,2.0,0])
        os_t=Text("OVERALL SURVIVAL (OS) — HARD ENDPOINT",font="Georgia",font_size=15,color=ManimColor(INK),weight=BOLD).move_to([0,2.0,0])
        pfs_box=Rectangle(width=BOX_W,height=BOX_H,fill_color=ManimColor(SLATE),fill_opacity=0.4,stroke_width=0,stroke_opacity=0)
        pfs_box.move_to([0,0.8,0])
        pfs_t=Text("PROGRESSION-FREE SURVIVAL (PFS) — SURROGATE",font="Georgia",font_size=15,color=ManimColor(INK)).move_to([0,0.8,0])
        orr_box=Rectangle(width=BOX_W,height=BOX_H,fill_color=ManimColor(SLATE),fill_opacity=0.2,stroke_width=0,stroke_opacity=0)
        orr_box.move_to([0,-0.4,0])
        orr_t=Text("OBJECTIVE RESPONSE RATE (ORR) — SURROGATE",font="Georgia",font_size=15,color=ManimColor(INK)).move_to([0,-0.4,0])
        arr_pass=Arrow([-3.5,1.15,0],[-3.5,1.65,0],stroke_width=2,color=ManimColor(PASS_CLR),buff=0.0,max_tip_length_to_length_ratio=0.3)
        pass_bg=Rectangle(width=1.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.5,1.4,0])
        pass_t=Text("translates",font="Georgia",font_size=13,color=ManimColor(PASS_CLR)).move_to([-4.5,1.4,0])
        arr_fail=Arrow([3.5,1.15,0],[3.5,1.65,0],stroke_width=2,color=ManimColor(CRIMSON),buff=0.0,max_tip_length_to_length_ratio=0.3)
        fail_bg=Rectangle(width=2.2,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.5,1.4,0])
        fail_t=Text("does not translate",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([4.5,1.4,0])
        translation=VGroup(arr_pass,pass_bg,pass_t,arr_fail,fail_bg,fail_t)
        ex_bg=Rectangle(width=5.5,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-1.5,0])
        ex_t=Text("Example: Bevacizumab (early breast cancer)\nPFS improved — OS unchanged (p=0.41)",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([0,-1.5,0])
        row1_bg=Rectangle(width=5.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.3,0])
        row1_t=Text("ORR 60% vs 20% (p<0.001)  ·  PFS +3 months (p=0.01)  ·  OS: same (p=0.41)",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([0,-2.3,0])
        footer=Line([-5.5,-3.0,0],[-4.7,-3.0,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title))
        self.play(FadeIn(os_box),FadeIn(os_t))
        self.play(FadeIn(pfs_box),FadeIn(pfs_t))
        self.play(FadeIn(orr_box),FadeIn(orr_t))
        self.play(FadeIn(translation))
        self.play(FadeIn(ex_bg),FadeIn(ex_t),FadeIn(row1_bg),FadeIn(row1_t))
        self.play(FadeIn(footer))
