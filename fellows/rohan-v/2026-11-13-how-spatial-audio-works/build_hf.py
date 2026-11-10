"""Builds the HyperFrames + three.js compositions for "How Spatial Audio Works" (B01-B06):
hyperframes/B0x-l.html (3840x2160) and B0x-v.html (2160x3840); each page's 3D stage is drawn by
hyperframes/scenes/B0x.js (three.js, seeked frame by frame), the HUD is HTML on the beat's word-clock cues.

LOOK: "listening room at night". Deep indigo; the listener is the textbook spherical head (a glass sphere with two
ears and a small nose: the model spatial.py measures, never a person); sound is warm amber light; the right ear is
cyan, the left ear violet, everywhere (3D and HUD). Source Serif 4 titles, Inter HUD.

DATA: everything drawn comes from evidence/scene.json (spatial.py) and the beat sheet; the filter curves in B03/B04
are spatial.py's own head-shadow and outer-ear filters, evaluated here with the same constants.

    python build_hf.py [B03 ...]            # write the compositions
    python build_hf.py [B03 ...] --render   # and render: media/B0x.mp4 (16:9), pantry/B0x-916.mp4 (9:16)
"""
import json
import shutil
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
KIT = HERE / "_kit" if (HERE / "_kit").is_dir() else HERE.parent / "_kit"     # the shared week-12 kit (a copy ships in _kit/)
sys.path.insert(0, str(KIT))
import hfkit  # noqa: E402

sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
BEATS = {b["beat_id"]: b for b in sheet["beats"]}

P = {"bg": "#04051A", "text": "#EEF0FF", "soft": "#A9AEDB", "dim": "#5F6596", "chap": "#5CE1FF", "acc": "#FFB454",
     "glass": "rgba(255,255,255,0.05)", "gline": "rgba(255,255,255,0.14)", "chip": "#FFFFFF",
     "ground_l": "radial-gradient(ellipse 54% 62% at 34% 56%, #151951 0%, #080A27 55%, #04051A 100%)",
     "ground_v": "radial-gradient(ellipse 80% 40% at 50% 30%, #171B57 0%, #090B2A 55%, #04051A 100%)"}
AMBER, CYAN, VIOLET, TEXT, SOFT, DIM = P["acc"], "#5CE1FF", "#C39BFF", P["text"], P["soft"], P["dim"]
PINK = "#FF7AB6"
CHAPTER = {"B01": "01 · TIMING", "B02": "02 · LOUDNESS", "B03": "03 · FRONT OR BACK", "B04": "04 · THE FILTERS",
           "B05": "05 · HEAD TRACKING", "B06": "06 · YOUR EARS"}
PTITLE = {"B01": "Two Ears, a Tiny Delay", "B02": "Your Head's Shadow", "B03": "Front or Behind?",
          "B04": "Every Direction", "B05": "The Sound Stays Put", "B06": "Tuned to Your Ears"}
SPARKS = {"B01": "Two thirds of a millisecond tells left from right.",
          "B02": "Timing for low sounds, loudness for high ones.",
          "B03": "Same timing, same loudness: the outer ear decides.",
          "B04": "Measure every direction once; play any of them back.",
          "B05": "Turn your head; the sound stays in the room.",
          "B06": "An ear scan builds a profile just for you."}
LOOK = hfkit.Look(HERE, BEATS, CHAPTER, PTITLE, SPARKS, P, "apple-01.svg")

# ---------------------------------------------------------------- spatial.py's filters, evaluated (same constants)
A, C = 0.0875, 343.0
FREQS = np.geomspace(200, 16000, 64)


def shadow_db(angle_to_ear):
    w0 = C / A
    a_min, th_min = 0.1, np.radians(150)
    alpha = (1 + a_min / 2) + (1 - a_min / 2) * np.cos(angle_to_ear / th_min * np.pi)
    s = 1j * 2 * np.pi * FREQS
    return 20 * np.log10(np.abs((1 + alpha * s / (2 * w0)) / (1 + s / (2 * w0))))


