"""9:16 native 4K (2160x3840) animated slate renderer.

All coordinates in true 4K pixels. Animated stages same recipe as landscape.
Remotion Claude beats (B00, B05, B08, B09) get letterboxed with title strips.
"""
from __future__ import annotations
import subprocess, sys, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

CREAM  = "#FAF9F5"
INK    = "#3D3929"
INK_S  = "#6b6357"
SEND   = "#D97757"
LINE   = "#E7E4DC"
CARD   = "#F1EEE4"

W, H = 2160, 3840
MARGIN = 120
CONTENT_W = W - 2*MARGIN  # 1920

TOOL = Path(r"C:/Users/Sanjana/OneDrive/Desktop/Humanitarians AI Brutalist files/brutalist.art")
REEL = Path(r"C:/Users/Sanjana/OneDrive/Desktop/Humanitarians AI Brutalist files/YouTube Process/youtube-process")
REF  = REEL.parent
MEDIA = REEL / "media_vert"; MEDIA.mkdir(exist_ok=True)
TMP = REEL / "_slate_png_vert"; TMP.mkdir(exist_ok=True)
LANDSCAPE = REEL / "media"

SERIF_R = str(TOOL / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf")
SERIF_M = str(TOOL / "runtime/fonts/EB_Garamond/static/EBGaramond-Medium.ttf")
SANS    = str(TOOL / "runtime/fonts/Inter/static/Inter_28pt-Regular.ttf")
SANS_M  = str(TOOL / "runtime/fonts/Inter/static/Inter_28pt-Medium.ttf")
def F(p, sz): return ImageFont.truetype(p, sz)

def canvas(bg=CREAM):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)

def kicker(d, text, y=260):
    d.text((MARGIN, y), text, font=F(SANS_M, 48), fill=INK_S)

def title_period(d, x, y, body, size):
    d.text((x, y), body, font=F(SERIF_M, size), fill=INK)
    tw = d.textlength(body, font=F(SERIF_M, size))
    d.text((x + tw, y), ".", font=F(SERIF_M, size), fill=SEND)

def bug(d):
    d.text((W - MARGIN, H - 120), "@HumanitariansAI",
           font=F(SANS, 40), fill=INK_S, anchor="rb")

# ============================================================= B01
def b01_stages():
    def base():
        img, d = canvas()
        d.text((MARGIN, 220),
               "HUMANITARIANS AI · FELLOWS BRIEFING",
               font=F(SANS_M, 40), fill=INK_S)
        d.text((MARGIN, 340), "The Video",   font=F(SERIF_M, 190), fill=INK)
        d.text((MARGIN, 540), "Review",      font=F(SERIF_M, 190), fill=INK)
        d.text((MARGIN, 740), "Pipeline",    font=F(SERIF_M, 190), fill=INK)
        pw = d.textlength("Pipeline", font=F(SERIF_M, 190))
        d.text((MARGIN + pw, 740), ".",      font=F(SERIF_M, 190), fill=SEND)
        bug(d)
        return img, d

    stages = []
    img, d = base(); stages.append(img)
    img, d = base()
    d.text((MARGIN, 1120),
           "Two videos a week.\nSix criteria.\nOne queue.",
           font=F(SERIF_R, 100), fill=INK_S, spacing=20)
    stages.append(img)

    stops = [
        ("FELLOW",             "uploads to Drive"),
        ("SANJANA / POOJA",    "reviews vs. 6 criteria"),
        ("QUEUE",              "playlist on YouTube"),
        ("PROF. BROWN & NINA", "final feedback"),
    ]
    y0 = 1750
    row_h = 480
    subline_txt = "Two videos a week.\nSix criteria.\nOne queue."

    def draw_pipeline(d, upto):
        for i, (name, sub) in enumerate(stops[:upto]):
            y = y0 + i*row_h
            cx = MARGIN + 100
            d.ellipse((cx-100, y-100, cx+100, y+100),
                      outline=INK, width=8, fill=CARD)
            d.text((cx, y), str(i+1), font=F(SERIF_M, 110), fill=SEND, anchor="mm")
            d.text((cx + 180, y - 30), name, font=F(SANS_M, 54), fill=INK, anchor="lm")
            d.text((cx + 180, y + 40), sub,  font=F(SANS,   46), fill=INK_S, anchor="lm")
            if i < upto - 1:
                d.line((cx, y+100, cx, y+row_h-100), fill=INK, width=6)

    for k in (1, 2, 3, 4):
        img, d = base()
        d.text((MARGIN, 1120), subline_txt,
               font=F(SERIF_R, 100), fill=INK_S, spacing=20)
        draw_pipeline(d, k)
        stages.append(img)
    return stages

