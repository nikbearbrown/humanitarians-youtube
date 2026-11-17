"""Illustrative toy disk: how the velocity error bar grows outward when light falls off.
ASSUMPTIONS (ours, labelled on screen): exponential disk, scale length 3 kpc; the centre ring collects 100,000
photons in the line; each ring's photons scale as exp(-R/3 kpc); line width 100 km/s everywhere; error = sigma_line/sqrt(N)*1.08
(1.08 = binning factor measured in photon_precision.py). Nothing here is a measured galaxy."""
import numpy as np, json
SIG=100/2.3548; RD=3.0; N0=100000; K=1.08
rows=[]
for R in [1,3,5,8,11,15]:
    N=N0*np.exp(-R/RD); e=K*SIG/np.sqrt(N); rows.append({'R_kpc':R,'photons':int(N),'err_kms':round(float(e),2)})
    print(rows[-1])
print('edge/centre error ratio (R=15 vs R=1):',round(rows[-1]['err_kms']/rows[0]['err_kms'],1))
json.dump(rows,open('rotation_bars.json','w'),indent=1)
