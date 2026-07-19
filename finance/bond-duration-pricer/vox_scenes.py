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


class B04_BondTimeline(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("BOND DURATION: WHY 'SAFE' BONDS DROP",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # --- TOP: Timeline ---
        tl=Line([-5.0,0.8,0],[4.8,0.8,0],stroke_width=2,color=ManimColor(INK))
        today_bg=Rectangle(width=0.9,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-5.0,0.45,0])
        today_t=Text("TODAY",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([-5.0,0.45,0])
        mat_bg=Rectangle(width=0.8,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.8,0.45,0])
        mat_t=Text("2049",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([4.8,0.45,0])
        # Coupon arrows (upward from timeline) at regular x positions
        coup_xs=[-4.2,-3.2,-2.2,-1.2,-0.2,0.8,1.8,2.8]
        coups=VGroup(*[Arrow([cx,0.8,0],[cx,1.8,0],stroke_width=1.5,color=ManimColor(SLATE),
                              buff=0.0,max_tip_length_to_length_ratio=0.2)
                       for cx in coup_xs])
        coup_bg=Rectangle(width=2.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-1.0,2.15,0])
        coup_lbl=Text("$14.75 coupon/yr",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([-1.0,2.15,0])
        # Face value arrow (large, at maturity)
        fv_arr=Arrow([4.5,0.8,0],[4.5,2.8,0],stroke_width=3,color=ManimColor(INK),
                      buff=0.0,max_tip_length_to_length_ratio=0.12)
        fv_bg=Rectangle(width=0.9,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.5,3.0,0])
        fv_t=Text("$1,000",font="Georgia",font_size=13,color=ManimColor(INK)).move_to([4.5,3.0,0])
        # --- BOTTOM: Price bar comparison ---
        # Price at YTM=5%: $707; at YTM=6%: $625
        BASE_P=-3.0; PSCALE=0.003
        p5_h=707*PSCALE; p6_h=625*PSCALE
        bar5=Rectangle(width=0.9,height=p5_h,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0)
        bar5.move_to([-3.5,BASE_P+p5_h/2,0])
        bar6=Rectangle(width=0.9,height=p6_h,fill_color=ManimColor(CRIMSON),fill_opacity=0.8,stroke_width=0,stroke_opacity=0)
        bar6.move_to([-2.4,BASE_P+p6_h/2,0])
        b5bg=Rectangle(width=1.0,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.5,BASE_P+p5_h+0.4,0])
        b5t=Text("$707\nYTM=5%",font="Georgia",font_size=13,color=ManimColor(INK)).move_to([-3.5,BASE_P+p5_h+0.4,0])
        b6bg=Rectangle(width=1.0,height=0.5,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-2.4,BASE_P+p6_h+0.4,0])
        b6t=Text("$625\nYTM=6%",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([-2.4,BASE_P+p6_h+0.4,0])
        # Duration annotation
        dur_bg=Rectangle(width=4.0,height=0.52,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.5,-2.3,0])
        dur_t=Text("Modified Duration: 16 yrs\n1pp rise = -11.7% price",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([1.5,-2.3,0])
        footer=Line([-5.0,-3.3,0],[-4.2,-3.3,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(tl),FadeIn(today_bg),FadeIn(today_t),FadeIn(mat_bg),FadeIn(mat_t))  # 1
        self.play(FadeIn(coups),FadeIn(coup_bg),FadeIn(coup_lbl))                                          # 2
        self.play(FadeIn(fv_arr),FadeIn(fv_bg),FadeIn(fv_t))                                              # 3
        self.play(FadeIn(bar5),FadeIn(b5bg),FadeIn(b5t))                                                  # 4
        self.play(FadeIn(bar6),FadeIn(b6bg),FadeIn(b6t))                                                  # 5
        self.play(FadeIn(dur_bg),FadeIn(dur_t))                                                            # 6
        self.play(FadeIn(footer))                                                                           # 7
