"""Executable evidence for "How Shazam Finds a Song": a small audio fingerprinter, built the way
the 2003 Shazam paper describes it (spectrogram peaks -> anchor/target hashes -> offset voting),
run on a library of synthetic songs (synth.py) and on noisy phone-style clips of them.

    python fingerprint.py            # writes evidence/run.log, evidence/fingerprint.json, evidence/*.wav

Every number and picture in the video comes from this run.
"""
import json
import time
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.ndimage import maximum_filter
from scipy.signal import butter, sosfilt, stft

from synth import render

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
SR = 11025                 # the paper's systems worked on downsampled audio; 11 kHz keeps the music audible
NFFT, HOP = 1024, 256      # 93 ms windows, a column every 23.2 ms
FAN_OUT = 5                # each anchor pairs with up to 5 peaks in its target zone
ZONE_T = (2, 64)           # target zone: 2..64 columns ahead (46 ms .. 1.49 s)
ZONE_F = 96                # ... and within 96 bins (1,034 Hz) up or down
SONGS = ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F"]
SEEDS = [11, 23, 37, 41, 59, 67]
SONG_S = 40.0
MIN_VOTES = 8           # fewer votes than this in the best offset bin = no confident match
log_lines = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    log_lines.append(s)


def spectrogram(y):
    f, t, Z = stft(y, SR, nperseg=NFFT, noverlap=NFFT - HOP, boundary=None, padded=False)
    return 20 * np.log10(np.abs(Z) + 1e-6)          # dB, shape (freq bins, columns)


def peaks(S):
    """Constellation map: points that are the loudest in their 21-bin x 15-column neighbourhood,
    and clearly above that column's typical level. Returns (column, bin) pairs, time-ordered."""
    local = maximum_filter(S, size=(21, 15), mode="constant", cval=-200) == S
    floor = np.median(S, axis=0, keepdims=True) + 18
    keep = local & (S > floor) & (np.arange(S.shape[0])[:, None] > 4)
    fb, tc = np.nonzero(keep)
    order = np.lexsort((fb, tc))
    return np.stack([tc[order], fb[order]], axis=1)


def hashes(pk):
    """(anchor column, hash) for every anchor and up to FAN_OUT targets in its zone.
    hash = f1 (10 bits) | f2 (10 bits) | dt (6 bits): three numbers that survive noise."""
    out = []
    for i, (t1, f1) in enumerate(pk):
        n = 0
        for t2, f2 in pk[i + 1:]:
            dt = t2 - t1
            if dt < ZONE_T[0]:
                continue
            if dt > ZONE_T[1] or n >= FAN_OUT:
                break
            if abs(int(f2) - int(f1)) > ZONE_F:
                continue
            out.append((int(t1), (int(f1) << 16) | (int(f2) << 6) | int(dt)))
            n += 1
    return out


def unpack(h):
    return h >> 16, (h >> 6) & 1023, h & 63


def phone(y, rng, snr_db, babble):
    """What a phone in a noisy room hears: the song plus room noise at `snr_db`, band-limited to
    150-4,000 Hz, with a level change. `babble` is crowd-like noise (a busy room)."""
    sos = butter(4, [150, 4000], btype="band", fs=SR, output="sos")
    s = sosfilt(sos, y)
    noise = sosfilt(sos, babble[: len(y)])
    p_s, p_n = np.mean(s ** 2), np.mean(noise ** 2)
    mix = s + noise * np.sqrt(p_s / (p_n * 10 ** (snr_db / 10)))
    mix *= 0.35 / (np.max(np.abs(mix)) + 1e-9)
    return mix.astype(np.float32)


