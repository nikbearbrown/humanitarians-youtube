import json,pathlib,subprocess,wave,hashlib,math,re,sys
import numpy as np
import os
base=pathlib.Path(__file__).resolve().parent
project=base.parent.parent
progress=project.parent/'2026-10-26-weekly-progress-video-reviews-and-claude-skills'
c={'stem':str(project),'progress':str(progress),'src':str(base),'runtime':str(project/'_qc/cinematic-runtime'),'output':str(project.parents[2]/'exports/Deepa_Claude_Skills_Final')}

rt=pathlib.Path(c['runtime']);out=pathlib.Path(c['output'])
s=json.load(open(c['src']+'/sheet.json'));sr=48000
signal=np.zeros(round(s['metadata']['duration_s']*sr),dtype=np.float32)
rng=np.random.default_rng(24)
for b in s['beats']:
 start=round(b['start_s']*sr)
 n=int(.18*sr);t=np.arange(n)/sr
 wavelet=(np.sin(2*np.pi*(480*t+800*t*t))*.65+rng.normal(0,.12,n))*np.sin(np.pi*np.arange(n)/n)**2*.004
 signal[start:start+n]+=wavelet[:len(signal[start:start+n])]
with wave.open(str(rt/'subtle-transitions.wav'),'wb') as w:
 w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((signal*32767).astype('<i2').tobytes())
jobs=[('STEMwide','STEM_AI_Final_16by9.mp4',c['stem']+'/mp4/STEM_AI_Claude_Skills_16by9.mp4',177.70833333333334),('STEMtall','STEM_AI_Final_9by16.mp4',c['stem']+'/mp4/STEM_AI_Claude_Skills_16by9.mp4',177.70833333333334),('Progresstall','Weekly_Progress_Final_9by16.mp4',c['progress']+'/mp4/Weekly_Progress_Report_16by9.mp4',235.83333333333334)]
for id,name,audio,duration in jobs:
 if len(sys.argv)>1 and id!=sys.argv[1]:continue
 assert (rt/(id+'.mp4')).exists(),id
 cmd=['ffmpeg','-v','error','-y','-i',str(rt/(id+'.mp4')),'-i',audio]
 if id.startswith('STEM'):
  cmd+=['-i',str(rt/'subtle-transitions.wav'),'-filter_complex','[1:a][2:a]amix=inputs=2:duration=first:normalize=0[a]','-map','0:v','-map','[a]','-c:a','aac','-b:a','192k']
 else:cmd+=['-map','0:v','-map','1:a','-c:a','copy']
 cmd+=['-c:v','copy','-t',str(duration),'-movflags','+faststart',str(out/name)]
 subprocess.run(cmd,check=True);print('MUXED',name,flush=True)
