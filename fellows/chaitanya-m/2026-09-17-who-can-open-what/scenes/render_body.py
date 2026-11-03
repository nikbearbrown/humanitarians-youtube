#!/usr/bin/env python3
"""
render_body.py — the five BODY beats of "Who Can Open What", native 4K.

WHY OUT-OF-TREE
  The Claude bookends (B00/B06/B07/B08) render from brutalist's own Remotion
  compositions, which are 1920x1080 and therefore true 4K at --scale=2. The
  structural illustration compositions (ClaudeScienceLayerStack / SourceFlow /
  ChipGrid) are registered at 1280x720 — at scale 2 that is 2560x1440 and would
  have to be upscaled. Reaching native 4K with them would mean adding 1080p
  compositions to Root.tsx, i.e. modifying the toolkit. So the body renders here
  instead, in the EXACT CLAUDE token palette, and drops into media/ slots.

BRAND (values copied from runtime/remotion/src/tokens/claude.ts — do not retint)
  PAGE #FAF9F5  CARD #FFFFFF  BORDER #E5E2D9  FOOTER #F1EFE7
  INK  #3D3929  INK_SOFT #73705F  GHOST #A9A491  SPARK #D97757  SEND #C6613F
  Serif: EB Garamond (brutalist's bundled Tiempos fallback). UI: Helvetica Neue.

LAWS OBSERVED
  ILLUSTRATE LAW — no Claude UI on these beats; each illustrates its concept.
  SPARK-LINE LAW — every beat carries the spark + one short serif line.
  LOGO LAW       — channel wordmark bug, low-opacity, lower-right, title-safe.
  ONE ACCENT     — terracotta marks the single focal thing per beat.
  NO REAL NAMES  — every person is a ROLE (ADMIN / INSTRUCTOR / STUDENT).
"""
import argparse, json, os, shutil, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FPS = 24
PAGE=(0xFA,0xF9,0xF5); CARD=(0xFF,0xFF,0xFF); BORDER=(0xE5,0xE2,0xD9)
FOOTER=(0xF1,0xEF,0xE7); INK=(0x3D,0x39,0x29); INK_SOFT=(0x73,0x70,0x5F)
GHOST=(0xA9,0xA4,0x91); SPARK=(0xD9,0x77,0x57); SEND=(0xC6,0x61,0x3F)

BRU = Path("/Users/chaitanyam/dev/brutalist")
SERIF_R = BRU/"runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf"
SERIF_M = BRU/"runtime/fonts/EB_Garamond/static/EBGaramond-Medium.ttf"
UI_TTC  = "/System/Library/Fonts/HelveticaNeue.ttc"
HANDLE  = "@HumanitariansAI"

_fc={}
def font(kind, size):
    k=(kind,size)
    if k not in _fc:
        if kind=="serif":  _fc[k]=ImageFont.truetype(str(SERIF_R), size)
        elif kind=="serifm":_fc[k]=ImageFont.truetype(str(SERIF_M), size)
        elif kind=="ui":   _fc[k]=ImageFont.truetype(UI_TTC, size, index=0)
        elif kind=="uim":  _fc[k]=ImageFont.truetype(UI_TTC, size, index=10)
        elif kind=="uib":  _fc[k]=ImageFont.truetype(UI_TTC, size, index=1)
        else: raise ValueError(kind)
    return _fc[k]


class L:
    def __init__(self,w,h):
        self.w,self.h=w,h
        self.portrait=h>w
        s = w/3840
        self.sx=s
        self.safe=(int(w*0.05), int(h*0.05), int(w*0.95), int(h*0.95))
        self.title=int(180*s*(1.0 if not self.portrait else 1.35))
        self.h2=int(110*s*(1.0 if not self.portrait else 1.35))
        self.body=int(72*s*(1.0 if not self.portrait else 1.4))
        self.lab=int(48*s*(1.0 if not self.portrait else 1.4))
        self.cap=int(36*s*(1.0 if not self.portrait else 1.4))
        self.r=int(18*s)


