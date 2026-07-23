import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np

DUR={}
try:
    d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def cloud(center,color=TEAL,scale=1):
    rings=VGroup(*[Circle(radius=r*scale,color=color,stroke_opacity=max(.12,.65-i*.1),stroke_width=3-i*.25).move_to(center) for i,r in enumerate((.55,.9,1.25,1.6,1.95))])
    return VGroup(rings,Dot(center,color=CRIMSON,radius=.12*scale))

class B02_CloudNotVoid(Scene):
    def construct(self):
        d=DUR.get("B02",10); self.add(bg())
        title=Text("AN ATOM IS A SPREAD-OUT QUANTUM STATE",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        c=cloud(ORIGIN,TEAL,1.45); lab=Text("electron probability cloud",font=SERIF,font_size=30,color=TEAL).move_to(DOWN*3.1)
        cross=VGroup(Line(LEFT*.35+UP*.35,RIGHT*.35+DOWN*.35,color=CRIMSON,stroke_width=7),Line(LEFT*.35+DOWN*.35,RIGHT*.35+UP*.35,color=CRIMSON,stroke_width=7)).move_to(RIGHT*5+UP*.6)
        myth=Text("tiny ball in\nan empty shell",font=MONO,font_size=23,color=CRIMSON).next_to(cross,DOWN)
        self.play(FadeIn(title),LaggedStart(*[Create(x) for x in c[0]],lag_ratio=.12),FadeIn(c[1]),run_time=1.8)
        self.play(FadeIn(lab),Create(cross),FadeIn(myth),run_time=.8); self.wait(max(.1,d-2.6))

class B03_Overlap(Scene):
    def construct(self):
        d=DUR.get("B03",10); self.add(bg())
        title=Text("PUSH CLOUDS TOGETHER → ENERGY RISES",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35)
        a=cloud(LEFT*3.7,TEAL,1); b=cloud(RIGHT*3.7,CRIMSON,1)
        arr=VGroup(Arrow(LEFT*6,LEFT*4.7,color=INK),Arrow(RIGHT*6,RIGHT*4.7,color=INK))
        meter=NumberLine(x_range=[0,4,1],length=5,color=INK).move_to(DOWN*3); ml=Text("interaction energy",font=MONO,font_size=20,color=INK).next_to(meter,UP,buff=.15); dot=Dot(meter.n2p(.4),color=TEAL)
        self.play(FadeIn(title),FadeIn(a),FadeIn(b),GrowArrow(arr[0]),GrowArrow(arr[1]),run_time=1.2)
        self.play(a.animate.shift(RIGHT*2),b.animate.shift(LEFT*2),dot.animate.move_to(meter.n2p(3.5)),FadeIn(meter),FadeIn(ml),run_time=2)
        self.wait(max(.1,d-3.2))

class B04_Antisymmetry(Scene):
    def construct(self):
        d=DUR.get("B04",11); self.add(bg())
        title=Text("IDENTICAL FERMIONS: SWAP LABELS, FLIP SIGN",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
        left=VGroup(Dot(LEFT*2,color=TEAL,radius=.28),Text("1",font=MONO,font_size=24,color=GROUND).move_to(LEFT*2),Dot(RIGHT*2,color=CRIMSON,radius=.28),Text("2",font=MONO,font_size=24,color=GROUND).move_to(RIGHT*2))
        eq=Text("ψ(1,2)  =  − ψ(2,1)",font=MONO,font_size=42,color=INK).move_to(DOWN*1.8)
        paths=VGroup(ArcBetweenPoints(LEFT*2,RIGHT*2,angle=-PI/2,color=TEAL),ArcBetweenPoints(RIGHT*2,LEFT*2,angle=-PI/2,color=CRIMSON))
        self.play(FadeIn(title),FadeIn(left),run_time=.8); self.play(Create(paths),run_time=1); self.play(FadeIn(eq),Indicate(eq,color=CRIMSON),run_time=1); self.wait(max(.1,d-2.8))

class B05_PauliCard(Scene):
    def construct(self):
        d=DUR.get("B05",7); self.add(bg())
        box=RoundedRectangle(width=13,height=2.3,corner_radius=.15).set_fill(TEAL,.07).set_stroke(TEAL,2)
        t=Text("NO TWO ELECTRONS CAN OCCUPY\nTHE SAME COMPLETE QUANTUM STATE",font=DISPLAY,font_size=34,color=INK,line_spacing=1.2)
        self.add(box,t); self.wait(d)

class B06_StateSeats(Scene):
    def construct(self):
        d=DUR.get("B06",12); self.add(bg())
        title=Text("QUANTUM STATES ARE LIMITED SEATS",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35)
        seats=VGroup(); labels=VGroup()
        for i,x in enumerate((-4.5,-1.5,1.5,4.5)):
            s=RoundedRectangle(width=2.1,height=1.3,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*x)
            seats.add(s); labels.add(Text(f"state {i+1}",font=MONO,font_size=18,color=INK).next_to(s,DOWN,buff=.2))
        e1=Dot(seats[0].get_center()+LEFT*.35,color=CRIMSON,radius=.2); e2=Dot(seats[0].get_center()+RIGHT*.35,color=TEAL,radius=.2)
        spins=Text("↑   ↓",font=MONO,font_size=25,color=INK).move_to(seats[0])
        blocked=VGroup(Dot(seats[0].get_center(),color=CRIMSON,radius=.22),Text("×",font=DISPLAY,font_size=55,color=CRIMSON).move_to(seats[0].get_center()))
        self.play(FadeIn(title),LaggedStart(*[FadeIn(s) for s in seats],lag_ratio=.15),FadeIn(labels),run_time=1.4)
        self.play(FadeIn(e1),FadeIn(e2),FadeIn(spins),run_time=.7); self.play(FadeIn(blocked),Indicate(seats[1],color=TEAL),run_time=.8); self.wait(max(.1,d-2.9))

class B07_ShellSize(Scene):
    def construct(self):
        d=DUR.get("B07",11); self.add(bg())
        title=Text("EXCLUSION BUILDS SHELLS — SHELLS GIVE ATOMS SIZE",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
        levels=VGroup(*[Circle(radius=r,color=TEAL,stroke_width=3) for r in (1,1.8,2.6)])
        dots=VGroup(*[Dot(np.array([r*np.cos(a),r*np.sin(a),0]),color=CRIMSON,radius=.13) for r,n in ((1,2),(1.8,6),(2.6,8)) for a in np.linspace(0,2*np.pi,n,endpoint=False)])
        brace=Brace(levels,direction=RIGHT,color=CRIMSON); lab=Text("finite atomic size",font=MONO,font_size=22,color=CRIMSON).next_to(brace,RIGHT)
        self.play(FadeIn(title),LaggedStart(*[Create(x) for x in levels],lag_ratio=.25),run_time=1.4); self.play(LaggedStart(*[GrowFromCenter(x) for x in dots],lag_ratio=.05),GrowFromCenter(brace),FadeIn(lab),run_time=1.4); self.wait(max(.1,d-2.8))

class B08_NotAForce(Scene):
    def construct(self):
        d=DUR.get("B08",8); self.add(bg())
        top=Text("PAULI EXCLUSION ≠ AN EXTRA FORCE",font=DISPLAY,font_size=39,color=CRIMSON).move_to(UP*.8)
        sub=Text("It is a constraint on allowed many-electron states.",font=SERIF,font_size=31,color=INK).move_to(DOWN*.8)
        self.add(top,sub); self.wait(d)

class B09_EnergyCost(Scene):
    def construct(self):
        d=DUR.get("B09",12); self.add(bg())
        title=Text("DEEPER OVERLAP REQUIRES COSTLIER STATES",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        ax=Axes(x_range=[0,5,1],y_range=[0,5,1],x_length=9,y_length=5,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4)
        curve=ax.plot(lambda x:.12*np.exp(.75*x),x_range=[0,4.7],color=CRIMSON,stroke_width=5)
        xl=Text("cloud overlap →",font=MONO,font_size=22,color=INK).next_to(ax,DOWN); yl=Text("energy",font=MONO,font_size=22,color=INK).rotate(PI/2).next_to(ax,LEFT)
        note=Text("antisymmetry + Coulomb interactions",font=MONO,font_size=21,color=TEAL).move_to(UP*2.4)
        self.play(FadeIn(title),Create(ax),FadeIn(xl),FadeIn(yl),run_time=1); self.play(Create(curve),FadeIn(note),run_time=1.5); self.wait(max(.1,d-2.5))

class B10_Contact(Scene):
    def construct(self):
        d=DUR.get("B10",12); self.add(bg())
        title=Text("CONTACT FORCE IS THE SLOPE OF THAT ENERGY COST",font=DISPLAY,font_size=27,color=INK).move_to(UP*3.35)
        table=Rectangle(width=14,height=1.3).set_fill(TEAL,.18).set_stroke(TEAL,2).move_to(DOWN*2.3)
        hand=RoundedRectangle(width=6,height=1.5,corner_radius=.6).set_fill(CRIMSON,.12).set_stroke(CRIMSON,3).move_to(UP*1.4)
        atoms=VGroup(*[Circle(radius=.3,color=TEAL).move_to(RIGHT*x+DOWN*1.4) for x in np.linspace(-5,5,9)])
        down=Arrow(UP*2.8,UP*2.1,color=CRIMSON); up=Arrow(DOWN*.9,UP*.1,color=TEAL)
        labs=VGroup(Text("push",font=MONO,font_size=21,color=CRIMSON).next_to(down,RIGHT),Text("table pushes back",font=MONO,font_size=21,color=TEAL).next_to(up,RIGHT))
        self.play(FadeIn(title),FadeIn(table),FadeIn(hand),FadeIn(atoms),run_time=1.1); self.play(hand.animate.shift(DOWN*.8),GrowArrow(down),GrowArrow(up),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-2.4))

class B11_TwoPartAnswer(Scene):
    def construct(self):
        d=DUR.get("B11",10); self.add(bg())
        title=Text("THE HONEST TWO-PART ANSWER",font=DISPLAY,font_size=30,color=INK).move_to(UP*3)
        l=RoundedRectangle(width=5.8,height=2.8,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(LEFT*3.3)
        r=l.copy().set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*3.3)
        lt=Text("ELECTROMAGNETISM\nprovides the forces",font=DISPLAY,font_size=29,color=CRIMSON,line_spacing=1.2).move_to(l)
        rt=Text("ANTISYMMETRY\nrestricts the states",font=DISPLAY,font_size=29,color=TEAL,line_spacing=1.2).move_to(r)
        self.add(title,l,r,lt,rt); self.wait(d)
