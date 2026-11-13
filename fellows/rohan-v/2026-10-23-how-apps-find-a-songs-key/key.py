"""A key detector built the classic way, and tested on synthetic Western songs in all 24 keys.

    python key.py            # writes evidence/run.log, evidence/results.json, evidence/scene.json

Pipeline (Fujishima-style chroma + the Krumhansl–Schmuckler key-finding algorithm):
  1. chroma   — STFT; every bin between 55 Hz and 5 kHz is folded onto its pitch class (C, C#, … B), so each
                frame becomes 12 numbers: how much of each note is sounding, in any octave.
  2. profile  — the chroma summed over the whole song and scaled to sum to 1: the song's note profile.
  3. match    — correlate that profile with the Krumhansl–Kessler major and minor key profiles, rotated to
                all 12 tonics: 24 candidate keys. The highest correlation wins.

Scoring (MIREX audio key detection): right = 1.0; a perfect fifth away (same mode) = 0.5; the relative
major/minor = 0.3; the parallel major/minor = 0.2; anything else = 0.
"""
import json
from pathlib import Path

import numpy as np

import songs

SR, NFFT, HOP = 22050, 8192, 2048
HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
NOTES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
# Krumhansl & Kessler (1982) probe-tone ratings, tonic first
KK_MAJOR = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
KK_MINOR = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
STYLE_NAMES = {"pop": "Pop (major)", "minor": "Minor ballad", "harmonic": "Minor, raised 7th",
               "rock": "Rock (flat 7th)", "blues": "12-bar blues"}


def name(tonic, mode):
    return f"{NOTES[tonic % 12]} {mode}"


