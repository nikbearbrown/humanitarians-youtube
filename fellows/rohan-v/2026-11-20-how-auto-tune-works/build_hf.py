"""Builds the HyperFrames + three.js compositions for "How Auto-Tune Works" (B01-B06):
hyperframes/B0x-l.html (3840x2160) and B0x-v.html (2160x3840); each page's 3D stage is drawn by
hyperframes/scenes/B0x.js (three.js, seeked frame by frame), the HUD is HTML on the beat's word-clock cues.

LOOK: "the vocal booth at night". Near-black plum; the singer's pitch is light drawn through a 3D piano roll whose
lanes are the notes of C major (lilac); as sung = coral, gentle correction = gold, retune speed zero = cyan,
everywhere (3D and HUD). Source Serif 4 titles, Inter HUD.

DATA: everything drawn comes from evidence/scene.json (autotune.py) and the beat sheet; B04's vowel envelopes are
autotune.py's own envelope() evaluated here on the run's held-note files.

    python build_hf.py [B03 ...]            # write the compositions
    python build_hf.py [B03 ...] --render   # and render: media/B0x.mp4 (16:9), pantry/B0x-916.mp4 (9:16)
"""
import json
import shutil
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile

HERE = Path(__file__).resolve().parent
KIT = HERE / "_kit" if (HERE / "_kit").is_dir() else HERE.parent / "_kit"     # the shared week-13 kit (a copy ships in _kit/)
sys.path.insert(0, str(KIT))
import hfkit  # noqa: E402

sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
R = S["results"]
BEATS = {b["beat_id"]: b for b in sheet["beats"]}

P = {"bg": "#0A0510", "text": "#F7EFF8", "soft": "#CDB8D6", "dim": "#7C6888", "chap": "#FF6FA8", "acc": "#FFC857",
     "glass": "rgba(255,255,255,0.05)", "gline": "rgba(255,255,255,0.14)", "chip": "#FFFFFF",
     "ground_l": "radial-gradient(ellipse 54% 62% at 34% 56%, #24102E 0%, #12081A 55%, #0A0510 100%)",
     "ground_v": "radial-gradient(ellipse 80% 40% at 50% 30%, #26112F 0%, #13081B 55%, #0A0510 100%)"}
CORAL, GOLD, CYAN, LILAC, PINK = "#FF8A5B", P["acc"], "#4FE3D1", "#B79CFF", P["chap"]
TEXT, SOFT, DIM = P["text"], P["soft"], P["dim"]
CHAPTER = {"B01": "01 · PITCH", "B02": "02 · OFF KEY", "B03": "03 · SNAP", "B04": "04 · SHIFTING",
           "B05": "05 · LISTEN", "B06": "06 · THEN AND NOW"}
PTITLE = {"B01": "Finding the Repeat", "B02": "Sharp and Flat", "B03": "Snap to the Note",
          "B04": "No Chipmunks", "B05": "Hear the Difference", "B06": "From Oil to Pop"}
SPARKS = {"B01": "Slide the wave along itself until it lines up.",
          "B02": "Close to the note is not on the note.",
          "B03": "Retune speed: how fast the voice is pulled in.",
          "B04": "Re-space the cycles; keep the vowel.",
          "B05": "Same singer, three settings.",
          "B06": "Maths for reading rock, reused for voices."}
LOOK = hfkit.Look(HERE, BEATS, CHAPTER, PTITLE, SPARKS, P, "none.svg")

# ---------------------------------------------------------------- data for drawing
T = S["t"]
TR = S["tracks"]


def track(name):
    """A pitch track for DRAWING: the detector's few onset misses (frames more than half a semitone from the median of
    their 9 neighbours: octave slips where one note fades into the next) are dropped, so they don't draw as spikes.
    Every number on screen comes from results.json, measured with the misses included."""
    pts = [(round(t, 3), v) for t, v in zip(T, TR[name]) if v is not None]
    vs = np.array([v for _, v in pts])
    med = np.array([np.median(vs[max(0, i - 4): i + 5]) for i in range(len(vs))])
    return [[t, v] for (t, v), m in zip(pts, med) if abs(v - m) <= 0.5]


