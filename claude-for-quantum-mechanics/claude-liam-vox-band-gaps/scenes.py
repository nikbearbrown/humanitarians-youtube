import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def scan_axes(): return Axes(x_range=[-2,2,1],y_range=[0,8,1],x_length=7,y_length=6,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.25)
def f(e): return 1.35*np.cos(1.55*e)+.28*np.sin(3.1*e)
def model_curve(ax): return ParametricFunction(lambda e:ax.c2p(f(e),e),t_range=[0,8,.025],color=CRIMSON,stroke_width=5)
def bound_strip(ax): return Rectangle(width=ax.x_axis.n2p(1)[0]-ax.x_axis.n2p(-1)[0],height=ax.y_axis.n2p(8)[1]-ax.y_axis.n2p(0)[1]).set_fill(TEAL,.09).set_stroke(TEAL,1).move_to((ax.c2p(-1,0)+ax.c2p(1,8))/2)

class B02_PeriodicPotential(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg()); title=Text("A CRYSTAL REPEATS THE SAME POTENTIAL CELL",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); axis=Line(LEFT*6.5,RIGHT*6.5,color=INK).shift(DOWN*2); wells=VGroup(*[ParametricFunction(lambda x,c=c:np.array([x,-1.2-1.2*np.exp(-((x-c)/.35)**2),0]),t_range=[c-.65,c+.65,.03],color=TEAL,stroke_width=4) for c in np.linspace(-5.5,5.5,9)]); ions=VGroup(*[Dot(RIGHT*c+DOWN*1.1,color=CRIMSON,radius=.12) for c in np.linspace(-5.5,5.5,9)]); brace=BraceBetweenPoints(RIGHT*-1.38+DOWN*2.9,ORIGIN+DOWN*2.9,DOWN,color=CRIMSON); lab=Text("lattice spacing a",font=MONO,font_size=21,color=CRIMSON).next_to(brace,DOWN)
  self.play(FadeIn(title),Create(axis),LaggedStart(*[Create(w) for w in wells],lag_ratio=.08),run_time=1.5); self.play(FadeIn(ions),GrowFromCenter(brace),FadeIn(lab),run_time=.8); self.wait(max(.1,d-2.3))
class B03_RepeatingWave(Scene):
 def construct(self):
  d=DUR.get("B03",10); self.add(bg()); title=Text("CELL TO CELL: SAME SHAPE, NEW PHASE",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); base=Line(LEFT*6.5,RIGHT*6.5,color=INK).shift(DOWN*.3); cells=VGroup(*[DashedLine(UP*2.5+RIGHT*x,DOWN*2.5+RIGHT*x,color=TEAL,stroke_opacity=.35) for x in np.linspace(-6,6,7)]); wave=ParametricFunction(lambda x:np.array([x,.9*np.sin(2.6*x)+.3*np.sin(.8*x)-.3,0]),t_range=[-6.4,6.4,.03],color=CRIMSON,stroke_width=4); eq=Text("ψ(x+a) = eⁱᵏᵃ ψ(x)",font=MONO,font_size=34,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),Create(base),FadeIn(cells),run_time=.8); self.play(Create(wave),FadeIn(eq),run_time=1.6); self.wait(max(.1,d-2.4))
class B04_MatchingCondition(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg()); title=Text("THE MATCHING CONDITION",font=DISPLAY,font_size=33,color=INK).move_to(UP*3.2); left=RoundedRectangle(width=5.2,height=2.3,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.4); right=RoundedRectangle(width=5.2,height=2.3,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*3.4); lt=Text("cos(ka)\nbounded wave side",font=MONO,font_size=30,color=TEAL,line_spacing=1.2).move_to(left); rt=Text("F(E)\nenergy-dependent side",font=MONO,font_size=30,color=CRIMSON,line_spacing=1.2).move_to(right); eq=Text("=",font=DISPLAY,font_size=50,color=INK); sub=Text("real k exists only when the two sides can meet",font=SERIF,font_size=28,color=INK).move_to(DOWN*2.5)
  self.play(FadeIn(title),FadeIn(left),FadeIn(lt),run_time=.8); self.play(FadeIn(eq),FadeIn(right),FadeIn(rt),FadeIn(sub),run_time=1); self.wait(max(.1,d-1.8))