def chroma(y):
    """frames x 12: energy per pitch class from a Hann STFT, each frame scaled to its loudest pitch class."""
    win = np.hanning(NFFT)
    y = np.pad(y, NFFT // 2)
    nfr = 1 + (len(y) - NFFT) // HOP
    fr = np.lib.stride_tricks.as_strided(y, (nfr, NFFT), (y.strides[0] * HOP, y.strides[0])) * win
    M = np.abs(np.fft.rfft(fr, axis=1))
    f = np.fft.rfftfreq(NFFT, 1 / SR)
    keep = (f >= 55) & (f <= 5000)
    pc = (np.round(12 * np.log2(f[keep] / 440.0)).astype(int) + 9) % 12      # 0 = C
    E = M[:, keep] ** 2                                   # energy per bin
    C = np.zeros((nfr, 12))
    for k in range(12):
        C[:, k] = E[:, pc == k].sum(1)
    return C / (C.max(1, keepdims=True) + 1e-12)          # each frame scaled so its loudest note = 1 (librosa norm=inf)


def profile(C):
    p = C.sum(0)
    return p / (p.sum() + 1e-12)


def correlate(p):
    """24 Pearson correlations: index 0–11 major on tonic 0–11, 12–23 minor."""
    out = []
    for prof in (KK_MAJOR, KK_MINOR):
        for t in range(12):
            out.append(float(np.corrcoef(p, np.roll(prof, t))[0, 1]))
    return np.array(out)


def detect(y):
    p = profile(chroma(y))
    r = correlate(p)
    i = int(np.argmax(r))
    return (i % 12, "major" if i < 12 else "minor"), p, r


def relation(est, true):
    (te, me), (tt, mt) = est, true
    if est == true:
        return "right", 1.0
    if me == mt and (te - tt) % 12 in (5, 7):
        return "fifth", 0.5
    if me != mt:
        rel = (tt + 9) % 12 if mt == "major" else (tt + 3) % 12   # relative minor of a major key is a minor third down
        if te == rel:
            return "relative", 0.3
        if te == tt:
            return "parallel", 0.2
    return "other", 0.0


def main():
    EV.mkdir(exist_ok=True)
    log = []
    P = lambda *a: (log.append(" ".join(str(x) for x in a)), print(*a))
    rows = []
    for si, style in enumerate(songs.STYLES):
        mode = songs.STYLES[style]["mode"]
        for tonic in range(12):
            y = songs.render(style, tonic, seed=1000 * si + tonic, seconds=20)
            est, _, r = detect(y)
            rel, sc = relation(est, (tonic, mode))
            rows.append(dict(style=style, tonic=tonic, mode=mode, true=name(tonic, mode), est=name(*est),
                             relation=rel, score=sc, r_best=round(float(r.max()), 3)))
    P(f"TEST SET: {len(rows)} songs, 20 s each, 5 Western styles x 12 tonics (synthetic, songs.py)")
    P("")
    summ = {}
    for style in songs.STYLES:
        rs = [r for r in rows if r["style"] == style]
        c = {}
        for r in rs:
            c[r["relation"]] = c.get(r["relation"], 0) + 1
        summ[style] = dict(counts=c, score=round(sum(r["score"] for r in rs) / len(rs), 3))
        ex = [f"{r['true']}->{r['est']}" for r in rs if r["relation"] != "right"][:4]
        P(f"{STYLE_NAMES[style]:18s} right {c.get('right', 0):2d}/12  {c}  mean MIREX score {summ[style]['score']:.3f}  e.g. {ex}")
    allc = {}
    for r in rows:
        allc[r["relation"]] = allc.get(r["relation"], 0) + 1
    total = round(sum(r["score"] for r in rows) / len(rows), 3)
    P("")
    P(f"ALL: right {allc.get('right', 0)}/{len(rows)}  {allc}  mean MIREX weighted score {total:.3f}")

    # the worked example: C major pop (the test set's own song) and A minor ballad (same notes)
    ex_pop = songs.render("pop", 0, seed=0, seconds=20)
    ex_min = songs.render("minor", 9, seed=1009, seconds=20)
    (_, pp, rp), (_, pm, rm) = detect(ex_pop)[0:3], detect(ex_min)[0:3]
    est_min = detect(ex_min)[0]
    P("")
    P(f"EXAMPLE pop in C major: profile {np.round(pp, 3).tolist()}; best {name(int(np.argmax(rp)) % 12, 'major' if np.argmax(rp) < 12 else 'minor')} "
      f"r={rp.max():.3f}; runner-up {name(int(np.argsort(rp)[-2]) % 12, 'major' if np.argsort(rp)[-2] < 12 else 'minor')} "
      f"r={np.sort(rp)[-2]:.3f}; A minor r={rp[12 + 9]:.3f}")
    P(f"EXAMPLE minor ballad in A minor: best {name(*est_min)} r={rm.max():.3f}; A minor r={rm[12 + 9]:.3f}; C major r={rm[0]:.3f}")

    # a key change: pop in C major, up a semitone at 10 s; global answer vs 8-second windows
    y = songs.render("pop", 0, seed=4242, seconds=20, modulate_at=10.0, modulate_by=1)
    g, _, _ = detect(y)
    C = chroma(y)
    fps = SR / HOP
    win = int(8 * fps)
    track = []
    for s in range(0, C.shape[0] - win + 1, int(fps)):
        r = correlate(profile(C[s:s + win]))
        i = int(np.argmax(r))
        track.append(dict(t=round((s + win / 2) / fps, 2), key=name(i % 12, "major" if i < 12 else "minor"), r=round(float(r.max()), 3)))
    P("")
    P(f"KEY CHANGE (C major -> C# major at 10 s): whole song says {name(*g)}; 8-s windows: "
      + ", ".join(f"{w['t']}s {w['key']}" for w in track))

    (EV / "run.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(dict(rows=rows, summary=summ, all=allc, score=total), indent=1),
                                     encoding="utf-8")
    (EV / "scene.json").write_text(json.dumps(dict(
        pop=dict(profile=np.round(pp, 4).tolist(), r=np.round(rp, 6).tolist(), chroma=np.round(chroma(ex_pop)[:40] / chroma(ex_pop)[:40].max(), 3).tolist()),
        minor=dict(profile=np.round(pm, 4).tolist(), r=np.round(rm, 6).tolist(), est=name(*est_min)),
        change=dict(global_key=name(*g), track=track),
        kk=dict(major=KK_MAJOR.tolist(), minor=KK_MINOR.tolist())), separators=(",", ":")), encoding="utf-8")
    import wave
    for nm, sig in (("song_c_major_pop.wav", ex_pop[: int(6 * SR)]), ("song_key_change.wav", y[int(6 * SR): int(14 * SR)])):
        pcm = (np.clip(sig / (np.abs(sig).max() + 1e-9) * 0.9, -1, 1) * 32767).astype("<i2")
        with wave.open(str(EV / nm), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


if __name__ == "__main__":
    main()
