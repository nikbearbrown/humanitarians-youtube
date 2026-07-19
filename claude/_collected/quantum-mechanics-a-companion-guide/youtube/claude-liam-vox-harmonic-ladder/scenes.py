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
def rung(y,width=6,color=INK): return Line(LEFT*width/2,RIGHT*width/2,color=color,stroke_width=3).move_to(UP*y)

class B02_Factorization(Scene):
    def construct(self):
        dur=DUR.get("B02",12); self.add(bg())
        title=Text("THE PARABOLA HIDES AN OPERATOR PAIR",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
        axes=VGroup(Line(LEFT*5.8,RIGHT*.2,color=INK).shift(DOWN*2.1),Line(DOWN*2.2,UP*2.5,color=INK).shift(LEFT*2.8))
        pot=ParametricFunction(lambda x:np.array([x-2.8,.16*x*x-2.1,0]),t_range=[-3,3,.04],color=TEAL,stroke_width=4)
        xop=RoundedRectangle(width=2.2,height=1.2,corner_radius=.12).set_fill(CRIMSON,.08).set_stroke(CRIMSON,2).move_to(RIGHT*2.1+UP*.8)
        pop=xop.copy().set_fill(TEAL,.08).set_stroke(TEAL,2).move_to(RIGHT*5+UP*.8)
        xl=Text("x̂",font=MONO,font_size=42,color=CRIMSON).move_to(xop); pl=Text("p̂",font=MONO,font_size=42,color=TEAL).move_to(pop)
        arrows=VGroup(Arrow(xop.get_right(),ORIGIN+RIGHT*3.45,buff=.1,color=INK),Arrow(pop.get_left(),ORIGIN+RIGHT*3.65,buff=.1,color=INK))
        pair=Text("a₋   a₊",font=MONO,font_size=38,color=INK).move_to(RIGHT*3.55+DOWN*.8)
        self.play(FadeIn(title),Create(axes),Create(pot),run_time=1.3); self.play(FadeIn(xop),FadeIn(pop),FadeIn(xl),FadeIn(pl),run_time=.7)
        self.play(Create(arrows),FadeIn(pair),run_time=.8); self.wait(max(.1,dur-2.8))

class B03_HamiltonianCard(Scene):
    def construct(self):
        dur=DUR.get("B03",11); self.add(bg())
        title=Text("THE WHOLE SPECTRUM IN ONE LINE",font=DISPLAY,font_size=25,color=TEAL).move_to(UP*2.6)
        box=RoundedRectangle(width=12,height=2,corner_radius=.14).set_fill(TEAL,.07).set_stroke(TEAL,2)
        eq=Text("H = ℏω ( N + 1/2 )",font=MONO,font_size=48,color=INK)
        sub=Text("N counts quanta • 1/2 survives at the bottom",font=SERIF,font_size=27,color=CRIMSON).move_to(DOWN*2.1)
        self.play(FadeIn(title),Create(box),run_time=.7); self.play(Write(eq),FadeIn(sub),run_time=1); self.wait(max(.1,dur-1.7))

class B04_Raising(Scene):
    def construct(self):
        dur=DUR.get("B04",12); self.add(bg())
        title=Text("a₊ ADDS EXACTLY ONE ℏω",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35)
        rs=VGroup(*[rung(-2.2+i*1.05,6,TEAL) for i in range(5)])
        labs=VGroup(*[Text(f"n={i}",font=MONO,font_size=20,color=INK).next_to(rs[i],LEFT,buff=.3) for i in range(5)])
        gaps=VGroup(*[DoubleArrow(RIGHT*3.3+UP*(-2.2+i*1.05),RIGHT*3.3+UP*(-1.15+i*1.05),buff=.1,color=CRIMSON,stroke_width=2) for i in range(4)])
        gl=VGroup(*[Text("ℏω",font=MONO,font_size=18,color=CRIMSON).next_to(gaps[i],RIGHT,buff=.15) for i in range(4)])
        dot=Dot(rs[0].get_center(),color=INK,radius=.15)
        self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rs],lag_ratio=.12),FadeIn(labs),run_time=1.5)
        self.play(FadeIn(gaps),FadeIn(gl),GrowFromCenter(dot),run_time=.7)
        for i in range(1,5): self.play(dot.animate.move_to(rs[i].get_center()),run_time=.65)
        self.wait(max(.1,dur-4.8))

class B05_Mechanism(Scene):
    def construct(self):
        d=DUR.get("B05",3); self.add(bg(),RoundedRectangle(width=12,height=1.6,corner_radius=.12).set_fill(TEAL,.07).set_stroke(TEAL,2),Text("ONE OPERATOR • ONE QUANTUM • ONE RUNG",font=DISPLAY,font_size=34,color=INK)); self.wait(d)

class B06_LoweringStops(Scene):
    def construct(self):
        dur=DUR.get("B06",12); self.add(bg())
        title=Text("a₋ LOWERS — UNTIL THE GROUND STATE STOPS IT",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
        rs=VGroup(*[rung(-2+i*1.1,6,TEAL) for i in range(5)]); labs=VGroup(*[Text(f"|{i}〉",font=MONO,font_size=22,color=INK).next_to(rs[i],LEFT,buff=.3) for i in range(5)])
        dot=Dot(rs[4].get_center(),color=CRIMSON,radius=.16); stop=Line(LEFT*.6,RIGHT*.6,color=CRIMSON,stroke_width=8).move_to(rs[0].get_center()+DOWN*.55)
        zero=Text("a₋|0〉 = 0",font=MONO,font_size=32,color=CRIMSON).move_to(RIGHT*4+DOWN*2)
        self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rs],lag_ratio=.1),FadeIn(labs),GrowFromCenter(dot),run_time=1.3)
        for i in (3,2,1,0): self.play(dot.animate.move_to(rs[i].get_center()),run_time=.65)
        self.play(Create(stop),FadeIn(zero),Indicate(dot,color=CRIMSON),run_time=1)
        self.wait(max(.1,dur-4.9))

