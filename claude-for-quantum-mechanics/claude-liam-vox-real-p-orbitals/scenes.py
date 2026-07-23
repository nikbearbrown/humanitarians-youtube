import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def dumbbell(axis='x'):
 if axis=='x':
  a=Ellipse(width=3.3,height=1.8,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).shift(LEFT*1.65); b=Ellipse(width=3.3,height=1.8,color=TEAL,fill_color=TEAL,fill_opacity=.15).shift(RIGHT*1.65)
 else:
  a=Ellipse(width=1.8,height=3.3,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).shift(UP*1.65); b=Ellipse(width=1.8,height=3.3,color=TEAL,fill_color=TEAL,fill_opacity=.15).shift(DOWN*1.65)
 return VGroup(a,b,Dot(ORIGIN,radius=.12,color=INK))
class B02_Subspace(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('THE l = 1 SUBSPACE HAS THREE BASIS STATES')); boxes=VGroup(*[RoundedRectangle(width=2.4,height=1.5,corner_radius=.15,color=c).set_fill(c,.1) for c in [CRIMSON,INK,TEAL]]).arrange(RIGHT,buff=.7); labs=VGroup(*[Text(s,font=MONO,font_size=32,color=c).move_to(b) for s,c,b in zip(['m = -1','m = 0','m = +1'],[CRIMSON,INK,TEAL],boxes)]); eq=Text('L^2 = 2 hbar^2 for every combination',font=MONO,font_size=32,color=INK).move_to(DOWN*2.3); self.play(Create(boxes),FadeIn(labs,eq),run_time=1); self.wait(max(.1,d-1))
class B03_Winding(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('OPPOSITE PHASE WINDING · OPPOSITE Lz')); c1=Circle(radius=1.5,color=TEAL).shift(LEFT*3); c2=Circle(radius=1.5,color=CRIMSON).shift(RIGHT*3); a1=CurvedArrow(LEFT*3+DOWN*1.2,LEFT*3+UP*1.2,color=TEAL); a2=CurvedArrow(RIGHT*3+UP*1.2,RIGHT*3+DOWN*1.2,color=CRIMSON); labs=VGroup(Text('m = +1 -> +hbar',font=MONO,font_size=28,color=TEAL).move_to(LEFT*3+DOWN*2.4),Text('m = -1 -> -hbar',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*3+DOWN*2.4)); self.play(Create(c1),Create(c2),Create(a1),Create(a2),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Density(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('THE TWO DENSITIES LOOK THE SAME')); t1=VGroup(Ellipse(width=4,height=1.4,color=TEAL),Ellipse(width=2,height=.65,color=TEAL)).shift(LEFT*3); t2=VGroup(Ellipse(width=4,height=1.4,color=CRIMSON),Ellipse(width=2,height=.65,color=CRIMSON)).shift(RIGHT*3); labs=VGroup(Text('|Y+1|^2',font=MONO,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*2),Text('|Y-1|^2',font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*2),Text('phase carries the difference',font=SERIF,font_size=31,color=INK).move_to(DOWN*3)); self.play(Create(t1),Create(t2),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B05_Morph(Scene):
 def construct(self):
  d=DUR.get('B05',10); self.add(bg(),ttl('OPPOSITE-m STATES COMBINE INTO REAL DUMBBELLS')); rings=VGroup(Circle(radius=1.2,color=TEAL).shift(LEFT*4),Circle(radius=1.2,color=CRIMSON).shift(LEFT*1.5)); plus=Text('+ relative phase',font=MONO,font_size=27,color=INK).move_to(UP*2); db=dumbbell('x').scale(.65).shift(RIGHT*3); arrow=Arrow(LEFT*.2,RIGHT*1.3,color=INK,buff=0); self.play(Create(rings),FadeIn(plus),GrowArrow(arrow),Create(db),run_time=1.2); self.wait(max(.1,d-1.2))
class B06_Node(Scene):
 def construct(self):
  d=DUR.get('B06',9); self.add(bg(),ttl('p_x: ORIENTED LOBES · y-z NODAL PLANE')); db=dumbbell('x'); plane=DashedLine(DOWN*2.7,UP*2.7,color=INK); labs=VGroup(Text('+ phase',font=MONO,font_size=26,color=TEAL).move_to(RIGHT*3),Text('- phase',font=MONO,font_size=26,color=CRIMSON).move_to(LEFT*3),Text('sign is not charge',font=SERIF,font_size=29,color=INK).move_to(DOWN*2.8)); self.play(Create(db),Create(plane),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B07_Outcomes(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('p_x IS NOT AN Lz EIGENSTATE')); db=dumbbell('x').scale(.55).shift(LEFT*3); split=VGroup(Arrow(ORIGIN,RIGHT*2+UP*1,color=TEAL,buff=0),Arrow(ORIGIN,RIGHT*2+DOWN*1,color=CRIMSON,buff=0)).shift(RIGHT*.5); labs=VGroup(Text('+hbar   50%',font=MONO,font_size=29,color=TEAL).move_to(RIGHT*4+UP*1),Text('-hbar   50%',font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*4+DOWN*1),Text('<Lz> = 0',font=MONO,font_size=31,color=INK).move_to(DOWN*2.5)); self.play(Create(db),*[GrowArrow(x) for x in split],FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B08_Variance(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('ZERO MEAN DOES NOT MEAN ZERO ANGULAR MOMENTUM')); rows=VGroup(Text('<Lz> = 0',font=MONO,font_size=38,color=SLATE),Text('Var(Lz) = hbar^2',font=MONO,font_size=38,color=CRIMSON),Text('L^2 = 2 hbar^2  (sharp)',font=MONO,font_size=38,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B09_Bases(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('SAME SUBSPACE · DIFFERENT CONVENIENT BASES')); left=VGroup(Text('COMPLEX m BASIS',font=DISPLAY,font_size=30,color=TEAL),Text('sharp Lz',font=MONO,font_size=30,color=TEAL),Text('phase winding',font=SERIF,font_size=28,color=TEAL)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('REAL CARTESIAN BASIS',font=DISPLAY,font_size=28,color=CRIMSON),Text('oriented p_x, p_y',font=MONO,font_size=30,color=CRIMSON),Text('bond symmetry',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B10_Context(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('CONTEXT CHOOSES THE BASIS')); mol=VGroup(Dot(LEFT*1.5,color=INK),Dot(RIGHT*1.5,color=INK),Line(LEFT*1.5,RIGHT*1.5,color=CRIMSON),Text('molecular axis',font=MONO,font_size=28,color=CRIMSON).move_to(DOWN*1.2)).shift(LEFT*3); field=VGroup(Arrow(DOWN*1.5,UP*1.5,color=TEAL,buff=0),Text('B along z',font=MONO,font_size=28,color=TEAL).move_to(DOWN*2)).shift(RIGHT*3); self.play(FadeIn(mol),Create(field),run_time=1); self.wait(max(.1,d-1))
class B11_Caveat(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('THE TITLE IS A DELIBERATE OVERSTATEMENT')); rows=VGroup(Text('real p orbitals ARE valid quantum states',font=MONO,font_size=33,color=TEAL),Text('sharp L^2 · not sharp Lz',font=MONO,font_size=33,color=CRIMSON),Text('many-electron orbitals are model-dependent objects',font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B12_Example(Scene):
 def construct(self):
  d=DUR.get('B12',9); self.add(bg(),ttl('WORKED RESULT: MEASURE Lz IN p_x')); rows=VGroup(Text('+hbar with probability 1/2',font=MONO,font_size=36,color=TEAL),Text('-hbar with probability 1/2',font=MONO,font_size=36,color=CRIMSON),Text('average 0 · every result nonzero',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN: NOW PREPARE p_y')); db=dumbbell('y').scale(.55).shift(LEFT*3); rows=VGroup(Text('Lz = +hbar or -hbar',font=MONO,font_size=33,color=INK),Text('each with probability 1/2',font=MONO,font_size=31,color=TEAL),Text('relative phase rotates p_x into p_y',font=SERIF,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.6).shift(RIGHT*2.6); self.play(Create(db),FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',9); self.add(bg(),Text('WHY CHEMISTRY DRAWS REAL DUMBBELLS',font=DISPLAY,font_size=35,color=CRIMSON).move_to(UP*2.3),Text('opposite-m states combine',font=MONO,font_size=34,color=TEAL).move_to(UP*.8),Text('L^2 sharp · Lz not sharp',font=MONO,font_size=34,color=INK).move_to(DOWN*.4),Text('same l=1 subspace · basis fits the question',font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
