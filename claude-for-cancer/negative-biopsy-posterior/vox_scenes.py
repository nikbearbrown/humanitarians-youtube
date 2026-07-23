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


class B04_BiopsyBars(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("NEGATIVE BIOPSY != NO CANCER: THE BAYESIAN MATH",font="Georgia",
                   font_size=20,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        BASE_Y=-2.5; SCALE=0.03; BAR_W=1.5
        p_pre=80; p_post=41
        h_pre=p_pre*SCALE; h_post=p_post*SCALE
        x_axis=Line([-4.0,BASE_Y,0],[4.0,BASE_Y,0],stroke_width=2,color=ManimColor(INK))
        bar_pre=Rectangle(width=BAR_W,height=h_pre,fill_color=ManimColor(CRIMSON),fill_opacity=0.85,stroke_width=0,stroke_opacity=0)
        bar_pre.move_to([-1.5,BASE_Y+h_pre/2,0])
        bar_post=Rectangle(width=BAR_W,height=h_post,fill_color=ManimColor(CRIMSON),fill_opacity=0.5,stroke_width=0,stroke_opacity=0)
        bar_post.move_to([1.5,BASE_Y+h_post/2,0])
        lbl_pre_bg=Rectangle(width=1.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-1.5,BASE_Y+h_pre+0.25,0])
        lbl_pre_t=Text("80%",font="Georgia",font_size=18,color=ManimColor(CRIMSON),weight=BOLD).move_to([-1.5,BASE_Y+h_pre+0.25,0])
        lbl_post_bg=Rectangle(width=1.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.5,BASE_Y+h_post+0.25,0])
        lbl_post_t=Text("~41%",font="Georgia",font_size=18,color=ManimColor(CRIMSON),weight=BOLD).move_to([1.5,BASE_Y+h_post+0.25,0])
        xl1_bg=Rectangle(width=1.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-1.5,BASE_Y-0.35,0])
        xl1_t=Text("PRETEST",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([-1.5,BASE_Y-0.35,0])
        xl2_bg=Rectangle(width=2.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.5,BASE_Y-0.35,0])
        xl2_t=Text("AFTER NEGATIVE FNA",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([1.5,BASE_Y-0.35,0])
        y_10=BASE_Y+10*SCALE
        ref_line=Line([-4.0,y_10,0],[4.0,y_10,0],stroke_width=1.5,color=ManimColor(SLATE))
        ref_bg=Rectangle(width=2.2,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.2,y_10+0.3,0])
        ref_t=Text("10% — safe to stop?",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([3.2,y_10+0.3,0])
        math_bg=Rectangle(width=5.5,height=0.52,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,1.8,0])
        math_t=Text("LR- = (1-0.85)/0.99 = 0.152\nPost-test odds = 4 x 0.152 = 0.606 -> prob ~41%",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,1.8,0])
        footer=Line([-4.0,-3.1,0],[-3.2,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis))
        self.play(FadeIn(bar_pre),FadeIn(lbl_pre_bg),FadeIn(lbl_pre_t),FadeIn(xl1_bg),FadeIn(xl1_t))
        self.play(FadeIn(bar_post),FadeIn(lbl_post_bg),FadeIn(lbl_post_t),FadeIn(xl2_bg),FadeIn(xl2_t))
        self.play(FadeIn(ref_line),FadeIn(ref_bg),FadeIn(ref_t))
        self.play(FadeIn(math_bg),FadeIn(math_t))
        self.play(FadeIn(footer))
