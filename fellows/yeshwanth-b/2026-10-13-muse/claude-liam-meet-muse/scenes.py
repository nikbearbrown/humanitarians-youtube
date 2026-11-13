"""Body scenes for claude-liam-meet-muse, drawn natively in 16:9 and 9:16.

    python3 scenes.py landscape REEL_DIR          # writes media/Bxx.mp4 (3840x2160)
    python3 scenes.py portrait  VERTICAL_DIR      # writes media/Bxx.mp4 (2160x3840)

Claude palette (cream page, warm ink, one terracotta accent). Each element fades in
on its spoken cue (cue_times in the beat sheet). Type is sized above GATE T floors:
x-height >= ~46 px in landscape, >= ~80 px in portrait. Interfaces of Blender and
Godot are labelled reconstructions; the Muse panel is a labelled illustrative stand-in
(no real Muse capture exists). Nothing here is a recording.
"""
import json
import math
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS = Path(os.environ.get('BRUTALIST_HOME', '/Users/yeshwanthbalaji/Documents/Brutalist_Updated')) / 'runtime/fonts'
SERIF = FONTS / 'EB_Garamond/static/EBGaramond-Medium.ttf'
SANS = FONTS / 'Inter/static/Inter_28pt-Medium.ttf'
SANS_R = FONTS / 'Inter/static/Inter_28pt-Regular.ttf'
MONO = FONTS / 'PT_Mono/PTMono-Regular.ttf'
PAGE, INK, SOFT, ACC = (0xFA, 0xF9, 0xF5), (0x3D, 0x39, 0x29), (0x5E, 0x54, 0x45), (0xD9, 0x77, 0x57)
ACC_D, ACC_BG, CARD, BORDER = (0x98, 0x50, 0x39), (0xF2, 0xE5, 0xD8), (0xFF, 0xFD, 0xF8), (0xCF, 0xC6, 0xB5)
DARK, STATUS = (0x30, 0x3D, 0x34), (0x30, 0x3D, 0x34)
FPS, FADE = 30, 10
HANDLE = '@HumanitariansAI'


class Frame:
    def __init__(self, w, h):
        self.w, self.h, self.p = w, h, h > w
        if self.p:
            self.sx0, self.sx1, self.sy0, self.sy1 = 108, 2052, 192, 3302
            self.body, self.small, self.title, self.mono = 148, 148, 178, 154
        else:
            self.sx0, self.sx1, self.sy0, self.sy1 = 192, 3648, 108, 2052
            self.body, self.small, self.title, self.mono = 92, 88, 150, 96
        self.sw, self.sh = self.sx1 - self.sx0, self.sy1 - self.sy0
        self.head = self.title if self.p else self.title * 0.85

    def f(self, path, size):
        return ImageFont.truetype(str(path), int(size))


def layer(fr):
    img = Image.new('RGBA', (fr.w, fr.h), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)


def wrap(d, text, f, width):
    out, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def text(d, xy, s, f, fill, width=None, lh=1.2, align='left'):
    x, y = xy
    lines = wrap(d, s, f, width) if width else [s]
    for ln in lines:
        xx = x if align == 'left' else x + (width - d.textlength(ln, font=f)) / 2
        d.text((xx, y), ln, font=f, fill=fill)
        y += int(f.size * lh)
    return y


def text_h(d, s, f, width, lh=1.2):
    return int(f.size * lh) * len(wrap(d, s, f, width))


def card(d, box, fill=CARD, outline=BORDER, accent=False, r=30):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=ACC_D if accent else outline, width=6)
    if accent:
        d.rectangle([box[0], box[1] + r, box[0] + 16, box[3] - r], fill=ACC_D)


