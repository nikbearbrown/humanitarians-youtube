"""quant_toy.py — every number shown on screen in claude-hai-quantization.

Run:  .venv/bin/python youtube/brutalist/claude-hai-quantization/evidence/quant_toy.py
Writes quant_toy.out.txt (human-readable) and quant_toy.json (copied into the scenes) next to itself.

Toy, not a benchmark: a seeded weight matrix stands in for a real layer. Its rows are drawn from a
heavy-tailed distribution (Student-t, df=4) scaled to std ~0.02, which gives the occasional large
"outlier" weight that real LLM layers have. Quantization is plain symmetric round-to-nearest (RTN):
    q = round(w / s),  s = max|w| / qmax,  qmax = 2**(bits-1) - 1,  w_hat = s * q
which is the baseline that GPTQ / AWQ improve on.
"""
import json
import pathlib

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
OUT = []
J = {}


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    OUT.append(line)


GB = 1e9  # decimal gigabytes, as model cards quote them

# ---------------------------------------------------------------- B02 / B03 / B06: memory math
say("== memory for the weights alone (decimal GB) ==")
mem = {}
for params, name in [(70e9, "70B"), (7e9, "7B")]:
    for bits in (16, 8, 4):
        gb = params * bits / 8 / GB
        mem[f"{name}@{bits}"] = gb
        say(f"{name} params x {bits:2d} bits = {gb:7.1f} GB")
J["mem"] = mem
# real 4-bit formats also store one 16-bit scale per group; group of 32 -> +0.5 bit/weight
over = 7e9 * (4 + 16 / 32) / 8 / GB
say(f"7B at 4 bits + one fp16 scale per 32 weights = {over:.2f} GB  (why '~3.5 GB' is 'about')")
J["mem_4bit_with_scales_g32"] = round(over, 2)
laptop = 16
say(f"70B@16 / a {laptop} GB laptop = {mem['70B@16'] / laptop:.2f}x its whole memory")
J["hook_ratio_16gb"] = round(mem["70B@16"] / laptop, 2)

# ---------------------------------------------------------------- B03: one weight, its 16 bits
w0 = np.float16(0.0213)
bits16 = format(w0.view(np.uint16), "016b")
say("\n== one weight in fp16 ==")
say(f"0.0213 as float16 = {float(w0):.6f}  bits {bits16[0]} {bits16[1:6]} {bits16[6:]}  (sign exponent mantissa)")
J["w0"] = {"value": float(w0), "bits": bits16}

# ---------------------------------------------------------------- toy layer
rng = np.random.default_rng(2026)
ROWS, COLS = 512, 4096
W = (rng.standard_t(df=4, size=(ROWS, COLS)) * 0.02 / np.sqrt(2)).astype(np.float32)  # t4 var = 2
X = rng.standard_normal((COLS, 64)).astype(np.float32)  # 64 input vectors
Y = W @ X
say(f"\n== toy layer: {ROWS}x{COLS} weights (seed 2026), std {W.std():.4f}, max|w| {np.abs(W).max():.4f} ==")


def rtn(w, bits, group=None):
    """symmetric round-to-nearest; one scale per row, or per `group` consecutive weights."""
    qmax = 2 ** (bits - 1) - 1
    shp = w.shape
    g = w.reshape(-1, group) if group else w.reshape(shp[0], -1)
    s = np.abs(g).max(axis=1, keepdims=True) / qmax
    s[s == 0] = 1
    q = np.clip(np.round(g / s), -qmax - 1, qmax)
    return (q * s).reshape(shp)


def rel(a, b):
    return float(np.sqrt(((a - b) ** 2).mean()) / np.sqrt((b ** 2).mean()))


# ---------------------------------------------------------------- B03: a patch of the toy layer, one weight's bits
patch = W[0, :24]
k = int(np.argmin(np.abs(np.abs(patch) - 0.02)))  # a typical-size weight to zoom into
wk = np.float16(patch[k])
bk = format(wk.view(np.uint16), "016b")
say("\n== B03: first 24 weights of row 0 ==")
say(" ".join(f"{v:+.4f}" for v in patch))
say(f"zoom: weight #{k} = {float(patch[k]):+.4f} -> float16 bits {bk[0]} {bk[1:6]} {bk[6:]}")
J["patch"] = {"w": [round(float(v), 4) for v in patch], "k": k, "bits": bk}

# ---------------------------------------------------------------- B04 / B05: a group of 8 weights
say("\n== B04/B05: eight weights rounded onto the 4-bit grid ==")
g8 = W[3, :8].copy()
qmax4 = 7
s8 = float(np.abs(g8).max() / qmax4)
q8 = np.clip(np.round(g8 / s8), -8, 7).astype(int)
say("weights :", " ".join(f"{v:+.4f}" for v in g8))
say(f"scale s = max|w| / 7 = {s8:.5f}")
say("q       :", " ".join(f"{v:+d}" for v in q8))
say("s*q     :", " ".join(f"{v:+.4f}" for v in q8 * s8))
J["group8"] = {"w": [round(float(v), 4) for v in g8], "s": round(s8, 5), "q": q8.tolist(),
               "deq": [round(float(v), 4) for v in q8 * s8]}
