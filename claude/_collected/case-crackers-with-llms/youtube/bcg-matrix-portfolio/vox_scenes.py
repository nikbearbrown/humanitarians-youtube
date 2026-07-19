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


class B04_BCGMatrix(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("BCG MATRIX: WHERE IS YOUR PORTFOLIO?",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Canvas: x in [-4.5,4.5]=relative share 0-2.0 (threshold=1.0 at x=0)
        #          y in [-2.5,2.5]=growth 0%-20% (threshold=10% at y=0)
        def pos(share,growth):
            x=-4.5+share/2.0*9.0
            y=-2.5+growth/20.0*5.0
            return [x,y,0]
        # Axes
        x_axis=Line([-4.5,-2.5,0],[4.5,-2.5,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-4.5,-2.5,0],[-4.5,2.5,0],stroke_width=2,color=ManimColor(INK))
        # Quadrant dividers at x=0 (share=1.0) and y=0 (growth=10%)
        div_v=Line([0,-2.5,0],[0,2.5,0],stroke_width=1.5,color=ManimColor(SLATE))
        div_h=Line([-4.5,0,0],[4.5,0,0],stroke_width=1.5,color=ManimColor(SLATE))
        # Axis labels
        xl_bg=Rectangle(width=3.2,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-3.0,0])
        xl=Text("RELATIVE MARKET SHARE →",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([0,-3.0,0])
        yl_bg=Rectangle(width=2.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.0,0.5,0])
        yl=Text("MARKET\nGROWTH →",font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to([-4.0,0.5,0])
        # Share labels
        sl1_bg=Rectangle(width=0.5,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-0.1,-2.85,0])
        sl1=Text("1.0×",font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to([-0.1,-2.85,0])
        # Growth label
        gl1_bg=Rectangle(width=0.8,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-5.1,0.0,0])
        gl1=Text("10%",font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to([-5.1,0.0,0])
        axes_group=VGroup(x_axis,y_axis,div_v,div_h,xl_bg,xl,yl_bg,yl,sl1_bg,sl1,gl1_bg,gl1)
        # Quadrant fill rectangles (subtle background tints)
        q_stars=Rectangle(width=4.5,height=2.5,fill_color=ManimColor(GOLD),fill_opacity=0.15,stroke_width=0,stroke_opacity=0)
        q_stars.move_to([2.25,1.25,0])
        q_cows=Rectangle(width=4.5,height=2.5,fill_color=ManimColor(SLATE),fill_opacity=0.12,stroke_width=0,stroke_opacity=0)
        q_cows.move_to([2.25,-1.25,0])
        q_qm=Rectangle(width=4.5,height=2.5,fill_color=ManimColor(CRIMSON),fill_opacity=0.08,stroke_width=0,stroke_opacity=0)
        q_qm.move_to([-2.25,1.25,0])
        q_dogs=Rectangle(width=4.5,height=2.5,fill_color=ManimColor(SLATE),fill_opacity=0.06,stroke_width=0,stroke_opacity=0)
        q_dogs.move_to([-2.25,-1.25,0])
        quadrant_fills=VGroup(q_stars,q_cows,q_qm,q_dogs)
        # Quadrant label text
        def qlbl(txt,cx,cy,clr):
            bg=Rectangle(width=len(txt)*0.12+0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([cx,cy,0])
            t=Text(txt,font="Georgia",font_size=16,color=ManimColor(clr),weight=BOLD).move_to([cx,cy,0])
            return VGroup(bg,t)
        q_lbls=VGroup(
            qlbl("STARS",         2.3,2.2,GOLD),
            qlbl("CASH COWS",     2.3,-2.2,SLATE),
            qlbl("QUESTION MARKS",-2.0,2.2,CRIMSON),
            qlbl("DOGS",          -2.3,-2.2,SLATE),
        )
        # Business unit dots
        units=[
            ("Enterprise\nSaaS", 1.4,15, GOLD),    # Star: share=1.4, growth=15%
            ("Legacy\nHardware",  1.6, 5, SLATE),   # Cash Cow: share=1.6, growth=5%
            ("IoT\nPlatform",     0.6,18, CRIMSON),  # Question Mark
            ("Print\nMedia",      0.7, 2, "#888888"), # Dog
        ]
        unit_dots=[]
        for name,share,growth,clr in units:
            p=pos(share,growth)
            dot=Dot(p,radius=0.18,color=ManimColor(clr))
            lbl_bg=Rectangle(width=1.1,height=0.44,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([p[0]+0.85,p[1],0])
            lbl_t=Text(name,font="Georgia",font_size=12,color=ManimColor(INK)).move_to([p[0]+0.85,p[1],0])
            unit_dots.append(VGroup(dot,lbl_bg,lbl_t))
        # Strategy annotations for each unit
        strat_data=[
            ("INVEST",   pos(1.4,15), GOLD),
            ("MILK",     pos(1.6, 5), SLATE),
            ("PROBE",    pos(0.6,18), CRIMSON),
            ("HARVEST",  pos(0.7, 2), "#888888"),
        ]
        strats=VGroup(*[
            VGroup(
                Rectangle(width=1.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([p[0]+0.85,p[1]-0.3,0]),
                Text(s,font="Georgia",font_size=11,color=ManimColor(c),weight=BOLD).move_to([p[0]+0.85,p[1]-0.3,0])
            ) for s,p,c in strat_data
        ])
        footer=Line([-4.5,-3.2,0],[-3.7,-3.2,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(axes_group))                        # 1
        self.play(FadeIn(quadrant_fills))                                   # 2
        self.play(FadeIn(q_lbls))                                           # 3
        self.play(*[FadeIn(u) for u in unit_dots])                         # 4
        self.play(FadeIn(strats))                                           # 5
        self.play(FadeIn(footer))                                           # 6
