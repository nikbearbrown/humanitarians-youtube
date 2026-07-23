import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception:
    pass

def hold(scene, beat, used=1.0): scene.wait(max(.1, DUR.get(beat, 10)-used))
def heading(text): return Text(text, font=DISPLAY, font_size=28, color=INK).to_edge(UP)

class B02_AngularMinimum(Scene):
    def construct(self):
        ax=Axes(x_range=[0,10,2],y_range=[0,1.2,.5],x_length=9,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.3)
        curve=ax.plot(lambda x:(np.sinc(x/3.2))**2,x_range=[0,10],color=TEAL,stroke_width=3)
        dot=Dot(ax.c2p(3.2,0),color=CRIMSON); note=Text("first measured minimum — may not reach zero",font=SERIF,font_size=22,color=CRIMSON).to_edge(DOWN)
        self.play(FadeIn(heading("COUNTS VERSUS ANGLE OR MOMENTUM TRANSFER")),FadeIn(ax),Create(curve),FadeIn(dot),run_time=1); self.play(FadeIn(note),run_time=.5); hold(self,"B02",1.5)

class B03_RadiusQuestion(Scene):
    def construct(self):
        q=VGroup(Text("What radius does the minimum measure?",font=DISPLAY,font_size=33,color=INK),Text("Which assumptions make the conversion?",font=SERIF,font_size=28,color=TEAL)).arrange(DOWN,buff=.6)
        self.play(FadeIn(heading("THE QUESTION")),FadeIn(q),run_time=1); hold(self,"B03")

class B04_PointBaseline(Scene):
    def construct(self):
        ax=Axes(x_range=[.5,5,1],y_range=[0,5,1],x_length=8,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.4)
        curve=ax.plot(lambda x:1/(x+.2)**2,x_range=[.5,5],color=CRIMSON,stroke_width=3)
        note=Text("point Coulomb/Mott baseline is angle-dependent",font=SERIF,font_size=24,color=CRIMSON).to_edge(DOWN)
        self.play(FadeIn(heading("POINT TARGET DOES NOT MEAN ISOTROPIC")),FadeIn(ax),Create(curve),FadeIn(note),run_time=1); hold(self,"B04")

class B05_Factorization(Scene):
    def construct(self):
        eq=Text("extended cross section  =  point result  ×  |F(q)|^2",font=MONO,font_size=30,color=INK)
        norm=Text("F(0) = 1",font=MONO,font_size=34,color=TEAL).next_to(eq,DOWN,buff=.8)
        self.play(FadeIn(heading("BORN-STYLE FACTORIZATION")),Write(eq),FadeIn(norm),run_time=1.2); hold(self,"B05",1.2)

