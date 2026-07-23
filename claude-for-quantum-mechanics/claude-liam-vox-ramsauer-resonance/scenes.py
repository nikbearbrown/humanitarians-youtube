import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def barrier(w=3): return Rectangle(width=w,height=4.3,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12)
def wav(x0,x1,k,y=0,col=TEAL):
 xs=np.linspace(x0,x1,300); return VMobject(color=col,stroke_width=3).set_points_smoothly([np.array([x,.55*np.sin(k*x)+y,0]) for x in xs])

class B02_Regions(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("ABOVE THE BARRIER: WAVES PROPAGATE EVERYWHERE")); b=barrier(); w1=wav(-6,-1.5,2,0); wi=wav(-1.5,1.5,3.5,0,CRIMSON); w2=wav(1.5,6,2,0); labs=VGroup(Text("k",font=MONO,font_size=25,color=TEAL).move_to(LEFT*4+DOWN*1.4),Text("q",font=MONO,font_size=25,color=CRIMSON).move_to(DOWN*1.4),Text("k",font=MONO,font_size=25,color=TEAL).move_to(RIGHT*4+DOWN*1.4),Text("E > V0",font=MONO,font_size=26,color=INK).move_to(UP*2)); self.play(FadeIn(b),Create(w1),Create(wi),Create(w2),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("How can two reflecting boundaries",font=SERIF,font_size=40,color=INK).move_to(UP*.5),Text("produce zero reflection?",font=SERIF,font_size=44,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_FirstPaths(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("TWO FIRST REFLECTED PATHS")); b=barrier(); inc=Arrow(LEFT*5,LEFT*1.7,color=TEAL,buff=0); r0=Arrow(LEFT*1.7,LEFT*4.5,color=CRIMSON,buff=0).shift(UP*1.2); inside=VGroup(Arrow(LEFT*1.3,RIGHT*1.3,color=TEAL,buff=0).shift(DOWN*.3),Arrow(RIGHT*1.3,LEFT*1.3,color=SLATE,buff=0).shift(DOWN*1.2)); labs=VGroup(Text("immediate reflection",font=MONO,font_size=23,color=CRIMSON).next_to(r0,UP),Text("one internal round trip",font=MONO,font_size=23,color=INK).move_to(DOWN*2.7)); self.play(FadeIn(b),GrowArrow(inc),run_time=.6); self.play(GrowArrow(r0),GrowFromCenter(inside),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B05_ManyPaths(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("THE BARRIER GENERATES A SERIES OF ROUND TRIPS")); b=barrier(5); ys=[1.3,.5,-.3,-1.1]; paths=VGroup(*[VGroup(Arrow(LEFT*2.2,RIGHT*2.2,color=TEAL,buff=0),Arrow(RIGHT*2.2,LEFT*2.2,color=CRIMSON,buff=0)).shift(UP*y) for y in ys]); weights=VGroup(*[Text(s,font=MONO,font_size=22,color=INK).move_to(RIGHT*4+UP*y) for y,s in zip(ys,["path 1","path 2","path 3","..."])]); self.play(FadeIn(b),GrowFromCenter(paths),FadeIn(weights),run_time=1.2); self.wait(max(.1,d-1.2))

class B06_Phase(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("INTERNAL PROPAGATION ADDS PHASE")); b=barrier(5); one=Arrow(LEFT*2.1,RIGHT*2.1,color=TEAL,buff=0).shift(UP*.8); two=VGroup(Arrow(LEFT*2.1,RIGHT*2.1,color=CRIMSON,buff=0),Arrow(RIGHT*2.1,LEFT*2.1,color=CRIMSON,buff=0)).shift(DOWN*.8); labs=VGroup(Text("one traversal: q L",font=MONO,font_size=27,color=TEAL).next_to(one,UP),Text("round trip: 2 q L",font=MONO,font_size=27,color=CRIMSON).next_to(two,DOWN)); self.play(FadeIn(b),GrowArrow(one),GrowFromCenter(two),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B07_HalfWaves(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("RESONANCE: AN INTEGER NUMBER OF HALF-WAVELENGTHS")); b=barrier(6); w=wav(-3,3,PI,0,TEAL); eq=Text("q L = n pi",font=MONO,font_size=40,color=CRIMSON).move_to(UP*2.5); cancel=VGroup(Arrow(LEFT*4.8,LEFT*2.3,color=INK,buff=0).shift(DOWN*2.5),Arrow(LEFT*2.3,LEFT*4.8,color=CRIMSON,buff=0).shift(DOWN*2.5)); lab=Text("reflected amplitudes cancel",font=SERIF,font_size=27,color=INK).move_to(RIGHT*2.5+DOWN*2.5); self.play(FadeIn(b),Create(w),FadeIn(eq),run_time=.9); self.play(GrowFromCenter(cancel),FadeIn(lab),run_time=.8); self.wait(max(.1,d-1.7))

class B08_Perfect(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("IDEAL RESONANCE")); left=VGroup(Text("REFLECTION",font=DISPLAY,font_size=29,color=CRIMSON),Text("R = 0",font=MONO,font_size=48,color=CRIMSON)).arrange(DOWN,buff=.6).move_to(LEFT*3.5); right=VGroup(Text("TRANSMISSION",font=DISPLAY,font_size=29,color=TEAL),Text("T = 1",font=MONO,font_size=48,color=TEAL)).arrange(DOWN,buff=.6).move_to(RIGHT*3.5); div=Line(UP*2.2,DOWN*2.2,color=SLATE); self.play(FadeIn(left,right),Create(div),run_time=1); self.wait(max(.1,d-1))

class B09_Scan(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("TRANSMISSION PEAKS AT SUCCESSIVE RESONANCES")); ax=Axes(x_range=[0,10,2],y_range=[0,1.1,.2],x_length=10,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda x:.12+.88/(1+15*np.sin(1.25*x)**2),x_range=[.1,10],color=TEAL); labs=VGroup(Text("energy",font=MONO,font_size=23,color=INK).next_to(ax,DOWN),Text("T",font=MONO,font_size=23,color=INK).next_to(ax,LEFT),Text("T = 1",font=MONO,font_size=23,color=CRIMSON).move_to(UP*2.3)); self.play(Create(ax),Create(curve),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B10_Width(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("WIDTH CHANGES THE PHASE CONDITION")); b1=barrier(2).move_to(LEFT*3.5); b2=barrier(4).move_to(RIGHT*3.5); labs=VGroup(Text("L",font=MONO,font_size=30,color=CRIMSON).next_to(b1,DOWN),Text("2L",font=MONO,font_size=30,color=CRIMSON).next_to(b2,DOWN),Text("qL = n pi",font=MONO,font_size=28,color=INK).move_to(LEFT*3.5+UP*2.6),Text("2qL = n pi",font=MONO,font_size=28,color=INK).move_to(RIGHT*3.5+UP*2.6)); self.play(FadeIn(b1,b2,labs),run_time=1); self.wait(max(.1,d-1))

class B11_Nonideal(Scene):
 def construct(self):
  d=DUR.get("B11",11); self.add(bg(),ttl("WHAT BLURS PERFECT TRANSPARENCY")); items=VGroup(*[Text(s,font=MONO,font_size=28,color=c) for s,c in [("absorption",CRIMSON),("disorder",INK),("dephasing",CRIMSON),("energy spread",INK)]]).arrange(DOWN,buff=.5).move_to(LEFT*3.2); ideal=VGroup(Line(LEFT*1.7,RIGHT*1.7,color=TEAL,stroke_width=5),Text("sharp T=1 peak",font=SERIF,font_size=25,color=TEAL)).arrange(DOWN).move_to(RIGHT*3.4+UP*.8); blurred=VGroup(Line(LEFT*2.2,RIGHT*2.2,color=SLATE,stroke_width=12),Text("lower, broader peak",font=SERIF,font_size=25,color=INK)).arrange(DOWN).move_to(RIGHT*3.4+DOWN*1.2); self.play(FadeIn(items,ideal,blurred),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("THE BARRIER REMAINS",font=DISPLAY,font_size=32,color=CRIMSON).move_to(UP*1.7),Text("its reflected paths erase one another",font=SERIF,font_size=40,color=INK),Text("q L = n pi  →  T = 1",font=MONO,font_size=31,color=TEAL).move_to(DOWN*1.8)); self.wait(d)
