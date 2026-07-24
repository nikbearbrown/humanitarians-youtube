import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(scene, beat, used=1.0): scene.wait(max(.1, DUR.get(beat, 10)-used))
def heading(text): return Text(text, font=DISPLAY, font_size=29, color=INK).to_edge(UP)
def lattice(n=11): return VGroup(*[Dot(LEFT*5+i*RIGHT, radius=.13, color=INK) for i in range(n)]).shift(DOWN*1.4)

class B02_NaiveScatterers(Scene):
    def construct(self):
        ions=lattice(); arrows=VGroup(*[Arrow(LEFT*5+i*RIGHT+UP*.2,LEFT*4.6+i*RIGHT+UP*(.4*(-1)**i),buff=0,color=CRIMSON,stroke_width=3) for i in range(10)])
        self.play(FadeIn(heading("THE WRONG MODEL: INDEPENDENT OBSTACLES")),FadeIn(ions),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.06),run_time=1.4); hold(self,"B02",1.4)

class B03_TranslationSymmetry(Scene):
    def construct(self):
        row1=lattice(); row2=row1.copy().shift(RIGHT); eq=Text("V(x + a) = V(x)    ⇒    [H, T_a] = 0",font=MONO,font_size=31,color=TEAL).shift(UP*.8); a=DoubleArrow(DOWN*2.15+LEFT*.5,DOWN*2.15+RIGHT*.5,color=CRIMSON); lab=Text("a",font=SERIF,font_size=24,color=CRIMSON).next_to(a,DOWN)
        self.play(FadeIn(heading("PERIODICITY IS A SYMMETRY")),FadeIn(row1),Write(eq),GrowArrow(a),FadeIn(lab),run_time=1.2); self.play(Transform(row1,row2),run_time=.5); hold(self,"B03",1.7)

class B04_BlochWave(Scene):
    def construct(self):
        ax=Axes(x_range=[-5,5,1],y_range=[-1.5,1.5,1],x_length=10,y_length=4,axis_config={"color":SLATE},tips=False).shift(DOWN*.2)
        carrier=ax.plot(lambda x: np.cos(3*x),x_range=[-5,5],color=TEAL,stroke_width=3); env=ax.plot(lambda x:(.75+.22*np.cos(2*np.pi*x))*np.cos(3*x),x_range=[-5,5],color=CRIMSON,stroke_width=4)
        eq=Text("ψ_nk(x) = e^(ikx) u_nk(x)     u(x+a)=u(x)",font=MONO,font_size=27,color=INK).shift(DOWN*2.45)
        self.play(FadeIn(heading("A BLOCH WAVE IS MODULATED, NOT RESET")),FadeIn(ax),Create(carrier),run_time=.8); self.play(Transform(carrier,env),FadeIn(eq),run_time=.7); hold(self,"B04",1.5)

class B05_CleanFlow(Scene):
    def construct(self):
        ions=lattice(); wave=VMobject(color=TEAL,stroke_width=5).set_points_smoothly([np.array([-5+x,.45*np.sin(2*x),0]) for x in np.linspace(0,10,80)]); k=Text("k conserved modulo G",font=MONO,font_size=31,color=CRIMSON).shift(UP*1.5)
        self.play(FadeIn(heading("THE LATTICE IS ALREADY IN THE EIGENSTATE")),FadeIn(ions),Create(wave),FadeIn(k),run_time=1.4); self.play(wave.animate.shift(RIGHT*.7),rate_func=linear,run_time=.8); hold(self,"B05",2.2)

class B06_DefectScattering(Scene):
    def construct(self):
        ions=lattice(); defect=ions[6]; incoming=Arrow(LEFT*5,RIGHT*.3+DOWN*.5,color=TEAL,buff=0); out1=Arrow(RIGHT*.5+DOWN*.5,RIGHT*4+UP*1.2,color=CRIMSON,buff=0); out2=Arrow(RIGHT*.5+DOWN*.5,RIGHT*3+DOWN*2,color=CRIMSON,buff=0)
        self.play(FadeIn(heading("BREAK THE PATTERN → OPEN SCATTERING CHANNELS")),FadeIn(ions),defect.animate.shift(UP*.7),GrowArrow(incoming),run_time=1); self.play(GrowArrow(out1),GrowArrow(out2),run_time=.6); hold(self,"B06",1.6)

