# Stricter check: discrete time, discrete paddle moves, ball speeds up g per hit, wall bounces,
# attacker searches every aim for the one the defender can't reach; defender waits mid-field then runs.
import math
W,H,h=858.0,525.0,60.0
vx0,g=6.0,0.0
k=40.0              # vy per unit offset fraction (offset in [-1,1] of half paddle) in units of vx -> reach
def fold(y):
    p=2*H;y%=p;return p-y if y>H else y
def lands(vx,y_a,vy_max,n=801):
    T=W/vx
    return [fold(y_a+(-vy_max+2*vy_max*i/(n-1))*T) for i in range(n)]
def defends(vx,vp,y_a,vy_max):
    T=int(round(W/vx));L=lands(vx,y_a,vy_max)
    y_d=(min(L)+max(L))/2
    worst=max(abs(l-y_d) for l in L)
    # discrete: paddle moves vp per tick for T ticks, covers paddle half-height on arrival
    return worst<=vp*T+h/2
def first_break(vp,vy_over_vx):
    for n in range(0,200):
        vx=vx0*(1+g)**n
        vy_max=vy_over_vx*vx
        if not all(defends(vx,vp,y,vy_max) for y in [i*H/20 for i in range(21)]):
            return n,round(vx,2)
    return None
for vp in [1.0,1.5,2.0,3.0]:
    print(f"vp={vp}: first hit at which some serve cannot be defended -> {first_break(vp,1.0)} (aim limited to vy<=vx)  | {first_break(vp,0.25)} (vy<=0.25vx)")
# closed form prediction for full-aim: hits until vp*W/vx < (H-h)/2
for vp in [1.0,1.5,2.0,3.0]:
    n=math.log(vp*2*W/((H-h)*vx0))/math.log(1+g)
    print(f"vp={vp}: closed-form break after n={n:.1f} hits (full aim)")