# ============================================================= B02
def b02_stages():
    def base():
        img, d = canvas()
        d.text((MARGIN, 220),
               "WEEKLY CADENCE",
               font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 320), "Two videos,", font=F(SERIF_M, 180), fill=INK)
        d.text((MARGIN, 520), "four files",  font=F(SERIF_M, 180), fill=INK)
        fw = d.textlength("four files", font=F(SERIF_M, 180))
        d.text((MARGIN + fw, 520), ".",      font=F(SERIF_M, 180), fill=SEND)
        bug(d)
        return img, d

    cx0 = MARGIN
    cy0 = 900
    cw  = CONTENT_W
    ch  = 550
    gap = 60
    cells = [
        ("Video 1", "STEM / AI topic", "16:9", "landscape",      True),
        ("Video 1", "STEM / AI topic", "9:16", "vertical Short", False),
        ("Video 2", "Project update",  "16:9", "landscape",      True),
        ("Video 2", "Project update",  "9:16", "vertical Short", False),
    ]

    def draw_upto(d, k):
        for i, (row, sub, aspect, atag, filled) in enumerate(cells[:k]):
            x = cx0; y = cy0 + i*(ch+gap)
            d.rectangle((x, y, x+cw, y+ch),
                        outline=INK, width=6, fill=CARD if filled else CREAM)
            d.text((x+50, y+40), row.upper(), font=F(SANS_M, 46), fill=SEND)
            d.text((x+50, y+120), sub, font=F(SERIF_M, 120), fill=INK)
            d.text((x+cw-50, y+ch-70), aspect,
                   font=F(SERIF_M, 110), fill=INK, anchor="rb")
            d.text((x+cw-50, y+ch-200), atag,
                   font=F(SANS, 42), fill=INK_S, anchor="rb")

    def draw_footer(d):
        fy = cy0 + 4*(ch+gap) + 20
        d.line((MARGIN, fy, W-MARGIN, fy), fill=LINE, width=4)
        d.text((MARGIN, fy+50),
               "Floor: at least 1 research update per\nrolling two-week window.",
               font=F(SERIF_R, 60), fill=INK, spacing=14)

    stages = []
    img, d = base(); stages.append(img)
    img, d = base(); draw_upto(d, 2); stages.append(img)
    img, d = base(); draw_upto(d, 4); stages.append(img)
    img, d = base(); draw_upto(d, 4); draw_footer(d); stages.append(img)
    return stages

# ============================================================= B03
def b03_stages():
    steps = [
        ("1", "Fellow uploads to Drive",              "FELLOW"),
        ("2", "Review vs. 6 criteria",                "SANJANA / POOJA"),
        ("3", "Quality checks — format · 4K",         "SANJANA / POOJA"),
        ("4", "Upload to HAI YouTube · Queue",        "HAI CHANNEL"),
        ("5", "Final feedback: publish or send back", "PROF. BROWN & NINA"),
    ]
    def base():
        img, d = canvas()
        d.text((MARGIN, 220),
               "PROCESS FLOW", font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 320), "Five steps,", font=F(SERIF_M, 170), fill=INK)
        d.text((MARGIN, 500), "two owners",  font=F(SERIF_M, 170), fill=INK)
        tw = d.textlength("two owners", font=F(SERIF_M, 170))
        d.text((MARGIN + tw, 500), ".",      font=F(SERIF_M, 170), fill=SEND)
        bug(d)
        return img, d

    y0 = 900; row_h = 560
    def draw_steps(d, k):
        for i, (n, what, who) in enumerate(steps[:k]):
            y = y0 + i*row_h
            d.ellipse((MARGIN, y, MARGIN+180, y+180),
                      outline=INK, width=8, fill=CARD)
            d.text((MARGIN+90, y+90), n, font=F(SERIF_M, 108), fill=SEND, anchor="mm")
            d.text((MARGIN+240, y+30), what, font=F(SERIF_M, 68), fill=INK)
            d.text((MARGIN+240, y+130), who, font=F(SANS_M, 40), fill=INK_S)
            if i < k-1:
                d.line((MARGIN+90, y+180, MARGIN+90, y+row_h-30),
                       fill=INK, width=6)
    stages = []
    img, d = base(); stages.append(img)
    for k in (2, 4, 5):
        img, d = base(); draw_steps(d, k); stages.append(img)
    return stages

