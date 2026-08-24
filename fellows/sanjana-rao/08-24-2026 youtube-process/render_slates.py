"""16:9 native 4K (3840x2160) animated slate renderer.

Every dimension is in true 4K pixels — no dual-scale math. Each authored beat
emits N reveal stages that fade into each other; the final stage holds with a
subtle Ken Burns zoom.
"""
from __future__ import annotations
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ------------------------------------------------------------- palette + paths
CREAM  = "#FAF9F5"
INK    = "#3D3929"
INK_S  = "#6b6357"
SEND   = "#D97757"
LINE   = "#E7E4DC"
CARD   = "#F1EEE4"

W, H = 3840, 2160
MARGIN = 200
CONTENT_W = W - 2*MARGIN  # 3440

TOOL = Path(r"C:/Users/Sanjana/OneDrive/Desktop/Humanitarians AI Brutalist files/brutalist.art")
REEL = Path(r"C:/Users/Sanjana/OneDrive/Desktop/Humanitarians AI Brutalist files/YouTube Process/youtube-process")
REF  = REEL.parent
MEDIA = REEL / "media"; MEDIA.mkdir(exist_ok=True)
TMP = REEL / "_slate_png"; TMP.mkdir(exist_ok=True)

SERIF_R = str(TOOL / "runtime/fonts/EB_Garamond/static/EBGaramond-Regular.ttf")
SERIF_M = str(TOOL / "runtime/fonts/EB_Garamond/static/EBGaramond-Medium.ttf")
SANS    = str(TOOL / "runtime/fonts/Inter/static/Inter_28pt-Regular.ttf")
SANS_M  = str(TOOL / "runtime/fonts/Inter/static/Inter_28pt-Medium.ttf")
def F(p, sz): return ImageFont.truetype(p, sz)

# ------------------------------------------------------------- primitives
def canvas(bg=CREAM):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)

def kicker(d, text, y=180):
    d.text((MARGIN, y), text, font=F(SANS_M, 44), fill=INK_S)

def title_period(d, x, y, body, size=180):
    d.text((x, y), body, font=F(SERIF_M, size), fill=INK)
    tw = d.textlength(body, font=F(SERIF_M, size))
    d.text((x + tw, y), ".", font=F(SERIF_M, size), fill=SEND)

def bug(d):
    d.text((W-MARGIN, H-90), "@HumanitariansAI",
           font=F(SANS, 40), fill=INK_S, anchor="rb")

# ============================================================= B01 · pipeline
def b01_stages():
    def base():
        img, d = canvas()
        kicker(d, "HUMANITARIANS AI · FELLOWS BRIEFING")
        title_period(d, MARGIN, 260, "The Video Review Pipeline", 180)
        bug(d)
        return img, d

    stages = []

    img, d = base(); stages.append(img)
    img, d = base()
    d.text((MARGIN, 620),
           "Two videos a week.  Six criteria.  One queue.",
           font=F(SERIF_R, 90), fill=INK_S)
    stages.append(img)

    stops = [
        ("FELLOW",              "uploads to Drive"),
        ("SANJANA / POOJA",     "reviews vs. 6 criteria"),
        ("QUEUE",               "playlist on YouTube"),
        ("PROF. BROWN & NINA",  "final feedback"),
    ]
    y_row = 1420
    col = CONTENT_W // 4

    def draw_pipeline(d, upto):
        for i, (name, sub) in enumerate(stops[:upto]):
            cx = MARGIN + col*i + col//2
            d.ellipse((cx-90, y_row-90, cx+90, y_row+90),
                      outline=INK, width=8, fill=CARD)
            d.text((cx, y_row), str(i+1), font=F(SERIF_M, 100), fill=SEND, anchor="mm")
            d.text((cx, y_row+170), name, font=F(SANS_M, 44), fill=INK, anchor="ma")
            d.text((cx, y_row+240), sub,  font=F(SANS,   38), fill=INK_S, anchor="ma")
            if i < upto - 1:
                ax1 = MARGIN + col*i + col//2 + 110
                ax2 = MARGIN + col*(i+1) + col//2 - 110
                d.line((ax1, y_row, ax2, y_row), fill=INK, width=6)
                d.polygon([(ax2, y_row-18),(ax2+22, y_row),(ax2, y_row+18)], fill=INK)

    # Progressive reveal: subhead → 1 node → 2 → 3 → all 4
    subline = "Two videos a week.  Six criteria.  One queue."
    for k in (1, 2, 3, 4):
        img, d = base()
        d.text((MARGIN, 620), subline, font=F(SERIF_R, 90), fill=INK_S)
        draw_pipeline(d, k)
        stages.append(img)
    return stages

