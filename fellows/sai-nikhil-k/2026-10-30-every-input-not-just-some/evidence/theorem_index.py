#!/usr/bin/env python3
"""theorem_index.py — tally Theorem's published index of OSS-Fuzz proof statements.

theorem-labs/oss-verify-proofs (MIT) keeps machine-generated indexes of every
OSS-Fuzz target it tracks and the status of each formal statement about it.
This counts them at a pinned commit, so the reel's "how far along" numbers are
measured, not quoted. The Anthropic post's 239 entry points / 123 libraries are
what Claude proved; this repo publishes a subset (proofs that needed no patch
and reveal no unpatched bug).

Run:  python3 theorem_index.py
"""
import csv, io, urllib.request

SHA = "f1fdc8dd00f2fec4654f4561fd44110416c7da6f"
BASE = f"https://raw.githubusercontent.com/theorem-labs/oss-verify-proofs/{SHA}/index/"
UA = {"User-Agent": "brutalist-art-evidence/1.0"}


def tsv(name):
    raw = urllib.request.urlopen(urllib.request.Request(BASE + name, headers=UA), timeout=60).read()
    return list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))


def num(r, k):
    return int(r[k]) if r[k].isdigit() else 0


P, H, R = tsv("projects.tsv"), tsv("harnesses.tsv"), tsv("proofs.tsv")
print(f"theorem-labs/oss-verify-proofs @ {SHA[:10]} (index/*.tsv)")
print(f"projects tracked      {len(P):>7,}")
print(f"OSS-Fuzz targets      {sum(num(r, 'oss_fuzz_targets') for r in P):>7,}")
for k in ["statements", "open", "proved", "false", "blocked_by_model"]:
    print(f"statements {k:<11s}{sum(num(r, k) for r in P):>7,}" if k != "statements"
          else f"statements total      {sum(num(r, k) for r in P):>7,}")
print(f"entry points proved   {len({(r['library'], r['entry_point']) for r in R}):>7,}")
print(f"libraries with proofs {len({r['library'] for r in R}):>7,}")
print("proved by kind        " + ", ".join(f"{k} {sum(1 for r in R if r['kind'] == k)}"
                                        for k in sorted({r['kind'] for r in R})))
