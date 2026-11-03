#!/usr/bin/env python3
"""make_cards.py — house-style 4K PIL body cards for the multimodal-ai reel.

Renders every beat whose shot.source == "still" (B01-B05) from its shot.card
spec in beat_sheet.json. Claude fidelity palette, EB Garamond serif. Two
aspects: 16x9 (3840x2160 → media/) and 9x16 (2160x3840 → short/media/).

    python3 make_cards.py                      # 16:9 into media/
    python3 make_cards.py --aspect 9x16 --out short/media   # portrait

The diagram lanes re-lay-out for portrait (stack vertically). Change the card
specs in beat_sheet.json, never the motion — these are held stills.
"""
import argparse, json, glob, os, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ── palette (claude fidelity tokens) ─────────────────────────────────────────
PAGE   = "#FAF9F5"; CARD = "#FFFFFF"; BORDER = "#E5E2D9"; FOOTER_BG = "#F1EFE7"
INK    = "#3D3929"; INK_SOFT = "#73705F"; GHOST = "#A9A491"
SPARK  = "#D97757"; SEND = "#C6613F"; INK_BOX = "#3D3929"

FONTS = Path.home() / "Documents/brutalist.art/runtime/fonts"

def _find(*cands):
    for c in cands:
        hits = glob.glob(str(FONTS / c), recursive=True)
        if hits: return sorted(hits)[0]
    return None

SERIF_REG  = _find("EB_Garamond/**/EBGaramond-Regular.ttf", "EB_Garamond/**/*Regular*.ttf")
SERIF_MED  = _find("EB_Garamond/**/EBGaramond-Medium.ttf", "EB_Garamond/**/*Medium*.ttf") or SERIF_REG
SERIF_ITAL = _find("EB_Garamond/**/EBGaramond-Italic.ttf", "EB_Garamond/**/*Italic*.ttf") or SERIF_REG
SANS       = _find("Inter/**/Inter_*SemiBold.ttf", "Inter/**/*SemiBold*.ttf",
                   "Inter/**/Inter_*Medium.ttf", "Inter/**/*Medium*.ttf",
                   "Montserrat/**/*SemiBold*.ttf") or SERIF_MED
SANS_REG   = _find("Inter/**/Inter_*Regular.ttf", "Inter/**/*Regular*.ttf") or SANS

_cache = {}
def font(path, size):
    key = (path, int(size))
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, int(size))
    return _cache[key]

# ── text helpers ─────────────────────────────────────────────────────────────
def tw(d, s, f):
    b = d.textbbox((0, 0), s, font=f); return b[2] - b[0]
def th(d, s, f):
    b = d.textbbox((0, 0), s, font=f); return b[3] - b[1]

def center(d, cx, cy, s, f, fill):
    d.text((cx, cy), s, font=f, fill=fill, anchor="mm")

def title_with_period(d, cx, cy, s, f):
    """Serif title centered; a trailing '.' rendered in SPARK (brand)."""
    if s.endswith("."):
        head, dot = s[:-1], "."
    else:
        head, dot = s, ""
    wh = tw(d, head, f); wd = tw(d, dot, f)
    total = wh + wd
    x = cx - total / 2
    d.text((x, cy), head, font=f, fill=INK, anchor="lm")
    if dot:
        d.text((x + wh, cy), dot, font=f, fill=SPARK, anchor="lm")

def tracked(d, cx, cy, s, f, fill, track):
    """Center a letter-spaced (small-caps footer) string."""
    widths = [tw(d, ch, f) for ch in s]
    total = sum(widths) + track * (len(s) - 1)
    x = cx - total / 2
    for ch, w in zip(s, widths):
        d.text((x, cy), ch, font=f, fill=fill, anchor="lm")
        x += w + track

def wrap(d, s, f, maxw):
    out, line = [], ""
    for word in s.split():
        t = (line + " " + word).strip()
        if tw(d, t, f) <= maxw:
            line = t
        else:
            if line: out.append(line)
            line = word
    if line: out.append(line)
    return out

def para(d, cx, cy, s, f, fill, maxw, lh):
    lines = wrap(d, s, f, maxw)
    for i, ln in enumerate(lines):
        center(d, cx, cy + i * lh, ln, f, fill)
    return len(lines) * lh

