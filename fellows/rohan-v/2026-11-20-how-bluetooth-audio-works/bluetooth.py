"""Executable evidence for "How Bluetooth Audio Works".

1. Too much data: a synthetic pop track (drums, bass, piano chords, a lead; human timing; 60 s, 44.1 kHz stereo) is
   CD-quality audio. It is encoded with the real Bluetooth codecs that ship in ffmpeg (SBC at the High Quality
   setting, aptX, aptX HD) plus AAC (ffmpeg's own encoder, not Apple's) and decoded back: data rate measured from the
   encoded bytes. (A frequency-cutoff and a waveform match are still computed into results.json but not used: the cutoff
   did not tell the codecs apart, and a waveform match ranks perceptual codecs unfairly.)
2. The radio: a simulated A2DP link. Audio leaves the phone in packets (5 SBC frames = 14.5 ms each) on a channel
   that hops among Bluetooth's 79; a Wi-Fi network sits on 23 of them, busy in bursts. With and without adaptive
   hopping (skipping the Wi-Fi channels), first-try losses are counted.
3. The buffer: lost packets are sent again; the headphones play each packet a fixed time after it was made. Body
   blocking (a phone in a pocket as you turn) wipes out bursts of packets. For each buffer size: glitches heard.
   The track is then played through the simulated link with a small and a large buffer (listening clips).
Nothing here is any company's code; the codecs are ffmpeg's implementations.

    python bluetooth.py         -> evidence/*.wav, results.json, scene.json, run.log
"""
import json
import subprocess
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
SR = 44100
DUR = 60.0
music = np.random.default_rng(1119)      # the song
perf = np.random.default_rng(77)         # the playing (timing, velocity)
radio = np.random.default_rng(2402)      # the radio world
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