def arrow(d, a, b, fill=INK, w=18):
    d.line([a, b], fill=fill, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    L = w * 4
    p1 = (b[0] - L * math.cos(ang - 0.45), b[1] - L * math.sin(ang - 0.45))
    p2 = (b[0] - L * math.cos(ang + 0.45), b[1] - L * math.sin(ang + 0.45))
    d.polygon([b, p1, p2], fill=fill)


def base(fr, title):
    img = Image.new('RGBA', (fr.w, fr.h), PAGE + (255,))
    d = ImageDraw.Draw(img)
    y = text(d, (fr.sx0, fr.sy0), title, fr.f(SERIF, fr.title), INK, width=fr.sw, lh=1.08)
    if not fr.p:
        fh = fr.f(SERIF, 104)
        d.text((fr.sx1 - d.textlength(HANDLE, font=fh), fr.sy1 - 122), HANDLE, font=fh, fill=INK)
    return img, y + (40 if fr.p else 30)


def recon_badge(d, fr, x, y, s):
    f = fr.f(SANS, fr.small)
    tw = d.textlength(s, font=f)
    d.rounded_rectangle([x, y, x + tw + 60, y + int(f.size * 1.5)], radius=20, fill=(0x55, 0x2E, 0x22))
    d.text((x + 30, y + int(f.size * 0.2)), s, font=f, fill=(0xFF, 0xF4, 0xEC))
    return y + int(f.size * 1.5)


# ---------------------------------------------------------------- scenes
# Each returns (base_image, [element layers]) in cue order.

def sc_terms(fr, spec, title):
    img, y0 = base(fr, title)
    els = []
    avail = fr.sy1 - (140 if not fr.p else 0) - y0
    n = len(spec['terms'])
    gap = 40
    h = (avail - gap * (n - 1)) // n
    for i, (term, defin) in enumerate(spec['terms']):
        L, d = layer(fr)
        top = y0 + i * (h + gap)
        card(d, [fr.sx0, top, fr.sx1, top + h], accent=True)
        if fr.p:
            text(d, (fr.sx0 + 70, top + 40), term, fr.f(SERIF, fr.title), ACC_D)
            text(d, (fr.sx0 + 70, top + 40 + int(fr.title * 1.15)), defin, fr.f(SANS_R, fr.body), INK, width=fr.sw - 140)
        else:
            text(d, (fr.sx0 + 80, top + (h - fr.title) // 2 - 20), term, fr.f(SERIF, fr.title), ACC_D)
            dh = text_h(d, defin, fr.f(SANS_R, fr.body), fr.sw - 1300)
            text(d, (fr.sx0 + 1150, top + (h - dh) // 2), defin, fr.f(SANS_R, fr.body), INK, width=fr.sw - 1300)
        els.append(L)
    return img, els


def sc_problem(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    els = []
    fb, fs = fr.f(SANS_R, fr.body), fr.f(SANS, fr.body)
    if fr.p:
        colA = (fr.sx0, y0, fr.sx1, y0 + 960)
        colB = (fr.sx0, y0 + 1000, fr.sx1, y0 + 2020)
        colC = (fr.sx0, y0 + 2060, fr.sx1, bot)
    else:
        colA = (fr.sx0, y0, fr.sx0 + 1050, bot)
        colB = (fr.sx0 + 1130, y0, fr.sx0 + 2300, bot)
        colC = (fr.sx0 + 2380, y0, fr.sx1, bot)
    # chatbot: one question, one answer, done
    L, d = layer(fr)
    card(d, colA)
    x0, y = colA[0] + 50, colA[1] + 40
    y = text(d, (x0, y), 'Chatbot', fr.f(SERIF, fr.head), INK)
    d.rounded_rectangle([x0, y + 20, colA[2] - 50, y + 20 + int(fr.body * 1.5)], radius=24, fill=CARD, outline=SOFT, width=5)
    d.text((x0 + 30, y + 30), 'Q: a question', font=fb, fill=INK)
    y += int(fr.body * 1.5) + 50
    d.rounded_rectangle([x0, y, colA[2] - 50, y + int(fr.body * 1.5)], radius=24, fill=CARD, outline=ACC_D, width=5)
    d.text((x0 + 30, y + 10), 'A: an answer', font=fb, fill=INK)
    y += int(fr.body * 1.5) + 30
    d.text((x0, y), 'Then it stops.', font=fs, fill=ACC_D)
    els.append(L)
    # the long multi-step job
    L, d = layer(fr)
    card(d, colB)
    steps = ['Install a tool', 'Write a script', 'Run it', 'Check output', 'Fix it', 'Run again']
    x0 = colB[0] + 50
    y = text(d, (x0, colB[1] + 40), 'A game or 3D asset', fr.f(SERIF, fr.head), INK, width=colB[2] - colB[0] - 100)
    els.append(L)
    L, d = layer(fr)
    avail = colB[3] - 40 - y
    step_h = min(int(fr.body * 1.45), avail // len(steps))
    if fr.p:
        for i, s in enumerate(['Install a tool', 'Write a script', 'Run and check', 'Fix, run again']):
            d.text((x0, y + i * int(fr.body * 1.25)), f'{i + 1}. {s}', font=fb, fill=INK)
    else:
        for i, s in enumerate(steps):
            d.text((x0, y + i * step_h), f'{i + 1}. {s}', font=fb, fill=INK)
    els.append(L)
    # your computer, busy
    L, d = layer(fr)
    card(d, colC)
    x0, y = colC[0] + 50, colC[1] + 40
    y = text(d, (x0, y), 'Your computer', fr.f(SERIF, fr.head), INK, width=colC[2] - colC[0] - 100)
    for lab in (('Memory and disk',) if fr.p else ('Memory', 'Disk')):
        d.text((x0, y + 10), lab, font=fs, fill=INK)
        y += int(fr.body * 1.3)
        d.rounded_rectangle([x0, y, colC[2] - 50, y + 40], radius=14, fill=ACC_D)
        y += 90 if fr.p else 110
    d.text((x0, y), 'Busy', font=fs, fill=ACC_D)
    els.append(L)
    return img, els


def cloud(d, box, fill=CARD, outline=INK):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    for cx, cy, r in ((0.3, 0.6, 0.28), (0.55, 0.42, 0.34), (0.78, 0.62, 0.24)):
        d.ellipse([x0 + w * cx - h * r * 1.5, y0 + h * cy - h * r * 1.5, x0 + w * cx + h * r * 1.5, y0 + h * cy + h * r * 1.5],
                  fill=fill, outline=outline, width=8)
    d.rounded_rectangle([x0 + w * 0.12, y0 + h * 0.55, x1 - w * 0.08, y1], radius=int(h * 0.2), fill=fill, outline=outline, width=8)
    d.rectangle([x0 + w * 0.14, y0 + h * 0.5, x1 - w * 0.1, y1 - 10], fill=fill)


def sc_flow(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fb, fT = fr.f(SANS, fr.body), fr.f(SERIF, fr.head)
    els = []
    if fr.p:
        H = (bot - y0) // 5
        boxes = [(fr.sx0 + 120, y0 + i * H + 10, fr.sx1 - 120, y0 + i * H + H - 100) for i in range(5)]
    else:
        W = (fr.sx1 - fr.sx0) // 5
        mid = (y0 + bot) // 2
        boxes = [(fr.sx0 + i * W, y0 + 60, fr.sx0 + i * W + W - 110, bot - 60) for i in range(5)]
    if fr.p:  # skeleton of the whole diagram from the first frame; boxes fill in on cue
        bd = ImageDraw.Draw(img)
        for bx in boxes:
            bd.rounded_rectangle(bx, radius=30, outline=BORDER, width=6)
    labels = [('Goal', 'you give it'), ('Muse', 'plans, works'), ('Check-in', 'asks first'),
              ('Tools', 'Blender, Godot'), ('Result', 'you inspect')]
    for i, (box, (a, b)) in enumerate(zip(boxes, labels)):
        L, d = layer(fr)
        if i == 1 and fr.p:
            d.rounded_rectangle(box, radius=30, fill=CARD, outline=ACC_D, width=14)
        elif i == 1:
            d.rounded_rectangle(box, radius=30, fill=CARD, outline=ACC_D, width=14)
            cw_ = (box[2] - box[0]) * 0.32
            cloud(d, (box[0] + (box[2] - box[0] - cw_) / 2, box[1] + 25, box[0] + (box[2] + box[0] + cw_) / 2 - box[0], box[1] + 25 + cw_ * 0.5), fill=CARD, outline=ACC_D)
        else:
            card(d, box, accent=(i == 2))
        cw = box[2] - box[0] - 60
        th = int(fT.size * 1.1) + int(fb.size * 1.2) * len(wrap(d, b, fb, cw))
        yy = box[1] + (box[3] - box[1] - th) // 2 + (int((box[2] - box[0]) * 0.1) if i == 1 and not fr.p else 0)
        yy = text(d, (box[0] + 30, yy), a, fT, INK, width=cw, align='center', lh=1.1)
        text(d, (box[0] + 30, yy), b, fb, SOFT, width=cw, align='center')
        if i > 0:
            pb = boxes[i - 1]
            if fr.p:
                arrow(d, ((box[0] + box[2]) // 2, pb[3] + 10), ((box[0] + box[2]) // 2, box[1] - 10))
            else:
                arrow(d, (pb[2] + 15, (pb[1] + pb[3]) // 2), (box[0] - 15, (box[1] + box[3]) // 2))
        els.append(L)
    return img, els


def sc_versus(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fb, fs, fT = fr.f(SANS_R, fr.body), fr.f(SANS, fr.body), fr.f(SERIF, fr.head)
    if fr.p:
        A = (fr.sx0, y0, fr.sx1, y0 + int((bot - y0) * 0.36))
        B = (fr.sx0, y0 + int((bot - y0) * 0.36) + 50, fr.sx1, bot)
    else:
        A = (fr.sx0, y0, fr.sx0 + fr.sw // 2 - 40, bot)
        B = (fr.sx0 + fr.sw // 2 + 40, y0, fr.sx1, bot)
    els = []

    def col(box, head, lines, accent):
        L, d = layer(fr)
        card(d, box, accent=accent)
        y = text(d, (box[0] + 60, box[1] + 50), head, fT, INK, width=box[2] - box[0] - 120)
        return L, d, y + 20
    L, d, y = col(A, 'Your computer', [], False)
    for lab in ('Memory', 'Disk'):
        d.text((A[0] + 60, y), lab, font=fs, fill=INK)
        y += int(fr.body * 1.25)
        d.rounded_rectangle([A[0] + 60, y, A[2] - 60, y + 40], radius=14, fill=ACC_D)
        y += 100
    text(d, (A[0] + 60, y), 'A local tool uses both.', fb, INK, width=A[2] - A[0] - 120)
    els.append(L)
    L, d, y = col(B, 'The cloud', [], True)
    y = text(d, (B[0] + 60, y), "Muse's own virtual machine", fs, ACC_D, width=B[2] - B[0] - 120) + 20
    els.append(L)
    L, d = layer(fr)
    yy = y
    for lab in ('Your memory', 'Your disk'):
        d.text((B[0] + 60, yy), lab + ': untouched', font=fb, fill=INK)
        yy += int(fr.body * 1.3)
    els.append(L)
    L, d = layer(fr)
    yy2 = yy + 20
    text(d, (B[0] + 60, yy2), 'Works around the clock', fs, INK, width=B[2] - B[0] - 120)
    els.append(L)
    L, d = layer(fr)
    yy3 = yy2 + int(fr.body * 1.3) + 10
    yy3 = text(d, (B[0] + 60, yy3), 'until its token allowance runs out', fb, ACC_D, width=B[2] - B[0] - 120)
    els.append(L)
    return img, els


def sc_muse_ui(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fb, fs, fm = fr.f(SANS_R, fr.body), fr.f(SANS, fr.body), fr.f(MONO, fr.mono)
    win = (fr.sx0, y0, fr.sx1, bot)
    G = (0x2F, 0x33, 0x3A)
    els = []
    L, d = layer(fr)
    d.rounded_rectangle(win, radius=30, fill=(0xEF, 0xF1, 0xF4), outline=(0x9A, 0xA1, 0xAB), width=6)
    d.rounded_rectangle([win[0], win[1], win[2], win[1] + int(fr.body * 1.6)], radius=30, fill=G)
    d.text((win[0] + 50, win[1] + int(fr.body * 0.25)), 'Muse (illustration)', font=fs, fill=(0xEE, 0xF0, 0xF3))
    if fr.p:
        yb = win[1] + int(fr.body * 1.6) + 40
        for part in ('ILLUSTRATION —', "not Muse's", 'actual screen'):
            yb = recon_badge(d, fr, win[0] + 50, yb, part) + 8
    else:
        yb = recon_badge(d, fr, win[0] + 50, win[1] + int(fr.body * 1.6) + 40, "ILLUSTRATION — not Muse's actual screen")
    els.append(L)
    inner_x = win[0] + 60
    width = win[2] - win[0] - 120
    L, d = layer(fr)
    y = yb + 50
    d.text((inner_x, y), 'Goal', font=fs, fill=G)
    y += int(fr.body * 1.25)
    gtxt = 'Make a simple 3D crate and try it in a game prototype' if not fr.p else 'Make a 3D crate; try it in Godot'
    gh = text_h(d, gtxt, fb, width - 60) + 50
    d.rounded_rectangle([inner_x, y, inner_x + width, y + gh], radius=20, fill=(0xFF, 0xFF, 0xFF), outline=(0x9A, 0xA1, 0xAB), width=4)
    text(d, (inner_x + 30, y + 22), gtxt, fb, INK, width=width - 60)
    y += gh + 40
    els.append(L)
    L, d = layer(fr)
    d.text((inner_x, y), 'Plan (example)', font=fs, fill=G)
    y += int(fr.body * 1.25)
    plan = ['Set up tools', 'Build the 3D model', 'Export the asset', 'Try it in Godot']
    if fr.p:
        plan = plan[:2]
    for i, s in enumerate(plan):
        d.text((inner_x + 20, y), f'{i + 1}.  {s}', font=fb, fill=INK)
        y += int(fr.body * 1.25)
    y += 30
    els.append(L)
    L, d = layer(fr)
    ch = int(fr.body * 1.2) * (3 if fr.p else 2) + 60
    box = [inner_x, min(y, bot - ch - 40), inner_x + width, min(y, bot - ch - 40) + ch]
    d.rounded_rectangle(box, radius=20, fill=ACC_BG, outline=ACC_D, width=6)
    yy = text(d, (box[0] + 30, box[1] + 25), 'Check-in: next step changes files. Continue?', fs, INK, width=width - 60)
    els.append(L)
    return img, els


def sc_blender(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fs, fm = fr.f(SANS, fr.small), fr.f(MONO, fr.mono)
    els = []
    L, d = layer(fr)
    yb = recon_badge(d, fr, fr.sx0, y0, 'ILLUSTRATION — simplified editor view' if not fr.p else 'ILLUSTRATION')
    ui_top = yb + 30
    term_h = int(fr.mono * 1.3) * (5 if fr.p else 2) + 80
    ui = (fr.sx0, ui_top, fr.sx1, bot - term_h - 40)
    BG, BAR, VP, TXT = (0x30, 0x30, 0x30), (0x23, 0x23, 0x23), (0x3D, 0x3D, 0x3D), (0xE6, 0xE6, 0xE6)
    d.rectangle(ui, fill=BG)
    bar_h = int(fr.small * 1.5)
    d.rectangle([ui[0], ui[1], ui[2], ui[1] + bar_h], fill=BAR)
    menus = ['File', 'Edit', 'Render'] if fr.p else ['File', 'Edit', 'Render', 'Window', 'Help', '   Layout', 'Modeling']
    x = ui[0] + 40
    for m in menus:
        d.text((x, ui[1] + int(fr.small * 0.2)), m, font=fs, fill=TXT)
        x += d.textlength(m, font=fs) + 60
    side = 0 if fr.p else 760
    vp = (ui[0] + 20, ui[1] + bar_h + 20, ui[2] - side - 30, ui[3] - 20)
    d.rectangle(vp, fill=VP)
    cx, cy = (vp[0] + vp[2]) // 2, (vp[1] + vp[3]) // 2 + 40
    g = Image.new('RGBA', (vp[2] - vp[0], vp[3] - vp[1]), VP + (255,))
    gd = ImageDraw.Draw(g)
    gcx, gcy = cx - vp[0], cy - vp[1]
    for k in range(-8, 9):  # floor grid, clipped to the viewport
        gd.line([(gcx + k * 120 - 600, gcy + 240), (gcx + k * 60, gcy - 60)], fill=(0x4A, 0x4A, 0x4A), width=3)
    gd.line([(0, gcy + 120), (g.width, gcy + 120)], fill=(0xB0, 0x3A, 0x3A), width=6)
    gd.line([(gcx - 300, g.height), (gcx + 150, 40)], fill=(0x6A, 0x9A, 0x3A), width=6)
    L.paste(g, (vp[0], vp[1]))
    s = min(vp[2] - vp[0], vp[3] - vp[1]) * 0.22
    top = [(cx, cy - s * 1.1), (cx + s, cy - s * 0.55), (cx, cy), (cx - s, cy - s * 0.55)]
    d.polygon(top, fill=(0xC8, 0xC8, 0xC8), outline=(0x10, 0x10, 0x10))
    d.polygon([(cx - s, cy - s * 0.55), (cx, cy), (cx, cy + s), (cx - s, cy + s * 0.45)], fill=(0x9A, 0x9A, 0x9A), outline=(0x10, 0x10, 0x10))
    d.polygon([(cx, cy), (cx + s, cy - s * 0.55), (cx + s, cy + s * 0.45), (cx, cy + s)], fill=(0x7A, 0x7A, 0x7A), outline=(0x10, 0x10, 0x10))
    if not fr.p:
        ol = (ui[2] - side - 10, ui[1] + bar_h + 20, ui[2] - 20, ui[3] - 20)
        d.rectangle(ol, fill=(0x28, 0x28, 0x28))
        y = ol[1] + 30
        for item in ('Scene', '  Camera', '  Cube', '  Light'):
            d.text((ol[0] + 30, y), item, font=fs, fill=TXT)
            y += int(fr.small * 1.4)
    els.append(L)
    L, d = layer(fr)  # headless: a terminal under the reconstruction
    tb = (fr.sx0, bot - term_h, fr.sx1, bot)
    d.rounded_rectangle(tb, radius=24, fill=(0x1E, 0x22, 0x2B))
    cmd = ['$ blender', '  --background', '  --python build.py'] if fr.p else ['$ blender --background --python build.py']
    y = tb[1] + 30
    for c in cmd:
        d.text((tb[0] + 40, y), c, font=fm, fill=(0xED, 0xF1, 0xF7))
        y += int(fr.mono * 1.3)
    d.text((tb[0] + 40, y), 'headless: no window' + ('' if fr.p else ' · example command, illustrative'), font=fs, fill=(0x9F, 0xA9, 0xB8))
    if fr.p:
        d.text((tb[0] + 40, y + int(fr.small * 1.3)), 'example, illustrative', font=fs, fill=(0x9F, 0xA9, 0xB8))
    els.append(L)
    L, d = layer(fr)
    d.rounded_rectangle([cx - s * 1.25, cy - s * 1.35, cx + s * 1.25, cy + s * 1.25], radius=20, outline=ACC, width=10)
    els.append(L)
    return img, els, [0, 1, 3]


def sc_godot(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fs = fr.f(SANS, fr.small)
    els = []
    L, d = layer(fr)
    yb = recon_badge(d, fr, fr.sx0, y0, 'ILLUSTRATION — simplified editor view' if not fr.p else 'ILLUSTRATION')
    tags_h = int(fr.body * 1.6) + 40
    ui = (fr.sx0, yb + 30, fr.sx1, bot - tags_h - 30)
    BG, BAR, VP, TXT, BLUE = (0x20, 0x25, 0x31), (0x34, 0x3D, 0x4D), (0x2B, 0x32, 0x40), (0xED, 0xF1, 0xF7), (0x8B, 0xC7, 0xF3)
    d.rectangle(ui, fill=BG)
    bar_h = int(fr.small * 1.5)
    d.rectangle([ui[0], ui[1], ui[2], ui[1] + bar_h], fill=BAR)
    menus = ['Scene', '2D', 'Script'] if fr.p else ['Scene', 'Project', 'Debug', 'Editor', '      2D', '3D', 'Script']
    x = ui[0] + 40
    for m in menus:
        d.text((x, ui[1] + int(fr.small * 0.2)), m, font=fs, fill=TXT)
        x += d.textlength(m, font=fs) + 60
    dock = 0 if fr.p else 820
    if not fr.p:
        dk = (ui[0] + 20, ui[1] + bar_h + 20, ui[0] + dock, ui[3] - 20)
        d.rectangle(dk, fill=VP)
        y = dk[1] + 30
        for item in ('Node2D', '  Player', '  Platform', '  Camera2D'):
            d.text((dk[0] + 30, y), item, font=fs, fill=TXT)
            y += int(fr.small * 1.4)
    vp = (ui[0] + dock + 40, ui[1] + bar_h + 20, ui[2] - 20, ui[3] - 20)
    d.rectangle(vp, fill=(0x3A, 0x41, 0x50))
    for gx in range(vp[0], vp[2], 120):
        d.line([(gx, vp[1]), (gx, vp[3])], fill=(0x44, 0x4C, 0x5C), width=2)
    for gy in range(vp[1], vp[3], 120):
        d.line([(vp[0], gy), (vp[2], gy)], fill=(0x44, 0x4C, 0x5C), width=2)
    w, h = vp[2] - vp[0], vp[3] - vp[1]
    d.rectangle([vp[0] + w * 0.1, vp[1] + h * 0.72, vp[0] + w * 0.9, vp[1] + h * 0.8], fill=(0x8F, 0xA8, 0x6A))
    d.rectangle([vp[0] + w * 0.55, vp[1] + h * 0.45, vp[0] + w * 0.8, vp[1] + h * 0.5], fill=(0x8F, 0xA8, 0x6A))
    d.rectangle([vp[0] + w * 0.25, vp[1] + h * 0.6, vp[0] + w * 0.25 + h * 0.12, vp[1] + h * 0.72], fill=ACC)
    els.append(L)
    L, d = layer(fr)
    d.rectangle([vp[0] + w * 0.22, vp[1] + h * 0.55, vp[0] + w * 0.25 + h * 0.15, vp[1] + h * 0.75], outline=BLUE, width=10)
    els.append(L)
    L, d = layer(fr)
    fb = fr.f(SANS, fr.body)
    x, y = fr.sx0, bot - tags_h + 20
    for tag in (('Unity, Unreal: possible',) if fr.p else ('Unity: possible', 'Unreal: possible')):
        tw = d.textlength(tag, font=fb)
        d.rounded_rectangle([x, y, x + tw + 80, y + int(fr.body * 1.5)], radius=30, fill=(0xEC, 0xEA, 0xE3), outline=BORDER, width=5)
        d.text((x + 40, y + int(fr.body * 0.2)), tag, font=fb, fill=SOFT)
        x += tw + 140
    els.append(L)
    return img, els


def sc_compare(fr, spec, title):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fb, fs, fT = fr.f(SANS_R, fr.body), fr.f(SANS, fr.body), fr.f(SERIF, fr.head)
    rows = [('Runs on', 'your machine', 'the cloud'), ('Your memory, disk', 'used', 'untouched'),
            ('AI model', 'Sonnet, Opus', 'not Sonnet or Opus')]
    els = []
    foot_h = int(fr.body * 1.4) + 60
    if fr.p:
        H = (bot - y0 - foot_h - 60) // 2
        cols = [(fr.sx0, y0, fr.sx1, y0 + H - 30), (fr.sx0, y0 + H + 30, fr.sx1, y0 + 2 * H)]
    else:
        cols = [(fr.sx0, y0, fr.sx0 + fr.sw // 2 - 40, bot - foot_h - 40), (fr.sx0 + fr.sw // 2 + 40, y0, fr.sx1, bot - foot_h - 40)]
    for ci, (head, box) in enumerate(zip(('Claude Code', 'Muse'), cols)):
        L, d = layer(fr)
        card(d, box, accent=(ci == 1))
        y = text(d, (box[0] + 60, box[1] + 40), head, fT, INK) + 10
        for lab, a, b in rows:
            if fr.p:
                y = text(d, (box[0] + 60, y), f'{lab}: ' + (a if ci == 0 else b), fb, INK, width=box[2] - box[0] - 120, lh=1.15) + 10
                continue
            d.text((box[0] + 60, y), lab, font=fs, fill=SOFT)
            y += int(fr.body * 1.2)
            y = text(d, (box[0] + 60, y), (a if ci == 0 else b), fb, INK, width=box[2] - box[0] - 120) + 15
        els.append(L)
    L, d = layer(fr)
    fy = bot - foot_h
    d.rounded_rectangle([fr.sx0, fy, fr.sx1, bot], radius=26, fill=DARK)
    d.text((fr.sx0 + 60, fy + 30), 'Best for simpler tasks', font=fs, fill=(0xFF, 0xFD, 0xF8))
    els.append(L)
    return img, els, [0, 1, 3]


def tiles(fr, title, items, glyph=None):
    img, y0 = base(fr, title)
    bot = fr.sy1 - (150 if not fr.p else 0)
    fs, fb = fr.f(SANS, fr.body), fr.f(SANS_R, fr.body)
    n = len(items)
    els = []
    if fr.p:
        H = (bot - y0 - 30 * (n - 1)) // n
        boxes = [(fr.sx0, y0 + i * (H + 30), fr.sx1, y0 + i * (H + 30) + H) for i in range(n)]
    else:
        cols = 2 if n == 4 else n
        rows_ = math.ceil(n / cols)
        Wc = (fr.sw - 60 * (cols - 1)) // cols
        Hc = (bot - y0 - 60 * (rows_ - 1)) // rows_
        boxes = [(fr.sx0 + (i % cols) * (Wc + 60), y0 + (i // cols) * (Hc + 60),
                  fr.sx0 + (i % cols) * (Wc + 60) + Wc, y0 + (i // cols) * (Hc + 60) + Hc) for i in range(n)]
    for (head, sub), box in zip(items, boxes):
        L, d = layer(fr)
        card(d, box, accent=True)
        x0 = box[0] + 70
        if glyph:
            g = int(fr.body * 1.1)
            gy = box[1] + 50
            d.polygon([(x0 + g / 2, gy), (x0 + g, gy + g), (x0, gy + g)], fill=ACC)
            d.text((x0 + g / 2 - fr.body * 0.12, gy + g * 0.25), '!', font=fr.f(SANS, fr.body * 0.75), fill=(0xFF, 0xFF, 0xFF))
            x0 += g + 40
        w = box[2] - x0 - 60
        th = text_h(d, head, fs, w) + text_h(d, sub, fb, w)
        y = box[1] + max(50, (box[3] - box[1] - th) // 2)
        y = text(d, (x0, y), head, fs, ACC_D, width=w)
        text(d, (x0, y), sub, fb, INK, width=w)
        els.append(L)
    return img, els


def sc_uses(fr, spec, title):
    return tiles(fr, title, [('Offload heavy jobs', 'to the cloud'), ('Run long tasks', 'overnight'),
                             ('First drafts', 'prototypes, assets; refine by hand'),
                             ('Pair with tools', 'e.g. Brutalist for videos')])


def sc_cautions(fr, spec, title):
    return tiles(fr, title, [('Verify', 'a person checks every AI output'), ('Limit access', 'only what the job needs'),
                             ('Disclose', 'say what the AI did; explain every part')], glyph=True)


SCENES = {'terms': sc_terms, 'problem': sc_problem, 'flow': sc_flow, 'versus': sc_versus, 'muse_ui': sc_muse_ui,
          'blender': sc_blender, 'godot': sc_godot, 'compare': sc_compare, 'uses': sc_uses, 'cautions': sc_cautions}
TITLES = {'B02': 'Six terms (1 of 2)', 'B03': 'Six terms (2 of 2)', 'B04': 'The problem', 'B05': 'What Muse is',
          'B06': 'Your computer vs the cloud', 'B07': 'Muse, in outline', 'B08': 'Muse and Blender',
          'B09': 'Muse and Godot', 'B10': 'Muse vs Claude Code', 'B11': 'How you could use it',
          'B12': 'Cautions', 'B14': 'Recap', 'B16': ''}


def render(reel, portrait):
    sheet = json.loads((reel / 'beat_sheet.json').read_text())
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import script as S
    specs = {s['id']: s for s in S.BEATS}
    W, H = (2160, 3840) if portrait else (3840, 2160)
    fr = Frame(W, H)
    for b in sheet['beats']:
        k = b['shot'].get('scene')
        if not k:
            continue
        spec = specs[b['beat_id']]
        res = SCENES[k](fr, spec, TITLES[b['beat_id']])
        bimg, els = res[0], res[1]
        cues = b['shot'].get('cue_times', [])
        times = [cues[i] if i < len(cues) else (cues[-1] if cues else 0.3) for i in range(len(els))]
        if len(res) > 2:  # explicit element->cue map
            times = [cues[j] if j < len(cues) else cues[-1] for j in res[2]][:len(els)] + times[len(res[2]):]
        times = [max(0.2, t - 0.15) for t in times]
        n = math.ceil(b['actual_duration_s'] * FPS - 1e-8)
        out = reel / f"media/{b['beat_id']}.mp4"
        out.parent.mkdir(exist_ok=True)
        enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                                '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '14',
                                '-pix_fmt', 'yuv420p', '-r', str(FPS), '-movflags', '+faststart', str(out)],
                               stdin=subprocess.PIPE)
        cache_key, cache_raw = None, None
        for f in range(n):
            t = f / FPS
            alphas = tuple(min(1.0, max(0.0, (t - st) * FPS / FADE)) for st in times)
            if alphas != cache_key:
                im = bimg.copy()
                for L, a in zip(els, alphas):
                    if a <= 0:
                        continue
                    if a >= 1:
                        im.alpha_composite(L)
                    else:
                        LL = L.copy()
                        LL.putalpha(LL.getchannel('A').point(lambda v, a=a: int(v * a)))
                        im.alpha_composite(LL)
                cache_key, cache_raw = alphas, im.convert('RGB').tobytes()
            enc.stdin.write(cache_raw)
        enc.stdin.close()
        if enc.wait() != 0:
            raise RuntimeError(out)
        print(b['beat_id'], k, n, 'frames', 'portrait' if portrait else 'landscape')



def sc_recap(fr, spec, title):
    import script as S
    return tiles(fr, title, [(f'{i + 1}.', line) for i, line in enumerate(S.RECAP)])


def sc_outro(fr, spec, title):
    import script as S
    img = Image.new('RGBA', (fr.w, fr.h), PAGE + (255,))
    d = ImageDraw.Draw(img)
    ft = fr.f(SERIF, fr.title * (1.25 if fr.p else 1.3))
    w = fr.sw - (100 if fr.p else 900)
    x0 = fr.sx0 + (fr.sw - w) // 2
    th = text_h(d, S.TITLE + '.', ft, w, lh=1.1)
    y = fr.sy0 + (fr.sh - th - int(fr.body * 4)) // 2
    y = text(d, (x0, y), S.TITLE + '.', ft, INK, width=w, lh=1.1, align='center') + 60
    L, d2 = layer(fr)
    fb = fr.f(SANS, fr.body)
    d2.line([(x0 + w * 0.3, y), (x0 + w * 0.7, y)], fill=ACC, width=8)
    y = text(d2, (x0, y + 50), S.PRESENTER, fr.f(SERIF, fr.title), ACC_D, width=w, align='center')
    text(d2, (x0, y + 10), S.HANDLE, fb, INK, width=w, align='center')
    return img, [L]


SCENES['recap'] = sc_recap
SCENES['outro'] = sc_outro


if __name__ == '__main__':
    render(Path(sys.argv[2]).resolve(), sys.argv[1] == 'portrait')
