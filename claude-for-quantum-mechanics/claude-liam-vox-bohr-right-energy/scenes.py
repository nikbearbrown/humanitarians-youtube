import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def lev(y,w=5.5,col=INK): return Line(LEFT*w/2,RIGHT*w/2,color=col,stroke_width=4).move_to(UP*y)

class B02_SameSpectrum(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg(),ttl("SAME IDEAL HYDROGEN SPECTRUM")); a=Text("BOHR",font=DISPLAY,font_size=27,color=CRIMSON).move_to(LEFT*3.7+UP*1.6); b=Text("SCHRODINGER",font=DISPLAY,font_size=27,color=TEAL).move_to(RIGHT*3.7+UP*1.6); f1=Text("E_n = -13.6 / n^2 eV",font=MONO,font_size=31,color=INK).move_to(LEFT*3.7); f2=f1.copy().move_to(RIGHT*3.7); divider=Line(UP*2.3,DOWN*2.2,color=SLATE); note=Text("ideal, nonrelativistic Coulomb problem",font=SERIF,font_size=25,color=SLATE).move_to(DOWN*2.8); self.play(FadeIn(a,b),Create(divider),run_time=.6); self.play(Write(f1),Write(f2),FadeIn(note),run_time=1); self.wait(max(.1,d-1.6))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",7); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("How can a wrong orbit\nproduce the right energy ladder?",font=SERIF,font_size=42,color=INK,line_spacing=1.25)); self.wait(d)

class B04_BohrScaling(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("BOHR'S CIRCULAR-ORBIT SCALING")); nucleus=Dot(LEFT*3.8,radius=.22,color=CRIMSON); rings=VGroup(*[Circle(radius=r,color=TEAL,stroke_opacity=.85) for r in [.65,1.25,1.9]]).move_to(nucleus); dots=VGroup(*[Dot(nucleus.get_center()+RIGHT*r,radius=.14,color=TEAL) for r in [.65,1.25,1.9]]); rules=VGroup(Text("Coulomb attraction",font=SERIF,font_size=27,color=INK),Text("+  L = n hbar",font=MONO,font_size=28,color=CRIMSON),Text("=>  r_n proportional to n^2",font=MONO,font_size=26,color=TEAL),Text("=>  E_n proportional to -1/n^2",font=MONO,font_size=26,color=TEAL)).arrange(DOWN,aligned_edge=LEFT,buff=.42).move_to(RIGHT*3.2); self.play(FadeIn(nucleus),Create(rings),FadeIn(dots),run_time=.9); self.play(FadeIn(rules),run_time=.9); self.wait(max(.1,d-1.8))

class B05_NoTrajectory(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("QUANTUM STATES ARE NOT LITTLE PLANETARY ORBITS")); left=VGroup(*[Circle(radius=r,color=TEAL,stroke_opacity=.15) for r in np.linspace(.25,1.5,8)]).move_to(LEFT*3.6); lobes=VGroup(Ellipse(width=1.6,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.18),Ellipse(width=1.6,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.18).rotate(PI/2)).move_to(RIGHT*3.4); labs=VGroup(Text("s-like probability cloud",font=MONO,font_size=22,color=INK).move_to(LEFT*3.6+DOWN*2.1),Text("p-like angular structure",font=MONO,font_size=22,color=INK).move_to(RIGHT*3.4+DOWN*2.1),Text("stationary state: no definite trajectory",font=SERIF,font_size=29,color=CRIMSON).move_to(DOWN*3)); self.play(FadeIn(left),FadeIn(lobes),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))

class B06_CoulombKey(Scene):
 def construct(self):
  d=DUR.get("B06",7); self.add(bg(),Text("THE SURVIVING ANSWER COMES FROM",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*1.8),Text("the special 1 / r Coulomb problem",font=SERIF,font_size=43,color=TEAL),Text("not from a literal orbit",font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*1.5)); self.wait(d)

class B07_HiddenSymmetry(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("ENERGY DEPENDS ONLY ON n")); ys=[2.1,.8,-.5,-1.8]; levels=VGroup(*[lev(y,6,TEAL) for y in ys]); labels=VGroup(*[Text(f"n = {i+1}",font=MONO,font_size=23,color=INK).next_to(levels[i],LEFT) for i in range(4)]); tags=VGroup(Text("many l and m states",font=SERIF,font_size=25,color=INK).move_to(RIGHT*4+UP*.8),Text("same energy within one shell",font=SERIF,font_size=25,color=INK).move_to(RIGHT*4+DOWN*.2),Text("extra conserved Runge-Lenz structure",font=MONO,font_size=23,color=CRIMSON).move_to(DOWN*3)); self.play(Create(levels),FadeIn(labels),run_time=.8); self.play(FadeIn(tags),run_time=.9); self.wait(max(.1,d-1.7))

