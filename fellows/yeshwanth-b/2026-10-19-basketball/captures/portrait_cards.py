"""Native 9:16 portrait cards for the Basketball Blaster verticals.

The shared portrait Remotion boards put fine print (23-30 design px) far below
GATE T's portrait floor (text-run height >= 1.9% of 3840 = 72 px). These cards
are drawn directly at 2160x3840 with every glyph's x-height >= ~80 px, so each
beat shows its key verbatim line(s) in large type. Narration, timing and the
landscape films are unchanged. Every quoted string is checked against its source
file (`assert_verbatim`) before a frame is drawn.

Layout stays inside the 9:16 title-safe box used by GATE T:
x 108-2052, y 192-3302 (bottom inset 14% for platform UI).
"""
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 2160, 3840, 30
SX0, SX1, SY0, SY1 = 108, 2052, 192, 3302
FONTS = Path('/Users/yeshwanthbalaji/Documents/Brutalist_Updated/runtime/fonts')
SERIF = FONTS / 'EB_Garamond/static/EBGaramond-Medium.ttf'
SANS = FONTS / 'Inter/static/Inter_28pt-Medium.ttf'
SANS_R = FONTS / 'Inter/static/Inter_28pt-Regular.ttf'
MONO = FONTS / 'PT_Mono/PTMono-Regular.ttf'
PAGE, INK, SOFT = (0xFA, 0xF9, 0xF5), (0x3D, 0x39, 0x29), (0x56, 0x47, 0x39)
ACC, ACC_BG, CARD, BORDER = (0x98, 0x50, 0x39), (0xF2, 0xE5, 0xD8), (0xFF, 0xFD, 0xF8), (0xCF, 0xC6, 0xB5)
DARK, DARK2, DTXT, DMUT, DMARK = (0x20, 0x25, 0x31), (0x2B, 0x32, 0x40), (0xED, 0xF1, 0xF7), (0xBE, 0xC8, 0xD7), (0x45, 0x5A, 0x71)
STATUS_BG = (0x30, 0x3D, 0x34)

F_TITLE, F_BODY, F_MONO, F_HANDLE = 178, 148, 154, 148


def font(path, size):
    return ImageFont.truetype(str(path), size)


def assert_verbatim(text, source_path):
    src = ' '.join(Path(source_path).read_text().replace('\t', ' ').split())
    want = ' '.join(text.split())
    if want not in src:
        raise ValueError(f'not verbatim in {source_path}: {text!r}')


def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if d.textlength(trial, font=f) <= width:
            cur = trial
            continue
        if cur:
            lines.append(cur)
        while d.textlength(w, font=f) > width:          # hard-break long tokens (code)
            k = len(w)
            while k > 1 and d.textlength(w[:k], font=f) > width:
                k -= 1
            lines.append(w[:k])
            w = w[k:]
        cur = w
    if cur:
        lines.append(cur)
    return lines


def wrap_code(d, line, f, width):
    out, cur = [], ''
    for ch in line:
        if d.textlength(cur + ch, font=f) > width:
            out.append(cur)
            cur = '  ' + ch.lstrip() if ch != ' ' else '  '
        else:
            cur += ch
    out.append(cur)
    return out


class Canvas:
    def __init__(self, bg=PAGE):
        self.img = Image.new('RGB', (W, H), bg)
        self.d = ImageDraw.Draw(self.img)
        self.y = SY0

    def need(self, h):
        if self.y + h > SY1:
            raise ValueError(f'layout overflow: y {self.y} + {h} > {SY1}')

    def text_block(self, text, f, colour, x0=SX0, x1=SX1, lh=1.18, align='left'):
        lines = wrap(self.d, text, f, x1 - x0)
        step = int(f.size * lh)
        self.need(step * len(lines))
        for ln in lines:
            x = x0 if align == 'left' else x0 + (x1 - x0 - self.d.textlength(ln, font=f)) / 2
            self.d.text((x, self.y), ln, font=f, fill=colour)
            self.y += step
        return len(lines)