def frame(l):
    im=Image.new("RGB",(l.w,l.h),PAGE)
    return im, ImageDraw.Draw(im)

def tw(d,txt,f): return d.textlength(txt,font=f)

def text(d,xy,txt,f,fill,center=False,right=False):
    x,y=xy; w=d.textlength(txt,font=f)
    if center: x-=w/2
    elif right: x-=w
    d.text((x,y),txt,font=f,fill=fill); return w

def card(d,box,fill=CARD,border=BORDER,r=None,bw=3,shadow=False):
    x0,y0,x1,y1=box
    d.rounded_rectangle([x0,y0,x1,y1],radius=(r if r is not None else 18),
                        fill=fill,outline=border,width=bw)

def spark(d,x,y,size,col=SPARK,w=None):
    """The Claude spark — an eight-point asterisk."""
    w = w or max(2,int(size*0.13))
    r=size/2
    import math
    for k in range(4):
        a=math.radians(k*45)
        dx,dy=math.cos(a)*r, math.sin(a)*r
        d.line([(x-dx,y-dy),(x+dx,y+dy)],fill=col,width=w)

def sparkline(d,l,txt,bottom=False):
    """SPARK-LINE LAW: spark + one short serif line. Top unless told otherwise."""
    s=int(l.h2*0.52)
    y = (l.h-int(l.h*0.085)) if bottom else int(l.h*0.072)
    x = l.safe[0]
    spark(d,x+s/2,y+s/2,s)
    text(d,(x+s*1.5,y-int(s*0.22)),txt,font("serifm",int(s*1.5)),INK)

def bug(d,l):
    """LOGO LAW: channel wordmark, low-opacity, lower-right, inside title-safe."""
    f=font("serif",l.cap)
    text(d,(l.safe[2],l.safe[3]-l.cap),HANDLE,f,GHOST,right=True)

def arrow(d,p0,p1,col=INK,w=4,head=22):
    import math
    d.line([p0,p1],fill=col,width=w)
    a=math.atan2(p1[1]-p0[1],p1[0]-p0[0])
    for s in (0.6,-0.6):
        d.line([p1,(p1[0]-math.cos(a-s)*head,p1[1]-math.sin(a-s)*head)],fill=col,width=w)


# ── scenes ───────────────────────────────────────────────────────────────────
def b01(l):
    """SCENE 1 — the click, the question, three routes converging on one box."""
    routes=["given directly","through a class","staff — gets everything"]
    # The question wraps to two lines and is width-checked against the box's
    # left edge: as one 180px line it ran straight through the access-check box
    # and over the route labels.
    qlines=["Are you allowed","to open this?"]
    def draw(click=False,q=False,nroutes=0,conv=False):
        im,d=frame(l); sparkline(d,l,"One question."); bug(d,l)
        colx=l.safe[0]
        boxl=int(l.w*0.58)                     # nothing in the left column may cross this
        cw,ch=int(l.w*0.15),int(l.h*0.21)
        cx,cy=colx,int(l.h*0.155)
        card(d,(cx,cy,cx+cw,cy+ch))
        text(d,(cx+cw/2,cy+ch*0.38),"TEXTBOOK",font("uib",l.lab),INK_SOFT,center=True)
        if click:
            px,py=cx+cw*0.70,cy+ch*0.66
            d.polygon([(px,py),(px,py+l.lab*1.5),(px+l.lab*0.42,py+l.lab*1.05),
                       (px+l.lab*0.92,py+l.lab*1.5)],fill=INK)
        qsz=l.title
        f=font("serifm",qsz)
        while qsz>40 and max(d.textlength(t,font=font("serifm",qsz)) for t in qlines) > (boxl-colx-int(l.w*0.03)):
            qsz-=8
        f=font("serifm",qsz); lead=int(qsz*1.12)
        qy=int(l.h*0.435)
        if q:
            for i,t in enumerate(qlines):
                text(d,(colx,qy+i*lead),t,f,INK)
        ry=int(l.h*0.70)
        for i,rt in enumerate(routes[:nroutes]):
            yy=ry+i*int(l.body*1.85)
            text(d,(colx,yy),"—  "+rt,font("ui",l.body),
                 INK_SOFT if not conv else GHOST)
        if conv:
            bx0,by0=boxl,int(l.h*0.42)
            bx1,by1=l.safe[2],int(l.h*0.66)
            card(d,(bx0,by0,bx1,by1),fill=CARD,border=SPARK,bw=6)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.058)),"the access check",
                 font("serifm",l.h2),INK,center=True)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.135)),"one question · one place",
                 font("ui",l.lab),INK_SOFT,center=True)
            for i in range(nroutes):
                y0=ry+i*int(l.body*1.85)+l.body*0.45
                arrow(d,(int(l.w*0.44),y0),(bx0-18,by1-int(l.h*0.03)),SPARK,4,20)
        return im
    segs=[(10,lambda: draw())]
    segs.append((EL(1),lambda: draw(click=True)))
    segs.append((EL(2),lambda: draw(click=True,q=True)))
    for i in (1,2,3):
        segs.append((EL(1),lambda i=i: draw(click=True,q=True,nroutes=i)))
    segs.append((EL(3),lambda: draw(click=True,q=True,nroutes=3,conv=True)))
    return segs


