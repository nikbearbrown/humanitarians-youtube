import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def wave(center=0,phase=0,col=CRIMSON):
 xs=np.linspace(-6,6,500); pts=[]
 for x in xs:
  env=np.exp(-.5*((x-center)/1.65)**2)
  pts.append(np.array([x,1.5*env*np.cos(3.4*x-phase),0]))
 return VMobject(color=col,stroke_width=4).set_points_smoothly(pts)
def envelope(center=0):
 xs=np.linspace(-6,6,300); top=[np.array([x,1.5*np.exp(-.5*((x-center)/1.65)**2),0]) for x in xs]; bot=[np.array([x,-1.5*np.exp(-.5*((x-center)/1.65)**2),0]) for x in xs[::-1]]; return VMobject(color=TEAL,stroke_width=3,fill_color=TEAL,fill_opacity=.12).set_points_smoothly(top+bot+[top[0]])

class B02_Objects(Scene):
 def construct(self):
  d=DUR.get("B02",11); self.add(bg(),ttl("ONE PACKET, TWO THINGS TO TRACK")); e=envelope(); w=wave(); crest=Dot(np.array([0,1.5,0]),radius=.16,color=CRIMSON); labs=VGroup(Text("envelope: probability region",font=MONO,font_size=24,color=TEAL).move_to(LEFT*3.8+DOWN*2.4),Text("carrier crests: internal phase",font=MONO,font_size=24,color=CRIMSON).move_to(RIGHT*3.8+DOWN*2.4)); self.play(FadeIn(e),Create(w),FadeIn(crest),run_time=1); self.play(FadeIn(labs),run_time=.7); self.wait(max(.1,d-1.7))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",7); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("Which speed follows the particle?",font=SERIF,font_size=44,color=INK).move_to(UP*.5),Text("a crest     or     the envelope",font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.1)); self.wait(d)

class B04_Phase(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("TRACK A CREST: HOLD PHASE CONSTANT")); eqs=VGroup(Text("k x - omega t = constant",font=MONO,font_size=32,color=INK),Text("k dx/dt - omega = 0",font=MONO,font_size=30,color=INK),Text("v_phase = omega / k",font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.65); self.play(Write(eqs[0]),run_time=.7); self.play(TransformFromCopy(eqs[0],eqs[1]),run_time=.7); self.play(FadeIn(eqs[2]),run_time=.6); self.wait(max(.1,d-2))

class B05_PhaseValue(Scene):
 def construct(self):
  d=DUR.get("B05",12); self.add(bg(),ttl("FREE PARTICLE: PHASE VELOCITY")); eqs=VGroup(Text("omega(k) = hbar k^2 / (2m)",font=MONO,font_size=31,color=INK),Text("v_phase = omega / k",font=MONO,font_size=29,color=SLATE),Text("= hbar k / (2m)",font=MONO,font_size=34,color=CRIMSON),Text("= p / (2m)",font=MONO,font_size=40,color=CRIMSON)).arrange(DOWN,buff=.48); self.play(FadeIn(eqs),run_time=1.4); self.wait(max(.1,d-1.4))

class B06_Group(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg(),ttl("NEARBY WAVES BUILD AN ENVELOPE")); xs=np.linspace(-5.5,5.5,350); w1=VMobject(color=SLATE,stroke_width=2).set_points_smoothly([np.array([x,.65*np.sin(3*x)+1.6,0]) for x in xs]); w2=VMobject(color=SLATE,stroke_width=2).set_points_smoothly([np.array([x,.65*np.sin(3.45*x)-.1,0]) for x in xs]); pack=wave(0,0,TEAL).scale(.75).move_to(DOWN*1.8); formula=Text("v_group = d omega / d k",font=MONO,font_size=34,color=TEAL).move_to(DOWN*3); self.play(Create(w1),Create(w2),run_time=.8); self.play(FadeIn(pack),FadeIn(formula),run_time=.9); self.wait(max(.1,d-1.7))

class B07_GroupValue(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("DIFFERENTIATE THE SAME DISPERSION")); eqs=VGroup(Text("omega = hbar k^2 / (2m)",font=MONO,font_size=29,color=INK),Text("v_group = d omega/dk = hbar k/m",font=MONO,font_size=32,color=TEAL),Text("v_group = p/m",font=MONO,font_size=39,color=TEAL),Text("v_group = 2 v_phase",font=DISPLAY,font_size=39,color=CRIMSON)).arrange(DOWN,buff=.55); self.play(FadeIn(eqs[:3]),run_time=1.1); self.play(FadeIn(eqs[3],scale=1.2),run_time=.7); self.wait(max(.1,d-1.8))

class B08_Overtake(Scene):
 def construct(self):
  d=DUR.get("B08",12); self.add(bg(),ttl("LAB FRAME: THE ENVELOPE OVERTAKES THE CRESTS")); base=Line(LEFT*6,RIGHT*6,color=SLATE,stroke_width=2).shift(DOWN*2); ep=Arrow(LEFT*4.8,LEFT*.8,color=TEAL,buff=0,stroke_width=7).shift(DOWN*2); cp=Arrow(LEFT*4.8,LEFT*2.8,color=CRIMSON,buff=0,stroke_width=7).shift(DOWN*.8); labs=VGroup(Text("packet: distance 2d",font=MONO,font_size=25,color=TEAL).next_to(ep,DOWN),Text("crest: distance d",font=MONO,font_size=25,color=CRIMSON).next_to(cp,UP),Text("same time interval",font=SERIF,font_size=28,color=INK).move_to(UP*1.5)); self.play(Create(base),GrowArrow(ep),GrowArrow(cp),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-1.3))

