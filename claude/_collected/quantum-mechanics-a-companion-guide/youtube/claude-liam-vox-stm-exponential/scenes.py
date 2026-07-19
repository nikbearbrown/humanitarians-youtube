import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
    _b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in _b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def title(s): return Text(s,font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)

class B02_TipApproach(Scene):
    def construct(self):
        d=DUR.get("B02",10); self.add(bg(),title("A ONE-ÅNGSTRÖM MOVE")); surf=Line(LEFT*6,RIGHT*6,color=INK,stroke_width=5).move_to(DOWN*2.2); tip=Polygon(LEFT*.8+UP*2.2,RIGHT*.8+UP*2.2,DOWN*.2,color=SLATE,fill_color=SLATE,fill_opacity=.55); gap=DoubleArrow(RIGHT*1.8+DOWN*.1,RIGHT*1.8+DOWN*2.1,color=INK,buff=0); g5=Text("d = 5 Å",font=MONO,font_size=23,color=INK).next_to(gap,RIGHT); result=Text("move closer:  5 Å → 4 Å",font=MONO,font_size=26,color=CRIMSON).move_to(LEFT*3.7+DOWN*3.1); jump=Text("current rises sharply",font=DISPLAY,font_size=25,color=TEAL).move_to(RIGHT*3.7+DOWN*3.1)
        gap4=DoubleArrow(RIGHT*1.8+DOWN*.82,RIGHT*1.8+DOWN*2.1,color=INK,buff=0)
        g4=Text("d = 4 Å",font=MONO,font_size=23,color=INK).next_to(gap4,RIGHT)
        self.play(Create(surf),FadeIn(tip),GrowArrow(gap),FadeIn(g5),run_time=1.1); self.play(tip.animate.shift(DOWN*.65),Transform(gap,gap4),Transform(g5,g4),run_time=1.2); self.play(FadeIn(result),FadeIn(jump),run_time=.6); self.wait(max(.1,d-2.9))

class B03_Question(Scene):
    def construct(self):
        d=DUR.get("B03",8); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=22,color=SLATE).move_to(UP*2.5),Text("How can a sub-atomic distance step\nproduce a multiplicative current change?",font=SERIF,font_size=34,color=INK,line_spacing=1.25)); self.wait(d)

class B04_LinearVsExponential(Scene):
    def construct(self):
        d=DUR.get("B04",10); self.add(bg(),title("GENTLE GUESS VS EXPONENTIAL REALITY")); ax1=Axes(x_range=[0,5,1],y_range=[0,1.1,.2],x_length=5.2,y_length=4.2,tips=True).move_to(LEFT*3.7+DOWN*.3); ax2=Axes(x_range=[0,5,1],y_range=[0,1.1,.2],x_length=5.2,y_length=4.2,tips=True).move_to(RIGHT*3.7+DOWN*.3); lin=ax1.plot(lambda x:1-.14*x,x_range=[0,5],color=CRIMSON,stroke_width=4); exp=ax2.plot(lambda x:np.exp(-.75*x),x_range=[0,5],color=TEAL,stroke_width=4); labs=VGroup(Text("naive: gradual",font=MONO,font_size=22,color=CRIMSON).next_to(ax1,DOWN),Text("tunneling: exponential",font=MONO,font_size=22,color=TEAL).next_to(ax2,DOWN)); self.play(Create(ax1),Create(ax2),run_time=.8); self.play(Create(lin),Create(exp),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-2))

class B05_EvanescentTail(Scene):
    def construct(self):
        d=DUR.get("B05",11); self.add(bg(),title("THE ELECTRON WAVE LEAKS INTO THE VACUUM GAP")); left=Rectangle(width=3,height=5.2,color=SLATE,fill_color=SLATE,fill_opacity=.35).move_to(LEFT*5.5); right=Rectangle(width=2,height=5.2,color=SLATE,fill_color=SLATE,fill_opacity=.35).move_to(RIGHT*5.8); ax=Axes(x_range=[0,8,1],y_range=[0,1.2,.2],x_length=8.8,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda x:np.exp(-.55*x),x_range=[0,8],color=TEAL,stroke_width=5); labs=VGroup(Text("tip",font=DISPLAY,font_size=23,color=INK).move_to(LEFT*5.5+DOWN*3),Text("vacuum barrier",font=DISPLAY,font_size=23,color=INK).move_to(DOWN*3),Text("surface",font=DISPLAY,font_size=23,color=INK).move_to(RIGHT*5.8+DOWN*3)); self.play(FadeIn(left),FadeIn(right),Create(ax),run_time=.8); self.play(Create(curve),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-2.1))

class B06_LawCard(Scene):
    def construct(self):
        d=DUR.get("B06",5); self.add(bg(),Text("TUNNELING CURRENT",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*1.8),Text("I(d)  ∝  exp(−2 κ d)",font=MONO,font_size=46,color=TEAL),Text("distance sits in the exponent",font=SERIF,font_size=27,color=INK).move_to(DOWN*1.4)); self.wait(d)

class B07_FartherRatio(Scene):
    def construct(self):
        d=DUR.get("B07",12); self.add(bg(),title("MOVE 1 Å FARTHER")); eq1=Text("I₂ / I₁ = exp(−2 κ Δd)",font=MONO,font_size=34,color=INK).move_to(UP*1.6); eq2=Text("κ ≈ 1 Å⁻¹,   Δd = +1 Å",font=MONO,font_size=30,color=CRIMSON); eq3=Text("I₂ / I₁ = e⁻² ≈ 0.135 ≈ 1 / 7.4",font=MONO,font_size=34,color=TEAL).move_to(DOWN*1.6); arrow=Arrow(LEFT*4+DOWN*2.6,RIGHT*4+DOWN*2.6,color=CRIMSON); lab=Text("farther  →  current falls",font=DISPLAY,font_size=24,color=CRIMSON).next_to(arrow,DOWN); self.play(FadeIn(eq1),run_time=.6); self.play(FadeIn(eq2),run_time=.6); self.play(FadeIn(eq3),run_time=.7); self.play(GrowArrow(arrow),FadeIn(lab),run_time=.5); self.wait(max(.1,d-2.4))

