"""Executable evidence for "How Pitch Correction Works".

Everything the reel shows about pitch detection and correction comes from running this file:

  1. SING   — synthesise a short melody (Twinkle Twinkle: C4 C4 G4 G4 A4 A4 G4) the way a real
              voice drifts: every note slightly off, a scoop into each onset, vibrato on held notes.
              The last note is deliberately 75 cents flat, so it sits closer to F#4 than to G4.
  2. DETECT — find the pitch frame by frame with the YIN method (de Cheveigné & Kawahara 2002):
              compare the wave with delayed copies of itself; the delay where it lines up best is
              one period, and 1 / period is the frequency.
  3. SNAP   — turn each measured pitch into cents, and round to the nearest allowed note, either
              any semitone (chromatic) or only the notes of C major.
  4. PULL   — move the pitch towards that target with a "retune speed" (a one-pole glide with
              time constant tau; tau = 0 is an instant jump).
  5. SHIFT  — actually change the pitch of the audio with TD-PSOLA (pitch-synchronous
              overlap-add): cut the wave into one-cycle grains and re-space them.
  6. CHECK  — run the same detector on the corrected audio and measure how far it is from the
              target. Nothing on screen is assumed; every "after" number is re-measured.

Outputs (in evidence/): pitch_demo.json (all data for the scenes), run.log, and WAV files of the
sung melody and each corrected version. Run:  python pitch_demo.py
"""
import json
import hashlib
import platform
import time
import wave
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "evidence"
OUT.mkdir(exist_ok=True)

SR = 22050
A4 = 440.0
RNG = np.random.default_rng(7)
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
C_MAJOR = {0, 2, 4, 5, 7, 9, 11}

LOG = []


def log(msg):
    print(msg)
    LOG.append(msg)


def midi_to_hz(m):
    return A4 * 2.0 ** ((m - 69) / 12.0)


def hz_to_midi(f):
    return 69 + 12 * np.log2(f / A4)


def name(m):
    m = int(round(m))
    return f"{NOTE_NAMES[m % 12]}{m // 12 - 1}"


# ---------------------------------------------------------------- 1. SING
MELODY = [  # (midi note, seconds, detune in cents)
    (60, 0.55, -28), (60, 0.55, +18), (67, 0.55, -35), (67, 0.55, +22),
    (69, 0.55, -40), (69, 0.55, +15), (67, 1.10, -75),
]
GAP = 0.06          # short breath between notes
SCOOP_CENTS = -90   # singers often slide up into a note
SCOOP_S = 0.07
VIB_HZ, VIB_CENTS, VIB_DELAY = 5.5, 22, 0.18


def sing():
    f0_track, audio = [], []
    t_note = 0.0
    notes = []
    for midi, dur, det in MELODY:
        n = int(dur * SR)
        t = np.arange(n) / SR
        cents = np.full(n, float(det))
        scoop = t < SCOOP_S
        cents[scoop] += SCOOP_CENTS * (1 - t[scoop] / SCOOP_S) ** 2
        vib_on = np.clip((t - VIB_DELAY) / 0.15, 0, 1)
        cents += vib_on * VIB_CENTS * np.sin(2 * np.pi * VIB_HZ * t)
        f0 = midi_to_hz(midi) * 2 ** (cents / 1200)
        phase = 2 * np.pi * np.cumsum(f0) / SR
        x = np.zeros(n)
        for k in range(1, 11):  # harmonics with a soft vocal-ish tilt
            x += (1.0 / k) * (1.0 if k < 4 else 0.6) * np.sin(k * phase + 0.3 * k)
        env = np.minimum(1, t / 0.03) * np.minimum(1, (dur - t) / 0.06)
        x *= env
        notes.append({"midi": midi, "name": name(midi), "start": round(t_note, 4), "end": round(t_note + dur, 4),
                      "detune_cents": det})
        audio.append(x)
        f0_track.append(f0)
        g = int(GAP * SR)
        audio.append(np.zeros(g))
        f0_track.append(np.zeros(g))
        t_note += dur + GAP
    x = np.concatenate(audio)
    x += 0.003 * RNG.standard_normal(len(x))
    x /= np.max(np.abs(x)) * 1.12
    return x, np.concatenate(f0_track), notes


# ---------------------------------------------------------------- 2. DETECT (YIN)
FRAME, HOP = 1024, 128
FMIN, FMAX = 90.0, 900.0