def pinna_db():
    s = 1j * FREQS / 3500
    return 20 * np.log10(np.abs(0.45 + 0.55 / (1 + s)))


def ang(theta, ear):
    return abs(np.angle(np.exp(1j * (theta - ear))))


R_AX, L_AX = np.pi / 2, -np.pi / 2
FRONT_R = shadow_db(ang(np.radians(30), R_AX))
BACK_R = shadow_db(ang(np.radians(150), R_AX))
BACK_R_P = BACK_R + pinna_db()
PAIR_R = shadow_db(ang(np.radians(60), R_AX))
PAIR_L = shadow_db(ang(np.radians(60), L_AX))
ITD60 = [r["measured_ms"] for r in S["itd"] if r["deg"] == 60][0]


def curve_path(xs, ys, w, h, ylo, yhi, logx=True):
    x0, x1 = (np.log10(xs[0]), np.log10(xs[-1])) if logx else (xs[0], xs[-1])
    pts = []
    for x, y in zip(xs, ys):
        px = ((np.log10(x) if logx else x) - x0) / (x1 - x0) * w
        py = h - (min(max(y, ylo), yhi) - ylo) / (yhi - ylo) * h
        pts.append(f"{px:.1f},{py:.1f}")
    return "M" + " L".join(pts)


def chart(f, cid, y, h, series, ylo, yhi, xticks, ylab, x=None, w=None):
    """A small line chart in the HUD. series: [(id, xs, ys, color, dash)]."""
    u, s = f.u, f.s_label
    x = f.hx if x is None else x
    w = f.hw if w is None else w
    padl, padb = s * 0.4, s * 1.6
    pw, ph = w - padl, h - padb - s * 1.5
    out = [f'<div id="{cid}" class="abs" style="left:{x}px; top:{y}px; width:{w}px; height:{h}px;">',
           f'<div class="caps" style="font-size:{s}px; color:{SOFT};">{ylab}</div>',
           f'<svg style="position:absolute; left:{padl}px; top:{s * 1.5}px; overflow:visible;" width="{pw}" height="{ph}">']
    for gy in (0.0, 0.5, 1.0):
        out.append(f'<line x1="0" x2="{pw}" y1="{gy * ph:.1f}" y2="{gy * ph:.1f}" stroke="rgba(255,255,255,0.1)" stroke-width="{1.5 * u}"/>')
    for sid, xs, ys, col, dash in series:
        d = curve_path(xs, ys, pw, ph, ylo, yhi)
        da = f' stroke-dasharray="{14 * u} {10 * u}"' if dash else ""
        out.append(f'<path id="{sid}" d="{d}" fill="none" stroke="{col}" stroke-width="{5 * u}" stroke-linecap="round" stroke-linejoin="round"{da} '
                   f'style="filter:drop-shadow(0 0 {6 * u}px {col});"/>')
    out.append("</svg>")
    lx0, lx1 = np.log10(FREQS[0]), np.log10(FREQS[-1])
    for fx, lab in xticks:
        px = padl + (np.log10(fx) - lx0) / (lx1 - lx0) * pw
        al, lx = ("left", px) if fx == xticks[0][0] else (("right", px - s * 4) if fx == xticks[-1][0] else ("center", px - s * 2))
        out.append(f'<div class="caps" style="position:absolute; left:{lx}px; width:{s * 4}px; text-align:{al}; top:{s * 1.5 + ph + s * 0.45}px; '
                   f'font-size:{s * 0.9}px; color:{DIM};">{lab}</div>')
    out.append("</div>")
    f.add("".join(out))


XT = [(250, "250 Hz"), (1000, "1 kHz"), (4000, "4 kHz"), (16000, "16 kHz")]


