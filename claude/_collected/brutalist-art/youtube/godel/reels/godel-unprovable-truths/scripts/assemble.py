#!/usr/bin/env python3
# Slate-cut assembler (vox-explainer previz) for the Godel music video.
# Per-beat mp4s (baked caption + review overlay) -> concat -> mux master song.
# Resumable: skips clips/B##.mp4 that already exist. Use --limit N to chunk.
import json, os, sys, subprocess, math, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

GODEL="/sessions/affectionate-sharp-rubin/mnt/bear-textbooks/books/unreal-reels/music/godel"
REELS=os.path.join(GODEL,"reels","godel-unprovable-truths")
PANTRY=os.path.join(GODEL,"pantry")
AUDIO=os.path.join(GODEL,"GodelUnprovabletruths-mastered.wav")
FR=os.path.join(REELS,"frames"); CL=os.path.join(REELS,"clips")
for d in (FR,CL): os.makedirs(d,exist_ok=True)

W,H,FPS=960,540,24
GROUND=(243,235,221); INK=(47,42,38); BLUE=(61,90,128)
TERRA=(211,95,67); HIGH=(245,208,97); TEAL=(62,85,89); CREAM=(243,235,221)

SER="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERB="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERI="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
MONO="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
def F(p,s): return ImageFont.truetype(p,s)

def newsprint():
    p=os.path.join(FR,"_newsprint.png")
    if os.path.exists(p): return p
    random.seed(1931)
    im=Image.new("RGB",(W,H),GROUND); d=ImageDraw.Draw(im)
    # faint fiber speckle
    for _ in range(9000):
        x=random.randint(0,W-1); y=random.randint(0,H-1)
        v=random.randint(-14,10)
        d.point((x,y),fill=(GROUND[0]+v,GROUND[1]+v,GROUND[2]+v))
    # faint column rules (newspaper)
    for cx in range(0,W,120):
        d.line([(cx,0),(cx,H)],fill=(GROUND[0]-10,GROUND[1]-10,GROUND[2]-12))
    im=im.filter(ImageFilter.GaussianBlur(0.4))
    im.save(p); return p

def wrap(draw,text,font,maxw):
    out=[]
    for para in text.split("\n"):
        words=para.split(); line=""
        for w in words:
            t=(line+" "+w).strip()
            if draw.textlength(t,font=font)<=maxw: line=t
            else:
                if line: out.append(line)
                line=w
        out.append(line)
    return out

def chip(d,xy,text,font,bg,fg=(255,255,255),pad=8):
    x,y=xy; tw=d.textlength(text,font=font); th=font.size
    d.rectangle([x,y,x+tw+2*pad,y+th+2*pad],fill=bg)
    d.text((x+pad,y+pad-1),text,font=font,fill=fg)
    return x+tw+2*pad, y

