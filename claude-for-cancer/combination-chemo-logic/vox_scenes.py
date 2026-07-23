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


class B04_ChemoMatrix(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("R-CHOP: DIFFERENT MECHANISMS, NON-OVERLAPPING TOXICITIES",font="Georgia",
                   font_size=18,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        drugs=[
            ("R  Rituximab",    "Anti-CD20 mAb",           "Infusion reaction",       SLATE),
            ("C  Cyclophos.",   "Alkylating agent",         "Myelosuppression (dose)",  CRIMSON),
            ("H  Doxorubicin",  "Topoisomerase II inhibit.","Cardiotoxicity (cumul.)",  "#C85010"),
            ("O  Vincristine",  "Microtubule inhibitor",    "Peripheral neuropathy",    SLATE),
            ("P  Prednisone",   "Glucocorticoid",           "Hyperglycemia / immune",   "#8A6A00"),
        ]
        CELL_H=0.55; ROW_GAP=0.62
        h_drug_bg=Rectangle(width=2.5,height=0.35,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.8,2.3,0])
        h_drug_t=Text("DRUG",font="Georgia",font_size=14,color=ManimColor(INK),weight=BOLD).move_to([-3.8,2.3,0])
        h_mech_bg=Rectangle(width=2.8,height=0.35,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0.0,2.3,0])
        h_mech_t=Text("MECHANISM",font="Georgia",font_size=14,color=ManimColor(INK),weight=BOLD).move_to([0.0,2.3,0])
        h_tox_bg=Rectangle(width=3.0,height=0.35,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.0,2.3,0])
        h_tox_t=Text("DOSE-LIMITING TOXICITY",font="Georgia",font_size=14,color=ManimColor(INK),weight=BOLD).move_to([4.0,2.3,0])
        hdiv=Line([-5.5,1.9,0],[5.5,1.9,0],stroke_width=1.5,color=ManimColor(INK))
        headers=VGroup(h_drug_bg,h_drug_t,h_mech_bg,h_mech_t,h_tox_bg,h_tox_t,hdiv)
        row_vgs=[]
        for i,(drug,mech,tox,tox_clr) in enumerate(drugs):
            cy=1.5-i*ROW_GAP
            d_bg=Rectangle(width=2.5,height=CELL_H,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.8,cy,0])
            d_t=Text(drug,font="Georgia",font_size=13,color=ManimColor(INK)).move_to([-3.8,cy,0])
            m_bg=Rectangle(width=2.8,height=CELL_H,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0.0,cy,0])
            m_t=Text(mech,font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([0.0,cy,0])
            t_bg=Rectangle(width=3.0,height=CELL_H,fill_color=ManimColor(tox_clr),fill_opacity=0.25,stroke_width=0,stroke_opacity=0).move_to([4.0,cy,0])
            t_t=Text(tox,font="Georgia",font_size=13,color=ManimColor(INK)).move_to([4.0,cy,0])
            div=Line([-5.5,cy-CELL_H/2,0],[5.5,cy-CELL_H/2,0],stroke_width=0.5,color=ManimColor(SLATE))
            row_vgs.append(VGroup(d_bg,d_t,m_bg,m_t,t_bg,t_t,div))
        ann_bg=Rectangle(width=5.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.0,0])
        ann_t=Text("No two drugs share the same dose-limiting toxicity — the design rule",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([0,-2.0,0])
        footer=Line([-5.5,-2.7,0],[-4.7,-2.7,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(headers))
        self.play(FadeIn(row_vgs[0]),FadeIn(row_vgs[1]))
        self.play(FadeIn(row_vgs[2]),FadeIn(row_vgs[3]))
        self.play(FadeIn(row_vgs[4]))
        self.play(FadeIn(ann_bg),FadeIn(ann_t))
        self.play(FadeIn(footer))
