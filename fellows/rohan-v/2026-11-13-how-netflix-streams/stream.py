"""EXECUTABLE EVIDENCE for "How Netflix Streams."

Real encodes and a simulated player. Nothing here is Netflix's code or Netflix's video.

  1. THE LADDER   two 10-second test clips made here with ffmpeg (a simple flat animation and a busy, grainy
                  zoom), each encoded with libx264 at six rungs from 235 kbit/s to 5.8 Mbit/s, and scored against
                  the original with VMAF (Netflix's open-source quality metric, 0-100) via ffmpeg's libvmaf.
  2. PER-TITLE    the bitrate each clip needs to reach VMAF 93: why one fixed ladder wastes bits or loses quality.
  3. THE PLAYER   a 10-minute stream cut into 4-second segments over a simulated home connection that sags and
                  drops; three players: always-highest, throughput-based and buffer-based (after Huang et al. 2014,
                  run on Netflix). Measured: stall time, average bitrate, quality switches.
  4. DISTANCE     segment download time from a far server vs a server inside your internet provider, from round
                  trips and TCP's slow start (a textbook model).

    python stream.py      # writes evidence/run.log, results.json, scene.json (+ evidence/ladder/*.mp4 frames)
"""
import json
import math
import subprocess
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
WORK = Path("D:/Rohan/Claude/HyperFrames/tmp/stream")          # big intermediate files stay out of the reel
EV.mkdir(exist_ok=True)
WORK.mkdir(parents=True, exist_ok=True)
LOG, SCENE = [], {}


def P(s=""):
    print(s, flush=True)
    LOG.append(s)


def ff(*args):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *args], check=True)


# ================================================================= 1. test clips + ladder
CLIPS = {
    # flat colours and clean edges: what cartoons and slide-like scenes look like to an encoder
    "simple": "testsrc2=size=1920x1080:rate=30:duration=10",
    # fine detail, grain and constant motion: the hard case
    "busy": "mandelbrot=size=1920x1080:rate=30:start_scale=3:end_scale=0.02:maxiter=600,noise=alls=22:allf=t+u,"
            "trim=duration=10",
}
LADDER = [(235, 320, 180), (750, 640, 360), (1750, 960, 540), (3000, 1280, 720), (4300, 1920, 1080), (5800, 1920, 1080)]


def vmaf(dist, ref):
    out = WORK / "vmaf.json"
    if out.exists():
        out.unlink()
    flt = (f"[0:v]scale=1920:1080:flags=bicubic,setpts=PTS-STARTPTS,format=yuv420p[d];"
           f"[1:v]setpts=PTS-STARTPTS,format=yuv420p[r];[d][r]libvmaf=log_fmt=json:log_path=vmaf.json:n_threads=8")   # relative: a drive colon breaks filter syntax
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(dist), "-i", str(ref), "-lavfi", flt, "-f", "null", "-"], check=True, cwd=WORK)
    j = json.loads(out.read_text())
    return round(float(j["pooled_metrics"]["vmaf"]["mean"]), 2)


ladder = {}
P("1. THE LADDER (libx264, 2-pass-free CBR-ish via maxrate; VMAF vs the 1080p original, scaled back up)")
for name, src in CLIPS.items():
    ref = WORK / f"{name}_ref.mp4"
    if not ref.exists():
        ff("-f", "lavfi", "-i", src, "-c:v", "libx264", "-preset", "slow", "-crf", "4", "-pix_fmt", "yuv420p", str(ref))
    rows = []
    for kbps, w, h in LADDER:
        out = WORK / f"{name}_{kbps}.mp4"
        if not out.exists():
            ff("-i", str(ref), "-vf", f"scale={w}:{h}", "-c:v", "libx264", "-preset", "medium", "-b:v", f"{kbps}k",
               "-maxrate", f"{int(kbps * 1.1)}k", "-bufsize", f"{kbps * 2}k", "-pix_fmt", "yuv420p", str(out))
        real = out.stat().st_size * 8 / 10 / 1000
        score = vmaf(out, ref)
        rows.append(dict(kbps=kbps, w=w, h=h, real_kbps=round(real), vmaf=score))
        P(f"  {name:6s} {kbps:5d} kbit/s {w}x{h}: VMAF {score:5.1f} (file {real:.0f} kbit/s)")
    ladder[name] = rows
    # a still from each rung's middle for the scenes (cropped detail)
    for kbps, w, h in (LADDER[0], LADDER[3], LADDER[5]):
        ff("-ss", "5", "-i", str(WORK / f"{name}_{kbps}.mp4"), "-frames:v", "1", "-vf",
           "scale=1920:1080:flags=neighbor,crop=640:360:640:360", str(EV / f"{name}_{kbps}.png"))

# ================================================================= 2. per-title
TARGET = 93.0


def need(rows):
    """Lowest bitrate on the ladder (interpolated in log-bitrate) that reaches the target VMAF."""
    for a, b in zip(rows, rows[1:]):
        if a["vmaf"] < TARGET <= b["vmaf"]:
            f = (TARGET - a["vmaf"]) / (b["vmaf"] - a["vmaf"])
            return round(math.exp(math.log(a["kbps"]) + f * (math.log(b["kbps"]) - math.log(a["kbps"]))))
    return rows[0]["kbps"] if rows[0]["vmaf"] >= TARGET else None


