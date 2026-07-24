import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 _bs=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t): return Text(t,font=DISPLAY,font_size=29,color=INK).to_edge(UP)

class B02_FormalSeries(Scene):
 def construct(self):
  terms=VGroup(Text("E(λ) =",font=MONO,font_size=42,color=INK),Text("E₀",font=MONO,font_size=42,color=INK),Text("+ c₁λ",font=MONO,font_size=39,color=TEAL),Text("+ c₂λ²",font=MONO,font_size=36,color=TEAL),Text("+ c₃λ³ + …",font=MONO,font_size=32,color=CRIMSON)).arrange(RIGHT,buff=.3); note=Text("formal perturbative expansion",font=SERIF,font_size=30,color=INK).shift(DOWN*2)
  self.play(FadeIn(heading("SMALL POWERS MAKE EARLY TERMS LOOK SAFE")),LaggedStart(*[FadeIn(t) for t in terms],lag_ratio=.12),FadeIn(note),run_time=1.2); hold(self,"B02",1.2)

class B03_TwoQuestions(Scene):
 def construct(self):
  left=VGroup(Text("CONVERGENCE",font=DISPLAY,font_size=32,color=TEAL),Text("N → ∞",font=MONO,font_size=42,color=INK),Text("Do partial sums settle?",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("USEFULNESS",font=DISPLAY,font_size=32,color=CRIMSON),Text("finite N",font=MONO,font_size=42,color=INK),Text("Is there an accurate window?",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3); self.play(FadeIn(heading("DIVERGENT DOES NOT MEAN USELESS")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B03")

class B04_SignFlip(Scene):
 def construct(self):
  ax=Axes(x_range=[-3,3,1],y_range=[-4,6,2],x_length=8,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.3); pos=ax.plot(lambda x:.5*x*x+.08*x**4,x_range=[-3,3],color=TEAL); neg=ax.plot(lambda x:.5*x*x-.08*x**4,x_range=[-3,3],color=CRIMSON); labs=VGroup(Text("λ>0 stable",font=SERIF,font_size=27,color=TEAL).move_to(LEFT*3+UP*2),Text("λ<0 unbounded",font=SERIF,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*1.8))
  title=Text("FLIP THE QUARTIC COUPLING'S SIGN",font=DISPLAY,font_size=26,color=INK).to_edge(UP)
  self.play(FadeIn(title),FadeIn(ax),Create(pos),run_time=.7); self.play(TransformFromCopy(pos,neg),FadeIn(labs),run_time=.7); hold(self,"B04",1.4)

class B05_NoGround(Scene):
 def construct(self):
  ax=Axes(x_range=[-3.2,3.2,1],y_range=[-5,3,2],x_length=8,y_length=5,axis_config={"color":INK},tips=False).shift(DOWN*.3); curve=ax.plot(lambda x:.5*x*x-.12*x**4,x_range=[-3,3],color=CRIMSON); arrows=VGroup(Arrow(ax.c2p(-2,-1),ax.c2p(-3,-4),color=CRIMSON,buff=0),Arrow(ax.c2p(2,-1),ax.c2p(3,-4),color=CRIMSON,buff=0)); note=Text("no lowest bound energy for λ<0",font=MONO,font_size=31,color=INK).shift(UP*2.4)
  self.play(FadeIn(heading("NEGATIVE COUPLING DESTROYS THE GROUND STATE")),FadeIn(ax),Create(curve),GrowArrow(arrows[0]),GrowArrow(arrows[1]),FadeIn(note),run_time=1.2); hold(self,"B05",1.2)

class B06_ZeroRadius(Scene):
 def construct(self):
  axis=NumberLine(x_range=[-1,1,.25],length=9,include_numbers=False,color=INK); zero=Dot(axis.n2p(0),color=INK); bad=VGroup(*[Dot(axis.n2p(-v),radius=.08,color=CRIMSON) for v in [.8,.5,.3,.18,.1,.05]]); labels=VGroup(Text("unstable for every λ<0",font=SERIF,font_size=29,color=CRIMSON).shift(UP*1.4+LEFT*2),Text("nonanalytic arbitrarily near 0",font=SERIF,font_size=29,color=INK).shift(DOWN*1.3),Text("Taylor radius = 0",font=MONO,font_size=38,color=TEAL).shift(DOWN*2.4))
  self.play(FadeIn(heading("THE BAD SIDE ACCUMULATES AT THE EXPANSION POINT")),Create(axis),FadeIn(zero),LaggedStart(*[FadeIn(d) for d in bad],lag_ratio=.1),FadeIn(labels),run_time=1.2); hold(self,"B06",1.2)

class B07_FactorialGrowth(Scene):
 def construct(self):
  ax=Axes(x_range=[1,12,2],y_range=[0,6,1],x_length=9,y_length=3.7,axis_config={"color":INK},tips=False).shift(DOWN*.8); curve=ax.plot(lambda x:min(5.8,math.gamma(x+1)**.18),x_range=[1,12],color=CRIMSON); note=VGroup(Text("c_k ~ k! A^k",font=MONO,font_size=39,color=CRIMSON),Text("factorial beats any fixed exponential at large k",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.25).move_to(UP*1.65)
  self.play(FadeIn(heading("LARGE-ORDER COEFFICIENTS GROW TOO FAST")),FadeIn(ax),Create(curve),FadeIn(note),run_time=1.2); hold(self,"B07",1.2)

class B08_TermValley(Scene):
 def construct(self):
  ax=Axes(x_range=[0,30,5],y_range=[0,4,1],x_length=9,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.35); curve=ax.plot(lambda x:.3+((x-19)/11)**2,x_range=[0,30],color=TEAL); dot=Dot(ax.c2p(19,.3),color=CRIMSON); labs=VGroup(Text("terms shrink",font=SERIF,font_size=27,color=TEAL).move_to(LEFT*3+UP*1.3),Text("terms grow",font=SERIF,font_size=27,color=CRIMSON).move_to(RIGHT*3+UP*1.3),Text("smallest term",font=SERIF,font_size=27,color=CRIMSON).next_to(dot,DOWN))
  self.play(FadeIn(heading("TERM MAGNITUDES FORM A VALLEY")),FadeIn(ax),Create(curve),FadeIn(dot),FadeIn(labs),run_time=1.2); hold(self,"B08",1.2)

class B09_Ratio(Scene):
 def construct(self):
  g=VGroup(Text("T_k ~ k! λ^k",font=MONO,font_size=45,color=TEAL),Text("|T_{k+1}/T_k| ~ (k+1)λ",font=MONO,font_size=43,color=CRIMSON),Text("< 1: shrinking     > 1: growing",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.7); self.play(FadeIn(heading("THE NEXT-TERM RATIO LOCATES THE TURN")),FadeIn(g),run_time=1); hold(self,"B09")

class B10_OptimalOrder(Scene):
 def construct(self):
  axis=NumberLine(x_range=[0,30,5],length=10,include_numbers=False,color=INK); mark=Triangle(color=CRIMSON,fill_opacity=1).scale(.18).rotate(PI).next_to(axis.n2p(19),UP); labs=VGroup(Text("N*",font=MONO,font_size=35,color=CRIMSON).next_to(mark,UP),Text("(k+1)λ ≈ 1",font=MONO,font_size=40,color=TEAL).shift(UP*1.8),Text("truncate near the smallest term",font=SERIF,font_size=31,color=INK).shift(DOWN*1.6))
  self.play(FadeIn(heading("OPTIMAL TRUNCATION IS A STOP SIGN")),Create(axis),FadeIn(mark),FadeIn(labs),run_time=1); hold(self,"B10")

class B11_ErrorCurve(Scene):
 def construct(self):
  ax=Axes(x_range=[0,30,5],y_range=[0,4,1],x_length=9,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.35); curve=ax.plot(lambda x:.15+.008*(x-19)**2,x_range=[0,30],color=INK); dot=Dot(ax.c2p(19,.15),color=CRIMSON); left=ax.plot(lambda x:.15+.008*(x-19)**2,x_range=[0,19],color=TEAL,stroke_width=5); right=ax.plot(lambda x:.15+.008*(x-19)**2,x_range=[19,30],color=CRIMSON,stroke_width=5); note=Text("minimum error near N*",font=SERIF,font_size=29,color=INK).next_to(dot,UP)
  self.play(FadeIn(heading("ERROR FALLS, BOTTOMS OUT, THEN RISES")),FadeIn(ax),Create(curve),Create(left),Create(right),FadeIn(dot),FadeIn(note),run_time=1.2); hold(self,"B11",1.2)

class B12_Limits(Scene):
 def construct(self):
  items=["constants and indexing are model-dependent","alternating signs can improve behavior","resummation may recover more information","small denominators are a different failure","practical rule: watch the term size"]
  rows=VGroup(*[Text("• "+x,font=SERIF,font_size=27,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.4); self.play(FadeIn(heading("THE CARTOON IS USEFUL — AND SCOPED")),FadeIn(rows),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=35,color=INK),Text("λ = 0.05",font=MONO,font_size=45,color=TEAL),Text("(k+1)λ ≈ 1",font=MONO,font_size=42,color=CRIMSON),Text("near which k do terms turn?",font=SERIF,font_size=30,color=INK)).arrange(DOWN,buff=.55); self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_Answer(Scene):
 def construct(self):
  g=VGroup(Text("ANSWER",font=DISPLAY,font_size=35,color=INK),Text("k+1 ≈ 1/0.05 = 20",font=MONO,font_size=42,color=TEAL),Text("k ≈ 19",font=MONO,font_size=54,color=CRIMSON),Text("truncate near order 19–20 in this toy model",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.55); self.play(FadeIn(g),run_time=1); hold(self,"B14")

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  self.camera.background_color="#201F1C"; title=Text("Why a Divergent Series Can Still Give the Right Answer",font=DISPLAY,font_size=30,color="#F2EFE8"); credit=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45); self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B15")
