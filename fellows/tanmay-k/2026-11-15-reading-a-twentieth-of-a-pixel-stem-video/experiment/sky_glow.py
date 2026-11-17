"""Does the width/sqrt(N) rule survive sky glow? Same line and pixels as photon_precision.py, plus a flat
background (uniform over the +/-600 km/s window) of B photons. Centre recovered with the SAME estimator
(weighted centroid refined three times), no background subtraction. Our own simulation."""
import numpy as np, json
src=open('photon_precision.py').read().split("out={'fwhm_kms'")[0]
exec(src)
WIN=600.0
def trial(n_line,n_bg,v):
    x=np.concatenate([rng.normal(v,SIG_KMS,n_line), rng.uniform(-WIN,WIN,n_bg)])
    edges=np.arange(-600,600+PIX_KMS,PIX_KMS); h,_=np.histogram(x,bins=edges); ctr=0.5*(edges[:-1]+edges[1:])
    m=(h*ctr).sum()/h.sum()
    for _ in range(3):
        w=np.exp(-0.5*((ctr-m)/(1.5*SIG_KMS))**2)*h; m=(w*ctr).sum()/w.sum()
    return m
rows=[]
for n_line in (100,1000):
    for ratio in (0,1,10):
        n_bg=n_line*ratio; errs=[]
        for _ in range(2000):
            v=rng.uniform(-PIX_KMS/2,PIX_KMS/2); errs.append(trial(n_line,n_bg,v)-v)
        e=float(np.sqrt(np.mean(np.square(errs)))); th=SIG_KMS/np.sqrt(n_line)
        rows.append({'line_photons':n_line,'background_photons':n_bg,'rms_kms':round(e,2),'rule_kms':round(float(th),2),'times_rule':round(e/th,2)})
        print(rows[-1])
json.dump(rows,open('sky_glow.json','w'),indent=1)
