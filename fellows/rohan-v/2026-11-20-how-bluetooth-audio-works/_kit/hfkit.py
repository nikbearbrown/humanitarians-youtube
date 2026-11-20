"""Shared HyperFrames page kit for the week-12 films (HTML HUD over a three.js canvas).

Each beat is one root composition per aspect: hyperframes/B0x-l.html (3840x2160) and B0x-v.html (2160x3840).
The page holds (1) a WebGL canvas drawn by hyperframes/scenes/B0x.js through assets/kit3.js, seeked frame by frame
via HyperFrames' hf-seek event (no clocks, no rAF), and (2) an HTML HUD (title, numbers, tags) revealed by a paused
GSAP timeline on the beat's word-clock cues. On the phone the HUD is re-laid out as one evenly spaced column
under the 3D stage (no overlaps; no closing line, its room goes to the column).
"""
import json
import os
import re
import subprocess
from pathlib import Path
from string import Template

TMPD = "D:/Rohan/Claude/HyperFrames/tmp"

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
  background: $GROUND; }
.abs { position: absolute; }
.serif { font-family: "Source Serif 4", serif; }
.caps { font-family: Inter, sans-serif; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; white-space: nowrap; }
.num { font-family: Inter, sans-serif; font-weight: 900; line-height: 0.95; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; white-space: nowrap; }
.glass { position: absolute; background: $GLASS; border: ${BW}px solid $GLINE; border-radius: ${RAD}px;
  box-shadow: 0 ${SH}px ${SH2}px rgba(0,0,0,0.35); }
#gl { position: absolute; }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="$D" data-width="$W" data-height="$H">
<div id="stage" class="clip" data-start="0" data-duration="$D" data-track-index="0" data-layout-allow-overlap data-layout-allow-overflow
 style="position:absolute; inset:0;">