# ================================================================== B01 · timing
def b01(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"itd": S["itd"]}
    f.mark_hud()
    f.stat("itd", x, y, f'<span id="itd-n">0.66</span><span style="font-size:0.42em; margin-left:0.18em;">ms</span>',
           "GAP BETWEEN YOUR EARS", color=CYAN)
    # two lanes: when the sound reaches each ear
    lh = s * 6.0
    lane = (f'<div id="lanes" class="glass" style="left:{x}px; top:{y + f.s_stat * 1.75}px; width:{w}px; height:{lh}px; padding:{s * 0.6}px {s * 0.8}px;">'
            f'<div id="itd-a" class="caps" style="font-size:{s * 0.9}px; color:{AMBER};">SOUND AT 90° RIGHT</div>')
    for i, (nm, col) in enumerate((("RIGHT EAR", CYAN), ("LEFT EAR", VIOLET))):
        ty = s * 2.35 + i * s * 1.75
        lane += (f'<div class="caps" style="position:absolute; left:{s * 0.8}px; top:{ty}px; font-size:{s * 0.9}px; color:{col};">{nm}</div>'
                 f'<div style="position:absolute; left:{s * 6.6}px; right:{s * 0.8}px; top:{ty + s * 0.45}px; height:{2 * u}px; background:rgba(255,255,255,0.14);"></div>'
                 f'<div id="pulse-{"r" if i == 0 else "l"}" style="position:absolute; left:{s * 6.6}px; top:{ty - s * 0.1}px; width:{s * 0.32}px; height:{s * 1.1}px; '
                 f'border-radius:{s * 0.16}px; background:{col}; box-shadow:0 0 {14 * u}px {col};"></div>')
    lane += "</div>"
    f.add(lane)
    # ITD vs angle, the measured points
    cy, ch = y + f.s_stat * 1.75 + lh + s * 1.4, s * 9.6 if not f.portrait else s * 6.0
    pts = S["itd"]
    pw, ph = w - s * 0.4, ch - s * 3.2
    svg = [f'<div id="chart" class="abs" style="left:{x}px; top:{cy}px; width:{w}px; height:{ch}px;">'
           f'<div class="caps" style="font-size:{s}px; color:{SOFT};">GAP vs DIRECTION · MY HEAD MODEL</div>'
           f'<svg style="position:absolute; left:{s * 0.2}px; top:{s * 1.5}px; overflow:visible;" width="{pw}" height="{ph}">']
    for gy in (0, 0.5, 1):
        svg.append(f'<line x1="0" x2="{pw}" y1="{gy * ph}" y2="{gy * ph}" stroke="rgba(255,255,255,0.1)" stroke-width="{1.5 * u}"/>')
    path = "M" + " L".join(f'{r["deg"] / 90 * pw:.1f},{ph - r["measured_ms"] / 0.7 * ph:.1f}' for r in pts)
    svg.append(f'<path id="itd-curve" d="{path}" fill="none" stroke="{CYAN}" stroke-width="{4 * u}" opacity="0.8"/>')
    for r in pts:
        svg.append(f'<circle class="itd-pt" cx="{r["deg"] / 90 * pw:.1f}" cy="{ph - r["measured_ms"] / 0.7 * ph:.1f}" r="{7 * u}" fill="{CYAN}"/>')
    svg.append(f'<circle id="itd-now" cx="{pw}" cy="{ph - 0.661 / 0.7 * ph:.1f}" r="{13 * u}" fill="{AMBER}" style="filter:drop-shadow(0 0 {10 * u}px {AMBER});"/>')
    svg.append("</svg>")
    for dg, lab in ((0, "AHEAD 0°"), (45, "45°"), (90, "SIDE 90°")):
        px = s * 0.2 + dg / 90 * pw
        al = "left" if dg == 0 else ("right" if dg == 90 else "center")
        off = 0 if dg == 0 else (-s * 6 if dg == 90 else -s * 3)
        svg.append(f'<div class="caps" style="position:absolute; left:{px + off}px; width:{s * 6}px; text-align:{al}; top:{s * 1.5 + ph + s * 0.4}px; font-size:{s * 0.9}px; color:{DIM};">{lab}</div>')
    svg.append("</div>")
    f.add("".join(svg))
    if not f.portrait:      # phone: the closing note goes; its room spaces out the panels
        f.note("note", "Straight ahead, the gap is zero.", x, cy + ch + s * 0.8, w)
    f.anim(f"""
inn("#itd", {f.t('gap') - 0.3}); inn("#lanes", {f.t('first') - 0.2}); inn("#chart", {f.t('model')});
tl.fromTo(".itd-pt", {{ opacity: 0, scale: 0, transformOrigin: "50% 50%" }}, {{ opacity: 1, scale: 1, duration: 0.5, stagger: 0.12, ease: "back.out(2)" }}, {f.t('model') + 0.3});
draw("#itd-curve", {f.t('model') + 0.3}, 1.2);
inn("#itd-now", {f.t('gap')}, 0.5, {{ y: 0 }});
""" + ("" if f.portrait else f'inn("#note", {f.t("front") - 0.4});'))


