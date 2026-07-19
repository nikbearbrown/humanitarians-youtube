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


class B04_DCFHeatmap(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("GORDON GROWTH: THE SENSITIVITY CLIFF",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        D1=4.0
        r_vals=[6,7,8,9,10,11,12]   # columns (x)
        g_vals=[1,2,3,4,5]          # rows (y, g=5 at top)
        CELL_W=1.1; CELL_H=0.52
        # Grid origin: top-left cell center at (-3.85, 2.2)
        def cell_pos(ri, gi):  # ri=r index 0..6, gi=g index 0..4 (gi=4->g=5 at top)
            x=-3.85+ri*CELL_W
            y=2.2-gi*CELL_H
            return [x,y,0]
        def price_color(r_pct,g_pct):
            if g_pct>=r_pct: return ManimColor(CRIMSON),1.0
            P=D1/(r_pct/100-g_pct/100)
            if P>300: return ManimColor(CRIMSON),0.9
            elif P>200: return ManimColor(CRIMSON),0.6
            elif P>130: return ManimColor(GOLD),1.0
            elif P>90:  return ManimColor(SLATE),0.5
            else:       return ManimColor(SLATE),0.25
        # Build grid — fix: check g>=r first before computing P
        low_cells=VGroup(); mid_cells=VGroup(); high_cells=VGroup(); cliff_cells=VGroup()
        for gi,g in enumerate(g_vals):
            for ri,r in enumerate(r_vals):
                cp=cell_pos(ri,gi)
                clr,op=price_color(r,g)
                cell=Rectangle(width=CELL_W-0.06,height=CELL_H-0.06,
                                fill_color=clr,fill_opacity=op,stroke_width=0.5,
                                stroke_color=ManimColor(INK),stroke_opacity=0.3)
                cell.move_to(cp)
                # Price label inside cell
                if g>=r:
                    plbl=Text("---",font="Georgia",font_size=11,color=ManimColor(CREAM)).move_to(cp)
                    grp=VGroup(cell,plbl)
                    cliff_cells.add(grp)
                else:
                    P=D1/(r/100-g/100)
                    plbl=Text(f"${P:.0f}",font="Georgia",font_size=11,color=ManimColor(INK)).move_to(cp)
                    grp=VGroup(cell,plbl)
                    if P>200: cliff_cells.add(grp)
                    elif P>130: high_cells.add(grp)
                    elif P>90: mid_cells.add(grp)
                    else: low_cells.add(grp)
        # Row/column headers
        r_hdrs=VGroup(*[Text(f"r={v}%",font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to(
                            [cell_pos(ri,0)[0],1.55,0]) for ri,v in enumerate(r_vals)])
        g_hdrs=VGroup(*[Text(f"g={v}%",font="Georgia",font_size=12,color=ManimColor(SLATE)).move_to(
                            [-5.2,cell_pos(0,gi)[1],0]) for gi,v in enumerate(g_vals)])
        # Annotation: r=8%,g=4% -> P=$100 (ri=2, gi=3)
        ann_pos=cell_pos(2,3)  # r=8%(ri=2), g=4%(gi=3)
        ann_arr=Arrow([3.5,-1.2,0],ann_pos,stroke_width=1.5,
                       color=ManimColor(INK),buff=0.08,max_tip_length_to_length_ratio=0.25)
        ann_bg=Rectangle(width=2.6,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.5,-1.5,0])
        ann_t=Text("P=$100 @ r=8%,g=4%",font="Georgia",font_size=13,color=ManimColor(INK)).move_to([3.5,-1.5,0])
        cliff_bg=Rectangle(width=2.6,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0.0,-2.0,0])
        cliff_t=Text("CLIFF: g to r means P to inf",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([0.0,-2.0,0])
        footer=Line([-5.2,-2.8,0],[-4.4,-2.8,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(r_hdrs),FadeIn(g_hdrs))    # 1
        self.play(FadeIn(low_cells))                                # 2
        self.play(FadeIn(mid_cells))                                # 3
        self.play(FadeIn(high_cells))                               # 4
        self.play(FadeIn(cliff_cells))                              # 5
        self.play(FadeIn(ann_arr),FadeIn(ann_bg),FadeIn(ann_t))    # 6
        self.play(FadeIn(cliff_bg),FadeIn(cliff_t),FadeIn(footer)) # 7