""")

FOOT = Template("""</div>
</div>
<script type="application/json" id="env">$ENV</script>
<script>
const tl = gsap.timeline({ paused: true });
const D = $D;
function q(s) { return document.querySelector(s); }
function qa(s) { return Array.from(document.querySelectorAll(s)); }
function inn(sel, t, dur, from) {
  tl.fromTo(sel, Object.assign({ opacity: 0, y: $RISE, filter: "blur(10px)" }, from || {}),
    { opacity: 1, y: 0, x: 0, filter: "blur(0px)", duration: dur || 0.7, ease: "expo.out" }, t);
}
function out(sel, t, dur) { tl.to(sel, { opacity: 0.28, duration: dur || 0.5, ease: "power2.out" }, t); }
function count(sel, to, t, dur, dec, suffix) {
  const o = { v: 0 }, el = q(sel);
  const show = function () { el.textContent = o.v.toLocaleString("en-US", { minimumFractionDigits: dec || 0, maximumFractionDigits: dec || 0 }) + (suffix || ""); };
  show();
  tl.to(o, { v: to, duration: dur || 1.2, ease: "power3.out", onUpdate: show }, t);
}
function grow(sel, t, dur, axis) {
  tl.fromTo(sel, axis === "y" ? { scaleY: 0, transformOrigin: "50% 100%" } : { scaleX: 0, transformOrigin: "0% 50%" },
    axis === "y" ? { scaleY: 1, duration: dur || 1.0, ease: "expo.out" } : { scaleX: 1, duration: dur || 1.0, ease: "expo.out" }, t);
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
tl.fromTo("#gl", { opacity: 0 }, { opacity: 1, duration: 0.9, ease: "power2.out" }, 0);
tl.fromTo("#rule", { scaleX: 0, transformOrigin: "0% 50%" }, { scaleX: 1, duration: 1.0, ease: "expo.out" }, 0.1);
tl.fromTo("#spark", { opacity: 0, x: -$RISE }, { opacity: 1, x: 0, duration: 0.8, ease: "expo.out" }, $TSPARK);
tl.to({}, { duration: 0.01 }, D - 0.01);
window.__timelines["main"] = tl;
tl.seek(0);
</script>
<script type="module">
import * as K from "./assets/kit3.js";
import scene from "./scenes/$BID.js";
const env = JSON.parse(document.getElementById("env").textContent);
const renderAt = scene(K, document.getElementById("gl"), env);
K.drive(renderAt);
</script>
</body>
</html>
""")

HUDJS = Template("""
(function () {   // HUD column: rows by authored top, then spread evenly between $Y0 and $Y1 (no overlaps).
  // Re-run once the web fonts are in (a serif line can wrap differently than its fallback) and on every seek,
  // so the measured heights are the rendered ones. Idempotent: positions depend only on the heights.
  function layout() {
  // HyperFrames hides a clip outside its active range (display:none -> every height reads 0): measure with the
  // stage shown, then put it back exactly as it was.
  const st = document.getElementById("stage"), oldDisp = st.style.display, oldVis = st.style.visibility;
  if (getComputedStyle(st).display === "none") { st.style.display = "block"; st.style.visibility = "hidden"; }
  const els = qa(".hud").map(function (e) { return { e: e, t: parseFloat(e.dataset.top) }; }).sort(function (a, b) { return a.t - b.t; });
  const rows = [];
  els.forEach(function (o) { const last = rows[rows.length - 1]; if (last && Math.abs(o.t - last.t) <= $TOL) last.items.push(o); else rows.push({ t: o.t, items: [o] }); });
  rows.forEach(function (row) { row.h = Math.max.apply(null, row.items.map(function (o) { return o.e.offsetHeight; })); });
  st.style.display = oldDisp; st.style.visibility = oldVis;
  if (!rows.length || rows.some(function (row) { return !(row.h > 0); })) return;     // not measurable yet: keep authored tops
  const total = rows.reduce(function (a, row) { return a + row.h; }, 0);
  const top = $TOPALIGN;
  const gap = Math.min($GMAX, Math.max(18, ($Y1 - $Y0 - total) / (rows.length + (top ? -1 : 1))));
  let y = top ? $Y0 : $Y0 + gap;
  rows.forEach(function (row) { row.items.forEach(function (o) { o.e.style.top = y + "px"; }); y += row.h + gap; });
  }
  layout();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(layout);
  window.addEventListener("hf-seek", layout);
})();
""")


class Look:
    """Per-film palette + copy tables."""

    def __init__(self, here, beats, chapter, ptitle, sparks, pal, logo):
        self.here, self.beats, self.chapter, self.ptitle, self.sparks = here, beats, chapter, ptitle, sparks
        self.p, self.logo = pal, logo


class Frame:
    def __init__(self, look, bid, portrait):
        self.L, self.bid, self.portrait = look, bid, portrait
        self.p = look.p
        self.W, self.H = (2160, 3840) if portrait else (3840, 2160)
        self.u = 2.0
        self.padx = self.W * (0.067 if portrait else 0.065)
        self.cw = self.W - 2 * self.padx
        b = look.beats[bid]
        self.D = round(b["actual_duration_s"], 3)
        self.cues = b["shot"]["remotion"]["props"].get("cues", {})
        self.title = look.ptitle[bid] if portrait else b["shot"]["remotion"]["props"]["title"]
        self.parts, self.js = [], []
        self.hud_start = self.hud_end = None
        self.data = {}
        H = self.H
        if portrait:      # phone type scale (fractions of height); the 4K phone floor is ~72 px
            self.s_title, self.s_label, self.s_stat, self.s_spark = H * 0.044, H * 0.0215, H * 0.062, H * 0.0425
        else:
            self.s_title, self.s_label, self.s_stat, self.s_spark = 128, 50, 200, 64
        # the 3D stage
        if portrait:
            self.area = (self.W * 0.05, H * 0.14, self.W * 0.9, H * 0.30)
        else:
            self.area = (self.W * 0.055, H * 0.17, self.W * 0.545, H * 0.68)
        # the HUD column
        if portrait:
            self.hx, self.hy, self.hw = self.padx, H * 0.455, self.cw
        else:
            self.hx, self.hy, self.hw = self.W * 0.615, H * 0.215, self.W - self.padx - self.W * 0.615

    def t(self, cue, default=0.0):
        return round(self.cues.get(cue, default) * self.D, 3)

    def add(self, html):
        self.parts.append(html)

    def anim(self, js):
        self.js.append(js)

    def mark_hud(self):
        self.hud_start = len(self.parts)

    def head(self):
        p = self.p
        y0 = self.H * (0.05 if self.portrait else 0.075)
        self.add(f'<div id="chapter" class="abs caps" style="left:{self.padx}px; top:{y0}px; font-size:{self.s_label * (1 if self.portrait else 0.8)}px; color:{p["chap"]};">{self.L.chapter[self.bid]}</div>')
        self.add(f'<div id="title" class="abs serif" style="left:{self.padx}px; top:{y0 + self.s_label * 1.7}px; font-size:{self.s_title}px; white-space:nowrap; '
                 f'font-weight:600; color:{p["text"]}; line-height:1.05; letter-spacing:-0.01em;">{self.title}</div>')

    def stage(self, fade=(50, 93)):
        x, y, w, h = self.area
        a, b = fade
        mask = f"radial-gradient(ellipse 50% 50% at 50% 50%, #000 {a}%, transparent {b}%)"
        self.add(f'<canvas id="gl" width="{round(w)}" height="{round(h)}" style="left:{x}px; top:{y}px; width:{w}px; height:{h}px; '
                 f'-webkit-mask-image:{mask}; mask-image:{mask};"></canvas>')

    def foot(self):
        self.hud_end = len(self.parts)
        p, u = self.p, self.u
        if self.portrait:
            self.add('<div id="rule" class="abs" style="display:none"></div><div id="spark" class="abs" style="display:none"></div>')
            return
        txt = self.L.sparks[self.bid]
        self.add(f'<div id="rule" class="abs" style="left:{self.padx}px; top:{self.H * 0.85}px; width:{self.cw}px; height:{2 * u}px; '
                 f'background:linear-gradient(90deg, rgba(255,255,255,0.22), rgba(255,255,255,0.04));"></div>')
        self.add(f'<div id="spark" class="abs" style="left:{self.padx}px; top:{self.H * 0.875}px; display:flex; align-items:baseline; gap:{18 * u}px; width:{self.cw}px;">'
                 f'<span style="display:inline-block; width:{48 * u}px; height:{4 * u}px; background:{p["acc"]}; border-radius:{2 * u}px; transform:translateY(-{self.s_spark * 0.3}px);"></span>'
                 f'<span class="serif" style="font-style:italic; font-size:{self.s_spark}px; color:{p["text"]}; line-height:1.2;">{txt}</span></div>')

    def html(self):
        if self.hud_start is not None:
            for i in range(self.hud_start, self.hud_end if self.hud_end is not None else len(self.parts)):
                m = re.match(r'<div id="([^"]+)" class="([^"]*)" style="([^"]*?)top:([\d.]+)px;', self.parts[i])
                if m:
                    self.parts[i] = self.parts[i].replace(f'class="{m.group(2)}"', f'class="{m.group(2)} hud" data-top="{m.group(4)}"', 1)
            if self.portrait:
                self.js.insert(0, HUDJS.substitute(Y0=round(self.H * 0.455), Y1=round(self.H * 0.86), TOL=round(self.H * 0.012),
                                                   TOPALIGN="false", GMAX=round(self.H * 0.06)))
            else:
                self.js.insert(0, HUDJS.substitute(Y0=round(self.hy), Y1=round(self.H * 0.83), TOL=round(self.H * 0.012),
                                                   TOPALIGN="true", GMAX=round(self.H * 0.05)))
        last = max(self.cues.values()) if self.cues else 0.8
        tspark = round(min(max(last + 0.05, 0.62), 0.9) * self.D, 3)
        p = self.p
        x, y, w, h = self.area
        env = {"W": round(w), "H": round(h), "X": round(x), "Y": round(y), "D": self.D, "portrait": self.portrait,
               "cue": {k: round(v * self.D, 3) for k, v in self.cues.items()}, "data": self.data}
        head = HEAD.substitute(W=self.W, H=self.H, D=self.D, BG=p["bg"], GROUND=p["ground_v" if self.portrait else "ground_l"], TEXT=p["text"], GLASS=p["glass"],
                               GLINE=p["gline"], BW=round(1.5 * self.u, 1), RAD=round(22 * self.u), SH=round(10 * self.u),
                               SH2=round(40 * self.u))
        return head + "\n".join(self.parts) + FOOT.substitute(
            D=self.D, JS="\n".join(self.js), RISE=round(18 * self.u), TSPARK=tspark, BID=self.bid,
            ENV=json.dumps(env).replace("</", "<\\/"))

    # ---------------------------------------------------------------- HUD pieces
    def stat(self, sid, x, y, value_html, lab, color=None, size=None, labw=None):
        p = self.p
        s = size or self.s_stat
        wrap = f"white-space:normal; width:{labw}px; line-height:1.35;" if labw else ""
        self.add(f'<div id="{sid}" class="abs" style="left:{x}px; top:{y}px;">'
                 f'<div id="{sid}-v" class="num" style="font-size:{s}px; color:{color or p["text"]};">{value_html}</div>'
                 f'<div class="caps" style="font-size:{self.s_label}px; color:{p["soft"]}; margin-top:{s * 0.16}px; {wrap}">{lab}</div></div>')

    def pin(self, pid, text, color=None, size=None):
        """A label the 3D scene places over a point every frame (K.pin); centred on that point."""
        self.add(f'<div id="{pid}" class="abs caps pin" style="left:0px; top:0px; opacity:0; transform:translate(-50%,-50%); '
                 f'font-size:{size or self.s_label}px; color:{color or self.p["soft"]}; text-shadow:0 0 {12 * self.u}px #000, 0 0 {4 * self.u}px #000;">{text}</div>')

    def label(self, lid, text, x, y, color=None, size=None, wrapw=None):
        wrap = f"white-space:normal; width:{wrapw}px; line-height:1.35;" if wrapw else ""
        self.add(f'<div id="{lid}" class="abs caps" style="left:{x}px; top:{y}px; font-size:{size or self.s_label}px; color:{color or self.p["soft"]}; {wrap}">{text}</div>')

    def note(self, nid, html, x, y, w, size=None, color=None):
        """A short serif sentence (body copy in the HUD)."""
        s = size or self.s_label * 1.25
        self.add(f'<div id="{nid}" class="abs serif" style="left:{x}px; top:{y}px; width:{w}px; font-size:{s}px; line-height:1.3; color:{color or self.p["text"]};">{html}</div>')

    def tag(self, gid, text, x, y, wrapw=None, chip_bg=None):
        """LOGO LAW: the company's own mark beside its name. Wraps inside the HUD column if it is long."""
        s, p = self.s_label, self.p
        wrapw = wrapw or (self.hw - s * 4.6)
        wrap = f"white-space:normal; max-width:{wrapw}px; line-height:1.35;"
        self.add(f'<div id="{gid}" class="glass" style="left:{x}px; top:{y}px; display:flex; align-items:center; gap:{s * 0.6}px; padding:{s * 0.55}px {s * 0.8}px;">'
                 f'<span style="display:flex; flex:none; width:{s * 1.9}px; height:{s * 1.9}px; border-radius:{s * 0.45}px; background:{chip_bg or p["chip"]}; align-items:center; justify-content:center;">'
                 f'<img src="assets/{self.L.logo}" style="height:{s * 1.3}px;" /></span>'
                 f'<span class="caps" style="font-size:{s}px; color:{p["text"]}; {wrap}">{text}</span></div>')

    def bar(self, bid_, x, y, w, frac, color, lab_left, lab_right, h=None):
        """A labelled horizontal bar: label left, value right, track + fill below."""
        s, p, u = self.s_label, self.p, self.u
        hh = h or s * 0.42
        self.add(f'<div id="{bid_}" class="abs" style="left:{x}px; top:{y}px; width:{w}px;">'
                 f'<div style="display:flex; justify-content:space-between; align-items:baseline;">'
                 f'<span class="caps" style="font-size:{s}px; color:{p["soft"]};">{lab_left}</span>'
                 f'<span class="num" style="font-size:{s * 1.5}px; color:{color};">{lab_right}</span></div>'
                 f'<div style="margin-top:{s * 0.35}px; height:{hh}px; border-radius:{hh / 2}px; background:rgba(255,255,255,0.08);">'
                 f'<div id="{bid_}-f" style="width:{frac * 100:.1f}%; height:100%; border-radius:{hh / 2}px; background:{color}; box-shadow:0 0 {12 * u}px {color};"></div></div></div>')


def build(look, builders, only=None):
    hf = look.here / "hyperframes"
    n = 0
    for bid, fn in builders.items():
        if only and bid not in only:
            continue
        for portrait in (False, True):
            f = Frame(look, bid, portrait)
            f.head()
            f.stage()
            fn(f)
            f.foot()
            (hf / f"{bid}-{'v' if portrait else 'l'}.html").write_text(f.html(), encoding="utf-8", newline="\n")
            n += 1
    print("wrote", n, "compositions to", hf)


def render(look, builders, only=None, aspects=("l", "v")):
    here, hf = look.here, look.here / "hyperframes"
    (here / "media").mkdir(exist_ok=True)
    (here / "pantry").mkdir(exist_ok=True)
    for bid in builders:
        if only and bid not in only:
            continue
        for a in aspects:
            portrait = a == "v"
            src = f"{bid}-{a}.html"
            dst = here / ("pantry" if portrait else "media") / (f"{bid}-916.mp4" if portrait else f"{bid}.mp4")
            js = hf / "scenes" / f"{bid}.js"
            newest = max((hf / src).stat().st_mtime, js.stat().st_mtime, (hf / "assets" / "kit3.js").stat().st_mtime)
            if dst.exists() and dst.stat().st_mtime > newest:
                print("up to date", dst.name, flush=True)
                continue
            print("render", src, "->", dst.relative_to(here), flush=True)
            env = dict(os.environ, TEMP=TMPD, TMP=TMPD, HYPERFRAMES_NO_UPDATE_CHECK="1", HYPERFRAMES_NO_TELEMETRY="1")
            subprocess.run(["npx.cmd", "--no-install", "hyperframes", "render", "-c", src, "-o", str(dst), "-q", "delivery",
                            "--workers", "2", "--quiet"], cwd=hf, check=True, env=env, stdin=subprocess.DEVNULL)
