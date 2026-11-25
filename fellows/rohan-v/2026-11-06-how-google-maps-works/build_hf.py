"""Builds the HyperFrames compositions for "How Google Maps Works" (B01-B07): hyperframes/B0x-l.html (3840x2160)
and hyperframes/B0x-v.html (2160x3840), one root composition per beat and aspect.

LOOK: "night city". The film leaves the channel's cream cards for a dark, map-app night mode: a deep navy
ground, the simulated city as a tilted 3D plane with glowing roads, a camera that drifts and pushes through each
beat, light trails for phones and cars, and glass HUD panels for the numbers. Type: Source Serif 4 for titles,
Inter for the HUD. Colour carries meaning: cyan = you (position), coral = the answer (route, trip, bus line),
green/amber/red = traffic, pale blue = the search.

DATA: everything drawn comes from evidence/scene.json + results.json (maps.py) and the beat sheet: each beat's
measured duration and its word-clock cues (fractions from sync_cues.py), so each reveal lands on its word.
(build_hf_v1_cream.py is the first, house-style cream version, kept for comparison.)

    python build_hf.py [B03 ...]            # write the compositions
    python build_hf.py [B03 ...] --render   # and render them: media/B0x.mp4 (16:9), pantry/B0x-916.mp4 (9:16)
"""
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path
from string import Template

import numpy as np

HERE = Path(__file__).resolve().parent
HF = HERE / "hyperframes"
TMPD = "D:/Rohan/Claude/HyperFrames/tmp"
sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
RES = json.loads((HERE / "evidence" / "results.json").read_text(encoding="utf-8"))
BEATS = {b["beat_id"]: b for b in sheet["beats"]}

BG, BG2 = "#070C17", "#0D1730"
TEXT, SOFT, DIM = "#EEF2F8", "#9FB0C8", "#5E6F8A"
CYAN, CORAL, SEARCH = "#58DCF5", "#FF7A59", "#9DBBFF"
GREEN, AMBER, RED = "#36D399", "#FBBF24", "#F25555"
GLASS, GLASS_LINE = "rgba(255,255,255,0.045)", "rgba(255,255,255,0.13)"
ROAD = {"local": ("#18263F", 22), "avenue": ("#24405F", 40), "highway": ("#2F6199", 64)}
CHAPTER = {"B01": "01 · WHERE AM I", "B02": "02 · THE MAP", "B03": "03 · THE ROUTE", "B04": "04 · TRAFFIC",
           "B05": "05 · ARRIVAL TIME", "B06": "06 · HOW BUSY", "B07": "07 · HOW CROWDED"}
PTITLE = {"B01": "Satellites and a Clock", "B02": "How the Map Is Built", "B03": "Roads Become a Graph",
          "B04": "Traffic From Phones", "B05": "History Plus Live", "B06": "How Busy It Is", "B07": "How Full the Bus Is"}
SPARKS = {
    "B01": ("Four satellites: three for place, one for time.", "Three for place, one for time."),
    "B02": ("Photos, partners and people, read by AI.", "Photos and people, read by AI."),
    "B03": ("Same route, far fewer corners checked.", "Same route, fewer corners."),
    "B04": ("History knows the usual. Phones catch the crash.", "Phones catch the crash."),
    "B05": ("History plus live beats the speed limit.", "History plus live wins."),
    "B06": ("Counted, pooled, blurred, then shown.", "Counted, pooled, blurred."),
    "B07": ("A few answers predict the crowd.", "A few answers, a good guess."),
}

NODES = {k: tuple(v) for k, v in S["city"]["nodes"].items()}
EDGES = S["city"]["edges"]                 # from, to, class, true lv, history lv, 500-phone lv, 2000-phone lv
VB = (-200, -200, 5040, 5040)
Q = chr(34)


def fmt(x):
    return f"{x:.0f}"


def polyline(keys):
    return " ".join(f"{fmt(NODES[k][0])},{fmt(NODES[k][1])}" for k in keys)


DEFS = """<defs>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26" result="b"/>
<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glow2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60" result="b"/>
<feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="plate" cx="50%" cy="50%" r="60%"><stop offset="0%" stop-color="#101C33"/><stop offset="100%" stop-color="#0A1222"/></radialGradient>
</defs>"""


def city_svg(sid, extra="", nodes=False):
    out = [f'<svg id="{sid}" viewBox="{" ".join(map(str, VB))}" style="position:absolute; inset:0; width:100%; height:100%; overflow:visible;">', DEFS,
           f'<rect x="{VB[0]}" y="{VB[1]}" width="{VB[2]}" height="{VB[3]}" rx="220" fill="url(#plate)" stroke="#1B2A45" stroke-width="16"/>']
    for cls in ("local", "avenue", "highway"):
        col, w = ROAD[cls]
        segs = []
        for a, b, c, tlv, h, p5, p20 in EDGES:
            if c != cls:
                continue
            (x1, y1), (x2, y2) = NODES[a], NODES[b]
            segs.append(f'<line class="seg {sid}-s h{h} p{p5} t{tlv}" x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" '
                        f'stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
        filt = ' filter="url(#glow)"' if cls == "highway" else ""
        out.append(f'<g class="{sid}-{cls}"{filt}>' + "".join(segs) + "</g>")
    if nodes:
        out.append(f'<g id="{sid}-nodes">' + "".join(
            f'<circle id="{sid}-n-{k.replace(",", "_")}" cx="{fmt(x)}" cy="{fmt(y)}" r="26" fill="{DIM}" opacity="0"/>'
            for k, (x, y) in NODES.items()) + "</g>")
    out.append(extra)
    out.append("</svg>")
    return "".join(out)


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
html, body { width: ${W}px; height: ${H}px; overflow: hidden; background: $BG; }
#root { position: relative; width: ${W}px; height: ${H}px; overflow: hidden; color: $TEXT; font-family: Inter, sans-serif;
  background: radial-gradient(ellipse 60% 55% at 50% 52%, $BG2 0%, $BG 100%); }