# ============================================================= B04 (vertical)
def b04_stages():
    src = REF / "Quality upto 2160p.png"
    ref = Image.open(src).convert("RGB")
    target_w = 1900
    ratio = target_w / ref.width
    ref = ref.resize((target_w, int(ref.height * ratio)), Image.LANCZOS)

    def base(with_callout=False):
        img, d = canvas()
        d.text((MARGIN, 220),
               "VIDEO STANDARDS · 4K ON YOUTUBE",
               font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 320), "It has to stream", font=F(SERIF_M, 150), fill=INK)
        d.text((MARGIN, 500), "2160p",            font=F(SERIF_M, 150), fill=INK)
        pw = d.textlength("2160p", font=F(SERIF_M, 150))
        d.text((MARGIN + pw, 500), ".",           font=F(SERIF_M, 150), fill=SEND)
        rx = (W - ref.width)//2
        ry = 780
        img.paste(ref, (rx, ry))
        d = ImageDraw.Draw(img)
        if with_callout:
            # Point at the 2160p 4K row in the quality menu — put callout BELOW
            # the screenshot in the vertical layout (safer than side placement).
            px = rx + int(ref.width * 0.78)
            py = ry + int(ref.height * 0.34)
            # vertical arrow shaft from below-left up to the target
            shaft_end_x = px - 60; shaft_end_y = py
            label_x = MARGIN; label_y = ry + ref.height + 120
            d.text((label_x, label_y),
                   "confirm 2160p", font=F(SANS_M, 60), fill=SEND)
            d.text((label_x, label_y + 80),
                   "after YouTube upload", font=F(SANS_M, 60), fill=SEND)
            # dotted-ish line from label toward the pill
            d.line((label_x + 600, label_y + 40, shaft_end_x, shaft_end_y),
                   fill=SEND, width=8)
            d.polygon([(shaft_end_x + 40, shaft_end_y),
                       (shaft_end_x, shaft_end_y - 22),
                       (shaft_end_x, shaft_end_y + 22)], fill=SEND)
        bug(d)
        return img
    return [base(False), base(True)]

# ============================================================= B06 (vertical)
def b06_stages():
    src = REF / "Screenshot 2026-08-23 111738.png"
    ref = Image.open(src).convert("RGB")
    target_w = 1900
    ratio = target_w / ref.width
    ref = ref.resize((target_w, int(ref.height * ratio)), Image.LANCZOS)

    def base(show_rules=False):
        img, d = canvas()
        d.text((MARGIN, 220),
               "NAMING · SHARED DRIVE",
               font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 320), "ProjectName",    font=F(SERIF_M, 140), fill=INK)
        d.text((MARGIN, 480), "_VolunteerName", font=F(SERIF_M, 140), fill=INK)
        pw = d.textlength("_VolunteerName", font=F(SERIF_M, 140))
        d.text((MARGIN + pw, 480), ".",         font=F(SERIF_M, 140), fill=SEND)
        rx = (W - ref.width) // 2
        ry = 780
        img.paste(ref, (rx, ry))
        d = ImageDraw.Draw(img)
        if show_rules:
            fy = ry + ref.height + 100
            d.text((MARGIN, fy), "NO", font=F(SANS_M, 60), fill=SEND)
            x0 = MARGIN + 200
            for i, bad in enumerate(("spaces", "dates", "_v2", "_final")):
                bx = x0 + i*400
                d.text((bx, fy), bad, font=F(SANS_M, 68), fill=INK)
                bw = d.textlength(bad, font=F(SANS_M, 68))
                d.line((bx-10, fy+90, bx+bw+10, fy+90), fill=SEND, width=6)
        bug(d)
        return img
    return [base(False), base(True)]

