import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def well(): return FunctionGraph(lambda x:.035*(x*x-9)**2-1.5,x_range=[-5,5],color=INK,stroke_width=4)
def lobes(): return VGroup(FunctionGraph(lambda x:2*np.exp(-3*(x+3)**2)-1.2,x_range=[-5,0],color=CRIMSON,stroke_width=4),FunctionGraph(lambda x:2*np.exp(-3*(x-3)**2)-1.2,x_range=[0,5],color=CRIMSON,stroke_width=4))
class B02_Equations(Scene):
 def construct(self):
  d=DUR.get('B02',15); self.add(bg(),ttl('EXACT THEOREM · APPROXIMATE CLASSICAL CLOSURE')); rows=VGroup(Text('d<x>/dt = <p>/m',font=MONO,font_size=39,color=TEAL),Text('d<p>/dt = <F(x)>',font=MONO,font_size=39,color=CRIMSON),Text('<F(x)> approx F(<x>)  only when justified',font=MONO,font_size=31,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B03_Narrow(Scene):
 def construct(self):
  d=DUR.get('B03',12); self.add(bg(),ttl('NARROW PACKET: LOCALLY CLASSICAL')); w=well(); p=FunctionGraph(lambda x:1.3*np.exp(-3*(x+2.3)**2)-.7,x_range=[-4,0],color=CRIMSON,stroke_width=4); mean=DashedLine(DOWN*2,UP*1.8,color=TEAL).shift(LEFT*2.3); lab=Text('short-time approximation',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.8); self.play(Create(w),Create(p),Create(mean),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B04_Split(Scene):
 def construct(self):
  d=DUR.get('B04',14); self.add(bg(),ttl('SPLIT STATE: MEAN ON THE BARRIER')); w=well(); p=lobes(); mean=DashedLine(DOWN*2.2,UP*2.1,color=TEAL); lab=Text('<x> = 0',font=MONO,font_size=32,color=TEAL).move_to(UP*2.5); self.play(Create(w),Create(p),Create(mean),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B05_MeanMode(Scene):
 def construct(self):
  d=DUR.get('B05',14); self.add(bg(),ttl('MEAN IS NOT MODE')); ax=NumberLine(x_range=[-4,4,1],length=10,color=SLATE); dots=VGroup(Dot(ax.n2p(-2),radius=.3,color=CRIMSON),Dot(ax.n2p(2),radius=.3,color=CRIMSON),Dot(ax.n2p(0),radius=.18,color=TEAL)); labs=VGroup(Text('modes',font=MONO,font_size=28,color=CRIMSON).move_to(LEFT*3+UP*1.3),Text('mean',font=MONO,font_size=28,color=TEAL).move_to(UP*1.3)); self.play(Create(ax),FadeIn(dots,labs),run_time=1); self.wait(max(.1,d-1))
class B06_NarrowForce(Scene):
 def construct(self):
  d=DUR.get('B06',17); self.add(bg(),ttl('NARROW SUPPORT SAMPLES NEARLY ONE FORCE')); curve=FunctionGraph(lambda x:.18*x*x-.8,x_range=[-3.8,3.8],color=INK); window=Rectangle(width=1.7,height=3.5,color=TEAL,fill_color=TEAL,fill_opacity=.1).shift(LEFT*2); tangent=Line(LEFT*3+DOWN*.3,LEFT*1+UP*.3,color=CRIMSON); eq=Text('<F> approx F(<x>)',font=MONO,font_size=36,color=TEAL).move_to(DOWN*2.5); self.play(Create(curve),FadeIn(window),Create(tangent),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B07_Symmetry(Scene):
 def construct(self):
  d=DUR.get('B07',14); self.add(bg(),ttl('EVEN POTENTIAL · ODD FORCE · CANCELLING AVERAGE')); left=Arrow(LEFT*4,LEFT*1.5,color=CRIMSON,buff=0); right=Arrow(RIGHT*4,RIGHT*1.5,color=CRIMSON,buff=0); center=DashedLine(DOWN*2,UP*2,color=TEAL); eq=Text('<F> = 0 by symmetry',font=MONO,font_size=37,color=INK).move_to(DOWN*2.6); self.play(GrowArrow(left),GrowArrow(right),Create(center),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B08_Ensemble(Scene):
 def construct(self):
  d=DUR.get('B08',16); self.add(bg(),ttl('ONE MEAN · TWO CLUSTERS OF OUTCOMES')); dots=VGroup(*[Dot(np.array([x,0,0]),radius=.12,color=CRIMSON) for x in [-3.4,-3.2,-3,-2.8,-2.6,2.6,2.8,3,3.2,3.4]]); mean=Arrow(DOWN*2,ORIGIN,color=TEAL,buff=0); labs=VGroup(Text('detections',font=MONO,font_size=29,color=CRIMSON).move_to(UP*1.2),Text('ensemble mean',font=MONO,font_size=29,color=TEAL).move_to(DOWN*2.5)); self.play(FadeIn(dots),GrowArrow(mean),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Moments(Scene):
 def construct(self):
  d=DUR.get('B09',16); self.add(bg(),ttl('A SPLIT STATE NEEDS MORE THAN ITS MEAN')); rows=VGroup(Text('<x> : center',font=MONO,font_size=36,color=SLATE),Text('variance : spread',font=MONO,font_size=36,color=TEAL),Text('full P(x) : two lobes',font=MONO,font_size=36,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',17); self.add(bg(),ttl('YOUR TURN: HALF AT -2 · HALF AT +2')); eqs=VGroup(Text('<x> = 0',font=MONO,font_size=42,color=TEAL),Text('Var(x) approx 4',font=MONO,font_size=42,color=CRIMSON),Text('variance reveals what the mean hides',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',18); self.add(bg(),Text('WHY THE AVERAGE STOPS LOOKING CLASSICAL',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('<F(x)> need not equal F(<x>)',font=MONO,font_size=34,color=TEAL).move_to(UP*.8),Text('split distributions defeat one-number summaries',font=MONO,font_size=30,color=INK).move_to(DOWN*.4),Text('expectation value is not a hidden trajectory',font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
