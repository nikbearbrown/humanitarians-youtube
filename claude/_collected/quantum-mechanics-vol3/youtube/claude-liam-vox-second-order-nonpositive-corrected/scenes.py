import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)
def level(y,w=6,c=INK): return Line(LEFT*w/2,RIGHT*w/2,color=c,stroke_width=3).shift(UP*y)

class B02_Scope(Scene):
 def construct(self):
  left=VGroup(Text("FULL SHIFT",font=DISPLAY,font_size=31,color=CRIMSON),Text("may rise or fall",font=SERIF,font_size=33,color=INK),Text("first order matters",font=MONO,font_size=26,color=CRIMSON)).arrange(DOWN,buff=.45).move_to(LEFT*3); right=VGroup(Text("SECOND ORDER",font=DISPLAY,font_size=31,color=TEAL),Text("never positive",font=SERIF,font_size=33,color=INK),Text("unique ground state",font=MONO,font_size=26,color=TEAL)).arrange(DOWN,buff=.45).move_to(RIGHT*3)
  self.play(FadeIn(heading("ONE COEFFICIENT IS NOT THE WHOLE ENERGY")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B02")

class B03_Assumptions(Scene):
 def construct(self):
  ls=VGroup(level(-2,6,TEAL),level(-.5,5),level(.8,5),level(1.9,5)); labs=VGroup(Text("unique ground state",font=SERIF,font_size=29,color=TEAL).next_to(ls[0],RIGHT),Text("separated excited levels",font=SERIF,font_size=27,color=INK).next_to(ls[2],RIGHT),Text("H = H0 + lambda H'",font=MONO,font_size=37,color=INK).shift(UP*2.7))
  self.play(FadeIn(heading("START INSIDE NONDEGENERATE PERTURBATION THEORY"),run_time=.4),LaggedStart(*[Create(x) for x in ls],lag_ratio=.15),FadeIn(labs),run_time=1); hold(self,"B03",1)

class B04_Formula(Scene):
 def construct(self):
  eq=VGroup(Text("E0^(2) = SUM",font=MONO,font_size=43,color=INK),Text("| <m|H'|0> |^2",font=MONO,font_size=38,color=TEAL),Line(LEFT*2.3,RIGHT*2.3,color=INK),Text("E0 - Em",font=MONO,font_size=38,color=CRIMSON)).arrange(DOWN,buff=.22); caps=VGroup(Text("squared coupling",font=SERIF,font_size=27,color=TEAL).shift(LEFT*3+DOWN*2.2),Text("energy difference",font=SERIF,font_size=27,color=CRIMSON).shift(RIGHT*3+DOWN*2.2))
  self.play(FadeIn(heading("SECOND ORDER IS A SUM OF VIRTUAL COUPLINGS")),FadeIn(eq),FadeIn(caps),run_time=1); hold(self,"B04")

class B05_Numerator(Scene):
 def construct(self):
  box=RoundedRectangle(width=8,height=2.2,corner_radius=.2,color=TEAL,fill_color=TEAL,fill_opacity=.06); eq=Text("| <m|H'|0> |^2  >=  0",font=MONO,font_size=45,color=TEAL); cases=VGroup(Text("positive when coupled",font=SERIF,font_size=29,color=INK),Text("zero when uncoupled",font=SERIF,font_size=29,color=INK)).arrange(RIGHT,buff=1.5).shift(DOWN*1.8)
  self.play(FadeIn(heading("THE NUMERATOR CANNOT SUPPLY A MINUS SIGN")),Create(box),FadeIn(eq),FadeIn(cases),run_time=1); hold(self,"B05")

class B06_Denominator(Scene):
 def construct(self):
  g=level(-2,7,TEAL); ex=VGroup(level(-.4,5),level(.8,5),level(1.9,5)); arrows=VGroup(*[Arrow(x.get_center(),g.get_center(),color=CRIMSON,buff=.15) for x in ex]); lab=Text("E0 - Em  <  0",font=MONO,font_size=43,color=CRIMSON).shift(RIGHT*3+UP*2.5)
  self.play(FadeIn(heading("EVERY OTHER LEVEL IS ABOVE THE GROUND STATE")),Create(g),LaggedStart(*[Create(x) for x in ex],lag_ratio=.15),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.12),FadeIn(lab),run_time=1.2); hold(self,"B06",1.2)

class B07_Accumulate(Scene):
 def construct(self):
  vals=["-a","-b","0","-c","-d"]; chips=VGroup(*[Text(v,font=MONO,font_size=37,color=TEAL if v!="0" else INK) for v in vals]).arrange(RIGHT,buff=.7).shift(UP*.7); line=Line(LEFT*4,RIGHT*4,color=INK).shift(DOWN*.3); total=Text("SUM  <=  0",font=MONO,font_size=50,color=CRIMSON).shift(DOWN*1.6)
  self.play(FadeIn(heading("NONPOSITIVE TERMS CANNOT ADD TO A POSITIVE TOTAL")),LaggedStart(*[FadeIn(x,shift=DOWN*.2) for x in chips],lag_ratio=.15),Create(line),FadeIn(total),run_time=1.1); hold(self,"B07",1.1)

class B08_ZeroCase(Scene):
 def construct(self):
  eq1=Text("H' = c I",font=MONO,font_size=48,color=INK).shift(UP*1.5); eq2=Text("<m|H'|0> = 0",font=MONO,font_size=43,color=TEAL); eq3=Text("E0^(2) = 0",font=MONO,font_size=50,color=CRIMSON).shift(DOWN*1.7)
  self.play(FadeIn(heading("THE WORD IS NONPOSITIVE, NOT ALWAYS NEGATIVE")),FadeIn(eq1),FadeIn(eq2),FadeIn(eq3),run_time=1); hold(self,"B08")

class B09_FirstOrder(Scene):
 def construct(self):
  axis=Axes(x_range=[0,1.2,.2],y_range=[0,1.2,.2],x_length=8,y_length=4.2,axis_config={"color":INK},tips=False).shift(DOWN*.5); line=axis.plot(lambda x:.75*x,x_range=[0,1.1],color=CRIMSON); cap=VGroup(Text("E(lambda) = E0 + c lambda",font=MONO,font_size=35,color=CRIMSON),Text("second-order coefficient = 0",font=SERIF,font_size=29,color=TEAL)).arrange(DOWN,buff=.3).shift(UP*2.1)
  self.play(FadeIn(heading("A POSITIVE FIRST-ORDER SHIFT CAN STILL RAISE ENERGY")),FadeIn(axis),Create(line),FadeIn(cap),run_time=1); hold(self,"B09")

class B10_Stark(Scene):
 def construct(self):
  axis=Axes(x_range=[-1,1,.5],y_range=[-1,.3,.25],x_length=8,y_length=4.3,axis_config={"color":INK},tips=False).shift(DOWN*.5); curve=axis.plot(lambda x:-.7*x*x,x_range=[-1,1],color=TEAL); labs=VGroup(Text("electric field",font=SERIF,font_size=27,color=INK).shift(DOWN*3),Text("parity: linear term = 0",font=MONO,font_size=29,color=CRIMSON).shift(UP*2.2),Text("quadratic Stark shift < 0",font=MONO,font_size=29,color=TEAL).shift(UP*1.5))
  self.play(FadeIn(heading("HYDROGEN'S GROUND-STATE STARK CURVE BENDS DOWN")),FadeIn(axis),Create(curve),FadeIn(labs),run_time=1.1); hold(self,"B10",1.1)

class B11_Degeneracy(Scene):
 def construct(self):
  pair=VGroup(level(0,6,CRIMSON),level(0,6,CRIMSON)); pair[0].shift(UP*.04); pair[1].shift(DOWN*.04); split=VGroup(level(1,5,TEAL),level(-1,5,TEAL)); arr=VGroup(Arrow(LEFT*.7,LEFT*.7+UP*.8,color=TEAL),Arrow(RIGHT*.7,RIGHT*.7+DOWN*.8,color=TEAL)); labs=VGroup(Text("zero denominator",font=MONO,font_size=32,color=CRIMSON).shift(UP*1),Text("diagonalize inside the subspace first",font=SERIF,font_size=31,color=INK).shift(DOWN*2.2))
  self.play(FadeIn(heading("DEGENERACY CHANGES THE STARTING BASIS")),Create(pair),FadeIn(labs[0]),TransformFromCopy(pair,split),FadeIn(arr),FadeIn(labs[1]),run_time=1.2); hold(self,"B11",1.2)

class B12_Audit(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=29,color=TEAL if i==0 else INK) for i,x in enumerate(["unique unperturbed ground state","Hermitian perturbation","well-defined sums or integrals","small parameter; no nearby breakdown"])]).arrange(DOWN,aligned_edge=LEFT,buff=.55)
  self.play(FadeIn(heading("THE SIGN THEOREM HAS A DOMAIN")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.15),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("4 / (-2)  +  1 / (-5)",font=MONO,font_size=50,color=CRIMSON),Text("What is E0^(2)?",font=SERIF,font_size=34,color=INK)).arrange(DOWN,buff=.8)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("-2  -  0.2",font=MONO,font_size=47,color=TEAL),Text("E0^(2) = -2.2",font=MONO,font_size=55,color=CRIMSON),Text("different sizes, same nonpositive sign",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why the Nondegenerate Ground State's\nSecond-Order Shift Is Never Positive",font=DISPLAY,font_size=34,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