def b02(l):
    """SCENE 2 — three stacked rows. ADMIN / INSTRUCTOR / STUDENT."""
    rows=[("ADMIN","every textbook  ·  nothing to set up",None),
          ("INSTRUCTOR","every textbook  except hidden","hidden"),
          ("STUDENT","nothing by default",None)]
    def draw(n=0,cap=False):
        im,d=frame(l); sparkline(d,l,"Role decides."); bug(d,l)
        x0,x1=l.safe[0],l.safe[2]
        top=int(l.h*0.20); rh=int(l.h*0.175); gap=int(rh*0.22)
        for i,(t,sub,acc) in enumerate(rows[:n]):
            y=top+i*(rh+gap)
            is_student = t=="STUDENT"
            card(d,(x0,y,x1,y+rh),fill=CARD,
                 border=SPARK if is_student else BORDER, bw=6 if is_student else 3)
            text(d,(x0+int(l.w*0.035),y+int(rh*0.22)),t,font("uib",l.h2),INK)
            f=font("ui",l.body)
            if acc:
                pre=sub.split(acc)[0]
                wpre=text(d,(x0+int(l.w*0.035),y+int(rh*0.62)),pre,f,INK_SOFT)
                text(d,(x0+int(l.w*0.035)+wpre,y+int(rh*0.62)),acc,
                     font("uim",l.body),SPARK)
            else:
                text(d,(x0+int(l.w*0.035),y+int(rh*0.62)),sub,f,
                     SPARK if is_student else INK_SOFT)
            if is_student:
                text(d,(x1-int(l.w*0.035),y+int(rh*0.40)),"empty shelf",
                     font("serif",l.lab),GHOST,right=True)
        if cap:
            text(d,(x0,int(l.h*0.855)),
                 "Permission arrives with the role — except for students.",
                 font("serifm",l.h2),INK)
        return im
    segs=[(8,lambda: draw(0))]
    for i in (1,2,3):
        segs.append((EL(2),lambda i=i: draw(i)))
    segs.append((EL(3),lambda: draw(3,cap=True)))
    return segs