def room_noise(n, rng):
    """Pink-ish noise plus overlapping voice-band bursts (a crowded cafe, not a real recording)."""
    w = rng.standard_normal(n)
    pink = np.cumsum(w) - np.convolve(np.cumsum(w), np.ones(200) / 200, mode="same")
    pink /= np.std(pink) + 1e-9
    talk = np.zeros(n)
    for _ in range(int(n / SR * 3)):
        L = int(rng.uniform(0.15, 0.6) * SR)
        i = int(rng.integers(0, max(1, n - L)))
        f = rng.uniform(110, 260)
        tt = np.arange(L) / SR
        syl = np.sin(2 * np.pi * f * tt + 2 * np.sin(2 * np.pi * 4 * tt)) * np.hanning(L)
        talk[i:i + L] += syl * rng.uniform(0.5, 1.2)
    talk /= np.std(talk) + 1e-9
    return 0.6 * pink + talk


class Index:
    def __init__(self):
        self.db = {}
        self.n = 0

    def add(self, sid, y):
        hs = hashes(peaks(spectrogram(y)))
        for t, h in hs:
            self.db.setdefault(h, []).append((sid, t))
        self.n += len(hs)
        return len(hs)

    def votes(self, y):
        """For each song, a histogram of offsets (library column - clip column) over matching hashes."""
        q = hashes(peaks(spectrogram(y)))
        per, self.pairs = {}, {}
        for tq, h in q:
            for sid, tl in self.db.get(h, ()):
                per.setdefault(sid, []).append(tl - tq)
                self.pairs.setdefault(sid, []).append((int(tq), int(tl)))
        result = {}
        for sid, offs in per.items():
            vals, counts = np.unique(np.array(offs), return_counts=True)
            k = int(np.argmax(counts))
            result[sid] = {"best_offset": int(vals[k]), "score": int(counts[k]), "matches": len(offs),
                           "offsets": offs}
        return len(q), result


def identify(index, y):
    nq, res = index.votes(y)
    ranked = sorted(res.items(), key=lambda kv: -kv[1]["score"])
    return nq, ranked


