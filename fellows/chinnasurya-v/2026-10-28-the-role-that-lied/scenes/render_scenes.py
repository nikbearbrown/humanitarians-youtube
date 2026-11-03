#!/usr/bin/env python3
"""Per-script renderer — The Role That Lied (reading an LTI role).

Single stacked column throughout, so one layout serves 16:9 and 9:16 with no
portrait variant. Core reused verbatim from medhavy-canvas-sync.
"""
import argparse, json, os, shutil, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FPS = 24
GROUND, PAPER = (0x0A, 0x0A, 0x0A), (0xF2, 0xF0, 0xEB)
SIGNAL, MUTE  = (0xE8, 0x45, 0x2C), (0x6B, 0x6B, 0x6B)


def find_font(cands):
    for path, idx in cands:
        if Path(path).exists():
            return path, idx
    raise SystemExit(f"no font found among {[c[0] for c in cands]}")

DISPLAY = find_font([("/System/Library/Fonts/HelveticaNeue.ttc", 1),
                     ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0)])
MONO    = find_font([("/System/Library/Fonts/Menlo.ttc", 0),
                     ("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 0)])
MONOB   = find_font([("/System/Library/Fonts/Menlo.ttc", 1),
                     ("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 0),
                     ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 0)])


def F(spec, size):
    return ImageFont.truetype(spec[0], int(size), index=spec[1])


def fit(spec, size, text, maxw, tracking=0.0):
    """Shrink until it fits maxw. Overflow is a gate-V blocker, so never risk it."""
    s = int(size)
    while s > 14:
        f = F(spec, s)
        w = sum(f.getlength(c) + tracking * s for c in text)
        if w <= maxw:
            return f
        s = int(s * 0.94)
    return F(spec, 14)


def blend(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

GRIDC = blend(GROUND, MUTE, 0.12)


class Layout:
    """12 columns. Margins sit OUTSIDE the gate-V title-safe inset."""
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.portrait = h > w
        ref = 1080.0 if self.portrait else 1920.0
        self.mx = int((54 if self.portrait else 96) * (w / ref)) + 60
        self.my = int((96 if self.portrait else 54) * (w / ref)) + 60
        self.gutter = 72 if self.portrait else 120
        self.cols = 12
        inner = w - 2 * self.mx
        self.col = (inner - self.gutter * (self.cols - 1)) / self.cols
        s = 1.18 if self.portrait else 1.0
        self.display = int(280 * s * (0.70 if self.portrait else 1))
        self.h1      = int(200 * s)
        self.h2      = int(140 * s)
        self.body    = int(108 * s)
        self.data    = int(88 * s)
        self.caption = int(62 * s)

    def x(self, c):    return self.mx + c * (self.col + self.gutter)
    def span(self, n): return n * self.col + (n - 1) * self.gutter
    @property
    def right(self):  return self.w - self.mx
    @property
    def bottom(self): return self.h - self.my


def frame(L, grid=True):
    img = Image.new("RGB", (L.w, L.h), GROUND)
    d = ImageDraw.Draw(img)
    if grid:
        for c in range(L.cols + 1):
            x = int(L.mx + c * (L.col + L.gutter) - (L.gutter / 2 if c else 0))
            if L.mx <= x <= L.right:
                d.rectangle([x, L.my, x + 2, L.bottom], fill=GRIDC)
    return img, d


def track(d, xy, text, font, fill, tracking=-0.02):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking * font.size
    return x


def box(d, x0, y0, x1, y1, color, wd=6):
    d.rectangle([x0, y0, x1, y0 + wd], fill=color)
    d.rectangle([x0, y1 - wd, x1, y1], fill=color)
    d.rectangle([x0, y0, x0 + wd, y1], fill=color)
    d.rectangle([x1 - wd, y0, x1, y1], fill=color)


def arrow(d, x0, x1, y, color, wd=8, head=34):
    right = x1 > x0
    sx, ex = (x0, x1 - head) if right else (x0, x1 + head)
    d.rectangle([min(sx, ex), y - wd // 2, max(sx, ex), y + wd // 2], fill=color)
    if right:
        d.polygon([(x1, y), (x1 - head, y - head * 0.62), (x1 - head, y + head * 0.62)], fill=color)
    else:
        d.polygon([(x1, y), (x1 + head, y - head * 0.62), (x1 + head, y + head * 0.62)], fill=color)


def rule(d, L, y, color=MUTE, wd=8, x0=None, x1=None):
    d.rectangle([x0 or L.mx, y, x1 or L.right, y + wd], fill=color)


def marker(d, x, y, size, color):
    d.rectangle([x, y, x + size, y + size], fill=color)


def footer(d, L, text):
    rule(d, L, L.bottom - 92, MUTE, 6)
    d.text((L.mx, L.bottom - 70), text,
           font=fit(MONO, L.caption, text, L.right - L.mx), fill=MUTE)


def head(d, L, kicker, y=None):
    y = L.my if y is None else y
    rule(d, L, y, SIGNAL, 12)
    d.text((L.mx, y + 34), kicker, font=F(MONOB, L.caption), fill=MUTE)
    return y + 34 + L.caption + 46


def stations(d, L, y, lit, labels):
    """Four handshake stations; the active one in signal, the rest mute."""
    n = len(labels)
    gap = 46
    wpx = (L.right - L.mx - gap * (n - 1)) / n
    for i, lab in enumerate(labels):
        x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
        on = (i == lit)
        col = SIGNAL if on else MUTE
        if on:
            d.rectangle([x0, y, x1, y + 170], fill=SIGNAL)
        else:
            box(d, x0, y, x1, y + 170, MUTE, 5)
        f = fit(MONOB, L.data, lab, wpx - 56)
        d.text((x0 + 32, y + 170 // 2 - f.size * 0.72),
               lab, font=f, fill=GROUND if on else col)
    return y + 170 + 60




# ─────────────────────────────────────────────────────────────── scenes ──\n
def EL(weight=1):
    return ("el", weight)


def zone(L, top):
    bot = L.bottom - 150
    return bot, bot - top


def fy(top, avail, f):
    return int(top + avail * f)


def arrow_v(d, y0, y1, x, color, wd=8, hd=34):
    down = y1 > y0
    sy, ey = (y0, y1 - hd) if down else (y0, y1 + hd)
    d.rectangle([x - wd // 2, min(sy, ey), x + wd // 2, max(sy, ey)], fill=color)
    if down:
        d.polygon([(x, y1), (x - hd * 0.62, y1 - hd), (x + hd * 0.62, y1 - hd)], fill=color)
    else:
        d.polygon([(x, y1), (x - hd * 0.62, y1 + hd), (x + hd * 0.62, y1 + hd)], fill=color)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines



# ─────────────────────────────────────────────────────────────── scenes ──
def node(d, L, x0, x1, y, h, label, color, filled=False):
    """A system block: CANVAS or THE HUB."""
    if filled:
        d.rectangle([x0, y, x1, y + h], fill=color); fg = GROUND
    else:
        box(d, x0, y, x1, y + h, color, 6); fg = color
    f = fit(MONOB, int(h * 0.30), label, (x1 - x0) - 56)
    d.text((x0 + 28, y + h / 2 - f.size * 0.70), label, font=f, fill=fg)


def pill(d, L, cx, y, w, h, label, color):
    """A labelled block riding on an arrow."""
    x0, x1 = int(cx - w / 2), int(cx + w / 2)
    d.rectangle([x0, y, x1, y + h], fill=color)
    f = fit(MONOB, int(h * 0.42), label, w - 44)
    d.text((x0 + 22, y + h / 2 - f.size * 0.70), label, font=f, fill=GROUND)


def strike(d, x0, x1, y, color, wd=14):
    d.rectangle([x0, y - wd // 2, x1, y + wd // 2], fill=color)



# ── aspect-agnostic helpers ─────────────────────────────────────────────────
# Every beat in this reel is a single stacked column, so the same layout serves
# 16:9 and 9:16. Nothing is placed side by side and nothing is placed by a
# fraction of the frame WIDTH.

def stack(L, y0, n, ratio=0.16, gap_ratio=0.045, cap=None):
    """n equal rows, centred in the band. Returns (rows, h, gap)."""
    bot, av = zone(L, y0)
    h = int(av * ratio)
    if cap:
        h = min(h, cap)
    gap = int(av * gap_ratio)
    total = n * h + (n - 1) * gap
    top = y0 + max(0, (av - total) // 2)
    return [top + i * (h + gap) for i in range(n)], h, gap


def row(d, L, y, h, text, fg, *, filled=False, mono=True, share=0.30):
    spec = MONOB if mono else DISPLAY
    if filled:
        d.rectangle([L.mx, y, L.right, y + h], fill=fg); ink = GROUND
    else:
        box(d, L.mx, y, L.right, y + h, fg, 6); ink = fg
    f = fit(spec, int(h * share), text, (L.right - L.mx) - 60)
    d.text((L.mx + 30, y + h / 2 - f.size * 0.70), text, font=f, fill=ink)


def title_card(L, foot, reveal=4):
    img, d = frame(L)
    rule(d, L, L.my, SIGNAL, 16)
    sub = F(MONOB, L.h2)
    ry = int(L.bottom - 92 - 60 - sub.size - 50)
    y = int(L.my + (L.h * 0.08))
    cap = int((ry - 90 - y) / 3.30)
    f = fit(DISPLAY, min(430, cap), "THE ROLE", L.right - L.mx, -0.02)
    for i, w in enumerate(("THE ROLE", "THAT", "LIED")):
        if reveal >= i + 1:
            track(d, (L.mx, y + int(f.size * 1.18) * i), w, f, PAPER)
    if reveal >= 4:
        rule(d, L, ry, MUTE, 8)
        d.text((L.mx, ry + 50), "READING AN LTI ROLE", font=sub, fill=SIGNAL)
    footer(d, L, foot)
    return img


def span_text(d, L, y, text, size, head_len, lead_fill, tail_fill, mono=True):
    """Draw text with the first head_len characters in one colour, rest in another."""
    spec = MONOB if mono else DISPLAY
    f = fit(spec, size, text, (L.right - L.mx))
    x = L.mx
    for i, ch in enumerate(text):
        d.text((x, y), ch, font=f, fill=(lead_fill if i < head_len else tail_fill))
        x += f.getlength(ch)
    return f


def hl_substring(d, L, y, text, needle, size):
    """Draw `text`, picking `needle` out in signal."""
    f = fit(MONOB, size, text, (L.right - L.mx))
    i = text.find(needle)
    x = L.mx
    for j, ch in enumerate(text):
        on = i >= 0 and i <= j < i + len(needle)
        d.text((x, y), ch, font=f, fill=(SIGNAL if on else PAPER))
        x += f.getlength(ch)
    return f


def b00(L):
    foot = "one line of code that decided who was a teacher"
    return [(6, lambda: title_card(L, foot, 0)), (7, lambda: title_card(L, foot, 1)),
            (7, lambda: title_card(L, foot, 2)), (7, lambda: title_card(L, foot, 3)),
            (EL(6), lambda: title_card(L, foot, 4))]


def b01(L):
    URN = "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHERE THE ROLE COMES FROM")
        ys, h, gap = stack(L, y0, 2, ratio=0.26, gap_ratio=0.14)
        if st >= 1:
            box(d, L.mx, ys[0], L.right, ys[0] + h, PAPER, 6)
            f = fit(MONO, int(h * 0.20), URN, (L.right - L.mx) - 56)
            d.text((L.mx + 28, ys[0] + h * 0.22), URN, font=f, fill=PAPER)
            cf = F(MONOB, int(h * 0.15))
            d.text((L.mx + 28, ys[0] + h * 0.60), "A LIST OF URNs - NOT WORDS",
                   font=cf, fill=MUTE)
        if st >= 2:
            arrow_v(d, ys[0] + h + 16, ys[1] - 12, (L.mx + L.right) // 2, MUTE, 12, 44)
        if st >= 3:
            row(d, L, ys[1], h, "STUDENT OR INSTRUCTOR", SIGNAL, filled=True, share=0.28)
        footer(d, L, "one decision, taken from a list of identifiers")
        return img
    return [(8, lambda: draw(0)), (EL(4), lambda: draw(1)), (4, lambda: draw(2)),
            (EL(7), lambda: draw(3))]


def b02(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE SHORTCUT")
        ys, h, gap = stack(L, y0, 2, ratio=0.27, gap_ratio=0.12)
        if st >= 1:
            row(d, L, ys[0], h, 'roles.includes("Instructor")', SIGNAL, share=0.30)
        if st >= 2:
            t1 = "ONE LINE - READS NATURALLY"
            t2 = "PASSES THE OBVIOUS TESTS"
            f = fit(MONOB, int(h * 0.26), t1, L.right - L.mx)
            d.text((L.mx, ys[1] + h * 0.14), t1, font=f, fill=MUTE)
            d.text((L.mx, ys[1] + h * 0.14 + f.size * 1.45), t2, font=f, fill=MUTE)
        footer(d, L, "it reads naturally, which is the problem")
        return img
    return [(7, lambda: draw(0)), (EL(5), lambda: draw(1)), (EL(7), lambda: draw(2))]


def b03(L):
    rows = ["LearnerInstructorFake",
            "urn:lti:role:ims/lis/Learner#PseudoInstructor",
            "NotAnInstructorReally"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHAT IT ACTUALLY MATCHES")
        ys, h, gap = stack(L, y0, 4, ratio=0.14, gap_ratio=0.05)
        longest = max(rows, key=len)
        uf = fit(MONOB, int(h * 0.52), longest, (L.right - L.mx))
        for i, t in enumerate(rows):
            if st < i + 1:
                continue
            hl_substring(d, L, ys[i] + h * 0.18, t, "Instructor", uf.size)
        if st >= 4:
            row(d, L, ys[3], h, "ALL THREE MATCH", SIGNAL, filled=True, share=0.34)
        footer(d, L, "the check asks whether ten letters appear, not what the role is")
        return img
    return [(7, lambda: draw(0))] + \
           [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(7), lambda: draw(4))]


def b04(L):
    URN = "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHERE THE MEANING LIVES")
        ys, h, gap = stack(L, y0, 2, ratio=0.24, gap_ratio=0.13)
        cut = URN.rfind("#") + 1
        size = int(h * 0.30)
        if st >= 1:
            span_text(d, L, ys[0] + h * 0.30, URN, size, cut, MUTE, MUTE)
        if st >= 2:
            f = span_text(d, L, ys[0] + h * 0.30, URN, size, cut, MUTE, SIGNAL)
            x0 = L.mx + sum(f.getlength(c) for c in URN[:cut])
            x1 = L.mx + sum(f.getlength(c) for c in URN)
            box(d, int(x0) - 16, int(ys[0] + h * 0.18), int(x1) + 16,
                int(ys[0] + h * 0.30 + f.size * 1.35), SIGNAL, 6)
        if st >= 3:
            t1 = "THE LAST SEGMENT"
            t2 = "EVERYTHING ELSE IS NAMESPACE"
            f = fit(MONOB, int(h * 0.26), t2, L.right - L.mx)
            d.text((L.mx, ys[1] + h * 0.12), t1, font=f, fill=PAPER)
            d.text((L.mx, ys[1] + h * 0.12 + f.size * 1.45), t2, font=f, fill=MUTE)
        footer(d, L, "does the final segment equal an identifier we accept")
        return img
    return [(8, lambda: draw(0)), (EL(4), lambda: draw(1)), (EL(5), lambda: draw(2)),
            (EL(6), lambda: draw(3))]


def b05(L):
    stages = ["SPLIT ON  /  #  :", "TAKE THE LAST SEGMENT", "LOWERCASE",
              "LOOK UP IN THE ALLOW LIST"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE FIX")
        ys, h, gap = stack(L, y0, 5, ratio=0.125, gap_ratio=0.035)
        for i, s in enumerate(stages):
            if st < i + 1:
                continue
            row(d, L, ys[i], h, s, PAPER, share=0.36)
            if i:
                arrow_v(d, ys[i] - gap + 4, ys[i] - 6, (L.mx + L.right) // 2, MUTE, 6, 22)
        if st >= 5:
            arrow_v(d, ys[4] - gap + 4, ys[4] - 6, (L.mx + L.right) // 2, SIGNAL, 8, 24)
            row(d, L, ys[4], h, "NOT IN THE SET = STUDENT", SIGNAL, filled=True, share=0.36)
        footer(d, L, "it fails closed, which is the direction you want a mistake to fall")
        return img
    return [(7, lambda: draw(0))] + \
           [(3, (lambda s: lambda: draw(s))(i)) for i in range(1, 5)] + \
           [(EL(8), lambda: draw(5))]


def b06(L):
    tests = [("LearnerInstructorFake", "student"),
             ("Learner#PseudoInstructor", "student"),
             ("instructor-wannabe", "student")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE TESTS ARE THE RECORD")
        ys, h, gap = stack(L, y0, 4, ratio=0.14, gap_ratio=0.05)
        for i, (inp, out) in enumerate(tests):
            if st < i + 1:
                continue
            f = F(MONOB, int(h * 0.40))
            marker(d, L.mx, ys[i] + h * 0.26, int(f.size * 0.38), SIGNAL)
            t = f"{inp}  ->  {out}"
            ff = fit(MONOB, int(h * 0.40), t, (L.right - L.mx) - int(f.size * 0.95))
            d.text((L.mx + int(f.size * 0.95), ys[i] + h * 0.18), t, font=ff, fill=PAPER)
        if st >= 4:
            t = "FAILS CLOSED - AND STAYS THAT WAY"
            rule(d, L, ys[3] + h * 0.1, SIGNAL, 14)
            d.text((L.mx, ys[3] + h * 0.1 + 50), t,
                   font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "the escalation strings are committed as test cases")
        return img
    return [(7, lambda: draw(0))] + \
           [(3, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(7), lambda: draw(4))]


def b07(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "TWO DIFFERENT CHECKS")
        ys, h, gap = stack(L, y0, 2, ratio=0.19, gap_ratio=0.07)
        if st >= 1:
            row(d, L, ys[0], h, "SUBSTRING - IS IT IN THERE SOMEWHERE", MUTE, share=0.26)
        if st >= 2:
            row(d, L, ys[1], h, "ALLOW LIST - IS IT EXACTLY THIS", SIGNAL,
                filled=True, share=0.26)
        footer(d, L, "they agree most of the time, which is why this survives")
        return img
    return [(6, lambda: draw(0)), (EL(4), lambda: draw(1)), (EL(6), lambda: draw(2)),
            (EL(5), lambda: title_card(L, "medhavy canvas lti 1.3"))]


SCENES = {"B00": b00, "B01": b01, "B02": b02, "B03": b03,
          "B04": b04, "B05": b05, "B06": b06, "B07": b07}


# ──────────────────────────────────────────────────────────── assembly ──
def allocate(segs, total):
    fixed = sum(f for f, _ in segs if isinstance(f, int))
    ws = [(i, 1 if f is None else f[1])
          for i, (f, _) in enumerate(segs) if not isinstance(f, int)]
    out = [f if isinstance(f, int) else 0 for f, _ in segs]
    left, wsum, acc = total - fixed, sum(w for _, w in ws) or 1, 0
    for j, (i, w) in enumerate(ws):
        share = left * w // wsum if j < len(ws) - 1 else left - acc
        out[i] = share; acc += share
    drift = total - sum(out)
    if drift:
        out[-1] = max(1, out[-1] + drift)
    return out


def render_beat(bid, L, dur, outdir, workroot):
    total = max(1, round(dur * FPS))
    segs = SCENES[bid](L)
    counts = allocate(segs, total)
    work = workroot / bid
    (work / "states").mkdir(parents=True); (work / "frames").mkdir()
    n = 0
    for idx, ((_, fn), cnt) in enumerate(zip(segs, counts)):
        if cnt <= 0:
            continue
        st = work / "states" / f"s{idx:04d}.png"
        fn().save(st, compress_level=1)
        for _ in range(cnt):
            n += 1
            os.link(st, work / "frames" / f"{n:06d}.png")
    out = outdir / f"{bid}.mp4"
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS),
                    "-i", str(work / "frames" / "%06d.png"),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                    "-pix_fmt", "yuv420p", "-color_primaries", "bt709",
                    "-color_trc", "bt709", "-colorspace", "bt709", str(out)],
                   check=True, capture_output=True)
    shutil.rmtree(work)
    return out, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    ap.add_argument("--sheet"); ap.add_argument("--out"); ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    reel = Path(__file__).resolve().parent.parent
    sheet = json.loads(Path(a.sheet or reel / "beat_sheet.json").read_text())
    W, H = (3840, 2160) if a.aspect == "16:9" else (2160, 3840)
    L, outdir = Layout(W, H), Path(a.out or reel / "media")
    outdir.mkdir(parents=True, exist_ok=True)
    workroot = Path(tempfile.mkdtemp(prefix="scenes-"))
    print(f"[render] {a.aspect} {W}x{H} @{FPS}fps -> {outdir}")
    for b in sheet["beats"]:
        bid = b["beat_id"]
        if a.only and bid not in a.only:
            continue
        if bid not in SCENES:
            print(f"[render] {bid}: no scene defined — skipped"); continue
        dur = b.get("actual_duration_s") or b["estimated_duration_s"]
        out, n = render_beat(bid, L, float(dur), outdir, workroot)
        print(f"[render] {bid} {float(dur):>6.2f}s {n:>5d} frames -> {out.name}")
    shutil.rmtree(workroot, ignore_errors=True)


if __name__ == "__main__":
    main()