class B05_CosineBound(Scene):
 def construct(self):
  d=DUR.get("B05",7); self.add(bg()); box=RoundedRectangle(width=12,height=2.5,corner_radius=.15).set_fill(TEAL,.07).set_stroke(TEAL,2); text=Text("−1 ≤ cos(ka) ≤ +1\nFOR EVERY REAL k",font=DISPLAY,font_size=39,color=INK,line_spacing=1.25); self.add(box,text); self.wait(d)
class B06_AllowedScan(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("INSIDE [−1,+1] → REAL k → ALLOWED BAND",font=DISPLAY,font_size=27,color=INK).move_to(UP*3.35); ax=scan_axes(); strip=bound_strip(ax); curve=model_curve(ax); bounds=VGroup(DashedLine(ax.c2p(-1,0),ax.c2p(-1,8),color=TEAL),DashedLine(ax.c2p(1,0),ax.c2p(1,8),color=TEAL)); labels=VGroup(Text("−1",font=MONO,font_size=19,color=TEAL).next_to(ax.c2p(-1,0),DOWN),Text("+1",font=MONO,font_size=19,color=TEAL).next_to(ax.c2p(1,0),DOWN),Text("E",font=MONO,font_size=21,color=INK).next_to(ax.y_axis,UP)); e=1.0; scan=Line(ax.c2p(-2,e),ax.c2p(2,e),color=INK,stroke_width=3); dot=Dot(ax.c2p(f(e),e),color=TEAL,radius=.14)
  self.play(FadeIn(title),Create(ax),FadeIn(strip),FadeIn(bounds),Create(curve),FadeIn(labels),run_time=1.5); self.play(FadeIn(scan),GrowFromCenter(dot),Indicate(dot,color=TEAL),run_time=1); self.wait(max(.1,d-2.5))
class B07_ForbiddenScan(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg()); title=Text("OUTSIDE [−1,+1] → NO REAL k → BAND GAP",font=DISPLAY,font_size=27,color=CRIMSON).move_to(UP*3.35); ax=scan_axes(); strip=bound_strip(ax); curve=model_curve(ax); bounds=VGroup(DashedLine(ax.c2p(-1,0),ax.c2p(-1,8),color=TEAL),DashedLine(ax.c2p(1,0),ax.c2p(1,8),color=TEAL)); e=4.15; scan=Line(ax.c2p(-2,e),ax.c2p(2,e),color=INK,stroke_width=3); dot=Dot(ax.c2p(f(e),e),color=CRIMSON,radius=.14); cross=Text("NO REAL k",font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*4.8)
  self.play(FadeIn(title),Create(ax),FadeIn(strip),FadeIn(bounds),Create(curve),run_time=1.4); self.play(FadeIn(scan),GrowFromCenter(dot),FadeIn(cross),Flash(dot,color=CRIMSON),run_time=1.1); self.wait(max(.1,d-2.5))
class B08_BandsAndGaps(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg()); title=Text("THE ENERGY AXIS BREAKS INTO BANDS AND GAPS",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); axis=Line(DOWN*2.6,UP*2.7,color=INK,stroke_width=4); segs=VGroup(); labs=VGroup(); intervals=[(-2.5,-1.7,"BAND",TEAL),(-1.65,-.9,"GAP",CRIMSON),(-.85,.2,"BAND",TEAL),(.25,1.05,"GAP",CRIMSON),(1.1,2.55,"BAND",TEAL)]
  for lo,hi,name,col in intervals:
   s=Rectangle(width=4,height=hi-lo).set_fill(col,.18).set_stroke(col,2).move_to(RIGHT*1.8+UP*(lo+hi)/2); segs.add(s); labs.add(Text(name,font=MONO,font_size=22,color=col).move_to(RIGHT*4.5+UP*(lo+hi)/2))
  atom=VGroup(*[Line(LEFT*5,LEFT*3,color=INK).shift(UP*y) for y in (-1.3,0,1.4)]); arrow=Arrow(LEFT*2.5,LEFT*.5,color=INK); cap=Text("many coupled cells",font=MONO,font_size=21,color=INK).move_to(LEFT*3.8+DOWN*2.7)
  self.play(FadeIn(title),FadeIn(atom),GrowArrow(arrow),FadeIn(cap),run_time=1); self.play(LaggedStart(*[FadeIn(s) for s in segs],lag_ratio=.12),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-2.2))
