"""How well can a Doppler shift be measured from counted photons?
Our own simulation. Ideal case: one Gaussian emission line, no sky background, no calibration error.
Each photon lands at a random wavelength drawn from the line, is binned into detector pixels, and the
line centre is recovered from the BINNED counts only (pixels, not photon arrival times)."""
import numpy as np, json, sys
C=299792.458; LAM0=656.28            # km/s, H-alpha rest wavelength in nm (air)
FWHM_KMS=100.0                       # line width in velocity units
SIG_KMS=FWHM_KMS/2.3548
PIX_NM=0.05; PIX_KMS=PIX_NM/LAM0*C   # detector pixel in velocity units
rng=np.random.default_rng(31)

def one_trial(n_phot, v_true):
    x=rng.normal(v_true, SIG_KMS, n_phot)             # photon velocities
    edges=np.arange(-600,600+PIX_KMS,PIX_KMS)          # pixel grid, velocity units
    h,_=np.histogram(x,bins=edges); ctr=0.5*(edges[:-1]+edges[1:])
    if h.sum()==0: return np.nan
    # Gaussian least-squares centre via 3 refinement steps of weighted centroid with window around peak
    m=(h*ctr).sum()/h.sum()
    for _ in range(3):
        w=np.exp(-0.5*((ctr-m)/(1.5*SIG_KMS))**2)*h
        if w.sum()==0: break
        m=(w*ctr).sum()/w.sum()
    return m

def rms_error(n_phot, trials=2000):
    errs=[]
    for _ in range(trials):
        v=rng.uniform(-PIX_KMS/2,PIX_KMS/2)            # random sub-pixel true velocity
        errs.append(one_trial(n_phot,v)-v)
    errs=np.array(errs); return float(np.sqrt(np.nanmean(errs**2)))

out={'fwhm_kms':FWHM_KMS,'pixel_kms':PIX_KMS,'pixel_nm':PIX_NM,'rows':[]}
for n in [10,30,100,300,1000,3000,10000,100000]:
    e=rms_error(n, 2000 if n<=10000 else 400)
    th=SIG_KMS/np.sqrt(n)
    out['rows'].append({'photons':n,'rms_kms':round(e,3),'theory_sigma_over_sqrtN':round(float(th),3),'ratio':round(e/th,2),'pixels_fraction':round(e/PIX_KMS,4)})
    print(out['rows'][-1])
print('pixel (km/s):',round(PIX_KMS,2),' sigma_line (km/s):',round(SIG_KMS,2))
# Andromeda-sized shift in nm
for v in (110,300): print(v,'km/s ->',round(LAM0*v/C,3),'nm =',round(LAM0*v/C/PIX_NM,2),'pixels')
json.dump(out,open('photon_precision.json','w'),indent=1)
