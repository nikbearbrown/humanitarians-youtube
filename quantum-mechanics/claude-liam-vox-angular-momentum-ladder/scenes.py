import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def ladder(labels):
 r=VGroup(*[Line(LEFT*1.7,RIGHT*1.7,color=INK).shift(UP*(i-(len(labels)-1)/2)*.8) for i in range(len(labels))])
 l=VGroup(*[Text(s,font=MONO,font_size=26,color=CRIMSON if i in [0,len(labels)-1] else INK).next_to(r[i],LEFT,buff=.4) for i,s in enumerate(labels)])
 return VGroup(r,l)
class B02_Multiplet(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('ONE j · MANY m PROJECTIONS')); rows=VGroup(Text('L^2 |j,m> = hbar^2 j(j+1) |j,m>',font=MONO,font_size=32,color=TEAL),Text('Lz |j,m> = hbar m |j,m>',font=MONO,font_size=34,color=CRIMSON),Text('j fixes magnitude · m labels projection',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B03_Shift(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('LADDER OPERATORS MOVE ONE RUNG')); lad=ladder(['m+2','m+1','m','m-1','m-2']); token=Dot(lad[0][2].get_center(),radius=.18,color=CRIMSON); up=Arrow(RIGHT*2+DOWN*.6,RIGHT*2+UP*.6,color=TEAL,buff=0); down=Arrow(RIGHT*3+UP*.6,RIGHT*3+DOWN*.6,color=CRIMSON,buff=0); labs=VGroup(Text('L+',font=MONO,font_size=28,color=TEAL).next_to(up,RIGHT),Text('L-',font=MONO,font_size=28,color=CRIMSON).next_to(down,RIGHT)); self.play(Create(lad),FadeIn(token),GrowArrow(up),GrowArrow(down),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Bound(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('WHY CAN THE LADDER NOT CONTINUE FOREVER?')); cone=VGroup(Circle(radius=2.2,color=SLATE),Arrow(ORIGIN,RIGHT*1.5+UP*1.3,color=CRIMSON,buff=0),DashedLine(DOWN*2.4,UP*2.4,color=INK)); eq=Text('every state norm squared >= 0',font=MONO,font_size=37,color=TEAL).move_to(DOWN*2.8); self.play(Create(cone),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B05_Norms(Scene):
 def construct(self):
  d=DUR.get('B05',10); self.add(bg(),ttl('THE TWO NONNEGATIVE NORM FACTORS')); rows=VGroup(Text('||L+|j,m>||^2 proportional to',font=MONO,font_size=29,color=TEAL),Text('j(j+1) - m(m+1) >= 0',font=MONO,font_size=38,color=TEAL),Text('||L-|j,m>||^2 proportional to',font=MONO,font_size=29,color=CRIMSON),Text('j(j+1) - m(m-1) >= 0',font=MONO,font_size=38,color=CRIMSON)).arrange(DOWN,buff=.4); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B06_Top(Scene):
 def construct(self):
  d=DUR.get('B06',9); self.add(bg(),ttl('TOP RUNG: RAISING ANNIHILATES THE STATE')); lad=ladder(['m=j','j-1','j-2','...']); lad.shift(DOWN*.2); stop=Cross(Dot(lad[0][0].get_center()+UP*.8),color=CRIMSON); eq=Text('L+ |j,j> = 0',font=MONO,font_size=39,color=TEAL).move_to(RIGHT*3); self.play(Create(lad),Create(stop),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B07_Bottom(Scene):
 def construct(self):
  d=DUR.get('B07',9); self.add(bg(),ttl('BOTTOM RUNG: LOWERING ANNIHILATES THE STATE')); lad=ladder(['...','-j+2','-j+1','m=-j']); lad.shift(DOWN*.2); stop=Cross(Dot(lad[0][-1].get_center()+DOWN*.8),color=CRIMSON); eq=Text('L- |j,-j> = 0',font=MONO,font_size=39,color=TEAL).move_to(RIGHT*3); count=Text('2j + 1 rungs',font=SERIF,font_size=31,color=INK).move_to(DOWN*3); self.play(Create(lad),Create(stop),FadeIn(eq,count),run_time=1); self.wait(max(.1,d-1))
class B08_Sequence(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('TWO j MUST BE AN INTEGER')); seq=VGroup(*[Text(s,font=MONO,font_size=34,color=CRIMSON if '/' in s else TEAL) for s in ['0','1/2','1','3/2','2','...']]).arrange(RIGHT,buff=.7); eq=Text('unit steps from -j to +j: 2j',font=MONO,font_size=32,color=INK).move_to(DOWN*2); self.play(FadeIn(seq,eq),run_time=1); self.wait(max(.1,d-1))
class B09_Scope(Scene):
 def construct(self):
  d=DUR.get('B09',10); self.add(bg(),ttl('LADDER ALGEBRA VERSUS ORBITAL BOUNDARY CONDITIONS')); left=VGroup(Text('GENERAL j',font=DISPLAY,font_size=31,color=TEAL),Text('integer or half-integer',font=MONO,font_size=29,color=TEAL),Text('spin included',font=SERIF,font_size=28,color=TEAL)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('ORBITAL ell',font=DISPLAY,font_size=31,color=CRIMSON),Text('0, 1, 2, ...',font=MONO,font_size=30,color=CRIMSON),Text('single-valued spatial states',font=SERIF,font_size=27,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B10_Magnitude(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('EVERY RUNG SHARES ONE TOTAL MAGNITUDE')); eq=Text('|L| = hbar sqrt(j(j+1))',font=MONO,font_size=44,color=CRIMSON).move_to(UP*1.7); dots=VGroup(*[Dot(np.array([x,-.4,0]),radius=.18,color=TEAL) for x in [-4,-2,0,2,4]]); labels=Text('different m · same j',font=SERIF,font_size=33,color=INK).move_to(DOWN*2); self.play(FadeIn(eq,dots,labels),run_time=1); self.wait(max(.1,d-1))
class B11_Ell2(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('EXAMPLE: ORBITAL ell = 2')); lad=ladder(['m=+2','m=+1','m=0','m=-1','m=-2']); lad.shift(LEFT*2); eq=VGroup(Text('5 rungs',font=MONO,font_size=32,color=TEAL),Text('|L| = hbar sqrt(6)',font=MONO,font_size=32,color=CRIMSON)).arrange(DOWN,buff=.7).shift(RIGHT*3); self.play(Create(lad),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B12_Caveat(Scene):
 def construct(self):
  d=DUR.get('B12',9); self.add(bg(),ttl('A LADDER OF EIGENSTATES — NOT HIDDEN TILTS')); left=VGroup(*[Dot(np.array([-3,y,0]),radius=.15,color=TEAL) for y in [-1.5,-.5,.5,1.5]]); right=VGroup(Text('superposition',font=MONO,font_size=31,color=CRIMSON),Text('measurement -> one allowed m',font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.7).shift(RIGHT*2.5); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN: j = 3/2')); lad=ladder(['m=+3/2','m=+1/2','m=-1/2','m=-3/2']); eq=Text('2j + 1 = 4 states',font=MONO,font_size=36,color=CRIMSON).move_to(RIGHT*3); self.play(Create(lad),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',9); self.add(bg(),Text('WHY ANGULAR MOMENTUM COMES IN A LADDER',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('L+ and L- shift m by one',font=MONO,font_size=33,color=TEAL).move_to(UP*.8),Text('nonnegative norms force endpoints',font=MONO,font_size=32,color=INK).move_to(DOWN*.4),Text('j integer/half · orbital ell integer',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
