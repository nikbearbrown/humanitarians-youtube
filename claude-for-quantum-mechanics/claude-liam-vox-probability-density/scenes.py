import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def rho(a=.5): return FunctionGraph(lambda x:(1/a)*np.exp(-2*abs(x)/a),x_range=[-3,3],color=CRIMSON,stroke_width=5).scale(1.7,about_point=ORIGIN)
class B02_Density(Scene):
 def construct(self):
  d=DUR.get('B02',8); self.add(bg(),ttl('PROBABILITY IS NOT PROBABILITY DENSITY')); p=Text('P(region)',font=MONO,font_size=43,color=TEAL).move_to(LEFT*3.5); den=Text('rho(x) = |psi(x)|^2',font=MONO,font_size=40,color=CRIMSON).move_to(RIGHT*3.2); units=VGroup(Text('dimensionless',font=SERIF,font_size=27,color=INK).move_to(LEFT*3.5+DOWN*1.2),Text('per unit length',font=SERIF,font_size=27,color=INK).move_to(RIGHT*3.2+DOWN*1.2)); self.play(FadeIn(p,den,units),run_time=1); self.wait(max(.1,d-1))
class B03_Units(Scene):
 def construct(self):
  d=DUR.get('B03',8); self.add(bg(),ttl('THE HEIGHT CARRIES UNITS')); eq=Text('rho(0) = 2 nm^-1',font=MONO,font_size=50,color=CRIMSON); note=Text('two per nanometer  !=  probability two',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*1.5); self.play(Write(eq),FadeIn(note),run_time=1); self.wait(max(.1,d-1))
class B04_Area(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('INTERVAL PROBABILITY IS AREA')); axes=Axes(x_range=[-3,3,1],y_range=[0,2.2,1],x_length=10,y_length=4,axis_config={'color':SLATE}).shift(DOWN*.5); curve=axes.plot(lambda x:2*np.exp(-4*abs(x)),x_range=[-3,3],color=CRIMSON); area=axes.get_area(curve,x_range=[-.6,.6],color=TEAL,opacity=.35); eq=Text('P = integral rho(x) dx',font=MONO,font_size=32,color=INK).move_to(UP*2.4); self.play(Create(axes),Create(curve),FadeIn(area,eq),run_time=1); self.wait(max(.1,d-1))
class B05_Wavefunction(Scene):
 def construct(self):
  d=DUR.get('B05',9); self.add(bg(),ttl('A NORMALIZED EXPONENTIAL STATE')); eq=Text('psi(x) = (1/sqrt(a)) exp(-|x|/a)',font=MONO,font_size=40,color=CRIMSON).move_to(UP*1.2); norm=Text('integral |psi|^2 dx = 1',font=MONO,font_size=35,color=TEAL).move_to(DOWN*.8); self.play(Write(eq),FadeIn(norm),run_time=1); self.wait(max(.1,d-1))
class B06_Peak(Scene):
 def construct(self):
  d=DUR.get('B06',9); self.add(bg(),ttl('a = 0.5 nm GIVES A PEAK ABOVE ONE')); curve=rho(); base=Line(LEFT*5,RIGHT*5,color=SLATE).shift(DOWN*1.5); curve.shift(DOWN*1.5); peak=DashedLine(np.array([0,-1.5,0]),np.array([0,1.9,0]),color=TEAL); labs=VGroup(Text('rho(x) = (1/a)e^(-2|x|/a)',font=MONO,font_size=29,color=INK).move_to(UP*2.6),Text('rho(0) = 2 nm^-1',font=MONO,font_size=34,color=CRIMSON).move_to(RIGHT*3+UP*1)); self.play(Create(base),Create(curve),Create(peak),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B07_Exact(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('EXACT PROBABILITY IN +/- 0.1 nm')); eqs=VGroup(Text('P = integral from -0.1 to +0.1 rho(x) dx',font=MONO,font_size=31,color=INK),Text('= 1 - exp(-0.4)',font=MONO,font_size=37,color=INK),Text('= 0.3297',font=MONO,font_size=50,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs[:2]),run_time=.7); self.play(FadeIn(eqs[2]),run_time=.5); self.wait(max(.1,d-1.2))
class B08_HeightArea(Scene):
 def construct(self):
  d=DUR.get('B08',8); self.add(bg(),ttl('HEIGHT > 1 · AREA < 1')); tall=Rectangle(width=1,height=4,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).move_to(LEFT*3); area=Rectangle(width=3.3,height=1,color=TEAL,fill_color=TEAL,fill_opacity=.18).move_to(RIGHT*3); labs=VGroup(Text('density: 2 nm^-1',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*2.6),Text('interval P: 0.3297',font=MONO,font_size=27,color=TEAL).move_to(RIGHT*3+DOWN*1.3)); self.play(FadeIn(tall,area,labs),run_time=1); self.wait(max(.1,d-1))
class B09_PointBin(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('A POINT HAS ZERO WIDTH')); line=Line(LEFT*5,RIGHT*5,color=SLATE); point=Dot(radius=.16,color=CRIMSON); bin=Rectangle(width=2.2,height=.8,color=TEAL,fill_color=TEAL,fill_opacity=.2).move_to(RIGHT*3); labs=VGroup(Text('exact point: width 0 -> P=0',font=MONO,font_size=26,color=CRIMSON).move_to(LEFT*2.8+DOWN*1.2),Text('detector bin: finite width',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*3+DOWN*1.2)); self.play(Create(line),FadeIn(point,bin,labs),run_time=1); self.wait(max(.1,d-1))
class B10_Convert(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('DENSITY HEIGHT DEPENDS ON UNITS')); left=Text('2 nm^-1',font=MONO,font_size=47,color=CRIMSON).move_to(LEFT*3.5); right=Text('2 x 10^9 m^-1',font=MONO,font_size=43,color=TEAL).move_to(RIGHT*3.5); eq=Text('same physical density',font=SERIF,font_size=31,color=INK).move_to(DOWN*1.5); arrow=DoubleArrow(LEFT*.8,RIGHT*.8,color=SLATE,buff=0); self.play(FadeIn(left,right,eq),GrowArrow(arrow),run_time=1); self.wait(max(.1,d-1))
class B11_City(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('THE SAME IDEA: POPULATION DENSITY')); grid=VGroup(*[Dot(np.array([i*.35-2,j*.35-1,0]),radius=.06,color=CRIMSON) for i in range(12) for j in range(7)]); eqs=VGroup(Text('10,000 people / km^2',font=MONO,font_size=36,color=INK),Text('density x area = count',font=MONO,font_size=35,color=TEAL)).arrange(DOWN,buff=.8).move_to(RIGHT*3); grid.move_to(LEFT*3.5); self.play(FadeIn(grid,eqs),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get('B12',7); self.add(bg(),Text('READ DENSITY AS AREA',font=DISPLAY,font_size=35,color=TEAL).move_to(UP*2.3),Text('check the units',font=MONO,font_size=34,color=INK).move_to(UP*.8),Text('choose the resolved region',font=MONO,font_size=34,color=CRIMSON).move_to(DOWN*.4),Text('integrate to get probability',font=MONO,font_size=40,color=TEAL).move_to(DOWN*2)); self.wait(d)
