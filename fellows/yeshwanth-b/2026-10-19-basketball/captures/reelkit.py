"""Shared, deterministic helpers for the three Basketball Blaster films.

Nothing here changes the game. It cuts exact-frame gameplay clips from the
scripted-input takes, pads narration to a clip's exact length, extracts
engine-frame stills, and hashes evidence. Every clip is cut at the take's own
30 fps with no retiming: N source frames in, N frames out.

Overlay policy (disclosed on screen and in CAPTURE.md): the 3840x2160 engine
frame is scaled to 90 % (3456x1944) and placed inside the title-safe width at
the top. The strip below it is not game pixels: it carries a fixed
"scripted-input capture" label on the left and, on the right, each key press,
click or gamepad input from the input log for 1 s after it happens. On menus the
white arrow cursor was drawn by the capture harness; in the arenas the orange
crosshair is the game's own.
"""
import base64
import hashlib
import io
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FPS = 30
HERE = Path(__file__).resolve().parent
TAKES = HERE / 'takes'
TOOLKIT = Path('/Users/yeshwanthbalaji/Documents/Brutalist_Updated')
FONT_DIR = TOOLKIT / 'runtime/fonts'
INTER = FONT_DIR / 'Inter/static/Inter_28pt-Medium.ttf'
INTER_REG = FONT_DIR / 'Inter/static/Inter_28pt-Regular.ttf'
BUILD_COMMIT = '8f86cc8'   # short build_id: the project is not a git repository
BUILD_ID = '8f86cc812e234160bb7f95e65f7150d29662426a460f387d9a7ed77fd59248d5'
GX0, GY0, GW, GH = 192, 0, 3456, 1944   # scaled engine frame inside the 3840x2160 film frame
GAME_X0, GAME_W = 0, 3840            # takes are full-frame 16:9 engine renders
BAR = (0x1f, 0x23, 0x29)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def take_path(take):
    return TAKES / f'{take}.mp4'


def take_log(take):
    return [json.loads(l) for l in (TAKES / f'{take}-inputs.jsonl').read_text().splitlines()]


def take_frames(take):
    out = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                          '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0',
                          str(take_path(take))], capture_output=True, text=True, check=True)
    return int(out.stdout.strip())