def yin_frame(frame, tau_min, tau_max):
    w = len(frame) - tau_max
    d = np.array([np.sum((frame[:w] - frame[tau:tau + w]) ** 2) for tau in range(tau_max + 1)])
    cmnd = np.ones_like(d)
    cum = np.cumsum(d[1:])
    cmnd[1:] = d[1:] * np.arange(1, len(d)) / np.maximum(cum, 1e-12)
    return d, cmnd


def detect(x, threshold=0.12):
    tau_min, tau_max = int(SR / FMAX), int(SR / FMIN)
    times, f0s = [], []
    for start in range(0, len(x) - FRAME, HOP):
        fr = x[start:start + FRAME]
        times.append((start + FRAME / 2) / SR)
        if np.sqrt(np.mean(fr ** 2)) < 0.02:
            f0s.append(0.0)
            continue
        _, cmnd = yin_frame(fr, tau_min, tau_max)
        cand = np.where(cmnd[tau_min:] < threshold)[0]
        if len(cand) == 0:
            f0s.append(0.0)
            continue
        tau = cand[0] + tau_min
        while tau + 1 < len(cmnd) and cmnd[tau + 1] < cmnd[tau]:
            tau += 1
        if 1 <= tau < len(cmnd) - 1:  # parabolic interpolation for sub-sample accuracy
            a, b, c = cmnd[tau - 1], cmnd[tau], cmnd[tau + 1]
            tau = tau + 0.5 * (a - c) / max(a - 2 * b + c, 1e-12)
        f0s.append(SR / tau)
    return np.array(times), np.array(f0s)


# ---------------------------------------------------------------- 3. SNAP and 4. PULL
def snap(midi_float, scale=None):
    base = np.round(midi_float)
    if scale is None:
        return base
    best = None
    for m in range(int(np.floor(midi_float)) - 2, int(np.ceil(midi_float)) + 3):
        if m % 12 in scale and (best is None or abs(m - midi_float) < abs(best - midi_float)):
            best = m
    return float(best)


def correction_curve(times, f0s, tau_ms, scale=None):
    """Returns the corrected pitch per frame (Hz, 0 = unvoiced) and the target note per frame."""
    dt = times[1] - times[0]
    out, target = np.zeros_like(f0s), np.zeros_like(f0s)
    shift = 0.0  # applied correction in semitones, glides towards the needed correction
    alpha = 1.0 if tau_ms == 0 else 1 - np.exp(-dt / (tau_ms / 1000))
    for i, f in enumerate(f0s):
        if f <= 0:
            shift = 0.0
            continue
        m = hz_to_midi(f)
        tgt = snap(m, scale)
        target[i] = tgt
        need = tgt - m
        shift += alpha * (need - shift)
        out[i] = f * 2 ** (shift / 12)
    return out, target


# ---------------------------------------------------------------- 5. SHIFT (TD-PSOLA)
def psola(x, times, f0_in, f0_out):
    n = len(x)
    ts = np.arange(n) / SR
    fin = np.interp(ts, times, f0_in, left=0, right=0)
    fout = np.interp(ts, times, f0_out, left=0, right=0)
    voiced = (fin > 0) & (fout > 0)
    y = np.zeros(n)
    wsum = np.zeros(n)
    # analysis pitch marks: one per input cycle (phase integration of the input pitch)
    ph = np.cumsum(np.where(voiced, fin, 0)) / SR
    marks = np.where(np.diff(np.floor(ph)) > 0)[0]
    if len(marks) < 2:
        return x.copy()
    # synthesis marks: one per output cycle
    phs = np.cumsum(np.where(voiced, fout, 0)) / SR
    smarks = np.where(np.diff(np.floor(phs)) > 0)[0]
    for s in smarks:
        a = marks[np.argmin(np.abs(marks - s))]
        period = int(SR / max(fin[a], 1))
        L = 2 * period
        lo, hi = a - period, a + period
        if lo < 0 or hi > n:
            continue
        win = np.hanning(L)
        so, se = s - period, s + period
        if so < 0 or se > n:
            continue
        y[so:se] += x[lo:hi] * win
        wsum[so:se] += win
    nz = wsum > 1e-3
    y[nz] /= wsum[nz]
    y[~voiced] = x[~voiced]  # breaths and silences pass through untouched
    return y


