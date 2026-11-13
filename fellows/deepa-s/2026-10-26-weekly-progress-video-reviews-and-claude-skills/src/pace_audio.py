from pathlib import Path
import json,subprocess,wave,math,shutil,sys
import numpy as np
p=Path(sys.argv[1]);s=json.load(open(p/'beat_sheet.json'));archive=p/'_qc/pre-pace-audio';archive.mkdir(exist_ok=True);allparts=[];clock=0;factor=1.08
for b in s['beats']:
 f=p/b['audio_file'];shutil.copy2(f,archive/f.name)
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(archive/f.name),'-af','atempo=1.08','-acodec','pcm_s16le',str(f)],check=True)
 with wave.open(str(f),'rb') as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2')
 frames=math.ceil(len(a)/sr*24);a=np.pad(a,(0,round(frames/24*sr)-len(a)))
 with wave.open(str(f),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(a.tobytes())
 for c in b['caption_cues']:c['start']/=factor;c['end']/=factor
 b.update(actual_duration_s=frames/24,render_duration_s=frames/24,frames=frames,start_s=clock);clock+=frames/24;allparts.append(a)
 (p/'audio'/(b['beat_id']+'.json')).write_text(json.dumps({'cues':b['caption_cues'],'frames':frames,'duration':frames/24},indent=2))
with wave.open(str(p/'audio/narration-review.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(np.concatenate(allparts).tobytes())
s['metadata']['duration_s']=clock;s['metadata']['audio_pace_adjustment']=1.08
(p/'beat_sheet.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n');print('Progress duration',clock)