class B09_Relative(Scene):
 def construct(self):
  d=DUR.get("B09",11); self.add(bg(),ttl("PACKET FRAME: CRESTS DRIFT FRONT TO REAR")); e=envelope(); front=Text("FRONT",font=DISPLAY,font_size=24,color=TEAL).move_to(RIGHT*3+DOWN*2); rear=Text("REAR",font=DISPLAY,font_size=24,color=TEAL).move_to(LEFT*3+DOWN*2); arr=Arrow(RIGHT*2.2,LEFT*2.2,color=CRIMSON,buff=0,stroke_width=7); crest=Dot(RIGHT*2.2,radius=.18,color=CRIMSON); wrong=Text("not rear to front",font=SERIF,font_size=27,color=SLATE).move_to(DOWN*3); self.play(FadeIn(e),FadeIn(front,rear,crest),run_time=.7); self.play(GrowArrow(arr),FadeIn(wrong),run_time=.8); self.wait(max(.1,d-1.5))

class B10_Detector(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg(),ttl("A POSITION DETECTOR FOLLOWS THE ENVELOPE")); e=envelope(-2); detector=Rectangle(width=.45,height=4.5,color=INK,fill_color=SLATE,fill_opacity=.2).move_to(RIGHT*3.6); path=Arrow(LEFT*1,RIGHT*3.1,color=TEAL,buff=.1,stroke_width=6); eq=Text("packet center speed = p / m",font=MONO,font_size=32,color=TEAL).move_to(DOWN*2.7); note=Text("not the location of one carrier crest",font=SERIF,font_size=26,color=CRIMSON).move_to(UP*2.3); self.play(FadeIn(e,detector),GrowArrow(path),run_time=.9); self.play(FadeIn(eq,note),run_time=.8); self.wait(max(.1,d-1.7))

class B11_NotUniversal(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("THE FACTOR TWO IS NOT UNIVERSAL")); ax1=Axes(x_range=[0,4,1],y_range=[0,8,2],x_length=4.5,y_length=4,tips=False).move_to(LEFT*3.6); ax2=ax1.copy().move_to(RIGHT*3.6); q=ax1.plot(lambda x:.45*x*x,x_range=[0,4],color=TEAL); l=ax2.plot(lambda x:1.5*x,x_range=[0,4],color=CRIMSON); labs=VGroup(Text("quadratic omega(k)",font=MONO,font_size=23,color=TEAL).next_to(ax1,DOWN),Text("linear omega(k)",font=MONO,font_size=23,color=CRIMSON).next_to(ax2,DOWN),Text("v_group = 2 v_phase",font=SERIF,font_size=25,color=INK).move_to(LEFT*3.6+UP*2.8),Text("v_group = v_phase",font=SERIF,font_size=25,color=INK).move_to(RIGHT*3.6+UP*2.8)); self.play(Create(ax1),Create(ax2),Create(q),Create(l),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-1.3))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("ONE PACKET · TWO VELOCITIES",font=DISPLAY,font_size=28,color=SLATE).move_to(UP*2.3),Text("crests:  p / (2m)",font=MONO,font_size=37,color=CRIMSON).move_to(UP*.6),Text("envelope:  p / m",font=MONO,font_size=39,color=TEAL).move_to(DOWN*.7),Text("THE PACKET IS TWICE AS FAST",font=DISPLAY,font_size=34,color=INK).move_to(DOWN*2.2)); self.wait(d)
