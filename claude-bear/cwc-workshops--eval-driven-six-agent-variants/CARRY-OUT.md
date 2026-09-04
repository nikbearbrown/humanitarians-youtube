# CARRY-OUT

> Score every version against the same fixed test and the same pinned
> baseline — a rule that only lives in the prompt doesn't survive a model
> swap.

Test: if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses both halves of the mechanism: the constant
(same test set, same pinned baseline, every round) and the boundary (a
prompt-level rule does not transfer when the change is the model instead
of the prompt).

**Wrong guess this defeats:** "Open the new deck next to the old one — if
it looks cleaner, ship it." The carry-out replaces the glance with the
actual mechanism: a two-layer eval (deterministic code checks, then an
LLM judge on the rendered result) run on the same five tasks every round,
scored against one pinned baseline so drift never disguises itself as
progress — and a boundary case (round four swaps the model, not the
prompt) that a glance-based comparison could never surface.