say(f"levels: 8 bits = {2 ** 8}, 4 bits = {2 ** 4}")
J["levels"] = {"8": 2 ** 8, "4": 2 ** 4}

# ---------------------------------------------------------------- B05: one scale vs a scale per group
say("\n== B05: weight error, one scale per row vs per group of 32 ==")
err = {}
for bits in (8, 4):
    for grp, lab in [(None, "per-row"), (32, "per-32")]:
        e = rel(rtn(W, bits, grp), W)
        err[f"{bits}-{lab}"] = e
        say(f"{bits}-bit {lab:8s}: relative weight error {e * 100:5.1f} %")
J["err"] = {k: round(v * 100, 1) for k, v in err.items()}

# ---------------------------------------------------------------- B07: errors cancel in the output
say("\n== B07: do the rounding errors cancel? (4-bit, per-32) ==")
Wq = rtn(W, 4, 32)
E = Wq - W
row = 0
NET = np.abs(E @ X)                 # actual error of every output (512 rows x 64 inputs)
WORST = np.abs(E) @ np.abs(X)       # the same sums if every error pushed the same way
worst, signed = float(WORST.mean()), float(NET.mean())
say(f"each output = a sum of {COLS} products; average error contribution over {ROWS * 64} outputs:")
say(f"  if every error pushed the same way: {worst:.4f}")
say(f"  actual net error (they cancel):     {signed:.4f}   {worst / signed:.0f}x smaller")
say(f"  mean weight error {E.mean():+.2e} (~0), share rounded up {float((E > 0).mean()) * 100:.1f} %")
hist, edges = np.histogram(E[row].reshape(-1, 32) / (np.abs(W[row].reshape(-1, 32)).max(1, keepdims=True) / 7),
                           bins=11, range=(-0.55, 0.55))
say("  histogram of row-0 errors in grid steps (-0.5..+0.5):", hist.tolist())
J["cancel"] = {"n": COLS, "worst": round(worst, 4), "net": round(signed, 4), "ratio": round(worst / signed),
               "pos_share": round(float((E > 0).mean()) * 100, 1), "hist": hist.tolist()}

# outliers: one big weight stretches its group's scale and crushes its neighbours
say("\n== B07: one outlier in a group of 32 (4-bit) ==")
grp = W[7, :32].copy()
grp[5] = 0.30  # an outlier ~15x the typical weight
base = rel(rtn(grp[None], 4, 32)[0], grp)
mask = np.ones(32, bool); mask[5] = False
rest = grp[mask]
kept = rtn(rest[None], 4, 31)[0]
both = grp.copy(); both[mask] = kept  # outlier kept at 16 bits, others re-scaled without it
prot = rel(both, grp)
nz_plain = int((np.round(grp / (np.abs(grp).max() / 7))[mask] != 0).sum())
nz_prot = int((np.round(rest / (np.abs(rest).max() / 7)) != 0).sum())
say(f"outlier in the group : error {base * 100:.1f} %, {nz_plain}/31 neighbours keep a non-zero level")
say(f"outlier set aside    : error {prot * 100:.1f} %, {nz_prot}/31 neighbours keep a non-zero level")
m_plain = (np.round(grp / (np.abs(grp).max() / 7)) != 0).astype(int)
m_prot = m_plain.copy(); m_prot[mask] = (np.round(rest / (np.abs(rest).max() / 7)) != 0).astype(int)
say("non-zero mask, outlier in :", "".join(map(str, m_plain)))
say("non-zero mask, set aside  :", "".join(map(str, m_prot)))
J["outlier"] = {"plain": round(base * 100, 1), "protected": round(prot * 100, 1),
                "nz_plain": nz_plain, "nz_prot": nz_prot, "mask_plain": "".join(map(str, m_plain)),
                "mask_prot": "".join(map(str, m_prot)), "idx": 5}

# ---------------------------------------------------------------- B08: error vs bits
say("\n== B08: error vs bits (per-32 scales) ==")
sweep = {}
for bits in (8, 6, 5, 4, 3, 2):
    e = rel(Wq_b := rtn(W, bits, 32), W)
    o = rel(Wq_b @ X, Y)
    sweep[str(bits)] = {"weight": round(e * 100, 1), "output": round(o * 100, 1)}
    say(f"{bits} bits: weight error {e * 100:5.1f} %   output error {o * 100:5.1f} %")
J["sweep"] = sweep

# ---------------------------------------------------------------- B06: memory bandwidth bound
say("\n== B06: why smaller is faster (illustrative 100 GB/s memory bandwidth) ==")
bw = 100
speed = {}
for bits in (16, 8, 4):
    gb = mem[f"7B@{bits}"]
    speed[str(bits)] = round(bw / gb, 1)
    say(f"7B @ {bits:2d} bits: every token reads {gb:4.1f} GB -> at most {bw / gb:5.1f} tokens/s")
J["speed"] = {"bw": bw, "tps": speed}

(HERE / "quant_toy.out.txt").write_text("\n".join(OUT) + "\n")
(HERE / "quant_toy.json").write_text(json.dumps(J, indent=1) + "\n")
