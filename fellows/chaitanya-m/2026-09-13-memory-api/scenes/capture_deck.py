#!/usr/bin/env python3
"""
capture_deck.py — render the ACTUAL deck to per-beat 4K video.

Not a re-implementation. For each scene we emit a static HTML variant with that
<section> already carrying .on (and the deck's own JS removed so nothing resets
it), then drive Chrome headless with --virtual-time-budget to screenshot the
CSS entrance animations at exact 24 fps sample points. Virtual time is
deterministic, so the same t always yields the same frame.

After the animations settle the deck holds a static frame, so we capture that
once and hold it for the rest of the beat. The progress rail is NOT captured —
it advances across the whole scene, so it is composited afterwards by ffmpeg
with a time expression across the beat's true measured duration.

Container-query units (cqw) mean the deck lays out natively at any width: at a
3840x2160 viewport the stage is exactly 3840x2160 and all type is vector-crisp.
"""
import argparse, json, math, os, shutil, subprocess, tempfile, re
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FPS = 24

# Animation settle time per deck scene: longest (delay + duration) in that
# scene, plus a small tail. Read off the deck's own .dN delay classes.
SETTLE = {"B00": 1.30, "B01": 1.60, "B02": 2.80, "B03": 2.80,
          "B04": 3.30, "B05": 2.40, "B06": 2.40}


def scene_html(deck_src: str, idx: int, name: str, total: int) -> str:
    """A one-scene, self-contained copy of the deck with its JS stripped."""
    html = deck_src
    # drop the deck's controller so it cannot reset the active scene
    html = re.sub(r"<script>.*?</script>", "", html, flags=re.S)
    # activate the target scene in markup
    sections = list(re.finditer(r'<section class="scene"', html))
    if idx < len(sections):
        m = sections[idx]
        html = html[:m.start()] + '<section class="scene on"' + html[m.end():]
    # rail text
    html = re.sub(r'(<div class="cell" id="scene-name">)[^<]*(</div>)',
                  lambda m: m.group(1) + name + m.group(2), html)
    html = re.sub(r'(<div class="cell" id="counter">)[^<]*(</div>)',
                  lambda m: m.group(1) + f"{idx+1:02d} / {total:02d}" + m.group(2), html)
    # hide the keyboard hint and the progress rail (composited later)
    return prepare(html)


def prepare(html: str) -> str:
    """Hide chrome we composite ourselves, freeze animations, inject the seek."""
    return html.replace("</style>",
                        "#hint{display:none!important}"
                        "#progress{display:none!important}"
                        "html,body{background:#fff!important}"
                        # Freeze every animation from the very first frame.
                        # Without this the entrances can finish during page
                        # load and the seek arrives too late to matter.
                        "*{animation-play-state:paused!important}</style>") + SEEK_JS


# --virtual-time-budget alone is not a clock: page load consumes budget, so a
# nominal t lands somewhere later in the animation. Instead we PAUSE every
# animation and seek it with a negative delay, which renders one exact frame
# no matter how much virtual time elapsed. Deterministic and offset-free.
SEEK_JS = """
<script>
(function(){
  var t = parseFloat((location.hash||'#0').slice(1)) || 0, done = false;
  function seek(){
    if (done) return;            // never seek twice: the second pass would
    done = true;                 // re-read our own delays and subtract again
    document.querySelectorAll('*').forEach(function(el){
      var cs = getComputedStyle(el);
      if (!cs.animationName || cs.animationName === 'none') return;
      var delays = cs.animationDelay.split(',').map(function(d){
        return (parseFloat(d) - t) + 's';
      }).join(',');
      // The deck declares its .d1-.d7 delays with !important, so an inline
      // style would lose. setProperty with priority is the only way in.
      el.style.setProperty('animation-delay', delays, 'important');
      el.style.setProperty('animation-play-state', 'paused', 'important');
    });
    document.documentElement.setAttribute('data-seeked','1');
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(seek);
  setTimeout(seek, 400);
})();
</script>
"""