class B08_N2Degeneracy(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg(),ttl("THE IDEAL n = 2 SHELL")); y=.4; line=lev(y,10,TEAL); states=VGroup(*[Dot(np.array([x,y,0]),radius=.2,color=c) for x,c in zip([-4,-1.3,1.3,4],[CRIMSON,TEAL,TEAL,TEAL])]); labs=VGroup(*[Text(s,font=MONO,font_size=24,color=INK).move_to(np.array([x,y-1,0])) for x,s in zip([-4,-1.3,1.3,4],["2s","2p m=-1","2p m=0","2p m=+1"])]); en=Text("all E = -3.4 eV  (ignoring spin)",font=MONO,font_size=28,color=CRIMSON).move_to(UP*2); self.play(Create(line),FadeIn(states),run_time=.7); self.play(FadeIn(labs),FadeIn(en),run_time=.9); self.wait(max(.1,d-1.6))

class B09_ClosestAnalogue(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("ONE BOHR ORBIT CANNOT REPRESENT A WHOLE SHELL")); orbit=Circle(radius=1.4,color=CRIMSON).move_to(LEFT*3.7); cloud=VGroup(*[Circle(radius=r,color=TEAL,stroke_opacity=.1) for r in np.linspace(.5,1.8,9)]).move_to(RIGHT*3.7); arrow=Arrow(LEFT*1.7,RIGHT*1.7,color=SLATE,buff=.2); labs=VGroup(Text("Bohr circular orbit",font=MONO,font_size=23,color=INK).move_to(LEFT*3.7+DOWN*2.2),Text("closest semiclassical match:\nhigh-l circular state",font=MONO,font_size=23,color=INK,line_spacing=1.15).move_to(RIGHT*3.7+DOWN*2.3),Text("not every s, p, ... state at that n",font=SERIF,font_size=27,color=CRIMSON).move_to(DOWN*3.25)); self.play(Create(orbit),GrowArrow(arrow),FadeIn(cloud),run_time=.9); self.play(FadeIn(labs),run_time=.8); self.wait(max(.1,d-1.7))

class B10_BreakSymmetry(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("CHANGE THE POTENTIAL, AND THE DEGENERACY SPLITS")); common=lev(1.5,4,TEAL).move_to(LEFT*3.8+UP*.4); split=VGroup(*[Line(LEFT*1.4,RIGHT*1.4,color=c,stroke_width=4).move_to(np.array([3.8,y,0])) for y,c in zip([2,.6,-.8],[CRIMSON,TEAL,SLATE])]); arr=Arrow(LEFT*1.3,RIGHT*1.3,color=INK); labs=VGroup(Text("pure 1/r",font=MONO,font_size=25,color=INK).move_to(LEFT*3.8+DOWN*1.2),Text("perturbation or\nelectron interactions",font=MONO,font_size=23,color=INK,line_spacing=1.1).move_to(RIGHT*3.8+DOWN*2),Text("same n",font=SERIF,font_size=24,color=TEAL).move_to(LEFT*3.8+UP*2.3),Text("different energies",font=SERIF,font_size=24,color=CRIMSON).move_to(RIGHT*3.8+UP*2.8)); self.play(Create(common),GrowArrow(arr),Create(split),run_time=1); self.play(FadeIn(labs),run_time=.8); self.wait(max(.1,d-1.8))

class B11_RealCorrections(Scene):
 def construct(self):
  d=DUR.get("B11",10)
  self.add(bg(),ttl("REAL HYDROGEN HAS SMALL CORRECTIONS"))
  base=lev(1.7,7,SLATE)
  fine=VGroup(*[Line(LEFT*3,RIGHT*3,color=c,stroke_width=4).move_to(UP*y) for y,c in zip([.7,.25,-.25,-.8],[TEAL,CRIMSON,TEAL,CRIMSON])])
  labels=VGroup(
   Text("ideal Coulomb level",font=MONO,font_size=21,color=INK).move_to(RIGHT*4.7+UP*1.7),
   Text("fine structure",font=MONO,font_size=22,color=INK).move_to(LEFT*4.2),
   Text("recoil",font=MONO,font_size=22,color=INK).move_to(LEFT*4.2+DOWN*.55),
   Text("Lamb shift",font=MONO,font_size=22,color=INK).move_to(LEFT*4.2+DOWN*1.1),
   Text("spacing exaggerated",font=SERIF,font_size=23,color=SLATE).move_to(DOWN*2.8))
  self.play(Create(base),run_time=.5)
  self.play(TransformFromCopy(base,fine),FadeIn(labels),run_time=1.1)
  self.wait(max(.1,d-1.6))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("BOHR FOUND THE RIGHT SCALING",font=DISPLAY,font_size=27,color=SLATE).move_to(UP*2.4),Text("because hydrogen's 1 / r symmetry is special",font=SERIF,font_size=37,color=TEAL).move_to(UP*.7),Text("THE SPECTRUM SURVIVED",font=DISPLAY,font_size=39,color=INK).move_to(DOWN*.7),Text("the orbit did not",font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*2)); self.wait(d)
