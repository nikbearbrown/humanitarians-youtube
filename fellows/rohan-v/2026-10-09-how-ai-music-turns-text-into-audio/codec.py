"""Executable evidence for "How AI Music Generators Turn Text Into Audio".

A tiny audio TOKENIZER and a tiny next-token MODEL, built from scratch on synthetic music
(synth.py; no copyrighted audio):

  1. Codec. Cut audio into frames (MDCT, 256 coefficients every 10.7 ms at 24 kHz) and code each
     frame with RESIDUAL VECTOR QUANTIZATION: codebook 1 (1,024 entries, learned with k-means)
     gives the nearest rough match, its number is token 1; codebook 2 codes what is left over,
     and so on. More codebooks = more tokens per second = closer to the original. This is the
     quantizer SoundStream and EnCodec use; they learn the encoder too, this keeps a fixed MDCT.
  2. Model. Count which coarse token follows which (a trigram model, the simplest language model)
     on the training music, then measure how often it guesses the next token of music it has
     never heard, and let it continue a piece, one token at a time.
  3. "Text". Two training sets, labelled "calm piano" and "busy drums"; the prompt picks which
     statistics the model predicts from. Real systems turn the prompt into numbers with a text
     encoder that steers every prediction; this toy only shows that the text changes the odds.

    python codec.py      # evidence/run.log, evidence/codec.json, evidence/*.wav  (several minutes)
"""
import json
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import soundfile as sf

from synth import render

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
EV.mkdir(exist_ok=True)
SR = 24000
N = 256                       # coefficients per frame = hop; 24000 / 256 = 93.75 frames per second
K = 1024                      # entries per codebook -> 10 bits per token
QMAX = 12
FPS = SR / N
TRAIN = {"band": list(range(101, 113)), "piano": list(range(201, 213)), "drums": list(range(301, 313))}
TEST = {"band": 999, "piano": 998, "drums": 997}
TRAIN_S, TEST_S = 20.0, 12.0
log_lines = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    log_lines.append(s)


# ---------- MDCT (sine window, 50% overlap, perfect reconstruction) -------------------------
_n = np.arange(2 * N)
WIN = np.sin(np.pi * (_n + 0.5) / (2 * N))
BASIS = np.cos(np.pi / N * (_n[:, None] + 0.5 + N / 2) * (np.arange(N)[None, :] + 0.5))   # (2N, N)


def mdct(x):
    x = np.concatenate([np.zeros(N), x, np.zeros(2 * N - (len(x) % N or N) + N)])
    frames = np.lib.stride_tricks.sliding_window_view(x, 2 * N)[::N]
    return (frames * WIN) @ BASIS                                    # (frames, N)


def imdct(X, length):
    frames = (X @ BASIS.T) * WIN * (2.0 / N)
    y = np.zeros((len(X) + 1) * N)
    for i, f in enumerate(frames):
        y[i * N:i * N + 2 * N] += f
    return y[N:N + length]


# ---------- k-means and residual vector quantization ----------------------------------------
WGT = [1.0]   # set to the spectral weighting once it is measured (main)
def nearest(X, C, c2=None):
    c2 = (C * C).sum(1) if c2 is None else c2
    best = np.empty(len(X), dtype=np.int32)
    for i in range(0, len(X), 4096):
        d = c2[None, :] - 2 * X[i:i + 4096] @ C.T
        best[i:i + 4096] = d.argmin(1)
    return best


def kmeans(X, k, iters, rng):
    C = X[rng.choice(len(X), k, replace=False)].copy()
    for _ in range(iters):
        a = nearest(X, C)
        sums = np.zeros_like(C)
        np.add.at(sums, a, X)
        cnt = np.bincount(a, minlength=k)
        empty = cnt == 0
        C[~empty] = sums[~empty] / cnt[~empty, None]
        if empty.any():                          # re-seed dead entries on the worst-coded frames
            err = ((X - C[a]) ** 2).sum(1)
            C[empty] = X[np.argsort(err)[-empty.sum():]]
    return C


def train_rvq(X, rng):
    books, R = [], X.copy()
    for q in range(QMAX):
        t = time.time()
        C = kmeans(R, K, 12, rng)
        R = R - C[nearest(R, C)]
        books.append(C)
        log(f"  codebook {q + 1}: trained in {time.time() - t:.0f} s; residual energy {(R ** 2).sum() / (X ** 2).sum() * 100:.2f}% of the original")
    return books