TRACKS = {k: track(k) for k in ("detected", "gentle", "hard")}
ROLL = {"t_starts": S["t_starts"], "t_end": S["t_end"], "tune": S["tune"], "names": S["names"],
        "offsets": R["as_sung"]["offsets"], "tracks": TRACKS}


def envelope_curves():
    """autotune.py's envelope(): cepstrally smoothed spectrum of each held-note file (dB), 300-4500 Hz, normalised."""
    sys.path.insert(0, str(HERE))
    import autotune as at
    out = {}
    ff = np.geomspace(300, 4500, 90)
    for k, fn in (("orig", "held_c4.wav"), ("fast", "held_resampled.wav"), ("psola", "held_psola.wav")):
        sr, x = wavfile.read(HERE / "evidence" / fn)
        x = x.astype(float) / 32768
        seg = x[int(0.2 * len(x)): int(0.85 * len(x))]
        f, e = at.envelope(seg)
        y = np.interp(ff, f, e)
        out[k] = (y - y.max()).round(2).tolist()
    return ff.round(1).tolist(), out


def chart_path(xs, ys, w, h, ylo, yhi, logx=True):
    x0, x1 = (np.log10(xs[0]), np.log10(xs[-1])) if logx else (xs[0], xs[-1])
    pts = []
    for x, y in zip(xs, ys):
        px = ((np.log10(x) if logx else x) - x0) / (x1 - x0) * w
        py = h - (min(max(y, ylo), yhi) - ylo) / (yhi - ylo) * h
        pts.append(f"{px:.1f},{py:.1f}")
    return "M" + " L".join(pts)


def panel(f, pid, y, inner, w=None, x=None, pad=(0.7, 0.9)):
    s = f.s_label
    f.add(f'<div id="{pid}" class="glass" style="left:{f.hx if x is None else x}px; top:{y}px; width:{f.hw if w is None else w}px; '
          f'padding:{s * pad[0]}px {s * pad[1]}px;">{inner}</div>')


def caps(t, size, color, extra=""):
    return f'<div class="caps" style="font-size:{size}px; color:{color}; {extra}">{t}</div>'


def chip_row(f, items):
    """A row of small colour keys: [(label, color)]."""
    s = f.s_label
    return ('<div style="display:flex; flex-wrap:wrap; gap:' + f'{s * 0.5}px {s * 1.1}px; margin-top:{s * 0.5}px;">' +
            "".join(f'<span style="display:flex; align-items:center; gap:{s * 0.4}px;"><span style="width:{s * 0.9}px; height:{s * 0.22}px; '
                    f'border-radius:{s * 0.11}px; background:{c}; box-shadow:0 0 {s * 0.25}px {c};"></span>'
                    f'<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">{t}</span></span>' for t, c in items) + "</div>")


NOTE_PINS = {60: "C4", 62: "D4", 64: "E4", 67: "G4", 69: "A4"}


def lane_pins(f):
    """Note names beside the roll's lit lanes (placed by the 3D scene every frame). Before mark_hud()."""
    for m, n in NOTE_PINS.items():
        f.pin(f"pn{m}", n, color=LILAC, size=f.s_label * 0.9)