.abs { position: absolute; }
.serif { font-family: "Source Serif 4", serif; }
.caps { font-family: Inter, sans-serif; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; white-space: nowrap; }
.num { font-family: Inter, sans-serif; font-weight: 900; line-height: 0.95; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; }
.glass { position: absolute; background: $GLASS; border: ${BW}px solid $GLINE; border-radius: ${RAD}px; }
.camwrap { position: absolute; perspective: ${PERSP}px; }
.cam { position: absolute; transform-style: preserve-3d; }
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
  tl.fromTo(sel, Object.assign({ opacity: 0, y: $RISE, filter: "blur(10px)" }, from || {}),
    { opacity: 1, y: 0, x: 0, filter: "blur(0px)", duration: dur || 0.7, ease: "expo.out" }, t);
}
function count(sel, to, t, dur, dec) {
  const o = { v: 0 }, el = q(sel);
  const show = function () { el.textContent = o.v.toLocaleString("en-US", { minimumFractionDigits: dec || 0, maximumFractionDigits: dec || 0 }); };
  show();
  tl.to(o, { v: to, duration: dur || 1.2, ease: "power3.out", onUpdate: show }, t);
}
function draw(sel, t, dur, ease) {
  qa(sel).forEach(function (el) {
    const L = el.getTotalLength ? el.getTotalLength() : 1000;
    gsap.set(el, { strokeDasharray: L, strokeDashoffset: L });
    tl.to(el, { strokeDashoffset: 0, duration: dur || 1.2, ease: ease || "power2.inOut" }, t);
  });
}
$JS
inn("#chapter", 0.05, 0.6); inn("#title", 0.15, 0.9);
tl.fromTo("#rule", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 1.0, ease: "expo.out" }, 0.1);
tl.fromTo("#spark", { opacity: 0, x: -$RISE }, { opacity: 1, x: 0, duration: 0.8, ease: "expo.out" }, $TSPARK);
tl.to({}, { duration: 0.01 }, D - 0.01);
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
""")


HUDJS = Template("""
(function () {   // phone HUD: rows by authored top, then spread evenly between $Y0 and $Y1 (no overlaps)
  const els = qa(".hud").map(function (e) { return { e: e, t: parseFloat(e.dataset.top) }; }).sort(function (a, b) { return a.t - b.t; });
  const rows = [];
  els.forEach(function (o) { const last = rows[rows.length - 1]; if (last && Math.abs(o.t - last.t) <= $TOL) last.items.push(o); else rows.push({ t: o.t, items: [o] }); });
  rows.forEach(function (row) { row.h = Math.max.apply(null, row.items.map(function (o) { return o.e.offsetHeight; })); });
  const total = rows.reduce(function (a, row) { return a + row.h; }, 0);
  const gap = Math.max(18, ($Y1 - $Y0 - total) / (rows.length + 1));
  let y = $Y0 + gap;
  rows.forEach(function (row) { row.items.forEach(function (o) { o.e.style.top = y + "px"; }); y += row.h + gap; });
})();
""")


class Frame:
    def __init__(self, bid, portrait):
        self.bid, self.portrait = bid, portrait
        self.W, self.H = (2160, 3840) if portrait else (3840, 2160)
        self.u = 2.0
        self.padx = self.W * (0.067 if portrait else 0.065)
        self.cw = self.W - 2 * self.padx
        b = BEATS[bid]
        self.D = round(b["actual_duration_s"], 3)
        self.cues = b["shot"]["remotion"]["props"].get("cues", {})
        self.title = PTITLE[bid] if portrait else b["shot"]["remotion"]["props"]["title"]
        self.parts, self.js = [], []
        self.hud_start = self.hud_end = None
        H = self.H
        if portrait:      # the phone type scale (fractions of height); 4K phone floor ~72 px
            self.s_title, self.s_label, self.s_stat, self.s_spark = H * 0.05, H * 0.0265, H * 0.07, H * 0.0425
        else:
            self.s_title, self.s_label, self.s_stat, self.s_spark = 128, 50, 240, 64

    def t(self, cue, default=0.0):
        return round(self.cues.get(cue, default) * self.D, 3)

    def add(self, html):
        self.parts.append(html)

    def mark_hud(self):
        """Everything added after this is HUD: on the phone it is re-laid out as one evenly spaced column."""
        self.hud_start = len(self.parts)

    def anim(self, js):
        self.js.append(js)

    def head(self):
        y0 = self.H * (0.06 if self.portrait else 0.075)
        self.add(f'<div id="chapter" class="abs caps" style="left:{self.padx}px; top:{y0}px; font-size:{self.s_label * (1 if self.portrait else 0.8)}px; color:{CYAN};">{CHAPTER[self.bid]}</div>')
        self.add(f'<div id="title" class="abs serif" style="left:{self.padx}px; top:{y0 + self.s_label * 1.7}px; font-size:{self.s_title}px; '
                 f'font-weight:600; color:{TEXT}; line-height:1.05; letter-spacing:-0.01em;">{self.title}</div>')

    def foot(self):
        self.hud_end = len(self.parts)
        u = self.u
        txt = SPARKS[self.bid][1 if self.portrait else 0]
        if self.portrait:      # phone: no closing line; its space goes to the HUD column (kept as hidden stubs for the timeline)
            self.add('<div id="rule" class="abs" style="display:none"></div><div id="spark" class="abs" style="display:none"></div>')
            return
        top = self.H * (0.8 if self.portrait else 0.875)
        self.add(f'<div id="rule" class="abs" style="left:{self.padx}px; top:{self.H * (0.782 if self.portrait else 0.85)}px; width:{self.cw}px; height:{2 * u}px; '
                 f'background:linear-gradient(90deg, rgba(255,255,255,0.22), rgba(255,255,255,0.04));"></div>')
        self.add(f'<div id="spark" class="abs" style="left:{self.padx}px; top:{top}px; display:flex; align-items:baseline; gap:{18 * u}px; width:{self.cw}px;">'
                 f'<span style="display:inline-block; width:{48 * u}px; height:{4 * u}px; background:{CORAL}; border-radius:{2 * u}px; transform:translateY(-{self.s_spark * 0.3}px);"></span>'
                 f'<span class="serif" style="font-style:italic; font-size:{self.s_spark}px; color:{TEXT}; line-height:1.2;">{txt}</span></div>')

    def html(self):
        if self.portrait and self.hud_start is not None:
            for i in range(self.hud_start, self.hud_end if self.hud_end is not None else len(self.parts)):
                m = re.match(r'<div id="([^"]+)" class="([^"]*)" style="([^"]*?)top:([\d.]+)px;', self.parts[i])
                if m and m.group(1) not in ("shopcard",):      # the shop card sits on the map, not in the column
                    self.parts[i] = self.parts[i].replace(f'class="{m.group(2)}"', f'class="{m.group(2)} hud" data-top="{m.group(4)}"', 1)
            self.js.insert(0, HUDJS.substitute(Y0=round(self.H * 0.478), Y1=round(self.H * 0.84), TOL=round(self.H * 0.012)))
        last = max(self.cues.values()) if self.cues else 0.8
        tspark = round(min(max(last + 0.05, 0.62), 0.9) * self.D, 3)
        head = HEAD.substitute(W=self.W, H=self.H, D=self.D, BG=BG, BG2=BG2, TEXT=TEXT, GLASS=GLASS, GLINE=GLASS_LINE,
                               BW=round(1.5 * self.u, 1), RAD=round(22 * self.u), PERSP=round(2600 * self.u))
        return head + "\n".join(self.parts) + FOOT.substitute(D=self.D, JS="\n".join(self.js), RISE=round(18 * self.u), TSPARK=tspark)

    def city(self, sid, extra="", nodes=False, area=None):
        """The city as a 3D plane in a fog-masked window (the fog keeps every edge inside title-safe)."""
        if area is None:
            area = (0, self.H * 0.145, self.W, self.H * 0.32) if self.portrait else (0, self.H * 0.13, self.W * 0.62, self.H * 0.74)
        x, y, w, h = area
        size = min(w, h) * (1.25 if self.portrait else 1.3)
        mask = "radial-gradient(ellipse 50% 50% at 50% 50%, #000 58%, transparent 96%)"
        self.add(f'<div id="{sid}-wrap" class="camwrap" style="left:{x}px; top:{y}px; width:{w}px; height:{h}px; -webkit-mask-image:{mask}; mask-image:{mask};">'
                 f'<div id="{sid}-cam" class="cam" style="left:{(w - size) / 2}px; top:{(h - size) / 2}px; width:{size}px; height:{size}px;">'
                 + city_svg(sid, extra=extra, nodes=nodes) + "</div></div>")

    def cam(self, sid, rx0=58, rz0=-36, s0=0.86, rx1=52, rz1=-28, s1=1.0):
        self.anim(Template("""
tl.fromTo("#${sid}-wrap", { opacity: 0 }, { opacity: 1, duration: 1.0, ease: "power2.out" }, 0);
tl.fromTo("#${sid}-cam", { rotationX: $rx0, rotationZ: $rz0, scale: $s0 },
  { rotationX: $rx1, rotationZ: $rz1, scale: $s1, duration: $dur, ease: "sine.inOut" }, 0);
""").substitute(sid=sid, rx0=rx0, rz0=rz0, s0=s0, rx1=rx1, rz1=rz1, s1=s1, dur=self.D))


def hud_col(f):
    if f.portrait:
        return f.padx, f.H * 0.49, f.cw
    return f.W * 0.62, f.H * 0.215, f.W - f.padx - f.W * 0.62


def stat(f, sid, x, y, value_html, lab, color=TEXT, size=None, labw=None):
    s = size or f.s_stat
    wrap = f"white-space:normal; width:{labw}px; line-height:1.35;" if labw else ""
    f.add(f'<div id="{sid}" class="abs" style="left:{x}px; top:{y}px;">'
          f'<div id="{sid}-v" class="num" style="font-size:{s}px; color:{color};">{value_html}</div>'
          f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT}; margin-top:{s * 0.16}px; {wrap}">{lab}</div></div>')


def label(f, lid, text, x, y, color=SOFT, size=None):
    f.add(f'<div id="{lid}" class="abs caps" style="left:{x}px; top:{y}px; font-size:{size or f.s_label}px; color:{color};">{text}</div>')


def gtag(f, gid, text, x, y, wrapw=None):
    """LOGO LAW: Google's own mark beside its name."""
    s = f.s_label
    wrap = f"white-space:normal; width:{wrapw}px; line-height:1.35;" if wrapw else ""
    f.add(f'<div id="{gid}" class="glass" style="left:{x}px; top:{y}px; display:flex; align-items:center; gap:{s * 0.6}px; padding:{s * 0.55}px {s * 0.8}px;">'
          f'<span style="display:flex; flex:none; width:{s * 1.9}px; height:{s * 1.9}px; border-radius:50%; background:#FFFFFF; align-items:center; justify-content:center;">'
          f'<img src="assets/google-01.svg" style="width:{s * 1.5}px; height:{s * 1.5}px;" /></span>'
          f'<span class="caps" style="font-size:{s}px; color:{TEXT}; {wrap}">{text}</span></div>')


# ================================================================== Google Maps UI (night mode), drawn to match the app
GM_CARD, GM_LINE, GM_TEXT, GM_SOFT = "#28292C", "#3C4043", "#E8EAED", "#9AA0A6"
GM_BLUE, GM_ROUTE, GM_CASE, GM_GREEN, GM_PIN = "#8AB4F8", "#4C8DF6", "#1A4FA8", "#81C995", "#EA4335"


def gm_card(f, cid, x, y, w, inner, pad=None):
    p = pad or 30 * f.u
    f.add(f'<div id="{cid}" class="abs" style="left:{x}px; top:{y}px; width:{w}px; padding:{p}px {p * 1.15}px; background:{GM_CARD}; '
          f'border:{1.5 * f.u}px solid {GM_LINE}; border-radius:{24 * f.u}px; box-shadow:0 {10 * f.u}px {40 * f.u}px rgba(0,0,0,0.45); '
          f'font-family:Roboto, Inter, sans-serif; color:{GM_TEXT};">{inner}</div>')


