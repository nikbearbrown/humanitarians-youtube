import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def gaussian(sig=1,color=CRIMSON,shift=ORIGIN): return FunctionGraph(lambda x:2*np.exp(-x*x/(2*sig*sig)),x_range=[-5,5],color=color,stroke_width=4).shift(shift)
class B02_OneKet(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('ONE STATE · TWO COMPONENT LISTS')); ket=Text('|psi>',font=MONO,font_size=56,color=INK).move_to(UP*1.7); left=VGroup(Text('position basis',font=SERIF,font_size=30,color=TEAL),Text('psi(x) = <x|psi>',font=MONO,font_size=34,color=TEAL)).arrange(DOWN).move_to(LEFT*3+DOWN*.7); right=VGroup(Text('momentum basis',font=SERIF,font_size=30,color=CRIMSON),Text('phi(p) = <p|psi>',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN).move_to(RIGHT*3+DOWN*.7); self.play(FadeIn(ket,left,right),run_time=1); self.wait(max(.1,d-1))
class B03_Axes(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('KEEP THE VECTOR FIXED · CHANGE THE AXES')); v=Arrow(ORIGIN,RIGHT*3+UP*2,color=CRIMSON,buff=0,stroke_width=7); axes1=VGroup(Line(LEFT*4,RIGHT*4,color=SLATE),Line(DOWN*2.5,UP*2.5,color=SLATE)); axes2=VGroup(Line(LEFT*3+DOWN*2,RIGHT*3+UP*2,color=TEAL),Line(LEFT*2+UP*3,RIGHT*2+DOWN*3,color=TEAL)); lab=Text('components change · vector does not',font=MONO,font_size=31,color=INK).move_to(DOWN*3); self.play(Create(axes1),GrowArrow(v),Transform(axes1,axes2),FadeIn(lab),run_time=1.5); self.wait(max(.1,d-1.5))
class B04_Position(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('POSITION REPRESENTATION')); g=gaussian(.75); lab=VGroup(Text('|psi(x)|^2',font=MONO,font_size=34,color=CRIMSON).move_to(UP*2.2),Text('narrow in x',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.3)); self.play(Create(g),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B05_Momentum(Scene):
 def construct(self):
  d=DUR.get('B05',9); self.add(bg(),ttl('MOMENTUM REPRESENTATION')); g=gaussian(2.2,TEAL); lab=VGroup(Text('|phi(p)|^2',font=MONO,font_size=34,color=TEAL).move_to(UP*2.2),Text('broad in p',font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*2.3)); self.play(Create(g),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B06_Map(Scene):
 def construct(self):
  d=DUR.get('B06',10); self.add(bg(),ttl('FOURIER TRANSFORM = UNITARY BASIS MAP')); x=Text('psi(x)',font=MONO,font_size=45,color=TEAL).shift(LEFT*3); p=Text('phi(p)',font=MONO,font_size=45,color=CRIMSON).shift(RIGHT*3); a=DoubleArrow(LEFT*1.6,RIGHT*1.6,color=INK,buff=0); labs=VGroup(Text('Fourier',font=SERIF,font_size=30,color=INK).move_to(UP*.7),Text('not time evolution · no physical kick',font=MONO,font_size=29,color=SLATE).move_to(DOWN*2)); self.play(FadeIn(x,p,labs),GrowArrow(a),run_time=1); self.wait(max(.1,d-1))
class B07_Widths(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('GAUSSIAN WIDTHS TRADE INVERSELY')); narrow=gaussian(.65,CRIMSON,LEFT*3+DOWN*.4).scale(.55); broad=gaussian(2.0,TEAL,RIGHT*3+DOWN*.4).scale(.55); labs=VGroup(Text('small sigma_x',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*2.3),Text('large sigma_p',font=MONO,font_size=27,color=TEAL).move_to(RIGHT*3+DOWN*2.3),Text('sigma_x sigma_p = hbar/2',font=MONO,font_size=35,color=INK).move_to(UP*2)); self.play(Create(narrow),Create(broad),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B08_Phase(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('SAME POSITION DENSITY · DIFFERENT PHASE')); env=gaussian(1.5,SLATE).shift(UP*.1); flat=Line(LEFT*4,RIGHT*4,color=TEAL).shift(DOWN*.8); ramp=Line(LEFT*4+DOWN*2,RIGHT*4+UP*.1,color=CRIMSON); labs=VGroup(Text('|psi|^2 same',font=MONO,font_size=29,color=SLATE).move_to(UP*2.5),Text('phase 0',font=MONO,font_size=27,color=TEAL).move_to(LEFT*4+DOWN*2.5),Text('phase kx',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*4+DOWN*2.5)); self.play(Create(env),Create(flat),Create(ramp),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Unitary(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('UNITARITY PRESERVES PHYSICAL INFORMATION')); rows=VGroup(Text('integral |psi(x)|^2 dx = 1',font=MONO,font_size=35,color=TEAL),Text('integral |phi(p)|^2 dp = 1',font=MONO,font_size=35,color=CRIMSON),Text('inner products preserved',font=SERIF,font_size=33,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_Caveat(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('THE METAPHOR HAS A BOUNDARY')); left=VGroup(Text('TURNING YOUR HEAD',font=DISPLAY,font_size=31,color=TEAL),Text('finite-dimensional analogy',font=SERIF,font_size=28,color=TEAL)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('EXACT MAP',font=DISPLAY,font_size=31,color=CRIMSON),Text('complex Fourier integral',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B11_Number(Scene):
 def construct(self):
  d=DUR.get('B11',10); self.add(bg(),ttl('ONE-NANOMETER MINIMUM-UNCERTAINTY PACKET')); rows=VGroup(Text('sigma_x = 1.0 nm',font=MONO,font_size=37,color=TEAL),Text('sigma_p,min = hbar / (2 sigma_x)',font=MONO,font_size=35,color=INK),Text('= 5.27 x 10^-26 kg m/s',font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B12_Shadows(Scene):
 def construct(self):
  d=DUR.get('B12',9); self.add(bg(),ttl('TWO SHADOWS · ONE STATE')); ket=Dot(ORIGIN,radius=.3,color=INK); x=Arrow(ORIGIN,LEFT*4+DOWN*1.5,color=TEAL,buff=0); p=Arrow(ORIGIN,RIGHT*4+DOWN*1.5,color=CRIMSON,buff=0); labs=VGroup(Text('position shadow',font=MONO,font_size=28,color=TEAL).move_to(LEFT*4+DOWN*2.3),Text('momentum shadow',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*4+DOWN*2.3),Text('|psi> fixed',font=MONO,font_size=32,color=INK).move_to(UP*1)); self.play(FadeIn(ket,labs),GrowArrow(x),GrowArrow(p),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN: HALVE sigma_x')); rows=VGroup(Text('sigma_x -> sigma_x / 2',font=MONO,font_size=37,color=TEAL),Text('sigma_p -> 2 sigma_p',font=MONO,font_size=37,color=CRIMSON),Text('product remains hbar/2',font=SERIF,font_size=33,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',9); self.add(bg(),Text('WHY FOURIER IS LIKE TURNING YOUR HEAD',font=DISPLAY,font_size=35,color=CRIMSON).move_to(UP*2.3),Text('one abstract ket',font=MONO,font_size=36,color=INK).move_to(UP*.8),Text('two basis-dependent component lists',font=MONO,font_size=32,color=TEAL).move_to(DOWN*.4),Text('exact map: unitary Fourier transform',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