# ================================================================== B01 · pitch (find the repeat)
def b01(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    fr = S["frame"]
    f.data = {"wave": fr["wave"], "cmnd": fr["cmnd"], "step_ms": fr["step_ms"], "tau_ms": fr["tau_ms"]}
    f.pin("lagpin", "SLID 0.00 ms", color=GOLD)
    f.pin("perpin", f"ONE REPEAT · {fr['tau_ms']:.2f} ms", color=LILAC)
    f.mark_hud()
    f.stat("a440", x, y, '440<span style="font-size:0.42em; margin-left:0.18em;">Hz</span>',
           "THE NOTE A · REPEATS PER SECOND", color=TEXT)
    # the line-up score: how badly the wave and its slid copy disagree, for every slide
    ch = s * (8.2 if not f.portrait else 6.2)
    pw, ph = w - s * 1.8, ch - s * 4.0
    cm = fr["cmnd"]
    step = fr["step_ms"]
    lagmax = step * (len(cm) - 1)
    pts = " L".join(f"{i * step / lagmax * pw:.1f},{min(v, 1.6) / 1.6 * ph:.1f}" for i, v in enumerate(cm))
    taux = fr["tau_ms"] / lagmax * pw
    tauy = min(cm[int(round(fr['tau_ms'] / step))], 1.6) / 1.6 * ph
    inner = (caps("MATCH AS THE COPY SLIDES", s, SOFT, "white-space:normal; line-height:1.35;") +
             f'<svg style="display:block; margin-top:{s * 0.6}px; overflow:visible;" width="{pw}" height="{ph}">'
             f'<line x1="0" x2="{pw}" y1="0" y2="0" stroke="rgba(255,255,255,0.1)" stroke-width="{1.5 * u}"/>'
             f'<line x1="0" x2="{pw}" y1="{ph}" y2="{ph}" stroke="rgba(255,255,255,0.1)" stroke-width="{1.5 * u}"/>'
             f'<path id="cm" d="M{pts}" fill="none" stroke="{LILAC}" stroke-width="{4 * u}" stroke-linejoin="round" style="filter:drop-shadow(0 0 {5 * u}px {LILAC});"/>'
             f'<line id="cm-tau" x1="{taux:.1f}" x2="{taux:.1f}" y1="{-s * 0.3}" y2="{ph}" stroke="{GOLD}" stroke-width="{2.5 * u}" stroke-dasharray="{8 * u} {7 * u}" opacity="0"/>'
             f'<circle id="cm-dot" cx="0" cy="0" r="{11 * u}" fill="{PINK}" style="filter:drop-shadow(0 0 {8 * u}px {PINK});"/></svg>'
             f'<div style="display:flex; justify-content:space-between; margin-top:{s * 0.45}px;">'
             + caps("SLID 0 ms", s * 0.9, DIM) + caps(f"{lagmax:.0f} ms", s * 0.9, DIM) + '</div>'
             f'<div id="cm-read" class="caps" style="font-size:{s}px; color:{GOLD}; margin-top:{s * 0.35}px; opacity:0;">'
             f'LINES UP AT {fr["tau_ms"]:.2f} ms → {fr["hz"]:.0f} Hz</div>')
    panel(f, "score", y + f.s_stat * 1.75, inner)
    f.stat("acc", x, y + f.s_stat * 1.75 + ch + s * 4.2, '<span id="acc-n">0</span>%',
           "OF MOMENTS WITHIN 5 CENTS OF THE TRUE PITCH", color=PINK, size=f.s_stat * 0.8,
           labw=w)
    if not f.portrait:
        f.note("nt", f"My singer's A came out at {fr['hz']:.0f} Hz: a little sharp.", x, y + f.s_stat * 1.75 + ch + s * 4.2 + f.s_stat * 0.8 + s * 2.4, w, color=SOFT)
    f.anim(f"""
inn("#a440", {f.t('a') - 0.2}); count("#a440-v", 440, {f.t('four') - 0.3}, 1.1, 0, "");
inn("#score", {f.t('slides') - 0.2});
tl.to("#cm-tau", {{ opacity: 1, duration: 0.4 }}, {f.t('line')}); tl.to("#cm-read", {{ opacity: 1, duration: 0.5 }}, {f.t('line') + 0.2});
inn("#acc", {f.t('detector')}); count("#acc-n", {R['yin_score']['within5'] * 100:.1f}, {f.t('five')}, 1.6, 0);
""" + ("" if f.portrait else f'inn("#nt", {f.t("ninety") + 0.6});'))


# ================================================================== B02 · off key
def b02(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"roll": ROLL}
    lane_pins(f)
    f.mark_hud()
    # one semitone = 100 cents, drawn as a ruler
    rw = w - s * 1.8
    ticks = "".join(f'<line x1="{i / 10 * rw:.1f}" x2="{i / 10 * rw:.1f}" y1="{0 if i % 5 == 0 else s * 0.3}" y2="{s * 0.9}" stroke="{SOFT if i % 5 == 0 else DIM}" stroke-width="{2 * u}"/>' for i in range(11))
    inner = (caps("ONE SEMITONE = 100 CENTS", s, SOFT) +
             f'<svg style="display:block; margin-top:{s * 0.8}px; overflow:visible;" width="{rw}" height="{s * 0.9}">{ticks}'
             f'<line x1="0" x2="{rw}" y1="{s * 0.9}" y2="{s * 0.9}" stroke="{SOFT}" stroke-width="{2 * u}"/>'
             f'<rect id="ru-off" x="0" y="{s * 0.05}" width="{0.29 * rw:.1f}" height="{s * 0.5}" rx="{s * 0.1}" fill="{CORAL}" opacity="0.9" style="filter:drop-shadow(0 0 {6 * u}px {CORAL});"/></svg>'
             f'<div style="display:flex; justify-content:space-between; margin-top:{s * 0.4}px;">' + caps("C", s * 0.9, LILAC) + caps("C#", s * 0.9, SOFT) + "</div>")
    panel(f, "ruler", y, inner)
    f.stat("off", x, y + s * 6.6, '<span id="off-n">0</span><span style="font-size:0.42em; margin-left:0.18em;">cents</span>',
           "AVERAGE DISTANCE FROM THE NOTE", color=CORAL)
    offs = R["as_sung"]["offsets"]
    cells = "".join(f'<div class="off-c" style="display:flex; flex-direction:column; align-items:center; gap:{s * 0.2}px;">'
                    f'<span class="caps" style="font-size:{s * 0.9}px; color:{LILAC};">{n[:-1]}</span>'
                    f'<span class="num" style="font-size:{s * 1.25}px; color:{CORAL};">{o:+.0f}</span></div>' for n, o in zip(S["names"], offs))
    panel(f, "notes", y + s * 6.6 + f.s_stat * 1.75,
          caps("EACH NOTE, IN CENTS · C MAJOR", s, SOFT) + f'<div style="display:flex; justify-content:space-between; margin-top:{s * 0.6}px;">{cells}</div>')
    f.anim(f"""
inn("#ruler", {f.t('semitone') - 0.2}); grow("#ru-off", {f.t('twenty')}, 0.9);
inn("#off", {f.t('singer') - 0.2}); count("#off-n", {R['as_sung']['avg_off']:.1f}, {f.t('twenty')}, 1.2, 0);
inn("#notes", {f.t('cmajor')});
tl.fromTo(".off-c", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.4, stagger: 0.12, ease: "expo.out" }}, {f.t('never') - 0.4});
""")


# ================================================================== B03 · snap (retune speed)
KNOB = ('<svg id="knob" viewBox="-60 -60 120 120" style="flex:none; width:{w}px; height:{w}px;">'
        '<circle r="50" fill="#1B0F22" stroke="rgba(255,255,255,0.18)" stroke-width="3"/>'
        '<path d="M -35.4 35.4 A 50 50 0 1 1 35.4 35.4" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="8" stroke-linecap="round"/>'
        '<path id="knob-arc" d="M -35.4 35.4 A 50 50 0 1 1 35.4 35.4" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round" pathLength="100" stroke-dasharray="100 100" stroke-dashoffset="40"/>'
        '<g id="knob-hand"><line x1="0" y1="0" x2="0" y2="-38" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/></g>'
        '<circle r="8" fill="#FFFFFF"/></svg>')


def b03(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"roll": ROLL}
    lane_pins(f)
    f.mark_hud()
    kw = s * 3.6
    panel(f, "dial", y, f'<div style="display:flex; align-items:center; gap:{s * 0.9}px;">' + KNOB.format(w=kw, c=GOLD) +
          f'<div>{caps("RETUNE SPEED", s, SOFT)}<div class="num" style="font-size:{s * 2.4}px; margin-top:{s * 0.3}px;">'
          f'<span id="rs-n">60</span><span class="caps" style="font-size:{s}px; color:{SOFT}; margin-left:{s * 0.4}px;">ms</span></div></div></div>')
    g, h = R["gentle"], R["hard"]

    def row(rid, col, head, big, unit, sub):
        return (f'<div id="{rid}" class="glass" style="position:relative; flex:1; min-width:0; padding:{s * 0.6}px {s * 0.8}px;">'
                + caps(head, s * 0.9, col) +
                f'<div class="num" style="font-size:{s * 2.1}px; margin-top:{s * 0.35}px; color:{TEXT};">{big}<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; margin-left:{s * 0.3}px;">{unit}</span></div>'
                + caps(sub, s * 0.9, DIM, f"margin-top:{s * 0.3}px;") + "</div>")
    f.add(f'<div id="pair" class="abs" style="left:{x}px; top:{y + s * 6.0}px; width:{w}px; display:flex; flex-direction:{"column" if f.portrait else "row"}; gap:{s * 0.8}px;">'
          + row("gen", GOLD, "GENTLE · 60 ms", f"{g['avg_off']:.1f}", "CENTS OFF", "VIBRATO KEPT")
          + row("hrd", CYAN, "ZERO · INSTANT", f"{h['on_note'] * 100:.0f}%", "ON A NOTE", "WITHIN 5 CENTS") + "</div>")
    if not f.portrait:      # phone: the card heads already name the colours; the key goes so the column fits
        panel(f, "key", y + s * 12.4, caps("THE TRACKS", s, SOFT) + chip_row(f, [("AS SUNG", CORAL), ("GENTLE", GOLD), ("ZERO", CYAN)]))
    if not f.portrait:
        f.add(f'<div id="bel" class="glass" style="left:{x}px; top:{y + s * 17.0}px; display:flex; align-items:center; gap:{s * 0.7}px; padding:{s * 0.55}px {s * 0.8}px;">'
              f'<span style="width:{s * 0.55}px; height:{s * 0.55}px; border-radius:50%; background:{CYAN}; box-shadow:0 0 {10 * u}px {CYAN};"></span>'
              f'<span class="caps" style="font-size:{s}px; color:{TEXT};">Cher · “Believe” · 1998</span></div>')
    f.anim(f"""
inn("#dial", {f.t('speed') - 0.3});""" + ("" if f.portrait else f"""inn("#key", {f.t('nearest') - 0.2});""") + f"""
inn("#gen", {f.t('gentle') - 0.2});
(function () {{ const o = {{ v: 60 }}; const el = q("#rs-n");
  tl.to(o, {{ v: 0, duration: 0.7, ease: "power3.inOut", onUpdate: function () {{ el.textContent = Math.round(o.v); }} }}, {f.t('zero') - 0.1}); }})();
tl.fromTo("#knob-hand", {{ rotation: 36, svgOrigin: "0 0" }}, {{ rotation: -135, svgOrigin: "0 0", duration: 0.7, ease: "power3.inOut" }}, {f.t('zero') - 0.1});
tl.fromTo("#knob-arc", {{ strokeDashoffset: 40 }}, {{ strokeDashoffset: 100, duration: 0.7, ease: "power3.inOut" }}, {f.t('zero') - 0.1});
tl.to("#knob-arc", {{ stroke: "{CYAN}", duration: 0.3 }}, {f.t('zero') + 0.3});
inn("#hrd", {f.t('ninety') - 0.4});
""" + ("" if f.portrait else f'inn("#bel", {f.t("believe") - 0.3});'))


# ================================================================== B04 · shifting without chipmunks
def b04(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    sh = R["shift"]
    ff, env = envelope_curves()
    f.data = {"wave": S["frame"]["wave"], "tau_ms": S["frame"]["tau_ms"], "step_ms": S["frame"]["step_ms"], "ratio": sh["ratio"]}
    for i, (lab, col) in enumerate((("ORIGINAL", LILAC), ("SPED UP", CORAL), ("PSOLA", CYAN))):
        f.pin(f"rl{i}", lab, color=col)
        f.parts[-1] = f.parts[-1].replace("transform:translate(-50%,-50%)", "transform:translate(0,-100%)")
    f.mark_hud()
    ch = s * (8.0 if not f.portrait else 5.6)
    pw, ph = w - s * 1.8, ch - s * 4.0
    paths = "".join(f'<path id="env-{k}" d="{chart_path(ff, env[k], pw, ph, -40, 2)}" fill="none" stroke="{c}" stroke-width="{4.5 * u}" '
                    f'stroke-linejoin="round" {"stroke-dasharray=" + chr(34) + f"{12 * u} {9 * u}" + chr(34) if k == "orig" else ""} style="filter:drop-shadow(0 0 {5 * u}px {c});"/>'
                    for k, c in (("orig", LILAC), ("fast", CORAL), ("psola", CYAN)))
    lx0, lx1 = np.log10(ff[0]), np.log10(ff[-1])
    ticks = "".join(f'<div class="caps" style="position:absolute; left:{(np.log10(fx) - lx0) / (lx1 - lx0) * pw - s * 2:.1f}px; width:{s * 4}px; text-align:center; font-size:{s * 0.9}px; color:{DIM};">{lab}</div>'
                    for fx, lab in ((500, "500 Hz"), (1000, "1 kHz"), (2000, "2 kHz")))
    inner = (caps("THE VOWEL'S SHAPE · NOTE MOVED UP 4 SEMITONES", s, SOFT, "white-space:normal; line-height:1.35;") +
             f'<svg style="display:block; margin-top:{s * 0.6}px; overflow:visible;" width="{pw}" height="{ph}">{paths}</svg>'
             f'<div style="position:relative; height:{s * 1.2}px; margin-top:{s * 0.35}px;">{ticks}</div>' +
             chip_row(f, [("ORIGINAL", LILAC), ("SPED UP", CORAL), ("PSOLA", CYAN)]))
    panel(f, "envp", y, inner)
    by = y + ch + s * (3.6 if not f.portrait else 3.4)

    def bar(bid_, yy, lab, pct, col, dur):
        f.bar(bid_, x, yy, w, min(abs(pct) / 30, 1), col, lab, f"{pct:+.1f}%" if abs(pct) < 5 else f"+{pct:.0f}%")
        f.parts[-1] = f.parts[-1].replace('</div></div></div>', f'</div></div><div class="caps" style="font-size:{s * 0.9}px; color:{DIM}; margin-top:{s * 0.3}px;">{dur}</div></div>', 1)

    bar("b-fast", by, "SPED UP", (sh["resampled"]["env_shift"] - 1) * 100, CORAL, f"VOWEL MOVED · {sh['resampled']['dur']:.2f} s LONG (WAS {sh['orig']['dur']:.2f})")
    bar("b-cyc", by + s * 3.9, "PATENT'S WAY", (sh["cycles"]["env_shift"] - 1) * 100, GOLD, f"VOWEL MOVED · {sh['cycles']['dur']:.2f} s LONG")
    bar("b-psola", by + s * 7.8, "PSOLA", (sh["psola"]["env_shift"] - 1) * 100, CYAN, f"VOWEL MOVED · {sh['psola']['dur']:.2f} s LONG")
    f.anim(f"""
inn("#envp", {f.t('speed') - 0.4}); draw("#env-orig", {f.t('speed')}, 1.0);
inn("#b-fast", {f.t('shorter') - 0.2}); grow("#b-fast-f", {f.t('quarter') - 0.4}, 1.0); draw("#env-fast", {f.t('vowel') - 0.2}, 1.0);
inn("#b-cyc", {f.t('cycles') - 0.2}); grow("#b-cyc-f", {f.t('quarter') - 0.2}, 1.0);
inn("#b-psola", {f.t('respace') - 0.2}); grow("#b-psola-f", {f.t('one') - 0.3}, 0.8); draw("#env-psola", {f.t('psola')}, 1.0);
""")


# ================================================================== B05 · listen
HP_SVG = ('<svg viewBox="0 0 48 48" width="100%" height="100%"><path d="M8 30 v-6 a16 16 0 0 1 32 0 v6" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round"/>'
          '<rect x="5" y="27" width="9" height="14" rx="3" fill="currentColor"/><rect x="34" y="27" width="9" height="14" rx="3" fill="currentColor"/></svg>')


def b05(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    props = BEATS["B05"]["shot"]["remotion"]["props"]
    win = [{"from": round(l["from"] * f.D, 3), "to": round(l["to"] * f.D, 3)} for l in props.get("listen", [])]
    f.data = {"roll": ROLL, "win": win}
    lane_pins(f)
    f.mark_hud()
    f.add(f'<div id="hp" class="glass" style="left:{x}px; top:{y}px; width:{w}px; display:flex; align-items:center; gap:{s * 0.9}px; padding:{s * 0.7}px {s * 0.9}px;">'
          f'<div style="flex:none; width:{s * 2.6}px; height:{s * 2.6}px; color:{GOLD};">{HP_SVG}</div>'
          f'<div>{caps("NOW PLAYING", s, SOFT)}<div id="now" class="serif" style="font-size:{s * 1.6}px; margin-top:{s * 0.2}px; color:{TEXT};">—</div></div></div>')
    rows = [("r0", CORAL, "AS SUNG", f"{R['as_sung']['avg_off']:.0f} CENTS OFF · {R['as_sung']['on_note'] * 100:.0f}% ON A NOTE"),
            ("r1", GOLD, "GENTLE · 60 ms", f"{R['gentle']['avg_off']:.1f} CENTS OFF · VIBRATO KEPT"),
            ("r2", CYAN, "RETUNE SPEED ZERO", f"{R['hard']['on_note'] * 100:.0f}% WITHIN 5 CENTS OF A NOTE")]
    for i, (rid, col, head, sub) in enumerate(rows):
        f.add(f'<div id="{rid}" class="glass" style="left:{x}px; top:{y + s * (5.2 + i * 4.3)}px; width:{w}px; padding:{s * 0.6}px {s * 0.9}px;">'
              f'<div style="display:flex; align-items:center; gap:{s * 0.5}px;"><span style="width:{s * 0.55}px; height:{s * 0.55}px; border-radius:50%; background:{col}; box-shadow:0 0 {10 * u}px {col};"></span>'
              + caps(head, s, col) + "</div>" + caps(sub, s * 0.9, SOFT, f"margin-top:{s * 0.35}px; white-space:normal; line-height:1.35;") + "</div>")
    js = f'inn("#hp", {max(f.t("sung") - 0.6, 0.2)}); inn("#r0", {f.t("sung")}); inn("#r1", {f.t("gentle")}); inn("#r2", {f.t("zero")});\n'
    labels = ["As sung", "Gentle, 60 ms", "Retune speed zero"]
    for i, wv in enumerate(win):
        js += (f'tl.call(function () {{ q("#now").textContent = "{labels[i]}"; }}, null, {wv["from"]});'
               f'tl.call(function () {{ q("#now").textContent = "{labels[i - 1] if i else "—"}"; }}, null, {wv["from"] - 0.001});\n')
        js += f'tl.to("#r{i}", {{ borderColor: "{rows[i][1]}", duration: 0.3 }}, {wv["from"]}); tl.to("#r{i}", {{ borderColor: "rgba(255,255,255,0.14)", duration: 0.3 }}, {wv["to"]});\n'
    f.anim(js)


# ================================================================== B06 · then and now
def b06(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"wave": S["frame"]["wave"]}
    f.mark_hud()

    def card(cid, yy, year, col, line1, line2):
        f.add(f'<div id="{cid}" class="glass" style="left:{x}px; top:{yy}px; width:{w}px; display:flex; gap:{s * 1.0}px; align-items:center; padding:{s * 0.7}px {s * 0.9}px;">'
              f'<div class="num" style="flex:none; font-size:{s * 2.0}px; color:{col};">{year}</div>'
              f'<div>{caps(line1, s, TEXT, "white-space:normal; line-height:1.3;")}{caps(line2, s * 0.9, SOFT, f"margin-top:{s * 0.3}px; white-space:normal; line-height:1.35;")}</div></div>')

    card("c97", y, "1997", GOLD, "AUTO-TUNE IS RELEASED", "ANTARES AUDIO TECHNOLOGIES")
    card("oil", y + s * 5.0, "OIL", LILAC, "THE MATHS CAME FIRST", "USED TO READ SEISMIC DATA")
    card("now", y + s * 10.0, "NOW", CYAN, "A STANDARD STUDIO TOOL", "OFTEN TOO SUBTLE TO NOTICE")
    f.anim(f'inn("#c97", {f.t("came") - 0.2}); inn("#oil", {f.t("oil") - 0.3}); inn("#now", {f.t("today") - 0.1});')


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06}

if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if a.startswith("B")] or None
    dst = HERE / "hyperframes" / "assets" / "kit3.js"
    if not dst.exists() or dst.read_bytes() != (KIT / "kit3.js").read_bytes():     # only when changed (mtime drives re-renders)
        shutil.copy(KIT / "kit3.js", dst)
    hfkit.build(LOOK, BUILDERS, only)
    if "--render" in sys.argv:
        hfkit.render(LOOK, BUILDERS, only, aspects=[a for a in ("l", "v") if f"--{a}" in sys.argv] or ("l", "v"))