def encode(X, books):
    R, toks = X / WGT[0], []
    for C in books:
        Cw = C / WGT[0]
        k = nearest(R, Cw)
        toks.append(k)
        R = R - Cw[k]
    return np.stack(toks, 1)                                         # (frames, Q)


def decode(T, books, q):
    return sum(books[i][T[:, i]] for i in range(q))


def lsd(X, Xh, lo_hz, hi_hz):
    """Log-spectral distance in dB over coarse bands (4 coefficients each), counting only bands you could
    hear: within 30 dB of that frame's loudest band. Silent bands would otherwise dominate."""
    a, b = int(lo_hz / (SR / 2) * N), int(hi_hz / (SR / 2) * N)
    b = a + (b - a) // 4 * 4
    Pf = (X ** 2).reshape(len(X), -1, 4).sum(2) + 1e-12
    P = (X[:, a:b] ** 2).reshape(len(X), -1, 4).sum(2) + 1e-12
    Ph = (Xh[:, a:b] ** 2).reshape(len(X), -1, 4).sum(2) + 1e-12
    audible = P > Pf.max(1, keepdims=True) * 1e-3
    if not audible.any():
        return float("nan")
    return float(np.sqrt(np.mean((10 * np.log10(P[audible] / Ph[audible])) ** 2)))


def kept(X, Xh, lo_hz, hi_hz):
    """How much of a band's energy the decoded audio still has, in dB (0 = all of it)."""
    a, b = int(lo_hz / (SR / 2) * N), int(hi_hz / (SR / 2) * N)
    return float(10 * np.log10((Xh[:, a:b] ** 2).sum() / ((X[:, a:b] ** 2).sum() + 1e-12) + 1e-12))


def snr(ref, est):
    return 10 * np.log10((ref ** 2).sum() / (((ref - est) ** 2).sum() + 1e-12))


def band_err(X, Xh, lo_hz, hi_hz):
    a, b = int(lo_hz / (SR / 2) * N), int(hi_hz / (SR / 2) * N)
    return float(((X[:, a:b] - Xh[:, a:b]) ** 2).sum() / ((X[:, a:b] ** 2).sum() + 1e-12))


# ---------- the language model: trigram over coarse tokens, with backoff ---------------------
class Trigram:
    def __init__(self, seqs):
        self.c3, self.c2, self.c1 = defaultdict(Counter), defaultdict(Counter), Counter()
        for s in seqs:
            for i, tok in enumerate(s):
                self.c1[tok] += 1
                if i >= 1:
                    self.c2[s[i - 1]][tok] += 1
                if i >= 2:
                    self.c3[(s[i - 2], s[i - 1])][tok] += 1

    def dist(self, a, b):
        for table, key in ((self.c3, (a, b)), (self.c2, b)):
            if key in table and sum(table[key].values()) > 0:
                return table[key]
        return self.c1

    def guess(self, a, b):
        return self.dist(a, b).most_common(1)[0][0]

    def sample(self, a, b, rng, temp=1.0):
        d = self.dist(a, b)
        toks = list(d)
        p = np.array([d[t] for t in toks], float) ** (1 / temp)
        return toks[rng.choice(len(toks), p=p / p.sum())]


