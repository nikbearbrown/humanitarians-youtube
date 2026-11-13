"""Builds the HyperFrames + three.js compositions for "How Netflix Streams" (B01-B06):
hyperframes/B0x-l.html (3840x2160) and B0x-v.html (2160x3840); each page's 3D stage is drawn by
hyperframes/scenes/B0x.js (three.js, seeked frame by frame), the HUD is HTML on the beat's word-clock cues.

LOOK: "the player at night". Netflix's own black and red: a black ground with a faint red glow, white for the clean
test card, Netflix red for the grainy clip and for the top quality, Netflix grey (#B3B3B3) for secondary text.
The ladder panes show the run's real encodes (evidence/rungs/*.png: frames of stream.py's libx264 files).

DATA: evidence/scene.json + results.json (stream.py) and week-12/_research/facts-netflix.md.

    python build_hf.py [B03 ...]            # write the compositions
    python build_hf.py [B03 ...] --render   # and render: media/B0x.mp4 (16:9), pantry/B0x-916.mp4 (9:16)
"""
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "_kit" if (HERE / "_kit").is_dir() else HERE.parent / "_kit"     # the shared week-12 kit (a copy ships in _kit/)
sys.path.insert(0, str(KIT))
import hfkit  # noqa: E402

sheet = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
S = json.loads((HERE / "evidence" / "scene.json").read_text(encoding="utf-8"))
BEATS = {b["beat_id"]: b for b in sheet["beats"]}

RED, WHITE, GREY = "#E50914", "#F5F5F1", "#B3B3B3"
P = {"bg": "#000000", "text": "#FFFFFF", "soft": GREY, "dim": "#6D6D6D", "chap": RED, "acc": RED,
     "glass": "rgba(255,255,255,0.045)", "gline": "rgba(255,255,255,0.13)", "chip": "#000000",
     "ground_l": "radial-gradient(ellipse 60% 70% at 30% 58%, #2A0508 0%, #0B0102 52%, #000000 100%)",
     "ground_v": "radial-gradient(ellipse 85% 40% at 50% 30%, #2A0508 0%, #0B0102 52%, #000000 100%)"}
DIM = P["dim"]
CHAPTER = {"B01": "01 · THE LADDER", "B02": "02 · THE SCORE", "B03": "03 · PER TITLE", "B04": "04 · THE PLAYER",
           "B05": "05 · CLOSE BY", "B06": "06 · SCALE"}
PTITLE = {"B01": "Many Copies of Every Show", "B02": "A Score for How It Looks", "B03": "A Ladder for Each Show",
          "B04": "Choose Every Chunk", "B05": "A Server Near You", "B06": "The Whole System"}
SPARKS = {"B01": "One show, six qualities, all stored ahead of time.",
          "B02": "VMAF scores the picture the way people see it.",
          "B03": "Easy pictures need fewer bits; hard ones need more.",
          "B04": "Watch the buffer, not the speed guess.",
          "B05": "Shorter trips mean faster chunks.",
          "B06": "Many copies, chosen chunk by chunk, from a box near you."}
LOOK = hfkit.Look(HERE, BEATS, CHAPTER, PTITLE, SPARKS, P, "netflix-01.svg")
LAD = S["ladder"]


def kb(k):
    return f"{k:,}"


def res(r):
    return f'{r["h"]}p' if r["h"] >= 720 else f'{r["w"]}×{r["h"]}'


def imgs(f, clips=("simple", "busy")):
    for c in clips:
        for r in S["rungs"]:
            f.add(f'<img id="rung-{c}-{r}" src="assets/rungs/{c}_{r}.png" alt="" style="position:absolute; width:4px; height:4px; opacity:0; pointer-events:none;" />')