# ================================================================ 1. the track
def m2f(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def piano(f, dur, vel):
    n = int(dur * SR)
    t = np.arange(n) / SR
    y = np.zeros(n)
    for k in range(1, 14):
        if k * f > 16000:
            break
        y += (vel / k ** 1.1) * np.exp(-t * (1.2 + 0.6 * k)) * np.sin(2 * np.pi * k * f * t * (1 + 0.0004 * k * k))
    return y * np.clip(t / 0.004, 0, 1)


def build_track():
    n = int(DUR * SR)
    L, R = np.zeros(n), np.zeros(n)
    bpm = 104
    beat = 60 / bpm
    prog = [(48, [60, 64, 67]), (45, [57, 60, 64]), (41, [57, 60, 65]), (43, [59, 62, 67])]    # C Am F G
    prog_b = [(41, [57, 60, 65]), (43, [59, 62, 67]), (48, [60, 64, 67]), (45, [57, 60, 64])]  # chorus: F G C Am
    hp = butter(4, 7000, "hp", fs=SR, output="sos")
    noise_hat = sosfilt(hp, perf.normal(0, 1, int(0.12 * SR)))
    bar = 0
    t0 = 0.0
    scale = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76]
    while t0 < DUR - 4 * beat:
        section = (bar // 8) % 2               # 8 bars verse, 8 bars chorus
        root, chord = (prog_b if section else prog)[bar % 4]
        for b4 in range(4):                    # each beat
            tb = t0 + b4 * beat + perf.normal(0, 0.006)
            i0 = int(tb * SR)
            # kick on 1 and 3, snare on 2 and 4
            if b4 in (0, 2):
                tt = np.arange(int(0.25 * SR)) / SR
                kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * perf.uniform(0.75, 0.9)
                L[i0:i0 + len(kick)] += kick[: n - i0]; R[i0:i0 + len(kick)] += kick[: n - i0]
            else:
                tt = np.arange(int(0.2 * SR)) / SR
                sn = (perf.normal(0, 1, len(tt)) * 0.5 + np.sin(2 * np.pi * 190 * tt)) * np.exp(-tt * 18) * perf.uniform(0.35, 0.45)
                L[i0:i0 + len(sn)] += sn[: n - i0] * 0.9; R[i0:i0 + len(sn)] += sn[: n - i0]
            # hats on eighths (more in the chorus)
            for e in range(2 if not section else 4):
                th = tb + e * beat / (2 if not section else 4) + perf.normal(0, 0.004)
                j = int(th * SR)
                env = np.exp(-np.arange(len(noise_hat)) / SR * (60 if e % 2 else 35))
                hat = noise_hat * env * perf.uniform(0.10, 0.18)
                L[j:j + len(hat)] += hat[: n - j] * 0.6; R[j:j + len(hat)] += hat[: n - j]
            # bass: root on every beat, octave jump on beat 4
            bf = m2f(root - 12 + (12 if b4 == 3 else 0))
            tt = np.arange(int(beat * 0.9 * SR)) / SR
            bass = sum(np.sin(2 * np.pi * k * bf * tt) / k for k in range(1, 8)) * np.exp(-tt * 3) * 0.28
            L[i0:i0 + len(bass)] += bass[: n - i0]; R[i0:i0 + len(bass)] += bass[: n - i0]
        # piano chord at the bar start (and on beat 3 in the chorus)
        for hit in ((0,) if not section else (0, 2)):
            j = int((t0 + hit * beat + perf.normal(0, 0.008)) * SR)
            for m in chord:
                y = piano(m2f(m), 2.2, perf.uniform(0.10, 0.14))
                L[j:j + len(y)] += y[: n - j] * 1.1; R[j:j + len(y)] += y[: n - j] * 0.8
        # a lead line in the chorus (the tune: notes from the scale, chosen by `music`)
        if section:
            for e in range(8):
                if music.random() < 0.25:
                    continue
                m = scale[music.integers(0, len(scale))] + 12
                j = int((t0 + e * beat / 2 + perf.normal(0, 0.01)) * SR)
                y = piano(m2f(m), beat * 0.6, perf.uniform(0.07, 0.10))
                L[j:j + len(y)] += y[: n - j] * 0.7; R[j:j + len(y)] += y[: n - j] * 1.0
        t0 += 4 * beat
        bar += 1
    x = np.stack([L, R], 1)
    fade = np.clip((DUR - np.arange(n) / SR) / 1.5, 0, 1)
    x *= fade[:, None]
    return x / np.abs(x).max() * 0.89


def ff(*a):
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", *a], check=True)


def ltas(x):
    W, hop = 4096, 2048
    m = x.mean(1)
    acc = np.zeros(W // 2 + 1)
    for s in range(0, len(m) - W, hop):
        acc += np.abs(np.fft.rfft(m[s:s + W] * np.hanning(W))) ** 2
    return np.fft.rfftfreq(W, 1 / SR), 10 * np.log10(acc + 1e-20)


def codecs(x):
    src = EV / "track.wav"
    CODECS = [("SBC", "sbc", ["-c:a", "sbc", "-b:a", "328k"], "sbc"),
              ("aptX", "aptx", ["-c:a", "aptx"], "aptx"),
              ("aptX HD", "aptx_hd", ["-c:a", "aptx_hd"], "aptx_hd"),
              ("AAC", "m4a", ["-c:a", "aac", "-b:a", "256k"], None)]
    f, ref = ltas(x)
    out = []
    for nm, ext, args, fmt in CODECS:
        enc = EV / f"_enc.{ext}"
        ff("-i", str(src), *args, *(["-f", fmt] if fmt else []), str(enc))
        if ext == "m4a":     # data rate from the audio stream itself, not the container
            r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=bit_rate",
                                "-of", "csv=p=0", str(enc)], capture_output=True, text=True)
            kbps = float(r.stdout.strip()) / 1000
        else:
            kbps = enc.stat().st_size * 8 / DUR / 1000
        dec = EV / f"_dec_{ext}.wav"
        ff(*(["-f", fmt] if fmt else []), "-i", str(enc), "-ac", "2", "-ar", str(SR), "-c:a", "pcm_s16le", str(dec))
        _, y = wavfile.read(dec)
        y = y.astype(float) / 32768
        # align (codec delay) by cross-correlation on a 2 s stretch
        a, b = x[SR * 10: SR * 12, 0], y[SR * 10 - 4000: SR * 12 + 4000, 0]
        c = np.correlate(b, a, "valid")
        lag = int(np.argmax(c)) - 4000
        y = np.roll(y, -lag, 0)[: len(x)]
        if len(y) < len(x):
            y = np.vstack([y, np.zeros((len(x) - len(y), 2))])
        fd, d = ltas(y)
        # highest frequency kept: 1/3-octave bands from 2 kHz where the ORIGINAL has sound (within 70 dB of its loudest
        # band); the first band where the decoded copy is more than 10 dB below the original
        bands = 2000 * 2 ** (np.arange(0, 14) / 3)
        cut = None
        lv0 = []
        for fc in bands:
            sel = (f >= fc / 2 ** (1 / 6)) & (f < fc * 2 ** (1 / 6))
            if not sel.any() or fc > SR / 2 * 0.95:
                continue
            e0 = 10 * np.log10(np.mean(10 ** (ref[sel] / 10)))
            e1 = 10 * np.log10(np.mean(10 ** (d[sel] / 10)))
            lv0.append((fc, e0, e1))
        top = max(e for _, e, _ in lv0)
        audible = [(fc, e0, e1) for fc, e0, e1 in lv0 if e0 > top - 70]
        for fc, e0, e1 in audible:
            if e1 < e0 - 10:
                cut = fc / 2 ** (1 / 6)
                break
        keep_to = cut if cut else audible[-1][0] * 2 ** (1 / 6)
        g = np.sum(x * y) / np.sum(y * y)
        snr = 10 * np.log10(np.sum(x ** 2) / np.sum((x - g * y) ** 2))
        out.append({"codec": nm, "kbps": round(kbps, 1), "ratio": round(1411.2 / kbps, 2), "keeps_to_hz": round(keep_to),
                    "cut": cut is not None, "lag_samples": lag, "waveform_snr_db": round(float(snr), 1)})
        enc.unlink(); dec.unlink()
    return out, audible[-1][0] * 2 ** (1 / 6)


