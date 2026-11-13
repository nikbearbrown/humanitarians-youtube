#!/usr/bin/env python3
"""fuzz_vs_proof.py — random testing vs a solver, on a toy decoder with a large-input bug.

The Anthropic post (Oct 22, 2026) says fuzzers miss bugs that only very large
inputs reach, because they mutate small inputs (typically capped around 1 MB),
and that a proof covers every input within its limits (there: up to 64 MB).
This is that idea at toy scale. It is OUR example, not code from the post, and
the solver here is Z3, not the Rocq proofs the post describes.

The toy: an 8-byte header says how many 4-byte records follow. The decoder
copies the records into an output buffer. In the buggy version the buffer was
capped at 16 MiB "for safety", so a valid file over 16 MiB writes past its end.

  1. Fuzzing: 1,000,000 random files of up to 1 MiB, the record count chosen
     valid for the file half the time (a generous fuzzer). Count crashes.
  2. Solving: ask Z3 for ANY input up to 64 MiB that makes the decoder write
     out of bounds, and the smallest one. Replay it on the real function.
  3. Fix the cap and ask again: no such input exists -> a proof for every
     input up to 64 MiB.

Run:  <venv with z3-solver>/bin/python fuzz_vs_proof.py
"""
import platform
import random
import sys
import time

import z3

MiB = 1 << 20
CAP = 16 * MiB          # the buggy buffer cap
FUZZ_MAX = 1 * MiB      # a typical fuzzer input cap (the post: "typically capped at 1 MB")
PROOF_MAX = 64 * MiB    # the post's proof bound
HEADER, RECORD = 8, 4


def decode(length, n_records, fixed=False):
    """Return 'rejected', 'ok' or 'CRASH' for a file of `length` bytes whose
    header claims `n_records` records."""
    buf = length if fixed else min(length, CAP)
    if length < HEADER or n_records < 1:
        return "rejected"
    end = HEADER + RECORD * n_records
    if end > length:
        return "rejected"            # the header claims more than the file holds
    if end > buf:
        return "CRASH"               # out-of-bounds write
    return "ok"


def fuzz(runs, seed=20261030):
    rng = random.Random(seed)
    crashes = valid = 0
    for _ in range(runs):
        length = rng.randint(0, FUZZ_MAX)
        if rng.random() < 0.5 and length >= HEADER + RECORD:
            n = rng.randint(1, (length - HEADER) // RECORD)     # a valid count for this file
        else:
            n = rng.getrandbits(32)                             # whatever the bytes say
        r = decode(length, n)
        valid += r != "rejected"
        crashes += r == "CRASH"
    return crashes, valid


def solve(fixed):
    L, n = z3.Ints("L n")
    buf = L if fixed else z3.If(L < CAP, L, CAP)
    end = HEADER + RECORD * n
    opt = z3.Optimize()
    opt.add(L >= HEADER, L <= PROOF_MAX, n >= 1, end <= L, end > buf)
    opt.minimize(L)
    t0 = time.perf_counter()
    res = opt.check()
    dt = time.perf_counter() - t0
    if res == z3.sat:
        m = opt.model()
        return "sat", m[L].as_long(), m[n].as_long(), dt
    return str(res), None, None, dt


def main():
    print(f"python {sys.version.split()[0]} · z3 {z3.get_version_string()} · {platform.machine()} · "
          f"{time.strftime('%Y-%m-%d %H:%M %Z')}")
    runs = 1_000_000
    t0 = time.perf_counter()
    crashes, valid = fuzz(runs)
    print(f"fuzz    {runs:,} random inputs <= {FUZZ_MAX // MiB} MiB ({valid:,} accepted): "
          f"{crashes} crashes in {time.perf_counter() - t0:.1f} s")

    res, L, n, dt = solve(fixed=False)
    replay = decode(L, n)
    print(f"solver  buggy decoder, every input <= {PROOF_MAX // MiB} MiB: {res}; smallest crashing "
          f"input {L:,} bytes = {L / MiB:.6f} MiB with {n:,} records; replay -> {replay}; {dt:.3f} s")
    assert res == "sat" and replay == "CRASH" and L > CAP

    res2, _, _, dt2 = solve(fixed=True)
    print(f"solver  fixed decoder, every input <= {PROOF_MAX // MiB} MiB: {res2} "
          f"(no crashing input exists); {dt2:.3f} s")
    assert res2 == "unsat"
    print(f"summary fuzz_runs {runs} fuzz_crashes {crashes} crash_mib {L / MiB:.2f} "
          f"fixed_counterexamples 0")


if __name__ == "__main__":
    main()
