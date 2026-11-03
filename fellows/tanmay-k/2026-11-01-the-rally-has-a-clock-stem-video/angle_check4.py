# Predict-then-find for (a) the narrow-aim column and (b) a second field geometry.
import math,re,importlib.util,sys
src=open('angle_check2.py').read().split('for vp in [1.0')[0]   # reuse the model, skip its printing
def run(W_,H_,h_,vp,ratio):
    ns={};code=src.replace("W,H,h=858.0,525.0,60.0",f"W,H,h={W_},{H_},{h_}")
    exec(code,ns);return ns['first_break'](vp,ratio)
def predict(W_,H_,h_,vp,ratio,vx0=6.0,g=0.05):
    # full aim -> half free height; narrow aim -> vy_max*T
    need=(H_-h_)/(2*W_) if ratio*W_>=H_/2*0+H_ else ratio-h_/(2*W_)
    n=math.log(vp/(need*vx0))/math.log(1+g) if vp>need*vx0 else -1
    return need,(math.floor(n)+1 if n>0 else 0)
print("narrow aim (vy<=0.25vx), field 858x525 paddle 60")
for vp in (1.0,1.5,2.0,3.0):
    need,n=predict(858,525,60,vp,0.25); print(f" vp={vp}: line {need:.3f} predicted break idx {n}  found {run(858,525,60,vp,0.25)}")
print("second field 1200x500 paddle 50, full aim (vy<=vx)")
for vp in (1.5,2.5,4.0):
    need,n=predict(1200,500,50,vp,1.0); print(f" vp={vp}: line {need:.4f} predicted break idx {n}  found {run(1200,500,50,vp,1.0)}")