def main():
    rng = np.random.default_rng(7)
    t0 = time.time()
    train = {st: [render(s, TRAIN_S, SR, st) for s in seeds] for st, seeds in TRAIN.items()}
    test = {st: render(s, TEST_S, SR, st) for st, s in TEST.items()}
    Xtr = {st: [mdct(y) for y in ys] for st, ys in train.items()}
    X_all = np.concatenate([x for xs in Xtr.values() for x in xs]).astype(np.float32)
    y0 = test["band"]
    X0 = mdct(y0)
    pr = imdct(X0, len(y0))
    log(f"MDCT: {N} coefficients per frame, {FPS:.2f} frames/s; perfect-reconstruction check SNR {snr(y0, pr):.0f} dB")
    log(f"training audio: {sum(len(v) for v in TRAIN.values())} synthetic tracks x {TRAIN_S:.0f} s "
        f"({len(X_all)} frames); test audio: 3 unseen tracks x {TEST_S:.0f} s")

    # Plain codebooks, no spectral weighting. Weighting each coefficient by its typical level was tried and
    # was worse on the unseen music (lower SNR, worse below 2 kHz); set CODEC_WEIGHTED=1 to repeat that test.
    import os
    W = np.sqrt((X_all ** 2).mean(0)) + 1e-6 if os.environ.get("CODEC_WEIGHTED") else np.ones(N, np.float32)
    log("training residual codebooks (k-means, 1,024 entries each):")
    WGT[0] = W
    books = [C * W for C in train_rvq((X_all / W).astype(np.float32), rng)]

    # --- quality per number of codebooks, on the unseen test tracks --------------------------
    T0 = encode(X0.astype(np.float32), books)
    curve = []
    for q in range(1, QMAX + 1):
        Xh = decode(T0, books, q)
        yh = imdct(Xh, len(y0))
        curve.append({"q": q, "kbps": round(FPS * q * 10 / 1000, 2), "tokens_per_s": round(FPS * q, 1),
                      "snr_db": round(float(snr(y0, yh)), 2),
                      "err_low": round(band_err(X0, Xh, 0, 2000), 4), "err_high": round(band_err(X0, Xh, 4000, 12000), 4),
                      "lsd_low": round(lsd(X0, Xh, 0, 2000), 2), "lsd_high": round(lsd(X0, Xh, 4000, 12000), 2),
                      "kept_high_db": round(kept(X0, Xh, 4000, 12000), 2), "kept_low_db": round(kept(X0, Xh, 0, 2000), 2)})
        log(f"  {q:2d} codebooks = {FPS * q:6.1f} tokens/s = {FPS * q * 10 / 1000:5.2f} kbps: SNR {curve[-1]['snr_db']:5.2f} dB; "
            f"spectrum off by {curve[-1]['lsd_low']:4.1f} dB below 2 kHz, {curve[-1]['lsd_high']:4.1f} dB above 4 kHz; "
            f"treble kept {curve[-1]['kept_high_db']:+5.1f} dB")
        if q in (1, 4, 12):
            sf.write(EV / f"codec_{q:02d}_books.wav", (0.8 * yh / np.max(np.abs(y0))).astype(np.float32), SR)
    sf.write(EV / "original.wav", (0.8 * y0 / np.max(np.abs(y0))).astype(np.float32), SR)

    # --- the language model ----------------------------------------------------------------
    seqs = {st: [encode(x.astype(np.float32), books[:1])[:, 0].tolist() for x in xs] for st, xs in Xtr.items()}
    lm = Trigram([s for v in seqs.values() for s in v])
    hit = tot = uni_hit = 0
    top = lm.c1.most_common(1)[0][0]
    for st, y in test.items():
        s = encode(mdct(y).astype(np.float32), books[:1])[:, 0].tolist()
        for i in range(2, len(s)):
            hit += lm.guess(s[i - 2], s[i - 1]) == s[i]
            uni_hit += top == s[i]
            tot += 1
    used = len(lm.c1)
    # a real stretch of the unseen piece's coarse tokens with the model's guess at each step
    s0 = encode(X0.astype(np.float32), books[:1])[:, 0].tolist()
    # the example window: the 12-token stretch (from 1 s on) whose 10 guesses' hit rate is closest to the
    # model's overall accuracy, so the picture is typical, not lucky or unlucky; the count shown is its own
    acc = hit / tot
    best = None
    for ex_i in range(int(FPS), len(s0) - 12):
        g = [lm.guess(s0[ex_i + i - 2], s0[ex_i + i - 1]) for i in range(2, 12)]
        h = sum(g[i - 2] == s0[ex_i + i] for i in range(2, 12))
        d = abs(h / 10 - acc)
        if best is None or d < best[0]:
            best = (d, ex_i, g)
    _, ex_i, g = best
    ex_tokens = s0[ex_i:ex_i + 12]
    ex_guess = [None, None] + g
    log(f"next-token model: trigram over codebook-1 tokens; {used} of {K} tokens used in training; on unseen music it "
        f"guesses the next token right {hit / tot * 100:.1f}% of the time ({hit}/{tot}); always guessing the most common "
        f"token: {uni_hit / tot * 100:.1f}%; a blind guess: {100 / K:.2f}%")

    # --- generation, "conditioned" on a prompt that picks the style statistics --------------
    # Two steps, coarse then fine (as published systems such as MusicLM do): the trigram predicts the
    # coarse token (codebook 1) one step at a time; then each coarse token gets the finer tokens
    # (codebooks 2-4) that most often went with it in that style's training music.
    gen = {}
    Qg = 4
    for prompt, st in (("calm piano", "piano"), ("busy drums", "drums")):
        full = [encode(x.astype(np.float32), books[:Qg]) for x in Xtr[st]]
        coarse = [s[:, 0].tolist() for s in full]
        lm_s = Trigram(coarse)
        fine = defaultdict(Counter)
        for s in full:
            for row in s:
                fine[int(row[0])][tuple(int(v) for v in row[1:])] += 1
        g = np.random.default_rng(11)
        out = coarse[0][:2]
        for _ in range(int(6 * FPS) - 2):
            out.append(lm_s.sample(out[-2], out[-1], g, temp=1.0))
        T = np.array([[k, *fine[k].most_common(1)[0][0]] for k in out])
        yg = imdct(decode(T, books, Qg), int(6 * SR))
        sf.write(EV / f"generated_{st}.wav", (0.8 * yg / (np.max(np.abs(yg)) + 1e-9)).astype(np.float32), SR)
        # how much is copied: a "seam" is where the next coarse token is not the next token of any
        # training passage it could be continuing; between seams it replays training music verbatim
        pos = defaultdict(set)
        for si, s in enumerate(coarse):
            for i, tk in enumerate(s):
                pos[tk].add((si, i))
        live, run, runs = set(pos[out[0]]), 1, []
        for tk in out[1:]:
            nxt = {(si, i + 1) for si, i in live if i + 1 < len(coarse[si]) and coarse[si][i + 1] == tk}
            if nxt:
                live, run = nxt, run + 1
            else:
                runs.append(run)
                live, run = set(pos[tk]), 1
        runs.append(run)
        gen[st] = {"prompt": prompt, "frames": len(out), "tokens": len(out) * Qg, "seams": len(runs) - 1,
                   "longest_copied_s": round(max(runs) / FPS, 2), "median_copied_s": round(float(np.median(runs)) / FPS, 3),
                   "first_tokens": T[:6].tolist()}
        log(f"generated 6 s for prompt '{prompt}': {len(out)} coarse tokens predicted one at a time, then 3 finer tokens each "
            f"= {len(out) * Qg} tokens; {len(runs) - 1} seams, so the longest stretch copied from training is "
            f"{max(runs) / FPS:.2f} s")

    # --- picture data -----------------------------------------------------------------------
    i0 = int(2.0 * SR)
    wave = y0[i0:i0 + int(0.004 * SR)]                                  # 4 ms = 96 samples
    fi = int(2.0 * FPS)
    frame = X0[fi]
    stages = [np.abs(decode(T0[fi:fi + 1], books, q)[0]) for q in (1, 2, 4, 12)]
    dn = lambda v: [round(float(x), 4) for x in np.log10(1e-3 + np.abs(v).reshape(64, -1).max(1))]
    used_c1 = Counter(T0[:, 0].tolist())
    data = {
        "params": {"sr": SR, "n": N, "fps": FPS, "K": K, "qmax": QMAX, "bits": 10},
        "wave": {"samples": [round(float(v), 4) for v in wave], "start_s": 2.0, "sr": SR},
        "tokens": {"first": T0[fi:fi + 8, :4].tolist(), "frame_index": fi},
        "frame": {"orig": dn(frame), "stages": {str(q): dn(s) for q, s in zip((1, 2, 4, 12), stages)}},
        "codebook_examples": [dn(books[0][k]) for k, _ in used_c1.most_common(6)],
        "curve": curve,
        "lm_example": {"tokens": ex_tokens, "guesses": ex_guess, "start_s": round(ex_i / FPS, 2)},
        "lm": {"accuracy": round(hit / tot, 4), "hits": hit, "total": tot, "baseline_common": round(uni_hit / tot, 4),
               "blind": 1 / K, "vocab_used": used},
        "gen": gen,
        "elapsed_s": round(time.time() - t0),
    }
    (EV / "codec.json").write_text(json.dumps(data), encoding="utf-8")
    (EV / "run.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    log(f"done in {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
