from pathlib import Path
import json,subprocess,hashlib,math,re,sys
import numpy as np
from PIL import Image,ImageDraw
base=Path(__file__).resolve().parent
project=base.parent.parent
c={'stem':str(project),'progress':str(project.parent/'2026-10-26-weekly-progress-video-reviews-and-claude-skills'),'runtime':str(project/'_qc/cinematic-runtime'),'output':str(project.parents[2]/'exports/Deepa_Claude_Skills_Final')}
out=Path(c['output']);rt=Path(c['runtime']);reports=[]
def run(args):return subprocess.run(args,capture_output=True,check=True).stdout
def pcm(path):return np.frombuffer(run(['ffmpeg','-v','error','-i',str(path),'-ac','1','-ar','8000','-f','f32le','-']),dtype='<f4')
jobs=[('STEM_AI_Final_16by9.mp4','stem',1920,1080),('STEM_AI_Final_9by16.mp4','stem',1080,1920),('Weekly_Progress_Final_16by9.mp4','progress',1920,1080),('Weekly_Progress_Final_9by16.mp4','progress',1080,1920)]
for name,kind,w,h in jobs:
 if len(sys.argv)>1 and name!=sys.argv[1]:continue
 p=out/name
 prior=json.loads((rt/'final-four-qc.json').read_text()) if (rt/'final-four-qc.json').exists() else []
 cached=next((r for r in prior if r['file']==str(p) and p.exists() and r['sha256']==hashlib.sha256(p.read_bytes()).hexdigest()),None)
 if cached:
  reports.append(cached);print('REUSED VALID QC',name,flush=True);continue
 s=json.load(open(Path(c[kind])/'beat_sheet.json'))
 info=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));v=next(x for x in info['streams'] if x['codec_type']=='video')
 assert (v['width'],v['height'])==(w,h)
 assert v['codec_name']=='h264' and v['pix_fmt'] in ['yuv420p','yuvj420p'] and v['r_frame_rate']=='24/1'
 assert int(v['nb_frames'])==sum(b['frames'] for b in s['beats'])
 assert abs(float(v['duration'])-s['metadata']['duration_s'])<.002
 result=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],capture_output=True);assert result.returncode==0 and not result.stderr,result.stderr
 loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-18:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
 metrics=json.loads(re.search(r'\{\s*"input_i"[\s\S]*?\}',loud)[0]);assert -22<float(metrics['input_i'])<-15 and float(metrics['input_tp'])<=-1,metrics
 ref=pcm(Path(c[kind])/'audio/narration-review.wav');audio=pcm(p);sync=[];rms=[]
 for b in s['beats']:
  a=round((b['start_s']+.8)*8000);z=round((b['start_s']+min(9,b['actual_duration_s']-1))*8000)
  corr=float(np.corrcoef(ref[a:z],audio[a:z])[0,1]);assert corr>.93,(name,b['beat_id'],corr);sync.append(corr)
  for cue in b['caption_cues']:
   assert 0<=cue['start']<cue['end']<=b['actual_duration_s']
   a=round((b['start_s']+cue['start'])*8000);z=round((b['start_s']+cue['end'])*8000)
   val=20*math.log10(float(np.sqrt(np.mean(audio[a:z]**2)))+1e-12);assert val>-40; rms.append(val)
 assert all(b['narration_text'] in (Path(c[kind])/'SCRIPT.md').read_text() for b in s['beats'])
 contact=Image.new('RGB',(1200,math.ceil(len(s['beats'])/4)*(550 if h>w else 200)),'#333333')
 motion=[]
 for i,b in enumerate(s['beats']):
  imgs=[]
  for t in [b['start_s']+.25,b['start_s']+min(2,b['actual_duration_s']/2)]:
   raw=run(['ffmpeg','-v','error','-ss',str(t),'-i',str(p),'-frames:v','1','-vf','scale=320:-1','-f','rawvideo','-pix_fmt','rgb24','-'])
   imgs.append(np.frombuffer(raw,dtype=np.uint8))
  change=float(np.mean(np.abs(imgs[0].astype(float)-imgs[1].astype(float))));assert change>.01;motion.append(change)
  t=b['start_s']+min(9,b['actual_duration_s']/2);dest=rt/(name+'-'+str(i)+'.png')
  run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(p),'-frames:v','1',str(dest)])
  im=Image.open(dest);im.thumbnail((295,520 if h>w else 170));y=(i//4)*(550 if h>w else 200);contact.paste(im,((i%4)*300,y+25));ImageDraw.Draw(contact).text(((i%4)*300,y),b['beat_id'],fill='white')
 contact.save(rt/(name+'-contact.jpg'))
 run(['ffmpeg','-v','error','-y','-ss',str((int(v['nb_frames'])-2)/24),'-i',str(p),'-frames:v','1',str(rt/(name+'-ending.png'))])
 report={'file':str(p),'dimensions':[w,h],'duration_s':float(v['duration']),'frame_count':int(v['nb_frames']),'codec':'h264','full_decode':'PASS','audio_loudness':metrics,'minimum_narration_correlation':min(sync),'minimum_sentence_rms_db':min(rms),'motion_sample_differences':motion,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'automated_qc':'PASS'}
 reports.append(report);print(json.dumps(report),flush=True)
 Path(rt/'final-four-qc.json').write_text(json.dumps(reports,indent=2))
Path(rt/'final-four-qc.json').write_text(json.dumps(reports,indent=2))
print('AUTOMATED QC PASS: '+str(len(reports))+' outputs')
