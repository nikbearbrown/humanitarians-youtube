#!/usr/bin/env python3
"""Per-script renderer — Ten Prefixes, Eleven Tables (the LTI schema).

Core (layout, fonts, elastic allocation, assembly) and the node/box helpers
reused verbatim from medhavy-canvas-sync; only the scene functions are new.
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
    d.text((L.mx, L.bottom - 70), text, font=F(MONO, L.caption), fill=MUTE)


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



def title_card(L, foot, reveal=3):
    """Two display lines + subtitle, sized upward from the footer rule.

    Same derivation as medhavy-canvas-sync: the subtitle rule position and the
    title size both come from the footer, never from a fraction of the frame.
    """
    img, d = frame(L)
    rule(d, L, L.my, SIGNAL, 16)
    sub = F(MONOB, L.h2)
    ry = int(L.bottom - 92 - 60 - sub.size - 50)
    y = int(L.h * 0.18)
    cap = int((ry - 90 - y) / 2.25)
    f = fit(DISPLAY, min(430, cap), "ELEVEN TABLES", L.right - L.mx, -0.02)
    for i, w in enumerate(("TEN PREFIXES", "ELEVEN TABLES")):
        if reveal >= i + 1:
            track(d, (L.mx, y + int(f.size * 1.18) * i), w, f, PAPER)
    if reveal >= 3:
        rule(d, L, ry, MUTE, 8)
        d.text((L.mx, ry + 50), "THE LTI SCHEMA", font=sub, fill=SIGNAL)
    footer(d, L, foot)
    return img


def tcard(d, L, x0, x1, y, h, name, purpose, lit=False):
    """A table card: mono name in paper, purpose in mute."""
    if lit:
        d.rectangle([x0, y, x1, y + h], fill=SIGNAL); fg, sg = GROUND, GROUND
    else:
        box(d, x0, y, x1, y + h, PAPER, 6); fg, sg = PAPER, MUTE
    nf = fit(MONOB, int(h * 0.20), name, (x1 - x0) - 56)
    d.text((x0 + 28, y + int(h * 0.16)), name, font=nf, fill=fg)
    pf = F(MONO, int(h * 0.135))
    for j, ln in enumerate(wrap(purpose, pf, (x1 - x0) - 56)[:2]):
        d.text((x0 + 28, y + int(h * 0.56) + j * int(pf.size * 1.35)), ln, font=pf, fill=sg)


def b00(L):
    foot = "eleven tables, and a count that looked like a mistake"
    return [(6, lambda: title_card(L, foot, 0)), (8, lambda: title_card(L, foot, 1)),
            (8, lambda: title_card(L, foot, 2)), (EL(6), lambda: title_card(L, foot, 3))]


def b01(L):
    bands = [("01", "WHO MAY LAUNCH"), ("02", "MAP IDENTITY"), ("03", "FORGET, ON A TIMER")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THREE JOBS")
        bot, av = zone(L, y0)
        h = int(av * 0.21)
        gap = int(av * 0.065)
        for i, (num, lab) in enumerate(bands):
            if st < i + 1:
                continue
            yy = fy(y0, av, 0.06) + i * (h + gap)
            on = (i == 2)
            if on:
                d.rectangle([L.mx, yy, L.right, yy + h], fill=SIGNAL); fg = GROUND
            else:
                box(d, L.mx, yy, L.right, yy + h, PAPER, 6); fg = PAPER
            nf = F(DISPLAY, int(h * 0.52))
            d.text((L.mx + 30, yy + h / 2 - nf.size * 0.62), num, font=nf, fill=fg)
            lf = fit(MONOB, int(h * 0.30), lab, (L.right - L.mx) - int(nf.size * 1.9) - 60)
            d.text((L.mx + 30 + nf.size * 1.5, yy + h / 2 - lf.size * 0.70),
                   lab, font=lf, fill=fg)
        footer(d, L, "the schema does three jobs, and nothing else")
        return img
    return [(8, lambda: draw(0))] + \
           [(3, (lambda s: lambda: draw(s))(i)) for i in range(1, 3)] + \
           [(EL(8), lambda: draw(3))]


def b02(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "WHO MAY LAUNCH")
        bot, av = zone(L, y0)
        gap = 70
        wpx = (L.right - L.mx - gap) / 2
        h = int(av * 0.44)
        yy = fy(y0, av, 0.05)
        cards = [("lti_platform_registrations", "which Canvas instances we trust"),
                 ("lti_deployments", "which installation inside it")]
        for i, (n, p) in enumerate(cards):
            if st < i + 1:
                continue
            x0 = int(L.mx + i * (wpx + gap))
            tcard(d, L, x0, int(x0 + wpx), yy, h, n, p)
        if st >= 3:
            cy = fy(y0, av, 0.70)
            rule(d, L, cy, SIGNAL, 14)
            t = "NOT IN HERE = NOT A LAUNCH"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "together they are the guest list")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (EL(5), lambda: draw(2)),
            (EL(7), lambda: draw(3))]


def b03(L):
    rows = ["lti_user_links", "lti_course_links", "lti_resource_links"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "MAPPING IDENTITY")
        bot, av = zone(L, y0)
        rh = int(av * 0.16)
        gap = int(av * 0.055)
        bw = int((L.right - L.mx) * 0.21)
        for i, name in enumerate(rows):
            if st < i + 1:
                continue
            yy = fy(y0, av, 0.03) + i * (rh + gap)
            mid = yy + rh // 2
            node(d, L, L.mx, L.mx + bw, yy, rh, "CANVAS SIDE", MUTE)
            node(d, L, L.right - bw, L.right, yy, rh, "OUR SIDE", MUTE)
            arrow(d, L.mx + bw + 40, L.right - bw - 40, mid, SIGNAL, 8, 34)
            nf = fit(MONOB, int(rh * 0.34), name, (L.right - bw - 40) - (L.mx + bw + 40) - 80)
            d.text((L.mx + bw + 90, mid - nf.size * 1.95), name, font=nf, fill=PAPER)
        if st >= 4:
            cy = fy(y0, av, 0.76)
            rule(d, L, cy, SIGNAL, 14)
            t = "A CORRESPONDENCE - NOT A COPY"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "we do not store a Canvas person, we store a correspondence")
        return img
    return [(8, lambda: draw(0))] + \
           [(4, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(7), lambda: draw(4))]


def b04(L):
    cards = [("lti_nonce_store", "10 MIN", "the one-time values from a login"),
             ("lti_launch_sessions", "1 HR", "the audit record of a launch")]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "TABLES THAT FORGET")
        bot, av = zone(L, y0)
        gap = 70
        wpx = (L.right - L.mx - gap) / 2
        h = int(av * 0.50)
        yy = fy(y0, av, 0.04)
        for i, (n, dur, p) in enumerate(cards):
            if st < i + 1:
                continue
            x0 = int(L.mx + i * (wpx + gap)); x1 = int(x0 + wpx)
            box(d, x0, yy, x1, yy + h, PAPER, 6)
            nf = fit(MONOB, int(h * 0.11), n, wpx - 56)
            d.text((x0 + 28, yy + int(h * 0.07)), n, font=nf, fill=PAPER)
            df = fit(DISPLAY, int(h * 0.34), dur, wpx - 56, -0.02)
            track(d, (x0 + 28, yy + int(h * 0.30)), dur, df, SIGNAL)
            pf = F(MONO, int(h * 0.085))
            for j, ln in enumerate(wrap(p, pf, wpx - 56)[:2]):
                d.text((x0 + 28, yy + int(h * 0.76) + j * int(pf.size * 1.35)),
                       ln, font=pf, fill=MUTE)
        if st >= 3:
            cy = fy(y0, av, 0.76)
            rule(d, L, cy, MUTE, 8)
            d.text((L.mx, cy + 44), "THEN PURGED", font=F(MONOB, L.h2), fill=MUTE)
        footer(d, L, "a table whose job is to expire is doing security work")
        return img
    return [(8, lambda: draw(0)), (6, lambda: draw(1)), (EL(5), lambda: draw(2)),
            (EL(9), lambda: draw(3))]


def b05(L):
    rows = ["lti_v1_credentials", "lti_v1_nonces", "lti_v1_launches"]
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "THE LEGACY THREE")
        bot, av = zone(L, y0)
        rf = F(MONOB, L.h2)
        ry = fy(y0, av, 0.10)
        inset = int((L.right - L.mx) * 0.08)
        for i, r in enumerate(rows):
            if st < i + 1:
                continue
            yy = ry + i * int(rf.size * 2.1)
            marker(d, L.mx + inset, yy + int(rf.size * 0.20), int(rf.size * 0.34), MUTE)
            d.text((L.mx + inset + int(rf.size * 0.85), yy), r, font=rf, fill=MUTE)
        if st >= 4:
            cy = fy(y0, av, 0.74)
            rule(d, L, cy, MUTE, 6)
            d.text((L.mx + inset, cy + 40), "OLDER HANDSHAKE - SAME SHAPES",
                   font=F(MONOB, L.caption), fill=MUTE)
        footer(d, L, "kept for platforms that have not moved yet")
        return img
    return [(7, lambda: draw(0))] + \
           [(3, (lambda s: lambda: draw(s))(i)) for i in range(1, 4)] + \
           [(EL(7), lambda: draw(4))]


def b06(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "TEN AND ELEVEN")
        bot, av = zone(L, y0)
        nf = fit(DISPLAY, int(av * 0.46), "11", int((L.right - L.mx) * 0.26), -0.02)
        ny = fy(y0, av, 0.02)
        lx = L.mx
        rx = L.mx + int((L.right - L.mx) * 0.56)
        cf = F(MONOB, L.caption)
        if st >= 1:
            track(d, (lx, ny), "10", nf, PAPER)
            d.text((lx, ny + int(nf.size * 1.10)), "TABLES NAMED lti_*", font=cf, fill=MUTE)
        if st >= 2:
            track(d, (rx, ny), "11", nf, PAPER)
            d.text((rx, ny + int(nf.size * 1.10)), "TABLES WITH RLS ENABLED", font=cf, fill=MUTE)
        if st >= 3:
            w10 = sum(nf.getlength(c) - 0.02 * nf.size for c in "10")
            gx0 = lx + int(w10) + 70
            gw = (rx - 70) - gx0
            lab = "+ institutions"
            lf = fit(MONOB, L.body, lab, gw)
            d.text((gx0, ny + int(nf.size * 0.34)), lab, font=lf, fill=SIGNAL)
        if st >= 4:
            cy = fy(y0, av, 0.72)
            rule(d, L, cy, SIGNAL, 14)
            t = "COUNTING NAMES vs COUNTING PROTECTIONS"
            d.text((L.mx, cy + 50), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        footer(d, L, "both numbers were right, counting different things")
        return img
    return [(8, lambda: draw(0)), (EL(4), lambda: draw(1)), (EL(4), lambda: draw(2)),
            (EL(4), lambda: draw(3)), (EL(7), lambda: draw(4))]


def b07(L):
    def draw(st):
        img, d = frame(L)
        y0 = head(d, L, "ELEVEN OF ELEVEN")
        bot, av = zone(L, y0)
        yy = fy(y0, av, 0.06)
        h = int(av * 0.30)
        if st >= 1:
            d.rectangle([L.mx, yy, L.right, yy + h], fill=SIGNAL)
            t = "RLS - 11/11 - SERVICE ROLE ONLY"
            f = fit(MONOB, int(h * 0.30), t, (L.right - L.mx) - 60)
            d.text((L.mx + 30, yy + h / 2 - f.size * 0.70), t, font=f, fill=GROUND)
        if st >= 2:
            cy = yy + h + int(av * 0.10)
            t = "NON-SERVICE ROLE - DENIED READ, DENIED WRITE"
            d.text((L.mx, cy), t, font=fit(MONOB, L.h2, t, L.right - L.mx), fill=PAPER)
        if st >= 3:
            cy2 = fy(y0, av, 0.78)
            rule(d, L, cy2, MUTE, 8)
            t = "every table it does not have is a table that cannot leak"
            d.text((L.mx, cy2 + 44), t, font=fit(MONO, L.body, t, L.right - L.mx), fill=MUTE)
        footer(d, L, "the schema is small deliberately")
        return img
    return [(7, lambda: draw(0)), (EL(4), lambda: draw(1)), (EL(4), lambda: draw(2)),
            (EL(5), lambda: draw(3)), (EL(5), lambda: title_card(L, "medhavy canvas lti 1.3"))]


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