# ============================================================= B07 (vertical)
def b07_stages():
    def base():
        img, d = canvas()
        d.text((MARGIN, 220),
               "TWO CLOSING RULES", font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 320), "Repo",     font=F(SERIF_M, 190), fill=INK)
        d.text((MARGIN, 520), "+ rhythm", font=F(SERIF_M, 190), fill=INK)
        rw = d.textlength("+ rhythm", font=F(SERIF_M, 190))
        d.text((MARGIN + rw, 520), ".",   font=F(SERIF_M, 190), fill=SEND)
        bug(d)
        return img, d

    top_y = 900; bot_y = 2300
    ph = 1300; pw = CONTENT_W

    def draw_top(d):
        d.rectangle((MARGIN, top_y, MARGIN+pw, top_y+ph),
                    outline=INK, width=6, fill=CARD)
        d.text((MARGIN+60, top_y+60), "GITHUB — MANDATORY",
               font=F(SANS_M, 46), fill=SEND)
        d.text((MARGIN+60, top_y+180), "Every submission",
               font=F(SERIF_M, 110), fill=INK)
        d.text((MARGIN+60, top_y+330), "ships a repo URL.",
               font=F(SERIF_M, 110), fill=INK)
        d.rectangle((MARGIN+60, top_y+720, MARGIN+pw-60, top_y+880),
                    outline=INK_S, width=3)
        d.text((MARGIN+90, top_y+760),
               "github.com/HumanitariansAI/<project>",
               font=F(SANS, 46), fill=INK)
        d.text((MARGIN+60, top_y+ph-150),
               "No repo → no upload.",
               font=F(SERIF_R, 60), fill=INK_S)

    def draw_bot(d):
        d.rectangle((MARGIN, bot_y, MARGIN+pw, bot_y+ph),
                    outline=INK, width=6, fill=CREAM)
        d.text((MARGIN+60, bot_y+60), "SHORTS · SCHEDULING",
               font=F(SANS_M, 46), fill=SEND)
        d.text((MARGIN+60, bot_y+180), "9:16 posts space",
               font=F(SERIF_M, 110), fill=INK)
        d.text((MARGIN+60, bot_y+330), "≥ 60 min apart.",
               font=F(SERIF_M, 110), fill=INK)
        for i, cx in enumerate((MARGIN+340, MARGIN+900)):
            cy = bot_y+800
            d.ellipse((cx-160, cy-160, cx+160, cy+160), outline=INK, width=6)
            d.line((cx, cy, cx, cy-100), fill=INK, width=6)
            d.line((cx, cy, cx, cy-130), fill=SEND, width=6)
            d.text((cx, cy+200), ["T", "T + 60 min"][i],
                   font=F(SANS_M, 46), fill=INK_S, anchor="ma")
        d.text((MARGIN+60, bot_y+ph-160),
               "Each Short links to the most",
               font=F(SERIF_R, 48), fill=INK_S)
        d.text((MARGIN+60, bot_y+ph-100),
               "popular related HAI video.",
               font=F(SERIF_R, 48), fill=INK_S)

    stages = []
    img, d = base(); stages.append(img)
    img, d = base(); draw_top(d); stages.append(img)
    img, d = base(); draw_top(d); draw_bot(d); stages.append(img)
    return stages

# ============================================================= native 9:16 Claude beats
#  (replace the tiny letterboxed landscape wraps — large, legible, no labels)

def _wrap(d, text, fnt, max_w):
    words = text.split(); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def _spark(d, cx, cy, r, color, width=8):
    """The Claude terracotta spark — a 6-armed asterisk drawn with lines."""
    import math
    for k in range(6):
        a = math.pi * k / 3
        d.line((cx - r*math.cos(a), cy - r*math.sin(a),
                cx + r*math.cos(a), cy + r*math.sin(a)),
               fill=color, width=width)

def _composer_card(greeting, command, running, kicker_txt):
    """A large, phone-legible Claude composer rendition for 9:16."""
    def base(stage):
        img, d = canvas()
        d.text((MARGIN, 240), kicker_txt, font=F(SANS_M, 42), fill=INK_S)
        # terracotta spark + greeting, big serif
        _spark(d, MARGIN + 55, 640, 55, SEND, width=10)
        d.text((MARGIN + 170, 560), greeting, font=F(SERIF_M, 150), fill=INK)
        if stage >= 1:
            # prompt bubble
            bx, by = MARGIN, 1180
            bw, bh = CONTENT_W, 1500
            d.rounded_rectangle((bx, by, bx+bw, by+bh), radius=48,
                                outline=LINE, width=6, fill="#FFFFFF")
            lines = _wrap(d, command, F(SANS, 70), bw - 160)
            ty = by + 90
            for ln in lines:
                d.text((bx + 80, ty), ln, font=F(SANS, 70), fill=INK)
                ty += 108
            # a small + affordance
            d.ellipse((bx+70, by+bh-160, bx+150, by+bh-80),
                      outline=INK_S, width=5)
            d.text((bx+110, by+bh-120), "+", font=F(SANS, 60),
                   fill=INK_S, anchor="mm")
        if stage >= 2:
            # folder chip + running line beneath the bubble
            fy = 2800
            # small drawn folder glyph
            d.rectangle((MARGIN, fy+14, MARGIN+52, fy+50), outline=INK_S, width=4)
            d.rectangle((MARGIN, fy+6, MARGIN+26, fy+20), outline=INK_S, width=4)
            d.text((MARGIN + 80, fy), "@HumanitariansAI",
                   font=F(SANS, 46), fill=INK_S)
            _spark(d, MARGIN + 24, fy + 130, 22, SEND, width=5)
            d.text((MARGIN + 80, fy + 100), running,
                   font=F(SANS, 46), fill=SEND)
        bug(d)
        return img
    return [base(0), base(1), base(2)]