def probe_duration(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'csv=p=0', str(path)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def _font(size, regular=False):
    return ImageFont.truetype(str(INTER_REG if regular else INTER), size)


def _input_events(take, start, end):
    """(frame, label) for key presses and clicks inside [start, end)."""
    events = []
    for row in take_log(take):
        if not start <= row['frame'] < end:
            continue
        ev, det = row['event'], row['detail']
        if ev in ('key', 'key_down'):
            events.append((row['frame'], ('KEY  ' if ev == 'key' else 'HOLD  ') + det['key'].split(' (')[0]))
        elif ev == 'click':
            events.append((row['frame'], 'RIGHT-CLICK' if det['button'] == 'right' else 'CLICK'))
        elif ev == 'mouse_down':
            events.append((row['frame'], 'HOLD  LEFT CLICK'))
        elif ev == 'joy_axis' and abs(det['value']) > 0.5:
            events.append((row['frame'], 'PAD  ' + det['axis']))
        elif ev == 'joy_button' and det['pressed']:
            events.append((row['frame'], 'PAD  ' + det['button']))
    return events


SAFE_L, SAFE_R, SAFE_T, SAFE_B = 192, 3648, 108, 2052   # 90% title-safe box at 3840x2160


def _centre(d, text, font, x0, x1, y, fill):
    d.text((x0 + (x1 - x0 - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def _bars(img, frame_no, events, label_lines):
    """Disclosure strip below the scaled game frame, inside title-safe."""
    d = ImageDraw.Draw(img)
    y = GH + 30
    d.text((SAFE_L, y), label_lines[0], font=_font(46), fill=(0xd9, 0xde, 0xe6))
    d.text((SAFE_L + d.textlength(label_lines[0], font=_font(46)) + 40, y + 2), '  ·  '.join(label_lines[1:]),
           font=_font(44, True), fill=(0xa9, 0xb2, 0xbf))
    live = [(f, t) for f, t in events if f <= frame_no < f + FPS]
    if live:
        f0, text = live[-1]
        a = int(255 * (1.0 - max(0.0, (frame_no - f0 - 20) / 10.0)))
        f = _font(46)
        w = d.textlength(text, font=f) + 80
        ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.rounded_rectangle([SAFE_R - w, GH + 18, SAFE_R, GH + 96], radius=18, fill=(0xd9, 0x77, 0x57, a))
        od.text((SAFE_R - w + 40, GH + 30), text, font=f, fill=(255, 255, 255, a))
        img.alpha_composite(ov)


def _compose(raw):
    """Full 3840x2160 engine frame -> film frame with the game at 90 % on the dark strip."""
    game = Image.frombytes('RGB', (GW, GH), raw)
    img = Image.new('RGBA', (3840, 2160), BAR + (255,))
    img.paste(game, (GX0, GY0))
    return img


def _decode(take, start, n):
    """Frames [start, start+n) scaled by ffmpeg (lanczos) to the 3456x1944 game area."""
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{start / FPS:.6f}', '-i', str(take_path(take)),
                            '-frames:v', str(n), '-vf', f'scale={GW}:{GH}:flags=lanczos',
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    size = GW * GH * 3
    for i in range(n):
        raw = dec.stdout.read(size)
        if len(raw) != size:
            raise RuntimeError(f'{take}: short read at frame {start + i}')
        yield start + i, raw
    dec.stdout.close()
    dec.wait()


def _tag(img, text, colour=(0x55, 0x5d, 0x69)):
    d = ImageDraw.Draw(img)
    text = text.replace('\n', ' ')
    f = _font(58)
    w = d.textlength(text, font=f) + 90
    x0 = GX0 + GW - w - 40
    d.rounded_rectangle([x0, GH - 150, x0 + w, GH - 40], radius=20, fill=colour)
    d.text((x0 + 45, GH - 134), text, font=f, fill=(255, 255, 255))


def cut_segments(take, segments, out, label_lines=None):
    """segments: ('play', start, n) real-time frames; ('replay', start, n, factor)
    the same source frames each repeated `factor` times, tagged REPLAY;
    ('hold', n) the last frame repeated, tagged HELD FRAME. Returns provenance."""
    total = take_frames(take)
    label_lines = label_lines or ['SCRIPTED INPUT', 'not a human playtest', f'build {BUILD_COMMIT}', 'Godot 4.7.2', 'game audio not captured']
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', '3840x2160', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p',
                            '-r', str(FPS), '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
    last, written, prov = None, 0, []
    for seg in segments:
        kind = seg[0]
        if kind in ('play', 'replay'):
            s0, n = seg[1], seg[2]
            if s0 < 0 or s0 + n > total:
                raise ValueError(f'{take}: frames {s0}+{n} exceed take length {total}')
            events = _input_events(take, s0, s0 + n)
            factor = seg[3] if kind == 'replay' else 1
            for fno, raw in _decode(take, s0, n):
                img = _compose(raw)
                _bars(img, fno, events if kind == 'play' else [], label_lines)
                if kind == 'replay':
                    _tag(img, f'REPLAY\n1/{factor} speed', (0xd9, 0x77, 0x57))
                last = img.convert('RGB').tobytes()
                for _ in range(factor):
                    enc.stdin.write(last)
                    written += 1
            prov.append({'kind': kind, 'source_start_frame': s0, 'source_frames': n,
                         'factor': factor, 'output_frames': n * factor})
        elif kind == 'hold':
            img = Image.frombytes('RGB', (3840, 2160), last).convert('RGBA')
            _tag(img, 'HELD\nFRAME')
            held = img.convert('RGB').tobytes()
            for _ in range(seg[1]):
                enc.stdin.write(held)
                written += 1
            prov.append({'kind': 'hold', 'output_frames': seg[1]})
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f'encode failed for {out}')
    return {'take': take, 'segments': prov, 'frames': written, 'duration_s': written / FPS}


def cut_clip(take, start, nframes, out, label_lines=None, hold_last=0):
    segs = [('play', start, nframes)] + ([('hold', hold_last)] if hold_last else [])
    return cut_segments(take, segs, out, label_lines)


def still(take, frame, out, width=None):
    """One engine frame (game area only, bars cropped) as PNG."""
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    vf = f'select=eq(n\\,{frame})'
    if width:
        vf += f',scale={width}:-1:flags=lanczos'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(take_path(take)), '-vf', vf,
                    '-frames:v', '1', str(out)], check=True)
    return out


def data_uri(png_path, width=1800):
    img = Image.open(png_path).convert('RGB')
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()


def pad_audio(src, out, lead_s, total_s):
    """Narration with lead silence, padded with silence to exactly total_s."""
    out = Path(out)
    ms = int(round(lead_s * 1000))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-af',
                    f'adelay={ms}|{ms},apad,atrim=0:{total_s:.6f}', '-ar', '48000', '-ac', '2',
                    '-c:a', 'pcm_s16le', str(out)], check=True)
    got = probe_duration(out)
    if abs(got - total_s) > 0.02:
        raise RuntimeError(f'{out}: padded to {got:.3f}s, wanted {total_s:.3f}s')
    return got


