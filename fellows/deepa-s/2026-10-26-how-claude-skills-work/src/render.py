from pathlib import Path
import json,math,subprocess,sys,hashlib,os
from PIL import Image,ImageDraw,ImageFont
W,H,FPS=1920,1080,24
BG='#F3EBDD';INK='#2F2A26';TEAL='#1F4E5F';NAVY='#29335C';ORANGE='#E4572E'
HOME=Path(os.environ.get('ART_HOME', str(Path.home()/'Downloads/brutalist.art-main')))
fonts=HOME/'runtime/fonts'
def font(size,bold=False,serif=False):
 name='EB_Garamond/static/EBGaramond-Medium.ttf' if serif else 'Montserrat/static/Montserrat-'+('Bold' if bold else 'Medium')+'.ttf'
 return ImageFont.truetype(str(fonts/name),size)
def lines(text,ft,width):
 out=[];line=''
 for word in text.split():
  test=(line+' '+word).strip()
  if ft.getlength(test)>width and line:out.append(line);line=word
  else:line=test
 if line:out.append(line)
 return out
checks=[]
def label(draw,text,xy,ft,width,leading,fill=INK,maxlines=3):
 ls=lines(text,ft,width);assert len(ls)<=maxlines,(text,len(ls),maxlines)
 x,y=xy
 for i,line in enumerate(ls):draw.text((x,y+i*leading),line,font=ft,fill=fill,stroke_width=0)
 checks.append({'text':text,'x':x,'y':y,'width':max(ft.getlength(z) for z in ls),'lines':len(ls),'height':len(ls)*leading})
 return len(ls)*leading
def icon(d,kind,x,y,col):
 # Original vector-like diagrams, built from primitives.
 if kind==0:
  d.rectangle((x,y,x+110,y+80),outline=col,width=5);d.line((x,y+21,x+110,y+21),fill=col,width=4)
  for q in range(3):d.ellipse((x+10+q*13,y+8,x+15+q*13,y+13),fill=col)
  d.line((x+20,y+43,x+44,y+43),fill=col,width=6);d.line((x+20,y+61,x+86,y+61),fill=col,width=6)
 elif kind==1:
  d.rectangle((x,y,x+100,y+84),outline=col,width=5)
  for q in range(1,3):d.line((x+q*33,y,x+q*33,y+84),fill=col,width=3);d.line((x,y+q*28,x+100,y+q*28),fill=col,width=3)
 elif kind==2:
  d.ellipse((x,y,x+82,y+82),outline=col,width=5);d.line((x+61,y+64,x+108,y+109),fill=col,width=7);d.line((x+18,y+41,x+33,y+56,x+63,y+25),fill=col,width=5)
 elif kind==3:
  for q in range(3):d.rectangle((x+q*15,y+q*10,x+80+q*15,y+65+q*10),outline=col,width=4)
  d.polygon([(x+47,y+36),(x+47,y+68),(x+73,y+52)],fill=col)
 else:
  for q in range(3):d.rectangle((x+q*40,y+q*12,x+24+q*40,y+65),fill=col)
def background(b,i,total):
 im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
 d.rectangle((96,72,108,112),fill=ORANGE)
 d.text((130,73),'HUMANITARIANS AI',font=font(28,True),fill=TEAL)
 d.text((1400,77),'DEEPA S.  /  '+str(i+1).zfill(2)+'—'+str(total).zfill(2),font=font(25),fill=TEAL)
 d.line((96,137,1824,137),fill=TEAL,width=2)
 d.text((100,174),b['section'],font=font(27,True),fill=TEAL)
 label(d,b['heading'],(96,220),font(76,serif=True),1720,88,maxlines=2)
 d.text((100,995),'@HumanitariansAI',font=font(27,True),fill=TEAL)
 d.text((1330,995),'Liam, narrating for Deepa.',font=font(24),fill=TEAL)
 return im
def cards(b):
 out=[]
 for j,txt in enumerate(b['labels']):
  im=Image.new('RGBA',(540,340),(0,0,0,0));d=ImageDraw.Draw(im)
  col=TEAL if j!=1 else NAVY
  d.rectangle((2,2,537,337),fill='#FFFAF1',outline=col,width=3)
  d.rectangle((2,2,537,9),fill=col)
  d.text((35,35),str(j+1).zfill(2),font=font(27,True),fill=col)
  icon(d,(1 if 'XLSX' in b['heading'] else 3 if 'GIF' in b['heading'] else 0 if 'Artifacts' in b['heading'] else 2 if 'Testing' in b['heading'] or 'review' in b['heading'].lower() else j),355,34,col)
  label(d,txt,(35,172),font(43,True),465,57,fill=col,maxlines=2)
  out.append(im)
 return out