def blue_dot(x, y, r, halo_id=None, halo_r=0, stroke=5):
    h = (f'<circle id="{halo_id}" cx="{x}" cy="{y}" r="{halo_r}" fill="#4285F4" fill-opacity="0.18" stroke="#4285F4" stroke-opacity="0.45" stroke-width="{stroke * 0.5}" opacity="0"/>'
         if halo_id else "")
    return h + (f'<circle cx="{x}" cy="{y}" r="{r * 1.35}" fill="#FFFFFF"/>'
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4285F4"/>')


def gm_pin(scale=1.0):
    """Google's red destination pin (drawn), tip at 0,0."""
    s = scale
    return (f'<path d="M0 0 C {-60 * s} {-90 * s} {-120 * s} {-140 * s} {-120 * s} {-220 * s} A {120 * s} {120 * s} 0 1 1 {120 * s} {-220 * s} '
            f'C {120 * s} {-140 * s} {60 * s} {-90 * s} 0 0 Z" fill="{GM_PIN}" stroke="#B31412" stroke-width="{8 * s}"/>'
            f'<circle cy="{-220 * s}" r="{44 * s}" fill="#8C0E0D"/>')


def route_lines(rid, keys):
    pts = polyline(keys)
    return (f'<polyline id="{rid}-case" points="{pts}" fill="none" stroke="{GM_CASE}" stroke-width="96" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polyline id="{rid}" points="{pts}" fill="none" stroke="{GM_ROUTE}" stroke-width="64" stroke-linejoin="round" stroke-linecap="round"/>')


# ================================================================== B01 · where am I
def b01(f):
    u, g = f.u, S["gps"]
    W, H = f.W, f.H
    sx, sy, sw, sh = (0, H * 0.14, W, H * 0.33) if f.portrait else (W * 0.055, H * 0.1, W * 0.545, H * 0.8)
    cx, R = sw * 0.5, sw * 1.6
    py = sh * 0.86
    cy = py + R
    px = cx
    sats = sorted(g["sats"], key=lambda s: -s[1])[:8]
    rng = np.random.default_rng(4)
    spos = [(cx + sw * 0.42 * math.cos(math.radians(el)) * math.sin(math.radians(az)),
             py - sh * 0.72 * math.sin(math.radians(el)) - sh * 0.05) for az, el in sats]
    mask = "radial-gradient(ellipse 50% 50% at 50% 50%, #000 62%, transparent 97%)"
    svg = [f'<div id="skywrap" class="abs" style="left:{sx}px; top:{sy}px; width:{sw}px; height:{sh}px; -webkit-mask-image:{mask}; mask-image:{mask};">'
           f'<svg id="sky" viewBox="0 0 {sw} {sh}" style="position:absolute; left:0; top:0; width:{sw}px; height:{sh}px; overflow:hidden;">', DEFS,
           f'<defs><radialGradient id="atmo" cx="50%" cy="50%" r="50%"><stop offset="92%" stop-color="{CYAN}" stop-opacity="0.0"/>'
           f'<stop offset="97%" stop-color="{CYAN}" stop-opacity="0.35"/><stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/></radialGradient></defs>']
    for _ in range(60):
        x, y = rng.uniform(sw * 0.06, sw * 0.94), rng.uniform(sh * 0.06, sh * 0.7)
        svg.append(f'<circle class="star" cx="{x:.0f}" cy="{y:.0f}" r="{rng.uniform(1.5, 3.5) * u:.1f}" fill="#FFFFFF" opacity="0"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R * 1.03}" fill="url(#atmo)"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#0B1528" stroke="{CYAN}" stroke-opacity="0.55" stroke-width="{3 * u}"/>')
    for k, rr in enumerate((0.42, 0.5)):
        svg.append(f'<ellipse class="orbit" cx="{cx}" cy="{py}" rx="{sw * rr}" ry="{sh * (0.78 + 0.08 * k)}" fill="none" stroke="#FFFFFF" stroke-opacity="0.08" stroke-width="{2 * u}" stroke-dasharray="{6 * u} {12 * u}"/>')
    for k, (x, y) in enumerate(spos[:4]):
        d = math.hypot(px - x, py - y)
        col = CORAL if k < 3 else CYAN
        svg.append(f'<circle id="ring{k}" cx="{x:.1f}" cy="{y:.1f}" r="{d:.1f}" fill="none" stroke="{col}" stroke-opacity="0.5" stroke-width="{3 * u}" opacity="0"/>')
        svg.append(f'<line id="ray{k}" x1="{x:.1f}" y1="{y:.1f}" x2="{px}" y2="{py}" stroke="{col}" stroke-width="{3 * u}" stroke-opacity="0.9" opacity="0"/>')
        svg.append(f'<circle id="pulse{k}" cx="{x:.1f}" cy="{y:.1f}" r="{9 * u}" fill="{col}" filter="url(#glow)" opacity="0"/>')
    for k, (x, y) in enumerate(spos):
        s = 24 * u
        svg.append(f'<g id="sat{k}" opacity="0" transform="translate({x:.1f} {y:.1f})"><g class="satb">'
                   f'<rect x="{-s * 1.9}" y="{-s * 0.3}" width="{s * 1.25}" height="{s * 0.6}" rx="{3 * u}" fill="#3A6FB0"/>'
                   f'<rect x="{s * 0.65}" y="{-s * 0.3}" width="{s * 1.25}" height="{s * 0.6}" rx="{3 * u}" fill="#3A6FB0"/>'
                   f'<rect x="{-s * 0.55}" y="{-s * 0.55}" width="{s * 1.1}" height="{s * 1.1}" rx="{6 * u}" fill="#DCE6F5"/></g></g>')
    cxk, cyk = spos[3]
    svg.append(f'<g id="clock" opacity="0" transform="translate({cxk + 62 * u:.1f} {cyk - 42 * u:.1f})">'
               f'<circle r="{30 * u}" fill="#0B1528" stroke="{CYAN}" stroke-width="{4 * u}"/>'
               f'<line id="hand" x1="0" y1="0" x2="0" y2="{-21 * u}" stroke="{CYAN}" stroke-width="{4 * u}" stroke-linecap="round"/>'
               f'<line x1="0" y1="0" x2="{14 * u}" y2="0" stroke="#DCE6F5" stroke-width="{4 * u}" stroke-linecap="round"/></g>')
    svg.append(f'<circle cx="{px}" cy="{py}" r="{26 * u}" fill="#4285F4" opacity="0.5" filter="url(#glow2)"/>')
    svg.append(blue_dot(px, py, 12 * u, "halo", 18 * u, 4 * u))
    svg.append("</svg></div>")
    f.add("".join(svg))
    f.mark_hud()
    x, y, w = hud_col(f)
    big = f.s_stat * (0.5 if f.portrait else 0.62)
    f.add(f'<div id="ms" class="glass" style="left:{x}px; top:{y}px; width:{w}px; padding:{26 * u}px {32 * u}px;">'
          f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT};">A CLOCK 1 MS OFF</div>'
          f'<div class="num" style="font-size:{big}px; color:{TEXT}; margin-top:{14 * u}px; white-space:nowrap;"><span id="ms-v">0</span> km'
          f'{"" if f.portrait else "<span class=" + Q + "caps" + Q + " style=" + Q + "font-size:" + str(f.s_label) + "px; color:" + CYAN + "; margin-left:" + str(24 * u) + "px; letter-spacing:0.12em; font-weight:700;" + Q + ">OF RANGE ERROR</span>"}</div></div>')
    cy0 = y + (H * 0.16 if f.portrait else H * 0.27)
    cw_ = (w - 32 * u) / 2
    ch = H * (0.1 if f.portrait else 0.24)
    label(f, "simlab", "MY SIMULATION" if f.portrait else "MY SIMULATION · MEDIAN ERROR", x, cy0 - f.s_label * 1.6, color=TEXT)
    rtall = min(cw_ * (0.3 if f.portrait else 1), ch) * 0.42
    ropen = max(g["open_med"] * rtall / g["canyon_med"], 14 * u)
    for k, (cid, lab, val) in enumerate((("open", "OPEN SKY", g["open_med"]), ("tall", "BUILDINGS" if f.portrait else "TALL BUILDINGS", g["canyon_med"]))):
        x2 = x + k * (cw_ + 32 * u)
        inner = [f'<svg viewBox="0 0 {cw_} {ch}" style="position:absolute; inset:0; width:{cw_}px; height:{ch}px;">']
        mx, my = (cw_ * 0.8, ch * 0.5) if f.portrait else (cw_ / 2, ch * 0.42)
        if cid == "tall":
            for bx, bw_, bh in ((0.06, 0.18, 0.7), (0.27, 0.14, 0.95), (0.62, 0.15, 0.85), (0.8, 0.14, 0.6)):
                if f.portrait and bx < 0.5:
                    continue
                inner.append(f'<rect class="bld" x="{cw_ * bx:.0f}" y="{ch * (1 - bh):.0f}" width="{cw_ * bw_:.0f}" height="{ch * bh:.0f}" rx="{6 * u}" fill="#16233A" stroke="#2A3F62" stroke-width="{2 * u}"/>')
        r0 = ropen if cid == "open" else rtall
        inner.append(f'<circle id="{cid}-c" cx="{mx}" cy="{my}" r="{r0:.1f}" fill="#4285F4" fill-opacity="0.18" stroke="#4285F4" stroke-opacity="0.7" stroke-width="{3 * u}"/>')
        inner.append(f'<circle cx="{mx}" cy="{my}" r="{14 * u}" fill="#FFFFFF"/><circle cx="{mx}" cy="{my}" r="{10 * u}" fill="#4285F4"/>')
        inner.append("</svg>")
        tpos = (f"left:{26 * u}px; top:{ch * 0.16}px;" if f.portrait else f"left:{26 * u}px; bottom:{22 * u}px;")
        inner.append(f'<div style="position:absolute; {tpos}"><div class="num" style="font-size:{f.s_stat * (0.36 if f.portrait else 0.42)}px; color:{TEXT};">≈ {val:.0f} m</div>'
                     f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT}; margin-top:{8 * u}px;">{lab}</div></div>')
        f.add(f'<div id="{cid}" class="glass" style="left:{x2}px; top:{cy0}px; width:{cw_}px; height:{ch}px; overflow:hidden;">' + "".join(inner) + "</div>")
    f.anim(Template("""
tl.fromTo("#skywrap", {opacity:0}, {opacity:1, duration:1.2}, 0.1);
tl.fromTo(".star", {opacity:0}, {opacity:0.4, duration:1.5, stagger:0.01}, 0.2);
tl.fromTo(".orbit", {opacity:0}, {opacity:1, duration:1.2}, $tw);
for (let k = 0; k < 8; k++) {
  tl.fromTo("#sat" + k, {opacity:0}, {opacity:1, duration:0.6}, $tw + 0.07 * k);
  tl.fromTo("#sat" + k + " .satb", {scale:0.3, transformOrigin:"50% 50%"}, {scale:1, duration:0.6, ease:"back.out(2.5)"}, $tw + 0.07 * k);
}
for (let k = 4; k < 8; k++) tl.to("#sat" + k, {opacity:0.3, duration:0.5}, $tf);
for (let k = 0; k < 4; k++) {
  tl.fromTo("#ray" + k, {opacity:0}, {opacity:0.9, duration:0.4}, $tf + 0.15 * k);
  const ray = q("#ray" + k), p = q("#pulse" + k);
  const x1 = +ray.getAttribute("x1"), y1 = +ray.getAttribute("y1"), x2 = +ray.getAttribute("x2"), y2 = +ray.getAttribute("y2");
  const o = {s:0}; const put = function () { const s = o.s % 1; p.setAttribute("cx", x1 + (x2 - x1) * s); p.setAttribute("cy", y1 + (y2 - y1) * s); };
  put(); tl.fromTo(p, {opacity:0}, {opacity:1, duration:0.2}, $tf + 0.15 * k);
  tl.to(o, {s: 5, duration: D - $tf - 0.15 * k, ease:"none", onUpdate: put}, $tf + 0.15 * k);
}
for (let k = 0; k < 3; k++) tl.fromTo("#ring" + k, {opacity:0, scale:0.2, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:1.4, ease:"expo.out"}, $tt + 0.2 * k);
tl.fromTo("#clock", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.6, ease:"back.out(2.5)"}, $tc);
tl.fromTo("#hand", {rotation:0, svgOrigin:"0 0"}, {rotation:1080, svgOrigin:"0 0", duration:4, ease:"power2.inOut"}, $tc);
inn("#ms", $tm, 0.8); count("#ms-v", $km, $tm + 0.2, 1.4, 0);
inn("#simlab", $to, 0.6);
inn("#open", $to, 0.7);
tl.fromTo("#open-c", {attr:{r:4}}, {attr:{r:$ropen}, duration:1.0, ease:"expo.out"}, $to + 0.2);
inn("#tall", $tb, 0.7);
tl.fromTo(".bld", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.8, stagger:0.08, ease:"expo.out"}, $tb + 0.1);
tl.fromTo("#tall-c", {attr:{r:4}}, {attr:{r:$rtall}, duration:1.3, ease:"expo.out"}, $tb + 0.3);
tl.fromTo("#halo", {opacity:0, attr:{r:$h0}}, {opacity:1, attr:{r:$h1}, duration:1.4, ease:"expo.out"}, $tci);
tl.to("#halo", {attr:{r:$h2}, duration:1.1, ease:"sine.inOut", yoyo:true, repeat:1}, $tci + 1.4);
""").substitute(tw=f.t("where", 0.02), tf=f.t("four"), tt=f.t("three"), tc=f.t("clock"), tm=f.t("milli"), to=f.t("open"),
                tb=f.t("tall"), tci=f.t("circle"), km=g["clock_km"], ropen=round(ropen, 1), rtall=round(rtall, 1),
                h0=round(16 * u), h1=round(110 * u), h2=round(150 * u)))