def b03(l):
    """SCENE 3 — two feeds merge into one shelf; a duplicate drops; class archives."""
    shelf=["Cell Biology","Organic Chemistry","Statistics I","Statistics I"]
    def draw(left=False,right=False,merge=False,dedup=False,archived=False):
        im,d=frame(l); sparkline(d,l,"Two ways in."); bug(d,l)
        fw,fh=int(l.w*0.26),int(l.h*0.145)
        ly,ry_=int(l.h*0.185),int(l.h*0.185)
        lx,rx=l.safe[0],l.safe[2]-fw
        if left:
            card(d,(lx,ly,lx+fw,ly+fh))
            text(d,(lx+fw/2,ly+fh*0.20),"DIRECT GRANT",font("uib",l.lab),INK,center=True)
            text(d,(lx+fw/2,ly+fh*0.58),"an admin grants one book",
                 font("ui",l.cap),INK_SOFT,center=True)
        if right:
            col = GHOST if archived else INK
            card(d,(rx,ry_,rx+fw,ry_+fh),fill=FOOTER if archived else CARD,
                 border=BORDER,bw=3)
            text(d,(rx+fw/2,ry_+fh*0.20),"CLASS ENROLMENT" if not archived else "ARCHIVED",
                 font("uib",l.lab),col if not archived else SPARK,center=True)
            text(d,(rx+fw/2,ry_+fh*0.58),
                 "join the class, get the books" if not archived else "semester ended",
                 font("ui",l.cap),GHOST if archived else INK_SOFT,center=True)
        sx0,sx1=int(l.w*0.30),int(l.w*0.70)
        sy0=int(l.h*0.50); rowh=int(l.h*0.078)
        if merge:
            arrow(d,(lx+fw/2,ly+fh+10),(sx0+int(l.w*0.06),sy0-20),INK,4)
            arrow(d,(rx+fw/2,ry_+fh+10),(sx1-int(l.w*0.06),sy0-20),
                  GHOST if archived else INK,4)
            n=len(shelf)
            visible=[]
            for i,t in enumerate(shelf):
                if dedup and i==3: continue
                if archived and t in ("Statistics I",): continue
                visible.append(t)
            sh=rowh*max(1,len(visible))+int(rowh*0.7)
            card(d,(sx0,sy0,sx1,sy0+sh),fill=CARD)
            text(d,((sx0+sx1)/2,sy0+int(rowh*0.18)),"THE SHELF",
                 font("uib",l.lab),INK_SOFT,center=True)
            for i,t in enumerate(visible):
                yy=sy0+int(rowh*0.78)+i*rowh
                text(d,(sx0+int(l.w*0.025),yy),t,font("ui",l.body),INK)
            if not dedup:
                yy=sy0+int(rowh*0.78)+3*rowh
                d.line([(sx0+int(l.w*0.02),yy+l.body*0.55),
                        (sx1-int(l.w*0.02),yy+l.body*0.55)],fill=SPARK,width=5)
                text(d,(sx1-int(l.w*0.025),yy),"duplicate",
                     font("serif",l.lab),SPARK,right=True)
        if archived:
            text(d,(l.safe[0],int(l.h*0.875)),
                 "Access came from the class, so it leaves with the class.",
                 font("serifm",l.h2),INK)
        return im
    segs=[(8,lambda: draw())]
    segs.append((EL(1),lambda: draw(left=True)))
    segs.append((EL(1),lambda: draw(left=True,right=True)))
    segs.append((EL(2),lambda: draw(left=True,right=True,merge=True)))
    segs.append((EL(2),lambda: draw(left=True,right=True,merge=True,dedup=True)))
    segs.append((EL(3),lambda: draw(left=True,right=True,merge=True,dedup=True,archived=True)))
    return segs


