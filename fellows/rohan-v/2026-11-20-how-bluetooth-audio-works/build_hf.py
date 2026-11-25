"""Builds the HyperFrames + three.js compositions for "How Bluetooth Audio Works" (B01-B06):
hyperframes/B0x-l.html (3840x2160) and B0x-v.html (2160x3840); each page's 3D stage is drawn by
hyperframes/scenes/B0x.js (three.js, seeked frame by frame), the HUD is HTML on the beat's word-clock cues.

LOOK: "the radio sky". Near-black blue; music is violet light, the radio link Bluetooth blue, Wi-Fi orange; a try that
gets through is green, a lost one red, everywhere (3D and HUD). Source Serif 4 titles, Inter HUD.

DATA: everything drawn comes from evidence/scene.json (bluetooth.py) and the beat sheet: the hops in B02 are the
simulation's own tries, the buffer levels in B04 its own window (the same 6 s the listening clips come from).

    python build_hf.py [B03 ...]            # write the compositions
    python build_hf.py [B03 ...] --render   # and render: media/B0x.mp4 (16:9), pantry/B0x-916.mp4 (9:16)
"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "_kit" if (HERE / "_kit").is_dir() else HERE.parent / "_kit"     # the shared week-13 kit (a copy ships in _kit/)
sys.path.insert(0, str(KIT))
import hfkit  # noqa: E402

sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
R = S["results"]
BEATS = {b["beat_id"]: b for b in sheet["beats"]}
CODEC = {c["codec"]: c for c in R["codecs"]}
BUF = {int(b["ms"]): b for b in R["buffers"]}

P = {"bg": "#030A12", "text": "#EAF4FF", "soft": "#A6BED6", "dim": "#5B7590", "chap": "#3DA9FF", "acc": "#3DA9FF",
     "glass": "rgba(255,255,255,0.05)", "gline": "rgba(255,255,255,0.14)", "chip": "#FFFFFF",
     "ground_l": "radial-gradient(ellipse 54% 62% at 34% 56%, #0B2036 0%, #06121F 55%, #030A12 100%)",
     "ground_v": "radial-gradient(ellipse 80% 40% at 50% 30%, #0C2239 0%, #061321 55%, #030A12 100%)"}
BLUE, ORANGE, GREEN, RED, VIOLET, GOLD = "#3DA9FF", "#FF9F43", "#5BE49B", "#FF5C6C", "#B48CFF", "#FFD166"
TEXT, SOFT, DIM = P["text"], P["soft"], P["dim"]
CHAPTER = {"B01": "01 · TOO MUCH DATA", "B02": "02 · THE RADIO", "B03": "03 · CODECS", "B04": "04 · THE BUFFER",
           "B05": "05 · LIP SYNC", "B06": "06 · LE AUDIO"}
PTITLE = {"B01": "Too Much Data", "B02": "Seventy-Nine Channels", "B03": "Picking a Codec",
          "B04": "Music in Reserve", "B05": "Holding the Picture", "B06": "What Comes Next"}
SPARKS = {"B01": "Squeeze it to a quarter before it leaves the phone.",
          "B02": "Hop around the busy channels.",
          "B03": "More data can sound better, and break up sooner.",
          "B04": "A bigger reserve: fewer gaps, more delay.",
          "B05": "Videos can wait for the sound. Games can't.",
          "B06": "Less data, one phone to many ears."}
LOOK = hfkit.Look(HERE, BEATS, CHAPTER, PTITLE, SPARKS, P, "apple-01.svg")


def caps(t, size, color, extra=""):
    return f'<div class="caps" style="font-size:{size}px; color:{color}; {extra}">{t}</div>'


def panel(f, pid, y, inner, w=None, x=None, pad=(0.7, 0.9)):
    s = f.s_label
    f.add(f'<div id="{pid}" class="glass" style="left:{f.hx if x is None else x}px; top:{y}px; width:{f.hw if w is None else w}px; '
          f'padding:{s * pad[0]}px {s * pad[1]}px;">{inner}</div>')


def tag2(f, gid, text, x, y, logo, chip_bg="#FFFFFF"):
    """LOGO LAW: the company's own mark beside its name (logos from the toolkit's icons/logos)."""
    s, p = f.s_label, f.p
    wrapw = f.hw - s * 4.6
    f.add(f'<div id="{gid}" class="glass" style="left:{x}px; top:{y}px; display:flex; align-items:center; gap:{s * 0.6}px; padding:{s * 0.55}px {s * 0.8}px;">'
          f'<span style="display:flex; flex:none; width:{s * 1.9}px; height:{s * 1.9}px; border-radius:{s * 0.45}px; background:{chip_bg}; align-items:center; justify-content:center;">'
          f'<img src="assets/{logo}" style="height:{s * 1.3}px;" /></span>'
          f'<span class="caps" style="font-size:{s}px; color:{p["text"]}; white-space:normal; max-width:{wrapw}px; line-height:1.35;">{text}</span></div>')


def chip_row(f, items):
    s = f.s_label
    return ('<div style="display:flex; flex-wrap:wrap; gap:' + f'{s * 0.5}px {s * 1.1}px; margin-top:{s * 0.5}px;">' +
            "".join(f'<span style="display:flex; align-items:center; gap:{s * 0.4}px;"><span style="width:{s * 0.55}px; height:{s * 0.55}px; '
                    f'border-radius:50%; background:{c}; box-shadow:0 0 {s * 0.25}px {c};"></span>'
                    f'<span class="caps" style="font-size:{s * 0.9}px; color:{SOFT};">{t}</span></span>' for t, c in items) + "</div>")


# ================================================================== B01 · too much data
def b01(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    sbc = CODEC["SBC"]
    f.data = {"ratio": sbc["ratio"]}
    f.pin("pl-cd", "CD QUALITY", color=VIOLET)
    f.pin("pl-link", "BLUETOOTH LINK", color=BLUE)
    f.pin("pl-codec", "SBC", color=BLUE)
    f.mark_hud()
    f.stat("cd", x, y, '<span id="cd-n">0</span><span style="font-size:0.38em; margin-left:0.2em;">kbit/s</span>',
           "CD-QUALITY STEREO", color=VIOLET)
    f.note("math", "44,100 samples × 16 bits × 2 channels, every second.", x, y + f.s_stat * 1.75, w, color=SOFT)
    yy = y + f.s_stat * 1.75 + s * 3.0
    f.stat("sbc", x, yy, '<span id="sbc-n">0</span><span style="font-size:0.38em; margin-left:0.2em;">kbit/s</span>',
           "SBC ON MY TEST TRACK · MEASURED", color=BLUE)
    by = yy + f.s_stat * 1.75
    f.add(f'<div id="cmp" class="abs" style="left:{x}px; top:{by}px; width:{w}px;">'
          f'<div style="height:{s * 0.5}px; border-radius:{s * 0.25}px; background:{VIOLET}; opacity:0.85;"></div>'
          f'<div id="cmp-b" style="margin-top:{s * 0.4}px; width:{100 / sbc["ratio"]:.1f}%; height:{s * 0.5}px; border-radius:{s * 0.25}px; background:{BLUE}; box-shadow:0 0 {12 * u}px {BLUE};"></div>'
          f'<div class="caps" style="margin-top:{s * 0.5}px; font-size:{s}px; color:{TEXT};">UNDER A QUARTER <span style="color:{SOFT};">· 1 / {sbc["ratio"]:.1f}</span></div></div>')
    tag2(f, "ff", "ENCODED WITH FFMPEG'S SBC ENCODER", x, by + s * 4.0, "ffmpeg-01.svg")
    f.anim(f"""
