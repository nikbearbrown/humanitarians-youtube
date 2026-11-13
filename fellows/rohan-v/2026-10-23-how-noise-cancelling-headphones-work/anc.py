"""A feedforward noise-cancelling headphone, simulated, and measured on four kinds of noise.

    python anc.py            # writes evidence/run.log, evidence/results.json, evidence/scene.json, WAVs

The model (48 kHz, all sound synthetic):
  - a microphone on the outside of the ear cup hears the noise x;
  - the same noise reaches the ear d_p samples later through the cup (the primary path P);
  - the electronics take d_s samples to turn the microphone signal into anti-noise at the ear (the secondary path S:
    converter + processing latency, plus the speaker's own response);
  - an adaptive filter W (128 taps) learns the anti-noise with filtered-x LMS: it filters x through a model of S,
    and nudges W against the residual e at an in-ear error microphone, every sample.
    e = d + (S * W * x)   with   d = P * x.

The noise types: engine hum (90 Hz and its harmonics), low rumble (random, below 300 Hz), voices (babble,
300 Hz – 3.4 kHz, with syllable-rate bursts), clatter (random clicks). For each, ANC on vs off at the ear, in dB,
over the last 4 s (after it has adapted). Plus broadband pink noise in one-third-octave bands: the cancellation
curve. Plus the timing-error rule: a fixed timing error t costs phase 360°·f·t, and the residual of a cancelled
tone is |1 − e^{jφ}| = 2·sin(φ/2).
"""
import json
from pathlib import Path

import numpy as np

FS = 48000
D_P = 4          # noise: outside mic -> ear, samples (83 µs: about 2.9 cm of sound travel)
D_S = 6          # anti-noise: mic -> speaker -> ear, samples (125 µs of electronic + acoustic delay)
TAPS = 128
SECONDS = 10.0
HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"


def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / FS)
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc; y[i] = acc
    return y


def bandpass_fft(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / FS)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))


def pink(n, rng):
    X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / FS)
    X[1:] /= np.sqrt(f[1:]); X[0] = 0
    X[(f < 30) | (f > 12000)] = 0
    return np.fft.irfft(X, n)


def noises(rng):
    n = int(SECONDS * FS); t = np.arange(n) / FS
    engine = sum(a * np.sin(2 * np.pi * 90 * k * t + rng.uniform(0, 6.28)) for k, a in ((1, 1), (2, .6), (3, .4), (4, .25)))
    engine *= 1 + 0.03 * np.sin(2 * np.pi * 0.7 * t)
    rumble = bandpass_fft(rng.standard_normal(n), 20, 300)
    babble = bandpass_fft(rng.standard_normal(n), 300, 3400)
    syll = np.clip(bandpass_fft(rng.standard_normal(n), 2, 6), 0, None)          # 2–6 Hz syllable bursts
    voices = babble * (0.2 + syll / (syll.max() + 1e-9))
    clatter = np.zeros(n)
    for i in rng.integers(0, n - 2000, 60):
        L = int(rng.integers(300, 1500))
        clatter[i:i + L] += rng.uniform(.5, 1) * rng.standard_normal(L) * np.exp(-np.arange(L) / (L / 5))
    out = {"engine": engine, "rumble": rumble, "voices": voices, "clatter": clatter, "pink": pink(n, rng)}
    return {k: v / (np.sqrt(np.mean(v ** 2)) + 1e-12) * 0.1 for k, v in out.items()}


def secondary_ir():
    """Delay D_S, then a simple speaker response (gentle low cut, high roll-off), 32 taps."""
    h = np.zeros(32); h[D_S] = 1.0
    h = np.convolve(h, [0.6, 0.3, 0.1])[:32]                     # high roll-off: a short smoothing
    h -= np.convolve(h, np.ones(16) / 16)[:32] * 0.15             # a slight low cut
    return h


def run(x, s, mu=0.002):
    """Filtered-x LMS. Returns (e with ANC, d without)."""
    n = len(x)
    d = np.concatenate([np.zeros(D_P), x[:-D_P]])                # primary path: a pure delay
    xf = np.convolve(x, s)[:n]                                   # x filtered through the secondary-path model
    w = np.zeros(TAPS)
    xbuf = np.zeros(TAPS); xfbuf = np.zeros(TAPS); ybuf = np.zeros(len(s))
    e = np.empty(n)
    for i in range(n):
        xbuf[1:] = xbuf[:-1]; xbuf[0] = x[i]
        xfbuf[1:] = xfbuf[:-1]; xfbuf[0] = xf[i]
        y = w @ xbuf                                             # anti-noise sent to the speaker
        ybuf[1:] = ybuf[:-1]; ybuf[0] = y
        e[i] = d[i] + s @ ybuf                                   # what the in-ear mic hears
        w -= mu * e[i] * xfbuf / (xfbuf @ xfbuf + 1e-6)          # normalised FxLMS step
    return e, d


def db(a, b):
    return 10 * np.log10((np.mean(a ** 2) + 1e-20) / (np.mean(b ** 2) + 1e-20))


