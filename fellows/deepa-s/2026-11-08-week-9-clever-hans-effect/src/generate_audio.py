from pathlib import Path
import os,json,re,wave,math,hashlib,sys
os.environ['OMP_NUM_THREADS']='4'
import numpy as np
from kokoro_onnx import Kokoro
home=Path(os.environ.get('ART_HOME',str(Path.home()/'Downloads/brutalist.art-main')))
engine=Kokoro(str(home/'runtime/models/kokoro/kokoro-v1.0.onnx'),str(home/'runtime/models/kokoro/voices-v1.0.bin'))
def write(p,a,sr):
 with wave.open(str(p),'wb') as w:
  w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
def read(p):
 with wave.open(str(p),'rb') as w:return np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(np.float32)/32767,w.getframerate()
paths=sys.argv[1:] or [str(Path(__file__).resolve().parents[1])]
for name in paths:
 p=Path(name);s=json.load(open(p/'beat_sheet.json'));(p/'audio/sentence-cache').mkdir(exist_ok=True);all_audio=[];clock=0;caps=[]
 for b in s['beats']:
  parts=[np.zeros(6000,dtype=np.float32)];local=.25;cues=[]
  for sentence in re.split(r'(?<=[.!?])\s+',b['narration_text']):
   key=hashlib.sha256(('am_onyx|1.04|'+sentence).encode()).hexdigest()[:20];cache=p/'audio/sentence-cache'/(key+'.wav')
   if cache.exists():a,sr=read(cache)
   else:a,sr=engine.create(sentence,voice='am_onyx',speed=1.04,lang='en-us');write(cache,a,sr)
   cues.append({'start':local,'end':local+len(a)/sr,'text':sentence})
   caps.append({'text':sentence,'startMs':round((clock+local)*1000),'endMs':round((clock+local+len(a)/sr)*1000),'timestampMs':None,'confidence':None})
   parts+=[a,np.zeros(round(.15*sr),dtype=np.float32)];local+=len(a)/sr+.15
  parts.append(np.zeros(round(.4*sr),dtype=np.float32));a=np.concatenate(parts);frames=math.ceil(len(a)/sr*24);a=np.pad(a,(0,round(frames/24*sr)-len(a)))
  a*=.65/max(float(np.max(np.abs(a))),.001)
  write(p/'audio'/(b['beat_id']+'.wav'),a,sr)
  dur=frames/24;b.update(start_s=clock,end_s=clock+dur,duration_s=dur,actual_duration_s=dur,frames=frames,caption_cues=cues,audio_file='audio/'+b['beat_id']+'.wav')
  clock+=dur;all_audio.append(a)
  print(p.name,b['beat_id'],dur,flush=True)
 write(p/'audio/narration.wav',np.concatenate(all_audio),sr)
 s['metadata'].update(duration_s=clock,duration_frames=round(clock*24),narration_generated=True,tts_speed=1.04,production_stage='narration_generated')
 (p/'beat_sheet.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
 (p/'captions.json').write_text(json.dumps(caps,indent=2,ensure_ascii=False)+'\n')
 print('TOTAL',p.name,clock,flush=True)