def rrect(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def arrow(d, x0, y0, x1, y1, color, w, head):
    d.line([(x0, y0), (x1, y1)], fill=color, width=w)
    import math
    ang = math.atan2(y1 - y0, x1 - x0)
    for da in (math.radians(150), math.radians(-150)):
        d.line([(x1, y1), (x1 + head * math.cos(ang + da), y1 + head * math.sin(ang + da))],
               fill=color, width=w)

# ── chip / box primitives ────────────────────────────────────────────────────
def chip(d, cx, cy, w, h, label, U, accent=False, sub=None):
    col = SPARK if accent else BORDER
    rrect(d, [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], r=int(0.02 * U["W"]),
          fill=CARD, outline=col, width=int(0.004 * U["W"]) if accent else int(0.0022 * U["W"]))
    if sub:
        center(d, cx, cy - h * 0.14, label, U["f_box"], INK)
        center(d, cx, cy + h * 0.24, sub, U["f_small"], INK_SOFT)
    else:
        center(d, cx, cy, label, U["f_box"], INK)

# ── card kinds ───────────────────────────────────────────────────────────────
def draw_flow(d, c, U):
    W, H, port = U["W"], U["H"], U["port"]
    inputs, hub, hub_sub, out = c["inputs"], c["hub"], c.get("hub_sub", ""), c["output"]
    n = len(inputs)
    if not port:
        ix = 0.15 * W; iw = 0.19 * W; ih = 0.10 * H
        top, bot = 0.34, 0.76
        ys = [(top + bot) / 2] if n == 1 else [top + (bot - top) * i / (n - 1) for i in range(n)]
        hubx, huby, hubw, hubh = 0.50 * W, 0.55 * H, 0.24 * W, 0.19 * H
        for lab, yf in zip(inputs, ys):
            cy = yf * H
            chip(d, ix, cy, iw, ih, lab, U)
            arrow(d, ix + iw / 2, cy, hubx - hubw / 2 - 0.01 * W,
                  huby + (cy - huby) * 0.22, INK_SOFT, U["aw"], U["ah"])
        rrect(d, [hubx - hubw / 2, huby - hubh / 2, hubx + hubw / 2, huby + hubh / 2],
              r=int(0.02 * W), fill=CARD, outline=SPARK, width=int(0.006 * W))
        center(d, hubx, huby - hubh * 0.12, hub, U["f_hub"], INK)
        center(d, hubx, huby + hubh * 0.24, hub_sub, U["f_small"], INK_SOFT)
        ox = 0.85 * W
        arrow(d, hubx + hubw / 2, huby, ox - 0.085 * W, huby, SPARK, U["aw"], U["ah"])
        chip(d, ox, huby, 0.16 * W, 0.12 * H, out, U)
    else:
        iw = 0.40 * W; ih = 0.075 * H
        if n <= 2:
            xs = [0.5 * W] if n == 1 else [0.29 * W, 0.71 * W]
            pos = [(x, 0.33 * H) for x in xs]
        else:
            pos = [(0.29 * W, 0.31 * H), (0.71 * W, 0.31 * H),
                   (0.29 * W, 0.41 * H), (0.71 * W, 0.41 * H)][:n]
        for lab, (x, y) in zip(inputs, pos):
            chip(d, x, y, iw, ih, lab, U)
        hubx, huby, hubw, hubh = 0.5 * W, 0.58 * H, 0.62 * W, 0.11 * H
        for (x, y) in pos:
            arrow(d, x, y + ih / 2, hubx + (x - 0.5 * W) * 0.2, huby - hubh / 2 - 0.008 * H,
                  INK_SOFT, U["aw"], U["ah"])
        rrect(d, [hubx - hubw / 2, huby - hubh / 2, hubx + hubw / 2, huby + hubh / 2],
              r=int(0.02 * W), fill=CARD, outline=SPARK, width=int(0.006 * W))
        center(d, hubx, huby - hubh * 0.15, hub, U["f_hub"], INK)
        center(d, hubx, huby + hubh * 0.25, hub_sub, U["f_small"], INK_SOFT)
        oy = 0.72 * H
        arrow(d, hubx, huby + hubh / 2, hubx, oy - 0.05 * H, SPARK, U["aw"], U["ah"])
        chip(d, hubx, oy, 0.5 * W, 0.075 * H, out, U)

def _node_text(d, x, y, label, U, maxw):
    lh = int(0.026 * U["W"])
    lines = wrap(d, label, U["f_box"], maxw)
    for j, ln in enumerate(lines):
        center(d, x, y - (len(lines) - 1) * lh / 2 + j * lh, ln, U["f_box"], INK)

def draw_loop(d, c, U):
    """The loop diagram: N nodes in sequence + a terracotta 'repeat' return arrow."""
    W, H, port = U["W"], U["H"], U["port"]
    nodes = c["nodes"]; ret = c.get("repeat_label", "repeat until the goal is met → stop")
    n = len(nodes)
    if not port:
        nw = 0.205 * W; nh = 0.17 * H; gap = 0.02 * W
        tot = n * nw + (n - 1) * gap
        x0 = (W - tot) / 2 + nw / 2; y = 0.45 * H
        xs = [x0 + i * (nw + gap) for i in range(n)]
        for i, (x, label) in enumerate(zip(xs, nodes)):
            rrect(d, [x - nw / 2, y - nh / 2, x + nw / 2, y + nh / 2], r=int(0.014 * W),
                  fill=CARD, outline=BORDER, width=int(0.0022 * W))
            _node_text(d, x, y, label, U, nw * 0.84)
            if i < n - 1:
                arrow(d, x + nw / 2, y, xs[i + 1] - nw / 2, y, INK_SOFT, U["aw"], U["ah"])
        yb = y + nh / 2 + 0.11 * H
        d.line([(xs[-1], y + nh / 2), (xs[-1], yb)], fill=SPARK, width=U["aw"])
        d.line([(xs[-1], yb), (xs[0], yb)], fill=SPARK, width=U["aw"])
        arrow(d, xs[0], yb, xs[0], y + nh / 2 + 0.004 * H, SPARK, U["aw"], U["ah"])
        center(d, (xs[0] + xs[-1]) / 2, yb + 0.045 * H, ret, U["f_note"], SPARK)
    else:
        nw = 0.62 * W; nh = 0.088 * H; gap = 0.05 * H
        x = 0.42 * W; y0 = 0.30 * H
        ys = [y0 + i * (nh + gap) for i in range(n)]
        for i, (yy, label) in enumerate(zip(ys, nodes)):
            rrect(d, [x - nw / 2, yy - nh / 2, x + nw / 2, yy + nh / 2], r=int(0.014 * W),
                  fill=CARD, outline=BORDER, width=int(0.0022 * W))
            _node_text(d, x, yy, label, U, nw * 0.84)
            if i < n - 1:
                arrow(d, x, yy + nh / 2, x, ys[i + 1] - nh / 2, INK_SOFT, U["aw"], U["ah"])
        rxx = 0.85 * W
        d.line([(x + nw / 2, ys[-1]), (rxx, ys[-1])], fill=SPARK, width=U["aw"])
        d.line([(rxx, ys[-1]), (rxx, ys[0])], fill=SPARK, width=U["aw"])
        arrow(d, rxx, ys[0], x + nw / 2 + 0.004 * W, ys[0], SPARK, U["aw"], U["ah"])
        center(d, 0.5 * W, ys[-1] + nh / 2 + 0.055 * H, ret, U["f_note"], SPARK)

def draw_grid(d, c, U):
    W, H, port = U["W"], U["H"], U["port"]
    items = c["items"]
    n = len(items)
    if not port:
        cols = 2 if n <= 4 else 3
        rows = (n + cols - 1) // cols
        cw = (0.285 * W) if cols == 3 else (0.40 * W)
        gx = (0.028 * W) if cols == 3 else (0.03 * W)
        ch, gy = 0.15 * H, 0.035 * H
        gridw = cols * cw + (cols - 1) * gx
        x0 = (W - gridw) / 2 + cw / 2
        y0 = 0.40 * H
        for i, it in enumerate(items):
            r, cidx = divmod(i, cols)
            # last row centering when ragged
            in_row = min(cols, n - r * cols)
            rw = in_row * cw + (in_row - 1) * gx
            rx0 = (W - rw) / 2 + cw / 2
            cx = rx0 + cidx * (cw + gx)
            cy = y0 + r * (ch + gy)
            _grid_card(d, cx, cy, cw, ch, it, U)
    else:
        cw, ch = 0.80 * W, 0.09 * H
        gy = 0.022 * H
        y0 = 0.34 * H
        for i, it in enumerate(items):
            cy = y0 + i * (ch + gy)
            _grid_card(d, 0.5 * W, cy, cw, ch, it, U)

def _grid_card(d, cx, cy, cw, ch, it, U):
    rrect(d, [cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2], r=int(0.016 * U["W"]),
          fill=CARD, outline=BORDER, width=int(0.0022 * U["W"]))
    dot = int(0.006 * U["W"])
    lx = cx - cw / 2 + 0.045 * cw
    d.ellipse([lx, cy - dot, lx + 2 * dot, cy + dot], fill=INK_SOFT)
    tx = lx + 3 * dot
    d.text((tx, cy - ch * 0.16), it["tag"], font=U["f_tag"], fill=INK, anchor="lm")
    d.text((tx, cy + ch * 0.20), it["quote"], font=U["f_quote"], fill=INK_SOFT, anchor="lm")

def draw_example(d, c, U):
    W, H, port = U["W"], U["H"], U["port"]
    if not port:
        # two input tiles (image + text) -> hub -> answer
        tx = 0.15 * W
        img_y, txt_y = 0.42 * H, 0.60 * H
        tw_, th_ = 0.20 * W, 0.13 * H
        chip(d, tx, img_y, tw_, th_, c["input_image"], U)
        chip(d, tx, txt_y, tw_, th_, c["input_text"], U)
        hubx, huby = 0.44 * W, 0.51 * H
        for yy in (img_y, txt_y):
            arrow(d, tx + tw_ / 2, yy, hubx - 0.075 * W, huby + (yy - huby) * 0.3, INK_SOFT, U["aw"], U["ah"])
        rrect(d, [hubx - 0.075 * W, huby - 0.06 * H, hubx + 0.075 * W, huby + 0.06 * H],
              r=int(0.02 * W), fill=CARD, outline=BORDER, width=int(0.003 * W))
        center(d, hubx, huby, c["hub"], U["f_box"], INK)
        ax0 = hubx + 0.075 * W
        ansx, answ = 0.75 * W, 0.34 * W
        arrow(d, ax0, huby, ansx - answ / 2 - 0.01 * W, huby, SPARK, U["aw"], U["ah"])
        _answer(d, ansx, huby, answ, 0.26 * H, c["answer"], U)
    else:
        img_y, txt_y = 0.32 * H, 0.42 * H
        tw_, th_ = 0.70 * W, 0.075 * H
        chip(d, 0.5 * W, img_y, tw_, th_, c["input_image"], U)
        chip(d, 0.5 * W, txt_y, tw_, th_, c["input_text"], U)
        huby = 0.53 * H
        arrow(d, 0.5 * W, txt_y + th_ / 2, 0.5 * W, huby - 0.05 * H, INK_SOFT, U["aw"], U["ah"])
        rrect(d, [0.5 * W - 0.30 * W, huby - 0.045 * H, 0.5 * W + 0.30 * W, huby + 0.045 * H],
              r=int(0.02 * W), fill=CARD, outline=BORDER, width=int(0.003 * W))
        center(d, 0.5 * W, huby, c["hub"], U["f_box"], INK)
        ansy = 0.70 * H
        arrow(d, 0.5 * W, huby + 0.045 * H, 0.5 * W, ansy - 0.09 * H, SPARK, U["aw"], U["ah"])
        _answer(d, 0.5 * W, ansy, 0.80 * W, 0.14 * H, c["answer"], U)

def _answer(d, cx, cy, w, h, text, U):
    rrect(d, [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], r=int(0.018 * U["W"]),
          fill=CARD, outline=SPARK, width=int(0.005 * U["W"]))
    para(d, cx, cy - U["quote_lh"] * 0.5, text, U["f_answer"], INK, w * 0.86, U["quote_lh"])

def draw_versus(d, c, U):
    W, H, port = U["W"], U["H"], U["port"]
    y_note = 0.72 * H   # fixed for both panels so notes align and never collide with caption
    def panel(px, pw, title, flow, note, accent):
        col = SPARK if accent else INK_SOFT
        center(d, px, 0.355 * H, title, U["f_tag"], col)
        by = 0.42 * H
        bw, bh = pw * 0.80, 0.072 * H
        gap = 0.040 * H
        for i, step in enumerate(flow):
            cy = by + i * (bh + gap)
            oc = SPARK if (accent and i == len(flow) - 1) else BORDER
            rrect(d, [px - bw / 2, cy - bh / 2, px + bw / 2, cy + bh / 2], r=int(0.014 * W),
                  fill=CARD, outline=oc, width=int(0.004 * W) if oc == SPARK else int(0.0022 * W))
            center(d, px, cy, step, U["f_box"], INK)
            if i < len(flow) - 1:
                arrow(d, px, cy + bh / 2, px, cy + bh / 2 + gap - 0.006 * H, INK_SOFT, U["aw"], U["ah"])
        center(d, px, y_note, note, U["f_note"], col)
    if not port:
        panel(0.29 * W, 0.38 * W, c["left_title"], c["left_flow"], c["left_note"], False)
        # divider
        d.line([(0.5 * W, 0.36 * H), (0.5 * W, 0.74 * H)], fill=BORDER, width=int(0.002 * W))
        panel(0.71 * W, 0.38 * W, c["right_title"], c["right_flow"], c["right_note"], True)
    else:
        # portrait: stack, left top / right bottom — but keep side-by-side (PROOF wants side-by-side)
        panel(0.27 * W, 0.50 * W, c["left_title"], c["left_flow"], c["left_note"], False)
        d.line([(0.5 * W, 0.34 * H), (0.5 * W, 0.72 * H)], fill=BORDER, width=int(0.003 * W))
        panel(0.73 * W, 0.50 * W, c["right_title"], c["right_flow"], c["right_note"], True)

KINDS = {"flow": draw_flow, "grid": draw_grid, "example": draw_example,
         "versus": draw_versus, "loop": draw_loop}

# ── render one card ──────────────────────────────────────────────────────────
def render(beat, W, H, out_path):
    c = beat["shot"]["card"]
    port = H > W
    img = Image.new("RGB", (W, H), PAGE)
    d = ImageDraw.Draw(img)
    U = {
        "W": W, "H": H, "port": port,
        "f_title": font(SERIF_MED, 0.064 * W),
        "f_sub":   font(SERIF_ITAL, 0.024 * W),
        "f_cap":   font(SERIF_ITAL, 0.021 * W),
        "f_foot":  font(SANS, 0.0135 * W),
        "f_box":   font(SERIF_REG, 0.020 * W),
        "f_hub":   font(SERIF_MED, 0.026 * W),
        "f_small": font(SANS_REG, 0.0125 * W),
        "f_tag":   font(SANS, 0.017 * W),
        "f_quote": font(SERIF_ITAL, 0.019 * W),
        "f_answer": font(SERIF_ITAL, 0.019 * W),
        "f_note":  font(SERIF_ITAL, 0.017 * W),
        "aw": max(3, int(0.0028 * W)),
        "ah": int(0.016 * W),
        "quote_lh": int(0.030 * W),
    }
    # title + subtitle
    title_with_period(d, W / 2, 0.115 * H if not port else 0.085 * H, c["title"], U["f_title"])
    if c.get("subtitle"):
        center(d, W / 2, 0.195 * H if not port else 0.135 * H, c["subtitle"], U["f_sub"], INK_SOFT)
    # body
    KINDS[c["kind"]](d, c, U)
    # caption (wrapped) + footer
    if c.get("caption"):
        para(d, W / 2, 0.82 * H, c["caption"], U["f_cap"], INK_SOFT,
             W * (0.80 if not port else 0.86), int(0.028 * W))
    if c.get("footer"):
        tracked(d, W / 2, 0.925 * H, c["footer"].upper(), U["f_foot"], INK_SOFT, int(0.004 * W))
    # channel bug (lower-right, low-key wordmark)
    d.text((W - 0.055 * W, H - 0.045 * H), "@HumanitariansAI", font=U["f_foot"],
           fill=GHOST, anchor="rm")
    img.save(out_path)
    return out_path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aspect", default="16x9", choices=["16x9", "9x16"])
    ap.add_argument("--out", default="media")
    ap.add_argument("--sheet", default="beat_sheet.json")
    a = ap.parse_args()
    reel = Path(__file__).resolve().parent
    sheet = json.loads((reel / a.sheet).read_text())
    W, H = (3840, 2160) if a.aspect == "16x9" else (2160, 3840)
    outdir = reel / a.out
    outdir.mkdir(parents=True, exist_ok=True)
    made = []
    for b in sheet["beats"]:
        shot = b.get("shot", {})
        if shot.get("source") == "still" and "card" in shot:
            p = outdir / f"{b['beat_id']}.png"
            render(b, W, H, str(p))
            made.append(b["beat_id"])
    print(f"[cards] {a.aspect} -> {outdir}  rendered: {' '.join(made)}")

if __name__ == "__main__":
    main()
