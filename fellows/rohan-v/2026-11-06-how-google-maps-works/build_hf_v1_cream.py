"""Builds the HyperFrames compositions for "How Google Maps Works" (B01-B07), one root composition per beat and
aspect: hyperframes/B0x-l.html (3840x2160) and hyperframes/B0x-v.html (2160x3840).

Everything drawn comes from evidence/scene.json (maps.py) and the beat sheet: each beat's measured duration and
its word-clock cues (fractions written by sync_cues.py), so every reveal lands on the word that names it. One
visual system across the film: the same simulated city, the channel's Claude palette (cream page, warm ink, one
terracotta accent), Source Serif 4 + Inter, and three diegetic traffic colours.

    python build_hf.py            # writes the 14 compositions
    python build_hf.py --render   # also renders them: media/B0x.mp4 and pantry/B0x-916.mp4
"""
import json
import math
import subprocess
import sys
from pathlib import Path
from string import Template

import numpy as np

HERE = Path(__file__).resolve().parent
HF = HERE / "hyperframes"
sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
RES = json.loads((HERE / "evidence" / "results.json").read_text(encoding="utf-8"))
BEATS = {b["beat_id"]: b for b in sheet["beats"]}

PAGE, CARD, BORDER, INK, INK_SOFT, GHOST = "#FAF9F5", "#FFFFFF", "#E5E2D9", "#3D3929", "#73705F", "#A9A491"
SPARK, ACCENT = "#A9482B", "#D97757"
GREEN, AMBER, RED = "#4F9A62", "#E0A12E", "#C23B22"
BLUE = "#3B78D8"                                     # the position dot: diegetic, as on every map app
ROAD = {"local": ("#E8E3D7", 22), "avenue": ("#D8D1C0", 40), "highway": ("#C8BFA9", 66)}

SPARKS = {
    "B01": ("Four satellites: three for place, one for time.", "Three for place, one for time."),
    "B02": ("Photos, partners and people, read by AI.", "Photos and people, read by AI."),
    "B03": ("Same route, far fewer corners checked.", "Same route, fewer corners."),
    "B04": ("History knows the usual. Phones catch the crash.", "Phones catch the crash."),
    "B05": ("History plus live beats the speed limit.", "History plus live wins."),
    "B06": ("Counted, pooled, blurred, then shown.", "Counted, pooled, blurred."),
    "B07": ("A few answers predict the crowd.", "A few answers, a good guess."),
}
PTITLE = {"B01": "Satellites and a Clock", "B02": "How the Map Is Built", "B03": "Roads Become a Graph",
          "B04": "Traffic From Phones", "B05": "History Plus Live", "B06": "How Busy It Is",
          "B07": "How Full the Bus Is"}

# ------------------------------------------------------------------ city geometry
NODES = {k: tuple(v) for k, v in S["city"]["nodes"].items()}
EDGES = S["city"]["edges"]                 # from, to, class, true lv, history lv, 500-phone lv, 2000-phone lv
VB = (-200, -200, 5040, 5040)              # viewBox of every city map


def fmt(x):
    return f"{x:.0f}"