# ================================================================== B01 · the ladder
def b01(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    imgs(f)
    f.data = {"rungs": S["rungs"], "ladder": LAD}
    f.mark_hud()
    rows = "".join(
        f'<div class="lrow" style="display:flex; justify-content:space-between; align-items:baseline; padding:{s * 0.32}px 0; border-top:{1.5 * u}px solid rgba(255,255,255,0.1);">'
        f'<span class="num" style="font-size:{s * 1.35}px; color:{RED if i == 5 else P["text"]};">{kb(r["kbps"])}<span class="caps" style="font-size:{s * 0.9}px; color:{GREY}; margin-left:{s * 0.3}px;">kbit/s</span></span>'
        f'<span class="caps" style="font-size:{s * 0.9}px; color:{GREY};">{res(r)}</span></div>'
        for i, r in reversed(list(enumerate(LAD["simple"]))))
    f.add(f'<div id="ladder" class="abs" style="left:{x}px; top:{y}px; width:{w}px;">'
          f'<div class="caps" style="font-size:{s}px; color:{RED}; margin-bottom:{s * 0.4}px;">ONE SHOW, SIX RUNGS</div>{rows}</div>')
    cw = (w - s * 0.8) / 2
    if f.portrait:          # phone: the 3D panes already switch clips on the word; the clip cards go (no room)
        f.anim(f"""
inn("#ladder", {f.t('ladder') - 0.3});
tl.fromTo(".lrow", {{ opacity: 0, x: {-20 * u} }}, {{ opacity: 1, x: 0, duration: 0.5, stagger: -0.14, ease: "expo.out" }}, {f.t('ladder')});
""")
        return
    f.add(f'<div id="clips" class="abs" style="left:{x}px; top:{y + s * 12.4}px; width:{w}px; display:flex; gap:{s * 0.8}px;">'
          f'<div id="clip-a" class="glass" style="position:relative; width:{cw}px; padding:{s * 0.6}px {s * 0.8}px;"><div class="caps" style="font-size:{s * 0.9}px; color:{GREY};">TEST CLIP 1</div>'
          f'<div class="serif" style="font-size:{s * 1.4}px; margin-top:{s * 0.2}px;">Clean test card</div></div>'
          f'<div id="clip-b" class="glass" style="position:relative; width:{cw}px; padding:{s * 0.6}px {s * 0.8}px;"><div class="caps" style="font-size:{s * 0.9}px; color:{GREY};">TEST CLIP 2</div>'
          f'<div class="serif" style="font-size:{s * 1.4}px; margin-top:{s * 0.2}px; color:#FF6B72;">Grainy zoom</div></div></div>')
    f.anim(f"""
inn("#ladder", {f.t('ladder') - 0.3});
tl.fromTo(".lrow", {{ opacity: 0, x: {-20 * u} }}, {{ opacity: 1, x: 0, duration: 0.5, stagger: -0.14, ease: "expo.out" }}, {f.t('ladder')});
inn("#clips", {f.t('two')}); tl.fromTo("#clip-a", {{ borderColor: "rgba(255,255,255,0.13)" }}, {{ borderColor: "rgba(255,255,255,0.7)", duration: 0.4 }}, {f.t('card')});
tl.to("#clip-a", {{ borderColor: "rgba(255,255,255,0.13)", duration: 0.4 }}, {f.t('grainy')});
tl.fromTo("#clip-b", {{ borderColor: "rgba(255,255,255,0.13)" }}, {{ borderColor: "{RED}", duration: 0.4 }}, {f.t('grainy')});
""")


# ================================================================== B02 · VMAF
def b02(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"ladder": LAD}
    ps = s * 0.9
    for i, r in enumerate(LAD["simple"]):
        if f.portrait and i not in (0, 5):      # phone: only the ends, so the labels never collide
            continue
        f.pin(f"pk{i}", f'{r["kbps"]:,}' + (" kbit/s" if f.portrait and i == 5 else ""), size=ps)
    f.pin("p100", "100", color=GREY, size=ps)
    f.pin("p50", "50", color=DIM, size=ps)
    f.mark_hud()
    f.add(f'<div id="vm" class="abs" style="left:{x}px; top:{y}px; width:{w}px;">'
          f'<div class="num" style="font-size:{f.s_stat}px;">VMAF</div>'
          f'<div class="caps" style="font-size:{s}px; color:{GREY}; margin-top:{s * 0.4}px;">A QUALITY SCORE FROM <span style="color:{P["text"]};">0</span> TO <span style="color:{P["text"]};">100</span></div></div>')
    f.tag("nf", "Netflix · open-sourced 2016", x, y + f.s_stat * 1.55)
    sy = y + f.s_stat * 1.55 + s * 3.6
    cw = (w - s * 1.6) / 3
    lo, hi = LAD["simple"][0]["vmaf"], LAD["simple"][-1]["vmaf"]
    bt = LAD["busy"][-1]["vmaf"]
    f.add(f'<div id="sc" class="abs" style="left:{x}px; top:{sy}px; width:{w}px; display:flex; gap:{s * 0.8}px;">'
          + "".join(f'<div id="{i}" style="width:{cw}px;"><div class="num" style="font-size:{s * 3.2}px; color:{c};"><span id="{i}-n">0</span></div>'
                    f'<div class="caps" style="font-size:{s * 0.9}px; color:{GREY}; margin-top:{s * 0.3}px; white-space:normal; line-height:1.3;">{lab}</div></div>'
                    for i, c, lab in (("s-lo", WHITE, "CARD · LOWEST RUNG"), ("s-hi", WHITE, "CARD · TOP RUNG"), ("s-bt", "#FF6B72", "GRAINY · TOP RUNG")))
          + "</div>")
    f.anim(f"""
inn("#vm", {f.t('score') - 0.2}); inn("#nf", {f.t('away')});
inn("#sc", {f.t('lowest') - 0.4});
count("#s-lo-n", {round(lo)}, {f.t('lowest')}, 0.9, 0); count("#s-hi-n", {round(hi)}, {f.t('top')}, 1.0, 0); count("#s-bt-n", {round(bt)}, {f.t('grain')}, 1.0, 0);
tl.fromTo("#s-hi", {{ opacity: 0.25 }}, {{ opacity: 1, duration: 0.4 }}, {f.t('top') - 0.2});
tl.fromTo("#s-bt", {{ opacity: 0.25 }}, {{ opacity: 1, duration: 0.4 }}, {f.t('grain') - 0.2});
""")


# ================================================================== B03 · per title
def b03(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    need = S["need"]["simple"]
    f.data = {"ladder": LAD, "need": need, "target": S["target"]}
    ps = s * 0.9
    f.pin("pt", "TARGET · SCORE 93", color=P["text"], size=ps)
    f.pin("pa", "CLEAN CARD", color=WHITE, size=ps)
    f.pin("pb", "GRAINY ZOOM", color="#FF6B72", size=ps)
    f.pin("px", "BITRATE →", color=DIM, size=ps)
    if not f.portrait:
        f.pin("py", "SCORE", color=DIM, size=ps)
    f.mark_hud()
    f.stat("st1", x, y, f'{need / 1000:.1f}<span style="font-size:0.42em; margin-left:0.18em;">Mbit/s</span>', "CLEAN CARD REACHES A SCORE OF 93", color=WHITE)
    f.stat("st2", x, y + f.s_stat * 1.9, 'never', "GRAINY CLIP, EVEN AT 5.8 MBIT/S", color="#FF6B72")
    f.tag("nf", "Per-title encoding · since 2015", x, y + f.s_stat * 3.8)
    f.anim(f"""
inn("#st1", {f.t('card') + 0.6}); inn("#st2", {f.t('never')}); inn("#nf", {f.t('since')});
""")


# ================================================================== B04 · the player
def b04(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    runs = S["runs"]
    # stall marks: in stream.py's player a stall empties the buffer, so the buffer after that chunk is exactly one
    # chunk (4.0 s); the stall's length is that chunk's download time minus the buffer it had. Checked against
    # run.log: one stall (chunk 50, 6.89 s) for always-the-best, none for the other two.
    stalls = {}
    for k, v in runs.items():
        st = [i for i in range(1, len(v)) if abs(v[i]["buf"] - 4.0) < 1e-6]
        tot = sum(v[i]["t"] - v[i - 1]["t"] - v[i - 1]["buf"] for i in st)
        assert abs(tot - S["player"][k]["stall"]) < 0.06, (k, tot)
        stalls[k] = st
    # the connection speed (scene.json: one sample per 2 s of clock time) placed on the chunk axis by the clock time
    # at which the buffer-based player fetched each chunk
    tb = [0.0] + [r["t"] for r in runs["buffer"]]
    bwx = []
    for j, b in enumerate(S["bw"]):
        c = 2.0 * j
        if c > tb[-1]:
            break
        k = next(i for i in range(1, len(tb)) if tb[i] >= c)
        bwx.append([round(k - 1 + (c - tb[k - 1]) / max(1e-6, tb[k] - tb[k - 1]), 3), b])
    f.data = {"q": {k: [r["q"] for r in v] for k, v in runs.items()}, "bw": bwx, "stalls": stalls}
    f.mark_hud()
    pl = S["player"]
    rows = [("highest", "ALWAYS THE BEST QUALITY", RED), ("buffer", "BY HOW FULL THE BUFFER IS", WHITE), ("throughput", "BY SPEED", GREY)]
    ph = s * 4.6
    for i, (k, lab, col) in enumerate(rows):
        r = pl[k]
        stall = f'{r["stall"]:.1f} s' if r["stall"] > 0 else "0 s"
        f.add(f'<div id="p-{k}" class="glass" style="left:{x}px; top:{y + i * (ph + s * 0.8)}px; width:{w}px; padding:{s * 0.6}px {s * 0.85}px;">'
              f'<div style="display:flex; align-items:center; gap:{s * 0.5}px;"><span style="width:{s * 0.9}px; height:{s * 0.34}px; border-radius:{s * 0.17}px; background:{col};"></span>'
              f'<span class="caps" style="font-size:{s * 0.9}px; color:{P["text"]};">{lab}</span></div>'
              f'<div style="display:flex; gap:{s * 1.4}px; margin-top:{s * 0.45}px;">'
              f'<div><div class="num" style="font-size:{s * (1.5 if f.portrait else 1.9)}px; color:{RED if r["stall"] > 0 else P["text"]};">{stall}</div><div class="caps" style="font-size:{s * 0.9}px; color:{GREY};">STALLED</div></div>'
              f'<div><div class="num" style="font-size:{s * (1.5 if f.portrait else 1.9)}px;">{r["avg_kbps"] / 1000:.1f}</div><div class="caps" style="font-size:{s * 0.9}px; color:{GREY};">AVG MBIT/S</div></div>'
              f'<div><div class="num" style="font-size:{s * (1.5 if f.portrait else 1.9)}px;">{r["switches"]}</div><div class="caps" style="font-size:{s * 0.9}px; color:{GREY};">SWITCHES</div></div></div></div>')
    f.anim(f"""
inn("#p-highest", {f.t('best') - 0.2}); inn("#p-buffer", {f.t('buffer') - 0.2}); inn("#p-throughput", {f.t('speed') - 0.4});
""")


# ================================================================== B05 · close by
def b05(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.data = {"far": S["far"], "near": S["near"]}
    ps = s * 0.9
    f.pin("pyou", "YOU", color=P["text"], size=ps)
    f.pin("pfar", "FAR SERVER", color=GREY, size=ps)
    f.pin("pisp", "YOUR PROVIDER", color="#FF6B72", size=ps)
    f.mark_hud()
    f.tag("nf", "Open Connect · servers inside internet providers", x, y)
    f.note("ov", "Popular shows are copied in overnight.", x, y + s * 3.6, w, color=GREY)
    f.stat("far", x, y + s * 6.6, f'<span id="far-n">0.00</span><span style="font-size:0.42em; margin-left:0.14em;">s</span>', "ONE CHUNK FROM A FAR SERVER", color=GREY)
    f.stat("near", x, y + s * 6.6 + f.s_stat * 1.9, f'<span id="near-n">0.00</span><span style="font-size:0.42em; margin-left:0.14em;">s</span>', "FROM INSIDE YOUR PROVIDER", color=RED)
    f.anim(f"""
inn("#nf", {f.t('open') - 0.2}); inn("#ov", {f.t('overnight')}); inn("#far", {f.t('far') - 0.3}); inn("#near", {f.t('near') - 0.3});
""")


# ================================================================== B06 · scale
def b06(f):
    s, u = f.s_label, f.u
    x, y, w = f.hx, f.hy, f.hw
    f.mark_hud()
    big = f.s_stat * (0.7 if f.portrait else 0.82)
    f.stat("n1", x, y, '<span id="n1-n">0</span>', "OPEN CONNECT SERVERS · 2022", size=big)
    f.stat("n2", x, y + big * 1.75, '<span id="n2-n">0</span>', "COUNTRIES · 2022", size=big)
    f.stat("n3", x, y + big * 3.5, '<span id="n3-n">0</span><span style="font-size:0.55em;">M+</span>', "MEMBERSHIPS", size=big, color=RED)
    f.stat("n4", x, y + big * 5.25, '<span style="font-size:0.5em; color:#B3B3B3; margin-right:0.25em;">AV1</span>≈<span id="n4-n">0</span>%', "OF VIEWING" if f.portrait else "OF VIEWING · FEWER BITS, SAME PICTURE", size=big)
    if not f.portrait:
        f.label("src6", "AS OF DEC 2022 (SERVERS) · JAN 2026 (MEMBERS) · DEC 2025 (AV1)", x, y + big * 7.1, color=DIM, size=s * 0.9, wrapw=w)
    f.anim(f"""
inn("#n1", {f.t('servers') - 0.3}); count("#n1-n", 18000, {f.t('servers')}, 1.4, 0);
inn("#n2", {f.t('countries') - 0.3}); count("#n2-n", 175, {f.t('countries')}, 1.0, 0);
inn("#n3", {f.t('members') - 0.3}); count("#n3-n", 325, {f.t('members')}, 1.2, 0);
inn("#n4", {f.t('av1') - 0.3}); count("#n4-n", 30, {f.t('av1')}, 1.0, 0);
""" + ("" if f.portrait else f'inn("#src6", {f.t("av1") + 0.6});'))


BUILDERS = {"B01": b01, "B02": b02, "B03": b03, "B04": b04, "B05": b05, "B06": b06}

if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if a.startswith("B")] or None
    dst = HERE / "hyperframes" / "assets" / "kit3.js"
    if not dst.exists() or dst.read_bytes() != (KIT / "kit3.js").read_bytes():     # only when changed (mtime drives re-renders)
        shutil.copy(KIT / "kit3.js", dst)
    shutil.copytree(HERE / "evidence" / "rungs", HERE / "hyperframes" / "assets" / "rungs", dirs_exist_ok=True)
    hfkit.build(LOOK, BUILDERS, only)
    if "--render" in sys.argv:
        hfkit.render(LOOK, BUILDERS, only, aspects=[a for a in ("l", "v") if f"--{a}" in sys.argv] or ("l", "v"))
