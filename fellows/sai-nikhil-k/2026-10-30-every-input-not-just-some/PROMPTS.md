# PROMPTS — Every Input, Not Just Some

**No open generation slots.** Eight Remotion compositions and two plates of the
post's figures (credited), a repo screenshot and Commons photos. No image model,
no paid API.

## B00 — the on-screen typed ask

> Anthropic says Claude can now write formal proofs for real open-source libraries. What does a proof cover that a million tests don't, and what does it still miss? Try the idea on a toy.

## B08 — the handoff the viewer can paste

> Here's a function I wrote. State one property it should satisfy for every input, as one precise sentence. Then list what we'd have to assume about the compiler, CPU and OS for a proof of it to mean anything.

## Evidence commands

```bash
REEL=weekly_updates/2026-10-30-every-input-not-just-some
# 1. the toy: 1,000,000 random tests vs Z3 (any venv with z3-solver)
<venv>/bin/python $REEL/evidence/fuzz_vs_proof.py > $REEL/evidence/fuzz_vs_proof.out
# 2. Theorem's published proof index at a pinned commit
python3 $REEL/evidence/theorem_index.py > $REEL/evidence/theorem_index.out
```
