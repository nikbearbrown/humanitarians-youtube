import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def sphere(angle=70):
 c=Circle(radius=2.25,color=SLATE); eq=Ellipse(width=4.5,height=1.15,color=SLATE); axis=DoubleArrow(DOWN*2.6,UP*2.6,color=INK,buff=0); a=np.deg2rad(angle); v=Arrow(ORIGIN,np.array([2*np.sin(a),2*np.cos(a),0]),color=CRIMSON,buff=0,stroke_width=7); return VGroup(c,eq,axis,v)
class B02_Resonant(Scene):
 def construct(self):
  d=DUR.get('B02',14); self.add(bg(),ttl('ON RESONANCE, A WEAK DRIVE CAN REACH THE SOUTH POLE')); s=sphere(155); wave=FunctionGraph(lambda x:.35*np.sin(5*x),x_range=[-2,2],color=TEAL).shift(LEFT*4); pulse=VGroup(wave,Text('RF on resonance',font=MONO,font_size=27,color=TEAL).move_to(LEFT*4+DOWN*2)); self.play(Create(s),Create(pulse),run_time=1.2); self.wait(max(.1,d-1.2))
class B03_Populations(Scene):
 def construct(self):
  d=DUR.get('B03',12); self.add(bg(),ttl('POPULATIONS EXCHANGE COMPLEMENTARILY')); ax=Axes(x_range=[0,6.3,1.57],y_range=[0,1,.25],x_length=10,y_length=5,axis_config={'color':SLATE}); up=ax.plot(lambda x:np.cos(x/2)**2,x_range=[0,6.28],color=TEAL); dn=ax.plot(lambda x:np.sin(x/2)**2,x_range=[0,6.28],color=CRIMSON); labs=VGroup(Text('P(up)',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*4+UP*2),Text('P(down)',font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*4+UP*1.4),Text('sum = 1',font=MONO,font_size=27,color=INK).move_to(DOWN*3)); self.play(Create(ax),Create(up),Create(dn),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B04_Accumulate(Scene):
 def construct(self):
  d=DUR.get('B04',14); self.add(bg(),ttl('WEAK MEANS SLOW — NOT SHALLOW')); steps=VGroup(*[Arrow(ORIGIN,RIGHT*.75,color=TEAL,buff=0).shift(LEFT*4+RIGHT*i*.85+UP*np.sin(i*.5)*.25) for i in range(10)]); eq=Text('small coherent rotations accumulate',font=SERIF,font_size=36,color=CRIMSON).move_to(DOWN*2); self.play(*[GrowArrow(x) for x in steps],FadeIn(eq),run_time=1.3); self.wait(max(.1,d-1.3))
class B05_Duration(Scene):
 def construct(self):
  d=DUR.get('B05',12); self.add(bg(),ttl('PULSE DURATION SETS THE ROTATION ANGLE')); short=sphere(35).scale(.65).shift(LEFT*3); full=sphere(180).scale(.65).shift(RIGHT*3); labs=VGroup(Text('short pulse: small move',font=MONO,font_size=26,color=SLATE).move_to(LEFT*3+DOWN*2.5),Text('pi-pulse: full flip',font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*3+DOWN*2.5)); self.play(Create(short),Create(full),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B06_Basis(Scene):
 def construct(self):
  d=DUR.get('B06',14); self.add(bg(),ttl('UP IS A SUPERPOSITION OF THE DRIVE EIGENSTATES')); eqs=VGroup(Text('|up> = (|+x> + |-x>) / sqrt(2)',font=MONO,font_size=38,color=INK),Text('|+x>',font=MONO,font_size=34,color=TEAL),Text('|-x>',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B07_Phase(Scene):
 def construct(self):
  d=DUR.get('B07',13); self.add(bg(),ttl('THE DRESSED-STATE PHASE GAP GROWS TO pi')); c1=Circle(radius=1.5,color=TEAL).shift(LEFT*3); c2=Circle(radius=1.5,color=CRIMSON).shift(RIGHT*3); h1=Arrow(c1.get_center(),c1.get_center()+UP*1.2,color=TEAL,buff=0); h2=Arrow(c2.get_center(),c2.get_center()+DOWN*1.2,color=CRIMSON,buff=0); lab=Text('Delta phi = pi at the flip',font=MONO,font_size=34,color=INK).move_to(DOWN*2.7); self.play(Create(c1),Create(c2),GrowArrow(h1),GrowArrow(h2),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B08_Interference(Scene):
 def construct(self):
  d=DUR.get('B08',14); self.add(bg(),ttl('INTERFERENCE SWAPS THE OUTPUT')); left=VGroup(Arrow(ORIGIN,RIGHT*1.7,color=TEAL,buff=0),Arrow(ORIGIN,LEFT*1.7,color=CRIMSON,buff=0)).shift(LEFT*3); right=VGroup(Arrow(ORIGIN,UP*1.7,color=TEAL,buff=0),Arrow(ORIGIN,UP*1.7,color=CRIMSON,buff=0)).shift(RIGHT*3); labs=VGroup(Text('up cancels',font=MONO,font_size=28,color=CRIMSON).move_to(LEFT*3+DOWN*2),Text('down adds',font=MONO,font_size=28,color=TEAL).move_to(RIGHT*3+DOWN*2)); self.play(*[GrowArrow(x) for x in [*left,*right]],FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Scope(Scene):
 def construct(self):
  d=DUR.get('B09',16); self.add(bg(),ttl('FULL INVERSION HAS CONDITIONS')); good=VGroup(Text('ON RESONANCE',font=DISPLAY,font_size=32,color=TEAL),Text('coherent',font=MONO,font_size=29,color=TEAL),Text('100% possible',font=MONO,font_size=29,color=TEAL)).arrange(DOWN,buff=.5).shift(LEFT*3); bad=VGroup(Text('DETUNED / DECOHERENT',font=DISPLAY,font_size=30,color=CRIMSON),Text('tilted axis / lost phase',font=MONO,font_size=27,color=CRIMSON),Text('reduced transfer',font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.5).shift(RIGHT*3); self.play(FadeIn(good,bad),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',18); self.add(bg(),ttl('YOUR TURN: f_R = 20 kHz')); eqs=VGroup(Text('t_pi = 1 / (2 f_R)',font=MONO,font_size=40,color=INK),Text('= 25 microseconds',font=MONO,font_size=42,color=CRIMSON),Text('another 25 microseconds -> back to up',font=MONO,font_size=31,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',16); self.add(bg(),Text('WHY A SPIN FLIPS WHEN YOU WHISPER',font=DISPLAY,font_size=36,color=CRIMSON).move_to(UP*2.3),Text('resonant coherent drive',font=MONO,font_size=35,color=TEAL).move_to(UP*.8),Text('relative phase accumulates',font=MONO,font_size=35,color=INK).move_to(DOWN*.4),Text('strength sets speed · coherence sets reach',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