def b04(l):
    """SCENE 4 — THE HERO. Two moments, one box; the counterfactual; collapse back."""
    def draw(m1=False,m2=False,box=False,split=False,collapse=False):
        im,d=frame(l); sparkline(d,l,"It cannot disagree."); bug(d,l)
        mw,mh=int(l.w*0.25),int(l.h*0.155)
        mx=l.safe[0]
        y1,y2=int(l.h*0.22),int(l.h*0.55)
        if m1:
            card(d,(mx,y1,mx+mw,y1+mh))
            text(d,(mx+mw/2,y1+mh*0.20),"MOMENT ONE",font("uib",l.cap),GHOST,center=True)
            text(d,(mx+mw/2,y1+mh*0.52),"the click",font("serifm",l.h2),INK,center=True)
        if m2:
            card(d,(mx,y2,mx+mw,y2+mh))
            text(d,(mx+mw/2,y2+mh*0.20),"MOMENT TWO",font("uib",l.cap),GHOST,center=True)
            text(d,(mx+mw/2,y2+mh*0.52),"the book checks back",
                 font("serifm",int(l.h2*0.78)),INK,center=True)
        bx0,bx1=int(l.w*0.55),int(l.w*0.90)
        if box and not split:
            by0,by1=int(l.h*0.33),int(l.h*0.60)
            card(d,(bx0,by0,bx1,by1),border=SPARK,bw=6)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.065)),"one place",
                 font("serifm",l.title),INK,center=True)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.155)),"same answer, both times",
                 font("ui",l.lab),INK_SOFT,center=True)
            if m1: arrow(d,(mx+mw+14,y1+mh/2),(bx0-16,by0+int(l.h*0.07)),SPARK,4)
            if m2: arrow(d,(mx+mw+14,y2+mh/2),(bx0-16,by1-int(l.h*0.07)),SPARK,4)
        if split:
            h=int(l.h*0.135)
            for i,(lab,val) in enumerate((("its own logic","OPEN"),
                                          ("its own logic","DENIED"))):
                by=int(l.h*0.30)+i*int(h*1.35)
                card(d,(bx0,by,bx1,by+h),border=BORDER,bw=3)
                text(d,(bx0+int(l.w*0.02),by+h*0.18),lab,font("ui",l.cap),GHOST)
                text(d,(bx1-int(l.w*0.02),by+h*0.42),val,
                     font("uib",l.h2),SPARK,right=True)
            text(d,(bx0,int(l.h*0.60)),"they disagree",
                 font("serifm",l.h2),SPARK)
            if m1: arrow(d,(mx+mw+14,y1+mh/2),(bx0-16,int(l.h*0.36)),INK,4)
            if m2: arrow(d,(mx+mw+14,y2+mh/2),(bx0-16,int(l.h*0.49)),INK,4)
        if collapse:
            text(d,(l.safe[0],int(l.h*0.875)),
                 "The decision lives in exactly one place — so they can't drift apart.",
                 font("serifm",l.h2),INK)
        return im
    segs=[(8,lambda: draw())]
    segs.append((EL(1),lambda: draw(m1=True)))
    segs.append((EL(1),lambda: draw(m1=True,m2=True)))
    segs.append((EL(3),lambda: draw(m1=True,m2=True,box=True)))
    segs.append((EL(2),lambda: draw(m1=True,m2=True,split=True)))
    segs.append((EL(3),lambda: draw(m1=True,m2=True,box=True,collapse=True)))
    return segs


def b05(l):
    """SCENE 5 — three rules collapse to one box; a new route slots in."""
    chips=[("ADMIN","everything"),("INSTRUCTOR","everything finished"),
           ("STUDENT","given + enrolled")]
    def draw(n=0,one=False,newroute=False):
        im,d=frame(l); sparkline(d,l,"One place."); bug(d,l)
        cw=int((l.safe[2]-l.safe[0]-int(l.w*0.04))/3); chh=int(l.h*0.165)
        top=int(l.h*0.20)
        for i,(t,s) in enumerate(chips[:n]):
            x=l.safe[0]+i*(cw+int(l.w*0.02))
            card(d,(x,top,x+cw,top+chh))
            text(d,(x+cw/2,top+chh*0.22),t,font("uib",l.lab),INK,center=True)
            text(d,(x+cw/2,top+chh*0.58),s,font("ui",l.body),INK_SOFT,center=True)
        if one:
            bx0,bx1=int(l.w*0.28),int(l.w*0.72)
            by0,by1=int(l.h*0.46),int(l.h*0.70)
            card(d,(bx0,by0,bx1,by1),border=SPARK,bw=6)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.055)),"one question",
                 font("serifm",l.title),INK,center=True)
            text(d,((bx0+bx1)/2,by0+int(l.h*0.145)),"answered the same way, every time",
                 font("ui",l.lab),INK_SOFT,center=True)
            for i in range(n):
                x=l.safe[0]+i*(cw+int(l.w*0.02))+cw/2
                arrow(d,(x,top+chh+12),(max(bx0+40,min(bx1-40,x)),by0-16),GHOST,3,16)
        if newroute:
            text(d,(l.safe[0],int(l.h*0.785)),"+  DEPARTMENT LICENCE",
                 font("uib",l.h2),SPARK)
            text(d,(l.safe[0],int(l.h*0.865)),
                 "added here once — and every door already knows.",
                 font("serifm",l.h2),INK)
        return im
    segs=[(8,lambda: draw(0))]
    for i in (1,2,3):
        segs.append((EL(1),lambda i=i: draw(i)))
    segs.append((EL(3),lambda: draw(3,one=True)))
    segs.append((EL(3),lambda: draw(3,one=True,newroute=True)))
    return segs