# ================================================================== B02 · the map is built (exploded view)
def b02(f):
    u = f.u
    W, H = f.W, f.H
    x0, y0, w0, h0 = (0, H * 0.14, W, H * 0.33) if f.portrait else (W * 0.05, H * 0.17, W * 0.55, H * 0.6)
    size = min(w0, h0) * (0.62 if f.portrait else 0.74)
    rng = np.random.default_rng(3)
    layers = [("street", "STREET VIEW CARS", "CARS", CORAL), ("photo", "SATELLITE + AERIAL PHOTOS", "PHOTOS", "#7C8DA8"),
              ("roads", "DATA PARTNERS", "PARTNERS", "#3C78C0"), ("edits", "PEOPLE'S EDITS", "EDITS", CYAN)]
    f.add(f'<div id="stack" class="camwrap" style="left:{x0}px; top:{y0}px; width:{w0}px; height:{h0}px;">')
    for lid, lab, short, col in layers:
        inner = [f'<svg viewBox="{" ".join(map(str, VB))}" style="position:absolute; inset:0; width:100%; height:100%; overflow:visible;">', DEFS,
                 f'<rect x="{VB[0]}" y="{VB[1]}" width="{VB[2]}" height="{VB[3]}" rx="220" fill="#0E1930" fill-opacity="0.82" stroke="{col}" stroke-opacity="0.6" stroke-width="22"/>']
        if lid == "photo":
            for _ in range(170):
                x, y = rng.uniform(0, 4600, 2)
                ww, hh = rng.uniform(120, 360, 2)
                inner.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{ww:.0f}" height="{hh:.0f}" rx="24" fill="#5D6E8C" opacity="{rng.uniform(0.25, 0.7):.2f}"/>')
        if lid == "roads":
            for a, b, c, *_ in EDGES:
                (x1, y1), (x2, y2) = NODES[a], NODES[b]
                inner.append(f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="{ROAD[c][0] if c == "local" else "#3C78C0"}" stroke-width="{ROAD[c][1] * 1.3}" stroke-linecap="round"/>')
        if lid == "street":
            row = sorted([k2 for k2 in NODES if k2.split(",")[1] == "15"], key=lambda s: int(s.split(",")[0]))
            inner.append(f'<polyline points="{polyline(row)}" fill="none" stroke="#2A3F62" stroke-width="80" stroke-linecap="round"/>')
            for i in range(6):
                x, y = NODES[f"{3 + 4 * i},15"]
                inner.append(f'<circle class="svcar" cx="{fmt(x)}" cy="{fmt(y)}" r="80" fill="{CORAL}" filter="url(#glow)"/>')
        if lid == "edits":
            for i in range(8):
                x, y = rng.uniform(500, 4200, 2)
                inner.append(f'<g transform="translate({x:.0f} {y:.0f})"><g class="pin">{gm_pin(1.15)}</g></g>')
        inner.append("</svg>")
        f.add(f'<div id="ly-{lid}" class="cam" style="left:{(w0 - size) / 2}px; top:{(h0 - size) / 2}px; width:{size}px; height:{size}px;">' + "".join(inner) + "</div>")
    f.add("</div>")
    f.mark_hud()
    chip = lambda col: f'<span style="display:inline-block; flex:none; width:{26 * u}px; height:{26 * u}px; border-radius:{7 * u}px; background:{col}; box-shadow:0 0 {18 * u}px {col};"></span>'
    if f.portrait:
        y = H * 0.5
        for k, (lid, lab, short, col) in enumerate(layers):
            f.add(f'<div id="lb-{lid}" class="abs caps" style="left:{f.padx + (k % 2) * f.cw * 0.5}px; top:{y + (k // 2) * f.s_label * 1.9}px; font-size:{f.s_label}px; color:{TEXT}; display:flex; align-items:center; gap:{16 * u}px;">{chip(col)}{short}</div>')
        ay = y + H * 0.09
        aw, ah = f.cw * 0.52, H * 0.085
        x = f.padx
    else:
        x, y, w = hud_col(f)
        step = f.s_label * 2.15
        for k, (lid, lab, short, col) in enumerate(layers):
            f.add(f'<div id="lb-{lid}" class="abs caps" style="left:{x}px; top:{y + k * step}px; font-size:{f.s_label}px; color:{TEXT}; display:flex; align-items:center; gap:{16 * u}px;">{chip(col)}{lab}</div>')
        ay = y + 4 * step + f.s_label * 0.6
        aw, ah = w, H * 0.16
    plate_w, plate_h = ah * 1.15, ah * 0.6
    bx, by = aw * 0.06, ah * 0.2
    brk = "".join(f'<div class="brk" style="position:absolute; left:{bx - 10 * u + dx * (plate_w - 10 * u)}px; top:{by - 10 * u + dy * (plate_h - 10 * u)}px; width:{30 * u}px; height:{30 * u}px; '
                  f'border-{"left" if dx == 0 else "right"}:{4 * u}px solid {CORAL}; border-{"top" if dy == 0 else "bottom"}:{4 * u}px solid {CORAL};"></div>'
                  for dx in (0, 1) for dy in (0, 1))
    tx = bx + plate_w + 36 * u
    f.add(f'<div id="ai" class="glass" style="left:{x}px; top:{ay}px; width:{aw}px; height:{ah}px; overflow:hidden;">'
          f'<div style="position:absolute; left:{bx}px; top:{by}px; width:{plate_w}px; height:{plate_h}px; background:#1F4F8C; border-radius:{10 * u}px; display:flex; align-items:center; justify-content:center;">'
          f'<span class="num" style="color:#FFFFFF; font-size:{plate_h * 0.55}px;">1106</span></div>' + brk
          + f'<div class="caps" style="position:absolute; left:{tx}px; top:{ah * (0.2 if f.portrait else 0.24)}px; font-size:{f.s_label * (1 if f.portrait else 0.9)}px; color:{CORAL};">{"AI" if f.portrait else "AI READS"}</div>'
          f'<div class="num" style="position:absolute; left:{tx}px; top:{ah * 0.52}px; font-size:{f.s_label * (1 if f.portrait else 1.25)}px; color:{TEXT};">{"1106" if f.portrait else "NO. 1106"}</div></div>')
    if f.portrait:
        stat(f, "bil", x + aw + 50 * u, ay - 6 * u, "2B+", "A MONTH", size=f.s_stat * 0.78)
        gtag(f, "gmaps", "GOOGLE MAPS · 2025", x, ay + ah + H * 0.035)
    else:
        sy = ay + ah + H * 0.04
        stat(f, "bil", x, sy, "2 billion+", "PEOPLE A MONTH · 2025", size=f.s_stat * 0.62)
        gtag(f, "gmaps", "GOOGLE MAPS", x, sy + f.s_stat * 0.62 + f.s_label * 2.6)
    gap = size * (0.15 if f.portrait else 0.1)
    f.anim(Template("""
const L = ["street", "photo", "roads", "edits"], T4 = [$t1, $t2, $t3, $t4], GAP = $gap;
L.forEach(function (l, k) {
  tl.fromTo("#ly-" + l, {opacity:0, rotationX:60, rotationZ:-40, y: -GAP * (k + 3)},
    {opacity:1, rotationX:60, rotationZ:-40, y: -GAP * (k - 1.5), duration:1.1, ease:"expo.out"}, T4[k]);
  tl.to("#ly-" + l, {rotationZ: -28, duration: Math.max(0.5, $tb - 0.4 - T4[k] - 1.1), ease:"sine.inOut"}, T4[k] + 1.1);
  tl.fromTo("#lb-" + l, {opacity:0, x:-$rise}, {opacity:1, x:0, duration:0.6, ease:"expo.out"}, T4[k] + 0.1);
  tl.to("#ly-" + l, {y: 0, rotationZ: -24, duration:1.2, ease:"expo.inOut"}, $tb - 0.4);
});
tl.fromTo(".svcar", {opacity:0}, {opacity:1, duration:0.3, stagger:0.08}, $t1 + 0.4);
tl.fromTo(".pin", {opacity:0, y:-120}, {opacity:1, y:0, duration:0.5, stagger:0.08, ease:"back.out(2)"}, $t4 + 0.3);
inn("#ai", $tai, 0.7);
tl.fromTo(".brk", {opacity:0, scale:2.4, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.7, ease:"expo.out"}, $tai + 0.4);
inn("#bil", $tb, 0.8); inn("#gmaps", $tb + 0.3, 0.7);
""").substitute(t1=f.t("street"), t2=f.t("photos"), t3=round(f.t("photos") + 0.9, 3), t4=f.t("edits"), tai=f.t("ai"), tb=f.t("billion"),
                gap=round(gap), rise=round(16 * u)))


# ================================================================== B03 · routing
def b03(f):
    u, c = f.u, S["city"]
    sx, sy = NODES[c["src"]]
    dx, dy = NODES[c["dst"]]
    extra = (f'<g id="routeg">{route_lines("route", c["route"])}</g>'
             f'<g id="src">{blue_dot(fmt(sx), fmt(sy), 70)}</g>'
             f'<g transform="translate({fmt(dx)} {fmt(dy)})"><g id="dst">{gm_pin(1.8)}</g></g>')
    f.city("rmap", extra=extra, nodes=True)
    f.cam("rmap", rx0=60, rz0=-40, s0=0.82, rx1=50, rz1=-24, s1=0.98)
    f.mark_hud()
    x, y, w = hud_col(f)
    if f.portrait:
        label(f, "corners", f"CORNERS CHECKED · OF {len(NODES)}", x, y, color=TEXT)
        stat(f, "dj", x, y + f.s_label * 1.9, '<span id="dj-n">0</span>', "DIJKSTRA", color=SEARCH, size=f.s_stat * 0.85)
        stat(f, "as", x + w * 0.5, y + f.s_label * 1.9, '<span id="as-n">0</span>', "A-STAR", color=CORAL, size=f.s_stat * 0.85)
        stat(f, "rt", x, y + f.H * 0.15, f'{c["route_min"]:.1f} min', "SAME ROUTE", size=f.s_stat * 0.55)
        gtag(f, "recipe", "METHOD UNPUBLISHED", x, y + f.H * 0.23)
    else:
        label(f, "corners", f"MY CITY · {len(NODES)} CORNERS", x, y, color=TEXT)
        stat(f, "dj", x, y + f.H * 0.06, '<span id="dj-n">0</span>', "DIJKSTRA · CORNERS CHECKED", color=SEARCH)
        stat(f, "as", x, y + f.H * 0.23, '<span id="as-n">0</span>', "A-STAR · AIMS AT THE DESTINATION", color=CORAL)
        stat(f, "rt", x, y + f.H * 0.4, f'{c["route_min"]:.1f} min', "SAME ROUTE, BOTH WAYS", size=f.s_stat * 0.55)
        gtag(f, "recipe", "GOOGLE DOESN'T PUBLISH ITS RECIPE", x, y + f.H * 0.535)
    dj = json.dumps([k.replace(",", "_") for k in c["dijkstra"]])
    ast = json.dumps([k.replace(",", "_") for k in c["astar"]])
    f.anim(Template("""
tl.fromTo("#rmap-nodes circle", {opacity:0}, {opacity:0.6, duration:0.01, stagger:{each:0.0012, from:"random"}}, $tc);
tl.fromTo("#routeg", {opacity:0}, {opacity:0, duration:0.01}, 0);
tl.fromTo("#src", {opacity:0}, {opacity:1, duration:0.5}, $tc + 0.6);
tl.fromTo("#dst", {opacity:0, y:-160}, {opacity:1, y:0, duration:0.8, ease:"bounce.out"}, $tc + 0.6);
inn("#corners", $tb, 0.6);
const DJ = $dj, AS = $ast;
const djDur = Math.max(1.2, $ta - $td - 0.5), asDur = Math.max(1.0, $ts - $ta - 0.3);
DJ.forEach(function (k, i) { tl.fromTo("#rmap-n-" + k, {fill:"#FFFFFF", attr:{r:60}}, {opacity:1, fill:"$search", attr:{r:40}, duration:0.35, ease:"power2.out", immediateRender:false}, $td + djDur * i / DJ.length); });
inn("#dj", $td, 0.6); count("#dj-n", DJ.length, $td, djDur, 0);
DJ.forEach(function (k) { tl.to("#rmap-n-" + k, {fill:"#2A3A57", attr:{r:30}, duration:0.5}, $ta - 0.3); });
AS.forEach(function (k, i) { tl.fromTo("#rmap-n-" + k, {fill:"#FFFFFF", attr:{r:64}}, {opacity:1, fill:"$coral", attr:{r:40}, duration:0.35, ease:"power2.out", immediateRender:false}, $ta + asDur * i / AS.length); });
inn("#as", $ta, 0.6); count("#as-n", AS.length, $ta, asDur, 0);
tl.to("#rmap-nodes circle", {opacity:0.22, duration:0.6}, $ts);
tl.set("#routeg", {opacity:1}, $ts);
draw("#route", $ts, 1.6, "power2.inOut"); draw("#route-case", $ts, 1.6, "power2.inOut");
inn("#rt", $ts + 0.5, 0.7);
inn("#recipe", $tr, 0.7);
""").substitute(tc=f.t("corners"), tb=f.t("built"), td=f.t("dijkstra"), ta=f.t("astar"), ts=f.t("same"), tr=f.t("recipe"),
                dj=dj, ast=ast, search=SEARCH, coral=CORAL))


# ================================================================== B04 · traffic
def b04(f):
    u, c = f.u, S["city"]
    pts = [NODES[k] for e in c["crash"] for k in e.split("|")]
    mx, my = np.mean([p[0] for p in pts]), np.mean([p[1] for p in pts])
    rng = np.random.default_rng(11)
    phones = []
    for _ in range(90):
        horiz = rng.random() < 0.5
        line = int(rng.integers(0, 30))
        a, b = (f"0,{line}", f"29,{line}") if horiz else (f"{line},0", f"{line},29")
        if a in NODES and b in NODES:
            if rng.random() < 0.5:
                a, b = b, a
            phones.append((NODES[a], NODES[b], float(rng.uniform(0, 1)), float(rng.uniform(0.9, 1.7))))
    extra = ['<g id="phones">']
    for k in range(len(phones)):
        for rr in (66, 50, 38, 30):      # big enough that GATE T never reads a dot as a letter
            extra.append(f'<circle class="ph ph{k}" r="{rr}" fill="#FFFFFF" opacity="0"/>')
    extra.append("</g>")
    extra.append(f'<g transform="translate({mx:.0f} {my:.0f})"><g id="crash" opacity="0">'
                 f'<circle id="crash-ring" r="300" fill="none" stroke="{RED}" stroke-width="30" filter="url(#glow)"/>'
                 f'<circle r="130" fill="{RED}" filter="url(#glow)"/><rect x="-18" y="-80" width="36" height="100" rx="12" fill="#FFFFFF"/>'
                 f'<circle cy="58" r="20" fill="#FFFFFF"/></g></g>')
    f.city("tmap", extra="".join(extra))
    f.cam("tmap", rx0=58, rz0=-34, s0=0.84, rx1=48, rz1=-22, s1=1.02)
    f.mark_hud()
    x, y, w = hud_col(f)
    r = RES["traffic"]
    hist = next(t for t in r if t["phones"] == 0)
    p5 = next(t for t in r if t["phones"] == 500)
    if f.portrait:
        label(f, "since", "ANONYMOUS SPEEDS · 2009", x, y, color=TEXT)
        stat(f, "hist", x, y + f.s_label * 1.9, f'{hist["colour_right"] * 100:.0f}%', "RIGHT FROM HISTORY", size=f.s_stat * 0.62)
        stat(f, "p500", x, y + f.H * 0.16, "500 phones", "SEE THE CRASH", color=RED, size=f.s_stat * 0.62)
    else:
        label(f, "since", "SINCE 2009 · ANONYMOUS SPEEDS", x, y, color=TEXT)
        stat(f, "hist", x, y + f.H * 0.06, f'{hist["colour_right"] * 100:.0f}%', "ROADS COLOURED RIGHT FROM HISTORY ALONE", labw=w)
        stat(f, "miss", x, y + f.H * 0.27, "missed", "THE CRASH, FROM HISTORY ALONE", color=SOFT, size=f.s_stat * 0.5, labw=w)
        stat(f, "p500", x, y + f.H * 0.41, "500 phones", f'TURN THE CRASH RED · {p5["crash_red"] * 100:.0f}% OF ITS ROADS', color=RED, size=f.s_stat * 0.55, labw=w)
        f.add(f'<div id="legend" class="abs caps" style="left:{x}px; top:{y + f.H * 0.585}px; font-size:{f.s_label * 0.85}px; color:{SOFT}; display:flex; gap:{26 * u}px;">'
              + "".join(f'<span style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{36 * u}px; height:{10 * u}px; border-radius:{5 * u}px; background:{col}; box-shadow:0 0 {12 * u}px {col};"></span>{t}</span>'
                        for col, t in ((GREEN, "MOVING"), (AMBER, "SLOW"), (RED, "JAMMED"))) + "</div>")
    js_ph = json.dumps([[a[0], a[1], b[0], b[1], o, sp] for a, b, o, sp in phones])
    f.anim(Template("""
const PH = $ph;
PH.forEach(function (p, k) {
  const els = qa(".ph" + k), o = { s: p[4] };
  const put = function () { els.forEach(function (el, j) { const s = ((o.s - j * 0.012) % 1 + 1) % 1;
    el.setAttribute("cx", p[0] + (p[2] - p[0]) * s); el.setAttribute("cy", p[1] + (p[3] - p[1]) * s); }); };
  put();
  els.forEach(function (el, j) { tl.fromTo(el, {opacity:0}, {opacity: [0.95, 0.45, 0.25, 0.12][j], duration:0.4}, $tp + 0.008 * k); });
  tl.to(o, {s: p[4] + p[5] * (D - $tp) / 8, duration: D - $tp, ease:"none", onUpdate: put}, $tp);
});
inn("#since", $ts, 0.6);
const COL = ["$green", "$amber", "$red"];
[0, 1, 2].forEach(function (lv) { tl.to(".tmap-s.h" + lv, {stroke: COL[lv], duration:0.7, stagger:{each:0.0006, from:"center"}}, $tu); });
if (q("#legend")) inn("#legend", $tu + 0.4, 0.6);
inn("#hist", $th, 0.7);
tl.fromTo("#crash", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.6, ease:"back.out(2.5)"}, $tc);
tl.fromTo("#crash-ring", {scale:0.6, opacity:1, transformOrigin:"50% 50%"}, {scale:1.6, opacity:0, duration:1.2, repeat:5, ease:"expo.out"}, $tc + 0.3);
if (q("#miss")) inn("#miss", $tc + 0.3, 0.6);
inn("#p500", $tf, 0.7);
[0, 1, 2].forEach(function (lv) { tl.to(".tmap-s.p" + lv, {stroke: COL[lv], duration:0.6}, $tr); });
""").substitute(ph=js_ph, tp=f.t("phones"), ts=f.t("since"), tu=f.t("usually"), th=f.t("history"), tc=f.t("crash"),
                tf=f.t("five"), tr=f.t("red"), green=GREEN, amber=AMBER, red=RED))


# ================================================================== B05 · arrival time
def b05(f):
    u = f.u
    ex = S["city"]["eta_example"]
    pts = [NODES[k] for k in ex["path"]]
    km = sum(math.dist(NODES[a], NODES[b]) for a, b in zip(ex["path"], ex["path"][1:])) / 1000
    extra = (f'<g id="tripg">{route_lines("trip", ex["path"])}</g>'
             f'<g transform="translate({fmt(pts[-1][0])} {fmt(pts[-1][1])})"><g id="tdst">{gm_pin(1.7)}</g></g>'
             + "".join(f'<circle class="car" r="{rr}" fill="{fill}" opacity="{op}"/>' for rr, op, fill in ((92, 1, "#FFFFFF"), (68, 1, "#4285F4"), (60, 0.35, "#4285F4"), (48, 0.18, "#4285F4"))))
    f.city("emap", extra=extra, area=(f.W * 0.05, f.H * 0.145, f.W * 0.9, f.H * 0.32) if f.portrait else None)
    f.cam("emap", rx0=56, rz0=-30, s0=0.86, rx1=46, rz1=-18, s1=1.04)
    f.mark_hud()
    x, y, w = hud_col(f)
    mins = round(ex["both"])
    card = (f'<div style="display:flex; align-items:baseline; gap:{18 * u}px;">'
            f'<span style="font-size:{f.s_stat * (0.5 if f.portrait else 0.45)}px; font-weight:500; color:{GM_GREEN};">{mins} min</span>'
            f'<span style="font-size:{f.s_label * 1.15}px; color:{GM_SOFT};">({km:.1f} km)</span></div>'
            + ("" if f.portrait else f'<div style="font-size:{f.s_label * 1.05}px; color:{GM_SOFT}; margin-top:{10 * u}px;">Fastest route now, with live traffic</div>'))
    gm_card(f, "gmeta", x, y, w * (1 if f.portrait else 0.9), card)
    e = RES["eta"]
    if f.portrait:
        sy = y + f.H * 0.13
        label(f, "all", "MY 237 TRIPS · ERROR", x, sy, color=TEXT)
        stat(f, "elim", x, sy + f.s_label * 1.9, f'{e["limits"]["median"] * 100:.0f}%', "SPEED LIMITS", color=SOFT, size=f.s_stat * 0.62)
        stat(f, "eboth", x, sy + f.s_label * 1.9 + f.H * 0.07, f'{e["both"]["median"] * 100:.0f}%', "HISTORY + LIVE", color=CORAL, size=f.s_stat * 0.62)
        gtag(f, "g97", "97%+ ACCURATE", x, sy + f.H * 0.2)
        rows = []
    else:
        rows = [("act", "THE ACTUAL TRIP", ex["actual"], TEXT), ("lim", "SPEED LIMITS SAID", ex["limits"], DIM)]
        mx = ex["actual"] * 1.08
        bh = f.s_label * 1.3
        gapr = bh * 2.9
        bw = w * 0.6
        y0 = y + f.H * 0.19
        for k, (rid, lab, m, col) in enumerate(rows):
            yy = y0 + k * gapr
            glow = f"box-shadow:0 0 {16 * u}px {col};" if col != DIM else ""
            f.add(f'<div id="{rid}" class="abs" style="left:{x}px; top:{yy}px; width:{w}px;">'
                  f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT};">{lab}</div>'
                  f'<div style="display:flex; align-items:center; gap:{18 * u}px; margin-top:{10 * u}px;">'
                  f'<div id="{rid}-bar" style="height:{bh}px; width:{bw * m / mx}px; background:{col}; border-radius:{bh / 2}px; {glow}"></div>'
                  f'<span class="num" style="font-size:{bh * 1.2}px; color:{col if col != DIM else SOFT};">{m:.1f} min</span></div></div>')
        yy = y0 + 2 * gapr + f.H * 0.01
        label(f, "all", "ALL 237 TRIPS · TYPICAL ERROR", x, yy, color=TEXT)
        stat(f, "elim", x, yy + f.s_label * 1.9, f'{e["limits"]["median"] * 100:.0f}%', "SPEED LIMITS", color=SOFT, size=f.s_stat * 0.62)
        stat(f, "eboth", x + w * 0.42, yy + f.s_label * 1.9, f'{e["both"]["median"] * 100:.0f}%', "HISTORY + LIVE", color=CORAL, size=f.s_stat * 0.62)
        gtag(f, "g97", "GOOGLE: ACCURATE FOR OVER 97% OF TRIPS (2020)", x, yy + f.s_label * 1.9 + f.s_stat * 0.62 + f.s_label * 3.0, wrapw=w * 0.8)
    pj = json.dumps([[round(p[0]), round(p[1])] for p in pts])
    rid_js = json.dumps([r_[0] for r_ in rows])
    f.anim(Template("""
draw("#trip", 0.6, 1.4); draw("#trip-case", 0.6, 1.4);
tl.fromTo("#tdst", {opacity:0, y:-160}, {opacity:1, y:0, duration:0.8, ease:"bounce.out"}, 1.6);
const P = $pts, cars = qa(".car"), o = { s: 0 };
const cum = [0]; for (let i = 1; i < P.length; i++) cum.push(cum[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
const at = function (s) { const d = Math.max(0, s) * cum[cum.length - 1]; let i = 1; while (i < cum.length - 1 && cum[i] < d) i++;
  const f2 = (d - cum[i - 1]) / Math.max(1, cum[i] - cum[i - 1]); return [P[i - 1][0] + (P[i][0] - P[i - 1][0]) * f2, P[i - 1][1] + (P[i][1] - P[i - 1][1]) * f2]; };
const lag = [0, 0, 0.012, 0.024];
const put = function () { cars.forEach(function (c, j) { const p = at(o.s - lag[j]); c.setAttribute("cx", p[0]); c.setAttribute("cy", p[1]); }); };
put();
tl.to(o, {s:1, duration: D - 1.8, ease:"sine.inOut", onUpdate: put}, 1.3);
inn("#gmeta", $tb, 0.7);
const R = $rids;
R.forEach(function (r, k) {
  const t0 = [$tl - 0.6, $tl][k];
  inn("#" + r, t0, 0.6);
  tl.fromTo("#" + r + "-bar", {scaleX:0, transformOrigin:"0% 50%"}, {scaleX:1, duration:1.0, ease:"expo.out"}, t0 + 0.1);
});
inn("#all", $tl + 0.6, 0.6); inn("#elim", $tl + 0.8, 0.7); inn("#eboth", $tv + 0.3, 0.7);
inn("#g97", $tg, 0.7);
""").substitute(pts=pj, rids=rid_js, tb=f.t("both"), tl=f.t("limits"), tv=f.t("live"), tg=f.t("google")))