def b00_native():
    return _composer_card(
        greeting="Hola, Sanjana",
        command=('claude "walk me through the Humanitarians AI YouTube '
                 'video review process — for a new fellow."'),
        running="this is Liam, in for Sanjana…",
        kicker_txt="HUMANITARIANS AI · FELLOWS BRIEFING")

def b08_native():
    return _composer_card(
        greeting="Your turn.",
        command=('claude "before you submit: Brutalist on the latest weekly '
                 'release · render 4K, both aspects, native · open with the '
                 'intro line · rename ProjectName_VolunteerName · push to '
                 'GitHub and share the URL · upload to the Drive, notify '
                 'Sanjana or Pooja."'),
        running="run this before every submission…",
        kicker_txt="HANDOFF · YOUR TURN")

def b05_native():
    """Six-criteria checklist, native 9:16, revealed in groups."""
    crit = [
        ("1", "Brutalist format", "current-week release"),
        ("2", "4K — source & upload", "still 2160p after YouTube"),
        ("3", "Both aspect ratios", "16:9 and 9:16, native"),
        ("4", "Clean formatting", "images render, text legible"),
        ("5", "Intro line present", "“Hi, I am [Name], and…”"),
        ("6", "Real takeaway", "one thing the viewer can now do"),
    ]
    def base(upto):
        img, d = canvas()
        d.text((MARGIN, 240), "THE PM GATE", font=F(SANS_M, 44), fill=INK_S)
        d.text((MARGIN, 340), "Six checks,", font=F(SERIF_M, 170), fill=INK)
        d.text((MARGIN, 520), "one gate",    font=F(SERIF_M, 170), fill=INK)
        tw = d.textlength("one gate", font=F(SERIF_M, 170))
        d.text((MARGIN + tw, 520), ".",      font=F(SERIF_M, 170), fill=SEND)
        y0 = 900; row_h = 470
        for i, (n, head, sub) in enumerate(crit[:upto]):
            y = y0 + i*row_h
            d.ellipse((MARGIN, y, MARGIN+150, y+150),
                      outline=INK, width=7, fill=CARD)
            d.text((MARGIN+75, y+75), n, font=F(SERIF_M, 90),
                   fill=SEND, anchor="mm")
            d.text((MARGIN+210, y+10), head, font=F(SERIF_M, 82), fill=INK)
            d.text((MARGIN+210, y+120), sub, font=F(SANS, 44), fill=INK_S)
        bug(d)
        return img
    return [base(2), base(4), base(6)]