class B08_CloserRatio(Scene):
    def construct(self):
        d=DUR.get("B08",9); self.add(bg(),title("REVERSE THE MOVE: 1 Å CLOSER")); e1=Text("Δd = −1 Å",font=MONO,font_size=34,color=CRIMSON).move_to(UP*1.5); e2=Text("I₂ / I₁ = exp(+2) ≈ 7.4",font=MONO,font_size=40,color=TEAL); e3=Text("same law • opposite sign",font=DISPLAY,font_size=25,color=INK).move_to(DOWN*1.7); self.play(FadeIn(e1),run_time=.6); self.play(FadeIn(e2),run_time=.8); self.play(FadeIn(e3),run_time=.5); self.wait(max(.1,d-1.9))

class B09_LogLine(Scene):
    def construct(self):
        d=DUR.get("B09",10); self.add(bg(),title("THE EXPONENTIAL BECOMES A STRAIGHT LINE")); ax=Axes(x_range=[0,6,1],y_range=[-6,1,1],x_length=9,y_length=5.2,tips=True).move_to(DOWN*.25); line=ax.plot(lambda x:-x,x_range=[0,6],color=TEAL,stroke_width=5); xl=Text("gap d",font=MONO,font_size=21,color=INK).next_to(ax,DOWN); yl=Text("ln I",font=MONO,font_size=21,color=INK).next_to(ax,LEFT); eq=Text("ln I = constant − 2κd",font=MONO,font_size=25,color=INK).move_to(RIGHT*4.4+UP*2.2); slope=Text("slope = −2κ",font=MONO,font_size=23,color=TEAL).move_to(RIGHT*4.5+UP*.9); self.play(Create(ax),FadeIn(xl),FadeIn(yl),run_time=.8); self.play(Create(line),FadeIn(eq),FadeIn(slope),run_time=1.1); self.wait(max(.1,d-1.9))

class B10_AtomicBump(Scene):
    def construct(self):
        d=DUR.get("B10",10); self.add(bg(),title("A 1 Å BUMP BECOMES A 7× CURRENT CONTRAST")); base=Line(LEFT*6,RIGHT*6,color=INK,stroke_width=5).move_to(DOWN*2); atom=Circle(radius=.5,color=TEAL,fill_color=TEAL,fill_opacity=.35).move_to(DOWN*1.5); tip=Polygon(LEFT*.8+UP*2.4,RIGHT*.8+UP*2.4,DOWN*.1,color=SLATE,fill_color=SLATE,fill_opacity=.5); flat=DoubleArrow(LEFT*3+DOWN*1.9,LEFT*3+DOWN*.1,color=INK,buff=0); bump=DoubleArrow(RIGHT*2.2+DOWN*.95,RIGHT*2.2+DOWN*.1,color=TEAL,buff=0); labels=VGroup(Text("flat gap d",font=MONO,font_size=21,color=INK).next_to(flat,LEFT),Text("gap d−1 Å",font=MONO,font_size=21,color=TEAL).next_to(bump,RIGHT),Text("≈ 7× current",font=DISPLAY,font_size=29,color=TEAL).move_to(DOWN*3.1)); self.play(Create(base),FadeIn(atom),FadeIn(tip),run_time=.8); self.play(GrowArrow(flat),GrowArrow(bump),FadeIn(labels),run_time=1.0); self.wait(max(.1,d-1.8))

class B11_WorkedExample(Scene):
    def construct(self):
        d=DUR.get("B11",11); self.add(bg(),title("ILLUSTRATIVE 4 eV BARRIER: κ ≈ 1.02 Å⁻¹"));
        def box(x,head,val,col):
            r=RoundedRectangle(width=3.8,height=3.1,corner_radius=.15,color=col,fill_color=col,fill_opacity=.07).move_to(x); t=VGroup(Text(head,font=MONO,font_size=23,color=INK),Text(val,font=MONO,font_size=25,color=col)).arrange(DOWN,buff=.55).move_to(x); return VGroup(r,t)
        b6=box(LEFT*4.6,"d = 6 Å","I₀ / 7.7",CRIMSON); b5=box(ORIGIN,"d = 5 Å","I₀",INK); b4=box(RIGHT*4.6,"d = 4 Å","7.7 I₀",TEAL); foot=Text("each 1 Å step changes current by exp(2κ) ≈ 7.7",font=MONO,font_size=22,color=INK).move_to(DOWN*3); self.play(FadeIn(b6),FadeIn(b5),FadeIn(b4),run_time=1.1); self.play(FadeIn(foot),run_time=.5); self.wait(max(.1,d-1.6))

class B12_Recap(Scene):
    def construct(self):
        d=DUR.get("B12",7); self.add(bg(),Text("ATOMIC SENSITIVITY",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*2.2),Text("equal height steps",font=SERIF,font_size=35,color=INK).move_to(UP*.8),Text("↓",font=DISPLAY,font_size=34,color=CRIMSON),Text("equal current ratios",font=SERIF,font_size=39,color=TEAL).move_to(DOWN*1.1),Text("because distance is in the exponent",font=MONO,font_size=22,color=INK).move_to(DOWN*2.5)); self.wait(d)
