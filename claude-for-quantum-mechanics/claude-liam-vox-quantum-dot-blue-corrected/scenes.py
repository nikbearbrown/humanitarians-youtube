import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
    _bs=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(scene,beat,used=1): scene.wait(max(.1,DUR.get(beat,10)-used))
def heading(text): return Text(text,font=DISPLAY,font_size=29,color=INK).to_edge(UP)

class B02_SameMaterialDifferentSize(Scene):
    def construct(self):
        big=VGroup(Circle(radius=1.6,color=TEAL,fill_opacity=.15),Text("R = 3 nm",font=MONO,font_size=27,color=INK)).arrange(DOWN,buff=.35).move_to(LEFT*3)
        small=VGroup(Circle(radius=1.05,color=CRIMSON,fill_opacity=.2),Text("R = 2 nm",font=MONO,font_size=27,color=INK)).arrange(DOWN,buff=.35).move_to(RIGHT*3)
        same=Text("same semiconductor • different boundary",font=SERIF,font_size=28,color=INK).shift(DOWN*2.7)
        self.play(FadeIn(heading("CHEMISTRY SETS THE BULK GAP; SIZE ADDS A SCALE")),FadeIn(big),FadeIn(small),FadeIn(same),run_time=1.1); hold(self,"B02",1.1)

class B03_WavelengthCost(Scene):
    def construct(self):
        left=RoundedRectangle(width=5,height=2.8,corner_radius=.2,color=TEAL).move_to(LEFT*3); right=RoundedRectangle(width=3.1,height=2.8,corner_radius=.2,color=CRIMSON).move_to(RIGHT*3)
        w1=VMobject(color=TEAL,stroke_width=4).set_points_smoothly([np.array([-5.2+x, .55*np.sin(np.pi*x/4.4),0]) for x in np.linspace(0,4.4,70)])
        w2=VMobject(color=CRIMSON,stroke_width=4).set_points_smoothly([np.array([1.65+x, .55*np.sin(2*np.pi*x/2.7),0]) for x in np.linspace(0,2.7,70)])
        eq=Text("R ↓  ⇒  k ~ 1/R ↑  ⇒  E_kin ~ 1/R² ↑",font=MONO,font_size=31,color=INK).shift(DOWN*2.45)
        self.play(FadeIn(heading("SQUEEZE THE WAVE → PAY KINETIC ENERGY")),Create(left),Create(right),Create(w1),Create(w2),FadeIn(eq),run_time=1.3); hold(self,"B03",1.3)

class B04_TwoCarriers(Scene):
    def construct(self):
        dot=Circle(radius=2.1,color=INK); e=Dot(LEFT*.9+UP*.5,radius=.22,color=TEAL); h=Dot(RIGHT*.9+DOWN*.5,radius=.22,color=CRIMSON); labs=VGroup(Text("electron  m_e*",font=MONO,font_size=26,color=TEAL).next_to(e,UP),Text("hole  m_h*",font=MONO,font_size=26,color=CRIMSON).next_to(h,DOWN)); plus=Text("both add confinement energy",font=SERIF,font_size=29,color=INK).shift(DOWN*2.65)
        self.play(FadeIn(heading("AN OPTICAL EXCITATION CONFINES TWO CARRIERS")),Create(dot),FadeIn(e),FadeIn(h),FadeIn(labs),FadeIn(plus),run_time=1.2); hold(self,"B04",1.2)

