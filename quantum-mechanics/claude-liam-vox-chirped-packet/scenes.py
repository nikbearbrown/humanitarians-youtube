import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def packet(sig=2,k=5,b=0,color=CRIMSON): return FunctionGraph(lambda x:1.7*np.exp(-x*x/(2*sig*sig))*np.cos(k*x+b*x*x),x_range=[-6,6],color=color,stroke_width=4)
class B02_Initial(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('INITIALLY: ONE CARRIER SLOPE ACROSS THE ENVELOPE')); p=packet(2,5,0); env=VGroup(FunctionGraph(lambda x:1.7*np.exp(-x*x/8),x_range=[-6,6],color=SLATE),FunctionGraph(lambda x:-1.7*np.exp(-x*x/8),x_range=[-6,6],color=SLATE)); lab=Text('uniform local k = k0',font=MONO,font_size=31,color=TEAL).move_to(DOWN*2.5); self.play(Create(env),Create(p),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B03_Fourier(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('THE SAME MOMENTUM WEIGHTS REMAIN')); bars=VGroup(*[Rectangle(width=.45,height=h,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.25).align_to(DOWN*1.8,DOWN).shift(RIGHT*x) for x,h in zip([-2,-1.5,-1,-.5,0,.5,1,1.5,2],[.5,1,1.8,2.8,3.4,2.8,1.8,1,.5])]); labels=VGroup(Text('|A(k)|^2',font=MONO,font_size=29,color=INK).move_to(UP*2.3),Text('unchanged by free evolution',font=SERIF,font_size=30,color=TEAL).move_to(DOWN*2.5)); self.play(FadeIn(bars,labels),run_time=1); self.wait(max(.1,d-1))
class B04_Dispersion(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('QUADRATIC DISPERSION SORTS SPEEDS')); eqs=VGroup(Text('omega(k) = hbar k^2 / (2m)',font=MONO,font_size=39,color=INK),Text('v_g(k) = d omega/dk = hbar k / m',font=MONO,font_size=37,color=CRIMSON),Text('larger k -> faster',font=SERIF,font_size=32,color=TEAL)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B05_Sort(Scene):
 def construct(self):
  d=DUR.get('B05',9); self.add(bg(),ttl('LOW k LAGS · HIGH k LEADS')); dots=VGroup(*[Dot(np.array([x,0,0]),radius=.22,color=c) for x,c in [(-4,SLATE),(-2.5,TEAL),(0,INK),(2.8,CRIMSON),(4.7,CRIMSON)]]); labs=VGroup(Text('low k',font=MONO,font_size=27,color=SLATE).move_to(LEFT*4+DOWN*1),Text('k0',font=MONO,font_size=27,color=INK).move_to(DOWN*1),Text('high k',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*4+DOWN*1)); direction=Arrow(LEFT*5.5,RIGHT*5.5,color=TEAL,buff=0).shift(DOWN*2.2); self.play(FadeIn(dots,labs),GrowArrow(direction),run_time=1); self.wait(max(.1,d-1))
class B06_Correlation(Scene):
 def construct(self):
  d=DUR.get('B06',9); self.add(bg(),ttl('DISTRIBUTION FIXED · CORRELATION GROWS')); hist=VGroup(*[Rectangle(width=.35,height=h,color=INK,fill_color=INK,fill_opacity=.15).shift(LEFT*3+RIGHT*i*.4+DOWN*(2-h)/2) for i,h in enumerate([.4,1,2,3,2,1,.4])]); diag=VGroup(*[Dot(np.array([1+i*.55,-1.5+i*.42,0]),radius=.13,color=CRIMSON) for i in range(8)]); labs=VGroup(Text('P(k): unchanged',font=MONO,font_size=27,color=INK).move_to(LEFT*3+UP*2),Text('x-k correlation',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*3+UP*2)); self.play(FadeIn(hist,diag,labs),run_time=1); self.wait(max(.1,d-1))
class B07_Phase(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('SPREADING BUILDS A QUADRATIC PHASE')); parabola=FunctionGraph(lambda x:.16*x*x-1.7,x_range=[-5,5],color=CRIMSON,stroke_width=4); tangent1=Line(LEFT*5+DOWN*.2,LEFT*1+DOWN*1.5,color=TEAL); tangent2=Line(RIGHT*1+DOWN*1.5,RIGHT*5+DOWN*.2,color=TEAL); eq=Text('phi(x,t) = k0 x + b(t)(x-xc)^2',font=MONO,font_size=32,color=INK).move_to(UP*2.3); self.play(Create(parabola),Create(tangent1),Create(tangent2),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B08_Ramp(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('LOCAL WAVENUMBER IS THE PHASE GRADIENT')); axes=Axes(x_range=[-4,4,1],y_range=[-2,2,1],x_length=10,y_length=4,axis_config={'color':SLATE}); line=axes.plot(lambda x:.35*x,x_range=[-4,4],color=CRIMSON); eq=Text('k_local = k0 + C(t)(x-xc)',font=MONO,font_size=34,color=INK).move_to(UP*2.7); labs=VGroup(Text('rear: lower k',font=MONO,font_size=25,color=TEAL).move_to(LEFT*4+DOWN*2.5),Text('front: higher k',font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*4+UP*1.7)); self.play(Create(axes),Create(line),FadeIn(eq,labs),run_time=1); self.wait(max(.1,d-1))
class B09_Chirp(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('LATER: LONG CRESTS BEHIND · SHORT CRESTS AHEAD')); p=packet(3,5,.32); env=VGroup(FunctionGraph(lambda x:1.7*np.exp(-x*x/18),x_range=[-6,6],color=SLATE),FunctionGraph(lambda x:-1.7*np.exp(-x*x/18),x_range=[-6,6],color=SLATE)); labs=VGroup(Text('longer lambda',font=MONO,font_size=25,color=TEAL).move_to(LEFT*4+DOWN*2.4),Text('shorter lambda',font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*4+DOWN*2.4)); self.play(Create(env),Create(p),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B10_Tails(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('THE TAILS CARRY LITTLE WEIGHT')); env=FunctionGraph(lambda x:2*np.exp(-x*x/8),x_range=[-6,6],color=CRIMSON,stroke_width=4); center=Rectangle(width=5,height=3,color=TEAL,fill_color=TEAL,fill_opacity=.08); tails=VGroup(Rectangle(width=3,height=3,color=SLATE,fill_color=SLATE,fill_opacity=.05).move_to(LEFT*4),Rectangle(width=3,height=3,color=SLATE,fill_color=SLATE,fill_opacity=.05).move_to(RIGHT*4)); labs=VGroup(Text('appreciable amplitude',font=MONO,font_size=26,color=TEAL).move_to(DOWN*2.2),Text('tiny tails',font=MONO,font_size=23,color=SLATE).move_to(RIGHT*4+DOWN*2.2)); self.play(Create(env),FadeIn(center,tails,labs),run_time=1); self.wait(max(.1,d-1))
class B11_Reverse(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('REVERSE EVOLUTION · REVERSE THE CHIRP')); plus=Line(LEFT*5,LEFT*1+UP*2,color=CRIMSON,stroke_width=5); minus=Line(RIGHT*1+UP*2,RIGHT*5,color=TEAL,stroke_width=5); arrow=DoubleArrow(LEFT*.8,RIGHT*.8,color=SLATE,buff=0); labs=VGroup(Text('C(t) > 0',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*1.5),Text('C(t) < 0',font=MONO,font_size=27,color=TEAL).move_to(RIGHT*3+DOWN*1.5)); self.play(Create(plus),Create(minus),GrowArrow(arrow),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get('B12',8); self.add(bg(),Text('CHIRP WITHOUT NEW MOMENTUM',font=DISPLAY,font_size=34,color=TEAL).move_to(UP*2.3),Text('same momentum weights',font=MONO,font_size=34,color=INK).move_to(UP*.8),Text('different group velocities',font=MONO,font_size=34,color=CRIMSON).move_to(DOWN*.4),Text('position-dependent phase slope',font=MONO,font_size=39,color=TEAL).move_to(DOWN*2)); self.wait(d)
