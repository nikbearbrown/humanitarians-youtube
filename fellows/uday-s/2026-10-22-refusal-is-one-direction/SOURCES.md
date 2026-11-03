# SOURCES — Refusal Is One Direction

Three sources, each read directly. No aggregator, forum post, wiki or blog
sourced any figure.

| On screen | Beat | Source |
|---|---|---|
| the two corrections (direction, not neuron; behaviour, not knowledge) | B01 | derived from the source paper's own description of the intervention |
| 13 open chat models, up to 72B | B03 | arXiv 2406.11717, abstract |
| one-dimensional subspace, one direction per model | B03 | same |
| erase it → stops refusing harmful | B03 | same |
| add it → refuses harmless | B03 | same |
| "underscore the brittleness of current safety fine-tuning methods" | B04 | same, quoted and attributed |
| geometrically distinct directions per refusal category | B05 | arXiv 2602.02132, abstract |
| nearly identical trade-offs; affects HOW not WHETHER | B05 | same |
| linear interventions collapse the structure | B05 | same |
| "minimal effect on other capabilities", with no figure | B06 | arXiv 2406.11717, abstract |
| trigger fire rate up to 100%; clean accuracy 99–100% | B07 | Cloud Security Alliance research note, 2026-10-21 |
| the scope panel: controlled experiment, not a hub survey, not abliteration | B07 | the same note, which states this itself |

## Reference links

- Arditi et al., NeurIPS 2024 — https://arxiv.org/abs/2406.11717
- NeurIPS 2024 poster listing — https://neurips.cc/virtual/2024/poster/93566
- Joad et al., EMNLP 2026 — https://arxiv.org/abs/2602.02132
- CSA research note (2026-10-21) — https://labs.cloudsecurityalliance.org/research/csa-research-note-abliterated-model-backdoors-20261021-csa-s/

## What was deliberately not sought

**No operational material was looked up.** No implementation, no notebook, no
model card for an edited model, and no model hub listing was opened. The reel
explains a finding; it does not reproduce a method, and the research for it was
scoped the same way.

## Why the security note is shown with its own limits attached

The note is the newest and least replicated of the three sources — a single
vendor's self-published experiment, 50-prompt test sets, no independent
replication found — and it is also the one whose headline travels furthest. So
B07 puts the scope panel on screen BEFORE the numbers, and the caveats on the
citation strip, rather than leaving either to this file.

Two things it does NOT support, and which the reel therefore does not say:

- that published abliterated models have been found to contain backdoors;
- that any particular proportion of edited models on hubs is compromised.

What it does support is the trust argument: a modified open-weight model can
carry a trigger that clean benchmarks do not reveal, and an abliterated model is
a modified open-weight model.

## A naming claim that was dropped

Several secondary pages attribute the coining of "abliteration" to a specific
person and its popularisation to another. Neither could be confirmed from a
primary source, so no attribution appears on screen.