class B05_LeadingModel(Scene):
    def construct(self):
        lines=VGroup(Text("E_opt(R)  ≈  E_bulk",font=MONO,font_size=37,color=INK),Text("+  A/R² · (1/m_e* + 1/m_h*)",font=MONO,font_size=36,color=TEAL),Text("leading confinement model",font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.65)
        self.play(FadeIn(heading("THE BOX-MODEL SPINE")),LaggedStart(*[FadeIn(x) for x in lines],lag_ratio=.16),run_time=1.3); hold(self,"B05",1.3)

class B06_LevelSpread(Scene):
    def construct(self):
        def levels(x,gap,color):
            return VGroup(*[Line(LEFT*.9,RIGHT*.9,color=color).shift(UP*(gap/2+i*.32) if i<2 else DOWN*(gap/2+(i-2)*.32)) for i in range(4)]).shift(RIGHT*x)
        big=levels(-3,1.1,TEAL); small=levels(3,2.5,CRIMSON); a1=DoubleArrow(LEFT*3+DOWN*.55,LEFT*3+UP*.55,color=TEAL); a2=DoubleArrow(RIGHT*3+DOWN*1.25,RIGHT*3+UP*1.25,color=CRIMSON)
        labs=VGroup(Text("larger R",font=SERIF,font_size=27,color=TEAL).move_to(LEFT*3+DOWN*2.6),Text("smaller R",font=SERIF,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*2.6))
        self.play(FadeIn(heading("SHRINK THE DOT → WIDEN THE LOWEST TRANSITION")),FadeIn(big),FadeIn(small),GrowArrow(a1),GrowArrow(a2),FadeIn(labs),run_time=1.2); hold(self,"B06",1.2)

class B07_ColorMap(Scene):
    def construct(self):
        colors=["#C41230"]*20+["#D6A63B"]*20+["#2F6BBA"]*20
        grad=VGroup(*[Rectangle(width=.15,height=1.2,stroke_width=0,fill_opacity=1,fill_color=c) for c in colors]).arrange(RIGHT,buff=0).set_width(10)
        arrow=Arrow(LEFT*4,RIGHT*4,color=INK).next_to(grad,UP,buff=.75); lab=Text("energy ↑     wavelength ↓",font=MONO,font_size=32,color=INK).next_to(arrow,UP)
        ends=VGroup(Text("redder",font=SERIF,font_size=28,color=CRIMSON),Text("bluer",font=SERIF,font_size=28,color=TEAL)).arrange(RIGHT,buff=7).next_to(grad,DOWN,buff=.5)
        self.play(FadeIn(heading("E = hc/λ")),FadeIn(grad),GrowArrow(arrow),FadeIn(lab),FadeIn(ends),run_time=1.2); hold(self,"B07",1.2)

class B08_CoulombCorrection(Scene):
    def construct(self):
        pos=Text("+ A/R²",font=MONO,font_size=48,color=TEAL).move_to(LEFT*2.8); neg=Text("− B/R",font=MONO,font_size=48,color=CRIMSON).move_to(RIGHT*2.8); note=Text("electron–hole attraction lowers the transition",font=SERIF,font_size=29,color=INK).shift(DOWN*2.4)
        self.play(FadeIn(heading("THE FIRST CORRECTION PULLS THE ENERGY DOWN")),FadeIn(pos),FadeIn(neg),FadeIn(note),run_time=1); hold(self,"B08")

class B09_ModelAudit(Scene):
    def construct(self):
        items=["nonparabolic bands / changing m*","finite barriers and wave leakage","shape and size distribution","dielectric environment","surface chemistry"]
        rows=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
        self.play(FadeIn(heading("RIGHT TREND CAN STILL MISS THE NUMBER")),LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.08),run_time=1.2); hold(self,"B09",1.2)

class B10_AbsorptionEmission(Scene):
    def construct(self):
        absorb=Arrow(DOWN*1.2,UP*1.5,color=TEAL); relax=Arrow(UP*1.5,UP*.6+RIGHT*2,color=CRIMSON); emit=Arrow(UP*.6+RIGHT*2,DOWN*1.2+RIGHT*2,color=TEAL)
        labs=VGroup(Text("absorb",font=SERIF,font_size=26,color=TEAL).next_to(absorb,LEFT),Text("relax",font=SERIF,font_size=26,color=CRIMSON).next_to(relax,UP),Text("emit",font=SERIF,font_size=26,color=TEAL).next_to(emit,RIGHT),Text("surface / defect paths can branch",font=SERIF,font_size=28,color=INK).shift(DOWN*2.5))
        self.play(FadeIn(heading("ABSORPTION EDGE ≠ ALWAYS THE EMISSION PEAK")),GrowArrow(absorb),GrowArrow(relax),GrowArrow(emit),FadeIn(labs),run_time=1.2); hold(self,"B10",1.2)

class B11_DurableScaling(Scene):
    def construct(self):
        ax=Axes(x_range=[1,5,1],y_range=[0,1.2,.3],x_length=9,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.35); curve=ax.plot(lambda x:1/x**2,x_range=[1,5],color=TEAL,stroke_width=4); dot=Dot(ax.c2p(1.4,1/1.4**2),color=CRIMSON); note=Text("shrinking length raises\nconfinement rapidly",font=SERIF,font_size=28,color=CRIMSON,line_spacing=1.15).move_to(RIGHT*2.7+UP*1.35)
        self.play(FadeIn(heading("THE SCALING SURVIVES THE CAVEATS")),FadeIn(ax),Create(curve),FadeIn(dot),FadeIn(note),run_time=1.2); hold(self,"B11",1.2)

class B12_YourTurn(Scene):
    def construct(self):
        g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=35,color=INK),Text("R:  3 nm  →  2 nm",font=MONO,font_size=39,color=TEAL),Text("confinement ∝ 1/R²",font=MONO,font_size=35,color=CRIMSON),Text("By what factor does it grow?",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B12")

class B13_Answer(Scene):
    def construct(self):
        g=VGroup(Text("ANSWER",font=DISPLAY,font_size=35,color=INK),Text("(3/2)² = 2.25",font=MONO,font_size=52,color=TEAL),Text("two and a quarter times larger",font=SERIF,font_size=31,color=CRIMSON),Text("trend only • real spectrum needs corrections",font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.52)
        self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        self.camera.background_color="#201F1C"; title=Text("Why a Smaller Quantum Dot Glows Bluer",font=DISPLAY,font_size=34,color="#F2EFE8"); credit=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45)
        self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B14")