def caption_band(base_rgba, cap):
    """draw bottom translucent cream caption band with serif ink text"""
    if not cap: return base_rgba
    d=ImageDraw.Draw(base_rgba,"RGBA")
    f=F(SERB,26)
    lines=wrap(d,cap,f,W-120)
    bh=len(lines)*(f.size+8)+28
    d.rectangle([0,H-bh,W,H],fill=(243,235,221,214))
    d.rectangle([0,H-bh,W,H-bh+4],fill=(*BLUE,255))
    y=H-bh+14
    for ln in lines:
        tw=d.textlength(ln,font=f); d.text(((W-tw)//2,y),ln,font=f,fill=(*INK,255)); y+=f.size+8
    return base_rgba

def review_header(d, b):
    """top-left review burn-in chip"""
    hf=F(MONO,15)
    s=b["shot"]
    tag=f'{b["beat_id"]} · {s["type"]}×{s["source"]} · {"FILLED" if b["media"] else "SLATE"}'
    tc=f'{b["t_start_s"]:.1f}–{b["t_end_s"]:.1f}s'
    d.rectangle([0,0,max(d.textlength(tag,font=hf),d.textlength(tc,font=hf))+24,52],fill=(47,42,38,220))
    d.text((12,7),tag,font=hf,fill=(243,235,221,255))
    d.text((12,27),tc,font=hf,fill=(245,208,97,255))

TYPE_LABEL={"GRAPHIC":"GRAPHIC — TO BUILD (Manim)","DOCUMENT":"DOCUMENT — TO SOURCE",
            "CARD":"DESIGN CARD","FOOTAGE":"FOOTAGE — TO GENERATE","STILL":"STILL — TO SOURCE",
            "COMPOSITE":"COMPOSITE — PLATE + ANNOTATION"}

def draw_slate(b):
    """full-frame vox slate PNG for an unfilled beat"""
    im=Image.open(newsprint()).convert("RGBA")
    d=ImageDraw.Draw(im,"RGBA")
    # header (big id sits below the review chip so they never overlap)
    d.text((28,58),b["beat_id"],font=F(SERB,48),fill=(*INK,255))
    d.text((30,116),f'SCENE {b["scene_index"]}   ·   {b["shot"]["type"]} × {b["shot"]["source"]}   ·   motion: {b["shot"]["motion"]}',
           font=F(SER,18),fill=(*INK,255))
    tc=f'{b["t_start_s"]:.1f}–{b["t_end_s"]:.1f}s  ({b["duration_s"]:.1f}s)'
    d.text((W-28-d.textlength(tc,font=F(MONO,18)),64),tc,font=F(MONO,18),fill=(*BLUE,255))
    d.line([(28,148),(W-28,148)],fill=(*INK,255),width=2)
    # type chip (teal)
    lbl=TYPE_LABEL.get(b["shot"]["type"],b["shot"]["type"])
    chip(d,(28,164),lbl,F(SERB,22),TEAL)
    # teach (what to build)
    y=218
    for ln in wrap(d,b["teach"],F(SER,24),W-80):
        d.text((30,y),ln,font=F(SER,24),fill=(*INK,255)); y+=32
    # prompt hint (dim mono)
    y+=6
    ph=("PROMPT  "+b["fill_prompt"])
    for ln in wrap(d,ph,F(MONO,14),W-80)[:4]:
        d.text((30,y),ln,font=F(MONO,14),fill=(90,84,78,255)); y+=19
    if b["archive_queries"]:
        aq="ARCHIVE  "+ " · ".join(b["archive_queries"][:3])
        for ln in wrap(d,aq,F(MONO,14),W-80)[:2]:
            d.text((30,y),ln,font=F(MONO,14),fill=(*BLUE,255)); y+=19
    # footer slot instruction
    d.text((30,H-96),f'FILL:  media/{b["beat_id"]}.png  (placeholder / i2v seed)   ›   media/{b["beat_id"]}.mp4  (upgrade)',
           font=F(MONO,14),fill=(120,60,50,255))
    # caption band (the on-screen line) + review header
    im=caption_band(im,b["caption"])
    review_header(d,b)
    p=os.path.join(FR,b["beat_id"]+".png"); im.convert("RGB").save(p); return p

def draw_overlay(b):
    """transparent caption+header overlay for a filled (footage) beat"""
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im,"RGBA")
    im=caption_band(im,b["caption"]); d=ImageDraw.Draw(im,"RGBA")
    review_header(d,b)
    p=os.path.join(FR,b["beat_id"]+"_ov.png"); im.save(p); return p

def run(cmd):
    r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if r.returncode!=0:
        print(cmd); print(r.stdout.decode()[-1500:]); raise SystemExit(1)

def nframes(dur): return max(1,round(dur*FPS))

def render_slate_clip(b,dur):
    png=draw_slate(b); out=os.path.join(CL,b["beat_id"]+".mp4"); N=nframes(dur)
    run(["ffmpeg","-y","-loop","1","-i",png,
         "-r",str(FPS),"-frames:v",str(N),"-vsync","cfr",
         "-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p",
         "-vf",f"scale={W}:{H},fps={FPS}","-an",out])

def render_footage_clip(b,dur):
    src=os.path.join(PANTRY,b["media"]); ov=draw_overlay(b)
    out=os.path.join(CL,b["beat_id"]+".mp4"); N=nframes(dur)
    # vox treatment: desaturate, gentle contrast, cream wash; scale/crop to frame;
    # conform: if beat longer than clip, freeze tail (tpad clone); exact N frames out.
    vf=(f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
        f"eq=saturation=0.22:contrast=1.12:brightness=0.02,"
        f"colorbalance=rm=0.05:gm=0.03:bm=-0.05,"
        f"tpad=stop_mode=clone:stop_duration=12,"
        f"format=rgba[bg];[bg][1:v]overlay=0:0,setpts=PTS-STARTPTS,format=yuv420p")
    run(["ffmpeg","-y","-i",src,"-i",ov,
         "-r",str(FPS),"-filter_complex",vf,"-frames:v",str(N),"-vsync","cfr",
         "-c:v","libx264","-preset","veryfast","-pix_fmt","yuv420p","-an",out])

def main():
    sheetp=os.path.join(REELS,"beat_sheet.json")
    bs=json.load(open(sheetp))
    beats=bs["beats"]
    if "--retime" in sys.argv:
        # snap every beat to a whole frame count so rendered video == sheet timeline
        t=0.0
        for b in beats:
            N=nframes(b["duration_s"]); d=N/FPS
            b["t_start_s"]=round(t,3); b["t_end_s"]=round(t+d,3)
            b["duration_s"]=round(d,3); b["frames"]=N; t+=d
        bs["metadata"]["total_duration_s"]=round(t,3)
        json.dump(bs,open(sheetp,"w"),indent=2)
        print("retimed: total",round(t,3),"s over",len(beats),"beats")
    limit=10**9
    if "--limit" in sys.argv: limit=int(sys.argv[sys.argv.index("--limit")+1])
    force=set()
    if "--force" in sys.argv:
        fv=sys.argv[sys.argv.index("--force")+1]
        force=set(fv.split(",")) if fv!="ALL" else set(b["beat_id"] for b in beats)
    done=0
    for b in beats:
        out=os.path.join(CL,b["beat_id"]+".mp4")
        if b["beat_id"] not in force and os.path.exists(out) and os.path.getsize(out)>0: continue
        if done>=limit: break
        dur=max(0.6,b["duration_s"])
        if b["media"]: render_footage_clip(b,dur)
        else: render_slate_clip(b,dur)
        print("rendered",b["beat_id"],b["shot"]["type"],f"{dur:.2f}s")
        done+=1
    # concat when all present
    missing=[b["beat_id"] for b in beats if not os.path.exists(os.path.join(CL,b["beat_id"]+".mp4"))]
    if missing:
        print("PENDING",len(missing),"clips:",missing[:6],"..."); return
    if "--final" in sys.argv:
        lst=os.path.join(REELS,"_concat.txt")
        open(lst,"w").write("\n".join(f"file '{os.path.join(CL,b['beat_id']+'.mp4')}'" for b in beats))
        silent=os.path.join(REELS,"_silent.mp4")
        run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",silent])
        out=os.path.join(REELS,"godel-unprovable-truths_slate-cut.mp4")
        run(["ffmpeg","-y","-i",silent,"-i",AUDIO,"-map","0:v","-map","1:a",
             "-c:v","copy","-c:a","aac","-b:a","192k","-shortest",out])
        print("FINAL",out)

if __name__=="__main__": main()
