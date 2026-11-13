from pathlib import Path
import json,subprocess,hashlib,sys,math,re,importlib.util
import numpy as np
from PIL import Image
p=Path(sys.argv[1]);s=json.load(open(p/'beat_sheet.json'));out=p/'mp4'/s['metadata']['output_filename'];q=p/'_qc';results={}
def cmd(args):return subprocess.run(args,capture_output=True,check=True).stdout
info=json.loads(cmd(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(out)]))
v=next(x for x in info['streams'] if x['codec_type']=='video');a=next(x for x in info['streams'] if x['codec_type']=='audio')
results['dimensions']=[v['width'],v['height']];assert results['dimensions']==[1920,1080]
assert v['codec_name']=='h264' and v['pix_fmt']=='yuv420p' and v['r_frame_rate']=='24/1'
duration=float(info['format']['duration']);assert abs(duration-s['metadata']['duration_s'])<1/24+.005
results['duration_s']=duration;results['video_frames']=int(v['nb_frames']);assert int(v['nb_frames'])==sum(b['frames'] for b in s['beats'])
r=subprocess.run(['ffmpeg','-hide_banner','-v','error','-i',str(out),'-f','null','-'],capture_output=True);assert r.returncode==0 and not r.stderr;results['full_decode']='PASS'
r=subprocess.run(['ffmpeg','-hide_banner','-i',str(out),'-af','loudnorm=I=-18:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True);assert r.returncode==0
(q/'final-loudness.log').write_text(r.stderr);metrics=json.loads(re.search(r'\{\s*"input_i"[\s\S]*?\}',r.stderr)[0]);assert -22<float(metrics['input_i'])<-15 and float(metrics['input_tp'])<=-1
results['audio_loudness']=metrics
def pcm(path):return np.frombuffer(cmd(['ffmpeg','-v','error','-i',str(path),'-ac','1','-ar','8000','-f','f32le','-']),dtype='<f4')
ref=pcm(p/'audio/narration-review.wav');final=pcm(out);assert abs(len(ref)-len(final))<=2000
sync=[];audible=[]
for b in s['beats']:
 begin=round((b['start_s']+.8)*8000);end=round((b['start_s']+min(9,b['actual_duration_s']-1))*8000)
 x=ref[begin:end];y=final[begin:end];c=float(np.corrcoef(x,y)[0,1]);assert c>.93,(b['beat_id'],c)
 sync.append({'beat':b['beat_id'],'correlation':c})
 for cue in b['caption_cues']:
  start=round((b['start_s']+cue['start'])*8000);stop=round((b['start_s']+cue['end'])*8000);rms=20*math.log10(float(np.sqrt(np.mean(final[start:stop]**2)))+1e-12);assert rms>-40,(cue['text'],rms);audible.append(rms)
results['audio_sync']=sync;results['quietest_sentence_rms_db']=min(audible)
# Compare native rendered frames against deterministic expected source at scene entry/middle/end.
spec=importlib.util.spec_from_file_location('graphics',p/'src/render.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
samples=[];contacts=[]
for i,b in enumerate(s['beats']):
 base=m.background(b,i,len(s['beats']));cs=m.cards(b);caps=[(c,m.caption(c['text'])) for c in b['caption_cues']]
 for frame_no in [1,int(b['frames']*.5),b['frames']-2]:
  local=frame_no/24;t=b['start_s']+local
  raw=cmd(['ffmpeg','-v','error','-ss',f'{t:.6f}','-i',str(out),'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'])
  actual=np.frombuffer(raw,dtype=np.uint8).reshape((1080,1920,3));expected=np.asarray(m.frame(base,cs,caps,local,b['actual_duration_s'],b),dtype=np.uint8)
  mae=float(np.mean(np.abs(actual.astype(np.float32)-expected.astype(np.float32))));assert mae<5,(b['beat_id'],frame_no,mae)
  samples.append({'beat':b['beat_id'],'time':t,'pixel_mae':mae})
  if frame_no==int(b['frames']*.5):contacts.append(Image.fromarray(actual))
results['motion_timing_and_cuts']=samples
contact=Image.new('RGB',(960,270*math.ceil(len(contacts)/2)),m.BG)
for i,im in enumerate(contacts):im.thumbnail((480,270));contact.paste(im,((i%2)*480,(i//2)*270))
contact.save(q/'final-contact.jpg',quality=94)
# Check full-sheet narration agreement and every caption fit; no word-level timing is claimed.
script=(p/'SCRIPT.md').read_text();assert all(b['narration_text'] in script for b in s['beats'])
assert all(c['end']<=b['actual_duration_s'] for b in s['beats'] for c in b['caption_cues'])
results['sha256']=hashlib.sha256(out.read_bytes()).hexdigest();results['path']=str(out);results['status']='PASS'
(q/'final-qc.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'path':str(out),'duration':duration,'dimensions':results['dimensions'],'sha256':results['sha256'],'status':'PASS'},indent=2),flush=True)