class B07_HalfIntegerSpectrum(Scene):
    def construct(self):
        dur=DUR.get("B07",12); self.add(bg())
        title=Text("THE BOTTOM IS 1/2 ℏω — EVERY GAP IS ℏω",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
        vals=("1/2","3/2","5/2","7/2","9/2")
        rs=VGroup(*[rung(-2.2+i*1.05,7,TEAL) for i in range(5)])
        labs=VGroup(*[Text(f"E{i} = {vals[i]} ℏω",font=MONO,font_size=22,color=INK).next_to(rs[i],LEFT,buff=.25) for i in range(5)])
        brackets=VGroup(*[BraceBetweenPoints(RIGHT*4+UP*(-2.2+i*1.05),RIGHT*4+UP*(-1.15+i*1.05),direction=RIGHT,color=CRIMSON) for i in range(4)])
        gl=VGroup(*[Text("ℏω",font=MONO,font_size=18,color=CRIMSON).next_to(brackets[i],RIGHT,buff=.1) for i in range(4)])
        self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rs],lag_ratio=.1),FadeIn(labs),run_time=1.5)
        self.play(LaggedStart(*[GrowFromCenter(b) for b in brackets],lag_ratio=.15),FadeIn(gl),run_time=1.1)
        self.wait(max(.1,dur-2.6))

class B08_Implication(Scene):
    def construct(self):
        d=DUR.get("B08",3); self.add(bg(),Text("THE BOTTOM IS NOT ZERO.  THE SPACING NEVER CHANGES.",font=DISPLAY,font_size=33,color=INK)); self.wait(d)

class B09_NodeSequence(Scene):
    def construct(self):
        dur=DUR.get("B09",11); self.add(bg())
        title=Text("RAISING ADDS ONE NODE",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35)
        rows=VGroup(); labels=VGroup()
        for n in range(4):
            y=1.9-n*1.25
            def psi(x, n=n):
                z=x/1.45
                poly=(1, z, z*z-1, z*z*z-3*z)[n]
                return .52*poly*np.exp(-z*z/2)
            f=ParametricFunction(lambda x,n=n,y=y:np.array([x,y+psi(x,n),0]),t_range=[-5,5,.04],color=TEAL,stroke_width=3)
            rows.add(f); labels.add(Text(f"n={n}   nodes={n}",font=MONO,font_size=20,color=INK).move_to(LEFT*6.1+UP*y))
        arrows=VGroup(*[Arrow(RIGHT*5.4+UP*(1.9-i*1.25),RIGHT*5.4+UP*(.65-i*1.25),color=CRIMSON,buff=.15) for i in range(3)])
        self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rows],lag_ratio=.2),FadeIn(labels),run_time=2.2)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.2),run_time=1); self.wait(max(.1,dur-3.2))

class B10_WorkedPath(Scene):
    def construct(self):
        dur=DUR.get("B10",15); self.add(bg())
        title=Text("RAISE THREE TIMES — LOWER ONCE",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        rs=VGroup(*[rung(-2+i*1.25,7,TEAL) for i in range(4)]); labs=VGroup(*[Text(f"n={i}   E=({2*i+1}/2)ℏω",font=MONO,font_size=21,color=INK).next_to(rs[i],LEFT,buff=.25) for i in range(4)])
        dot=Dot(rs[0].get_center(),color=CRIMSON,radius=.17); history=VGroup()
        self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rs],lag_ratio=.1),FadeIn(labs),GrowFromCenter(dot),run_time=1.3)
        for i in (1,2,3):
            a=Arrow(rs[i-1].get_center()+RIGHT*2.2,rs[i].get_center()+RIGHT*2.2,color=CRIMSON,buff=.15)
            history.add(a); self.play(GrowArrow(a),dot.animate.move_to(rs[i].get_center()),run_time=.8)
        down=Arrow(rs[3].get_center()+RIGHT*3,rs[2].get_center()+RIGHT*3,color=TEAL,buff=.15)
        self.play(GrowArrow(down),dot.animate.move_to(rs[2].get_center()),run_time=1)
        verdict=Text("+ℏω  +ℏω  +ℏω  −ℏω",font=MONO,font_size=27,color=INK).move_to(DOWN*3.25)
        self.play(FadeIn(verdict),run_time=.5); self.wait(max(.1,dur-5.2))

class B11_Recap(Scene):
    def construct(self):
        dur=DUR.get("B11",14); self.add(bg())
        title=Text("THE ANSWER",font=DISPLAY,font_size=22,color=TEAL).move_to(UP*2.8)
        box=RoundedRectangle(width=12.5,height=2.4,corner_radius=.12).set_fill(TEAL,.07).set_stroke(TEAL,2)
        ans=Text("Factorization creates operators that change\nenergy by one fixed quantum:  ℏω.",font=DISPLAY,font_size=31,color=INK,line_spacing=1.25)
        kick=Text("THE SAME IDEA BECOMES CREATION / ANNIHILATION",font=MONO,font_size=21,color=CRIMSON).move_to(DOWN*2.4)
        self.play(FadeIn(title),Create(box),run_time=.7); self.play(FadeIn(ans),FadeIn(kick),run_time=.7); self.wait(max(.1,dur-1.4))