# ================================================================ 2-3. the radio link and the buffer
SLOT = 625e-6
PKT_SAMPLES = 640                    # 5 SBC frames of 128 samples
PKT_T = PKT_SAMPLES / SR             # 14.5 ms of music per packet
ATTEMPT = 6 * SLOT                   # a 5-slot packet + the 1-slot reply
WIFI = list(range(24, 47))           # Wi-Fi channel 6 (2426-2448 MHz) covers Bluetooth channels 24..46


def world(T):
    """Wi-Fi busy/idle bursts and body-blocking fades, the same for every run (seeded)."""
    t, busy = 0.0, []
    on = False
    while t < T:
        d = radio.exponential(0.012 if on else 0.010)
        busy.append((t, t + d, on))
        t += d
        on = not on
    fades, t = [], 2.0
    while t < T - 1:
        t += radio.exponential(6.0) + 1.0
        if t < T - 1:
            fades.append((t, t + radio.uniform(0.06, 0.32)))
    return busy, fades


def wifi_busy(busy, t):
    lo, hi = 0, len(busy) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if busy[mid][1] <= t:
            lo = mid + 1
        else:
            hi = mid
    return busy[lo][2]


def link(T, busy, fades, afh, B, seed=5):
    """Send packets in order; each attempt hops to a channel; returns per-packet arrival times (None = flushed)."""
    rng = np.random.default_rng(seed)
    hopset = [c for c in range(79) if not (afh and c in WIFI)]
    npk = int(T / PKT_T)
    made = np.arange(npk) * PKT_T + PKT_T           # a packet can leave once its 14.5 ms of music exist
    arrive = [None] * npk
    now = 0.0
    attempts = []
    for i in range(npk):
        now = max(now, made[i])
        while True:
            if now > made[i] - PKT_T + B:           # too late to be played: the phone flushes it
                break
            ch = hopset[rng.integers(0, len(hopset))]
            lost = False
            if ch in WIFI and wifi_busy(busy, now):
                lost = True
            for a, b in fades:
                if a <= now < b and rng.random() < 0.92:
                    lost = True
            if any(a <= now < b for a, b in fades):
                pass
            elif rng.random() < 0.01:               # the odd random error
                lost = True
            attempts.append((now, ch, lost))
            now += ATTEMPT
            if not lost:
                arrive[i] = now
                break
    return made, arrive, attempts