class B06_FourierMap(Scene):
    def construct(self):
        left=VGroup(Text("charge density ρ(r)",font=DISPLAY,font_size=28,color=INK),Circle(radius=1.2,color=TEAL,fill_opacity=.25)).arrange(DOWN,buff=.4).move_to(LEFT*3)
        arrow=Arrow(LEFT*.8,RIGHT*.8,color=CRIMSON); lab=Text("Fourier transform",font=SERIF,font_size=22,color=CRIMSON).next_to(arrow,UP)
        right=VGroup(Text("form factor F(q)",font=DISPLAY,font_size=28,color=INK),Text("small q → broad scale\nlarge q → fine scale",font=SERIF,font_size=23,color=TEAL,line_spacing=1.3)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
        self.play(FadeIn(heading("REAL SPACE ↔ MOMENTUM SPACE")),FadeIn(left),GrowArrow(arrow),FadeIn(lab),FadeIn(right),run_time=1.2); hold(self,"B06",1.2)

class B07_UniformSphere(Scene):
    def construct(self):
        ax=Axes(x_range=[0,10,2],y_range=[-0.3,1.1,.5],x_length=9,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.3)
        def f(x): return 1 if abs(x)<.02 else 3*(np.sin(x)-x*np.cos(x))/(x**3)
        curve=ax.plot(f,x_range=[.02,10],color=TEAL,stroke_width=3); zero=Dot(ax.c2p(4.493,0),color=CRIMSON)
        label=Text("first zero: qR = 4.493",font=MONO,font_size=23,color=CRIMSON).to_edge(DOWN)
        self.play(FadeIn(heading("UNIFORM SHARP SPHERE MODEL")),FadeIn(ax),Create(curve),FadeIn(zero),FadeIn(label),run_time=1.1); hold(self,"B07",1.1)

class B08_VolumeCancellation(Scene):
    def construct(self):
        disk=Circle(radius=2,color=INK); rays=VGroup(*[Arrow(np.array([2*np.cos(a),2*np.sin(a),0]),RIGHT*4+UP*(1.4*np.sin(a)),color=TEAL if i%2==0 else CRIMSON,buff=0) for i,a in enumerate(np.linspace(0,2*np.pi,10,endpoint=False))])
        note=Text("cancellation across the full charge volume",font=SERIF,font_size=25,color=INK).to_edge(DOWN)
        self.play(FadeIn(heading("THE FORM-FACTOR ZERO")),Create(disk),LaggedStart(*[GrowArrow(r) for r in rays],lag_ratio=.08),FadeIn(note),run_time=1.3); hold(self,"B08",1.3)

class B09_AngleToRadius(Scene):
    def construct(self):
        lines=VGroup(Text("q0 = 2k sin(theta0/2)",font=MONO,font_size=34,color=INK),Text("uniform sphere:  q0 R = 4.493",font=MONO,font_size=31,color=TEAL),Text("R = 4.493 / q0",font=MONO,font_size=38,color=CRIMSON)).arrange(DOWN,buff=.65)
        self.play(FadeIn(heading("ANGLE → q0 → MODEL RADIUS")),FadeIn(lines),run_time=1); hold(self,"B09")

class B10_RadiusTypes(Scene):
    def construct(self):
        left=VGroup(Text("sharp radius R",font=DISPLAY,font_size=29,color=TEAL),Circle(radius=1.3,color=TEAL),Text("uniform edge",font=SERIF,font_size=21,color=INK)).arrange(DOWN,buff=.35).move_to(LEFT*3)
        right=VGroup(Text("RMS charge radius",font=DISPLAY,font_size=29,color=CRIMSON),Text("r_rms = sqrt(3/5) R",font=MONO,font_size=28,color=CRIMSON),Text("only for uniform sphere",font=SERIF,font_size=21,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3)
        self.play(FadeIn(heading("WHICH RADIUS?")),FadeIn(left),FadeIn(right),run_time=1); hold(self,"B10")

class B11_LimitsAudit(Scene):
    def construct(self):
        items=["diffuse surface / deformation","Coulomb distortion","relativistic corrections","inelastic contamination","finite resolution / q coverage"]
        rows=VGroup(*[Text("• "+x,font=SERIF,font_size=25,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.38)
        self.play(FadeIn(heading("FROM MINIMUM TO DENSITY: MODEL + CORRECTIONS")),FadeIn(rows),run_time=1); hold(self,"B11")

class B12_YourTurn(Scene):
    def construct(self):
        g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=32,color=INK),Text("q0 = 0.75 fm^-1",font=MONO,font_size=36,color=TEAL),Text("R = 4.493 / q0",font=MONO,font_size=32,color=INK),Text("Estimate the sharp radius.",font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B12")

class B13_YourTurnAnswer(Scene):
    def construct(self):
        g=VGroup(Text("ANSWER",font=DISPLAY,font_size=32,color=INK),Text("R = 4.493 / 0.75 = 5.99 fm",font=MONO,font_size=32,color=TEAL),Text("r_rms = sqrt(3/5) R = 4.64 fm",font=MONO,font_size=28,color=CRIMSON),Text("uniform-sphere model",font=SERIF,font_size=22,color=SLATE)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        self.camera.background_color="#201F1C"; title=Text("The First Diffraction Minimum and Nuclear Size",font=DISPLAY,font_size=31,color="#F2EFE8"); credit=Text("Liam, in for Bear",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45)
        self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B14")
