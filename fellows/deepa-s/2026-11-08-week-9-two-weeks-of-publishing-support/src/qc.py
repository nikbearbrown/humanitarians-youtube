import sys,json,subprocess,hashlib,math
from pathlib import Path
import numpy as np
from PIL import ImageFont

def run(args):return subprocess.run(args,check=True,capture_output=True).stdout
p=Path(sys.argv[1]);s=json.loads((p/'beat_sheet.json').read_text());m=s['metadata'];caps=json.loads((p/'captions.json').read_text());out=[]
def pcm(f):return np.frombuffer(run(['ffmpeg','-v','error','-i',str(f),'-vn','-ac','1','-ar','8000','-f','f32le','-']),dtype='<f4')
original=pcm(p/'audio/narration.wav')
assert len(original)/8000==m['duration_frames']/24 or abs(len(original)/8000-m['duration_s'])<.001
for portrait in [False,True]:
 aspect='9x16' if portrait else '16x9';f=(Path(sys.argv[2]) if len(sys.argv)>2 else p/('vertical/mp4' if portrait else 'mp4'))/f"Week{m['week']}_{m['category']}_{aspect}.mp4"
 assert f.exists(),f
 probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio');dur=float(v['duration']);dims=(1080,1920) if portrait else (1920,1080)
 assert (v['width'],v['height'])==dims and v['codec_name']=='h264' and v['r_frame_rate']=='24/1'
 assert int(v['nb_frames'])==m['duration_frames'] and abs(dur-m['duration_s'])<.001 and 175<=dur<=185
 assert abs(float(a['duration'])-dur)<.05
 dec=subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(f),'-f','null','-'],capture_output=True);assert dec.returncode==0 and not dec.stderr,dec.stderr
 loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(f),'-vn','-af','loudnorm=I=-18:TP=-2:LRA=9:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
 stats=json.JSONDecoder().raw_decode(loud[loud.rfind('{'):])[0];assert -21<=float(stats['input_i'])<=-15 and float(stats['input_tp'])<=-1
 audio=pcm(f);corr=[];rms=[]
 for b in s['beats']:
  lo=round(b['start_s']*8000);hi=min(round(b['end_s']*8000),len(audio),len(original));corr.append(float(np.corrcoef(original[lo:hi],audio[lo:hi])[0,1]))
 assert min(corr)>.97,corr
 for c in caps:
  lo=round(c['startMs']*8);hi=min(round(c['endMs']*8),len(audio));rms.append(float(20*np.log10(np.sqrt(np.mean(audio[lo:hi]**2))+1e-10)))
 assert min(rms)>-40,rms
 # Sample motion throughout every scene, excluding start/end transitions.
 ww,hh=(90,160) if portrait else (160,90)
 arr=np.frombuffer(run(['ffmpeg','-v','error','-i',str(f),'-an','-vf',f'fps=2,scale={ww}:{hh},format=gray','-f','rawvideo','-']),dtype=np.uint8).reshape(-1,hh,ww).astype(float)
 dif=np.mean(np.abs(np.diff(arr,axis=0)),axis=(1,2));motion=[]
 for b in s['beats']:
  seg=dif[math.ceil((b['start_s']+1)*2):math.floor((b['end_s']-1)*2)];motion.append(float(np.max(seg)));assert max(seg)>.03
 # Check caption wrapping and header vertical allocation with actual font metrics.
 font=ImageFont.truetype(str(p/'public/fonts/Montserrat-Medium.ttf'),29);maxwidth=950 if portrait else 1720;maxlines=0
 for c in caps:
  lines=['']
  for word in c['text'].split():
   if font.getlength((lines[-1]+' '+word).strip())>maxwidth:lines.append(word)
   else:lines[-1]=(lines[-1]+' '+word).strip()
  maxlines=max(maxlines,len(lines))
 assert maxlines<=4 if portrait else maxlines<=2
 header=ImageFont.truetype(str(p/'public/fonts/EBGaramond-Regular.ttf'),72 if portrait else 78)
 for b in s['beats']:
  lines=['']
  for word in b['heading'].split():
   if header.getlength((lines[-1]+' '+word).strip())>(950 if portrait else 1720):lines.append(word)
   else:lines[-1]=(lines[-1]+' '+word).strip()
  assert len(lines)<=2 if portrait else len(lines)<=1
 rec={'file':str(f),'width':dims[0],'height':dims[1],'fps':24,'duration_s':dur,'frames':int(v['nb_frames']),'codec':v['codec_name'],'audio_codec':a['codec_name'],'integrated_lufs':stats['input_i'],'true_peak_dbtp':stats['input_tp'],'minimum_scene_audio_correlation':min(corr),'minimum_narrated_sentence_rms_dbfs':min(rms),'motion_maxima_per_scene':motion,'max_caption_lines':maxlines,'full_decode':'PASS','sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'automated_qc':'PASS'};out.append(rec);print(json.dumps(rec),flush=True)
((Path(sys.argv[2]) if len(sys.argv)>2 else p/'_qc')/'technical-qc.json').write_text(json.dumps(out,indent=2)+'\n')
