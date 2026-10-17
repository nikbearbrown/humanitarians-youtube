"""
Primary evidence for "Same Prompt, Different Answer".

Why an identical prompt returns different text, and why turning the temperature
to zero does not actually promise you the same answer twice.

Nothing here calls a model. Everything is arithmetic you can check by hand: a
plausible next-token distribution, the softmax that temperature rescales, and
one demonstration that floating-point addition is not associative.

Run:  python sampling_evidence.py
"""
import numpy as np

# A plausible set of next-token scores at one position. The exact values are
# illustrative -- the ARGUMENT is about the shape of the softmax, which holds
# for any logits, and every figure below is computed from these.
TOKENS = ["the", "a", "this", "that", "its", "every", "such"]
LOGITS = np.array([3.2, 2.6, 1.9, 1.5, 0.6, 0.1, -0.4])
ANSWER_LEN = 200


def softmax(z, temperature):
    z = z / temperature
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


def table():
    print("ONE position. The same prompt, the same model, the same scores.\n")
    print(f"{'token':<8}{'T=0.2':>10}{'T=1.0':>10}{'T=1.5':>10}")
    lo, mid, hi = softmax(LOGITS, 0.2), softmax(LOGITS, 1.0), softmax(LOGITS, 1.5)
    for i, t in enumerate(TOKENS):
        print(f"{t:<8}{lo[i]:>10.3f}{mid[i]:>10.3f}{hi[i]:>10.3f}")
    print("\nTemperature does not add randomness. It reshapes how peaked the")
    print("distribution already is, and then one draw is taken from it.")


def disagreement():
    print("\n--- chance this single position does NOT take the top token ---")
    for T in (0.2, 0.5, 0.7, 1.0, 1.5):
        p = softmax(LOGITS, T)
        print(f"  T={T:<4} top token p={p.max():.3f}   something else: {100*(1-p.max()):>5.1f}%")


def nucleus():
    print("\n--- top-p: how many tokens are even eligible at T=1.0 ---")
    p = softmax(LOGITS, 1.0)
    order = np.argsort(-p)
    cum = np.cumsum(p[order])
    for top_p in (0.5, 0.8, 0.9, 0.95, 1.0):
        k = int(np.searchsorted(cum, top_p) + 1)
        print(f"  top_p={top_p:<5} {k} of {len(TOKENS)}: " + ", ".join(TOKENS[i] for i in order[:k]))


def whole_answer():
    print(f"\n--- chance a {ANSWER_LEN}-token answer takes the top token EVERY time ---")
    for T in (0.2, 0.7, 1.0):
        pm = float(softmax(LOGITS, T).max())
        p_all = pm ** ANSWER_LEN
        odds = f"1 in {1/p_all:,.0f}" if p_all > 1e-12 else "effectively never"
        print(f"  T={T:<4} per-token {pm:.3f}   all {ANSWER_LEN}: {p_all:.2e}   ({odds})")
    print("  Even at a low temperature, two identical long answers are a coincidence,")
    print("  not a guarantee.")


def temperature_zero():
    print("\n--- and temperature 0 is not the guarantee people think it is ---")
    print("  Greedy decoding picks the largest score, so it is deterministic ONLY")
    print("  if the scores come out the same every time. They need not: floating")
    print("  point addition is not associative, so changing the ORDER the sum is")
    print("  accumulated in changes the result. Batch size, kernel choice and")
    print("  hardware all change that order.\n")

    rng = np.random.default_rng(0)
    vals = (rng.normal(0, 1, 1000) * 1e3).astype(np.float32)

    seq = np.float32(0.0)
    for v in vals:
        seq = np.float32(seq + v)
    blocked = vals.reshape(10, 100).sum(axis=1, dtype=np.float32).sum(dtype=np.float32)

    print(f"  same 1000 float32 numbers, summed one at a time : {seq:.8f}")
    print(f"  same 1000 float32 numbers, summed in 10 blocks  : {blocked:.8f}")
    print(f"  identical? {bool(seq == blocked)}        difference: {abs(float(seq)-float(blocked)):.3e}")
    print("\n  Note what this does and does not show. Non-associativity on its own")
    print("  does NOT make a model nondeterministic: the same code on the same")
    print("  input, in the same order, gives the same answer every time. What")
    print("  changes the order in a real server is dynamic batching -- your")
    print("  request lands in a batch of a different size, the kernel splits its")
    print("  reductions differently, and the logits come out a hair apart. If the")
    print("  top two candidates are closer than that hair, greedy decoding can")
    print("  pick the other one. SGLang's own docs name varying batch size as the")
    print("  main source and ship --enable-deterministic-inference to pin it.")


def main():
    print(__doc__.split("Run:")[0].strip())
    print()
    table()
    disagreement()
    nucleus()
    whole_answer()
    temperature_zero()
    print("\n--- the numbers the video uses ---")
    lo, mid = softmax(LOGITS, 0.2), softmax(LOGITS, 1.0)
    print(f"  T=0.2  top token {100*lo.max():.1f}%  -> {100*(1-lo.max()):.1f}% chance of a different word")
    print(f"  T=1.0  top token {100*mid.max():.1f}%  -> {100*(1-mid.max()):.1f}% chance of a different word")
    print(f"  identical {ANSWER_LEN}-token answer at T=0.2: 1 in {1/(lo.max()**ANSWER_LEN):,.0f}")
    print(f"  top_p=0.5 at T=1.0 leaves 2 of {len(TOKENS)} tokens eligible")

    print("\n--- for the on-screen curve: chance of an identical answer by length ---")
    lens = [1, 5, 10, 25, 50, 100, 200]
    pm = float(softmax(LOGITS, 0.2).max())
    pct = [round(100 * pm ** n, 3) for n in lens]
    print("   answer length :", lens)
    print("   identical %   :", pct)

    print("\n--- for the on-screen bars and silhouettes ---")
    p10, p02 = softmax(LOGITS, 1.0), softmax(LOGITS, 0.2)
    print("   tokens          :", TOKENS)
    print("   T=1.0 percent   :", [round(100*v, 1) for v in p10])
    print("   T=0.2 percent   :", [round(100*v, 1) for v in p02])
    sc = p02.max()
    print("   T=0.2 normalised:", [round(float(v/sc), 3) for v in p02])
    print("   T=1.0 normalised:", [round(float(v/sc), 3) for v in p10], " (same scale, so comparable)")


if __name__ == "__main__":
    main()