inn("#cd", {f.t('cd') - 0.2}); count("#cd-n", {R['cd_kbps']:.0f}, {f.t('fourteen') - 0.3}, 1.2, 0);
inn("#math", {f.t("fourteen") + 0.8});
""" + f"""
inn("#sbc", {f.t('test') - 0.3}); count("#sbc-n", {sbc['kbps']:.0f}, {f.t('three') - 0.2}, 1.1, 0);
inn("#cmp", {f.t('three')}); grow("#cmp-b", {f.t('three') + 0.2}, 1.0); inn("#ff", {f.t('quarter')});
""")


# ================================================================== B02 · the radio (hopping)
def b02(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    off, on = R["runs"]["afh_False"], R["runs"]["afh_True"]
    f.data = {"hops_off": S["hops_off"], "hops_on": S["hops_on"], "wifi": S["wifi"]}
    f.pin("pl-wifi", "WI-FI", color=ORANGE)
    f.mark_hud()
    f.add(f'<div id="ch" class="abs" style="left:{x}px; top:{y}px; width:{w}px; display:flex; gap:{s * 0.8}px;">'
          f'<div class="glass" style="position:relative; flex:1; padding:{s * 0.6}px {s * 0.8}px;">{caps("CHANNELS", s * 0.9, SOFT)}'
          f'<div class="num" style="font-size:{s * 2.4}px; margin-top:{s * 0.3}px;">79</div></div>'
          f'<div class="glass" style="position:relative; flex:1; padding:{s * 0.6}px {s * 0.8}px;">{caps("HOPS PER SECOND", s * 0.9, SOFT)}'
          f'<div class="num" style="font-size:{s * 2.4}px; margin-top:{s * 0.3}px;"><span class="caps" style="font-size:{s * 0.9}px; color:{SOFT}; letter-spacing:0.1em; margin-right:{s * 0.3}px;">UP TO</span>1,600</div></div></div>')
    f.stat("loss0", x, y + s * 6.2, '<span id="l0-n">0</span><span style="font-size:0.5em;">%</span>',
           "OF TRIES FAILED · BUSY WI-FI", color=RED, size=f.s_stat * 0.8)
    f.stat("loss1", x, y + s * 6.2 + f.s_stat * 1.55, '<span id="l1-n">0</span><span style="font-size:0.5em;">%</span>',
           "WITH ADAPTIVE HOPPING", color=GREEN, size=f.s_stat * 0.8)
    panel(f, "key", y + s * 6.2 + f.s_stat * 3.1, caps("MY SIMULATION · 2 MINUTES", s * 0.9, SOFT) +
          chip_row(f, [("WI-FI", ORANGE), ("GOT THROUGH", GREEN), ("LOST", RED)]))
    f.anim(f"""