# ================================================================== B06 · how busy
def b06(f):
    u, b = f.u, S["busy"]
    W, H = f.W, f.H
    cafe, shop = NODES["12,17"], NODES["21,8"]
    rng = np.random.default_rng(5)
    vis = []
    for _ in range(60):
        ang, rad = rng.uniform(0, 2 * math.pi), rng.uniform(900, 2000)
        vis.append((cafe[0] + rad * math.cos(ang), cafe[1] + rad * math.sin(ang), bool(rng.random() < b["opt_in"]), float(rng.uniform(0, 1))))
    extra = ['<g id="visitors">']
    for k, (vx, vy, lit, o) in enumerate(vis):
        filt = f' filter={Q}url(#glow){Q}' if lit else ""
        extra.append(f'<circle class="vz{" lit" if lit else " unlit"}" id="vz{k}" cx="{vx:.0f}" cy="{vy:.0f}" r="{44 if lit else 30}" fill="{CYAN if lit else DIM}" opacity="0"{filt}/>')
    extra.append("</g>")
    extra.append(f'<g transform="translate({cafe[0]:.0f} {cafe[1]:.0f})"><circle id="cafe-glow" r="260" fill="{GM_PIN}" opacity="0.25" filter="url(#glow2)"/>{gm_pin(1.8)}</g>')
    extra.append(f'<g id="shop" transform="translate({shop[0]:.0f} {shop[1]:.0f})" opacity="0">{gm_pin(1.3).replace(GM_PIN, "#7A7F87").replace("#B31412", "#4A4E55").replace("#8C0E0D", "#3A3D42")}</g>')
    area = (0, H * 0.145, W, H * 0.3) if f.portrait else (W * 0.05, H * 0.13, W * 0.47, H * 0.74)
    f.city("bzmap", extra="".join(extra), area=area)
    f.cam("bzmap", rx0=58, rz0=-30, s0=0.9, rx1=50, rz1=-20, s1=1.12)
    f.mark_hud()
    # the Popular times card, as the app draws it (night mode)
    if f.portrait:
        cx, cy, cw = f.padx, H * 0.475, f.cw
        chh = H * 0.06
    else:
        cx, cy, cw = W * 0.53, H * 0.215, W * 0.4
        chh = H * 0.24
    pad = 30 * u
    iw = cw - 2 * pad * 1.15
    hours = b["hours"]
    slot = iw / len(hours)
    ipk = hours.index(b["peak_est"])
    bars = [f'<svg id="chart" viewBox="0 0 {iw} {chh}" style="display:block; width:{iw}px; height:{chh}px; overflow:visible; margin-top:{22 * u}px;">']
    for i, (tv, ev) in enumerate(zip(b["true"], b["est"])):
        x = i * slot + slot * 0.1
        bw = slot * 0.8
        pk = i == ipk
        bars.append(f'<rect class="est" x="{x:.1f}" y="{chh - ev * chh:.1f}" width="{bw:.1f}" height="{ev * chh:.1f}" rx="{4 * u}" fill="{GM_BLUE}" fill-opacity="{1 if pk else 0.55}"/>')
        bars.append(f'<rect class="ghost" x="{x:.1f}" y="{chh - tv * chh:.1f}" width="{bw:.1f}" height="{tv * chh:.1f}" rx="{4 * u}" fill="none" stroke="#FFFFFF" stroke-width="{3 * u}" stroke-dasharray="{7 * u} {5 * u}" opacity="0"/>')
    bars.append(f'<line x1="0" y1="{chh}" x2="{iw}" y2="{chh}" stroke="{GM_LINE}" stroke-width="{2 * u}"/>')
    for i, h in enumerate(hours):
        if h % 3 == 0:
            bars.append(f'<text x="{i * slot + slot / 2:.1f}" y="{chh + f.s_label * 1.25:.1f}" text-anchor="middle" font-family="Roboto" font-size="{f.s_label * 0.95}" fill="{GM_SOFT}">{h % 12 or 12}{"a" if h < 12 else "p"}</text>')
    bars.append("</svg>")
    chev = f'<svg width="{f.s_label * 0.7}" height="{f.s_label * 0.45}" viewBox="0 0 10 6" style="margin-left:{10 * u}px;"><path d="M1 1 L5 5 L9 1" fill="none" stroke="{GM_TEXT}" stroke-width="1.6"/></svg>'
    inner = (f'<div style="display:flex; align-items:center; justify-content:space-between;">'
             f'<span style="font-size:{f.s_label * 1.25}px; font-weight:500;">Popular times</span>'
             f'<span style="display:flex; align-items:center; font-size:{f.s_label}px; padding:{8 * u}px {18 * u}px; border:{1.5 * u}px solid {GM_LINE}; border-radius:{40 * u}px;">Fridays{chev}</span></div>'
             f'<div id="usual" style="font-size:{f.s_label * 0.95}px; color:{GM_SOFT}; margin-top:{12 * u}px;"><span style="color:{GM_TEXT}; font-weight:500;">1 PM:</span> Usually as busy as it gets</div>'
             + "".join(bars) + f'<div style="height:{f.s_label * (1.6 if not f.portrait else 1.25)}px;"></div>')
    gm_card(f, "ptcard", cx, cy, cw, inner)
    cardh = chh + f.s_label * 5.6 + 2 * pad + 22 * u
    ky = cy + cardh + f.s_label * 0.8
    if f.portrait:
        f.add(f'<div id="key" class="abs caps" style="left:{cx}px; top:{ky}px; font-size:{f.s_label}px; color:{SOFT}; display:flex; align-items:center; gap:{14 * u}px;">'
              f'<span style="display:inline-block; width:{30 * u}px; height:{18 * u}px; border:{3 * u}px dashed #FFFFFF; border-radius:{4 * u}px;"></span>DASHED: REAL CROWD</div>')
        shx, shy = W * 0.5, H * 0.37
    else:
        f.add(f'<div id="key" class="abs caps" style="left:{cx}px; top:{ky}px; font-size:{f.s_label * 0.9}px; color:{SOFT}; display:flex; gap:{30 * u}px;">'
              f'<span style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{30 * u}px; height:{18 * u}px; background:{GM_BLUE}; opacity:0.6; border-radius:{4 * u}px;"></span>COUNTED + PRIVACY NOISE</span>'
              f'<span style="display:flex; align-items:center; gap:{10 * u}px;"><span style="display:inline-block; width:{30 * u}px; height:{18 * u}px; border:{3 * u}px dashed #FFFFFF; border-radius:{4 * u}px;"></span>REAL CROWD</span></div>')
        sy = ky + f.s_label * 2.4
        stat(f, "cnt", cx, sy, f'{b["counted"]:,}<span style="color:{SOFT}; font-weight:700;"> / {b["visitors"]:,}</span>', "VISITS COUNTED · A QUARTER", size=f.s_stat * 0.42)
        shx, shy = cx, sy + f.s_stat * 0.42 + f.s_label * 2.8
    f.add(f'<div id="shopcard" class="glass" style="left:{shx}px; top:{shy}px; padding:{16 * u}px {24 * u}px; display:flex; flex-direction:{"column" if f.portrait else "row"}; gap:{f.portrait and 4 * u or 22 * u}px; align-items:{"flex-start" if f.portrait else "center"};">'
          f'<span class="caps" style="font-size:{f.s_label}px; color:{TEXT};">QUIET SHOP</span>'
          f'<span class="serif" style="font-size:{f.s_label * 1.2}px; color:{TEXT}; font-style:italic;">Not enough data</span>'
          + ("" if f.portrait else f'<span class="caps" style="font-size:{f.s_label * 0.9}px; color:{SOFT};">{b["shop_counted"]} VISITS COUNTED</span>') + "</div>")
    vz = json.dumps([[round(v[0]), round(v[1]), v[3]] for v in vis])
    f.anim(Template("""
const V = $vz, C = [$cx, $cy];
V.forEach(function (v, k) {
  const el = q("#vz" + k), o = { s: v[2] };
  const put = function () { const s = o.s % 1; el.setAttribute("cx", v[0] + (C[0] - v[0]) * s); el.setAttribute("cy", v[1] + (C[1] - v[1]) * s);
    el.setAttribute("r", (el.classList.contains("lit") ? 44 : 30) * (s > 0.9 ? (1 - s) * 10 : 1)); };
  put();
  tl.fromTo(el, {opacity:0}, {opacity:0.9, duration:0.4}, 0.6 + 0.02 * k);
  tl.to(o, {s: v[2] + 3, duration: D - 0.6, ease:"none", onUpdate: put}, 0.6);
});
tl.fromTo("#cafe-glow", {scale:0.7, transformOrigin:"50% 50%"}, {scale:1.2, duration:1.6, yoyo:true, repeat:8, ease:"sine.inOut"}, 0.5);
tl.fromTo(".unlit", {fill:"$dim"}, {fill:"#2B3A55", duration:0.6}, $to);
inn("#ptcard", $tq - 0.2, 0.8);
tl.fromTo(".est", {scaleY:0, transformOrigin:"50% 100%"}, {scaleY:1, duration:0.7, stagger:0.045, ease:"expo.out"}, $tn);
tl.fromTo("#usual", {opacity:0}, {opacity:1, duration:0.5}, $t1);
if (q("#cnt")) inn("#cnt", $tq + 0.4, 0.7);
tl.to(".ghost", {opacity:1, duration:0.6, stagger:0.03}, $tm);
inn("#key", $tm, 0.6);
tl.to("#shop", {opacity:1, duration:0.5}, $tsh); inn("#shopcard", $tsh, 0.7);
""").substitute(vz=vz, cx=round(cafe[0]), cy=round(cafe[1]), dim=DIM, to=f.t("opted"), tq=f.t("quarter"), tn=f.t("noise"),
                tm=f.t("matched"), t1=f.t("one"), tsh=f.t("shop")))