class B09_EnergyNotSpace(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); top=Text("A BAND GAP IS NOT FORBIDDEN SPACE",font=DISPLAY,font_size=36,color=CRIMSON).move_to(UP*1.4); bot=Text("It is a forbidden ENERGY INTERVAL\nfor extended states in the ideal crystal.",font=DISPLAY,font_size=31,color=INK,line_spacing=1.25).move_to(DOWN*.8); self.add(top,bot); self.wait(d)
class B10_MetalInsulator(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg()); title=Text("OCCUPATION TURNS BANDS INTO MATERIAL BEHAVIOR",font=DISPLAY,font_size=27,color=INK).move_to(UP*3.35); groups=VGroup()
  for x,label,partial in ((-3.6,"METAL",True),(3.6,"INSULATOR",False)):
   low=Rectangle(width=4.8,height=1.5).set_fill(TEAL,.18).set_stroke(TEAL,2).move_to(RIGHT*x+DOWN*1.2); high=Rectangle(width=4.8,height=1.3).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*x+UP*1.4); fill=Rectangle(width=4.6,height=(.75 if partial else 1.3)).set_fill(INK,.3).set_stroke(width=0).align_to(low,DOWN).move_to(low.get_bottom()+UP*((.75 if partial else 1.3)/2)); lab=Text(label,font=DISPLAY,font_size=29,color=INK).move_to(RIGHT*x+UP*2.8); groups.add(VGroup(low,high,fill,lab))
  notes=VGroup(Text("nearby empty states",font=MONO,font_size=20,color=TEAL).move_to(LEFT*3.6+DOWN*2.7),Text("filled band + large gap",font=MONO,font_size=20,color=CRIMSON).move_to(RIGHT*3.6+DOWN*2.7)); self.play(FadeIn(title),FadeIn(groups),FadeIn(notes),run_time=1.2); self.wait(max(.1,d-1.2))
class B11_Semiconductor(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); title=Text("SEMICONDUCTOR: SAME ARCHITECTURE, MODEST GAP",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); val=Rectangle(width=8,height=1.6).set_fill(TEAL,.2).set_stroke(TEAL,2).move_to(DOWN*1.7); con=Rectangle(width=8,height=1.3).set_fill(CRIMSON,.07).set_stroke(CRIMSON,2).move_to(UP*1.4); gap=DoubleArrow(DOWN*.85,UP*.72,color=CRIMSON,buff=.05); eg=Text("E gap",font=MONO,font_size=25,color=CRIMSON).next_to(gap,RIGHT); electron=Dot(DOWN*1.3,color=INK,radius=.15); jump=Arrow(DOWN*.9,UP*.8,color=INK); device=Text("a controllable energy threshold",font=MONO,font_size=24,color=INK).move_to(DOWN*3.2)
  self.play(FadeIn(title),FadeIn(val),FadeIn(con),GrowFromCenter(gap),FadeIn(eg),run_time=1); self.play(GrowFromCenter(electron),GrowArrow(jump),electron.animate.move_to(UP*1.4),FadeIn(device),run_time=1.1); self.wait(max(.1,d-2.1))