def third_octave(e, d):
    centres = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000]
    E = np.abs(np.fft.rfft(e * np.hanning(len(e)))) ** 2; D = np.abs(np.fft.rfft(d * np.hanning(len(d)))) ** 2
    f = np.fft.rfftfreq(len(e), 1 / FS)
    out = []
    for c in centres:
        m = (f >= c / 2 ** (1 / 6)) & (f < c * 2 ** (1 / 6))
        out.append(dict(hz=c, db=round(float(10 * np.log10(E[m].sum() / D[m].sum())), 1)))
    return out


def main():
    EV.mkdir(exist_ok=True)
    log = []
    P = lambda *a: (log.append(" ".join(str(x) for x in a)), print(*a))
    rng = np.random.default_rng(9)
    N = noises(rng)
    s = secondary_ir()
    tail = int(4 * FS)
    P(f"MODEL: {FS} Hz; noise reaches the ear {D_P} samples ({1e6 * D_P / FS:.0f} us) after the outside mic; "
      f"anti-noise takes {D_S} samples ({1e6 * D_S / FS:.0f} us); FxLMS, {TAPS} taps")
    res, keep = {}, {}
    for k in ("engine", "rumble", "voices", "clatter", "pink"):
        e, d = run(N[k], s)
        res[k] = round(db(e[-tail:], d[-tail:]), 1)
        keep[k] = (e, d)
        P(f"  {k:8s} ANC on vs off at the ear: {res[k]:+.1f} dB")
    bands = third_octave(*[a[-tail:] for a in keep["pink"]])
    P("")
    P("PINK NOISE, one-third-octave bands (ANC on vs off, dB): " + ", ".join(f"{b['hz']} {b['db']:+.1f}" for b in bands))
    # where the curve crosses -10 dB and 0 dB
    m10 = max((b["hz"] for b in bands if b["db"] <= -10), default=None)
    m0 = max((b["hz"] for b in bands if b["db"] < 0), default=None)
    P(f"  at least 10 dB quieter up to {m10} Hz; any reduction up to {m0} Hz")

    # timing error rule, and a check by simulation: a tone cancelled with a copy that is 0.1 ms late
    tau = 1e-4
    rule = []
    for f in (100, 500, 1000, 2000, 3000):
        phi = 2 * np.pi * f * tau
        resid = 2 * np.sin(phi / 2)
        t = np.arange(int(0.5 * FS)) / FS
        tone = np.sin(2 * np.pi * f * t)
        late = -np.sin(2 * np.pi * f * (t - tau))
        sim = db(tone + late, tone)
        rule.append(dict(hz=f, phase_deg=round(float(np.degrees(phi)), 1), residual=round(float(resid), 3),
                         db=round(float(20 * np.log10(resid)), 1), sim_db=round(float(sim), 1)))
    P("")
    P("TIMING ERROR 0.1 ms: " + "; ".join(f"{r['hz']} Hz: {r['phase_deg']} deg -> {r['db']:+.1f} dB (sim {r['sim_db']:+.1f})" for r in rule))
    f60 = 60 / 360 / tau
    P(f"  no reduction at all once the phase error passes 60 degrees: above {f60:.0f} Hz for a 0.1 ms error")

    # adaptation: the engine hum's residual level over the first 2 s (50 ms windows)
    e, d = keep["engine"]
    w = int(0.05 * FS)
    conv = [round(float(db(e[i:i + w], d[i:i + w])), 1) for i in range(0, int(2 * FS), w)]
    P("")
    P("ENGINE HUM, adapting (dB per 50 ms, first 2 s): " + " ".join(f"{c:+.0f}" for c in conv))

    (EV / "run.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(dict(types=res, bands=bands, rule=rule, f60=round(f60), conv=conv,
                                                     model=dict(fs=FS, d_p=D_P, d_s=D_S, taps=TAPS)), indent=1), encoding="utf-8")
    # waveform snippets for the scenes: 40 ms of engine hum at the ear, off and on (after adapting)
    i0 = int(8 * FS); n = int(0.04 * FS)
    (EV / "scene.json").write_text(json.dumps(dict(
        hum_off=np.round(keep["engine"][1][i0:i0 + n] / 0.3, 4).tolist(),
        hum_on=np.round(keep["engine"][0][i0:i0 + n] / 0.3, 4).tolist(),
        hum_anti=np.round(-keep["engine"][1][i0:i0 + n] / 0.3, 4).tolist()), separators=(",", ":")), encoding="utf-8")
    import wave
    for nm, k in (("engine", "engine"), ("voices", "voices")):
        e, d = keep[k]
        clip = np.concatenate([d[int(6 * FS): int(8 * FS)], e[int(8 * FS): int(10 * FS)]])     # 2 s off, then 2 s on
        pcm = (np.clip(clip / (np.abs(clip).max() + 1e-9) * 0.9, -1, 1) * 32767).astype("<i2")
        with wave.open(str(EV / f"{nm}_off_then_on.wav"), "wb") as wv:
            wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(FS); wv.writeframes(pcm.tobytes())


if __name__ == "__main__":
    main()