inn("#ch", {f.t('seventy') - 0.3}); inn("#key", {f.t('sim') - 0.2});
inn("#loss0", {f.t('seventeen') - 0.4}); count("#l0-n", {off['loss_quiet'] * 100:.0f}, {f.t('seventeen') - 0.2}, 1.0, 0);
inn("#loss1", {f.t('one') - 0.5}); count("#l1-n", {on['loss_quiet'] * 100:.1f}, {f.t('one') - 0.3}, 1.0, 1);
""")


# ================================================================== B03 · codecs
def b03(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    rows = [("SBC", CODEC["SBC"]["kbps"], BLUE, "EVERY DEVICE", "sbc"),
            ("AAC", CODEC["AAC"]["kbps"], "#E8EEF5", "APPLE", "aac"),
            ("aptX", CODEC["aptX"]["kbps"], GOLD, "ANDROID", "aptx"),
            ("LDAC", 990, VIOLET, "UP TO, SONY", "ldac")]
    f.data = {"rows": [[n, k] for n, k, *_ in rows]}
    for n, *_ in rows:
        f.pin(f"pl-{n.lower()}", n, color=TEXT)
    f.mark_hud()
    gap = s * (3.4 if not f.portrait else 3.2)
    for i, (n, k, col, sub, cue) in enumerate(rows):
        f.bar(f"bar-{cue}", x, y + i * gap, w, k / 1000, col, f"{n} · {sub}", f"{k:.0f}" + ("" if n != "LDAC" else ""))
    ty = y + len(rows) * gap + s * 0.4
    if not f.portrait:
        f.note("meas", "SBC, AAC and aptX measured on my test track with ffmpeg's encoders (kbit/s); LDAC from Sony.", x, ty, w, size=s * 1.05, color=SOFT)
        ty += s * 3.6
    else:
        f.label("meas", "KBIT/S · MEASURED WITH FFMPEG'S ENCODERS · LDAC: SONY", x, ty, color=SOFT, size=s * 0.9, wrapw=w)
        ty += s * 3.2
    tag2(f, "apple", "APPLE DEVICES PREFER AAC", x, ty, "apple-01.svg")
    tag2(f, "android", "aptX · LDAC ON MANY ANDROID PHONES", x, ty + s * 3.0, "android-01.svg")
    f.anim(f"""