# ============================================================= B02 · weekly grid
def b02_stages():
    def base():
        img, d = canvas()
        kicker(d, "WEEKLY CADENCE")
        title_period(d, MARGIN, 260, "Two videos · four files", 180)
        bug(d)
        return img, d

    # Grid inside the safe area — 2 cols x 2 rows
    grid_x = MARGIN
    grid_y = 700
    gap = 60
    cw = (CONTENT_W - gap) // 2       # 1690
    ch = 480
    cells = [
        ("Video 1", "STEM / AI topic", "16:9", "landscape",      True),
        ("Video 1", "STEM / AI topic", "9:16", "vertical Short", False),
        ("Video 2", "Project update",  "16:9", "landscape",      True),
        ("Video 2", "Project update",  "9:16", "vertical Short", False),
    ]

    def draw_cells(d, k):
        for i, (row, sub, aspect, atag, filled) in enumerate(cells[:k]):
            r, c = i//2, i%2
            x = grid_x + c*(cw+gap); yy = grid_y + r*(ch+gap)
            d.rectangle((x, yy, x+cw, yy+ch),
                        outline=INK, width=6, fill=CARD if filled else CREAM)
            d.text((x+50, yy+50), row.upper(), font=F(SANS_M, 44), fill=SEND)
            d.text((x+50, yy+130), sub, font=F(SERIF_M, 96), fill=INK)
            d.text((x+cw-50, yy+ch-80), aspect,
                   font=F(SERIF_M, 100), fill=INK, anchor="rb")
            d.text((x+cw-50, yy+ch-190), atag,
                   font=F(SANS, 40), fill=INK_S, anchor="rb")

    def draw_footer(d):
        fy = grid_y + 2*(ch+gap) + 60
        d.line((MARGIN, fy, W-MARGIN, fy), fill=LINE, width=4)
        d.text((MARGIN, fy+40),
               "Floor: at least 1 research update in every rolling two-week window.",
               font=F(SERIF_R, 56), fill=INK)

    stages = []
    img, d = base(); stages.append(img)
    img, d = base(); draw_cells(d, 2); stages.append(img)
    img, d = base(); draw_cells(d, 4); stages.append(img)
    img, d = base(); draw_cells(d, 4); draw_footer(d); stages.append(img)
    return stages

# ============================================================= B03 · five steps
def b03_stages():
    steps = [
        ("1", "Fellow uploads to Drive + notifies",     "FELLOW"),
        ("2", "Review vs. 6 criteria",                  "SANJANA / POOJA"),
        ("3", "Quality checks — format · 4K · content", "SANJANA / POOJA"),
        ("4", "Upload to HAI YouTube · Queue playlist", "HAI CHANNEL"),
        ("5", "Final feedback: publish or send back",   "PROF. BROWN & PROF. NINA"),
    ]

    def base():
        img, d = canvas()
        kicker(d, "PROCESS FLOW")
        title_period(d, MARGIN, 260, "Five steps, two owners", 170)
        bug(d)
        return img, d

    y0 = 620; row_h = 260
    def draw_steps(d, k):
        for i, (n, what, who) in enumerate(steps[:k]):
            y = y0 + i*row_h
            d.ellipse((MARGIN, y, MARGIN+180, y+180),
                      outline=INK, width=8, fill=CARD)
            d.text((MARGIN+90, y+90), n, font=F(SERIF_M, 108), fill=SEND, anchor="mm")
            d.text((MARGIN+240, y+30), what, font=F(SERIF_M, 78), fill=INK)
            d.text((MARGIN+240, y+140), who, font=F(SANS_M, 44), fill=INK_S)
            if i < k-1:
                d.line((MARGIN+240, y+row_h-15, W-MARGIN, y+row_h-15),
                       fill=LINE, width=3)

    stages = []
    img, d = base(); stages.append(img)
    for k in (2, 4, 5):
        img, d = base(); draw_steps(d, k); stages.append(img)
    return stages

