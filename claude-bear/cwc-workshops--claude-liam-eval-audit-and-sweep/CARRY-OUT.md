# CARRY-OUT

> Eval-audit-and-sweep audits the eval before it ranks models — and it only
> answers "which model" when more than one model actually made the grid.

Test: if someone repeats only this in a meeting next week, is it still true? Yes —
it compresses the key distinction (order: audit gates sweep; scope: the
answer is bounded by how many models cleared access) without overstating
either half.

**Wrong guess this defeats:** "Hand Claude's eval skill your eval and ask
which model wins, and it runs straight into the model-vs-model sweep." The
carry-out replaces that frame: the skill enforces audit before sweep on any
ambiguous-or-both request, because a sweep over a broken eval produces
misleading numbers (SKILL.md step 2) — and even after the audit clears, the
sweep can only compare models that actually survive the access check
(SKILL.md step 4).