def frames_for(seconds):
    return math.ceil(seconds * FPS - 1e-9)


# ---- portrait (9:16) gameplay -------------------------------------------------
# The same exact source frames as the landscape clips: the 3049x2160 engine frame
# is cropped out of the padded take and scaled to the full 2160 width (2160x1530),
# centred on a 2160x3840 canvas. Disclosure above, input chips and tags below,
# all inside the 9:16 title-safe box (x 108-2052, y 192-3648).
PW, PH, PGH = 2160, 3840, 1215
PY0 = (PH - PGH) // 2


def _decode_portrait(take, start, n):
    vf = f'scale={PW}:{PGH}:flags=lanczos'
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{start / FPS:.6f}', '-i', str(take_path(take)),
                            '-frames:v', str(n), '-vf', vf,
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    size = PW * PGH * 3
    for i in range(n):
        raw = dec.stdout.read(size)
        if len(raw) != size:
            raise RuntimeError(f'{take}: short read at frame {start + i}')
        yield start + i, raw
    dec.stdout.close()
    dec.wait()


def _portrait_frame(game_raw, frame_no, events, label_lines, tag=None, tag_colour=(0x55, 0x5d, 0x69)):
    img = Image.new('RGBA', (PW, PH), BAR + (255,))
    img.paste(Image.frombytes('RGB', (PW, PGH), game_raw), (0, PY0))
    d = ImageDraw.Draw(img)
    y = 560
    for i, line in enumerate(label_lines):
        f = _font(64) if i == 0 else _font(46, True)
        _centre(d, line, f, 108, 2052, y, (0xd9, 0xde, 0xe6) if i == 0 else (0xa9, 0xb2, 0xbf))
        y += 92 if i == 0 else 64
    live = [(f, t) for f, t in events if f <= frame_no < f + FPS]
    if live:
        f0, text = live[-1]
        a = int(255 * (1.0 - max(0.0, (frame_no - f0 - 20) / 10.0)))
        ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.rounded_rectangle([680, 2860, 1480, 3040], radius=30, fill=(0xd9, 0x77, 0x57, a))
        _centre(od, text, _font(68), 680, 1480, 2905, (255, 255, 255, a))
        img.alpha_composite(ov)
        d = ImageDraw.Draw(img)
    _centre(d, 'input log', _font(40, True), 108, 2052, 3070, (0x8f, 0x99, 0xa6))
    if tag:
        lines = tag.split('\n')
        h = 40 + 80 * len(lines)
        d.rounded_rectangle([680, 3600 - h, 1480, 3600], radius=26, fill=tag_colour)
        yy = 3600 - h + 24
        for line in lines:
            _centre(d, line, _font(60), 680, 1480, yy, (255, 255, 255))
            yy += 80
    return img.convert('RGB').tobytes()


def cut_segments_portrait(take, segments, out, label_lines=None):
    """Portrait twin of cut_segments: identical source frames and segment list."""
    total = take_frames(take)
    label_lines = label_lines or ['SCRIPTED INPUT', 'not a human playtest', f'build {BUILD_COMMIT} · Godot 4.7.2', 'game audio not captured']
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', f'{PW}x{PH}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p',
                            '-r', str(FPS), '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
    last_game, last_no, written = None, 0, 0
    for seg in segments:
        kind = seg['kind'] if isinstance(seg, dict) else seg[0]
        if isinstance(seg, dict):
            s0, n, factor = seg.get('source_start_frame'), seg.get('source_frames'), seg.get('factor', 1)
            hold_n = seg['output_frames']
        else:
            s0, n = (seg[1], seg[2]) if kind != 'hold' else (None, None)
            factor = seg[3] if kind == 'replay' else 1
            hold_n = seg[1] if kind == 'hold' else None
        if kind in ('play', 'replay'):
            if s0 < 0 or s0 + n > total:
                raise ValueError(f'{take}: frames {s0}+{n} exceed {total}')
            events = _input_events(take, s0, s0 + n) if kind == 'play' else []
            for fno, raw in _decode_portrait(take, s0, n):
                fr = _portrait_frame(raw, fno, events, label_lines,
                                     *(('REPLAY\n1/%d speed' % factor, (0xd9, 0x77, 0x57)) if kind == 'replay' else (None,)))
                for _ in range(factor):
                    enc.stdin.write(fr)
                    written += 1
                last_game, last_no = raw, fno
        else:
            fr = _portrait_frame(last_game, last_no, [], label_lines, 'HELD\nFRAME')
            for _ in range(hold_n):
                enc.stdin.write(fr)
                written += 1
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f'encode failed for {out}')
    return written