# ============================================================= B04 · quality selector
def b04_stages():
    src = REF / "Quality upto 2160p.png"
    ref = Image.open(src).convert("RGB")
    target_w = 2400
    ratio = target_w / ref.width
    ref = ref.resize((target_w, int(ref.height * ratio)), Image.LANCZOS)

    def base(with_callout=False):
        img, d = canvas()
        kicker(d, "VIDEO STANDARDS · 4K ON YOUTUBE")
        title_period(d, MARGIN, 260, "It has to stream 2160p", 160)
        rx = (W - ref.width) // 2
        ry = 540
        img.paste(ref, (rx, ry))
        d = ImageDraw.Draw(img)
        if with_callout:
            # Callout sits in the empty band ABOVE the screenshot so it never
            # overlaps composer text. An L-shaped arrow drops down to the
            # "2160p 4K" pill (top of the Quality menu on the right).
            px = rx + int(ref.width * 0.78)   # pill x
            py = ry + int(ref.height * 0.34)  # pill y
            band_y = 490                       # label baseline in the top band
            # label
            d.text((px - 30, band_y), "stream 2160p after upload",
                   font=F(SANS_M, 52), fill=SEND, anchor="rb")
            # vertical shaft
            d.line((px, band_y + 20, px, py - 30), fill=SEND, width=10)
            # arrowhead pointing down at the pill
            d.polygon([(px, py), (px - 22, py - 40), (px + 22, py - 40)], fill=SEND)
        bug(d)
        return img
    return [base(False), base(True)]

# ============================================================= B06 · Drive folder
def b06_stages():
    src = REF / "Screenshot 2026-08-23 111738.png"
    ref = Image.open(src).convert("RGB")
    target_w = 2400
    ratio = target_w / ref.width
    ref = ref.resize((target_w, int(ref.height * ratio)), Image.LANCZOS)

    def base(show_rules=False):
        img, d = canvas()
        kicker(d, "NAMING · SHARED DRIVE")
        title_period(d, MARGIN, 260, "ProjectName_VolunteerName", 130)
        rx = (W - ref.width)//2
        ry = 540
        img.paste(ref, (rx, ry))
        d = ImageDraw.Draw(img)
        if show_rules:
            fy = ry + ref.height + 60
            d.text((MARGIN, fy), "NO", font=F(SANS_M, 44), fill=SEND)
            x0 = MARGIN + 130
            for i, bad in enumerate(("spaces", "dates", "_v2", "_final")):
                bx = x0 + i*520
                d.text((bx, fy-6), bad, font=F(SANS_M, 60), fill=INK)
                bw = d.textlength(bad, font=F(SANS_M, 60))
                d.line((bx-10, fy+80, bx+bw+10, fy+80), fill=SEND, width=6)
        bug(d)
        return img
    return [base(False), base(True)]