need_simple, need_busy = need(ladder["simple"]), need(ladder["busy"])
P("")
P(f"2. PER-TITLE: bitrate to reach VMAF {TARGET:.0f}: simple {need_simple} kbit/s, busy {need_busy if need_busy else 'not reached by 5800'} kbit/s")

# ================================================================= 3. the player
rng = np.random.default_rng(1113)
SEG, N = 4.0, 150                                       # 4-second segments, 10 minutes
RUNGS = [r[0] for r in LADDER]
t = np.arange(0, 700, 1.0)
bw = 7.0 + 1.5 * np.sin(t / 37) + rng.normal(0, 0.6, len(t))          # Mbit/s, a decent home connection
bw[(t > 150) & (t < 210)] *= 0.28                                       # someone starts a big download
bw[(t > 380) & (t < 400)] = 0.9                                         # a bad patch of Wi-Fi
bw = np.clip(bw, 0.4, None)


def throughput_at(clock):
    return float(np.interp(clock, t, bw))


def play(policy):
    """Simulate segment downloads; return stalls, bitrates and switches."""
    clock, buf, played, stall, hist, est = 0.0, 0.0, 0.0, 0.0, [], 3.0
    for i in range(N):
        if policy == "highest":
            q = len(RUNGS) - 1
        elif policy == "throughput":
            q = max([k for k, r in enumerate(RUNGS) if r / 1000 <= 0.8 * est] or [0])
        else:                                         # buffer-based: map buffer level to a rung (reservoir 8 s, cushion 30 s)
            frac = np.clip((buf - 8) / 30, 0, 1)
            q = int(round(frac * (len(RUNGS) - 1)))
        size_mbit = RUNGS[q] / 1000 * SEG
        # download, integrating the changing bandwidth second by second
        left, dt = size_mbit, 0.0
        while left > 0:
            rate = throughput_at(clock + dt)
            step = min(0.25, left / rate)
            left -= rate * step
            dt += step
        est = 0.7 * est + 0.3 * (size_mbit / dt)
        if dt > buf and i > 0:
            stall += dt - buf
            buf = 0.0
        else:
            buf = max(0.0, buf - dt) if i > 0 else 0.0
        buf += SEG
        clock += dt
        if buf > 40:                                   # player caps its buffer; waits while it drains
            clock += buf - 40
            buf = 40.0
        hist.append(dict(i=i, q=q, t=round(clock, 2), buf=round(buf, 2)))
    qs = [h["q"] for h in hist]
    return dict(stall=round(stall, 1), avg_kbps=round(float(np.mean([RUNGS[q] for q in qs]))),
                switches=int(sum(a != b for a, b in zip(qs, qs[1:]))), hist=hist)


P("")
P(f"3. THE PLAYER ({N} segments of {SEG:.0f} s over a home connection that sags, then drops)")
runs = {}
for pol, lab in (("highest", "always highest quality"), ("throughput", "throughput-based"), ("buffer", "buffer-based")):
    r = play(pol)
    runs[pol] = r
    P(f"  {lab:22s}: stalled {r['stall']:5.1f} s, average {r['avg_kbps']:5d} kbit/s, {r['switches']:3d} quality switches")

# ================================================================= 4. distance
def seg_time(size_mbit, rtt_ms, link_mbps):
    """TCP slow start from a 10-packet window (1,460-byte packets), doubling each round trip, capped by the link."""
    size_bytes, cwnd, sent, rounds = size_mbit * 1e6 / 8, 10 * 1460, 0.0, 0
    while sent < size_bytes:
        per_round = min(cwnd, link_mbps * 1e6 / 8 * rtt_ms / 1000)
        sent += per_round
        cwnd *= 2
        rounds += 1
    return rounds * rtt_ms / 1000 + rtt_ms / 1000            # plus the request itself


seg_mb = 5.8 * SEG
far, near = seg_time(seg_mb, 150, 50), seg_time(seg_mb, 8, 50)
P("")
P(f"4. DISTANCE (one 4-second 5.8 Mbit/s segment, a 50 Mbit/s line, a fresh connection)")
P(f"  far server (150 ms round trip): {far:.2f} s;  server inside your provider (8 ms): {near:.2f} s")

# ================================================================= write
res = dict(ladder=ladder, target=TARGET, need_simple=need_simple, need_busy=need_busy,
           player={k: {kk: vv for kk, vv in v.items() if kk != "hist"} for k, v in runs.items()},
           far_s=round(far, 2), near_s=round(near, 2), seg=SEG, n=N)
SCENE.update(ladder=ladder, rungs=RUNGS, target=TARGET, need=dict(simple=need_simple, busy=need_busy),
             bw=[round(float(x), 2) for x in bw[::2]], runs={k: v["hist"] for k, v in runs.items()},
             player=res["player"], far=res["far_s"], near=res["near_s"])
(EV / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
(EV / "scene.json").write_text(json.dumps(SCENE), encoding="utf-8")
(EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
P("")
P("wrote evidence/run.log, results.json, scene.json")