# ================================================================== B02 · loudness (head shadow)
def b02(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    hi_far, lo_far = 10 ** (-S["ild_high_db"] / 20), 10 ** (-S["ild_low_db"] / 20)
    f.data = {"hi_far": hi_far, "lo_far": lo_far}
    f.mark_hud()
    gap = s * 0.9
    ph = s * 6.4

    def panel(pid, py, head, sub, far, db, col):
        f.add(f'<div id="{pid}" class="glass" style="left:{x}px; top:{py}px; width:{w}px; padding:{s * 0.7}px {s * 0.9}px;">'
              f'<div style="display:flex; justify-content:space-between; align-items:baseline;">'
              f'<span class="caps" style="font-size:{s}px; color:{col};">{head}</span><span class="caps" style="font-size:{s * 0.9}px; color:{DIM};">{sub}</span></div>'
              f'<div style="display:flex; align-items:center; gap:{s * 0.6}px; margin-top:{s * 0.7}px;"><span class="caps" style="width:{s * 5.4}px; font-size:{s * 0.9}px; color:{CYAN};">NEAR EAR</span>'
              f'<div style="flex:1; height:{s * 0.45}px; border-radius:{s}px; background:rgba(255,255,255,0.08);"><div class="{pid}-b" style="width:100%; height:100%; border-radius:{s}px; background:{CYAN};"></div></div></div>'
              f'<div style="display:flex; align-items:center; gap:{s * 0.6}px; margin-top:{s * 0.5}px;"><span class="caps" style="width:{s * 5.4}px; font-size:{s * 0.9}px; color:{VIOLET};">FAR EAR</span>'
              f'<div style="flex:1; height:{s * 0.45}px; border-radius:{s}px; background:rgba(255,255,255,0.08);"><div class="{pid}-b" style="width:{far * 100:.1f}%; height:100%; border-radius:{s}px; background:{VIOLET};"></div></div></div>'
              f'<div class="num" style="font-size:{s * (1.7 if f.portrait else 2.3)}px; margin-top:{s * (0.4 if f.portrait else 0.6)}px; color:{TEXT};"><span id="{pid}-n">{db:.1f}</span><span class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; margin-left:{s * 0.5}px; letter-spacing:0.1em;">dB QUIETER IN THE FAR EAR</span></div></div>')

    panel("hi", y, "HIGH SOUNDS", "3–6 kHz", hi_far, S["ild_high_db"], AMBER)
    panel("lo", y + ph + gap * 1.6, "LOW SOUNDS", "350–700 Hz", lo_far, S["ild_low_db"], "#FFD9A0")
    ry = y + 2 * (ph + gap * 1.6)
    if not f.portrait:      # phone: the panels already say it; the rule card goes so nothing runs past the safe area
      f.add(f'<div id="rule2" class="abs" style="left:{x}px; top:{ry}px; width:{w}px; display:flex; gap:{s * 0.8}px;">'
          f'<div class="glass" style="position:relative; flex:1; padding:{s * 0.6}px {s * 0.8}px;"><div class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">LOW SOUNDS</div>'
          f'<div class="serif" style="font-size:{s * 1.5}px; margin-top:{s * 0.2}px;">use timing</div></div>'
          f'<div class="glass" style="position:relative; flex:1; padding:{s * 0.6}px {s * 0.8}px;"><div class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">HIGH SOUNDS</div>'
          f'<div class="serif" style="font-size:{s * 1.5}px; margin-top:{s * 0.2}px;">use loudness</div></div></div>')
    if not f.portrait:      # phone: the closing note goes (no room under the panels)
        f.note("ray", "Lord Rayleigh, 1907: the “duplex” theory.", x, ry + s * 4.6, w, color=SOFT)
    f.anim(f"""
inn("#hi", {f.t('high')}); tl.fromTo(".hi-b", {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 1.1, stagger: 0.25, ease: "expo.out" }}, {f.t('high') + 0.3});
count("#hi-n", {S['ild_high_db']}, {f.t('fourteen') - 0.4}, 1.0, 1);
inn("#lo", {f.t('low')}); tl.fromTo(".lo-b", {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 1.1, stagger: 0.25, ease: "expo.out" }}, {f.t('low') + 0.3});
count("#lo-n", {S['ild_low_db']}, {f.t('two') - 0.4}, 0.9, 1);
""" + ("" if f.portrait else f'inn("#rule2", {f.t("rule")});') + ("" if f.portrait else f'inn("#ray", {f.t("rayleigh")});'))


# ================================================================== B03 · front or back
def b03(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.mark_hud()
    cw = (w - s * 0.8) / 2

    def card(cid, cx, head, col, sub):
        f.add(f'<div id="{cid}" class="glass" style="left:{cx}px; top:{y}px; width:{cw}px; padding:{s * 0.6}px {s * 0.8}px;">'
              f'<div class="caps" style="font-size:{s * 0.9}px; color:{col};">{head}</div>'
              f'<div class="num" style="font-size:{s * 2.2}px; margin-top:{s * 0.45}px;">{S["itd_front_ms"]:.3f}<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; margin-left:{s * 0.35}px;">ms GAP</span></div>'
              f'<div class="caps" style="font-size:{s * 0.9}px; color:{DIM}; margin-top:{s * 0.35}px;">{sub}</div></div>')

    card("fr", x, "IN FRONT · 30°", AMBER, "SAME LOUDNESS")
    card("bk", x + cw + s * 0.8, "BEHIND · 150°", PINK, "SAME LOUDNESS")
    cy = y + s * 6.2
    ch = s * 8.6 if not f.portrait else s * 7.2
    if not f.portrait:
        chart(f, "c1", cy, ch, [("c1a", FREQS, FRONT_R, AMBER, False), ("c1b", FREQS, BACK_R, PINK, True)], -12, 6, XT,
              f"HEAD ONLY · {S['frontback_head_db']:.1f} dB APART")
    chart(f, "c2", cy + ch + s * 0.9, ch, [("c2a", FREQS, FRONT_R, AMBER, False), ("c2b", FREQS, BACK_R_P, PINK, False)], -12, 6, XT,
          f"WITH OUTER EARS · {S['frontback_pinna_db']:.1f} dB APART")
    f.anim(f"""
inn("#fr", {f.t('mirror')}); inn("#bk", {f.t('mirror') + 0.5});
""" + ("" if f.portrait else f'''inn("#c1", {f.t('exactly') - 0.6}); draw("#c1a", {f.t('exactly') - 0.4}, 1.0); draw("#c1b", {f.t('exactly')}, 1.0);''') + f"""
inn("#c2", {f.t('folds')}); draw("#c2a", {f.t('folds') + 0.2}, 1.0); draw("#c2b", {f.t('folds') + 0.6}, 1.2);
""")


# ================================================================== B04 · the filters (HRTF)
HP_SVG = ('<svg viewBox="0 0 48 48" width="100%" height="100%"><path d="M8 30 v-6 a16 16 0 0 1 32 0 v6" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round"/>'
          '<rect x="5" y="27" width="9" height="14" rx="3" fill="currentColor"/><rect x="34" y="27" width="9" height="14" rx="3" fill="currentColor"/></svg>')


def b04(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    t0 = f.t("listen") + 0.0
    clip0 = 18.349
    f.data = {"clip0": clip0, "clipdur": 8.0}
    f.mark_hud()
    f.stat("dirs", x, y, '<span id="dirs-n">0</span>', "DIRECTIONS MEASURED", color=TEXT)
    ch = s * 8.0 if not f.portrait else s * 5.8
    cy = y + f.s_stat * 1.75
    chart(f, "pair", cy, ch, [("pr", FREQS, PAIR_R, CYAN, False), ("pl", FREQS, PAIR_L, VIOLET, False)], -14, 6, XT,
          "MY MODEL'S FILTER PAIR · 60° RIGHT")
    hy = cy + ch + s * 1.0
    f.add(f'<div id="hp" class="glass" style="left:{x}px; top:{hy}px; width:{w}px; display:flex; align-items:center; gap:{s * 0.9}px; padding:{s * 0.7}px {s * 0.9}px;">'
          f'<div style="flex:none; width:{s * 2.6}px; height:{s * 2.6}px; color:{AMBER};">{HP_SVG}</div>'
          f'<div><div class="caps" style="font-size:{s}px; color:{AMBER};">HEADPHONES ON</div>'
          f'<div class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; margin-top:{s * 0.3}px;">NOW FROM: <span id="dir-now" style="color:{TEXT};">AHEAD</span></div></div>'
          f'<svg id="dial" viewBox="-50 -50 100 100" style="margin-left:auto; flex:none; width:{s * 3.2}px; height:{s * 3.2}px;">'
          f'<circle r="40" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="2"/><circle r="9" fill="#1A1F55" stroke="#8A9BFF" stroke-width="2"/>'
          f'<path d="M0 -12 L-4 -9 L4 -9 Z" fill="#DFE3FF"/><circle id="dial-dot" cx="0" cy="-40" r="6.5" fill="{AMBER}"/></svg></div>')
    if not f.portrait:
        f.note("lis", "One turn around your head, rendered by my model.", x, hy + s * 4.4, w, color=SOFT)
    f.anim(f"""
inn("#dirs", {f.t('seven') - 0.3}); count("#dirs-n", 710, {f.t('seven')}, 3.0, 0);
inn("#pair", {f.t('hrtf')}); draw("#pr", {f.t('hrtf') + 0.3}, 1.0); draw("#pl", {f.t('hrtf') + 0.6}, 1.0);
inn("#hp", {t0});
""" + ("" if f.portrait else f'inn("#lis", {clip0 - 0.2});'))


# ================================================================== B05 · head tracking
def b05(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    tw = f.t("turn"); tw2 = f.t("sensors") + 0.4
    f.data = {"turn": S["turn_deg"], "a0": tw + 0.2, "a1": f.t("with") + 0.2, "b0": tw2 + 0.6}
    f.mark_hud()
    ph = s * 6.2

    def card(cid, py, head, col, sub, rid):
        f.add(f'<div id="{cid}" class="glass" style="left:{x}px; top:{py}px; width:{w}px; padding:{s * 0.7}px {s * 0.9}px;">'
              f'<div style="display:flex; align-items:center; gap:{s * 0.5}px;"><span style="width:{s * 0.55}px; height:{s * 0.55}px; border-radius:50%; background:{col}; box-shadow:0 0 {10 * u}px {col};"></span>'
              f'<span class="caps" style="font-size:{s}px; color:{col};">{head}</span></div>'
              f'<div class="serif" style="font-size:{s * (1.15 if f.portrait else 1.45)}px; margin-top:{s * 0.35}px;">{sub}</div>'
              f'<div style="display:flex; gap:{s * 1.4}px; margin-top:{s * 0.5}px;">'
              f'<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">HEAD <span id="{rid}-h" class="num" style="font-size:{s * 1.5}px; color:{TEXT}; margin-left:{s * 0.2}px;">0°</span></span>'
              f'<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">SOUND <span id="{rid}-s" class="num" style="font-size:{s * 1.5}px; color:{AMBER}; margin-left:{s * 0.2}px;">0°</span></span></div></div>')

    card("off", y, "TRACKING OFF", "#FF8A7A", "The sound turns with you.", "off")
    card("on", y + ph + s * 1.0, "TRACKING ON", "#7CF0B4", "Motion sensors turn it back: it stays put.", "on")
    f.tag("apple", "AirPods · head tracking · 2020", x, y + 2 * (ph + s * 1.0) + s * 0.2)
    f.anim(f"""
inn("#off", {f.t('turn') - 0.3}); out("#off", {f.t('sensors') - 0.2}, 0.5);
inn("#on", {f.t('sensors')}); inn("#apple", {f.t('apple')});
""")


# ================================================================== B06 · your ears
def b06(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.mark_hud()
    f.add(f'<div id="diff" class="glass" style="left:{x}px; top:{y}px; width:{w}px; padding:{s * 0.7}px {s * 0.9}px;">'
          f'<div class="caps" style="font-size:{s}px; color:{VIOLET};">EVERY EAR IS DIFFERENT</div>'
          f'<div class="serif" style="font-size:{s * 1.4}px; margin-top:{s * 0.35}px;">Filters from a dummy head can flip front and back.</div></div>')
    if not f.portrait:
      f.add(f'<div id="flip" class="abs" style="left:{x}px; top:{y + s * 5.6}px; width:{w}px; display:flex; align-items:center; justify-content:center; gap:{s * 1.2}px;">'
          f'<span class="caps" style="font-size:{s * 1.1}px; color:{AMBER};">FRONT</span>'
          f'<svg viewBox="0 0 120 40" style="width:{s * 4.4}px; height:{s * 1.5}px;"><path d="M8 14 H108 M96 4 L110 14 L96 24" fill="none" stroke="{SOFT}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
          f'<path d="M112 30 H12 M24 20 L10 30 L24 40" fill="none" stroke="{SOFT}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" transform="translate(0,-4)"/></svg>'
          f'<span class="caps" style="font-size:{s * 1.1}px; color:{PINK};">BEHIND</span></div>')
    f.add(f'<div id="scan" class="glass" style="left:{x}px; top:{y + s * 8.6}px; width:{w}px; padding:{s * 0.7}px {s * 0.9}px;">'
          f'<div class="caps" style="font-size:{s}px; color:{CYAN};">iPHONE CAMERA EAR SCAN</div>'
          f'<div class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; margin-top:{s * 0.35}px;">THE SHAPE OF YOUR EAR</div></div>')
    f.tag("apple", "Personalized Spatial Audio · iOS 16", x, y + s * 13.0)
    if not f.portrait:
        f.note("prof", "A profile built for your ears.", x, y + s * 16.2, w)
    f.anim(f"""
inn("#diff", {f.t('different') + 0.2});
""" + ("" if f.portrait else f'''inn("#flip", {f.t('mixup')});
tl.fromTo("#flip svg", {{ rotation: 0 }}, {{ rotation: 180, duration: 0.8, ease: "power2.inOut", repeat: 1, yoyo: true }}, {f.t('mixup') + 0.6});''') + f"""
inn("#scan", {f.t('scan')});
inn("#apple", {f.t('profile') - 1.2});
""" + ("" if f.portrait else f'inn("#prof", {f.t("profile")});'))


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06}

if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if a.startswith("B")] or None
    dst = HERE / "hyperframes" / "assets" / "kit3.js"
    if not dst.exists() or dst.read_bytes() != (KIT / "kit3.js").read_bytes():     # only when changed (mtime drives re-renders)
        shutil.copy(KIT / "kit3.js", dst)
    hfkit.build(LOOK, BUILDERS, only)
    if "--render" in sys.argv:
        hfkit.render(LOOK, BUILDERS, only, aspects=[a for a in ("l", "v") if f"--{a}" in sys.argv] or ("l", "v"))