def board_frames(spec, highlight):
    """spec: title, status, quote, source_label, cards[(label, text)], image(png path)."""
    c = Canvas()
    c.text_block(spec['title'], font(SERIF, F_TITLE), INK, lh=1.08)
    c.y += 90
    fs = font(SANS, F_BODY)
    lines = wrap(c.d, spec['status'], fs, SX1 - SX0 - 100)
    h = int(F_BODY * 1.2) * len(lines) + 70
    c.need(h)
    c.d.rounded_rectangle([SX0, c.y, SX1, c.y + h], radius=30, fill=STATUS_BG)
    yy = c.y + 35
    for ln in lines:
        c.d.text((SX0 + 50, yy), ln, font=fs, fill=(0xFF, 0xFD, 0xF8))
        yy += int(F_BODY * 1.2)
    c.y += h + 50
    if spec.get('quote'):
        fq = font(SANS_R, F_BODY)
        qlines = wrap(c.d, '“' + spec['quote'] + '”', fq, SX1 - SX0 - 70)
        step = int(F_BODY * 1.2)
        c.need(step * len(qlines) + int(F_BODY * 1.3))
        top = c.y
        for ln in qlines:
            c.d.text((SX0 + 70, c.y), ln, font=fq, fill=INK)
            c.y += step
        c.d.rectangle([SX0, top + 10, SX0 + 18, c.y - 20], fill=ACC)
        c.d.text((SX0 + 70, c.y + 5), spec['source_label'], font=font(SANS, F_BODY), fill=SOFT)
        c.y += int(F_BODY * 1.3) + 40
    fl, ft = font(SANS, F_BODY), font(SANS_R, F_BODY)
    step_c = int(F_BODY * 1.18)
    cards_h = sum(step_c * (len(wrap(c.d, l, fl, SX1 - SX0 - 110)) + len(wrap(c.d, t, ft, SX1 - SX0 - 110))) + 116
                  for l, t in spec.get('cards', []))
    if spec.get('image'):
        im = Image.open(spec['image']).convert('RGB')
        iw = spec.get('image_width', SX1 - SX0)
        ih = round(im.height * iw / im.width)
        room = SY1 - c.y - cards_h - 50
        if ih > room:
            ih = room
            iw = round(im.width * ih / im.height)
        if iw < 1000:
            raise ValueError(f'image would shrink to {iw}px wide; shorten the quote or cards')
        c.need(ih)
        c.img.paste(im.resize((iw, ih), Image.LANCZOS), (SX0 + (SX1 - SX0 - iw) // 2, c.y))
        c.y += ih + 50
    fl, ft = font(SANS, F_BODY), font(SANS_R, F_BODY)
    if spec.get('cards'):
        c.y = max(c.y, SY1 - 10 - cards_h + 36)
    for i, (label, text) in enumerate(spec.get('cards', [])):
        on = i == highlight
        tl = wrap(c.d, label, fl, SX1 - SX0 - 110)
        tt = wrap(c.d, text, ft, SX1 - SX0 - 110)
        step = int(F_BODY * 1.18)
        h = step * (len(tl) + len(tt)) + 80
        c.need(h)
        c.d.rounded_rectangle([SX0, c.y, SX1, c.y + h], radius=26, fill=ACC_BG if on else CARD,
                              outline=ACC if on else BORDER, width=6)
        c.d.rectangle([SX0, c.y, SX0 + 18, c.y + h], fill=ACC if on else BORDER)
        yy = c.y + 38
        for ln in tl:
            c.d.text((SX0 + 60, yy), ln, font=fl, fill=(0x66, 0x37, 0x25))
            yy += step
        for ln in tt:
            c.d.text((SX0 + 60, yy), ln, font=ft, fill=INK)
            yy += step
        c.y += h + 36
    return c.img


def code_frames(spec, highlight):
    """spec: title, path, lines[(lineno, text)], note, source_label. highlight = lineno or None."""
    c = Canvas()
    c.text_block(spec['title'], font(SERIF, F_TITLE), INK, lh=1.08)
    c.y += 90
    fm, fs = font(MONO, F_MONO), font(SANS, F_BODY)
    pad = 50
    rows = []
    for no, text in spec['lines']:
        if no is None:
            rows.append((None, '…'))
            continue
        for k, r in enumerate(wrap_code(c.d, text.strip() if spec.get('strip', True) else text, fm, SX1 - SX0 - 2 * pad - 30)):
            rows.append((no if k == 0 else -no, r))
    step = int(F_MONO * 1.22)
    head = int(F_BODY * 1.2) + 60
    h = head + step * len(rows) + 2 * pad
    c.need(h)
    top = c.y
    c.d.rounded_rectangle([SX0, top, SX1, top + h], radius=28, fill=DARK)
    c.d.rounded_rectangle([SX0, top, SX1, top + head], radius=28, fill=DARK2)
    c.d.rectangle([SX0, top + head - 30, SX1, top + head], fill=DARK2)
    c.d.text((SX0 + pad, top + 30), spec['path'], font=fs, fill=DTXT)
    yy = top + head + pad
    for no, r in rows:
        on = highlight is not None and no is not None and abs(no) == highlight
        if on:
            c.d.rectangle([SX0 + 14, yy - 8, SX1 - 14, yy + step - 18], fill=DMARK)
            c.d.rectangle([SX0 + 14, yy - 8, SX0 + 30, yy + step - 18], fill=(0x8B, 0xC7, 0xF3))
        c.d.text((SX0 + pad + 30, yy), r, font=fm, fill=DTXT if r != '…' else DMUT)
        yy += step
    c.y = top + h + 50
    c.text_block(spec['source_label'], fs, SOFT)
    c.y += 30
    if spec.get('note'):
        tl = wrap(c.d, spec['note'], font(SANS_R, F_BODY), SX1 - SX0 - 110)
        st = int(F_BODY * 1.18)
        hh = st * len(tl) + 80
        c.y = max(c.y, SY1 - 10 - hh)
        c.need(hh)
        c.d.rounded_rectangle([SX0, c.y, SX1, c.y + hh], radius=26, fill=CARD, outline=BORDER, width=6)
        yy = c.y + 38
        for ln in tl:
            c.d.text((SX0 + 60, yy), ln, font=font(SANS_R, F_BODY), fill=INK)
            yy += st
        c.y += hh
    return c.img


def write_states(states, nframes, out):
    """states: [(start_seconds, PIL.Image)] sorted; holds each until the next."""
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '14',
                            '-pix_fmt', 'yuv420p', '-r', str(FPS), '-movflags', '+faststart', str(out)],
                           stdin=subprocess.PIPE)
    starts = [round(s * FPS) for s, _ in states] + [nframes]
    starts[0] = 0
    for i, (_, img) in enumerate(states):
        raw = img.tobytes()
        for _ in range(max(0, min(nframes, starts[i + 1]) - starts[i])):
            enc.stdin.write(raw)
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f'encode failed: {out}')