def city_svg(sid, roads=True, nodes=False, extra=""):
    """The city as SVG: roads by class (each segment its own element so traffic can recolour it)."""
    out = [f'<svg id="{sid}" viewBox="{" ".join(map(str, VB))}" class="map">',
           f'<rect x="{VB[0]}" y="{VB[1]}" width="{VB[2]}" height="{VB[3]}" rx="120" fill="{CARD}"/>']
    if roads:
        for cls in ("local", "avenue", "highway"):
            col, w = ROAD[cls]
            segs = []
            for k, (a, b, c, tl_, h, p5, p20) in enumerate(EDGES):
                if c != cls:
                    continue
                (x1, y1), (x2, y2) = NODES[a], NODES[b]
                segs.append(f'<line class="seg {sid}-s h{h} p{p5} t{tl_}" data-k="{k}" x1="{fmt(x1)}" y1="{fmt(y1)}" '
                            f'x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
            out.append(f'<g class="{sid}-{cls}">' + "".join(segs) + "</g>")
    if nodes:
        out.append(f'<g id="{sid}-nodes">' + "".join(
            f'<circle id="{sid}-n-{k.replace(",", "_")}" cx="{fmt(x)}" cy="{fmt(y)}" r="30" fill="{GHOST}" opacity="0"/>'
            for k, (x, y) in NODES.items()) + "</g>")
    out.append(extra)
    out.append("</svg>")
    return "".join(out)


def polyline(keys):
    return " ".join(f"{fmt(NODES[k][0])},{fmt(NODES[k][1])}" for k in keys)


def path_len(keys):
    return sum(math.dist(NODES[a], NODES[b]) for a, b in zip(keys, keys[1:]))


# ------------------------------------------------------------------ page frame
HEAD = Template("""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=$W, height=$H" />
<script src="assets/gsap.min.js"></script>
<style>
@font-face { font-family: "Source Serif 4"; src: url("assets/fonts/SourceSerif4.ttf") format("truetype"); font-weight: 200 900; font-style: normal; }
@font-face { font-family: "Source Serif 4"; src: url("assets/fonts/SourceSerif4-Italic.ttf") format("truetype"); font-weight: 200 900; font-style: italic; }
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: $PAGE; }
#root { position: relative; width: ${W}px; height: ${H}px; background: $PAGE; color: $INK;
  font-family: Inter, sans-serif; overflow: hidden; }
.abs { position: absolute; }
.serif { font-family: "Source Serif 4", serif; }
.caps { font-family: Inter, sans-serif; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; white-space: nowrap; }
.map { position: absolute; display: block; }
.card { position: absolute; background: $CARD; border: ${BW}px solid $BORDER; border-radius: ${RAD}px; }
.num { font-family: "Source Serif 4", serif; font-weight: 700; line-height: 1; font-variant-numeric: lining-nums tabular-nums; }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="$D" data-width="$W" data-height="$H">
<div id="stage" class="clip" data-start="0" data-duration="$D" data-track-index="0" data-layout-allow-overlap data-layout-allow-overflow
 style="position:absolute; inset:0;">
""")
FOOT = Template("""</div>
</div>
<script>
const tl = gsap.timeline({ paused: true });
const D = $D;
function q(s) { return document.querySelector(s); }
function qa(s) { return Array.from(document.querySelectorAll(s)); }
function inn(sel, t, dur, from) {
  tl.fromTo(sel, Object.assign({ opacity: 0, y: $RISE }, from || {}), { opacity: 1, y: 0, duration: dur || 0.6, ease: "power3.out" }, t);
}
function count(sel, to, t, dur, dec, suffix, pre) {
  const o = { v: 0 }, el = q(sel);
  const show = function () { el.textContent = (pre || "") + o.v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + (suffix || ""); };
  show();
  tl.to(o, { v: to, duration: dur || 1.0, ease: "power2.out", onUpdate: show }, t);
}
function draw(sel, t, dur, ease) {
  qa(sel).forEach(function (el) {
    const L = el.getTotalLength ? el.getTotalLength() : 1000;
    gsap.set(el, { strokeDasharray: L, strokeDashoffset: L });
    tl.to(el, { strokeDashoffset: 0, duration: dur || 1.0, ease: ease || "power2.inOut" }, t);
  });
}
$JS
// common: head, spark line, baseline
inn("#eyebrow", 0.05, 0.5); inn("#title", 0.12, 0.7);
tl.fromTo("#baseline", { opacity: 0 }, { opacity: 0.7, duration: 0.6 }, 0.1);
tl.fromTo("#spark", { opacity: 0, x: -$RISE }, { opacity: 1, x: 0, duration: 0.7, ease: "power3.out" }, $TSPARK);
tl.to({}, { duration: 0.01 }, D - 0.01);
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
""")


class Frame:
    def __init__(self, bid, portrait):
        self.bid, self.portrait = bid, portrait
        self.W, self.H = (2160, 3840) if portrait else (3840, 2160)
        self.u = self.W / 1080 if portrait else self.H / 1080          # 2.0 either way
        self.padx = self.W * (0.067 if portrait else 0.065)
        self.cw = self.W - 2 * self.padx
        b = BEATS[bid]
        self.D = round(b["actual_duration_s"], 3)
        self.cues = b["shot"]["remotion"]["props"].get("cues", {})
        self.title = PTITLE[bid] if portrait else b["shot"]["remotion"]["props"]["title"]
        self.parts, self.js = [], []
        u = self.u
        # sizes: landscape design units x u; portrait on the phone type scale (fractions of height)
        if portrait:
            H = self.H
            self.s_title, self.s_label, self.s_body, self.s_stat, self.s_spark = H * 0.05, H * 0.033 * 0.8, H * 0.04, H * 0.065, H * 0.034 * 1.25
        else:
            self.s_title, self.s_label, self.s_body, self.s_stat, self.s_spark = 56 * u, 24 * u, 42 * u, 104 * u, 30 * u

    def t(self, cue, default=0.0):
        return round(self.cues.get(cue, default) * self.D, 3)

    def add(self, html):
        self.parts.append(html)

    def anim(self, js):
        self.js.append(js)

    def head(self):
        u, p = self.u, self.portrait
        if not p:
            self.add(f'<div id="eyebrow" class="abs caps" style="left:{self.padx}px; top:{self.H * 0.085}px; font-size:{18 * u}px; '
                     f'color:{INK_SOFT}; letter-spacing:0.14em;">HUMANITARIANS AI · TECH CONCEPTS</div>')
            self.add(f'<div id="title" class="abs serif" style="left:{self.padx}px; top:{self.H * 0.115}px; font-size:{self.s_title}px; '
                     f'font-weight:600; color:{INK};">{self.title}</div>')
        else:
            self.add('<div id="eyebrow" class="abs" style="display:none"></div>')
            self.add(f'<div id="title" class="abs serif" style="left:{self.padx}px; top:{self.H * 0.075}px; font-size:{self.s_title}px; '
                     f'font-weight:600; color:{INK}; line-height:1.1;">{self.title}</div>')

    def foot(self):
        u, p = self.u, self.portrait
        txt = SPARKS[self.bid][1 if p else 0]
        if p:
            top, fs = self.H * 0.8, self.s_spark
            self.add(f'<div id="baseline" class="abs" style="left:{self.padx}px; top:{self.H * 0.782}px; width:{self.cw}px; height:{3 * u}px; background:{GHOST};"></div>')
        else:
            top, fs = self.H * 0.885, self.s_spark
            self.add(f'<div id="baseline" class="abs" style="left:{self.padx}px; top:{self.H * 0.85}px; width:{self.cw}px; height:{3 * u}px; background:{GHOST};"></div>')
        self.add(f'<div id="spark" class="abs" style="left:{self.padx}px; top:{top}px; display:flex; align-items:baseline; gap:{18 * u}px; width:{self.cw}px;">'
                 f'<span style="display:inline-block; width:{48 * u}px; height:{3 * u}px; background:{ACCENT}; transform:translateY(-{fs * 0.3}px);"></span>'
                 f'<span class="serif" style="font-style:italic; font-size:{fs}px; color:{INK}; line-height:1.2;">{txt}</span></div>')

    def html(self):
        last = max(self.cues.values()) if self.cues else 0.8
        tspark = round(min(max(last + 0.05, 0.62), 0.9) * self.D, 3)
        head = HEAD.substitute(W=self.W, H=self.H, D=self.D, PAGE=PAGE, INK=INK, BORDER=BORDER, CARD=CARD,
                               BW=round(1.5 * self.u, 1), RAD=round(16 * self.u))
        return head + "\n".join(self.parts) + FOOT.substitute(D=self.D, JS="\n".join(self.js), RISE=round(16 * self.u), TSPARK=tspark)


# ------------------------------------------------------------------ shared pieces
def map_box(f, frac_size=None):
    """Where the city map sits: left block in landscape, a centred square under the title on the phone."""
    if f.portrait:
        size = f.cw * 0.86 if frac_size is None else frac_size
        return (f.W - size) / 2, f.H * 0.16, size
    size = f.H * 0.62 if frac_size is None else frac_size
    return f.padx, f.H * 0.205, size


def right_col(f):
    """The text/stat column: right of the map in landscape, under it on the phone."""
    if f.portrait:
        x0, y0, s = map_box(f)
        return f.padx, y0 + s + f.H * 0.025, f.cw
    x0, y0, s = map_box(f)
    x = x0 + s + f.W * 0.045
    return x, f.H * 0.215, f.W - f.padx - x


def label(f, lid, text, x, y, color=INK_SOFT, size=None, extra=""):
    f.add(f'<div id="{lid}" class="abs caps" style="left:{x}px; top:{y}px; font-size:{size or f.s_label}px; color:{color}; {extra}">{text}</div>')


def stat(f, sid, x, y, value_html, lab, color=INK, size=None, labw=None):
    s = size or f.s_stat
    f.add(f'<div id="{sid}" class="abs" style="left:{x}px; top:{y}px;">'
          f'<div id="{sid}-v" class="num" style="font-size:{s}px; color:{color};">{value_html}</div>'
          f'<div class="caps" style="font-size:{f.s_label}px; color:{INK_SOFT}; margin-top:{s * 0.14}px; '
          f'{"white-space:normal; width:" + str(labw) + "px; line-height:1.3;" if labw else ""}">{lab}</div></div>')


def gtag(f, gid, text, x, y, size=None):
    """LOGO LAW: Google's own mark beside its name."""
    s = size or f.s_label
    f.add(f'<div id="{gid}" class="abs" style="left:{x}px; top:{y}px; display:flex; align-items:center; gap:{s * 0.45}px;">'
          f'<img src="assets/google-01.svg" style="width:{s * 1.7}px; height:{s * 1.7}px;" />'
          f'<span class="caps" style="font-size:{s}px; color:{INK};">{text}</span></div>')


def svg_place(f, inner_svg, x, y, size, sid):
    f.add(f'<div id="{sid}-wrap" class="abs" style="left:{x}px; top:{y}px; width:{size}px; height:{size}px;">'
          + inner_svg.replace('class="map">', f'class="map" style="width:{size}px; height:{size}px; left:0; top:0;">', 1) + "</div>")


# ================================================================== B01 · where am I
def b01(f):
    u = f.u
    g = S["gps"]
    sats = g["sats"]
    # sky panel: horizon at the bottom, the phone in the middle, satellites placed by azimuth/elevation (side view)
    if f.portrait:
        px, py, pw, ph = f.padx, f.H * 0.16, f.cw, f.H * 0.3
    else:
        px, py, pw, ph = f.padx, f.H * 0.205, f.W * 0.5, f.H * 0.6
    hz = ph * 0.84
    cx = pw / 2
    R = min(pw * 0.46, hz * 0.95)
    order = sorted(range(len(sats)), key=lambda i: -sats[i][1])[:8]
    pos = []
    for i in order:
        az, el = math.radians(sats[i][0]), math.radians(sats[i][1])
        pos.append((cx + R * math.cos(el) * math.sin(az), hz - R * math.sin(el) * 0.92 - 40 * u))
    sk = [f'<svg id="sky" class="map" viewBox="0 0 {pw} {ph}" style="left:{px}px; top:{py}px; width:{pw}px; height:{ph}px;">',
          f'<rect x="0" y="0" width="{pw}" height="{ph}" rx="{16 * u}" fill="{CARD}" stroke="{BORDER}" stroke-width="{1.5 * u}"/>',
          f'<path d="M {cx - R} {hz} A {R} {R * 0.92} 0 0 1 {cx + R} {hz}" fill="none" stroke="{BORDER}" stroke-width="{3 * u}" stroke-dasharray="{10 * u} {10 * u}"/>',
          f'<line x1="{30 * u}" y1="{hz}" x2="{pw - 30 * u}" y2="{hz}" stroke="{GHOST}" stroke-width="{3 * u}"/>']
    for k, (x, y) in enumerate(pos):
        col = SPARK if k < 3 else INK
        sk.append(f'<line id="ray{k}" x1="{x}" y1="{y}" x2="{cx}" y2="{hz}" stroke="{col}" stroke-width="{4 * u}" '
                  f'stroke-dasharray="{14 * u} {10 * u}" opacity="0"/>')
    for k, (x, y) in enumerate(pos):
        s = 26 * u
        sk.append(f'<g id="sat{k}" opacity="0" transform="translate({x} {y})">'
                  f'<rect x="{-s * 1.7}" y="{-s * 0.28}" width="{s * 1.1}" height="{s * 0.56}" fill="{INK_SOFT}" rx="{2 * u}"/>'
                  f'<rect x="{s * 0.6}" y="{-s * 0.28}" width="{s * 1.1}" height="{s * 0.56}" fill="{INK_SOFT}" rx="{2 * u}"/>'
                  f'<rect x="{-s * 0.5}" y="{-s * 0.5}" width="{s}" height="{s}" fill="{INK}" rx="{4 * u}"/></g>')
    # the 4th satellite carries a clock
    cxk, cyk = pos[3]
    sk.append(f'<g id="clock" opacity="0" transform="translate({cxk + 56 * u} {cyk - 30 * u})">'
              f'<circle r="{24 * u}" fill="{CARD}" stroke="{INK}" stroke-width="{4 * u}"/>'
              f'<line id="hand" x1="0" y1="0" x2="0" y2="{-16 * u}" stroke="{SPARK}" stroke-width="{4 * u}" stroke-linecap="round"/>'
              f'<line x1="0" y1="0" x2="{11 * u}" y2="0" stroke="{INK}" stroke-width="{4 * u}" stroke-linecap="round"/></g>')
    sk.append(f'<circle id="halo" cx="{cx}" cy="{hz}" r="{20 * u}" fill="{BLUE}" fill-opacity="0.16" stroke="{BLUE}" stroke-opacity="0.5" stroke-width="{2 * u}" opacity="0"/>')
    sk.append(f'<circle id="dot" cx="{cx}" cy="{hz}" r="{14 * u}" fill="{BLUE}" stroke="{CARD}" stroke-width="{5 * u}"/>')
    sk.append("</svg>")
    f.add("".join(sk))
    lab_y = py + ph + 14 * u
    label(f, "skylab", "ILLUSTRATION · RANGES FROM EACH SATELLITE TO YOUR PHONE" if not f.portrait else "RANGES TO YOUR PHONE", px, lab_y, size=f.s_label * (0.8 if not f.portrait else 1))
    # right column / below: the clock number and the two measured circles
    x, y, w = (f.padx, f.H * 0.505, f.cw) if f.portrait else (f.padx + f.W * 0.5 + f.W * 0.04, f.H * 0.215, f.W * 0.94 - f.padx - f.W * 0.54)
    stat(f, "ms", x, y, f'1 ms = {g["clock_km"]} km', "A CLOCK 1 MS OFF, AS DISTANCE", color=SPARK,
         size=f.s_stat * (0.85 if f.portrait else 0.9))
    cy0 = y + (f.H * 0.085 if f.portrait else f.H * 0.2)
    cw = (w - 40 * u) / 2
    ch = f.H * (0.17 if f.portrait else 0.36)
    for k, (cid, lab, val, rpx) in enumerate((("open", "OPEN SKY", g["open_med"], 14), ("tall", "TALL BUILDINGS", g["canyon_med"], 0))):
        cx2 = x + k * (cw + 40 * u)
        inner = [f'<svg class="map" viewBox="0 0 {cw} {ch}" style="left:0; top:0; width:{cw}px; height:{ch}px;">',
                 f'<rect x="0" y="0" width="{cw}" height="{ch}" rx="{16 * u}" fill="{CARD}" stroke="{BORDER}" stroke-width="{1.5 * u}"/>']
        mx, my = cw / 2, ch * 0.5
        if cid == "tall":
            for bx, bw_, bh in ((0.08, 0.2, 0.55), (0.3, 0.14, 0.8), (0.62, 0.16, 0.7), (0.8, 0.13, 0.5)):
                inner.append(f'<rect x="{cw * bx}" y="{ch * (0.92 - bh)}" width="{cw * bw_}" height="{ch * bh}" fill="#EEEAE0" rx="{4 * u}"/>')
        # circle radius proportional to measured median error (scaled so 69 m nearly fills the card)
        scale = (min(cw, ch) * 0.42) / max(g["canyon_med"], 1)
        r = max(val * scale, 16 * u)
        inner.append(f'<circle id="{cid}-c" cx="{mx}" cy="{my}" r="{r}" fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-opacity="0.55" stroke-width="{3 * u}"/>')
        inner.append(f'<circle cx="{mx}" cy="{my}" r="{12 * u}" fill="{BLUE}" stroke="{CARD}" stroke-width="{4 * u}"/>')
        inner.append("</svg>")
        f.add(f'<div id="{cid}" class="abs" style="left:{cx2}px; top:{cy0}px; width:{cw}px; height:{ch}px;">' + "".join(inner) + "</div>")
        f.add(f'<div id="{cid}-t" class="abs" style="left:{cx2}px; top:{cy0 + ch + 16 * u}px;">'
              f'<div class="num" style="font-size:{f.s_stat * 0.62}px; color:{INK};">≈ {val:.0f} m</div>'
              f'<div class="caps" style="font-size:{f.s_label}px; color:{INK_SOFT}; margin-top:{8 * u}px;">{lab}</div></div>')
    label(f, "simlab", "MY SIMULATION · MEDIAN ERROR", x, cy0 - f.s_label * 1.9, color=INK)
    f.anim(Template("""
qa("#sky").forEach(function(e){ tl.fromTo(e, {opacity:0}, {opacity:1, duration:0.6}, 0.2); });
inn("#skylab", $tw, 0.5);
for (let k = 0; k < 8; k++) { tl.fromTo("#sat" + k, {opacity:0, y:-20}, {opacity:1, y:0, duration:0.5, ease:"back.out(2)"}, $tw + 0.08 * k); }
for (let k = 0; k < 4; k++) { tl.fromTo("#ray" + k, {opacity:0}, {opacity:1, duration:0.4}, $tf + 0.15 * k); }
for (let k = 4; k < 8; k++) { tl.to("#sat" + k, {opacity:0.35, duration:0.4}, $tf); }
for (let k = 0; k < 3; k++) { tl.to("#ray" + k, {strokeWidth: $thick, duration:0.4}, $tt + 0.1 * k); }
tl.fromTo("#clock", {opacity:0, scale:0.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.5, ease:"back.out(2)"}, $tc);
tl.fromTo("#hand", {rotation:0, svgOrigin:"0 0"}, {rotation:720, svgOrigin:"0 0", duration:3, ease:"power1.inOut"}, $tc);
inn("#ms", $tm, 0.7);
inn("#simlab", $to, 0.5);
inn("#open", $to, 0.6); inn("#open-t", $to + 0.15, 0.6);
tl.fromTo("#open-c", {attr:{r:4}}, {attr:{r:$ropen}, duration:0.9, ease:"power3.out"}, $to + 0.2);
inn("#tall", $tb, 0.6); inn("#tall-t", $tb + 0.15, 0.6);
tl.fromTo("#tall-c", {attr:{r:4}}, {attr:{r:$rtall}, duration:1.1, ease:"power3.out"}, $tb + 0.2);
tl.fromTo("#halo", {opacity:0, attr:{r:$h0}}, {opacity:1, attr:{r:$h1}, duration:1.2, ease:"power2.out"}, $tci);
tl.to("#halo", {attr:{r:$h2}, duration:1.2, ease:"sine.inOut", yoyo:true, repeat:1}, $tci + 1.2);
""").substitute(tw=f.t("where", 0.02), tf=f.t("four"), tt=f.t("three"), tc=f.t("clock"), tm=f.t("milli"),
                to=f.t("open"), tb=f.t("tall"), tci=f.t("circle"), thick=round(7 * u, 1),
                ropen=round(max(g["open_med"] * (min(cw, ch) * 0.42) / g["canyon_med"], 16 * u), 1),
                rtall=round(min(cw, ch) * 0.42, 1), h0=round(16 * u), h1=round(90 * u), h2=round(120 * u)))


# ================================================================== B02 · the map is built
def b02(f):
    u = f.u
    if f.portrait:
        ox, oy, size = f.W * 0.5, f.H * 0.33, f.cw * 0.62
    else:
        ox, oy, size = f.padx + f.W * 0.24, f.H * 0.53, f.H * 0.5
    layers = [("street", "STREET VIEW CARS"), ("photo", "SATELLITE AND AERIAL PHOTOS"), ("roads", "DATA PARTNERS"), ("edits", "PEOPLE'S EDITS")]
    rng = np.random.default_rng(3)
    gap = size * 0.2
    for k, (lid, lab) in enumerate(layers):
        inner = [f'<svg class="map" viewBox="{" ".join(map(str, VB))}" style="left:0; top:0; width:{size}px; height:{size}px;">',
                 f'<rect x="{VB[0]}" y="{VB[1]}" width="{VB[2]}" height="{VB[3]}" rx="140" fill="{CARD}" fill-opacity="0.94" stroke="{BORDER}" stroke-width="24"/>']
        if lid == "photo":
            for _ in range(160):
                x, y = rng.uniform(0, 4600, 2)
                w_, h_ = rng.uniform(120, 360, 2)
                inner.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{w_:.0f}" height="{h_:.0f}" fill="#D9D3C4" opacity="{rng.uniform(0.35, 0.8):.2f}" rx="20"/>')
        if lid == "roads":
            for a, b, c, *_ in EDGES:
                if c != "local":
                    (x1, y1), (x2, y2) = NODES[a], NODES[b]
                    inner.append(f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="{ROAD[c][0]}" stroke-width="{ROAD[c][1] * 1.4}"/>')
        if lid == "street":
            row = [k2 for k2 in NODES if k2.split(",")[1] == "15"]
            inner.append(f'<polyline points="{polyline(sorted(row, key=lambda s: int(s.split(",")[0])))}" fill="none" stroke="{ROAD["avenue"][0]}" stroke-width="60"/>')
            for i in range(6):
                x, y = NODES[f"{4 + 4 * i},15"]
                inner.append(f'<circle class="svcar" cx="{fmt(x)}" cy="{fmt(y)}" r="70" fill="{SPARK}"/>')
        if lid == "edits":
            for i in range(7):
                x, y = rng.uniform(400, 4300, 2)
                inner.append(f'<g class="pin" transform="translate({x:.0f} {y:.0f})"><path d="M0 0 C -140 -170 -140 -330 0 -330 C 140 -330 140 -170 0 0 Z" fill="{ACCENT}"/>'
                             f'<circle cy="-230" r="55" fill="{CARD}"/></g>')
        inner.append("</svg>")
        z = oy - k * gap
        f.add(f'<div class="abs" style="left:{ox - size / 2}px; top:{z - size / 2}px; width:{size}px; height:{size}px; '
              f'transform: perspective({6000 * u}px) rotateX(58deg) rotateZ(-38deg); transform-style:preserve-3d;">'
              f'<div id="ly-{lid}" style="position:absolute; inset:0;">' + "".join(inner) + "</div></div>")
    # labels in a column, each tied to its layer
    lx = f.padx if f.portrait else f.padx + f.W * 0.47
    ly0 = f.H * 0.5 if f.portrait else f.H * 0.22
    step = f.s_label * 2.0
    for k, (lid, lab) in enumerate(reversed(layers)):
        kk = len(layers) - 1 - k
        f.add(f'<div id="lb-{layers[kk][0]}" class="abs caps" style="left:{lx}px; top:{ly0 + k * step}px; font-size:{f.s_label}px; color:{INK}; display:flex; align-items:center; gap:{14 * u}px;">'
              f'<span style="display:inline-block; width:{22 * u}px; height:{22 * u}px; border-radius:{6 * u}px; background:{[SPARK, "#D9D3C4", ROAD["highway"][0], ACCENT][kk]};"></span>{layers[kk][1]}</div>')
    # AI reading a house number
    ax, ay = (f.padx, f.H * 0.5 + 5 * step) if f.portrait else (lx, f.H * 0.22 + 4.6 * step)
    aw, ah = (f.cw * 0.56, f.H * 0.09) if f.portrait else (f.W * 0.22, f.H * 0.2)
    f.add(f'<div id="ai" class="card" style="left:{ax}px; top:{ay}px; width:{aw}px; height:{ah}px; overflow:hidden;">'
          f'<div style="position:absolute; left:{aw * 0.12}px; top:{ah * 0.2}px; width:{aw * 0.42}px; height:{ah * 0.6}px; background:#2F4A6B; border-radius:{8 * u}px; '
          f'display:flex; align-items:center; justify-content:center;"><span class="num" style="color:#F4F1EA; font-size:{ah * 0.36}px;">1106</span></div>'
          f'<div id="scan" style="position:absolute; left:{aw * 0.08}px; top:{ah * 0.12}px; width:{aw * 0.5}px; height:{ah * 0.76}px; border:{4 * u}px solid {SPARK}; border-radius:{8 * u}px;"></div>'
          f'<div class="caps" style="position:absolute; left:{aw * 0.62}px; top:{ah * 0.34}px; font-size:{f.s_label * 0.9}px; color:{SPARK}; white-space:normal; width:{aw * 0.36}px; line-height:1.3;">AI READS: 1106</div></div>')
    label(f, "ailab", "AI READS SIGNS AND HOUSE NUMBERS", ax, ay - f.s_label * 1.8, color=INK_SOFT)
    sx, sy = (f.padx + f.cw * 0.6, ay - f.s_label * 1.8) if f.portrait else (lx, ay + ah + f.H * 0.05)
    stat(f, "bil", sx, sy, "2 billion+", "PEOPLE A MONTH (2025)", size=f.s_stat * (0.62 if f.portrait else 0.85))
    gtag(f, "gmaps", "GOOGLE MAPS", f.padx if f.portrait else lx, (f.H * 0.47 if f.portrait else f.H * 0.215 - f.s_label * 2.6))
    f.anim(Template("""
const L = ["street", "photo", "roads", "edits"], T = [$t1, $t2, $t3, $t3 + 0.9];
const T4 = [$t1, $t2, $t3, $t4];
L.forEach(function (l, k) {
  tl.fromTo("#ly-" + l, {opacity:0, y:-$drop}, {opacity:1, y:0, duration:0.8, ease:"power3.out"}, T4[k]);
  tl.fromTo("#lb-" + l, {opacity:0, x:-$rise}, {opacity:1, x:0, duration:0.5, ease:"power3.out"}, T4[k] + 0.1);
});
tl.fromTo(".svcar", {opacity:0}, {opacity:1, duration:0.3, stagger:0.08}, $t1 + 0.4);
tl.fromTo(".pin", {opacity:0, y:-120}, {opacity:1, y:0, duration:0.5, stagger:0.07, ease:"back.out(2)"}, $t4 + 0.3);
inn("#gmaps", 0.4, 0.6);
inn("#ailab", $tai, 0.5); inn("#ai", $tai, 0.6);
tl.fromTo("#scan", {opacity:0, scale:1.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.6, ease:"power3.out"}, $tai + 0.4);
inn("#bil", $tb, 0.7);
""").substitute(t1=f.t("street"), t2=f.t("photos"), t3=f.t("photos") + 0.9, t4=f.t("edits"), tai=f.t("ai"), tb=f.t("billion"),
                drop=round(220 * u), rise=round(16 * u)))


# ================================================================== B03 · routing
def b03(f):
    u = f.u
    c = S["city"]
    x0, y0, size = map_box(f)
    rpts = polyline(c["route"])
    sx, sy = NODES[c["src"]]
    dx, dy = NODES[c["dst"]]
    extra = (f'<polyline id="route" points="{rpts}" fill="none" stroke="{SPARK}" stroke-width="64" stroke-linejoin="round" stroke-linecap="round"/>'
             f'<circle id="src" cx="{fmt(sx)}" cy="{fmt(sy)}" r="80" fill="{CARD}" stroke="{INK}" stroke-width="30"/>'
             f'<g id="dst" transform="translate({fmt(dx)} {fmt(dy)})"><path d="M0 0 C -150 -180 -150 -350 0 -350 C 150 -350 150 -180 0 0 Z" fill="{SPARK}"/>'
             f'<circle cy="-240" r="60" fill="{CARD}"/></g>')
    svg_place(f, city_svg("rmap", nodes=True, extra=extra), x0, y0, size, "rmap")
    x, y, w = right_col(f)
    gap = f.H * (0.11 if f.portrait else 0.16)
    if f.portrait:
        stat(f, "dj", x, y, '<span id="dj-n">0</span>', "DIJKSTRA · CORNERS CHECKED", size=f.s_stat * 0.85)
        stat(f, "as", x + w * 0.52, y, '<span id="as-n">0</span>', "A-STAR · CORNERS CHECKED", color=SPARK, size=f.s_stat * 0.85)
        stat(f, "rt", x, y + gap, f'{c["route_min"]:.1f} min', "SAME ROUTE, BOTH WAYS", size=f.s_stat * 0.62)
        gtag(f, "recipe", "GOOGLE DOESN'T PUBLISH ITS RECIPE", x, y + gap * 1.9)
    else:
        label(f, "corners", f"MY CITY · {len(NODES)} CORNERS", x, y, color=INK)
        stat(f, "dj", x, y + gap * 0.4, '<span id="dj-n">0</span>', "DIJKSTRA · CORNERS CHECKED")
        stat(f, "as", x, y + gap * 1.45, '<span id="as-n">0</span>', "A-STAR · AIMS AT THE DESTINATION", color=SPARK)
        stat(f, "rt", x, y + gap * 2.5, f'{c["route_min"]:.1f} min', "SAME ROUTE, BOTH WAYS", size=f.s_stat * 0.62)
        gtag(f, "recipe", "GOOGLE DOESN'T PUBLISH ITS RECIPE", x, y + gap * 3.35)
    dj = json.dumps([k.replace(",", "_") for k in c["dijkstra"]])
    ast = json.dumps([k.replace(",", "_") for k in c["astar"]])
    f.anim(Template("""
tl.fromTo("#rmap-wrap", {opacity:0, scale:0.97, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.8, ease:"power3.out"}, 0.15);
tl.fromTo("#rmap-nodes circle", {opacity:0}, {opacity:0.55, duration:0.01, stagger:{each:0.0012, from:"random"}}, $tc);
qa("#route").forEach(function(e){ gsap.set(e, {opacity:0}); });
gsap.set(["#src", "#dst"], {opacity:0});
tl.to(["#src", "#dst"], {opacity:1, duration:0.4}, $tc + 0.6);
if (q("#corners")) inn("#corners", $tb, 0.5);
const DJ = $dj, AS = $ast;
const djDur = Math.max(1.2, $ta - $td - 0.5), asDur = Math.max(1.0, $ts - $ta - 0.3);
DJ.forEach(function (k, i) { tl.to("#rmap-n-" + k, {opacity:1, fill:"$ink_soft", attr:{r:46}, duration:0.12}, $td + djDur * i / DJ.length); });
inn("#dj", $td, 0.5); count("#dj-n", DJ.length, $td, djDur, 0);
DJ.forEach(function (k) { tl.to("#rmap-n-" + k, {fill:"#D3CBB8", attr:{r:34}, duration:0.4}, $ta - 0.25); });
AS.forEach(function (k, i) { tl.to("#rmap-n-" + k, {opacity:1, fill:"$accent", attr:{r:46}, duration:0.12}, $ta + asDur * i / AS.length); });
inn("#as", $ta, 0.5); count("#as-n", AS.length, $ta, asDur, 0);
tl.set("#route", {opacity:1}, $ts);
draw("#route", $ts, 1.4, "power2.inOut");
inn("#rt", $ts + 0.4, 0.6);
inn("#recipe", $tr, 0.6);
""").substitute(tc=f.t("corners"), tb=f.t("built"), td=f.t("dijkstra"), ta=f.t("astar"), ts=f.t("same"), tr=f.t("recipe"),
                dj=dj, ast=ast, ink_soft=INK_SOFT, ghost=GHOST, accent=ACCENT))


# ================================================================== B04 · traffic
def b04(f):
    u = f.u
    c = S["city"]
    x0, y0, size = map_box(f)
    # crash marker at the middle of the crash segments
    crash = c["crash"]
    pts = [NODES[k] for e in crash for k in e.split("|")]
    mx, my = np.mean([p[0] for p in pts]), np.mean([p[1] for p in pts])
    rng = np.random.default_rng(11)
    phones = []
    for i in range(70):
        horiz = rng.random() < 0.5
        line = int(rng.integers(0, 30))
        a, b = (f"0,{line}", f"29,{line}") if horiz else (f"{line},0", f"{line},29")
        if a not in NODES or b not in NODES:
            continue
        if rng.random() < 0.5:
            a, b = b, a
        phones.append((NODES[a], NODES[b], float(rng.uniform(0, 1))))
    extra = [f'<g id="phones">']
    for k, ((ax, ay), (bx, by), off) in enumerate(phones):
        extra.append(f'<circle id="ph{k}" cx="{fmt(ax)}" cy="{fmt(ay)}" r="44" fill="{BLUE}" stroke="{CARD}" stroke-width="14" opacity="0"/>')
    extra.append("</g>")
    extra.append(f'<g id="crash" transform="translate({mx:.0f} {my:.0f})" opacity="0"><circle r="260" fill="none" stroke="{RED}" stroke-width="26" stroke-dasharray="60 40"/>'
                 f'<path d="M0 -150 L 140 110 L -140 110 Z" fill="{RED}"/><rect x="-16" y="-70" width="32" height="110" rx="10" fill="{CARD}"/>'
                 f'<circle cy="78" r="18" fill="{CARD}"/></g>')
    svg_place(f, city_svg("tmap", extra="".join(extra)), x0, y0, size, "tmap")
    x, y, w = right_col(f)
    r = RES["traffic"]
    hist = next(t for t in r if t["phones"] == 0)
    p5 = next(t for t in r if t["phones"] == 500)
    if f.portrait:
        label(f, "since", "SINCE 2009 · ANONYMOUS SPEEDS FROM PHONES", x, y, color=INK)
        stat(f, "hist", x, y + f.H * 0.035, f'{hist["colour_right"] * 100:.0f}%', "ROADS RIGHT FROM HISTORY ALONE", size=f.s_stat * 0.8)
        stat(f, "p500", x + w * 0.52, y + f.H * 0.035, "500", "PHONES TURN THE CRASH RED", color=RED, size=f.s_stat * 0.8)
    else:
        label(f, "since", "SINCE 2009 · ANONYMOUS SPEEDS", x, y, color=INK)
        stat(f, "hist", x, y + f.H * 0.07, f'{hist["colour_right"] * 100:.0f}%', "ROADS COLOURED RIGHT FROM HISTORY ALONE", labw=w)
        stat(f, "miss", x, y + f.H * 0.29, "0%", "OF THE CRASH SHOWN, HISTORY ALONE", color=INK_SOFT, size=f.s_stat * 0.62, labw=w)
        stat(f, "p500", x, y + f.H * 0.45, "500 phones", f'CRASH RED ON {p5["crash_red"] * 100:.0f}% OF ITS ROADS', color=RED, size=f.s_stat * 0.72, labw=w)
    # legend chips
    lgx, lgy = (x, y + f.H * 0.13) if f.portrait else (x0, y0 + size + 16 * u)
    f.add(f'<div id="legend" class="abs caps" style="left:{lgx}px; top:{lgy}px; font-size:{f.s_label * (1 if f.portrait else 0.8)}px; color:{INK_SOFT}; display:flex; gap:{26 * u}px;">'
          + "".join(f'<span style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{34 * u}px; height:{10 * u}px; border-radius:{5 * u}px; background:{col};"></span>{t}</span>'
                    for col, t in ((GREEN, "MOVING"), (AMBER, "SLOW"), (RED, "JAMMED"))) + "</div>")
    js_ph = json.dumps([[a[0], a[1], b[0], b[1], o] for a, b, o in phones])
    f.add("")
    f.anim(Template("""
tl.fromTo("#tmap-wrap", {opacity:0}, {opacity:1, duration:0.7}, 0.15);
const PH = $ph;
PH.forEach(function (p, k) {
  const el = q("#ph" + k), o = { s: p[4] };
  const put = function () { const s = o.s % 1; el.setAttribute("cx", p[0] + (p[2] - p[0]) * s); el.setAttribute("cy", p[1] + (p[3] - p[1]) * s); };
  put();
  tl.to(el, {opacity:0.95, duration:0.3}, $tp + 0.01 * k);
  tl.to(o, {s: p[4] + 1.6, duration: D - $tp, ease:"none", onUpdate: put}, $tp);
});
inn("#since", $ts, 0.5);
const COL = ["$green", "$amber", "$red"];
[0, 1, 2].forEach(function (lv) {
  tl.to(".tmap-s.h" + lv, {stroke: COL[lv], duration:0.6, stagger:{each:0.0007, from:"center"}}, $tu);
});
inn("#legend", $tu + 0.3, 0.5);
inn("#hist", $th, 0.6);
tl.fromTo("#crash", {opacity:0, scale:0.5, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.5, ease:"back.out(2.2)"}, $tc);
if (q("#miss")) inn("#miss", $tc + 0.3, 0.5);
inn("#p500", $tf, 0.6);
[0, 1, 2].forEach(function (lv) { tl.to(".tmap-s.p" + lv, {stroke: COL[lv], duration:0.5}, $tr); });
tl.to("#crash", {scale:1.15, duration:0.35, yoyo:true, repeat:1, transformOrigin:"50% 50%"}, $tr);
""").substitute(ph=js_ph, tp=f.t("phones"), ts=f.t("since"), tu=f.t("usually"), th=f.t("history"), tc=f.t("crash"),
                tf=f.t("five"), tr=f.t("red"), green=GREEN, amber=AMBER, red=RED))


# ================================================================== B05 · arrival time
def b05(f):
    u = f.u
    ex = S["city"]["eta_example"]
    x0, y0, size = map_box(f)
    pts = [NODES[k] for k in ex["path"]]
    extra = (f'<polyline id="trip" points="{polyline(ex["path"])}" fill="none" stroke="{SPARK}" stroke-width="58" stroke-linejoin="round" stroke-linecap="round"/>'
             f'<circle id="car" cx="{fmt(pts[0][0])}" cy="{fmt(pts[0][1])}" r="70" fill="{BLUE}" stroke="{CARD}" stroke-width="20"/>')
    svg_place(f, city_svg("emap", extra=extra), x0, y0, size, "emap")
    x, y, w = right_col(f)
    rows = [("act", "ACTUAL TRIP", ex["actual"], INK), ("lim", "SPEED LIMITS SAID", ex["limits"], GHOST), ("both", "HISTORY + LIVE SAID", ex["both"], SPARK)]
    mx = max(r_[2] for r_ in rows) * 1.08
    bh = f.s_label * (1.6 if f.portrait else 1.5)
    gapr = bh * (3.0 if f.portrait else 2.9)
    bw = w * (0.62 if f.portrait else 0.6)
    label(f, "one", "ONE RUSH-HOUR TRIP", x, y, color=INK)
    for k, (rid, lab, mins, col) in enumerate(rows):
        yy = y + f.s_label * 2.2 + k * gapr
        f.add(f'<div id="{rid}" class="abs" style="left:{x}px; top:{yy}px; width:{w}px;">'
              f'<div class="caps" style="font-size:{f.s_label}px; color:{INK_SOFT};">{lab}</div>'
              f'<div style="display:flex; align-items:center; gap:{18 * u}px; margin-top:{10 * u}px;">'
              f'<div id="{rid}-bar" style="height:{bh}px; width:{bw * mins / mx}px; background:{col}; border-radius:{bh / 2}px;"></div>'
              f'<span class="num" style="font-size:{bh * 1.25}px; color:{col if col != GHOST else INK_SOFT};">{mins:.1f} min</span></div></div>')
    e = RES["eta"]
    yy = y + f.s_label * 2.2 + 3 * gapr + f.H * 0.01
    label(f, "all", f"ALL {237} TRIPS · TYPICAL ERROR", x, yy, color=INK)
    stat(f, "elim", x, yy + f.s_label * 1.9, f'{e["limits"]["median"] * 100:.0f}%', "SPEED LIMITS", color=INK_SOFT, size=f.s_stat * 0.7)
    stat(f, "eboth", x + w * 0.42, yy + f.s_label * 1.9, f'{e["both"]["median"] * 100:.0f}%', "HISTORY + LIVE", color=SPARK, size=f.s_stat * 0.7)
    gy = yy + f.s_label * 1.9 + f.s_stat * 0.7 + f.s_label * 3.2
    gtag(f, "g97", "GOOGLE: ACCURATE FOR OVER 97% OF TRIPS (2020)", x, gy)
    pj = json.dumps([[round(p[0]), round(p[1])] for p in pts])
    f.anim(Template("""
tl.fromTo("#emap-wrap", {opacity:0}, {opacity:1, duration:0.7}, 0.15);
draw("#trip", 0.5, 1.2);
inn("#one", 0.6, 0.5);
const P = $pts, car = q("#car"), o = { s: 0 };
const cum = [0]; for (let i = 1; i < P.length; i++) cum.push(cum[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
const put = function () { const d = o.s * cum[cum.length - 1]; let i = 1; while (i < cum.length - 1 && cum[i] < d) i++;
  const f2 = (d - cum[i - 1]) / Math.max(1, cum[i] - cum[i - 1]);
  car.setAttribute("cx", P[i - 1][0] + (P[i][0] - P[i - 1][0]) * f2); car.setAttribute("cy", P[i - 1][1] + (P[i][1] - P[i - 1][1]) * f2); };
put();
tl.to(o, {s:1, duration: D - 1.6, ease:"sine.inOut", onUpdate: put}, 1.2);
["act", "lim", "both"].forEach(function (r, k) {
  const t0 = [$tb, $tl, $tv][k];
  inn("#" + r, t0, 0.5);
  tl.fromTo("#" + r + "-bar", {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:0.9, ease:"power3.out"}, t0 + 0.1);
});
inn("#all", $tl + 0.6, 0.5); inn("#elim", $tl + 0.8, 0.6); inn("#eboth", $tv + 0.3, 0.6);
inn("#g97", $tg, 0.6);
""").substitute(pts=pj, tb=f.t("both"), tl=f.t("limits"), tv=f.t("live"), tg=f.t("google")))


# ================================================================== B06 · how busy
def b06(f):
    u = f.u
    b = S["busy"]
    # left/top: a dot field of visitors (100 dots = all visitors; a quarter lit = counted)
    if f.portrait:
        gx, gy, gw = f.padx, f.H * 0.17, f.cw * 0.42
        cx, cy, cwid, chh = f.padx, f.H * 0.47, f.cw, f.H * 0.2
    else:
        gx, gy, gw = f.padx, f.H * 0.25, f.W * 0.24
        cx, cy, cwid, chh = f.padx + f.W * 0.32, f.H * 0.3, f.W * 0.54, f.H * 0.38
    cols, n = 10, 100
    cell = gw / cols
    rng = np.random.default_rng(5)
    lit = set(rng.choice(n, int(round(n * b["opt_in"])), replace=False).tolist())
    dots = [f'<svg id="dots" class="map" viewBox="0 0 {gw} {gw}" style="left:{gx}px; top:{gy}px; width:{gw}px; height:{gw}px;">']
    for i in range(n):
        dots.append(f'<circle class="vis{" lit" if i in lit else ""}" cx="{(i % cols + 0.5) * cell:.1f}" cy="{(i // cols + 0.5) * cell:.1f}" r="{cell * 0.3:.1f}" fill="{BORDER}"/>')
    dots.append("</svg>")
    f.add("".join(dots))
    label(f, "optlab", "EACH DOT: 1% OF VISITORS · LIT: OPTED IN", gx, gy + gw + 14 * u, size=f.s_label * (0.8 if not f.portrait else 0.9))
    stat(f, "cnt", gx + (gw + 60 * u if f.portrait else 0), gy + (0 if f.portrait else gw + f.H * 0.06),
         f'{b["counted"]:,} of {b["visitors"]:,}', "VISITS COUNTED (A QUARTER)", size=f.s_stat * (0.55 if f.portrait else 0.5))
    # popular-times chart
    hours = b["hours"]
    nb = len(hours)
    slot = cwid / nb
    bars = [f'<svg id="chart" class="map" viewBox="0 0 {cwid} {chh}" style="left:{cx}px; top:{cy}px; width:{cwid}px; height:{chh}px; overflow:visible;">',
            f'<line x1="0" y1="{chh}" x2="{cwid}" y2="{chh}" stroke="{INK}" stroke-width="{3 * u}"/>']
    for i, (tv, ev) in enumerate(zip(b["true"], b["est"])):
        x = i * slot + slot * 0.12
        bw = slot * 0.76
        bars.append(f'<rect class="ghost" x="{x:.1f}" y="{chh - tv * chh * 0.92:.1f}" width="{bw:.1f}" height="{tv * chh * 0.92:.1f}" fill="none" stroke="{INK}" stroke-width="{3 * u}" stroke-dasharray="{8 * u} {6 * u}" rx="{6 * u}" opacity="0"/>')
        pk = hours[i] == b["peak_est"]
        bars.append(f'<rect id="bar{i}" class="est" x="{x:.1f}" y="{chh - ev * chh * 0.92:.1f}" width="{bw:.1f}" height="{ev * chh * 0.92:.1f}" fill="{SPARK if pk else ACCENT}" fill-opacity="{1 if pk else 0.55}" rx="{6 * u}"/>')
    for i, h in enumerate(hours):
        if h % 3 == 0:
            lab = f"{h % 12 or 12}{'a' if h < 12 else 'p'}"
            bars.append(f'<text x="{i * slot + slot / 2:.1f}" y="{chh + f.s_label * 1.3:.1f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{f.s_label}" fill="{INK_SOFT}">{lab}</text>')
    bars.append("</svg>")
    f.add("".join(bars))
    label(f, "ptlab", "POPULAR TIMES · ONE CAFE, 8 FRIDAYS", cx, cy - f.s_label * 2.0, color=INK)
    ipk = hours.index(b["peak_est"])
    f.add(f'<div id="peak" class="abs caps" style="left:{cx + ipk * slot - slot * 0.5}px; top:{cy - f.s_label * 0.2 + chh * 0.02}px; font-size:{f.s_label}px; color:{SPARK};"></div>')
    key_y = cy + chh + f.s_label * 2.6
    f.add(f'<div id="key" class="abs caps" style="left:{cx}px; top:{key_y}px; font-size:{f.s_label * (0.9 if f.portrait else 0.85)}px; color:{INK_SOFT}; display:flex; gap:{30 * u}px; flex-wrap:wrap;">'
          f'<span style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{30 * u}px; height:{18 * u}px; background:{ACCENT}; border-radius:{4 * u}px;"></span>COUNTED + NOISE</span>'
          f'<span id="key2" style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{30 * u}px; height:{18 * u}px; border:{3 * u}px dashed {INK}; border-radius:{4 * u}px;"></span>THE REAL CROWD</span></div>')
    stat(f, "busiest", cx + cwid * (0.0 if f.portrait else 0.0), key_y + f.s_label * 2.4, "1 pm", f'BUSIEST HOUR, AS IN REAL LIFE',
         color=SPARK, size=f.s_stat * 0.6)
    # the quiet shop
    qx, qy = (cx + cwid * 0.5, key_y + f.s_label * 2.4) if True else (0, 0)
    f.add(f'<div id="shop" class="card" style="left:{qx}px; top:{qy}px; width:{cwid * 0.5}px; padding:{22 * u}px {26 * u}px;">'
          f'<div class="caps" style="font-size:{f.s_label}px; color:{INK};">QUIET SHOP</div>'
          f'<div class="serif" style="font-size:{f.s_body * 0.8}px; color:{INK}; margin-top:{8 * u}px;">Not enough data</div>'
          f'<div class="caps" style="font-size:{f.s_label * 0.85}px; color:{INK_SOFT}; margin-top:{6 * u}px;">{b["shop_counted"]} VISITS COUNTED · NO CHART</div></div>')
    f.anim(Template("""
tl.fromTo("#dots", {opacity:0}, {opacity:1, duration:0.5}, 0.2);
tl.fromTo(".vis", {scale:0, transformOrigin:"50% 50%"}, {scale:1, duration:0.3, stagger:{each:0.006, from:"random"}, ease:"back.out(2)"}, 0.3);
tl.to(".vis.lit", {fill:"$ink", duration:0.3, stagger:0.02}, $to);
inn("#optlab", $to + 0.2, 0.5);
inn("#cnt", $tq, 0.6);
inn("#ptlab", $tq, 0.5); tl.fromTo("#chart", {opacity:0}, {opacity:1, duration:0.4}, $tq);
tl.fromTo(".est", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.6, stagger:0.04, ease:"power3.out"}, $tn);
tl.fromTo(".est", {y:0}, {y:-6, duration:0.12, yoyo:true, repeat:5, stagger:0.02, ease:"sine.inOut"}, $tn + 0.7);
tl.to(".ghost", {opacity:0.8, duration:0.6, stagger:0.03}, $tm);
inn("#key", $tm, 0.5);
inn("#busiest", $t1, 0.6);
inn("#shop", $tsh, 0.6);
""").substitute(ink=INK, to=f.t("opted"), tq=f.t("quarter"), tn=f.t("noise"), tm=f.t("matched"), t1=f.t("one"), tsh=f.t("shop")))


# ================================================================== B07 · how crowded
def b07(f):
    u = f.u
    bus = S["bus"]
    x0, y0, size = map_box(f, (f.cw * 0.6) if f.portrait else f.H * 0.5)
    if f.portrait:
        x0 = f.padx
    line = sorted([k for k in NODES if k.split(",")[0] == "10"], key=lambda s: int(s.split(",")[1]))
    stops = line[2::4]
    extra = (f'<polyline id="busline" points="{polyline(line)}" fill="none" stroke="{SPARK}" stroke-width="70" stroke-linecap="round"/>'
             + "".join(f'<circle class="stop" cx="{fmt(NODES[s][0])}" cy="{fmt(NODES[s][1])}" r="70" fill="{CARD}" stroke="{SPARK}" stroke-width="26"/>' for s in stops)
             + f'<g id="bus"><rect x="-150" y="-100" width="300" height="200" rx="50" fill="{INK}"/><rect x="-110" y="-60" width="220" height="70" rx="16" fill="{CARD}"/></g>')
    svg_place(f, city_svg("bmap", extra=extra), x0, y0, size, "bmap")
    # GTFS chip + the question card
    if f.portrait:
        x, y, w = x0 + size + 40 * u, y0, f.W - f.padx - (x0 + size + 40 * u)
    else:
        x, y, w = x0 + size + f.W * 0.04, f.H * 0.215, f.W - f.padx - (x0 + size + f.W * 0.04)
    f.add(f'<div id="gtfs" class="card" style="left:{x}px; top:{y}px; padding:{18 * u}px {24 * u}px; width:{w}px;">'
          f'<div class="num" style="font-size:{f.s_stat * 0.5}px; color:{INK};">GTFS</div>'
          f'<div class="caps" style="font-size:{f.s_label * 0.9}px; color:{INK_SOFT}; margin-top:{8 * u}px; white-space:normal; line-height:1.35;">TIMETABLES + LIVE VEHICLE DATA, PUBLISHED BY AGENCIES</div></div>')
    qy = y + f.H * (0.12 if f.portrait else 0.17)
    opts = ["Many seats", "Few seats", "Standing"]
    f.add(f'<div id="ask" class="card" style="left:{x}px; top:{qy}px; padding:{20 * u}px {24 * u}px; width:{w}px;">'
          f'<div class="serif" style="font-size:{f.s_body * 0.85}px; color:{INK};">How crowded was it?</div>'
          + "".join(f'<div class="opt" style="margin-top:{12 * u}px; display:flex; align-items:center; gap:{14 * u}px;">'
                    f'<span style="display:inline-block; width:{26 * u}px; height:{26 * u}px; border-radius:50%; border:{4 * u}px solid {INK_SOFT};{"background:" + SPARK + ";" if i == 1 else ""}"></span>'
                    f'<span class="serif" style="font-size:{f.s_body * 0.7}px; color:{INK};">{o}</span></div>' for i, o in enumerate(opts)) + "</div>")
    # the crowding strip: 32 trips, predicted vs the next day
    sx = f.padx
    sy = (y0 + size + f.H * 0.04) if f.portrait else (f.H * 0.76 - f.H * 0.02)
    sw = f.cw if f.portrait else f.cw
    n = len(bus["trips"])
    cellw = sw / n
    ch = f.s_label * (1.6 if f.portrait else 1.3)
    LV = [GREEN, AMBER, RED]
    if not f.portrait:
        sy = y0 + size + f.H * 0.035
    rows = []
    for r_, (key, lab) in enumerate((("pred", "PREDICTED FROM ANSWERS"), ("truth", "THE NEXT DAY"))):
        yy = sy + r_ * (ch * 2.4)
        rows.append(f'<div class="caps" style="position:absolute; left:0; top:{yy - f.s_label * 1.35}px; font-size:{f.s_label * 0.85}px; color:{INK_SOFT};">{lab}</div>')
        for i, lv in enumerate(bus[key]):
            col = LV[lv] if lv >= 0 else BORDER
            rows.append(f'<div class="cell c{r_}" style="position:absolute; left:{i * cellw + cellw * 0.08}px; top:{yy}px; width:{cellw * 0.84}px; height:{ch}px; background:{col}; border-radius:{5 * u}px;"></div>')
    miss = [i for i in range(n) if bus["pred"][i] >= 0 and bus["pred"][i] != bus["truth"][i]]
    for i in miss:
        rows.append(f'<div class="miss" style="position:absolute; left:{i * cellw + cellw * 0.5 - 4 * u}px; top:{sy + ch}px; width:{8 * u}px; height:{ch * 1.4}px; background:{INK};"></div>')
    f.add(f'<div id="strip" class="abs" style="left:{sx}px; top:0px; width:{sw}px; height:{f.H}px;">' + "".join(rows) + "</div>")
    label(f, "striplab", f"ONE BUS ROUTE · {n} TRIPS A DAY · MARK: A MISS", sx, sy - f.s_label * 3.0, color=INK)
    sty = sy + ch * 2.4 + ch + f.s_label * 1.2
    stat(f, "acc", sx, sty, f'{bus["acc"] * 100:.0f}%', "OF TRIPS PREDICTED RIGHT", color=SPARK, size=f.s_stat * (0.55 if f.portrait else 0.55))
    stat(f, "few", sx + sw * 0.4, sty, "3 in 100", "RIDERS ANSWERED", size=f.s_stat * 0.55)
    sp = json.dumps([[round(NODES[s][0]), round(NODES[s][1])] for s in line])
    f.anim(Template("""
tl.fromTo("#bmap-wrap", {opacity:0}, {opacity:1, duration:0.7}, 0.15);
draw("#busline", 0.4, 1.0);
tl.fromTo(".stop", {opacity:0}, {opacity:1, duration:0.3, stagger:0.08}, 1.0);
const P = $pts, bus = q("#bus"), o = {s:0};
const put = function () { const d = o.s * (P.length - 1), i = Math.min(P.length - 2, Math.floor(d)), f2 = d - i;
  bus.setAttribute("transform", "translate(" + (P[i][0] + (P[i + 1][0] - P[i][0]) * f2) + " " + (P[i][1] + (P[i + 1][1] - P[i][1]) * f2) + ")"); };
put();
tl.to(o, {s:1, duration: D - 1.5, ease:"none", onUpdate: put}, 1.0);
inn("#gtfs", $ta, 0.6);
tl.fromTo("#gtfs", {borderColor:"$border"}, {borderColor:"$spark", duration:0.4, yoyo:true, repeat:1}, $tg);
inn("#ask", $tr, 0.6);
tl.fromTo(".opt", {opacity:0, x:-12}, {opacity:1, x:0, duration:0.35, stagger:0.12}, $tr + 0.3);
inn("#striplab", $tt - 0.2, 0.5);
inn("#few", $tt, 0.5);
tl.fromTo(".c0", {opacity:0, scaleY:0, transformOrigin:"50% 100%"}, {opacity:1, scaleY:1, duration:0.3, stagger:0.025}, $tt);
tl.fromTo(".c1", {opacity:0, scaleY:0, transformOrigin:"50% 0%"}, {opacity:1, scaleY:1, duration:0.3, stagger:0.025}, $te - 0.4);
tl.fromTo(".miss", {opacity:0}, {opacity:1, duration:0.3}, $te + 0.5);
inn("#acc", $te, 0.6);
""").substitute(pts=sp, ta=f.t("agencies"), tg=f.t("gtfs"), tr=f.t("riders"), tt=f.t("three"), te=f.t("eighty"),
                border=BORDER, spark=SPARK))


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07}


def build():
    out = []
    for bid, fn in BUILDERS.items():
        for portrait in (False, True):
            f = Frame(bid, portrait)
            f.head()
            fn(f)
            f.foot()
            p = HF / f"{bid}-{'v' if portrait else 'l'}.html"
            p.write_text(f.html(), encoding="utf-8", newline="\n")
            out.append(p)
    print("wrote", len(out), "compositions to", HF)
    return out


def render(only=None):
    (HERE / "media").mkdir(exist_ok=True)
    (HERE / "pantry").mkdir(exist_ok=True)
    for bid in BUILDERS:
        if only and bid not in only:
            continue
        for portrait in (False, True):
            src = f"{bid}-{'v' if portrait else 'l'}.html"
            dst = HERE / ("pantry" if portrait else "media") / (f"{bid}-916.mp4" if portrait else f"{bid}.mp4")
            cmd = ["npx.cmd", "--no-install", "hyperframes", "render", "-c", src, "-o", str(dst), "-q", "delivery", "--quiet"]
            print("render", src, "->", dst.relative_to(HERE), flush=True)
            subprocess.run(cmd, cwd=HF, check=True)


if __name__ == "__main__":
    build()
    if "--render" in sys.argv:
        only = [a for a in sys.argv[2:] if a.startswith("B")]
        render(only or None)
