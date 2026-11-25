# Does 'no perfect defense' reduce to one inequality?  Our own simulation, no outside data.
import numpy as np
W,H,h=858.0,525.0,60.0   # field, paddle height (arbitrary Pong-like proportions)
def fold(y):
    p=2*H; y=y%p
    return np.where(y>H,p-y,y)
def defender_ok(vx,vp,k,y_a,n=2001):
    T=W/vx
    vmax=k*(h/2)            # contact offset sets vy (k per unit offset)
    vys=np.linspace(-vmax,vmax,n)
    land=fold(y_a+vys*T)
    y_d=(land.min()+land.max())/2     # best waiting spot
    need=np.abs(land-y_d).max()
    return need<=vp*T+h/2
def perfect(vx,vp,k):
    # perfect only if defender survives every arrival height
    return all(defender_ok(vx,vp,k,y) for y in np.linspace(0,H,41))
k=12.0   # vy per unit paddle offset, in units of vx
for vx in [4,6,8,12]:
    thr=(H-h)/(2*W)*vx
    lo=[vp for vp in np.linspace(0.05,vx,400) if perfect(vx,vp,k/ (1) *0+k*vx/ vx)]
    sim=lo[0] if lo else None
    print(f"vx={vx:>2}  predicted vp*={thr:5.2f}  measured vp*={sim if sim is None else round(sim,2)}  ratio={None if sim is None else round(sim/vx,3)}")
