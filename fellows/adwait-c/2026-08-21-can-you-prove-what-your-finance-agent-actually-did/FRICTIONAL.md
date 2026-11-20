# Frictional Log — Can You Prove What Your Finance Agent Did

**Week of 2026-08-21** · Adwait Changan · Mycroft track
Topic: the evidence was real but scattered across dozens of files — this week makes it one auditable package.

**What I built this week**
- `bundle.py` — before copying a single file, it hash-validates the whole chain (run ID, validation result, review-request hash, evaluation-case hash, scenario-plan hash, raw + verified data hashes).
- Packages **54 artifacts** with `manifest.json`, `manifest.sha256`, and `REVIEW.md`.
- An independent `verify-bundle` recomputes the hashes to confirm nothing drifted.

**The one idea it teaches**
- "Auditable" means someone else can recompute your evidence from scratch — not that you kept the files.

**Where it pushed back (and what I did)**
- Made the bundle refuse to assemble if any link in the hash chain didn't validate first.

**What I learned**
- Proof is reproducibility: a bundle only counts if an independent verifier can regenerate the same hashes.

_Hours this week: ~20 (across the two videos built this week)._