def glitches(made, arrive, B):
    """The headphones play packet i from (made_i - PKT_T) + B. Late or missing = a gap."""
    gaps = []
    for i, (m, a) in enumerate(zip(made, arrive)):
        play = m - PKT_T + B
        if a is None or a > play:
            gaps.append(i)
    # merge consecutive gaps into events
    ev = []
    for i in gaps:
        if ev and ev[-1][1] == i - 1:
            ev[-1][1] = i
        else:
            ev.append([i, i])
    return gaps, ev


def first_try_loss(attempts):
    return float(np.mean([l for _, _, l in attempts]))


def render_through(x, made, gaps, B, t0, t1):
    """The music as the headphones play it: missing packets are silent (2 ms fades)."""
    y = x.copy()
    f = int(0.002 * SR)
    for i in gaps:
        s = int((made[i] - PKT_T) * SR)
        if s - f < 0 or s + PKT_SAMPLES + f >= len(y):
            continue
        e = s + PKT_SAMPLES
        y[s:e] = 0
        if s - f > 0:
            y[s - f:s] *= np.linspace(1, 0, f)[:, None]
        if e + f < len(y):
            y[e:e + f] *= np.linspace(0, 1, f)[:, None]
    return y[int(t0 * SR): int(t1 * SR)]


def main():
    x = build_track()
    wavfile.write(EV / "track.wav", SR, (x * 32767).astype(np.int16))
    log("BLUETOOTH AUDIO EVIDENCE (bluetooth.py): real codecs from ffmpeg + a simulated A2DP link")
    log(f"THE TRACK: synthetic pop (drums, bass, piano, lead), {DUR:.0f} s, 44.1 kHz, 16-bit stereo")
    cd = SR * 16 * 2 / 1000
    log(f"1. TOO MUCH DATA: CD quality = 44,100 x 16 bits x 2 channels = {cd:,.1f} kbit/s")
    table, orig_top = codecs(x)
    for r in table:
        log(f"  {r['codec']:8s}: {r['kbps']:6.1f} kbit/s measured from the encoded bytes = 1/{r['ratio']:.1f} of CD"
            + (" (ffmpeg's AAC encoder set to 256k; not Apple's encoder)" if r["codec"] == "AAC" else ""))
    log("  (no quality score: a waveform match ranks a perceptual codec unfairly, and no listening test was run)")

    T = 120.0
    busy, fades = world(T)
    duty = sum(b - a for a, b, on in busy if on) / T
    log()
    log(f"2. THE RADIO (simulated {T:.0f} s): 79 channels; Wi-Fi on channels 24-46 ({len(WIFI)} of 79), busy {duty * 100:.0f}% of the time;")
    log(f"  {len(fades)} body-blocking moments of 60-320 ms (a phone in a pocket as you turn); {PKT_T * 1000:.1f} ms of music per packet,")
    log(f"  one try every {ATTEMPT * 1000:.2f} ms (hops to a new channel each try) = {1 / ATTEMPT:.0f} tries/s for {1 / PKT_T:.0f} packets/s")
    res = {"cd_kbps": cd, "codecs": table, "orig_top_hz": orig_top, "wifi_duty": duty, "fades": fades,
           "pkt_ms": PKT_T * 1000, "attempt_ms": ATTEMPT * 1000, "runs": {}}
    for afh in (False, True):
        made, arrive, att = link(T, busy, fades, afh, 0.2)
        quiet = [l for (t, c, l) in att if not any(a <= t < b for a, b in fades)]
        wf = [l for (t, c, l) in att if c in WIFI]
        log(f"  {'with' if afh else 'without'} adaptive hopping: {first_try_loss(att) * 100:.1f}% of tries lost "
            f"({np.mean(quiet) * 100:.1f}% outside the body-blocking moments)")
        res["runs"][f"afh_{afh}"] = {"loss": first_try_loss(att), "loss_quiet": float(np.mean(quiet))}
    log()
    log("3. THE BUFFER (adaptive hopping on): the headphones play each packet a fixed time after it was made")
    res["buffers"] = []
    for B in (0.02, 0.05, 0.1, 0.15, 0.2, 0.3):
        made, arrive, att = link(T, busy, fades, True, B)
        gaps, ev = glitches(made, arrive, B)
        res["buffers"].append({"ms": B * 1000, "gaps": len(ev), "missing_ms": len(gaps) * PKT_T * 1000})
        log(f"  buffer {B * 1000:4.0f} ms: {len(ev):3d} glitches in {T:.0f} s ({len(gaps) * PKT_T * 1000:6.0f} ms of music missing)")

    # listening + drawing window: 6 s whose small-buffer glitch count is closest to that buffer's average rate
    Bs, Bl = 0.05, 0.2
    made_s, arr_s, att_s = link(T, busy, fades, True, Bs)
    gaps_s, ev_s = glitches(made_s, arr_s, Bs)
    made_l, arr_l, att_l = link(T, busy, fades, True, Bl)
    gaps_l, ev_l = glitches(made_l, arr_l, Bl)
    rate = len(ev_s) / T
    best = None
    for w0 in np.arange(2.0, DUR - 7.0, 0.5):
        k = sum(1 for a, b in ev_s if w0 + 0.3 < made_s[a] < w0 + 5.7)
        if k == 0:
            continue
        score = abs(k / 6.0 - rate)
        if best is None or score < best[0]:
            best = (score, w0, k)
    _, w0, k = best
    w1 = w0 + 6.0
    log()
    log(f"LISTENING (window {w0:.1f}-{w1:.1f} s, picked as the 6 s whose glitch rate is closest to the {Bs * 1000:.0f} ms average: "
        f"{k} glitches vs {rate * 6:.1f} expected)")
    small = render_through(x, made_s, gaps_s, Bs, w0, w1)
    large = render_through(x, made_l, gaps_l, Bl, w0, w1)
    kl = sum(1 for a, b in ev_l if w0 < made_l[a] < w1)
    wavfile.write(EV / "small_buffer.wav", SR, (small * 32767).astype(np.int16))
    wavfile.write(EV / "large_buffer.wav", SR, (large * 32767).astype(np.int16))
    log(f"  small_buffer.wav: {Bs * 1000:.0f} ms buffer, {k} glitches;  large_buffer.wav: {Bl * 1000:.0f} ms buffer, {kl} glitches "
        f"(the same moments, {Bl * 1000:.0f} ms later)")
    res["listen"] = {"w0": float(w0), "w1": float(w1), "small_ms": Bs * 1000, "large_ms": Bl * 1000, "small_glitches": k,
                     "large_glitches": kl}

    # scene data: hops (first 160 tries of the window, both modes), buffer level in the window for both buffers
    def hops(afh):
        _, _, att = link(T, busy, fades, afh, 0.2)
        sel = [a for a in att if w0 <= a[0] < w0 + 0.6][:160]
        return [[round(t - w0, 4), c, int(l)] for t, c, l in sel]

    def level(made, arrive, B):
        """Music waiting in the headphones (ms) every 10 ms."""
        ts = np.arange(w0, w1, 0.01)
        arr = np.array([a if a is not None else np.inf for a in arrive])
        lv = []
        for t in ts:
            have = np.sum((arr <= t) & (made - PKT_T + B > t))      # arrived and not yet played
            lv.append(round(float(min(have * PKT_T * 1000, B * 1000 + PKT_T * 1000)), 1))
        return lv

    scene = {"w0": float(w0), "w1": float(w1), "wifi": [WIFI[0], WIFI[-1]], "hops_off": hops(False), "hops_on": hops(True),
             "level_small": level(made_s, arr_s, Bs), "level_large": level(made_l, arr_l, Bl),
             "gaps_small": [round(made_s[a] - PKT_T - w0, 3) for a, b in ev_s if w0 < made_s[a] < w1],
             "fades": [[round(a - w0, 3), round(b - w0, 3)] for a, b in fades if b > w0 and a < w1],
             "results": res}
    (EV / "scene.json").write_text(json.dumps(scene), encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    (EV / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
