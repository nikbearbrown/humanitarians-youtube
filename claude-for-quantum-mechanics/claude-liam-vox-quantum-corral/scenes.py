import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def corral(r=2.5,n=48): return VGroup(*[Dot(r*np.array([np.cos(a),np.sin(a),0]),radius=.085,color=INK) for a in np.linspace(0,TAU,n,endpoint=False)])
def rings(rs=(.6,1.25,1.9),color=CRIMSON): return VGroup(*[Circle(radius=r,color=color,stroke_width=4) for r in rs])
class B02_Surface(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('Cu(111) HOSTS A TWO-DIMENSIONAL SURFACE STATE')); plane=Rectangle(width=11,height=5,color=SLATE,fill_color=SLATE,fill_opacity=.05); waves=VGroup(*[FunctionGraph(lambda x,y=y:.22*np.sin(2*x)+y,x_range=[-5,5],color=TEAL,stroke_width=3) for y in [-1.5,-.5,.5,1.5]]); note=Text('electron waves propagate along the surface',font=MONO,font_size=28,color=INK).move_to(DOWN*2.9); self.play(FadeIn(plane),Create(waves),FadeIn(note),run_time=1); self.wait(max(.1,d-1))
class B03_Atoms(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('48 IRON ADATOMS FORM A STRONG SCATTERING RING')); c=corral().shift(LEFT*.5); radius=DoubleArrow(LEFT*.5,RIGHT*2,color=CRIMSON,buff=0); labs=VGroup(Text('48 Fe atoms',font=MONO,font_size=28,color=INK).move_to(LEFT*4.8),Text('R = 7.13 nm',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*4.8),Text('strong scatterer · not a perfect wall',font=SERIF,font_size=28,color=TEAL).move_to(DOWN*3)); self.play(LaggedStart(*[FadeIn(x) for x in c],lag_ratio=.01),GrowArrow(radius),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B04_Scatter(Scene):
 def construct(self):
  d=DUR.get('B04',10); self.add(bg(),ttl('OUTGOING AND RETURNING AMPLITUDES INTERFERE'),corral()); out=VGroup(*[Arrow(ORIGIN,2.1*np.array([np.cos(a),np.sin(a),0]),color=CRIMSON,buff=.1) for a in np.linspace(0,TAU,8,endpoint=False)]); back=VGroup(*[Arrow(2.2*np.array([np.cos(a),np.sin(a),0]),.5*np.array([np.cos(a),np.sin(a),0]),color=TEAL,buff=.1) for a in np.linspace(0,TAU,8,endpoint=False)]); self.play(GrowFromCenter(out),run_time=.7); self.play(GrowFromCenter(back),run_time=.7); self.wait(max(.1,d-1.4))
class B05_Interference(Scene):
 def construct(self):
  d=DUR.get('B05',9); pattern=VGroup(corral(),rings()).shift(LEFT*2.5); self.add(bg(),ttl('BRIGHT MAXIMA · DARK NODES'),pattern); labels=VGroup(Text('bright: constructive maxima',font=MONO,font_size=25,color=CRIMSON),Text('dark: destructive nodes',font=MONO,font_size=25,color=INK)).arrange(DOWN,buff=.8).move_to(RIGHT*3.5); self.play(FadeIn(labels),run_time=.7); self.wait(max(.1,d-.7))
class B06_Select(Scene):
 def construct(self):
  d=DUR.get('B06',10); self.add(bg(),ttl('THE CORRAL ENHANCES COMPATIBLE RESONANCES')); bad=VGroup(*[Circle(radius=r,color=SLATE,stroke_opacity=.3) for r in [.45,.9,1.35,1.8,2.25]]).move_to(LEFT*3.5); good=VGroup(corral(),rings()).scale(.75).move_to(RIGHT*3.2); labs=VGroup(Text('mismatched: weak buildup',font=MONO,font_size=24,color=SLATE).move_to(LEFT*3.5+DOWN*2.5),Text('compatible: strong LDOS pattern',font=MONO,font_size=24,color=CRIMSON).move_to(RIGHT*3.2+DOWN*2.5)); self.play(FadeIn(bad,good,labs),run_time=1); self.wait(max(.1,d-1))
class B07_Modes(Scene):
 def construct(self):
  d=DUR.get('B07',9); self.add(bg(),ttl('CIRCULAR GEOMETRY ALLOWS MORE THAN RINGS')); radial=rings((.5,1,1.5),CRIMSON).move_to(LEFT*3.5); lobes=VGroup(*[Ellipse(width=2.6,height=.9,color=TEAL,fill_color=TEAL,fill_opacity=.08).rotate(a) for a in [0,PI/3,2*PI/3]]).move_to(RIGHT*3.5); labs=VGroup(Text('radial symmetry',font=MONO,font_size=26,color=CRIMSON).move_to(LEFT*3.5+DOWN*2.2),Text('angular lobes',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*3.5+DOWN*2.2)); self.play(FadeIn(radial,lobes,labs),run_time=1); self.wait(max(.1,d-1))
class B08_NotString(Scene):
 def construct(self):
  d=DUR.get('B08',10); self.add(bg(),ttl('A DISK IS NOT A ONE-DIMENSIONAL STRING')); string=Line(LEFT*5,LEFT*1,color=SLATE,stroke_width=5); ticks=VGroup(*[Dot(np.array([x,0,0]),radius=.1,color=SLATE) for x in [-5,-3,-1]]); disk=Circle(radius=2,color=CRIMSON).move_to(RIGHT*3); formula=Text('lambda = diameter / integer',font=MONO,font_size=27,color=INK).move_to(DOWN*2.6); cross=Cross(formula.copy(),stroke_color=CRIMSON); self.play(Create(string),FadeIn(ticks),Create(disk),FadeIn(formula,cross),run_time=1); self.wait(max(.1,d-1))
class B09_STM(Scene):
 def construct(self):
  d=DUR.get('B09',10); self.add(bg(),ttl('STM SPECTROSCOPY MAPS LOCAL DENSITY OF STATES')); c=VGroup(corral(),rings()).scale(.75).move_to(RIGHT*2.5); tip=Polygon(LEFT*5+UP*2,LEFT*4+UP*2,LEFT*4.5+UP*.6,color=INK,fill_color=INK,fill_opacity=.3); scan=Arrow(LEFT*4.5+UP*.4,RIGHT*1+UP*.4,color=CRIMSON,buff=0); eq=Text('dI/dV(r,V)  ~  LDOS(r,E)',font=MONO,font_size=33,color=TEAL).move_to(DOWN*2.5); self.play(FadeIn(tip,c,eq),GrowArrow(scan),run_time=1); self.wait(max(.1,d-1))
class B10_NotOrbits(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('NOT ELECTRON ORBITS · AN ENERGY-RESOLVED MAP')); left=VGroup(*[Dot(np.array([-4+i*.6,np.sin(i),0]),radius=.13,color=SLATE) for i in range(7)]); right=VGroup(corral(),rings()).scale(.7).move_to(RIGHT*3); cross=Cross(left,stroke_color=CRIMSON); labels=VGroup(Text('particle tracks',font=MONO,font_size=25,color=SLATE).move_to(LEFT*3.2+DOWN*2),Text('surface-state LDOS',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*2)); self.play(FadeIn(cross,right,labels),run_time=1); self.wait(max(.1,d-1))
class B11_Change(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('CHANGE ENERGY OR GEOMETRY · CHANGE THE PATTERN')); a=VGroup(Circle(radius=2,color=INK),rings((.6,1.2),CRIMSON)).move_to(LEFT*3.5); b=VGroup(Ellipse(width=5,height=3,color=INK),Ellipse(width=3.8,height=1.8,color=TEAL),Ellipse(width=2.3,height=.9,color=TEAL)).move_to(RIGHT*3.5); arrow=Arrow(LEFT*.7,RIGHT*.7,color=SLATE,buff=0); self.play(FadeIn(a,b),GrowArrow(arrow),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get('B12',8); self.add(bg(),Text('WHO DREW THE RINGS?',font=DISPLAY,font_size=35,color=TEAL).move_to(UP*2.3),Text('48 Fe atoms supplied scattering',font=MONO,font_size=31,color=INK).move_to(UP*.7),Text('circular confinement selected resonances',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*.5),Text('STM mapped their local density of states',font=SERIF,font_size=29,color=TEAL).move_to(DOWN*2)); self.wait(d)