def caption(text):
 im=Image.new('RGBA',(1728,172),(0,0,0,0));d=ImageDraw.Draw(im)
 ls=lines(text,font(36),1660);assert len(ls)<=4,(text,ls)
 if text:
  d.rounded_rectangle((0,0,1727,171),radius=6,fill=NAVY)
  for j,line in enumerate(ls):
   ft=font(36);x=(1728-ft.getlength(line))/2;d.text((x, (172-len(ls)*43)/2+j*43-5),line,font=ft,fill='#FFFFFF')
 return im
def frame(base,cs,caps,t,seconds,b):
 im=base.copy();d=ImageDraw.Draw(im)
 for j,c in enumerate(cs):
  u=min(1,max(0,(t-j*.2)/.6));ease=1-(1-u)**3
  im.paste(c,(96+j*594,420+round(22*(1-ease))),c)
  if j<2 and b['section'] not in ['WHAT I DID','WHAT I LEARNED','KEY TAKEAWAYS']:
   x=648+j*594;d.line((x,590,x+25,590),fill=TEAL,width=4);d.polygon([(x+25,582),(x+36,590),(x+25,598)],fill=TEAL)
 # Discrete flow dot moves steadily; labels never move outside their safe boxes.
 x=106+int((t%5)/5*1700);d.line((100,784,1820,784),fill='#C8C3B8',width=2);d.ellipse((x-5,779,x+5,789),fill=TEAL)
 for cue,cap in caps:
  if cue['start']<=t<cue['end']:im.paste(cap,(96,798),cap);break
 d.rectangle((96,1056,96+int(1728*min(1,t/seconds)),1061),fill=TEAL)
 return im
def run(p,preview=False):

 for directory in ['media','mp4','_qc']:(p/directory).mkdir(exist_ok=True)
 sheet=json.load(open(p/'beat_sheet.json'));previews=[]
 for i,b in enumerate(sheet['beats']):
  duration=b.get('actual_duration_s',20);frames=b.get('frames',round(duration*FPS));base=background(b,i,len(sheet['beats']));cs=cards(b);caps=[(c,caption(c['text'])) for c in b.get('caption_cues',[])]
  prev=p/'_qc'/(b['beat_id']+'-preview.jpg');frame(base,cs,caps,min(5,duration/2),duration,b).save(prev,quality=92);previews.append(prev)
  if preview:continue
  out=p/'media'/(b['beat_id']+'.mp4')
  if out.exists():print('REUSE',out,flush=True);continue
  cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','24','-i','-','-an','-c:v','libx264','-preset','ultrafast','-crf','19','-pix_fmt','yuv420p','-threads','4',str(out)]
  proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
  for k in range(frames):proc.stdin.write(frame(base,cs,caps,k/FPS,duration,b).tobytes())
  proc.stdin.close();assert proc.wait()==0;print('SCENE',p.name,b['beat_id'],duration,flush=True)
 contact=Image.new('RGB',(960,270*math.ceil(len(previews)/2)),BG)
 for i,q in enumerate(previews):
  im=Image.open(q);im.thumbnail((480,270));contact.paste(im,((i%2)*480,(i//2)*270))
 contact.save(p/'_qc/contact.jpg',quality=92)
 (p/'_qc/layout.json').write_text(json.dumps(checks,indent=2))
 if preview:return
 listing=p/'_qc/concat.txt';listing.write_text(''.join("file '"+str(p/'media'/(b['beat_id']+'.mp4'))+"'\n" for b in sheet['beats']))
 out=p/'mp4'/sheet['metadata']['output_filename']
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(listing),'-i',str(p/'audio/narration-review.wav'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-af','loudnorm=I=-18:TP=-2:LRA=11','-ar','48000','-movflags','+faststart','-t',str(sheet['metadata']['duration_s']),str(out)]
 subprocess.run(cmd,check=True);print('EXPORT COMPLETE',out,flush=True)
if __name__=='__main__':
 run(Path(sys.argv[1]),'--preview' in sys.argv)