def cut_zoom(take, start, n, crop, out, hold=0):
    """Real-time frames [start, start+n) of `take`, cropped to `crop` (x, y, w, h in the
    3840x2160 engine frame, 16:9) and scaled into the game area, tagged ZOOM. No retiming."""
    x, y, w, h = crop
    factor = round(GW / w, 1)
    total = take_frames(take)
    if start < 0 or start + n > total:
        raise ValueError(f'{take}: frames {start}+{n} exceed {total}')
    events = _input_events(take, start, start + n)
    vf = f'crop={w}:{h}:{x}:{y},scale={GW}:{GH}:flags=neighbor'
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{start / FPS:.6f}', '-i', str(take_path(take)),
                            '-frames:v', str(n), '-vf', vf,
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', '3840x2160', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p',
                            '-r', str(FPS), '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
    labels = ['SCRIPTED INPUT', 'not a human playtest', f'build {BUILD_COMMIT}', 'Godot 4.7.2', 'game audio not captured']
    last = None
    for i in range(n):
        raw = dec.stdout.read(GW * GH * 3)
        img = Image.new('RGBA', (3840, 2160), BAR + (255,))
        img.paste(Image.frombytes('RGB', (GW, GH), raw), (GX0, GY0))
        _bars(img, start + i, events, labels)
        _tag(img, f'ZOOM {factor}× · cropped engine frame', (0x55, 0x5d, 0x69))
        last = img.convert('RGB').tobytes()
        enc.stdin.write(last)
    dec.stdout.close()
    dec.wait()
    if hold:
        img = Image.frombytes('RGB', (3840, 2160), last).convert('RGBA')
        _tag(img, 'HELD FRAME · ZOOM', (0x55, 0x5d, 0x69))
        held = img.convert('RGB').tobytes()
        for _ in range(hold):
            enc.stdin.write(held)
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f'encode failed for {out}')
    segs = [{'kind': 'zoom', 'source_start_frame': start, 'source_frames': n, 'crop': list(crop),
             'factor': 1, 'output_frames': n}] + ([{'kind': 'hold', 'output_frames': hold}] if hold else [])
    return {'take': take, 'segments': segs, 'frames': n + hold, 'duration_s': (n + hold) / FPS}


def cut_zoom_portrait(take, start, n, crop, out, hold=0):
    """Portrait twin of cut_zoom: same frames and crop, game area 2160x1215."""
    x, y, w, h = crop
    vf = f'crop={w}:{h}:{x}:{y},scale={PW}:{PGH}:flags=neighbor'
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{start / FPS:.6f}', '-i', str(take_path(take)),
                            '-frames:v', str(n), '-vf', vf,
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                            '-s', f'{PW}x{PH}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p',
                            '-r', str(FPS), '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
    labels = ['SCRIPTED INPUT', 'not a human playtest', f'build {BUILD_COMMIT} · Godot 4.7.2', 'game audio not captured']
    events = _input_events(take, start, start + n)
    tag = f'ZOOM {round(GW / w, 1)}×'
    fr, written, raw = None, 0, None
    for i in range(n):
        raw = dec.stdout.read(PW * PGH * 3)
        fr = _portrait_frame(raw, start + i, events, labels, tag)
        enc.stdin.write(fr)
        written += 1
    dec.stdout.close()
    dec.wait()
    if hold:
        held = _portrait_frame(raw, start + n - 1, [], labels, 'HELD FRAME\n' + tag)
        for _ in range(hold):
            enc.stdin.write(held)
            written += 1
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f'encode failed for {out}')
    return written
