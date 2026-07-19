import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)

class B02_EnergyFloor(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("TRIAL ENERGIES DESCEND — NEVER THROUGH THE FLOOR")); floor=Line(LEFT*6,RIGHT*6,color=CRIMSON,stroke_width=6).move_to(DOWN*2.2); fl=Text("exact E0",font=MONO,font_size=24,color=CRIMSON).next_to(floor,DOWN); ys=[2.0,1.0,.1,-1.0]; dots=VGroup(*[Dot(np.array([-4+i*2.6,y,0]),radius=.22,color=TEAL) for i,y in enumerate(ys)]); labs=VGroup(*[Text(f"trial {i+1}",font=MONO,font_size=18,color=INK).next_to(dot,UP) for i,dot in enumerate(dots)]); arrows=VGroup(*[Arrow(dot.get_center(),np.array([dot.get_x(),-1.85,0]),color=TEAL,buff=.3) for dot in dots]); self.play(Create(floor),FadeIn(fl),run_time=.6); self.play(FadeIn(dots),FadeIn(labs),GrowFromCenter(arrows),run_time=1.1); self.wait(max(.1,d-1.7))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",8); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=22,color=SLATE).move_to(UP*2.4),Text("Why can a wrong wave function err high,\nbut never below the true ground energy?",font=SERIF,font_size=37,color=INK,line_spacing=1.3)); self.wait(d)

class B04_Decomposition(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("EXPAND THE TRIAL STATE IN EXACT ENERGY STATES")); psi=Text("|psi> = c0|0> + c1|1> + c2|2> + ...",font=MONO,font_size=36,color=INK).move_to(UP*1.4); bars=VGroup(*[Rectangle(width=w*4,height=.65,color=c,fill_color=c,fill_opacity=.35) for w,c in [(.55,TEAL),(.28,GOLD),(.17,CRIMSON)]]).arrange(DOWN,buff=.35).move_to(DOWN*.7); labs=VGroup(Text("|c0|^2",font=MONO,font_size=20,color=INK).next_to(bars[0],LEFT),Text("|c1|^2",font=MONO,font_size=20,color=INK).next_to(bars[1],LEFT),Text("|c2|^2",font=MONO,font_size=20,color=INK).next_to(bars[2],LEFT)); norm=Text("sum |c_n|^2 = 1",font=MONO,font_size=26,color=INK).move_to(DOWN*2.7); self.play(FadeIn(psi),run_time=.7); self.play(GrowFromEdge(bars,LEFT),FadeIn(labs),FadeIn(norm),run_time=1.1); self.wait(max(.1,d-1.8))

class B05_WeightedAverage(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("EXPECTED ENERGY = A WEIGHTED AVERAGE")); eq=Text("<H> = sum |c_n|^2 E_n",font=MONO,font_size=43,color=TEAL).move_to(UP*1.7); terms=VGroup(Text("nonnegative weights",font=DISPLAY,font_size=25,color=INK),Text("x",font=DISPLAY,font_size=28,color=CRIMSON),Text("exact energies",font=DISPLAY,font_size=25,color=INK)).arrange(RIGHT,buff=.6); sum1=Text("weights sum to one",font=MONO,font_size=25,color=INK).move_to(DOWN*1.4); self.play(FadeIn(eq),run_time=.8); self.play(FadeIn(terms),FadeIn(sum1),run_time=.8); self.wait(max(.1,d-1.6))

class B06_MinimumCard(Scene):
 def construct(self):
  d=DUR.get("B06",5); self.add(bg(),Text("ONE FACT DOES THE WORK",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*2),Text("weighted average",font=SERIF,font_size=36,color=INK).move_to(UP*.7),Text("≥",font=MONO,font_size=45,color=CRIMSON),Text("smallest entry",font=SERIF,font_size=41,color=TEAL).move_to(DOWN*1.2)); self.wait(d)

class B07_NonnegativeDifference(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("SUBTRACT THE GROUND ENERGY")); e1=Text("<H> - E0 = sum |c_n|^2 (E_n - E0)",font=MONO,font_size=35,color=INK).move_to(UP*1.3); e2=Text("|c_n|^2 >= 0",font=MONO,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*.3); e3=Text("E_n - E0 >= 0",font=MONO,font_size=29,color=TEAL).move_to(RIGHT*3+DOWN*.3); result=Text("therefore  <H> - E0 >= 0",font=MONO,font_size=35,color=CRIMSON).move_to(DOWN*2); self.play(FadeIn(e1),run_time=.8); self.play(FadeIn(e2),FadeIn(e3),run_time=.7); self.play(FadeIn(result),run_time=.7); self.wait(max(.1,d-2.2))