# ============================================================= B07 · GitHub + scheduling
def b07_stages():
    def base():
        img, d = canvas()
        kicker(d, "TWO CLOSING RULES")
        title_period(d, MARGIN, 260, "Repo + rhythm", 180)
        bug(d)
        return img, d

    panel_y = 700
    panel_h = 1220
    gap = 100
    pw = (CONTENT_W - gap) // 2   # 1670
    lx = MARGIN
    rx = MARGIN + pw + gap

    def draw_left(d):
        d.rectangle((lx, panel_y, lx+pw, panel_y+panel_h),
                    outline=INK, width=6, fill=CARD)
        d.text((lx+60, panel_y+60), "GITHUB — MANDATORY",
               font=F(SANS_M, 46), fill=SEND)
        d.text((lx+60, panel_y+180), "Every submission",
               font=F(SERIF_M, 96), fill=INK)
        d.text((lx+60, panel_y+300), "ships a repo URL.",
               font=F(SERIF_M, 96), fill=INK)
        d.rectangle((lx+60, panel_y+700, lx+pw-60, panel_y+840),
                    outline=INK_S, width=3)
        d.text((lx+90, panel_y+735),
               "github.com/HumanitariansAI/<project>",
               font=F(SANS, 52), fill=INK)
        d.text((lx+60, panel_y+panel_h-130),
               "No repo → no upload.",
               font=F(SERIF_R, 60), fill=INK_S)

    def draw_right(d):
        d.rectangle((rx, panel_y, rx+pw, panel_y+panel_h),
                    outline=INK, width=6, fill=CREAM)
        d.text((rx+60, panel_y+60), "SHORTS · SCHEDULING",
               font=F(SANS_M, 46), fill=SEND)
        d.text((rx+60, panel_y+180), "9:16 posts space",
               font=F(SERIF_M, 96), fill=INK)
        d.text((rx+60, panel_y+300), "≥ 60 min apart.",
               font=F(SERIF_M, 96), fill=INK)
        # two clocks
        for i, cx in enumerate((rx+380, rx+900)):
            cy = panel_y+780
            d.ellipse((cx-140, cy-140, cx+140, cy+140), outline=INK, width=6)
            d.line((cx, cy, cx, cy-90), fill=INK, width=6)
            d.line((cx, cy, cx, cy-118), fill=SEND, width=6)
            d.text((cx, cy+180), ["T", "T + 60 min"][i],
                   font=F(SANS_M, 44), fill=INK_S, anchor="ma")
        d.text((rx+60, panel_y+panel_h-130),
               "Each Short links to the most popular related HAI video.",
               font=F(SERIF_R, 48), fill=INK_S)

    stages = []
    img, d = base(); stages.append(img)
    img, d = base(); draw_left(d); stages.append(img)
    img, d = base(); draw_left(d); draw_right(d); stages.append(img)
    return stages

# ------------------------------------------------------------- encode
BEATS = [
    ("B01", 16.87, b01_stages),
    ("B02", 22.36, b02_stages),
    ("B03", 27.77, b03_stages),
    ("B04", 28.11, b04_stages),
    ("B06", 19.88, b06_stages),
    ("B07", 28.64, b07_stages),
]

REVEAL = 0.9
HOLD   = 0.9

def encode(bid, dur, stages):
    n = len(stages)
    # Total video length with proper reveals + holds:
    #   dur = (n-1) * (HOLD + REVEAL) + tail_hold
    reserved = (n - 1) * (HOLD + REVEAL)
    tail_hold = dur - reserved
    if tail_hold < 1.5:
        # collapse to 2 stages so tail_hold has room
        stages = [stages[0], stages[-1]]
        n = 2
        reserved = HOLD + REVEAL
        tail_hold = max(2.0, dur - reserved)

    # Save PNGs
    pngs = []
    for i, img in enumerate(stages):
        p = TMP / f"{bid}_s{i}.png"
        img.save(p, optimize=True)
        pngs.append(p)

    # Per-stage input durations (long enough for the xfade to consume them)
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
    offset = HOLD  # first xfade begins after stage 0 has held
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
        raise SystemExit(f"[render_slates] ffmpeg failed for {bid}")
    print(f"[render_slates] {bid} → {mp4.name}  {dur:.1f}s  ({n} stages)")

for bid, dur, fn in BEATS:
    encode(bid, dur, fn())
print("[render_slates] done.")
