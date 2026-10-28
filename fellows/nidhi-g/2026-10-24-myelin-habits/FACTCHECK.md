# FACTCHECK — myelin-habits
Trace counts were re-counted from the raw files in `Downloads/myelin/data/historical_trajectories` (tool_calls per assistant message). Design facts are from `Downloads/myelin/docs/DESIGN_SPECIFICATION.md`. Myelin is presented throughout as an initial plan, not results.

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B00 | Myelin is an initial plan for making agents stop re-asking the model routine questions | TRUE (design stage; no code in the folder) | README.md; DESIGN_SPECIFICATION.md §1 |
| B01 | Routine decisions run as plain code; the model is asked only when the code is unsure | TRUE (as the plan) | DESIGN_SPECIFICATION.md §1, §4 |
| B02 | Booking lookups 1,419 (airline: 377 GPT-4o + 1,042 Claude 3.5 Sonnet, 600 conversations); order lookups 1,029 (retail, GPT-4o, 460 conversations); flight searches 538 (141 + 397); user lookups 486 (120 + 366) | TRUE (re-counted) | trajectory files |
| B02 | "Public traces of customer-service agents" | TRUE | sierra-research tau-bench historical trajectories |
| B03 | A customer with six bookings; the agent spends six separate model turns, one per booking | TRUE as a common pattern: airline task 2, 9 of 12 runs made exactly 6 lookups. The docs cite "Episode 2" (task 2 trial 0), which made 3: **docs wrong** | trajectory files |
| B03 | Booking codes shown | ILLUSTRATIVE (not from the traces; on-screen generic) | n/a |
| B04 | IDs, codes and dates follow fixed patterns | TRUE (examples generic; ID/code shapes per EMPIRICAL_FINDINGS §4B) | EMPIRICAL_FINDINGS.md §4 |
| B05 | Myelin wraps frequently used nerve pathways; signals travel faster | TRUE (standard neurobiology; no figure quoted) | general |
| B06 | Plan: mine logs, keep decisions repeating ≥ 50 times, a strong model writes a Python function, sandbox with no network and no model, registry | TRUE (plan) | DESIGN_SPECIFICATION.md §1, §3 |
| B07 | "unsure" hands back to the model; agreement ≥ 98% on non-abstained cases, on later (held-out) sessions | TRUE (plan) | DESIGN_SPECIFICATION.md §1, §5 |
| B07 | Formula: agreement = correct ÷ (total − unsure) ≥ 0.98 | TRUE: matches §5 exactly. Algebra check: denominator excludes abstentions; e.g. 100 decisions, 10 unsure, 89 correct → 89/90 = 0.989 ≥ 0.98 (pass); 87 correct → 0.967 (fail) | DESIGN_SPECIFICATION.md §5 |
| B08 | Baselines: semantic cache (nearest-neighbour lookup on input embeddings; reuses the most similar past input's answer), small classifier, small local model; same 70/30 time split | TRUE (plan) | DESIGN_SPECIFICATION.md §3, §6 |
| B09 | Deliverables: habit-compiler Python package; dashboard mapping compiled habits | TRUE (plan) | DESIGN_SPECIFICATION.md §7, §8 |
| B09 | Only call counts are measured; savings are targets | TRUE: traces have no token or timing fields; docs' 15,000 tokens / 9 s / 0.002 ms / 15,000× / 60–80% / 0.0% are not measured here and are not shown | trajectory files |
| — | Docs: Sonnet retail "460 episodes / 3,410 calls" | **docs wrong** (file has 920 / 7,086); not used on screen | trajectory files |