class B08_Equality(Scene):
 def construct(self):
  d=DUR.get("B08",9); self.add(bg(),ttl("WHEN DOES EQUALITY HOLD?")); ground=Rectangle(width=5,height=1.2,color=TEAL,fill_color=TEAL,fill_opacity=.12).move_to(LEFT*3.4); excited=Rectangle(width=5,height=1.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.1).move_to(RIGHT*3.4); gl=Text("ground-energy space",font=DISPLAY,font_size=24,color=TEAL).move_to(LEFT*3.4); el=Text("excited component",font=DISPLAY,font_size=24,color=CRIMSON).move_to(RIGHT*3.4); zero=Text("zero excess",font=MONO,font_size=23,color=TEAL).move_to(LEFT*3.4+DOWN*1.4); lift=Text("pushes average up",font=MONO,font_size=23,color=CRIMSON).move_to(RIGHT*3.4+DOWN*1.4); self.play(GrowFromCenter(ground),GrowFromCenter(excited),FadeIn(gl),FadeIn(el),run_time=.9); self.play(FadeIn(zero),FadeIn(lift),run_time=.6); self.wait(max(.1,d-1.5))

class B09_HeliumTrial(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("HELIUM: ONE ADJUSTABLE EFFECTIVE CHARGE")); nucleus=Dot(radius=.45,color=CRIMSON); e1=Dot(LEFT*3,radius=.28,color=TEAL); e2=Dot(RIGHT*3,radius=.28,color=TEAL); or1=Circle(radius=3,color=SLATE).stretch(.55,1); or2=Circle(radius=3,color=SLATE).stretch(.55,1).rotate(PI/2); z=Text("Z* controls orbital size",font=MONO,font_size=28,color=INK).move_to(DOWN*2.8); note=Text("simple product trial",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*2.7); self.play(FadeIn(nucleus),Create(or1),Create(or2),FadeIn(e1),FadeIn(e2),run_time=1); self.play(FadeIn(z),FadeIn(note),run_time=.6); self.wait(max(.1,d-1.6))

class B10_Parabola(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg(),ttl("MINIMIZE THE ONE-PARAMETER ENERGY")); ax=Axes(x_range=[1,2.4,.2],y_range=[-2.9,-2.3,.1],x_length=9.5,y_length=5,tips=True).move_to(DOWN*.25); f=lambda z:z*z-27*z/8; curve=ax.plot(f,x_range=[1,2.4],color=TEAL,stroke_width=5); z0=27/16; dot=Dot(ax.c2p(z0,f(z0)),radius=.16,color=CRIMSON); eq=Text("E(Z*) = Z*² − (27/8)Z*",font=MONO,font_size=24,color=INK).move_to(RIGHT*4.4+UP*2.2); lab=Text("minimum: Z* = 27/16 = 1.6875",font=MONO,font_size=22,color=CRIMSON).move_to(RIGHT*4.1+DOWN*2.6); self.play(Create(ax),run_time=.7); self.play(Create(curve),FadeIn(dot),FadeIn(eq),FadeIn(lab),run_time=1.2); self.wait(max(.1,d-1.9))

class B11_HeliumNumbers(Scene):
 def construct(self):
  d=DUR.get("B11",11); self.add(bg(),ttl("ALL TRIAL VALUES STAY ABOVE THE EXACT FLOOR")); floor=Line(LEFT*6,RIGHT*6,color=CRIMSON,stroke_width=5).move_to(DOWN*2); exact=Text("exact nonrelativistic: −79.01 eV",font=MONO,font_size=23,color=CRIMSON).next_to(floor,DOWN); p1=Dot(LEFT*3.5+UP*1.7,radius=.22,color=SLATE); p2=Dot(RIGHT*1+UP*.1,radius=.22,color=TEAL); l1=Text("Z*=2\n−74.83 eV",font=MONO,font_size=22,color=SLATE,line_spacing=1).next_to(p1,UP); l2=Text("optimized Z*=1.6875\n−77.49 eV",font=MONO,font_size=22,color=TEAL,line_spacing=1).next_to(p2,UP); a1=Arrow(p1.get_center(),np.array([p1.get_x(),-1.65,0]),color=SLATE,buff=.3); a2=Arrow(p2.get_center(),np.array([p2.get_x(),-1.65,0]),color=TEAL,buff=.3); self.play(Create(floor),FadeIn(exact),run_time=.6); self.play(FadeIn(p1),FadeIn(p2),FadeIn(l1),FadeIn(l2),GrowArrow(a1),GrowArrow(a2),run_time=1.1); self.wait(max(.1,d-1.7))

class B12_Ceiling(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("OPTIMIZATION TIGHTENS THE CEILING",font=DISPLAY,font_size=26,color=SLATE).move_to(UP*2.4)); floor=Line(LEFT*5.5,RIGHT*5.5,color=CRIMSON,stroke_width=5).move_to(DOWN*2); bars=VGroup(*[Line(LEFT*2,RIGHT*2,color=TEAL,stroke_width=6).move_to(UP*y) for y in [1.2,.3,-.6,-1.3]]); arrows=VGroup(*[Arrow(bars[i].get_center()+RIGHT*2.4,bars[i+1].get_center()+RIGHT*2.4,color=TEAL,buff=.15) for i in range(3)]); self.play(Create(floor),FadeIn(bars),FadeIn(arrows),run_time=1); self.add(Text("approach E₀ from above",font=MONO,font_size=25,color=INK).next_to(floor,DOWN)); self.wait(max(.1,d-1))