SCENES={"B01":b01,"B02":b02,"B03":b03,"B04":b04,"B05":b05}


# ── assembly (weighted elastics; empty states never match content) ───────────
def EL(w=1): return ("el",w)
def _fx(f): return isinstance(f,int)

def allocate(segs,total):
    fixed=sum(f for f,_ in segs if _fx(f))
    ws=[(i,1 if f is None else f[1]) for i,(f,_) in enumerate(segs) if not _fx(f)]
    out=[f if _fx(f) else 0 for f,_ in segs]
    left=total-fixed
    if ws:
        if left<len(ws):
            sc=max(0.0,(total-len(ws))/max(fixed,1))
            for i,(f,_) in enumerate(segs): out[i]=max(1,int(f*sc)) if _fx(f) else 1
        else:
            wsum,acc=sum(w for _,w in ws),0
            for j,(i,w) in enumerate(ws):
                sh=left*w//wsum if j<len(ws)-1 else left-acc
                out[i]=sh; acc+=sh
    drift=total-sum(out)
    if drift: out[-1]=max(1,out[-1]+drift)
    return out


def render_beat(bid,l,dur,outdir,workroot):
    total=max(1,round(dur*FPS)); segs=SCENES[bid](l); counts=allocate(segs,total)
    work=workroot/bid; (work/"st").mkdir(parents=True); (work/"fr").mkdir()
    n=0
    for idx,((_,fn),c) in enumerate(zip(segs,counts)):
        if c<=0: continue
        p=work/"st"/f"s{idx:04d}.png"; fn().save(p,compress_level=1)
        for _ in range(c): n+=1; os.link(p,work/"fr"/f"{n:06d}.png")
    out=outdir/f"{bid}.mp4"
    r=subprocess.run(["ffmpeg","-y","-framerate",str(FPS),"-i",str(work/"fr"/"%06d.png"),
        "-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p",
        "-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709",str(out)],
        capture_output=True,text=True)
    if r.returncode: raise SystemExit(f"[body] ffmpeg failed {bid}:\n{r.stderr[-1200:]}")
    shutil.rmtree(work); return out,n,len(counts)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--aspect",default="16:9",choices=["16:9","9:16"])
    ap.add_argument("--sheet"); ap.add_argument("--out"); ap.add_argument("--only",nargs="*")
    a=ap.parse_args()
    reel=Path(__file__).resolve().parent.parent
    sheet=json.loads(Path(a.sheet or reel/"beat_sheet.json").read_text())
    W,H=(3840,2160) if a.aspect=="16:9" else (2160,3840)
    l=L(W,H); outdir=Path(a.out or reel/"media"); outdir.mkdir(parents=True,exist_ok=True)
    wr=Path(tempfile.mkdtemp(prefix="wcow-"))
    print(f"[body] {a.aspect} {W}x{H} @{FPS} -> {outdir}")
    for b in sheet["beats"]:
        bid=b["beat_id"]
        if bid not in SCENES: continue
        if a.only and bid not in a.only: continue
        dur=float(b.get("actual_duration_s") or b["estimated_duration_s"])
        o,n,ns=render_beat(bid,l,dur,outdir,wr)
        print(f"[body] {bid} {dur:6.2f}s {n:5d} frames {ns:3d} states -> {o.name}")
    shutil.rmtree(wr,ignore_errors=True); print("[body] done")

if __name__=="__main__": main()
