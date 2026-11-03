import json,pathlib,re,wave,math,os,sys
os.environ['OMP_NUM_THREADS']='4'
import numpy as np
from kokoro_onnx import Kokoro
home=pathlib.Path(os.environ.get('ART_HOME', str(pathlib.Path.home()/'Downloads/brutalist.art-main')))
engine=Kokoro(str(home/'runtime/models/kokoro/kokoro-v1.0.onnx'),str(home/'runtime/models/kokoro/voices-v1.0.bin'))
def write(p,a,sr):
 with wave.open(str(p),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(a,-1,1)*32767).astype('<i2').tobytes())
for path in sys.argv[1:]:
 p=pathlib.Path(path);(p/'audio').mkdir(exist_ok=True);s=json.load(open(p/'beat_sheet.json'));all_audio=[];clock=0;sr=24000
 for b in s['beats']:
  record=p/'audio'/(b['beat_id']+'.json')
  if record.exists():
   info=json.load(open(record));a=np.frombuffer(wave.open(str(p/'audio'/(b['beat_id']+'.wav')),'rb').readframes(99999999),dtype='<i2').astype(np.float32)/32767
  else:
   sentences=re.split(r'(?<=[.!?])\s+',b['narration_text']);parts=[np.zeros(int(.3*sr),dtype=np.float32)];cues=[];local=.3
   for sentence in sentences:
    spoken=sentence.replace('XLSX','Excel').replace('openpyxl','open pie excel').replace('SKILL dot M D','skill dot em dee')
    a,sr=engine.create(spoken,voice='am_onyx',speed=1.04,lang='en-us')
    cues.append({'start':local,'end':local+len(a)/sr,'text':sentence});parts.extend([a,np.zeros(int(.2*sr),dtype=np.float32)]);local+=len(a)/sr+.2
   parts.append(np.zeros(int(.8*sr),dtype=np.float32));a=np.concatenate(parts);n=math.ceil(len(a)/sr*24);a=np.pad(a,(0,round(n/24*sr)-len(a)))
   # Normalize each scene's spoken signal to conservative headroom; final loudness normalization follows.
   peak=float(np.max(np.abs(a)));a=a*(.65/max(peak,.001))
   write(p/'audio'/(b['beat_id']+'.wav'),a,sr);info={'cues':cues,'frames':n,'duration':n/24};record.write_text(json.dumps(info,indent=2))
  b['actual_duration_s']=info['duration'];b['render_duration_s']=info['duration'];b['audio_file']='audio/'+b['beat_id']+'.wav';b['caption_cues']=info['cues'];b['start_s']=clock;b['frames']=info['frames'];clock+=info['duration'];all_audio.append(a)
  print(p.name,b['beat_id'],info['duration'],flush=True)
 write(p/'audio/narration-review.wav',np.concatenate(all_audio),sr)
 s['metadata']['duration_s']=clock;(p/'beat_sheet.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n')
 print('AUDIO COMPLETE',p.name,clock,flush=True)