def b09_native():
    """Outro, centered, large."""
    def base(stage):
        img, d = canvas()
        title_lines = ["How the", "Humanitarians AI", "Video Review",
                       "Process Works"]
        y = 1000
        for i, ln in enumerate(title_lines):
            d.text((W//2, y), ln, font=F(SERIF_M, 150), fill=INK, anchor="ma")
            if i == len(title_lines)-1:
                lw = d.textlength(ln, font=F(SERIF_M, 150))
                d.text((W//2 + lw//2 + 6, y), ".", font=F(SERIF_M, 150),
                       fill=SEND, anchor="ma")
            y += 210
        if stage >= 1:
            d.text((W//2, 2200), "@HumanitariansAI",
                   font=F(SERIF_M, 90), fill=INK, anchor="ma")
            d.text((W//2, 2360), "Liam, in for Sanjana",
                   font=F(SANS_M, 54), fill=INK_S, anchor="ma")
            d.text((W//2, 2440), "a fellows briefing",
                   font=F(SANS, 48), fill=INK_S, anchor="ma")
        return img
    return [base(0), base(1)]

# ============================================================= Remotion wrapper (legacy, unused)
def wrap_remotion(bid, dur, label_top, label_bot):
    src = LANDSCAPE / f"{bid}.mp4"
    inner_w = W
    inner_h = int(inner_w * 9 / 16)  # 1215
    y_video = (H - inner_h) // 2

    frame_img, d = canvas()
    d.text((W//2, 700), label_top,
           font=F(SERIF_M, 100), fill=INK, anchor="mm")
    tw = d.textlength(label_top, font=F(SERIF_M, 100))
    d.text((W//2 + tw//2, 700), ".",
           font=F(SERIF_M, 100), fill=SEND, anchor="lm")
    d.text((W//2, y_video - 100), label_bot,
           font=F(SANS_M, 46), fill=INK_S, anchor="mm")
    bug(d)
    frame_png = TMP / f"_wrap_{bid}.png"
    frame_img.save(frame_png)

    out = MEDIA / f"{bid}.mp4"
    cmd = ["ffmpeg", "-y",
           "-loop", "1", "-t", f"{dur:.3f}", "-i", str(frame_png),
           "-i", str(src),
           "-filter_complex",
           f"[1:v]scale={inner_w}:{inner_h},setsar=1,fps=30[vid];"
           f"[0:v]scale={W}:{H},setsar=1,fps=30[bg];"
           f"[bg][vid]overlay=0:{y_video}[vout]",
           "-map", "[vout]", "-t", f"{dur:.3f}",
           "-r", "30", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-2500:])
        raise SystemExit(f"[render_slates_vert] wrap failed for {bid}")
    print(f"[render_slates_vert] {bid} → {out.name}  {dur:.1f}s (wrapped)")

# ============================================================= encode
REVEAL = 0.9
HOLD   = 0.9

def encode_stages(bid, dur, stages):
    n = len(stages)
    reserved = (n - 1) * (HOLD + REVEAL)
    tail_hold = dur - reserved
    if tail_hold < 1.5:
        stages = [stages[0], stages[-1]]
        n = 2
        reserved = HOLD + REVEAL
        tail_hold = max(2.0, dur - reserved)

    pngs = []
    for i, img in enumerate(stages):
        p = TMP / f"{bid}_s{i}.png"
        img.save(p, optimize=True)
        pngs.append(p)

    D = [0.0] * n
    D[0] = HOLD + REVEAL if n > 1 else dur
    for i in range(1, n - 1):
        D[i] = REVEAL + HOLD + REVEAL
    if n > 1:
        D[-1] = REVEAL + tail_hold

    inputs = []
    for p, sd in zip(pngs, D):
        inputs += ["-loop", "1", "-t", f"{sd:.3f}", "-i", str(p)]

    fc = []
    for i in range(n):
        fc.append(f"[{i}:v]scale={W}:{H},setsar=1,fps=30[v{i}]")
    prev = "v0"
    offset = HOLD
    for i in range(1, n):
        out = f"x{i}" if i < n - 1 else "vout"
        fc.append(f"[{prev}][v{i}]xfade=transition=fade:duration={REVEAL}:offset={offset:.3f}[{out}]")
        offset += HOLD + REVEAL
        prev = out

    mp4 = MEDIA / f"{bid}.mp4"
    cmd = ["ffmpeg", "-y", *inputs,
           "-filter_complex", ";".join(fc),
           "-map", "[vout]", "-t", f"{dur:.3f}",
           "-r", "30", "-c:v", "libx264", "-preset", "medium",
           "-crf", "18", "-pix_fmt", "yuv420p", str(mp4)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-2500:])
        raise SystemExit(f"[render_slates_vert] encode failed for {bid}")
    print(f"[render_slates_vert] {bid} → {mp4.name}  {dur:.1f}s  ({n} stages)")

# ============================================================= main
DURS = {b["beat_id"]: b.get("actual_duration_s") or b["estimated_duration_s"]
        for b in json.loads((REEL/"beat_sheet.json").read_text())["beats"]}

# B07 is DROPPED from the Short (longest peripheral middle beat) to clear the
# 3:00 YouTube Shorts cap. Every remaining beat is a NATIVE 9:16 render.
BUILDERS = [
    ("B00", b00_native),
    ("B01", b01_stages),
    ("B02", b02_stages),
    ("B03", b03_stages),
    ("B04", b04_stages),
    ("B05", b05_native),
    ("B06", b06_stages),
    ("B08", b08_native),
    ("B09", b09_native),
]
for bid, fn in BUILDERS:
    encode_stages(bid, float(DURS[bid]), fn())
print("[render_slates_vert] done (B07 dropped for the 3:00 Shorts cap).")