# ================================================================== B07 · how crowded
def b07(f):
    u, bus = f.u, S["bus"]
    W, H = f.W, f.H
    line = sorted([k for k in NODES if k.split(",")[0] == "10"], key=lambda s: int(s.split(",")[1]))
    stops = line[2::4]
    extra = (f'<polyline id="busline-glow" points="{polyline(line)}" fill="none" stroke="{CORAL}" stroke-width="160" stroke-opacity="0.35" stroke-linecap="round" filter="url(#glow2)"/>'
             f'<polyline id="busline" points="{polyline(line)}" fill="none" stroke="{CORAL}" stroke-width="64" stroke-linecap="round"/>'
             + "".join(f'<g transform="translate({fmt(NODES[s][0])} {fmt(NODES[s][1])})"><circle class="stop" r="74" fill="#0B1528" stroke="#FFFFFF" stroke-width="22"/></g>' for s in stops)
             + f'<g id="bus"><rect x="-170" y="-110" width="340" height="220" rx="60" fill="#FFFFFF" filter="url(#glow)"/><rect x="-120" y="-60" width="240" height="66" rx="18" fill="{CORAL}"/></g>')
    area = (0, H * 0.145, W, H * 0.28) if f.portrait else (W * 0.05, H * 0.13, W * 0.45, H * 0.66)
    f.city("bmap", extra=extra, area=area)
    f.cam("bmap", rx0=58, rz0=-48, s0=0.9, rx1=50, rz1=-38, s1=1.08)
    f.mark_hud()
    opts = ["Many empty seats", "Few empty seats", "Standing room only"]
    radio = lambda sel: (f'<span style="display:inline-block; flex:none; width:{28 * u}px; height:{28 * u}px; border-radius:50%; border:{4 * u}px solid {GM_BLUE if sel else GM_SOFT}; '
                         f'box-shadow: inset 0 0 0 {6 * u}px {GM_CARD}; background:{GM_BLUE if sel else "transparent"};"></span>')
    tsz, osz = (f.s_label * 1.08, f.s_label) if f.portrait else (f.s_label * 1.25, f.s_label * 1.05)
    ask = (f'<div style="font-size:{tsz}px; font-weight:500; white-space:nowrap;">How crowded was it?</div>'
           + "".join(f'<div class="opt" style="margin-top:{12 * u}px; display:flex; align-items:center; gap:{18 * u}px; font-size:{osz}px; white-space:nowrap;">{radio(i == 1)}{o}</div>'
                     for i, o in enumerate(opts)))
    if f.portrait:
        x, y, w = f.padx, H * 0.5, f.cw
        gm_card(f, "ask", x, y, w * 0.7, ask, pad=22 * u)
        f.add(f'<div id="gtfs" class="glass" style="left:{x}px; top:{H * 0.44}px; padding:{14 * u}px {22 * u}px; display:flex; align-items:baseline; gap:{18 * u}px;">'
              f'<span class="num" style="font-size:{f.s_label * 1.3}px; color:{TEXT};">GTFS</span>'
              f'<span class="caps" style="font-size:{f.s_label}px; color:{SOFT};">OPEN TIMETABLES</span></div>')
        sy = y + H * 0.165
        lab_pred, lab_truth = "PREDICTED", "NEXT DAY"
    else:
        x, y, w = W * 0.52, H * 0.215, W - f.padx - W * 0.52
        hw = w * 0.44
        f.add(f'<div id="gtfs" class="glass" style="left:{x}px; top:{y}px; width:{hw}px; padding:{22 * u}px {26 * u}px;">'
              f'<div class="num" style="font-size:{f.s_stat * 0.42}px; color:{TEXT};">GTFS</div>'
              f'<div class="caps" style="font-size:{f.s_label * 0.9}px; color:{SOFT}; margin-top:{10 * u}px; white-space:normal; line-height:1.4;">OPEN FORMAT: TIMETABLES + LIVE VEHICLES</div></div>')
        gm_card(f, "ask", x + hw + 30 * u, y, w - hw - 30 * u, ask)
        sy = y + H * 0.3
        lab_pred, lab_truth = "PREDICTED FROM ANSWERS", "THE NEXT DAY"
    n = len(bus["trips"])
    lw = 380 * u if f.portrait else 0          # phone: the row label sits left of its cells
    cellw = (w - lw) / n
    ch = f.s_label * (0.9 if f.portrait else 1.3)
    LV = [GREEN, AMBER, RED]
    rows = []
    for r_, (key, lab) in enumerate((("pred", lab_pred), ("truth", lab_truth))):
        yy = (r_ * (ch + f.s_label * 0.9) + f.s_label * 0.25) if f.portrait else (r_ * (ch + f.s_label * 1.7) + f.s_label * 1.45)
        ltop = yy + ch / 2 - f.s_label * 0.6 if f.portrait else yy - f.s_label * 1.35
        rows.append(f'<div class="caps" style="position:absolute; left:0; top:{ltop}px; font-size:{f.s_label * (1 if f.portrait else 0.85)}px; color:{SOFT};">{lab}</div>')
        for i, lv in enumerate(bus[key]):
            col = LV[lv] if lv >= 0 else "#1E2A40"
            rows.append(f'<div class="cell c{r_}" style="position:absolute; left:{lw + i * cellw + cellw * 0.1}px; top:{yy}px; width:{cellw * 0.8}px; height:{ch}px; background:{col}; border-radius:{ch / 2}px; box-shadow:0 0 {10 * u}px {col};"></div>')
    miss = [i for i in range(n) if bus["pred"][i] >= 0 and bus["pred"][i] != bus["truth"][i]]
    for i in miss:
        mt, mh = ((f.s_label * 0.25 + ch + 4 * u, f.s_label * 0.9 - 8 * u) if f.portrait else (f.s_label * 1.45 + ch + 4 * u, f.s_label * 1.9 - 8 * u))
        rows.append(f'<div class="miss" style="position:absolute; left:{lw + i * cellw + cellw * 0.5 - 3 * u}px; top:{mt}px; width:{6 * u}px; height:{mh}px; background:#FFFFFF; border-radius:{3 * u}px;"></div>')
    sh = (2 * ch + f.s_label * 1.4) if f.portrait else (2 * ch + f.s_label * 3.4)
    f.add(f'<div id="strip" class="abs" style="left:{x}px; top:{sy}px; width:{w}px; height:{sh}px;">' + "".join(rows) + "</div>")
    if not f.portrait:
        label(f, "striplab", f"ONE BUS ROUTE · {n} TRIPS · WHITE MARK: A MISS", x, sy - f.s_label * 1.7, color=TEXT)
    if f.portrait:
        sz = f.s_stat * 0.5
        f.add(f'<div id="accfew" class="abs" style="left:{x + w * 0.75}px; top:{y}px;">'
              f'<div id="acc"><div class="num" style="font-size:{sz}px; color:{CORAL};">{bus["acc"] * 100:.0f}%</div>'
              f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT}; margin-top:{sz * 0.16}px;">RIGHT</div></div>'
              f'<div id="few" style="margin-top:{40 * u}px;"><div class="num" style="font-size:{sz}px; color:{TEXT};">3/100</div>'
              f'<div class="caps" style="font-size:{f.s_label}px; color:{SOFT}; margin-top:{sz * 0.16}px;">ASKED</div></div></div>')
    else:
        sty = sy + sh + f.s_label * 0.8
        stat(f, "acc", x, sty, f'{bus["acc"] * 100:.0f}%', "OF TRIPS RIGHT", color=CORAL, size=f.s_stat * 0.55)
        stat(f, "few", x + w * 0.5, sty, "3 in 100", "RIDERS ANSWERED", size=f.s_stat * 0.55)
    sp = json.dumps([[round(NODES[s][0]), round(NODES[s][1])] for s in line])
    f.anim(Template("""
draw("#busline", 0.5, 1.3); draw("#busline-glow", 0.5, 1.3);
tl.fromTo(".stop", {opacity:0, scale:0.3, transformOrigin:"50% 50%"}, {opacity:1, scale:1, duration:0.5, stagger:0.08, ease:"back.out(2.5)"}, 1.1);
const P = $pts, bus = q("#bus"), o = {s:0};
const put = function () { const d = o.s * (P.length - 1), i = Math.min(P.length - 2, Math.floor(d)), f2 = d - i;
  bus.setAttribute("transform", "translate(" + (P[i][0] + (P[i + 1][0] - P[i][0]) * f2) + " " + (P[i][1] + (P[i + 1][1] - P[i][1]) * f2) + ")"); };
put();
tl.to(o, {s:1, duration: D - 1.5, ease:"none", onUpdate: put}, 1.0);
inn("#gtfs", $ta, 0.7);
inn("#ask", $tr, 0.7);
tl.fromTo(".opt", {opacity:0, x:-12}, {opacity:1, x:0, duration:0.4, stagger:0.12}, $tr + 0.3);
if (q("#striplab")) inn("#striplab", $tt - 0.2, 0.6);
inn("#few", $tt, 0.6);
tl.fromTo(".c0", {opacity:0, scaleX:0, transformOrigin:"0% 50%"}, {opacity:1, scaleX:1, duration:0.35, stagger:0.025, ease:"expo.out"}, $tt);
tl.fromTo(".c1", {opacity:0, scaleX:0, transformOrigin:"0% 50%"}, {opacity:1, scaleX:1, duration:0.35, stagger:0.025, ease:"expo.out"}, $te - 0.5);
tl.fromTo(".miss", {opacity:0}, {opacity:0.85, duration:0.3}, $te + 0.5);
inn("#acc", $te, 0.7);
""").substitute(pts=sp, ta=f.t("agencies"), tr=f.t("riders"), tt=f.t("three"), te=f.t("eighty")))


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06, "B07": b07}