def write_wav(path, x):
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def main():
    t0 = time.time()
    log(f"pitch_demo.py  python {platform.python_version()}  numpy {np.__version__}  {platform.platform()}")
    x, f0_true, notes = sing()
    write_wav(OUT / "sung.wav", x)
    log(f"sung melody: {len(x)/SR:.2f} s at {SR} Hz, {len(notes)} notes")

    times, f0 = detect(x)
    voiced = f0 > 0
    # detector accuracy against the pitch we synthesised
    true_at = np.interp(times, np.arange(len(f0_true)) / SR, f0_true)
    ok = voiced & (true_at > 0)
    det_err = np.abs(1200 * np.log2(f0[ok] / true_at[ok]))
    log(f"detector: {voiced.sum()} voiced frames of {len(f0)}; median error vs synthesised pitch "
        f"{np.median(det_err):.2f} cents, 95th pct {np.percentile(det_err, 95):.2f} cents")

    # the worked example for the mechanism beat: one frame in the middle of note 5 (A4, -40 cents)
    a4 = notes[4]
    i_ex = int(np.argmin(np.abs(times - (a4["start"] + 0.12))))
    fr = x[int(times[i_ex] * SR - FRAME / 2):int(times[i_ex] * SR + FRAME / 2)]
    d, cmnd = yin_frame(fr, int(SR / FMAX), int(SR / FMIN))
    f_ex = f0[i_ex]
    m_ex = hz_to_midi(f_ex)
    cents_ex = 100 * (m_ex - round(m_ex))
    log(f"worked example: t={times[i_ex]:.3f}s measured {f_ex:.1f} Hz -> nearest {name(round(m_ex))} "
        f"({midi_to_hz(round(m_ex)):.1f} Hz), {cents_ex:+.1f} cents")

    # baseline: how far the singer is from the nearest correct note, per frame
    _, tgt_major = correction_curve(times, f0, 0, C_MAJOR)
    before_err = np.abs(1200 * np.log2(f0[voiced] / midi_to_hz(tgt_major[voiced])))
    log(f"before correction: mean {before_err.mean():.1f} cents off the nearest C-major note, "
        f"max {before_err.max():.1f}")

    runs = {}
    for label, tau, scale in [("instant", 0, C_MAJOR), ("fast", 40, C_MAJOR), ("natural", 250, C_MAJOR),
                              ("chromatic", 0, None)]:
        f_out, tgt = correction_curve(times, f0, tau, scale)
        y = psola(x, times, f0, f_out)
        write_wav(OUT / f"corrected_{label}.wav", y)
        t2, f_meas = detect(y)
        f_meas_on = np.interp(times, t2, f_meas)
        v = voiced & (f_meas_on > 0) & (tgt > 0)
        err = np.abs(1200 * np.log2(f_meas_on[v] / midi_to_hz(tgt[v])))
        last = notes[-1]
        in_last = (times > last["start"] + 0.2) & (times < last["end"] - 0.1) & v
        last_note = name(np.median(hz_to_midi(f_meas_on[in_last])))
        runs[label] = {"tau_ms": tau, "scale": "C major" if scale else "chromatic",
                       "f0_target_hz": np.round(f_out, 2).tolist(), "target_midi": tgt.tolist(),
                       "f0_measured_after_hz": np.round(f_meas_on, 2).tolist(),
                       "mean_err_cents": round(float(err.mean()), 1),
                       "median_err_cents": round(float(np.median(err)), 1),
                       "last_note_after": last_note}
        log(f"{label:9s} tau={tau:3d} ms {runs[label]['scale']:9s}: re-measured after correction mean "
            f"{err.mean():.1f} cents, median {np.median(err):.1f} from target; last note lands on {last_note}")

    data = {
        "sr": SR, "frame": FRAME, "hop": HOP,
        "melody": notes,
        "times": np.round(times, 4).tolist(),
        "f0_sung_hz": np.round(f0, 2).tolist(),
        "worked_example": {
            "time": round(float(times[i_ex]), 3),
            "wave": np.round(fr[:600] / np.max(np.abs(fr)), 4).tolist(),
            "cmnd": np.round(cmnd[:300], 4).tolist(),
            "period_samples": round(float(SR / f_ex), 2),
            "hz": round(float(f_ex), 1),
            "nearest": name(round(m_ex)),
            "nearest_hz": round(midi_to_hz(round(m_ex)), 1),
            "cents": round(float(cents_ex), 1),
        },
        "before_mean_err_cents": round(float(before_err.mean()), 1),
        "before_max_err_cents": round(float(before_err.max()), 1),
        "detector_median_err_cents": round(float(np.median(det_err)), 2),
        "runs": runs,
    }
    p = OUT / "pitch_demo.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    log(f"wrote {p.name} sha256 {hashlib.sha256(p.read_bytes()).hexdigest()[:16]}...  ({time.time()-t0:.1f} s)")
    (OUT / "run.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