inn("#bar-sbc", {f.t('sbc') - 0.3}); grow("#bar-sbc-f", {f.t('sbc')}, 0.9);
inn("#bar-aac", {f.t('aac') - 0.3}); grow("#bar-aac-f", {f.t('aac')}, 0.9); inn("#apple", {f.t('aac') + 0.2});
inn("#bar-aptx", {f.t('aptx') - 0.3}); grow("#bar-aptx-f", {f.t('aptx')}, 0.9); inn("#android", {f.t('aptx') + 0.3});
inn("#bar-ldac", {f.t('ldac') - 0.3}); grow("#bar-ldac-f", {f.t('ldac')}, 1.2);
inn("#meas", {f.t("more")});
""")


# ================================================================== B04 · the buffer (+ listening)
HP_SVG = ('<svg viewBox="0 0 48 48" width="100%" height="100%"><path d="M8 30 v-6 a16 16 0 0 1 32 0 v6" fill="none" stroke="currentColor" stroke-width="3.6" stroke-linecap="round"/>'
          '<rect x="5" y="27" width="9" height="14" rx="3" fill="currentColor"/><rect x="34" y="27" width="9" height="14" rx="3" fill="currentColor"/></svg>')


def b04(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    props = BEATS["B04"]["shot"]["remotion"]["props"]
    win = [{"from": round(l["from"] * f.D, 3), "to": round(l["to"] * f.D, 3)} for l in props.get("listen", [])]
    clips = BEATS["B04"].get("listen_clips", [])
    f.data = {"small": S["level_small"], "large": S["level_large"], "gaps": S["gaps_small"], "fades": S["fades"],
              "w0": S["w0"], "win": win, "clip_from": [c["clip_from_s"] for c in clips] or [1.5, 1.5],
              "small_ms": R["listen"]["small_ms"], "large_ms": R["listen"]["large_ms"]}
    f.pin("pl-s", "50 ms", color=RED)
    f.pin("pl-l", "200 ms", color=GREEN)
    f.pin("pl-glitch", "GAP", color=RED)
    f.mark_hud()
    gmax = max(BUF[b]["gaps"] for b in (50, 100, 200, 300))
    rows = ""
    for b in (50, 100, 200, 300):
        g = BUF[b]["gaps"]
        col = RED if g > 10 else (GOLD if g > 0 else GREEN)
        rows += (f'<div class="brow" style="display:flex; align-items:center; gap:{s * 0.6}px; margin-top:{s * 0.55}px;">'
                 f'<span class="caps" style="width:{s * 4.6}px; font-size:{s * 0.9}px; color:{SOFT};">{b} ms</span>'
                 f'<div style="flex:1; height:{s * 0.5}px; border-radius:{s * 0.25}px; background:rgba(255,255,255,0.07);">'
                 f'<div class="brow-f" style="width:{max(g / gmax, 0.012) * 100:.1f}%; height:100%; border-radius:{s * 0.25}px; background:{col}; box-shadow:0 0 {10 * u}px {col};"></div></div>'
                 f'<span class="num" style="width:{s * 2.6}px; text-align:right; font-size:{s * 1.4}px; color:{col};">{g}</span></div>')
    panel(f, "tab", y, caps("GLITCHES IN 2 MINUTES · BY BUFFER SIZE", s, SOFT, "white-space:normal; line-height:1.35;") + rows)
    hy = y + s * 10.4
    f.add(f'<div id="hp" class="glass" style="left:{x}px; top:{hy}px; width:{w}px; display:flex; align-items:center; gap:{s * 0.9}px; padding:{s * 0.7}px {s * 0.9}px;">'
          f'<div style="flex:none; width:{s * 2.6}px; height:{s * 2.6}px; color:{BLUE};">{HP_SVG}</div>'
          f'<div>{caps("NOW PLAYING", s, SOFT)}<div id="now" class="serif" style="font-size:{s * 1.6}px; margin-top:{s * 0.2}px; color:{TEXT};">—</div></div></div>')
    if not f.portrait:
        f.note("lag", "The reserve is the delay: every millisecond kept back is a millisecond late.", x, hy + s * 4.6, w, color=SOFT)
    js = f"""