def build(only=None):
    n = 0
    for bid, fn in BUILDERS.items():
        if only and bid not in only:
            continue
        for portrait in (False, True):
            f = Frame(bid, portrait)
            f.head()
            fn(f)
            f.foot()
            (HF / f"{bid}-{'v' if portrait else 'l'}.html").write_text(f.html(), encoding="utf-8", newline="\n")
            n += 1
    print("wrote", n, "compositions to", HF)


def render(only=None):
    (HERE / "media").mkdir(exist_ok=True)
    (HERE / "pantry").mkdir(exist_ok=True)
    for bid in BUILDERS:
        if only and bid not in only:
            continue
        for portrait in (False, True):
            src = f"{bid}-{'v' if portrait else 'l'}.html"
            dst = HERE / ("pantry" if portrait else "media") / (f"{bid}-916.mp4" if portrait else f"{bid}.mp4")
            if dst.exists() and dst.stat().st_mtime > (HF / src).stat().st_mtime:
                print("up to date", dst.name); continue
            print("render", src, "->", dst.relative_to(HERE), flush=True)
            # frames go to D: (never C:); D: has the room for the frame cache
            env = dict(os.environ, TEMP=TMPD, TMP=TMPD, HYPERFRAMES_NO_UPDATE_CHECK="1", HYPERFRAMES_NO_TELEMETRY="1")
            subprocess.run(["npx.cmd", "--no-install", "hyperframes", "render", "-c", src, "-o", str(dst), "-q", "delivery",
                            "--workers", "2", "--quiet"], cwd=HF, check=True, env=env, stdin=subprocess.DEVNULL)


if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if a.startswith("B")] or None
    build(only)
    if "--render" in sys.argv:
        render(only)