class B07_RelaxationTime(Scene):
    def construct(self):
        eq=Text("σ = n e² τ / m*",font=MONO,font_size=50,color=INK); chain=VGroup(Text("more scattering",font=SERIF,font_size=28,color=CRIMSON),Arrow(LEFT,RIGHT,color=CRIMSON),Text("shorter τ",font=SERIF,font_size=28,color=TEAL),Arrow(LEFT,RIGHT,color=CRIMSON),Text("larger ρ",font=SERIF,font_size=28,color=CRIMSON)).arrange(RIGHT,buff=.35).next_to(eq,DOWN,buff=1)
        self.play(FadeIn(heading("A SIMPLE TRANSPORT CLOCK")),Write(eq),run_time=.8); self.play(LaggedStart(*[FadeIn(x) for x in chain],lag_ratio=.1),run_time=.8); hold(self,"B07",1.6)

class B08_FilledBand(Scene):
    def construct(self):
        band=RoundedRectangle(width=9,height=3.4,corner_radius=.25,color=INK).shift(UP*.15); states=VGroup(*[Dot(radius=.14,color=TEAL) for _ in range(24)]).arrange_in_grid(rows=4,buff=.48).move_to(band); cancel=Text("+v and −v contributions cancel",font=SERIF,font_size=29,color=CRIMSON).shift(DOWN*2.55)
        self.play(FadeIn(heading("PERFECT LATTICE ≠ AUTOMATIC CONDUCTOR")),Create(band),LaggedStart(*[FadeIn(d) for d in states],lag_ratio=.03),FadeIn(cancel),run_time=1.2); hold(self,"B08",1.2)

class B09_PartialBand(Scene):
    def construct(self):
        ax=Axes(x_range=[-4,4,2],y_range=[0,5,1],x_length=9,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.3); curve=ax.plot(lambda x:.22*x*x+.5,x_range=[-4,4],color=TEAL); dots=VGroup(*[Dot(ax.c2p(x,.22*x*x+.5),radius=.09,color=CRIMSON) for x in np.linspace(-2.4,2.4,13)]); arrow=Arrow(ax.c2p(0,3.6),ax.c2p(.8,3.6),color=CRIMSON)
        self.play(FadeIn(heading("PARTIALLY FILLED BAND: OCCUPATIONS CAN SHIFT")),FadeIn(ax),Create(curve),FadeIn(dots),run_time=1); self.play(dots.animate.shift(RIGHT*.45),GrowArrow(arrow),run_time=.7); hold(self,"B09",1.7)

class B10_NotSuperconductivity(Scene):
    def construct(self):
        left=VGroup(Text("ideal band model",font=DISPLAY,font_size=31,color=TEAL),Text("no momentum relaxation",font=SERIF,font_size=25,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("superconductor",font=DISPLAY,font_size=31,color=CRIMSON),Text("collective phase rigidity\n+ Meissner effect",font=SERIF,font_size=25,color=INK,line_spacing=1.2)).arrange(DOWN,buff=.5).move_to(RIGHT*3); neq=Text("≠",font=DISPLAY,font_size=60,color=CRIMSON)
        self.play(FadeIn(heading("ZERO IDEAL RELAXATION IS NOT THE MEISSNER STATE")),FadeIn(left),FadeIn(right),FadeIn(neq),run_time=1); hold(self,"B10")

class B11_Limits(Scene):
    def construct(self):
        items=["electron–electron + Umklapp","phonons and defects","boundaries and contacts","band filling","order of DC limits"]
        rows=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
        self.play(FadeIn(heading("WHAT THE ONE-ELECTRON SLOGAN LEAVES OUT")),LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.08),run_time=1.2); hold(self,"B11",1.2)

class B12_YourTurn(Scene):
    def construct(self):
        g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=35,color=INK),Text("perfect lattice, T = 0",font=MONO,font_size=34,color=TEAL),Text("filled band   vs.   partial band",font=MONO,font_size=32,color=CRIMSON),Text("Predict each transport response.",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B12")

class B13_Answer(Scene):
    def construct(self):
        left=VGroup(Text("FILLED",font=DISPLAY,font_size=32,color=INK),Text("insulating",font=SERIF,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("PARTIAL",font=DISPLAY,font_size=32,color=INK),Text("undamped ideal response",font=SERIF,font_size=29,color=TEAL)).arrange(DOWN,buff=.5).move_to(RIGHT*3); bottom=Text("band filling is the missing variable",font=SERIF,font_size=27,color=INK).shift(DOWN*2.55)
        self.play(FadeIn(left),FadeIn(right),FadeIn(bottom),run_time=1); hold(self,"B13")

class B14_CorrectTitleOutro(Scene):
    def construct(self):
        self.camera.background_color="#201F1C"; title=Text("Why a Perfect Lattice Does Not Cause Resistance",font=DISPLAY,font_size=31,color="#F2EFE8"); credit=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45)
        self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B14")