inn("#tab", {f.t('fifty') - 0.6});
tl.fromTo(".brow", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.5, stagger: 0.0, ease: "expo.out" }}, {f.t('fifty') - 0.3});
tl.fromTo(".brow-f", {{ scaleX: 0, transformOrigin: "0% 50%" }}, {{ scaleX: 1, duration: 0.9, stagger: 0.55, ease: "expo.out" }}, {f.t('fifty')});
inn("#hp", {f.t('listen') - 0.3});
""" + ("" if f.portrait else f'inn("#lag", {f.t("lag") - 0.2});\n')
    labels = ["A 50 ms buffer", "A 200 ms buffer"]
    for i, wv in enumerate(win):
        js += f'tl.call(function () {{ q("#now").textContent = "{labels[i]}"; }}, null, {wv["from"]});\n'
        js += f'tl.call(function () {{ q("#now").textContent = "{labels[i - 1] if i else "—"}"; }}, null, {wv["from"] - 0.001});\n'
    f.anim(js)


# ================================================================== B05 · lip sync
def b05(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.pin("pl-vid", "PICTURE", color=VIOLET)
    f.pin("pl-snd", "SOUND", color=BLUE)
    f.pin("pl-lag", "BEHIND", color=GOLD)
    f.mark_hud()
    f.stat("lag", x, y, '170–370<span style="font-size:0.38em; margin-left:0.2em;">ms</span>',
           "BEHIND · TWO PUBLISHED TESTS", color=GOLD, size=f.s_stat * 0.8)

    def step(sid, yy, n, col, head, sub):
        f.add(f'<div id="{sid}" class="glass" style="left:{x}px; top:{yy}px; width:{w}px; display:flex; gap:{s * 0.8}px; align-items:center; padding:{s * 0.6}px {s * 0.9}px;">'
              f'<div class="num" style="flex:none; font-size:{s * 1.9}px; color:{col};">{n}</div>'
              f'<div>{caps(head, s, TEXT, "white-space:normal; line-height:1.3;")}{caps(sub, s * 0.9, SOFT, f"margin-top:{s * 0.25}px; white-space:normal; line-height:1.35;")}</div></div>')

    step("s1", y + f.s_stat * 1.55, "1", BLUE, "THE HEADPHONES REPORT THEIR DELAY", "DELAY REPORTING · A2DP")
    step("s2", y + f.s_stat * 1.55 + s * 4.6, "2", VIOLET, "THE PHONE HOLDS THE PICTURE BACK", "SO THEY LINE UP AGAIN")
    step("s3", y + f.s_stat * 1.55 + s * 9.2, "✕", RED, "GAMES CAN'T WAIT", "YOUR BUTTON PRESS HAPPENS NOW")
    f.anim(f"""
inn("#lag", {f.t('behind') - 0.3}); inn("#s1", {f.t('report') - 0.3}); inn("#s2", {f.t('holds') - 0.3}); inn("#s3", {f.t('game') - 0.2});
""")


# ================================================================== B06 · LE Audio
def b06(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.pin("pl-src", "ONE PHONE OR TV", color=BLUE)
    f.mark_hud()

    def card(cid, yy, head, col, big, sub):
        f.add(f'<div id="{cid}" class="glass" style="left:{x}px; top:{yy}px; width:{w}px; padding:{s * 0.7}px {s * 0.9}px;">'
              + caps(head, s * 0.9, col) +
              f'<div class="serif" style="font-size:{s * 1.5}px; margin-top:{s * 0.3}px; line-height:1.25;">{big}</div>'
              + caps(sub, s * 0.9, DIM, f"margin-top:{s * 0.35}px; white-space:normal; line-height:1.35;") + "</div>")

    card("le", y, "LE AUDIO", BLUE, "Bluetooth audio's next generation", "ANNOUNCED 2020 · SPECS DONE 2022")
    card("lc3", y + s * 5.6, "LC3 · THE NEW CODEC", GREEN, "Beats SBC at half the bit rate", "SAYS THE BLUETOOTH SIG")
    card("aura", y + s * 11.2, "AURACAST", GOLD, "One phone or TV, any number of earbuds", "BROADCAST AUDIO")
    f.anim(f'inn("#le", {f.t("le") - 0.3}); inn("#lc3", {f.t("lc3") - 0.2}); inn("#aura", {f.t("auracast") - 0.3});')


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06}

if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if a.startswith("B")] or None
    dst = HERE / "hyperframes" / "assets" / "kit3.js"
    if not dst.exists() or dst.read_bytes() != (KIT / "kit3.js").read_bytes():     # only when changed (mtime drives re-renders)
        shutil.copy(KIT / "kit3.js", dst)
    hfkit.build(LOOK, BUILDERS, only)
    if "--render" in sys.argv:
        hfkit.render(LOOK, BUILDERS, only, aspects=[a for a in ("l", "v") if f"--{a}" in sys.argv] or ("l", "v"))