def shoot(url: str, out: Path, t_s: float, w: int, h: int, budget=2500):
    """Screenshot the page with every animation seeked to t_s and paused."""
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--disable-lcd-text",
                    f"--window-size={w},{h}",
                    f"--virtual-time-budget={budget}",
                    f"--screenshot={out}", f"{url}#{t_s:.4f}"],
                   capture_output=True)
    if not out.exists():
        raise SystemExit(f"[deck] Chrome produced no frame for t={t_s}s")


def render_beat(bid, idx, name, dur_s, deck_src, outdir, workroot, w, h, total_scenes,
                intro_html=None):
    work = workroot / bid
    (work / "frames").mkdir(parents=True)
    page = work / "page.html"
    page.write_text(prepare(intro_html) if intro_html is not None
                    else scene_html(deck_src, idx, name, total_scenes))
    url = page.resolve().as_uri()

    total_frames = max(1, round(dur_s * FPS))
    settle = SETTLE.get(bid, 2.6)
    n_anim = min(total_frames, int(math.ceil(settle * FPS)))

    # 1. the animated entrance, sampled at true 24 fps
    for i in range(n_anim):
        shoot(url, work / "frames" / f"a{i:05d}.png", i / FPS, w, h)

    # 2. the settled state, captured once and held
    settled = work / "settled.png"
    shoot(url, settled, settle + 2.0, w, h)

    seq = work / "seq"
    seq.mkdir()
    n = 0
    for i in range(n_anim):
        n += 1
        os.link(work / "frames" / f"a{i:05d}.png", seq / f"{n:06d}.png")
    while n < total_frames:
        n += 1
        os.link(settled, seq / f"{n:06d}.png")

    # 3. encode, compositing the deck's progress rail across the REAL duration
    bar_h = max(2, int(round(h * 0.009 * (16 / 9) / (w / h) if False else w * 0.009)))
    bar_h = max(2, int(round(w * 0.009)))             # .9cqw of stage width
    vf = (f"drawbox=x=0:y={h - bar_h}:w='min(iw,iw*t/{dur_s:.4f})':"
          f"h={bar_h}:color=black@1.0:t=fill")
    out = outdir / f"{bid}.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS),
                        "-i", str(seq / "%06d.png"), "-vf", vf,
                        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
                        "-pix_fmt", "yuv420p", "-color_primaries", "bt709",
                        "-color_trc", "bt709", "-colorspace", "bt709", str(out)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"[deck] ffmpeg failed on {bid}:\n{r.stderr[-1500:]}")
    shutil.rmtree(work)
    return out, total_frames, n_anim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=3840)
    ap.add_argument("--height", type=int, default=2160)
    ap.add_argument("--out", default=None)
    ap.add_argument("--only", nargs="*", default=None)
    a = ap.parse_args()

    here = Path(__file__).resolve().parent
    reel = here.parent
    deck = (reel.parent / "memory-api-deck.html").read_text()
    sheet = json.loads((reel / "beat_sheet.json").read_text())
    outdir = Path(a.out) if a.out else reel / "media"
    outdir.mkdir(parents=True, exist_ok=True)
    workroot = Path(tempfile.mkdtemp(prefix="deckcap-"))
    intro = (here / "intro.html").read_text() if (here / "intro.html").exists() else None

    names = re.findall(r'data-name="([^"]+)"', deck)
    total_scenes = len(names)
    print(f"[deck] {a.width}x{a.height} @{FPS}fps -> {outdir}  ({total_scenes} deck scenes)")

    for b in sheet["beats"]:
        bid = b["beat_id"]
        if a.only and bid not in a.only:
            continue
        dur = float(b.get("actual_duration_s") or b["estimated_duration_s"])
        if bid == "B00":
            out, nf, na = render_beat(bid, -1, "SIGN-IN", dur, deck, outdir, workroot,
                                      a.width, a.height, total_scenes, intro_html=intro)
        else:
            idx = int(bid[1:]) - 1
            out, nf, na = render_beat(bid, idx, names[idx], dur, deck, outdir, workroot,
                                      a.width, a.height, total_scenes)
        print(f"[deck] {bid}  {dur:>6.2f}s  {nf:>5d} frames ({na} animated) -> {out.name}")

    shutil.rmtree(workroot, ignore_errors=True)
    print("[deck] done")


if __name__ == "__main__":
    main()