def main():
    rng = np.random.default_rng(2026)
    t0 = time.time()
    lib = [render(s, SONG_S, SR, "band") for s in SEEDS]
    index = Index()
    per_song = [index.add(i, y) for i, y in enumerate(lib)]
    pk_rate = np.mean([len(peaks(spectrogram(y))) / SONG_S for y in lib])
    log(f"library: {len(lib)} synthetic songs x {SONG_S:.0f} s at {SR} Hz; {index.n} hashes "
        f"({', '.join(str(n) for n in per_song)}); {pk_rate:.1f} peaks/s; {index.n / (len(lib) * SONG_S):.0f} hashes/s; "
        f"{len(index.db)} distinct hash values; built in {time.time() - t0:.1f} s")
    babble = room_noise(int(SR * SONG_S), rng)

    # --- the worked example: 5 s of Song C from 12.0 s, in a cafe at 0 dB SNR ---------------
    sid, start, dur, snr = 2, 12.0, 5.0, 0.0
    i0 = int(start * SR)
    clean = lib[sid][i0:i0 + int(dur * SR)]
    clip = phone(clean, rng, snr, babble[int(3.1 * SR):])
    t1 = time.time()
    nq, ranked = identify(index, clip)
    ms = (time.time() - t1) * 1000
    pairs = {SONGS[s]: [[round(a * HOP / SR, 3), round(b * HOP / SR, 3)] for a, b in index.pairs[s]] for s, _ in ranked[:2]}
    top, second = ranked[0], ranked[1]
    col_s = HOP / SR
    log(f"query: {SONGS[sid]} from {start:.1f} s, {dur:.0f} s long, cafe noise at {snr:+.0f} dB SNR, 150-4000 Hz: "
        f"{nq} hashes; search {ms:.0f} ms")
    for s, r in ranked:
        log(f"  {SONGS[s]}: {r['matches']} hash matches, best offset bin {r['score']} votes "
            f"at {r['best_offset'] * col_s:.2f} s")
    found = top[0] == sid
    log(f"=> {SONGS[top[0]]} at {top[1]['best_offset'] * col_s:.2f} s ({'correct' if found else 'WRONG'}); "
        f"{top[1]['score']} votes vs {second[1]['score']} for the runner-up")
    sf.write(EV / "clip_cafe.wav", clip, SR)
    seg = lib[sid][i0:i0 + int(dur * SR)]
    sf.write(EV / "original_segment.wav", (0.35 * seg / np.max(np.abs(seg))).astype(np.float32), SR)

    # picture data for B01/B02: 3 s of the CLEAN clip's spectrogram + its peaks + a hash fan
    S = spectrogram(clean)
    pk = peaks(S)
    ncol = int(3.0 / col_s)
    fmax_bin = int(3000 / (SR / NFFT))
    sub = S[:fmax_bin, :ncol]
    lo, hi = np.percentile(sub, 20), np.percentile(sub, 99.5)
    grid = np.clip((sub - lo) / (hi - lo), 0, 1)
    # display grid: every column, frequency pooled in pairs (mean), a gentle gamma for print-like contrast
    gf = grid.shape[0] // 2
    small = grid[: gf * 2].reshape(gf, 2, grid.shape[1]).mean(axis=1) ** 1.6
    vis_pk = [[int(t), int(f)] for t, f in pk if t < ncol and f < fmax_bin]
    # the same 3 s as the phone heard it (0 dB cafe noise, band-limited): which clean peaks survive?
    Sn = spectrogram(clip)
    pkn = peaks(Sn)
    nsub = Sn[:fmax_bin, :ncol]
    ngrid = np.clip((nsub - lo) / (hi - lo), 0, 1)
    vis_pkn = [[int(t), int(f)] for t, f in pkn if t < ncol and f < fmax_bin]
    noisy_set = {(t, f) for t, f in vis_pkn}
    survived = [p for p in vis_pk if any((p[0] + dt, p[1] + df) in noisy_set for dt in (-1, 0, 1) for df in (-2, -1, 0, 1, 2))]
    log(f"peaks in the 3 s picture: {len(vis_pk)} clean, {len(vis_pkn)} in the noisy phone clip; {len(survived)} of the "
        f"{len(vis_pk)} clean peaks are still there (within 1 column and 2 bins)")
    hs = hashes(pk)
    anchor_i = None
    for k, (t, f) in enumerate(pk):
        if 0.9 / col_s < t < 1.4 / col_s and 30 < f < fmax_bin * 0.6:
            fan = [h for tt, h in hs if tt == t and unpack(h)[0] == f]
            if len(fan) >= 4:
                anchor_i = k
                break
    at, af = pk[anchor_i]
    fan = [unpack(h) for tt, h in hs if tt == at and unpack(h)[0] == af]
    ex = fan[0]
    log(f"worked hash: anchor {af * SR / NFFT:.0f} Hz at {at * col_s:.2f} s -> target {ex[1] * SR / NFFT:.0f} Hz, "
        f"dt {ex[2] * col_s:.2f} s; packed value {(ex[0] << 16) | (ex[1] << 6) | ex[2]}")

    # --- noise sweep: 30 random 5 s queries per level --------------------------------------
    sweep = []
    for snr_i in [10, 5, 0, -5, -10, -15]:
        ok = wrong = none = off_ok = 0
        tops = []
        for _ in range(30):
            s = int(rng.integers(len(lib)))
            st = rng.uniform(1, SONG_S - dur - 1)
            seg = lib[s][int(st * SR):int(st * SR) + int(dur * SR)]
            off = rng.uniform(0, SONG_S - dur - 1)
            q = phone(seg, rng, snr_i, babble[int(off * SR):])
            _, rk = identify(index, q)
            top = rk[0][1]["score"] if rk else 0
            tops.append(top)
            if top < MIN_VOTES:
                none += 1
            elif rk[0][0] == s:
                ok += 1
                off_ok += abs(rk[0][1]["best_offset"] * col_s - st) < 0.1
            else:
                wrong += 1
        sweep.append({"snr": snr_i, "correct": ok, "wrong": wrong, "no_match": none, "of": 30,
                      "start_within_0_1s": off_ok, "median_top_votes": float(np.median(tops))})
        log(f"sweep {snr_i:+d} dB: {ok}/30 named correctly, {wrong} wrong, {none} no match "
            f"(start time within 0.1 s on {off_ok} of the {ok}); median top score {np.median(tops):.0f}")

    # --- the catch: re-performances of the same song ---------------------------------------
    variants = {}
    for name, kw in [("same recording", {}), ("one semitone higher", {"transpose": 1}),
                     ("6% faster", {"tempo": 1.06}), ("melody only, hummed", {"style": "hum"})]:
        style = kw.pop("style", "band")
        y = render(SEEDS[sid], SONG_S, SR, style, **kw) if (kw or style != "band") else lib[sid]
        st = start if "faster" not in name else start / 1.06
        seg = y[int(st * SR):int(st * SR) + int(dur * SR)]
        q = phone(seg, np.random.default_rng(5), 10.0, babble[int(7 * SR):])
        _, rk = identify(index, q)
        sc = {SONGS[s]: r["score"] for s, r in rk}
        variants[name] = {"top": SONGS[rk[0][0]] if rk else None, "song_c_votes": sc.get("Song C", 0),
                          "best_other": max([v for k, v in sc.items() if k != "Song C"] or [0]),
                          "identified": bool(rk) and rk[0][0] == sid and rk[0][1]["score"] >= MIN_VOTES}
        log(f"variant '{name}' (+10 dB SNR): Song C {variants[name]['song_c_votes']} votes, best other "
            f"{variants[name]['best_other']} -> {'MATCH' if variants[name]['identified'] else 'no match'}")

    data = {
        "params": {"sr": SR, "nfft": NFFT, "hop": HOP, "col_s": col_s, "fan_out": FAN_OUT, "zone_t": ZONE_T,
                   "zone_f_hz": ZONE_F * SR / NFFT, "songs": SONGS, "song_s": SONG_S},
        "library": {"hashes": index.n, "per_song": per_song, "distinct": len(index.db),
                    "peaks_per_s": round(float(pk_rate), 1), "hashes_per_s": round(index.n / (len(lib) * SONG_S))},
        "query": {"song": SONGS[sid], "start": start, "dur": dur, "snr": snr, "hashes": nq, "search_ms": round(ms),
                  "ranked": [{"song": SONGS[s], "matches": r["matches"], "score": r["score"],
                              "offset_s": round(r["best_offset"] * col_s, 2),
                              "hist": offset_hist(r["offsets"], col_s)} for s, r in ranked]},
        "pairs": pairs,
        "spec": {"grid": np.round(small, 3).tolist(), "cols": ncol, "fmax_hz": fmax_bin * SR / NFFT,
                 "peaks": vis_pk, "bins": fmax_bin,
                 "noisy_grid": np.round(ngrid[: gf * 2].reshape(gf, 2, ngrid.shape[1]).mean(axis=1) ** 1.6, 3).tolist(),
                 "noisy_peaks": vis_pkn, "survived": survived},
        "hash_example": {"anchor": [int(at), int(af)], "targets": [[int(at + d), int(f2)] for _, f2, d in fan],
                         "anchor_hz": round(af * SR / NFFT), "target_hz": round(ex[1] * SR / NFFT),
                         "dt_s": round(ex[2] * col_s, 2), "packed": int((ex[0] << 16) | (ex[1] << 6) | ex[2])},
        "sweep": sweep,
        "variants": variants,
    }
    (EV / "fingerprint.json").write_text(json.dumps(data), encoding="utf-8")
    (EV / "run.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")


def offset_hist(offs, col_s, lo=-2.0, hi=40.0, bins=168):
    h, _ = np.histogram(np.array(offs) * col_s, bins=bins, range=(lo, hi))
    return h.tolist()


if __name__ == "__main__":
    main()
